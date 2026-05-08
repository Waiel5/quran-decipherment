#!/usr/bin/env python3
"""
Q046-F-01 — Q 46 → Q 47 canonical-adjacency cost rank.

Pre-reg SHA: 0eafb9802f5a62a8f9704fe3fe6771ebf0c9e2037e224e9b42633fdea4e02374
File: /Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-01-boundary-cost-prereg.md
"""
import json, hashlib, sys

PREREG = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-01-boundary-cost-prereg.md'
EXPECTED_SHA = '0eafb9802f5a62a8f9704fe3fe6771ebf0c9e2037e224e9b42633fdea4e02374'
OUT = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-01.json'

actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA} got {actual}')

d720 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json'))
adj = d720['per_adjacency']
sorted_adj = sorted(adj, key=lambda x: -x['delta'])

q46_q47 = next((a for a in adj if a['pair'] == [46, 47]), None)
q45_q46 = next((a for a in adj if a['pair'] == [45, 46]), None)
rank_46_47 = sorted_adj.index(q46_q47) + 1
rank_45_46 = sorted_adj.index(q45_q46) + 1

# Verdict
threshold_top10 = 10
threshold_top25 = 25
threshold_median = 56  # of 113

if rank_46_47 <= threshold_top10:
    verdict = 'VINDICATED'
elif rank_46_47 <= threshold_top25:
    verdict = 'DIRECTIONAL VINDICATION'
elif rank_46_47 <= threshold_median:
    verdict = 'REFINED-MODERATE'
else:
    verdict = 'NULL/REFUTED'

result = {
    'finding_id': 'Q046-F-01',
    'prereg_sha_expected': EXPECTED_SHA,
    'prereg_sha_actual': actual,
    'sha_match': True,
    'q46_q47_delta': q46_q47['delta'],
    'q46_q47_rank': rank_46_47,
    'q46_q47_fraction_residual': q46_q47['fraction_residual'],
    'q45_q46_delta': q45_q46['delta'],
    'q45_q46_rank': rank_45_46,
    'q45_q46_fraction_residual': q45_q46['fraction_residual'],
    'top10_expensive_pairs': [(a['pair'], a['delta']) for a in sorted_adj[:10]],
    'pre_committed_direction': 'rank ≤ 25 (top-22%)',
    'verdict': verdict,
    'note': 'User-prompt characterised Q 46→Q 47 as HIGH cost; empirical rank refines.',
}

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f'WROTE {OUT}')
print(f'Q 46-47 rank: {rank_46_47}/113')
print(f'Q 45-46 rank: {rank_45_46}/113')
print(f'Verdict: {verdict}')
