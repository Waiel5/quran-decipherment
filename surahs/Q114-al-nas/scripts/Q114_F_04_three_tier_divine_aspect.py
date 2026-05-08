#!/usr/bin/env python3
"""Q114-F-04: 3-tier divine-aspect rules-tuple stability."""
import hashlib, json, os, sys, unicodedata

PREREG = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/Q114-F-04-three-tier-divine-aspect-prereg.md"
PREREG_SHA = "871641c75975d91c1031077ae2c20e282cd73982fc40b6e37b287097b31d5955"
OUT = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/csv/Q114-F-04.json"
VARIANTS = [
    ("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json", "no-tashkeel"),
    ("/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json", "min-tashkeel"),
    ("/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json", "full-tashkeel"),
]

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA: print("FATAL", file=sys.stderr); sys.exit(1)
    print(f"[OK] SHA verified: {sha}")

def normalize(s):
    s = "".join(c for c in s if not unicodedata.combining(c))
    keep = []
    for c in s:
        cp = ord(c)
        if (0x0610 <= cp <= 0x061A) or (0x064B <= cp <= 0x065F) or cp == 0x0670 or (0x06D6 <= cp <= 0x06ED) or cp == 0x0640: continue
        keep.append(c)
    s = "".join(keep)
    s = s.replace("ٱ","ا").replace("آ","ا").replace("أ","ا").replace("إ","ا")
    return s

def main():
    verify()
    per_variant = {}
    for path, label in VARIANTS:
        with open(path) as f: d = json.load(f)
        Q114 = d[113]
        v1 = normalize(Q114["verses"][0]["text"])
        v2 = normalize(Q114["verses"][1]["text"])
        v3 = normalize(Q114["verses"][2]["text"])
        # Tests: v1 has رب, v2 has ملك, v3 has اله, each contains الناس
        tests = {
            "v1_has_rabb": "رب" in v1 or "ربب" in v1,
            "v2_has_malik": "ملك" in v2,
            "v3_has_ilah": "اله" in v3,
            "v1_has_al_nas": "الناس" in v1,
            "v2_has_al_nas": "الناس" in v2,
            "v3_has_al_nas": "الناس" in v3,
        }
        per_variant[label] = {
            "v1_normalized": v1,
            "v2_normalized": v2,
            "v3_normalized": v3,
            "tests": tests,
            "all_pass": all(tests.values()),
        }
    rules_tuple_stable = all(per_variant[v]["all_pass"] for v in per_variant)
    result = {
        "preregistration_id": "Q114-F-04",
        "prereg_sha": PREREG_SHA,
        "per_variant": per_variant,
        "rules_tuple_stable": rules_tuple_stable,
        "verdict": "VINDICATED-RULES-TUPLE-STABLE" if rules_tuple_stable else "RULES-TUPLE-FRAGILE",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    for label, v in per_variant.items():
        print(f"[{label}] all_pass={v['all_pass']}; tests={v['tests']}")
    print(f"[rules-tuple stable]: {rules_tuple_stable}")
    print(f"[verdict] {result['verdict']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
