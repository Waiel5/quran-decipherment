#!/usr/bin/env python3
"""
Q044-F-04 — dukhān (dxn) root corpus rank-1 test for Q 44.
Pre-reg SHA256: 5508294c18cc97b95e5f99e42978bbe82608e9417ee5c5e47d70715db19eb16b
Seed: 20260509.
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

PREREG = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-04-dukhan-root-corpus-rank-prereg.md"
EXPECTED_SHA = "5508294c18cc97b95e5f99e42978bbe82608e9417ee5c5e47d70715db19eb16b"
ROOT_IDX = "/Users/grey/Downloads/quran/data/morphology/root-index.json"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-04.json"

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
    target = "dxn"
    atts = root_idx.get(target, [])
    surah_counts = Counter()
    for s, v, w in atts:
        surah_counts[s] += 1
    n_total = len(atts)
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
    q44_count = surah_counts.get(44, 0)
    counts_with = [(s, c) for s, c in surah_counts.items() if c > 0]
    counts_with.sort(key=lambda x: (-x[1], x[0]))
    q44_count_rank = None
    for i, (s, c) in enumerate(counts_with):
        if s == 44:
            q44_count_rank = i+1
            break
    q44_density_rank = next(i+1 for i, (s, _) in enumerate(dens_sorted) if s == 44)
    q44_density = densities[44]
    top5_counts = counts_sorted[:5]
    top5_density = dens_sorted[:5]
    if q44_count_rank == 1 and q44_density_rank == 1:
        verdict = "VINDICATED — Q 44 rank-1 by both count and density"
    elif q44_count_rank == 1 or q44_density_rank == 1:
        verdict = "MIXED — Q 44 rank-1 by only one metric"
    else:
        verdict = "NULL — Q 44 not rank-1 by either"
    out = {
        "prereg_id": "Q044-F-04",
        "prereg_sha": EXPECTED_SHA,
        "target_root": target,
        "corpus_total_attestations": n_total,
        "n_surahs_with_attestation": len(counts_with),
        "surahs_with_attestation": sorted(s for s, _ in counts_with),
        "attestations_loci": atts,
        "per_surah_count": dict(surah_counts),
        "q44_count": q44_count,
        "q44_count_rank": q44_count_rank,
        "q44_density_per_1000": q44_density,
        "q44_density_rank_among_all_114": q44_density_rank,
        "top5_by_count": [{"surah": s, "count": c} for s, c in top5_counts],
        "top5_by_density": [{"surah": s, "density": d} for s, d in top5_density],
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(json.dumps(out, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
