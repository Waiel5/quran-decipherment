#!/usr/bin/env python3
"""
Q067-F-03 — Corpus-singleton phrase signature audit.
Tests Q67:1 *bi-yadihi al-mulk*, Q67:3 *fa-rjiʿi al-baṣar*, Q67:3 *sabʿa samāwātin ṭibāqan*.
"""
import hashlib, json, os, sys

PROJECT = '/Users/grey/Downloads/quran'
PREREG_PATH = f'{PROJECT}/surahs/Q067-al-mulk/preregs/Q067-F-03-corpus-singleton-phrases-prereg.md'
EXPECTED_SHA = '6722a3a4f9af866a759222fd0df008a94d4510a0dda7e66a189adafc2d7ff385'

with open(PREREG_PATH, 'rb') as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual_sha}')

with open(f'{PROJECT}/quran-text/quran-no-tashkeel.json') as f:
    qd = json.load(f)

mushaf_marks = ['۞', 'ۚ', 'ۖ', 'ۗ', 'ۛ', 'ۜ', '۠', '۩', 'ۭ']

phrases_to_test = {
    'A_bi_yadihi_al_mulk': {
        'arabic': 'بيده الملك',
        'predicted_count': 1,
        'predicted_locations': [(67, 1)],
        'description': 'Q67:1 *bi-yadihi al-mulk* — corpus-singleton (predicted 1)',
    },
    'B_fa_rjii_al_basar': {
        'arabic': 'فارجع البصر',
        'predicted_count': 1,
        'predicted_locations': [(67, 3)],
        'description': 'Q67:3 *fa-rjiʿi al-baṣar* — corpus-singleton (predicted 1)',
    },
    'C_sabaa_samawat_tibaqa': {
        'arabic': 'سبع سماوات طباقا',
        'predicted_count': 2,
        'predicted_locations': [(67, 3), (71, 15)],
        'description': 'Q67:3 *sabʿa samāwātin ṭibāqan* — corpus-pair (predicted 2)',
    },
}

results = {}
for key, p in phrases_to_test.items():
    arabic = p['arabic']
    found_locations = []
    for q in qd:
        for v in q['verses']:
            t = v['text']
            for m in mushaf_marks:
                t = t.replace(m, '')
            t = ' '.join(t.split())
            if arabic in t:
                found_locations.append((q['id'], v['id']))
    actual_count = len(found_locations)
    predicted = p['predicted_count']
    matches_predicted = (actual_count == predicted) and (
        sorted(found_locations) == sorted(p['predicted_locations'])
    )
    results[key] = {
        'phrase': arabic,
        'predicted_count': predicted,
        'predicted_locations': p['predicted_locations'],
        'actual_count': actual_count,
        'actual_locations': found_locations,
        'matches_predicted': matches_predicted,
        'description': p['description'],
    }

# Verdict
all_match = all(r['matches_predicted'] for r in results.values())
n_match = sum(1 for r in results.values() if r['matches_predicted'])

if all_match:
    verdict = 'CONFIRMED'
    interpretation = 'All three pre-registered phrase-uniqueness predictions match the corpus exactly.'
else:
    verdict = 'PARTIAL'
    interpretation = f'{n_match}/3 phrase-uniqueness predictions match.'

output = {
    'finding_id': 'Q067-F-03',
    'prereg_sha256': actual_sha,
    'date_run': '2026-04-28',
    'rules_tuple': '(no-tashkeel, orthographic-token, exact substring match, basmala-not-counted-in-Q67, Hafs-Kufan, mushaf-order)',
    'phrases_tested': results,
    'n_predicted_correct': n_match,
    'n_total': 3,
    'verdict': verdict,
    'interpretation': interpretation,
}

out_path = f'{PROJECT}/surahs/Q067-al-mulk/csv/Q067-F-03.json'
with open(out_path, 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f'Q067-F-03: VERDICT={verdict} ({n_match}/3 confirmed)')
for k, r in results.items():
    flag = 'OK' if r['matches_predicted'] else 'MISS'
    print(f'  [{flag}] {k}: {r["actual_count"]} (expected {r["predicted_count"]}) at {r["actual_locations"]}')
print(f'  Output: {out_path}')
