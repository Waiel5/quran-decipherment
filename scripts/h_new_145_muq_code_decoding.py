#!/usr/bin/env python3
"""H-NEW-145 — Muqaṭṭāʿat letter-sets as CODE: attempted decoding.

Pre-registered tests (Bonferroni k=4, α_bon=0.0125, family=h-new-145-muq-code):

  Cell A — cardinality-mod-3 vs verse-count-mod-3 match rate. PASS if
           match rate > 0.55 with hypergeometric-like 2-sided p < 0.0125.
  Cell B — 4 per-letter binary-feature tests:
           (B1) M ↔ surah length Spearman ρ > 0 at α_within=0.003125
           (B2) ḤĀ ↔ Medinan-bias Spearman ρ vs chronology
           (B3) SAD ↔ patience-theme hypergeometric enrichment (patience root ṣbr)
           (B4) Q ↔ eschatology hypergeometric enrichment (root qwm/qyām)
           Cell PASS if ≥ 2/4 pass at α_within.
  Cell C — RF reverse-decoding on 29×14 binary letter-presence matrix.
           Targets: (C1) length-bin, (C2) chronology-bin, (C3) name-class.
           LOOCV accuracy vs permutation null. PASS if any has p < 0.0125.
  Cell D — Classical singleton-interpretations top-5-of-29 rank test:
           (D1) ص (Q 38) ↔ ṣbr root density
           (D2) ق (Q 50) ↔ qwm ∨ qrʾ root density
           (D3) ن (Q 68) ↔ whale-narrative (root Hwt or ywns)
           PASS if 3/3 (exact binomial p≈0.005).

MW-5 positive control: shuffled letter-set null; all cells should fail.

Seed 20260417. Deterministic.
"""
import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    from sklearn.ensemble import RandomForestClassifier
    HAS_SKLEARN = True
except ImportError:
    HAS_SKLEARN = False

try:
    from scipy.stats import spearmanr, hypergeom, binom_test
except ImportError:
    # fallback for older scipy
    from scipy.stats import spearmanr, hypergeom
    try:
        from scipy.stats import binomtest
        def binom_test(k, n, p):
            return binomtest(k, n, p).pvalue
    except ImportError:
        # manual binomial exact
        def binom_test(k, n, p):
            from math import comb
            # 2-sided for k>=n*p: sum P(X>=k)
            if k >= n*p:
                return 2.0 * sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(k, n+1))
            else:
                return 2.0 * sum(comb(n,i)*p**i*(1-p)**(n-i) for i in range(0, k+1))

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERMS = 1000

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
CHRONO_CSV = ROOT / 'data/revelation-order.csv'
NAMECLASS_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-49.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-145-muq-code-decoding-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-145.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

random.seed(SEED)

# ---------------------------------------------------------------------------
# 1. Canonical muq letter-sets (14 sets, 29 surahs, 14 distinct letters)
# ---------------------------------------------------------------------------
MUQ = {
    2:  ('ALM',    ['A','L','M']),
    3:  ('ALM',    ['A','L','M']),
    7:  ('ALMS',   ['A','L','M','SAD']),
    10: ('ALR',    ['A','L','R']),
    11: ('ALR',    ['A','L','R']),
    12: ('ALR',    ['A','L','R']),
    13: ('ALMR',   ['A','L','M','R']),
    14: ('ALR',    ['A','L','R']),
    15: ('ALR',    ['A','L','R']),
    19: ('KHYAS',  ['K','HA','Y','AYN','SAD']),
    20: ('TAH',    ['TA','HA']),
    26: ('TASM',   ['TA','SIN','M']),
    27: ('TAS',    ['TA','SIN']),
    28: ('TASM',   ['TA','SIN','M']),
    29: ('ALM',    ['A','L','M']),
    30: ('ALM',    ['A','L','M']),
    31: ('ALM',    ['A','L','M']),
    32: ('ALM',    ['A','L','M']),
    36: ('YS',     ['Y','SIN']),
    38: ('SAD',    ['SAD']),
    40: ('HM',     ['HHA','M']),
    41: ('HM',     ['HHA','M']),
    42: ('HMASQ',  ['HHA','M','AYN','SIN','Q']),
    43: ('HM',     ['HHA','M']),
    44: ('HM',     ['HHA','M']),
    45: ('HM',     ['HHA','M']),
    46: ('HM',     ['HHA','M']),
    50: ('Q',      ['Q']),
    68: ('N',      ['N']),
}
ALL_LETTERS = sorted(set(l for _, letters in MUQ.values() for l in letters))
assert len(ALL_LETTERS) == 14, f"expected 14 muq letters, got {len(ALL_LETTERS)}"
MUQ_SURAHS = sorted(MUQ.keys())
assert len(MUQ_SURAHS) == 29

print(f"muq letters ({len(ALL_LETTERS)}): {ALL_LETTERS}", file=sys.stderr)
print(f"muq surahs ({len(MUQ_SURAHS)}): {MUQ_SURAHS}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Quran metadata
# ---------------------------------------------------------------------------
quran = json.loads(QURAN_JSON.read_text())
surah_nverses = {s['id']: len(s['verses']) for s in quran}

# Chronology
chronology = {}  # mushaf_sid -> noldeke_order
noldeke_phase = {}  # mushaf_sid -> phase string
import csv as csvlib
with open(CHRONO_CSV, encoding='utf-8') as f:
    rdr = csvlib.DictReader(f)
    for row in rdr:
        msid = int(row['mushaf_order'])
        chronology[msid] = int(row['noldeke_order'])
        noldeke_phase[msid] = row['noldeke_phase']

# Name-class (9 classes from H-NEW-49)
nameclass_data = json.loads(NAMECLASS_JSON.read_text())
surah_class_assign = nameclass_data['surah_class_assignments']
NAME_CLASSES = nameclass_data['classes']
surah_nameclass = {}
for sid_str, rec in surah_class_assign.items():
    surah_nameclass[int(sid_str)] = rec['class']

# Length-bin (tertiles)
lengths = sorted([surah_nverses[s] for s in range(1, 115)])
q33 = lengths[len(lengths) // 3]
q67 = lengths[2 * len(lengths) // 3]
def length_bin(nverses):
    if nverses <= q33: return 'short'
    if nverses <= q67: return 'mid'
    return 'long'

# Chronology-bin (4 Nöldeke phases)
# Convert noldeke_phase strings to 4 canonical bins
PHASE_BINS = ['Early Meccan', 'Middle Meccan', 'Late Meccan', 'Medinan']

# ---------------------------------------------------------------------------
# 3. QAC root tokens for Cell B and Cell D cognate density tests
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots = defaultdict(list)
per_surah_verse_roots = defaultdict(lambda: defaultdict(list))  # sid -> vid -> [roots]
with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        vid = int(m.group(2))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_surah_roots[sid].append(root)
        per_surah_verse_roots[sid][vid].append(root)

def root_count_in_surah(sid, target_roots):
    """Count occurrences of any root in target_roots list within surah sid."""
    roots = per_surah_roots.get(sid, [])
    return sum(1 for r in roots if r in target_roots)

def root_density_per_verse(sid, target_roots):
    """Count of target roots / number of verses in surah."""
    count = root_count_in_surah(sid, target_roots)
    return count / surah_nverses[sid]

# Root identifiers in QAC Buckwalter transliteration
# Note: QAC uses Buckwalter. Let me verify the root forms:
# ṣbr (patience) = Sbr
# qwm (standing/resurrection) = qwm
# qrʾ (recite/read; Qurʾan) = qrA (hamza as A)
# ywns (Jonah) = ywns (or ynos)
# Hwt (whale) = Hwt
# Let me check the QAC actual forms:

# Sample check to confirm roots:
sample_roots = Counter()
for s in range(1, 115):
    for r in per_surah_roots[s]:
        sample_roots[r] += 1
print(f"'Sbr' (patience) corpus count: {sample_roots.get('Sbr', 0)}", file=sys.stderr)
print(f"'qwm' (standing) corpus count: {sample_roots.get('qwm', 0)}", file=sys.stderr)
print(f"'qrA' (recite) corpus count: {sample_roots.get('qrA', 0)}", file=sys.stderr)
print(f"'Hwt' (whale) corpus count: {sample_roots.get('Hwt', 0)}", file=sys.stderr)
print(f"'ynos' (Jonah) corpus count: {sample_roots.get('ynos', 0)}", file=sys.stderr)
print(f"'nwn' (nun) corpus count: {sample_roots.get('nwn', 0)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Helper: letter-presence binary matrix
# ---------------------------------------------------------------------------
def letter_presence_matrix(muq_dict):
    """Return dict: surah_id -> dict letter -> 0/1"""
    mat = {}
    for sid, (_, letters) in muq_dict.items():
        row = {l: 0 for l in ALL_LETTERS}
        for l in letters:
            row[l] = 1
        mat[sid] = row
    return mat

# ---------------------------------------------------------------------------
# 5. CELL A — cardinality-mod-3 vs verse-count-mod-3 match rate
# ---------------------------------------------------------------------------
def cell_A(muq_dict):
    matches = 0
    total = 0
    details = []
    for sid in sorted(muq_dict.keys()):
        _, letters = muq_dict[sid]
        card_mod = len(letters) % 3
        nv_mod = surah_nverses[sid] % 3
        match = (card_mod == nv_mod)
        matches += int(match)
        total += 1
        details.append({'sid': sid, 'card': len(letters), 'nverses': surah_nverses[sid],
                        'card_mod3': card_mod, 'nv_mod3': nv_mod, 'match': match})
    match_rate = matches / total
    # Null: for each surah, verse-count mod-3 is ~uniform over {0,1,2}; match prob ~1/3
    # Under independent binomial(29, 1/3), 1-sided upper-tail test:
    p_one_sided = sum(math.comb(total, k) * (1/3)**k * (2/3)**(total-k)
                      for k in range(matches, total + 1))
    return {
        'matches': matches,
        'total': total,
        'match_rate': match_rate,
        'threshold_match_rate': 0.55,
        'p_one_sided_binomial_p_one_third': p_one_sided,
        'alpha_bon': 0.0125,
        'pass': (match_rate > 0.55) and (p_one_sided < 0.0125),
        'details': details,
    }

print("\n[Cell A] cardinality-mod-3 vs verse-count-mod-3...", file=sys.stderr)
A_result = cell_A(MUQ)
print(f"  matches: {A_result['matches']}/{A_result['total']} = {A_result['match_rate']:.3f}", file=sys.stderr)
print(f"  1-sided p (vs 1/3 null) = {A_result['p_one_sided_binomial_p_one_third']:.6f}", file=sys.stderr)
print(f"  Cell A {'PASS' if A_result['pass'] else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. CELL B — per-letter binary-feature hypothesis tests
# ---------------------------------------------------------------------------
def cell_B(muq_dict):
    mat = letter_presence_matrix(muq_dict)
    alpha_within = 0.0125 / 4  # 0.003125
    results = {}

    # B1: M ↔ surah length (Spearman)
    m_presence = [mat[s]['M'] for s in MUQ_SURAHS]
    lengths_muq = [surah_nverses[s] for s in MUQ_SURAHS]
    rho, p = spearmanr(m_presence, lengths_muq)
    # 1-sided for ρ > 0
    p_one_sided = p / 2 if rho > 0 else 1 - p / 2
    results['B1_M_vs_length'] = {'rho': rho, 'p_one_sided': p_one_sided,
                                  'alpha_within': alpha_within,
                                  'pass': rho > 0 and p_one_sided < alpha_within}

    # B2: ḤĀ presence ↔ Medinan-bias (Nöldeke chronology; larger = later)
    hha_presence = [mat[s]['HHA'] for s in MUQ_SURAHS]
    chrono_muq = [chronology[s] for s in MUQ_SURAHS]
    rho, p = spearmanr(hha_presence, chrono_muq)
    p_one_sided = p / 2 if rho > 0 else 1 - p / 2
    results['B2_HHA_vs_chronology'] = {'rho': rho, 'p_one_sided': p_one_sided,
                                        'alpha_within': alpha_within,
                                        'pass': rho > 0 and p_one_sided < alpha_within}

    # B3: SAD ↔ patience-theme (hypergeometric enrichment of Sbr root)
    # Classify each muq surah by: is it in top-third for Sbr-density?
    sbr_densities = {s: root_density_per_verse(s, ['Sbr']) for s in MUQ_SURAHS}
    # Top-third threshold:
    sorted_sbr = sorted(sbr_densities.values(), reverse=True)
    top_third_threshold = sorted_sbr[len(sorted_sbr) // 3]
    top_third_surahs = [s for s, d in sbr_densities.items() if d >= top_third_threshold]
    sad_surahs = [s for s in MUQ_SURAHS if mat[s]['SAD'] == 1]
    overlap = len(set(sad_surahs) & set(top_third_surahs))
    # hypergeom: population=29, success_in_pop=top_third, sample_size=|sad|
    M_pop = len(MUQ_SURAHS)
    N_success = len(top_third_surahs)
    n_sample = len(sad_surahs)
    k_overlap = overlap
    # 1-sided upper-tail p = P(X >= k)
    p_hg = 1 - hypergeom.cdf(k_overlap - 1, M_pop, N_success, n_sample)
    results['B3_SAD_vs_sbr_patience'] = {
        'sad_surahs': sad_surahs,
        'top_third_sbr_surahs': sorted(top_third_surahs),
        'overlap': overlap,
        'p_hypergeom_one_sided': p_hg,
        'alpha_within': alpha_within,
        'pass': p_hg < alpha_within
    }

    # B4: Q presence ↔ eschatology (qwm OR qrA root density)
    escha_densities = {s: root_density_per_verse(s, ['qwm', 'qrA']) for s in MUQ_SURAHS}
    sorted_escha = sorted(escha_densities.values(), reverse=True)
    top_third_escha = sorted_escha[len(sorted_escha) // 3]
    top_third_e = [s for s, d in escha_densities.items() if d >= top_third_escha]
    q_surahs = [s for s in MUQ_SURAHS if mat[s]['Q'] == 1]
    overlap_e = len(set(q_surahs) & set(top_third_e))
    p_hg_q = 1 - hypergeom.cdf(overlap_e - 1, M_pop, len(top_third_e), len(q_surahs))
    results['B4_Q_vs_qwm_qrA'] = {
        'q_surahs': q_surahs,
        'top_third_escha_surahs': sorted(top_third_e),
        'overlap': overlap_e,
        'p_hypergeom_one_sided': p_hg_q,
        'alpha_within': alpha_within,
        'pass': p_hg_q < alpha_within
    }

    n_pass = sum(1 for k, v in results.items() if v.get('pass', False))
    cell_pass = n_pass >= 2
    return {'sub_tests': results, 'n_pass_of_4': n_pass, 'cell_B_pass': cell_pass,
            'alpha_within': alpha_within}

print("\n[Cell B] per-letter binary-feature tests...", file=sys.stderr)
B_result = cell_B(MUQ)
for name, r in B_result['sub_tests'].items():
    print(f"  {name}: {r}", file=sys.stderr)
print(f"  Cell B n_pass: {B_result['n_pass_of_4']}/4 → "
      f"{'PASS' if B_result['cell_B_pass'] else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. CELL C — RF reverse-decoding (letter-presence → metadata targets)
# ---------------------------------------------------------------------------
def cell_C(muq_dict, n_perms=N_PERMS):
    mat = letter_presence_matrix(muq_dict)
    X = [[mat[s][l] for l in ALL_LETTERS] for s in MUQ_SURAHS]

    # Targets
    targets = {
        'C1_length_bin': [length_bin(surah_nverses[s]) for s in MUQ_SURAHS],
        'C2_chronology_phase': [noldeke_phase[s] for s in MUQ_SURAHS],
        'C3_name_class': [surah_nameclass.get(s, 'OTHER') for s in MUQ_SURAHS],
    }

    results = {}
    for tname, y in targets.items():
        # LOOCV with RF
        y_unique = sorted(set(y))
        correct = 0
        for i in range(len(X)):
            X_train = [X[j] for j in range(len(X)) if j != i]
            y_train = [y[j] for j in range(len(X)) if j != i]
            if len(set(y_train)) == 0:
                continue
            rf = RandomForestClassifier(n_estimators=100, random_state=SEED, n_jobs=1)
            rf.fit(X_train, y_train)
            pred = rf.predict([X[i]])[0]
            if pred == y[i]:
                correct += 1
        acc = correct / len(X)
        # Majority-class baseline
        mode_class = Counter(y).most_common(1)[0][0]
        majority_acc = sum(1 for yy in y if yy == mode_class) / len(y)

        # Permutation null
        rng = random.Random(SEED + hash(tname) % 1000)
        null_accs = []
        for perm_idx in range(n_perms):
            y_perm = y[:]
            rng.shuffle(y_perm)
            correct_p = 0
            for i in range(len(X)):
                X_train = [X[j] for j in range(len(X)) if j != i]
                y_train = [y_perm[j] for j in range(len(X)) if j != i]
                if len(set(y_train)) == 0:
                    continue
                rf = RandomForestClassifier(n_estimators=30, random_state=SEED + perm_idx, n_jobs=1)
                rf.fit(X_train, y_train)
                pred = rf.predict([X[i]])[0]
                if pred == y_perm[i]:
                    correct_p += 1
            null_accs.append(correct_p / len(X))
        # 1-sided upper-tail p
        p_perm = (sum(1 for a in null_accs if a >= acc) + 1) / (n_perms + 1)
        results[tname] = {
            'loocv_accuracy': acc,
            'majority_baseline': majority_acc,
            'uniform_chance_baseline': 1.0 / len(y_unique),
            'n_classes': len(y_unique),
            'permutation_null_mean': statistics.mean(null_accs),
            'permutation_null_max': max(null_accs),
            'p_permutation_one_sided': p_perm,
            'alpha_bon': 0.0125,
            'pass': p_perm < 0.0125,
        }

    cell_pass = any(r['pass'] for r in results.values())
    return {'targets': results, 'cell_C_pass': cell_pass}

print("\n[Cell C] RF reverse-decoding (this is the slow cell; ~3 min)...", file=sys.stderr)
# Use fewer perms for the main run to stay under time budget
C_result = cell_C(MUQ, n_perms=200)
for tname, r in C_result['targets'].items():
    print(f"  {tname}: acc={r['loocv_accuracy']:.3f} majority={r['majority_baseline']:.3f} "
          f"null_mean={r['permutation_null_mean']:.3f} p={r['p_permutation_one_sided']:.4f} "
          f"{'PASS' if r['pass'] else 'FAIL'}",
          file=sys.stderr)
print(f"  Cell C {'PASS' if C_result['cell_C_pass'] else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. CELL D — classical singleton-interpretation top-5 rank test
# ---------------------------------------------------------------------------
def cell_D():
    # Cognate root assignments:
    cognates = {
        'D1_SAD_Q38_patience_sbr': (38, ['Sbr']),
        'D2_Q_Q50_resurrection_qwm_qrA': (50, ['qwm', 'qrA']),
        'D3_N_Q68_whale_narrative': (68, ['Hwt', 'ynos']),  # whale, Jonah
    }
    results = {}
    all_29_densities = {}
    for tname, (target_sid, target_roots) in cognates.items():
        densities_by_muq = {s: root_density_per_verse(s, target_roots) for s in MUQ_SURAHS}
        # rank: where does target_sid sit among 29 muq surahs?
        sorted_surahs = sorted(densities_by_muq.items(), key=lambda x: -x[1])  # descending density
        rank_of_target = next(i + 1 for i, (s, d) in enumerate(sorted_surahs) if s == target_sid)
        top_5 = [(s, d) for s, d in sorted_surahs[:5]]
        all_29_densities[tname] = {
            'target_sid': target_sid,
            'target_roots': target_roots,
            'target_density': densities_by_muq[target_sid],
            'rank_of_target_in_29_muq': rank_of_target,
            'in_top5': rank_of_target <= 5,
            'top5_surahs_by_density': top_5,
        }
        results[tname] = all_29_densities[tname]

    n_in_top5 = sum(1 for r in results.values() if r['in_top5'])
    # Exact binomial p under null = P(X >= n_in_top5) for n=3, p=5/29
    p_null = 5 / 29
    # 1-sided upper tail
    p_upper = sum(math.comb(3, k) * p_null**k * (1-p_null)**(3-k) for k in range(n_in_top5, 4))
    cell_pass = n_in_top5 == 3 and p_upper < 0.0125
    return {
        'cognates': results,
        'n_in_top5': n_in_top5,
        'p_null_per_cell': p_null,
        'p_binomial_upper_tail': p_upper,
        'cell_D_pass': cell_pass,
    }

print("\n[Cell D] classical singleton-interpretation top-5 test...", file=sys.stderr)
D_result = cell_D()
for cname, r in D_result['cognates'].items():
    print(f"  {cname}: target Q{r['target_sid']} rank {r['rank_of_target_in_29_muq']}/29 "
          f"density={r['target_density']:.4f} in_top5={r['in_top5']}", file=sys.stderr)
print(f"  n_in_top5: {D_result['n_in_top5']}/3; binomial p={D_result['p_binomial_upper_tail']:.4f} → "
      f"{'PASS' if D_result['cell_D_pass'] else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. MW-5 positive control — shuffled surah→letter-set assignment
# ---------------------------------------------------------------------------
print("\n[MW-5] shuffled-null positive control...", file=sys.stderr)
rng_mw5 = random.Random(SEED + 999)
shuffled_letter_sets = [MUQ[s] for s in MUQ_SURAHS]
rng_mw5.shuffle(shuffled_letter_sets)
MUQ_shuf = {MUQ_SURAHS[i]: shuffled_letter_sets[i] for i in range(len(MUQ_SURAHS))}

A_null = cell_A(MUQ_shuf)
B_null = cell_B(MUQ_shuf)
print(f"  Cell A (shuffled): pass={A_null['pass']} (match_rate={A_null['match_rate']:.3f})", file=sys.stderr)
print(f"  Cell B (shuffled): n_pass={B_null['n_pass_of_4']}/4 cell_pass={B_null['cell_B_pass']}", file=sys.stderr)
# Cell C is expensive; run with fewer perms for MW-5
C_null = cell_C(MUQ_shuf, n_perms=100)
print(f"  Cell C (shuffled): cell_pass={C_null['cell_C_pass']}", file=sys.stderr)

mw5_pass = (not A_null['pass']) and (not B_null['cell_B_pass']) and (not C_null['cell_C_pass'])
print(f"  MW-5 positive control (shuffled null): "
      f"{'PASS (null correctly fails cells)' if mw5_pass else 'FAIL (null passes some cell — instrument broken)'}",
      file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. Final verdict
# ---------------------------------------------------------------------------
cells_passed = sum([A_result['pass'], B_result['cell_B_pass'],
                    C_result['cell_C_pass'], D_result['cell_D_pass']])

if not mw5_pass:
    final_verdict = "INSTRUMENT-BROKEN — shuffled null spuriously passes one or more cells"
elif cells_passed >= 3:
    final_verdict = "STRONG-DECODING — muq letter-sets carry decodable metadata"
elif cells_passed == 2:
    final_verdict = "PARTIAL-DECODING — some metadata encoded, not all"
elif cells_passed == 1:
    final_verdict = "WEAK-SIGNAL — isolated correlation, likely noise"
else:
    final_verdict = "NULL — letter-sets are NOT a decodable metadata code"

print("\n" + "=" * 70, file=sys.stderr)
print(f"Cell A: {'PASS' if A_result['pass'] else 'FAIL'} "
      f"(match_rate={A_result['match_rate']:.3f}, p={A_result['p_one_sided_binomial_p_one_third']:.4f})",
      file=sys.stderr)
print(f"Cell B: {'PASS' if B_result['cell_B_pass'] else 'FAIL'} "
      f"({B_result['n_pass_of_4']}/4 sub-tests)", file=sys.stderr)
print(f"Cell C: {'PASS' if C_result['cell_C_pass'] else 'FAIL'}", file=sys.stderr)
print(f"Cell D: {'PASS' if D_result['cell_D_pass'] else 'FAIL'} "
      f"({D_result['n_in_top5']}/3 cognates in top-5)", file=sys.stderr)
print(f"MW-5: {'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)
print(f"FINAL: {final_verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 11. Write JSON
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-145',
    'title': 'Muqaṭṭāʿat letter-sets as CODE: attempted decoding',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'bonferroni': {'k': 4, 'alpha_bon': 0.0125, 'family': 'h-new-145-muq-code'},
    'canonical_muq_surahs': MUQ_SURAHS,
    'distinct_muq_letters': ALL_LETTERS,
    'cell_A': A_result,
    'cell_B': B_result,
    'cell_C': C_result,
    'cell_D': D_result,
    'mw5_shuffled_null': {
        'A': A_null,
        'B': B_null,
        'C': C_null,
        'all_null_cells_fail': mw5_pass,
    },
    'cells_passed_of_4': cells_passed,
    'final_verdict': final_verdict,
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
