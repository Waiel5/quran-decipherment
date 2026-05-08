#!/usr/bin/env python3
"""Q114-F-01: iʿjāz-al-maʿnā cell co-membership."""
import hashlib, json, os, sys
import numpy as np

PREREG = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/Q114-F-01-cell-co-member-prereg.md"
PREREG_SHA = "6df81b946a89f8abf23270338a8571428c6b5e0468d9ca028cb7cb17f0352006"
OUT = "/Users/grey/Downloads/quran/surahs/Q114-al-nas/csv/Q114-F-01.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA: print("FATAL", file=sys.stderr); sys.exit(1)
    print(f"[OK] SHA verified: {sha}")

def main():
    verify()
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json") as f: d840 = json.load(f)
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json") as f: d590 = json.load(f)
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json") as f: d720 = json.load(f)
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json") as f: d111 = json.load(f)
    UAS_ranked = sorted(d840["all_uas"], key=lambda x: -x["UAS"])
    UAS_rank = next(i for i,r in enumerate(UAS_ranked,1) if r["surah"]==114)
    Q114_590 = next(r for r in d590["all_surahs_results"] if r["X"]==114)
    delta_pct = Q114_590["delta_pct"]
    classification = Q114_590["classification"]
    adj_ranked = sorted(d720["per_adjacency"], key=lambda x: -x["fraction_residual"])
    adj_113_114 = next(r for r in d720["per_adjacency"] if r["pair"]==[113,114])
    adj_rank = adj_ranked.index(adj_113_114)+1
    # Compute FR-centroid rank
    D = np.zeros((114,114))
    for elt in d111["D_matrix_upper_triangular"]:
        i, j, dist = elt[0], elt[1], elt[2]
        D[i-1][j-1] = dist
        D[j-1][i-1] = dist
    mean_d = np.array([np.mean([D[s][j] for j in range(114) if j!=s]) for s in range(114)])
    sorted_centroid = np.argsort(mean_d)
    centroid_rank = list(sorted_centroid).index(113)+1  # surah 114 = idx 113
    crit = {
        "c1_UAS_rank_>=100": UAS_rank >= 100,
        "c2_outlier_NULL_or_zero": delta_pct == 0.0 or classification == "NULL",
        "c3_adj_rank_>30": adj_rank > 30,
        "c4_FR_centroid_rank_<=10": centroid_rank <= 10,
    }
    cell_member = all(crit.values())
    result = {
        "preregistration_id": "Q114-F-01",
        "prereg_sha": PREREG_SHA,
        "Q114_UAS_rank": UAS_rank,
        "Q114_outlier_delta_pct": delta_pct,
        "Q114_outlier_classification": classification,
        "Q114_Q113_adj_rank": adj_rank,
        "Q114_FR_centroid_rank": centroid_rank,
        "Q114_FR_centroid_mean_d": float(mean_d[113]),
        "criteria": crit,
        "cell_member": cell_member,
        "verdict": "VINDICATED" if cell_member else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    for k,v in result.items():
        if k != "criteria":
            print(f"[{k}] {v}")
    print(f"[criteria] {crit}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
