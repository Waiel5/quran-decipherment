#!/usr/bin/env python3
"""Q073-F-03 — Q 73:20 long-verse abrogation classical claim — hadith on-disk verification.

Pre-reg: surahs/Q073-al-muzzammil/Q073-F-03-abrogation-classical-claim-prereg.md
Pre-reg SHA256: 01590e7ce45e692cdb323a1c7a87976c0eedf644cb1a58a4275803d58c455f7a
Rules-tuple: (no-tashkeel via harakat-strip, ahmedbaset-json 9-books corpus, descriptive verification)
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/Q073-F-03-abrogation-classical-claim-prereg.md'
EXPECTED_SHA = '01590e7ce45e692cdb323a1c7a87976c0eedf644cb1a58a4275803d58c455f7a'
SEED = 20260509

OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/csv/Q073-F-03.json'
HADITH_BASE = '/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books'

NINE_BOOKS = [
    ('Bukhari', f'{HADITH_BASE}/bukhari.json'),
    ('Muslim', f'{HADITH_BASE}/muslim.json'),
    ('AbuDawud', f'{HADITH_BASE}/abudawud.json'),
    ('Tirmidhi', f'{HADITH_BASE}/tirmidhi.json'),
    ('Nasai', f'{HADITH_BASE}/nasai.json'),
    ('IbnMajah', f'{HADITH_BASE}/ibnmajah.json'),
    ('Ahmad', f'{HADITH_BASE}/ahmed.json'),
    ('Malik', f'{HADITH_BASE}/malik.json'),
    ('Darimi', f'{HADITH_BASE}/darimi.json'),
]

HARAKAT = re.compile(r'[ً-ٰٟؐ-ؚۖ-ۭ]')


def strip_haraka(s):
    return HARAKAT.sub('', s)


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    target_phrases = {
        'qum_al_layl': 'قم الليل إلا قليلا',
        'nasakh_al_aya': 'نسختها الآية',
        'lan_tuhsuhu': 'علم أن لن تحصوه',
        'fa_iqraa_tayassara': 'فاقرءوا ما تيسر',
    }

    naskh_root_pat = re.compile(r'نسخ|نسخت|نسخها|ناسخ|منسوخ')
    q73_marker_pat = re.compile(r'المزمل|قم الليل')

    all_results = {}
    for label, path in NINE_BOOKS:
        if not os.path.exists(path):
            all_results[label] = {'status': 'missing', 'hits': []}
            continue
        with open(path) as f:
            data = json.load(f)
        hits = []
        for h in data.get('hadiths', []):
            txt_raw = h.get('arabic', '')
            txt = strip_haraka(txt_raw)
            matched = {k: (v in txt) for k, v in target_phrases.items()}
            n_matched = sum(matched.values())
            naskh_present = bool(naskh_root_pat.search(txt))
            q73_present = bool(q73_marker_pat.search(txt))

            # Hit criteria: ≥2 of 4 phrases (per pre-reg §2)
            if n_matched >= 2 or (naskh_present and q73_present):
                hits.append({
                    'idInBook': h.get('idInBook'),
                    'chapterId': h.get('chapterId'),
                    'matched_phrases': [k for k, v in matched.items() if v],
                    'n_matched': n_matched,
                    'naskh_root_present': naskh_present,
                    'q73_marker_present': q73_present,
                    'arabic': txt[:1000],
                    'english': h.get('english', {}).get('text', '')[:600] if isinstance(h.get('english'), dict) else '',
                })
        all_results[label] = {
            'status': 'searched',
            'n_hits': len(hits),
            'hits': hits,
        }

    # === Verification verdict ===
    total_hits = sum(r.get('n_hits', 0) for r in all_results.values())
    explicit_naskh_hits = []
    for src, r in all_results.items():
        for h in r.get('hits', []):
            # An explicit abrogation hit must contain `nasakh_al_aya` phrase
            # OR the naskh root + Q 73 marker together
            if 'nasakh_al_aya' in h['matched_phrases'] or (h['naskh_root_present'] and h['q73_marker_present']):
                explicit_naskh_hits.append({'src': src, **h})

    if explicit_naskh_hits:
        verdict = "VERIFIED"
        verdict_detail = f"{len(explicit_naskh_hits)} explicit abrogation hadith found across {len(set(h['src'] for h in explicit_naskh_hits))} of 9 collections"
    elif total_hits >= 3:
        verdict = "PARTIALLY-VERIFIED"
        verdict_detail = f"{total_hits} associative hits but no single hadith with explicit abrogation language"
    elif total_hits >= 1:
        verdict = "PARTIALLY-VERIFIED-WEAK"
        verdict_detail = f"{total_hits} loose hits"
    else:
        verdict = "NULL"
        verdict_detail = "no on-disk evidence in 9-books"

    # Brief said "Mālik Muwaṭṭaʾ + Bukhārī" — check those specifically
    brief_check = {
        'Bukhari_explicit_naskh': any(h['src'] == 'Bukhari' for h in explicit_naskh_hits),
        'Malik_explicit_naskh': any(h['src'] == 'Malik' for h in explicit_naskh_hits),
        'AbuDawud_explicit_naskh': any(h['src'] == 'AbuDawud' for h in explicit_naskh_hits),
    }
    if not (brief_check['Bukhari_explicit_naskh'] or brief_check['Malik_explicit_naskh']):
        brief_correction = "BRIEF-INCORRECT: brief specified Mālik + Bukhārī but explicit abrogation chain located elsewhere"
    else:
        brief_correction = None

    out = {
        "test_id": "Q073-F-03",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "target_phrases": target_phrases,
        "per_collection": all_results,
        "total_hits": total_hits,
        "explicit_naskh_hits": explicit_naskh_hits,
        "n_explicit_naskh_hits": len(explicit_naskh_hits),
        "brief_check": brief_check,
        "brief_correction": brief_correction,
        "verdict": verdict,
        "verdict_detail": verdict_detail,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"Verdict: {verdict}")
    print(f"  Detail: {verdict_detail}")
    print(f"  Explicit naskh hits: {len(explicit_naskh_hits)}")
    for h in explicit_naskh_hits[:5]:
        print(f"    {h['src']} #{h['idInBook']}: matched={h['matched_phrases']}")
    print(f"  Brief check: {brief_check}")
    if brief_correction:
        print(f"  Brief correction: {brief_correction}")
    print(f"Written to: {OUT_PATH}")


if __name__ == '__main__':
    main()
