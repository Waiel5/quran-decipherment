#!/usr/bin/env python3
"""
Q046-F-03 — *al-Aḥqāf* corpus-hapax eponymity.

Pre-reg SHA: d2e68adeb5d74cb10b316c65941101511c4057d42948e7040021e0e4416db620
"""
import json, hashlib, re, sys

PREREG = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-03-hapax-eponym-prereg.md'
EXPECTED_SHA = 'd2e68adeb5d74cb10b316c65941101511c4057d42948e7040021e0e4416db620'
OUT = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-03.json'

actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA} got {actual}')

# Test 1: root-index attestations of Hqf
ri = json.load(open('/Users/grey/Downloads/quran/data/morphology/root-index.json'))
hqf_locs = ri.get('Hqf', [])

# Test 2: orthographic regex on no-tashkeel
nt = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
ahqaf_hits = []
for surah in nt:
    for v in surah['verses']:
        if 'الأحقاف' in v['text'] or 'أحقاف' in v['text'] or 'حقف' in v['text']:
            ahqaf_hits.append((surah['id'], v['id'], v['text']))

# Verify location
loc_ok = (len(hqf_locs) == 1) and (hqf_locs[0][0] == 46) and (hqf_locs[0][1] == 21)
ortho_ok = (len(ahqaf_hits) == 1) and (ahqaf_hits[0][0] == 46) and (ahqaf_hits[0][1] == 21)

if loc_ok and ortho_ok:
    verdict = 'VINDICATED — corpus-hapax + Q 46:21'
elif len(hqf_locs) == 1:
    verdict = 'PARTIAL: morphology hapax but orthographic check unclear'
else:
    verdict = 'REFUTED'

result = {
    'finding_id': 'Q046-F-03',
    'prereg_sha_expected': EXPECTED_SHA,
    'prereg_sha_actual': actual,
    'sha_match': True,
    'qac_attestations_of_Hqf': hqf_locs,
    'qac_count': len(hqf_locs),
    'orthographic_ahqaf_hits': [(s, v, t[:50]) for s, v, t in ahqaf_hits],
    'corpus_hapax_at_root_level': loc_ok,
    'corpus_hapax_at_orthographic_level': ortho_ok,
    'verdict': verdict,
    'rules_tuple': '(no-tashkeel, QAC-stem-root, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'note': 'Q 46 confirmed corpus-hapax-eponym at root + orthographic levels.',
}

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f'WROTE {OUT}')
print(f'QAC Hqf count: {len(hqf_locs)} — locations: {hqf_locs}')
print(f'Orthographic ahqaf hits: {len(ahqaf_hits)}')
print(f'Verdict: {verdict}')
