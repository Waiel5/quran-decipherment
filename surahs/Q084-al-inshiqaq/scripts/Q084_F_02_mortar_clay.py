#!/usr/bin/env python3
"""
Q084-F-02 — Q 84:6 root k-d-ḥ rarity audit.

Hypothesis: The root k-d-ḥ (كدح) is corpus-RARE and clusters in Q 84:6 only.
The Q 84:6 verse 'innaka kādiḥun ilā rabbika kadḥan fa-mulāqīh' contains
both surface forms (active participle kādiḥ + verbal-noun kadḥ) in
mafʿūl-muṭlaq construction — a corpus-EXACT rhetorical bigram.

Pre-reg locked: see preregs/Q084-F-02-mortar-and-clay-verse-prereg.md
Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import os
import re
import unicodedata

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q084-al-inshiqaq/csv/Q084-F-02.json')


def strip_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize(s):
    s = strip_diacritics(s)
    s = re.sub(r'[إأآٱ]', 'ا', s)
    # collapse alif-maqsura → yaa (NB: this preserves the FORM but loses
    # alif-maqsura distinction; for k-d-ḥ root this is OK because the
    # surface forms are kādiḥ and kadḥ — no maqsura)
    s = re.sub(r'[۩ۖۗۚۛۘۙۜۤ]', '', s)
    return s.strip()


def main():
    print("=== Q084-F-02: Root k-d-ḥ corpus-rarity audit ===\n")
    out = {
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pre_reg_finding_id': 'Q084-F-02',
    }

    data = json.load(open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')))

    # Corpus-wide search for k-d-ḥ surface forms
    # Surface forms of k-d-ḥ root in Arabic:
    # - kādiḥ (active participle): كادح, كادحٌ, كادحون, كادحين, كادحه, etc.
    # - kadḥ (verbal noun): كدح, كدحا (acc.), كدحه, كدحان, etc.
    # Substring search anchored on the consonant root sequence
    pat = re.compile(r'[^\s]*ك[اا]?دح[^\s]*|[^\s]*كد[ح]ا?[^\s]*')
    # Simpler: any orthographic token containing the consonant sequence k-d-ḥ
    # (with optional vowel-letter alif between k-d for the active-participle form)

    print("[1] Corpus-wide root k-d-ḥ search")
    hits = []
    for s in data:
        for v in s['verses']:
            norm = normalize(v['text'])
            tokens = norm.split()
            for tok in tokens:
                # Active participle form: kādiḥ → starts with كاد
                # Verbal noun: kadḥ → starts with كد + ح
                if (re.search(r'^كادح', tok) or
                        re.search(r'^كدح', tok) or
                        re.search(r'كادح', tok) or
                        re.search(r'كدح$', tok) or
                        re.search(r'كدحا$', tok)):
                    hits.append({
                        'surah': s['id'],
                        'verse': v['id'],
                        'token': tok,
                        'verse_text': v['text'],
                    })
    out['hits'] = hits
    out['n_hits'] = len(hits)
    print(f"  Total surface-form hits: {len(hits)}")
    for h in hits:
        print(f"  Q {h['surah']}:{h['verse']} | token: '{h['token']}' | verse: '{h['verse_text']}'")

    distinct_verses = sorted(set((h['surah'], h['verse']) for h in hits))
    distinct_surahs = sorted(set(h['surah'] for h in hits))
    out['n_distinct_verses'] = len(distinct_verses)
    out['n_distinct_surahs'] = len(distinct_surahs)
    out['distinct_verses'] = distinct_verses
    out['distinct_surahs'] = distinct_surahs
    print(f"\n[2] Distinct verses: {distinct_verses}")
    print(f"    Distinct surahs: {distinct_surahs}")

    # Verify Q 84:6 contains BOTH forms (kādiḥ + kadḥ) — the mafʿūl-muṭlaq bigram
    q84_v6_hits = [h for h in hits if h['surah'] == 84 and h['verse'] == 6]
    out['Q84_v6_hits'] = q84_v6_hits
    forms_in_v6 = set(h['token'] for h in q84_v6_hits)
    print(f"\n[3] Q 84:6 distinct forms: {forms_in_v6}")

    # Test for the bigram (active participle + verbal noun in same verse)
    # active ptc starts with كاد ; verbal noun starts with كد (no alif)
    has_active = any(t.startswith('كادح') for t in forms_in_v6)
    has_vn = any(t.startswith('كدح') and not t.startswith('كادح') for t in forms_in_v6)
    out['Q84_v6_has_active_participle'] = has_active
    out['Q84_v6_has_verbal_noun'] = has_vn
    out['Q84_v6_has_mafol_mutlaq_bigram'] = has_active and has_vn
    print(f"  Has active participle (kādiḥ): {has_active}")
    print(f"  Has verbal noun (kadḥ): {has_vn}")
    print(f"  Has mafʿūl-muṭlaq bigram: {has_active and has_vn}")

    # VERDICT
    print("\n[4] VERDICT")
    if (out['n_distinct_verses'] == 1
            and distinct_verses[0] == (84, 6)
            and out['Q84_v6_has_mafol_mutlaq_bigram']):
        verdict = ('CONFIRMED — Root k-d-ḥ is corpus-EXACT to Q 84:6 (1 verse, '
                   '2 surface forms in mafʿūl-muṭlaq construction). The verse '
                   '"innaka kādiḥun ilā rabbika kadḥan fa-mulāqīh" contains BOTH '
                   'attested forms of the root in the entire Quran corpus. '
                   'Q 84:6 is the corpus-anchor verse for this root.')
    elif out['n_distinct_verses'] <= 3 and 84 in distinct_surahs:
        verdict = (f'DIRECTIONAL-RARE — Root k-d-ḥ in {len(distinct_verses)} verses '
                   f'across surahs {distinct_surahs}; Q 84 holds the bigram.')
    else:
        verdict = (f'NULL on uniqueness — Root in {len(distinct_verses)} verses '
                   f'across {len(distinct_surahs)} surahs; not Q 84-exclusive.')
    out['verdict'] = verdict
    print(f"  {verdict}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nWrote: {OUT}")


if __name__ == '__main__':
    main()
