#!/usr/bin/env python3
"""Q113-F-04: rhyme-shift / typology alignment, rules-tuple stability."""
import hashlib, json, os, sys, unicodedata

PREREG = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/Q113-F-04-rhyme-typology-prereg.md"
PREREG_SHA = "c614545d2bda1a624772c927e888d80cf9de051cf212f0d13e7b5d080e87f7fc"
OUT = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/csv/Q113-F-04.json"
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

def strip(s):
    s = "".join(c for c in s if not unicodedata.combining(c))
    keep = []
    for c in s:
        cp = ord(c)
        if (0x0610 <= cp <= 0x061A) or (0x064B <= cp <= 0x065F) or cp == 0x0670 or (0x06D6 <= cp <= 0x06ED) or cp == 0x0640: continue
        keep.append(c)
    return "".join(keep)

def main():
    verify()
    per_variant = {}
    for path, label in VARIANTS:
        with open(path) as f: data = json.load(f)
        s = data[112]  # Q113
        finals = []
        for v in s["verses"]:
            words = v["text"].strip().split()
            stripped = strip(words[-1].strip())
            if stripped:
                finals.append(stripped[-1])
        per_variant[label] = finals
    expected = ["ق","ق","ب","د","د"]
    matches = {k: v == expected for k,v in per_variant.items()}
    rules_tuple_stable = all(matches.values())
    typology_clusters = {
        "vv1_2_qaf": "refuge-formula + universal-evil",
        "v3_ba": "cosmic-darkness evil",
        "vv4_5_dal": "magical + affective evils",
    }
    typology_aligned = rules_tuple_stable
    result = {
        "preregistration_id": "Q113-F-04",
        "prereg_sha": PREREG_SHA,
        "per_variant_final_letters": per_variant,
        "expected_sequence": expected,
        "rules_tuple_stable": rules_tuple_stable,
        "matches_per_variant": matches,
        "typology_clusters": typology_clusters,
        "verdict": "VINDICATED-RULES-TUPLE-STABLE" if rules_tuple_stable else "DIRECTIONAL" if matches.get("no-tashkeel") else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    for k,v in per_variant.items():
        print(f"[{k}] finals: {v}")
    print(f"[expected] {expected}")
    print(f"[rules-tuple stable] {rules_tuple_stable}")
    print(f"[verdict] {result['verdict']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
