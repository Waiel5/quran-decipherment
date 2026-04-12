"""Phase B: verse-length sequence analysis per surah.

- Extracts letter-count sequence per surah (graphemes, no-tashkeel).
- Detects palindromic subsequences at lengths 5, 7, 9.
- Detects strictly monotonic runs at length >= 5.
- Verifies the three known length-7 palindromes.
- Autocorrelation & spectral signature per surah.
- Ar-Rahman refrain partitioning analysis (31 refrains of 55:13-pattern).
"""
from __future__ import annotations

import json
import math
import os
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran  # noqa: E402
from tools.tokenize import graphemes  # noqa: E402


OUT_DIR = "/tmp/verse-length-run"
os.makedirs(OUT_DIR, exist_ok=True)


def is_pal(seq: List[int]) -> bool:
    return seq == seq[::-1]


def find_palindromes(seq: List[int], L: int) -> List[Tuple[int, List[int]]]:
    """Return (start_index_0based, subsequence) for every length-L palindrome."""
    out = []
    if len(seq) < L:
        return out
    for i in range(len(seq) - L + 1):
        window = seq[i:i + L]
        if is_pal(window):
            # guard against trivial all-equal runs — flag but keep
            out.append((i, window))
    return out


def find_monotonic_runs(seq: List[int], min_len: int = 5) -> Dict[str, List[Tuple[int, List[int]]]]:
    """Return strictly-increasing and strictly-decreasing maximal runs
    of length >= min_len, as (start_index_0based, subsequence)."""
    inc: List[Tuple[int, List[int]]] = []
    dec: List[Tuple[int, List[int]]] = []
    n = len(seq)
    i = 0
    while i < n - 1:
        # increasing run starting at i
        j = i
        while j + 1 < n and seq[j + 1] > seq[j]:
            j += 1
        if j - i + 1 >= min_len:
            inc.append((i, seq[i:j + 1]))
        # dec run
        k = i
        while k + 1 < n and seq[k + 1] < seq[k]:
            k += 1
        if k - i + 1 >= min_len:
            dec.append((i, seq[i:k + 1]))
        i = max(i + 1, min(j, k) if j != i or k != i else i + 1)
        # simpler: just advance by 1
    # simpler sweep — use scan for maximal runs
    inc, dec = [], []
    if n >= 2:
        start = 0
        for t in range(1, n):
            if seq[t] > seq[t - 1]:
                continue
            run = seq[start:t]
            if len(run) >= min_len and all(run[u] < run[u + 1] for u in range(len(run) - 1)):
                inc.append((start, run))
            start = t
        run = seq[start:n]
        if len(run) >= min_len and all(run[u] < run[u + 1] for u in range(len(run) - 1)):
            inc.append((start, run))
        start = 0
        for t in range(1, n):
            if seq[t] < seq[t - 1]:
                continue
            run = seq[start:t]
            if len(run) >= min_len and all(run[u] > run[u + 1] for u in range(len(run) - 1)):
                dec.append((start, run))
            start = t
        run = seq[start:n]
        if len(run) >= min_len and all(run[u] > run[u + 1] for u in range(len(run) - 1)):
            dec.append((start, run))
    return {"inc": inc, "dec": dec}


def autocorr(seq: List[int], max_lag: int = 20) -> List[float]:
    n = len(seq)
    if n < 2:
        return []
    m = sum(seq) / n
    var = sum((x - m) ** 2 for x in seq) / n
    if var == 0:
        return [1.0] + [0.0] * (max_lag - 1)
    out = []
    for k in range(1, max_lag + 1):
        if k >= n:
            out.append(0.0)
            continue
        c = sum((seq[i] - m) * (seq[i + k] - m) for i in range(n - k)) / (n - k)
        out.append(c / var)
    return out


def dft_power(seq: List[int]) -> List[float]:
    """Return normalized power spectrum magnitudes for k=1..N/2.
    Normalized by total energy so peak is a fraction of energy."""
    n = len(seq)
    if n < 4:
        return []
    m = sum(seq) / n
    x = [v - m for v in seq]
    total_energy = sum(xi * xi for xi in x)
    if total_energy == 0:
        return []
    out = []
    for k in range(1, n // 2 + 1):
        re = sum(x[t] * math.cos(-2 * math.pi * k * t / n) for t in range(n))
        im = sum(x[t] * math.sin(-2 * math.pi * k * t / n) for t in range(n))
        power = (re * re + im * im) / n  # periodogram
        out.append(power)
    # normalize so they sum ~ total_energy/n/2 ish; return fractions of max
    return out


def main():
    surahs = load_quran("no-tashkeel")
    # build length sequence per surah
    seqs: Dict[int, List[int]] = {}
    meta: Dict[int, dict] = {}
    for s in surahs:
        seqs[s.id] = [graphemes(v.text) for v in s.verses]
        meta[s.id] = {"name": s.name, "translit": s.transliteration, "type": s.type,
                      "n": len(s.verses)}

    # -------------------- 1. extract sequences --------------------
    # dumped to file for record
    with open(os.path.join(OUT_DIR, "verse-length-sequences.json"), "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in seqs.items()}, f, ensure_ascii=False)

    # -------------------- 2. palindrome scan L=5,7,9 --------------------
    palindromes: Dict[int, Dict[int, List[Tuple[int, List[int]]]]] = {}
    palindrome_summary: List[dict] = []
    for L in (5, 7, 9):
        for s in surahs:
            seq = seqs[s.id]
            hits = find_palindromes(seq, L)
            for start, win in hits:
                # ignore degenerate all-equal palindromes (they are
                # technically palindromes but uninteresting — flag them)
                all_equal = all(x == win[0] for x in win)
                # first/last distinctness
                palindromes.setdefault(L, {}).setdefault(s.id, []).append((start, win, all_equal))
                palindrome_summary.append({
                    "surah": s.id, "name": s.transliteration, "L": L,
                    "start_verse": start + 1, "end_verse": start + L,
                    "window": win, "all_equal": all_equal,
                })

    # known targets
    known = [
        (91, 1, 7, [12, 14, 15, 15, 15, 14, 12]),
        (81, 2, 8, [16, 14, 14, 14, 14, 14, 16]),
        (37, 127, 133, [18, 19, 19, 14, 19, 19, 18]),
    ]
    verification = []
    for s_id, start, end, claimed in known:
        actual = seqs[s_id][start - 1:end]
        verification.append({
            "surah": s_id, "start": start, "end": end,
            "claimed": claimed, "actual": actual,
            "match": actual == claimed,
            "is_palindrome": is_pal(actual),
        })

    # -------------------- 3. monotonic runs len >= 5 --------------------
    mono_hits: List[dict] = []
    for s in surahs:
        seq = seqs[s.id]
        runs = find_monotonic_runs(seq, 5)
        for direction in ("inc", "dec"):
            for start, run in runs[direction]:
                mono_hits.append({
                    "surah": s.id, "name": s.transliteration, "dir": direction,
                    "start_verse": start + 1, "end_verse": start + len(run),
                    "length": len(run), "seq": run,
                })

    # -------------------- 4. autocorrelation / spectrum --------------------
    ac_sigs = []
    for s in surahs:
        seq = seqs[s.id]
        if len(seq) < 8:
            continue
        ac = autocorr(seq, max_lag=min(20, len(seq) // 2))
        spec = dft_power(seq)
        max_ac = max((abs(a), i + 1) for i, a in enumerate(ac)) if ac else (0, 0)
        # find max spectral peak as fraction of total
        total_spec = sum(spec) if spec else 0.0
        if total_spec > 0:
            top_idx, top_val = max(enumerate(spec), key=lambda p: p[1])
            # frequency k -> period = n / (top_idx+1)
            period = len(seq) / (top_idx + 1)
            frac = top_val / total_spec
        else:
            period, frac = 0.0, 0.0
        ac_sigs.append({
            "surah": s.id, "name": s.transliteration, "n": len(seq),
            "max_abs_autocorr": max_ac[0], "lag": max_ac[1],
            "top_period": period, "top_spec_frac": frac,
            "mean": sum(seq) / len(seq),
            "variance": (sum((x - sum(seq) / len(seq)) ** 2 for x in seq) / len(seq)),
        })

    # -------------------- 5. Ar-Rahman refrain partition --------------------
    # The refrain "fa-bi-ayyi ala'i rabbikuma tukadhdhiban" — Q 55 occurrences
    # per rahman-deep doc: 31 refrains partitioned 8+7+8+8
    rahman = surahs[54]  # id 55, index 54
    # identify refrain verses by matching the canonical phrase (no-tashkeel)
    refrain_letters_target = "فباي الاء ربكما تكذبان"
    refrain_verses = []
    for v in rahman.verses:
        # use approximate test on grapheme-stripped form
        txt = v.text.replace("ۚ", "").replace("ۛ", "").replace("ۖ", "").strip()
        # simpler: contains "تكذبان"
        if "تكذبان" in v.text:
            refrain_verses.append(v.id)
    # partition into blocks: gaps where successive refrain_verses skip verses form partitions
    rahman_seq = seqs[55]
    # partitions = verses BETWEEN refrains — we also include pre-first-refrain segment
    partitions: List[Tuple[int, int, List[int]]] = []
    prev = 0
    for rv in refrain_verses:
        if rv - 1 > prev:
            start = prev + 1
            end = rv - 1
            partitions.append((start, end, rahman_seq[start - 1:end]))
        prev = rv
    if prev < len(rahman_seq):
        partitions.append((prev + 1, len(rahman_seq), rahman_seq[prev:]))

    # per rahman-deep note, canonical partition count is 8+7+8+8 = 31 refrains
    rahman_out = {
        "n_refrains": len(refrain_verses),
        "refrain_verses": refrain_verses,
        "n_verses": len(rahman_seq),
        "mean_length": sum(rahman_seq) / len(rahman_seq),
        "partition_count": len(partitions),
        "partitions": [{"start": s, "end": e, "len": e - s + 1, "seq": q,
                        "sum_letters": sum(q), "mean": sum(q) / len(q) if q else 0}
                       for s, e, q in partitions],
        "sequence": rahman_seq,
    }

    # -------------------- 6. Unusual spectral signature --------------------
    # flag surahs whose top-spec-fraction is very high (energy concentration)
    ac_sigs.sort(key=lambda r: -r["top_spec_frac"])
    # top concentrations among surahs with n >= 15 (to get meaningful DFT)
    spec_out = [r for r in ac_sigs if r["n"] >= 15][:25]

    # -------------------- 7. base rate / null --------------------
    # rough base rate for length-L palindrome in random integer sequence
    # computed empirically: shuffle all verse lengths within each surah
    import random
    rng = random.Random(42)
    null_counts = {5: [], 7: [], 9: []}
    trials = 200
    for _ in range(trials):
        c5 = c7 = c9 = 0
        for s in surahs:
            seq = list(seqs[s.id])
            rng.shuffle(seq)
            for L, ref in ((5, c5), (7, c7), (9, c9)):
                pass
            c5 += sum(1 for (i, w) in find_palindromes(seq, 5) if not all(x == w[0] for x in w))
            c7 += sum(1 for (i, w) in find_palindromes(seq, 7) if not all(x == w[0] for x in w))
            c9 += sum(1 for (i, w) in find_palindromes(seq, 9) if not all(x == w[0] for x in w))
        null_counts[5].append(c5)
        null_counts[7].append(c7)
        null_counts[9].append(c9)

    observed = {}
    for L in (5, 7, 9):
        observed[L] = sum(1 for e in palindrome_summary if e["L"] == L and not e["all_equal"])

    null_summary = {
        L: {
            "observed_nontrivial": observed[L],
            "null_mean": sum(null_counts[L]) / trials,
            "null_p95": sorted(null_counts[L])[int(0.95 * trials)],
            "null_min": min(null_counts[L]),
            "null_max": max(null_counts[L]),
            "trials": trials,
        }
        for L in (5, 7, 9)
    }

    # -------------------- write results --------------------
    with open(os.path.join(OUT_DIR, "palindromes.json"), "w", encoding="utf-8") as f:
        json.dump(palindrome_summary, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "monotonic.json"), "w", encoding="utf-8") as f:
        json.dump(mono_hits, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "verification.json"), "w", encoding="utf-8") as f:
        json.dump(verification, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "ac_signatures.json"), "w", encoding="utf-8") as f:
        json.dump(ac_sigs, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "rahman_refrain.json"), "w", encoding="utf-8") as f:
        json.dump(rahman_out, f, ensure_ascii=False, indent=1)
    with open(os.path.join(OUT_DIR, "null_summary.json"), "w", encoding="utf-8") as f:
        json.dump(null_summary, f, ensure_ascii=False, indent=1)

    # print highlights for quick review
    print("=== VERIFICATION ===")
    for r in verification:
        print(r)
    print("=== PALINDROME COUNTS (non-trivial) ===")
    for L in (5, 7, 9):
        non_trivial = [e for e in palindrome_summary if e["L"] == L and not e["all_equal"]]
        print(f"L={L}: {len(non_trivial)} non-trivial (of "
              f"{sum(1 for e in palindrome_summary if e['L']==L)} raw hits)")
    print("=== NULL COMPARISON ===")
    for L in (5, 7, 9):
        r = null_summary[L]
        print(f"L={L}: obs={r['observed_nontrivial']}  null-mean={r['null_mean']:.1f}  "
              f"null-p95={r['null_p95']}  range=[{r['null_min']},{r['null_max']}]")
    print("=== MONOTONIC >= 5 ===")
    for r in mono_hits:
        print(r)
    print("=== TOP SPECTRAL CONCENTRATIONS (n>=15) ===")
    for r in spec_out[:15]:
        print(r)
    print("=== RAHMAN ===")
    print("refrains:", rahman_out["n_refrains"],
          "partitions:", rahman_out["partition_count"])
    for p in rahman_out["partitions"]:
        print(p)


if __name__ == "__main__":
    main()
