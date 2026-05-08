#!/usr/bin/env python3
"""
Q046-F-04 — Q 45→Q 46 (internal HM-B) vs Q 46→Q 47 (HM exit) cost asymmetry.

Pre-reg SHA: 71c8d4f6467612d5d51a1713fdd9c732f82bcf78caae2ca47d9e0efceef5e7ef
"""
import json, hashlib, sys

PREREG = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-04-internal-vs-exit-prereg.md'
EXPECTED_SHA = '71c8d4f6467612d5d51a1713fdd9c732f82bcf78caae2ca47d9e0efceef5e7ef'
OUT = '/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-04.json'

actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
if actual != EXPECTED_SHA:
    sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA} got {actual}')

d720 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json'))
adj = d720['per_adjacency']
sorted_adj = sorted(adj, key=lambda x: -x['delta'])

q45_q46 = next(a for a in adj if a['pair'] == [45, 46])
q46_q47 = next(a for a in adj if a['pair'] == [46, 47])

ratio = q45_q46['delta'] / q46_q47['delta']
margin_pct = (q45_q46['delta'] - q46_q47['delta']) / q46_q47['delta'] * 100

if q45_q46['delta'] > q46_q47['delta']:
    if margin_pct >= 5.0:
        verdict = 'VINDICATED — internal > exit by ≥5%'
    else:
        verdict = 'DIRECTIONAL — internal > exit but margin <5%'
else:
    verdict = 'NULL with pre-commit violation: exit ≥ internal'

result = {
    'finding_id': 'Q046-F-04',
    'prereg_sha_expected': EXPECTED_SHA,
    'prereg_sha_actual': actual,
    'sha_match': True,
    'q45_q46_delta': q45_q46['delta'],
    'q45_q46_rank': sorted_adj.index(q45_q46) + 1,
    'q46_q47_delta': q46_q47['delta'],
    'q46_q47_rank': sorted_adj.index(q46_q47) + 1,
    'ratio_internal_to_exit': ratio,
    'margin_pct': margin_pct,
    'verdict': verdict,
    'note': 'Counter-intuitive if vindicated: HM-B internal step costs more than HM exit.',
}

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
print(f'WROTE {OUT}')
print(f'Q 45→46 delta: {q45_q46["delta"]:.4f} (rank {sorted_adj.index(q45_q46)+1})')
print(f'Q 46→47 delta: {q46_q47["delta"]:.4f} (rank {sorted_adj.index(q46_q47)+1})')
print(f'Ratio: {ratio:.3f}; margin: {margin_pct:.1f}%')
print(f'Verdict: {verdict}')
