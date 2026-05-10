#!/usr/bin/env python3
"""
Q045-F-05 — *jāthiya* (جاثية) surface-form hapax verification.
Pre-reg SHA256: 718ca3b4632b81d41f739993a7921b4d89506ec095b76f0e4623cc5b66c3b1d4
Seed: 20260509.
"""
import hashlib
import json
import os
import re
import sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/preregs/Q045-F-05-jathiya-hapax-prereg.md"
EXPECTED_SHA = "718ca3b4632b81d41f739993a7921b4d89506ec095b76f0e4623cc5b66c3b1d4"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
ROOT_IDX = "/Users/grey/Downloads/quran/data/morphology/root-index.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/csv/Q045-F-05.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def main():
    verify()
    quran = json.load(open(QURAN))
    root_idx = json.load(open(ROOT_IDX))
    target = "جاثية"
    # Surface-form matches with word-boundary
    pat = re.compile(r"(?:^|\s)" + re.escape(target) + r"(?=\s|$|[^؀-ۿ])")
    hits = []
    for s in quran:
        sid = s["id"]
        for v in s["verses"]:
            if pat.search(v["text"]):
                hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    observed_loci = [(h["surah"], h["verse"]) for h in hits]
    expected_loci = [(45, 28)]
    if sorted(observed_loci) == sorted(expected_loci):
        verdict = "VINDICATED — corpus-singleton at Q 45:28"
    else:
        verdict = "NULL_OR_DISCREPANCY"
    root_atts = root_idx.get("jvw", [])
    out = {
        "prereg_id": "Q045-F-05",
        "prereg_sha": EXPECTED_SHA,
        "search_string": target,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_attestations": len(hits),
        "attestations": hits,
        "expected_loci": expected_loci,
        "observed_loci": observed_loci,
        "root_jvw_total_attestations": len(root_atts),
        "root_jvw_attestations": root_atts,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
