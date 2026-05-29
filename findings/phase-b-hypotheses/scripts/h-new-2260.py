#!/usr/bin/env python3
"""H-NEW-2260 — Prophet-cycle pericope parallelism/cohesion (Nūḥ / Mūsā / Ibrāhīm).

For each of three prophet cycles, computes the mean pairwise root-Jaccard among
the cycle's bounded pericopes and tests it against a length-matched
random-pericope permutation null. Extends cross-finding-025-formal (the
scale-of-aggregation pericope-flip law) to the recurring-prophet-narrative
marker class.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2260-prophet-cycle-pericope.md
Pre-reg SHA256: 0845e412aa91ac3668c1ada6b9969de6341ee9fcd658fdbaad9e76eac435ec25

Direction lock (all 3 cycles): TIGHTER (J_mean > null_mean, z > 0).
Seed 20260509, n_perm=10000. Bonferroni across 3 cycles: α = 0.05/3 = 0.016667.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, verse-union pericope,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict
from itertools import combinations

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(
    PROJECT_ROOT,
    'findings/phase-b-hypotheses/prereg-h-new-2260-prophet-cycle-pericope.md',
)
EXPECTED_SHA = '0845e412aa91ac3668c1ada6b9969de6341ee9fcd658fdbaad9e76eac435ec25'
SEED = 20260509
N_PERM = 10000
BONFERRONI_K = 3
ALPHA_CORRECTED = 0.05 / BONFERRONI_K  # 0.016667

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_NO_TASHKEEL = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-2260.json')

# LOCKED pericope inventory (boundaries verified against quran-no-tashkeel.json).
# (label, surah, verse_start, verse_end)
CYCLES = {
    'NUH': [
        ('Q 7:59-64',     7,  59,  64),
        ('Q 11:25-49',   11,  25,  49),
        ('Q 23:23-30',   23,  23,  30),
        ('Q 26:105-122', 26, 105, 122),
        ('Q 54:9-17',    54,   9,  17),
        ('Q 71:1-28',    71,   1,  28),
    ],
    'MUSA': [
        ('Q 20:9-36',  20,  9, 36),
        ('Q 27:7-14',  27,  7, 14),
        ('Q 28:29-35', 28, 29, 35),
        ('Q 79:15-26', 79, 15, 26),
    ],
    'IBRAHIM': [
        ('Q 6:74-83',   6,  74,  83),
        ('Q 19:41-50', 19,  41,  50),
        ('Q 21:51-70', 21,  51,  70),
        ('Q 26:69-104', 26, 69, 104),
        ('Q 37:83-113', 37, 83, 113),
    ],
}


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def verify_boundaries():
    """Confirm every locked pericope verse-range exists in the canonical text."""
    text = json.load(open(QURAN_NO_TASHKEEL))
    counts = {int(s['id']): len(s['verses']) for s in text}
    failures = []
    for cyc, pers in CYCLES.items():
        for label, s, v0, v1 in pers:
            if s not in counts:
                failures.append(f'{cyc} {label}: surah {s} not found')
                continue
            if v0 < 1 or v1 > counts[s] or v0 > v1:
                failures.append(f'{cyc} {label}: range invalid (surah has {counts[s]} verses)')
    if failures:
        print('FAIL: pericope boundary verification failed:', file=sys.stderr)
        for f in failures:
            print('  ' + f, file=sys.stderr)
        sys.exit(1)


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4 — extraction identical
    to H-NEW-1380 / H-NEW-1500 / H-NEW-1760 (first ROOT feature per segment)."""
    verse_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    verse_roots[(s, v)].add(root)
                    break
    return dict(verse_roots)


def pericope_roots(verse_roots, surah, vstart, vend):
    out = set()
    for v in range(vstart, vend + 1):
        out |= verse_roots.get((surah, v), set())
    return out


def mean_pairwise_jaccard(root_sets):
    pairs = list(combinations(range(len(root_sets)), 2))
    if not pairs:
        return 0.0
    vals = []
    for i, j in pairs:
        a, b = root_sets[i], root_sets[j]
        u = a | b
        vals.append(len(a & b) / len(u) if u else 0.0)
    return sum(vals) / len(vals)


def run_cycle(cyc_name, pers, verse_roots, all_verses, rng):
    # Observed
    obs_root_sets, obs_lengths, per_summary = [], [], []
    for label, s, v0, v1 in pers:
        rs = pericope_roots(verse_roots, s, v0, v1)
        L = v1 - v0 + 1
        obs_root_sets.append(rs)
        obs_lengths.append(L)
        per_summary.append({
            'label': label, 'surah': s, 'verse_start': v0, 'verse_end': v1,
            'n_verses': L, 'n_unique_roots': len(rs),
        })

    obs_J = mean_pairwise_jaccard(obs_root_sets)

    # Per-pair Jaccard table (transparency)
    pair_table = []
    for (i, j) in combinations(range(len(obs_root_sets)), 2):
        a, b = obs_root_sets[i], obs_root_sets[j]
        u = a | b
        Jij = (len(a & b) / len(u)) if u else 0.0
        pair_table.append({
            'i': pers[i][0], 'j': pers[j][0],
            'inter': len(a & b), 'union': len(u),
            'shared_roots': sorted(a & b),
            'jaccard': Jij,
        })

    # Length-matched permutation null
    null_Js = []
    for _ in range(N_PERM):
        null_sets = []
        for L in obs_lengths:
            start = rng.randrange(0, len(all_verses) - L + 1)
            window = all_verses[start:start + L]
            rs = set()
            for vk in window:
                rs |= verse_roots.get(vk, set())
            null_sets.append(rs)
        null_Js.append(mean_pairwise_jaccard(null_sets))

    null_mean = sum(null_Js) / len(null_Js)
    null_std = (sum((x - null_mean) ** 2 for x in null_Js) / len(null_Js)) ** 0.5
    z = (obs_J - null_mean) / null_std if null_std > 0 else float('nan')
    n_ge = sum(1 for x in null_Js if x >= obs_J)
    p_greater = n_ge / N_PERM
    sorted_null = sorted(null_Js)
    p95 = sorted_null[int(0.95 * N_PERM)]
    p_reportable_max = 1.0 / N_PERM if n_ge == 0 else p_greater

    direction_match = obs_J > null_mean
    pre_commit_violation = obs_J < null_mean

    if pre_commit_violation:
        verdict = 'PRE-COMMIT-VIOLATION'
    elif direction_match and p_greater < ALPHA_CORRECTED:
        verdict = 'PASS-DIRECTED'
    elif direction_match and p_greater < 0.05:
        verdict = 'DIRECTIONAL'
    elif direction_match:
        verdict = 'NULL-AT-PERICOPE-SCALE'
    else:
        verdict = 'NULL-AT-PERICOPE-SCALE'

    return {
        'cycle': cyc_name,
        'n_pericopes': len(pers),
        'n_pairs': len(pair_table),
        'pericopes': per_summary,
        'pericope_lengths': obs_lengths,
        'pairwise_jaccards': pair_table,
        'observed_mean_pairwise_jaccard': obs_J,
        'null_mean': null_mean,
        'null_std': null_std,
        'null_p95': p95,
        'z_score': z,
        'p_greater_perm_strict': p_greater,
        'p_reportable_upper_bound': p_reportable_max,
        'n_perm_ge_obs': n_ge,
        'direction_locked': 'TIGHTER (J_mean > null_mean)',
        'direction_match': direction_match,
        'bonferroni_alpha': ALPHA_CORRECTED,
        'passes_bonferroni': (direction_match and p_greater < ALPHA_CORRECTED),
        'verdict': verdict,
    }


def main():
    verify_sha()
    verify_boundaries()
    rng = random.Random(SEED)
    verse_roots = load_qac_roots_by_verse()
    all_verses = sorted(verse_roots.keys())

    results = {}
    for cyc_name in ('NUH', 'MUSA', 'IBRAHIM'):
        results[cyc_name] = run_cycle(cyc_name, CYCLES[cyc_name], verse_roots, all_verses, rng)

    n_pass = sum(1 for r in results.values() if r['verdict'] == 'PASS-DIRECTED')
    n_directional = sum(1 for r in results.values() if r['verdict'] == 'DIRECTIONAL')
    n_null = sum(1 for r in results.values() if r['verdict'] in ('NULL-AT-PERICOPE-SCALE', 'PRE-COMMIT-VIOLATION'))

    if n_pass >= 2:
        synthesis = (
            f'{n_pass}/3 cycles PASS-DIRECTED — prophet-cycle pericopes cohere; '
            'further cross-finding-025 evidence (pericope-scale cohesion generalizes '
            'to the recurring-prophet-narrative marker class)'
        )
        supports_cf025 = True
    elif n_pass == 1:
        synthesis = (
            f'1/3 cycles PASS-DIRECTED, {n_directional} DIRECTIONAL, {n_null} NULL — '
            'partial / cycle-conditional; cohesion of recurring-prophet narrative is '
            'not uniform across cycles'
        )
        supports_cf025 = False
    else:
        synthesis = (
            f'0/3 cycles PASS-DIRECTED — recurring-prophet narrative does NOT cohere at '
            'pericope scale; substantive NULL about narrative-vocabulary variation'
        )
        supports_cf025 = False

    out = {
        'finding_id': 'H-NEW-2260',
        'title': 'Prophet-cycle pericope parallelism/cohesion — Nūḥ / Mūsā / Ibrāhīm',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': BONFERRONI_K,
        'bonferroni_alpha': ALPHA_CORRECTED,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'aggregation_scale': 'pericope (locked verse ranges per prophet cycle)',
        'extends': 'cross-finding-025-formal (scale-of-aggregation pericope-flip law)',
        'cycles': results,
        'n_pass_directed': n_pass,
        'n_directional': n_directional,
        'n_null': n_null,
        'synthesis_verdict': synthesis,
        'supports_cross_finding_025': supports_cf025,
        'cross_finding_025_note': (
            'H-NEW-1310 Christ-narrative was NULL at whole-surah but flipped at pericope '
            'scale (H-NEW-1500). This finding tests three additional prophet cycles directly '
            'at pericope scale with a length-matched random-pericope null and Bonferroni-3.'
        ),
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Bonferroni α = 0.05/{BONFERRONI_K} = {ALPHA_CORRECTED:.6f}\n")
    for cyc_name in ('NUH', 'MUSA', 'IBRAHIM'):
        r = results[cyc_name]
        print(f"=== {cyc_name} ({r['n_pericopes']} pericopes, {r['n_pairs']} pairs) ===")
        print(f"  J_obs    = {r['observed_mean_pairwise_jaccard']:.6f}")
        print(f"  null mean= {r['null_mean']:.6f}  std = {r['null_std']:.6f}  p95 = {r['null_p95']:.6f}")
        print(f"  z        = {r['z_score']:.3f}")
        print(f"  p_perm   = {r['p_greater_perm_strict']:.4f}  (>= obs: {r['n_perm_ge_obs']}/{N_PERM})")
        print(f"  Bonferroni-pass: {r['passes_bonferroni']}")
        print(f"  Verdict  = {r['verdict']}\n")
    print(f"Synthesis: {synthesis}")
    print(f"Supports cross-finding-025: {supports_cf025}")


if __name__ == '__main__':
    main()
