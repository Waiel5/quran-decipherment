#!/usr/bin/env python3
"""Q084-F-03 — Q 84:7-15 book-hand antithesis-diptych shared-anchor cohesion.

Tests whether the two antithetical arms of the Q 84 judgment-scene reuse anchor-roots
(the *muqābala* mirror) at a rate above what length-matched within-surah adjacent
verse-block pairs share by chance.

  Arm A (vv 7-9)   = right-hand fate (book in right hand, easy reckoning, returns joyful).
  Arm B (vv 10-15) = behind-back fate (book behind back, calls ruin, burns, had-been-joyful).

Statistic S_obs = |roots(A) ∩ roots(B)|  (also report J(A,B) = |A∩B|/|A∪B|).
Direction LOCKED: S_obs > null mean (the antithesis is built ON shared anchors).
Null (seed 20260509, 10000 perms): random within-surah contiguous 9-verse windows,
split 3|6, |roots(block1) ∩ roots(block2)|.

Pre-reg: surahs/Q084-al-inshiqaq/preregs/Q084-F-03-book-hand-antithesis-prereg.md
Pre-reg SHA256: bf28ee3f6aafcf3fc17d8fcd9718052f5e5ddc054f1a43225c4a5ac051c38ffb
Rules-tuple: (no-tashkeel, QAC-v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import os
import sys
import random
from collections import defaultdict

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT_ROOT,
                      'surahs/Q084-al-inshiqaq/preregs/Q084-F-03-book-hand-antithesis-prereg.md')
EXPECTED_SHA = 'bf28ee3f6aafcf3fc17d8fcd9718052f5e5ddc054f1a43225c4a5ac051c38ffb'
SEED = 20260509
REPLICATION_SEED = 20260511
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_JSON = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
OUT_JSON = os.path.join(PROJECT_ROOT, 'surahs/Q084-al-inshiqaq/csv/Q084-F-03.json')

ARM_A = [7, 8, 9]
ARM_B = [10, 11, 12, 13, 14, 15]


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: pre-reg SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"[SHA-OK] pre-reg verified: {actual}")


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4."""
    verse_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0].strip('()')
            features = parts[3]
            try:
                s, v, w, seg = (int(x) for x in loc.split(':'))
            except ValueError:
                continue
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    verse_roots[(s, v)].add(tok[len('ROOT:'):])
                    break
    return dict(verse_roots)


def block_roots(verse_roots, surah, verses):
    out = set()
    for v in verses:
        out |= verse_roots.get((surah, v), set())
    return out


def run_null(verse_roots, surah_verse_list, seed, s_obs):
    """Random within-surah contiguous 9-verse windows split 3|6."""
    rng = random.Random(seed)
    lenA, lenB = len(ARM_A), len(ARM_B)
    total = lenA + lenB  # 9
    # candidate windows: all (surah, start) with start..start+8 within surah
    candidates = []
    for surah, n in surah_verse_list:
        for start in range(1, n - total + 2):
            candidates.append((surah, start))
    null_S = []
    for _ in range(N_PERM):
        surah, start = candidates[rng.randrange(len(candidates))]
        b1 = list(range(start, start + lenA))
        b2 = list(range(start + lenA, start + total))
        r1 = block_roots(verse_roots, surah, b1)
        r2 = block_roots(verse_roots, surah, b2)
        null_S.append(len(r1 & r2))
    null_mean = sum(null_S) / len(null_S)
    null_std = (sum((x - null_mean) ** 2 for x in null_S) / len(null_S)) ** 0.5
    n_ge = sum(1 for x in null_S if x >= s_obs)
    p = (n_ge + 1) / (N_PERM + 1)
    return {
        'seed': seed,
        'null_mean': null_mean,
        'null_std': null_std,
        'n_candidate_windows': len(candidates),
        'n_ge_obs': n_ge,
        'p_perm': p,
        'z': (s_obs - null_mean) / null_std if null_std > 0 else None,
    }


def main():
    verify_sha()
    verse_roots = load_qac_roots_by_verse()

    data = json.load(open(QURAN_JSON))
    surah_verse_list = [(s['id'], s['total_verses']) for s in data]

    rA = block_roots(verse_roots, 84, ARM_A)
    rB = block_roots(verse_roots, 84, ARM_B)
    shared = sorted(rA & rB)
    union = rA | rB
    s_obs = len(shared)
    j_ab = s_obs / len(union) if union else 0.0

    print(f"[obs] Arm A (vv {ARM_A}) roots ({len(rA)}): {sorted(rA)}")
    print(f"[obs] Arm B (vv {ARM_B}) roots ({len(rB)}): {sorted(rB)}")
    print(f"[obs] SHARED mirror-anchors ({s_obs}): {shared}")
    print(f"[obs] S_obs = {s_obs}; J(A,B) = {j_ab:.4f}")

    primary = run_null(verse_roots, surah_verse_list, SEED, s_obs)
    replication = run_null(verse_roots, surah_verse_list, REPLICATION_SEED, s_obs)

    direction_match = s_obs > primary['null_mean']
    pre_commit_violation = s_obs < primary['null_mean']
    if pre_commit_violation:
        verdict = 'NULL (pre-commit violation)'
    elif direction_match and primary['p_perm'] < 0.05:
        verdict = 'PASS-DIRECTED'
    elif direction_match:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q084-F-03',
        'rules_tuple': '(no-tashkeel, QAC-v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'prereg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
        'arm_A_verses': ARM_A,
        'arm_B_verses': ARM_B,
        'arm_A_roots': sorted(rA),
        'arm_B_roots': sorted(rB),
        'shared_mirror_anchors': shared,
        'S_obs': s_obs,
        'jaccard_AB': j_ab,
        'primary_null': primary,
        'replication_null': replication,
        'direction_match_lock': direction_match,
        'pre_commit_violation': pre_commit_violation,
        'verdict': verdict,
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"\n[null seed {SEED}] mean={primary['null_mean']:.4f} sd={primary['null_std']:.4f} "
          f"z={primary['z']:.3f} p_perm={primary['p_perm']:.5f} (n_ge={primary['n_ge_obs']})")
    print(f"[null seed {REPLICATION_SEED}] mean={replication['null_mean']:.4f} "
          f"p_perm={replication['p_perm']:.5f}")
    print(f"\nVERDICT: {verdict}")
    print(f"Wrote: {OUT_JSON}")


if __name__ == '__main__':
    main()
