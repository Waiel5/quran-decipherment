#!/usr/bin/env python3
"""
Q044-F-06 — Muslim 10-signs-of-hour hadith verification (dukhān eschatology).
Pre-reg SHA256: a3a29927abfd04ef9f5c72199751d0f7a0ad526294422cc0fc1d42fefdce8ce3
Seed: 20260509 (unused; this is a citation-verification test).
"""
import hashlib
import json
import os
import re
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-06-bukhari-10-signs-prereg.md"
EXPECTED_SHA = "a3a29927abfd04ef9f5c72199751d0f7a0ad526294422cc0fc1d42fefdce8ce3"
MUSLIM = "/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-06.json"

DIACRITICS = re.compile("[ً-ْٰ]")
def strip(s):
    return DIACRITICS.sub("", s) if s else ""

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def main():
    verify()
    muslim = json.load(open(MUSLIM))
    hadiths = muslim.get("hadiths", [])
    print(f"[INFO] Loaded {len(hadiths)} Muslim hadiths.")
    # Look for #2901 and #2902 by idInBook
    h_by_idInBook = {h.get("idInBook"): h for h in hadiths}
    h_2901 = h_by_idInBook.get(2901)
    h_2902 = h_by_idInBook.get(2902)
    def contains_dukhan(h):
        if not h:
            return False, ""
        ar = strip(h.get("arabic", "") or "")
        en_field = h.get("english")
        if isinstance(en_field, dict):
            en = en_field.get("text", "") or ""
        else:
            en = en_field or ""
        has_dukhan = ("دخان" in ar) or ("الدخان" in ar) or ("smoke" in en.lower())
        return has_dukhan, ar[:400]
    h2901_has, h2901_preview = contains_dukhan(h_2901)
    h2902_has, h2902_preview = contains_dukhan(h_2902)
    # Corpus-wide cross-check (diacritic-stripped): hadiths containing both عشر آيات and دخان
    dukhan_corpus = []
    ten_signs_corpus = []
    for h in hadiths:
        ar = strip(h.get("arabic", "") or "")
        if "دخان" in ar or "الدخان" in ar:
            dukhan_corpus.append({
                "idInBook": h.get("idInBook"),
                "preview": ar[:300]
            })
        if ("عشر آيات" in ar) and ("دخان" in ar):
            ten_signs_corpus.append({
                "idInBook": h.get("idInBook"),
                "preview": ar[:500]
            })
    if h2901_has or h2902_has:
        verdict = "VERIFIED — at least one of #2901/#2902 contains دخان"
    elif dukhan_corpus:
        verdict = "VERIFIED-PARTIAL — دخان attested in Muslim but at different numbers"
    else:
        verdict = "NULL — no Muslim hadith on disk contains دخان"
    out = {
        "prereg_id": "Q044-F-06",
        "prereg_sha": EXPECTED_SHA,
        "muslim_total_hadiths": len(hadiths),
        "hadith_2901_idInBook_found": h_2901 is not None,
        "hadith_2901_has_dukhan": h2901_has,
        "hadith_2901_preview": h2901_preview if h_2901 else None,
        "hadith_2902_idInBook_found": h_2902 is not None,
        "hadith_2902_has_dukhan": h2902_has,
        "hadith_2902_preview": h2902_preview if h_2902 else None,
        "dukhan_attestations_in_muslim_n": len(dukhan_corpus),
        "dukhan_attestations_in_muslim_sample": dukhan_corpus[:10],
        "ten_signs_with_dukhan_n": len(ten_signs_corpus),
        "ten_signs_with_dukhan_loci": ten_signs_corpus[:5],
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"#2901 found: {h_2901 is not None}, has dukhān: {h2901_has}")
    print(f"#2902 found: {h_2902 is not None}, has dukhān: {h2902_has}")
    print(f"دخان attestations in Muslim corpus: {len(dukhan_corpus)}")
    print(f"10-signs with dukhān loci: {len(ten_signs_corpus)}")
    print(f"VERDICT: {verdict}")

if __name__ == "__main__":
    main()
