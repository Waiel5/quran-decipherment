#!/usr/bin/env python3
"""Q030-F-01 — Q 29 + Q 30 ALM-exception sub-cluster coherence (joint test).

Pre-reg: surahs/Q030-al-rum/Q030-F-01-alm-exception-subcluster-prereg.md
Pre-reg SHA256: 05a893361805442c1a83969f3f899f4e1d0563bebb7d92b52d76b902d657fa8f
Rules-tuple: (no-tashkeel, QAC-stem-roots, hafs-kufan, basmala-counted-only-in-Q1, mashriqi)
"""
import json, re, hashlib, sys, os, itertools, random
from collections import defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-01-alm-exception-subcluster-prereg.md'
EXPECTED_SHA = '05a893361805442c1a83969f3f899f4e1d0563bebb7d92b52d76b902d657fa8f'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
SEED = 20260507
N_PERMS = 10000

TARGET = [29, 30]
NON_EXCEPTION_ALM = [2, 3, 31, 32]
ALM_ALL = [2, 3, 29, 30, 31, 32]

IMTIHAN_ROOTS = ['ftn', 'blw', 'mHn', 'Sbr', 'jhd']
HIST_ROOTS = ['glb', 'nSr', 'kwn', 'rwm', 'bDE', 'snw']


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual={actual}", file=sys.stderr)
        sys.exit(1)


def load_qac():
    surah_root_counts = defaultdict(lambda: defaultdict(int))
    surah_word_count = defaultdict(int)
    with open(QAC) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc, form, pos, attrs = parts
            m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
            if not m:
                continue
            s, v, w, t = (int(x) for x in m.groups())
            rm = re.search(r'ROOT:([^|]+)', attrs)
            if rm:
                surah_root_counts[s][rm.group(1)] += 1
            if t == 1:
                surah_word_count[s] += 1
    return surah_root_counts, surah_word_count


def density(surahs, roots, src, wc):
    n_root = sum(src[s][r] for s in surahs for r in roots)
    n_words = sum(wc[s] for s in surahs)
    return n_root, n_words, (n_root / n_words if n_words else 0.0)


def main():
    verify_sha()
    src, wc = load_qac()

    # Per-surah descriptors
    per_surah = {}
    for s in ALM_ALL:
        per_surah[s] = {
            'imtihan_count': sum(src[s][r] for r in IMTIHAN_ROOTS),
            'hist_count': sum(src[s][r] for r in HIST_ROOTS),
            'wc': wc[s],
        }

    # Pooled densities (target vs non-exception ALM)
    t_imt_n, t_wc, t_imt_rate = density(TARGET, IMTIHAN_ROOTS, src, wc)
    t_hist_n, _, t_hist_rate = density(TARGET, HIST_ROOTS, src, wc)
    r_imt_n, r_wc, r_imt_rate = density(NON_EXCEPTION_ALM, IMTIHAN_ROOTS, src, wc)
    r_hist_n, _, r_hist_rate = density(NON_EXCEPTION_ALM, HIST_ROOTS, src, wc)

    obs_imt_diff = t_imt_rate - r_imt_rate
    obs_hist_diff = t_hist_rate - r_hist_rate

    # Primary frame: enumerate all C(6,2)=15 partitions of ALM-cluster into target=2 + ref=4
    perms = list(itertools.combinations(ALM_ALL, 2))
    enum_imt_diffs = []
    enum_hist_diffs = []
    for tgt in perms:
        ref = [s for s in ALM_ALL if s not in tgt]
        _, _, t_im = density(tgt, IMTIHAN_ROOTS, src, wc)
        _, _, r_im = density(ref, IMTIHAN_ROOTS, src, wc)
        _, _, t_hi = density(tgt, HIST_ROOTS, src, wc)
        _, _, r_hi = density(ref, HIST_ROOTS, src, wc)
        enum_imt_diffs.append((tgt, t_im - r_im))
        enum_hist_diffs.append((tgt, t_hi - r_hi))

    # one-sided p (rank of observed in 15)
    sorted_imt = sorted(enum_imt_diffs, key=lambda x: -x[1])
    sorted_hist = sorted(enum_hist_diffs, key=lambda x: -x[1])
    rank_imt = next(i for i, (t, _) in enumerate(sorted_imt, 1) if set(t) == set(TARGET))
    rank_hist = next(i for i, (t, _) in enumerate(sorted_hist, 1) if set(t) == set(TARGET))
    p_one_sided_imt = rank_imt / 15
    p_one_sided_hist = rank_hist / 15

    # Secondary frame: 10000 perms drawing 2 surahs from a wider Meccan pool of moderate length
    rng = random.Random(SEED)
    all_meccan = [29, 30, 6, 7, 10, 11, 12, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 50, 51, 52, 53, 54, 56, 67, 68, 69, 70, 71, 72]
    # Filter: word_count between 200 and 1500
    candidates = [s for s in all_meccan if 200 <= wc[s] <= 1500]
    if 29 not in candidates:
        candidates.append(29)
    if 30 not in candidates:
        candidates.append(30)
    perm_imt_diffs = []
    perm_hist_diffs = []
    for _ in range(N_PERMS):
        sample = rng.sample(candidates, 2)
        rest = [s for s in NON_EXCEPTION_ALM]  # fixed reference
        _, _, t_im = density(sample, IMTIHAN_ROOTS, src, wc)
        _, _, r_im = density(rest, IMTIHAN_ROOTS, src, wc)
        _, _, t_hi = density(sample, HIST_ROOTS, src, wc)
        _, _, r_hi = density(rest, HIST_ROOTS, src, wc)
        perm_imt_diffs.append(t_im - r_im)
        perm_hist_diffs.append(t_hi - r_hi)
    p_perm_imt = sum(1 for d in perm_imt_diffs if d >= obs_imt_diff) / N_PERMS
    p_perm_hist = sum(1 for d in perm_hist_diffs if d >= obs_hist_diff) / N_PERMS

    out = {
        'finding_id': 'Q030-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perms_secondary': N_PERMS,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, hafs-kufan, basmala-counted-only-in-Q1, mashriqi)',
        'imtihan_roots': IMTIHAN_ROOTS,
        'hist_roots': HIST_ROOTS,
        'per_surah': {str(s): per_surah[s] for s in ALM_ALL},
        'observed': {
            'target_imtihan_rate_per1000': t_imt_rate * 1000,
            'target_hist_rate_per1000': t_hist_rate * 1000,
            'reference_imtihan_rate_per1000': r_imt_rate * 1000,
            'reference_hist_rate_per1000': r_hist_rate * 1000,
            'imt_diff_per1000': obs_imt_diff * 1000,
            'hist_diff_per1000': obs_hist_diff * 1000,
            'target_imt_count': t_imt_n,
            'target_hist_count': t_hist_n,
            'reference_imt_count': r_imt_n,
            'reference_hist_count': r_hist_n,
            'target_wc': t_wc,
            'reference_wc': r_wc,
        },
        'primary_enumeration_C62_15': {
            'rank_imtihan_in_15': rank_imt,
            'rank_hist_in_15': rank_hist,
            'p_one_sided_imt': p_one_sided_imt,
            'p_one_sided_hist': p_one_sided_hist,
            'partition_imt_descending': [{'target': list(t), 'diff_per1000': d * 1000} for t, d in sorted_imt],
            'partition_hist_descending': [{'target': list(t), 'diff_per1000': d * 1000} for t, d in sorted_hist],
        },
        'secondary_perm_meccan_moderate_length': {
            'candidate_pool_n': len(candidates),
            'p_perm_imt_one_sided': p_perm_imt,
            'p_perm_hist_one_sided': p_perm_hist,
        },
        'verdict_imt': (
            'PASS-DIRECTED' if rank_imt <= 1 and p_perm_imt < 0.025 else
            'DIRECTIONAL' if rank_imt <= 7 else
            'NULL'
        ),
        'verdict_hist': (
            'PASS-DIRECTED' if rank_hist <= 1 and p_perm_hist < 0.025 else
            'DIRECTIONAL' if rank_hist <= 7 else
            'NULL'
        ),
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-01 results:")
    print(f"  TARGET (Q29+30): imt/k={t_imt_rate*1000:.2f}, hist/k={t_hist_rate*1000:.2f}")
    print(f"  REF (Q2+3+31+32): imt/k={r_imt_rate*1000:.2f}, hist/k={r_hist_rate*1000:.2f}")
    print(f"  Diff: imt={obs_imt_diff*1000:+.2f}/k, hist={obs_hist_diff*1000:+.2f}/k")
    print(f"  Primary enumeration ranks: imt={rank_imt}/15 (p={p_one_sided_imt:.4f}), hist={rank_hist}/15 (p={p_one_sided_hist:.4f})")
    print(f"  Secondary perm p_imt={p_perm_imt:.4f}, p_hist={p_perm_hist:.4f}")
    print(f"  Verdicts: imt={out['verdict_imt']}, hist={out['verdict_hist']}")


if __name__ == '__main__':
    main()
