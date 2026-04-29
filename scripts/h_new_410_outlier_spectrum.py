#!/usr/bin/env python3
"""H-NEW-410: full 114-surah local-outlier spectrum ranking."""
import hashlib, json
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-410-outlier-spectrum-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-410.json"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load_D():
    with open(H_NEW_111) as f: d = json.load(f)
    mat = [[0.0]*115 for _ in range(115)]
    for i, j, dist in d["D_matrix_upper_triangular"]:
        mat[i][j] = dist; mat[j][i] = dist
    return mat

SURAH_NAMES = {
    1: "al-Fātiḥa", 2: "al-Baqarah", 3: "Āl ʿImrān", 4: "al-Nisāʾ", 5: "al-Māʾidah",
    6: "al-Anʿām", 7: "al-Aʿrāf", 8: "al-Anfāl", 9: "al-Tawbah", 10: "Yūnus",
    11: "Hūd", 12: "Yūsuf", 13: "al-Raʿd", 14: "Ibrāhīm", 15: "al-Ḥijr",
    16: "al-Naḥl", 17: "al-Isrāʾ", 18: "al-Kahf", 19: "Maryam", 20: "Ṭā Hā",
    21: "al-Anbiyāʾ", 22: "al-Ḥajj", 23: "al-Muʾminūn", 24: "al-Nūr", 25: "al-Furqān",
    26: "al-Shuʿarāʾ", 27: "al-Naml", 28: "al-Qaṣaṣ", 29: "al-ʿAnkabūt", 30: "al-Rūm",
    31: "Luqmān", 32: "al-Sajdah", 33: "al-Aḥzāb", 34: "Sabaʾ", 35: "Fāṭir",
    36: "Yā Sīn", 37: "al-Ṣāffāt", 38: "Ṣād", 39: "al-Zumar", 40: "Ghāfir",
    41: "Fuṣṣilat", 42: "al-Shūrā", 43: "al-Zukhruf", 44: "al-Dukhān", 45: "al-Jāthiyah",
    46: "al-Aḥqāf", 47: "Muḥammad", 48: "al-Fatḥ", 49: "al-Ḥujurāt", 50: "Qāf",
    51: "al-Dhāriyāt", 52: "al-Ṭūr", 53: "al-Najm", 54: "al-Qamar", 55: "al-Raḥmān",
    56: "al-Wāqiʿah", 57: "al-Ḥadīd", 58: "al-Mujādilah", 59: "al-Ḥashr", 60: "al-Mumtaḥanah",
    61: "al-Ṣaff", 62: "al-Jumuʿah", 63: "al-Munāfiqūn", 64: "al-Taghābun", 65: "al-Ṭalāq",
    66: "al-Taḥrīm", 67: "al-Mulk", 68: "al-Qalam", 69: "al-Ḥāqqah", 70: "al-Maʿārij",
    71: "Nūḥ", 72: "al-Jinn", 73: "al-Muzzammil", 74: "al-Muddaththir", 75: "al-Qiyāmah",
    76: "al-Insān", 77: "al-Mursalāt", 78: "al-Nabaʾ", 79: "al-Nāziʿāt", 80: "ʿAbasa",
    81: "al-Takwīr", 82: "al-Infiṭār", 83: "al-Muṭaffifīn", 84: "al-Inshiqāq", 85: "al-Burūj",
    86: "al-Ṭāriq", 87: "al-Aʿlā", 88: "al-Ghāshiyah", 89: "al-Fajr", 90: "al-Balad",
    91: "al-Shams", 92: "al-Layl", 93: "al-Ḍuḥā", 94: "al-Sharḥ", 95: "al-Tīn",
    96: "al-ʿAlaq", 97: "al-Qadr", 98: "al-Bayyinah", 99: "al-Zalzalah", 100: "al-ʿĀdiyāt",
    101: "al-Qāriʿah", 102: "al-Takāthur", 103: "al-ʿAṣr", 104: "al-Humazah", 105: "al-Fīl",
    106: "Quraysh", 107: "al-Māʿūn", 108: "al-Kawthar", 109: "al-Kāfirūn", 110: "al-Naṣr",
    111: "al-Masad", 112: "al-Ikhlāṣ", 113: "al-Falaq", 114: "al-Nās",
}

def main():
    print(f"=== H-NEW-410 ===\nPre-reg SHA: {sha(PREREG)}")
    D = load_D()

    # Compute mean dist to ±2 neighbors for each surah
    results = []
    for k in range(1, 115):
        neighbors = [n for n in [k-2, k-1, k+1, k+2] if 1 <= n <= 114]
        dists = [D[k][n] for n in neighbors]
        mean_d = sum(dists)/len(dists)
        results.append({
            "surah": k, "name": SURAH_NAMES[k],
            "mean_dist_to_neighbors": mean_d,
            "neighbors": neighbors,
            "neighbor_dists": dict(zip(neighbors, dists)),
        })

    # Sort descending by mean_dist — highest = most outlier
    results_sorted = sorted(results, key=lambda x: -x["mean_dist_to_neighbors"])

    print(f"\nTop-15 local content outliers (mean FR distance to ±2 neighbors):")
    print(f"{'Rank':>4} {'Q':>4} {'Name':<20} {'mean_dist':>9} {'neighbors':<20}")
    print("-" * 80)
    for i, r in enumerate(results_sorted[:15], 1):
        nb_str = ",".join(str(n) for n in r["neighbors"])
        print(f"{i:>4} {r['surah']:>4} {r['name']:<20} {r['mean_dist_to_neighbors']:>9.4f} [{nb_str}]")

    print(f"\nBottom-10 MOST-COHESIVE-to-neighbors (lowest distances):")
    for i, r in enumerate(sorted(results, key=lambda x: x["mean_dist_to_neighbors"])[:10], 1):
        nb_str = ",".join(str(n) for n in r["neighbors"])
        print(f"{i:>4} {r['surah']:>4} {r['name']:<20} {r['mean_dist_to_neighbors']:>9.4f} [{nb_str}]")

    # Specific pre-committed surahs
    print(f"\nPre-committed surahs:")
    for target, desc in [(55, "al-Raḥmān (H-NEW-390 outlier)"),
                          (62, "al-Jumuʿa (H-NEW-400 NOT-outlier)"),
                          (1, "al-Fātiḥa (H-NEW-155 sui-generis)"),
                          (112, "al-Ikhlāṣ (classical 1/3-Quran)")]:
        rank = next(i+1 for i, r in enumerate(results_sorted) if r["surah"] == target)
        entry = next(r for r in results_sorted if r["surah"] == target)
        print(f"  Q {target} {SURAH_NAMES[target]:<20} rank {rank}/114, mean_dist={entry['mean_dist_to_neighbors']:.4f}")

    corpus_mean = sum(r["mean_dist_to_neighbors"] for r in results) / 114
    print(f"\nCorpus-wide mean of mean-distances: {corpus_mean:.4f}")
    print(f"Corpus null-mean pairwise FR: ~0.92 (for reference)")

    out = {"id": "H-NEW-410", "prereg_sha": sha(PREREG),
           "corpus_mean_of_mean_distances": corpus_mean,
           "top_15_outliers": results_sorted[:15],
           "bottom_10_cohesive": sorted(results, key=lambda x: x["mean_dist_to_neighbors"])[:10],
           "pre_committed_ranks": {
               55: {"rank": next(i+1 for i, r in enumerate(results_sorted) if r["surah"] == 55),
                    "mean_dist": next(r for r in results_sorted if r["surah"] == 55)["mean_dist_to_neighbors"]},
               62: {"rank": next(i+1 for i, r in enumerate(results_sorted) if r["surah"] == 62),
                    "mean_dist": next(r for r in results_sorted if r["surah"] == 62)["mean_dist_to_neighbors"]},
               1: {"rank": next(i+1 for i, r in enumerate(results_sorted) if r["surah"] == 1),
                   "mean_dist": next(r for r in results_sorted if r["surah"] == 1)["mean_dist_to_neighbors"]},
               112: {"rank": next(i+1 for i, r in enumerate(results_sorted) if r["surah"] == 112),
                     "mean_dist": next(r for r in results_sorted if r["surah"] == 112)["mean_dist_to_neighbors"]},
           }}
    with open(OUT_JSON, "w") as f: json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")

if __name__ == "__main__": main()
