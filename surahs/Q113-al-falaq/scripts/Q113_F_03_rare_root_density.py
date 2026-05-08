#!/usr/bin/env python3
"""Q113-F-03: corpus-rare-root density."""
import hashlib, json, os, re, sys
from collections import Counter

PREREG = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/Q113-F-03-rare-root-density-prereg.md"
PREREG_SHA = "1a92cb01834ab9b73bd4f3097cf80c20d81a360f892fba50c6895eebf4b33c82"
MORPH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT = "/Users/grey/Downloads/quran/surahs/Q113-al-falaq/csv/Q113-F-03.json"

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != PREREG_SHA: print("FATAL", file=sys.stderr); sys.exit(1)
    print(f"[OK] SHA verified: {sha}")

def main():
    verify()
    per_surah_roots = {s: [] for s in range(1, 115)}
    with open(MORPH) as f:
        for line in f:
            m = re.match(r'^\((\d+):(\d+):(\d+):(\d+)\)', line)
            if not m: continue
            s = int(m.group(1))
            rm = re.search(r'ROOT:(\w+)', line)
            if rm: per_surah_roots[s].append(rm.group(1))
    # corpus root frequency
    corpus_freq = Counter()
    for rs in per_surah_roots.values(): corpus_freq.update(rs)
    rare_threshold = 5
    rare_roots = {r for r,c in corpus_freq.items() if c <= rare_threshold}
    # verse counts
    with open(QURAN) as f: q = json.load(f)
    verse_counts = {n+1: q[n]["total_verses"] for n in range(114)}
    # short surahs n<=10
    short_surahs = [s for s,n in verse_counts.items() if n <= 10]
    # per-surah fraction_rare among distinct roots
    fraction_rare = {}
    for s, rs in per_surah_roots.items():
        distinct = set(rs)
        if not distinct:
            fraction_rare[s] = 0.0
            continue
        n_rare = sum(1 for r in distinct if r in rare_roots)
        fraction_rare[s] = n_rare / len(distinct)
    # rank Q113 among short surahs
    short_fractions = [(s, fraction_rare[s]) for s in short_surahs]
    short_fractions_sorted = sorted(short_fractions, key=lambda r: -r[1])
    Q113_rank = next(i for i,(s,_) in enumerate(short_fractions_sorted, 1) if s==113)
    Q113_frac = fraction_rare[113]
    n_short = len(short_surahs)
    p90_idx = int(0.10 * n_short)  # top-10% rank threshold
    p90_pass = Q113_rank <= p90_idx
    # Q113 specifics
    q113_distinct = list(set(per_surah_roots[113]))
    q113_rare_roots = [r for r in q113_distinct if r in rare_roots]
    q113_freq_per_root = {r: corpus_freq[r] for r in q113_distinct}
    result = {
        "preregistration_id": "Q113-F-03",
        "prereg_sha": PREREG_SHA,
        "rare_threshold": rare_threshold,
        "Q113_distinct_roots": q113_distinct,
        "Q113_distinct_root_corpus_freq": q113_freq_per_root,
        "Q113_rare_roots": q113_rare_roots,
        "Q113_n_distinct": len(q113_distinct),
        "Q113_n_rare": len(q113_rare_roots),
        "Q113_fraction_rare": Q113_frac,
        "Q113_rank_among_short": Q113_rank,
        "n_short_surahs": n_short,
        "p90_threshold_rank": p90_idx,
        "p90_pass": p90_pass,
        "verdict": "VINDICATED" if p90_pass else "NULL",
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT,"w") as f: json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"[Q113 distinct roots] {q113_distinct}")
    print(f"[Q113 corpus freq per root] {q113_freq_per_root}")
    print(f"[Q113 rare roots (<= {rare_threshold} attestations)] {q113_rare_roots}")
    print(f"[Q113 fraction_rare] {Q113_frac:.4f}")
    print(f"[Q113 rank among {n_short} short surahs] {Q113_rank}")
    print(f"[p90 threshold rank] {p90_idx}")
    print(f"[verdict] {result['verdict']}")
    print(f"[OK] -> {OUT}")

if __name__=="__main__": main()
