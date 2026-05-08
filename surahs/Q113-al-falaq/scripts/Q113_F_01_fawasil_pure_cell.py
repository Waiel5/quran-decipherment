#!/usr/bin/env python3
"""Q113-F-01: iʿjāz-al-fawāṣil-pure cell membership."""
import hashlib, json, os, sys

PREREG = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/Q113-F-01-fawasil-pure-cell-prereg.md"
PREREG_SHA = "2f6ae67a3ca9a1fe20a313c4263831741ceb38c198ee7583904b8f5ea79f22d9"
OUT = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/csv/Q113-F-01.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA: print("FATAL: SHA mismatch", file=sys.stderr); sys.exit(1)
    print(f"[OK] SHA verified: {sha}")

def main():
    verify()
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json") as f:
        d750 = json.load(f)
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json") as f:
        d840 = json.load(f)
    with open("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json") as f:
        d720 = json.load(f)
    Q113_750 = next(r for r in d750["per_surah"] if r["surah"]==113)
    Q113_840 = next(r for r in d840["all_uas"] if r["surah"]==113)
    UAS_ranked = sorted(d840["all_uas"], key=lambda x: -x["UAS"])
    UAS_rank = next(i for i,r in enumerate(UAS_ranked,1) if r["surah"]==113)
    sig_A_rank = Q113_750["rank_A"]
    # adjacency
    adj_ranked = sorted(d720["per_adjacency"], key=lambda x: -x["fraction_residual"])
    adj_112_113 = next(r for r in d720["per_adjacency"] if r["pair"]==[112,113])
    adj_113_114 = next(r for r in d720["per_adjacency"] if r["pair"]==[113,114])
    rank_112_113 = adj_ranked.index(adj_112_113)+1
    rank_113_114 = adj_ranked.index(adj_113_114)+1
    crit = {
        "c1_sig_A_top20": sig_A_rank <= 20,
        "c2_UAS_below_top30": UAS_rank > 30,
        "c3_left_non_top15": rank_112_113 > 15,
        "c4_right_non_top15": rank_113_114 > 15,
    }
    cell_member = all(crit.values())
    cell_roster = [86,89,100,106,113]
    in_roster = 113 in cell_roster
    result = {
        "preregistration_id": "Q113-F-01",
        "prereg_sha": PREREG_SHA,
        "Q113_sig_A": Q113_750["sig_A"],
        "Q113_sig_A_rank": sig_A_rank,
        "Q113_UAS": Q113_840["UAS"],
        "Q113_UAS_rank": UAS_rank,
        "Q112_Q113_adj_rank": rank_112_113,
        "Q113_Q114_adj_rank": rank_113_114,
        "criteria": crit,
        "cell_member_quantitative": cell_member,
        "in_cross_finding_026_roster": in_roster,
        "cell_roster": cell_roster,
        "verdict": "VINDICATED" if cell_member and in_roster else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    for k,v in result.items():
        if k != "criteria":
            print(f"[{k}] {v}")
    print(f"[criteria] {crit}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
