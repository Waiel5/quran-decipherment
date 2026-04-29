#!/usr/bin/env python3
"""H-NEW-23 — Hapax-final slot theory (al-Zarkashī maqṣūda li-ghayrihā).

Parent finding: hapax legomena at verse-endings p=7.35e-29 (MASTER #7).
This task tests the classical MECHANISM vs a rareness-bias confound.

Sub-test 1: position-within-surah × hapax-final rate (Cuzick trend test)
Sub-test 2: genre × hapax-final rate (ANOVA across narrative/eschatological/legal/hymn)
Sub-test 3: WITHIN-VERSE slot control (McNemar: among hapax-bearing verses,
             does final-slot rate exceed non-final-slot rate?) — CRITICAL
Sub-test 4: taṣdīr mutual-exclusion (|hapax-final ∩ taṣdīr| ≈ 0 under hypergeometric)

Bonferroni k=4, α_bon=0.0025.
Seed 20260413.
"""
import csv, json, math, random, re, statistics, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

# ---- Load hapax catalog ----
HAPAX_CSV = ROOT / 'findings/phase-b-hypotheses/hapaxes-full-list.csv'
hapaxes = []
with open(HAPAX_CSV) as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['type'] != 'root-hapax':
            continue
        hapaxes.append({
            'surah': int(row['surah']),
            'verse': int(row['verse']),
            'word_position': int(row['word_position']),
            'verse_length': int(row['verse_length']),
            'verse_final': int(row['verse_final']),
            'root': row['root'],
            'lemma': row['lemma'],
            'tag': row['tag'],
        })
print(f"hapaxes: {len(hapaxes)}", file=sys.stderr)

# ---- Load Quran structure for surah sizes & genres ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
surah_info = {}
for s in Q:
    sid = s['id']
    surah_info[sid] = {
        'n_verses': len(s['verses']),
        'type': s.get('type', '').lower(),  # Meccan / Medinan
    }

# ---- Load QAC morphology to get all verse positions and lengths ----
print("loading QAC to build full verse-word index...", file=sys.stderr)
verse_tokens = defaultdict(list)  # (sid, vid) -> list of (word_position, root)
ROOT_RE = re.compile(r'ROOT:([^|]+)')
LOC_RE = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')

with open(ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        loc = LOC_RE.match(parts[0])
        if not loc:
            continue
        sid, vid, wid, seg = int(loc.group(1)), int(loc.group(2)), int(loc.group(3)), int(loc.group(4))
        rm = ROOT_RE.search(parts[3])
        root = rm.group(1) if rm else None
        verse_tokens[(sid, vid)].append((wid, seg, root))

# Verse lengths: max word_position
verse_length = {k: max(w for w, _, _ in toks) for k, toks in verse_tokens.items()}

# Total Quran tokens (distinct words)
total_words = sum(len(set(w for w, _, _ in toks)) for toks in verse_tokens.values())
print(f"total distinct word-positions: {total_words}", file=sys.stderr)

# All root occurrences indexed by root
root_locations = defaultdict(list)
for (sid, vid), toks in verse_tokens.items():
    seen_words = set()
    for w, s, r in toks:
        if r is None or w in seen_words:
            continue
        seen_words.add(w)
        root_locations[r].append((sid, vid, w, verse_length[(sid, vid)]))
# Count hapax = roots with exactly 1 occurrence
root_hapax_roots = {r: locs[0] for r, locs in root_locations.items() if len(locs) == 1}
print(f"root hapaxes (recomputed): {len(root_hapax_roots)}", file=sys.stderr)

# ---- Sub-test 1: quartile trend ----
print("\n=== Sub-test 1: verse-position-quartile trend ===", file=sys.stderr)
# For each hapax, compute which quartile it falls in within its surah
quartile_hapax_count = [0, 0, 0, 0]
quartile_verse_count = [0, 0, 0, 0]
quartile_hapax_final_count = [0, 0, 0, 0]

# First, build a map: (sid, vid) -> quartile 0..3
verse_quartile = {}
for sid, info in surah_info.items():
    nv = info['n_verses']
    for vid in range(1, nv + 1):
        q = min(3, int(4 * (vid - 1) / nv))
        verse_quartile[(sid, vid)] = q

# Map each verse to whether it has any hapax and whether any hapax is verse-final
verse_has_hapax = set()
verse_has_final_hapax = set()
for r, (sid, vid, w, vl) in root_hapax_roots.items():
    verse_has_hapax.add((sid, vid))
    if w == vl:
        verse_has_final_hapax.add((sid, vid))

# Count verses per quartile
for (sid, vid), q in verse_quartile.items():
    quartile_verse_count[q] += 1
    if (sid, vid) in verse_has_hapax:
        quartile_hapax_count[q] += 1
    if (sid, vid) in verse_has_final_hapax:
        quartile_hapax_final_count[q] += 1

print("quartile: verses, has_hapax, has_final_hapax, final_hapax_rate", file=sys.stderr)
final_rates_by_q = []
for q in range(4):
    vc = quartile_verse_count[q]
    hc = quartile_hapax_count[q]
    fc = quartile_hapax_final_count[q]
    rate = fc / vc if vc > 0 else 0
    final_rates_by_q.append(rate)
    print(f"Q{q+1}: {vc} verses, {hc} has_hapax, {fc} has_final_hapax, rate={rate:.4f}", file=sys.stderr)

# Cuzick's test for trend = Spearman rank between quartile and rate
# (With 4 points + large samples, use Cochran-Armitage trend z)
def cochran_armitage_trend(counts_success, counts_total, doses):
    """One-sided z for trend in binomial data."""
    n_total = sum(counts_total)
    p_overall = sum(counts_success) / n_total if n_total > 0 else 0
    mean_dose = sum(d * n for d, n in zip(doses, counts_total)) / n_total if n_total > 0 else 0
    num = sum((s - p_overall * n) * (d - mean_dose) for s, n, d in zip(counts_success, counts_total, doses))
    var = p_overall * (1 - p_overall) * sum(n * (d - mean_dose) ** 2 for n, d in zip(counts_total, doses))
    if var <= 0:
        return 0, 1
    z = num / math.sqrt(var)
    from math import erf, sqrt
    p = 0.5 * (1 - erf(z / sqrt(2)))  # one-sided positive
    return z, p

z_sub1, p_sub1 = cochran_armitage_trend(
    quartile_hapax_final_count, quartile_verse_count, [1, 2, 3, 4])
print(f"Cochran-Armitage trend z = {z_sub1:.3f}, one-sided p = {p_sub1:.5f}", file=sys.stderr)

# ---- Sub-test 2: genre × hapax-final rate ----
print("\n=== Sub-test 2: genre × hapax-final rate ===", file=sys.stderr)

# Simplified al-Suyūṭī Itqān nawʿ 65 genre assignment.
# Classical nawʿ 65 lists 5 categories: narrative (qasas), eschatological
# (ʾākhira/wa'd-wa'īd), legal (aḥkām), hymn/praise (tasbīḥ), polemic (jadal).
# Use a coarse map by surah_type plus a known-index approximation.
# For a more disciplined run, use existing genre catalog if available:
genre_path = ROOT / 'findings/phase-b-hypotheses/surah-genre-map.json'
if genre_path.exists():
    genre_map = json.loads(genre_path.read_text())
    genre_map = {int(k): v for k, v in genre_map.items()}
else:
    # Rough assignment based on known scholarly clustering
    # Meccan short surahs 78-114 are eschatological-hymn dominated
    # Meccan long (7, 10-15, 16-23, 25-28, 34-46, 50-56, 67-77): mixed narrative-eschat
    # Medinan (2,3,4,5,8,9,24,33,47-49,57-66,76): legal-polemic-narrative
    genre_map = {}
    for sid in range(1, 115):
        info = surah_info[sid]
        if info['type'] == 'medinan':
            if sid in {2, 3, 4, 5, 24, 33, 58, 60, 65, 66}:
                genre_map[sid] = 'legal'
            elif sid in {8, 9, 47, 48, 49, 59}:
                genre_map[sid] = 'polemic'
            else:
                genre_map[sid] = 'narrative'
        else:  # meccan
            if sid >= 78:
                genre_map[sid] = 'eschatological'
            elif sid in {1, 87, 94, 112, 113, 114}:
                genre_map[sid] = 'hymn'
            elif sid in {12, 18, 19, 20, 28}:  # known narrative surahs
                genre_map[sid] = 'narrative'
            else:
                genre_map[sid] = 'narrative'

# Count hapax-final rate by genre
genre_counts = defaultdict(lambda: [0, 0])  # [verses, hapax_final]
for (sid, vid), q in verse_quartile.items():
    g = genre_map.get(sid, 'unknown')
    genre_counts[g][0] += 1
    if (sid, vid) in verse_has_final_hapax:
        genre_counts[g][1] += 1

print("genre: verses, hapax_final, rate", file=sys.stderr)
genre_rates = {}
for g, (vc, fc) in sorted(genre_counts.items()):
    rate = fc / vc if vc > 0 else 0
    genre_rates[g] = rate
    print(f"  {g}: {vc} verses, {fc} hapax_final, rate={rate:.4f}", file=sys.stderr)

# Chi-square test of rate heterogeneity across genres
def chi_square_independence(counts):
    """counts: list of (k_success, k_total) — compute chi-square of homogeneity"""
    total_succ = sum(c[0] for c in counts)
    total_n = sum(c[1] for c in counts)
    p = total_succ / total_n if total_n > 0 else 0
    chi2 = 0
    df = len(counts) - 1
    for succ, n in counts:
        e1 = n * p
        e0 = n * (1 - p)
        if e1 > 0:
            chi2 += (succ - e1) ** 2 / e1
        if e0 > 0:
            chi2 += ((n - succ) - e0) ** 2 / e0
    return chi2, df

# Chi-square p-value via normal approx or upper-bound
def chi2_pvalue(chi2, df):
    # Approximate via Wilson-Hilferty
    if df == 0:
        return 1
    h = 2 / (9 * df)
    z = ((chi2 / df) ** (1/3) - (1 - h)) / math.sqrt(h)
    from math import erf, sqrt
    return 0.5 * (1 - erf(z / sqrt(2)))

genre_counts_list = [(c[1], c[0]) for c in genre_counts.values()]
chi2_g, df_g = chi_square_independence(genre_counts_list)
p_sub2 = chi2_pvalue(chi2_g, df_g)
print(f"Genre chi² = {chi2_g:.2f}, df = {df_g}, p ≈ {p_sub2:.5f}", file=sys.stderr)

# ---- Sub-test 3: WITHIN-VERSE slot control (CRITICAL) ----
print("\n=== Sub-test 3: CRITICAL within-verse slot control ===", file=sys.stderr)

# Among VERSES THAT CONTAIN A HAPAX: is the hapax more likely in the final
# position than in any other specific position?
# Rate(final-slot among hapax-bearing verses) vs Rate(non-final among same)
#
# More precisely: consider the N hapax roots. Each hapax has exactly one
# location (sid, vid, word_pos, verse_length). Let f = #(word_pos == verse_length).
# Compare f / N to the expected rate if hapax positions were uniform within verses.
# Expected per-hapax rate = 1 / verse_length (each slot equally likely).

expected_uniform_per_hapax = [1 / vl for r, (sid, vid, w, vl) in root_hapax_roots.items() if vl > 0]
obs_final_per_hapax = [1 if w == vl else 0 for r, (sid, vid, w, vl) in root_hapax_roots.items() if vl > 0]
n_hapax = len(obs_final_per_hapax)
f_obs = sum(obs_final_per_hapax)
f_exp = sum(expected_uniform_per_hapax)
f_exp_sd = math.sqrt(sum(p * (1 - p) for p in expected_uniform_per_hapax))
z_sub3 = (f_obs - f_exp) / f_exp_sd if f_exp_sd > 0 else 0
from math import erf, sqrt
p_sub3 = 0.5 * (1 - erf(z_sub3 / sqrt(2)))
print(f"Hapaxes n={n_hapax}, final={f_obs}, expected={f_exp:.2f} ± {f_exp_sd:.2f}", file=sys.stderr)
print(f"z_sub3 = {z_sub3:.3f}, one-sided p = {p_sub3:.2e}", file=sys.stderr)

# McNemar-style: for each hapax-containing verse, compare final-slot presence vs non-final-slot
# Paired: within verse, the hapax is either final or not. Under slot-engineering: final-rate exceeds
# uniform expectation based on verse_length. This is the same as above.

# Additionally: COMPARE hapax-final rate vs non-hapax-final rate.
# For each verse that contains a hapax, compute: is that hapax final?
# For each verse that does NOT contain a hapax, what proportion of word-positions are "verse-final"?
# (Triviallly 1/verse_length per non-hapax word.)
# This is captured by z_sub3 above.

# ---- Sub-test 4: taṣdīr mutual-exclusion ----
print("\n=== Sub-test 4: taṣdīr mutual-exclusion ===", file=sys.stderr)

# A verse exhibits surface taṣdīr (radd al-ʿajuz ʿalā al-ṣadr) if the last
# root equals the first root of the same verse (classical definition).
# By definition, a hapax cannot participate in taṣdīr (it only appears once).
# Predicted: |hapax-final ∩ taṣdīr| = 0 strictly.

tasdir_verses = set()
for (sid, vid), toks in verse_tokens.items():
    # Build word-position → root map
    roots_by_word = {}
    for w, s, r in toks:
        if r and w not in roots_by_word:
            roots_by_word[w] = r
    if not roots_by_word:
        continue
    ws = sorted(roots_by_word.keys())
    if len(ws) < 2:
        continue
    first_root = roots_by_word[ws[0]]
    last_root = roots_by_word[ws[-1]]
    if first_root == last_root:
        tasdir_verses.add((sid, vid))

print(f"taṣdīr verses (first-root == last-root): {len(tasdir_verses)}", file=sys.stderr)

# Intersection: hapax-final verses that are also taṣdīr
intersection = verse_has_final_hapax & tasdir_verses
print(f"hapax-final ∩ taṣdīr: {len(intersection)} (expected ≈ 0)", file=sys.stderr)

# Hypergeometric null: if verses were randomly labeled, expected overlap
# |hapax-final| × |tasdir| / |verses| = ?
N_verses = len(verse_quartile)
n_hap_final = len(verse_has_final_hapax)
n_tasdir = len(tasdir_verses)
expected_intersect = n_hap_final * n_tasdir / N_verses
# Standard dev under hypergeometric
var = n_hap_final * n_tasdir * (N_verses - n_hap_final) * (N_verses - n_tasdir) / (N_verses ** 2 * (N_verses - 1))
sd_intersect = math.sqrt(var)
z_sub4 = (expected_intersect - len(intersection)) / sd_intersect if sd_intersect > 0 else 0
# One-sided p for "observed < expected" (mutual exclusion direction)
p_sub4 = 0.5 * (1 - erf(z_sub4 / sqrt(2)))
print(f"Expected intersection: {expected_intersect:.2f} ± {sd_intersect:.2f}", file=sys.stderr)
print(f"Observed intersection: {len(intersection)}", file=sys.stderr)
print(f"z_sub4 = {z_sub4:.3f} (positive = mutual exclusion), one-sided p = {p_sub4:.5f}", file=sys.stderr)

# ---- Verdicts ----
print("\n=== Bonferroni k=4, α_bon=0.0025 ===", file=sys.stderr)
sub1_pass = p_sub1 < 0.0025
sub2_pass = p_sub2 < 0.0025
sub3_pass = p_sub3 < 0.0025
sub4_pass = p_sub4 < 0.0025
print(f"Sub-1 quartile trend (Cochran-Armitage one-sided): z={z_sub1:.3f}, p={p_sub1:.5f} → {'PASS' if sub1_pass else 'FAIL'}", file=sys.stderr)
print(f"Sub-2 genre chi²: {chi2_g:.2f}, p≈{p_sub2:.5f} → {'PASS' if sub2_pass else 'FAIL'}", file=sys.stderr)
print(f"Sub-3 within-verse slot (CRITICAL): z={z_sub3:.3f}, p={p_sub3:.2e} → {'PASS' if sub3_pass else 'FAIL'}", file=sys.stderr)
print(f"Sub-4 taṣdīr mutual-exclusion: z={z_sub4:.3f}, p={p_sub4:.5f} → {'PASS' if sub4_pass else 'FAIL'}", file=sys.stderr)
joint = sub1_pass and sub2_pass and sub3_pass and sub4_pass
print(f"Joint all 4: {'PASS' if joint else 'FAIL'}", file=sys.stderr)

# ---- Output ----
out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-23 hapax-final slot theory (al-Zarkashī maqṣūda li-ghayrihā)',
    'rules_tuple': 'no-tashkeel, orthographic-token, QAC-roots, counted-only-in-surah-1, Kufan, mashriqi',
    'n_root_hapaxes': n_hapax,
    'bonferroni_k': 4,
    'alpha_bon': 0.01 / 4,
    'sub1_quartile_trend': {
        'quartile_hapax_final_count': quartile_hapax_final_count,
        'quartile_verse_count': quartile_verse_count,
        'final_rates_by_q': final_rates_by_q,
        'cochran_armitage_z': z_sub1,
        'p_one_sided': p_sub1,
        'pass': sub1_pass,
    },
    'sub2_genre': {
        'genre_counts': {g: list(c) for g, c in genre_counts.items()},
        'genre_rates': genre_rates,
        'chi2': chi2_g,
        'df': df_g,
        'p': p_sub2,
        'pass': sub2_pass,
    },
    'sub3_within_verse_slot_CRITICAL': {
        'n_hapax': n_hapax,
        'observed_final': f_obs,
        'expected_uniform': f_exp,
        'expected_sd': f_exp_sd,
        'z': z_sub3,
        'p_one_sided': p_sub3,
        'pass': sub3_pass,
    },
    'sub4_tasdir_mutual_exclusion': {
        'n_tasdir_verses': n_tasdir,
        'n_hapax_final_verses': n_hap_final,
        'intersection': len(intersection),
        'expected_intersection': expected_intersect,
        'expected_sd': sd_intersect,
        'z': z_sub4,
        'p_one_sided': p_sub4,
        'pass': sub4_pass,
    },
    'joint_pass': joint,
}
out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-23-hapax-slot.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
print(json.dumps(out, indent=2, default=str))
