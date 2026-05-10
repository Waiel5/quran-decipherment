#!/usr/bin/env python3
"""Q028-F-06 — Q 28 al-Qaṣaṣ Mūsā-token absolute-count and density corpus rank.

Pre-reg: surahs/Q028-al-qasas/Q028-F-06-musa-density-rank-prereg.md
Pre-reg SHA256: b2c6d43332bbd81bd267d3a38d027f617d395d0e270cb6469e8b1c251cef2d03
Rules-tuple: (QAC-PN-lemma + no-tashkeel-orthographic, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260509
"""
import hashlib
import json
import re
import sys
import os
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q028-al-qasas/Q028-F-06-musa-density-rank-prereg.md'
EXPECTED_SHA = 'b2c6d43332bbd81bd267d3a38d027f617d395d0e270cb6469e8b1c251cef2d03'
SEED = 20260509
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q028-al-qasas/csv/Q028-F-06.json'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'

# Buckwalter-coded QAC lemma for Mūsā (verified via grep on QAC)
MUSA_LEMMA_RE = re.compile(r'LEM:muwsaY`')
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')

# Orthographic substring for Mūsā in no-tashkeel text
MUSA_ORTH_RE = re.compile(r'موسى')


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}",
              file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    # ---- QAC pass: per-surah Mūsā count + total STEM-token count ----
    musa_per_surah = Counter()
    stem_tokens_per_surah = Counter()
    musa_total = 0

    with open(QAC, encoding='utf-8') as f:
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
            feat = parts[3]
            if 'STEM' not in feat:
                continue
            stem_tokens_per_surah[sid] += 1
            if MUSA_LEMMA_RE.search(feat):
                musa_per_surah[sid] += 1
                musa_total += 1

    # Sanity vs H-NEW-1710: corpus total Mūsā should be 136 per QAC
    musa_corpus_total = musa_total

    # ---- Absolute-count rank ----
    sorted_by_count = sorted(((s, musa_per_surah.get(s, 0)) for s in range(1, 115)),
                             key=lambda x: -x[1])
    q28_count = musa_per_surah.get(28, 0)
    # Rank with ties: count number of surahs with strictly higher count + 1
    q28_count_rank = 1 + sum(1 for s in range(1, 115) if musa_per_surah.get(s, 0) > q28_count)
    n_ties_at_q28 = sum(1 for s in range(1, 115) if musa_per_surah.get(s, 0) == q28_count and s != 28)

    # ---- Density rank (per-1000-words) ----
    densities = []
    for s in range(1, 115):
        n_tok = stem_tokens_per_surah.get(s, 0)
        d = (musa_per_surah.get(s, 0) / n_tok * 1000.0) if n_tok else 0.0
        densities.append((s, d, musa_per_surah.get(s, 0), n_tok))
    sorted_by_density = sorted(densities, key=lambda x: -x[1])
    q28_density = next(d for s, d, _, _ in densities if s == 28)
    q28_density_rank = 1 + sum(1 for _, d, _, _ in densities if d > q28_density)

    # ---- Orthographic sensitivity check ----
    quran = json.load(open(QURAN))
    musa_orth_per_surah = Counter()
    word_count_per_surah = Counter()
    for s in quran:
        sid = s['id']
        for v in s['verses']:
            tokens = [t for t in v['text'].split()
                      if not all(c in '۞ۖۗۚ۟ۘ۠ۤۛ' for c in t)]
            word_count_per_surah[sid] += len(tokens)
            for tok in tokens:
                # substring match (covers prefixes like وموسى, لموسى)
                if MUSA_ORTH_RE.search(tok):
                    musa_orth_per_surah[sid] += 1

    q28_orth = musa_orth_per_surah.get(28, 0)
    q28_orth_rank = 1 + sum(1 for s in range(1, 115)
                            if musa_orth_per_surah.get(s, 0) > q28_orth)
    sorted_by_orth = sorted(((s, musa_orth_per_surah.get(s, 0)) for s in range(1, 115)),
                            key=lambda x: -x[1])

    # ---- Verdicts ----
    h1_pass = (q28_count_rank == 1)
    h2_pass = (q28_density_rank <= 3)
    h3_pass = (q28_count >= 20)

    if h1_pass and h2_pass and h3_pass:
        verdict = 'CONFIRMED'
    elif h1_pass or h2_pass or h3_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q028-F-06',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(QAC-PN-lemma + no-tashkeel-orthographic, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'corpus_total_musa_qac': musa_corpus_total,
        'h_new_1710_reference_value': 136,
        'q28_absolute_count_qac': q28_count,
        'q28_total_stem_tokens_qac': stem_tokens_per_surah.get(28, 0),
        'q28_musa_density_per_1000': q28_density,
        'q28_absolute_count_rank': q28_count_rank,
        'q28_ties_at_count': n_ties_at_q28,
        'q28_density_rank': q28_density_rank,
        'q28_orthographic_count': q28_orth,
        'q28_orthographic_rank': q28_orth_rank,
        'top_10_by_qac_count': [{'sid': s, 'musa_count': c} for s, c in sorted_by_count[:10]],
        'top_10_by_density': [{'sid': s, 'density_per_1000': round(d, 3),
                                'musa_count': c, 'n_stem_tokens': n}
                               for s, d, c, n in sorted_by_density[:10]],
        'top_10_by_orthographic_count': [{'sid': s, 'musa_orth_count': c}
                                          for s, c in sorted_by_orth[:10]],
        'h1_absolute_rank_1': h1_pass,
        'h2_density_top_3': h2_pass,
        'h3_count_ge_20': h3_pass,
        'verdict': verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, 'w'), indent=2, ensure_ascii=False)

    print(f"Q028-F-06 verdict: {verdict}")
    print(f"  corpus Mūsā count (QAC): {musa_corpus_total} (H-NEW-1710 ref: 136)")
    print(f"  Q 28 absolute count: {q28_count} (rank {q28_count_rank}/114; H1 pass={h1_pass})")
    print(f"  Q 28 density per 1000 stem tokens: {q28_density:.2f} (rank {q28_density_rank}/114; H2 pass={h2_pass})")
    print(f"  Q 28 orthographic substring count: {q28_orth} (rank {q28_orth_rank}/114)")
    print(f"  H3 count >= 20: pass={h3_pass}")
    print(f"  top-5 by QAC count: {[(s, c) for s, c in sorted_by_count[:5]]}")
    print(f"  top-5 by density:   {[(s, round(d,2)) for s, d, _, _ in sorted_by_density[:5]]}")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
