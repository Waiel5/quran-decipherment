#!/usr/bin/env python3
"""Q114-F-02: max-token-density among short surahs."""
import hashlib, json, os, sys, unicodedata
from collections import Counter

PREREG = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/Q114-F-02-al-nas-density-prereg.md"
PREREG_SHA = "93320134870553dcca2c37916d22cd2c6c23050e77cc57b5d046ac60b5b1f6cd"
OUT = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/csv/Q114-F-02.json"

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
    s = s.replace("ٱ","ا").replace("آ","ا").replace("أ","ا").replace("إ","ا").replace("ى","ي").replace("ة","ه")
    return s

def main():
    verify()
    with open("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json") as f: q = json.load(f)
    short_results = []
    for s in q:
        if s["total_verses"] > 10: continue
        text = " ".join(v["text"] for v in s["verses"])
        toks = [normalize(t) for t in text.split() if t]
        # strip leading particles (و، ف، ل، ب، ك) for token-based count? - keep simple
        if not toks:
            continue
        cnt = Counter(toks)
        most_common_token, most_common_count = cnt.most_common(1)[0]
        density = most_common_count / len(toks)
        short_results.append({
            "surah": s["id"],
            "name": s["name"],
            "n_words": len(toks),
            "n_verses": s["total_verses"],
            "most_common_token": most_common_token,
            "most_common_count": most_common_count,
            "max_token_density": density,
        })
    sorted_r = sorted(short_results, key=lambda r: -r["max_token_density"])
    Q114_idx = next(i for i, r in enumerate(sorted_r,1) if r["surah"]==114)
    Q114 = next(r for r in sorted_r if r["surah"]==114)
    result = {
        "preregistration_id": "Q114-F-02",
        "prereg_sha": PREREG_SHA,
        "n_short_surahs": len(short_results),
        "ranking_desc": sorted_r,
        "Q114_rank": Q114_idx,
        "Q114_data": Q114,
        "verdict": "VINDICATED" if Q114_idx == 1 else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[Q114] {Q114}")
    print(f"[Q114 rank among {len(short_results)} short surahs] {Q114_idx}")
    print(f"[Top-5]:")
    for r in sorted_r[:5]:
        print(f"   Q{r['surah']} ({r['name']}): token={r['most_common_token']!r} count={r['most_common_count']}/{r['n_words']} density={r['max_token_density']:.4f}")
    print(f"[verdict] {result['verdict']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
