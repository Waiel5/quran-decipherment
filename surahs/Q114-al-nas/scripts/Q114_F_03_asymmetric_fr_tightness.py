#!/usr/bin/env python3
"""Q114-F-03: asymmetric FR-tightness Q 113 ↔ Q 114."""
import hashlib, json, os, sys
import numpy as np

PREREG = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/Q114-F-03-asymmetric-fr-tightness-prereg.md"
PREREG_SHA = "923c3fbc0bef4a23fe0c734213a0008413cb0af7803dad0abf558397e8f97290"
OUT = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/csv/Q114-F-03.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA: print("FATAL", file=sys.stderr); sys.exit(1)
    print(f"[OK] SHA verified: {sha}")

def main():
    verify()
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json") as f:
        d111 = json.load(f)
    D = np.zeros((114,114))
    for elt in d111["D_matrix_upper_triangular"]:
        i, j, dist = elt[0], elt[1], elt[2]
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist
    def topk(s, k=5):
        row = D[s-1].copy()
        row[s-1] = np.inf
        idx = np.argsort(row)
        return [(int(i+1), float(row[i])) for i in idx[:k]]
    Q113_top = topk(113, 5)
    Q114_top = topk(114, 5)
    Q114_nearest = Q114_top[0][0]
    Q113_nearest = Q113_top[0][0]
    cond_a = (Q114_nearest == 113)
    cond_b = (Q113_nearest != 114)
    asymmetric = cond_a and cond_b
    result = {
        "preregistration_id": "Q114-F-03",
        "prereg_sha": PREREG_SHA,
        "Q113_top5_nearest": Q113_top,
        "Q114_top5_nearest": Q114_top,
        "Q114_nearest": Q114_nearest,
        "Q113_nearest": Q113_nearest,
        "cond_a_Q114_to_Q113_is_1st": cond_a,
        "cond_b_Q113_to_Q114_is_NOT_1st": cond_b,
        "asymmetric_pair": asymmetric,
        "verdict": "VINDICATED" if asymmetric else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[Q113 top-5 nearest]: {Q113_top}")
    print(f"[Q114 top-5 nearest]: {Q114_top}")
    print(f"[Q114 nearest is Q113]: {cond_a}")
    print(f"[Q113 nearest is NOT Q114]: {cond_b} (Q113's #1 = Q{Q113_nearest})")
    print(f"[verdict] {result['verdict']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
