#!/usr/bin/env python3
"""
Q084-F-01 — Sajda + idhā-cosmic-event-opener double-marker corpus-uniqueness.

Hypothesis: Q 84 al-Inshiqāq is the corpus's UNIQUE surah that is BOTH
- (a) An idhā-cosmic-event-opener (5-surah Sub-cluster A: {Q 56, 81, 82, 84, 99})
- (b) A sajdat al-tilāwa surah (14-surah Sunnī list: Q 7, 13, 16, 17, 19, 22,
      25, 27, 32, 38, 41, 53, 84, 96)

Pre-reg locked: see preregs/Q084-F-01-sajda-idha-double-marker-prereg.md.
"""
import json
import os
import re

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q084-al-inshiqaq/csv/Q084-F-01.json')


def load_quran():
    p = os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')
    return json.load(open(p))


def main():
    print("=== Q084-F-01: Sajda + idhā-opener double-marker uniqueness ===\n")
    out = {
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pre_reg_finding_id': 'Q084-F-01',
        'parent_findings': ['H-NEW-1200', 'H-NEW-1330'],
    }

    # LOCKED classical sets
    idha_openers = [56, 81, 82, 84, 99]
    sajda_surahs = [7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96]
    out['idha_cosmic_opener_set'] = idha_openers
    out['sajda_surahs_set'] = sajda_surahs

    # Compute intersection
    intersection = sorted(set(idha_openers) & set(sajda_surahs))
    out['intersection'] = intersection
    out['intersection_size'] = len(intersection)
    print(f"[1] idhā-cosmic-opener set: {idha_openers}")
    print(f"    sajda surahs (Sunnī): {sajda_surahs}")
    print(f"    intersection: {intersection} (size = {len(intersection)})")

    # Verify Q 84:1 opens with "idhā al-samāʾu inshaqqat" pattern
    data = load_quran()
    q84 = next(s for s in data if s['id'] == 84)
    v1 = next(v for v in q84['verses'] if v['id'] == 1)
    v21 = next(v for v in q84['verses'] if v['id'] == 21)
    out['Q84_v1_text'] = v1['text']
    out['Q84_v21_text'] = v21['text']
    print(f"\n[2] Q 84:1 (opening): '{v1['text']}'")
    print(f"    Q 84:21 (sajda): '{v21['text']}'")

    # Idhā-opener verification (the pattern is الس/إذا+ سماء + verb)
    has_idha = bool(re.search(r'إذا\s+الس(م|ـم)اء\s+\S+', v1['text']))
    out['Q84_v1_idha_pattern'] = has_idha
    print(f"    Q 84:1 has 'idhā al-samāʾu V' pattern: {has_idha}")

    # Sajda glyph (۩) verification
    has_sajda_glyph = '۩' in v21['text']
    out['Q84_v21_has_sajda_glyph'] = has_sajda_glyph
    print(f"    Q 84:21 has sajda glyph (۩): {has_sajda_glyph}")

    # Cross-check ALL idhā-openers and ALL sajda-surahs for double-marker
    print("\n[3] Cross-check: which idhā-openers carry sajda glyph anywhere?")
    idha_with_sajda = []
    for sid in idha_openers:
        s = next(x for x in data if x['id'] == sid)
        for v in s['verses']:
            if '۩' in v['text']:
                idha_with_sajda.append({'surah': sid, 'verse': v['id'], 'text': v['text']})
                print(f"  Q {sid}:{v['id']} carries sajda glyph: '{v['text']}'")
    out['idha_openers_with_sajda_glyph'] = idha_with_sajda

    # Sajda-surahs with idhā-cosmic-event opener?
    print("\n[4] Cross-check: which sajda-surahs open with 'idhā V' cosmic-event?")
    sajda_with_idha_open = []
    for sid in sajda_surahs:
        s = next(x for x in data if x['id'] == sid)
        v1 = s['verses'][0]
        # An idhā-cosmic-opener is a v1 that begins with "idhā" + cosmic-event noun + verb
        # (loose pattern: starts with إذا followed by definite-noun + verb)
        m = re.match(r'^إذا\s+', v1['text'].strip())
        if m:
            sajda_with_idha_open.append({'surah': sid, 'v1_text': v1['text']})
            print(f"  Q {sid}:1 opens with 'idhā ...': '{v1['text']}'")
    out['sajda_surahs_with_idha_opener'] = sajda_with_idha_open

    # VERDICT
    print("\n[5] VERDICT")
    if (len(intersection) == 1 and intersection[0] == 84
            and has_idha and has_sajda_glyph):
        verdict = ('CONFIRMED — Q 84 al-Inshiqāq is the corpus-UNIQUE BIPLEX-MARKER '
                   'surah, simultaneously a member of the 5-surah idhā-cosmic-opener '
                   'set (H-NEW-1200 Sub-cluster A) AND the 14-surah Sunnī sajda set '
                   '(H-NEW-1330). Both markers are textually confirmed in the canonical '
                   'Hafs-Kufan corpus: Q 84:1 opens with "idhā al-samāʾu inshaqqat" '
                   'and Q 84:21 carries the sajda glyph (۩).')
    elif len(intersection) > 1:
        verdict = (f'NULL on uniqueness — intersection has {len(intersection)} '
                   f'members: {intersection}')
    elif 84 not in intersection:
        verdict = 'INSTRUMENT FAILURE — Q 84 not in expected intersection.'
    else:
        verdict = 'PARTIAL — set membership confirmed but textual markers missing.'
    out['verdict'] = verdict
    print(f"  {verdict}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nWrote: {OUT}")


if __name__ == '__main__':
    main()
