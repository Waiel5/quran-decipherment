#!/usr/bin/env python3
"""Q038-F-08 — David-narrative (Q 38:17-29) repentance-marker density vs David-praise (Q 21:78-80).

Pre-reg: surahs/Q038-sad/Q038-F-08-david-repentance-marker-prereg.md
Pre-reg SHA256: 20cd8ed33367cfef0c1bf6acdaba7b25658ccdccfc96a81f39cc0239f950a39f
Rules-tuple: (no-tashkeel, root-tokens via QAC-v0.4, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, random
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-08-david-repentance-marker-prereg.md'
EXPECTED_SHA = '20cd8ed33367cfef0c1bf6acdaba7b25658ccdccfc96a81f39cc0239f950a39f'
SEED = 20260509
N_PERM = 10000

MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

# Repentance-root set R (locked in pre-reg)
R_ROOTS = {'Awb', 'twb', 'gfr', 'sjd', 'rjE', 'ndm'}

# Segments
SEG_A = ('Q 38:17-29', 38, 17, 29)
SEG_B = ('Q 21:78-80', 21, 78, 80)


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_qac_tokens():
    """Returns list of (surah, verse, word, root_or_None). Only STEM rows yield root; PREFIX/SUFFIX rows are token-position-bound but no ROOT field.

    For density we count by WORD: a word at (s, v, w) is counted ONCE; it counts as a repentance-token if ANY of its segments has ROOT in R.
    """
    # word_id -> set(roots)
    word_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
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
            features = parts[3]
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    word_roots[(s, v, w)].add(root)
                    break
    return word_roots


def segment_densities(word_roots, surah, v0, v1):
    """Return (n_tokens, n_repentance_tokens) for the segment."""
    n_tokens = 0
    n_rep = 0
    # Group by (s, v) -> set of word ids
    by_verse = defaultdict(set)
    by_verse_R = defaultdict(set)
    for (s, v, w), roots in word_roots.items():
        if s == surah and v0 <= v <= v1:
            by_verse[v].add(w)
            if roots & R_ROOTS:
                by_verse_R[v].add(w)
    per_verse = {}
    for v in range(v0, v1 + 1):
        nt = len(by_verse.get(v, set()))
        nr = len(by_verse_R.get(v, set()))
        per_verse[v] = (nt, nr)
        n_tokens += nt
        n_rep += nr
    return n_tokens, n_rep, per_verse


def main():
    verify_sha()
    rng = random.Random(SEED)

    word_roots = load_qac_tokens()

    # Verify all roots have ≥ 1 attestation in QAC
    all_roots_seen = set()
    for rs in word_roots.values():
        all_roots_seen |= rs
    missing = R_ROOTS - all_roots_seen
    if missing:
        print(f"FAIL: pre-registered roots not found in QAC: {missing}", file=sys.stderr)
        sys.exit(1)

    # Segment A: Q 38:17-29
    nt_A, nr_A, perv_A = segment_densities(word_roots, SEG_A[1], SEG_A[2], SEG_A[3])
    dens_A = nr_A / nt_A if nt_A else 0.0

    # Segment B: Q 21:78-80
    nt_B, nr_B, perv_B = segment_densities(word_roots, SEG_B[1], SEG_B[2], SEG_B[3])
    dens_B = nr_B / nt_B if nt_B else 0.0

    delta = dens_A - dens_B

    # Permutation null: pool the 16 verses, randomly assign 13 to "A" and 3 to "B", recompute Δ
    pool = []
    for v in range(SEG_A[2], SEG_A[3] + 1):
        nt, nr = perv_A[v]
        pool.append((nt, nr))
    for v in range(SEG_B[2], SEG_B[3] + 1):
        nt, nr = perv_B[v]
        pool.append((nt, nr))

    nA, nB = len(perv_A), len(perv_B)
    null_deltas = []
    for _ in range(N_PERM):
        idx = list(range(len(pool)))
        rng.shuffle(idx)
        Aset = idx[:nA]
        Bset = idx[nA:]
        ntA = sum(pool[i][0] for i in Aset)
        nrA = sum(pool[i][1] for i in Aset)
        ntB = sum(pool[i][0] for i in Bset)
        nrB = sum(pool[i][1] for i in Bset)
        dA = nrA / ntA if ntA else 0.0
        dB = nrB / ntB if ntB else 0.0
        null_deltas.append(dA - dB)

    p_greater = sum(1 for d in null_deltas if d >= delta) / N_PERM
    null_mean = sum(null_deltas) / N_PERM
    null_std = (sum((d - null_mean)**2 for d in null_deltas) / N_PERM)**0.5

    direction_match = delta > 0

    if direction_match and p_greater < 0.05:
        verdict = 'CONFIRMED'
    elif direction_match and p_greater < 0.5:
        verdict = 'DIRECTIONAL'
    elif not direction_match:
        verdict = 'PRE-COMMIT-VIOLATION' if delta < 0 else 'NULL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q038-F-08',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, root-tokens via QAC-v0.4, Hafs-Kufan, Mashriqi)',
        'repentance_roots': sorted(R_ROOTS),
        'segment_A': {
            'label': SEG_A[0], 'surah': SEG_A[1], 'v0': SEG_A[2], 'v1': SEG_A[3],
            'n_tokens': nt_A, 'n_repentance_tokens': nr_A, 'density': dens_A,
            'per_verse': {str(v): {'n_tokens': perv_A[v][0], 'n_rep': perv_A[v][1]} for v in perv_A},
        },
        'segment_B': {
            'label': SEG_B[0], 'surah': SEG_B[1], 'v0': SEG_B[2], 'v1': SEG_B[3],
            'n_tokens': nt_B, 'n_repentance_tokens': nr_B, 'density': dens_B,
            'per_verse': {str(v): {'n_tokens': perv_B[v][0], 'n_rep': perv_B[v][1]} for v in perv_B},
        },
        'delta_A_minus_B': delta,
        'null_mean': null_mean,
        'null_std': null_std,
        'p_greater_perm': p_greater,
        'direction_locked': 'A > B (Q 38 David-narrative more repentance-focused than Q 21 David-praise)',
        'direction_match': direction_match,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-08.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Repentance roots (locked): {sorted(R_ROOTS)}")
    print(f"Segment A {SEG_A[0]}: n_tokens={nt_A}  n_rep={nr_A}  density={dens_A*100:.2f}%")
    print(f"Segment B {SEG_B[0]}: n_tokens={nt_B}  n_rep={nr_B}  density={dens_B*100:.2f}%")
    print(f"Δ = density(A) - density(B) = {delta*100:+.2f} pp")
    print(f"Null mean: {null_mean*100:+.3f} pp  std: {null_std*100:.3f} pp")
    print(f"p_greater (one-tailed perm): {p_greater:.4f}")
    print(f"Verdict: {verdict}")


if __name__ == '__main__':
    main()
