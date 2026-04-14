#!/usr/bin/env python3
"""
Analyze baseline classical Arabic corpora and compare to the Quran.

Tasks:
  1. Per-corpus basic stats (bytes, words, letters, vocab, Zipf, letter freq)
  2. Quran reference stats from quran-text/quran-no-tashkeel.json
  3. Critical test 1: matching-count word-pair denominator
  4. Critical test 2: thematic concentration null rate
       (chunk a baseline corpus into 114 size-distribution-matched chunks
        and ask: how often does a word with frequency f land all instances
        in a single chunk?)
  5. Critical test 4: chiasmus / ring ratios on Mu'allaqat
  6. Letter-frequency comparison with binomial CIs
  7. Word-frequency Zipf comparison
"""
from __future__ import annotations

import csv
import json
import math
import random
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
RAW = ROOT / "data" / "baseline-corpora" / "raw"
OUT = ROOT / "data" / "baseline-corpora"
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"

# Letter range from methodology §3: U+0621..064A ∪ U+0671..06D3
ARABIC_LETTERS = set()
for cp in range(0x0621, 0x064B):
    ARABIC_LETTERS.add(chr(cp))
for cp in range(0x0671, 0x06D4):
    ARABIC_LETTERS.add(chr(cp))

# Recitation mark range to filter out (matches methodology)
REC_MARKS = set(chr(c) for c in range(0x06D6, 0x06EE))

# Arabic diacritics (tashkeel) to strip from baseline texts
TASHKEEL = set(chr(c) for c in range(0x064B, 0x0660))  # fatha..sukun
TASHKEEL |= {chr(0x0670), chr(0x0640)}  # superscript alif, tatweel

# Punctuation/digits to drop from token streams
ARABIC_DIGITS = set(chr(c) for c in range(0x0660, 0x066A))
WESTERN_DIGITS = set("0123456789")
PUNCT = set(",.;:!?()[]{}\"'/-—–…«»‹›؟،؛٪٠٫٬·")


def strip_tashkeel(s: str) -> str:
    return "".join(ch for ch in s if ch not in TASHKEEL)


def is_arabic_letter(ch: str) -> bool:
    return ch in ARABIC_LETTERS


def normalize(s: str) -> str:
    """Normalize: drop tashkeel, drop recitation marks, drop digits/punct,
    keep only Arabic letter graphemes plus single spaces between tokens."""
    s = strip_tashkeel(s)
    out = []
    for ch in s:
        if ch in REC_MARKS:
            continue
        if is_arabic_letter(ch):
            out.append(ch)
        elif ch in ARABIC_DIGITS or ch in WESTERN_DIGITS:
            out.append(" ")
        elif ch.isspace():
            out.append(" ")
        else:
            out.append(" ")
    s = "".join(out)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def tokenize(s: str) -> list[str]:
    return [t for t in s.split() if t]


def letter_count(s: str) -> int:
    return sum(1 for ch in s if is_arabic_letter(ch))


def letter_freqs(s: str) -> dict[str, int]:
    c: Counter[str] = Counter()
    for ch in s:
        if is_arabic_letter(ch):
            c[ch] += 1
    return dict(c)


def zipf_exponent(token_counts: list[int]) -> float:
    """Fit log f = -alpha log r + c by least squares on top tokens."""
    if len(token_counts) < 10:
        return float("nan")
    counts = sorted(token_counts, reverse=True)
    # Use top min(2000, len) tokens
    n = min(len(counts), 2000)
    xs = [math.log(r + 1) for r in range(n)]
    ys = [math.log(counts[r]) for r in range(n)]
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den == 0:
        return float("nan")
    slope = num / den
    return -slope  # alpha (positive)


def basic_stats(name: str, raw_text: str) -> dict:
    norm = normalize(raw_text)
    tokens = tokenize(norm)
    letters = letter_count(norm)
    lf = letter_freqs(norm)
    counts = Counter(tokens)
    return {
        "name": name,
        "bytes": len(raw_text.encode("utf-8")),
        "raw_chars": len(raw_text),
        "norm_chars": len(norm),
        "tokens": len(tokens),
        "vocab": len(counts),
        "letters": letters,
        "zipf_alpha": round(zipf_exponent(list(counts.values())), 4),
        "letter_freqs": lf,
        "tokens_list": tokens,  # keep for downstream tests
    }


def load_quran_text() -> str:
    with QURAN_JSON.open() as f:
        d = json.load(f)
    parts = []
    for surah in d:
        for verse in surah["verses"]:
            parts.append(verse["text"])
    return " ".join(parts)


def per_surah_token_lists() -> list[list[str]]:
    with QURAN_JSON.open() as f:
        d = json.load(f)
    out = []
    for surah in d:
        toks = []
        for verse in surah["verses"]:
            toks.extend(tokenize(normalize(verse["text"])))
        out.append(toks)
    return out


# ---------- Critical Test 1: matching-count pairs ----------

def matching_pair_denominator(tokens: list[str], min_count: int = 10) -> dict:
    """Compute the analog of the §8 root-cartographer pair denominator
    on a token corpus. Returns total tied unordered pairs and the
    distribution of group sizes."""
    counts = Counter(tokens)
    # restrict to types with frequency >= min_count
    filtered = [(t, c) for t, c in counts.items() if c >= min_count]
    by_count: dict[int, int] = Counter(c for _, c in filtered)
    # number of unordered pairs in groups of size k is C(k,2)
    pairs = 0
    n_tied_groups = 0
    for k in by_count.values():
        if k >= 2:
            pairs += k * (k - 1) // 2
            n_tied_groups += 1
    return {
        "n_types_above_threshold": len(filtered),
        "tied_groups": n_tied_groups,
        "tied_pair_count": pairs,
        "max_group_size": max(by_count.values()) if by_count else 0,
    }


# ---------- Critical Test 2: thematic concentration ----------

def chunk_into_n(tokens: list[str], n: int, surah_lengths: list[int]) -> list[list[str]]:
    """Chunk tokens into n parts whose sizes match the given length distribution
    (rescaled to total tokens). Returns the chunks."""
    total = len(tokens)
    target = sum(surah_lengths)
    chunks = []
    start = 0
    for sl in surah_lengths:
        size = max(1, round(sl * total / target))
        end = min(total, start + size)
        chunks.append(tokens[start:end])
        start = end
        if start >= total:
            break
    # consume any remainder
    if start < total and chunks:
        chunks[-1].extend(tokens[start:])
    # If we ran out before assigning all chunks, pad with empty
    while len(chunks) < n:
        chunks.append([])
    return chunks


def concentration_test(tokens: list[str], surah_lengths: list[int],
                       freq_target: int) -> dict:
    """Of all word-types with total frequency exactly freq_target,
    how many appear entirely within a single chunk?
    Returns count + total qualifying types."""
    chunks = chunk_into_n(tokens, len(surah_lengths), surah_lengths)
    type_counts = Counter(tokens)
    candidates = [t for t, c in type_counts.items() if c == freq_target]
    total = len(candidates)
    concentrated = 0
    for tok in candidates:
        chunks_used = set()
        for i, ch in enumerate(chunks):
            if tok in ch:
                chunks_used.add(i)
                if len(chunks_used) > 1:
                    break
        if len(chunks_used) == 1:
            concentrated += 1
    return {
        "freq_target": freq_target,
        "total_types": total,
        "single_chunk_types": concentrated,
        "rate": concentrated / total if total else 0.0,
    }


def quran_concentration(per_surah: list[list[str]], freq_target: int) -> dict:
    """Quran analog: of all word-types with total frequency exactly freq_target,
    how many appear in only one surah?"""
    type_counts: Counter[str] = Counter()
    type_surahs: dict[str, set[int]] = {}
    for i, toks in enumerate(per_surah):
        for t in toks:
            type_counts[t] += 1
            type_surahs.setdefault(t, set()).add(i)
    candidates = [t for t, c in type_counts.items() if c == freq_target]
    total = len(candidates)
    single = sum(1 for t in candidates if len(type_surahs[t]) == 1)
    return {
        "freq_target": freq_target,
        "total_types": total,
        "single_surah_types": single,
        "rate": single / total if total else 0.0,
    }


# ---------- Critical Test 4: chiasmus / ring ratios ----------

def ring_score(tokens: list[str]) -> float:
    """Simple ring score: sum over symmetric pairs (i, n-1-i) of token equality
    weighted by 1/(distance to centre + 1)."""
    n = len(tokens)
    if n < 4:
        return 0.0
    score = 0.0
    half = n // 2
    matches = 0
    for i in range(half):
        if tokens[i] == tokens[n - 1 - i]:
            matches += 1
            score += 1.0
    return matches / half if half else 0.0


# ---------- main pipeline ----------

def main():
    files = sorted(p for p in RAW.glob("*.txt") if "raw.txt" not in p.name and "openiti.raw" not in p.name)
    print(f"Found {len(files)} corpus files", file=sys.stderr)

    quran_raw = load_quran_text()
    quran = basic_stats("quran-no-tashkeel", quran_raw)
    quran_per_surah = per_surah_token_lists()
    quran_surah_lengths = [len(s) for s in quran_per_surah]

    all_stats = [quran]
    print(f"Quran loaded: {quran['tokens']} tokens, {quran['letters']} letters", file=sys.stderr)

    for f in files:
        text = f.read_text(encoding="utf-8")
        st = basic_stats(f.stem, text)
        all_stats.append(st)
        print(f"  {f.stem}: {st['tokens']} tokens, {st['letters']} letters", file=sys.stderr)

    # ---------- write basic stats CSV ----------
    out_csv = OUT / "baseline-stats.csv"
    with out_csv.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow([
            "name", "bytes", "raw_chars", "norm_chars", "tokens", "vocab",
            "letters", "type_token_ratio", "zipf_alpha"
        ])
        for s in all_stats:
            ttr = s["vocab"] / s["tokens"] if s["tokens"] else 0
            w.writerow([
                s["name"], s["bytes"], s["raw_chars"], s["norm_chars"],
                s["tokens"], s["vocab"], s["letters"],
                round(ttr, 4), s["zipf_alpha"]
            ])
    print(f"Wrote {out_csv}", file=sys.stderr)

    # ---------- letter frequency CSV (relative %) ----------
    out_lfcsv = OUT / "letter-freqs.csv"
    all_letters = sorted({l for s in all_stats for l in s["letter_freqs"]})
    with out_lfcsv.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["name"] + all_letters)
        for s in all_stats:
            tot = sum(s["letter_freqs"].values())
            row = [s["name"]] + [
                round(s["letter_freqs"].get(l, 0) / tot, 5) if tot else 0
                for l in all_letters
            ]
            w.writerow(row)
    print(f"Wrote {out_lfcsv}", file=sys.stderr)

    # ---------- Critical test 1: matching-count word pairs ----------
    print("\n=== Critical Test 1: matching-count word pairs ===", file=sys.stderr)
    test1 = []
    for s in all_stats:
        d = matching_pair_denominator(s["tokens_list"], min_count=10)
        d["name"] = s["name"]
        d["tokens"] = s["tokens"]
        test1.append(d)
        print(f"  {s['name']}: {d['n_types_above_threshold']} types ≥10, "
              f"{d['tied_pair_count']} tied pairs, {d['tied_groups']} tied groups",
              file=sys.stderr)
    with (OUT / "test1-matching-pairs.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["name", "tokens", "n_types_above_threshold",
                                            "tied_groups", "tied_pair_count",
                                            "max_group_size"])
        w.writeheader()
        for d in test1:
            w.writerow(d)

    # ---------- Critical test 2: thematic concentration ----------
    print("\n=== Critical Test 2: thematic concentration ===", file=sys.stderr)

    # Combine baseline corpora to ~Quran-length pools to test the concentration null
    big_corpora = {
        "bukhari": next(s for s in all_stats if s["name"] == "bukhari"),
        "jahiz-hayawan": next(s for s in all_stats if s["name"] == "jahiz-hayawan"),
        "sira-ibn-hisham": next(s for s in all_stats if s["name"] == "sira-ibn-hisham"),
    }
    test2_rows = []

    # Quran reference: of all token-types with frequency exactly k,
    # how many are concentrated in a single surah?
    for freq in [5, 6, 8, 10, 12, 15, 20]:
        qd = quran_concentration(quran_per_surah, freq)
        qd["corpus"] = "quran (real surahs)"
        test2_rows.append(qd)
        print(f"  Quran freq={freq}: {qd['single_surah_types']}/{qd['total_types']} "
              f"= {qd['rate']:.3f}", file=sys.stderr)
        for cname, cs in big_corpora.items():
            cd = concentration_test(cs["tokens_list"], quran_surah_lengths, freq)
            cd["corpus"] = cname
            test2_rows.append(cd)
            print(f"    {cname} freq={freq}: {cd['single_chunk_types']}/{cd['total_types']} "
                  f"= {cd['rate']:.3f}", file=sys.stderr)

    with (OUT / "test2-concentration.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["corpus", "freq_target", "total_types",
                                            "single_chunk_types", "single_surah_types", "rate"])
        w.writeheader()
        for r in test2_rows:
            w.writerow({
                "corpus": r["corpus"],
                "freq_target": r["freq_target"],
                "total_types": r["total_types"],
                "single_chunk_types": r.get("single_chunk_types", ""),
                "single_surah_types": r.get("single_surah_types", ""),
                "rate": round(r["rate"], 4),
            })

    # ---------- Critical test 4: ring scores on Mu'allaqat ----------
    print("\n=== Critical Test 4: ring scores ===", file=sys.stderr)
    ring_rows = []
    for s in all_stats:
        if s["name"].startswith("muallaqa-") or s["name"] == "quran-no-tashkeel":
            ring = ring_score(s["tokens_list"])
            ring_rows.append({"name": s["name"], "tokens": s["tokens"], "ring_score": round(ring, 4)})
            print(f"  {s['name']}: ring={ring:.4f}", file=sys.stderr)
    # Per-surah ring scores
    print("  -- per-surah Quran ring scores --", file=sys.stderr)
    surah_rings = []
    for i, toks in enumerate(quran_per_surah):
        if len(toks) >= 10:
            r = ring_score(toks)
            surah_rings.append((i + 1, len(toks), r))
    top_rings = sorted(surah_rings, key=lambda x: -x[2])[:10]
    for sid, n, r in top_rings:
        print(f"    surah {sid} ({n} tok): ring={r:.4f}", file=sys.stderr)

    with (OUT / "test4-ring-scores.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["corpus", "tokens", "ring_score"])
        for r in ring_rows:
            w.writerow([r["name"], r["tokens"], r["ring_score"]])
        w.writerow(["", "", ""])
        w.writerow(["surah_id", "tokens", "ring_score"])
        for sid, n, r in surah_rings:
            w.writerow([sid, n, round(r, 4)])

    # ---------- summary JSON ----------
    summary = {
        "n_corpora": len(files),
        "quran_tokens": quran["tokens"],
        "quran_vocab": quran["vocab"],
        "quran_letters": quran["letters"],
        "test1_quran_pairs": next(d["tied_pair_count"] for d in test1
                                   if d["name"] == "quran-no-tashkeel"),
        "test1_quran_types": next(d["n_types_above_threshold"] for d in test1
                                   if d["name"] == "quran-no-tashkeel"),
    }
    with (OUT / "analysis-summary.json").open("w") as fh:
        json.dump(summary, fh, indent=2)
    print(f"\n{json.dumps(summary, indent=2)}", file=sys.stderr)


if __name__ == "__main__":
    main()
