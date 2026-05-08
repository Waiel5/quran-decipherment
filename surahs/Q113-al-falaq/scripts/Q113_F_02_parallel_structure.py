#!/usr/bin/env python3
"""Q113-F-02: token-level parallel structure between Q 113 and Q 114."""
import hashlib, json, os, sys, unicodedata
from itertools import combinations

PREREG = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/Q113-F-02-parallel-structure-prereg.md"
PREREG_SHA = "b35bcb0aee7e3a3354767d47aaa1b78dfb1d52e6646f2802cab98c4baeb9ecdb"
OUT = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/csv/Q113-F-02.json"

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
        if (0x0610 <= cp <= 0x061A) or (0x064B <= cp <= 0x065F) or cp == 0x0670 or (0x06D6 <= cp <= 0x06ED) or cp == 0x0640:
            continue
        keep.append(c)
    s = "".join(keep)
    s = s.replace("ٱ","ا").replace("آ","ا").replace("أ","ا").replace("إ","ا").replace("ى","ي").replace("ة","ه")
    return s

def main():
    verify()
    with open("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json") as f:
        q = json.load(f)
    cluster = [109, 110, 111, 112, 113, 114]
    tokens = {}
    for n in cluster:
        s = q[n-1]
        text = " ".join(v["text"] for v in s["verses"])
        toks = [normalize(t) for t in text.split() if t]
        tokens[n] = set(toks)
    # All-pair Jaccard among 6 cluster surahs
    pairs = list(combinations(cluster, 2))
    jaccards = []
    for a, b in pairs:
        I = tokens[a] & tokens[b]
        U = tokens[a] | tokens[b]
        j = len(I) / len(U) if U else 0.0
        jaccards.append({"a": a, "b": b, "intersection": sorted(I), "n_inter": len(I), "n_union": len(U), "jaccard": j})
    # Sort descending
    sorted_j = sorted(jaccards, key=lambda r: -r["jaccard"])
    # Q113-Q114
    q113_q114 = next(r for r in jaccards if (r["a"]==113 and r["b"]==114) or (r["a"]==114 and r["b"]==113))
    rank = sorted_j.index(q113_q114) + 1
    # Shared head check: do tokens of v.1 share "qul aʿūdhu bi-rabbi" structure
    q113_v1 = " ".join([normalize(t) for t in q[112]["verses"][0]["text"].split()])
    q114_v1 = " ".join([normalize(t) for t in q[113]["verses"][0]["text"].split()])
    # Strip alif normalization: قل اعوذ برب الفلق  / قل اعوذ برب الناس
    q113_v1_tokens = q113_v1.split()
    q114_v1_tokens = q114_v1.split()
    shared_head = []
    for a, b in zip(q113_v1_tokens, q114_v1_tokens):
        if a == b:
            shared_head.append(a)
        else:
            break
    # Final check: count "min sharri" across both
    min_sharri_113 = sum(1 for v in q[112]["verses"] if normalize(v["text"]).startswith("من شر") or " من شر" in normalize(v["text"]) or "ومن شر" in normalize(v["text"]))
    min_sharri_114 = sum(1 for v in q[113]["verses"] if normalize(v["text"]).startswith("من شر") or " من شر" in normalize(v["text"]) or "ومن شر" in normalize(v["text"]))
    result = {
        "preregistration_id": "Q113-F-02",
        "prereg_sha": PREREG_SHA,
        "all_pair_jaccards_desc": sorted_j,
        "Q113_Q114_pair": q113_q114,
        "Q113_Q114_rank_in_15_pairs": rank,
        "shared_head_v1": shared_head,
        "min_sharri_count_Q113": min_sharri_113,
        "min_sharri_count_Q114": min_sharri_114,
        "verdict": "VINDICATED" if rank <= 3 else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[Q113-Q114 Jaccard] {q113_q114['jaccard']:.4f}; |inter|={q113_q114['n_inter']}, |union|={q113_q114['n_union']}")
    print(f"[Q113-Q114 rank] {rank}/15 pairs in terminal cluster (Q109-Q114)")
    print(f"[Top 3 pairs]: {[(r['a'],r['b'],r['jaccard']) for r in sorted_j[:3]]}")
    print(f"[Shared v.1 head] {shared_head}")
    print(f"[min sharri count] Q113={min_sharri_113}, Q114={min_sharri_114}")
    print(f"[verdict] {result['verdict']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
