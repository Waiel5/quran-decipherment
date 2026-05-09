#!/usr/bin/env python3
"""Q067-F-07 — mulk-stem density rank across 114 surahs.

Reports rank of Q 67 by per-1000-root-token density of the QAC stem-root mlk,
plus full rank table.

Pre-reg: surahs/Q067-al-mulk/preregs/Q067-F-07-mulk-root-density-rank-prereg.md
Pre-reg SHA256: 61ded14703d78a04d1277970f909aedd263065a98ff9d22d264b97c97c5630e8
Seed: 20260509
"""
import json
import hashlib
import sys
import re
from collections import Counter, defaultdict

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-07-mulk-root-density-rank-prereg.md'
EXPECTED_SHA = '61ded14703d78a04d1277970f909aedd263065a98ff9d22d264b97c97c5630e8'
QAC_PATH = f'{PROJECT}/data/morphology/quranic-corpus-morphology-0.4.txt'
OUT_PATH = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-07.json'

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f'PRE-REG SHA MISMATCH:\n  expected {EXPECTED_SHA}\n  actual   {actual}', file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    target_root = 'mlk'

    # Per-surah STEM-roots
    counts = defaultdict(Counter)
    total_per_surah = Counter()
    corpus_total_root_tokens = 0
    corpus_target_total = 0
    with open(QAC_PATH, encoding='utf-8') as f:
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
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            counts[sid][root] += 1
            total_per_surah[sid] += 1
            corpus_total_root_tokens += 1
            if root == target_root:
                corpus_target_total += 1

    # Build per-surah summary
    records = []
    for sid in range(1, 115):
        cnt = counts[sid].get(target_root, 0)
        n_tok = total_per_surah[sid]
        density = (cnt / n_tok * 1000) if n_tok else 0.0
        records.append({
            'surah': sid,
            'mlk_count': cnt,
            'total_stem_root_tokens': n_tok,
            'density_per_1000': round(density, 4),
        })

    # Rank by density
    sorted_density = sorted(records, key=lambda r: -r['density_per_1000'])
    rank_density_map = {r['surah']: i + 1 for i, r in enumerate(sorted_density)}
    # Rank by raw count
    sorted_count = sorted(records, key=lambda r: -r['mlk_count'])
    rank_count_map = {r['surah']: i + 1 for i, r in enumerate(sorted_count)}

    q67_rank_density = rank_density_map[67]
    q67_rank_count = rank_count_map[67]
    passes_top5 = q67_rank_density <= 5

    if passes_top5:
        verdict = 'PASS-DIRECTED'
        interpretation = (
            f'Q 67 ranks {q67_rank_density}/114 by mlk-density (top-5 pre-registered threshold met). '
            f'Name-tracks-density holds for Q 67 by rank.'
        )
    else:
        verdict = 'NULL'
        interpretation = (
            f'Q 67 ranks {q67_rank_density}/114 by mlk-stem-density (>5). '
            f'Pre-registered top-5 direction NOT met. Q 67 has 1 mlk-stem-token across 30 verses, '
            f'density ≈ {records[66]["density_per_1000"]:.2f}/1000 — middle of corpus. '
            f'The name "al-Mulk" follows the OPENING-WORD convention (Q 67:1 *bi-yadihi al-mulk*), '
            f'not a thematic lexical-density concentration. This complements Q067-F-04 NULL.'
        )

    out = {
        'finding_id': 'Q067-F-07',
        'pre_reg_sha256': EXPECTED_SHA,
        'target_root': target_root,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, density-per-root-token, Hafs-Kufan)',
        'corpus_total_stem_root_tokens': corpus_total_root_tokens,
        'corpus_mlk_total': corpus_target_total,
        'q67_mlk_count': records[66]['mlk_count'],
        'q67_total_stem_root_tokens': records[66]['total_stem_root_tokens'],
        'q67_density_per_1000': records[66]['density_per_1000'],
        'q67_rank_density': q67_rank_density,
        'q67_rank_count': q67_rank_count,
        'passes_top5_density': passes_top5,
        'top10_by_density': sorted_density[:10],
        'top10_by_raw_count': sorted_count[:10],
        'verdict': verdict,
        'interpretation': interpretation,
        'companion_finding': 'Q067-F-04 (hypergeometric over-concentration NULL p=0.58)',
    }

    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f'Q067-F-07: VERDICT={verdict}')
    print(f'  Q 67 mlk-count: {records[66]["mlk_count"]}; density per 1000: {records[66]["density_per_1000"]:.4f}')
    print(f'  Q 67 rank by density: {q67_rank_density}/114 (pre-reg threshold ≤ 5)')
    print(f'  Q 67 rank by raw count: {q67_rank_count}/114')
    print(f'  Top-5 by density:')
    for r in sorted_density[:5]:
        print(f'    Q {r["surah"]:3d}: count={r["mlk_count"]}, density={r["density_per_1000"]:.2f}/1000')
    print(f'  Output: {OUT_PATH}')


if __name__ == '__main__':
    main()
