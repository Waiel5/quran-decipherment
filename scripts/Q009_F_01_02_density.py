#!/usr/bin/env python3
"""Q009-F-01 + Q009-F-02 — root-density audits for Q9.

F-01: rHm (mercy) density rank for Q9.
F-02: nfq (hypocrisy) density rank for Q9; cross-ref with kfr.

Pre-reg SHAs:
  F-01: edb931a1294429b216bd18332d59c4c42189cda6bc2d09a192e5ce403b01ec62
  F-02: 980b8caa77bf0778318aa51bb09250c1780adaeb313fef5c9e59bba3d4a83b40
"""
import json
import hashlib
import sys
import collections
import statistics
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')

PREREG_F01 = ROOT / 'surahs/Q009-al-tawba/Q009-F-01-mercy-density-prereg.md'
PREREG_F02 = ROOT / 'surahs/Q009-al-tawba/Q009-F-02-hypocrite-density-prereg.md'
EXPECTED_SHA_F01 = 'edb931a1294429b216bd18332d59c4c42189cda6bc2d09a192e5ce403b01ec62'
EXPECTED_SHA_F02 = '980b8caa77bf0778318aa51bb09250c1780adaeb313fef5c9e59bba3d4a83b40'


def verify_sha(path, expected):
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != expected:
        print(f'PRE-COMMIT VIOLATION: {path.name} sha={h} != expected={expected}')
        sys.exit(1)
    print(f'pre-reg sha verified: {path.name}')


def per_surah_count(ri, root):
    c = collections.Counter()
    for a in ri.get(root, []):
        s = a[0] if isinstance(a, list) else (a.get('surah') if isinstance(a, dict) else int(str(a).split(':')[0]))
        c[s] += 1
    return c


def main():
    verify_sha(PREREG_F01, EXPECTED_SHA_F01)
    verify_sha(PREREG_F02, EXPECTED_SHA_F02)

    qd = json.load(open(ROOT / 'quran-text/quran-no-tashkeel.json'))
    ri = json.load(open(ROOT / 'data/morphology/root-index.json'))
    surah_wcount = {}
    for s in qd:
        txt = ' '.join(v['text'] for v in s['verses'])
        surah_wcount[s['id']] = len(txt.split())
    assert surah_wcount[9] == 2674

    out = {
        'finding_ids': ['Q009-F-01', 'Q009-F-02'],
        'prereg_sha_F01': EXPECTED_SHA_F01,
        'prereg_sha_F02': EXPECTED_SHA_F02,
        'rules_tuple': {
            'corpus': 'quran-text/quran-no-tashkeel.json (Hafs, no-tashkeel)',
            'tokens': 'orthographic-word, whitespace-split',
            'root_index': 'data/morphology/root-index.json (QAC v0.4)',
        },
        'q9_word_count': surah_wcount[9],
        'corpus_word_count': sum(surah_wcount.values()),
        'roots_tested': {},
    }

    roots = {
        'rHm': 'mercy (r-ḥ-m)',
        'nfq': 'hypocrisy (n-f-q)',
        'twb': 'repentance (t-w-b)',
        'kfr': 'disbelief (k-f-r)',
        '$rk': 'shirk',
        'jhd': 'striving (j-h-d)',
        'Hrm': 'sanctify (ḥ-r-m)',
    }

    for r, name in roots.items():
        cnt = per_surah_count(ri, r)
        densities = []
        for sid in range(1, 115):
            d = 1000.0 * cnt.get(sid, 0) / surah_wcount[sid]
            densities.append({'surah': sid, 'density_per_1k': d, 'count': cnt.get(sid, 0)})
        sorted_desc = sorted(densities, key=lambda x: -x['density_per_1k'])
        # rank
        for i, e in enumerate(sorted_desc, 1):
            e['rank_from_top'] = i
        # Q9 entry
        q9 = next(e for e in sorted_desc if e['surah'] == 9)
        all_d = [e['density_per_1k'] for e in densities]
        out['roots_tested'][r] = {
            'name': name,
            'q9_count': q9['count'],
            'q9_density_per_1k': q9['density_per_1k'],
            'q9_rank_from_top': q9['rank_from_top'],
            'q9_percentile_from_top': 100.0 * q9['rank_from_top'] / 114,
            'corpus_mean_density': statistics.mean(all_d),
            'corpus_median_density': statistics.median(all_d),
            'corpus_stdev_density': statistics.stdev(all_d),
            'top_5_surahs': [(e['surah'], round(e['density_per_1k'], 3), e['count']) for e in sorted_desc[:5]],
            'bottom_5_surahs': [(e['surah'], round(e['density_per_1k'], 3), e['count']) for e in sorted_desc[-5:]],
        }

    # F-01 verdict
    rhm = out['roots_tested']['rHm']
    if rhm['q9_rank_from_top'] >= 87:
        v01 = 'VINDICATED'
    elif rhm['q9_rank_from_top'] <= 28:
        v01 = 'DIRECTIONAL_VIOLATION_no_basmala_no_mercy_FALSIFIED'
    else:
        v01 = 'NULL'
    out['F01_verdict'] = v01
    out['F01_verdict_rationale'] = (
        f'Q9 rHm density rank {rhm["q9_rank_from_top"]}/114 (count={rhm["q9_count"]}, '
        f'density={rhm["q9_density_per_1k"]:.3f}/1k vs corpus mean {rhm["corpus_mean_density"]:.3f}). '
        f'Pre-commit threshold: VINDICATED if rank >= 87; FALSIFIED if rank <= 28; NULL otherwise.'
    )

    # F-02 verdict
    nfq = out['roots_tested']['nfq']
    if nfq['q9_rank_from_top'] <= 12:
        v02 = 'VINDICATED'
    elif nfq['q9_rank_from_top'] <= 28:
        v02 = 'DIRECTIONAL'
    else:
        v02 = 'FALSIFIED'
    out['F02_verdict'] = v02
    out['F02_verdict_rationale'] = (
        f'Q9 nfq density rank {nfq["q9_rank_from_top"]}/114 (count={nfq["q9_count"]}, '
        f'density={nfq["q9_density_per_1k"]:.3f}/1k vs corpus mean {nfq["corpus_mean_density"]:.3f}).'
    )
    # F-02 differential: nfq rank vs kfr rank
    kfr = out['roots_tested']['kfr']
    out['F02_differential_nfq_vs_kfr'] = {
        'q9_nfq_rank': nfq['q9_rank_from_top'],
        'q9_kfr_rank': kfr['q9_rank_from_top'],
        'difference': nfq['q9_rank_from_top'] - kfr['q9_rank_from_top'],
        'interpretation': (
            'NEGATIVE means Q9 is more distinctive in hypocrisy than in disbelief, '
            'supporting the al-Faḍiḥa claim specifically (vs general anti-disbelief).'
        ),
    }

    out_path = ROOT / 'surahs/Q009-al-tawba/csv/Q009-F-01-02-density-results.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f'wrote {out_path}')
    print()
    print(f'F-01 (mercy/rHm): {v01}')
    print(f'  Q9 rank {rhm["q9_rank_from_top"]}/114, density {rhm["q9_density_per_1k"]:.3f}/1k '
          f'(corpus mean {rhm["corpus_mean_density"]:.3f}, median {rhm["corpus_median_density"]:.3f})')
    print()
    print(f'F-02 (hypocrisy/nfq): {v02}')
    print(f'  Q9 rank {nfq["q9_rank_from_top"]}/114, density {nfq["q9_density_per_1k"]:.3f}/1k '
          f'(corpus mean {nfq["corpus_mean_density"]:.3f}, median {nfq["corpus_median_density"]:.3f})')
    print(f'  Differential nfq-rank minus kfr-rank: {out["F02_differential_nfq_vs_kfr"]["difference"]}')
    print()
    for r in ['twb', '$rk', 'jhd', 'Hrm']:
        e = out['roots_tested'][r]
        print(f'  Auxiliary: {r} ({e["name"]}) Q9 rank {e["q9_rank_from_top"]}/114, '
              f'density {e["q9_density_per_1k"]:.3f}/1k')


if __name__ == '__main__':
    main()
