#!/usr/bin/env python3
"""
Q043-F-08 — zukhruf (zxrf) root corpus rank full inventory.
Pre-reg SHA256: ed564811745f4261226f7d05bb1acaecb314ec6c4dab0adac099dd2a594c5430
Seed: 20260509.
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

PREREG = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-08-zukhruf-root-corpus-rank-prereg.md"
EXPECTED_SHA = "ed564811745f4261226f7d05bb1acaecb314ec6c4dab0adac099dd2a594c5430"
ROOT_IDX = "/Users/grey/Downloads/quran/data/morphology/root-index.json"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-08.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def main():
    verify()
    root_idx = json.load(open(ROOT_IDX))
    quran = json.load(open(QURAN))
    target = "zxrf"
    atts = root_idx.get(target, [])
    surah_counts = Counter()
    for s, v, w in atts:
        surah_counts[s] += 1
    surahs_with = sorted(surah_counts.keys())
    n_total = len(atts)
    n_surahs_with = len(surahs_with)
    surah_tokens = {}
    for s in quran:
        sid = s["id"]
        tot = 0
        for v in s["verses"]:
            tot += len(re.findall(r"[ء-ي]+", v["text"]))
        surah_tokens[sid] = tot
    densities = {sid: (surah_counts.get(sid, 0) / surah_tokens[sid] * 1000) for sid in surah_tokens}
    counts_sorted = sorted(surah_counts.items(), key=lambda x: (-x[1], x[0]))
    dens_sorted = sorted(densities.items(), key=lambda x: (-x[1], x[0]))
    def rank_count(sid):
        counts_with = [(s, c) for s, c in surah_counts.items() if c > 0]
        counts_with.sort(key=lambda x: (-x[1], x[0]))
        for i, (s, c) in enumerate(counts_with):
            if s == sid:
                return i+1, c
        return None, 0
    q43_count_rank, q43_count = rank_count(43)
    q43_density_rank = next(i+1 for i, (s, _) in enumerate(dens_sorted) if s == 43)
    q43_density = densities[43]
    top5_counts = counts_sorted[:5]
    top5_density = dens_sorted[:5]
    pred_total = 4
    pred_n_surahs = 4
    pred_q43_count_tied1 = (q43_count_rank == 1)
    pred_q43_dens_gt1 = (q43_density_rank > 1)
    expected_total = (n_total == pred_total)
    expected_n_surahs = (n_surahs_with == pred_n_surahs)
    if expected_total and expected_n_surahs and pred_q43_count_tied1 and pred_q43_dens_gt1:
        verdict = "VINDICATED"
    else:
        verdict = "NULL_OR_DISCREPANCY"
    out = {
        "prereg_id": "Q043-F-08",
        "prereg_sha": EXPECTED_SHA,
        "target_root": target,
        "corpus_total_attestations": n_total,
        "n_surahs_with_attestation": n_surahs_with,
        "surahs_with_attestation": surahs_with,
        "attestations_loci": atts,
        "per_surah_count": dict(surah_counts),
        "q43_count": q43_count,
        "q43_count_rank_among_nonzero": q43_count_rank,
        "q43_density_per_1000": q43_density,
        "q43_density_rank_among_all_114": q43_density_rank,
        "top5_by_count": [{"surah": s, "count": c} for s, c in top5_counts],
        "top5_by_density": [{"surah": s, "density": d} for s, d in top5_density],
        "predicted_total_4": expected_total,
        "predicted_n_surahs_4": expected_n_surahs,
        "predicted_q43_count_rank_1": pred_q43_count_tied1,
        "predicted_q43_density_rank_gt1": pred_q43_dens_gt1,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
