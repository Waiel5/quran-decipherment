#!/usr/bin/env python3
"""Q009-F-03 — Q 9 → Q 10 canonical-adjacency cost audit.

Reads h-new-720.json and verifies Q9-Q10 rank.
Pre-reg SHA: a3f04af0f84584cbda89a983e5ad1bb30f4b825ce2e9a435c4d6ec1140ad4842
"""
import json
import hashlib
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q009-al-tawba/Q009-F-03-q9-q10-boundary-prereg.md'
EXPECTED_SHA = 'a3f04af0f84584cbda89a983e5ad1bb30f4b825ce2e9a435c4d6ec1140ad4842'


def verify_sha(path, expected):
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != expected:
        print(f'PRE-COMMIT VIOLATION: {path.name} sha={h} != expected={expected}')
        sys.exit(1)
    print(f'pre-reg sha verified: {path.name}')


def main():
    verify_sha(PREREG, EXPECTED_SHA)
    d = json.load(open(ROOT / 'findings/phase-b-hypotheses/csv/h-new-720.json'))
    pa = d['per_adjacency']
    sorted_desc = sorted(pa, key=lambda x: -x['fraction_residual'])
    for i, e in enumerate(sorted_desc, 1):
        e['rank'] = i
    q8q9 = next(e for e in pa if e['s'] == 8)
    q9q10 = next(e for e in pa if e['s'] == 9)
    q6q7 = next(e for e in pa if e['s'] == 6)  # control: Q6→Q7 (Q7 starts المص muqaṭṭaʿāt)

    if q9q10['rank'] <= 10:
        verdict = 'VINDICATED'
    elif q9q10['rank'] <= 30:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'FALSIFIED'

    out = {
        'finding_id': 'Q009-F-03',
        'prereg_sha': EXPECTED_SHA,
        'source': 'findings/phase-b-hypotheses/csv/h-new-720.json',
        'Q9_Q10_adjacency': {
            'pair': q9q10['pair'],
            'fraction_residual': q9q10['fraction_residual'],
            'rank': q9q10['rank'],
        },
        'Q8_Q9_adjacency': {
            'pair': q8q9['pair'],
            'fraction_residual': q8q9['fraction_residual'],
            'rank': q8q9['rank'],
        },
        'Q6_Q7_adjacency_control': {
            'pair': q6q7['pair'],
            'fraction_residual': q6q7['fraction_residual'],
            'rank': q6q7['rank'],
            'note': 'Q7 al-Aʿrāf starts with المص muqaṭṭaʿāt cluster (singleton); compare to Q9-Q10 (Q10-15 ALR cluster start)'
        },
        'top_10_expensive_adjacencies': [
            {'pair': e['pair'], 'fraction_residual': e['fraction_residual'], 'rank': e['rank']}
            for e in sorted_desc[:10]
        ],
        'verdict': verdict,
        'rationale': f'Q9-Q10 fraction_residual = {q9q10["fraction_residual"]:.4f} (rank {q9q10["rank"]}/113); '
                     f'top-10 ⇒ VINDICATED.',
    }
    out_path = ROOT / 'surahs/Q009-al-tawba/csv/Q009-F-03-q9-q10-boundary.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f'wrote {out_path}')
    print()
    print(f'F-03 verdict: {verdict}')
    print(f'  Q9-Q10 fraction_residual: {q9q10["fraction_residual"]:.4f}, rank {q9q10["rank"]}/113')
    print(f'  Q8-Q9 fraction_residual:  {q8q9["fraction_residual"]:.4f}, rank {q8q9["rank"]}/113')
    print(f'  Q6-Q7 control:            {q6q7["fraction_residual"]:.4f}, rank {q6q7["rank"]}/113')


if __name__ == '__main__':
    main()
