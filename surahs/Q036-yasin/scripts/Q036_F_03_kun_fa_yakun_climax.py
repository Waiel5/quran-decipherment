#!/usr/bin/env python3
"""
Q036-F-03 — Q 36:82 *kun-fa-yakūn* climax-position uniqueness.

Pre-reg SHA-256:
    1575bf3f4bd165b2f3148a7cf27792fbdaa9fee8d71bc8f6b447ec318b821150
"""

import hashlib
import json
import os
import re
import sys

PROJECT = '/Users/grey/Downloads/quran'

PREREG_PATH = os.path.join(PROJECT, 'surahs/Q036-yasin/preregs/Q036-F-03-kun-fa-yakun-climax-position-prereg.md')
PREREG_SHA_EXPECTED = '1575bf3f4bd165b2f3148a7cf27792fbdaa9fee8d71bc8f6b447ec318b821150'


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != PREREG_SHA_EXPECTED:
        print(f"PRE-REG SHA MISMATCH: expected {PREREG_SHA_EXPECTED}, got {h}", file=sys.stderr)
        sys.exit(1)
    return h


def main():
    sha = verify_prereg_sha()
    print(f"pre-reg SHA verified: {sha[:12]}...")

    # Load Quran no-tashkeel
    with open(os.path.join(PROJECT, 'quran-text/quran-no-tashkeel.json')) as f:
        qd = json.load(f)

    pat = re.compile(r'كن فيكون')
    locations = []
    for s in qd:
        sid = s['id']
        nv = s['total_verses']
        for v in s['verses']:
            if pat.search(v['text']):
                pos = v['id'] / nv
                locations.append({
                    'surah': sid,
                    'verse': v['id'],
                    'total_verses': nv,
                    'position_in_surah': round(pos, 4),
                    'position_pct': round(pos * 100, 2),
                })

    # Cross-validate against min-tashkeel
    with open(os.path.join(PROJECT, 'quran-text/quran-min-tashkeel.json')) as f:
        qd_min = json.load(f)
    pat_min = re.compile(r'كَن? فَيَكُون|كن فيكون')  # tolerant
    min_locations = []
    for s in qd_min:
        sid = s['id']
        nv = s['total_verses']
        for v in s['verses']:
            txt = v['text']
            # tolerate min-tashkeel marks: strip combining marks for match
            stripped = re.sub(r'[ً-ْٰٓ-ٟ]', '', txt)
            if 'كن فيكون' in stripped:
                min_locations.append({
                    'surah': sid, 'verse': v['id'], 'total_verses': nv,
                    'position_pct': round(v['id'] / nv * 100, 2),
                })

    cross_validated = (
        len(locations) == len(min_locations)
        and all(a['surah'] == b['surah'] and a['verse'] == b['verse']
                for a, b in zip(locations, min_locations))
    )

    # Tests
    q36_82 = next((loc for loc in locations if loc['surah'] == 36 and loc['verse'] == 82), None)
    others = [loc for loc in locations if not (loc['surah'] == 36 and loc['verse'] == 82)]
    other_max_pos = max(loc['position_pct'] for loc in others) if others else 0.0

    cond_1 = q36_82 is not None and q36_82['position_pct'] > 95.0
    cond_2 = other_max_pos < 90.0
    cond_3 = q36_82 is not None and (q36_82['position_pct'] - other_max_pos) >= 10.0

    n_pass = sum([cond_1, cond_2, cond_3])
    if n_pass == 3:
        verdict = 'CONFIRMED'
    elif n_pass == 2:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q036-F-03',
        'pre_reg_sha256': sha,
        'rules_tuple': '(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)',
        'corpus_kun_fayakun_count': len(locations),
        'locations': locations,
        'q36_82_position_pct': q36_82['position_pct'] if q36_82 else None,
        'other_max_position_pct': other_max_pos,
        'gap_pp': (q36_82['position_pct'] - other_max_pos) if q36_82 else None,
        'cross_validated_min_tashkeel': cross_validated,
        'cond_1_q36_above_95': cond_1,
        'cond_2_others_below_90': cond_2,
        'cond_3_gap_at_least_10pp': cond_3,
        'n_pass': n_pass,
        'verdict': verdict,
    }
    out_path = os.path.join(PROJECT, 'surahs/Q036-yasin/csv/Q036-F-03.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"wrote {out_path}")
    print(f"corpus instances: {len(locations)}")
    for loc in locations:
        print(f"  Q{loc['surah']}:{loc['verse']} of {loc['total_verses']} = {loc['position_pct']}%")
    print(f"Q 36:82 = {q36_82['position_pct'] if q36_82 else 'NOT FOUND'}%, others max = {other_max_pos}%")
    print(f"gap: {(q36_82['position_pct'] - other_max_pos) if q36_82 else 'N/A'} pp")
    print(f"verdict: {verdict}")


if __name__ == '__main__':
    main()
