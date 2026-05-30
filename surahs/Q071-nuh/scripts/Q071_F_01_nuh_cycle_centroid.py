#!/usr/bin/env python3
"""Q071-F-01 — Is Q 71 the lexical CENTROID / anchor of the Nūḥ-pericope cycle?

Extends H-NEW-2260 (Nūḥ-cycle pericope cohesion PASS, z=+2.51). Direction LOCKED
toward the intuitive hypothesis: Q 71 (the dedicated Nūḥ surah) is the MOST-CENTRAL
pericope of the 6-member Nūḥ cycle (Arm A rank==1) AND its mean intra-cycle
root-Jaccard exceeds a length-matched random-anchor null (Arm B z>0, one-sided).

Pre-reg: surahs/Q071-nuh/Q071-F-01-nuh-cycle-centroid-prereg.md
Pre-reg SHA-256: e19913e96977f32ea95405ab399f69f992e774b68f33d331214e59d7b5cf996f
Seed 20260509, n_perm=10000, Bonferroni-2 -> alpha = 0.025.
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

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs/Q071-nuh/Q071-F-01-nuh-cycle-centroid-prereg.md')
EXPECTED_SHA = 'e19913e96977f32ea95405ab399f69f992e774b68f33d331214e59d7b5cf996f'
SEED = 20260509
N_PERM = 10000
BONFERRONI_K = 2
ALPHA = 0.05 / BONFERRONI_K  # 0.025

MORPH = os.path.join(ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN = os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')
OUT = os.path.join(ROOT, 'surahs/Q071-nuh/csv/Q071-F-01.json')

# LOCKED Nūḥ-cycle pericope inventory — copied verbatim from H-NEW-2260.
# (label, surah, verse_start, verse_end)
NUH = [
    ('Q 7:59-64',     7,  59,  64),
    ('Q 11:25-49',   11,  25,  49),
    ('Q 23:23-30',   23,  23,  30),
    ('Q 26:105-122', 26, 105, 122),
    ('Q 54:9-17',    54,   9,  17),
    ('Q 71:1-28',    71,   1,  28),
]
Q71_LABEL = 'Q 71:1-28'

# MW-7: the 15 stored H-NEW-2260 Nūḥ pairwise Jaccards must reproduce exactly.
STORED_2260_JACCARD = {
    ('Q 7:59-64', 'Q 11:25-49'): 0.1984732824427481,
    ('Q 7:59-64', 'Q 23:23-30'): 0.25757575757575757,
    ('Q 7:59-64', 'Q 26:105-122'): 0.3076923076923077,
    ('Q 7:59-64', 'Q 54:9-17'): 0.16666666666666666,
    ('Q 7:59-64', 'Q 71:1-28'): 0.15384615384615385,
    ('Q 11:25-49', 'Q 23:23-30'): 0.27007299270072993,
    ('Q 11:25-49', 'Q 26:105-122'): 0.16911764705882354,
    ('Q 11:25-49', 'Q 54:9-17'): 0.14184397163120568,
    ('Q 11:25-49', 'Q 71:1-28'): 0.17222222222222222,
    ('Q 23:23-30', 'Q 26:105-122'): 0.1643835616438356,
    ('Q 23:23-30', 'Q 54:9-17'): 0.16,
    ('Q 23:23-30', 'Q 71:1-28'): 0.1322314049586777,
    ('Q 26:105-122', 'Q 54:9-17'): 0.125,
    ('Q 26:105-122', 'Q 71:1-28'): 0.14018691588785046,
    ('Q 54:9-17', 'Q 71:1-28'): 0.14814814814814814,
}


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected {EXPECTED_SHA}\n  actual   {actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"Pre-reg SHA-256 OK: {actual}")


def load_qac_roots_by_verse():
    vr = defaultdict(set)
    with open(MORPH, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0].strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc.split(':'))
            except ValueError:
                continue
            for tok in parts[3].split('|'):
                if tok.startswith('ROOT:'):
                    vr[(s, v)].add(tok[len('ROOT:'):])
                    break
    return dict(vr)


def pericope_roots(vr, s, v0, v1):
    out = set()
    for v in range(v0, v1 + 1):
        out |= vr.get((s, v), set())
    return out


def jac(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def window_roots(vr, all_verses, start, L):
    out = set()
    for vk in all_verses[start:start + L]:
        out |= vr.get(vk, set())
    return out


def main():
    verify_sha()
    # boundary check
    text = json.load(open(QURAN))
    counts = {int(s['id']): len(s['verses']) for s in text}
    for label, s, v0, v1 in NUH:
        assert s in counts and 1 <= v0 <= v1 <= counts[s], f"bad range {label}"
    print("Pericope boundaries OK.")

    vr = load_qac_roots_by_verse()
    all_verses = sorted(vr.keys())

    # observed root-sets
    rs = {label: pericope_roots(vr, s, v0, v1) for label, s, v0, v1 in NUH}
    labels = [p[0] for p in NUH]

    # MW-7 reproduction of stored H-NEW-2260 Jaccards
    print("\nMW-7 reproduction of stored H-NEW-2260 Nūḥ pairwise Jaccards:")
    repro_ok = True
    for (i, j), stored in STORED_2260_JACCARD.items():
        got = jac(rs[i], rs[j])
        ok = abs(got - stored) < 1e-9
        repro_ok = repro_ok and ok
        if not ok:
            print(f"  MISMATCH {i} x {j}: got {got} stored {stored}")
    if not repro_ok:
        print("FATAL: H-NEW-2260 reproduction failed.", file=sys.stderr)
        sys.exit(1)
    print("  all 15 pairwise Jaccards reproduce exactly (tol 1e-9). OK.")

    # symmetric Jaccard lookup
    J = {}
    for i, j in combinations(labels, 2):
        v = jac(rs[i], rs[j])
        J[(i, j)] = v
        J[(j, i)] = v

    # ---- Arm A: centrality rank ----
    centrality = {a: sum(J[(a, b)] for b in labels if b != a) / (len(labels) - 1)
                  for a in labels}
    ranked = sorted(labels, key=lambda a: -centrality[a])
    centrality_table = [{'pericope': a, 'mean_jaccard': centrality[a],
                         'rank': ranked.index(a) + 1} for a in labels]
    q71_rank = ranked.index(Q71_LABEL) + 1
    q71_centrality = centrality[Q71_LABEL]
    centroid = ranked[0]

    if q71_rank == 1:
        armA = 'PASS-DIRECTED'
    elif q71_rank == 2:
        armA = 'DIRECTIONAL'
    else:
        armA = 'NULL'

    # ---- Arm B: length-matched random-anchor swap null ----
    L71 = 28
    other5 = [a for a in labels if a != Q71_LABEL]
    other5_sets = [rs[a] for a in other5]
    rng = random.Random(SEED)
    null_centralities = []
    max_start = len(all_verses) - L71
    for _ in range(N_PERM):
        start = rng.randrange(0, max_start + 1)
        w = window_roots(vr, all_verses, start, L71)
        c = sum(jac(w, o) for o in other5_sets) / len(other5_sets)
        null_centralities.append(c)
    null_mean = sum(null_centralities) / N_PERM
    null_std = (sum((x - null_mean) ** 2 for x in null_centralities) / N_PERM) ** 0.5
    z = (q71_centrality - null_mean) / null_std if null_std > 0 else float('nan')
    n_ge = sum(1 for x in null_centralities if x >= q71_centrality)
    p_perm = n_ge / N_PERM
    sorted_null = sorted(null_centralities)
    null_p95 = sorted_null[int(0.95 * N_PERM)]

    if z <= 0:
        armB = 'PRE-COMMIT-VIOLATION'
    elif p_perm <= ALPHA:
        armB = 'PASS-DIRECTED'
    elif p_perm <= 0.05:
        armB = 'DIRECTIONAL'
    else:
        armB = 'NULL'

    # ---- overall verdict ----
    if armA == 'PASS-DIRECTED' and armB == 'PASS-DIRECTED':
        verdict = 'CONFIRMED'
    elif armA == 'NULL' and armB in ('PASS-DIRECTED', 'DIRECTIONAL'):
        verdict = 'PARTIAL'
    elif armA == 'NULL' and armB in ('NULL', 'PRE-COMMIT-VIOLATION'):
        verdict = 'NULL'
    else:
        verdict = f'MIXED (A={armA}, B={armB})'

    out = {
        'finding_id': 'Q071-F-01',
        'title': 'Q 71 Nūḥ as lexical centroid/anchor of the Nūḥ-pericope cycle',
        'prereg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': BONFERRONI_K,
        'alpha_bon': ALPHA,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'parent': 'H-NEW-2260 (Nūḥ cycle PASS z=+2.51)',
        'mw7_2260_reproduction_ok': True,
        'direction_locked': 'Q71 most-central (Arm A rank==1) AND Q71 centrality > random-anchor null (Arm B z>0)',
        'arm_A_centrality': {
            'table': sorted(centrality_table, key=lambda r: r['rank']),
            'q71_rank': q71_rank,
            'q71_mean_jaccard': q71_centrality,
            'centroid_pericope': centroid,
            'centroid_mean_jaccard': centrality[centroid],
            'verdict': armA,
        },
        'arm_B_anchor_swap_null': {
            'L_matched': L71,
            'q71_observed_centrality': q71_centrality,
            'null_mean': null_mean,
            'null_std': null_std,
            'null_p95': null_p95,
            'z': z,
            'p_perm_one_sided_greater': p_perm,
            'n_perm_ge_obs': n_ge,
            'verdict': armB,
        },
        'overall_verdict': verdict,
        'honest_note': (
            'Direction was LOCKED toward the intuitive Q71-as-centroid hypothesis. '
            'Q 71 is the longest pericope (L=28, 87 unique roots) and carries large '
            'private vocabulary blocks (cosmological signs vv15-20; the five named '
            'idols v23; the night/day complaint) that the short cross-surah retellings '
            'lack — which depresses lexical (Jaccard) centrality even if Q 71 is the '
            'NARRATIVE anchor of the cycle.'
        ),
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"\nBonferroni-{BONFERRONI_K} alpha = {ALPHA}")
    print("\n=== Arm A — centrality rank ===")
    for r in sorted(centrality_table, key=lambda r: r['rank']):
        mark = '  <-- Q 71' if r['pericope'] == Q71_LABEL else ''
        print(f"  rank {r['rank']}  {r['pericope']:14s} mean_J={r['mean_jaccard']:.5f}{mark}")
    print(f"  centroid = {centroid}; Q 71 rank = {q71_rank}/6 -> Arm A {armA}")
    print("\n=== Arm B — length-matched random-anchor swap null (L=28) ===")
    print(f"  Q 71 observed centrality = {q71_centrality:.5f}")
    print(f"  null mean = {null_mean:.5f}  std = {null_std:.5f}  p95 = {null_p95:.5f}")
    print(f"  z = {z:.3f}   p_perm(one-sided greater) = {p_perm:.4f}  (#null>=obs = {n_ge})")
    print(f"  Arm B {armB}")
    print(f"\nOVERALL VERDICT: {verdict}")
    print(f"Result written to {OUT}")


if __name__ == '__main__':
    main()
