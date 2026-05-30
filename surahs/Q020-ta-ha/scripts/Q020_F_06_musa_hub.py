#!/usr/bin/env python3
"""
Q020-F-06 — Ṭā-Hā as the burning-bush prototype of the Mūsā pericope cycle.

Arm A (deterministic-descriptive, MW-7-capped): Q 20:9-36 carries the most complete
  H-NEW-2260 burning-bush signature-root set of the four Mūsā-cycle pericopes.
Arm B (direction-locked permutation, the single confirmatory cell): the Ṭā-Hā
  hub-strength H(Q20) = mean root-Jaccard to {Q27, Q28, Q79} exceeds a length-matched
  random-pericope null (direction TIGHTER, inherited from H-NEW-2260). Seed 20260509,
  10000 perms, alpha_bon = 0.05/1 = 0.05.

Pre-reg SHA-256 is embedded below and verified at runtime (fail-fast on mismatch).
"""
import json, hashlib, random, statistics, itertools, sys
from pathlib import Path
from collections import defaultdict

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG = PROJECT / 'surahs/Q020-ta-ha/Q020-F-06-musa-hub-prereg.md'
OUT = PROJECT / 'surahs/Q020-ta-ha/csv/Q020-F-06.json'
EXPECTED_SHA = 'c3d5c3a6e4c44853af2a599b3a38ef9cc89bd1f81350cb84c2e84461b7302309'

SEED = 20260509
NPERM = 10000
ALPHA_BON = 0.05  # k=1 permutation cell

def verify_sha():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}')
    print(f'[SHA OK] {PREREG.name} verified.')

# ---- data ----
QURAN = json.load(open(PROJECT / 'quran-text/quran-no-tashkeel.json'))
RI = json.load(open(PROJECT / 'data/morphology/root-index.json'))

# (surah, verse) -> set of QAC roots
VROOTS = defaultdict(set)
for root, atts in RI.items():
    for s, v, w in atts:
        VROOTS[(s, v)].add(root)

# Locked cycle pericopes (H-NEW-2260)
CYCLE = {
    'Q20:9-36': (20, 9, 36),
    'Q27:7-14': (27, 7, 14),
    'Q28:29-35': (28, 29, 35),
    'Q79:15-26': (79, 15, 26),
}
SIGNATURE_ROOTS = ['byD', 'ESw', 'Twy', 'Ans', '*hb', 'dbr']  # imported from H-NEW-2260

def peri_roots(s, v0, v1):
    rs = set()
    for v in range(v0, v1 + 1):
        rs |= VROOTS[(s, v)]
    return rs

def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0

def verify_boundaries():
    """Each pericope range must exist and narrate Mūsā in the no-tashkeel text."""
    sidx = {QURAN[i].get('id', i + 1): QURAN[i] for i in range(len(QURAN))}
    for name, (s, v0, v1) in CYCLE.items():
        verses = {vv['id']: vv['text'] for vv in sidx[s]['verses']}
        for v in range(v0, v1 + 1):
            if v not in verses:
                sys.exit(f'BOUNDARY FAIL: {name} verse {v} missing')
        joined = ' '.join(verses[v] for v in range(v0, v1 + 1))
        if 'موسى' not in joined and 'موسي' not in joined:
            sys.exit(f'BOUNDARY WARN: {name} does not contain موسى')
    print('[BOUNDARIES OK] all 4 cycle pericopes verified on disk.')

def main():
    verify_sha()
    verify_boundaries()

    R = {name: peri_roots(*rng) for name, rng in CYCLE.items()}
    nroots = {name: len(R[name]) for name in CYCLE}

    # ---- Arm A: signature-root completeness (deterministic) ----
    sig_count = {}
    for name in CYCLE:
        sig_count[name] = sum(1 for r in SIGNATURE_ROOTS if r in R[name])
    q20_sig = sig_count['Q20:9-36']
    a_h1 = q20_sig == max(sig_count.values()) and q20_sig > 0
    core = R['Q20:9-36'] & R['Q27:7-14'] & R['Q28:29-35'] & R['Q79:15-26']
    a_h2 = len(core) > 0
    arm_a_verdict = 'CONFIRMED' if (a_h1 and a_h2) else 'NULL'

    # ---- descriptive: pairwise Jaccard + hub-strengths (MW-7 capped) ----
    pair_J = {}
    for a, b in itertools.combinations(CYCLE, 2):
        pair_J[f'{a} x {b}'] = round(jaccard(R[a], R[b]), 4)
    hub = {}
    for a in CYCLE:
        hub[a] = statistics.mean(jaccard(R[a], R[b]) for b in CYCLE if b != a)
    hub_rank = sorted(CYCLE, key=lambda x: -hub[x])

    # ---- Arm B: Ṭā-Hā hub-strength vs length-matched random-pericope null ----
    partners = ['Q27:7-14', 'Q28:29-35', 'Q79:15-26']
    Rpart = [R[p] for p in partners]
    H_obs = statistics.mean(jaccard(R['Q20:9-36'], rp) for rp in Rpart)

    # build per-surah verse counts and a flat (surah, verse) index for windows
    sid_list = [QURAN[i].get('id', i + 1) for i in range(len(QURAN))]
    nverses = {sid_list[i]: len(QURAN[i]['verses']) for i in range(len(QURAN))}

    L = 28  # Q20:9-36 length
    TOL = 3
    # forbidden (surah, verse) cells = the four cycle pericopes
    forbidden = set()
    for (s, v0, v1) in CYCLE.values():
        for v in range(v0, v1 + 1):
            forbidden.add((s, v))

    # candidate windows: contiguous within a single surah, length in [L-TOL, L+TOL], no overlap w/ cycle
    candidates = []
    for sid in sid_list:
        nv = nverses[sid]
        for wlen in range(L - TOL, L + TOL + 1):
            if wlen < 1 or wlen > nv:
                continue
            for start in range(1, nv - wlen + 2):
                cells = [(sid, start + k) for k in range(wlen)]
                if any(c in forbidden for c in cells):
                    continue
                candidates.append((sid, start, wlen))

    rng = random.Random(SEED)
    null_H = []
    for _ in range(NPERM):
        s, start, wlen = candidates[rng.randrange(len(candidates))]
        rs = set()
        for k in range(wlen):
            rs |= VROOTS[(s, start + k)]
        h = statistics.mean(jaccard(rs, rp) for rp in Rpart)
        null_H.append(h)

    null_mean = statistics.mean(null_H)
    null_std = statistics.pstdev(null_H)
    null_p95 = sorted(null_H)[int(0.95 * NPERM)]
    z = (H_obs - null_mean) / null_std if null_std else 0.0
    p_perm = (sum(1 for x in null_H if x >= H_obs) + 1) / (NPERM + 1)

    if z <= 0:
        arm_b_verdict = 'NULL (pre-commit violation)'
    elif p_perm <= ALPHA_BON:
        arm_b_verdict = 'CONFIRMED'
    else:
        arm_b_verdict = 'DIRECTIONAL'

    out = {
        'finding_id': 'Q020-F-06',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED, 'n_perm': NPERM, 'alpha_bon': ALPHA_BON,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'cycle_pericopes': {k: list(v) for k, v in CYCLE.items()},
        'pericope_n_roots': nroots,
        'arm_A_signature_completeness': {
            'signature_roots': SIGNATURE_ROOTS,
            'signature_count_per_pericope': sig_count,
            'Q20_signature_count': q20_sig,
            'A_H1_Q20_is_max_signature': a_h1,
            'Q20_anchored_4way_core': sorted(core),
            'A_H2_core_nonempty': a_h2,
            'verdict': arm_a_verdict,
        },
        'descriptive_hub_ranking_MW7capped': {
            'pairwise_jaccard': pair_J,
            'hub_strength': {k: round(hub[k], 4) for k in CYCLE},
            'hub_rank_descending': hub_rank,
        },
        'arm_B_hub_strength_null': {
            'H_obs_Q20': round(H_obs, 4),
            'null_mean': round(null_mean, 4),
            'null_std': round(null_std, 4),
            'null_p95': round(null_p95, 4),
            'z': round(z, 3),
            'p_perm': round(p_perm, 5),
            'n_candidate_windows': len(candidates),
            'direction_locked': 'TIGHTER (z>0)',
            'verdict': arm_b_verdict,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(OUT, 'w'), indent=2, ensure_ascii=False)

    print('\n=== Q020-F-06 — Ṭā-Hā burning-bush prototype ===')
    print(f'  Arm A: Q20 signature-roots = {q20_sig}/6  per-pericope={sig_count}')
    print(f'         4-way core (n={len(core)}): {sorted(core)}')
    print(f'         Arm A verdict: {arm_a_verdict}')
    print(f'  Descriptive hub-strengths: ' + ', '.join(f'{k}={hub[k]:.4f}' for k in CYCLE))
    print(f'         hub-rank (desc): {hub_rank}')
    print(f'  Arm B: H_obs(Q20)={H_obs:.4f}  null_mean={null_mean:.4f}  p95={null_p95:.4f}  z={z:+.3f}  p_perm={p_perm:.5f}')
    print(f'         n_candidate_windows={len(candidates)}')
    print(f'         Arm B verdict: {arm_b_verdict}')

if __name__ == '__main__':
    main()
