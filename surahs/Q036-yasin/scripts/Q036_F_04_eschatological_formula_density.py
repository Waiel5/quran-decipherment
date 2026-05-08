#!/usr/bin/env python3
"""
Q036-F-04 — Eschatological-formula density audit.

Pre-reg SHA-256:
    515ce2dea2c6bd07083c233b46be6554214afb620c46e64542513d8a64d386ae
"""

import hashlib
import json
import os
import random
import re
import sys

PROJECT = '/Users/grey/Downloads/quran'

PREREG_PATH = os.path.join(PROJECT, 'surahs/Q036-yasin/preregs/Q036-F-04-eschatological-formula-density-prereg.md')
PREREG_SHA_EXPECTED = '515ce2dea2c6bd07083c233b46be6554214afb620c46e64542513d8a64d386ae'

SEED = 20260428
N_PERM = 10000
ALPHA_RAW = 0.05
ALPHA_BON = 0.05 / 114


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != PREREG_SHA_EXPECTED:
        print(f"PRE-REG SHA MISMATCH: expected {PREREG_SHA_EXPECTED}, got {h}", file=sys.stderr)
        sys.exit(1)
    return h


# Locked patterns
PATTERNS = [
    re.compile(r'يوم'),
    re.compile(r'الساعة'),
    re.compile(r'الصور'),
    re.compile(r'القيامة'),
    re.compile(r'(يبعث|بعثنا|نبعث|البعث)'),
    re.compile(r'نار|النار'),
    re.compile(r'الجنة'),
    re.compile(r'الموتى|موت'),
]


def count_eschat(text):
    return sum(len(p.findall(text)) for p in PATTERNS)


def main():
    sha = verify_prereg_sha()
    print(f"pre-reg SHA verified: {sha[:12]}...")

    with open(os.path.join(PROJECT, 'quran-text/quran-no-tashkeel.json')) as f:
        qd = json.load(f)

    per_surah_counts = {}
    per_surah_words = {}
    for s in qd:
        sid = s['id']
        cnt = 0
        wc = 0
        for v in s['verses']:
            t = v['text']
            cnt += count_eschat(t)
            wc += len(t.split())
        per_surah_counts[sid] = cnt
        per_surah_words[sid] = wc

    total_count = sum(per_surah_counts.values())
    total_words = sum(per_surah_words.values())

    # Density
    density = {sid: (per_surah_counts[sid] / per_surah_words[sid] * 1000) if per_surah_words[sid] else 0.0
               for sid in per_surah_counts}

    # Rank
    ranked = sorted(density.items(), key=lambda x: -x[1])
    rank_of = {sid: i + 1 for i, (sid, _) in enumerate(ranked)}

    q36_density = density[36]
    q36_count = per_surah_counts[36]
    q36_words = per_surah_words[36]
    q36_rank = rank_of[36]

    # Per-surah hypergeometric-like permutation null
    # Null: shuffle the words-vs-eschat-count pairing across surahs
    rng = random.Random(SEED)
    null_q36_densities = []
    surahs = list(per_surah_counts.keys())
    for _ in range(N_PERM):
        # Generate a permutation: shuffle counts independently of words.
        shuffled_counts = list(per_surah_counts.values())
        rng.shuffle(shuffled_counts)
        # Find what density Q 36 would receive
        q36_idx = surahs.index(36)
        null_density = (shuffled_counts[q36_idx] / per_surah_words[36] * 1000)
        null_q36_densities.append(null_density)

    n_ge = sum(1 for d in null_q36_densities if d >= q36_density)
    p_value = (n_ge + 1) / (N_PERM + 1)

    # Top-10 + control
    top10 = ranked[:10]
    bottom5 = ranked[-5:]

    # Q 75 control
    q75_density = density[75]
    q75_rank = rank_of[75]

    # Verdict
    if q36_density < (total_count / total_words * 1000):
        verdict = 'NULL (Q 36 below corpus mean density; direction-violation)'
    elif p_value < ALPHA_BON:
        verdict = f'VINDICATED (p={p_value:.4e} < α_Bon={ALPHA_BON:.4e})'
    elif p_value < ALPHA_RAW and q36_rank <= 23:
        verdict = f'DIRECTIONAL (p={p_value:.4f}, rank {q36_rank}/114 top-quintile)'
    elif q36_rank <= 23:
        verdict = f'DIRECTIONAL (rank {q36_rank}/114 top-quintile but p={p_value:.4f} not significant)'
    else:
        verdict = f'NULL (rank {q36_rank}/114, p={p_value:.4f})'

    out = {
        'finding_id': 'Q036-F-04',
        'pre_reg_sha256': sha,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)',
        'corpus_total_eschat_count': total_count,
        'corpus_total_words': total_words,
        'corpus_mean_density_per_1000': total_count / total_words * 1000,
        'q36_eschat_count': q36_count,
        'q36_words': q36_words,
        'q36_density_per_1000': q36_density,
        'q36_rank': q36_rank,
        'q75_density_per_1000': q75_density,
        'q75_rank': q75_rank,
        'p_value_perm': p_value,
        'alpha_raw': ALPHA_RAW,
        'alpha_bonferroni': ALPHA_BON,
        'top10_by_density': [{'surah': s, 'density': d} for s, d in top10],
        'bottom5_by_density': [{'surah': s, 'density': d} for s, d in bottom5],
        'verdict': verdict,
    }

    out_path = os.path.join(PROJECT, 'surahs/Q036-yasin/csv/Q036-F-04.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"wrote {out_path}")
    print(f"Q 36 eschat density: {q36_density:.2f}/1000 (count={q36_count}, words={q36_words}); rank {q36_rank}/114")
    print(f"Corpus mean density: {total_count / total_words * 1000:.2f}/1000")
    print(f"Q 75 control density: {q75_density:.2f}/1000 (rank {q75_rank})")
    print(f"p_value (perm): {p_value:.4e}; α_Bon = {ALPHA_BON:.4e}")
    print(f"verdict: {verdict}")


if __name__ == '__main__':
    main()
