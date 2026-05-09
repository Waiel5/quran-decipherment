#!/usr/bin/env python3
"""
Q049-F-03 — Q 49 → Q 50 universal-hinge cross-feature confirmation.
Pre-reg SHA: 91106ef25902ae631c537d6e0c8299729fbf6f444a016fe7b8e5dcf20b739760
Direction: POSITIVE — Q 49 → Q 50 hypothesized in all-three-feature top-15 intersection
AND Nöldeke-chronology gap ≥ 50 positions.
Seed: 20260509  (no random component; corpus enumeration cross-tabulation).
"""

import json
import os

ROOT = '/Users/grey/Downloads/quran'
PRE_REG_SHA = '91106ef25902ae631c537d6e0c8299729fbf6f444a016fe7b8e5dcf20b739760'

# Standard al-Suyūṭī revelation-order ranks (from al-Itqān nawʿ 1, Egyptian standard)
# Q 49 al-Ḥujurāt: revelation rank ~ 106 (Medinan late phase)
# Q 50 Qāf: revelation rank ~ 34 (mid-Meccan, "second Meccan")
NOLDEKE_Q49 = 106
NOLDEKE_Q50 = 34


def in_top15(jumps_list, i, j):
    """Check if (i, j) appears in a top-15 jumps list."""
    for entry in jumps_list:
        if entry.get('i') == i and entry.get('j') == j:
            return True, entry
    return False, None


def main():
    h130 = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-130.json')))
    h130b = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-130b.json')))
    h130c = json.load(open(os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-130c.json')))

    in_root, e_root = in_top15(h130['top15_largest_jumps'], 49, 50)
    in_char, e_char = in_top15(h130b['top15_largest_jumps'], 49, 50)
    in_vlen, e_vlen = in_top15(h130c['top15_largest_jumps'], 49, 50)

    primary_pass = in_root and in_char and in_vlen

    noldeke_gap = abs(NOLDEKE_Q49 - NOLDEKE_Q50)
    secondary_pass = noldeke_gap >= 50

    if primary_pass and secondary_pass:
        verdict = 'CONFIRMED-CROSS-FEATURE'
    elif primary_pass:
        verdict = 'PASS-PRIMARY-ONLY'
    elif secondary_pass:
        verdict = 'PASS-SECONDARY-ONLY'
    else:
        verdict = 'NULL'

    result = {
        'finding_id': 'Q049-F-03',
        'pre_reg_sha256': PRE_REG_SHA,
        'seed': 20260509,
        'rules_tuple': '(QAC-v0.4-roots+char-4-gram+verse-length+Nöldeke-chronology)',
        'q49_q50_pair': [49, 50],
        'in_h130_top15_root': in_root,
        'h130_entry_root': e_root,
        'in_h130b_top15_char4gram': in_char,
        'h130b_entry_char4gram': e_char,
        'in_h130c_top15_verselen': in_vlen,
        'h130c_entry_verselen': e_vlen,
        'primary_all_three': primary_pass,
        'noldeke_q49': NOLDEKE_Q49,
        'noldeke_q50': NOLDEKE_Q50,
        'noldeke_gap_positions': noldeke_gap,
        'noldeke_gap_threshold_50': secondary_pass,
        'verdict': verdict,
        'classical_anchor': 'H-NEW-130 + H-NEW-130b + H-NEW-130c + H-NEW-142 (cross-finding-013 ring-topology); Q 49 → Q 50 is one of the THREE universal hinges (Q 14→15, Q 49→50, Q 56→57).',
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q049-al-hujurat', 'csv', 'Q049-F-03.json')
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2)

    print(f'Q049-F-03 verdict: {verdict}')
    print(f'  Q 49→Q 50 in H-NEW-130 (root)        top-15: {in_root}')
    print(f'  Q 49→Q 50 in H-NEW-130b (char-4-gram) top-15: {in_char}')
    print(f'  Q 49→Q 50 in H-NEW-130c (verse-length) top-15: {in_vlen}')
    print(f'  Primary (all-three): {primary_pass}')
    print(f'  Nöldeke gap = {noldeke_gap} positions (≥ 50 threshold: {secondary_pass})')


if __name__ == '__main__':
    main()
