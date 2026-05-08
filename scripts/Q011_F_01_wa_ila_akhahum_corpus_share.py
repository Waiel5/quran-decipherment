#!/usr/bin/env python3
"""Q011-F-01 — wa-ilā-[TRIBE]-akhāhum-[PROPHET] corpus-share.

Pre-reg: surahs/Q011-hud/preregs/Q011-F-01-wa-ila-akhahum-corpus-share-prereg.md
Pre-reg SHA256: e795ac43090f93dfd06a6403a86d333552000d58c1b03c20d9000d9f26da16cf
Rules-tuple: (no-tashkeel, orthographic-token, exact-string-match,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
Seed: 20260507
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q011-hud/preregs/Q011-F-01-wa-ila-akhahum-corpus-share-prereg.md'
EXPECTED_SHA = 'e795ac43090f93dfd06a6403a86d333552000d58c1b03c20d9000d9f26da16cf'

TRIBES = ['عاد', 'ثمود', 'مدين']
PROPHETS = ['هودا', 'صالحا', 'شعيبا']
WA_ILA = 'وإلى'
AKHAHUM = 'أخاهم'

# Punctuation marks that mark token-boundaries in our corpus text
PUNCT_PATTERN = re.compile(r'[\s۞ۚۗۖۘۙ]+')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def tokenize(text):
    return [t for t in PUNCT_PATTERN.split(text) if t]


def find_matches(tokens):
    """Yield (i, tribe, prophet) where tokens[i:i+4] == [WA_ILA, TRIBE, AKHAHUM, PROPHET]."""
    matches = []
    for i in range(len(tokens) - 3):
        if (tokens[i] == WA_ILA and
            tokens[i+1] in TRIBES and
            tokens[i+2] == AKHAHUM and
            tokens[i+3] in PROPHETS):
            matches.append((i, tokens[i+1], tokens[i+3]))
    return matches


def main():
    verify_sha()
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        d = json.load(f)
    per_surah = {}
    all_matches = []
    for s in d:
        sid = s['id']
        verse_matches = []
        for v in s['verses']:
            vid = v['id']
            toks = tokenize(v['text'])
            ms = find_matches(toks)
            if ms:
                for (idx, tribe, prophet) in ms:
                    verse_matches.append({
                        'verse': f'{sid}:{vid}',
                        'tribe': tribe,
                        'prophet': prophet,
                        'token_index': idx,
                        'verse_text': v['text'][:200],
                    })
        if verse_matches:
            per_surah[sid] = verse_matches
            all_matches.extend(verse_matches)
    # Per-surah unique-verse counts
    surah_counts = {}
    for sid, ms in per_surah.items():
        verses = set(m['verse'] for m in ms)
        surah_counts[sid] = len(verses)
    total = sum(surah_counts.values())
    q11_count = surah_counts.get(11, 0)
    q11_share = q11_count / total if total else 0
    # Verdict
    if q11_count >= 3 and q11_share >= 0.5:
        verdict = 'CONFIRMED'
    elif q11_count >= 3 and 1/3 <= q11_share < 0.5:
        verdict = 'DIRECTIONAL'
    elif q11_count <= 1:
        verdict = 'NULL — pre-commit violation possible'
    else:
        verdict = 'NULL'
    out = {
        'finding_id': 'Q011-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': 20260507,
        'rules_tuple': '(no-tashkeel, orthographic-token, exact-string-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'exact 4-token match: وإلى TRIBE أخاهم PROPHET',
        'tribes': TRIBES,
        'prophets': PROPHETS,
        'per_surah_counts': surah_counts,
        'corpus_total_unique_verses': total,
        'q11_count': q11_count,
        'q11_share': q11_share,
        'all_matches': all_matches,
        'verdict': verdict,
    }
    out_dir = '/Users/grey/Downloads/quran/surahs/Q011-hud/csv'
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'Q011-F-01.json'), 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Q011-F-01 verdict: {verdict}")
    print(f"  corpus total: {total}")
    print(f"  Q 11 count: {q11_count}")
    print(f"  Q 11 share: {q11_share:.3f}")
    print(f"  per-surah counts: {surah_counts}")


if __name__ == '__main__':
    main()
