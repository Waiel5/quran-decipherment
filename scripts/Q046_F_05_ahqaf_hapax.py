#!/usr/bin/env python3
"""
Q046-F-05 — *aḥqāf* surface-form hapax verification.
Pre-reg SHA256: 523f270da6b993ca306bf645bb06a74a699d0a72684e87bcc578b38a397dc0d4
Seed: 20260509.
"""
import hashlib
import json
import os
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-05-ahqaf-hapax-prereg.md"
EXPECTED_SHA = "523f270da6b993ca306bf645bb06a74a699d0a72684e87bcc578b38a397dc0d4"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
ROOT_IDX = "/Users/grey/Downloads/quran/data/morphology/root-index.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-05.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def search(quran, needle):
    hits = []
    for s in quran:
        sid = s["id"]
        for v in s["verses"]:
            if needle in v["text"]:
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    return hits

def main():
    verify()
    quran = json.load(open(QURAN))
    root_idx = json.load(open(ROOT_IDX))
    t1 = "الأحقاف"
    t2 = "أحقاف"
    hits_def = search(quran, t1)
    hits_indef = search(quran, t2)
    # The indefinite search subsumes the definite (since الأحقاف contains أحقاف)
    # Compute unique indef-only (those not from the definite article spans)
    observed_loci_def = [(h["surah"], h["verse"]) for h in hits_def]
    expected_loci_def = [(46, 21)]
    if sorted(observed_loci_def) == sorted(expected_loci_def):
        verdict = "VINDICATED — corpus-singleton at Q 46:21"
    else:
        verdict = "NULL_OR_DISCREPANCY"
    root_atts = root_idx.get("Hqf", [])
    out = {
        "prereg_id": "Q046-F-05",
        "prereg_sha": EXPECTED_SHA,
        "definite_form": t1,
        "definite_hits": hits_def,
        "definite_observed_loci": observed_loci_def,
        "definite_expected_loci": expected_loci_def,
        "stem_form_hits": hits_indef,
        "stem_form_loci": [(h["surah"], h["verse"]) for h in hits_indef],
        "root_Hqf_total_attestations": len(root_atts),
        "root_Hqf_attestations": root_atts,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
