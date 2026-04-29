"""Q042-F-01: two-verse muqaṭṭaʿāt-split uniqueness test."""
import hashlib
import json
import os
import sys
import re

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q042-al-shura/preregs/Q042-F-01-muqattaat-split-prereg.md"
EXPECTED_SHA = "c96f4e46b179c0a961ba6374f69e2c2858eb5c509fd8a0ec1aa3f426cd8dda25"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q042-al-shura/csv/Q042-F-01.json"

# The 29 canonical muqaṭṭaʿāt-opened surahs
MUQATTAAT_SURAHS = [2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68]

# Set of valid muqaṭṭaʿāt letters (from the canonical ḥurūf muqaṭṭaʿāt)
MUQ_LETTERS = set("الـمصرنكهيعطسحقطسمفصق")  # superset; we treat any verse with only Arabic-letter graphemes and no spaces split as candidate

def is_muqattaat_only(text):
    # Strip whitespace; check if only consists of disconnected Arabic letters (i.e., very short, no full word)
    txt = text.strip()
    # No spaces, length small (≤ 6 letters), all Arabic letters
    if len(txt.split()) > 1:
        return False
    if len(txt) > 6:
        return False
    # Should be pure Arabic letters
    return bool(re.fullmatch(r'[؀-ۿ]+', txt))

def main():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha}")

    with open(QURAN_PATH) as f:
        quran = json.load(f)

    per_surah = []
    for sid in MUQATTAAT_SURAHS:
        s = quran[sid - 1]
        v1 = s["verses"][0]
        v1_is_muq = is_muqattaat_only(v1["text"])
        v2_text = s["verses"][1]["text"] if len(s["verses"]) > 1 else ""
        v2_is_muq = is_muqattaat_only(v2_text) if v2_text else False
        per_surah.append({
            "surah": sid,
            "name": s.get("transliteration"),
            "v1_text": v1["text"],
            "v1_is_muqattaat_only": v1_is_muq,
            "v2_text": v2_text,
            "v2_is_muqattaat_only": v2_is_muq,
            "split_pattern": "v1+v2" if (v1_is_muq and v2_is_muq) else ("v1_only" if v1_is_muq else "neither"),
        })

    splits = [d for d in per_surah if d["split_pattern"] == "v1+v2"]
    expected_split_surahs = [42]
    observed_split_surahs = [d["surah"] for d in splits]
    verdict = "VINDICATED" if observed_split_surahs == expected_split_surahs else "NULL_OR_DISCREPANCY"

    out = {
        "prereg_id": "Q042-F-01",
        "prereg_sha": EXPECTED_SHA,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_muqattaat_surahs_examined": len(MUQATTAAT_SURAHS),
        "expected_split_surahs": expected_split_surahs,
        "observed_split_surahs": observed_split_surahs,
        "verdict": verdict,
        "per_surah_detail": per_surah,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    # Print compact summary
    print(json.dumps({"verdict": verdict, "observed_split_surahs": observed_split_surahs, "n_examined": len(per_surah)}, indent=2))

if __name__ == "__main__":
    main()
