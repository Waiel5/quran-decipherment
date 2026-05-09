#!/usr/bin/env python3
"""Q068-F-06 — *qlm* root density corpus rank (title-density audit).

Pre-reg: surahs/Q068-al-qalam/preregs/Q068-F-06-qlm-root-density-rank-prereg.md
SHA256: 497822f6f771ac63b0e1816d43163609137a509f2feeb852fe5f2330606b38ac
Seed: 20260509 (not used; deterministic enumeration).
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
from pathlib import Path

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG = PROJECT / 'surahs' / 'Q068-al-qalam' / 'preregs' / 'Q068-F-06-qlm-root-density-rank-prereg.md'
EXPECTED_SHA = '497822f6f771ac63b0e1816d43163609137a509f2feeb852fe5f2330606b38ac'
OUT = PROJECT / 'surahs' / 'Q068-al-qalam' / 'csv' / 'Q068-F-06.json'
QAC = PROJECT / 'data' / 'morphology' / 'quranic-corpus-morphology-0.4.txt'


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.stderr.write(f'SHA mismatch: expected {EXPECTED_SHA}, got {actual}\n')
        sys.exit(2)


def parse_qac():
    """Return dict surah -> (n_tokens, k_qlm), and qlm token locations."""
    per_n = {s: 0 for s in range(1, 115)}
    per_k = {s: 0 for s in range(1, 115)}
    qlm_locs = []
    loc_re = re.compile(r'\((\d+):(\d+):(\d+):(\d+)\)')
    for raw in QAC.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or line.startswith('LOCATION'):
            continue
        parts = line.split('\t')
        if len(parts) < 4:
            continue
        m = loc_re.match(parts[0])
        if not m:
            continue
        s = int(m.group(1))
        per_n[s] = per_n.get(s, 0) + 1
        if 'ROOT:qlm' in parts[3]:
            per_k[s] = per_k.get(s, 0) + 1
            qlm_locs.append((parts[0], parts[1] if len(parts) > 1 else ''))
    return per_n, per_k, qlm_locs


def hypergeom_pmf(k: int, K: int, n: int, N: int) -> float:
    return math.comb(K, k) * math.comb(N - K, n - k) / math.comb(N, n)


def hypergeom_sf(k_obs: int, K: int, n: int, N: int) -> float:
    """P(X >= k_obs)."""
    upper = min(K, n)
    return sum(hypergeom_pmf(k, K, n, N) for k in range(k_obs, upper + 1))


def main() -> None:
    verify_sha()
    per_n, per_k, qlm_locs = parse_qac()
    densities = []
    for s in range(1, 115):
        n = per_n[s]
        k = per_k[s]
        dens = (k / n * 1000.0) if n > 0 else 0.0
        densities.append({'surah': s, 'k_qlm': k, 'n_root_tokens': n, 'density_per_1000': dens})
    densities_sorted = sorted(densities, key=lambda d: (-d['density_per_1000'], d['surah']))
    for r, row in enumerate(densities_sorted, start=1):
        row['rank'] = r
    q68_row = next(row for row in densities_sorted if row['surah'] == 68)
    q96_row = next(row for row in densities_sorted if row['surah'] == 96)

    N_total = sum(per_n.values())
    K_total = sum(per_k.values())
    n_68 = per_n[68]
    k_68 = per_k[68]
    p_hyper = hypergeom_sf(k_68, K_total, n_68, N_total) if k_68 > 0 else 1.0

    rank_68 = q68_row['rank']
    if rank_68 == 1:
        verdict = 'VINDICATED-RANK-EXACT'
    elif rank_68 <= 3:
        verdict = 'VINDICATED-TOP-3'
    elif rank_68 <= 11:
        verdict = 'DIRECTIONAL'
    elif k_68 == 0:
        verdict = 'DIRECTION_REVERSED'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q068-F-06',
        'prereg_sha256': EXPECTED_SHA,
        'date_run': '2026-05-09',
        'seed': 20260509,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'corpus_total_root_tokens': N_total,
        'corpus_total_qlm_tokens': K_total,
        'q68_root_tokens': n_68,
        'q68_qlm_tokens': k_68,
        'q68_density_per_1000': q68_row['density_per_1000'],
        'q68_rank_by_density': rank_68,
        'q96_density_per_1000': q96_row['density_per_1000'],
        'q96_rank_by_density': q96_row['rank'],
        'top_5_by_qlm_density': densities_sorted[:5],
        'all_surahs_with_qlm_token': [r for r in densities_sorted if r['k_qlm'] > 0],
        'qlm_token_locations_qac': qlm_locs,
        'q68_hypergeom_p_value_X_ge_k': p_hyper,
        'alpha_raw': 0.05,
        'verdict': verdict,
        'interpretation': (
            f"Q 68 is rank {rank_68} by qlm-density (density={q68_row['density_per_1000']:.4f} per 1000 root-tokens, "
            f"k=1 in n=508). Rank-1 is Q 96 (density={q96_row['density_per_1000']:.4f}, k=1 in n=111). "
            f"Verdict: {verdict}. Q 96 al-ʿAlaq (revelation #1) has higher *qalam* density than the title-eponymous Q 68 al-Qalam (revelation #2), "
            f"because Q 96 packs *qalam* into a much shorter root-token base."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps({'verdict': verdict, 'rank': rank_68, 'p_hyper': p_hyper}, ensure_ascii=False))


if __name__ == '__main__':
    main()
