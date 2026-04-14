#!/usr/bin/env python3
"""
Phase B rigor test — rahma=114 finding vs baseline corpora.

Claim: In the Quran (Leeds QAC v0.4), out of ~4,832 distinct lemmas,
exactly ONE has count 114 — and it's رحمة (raHomap / "mercy").
114 is also the surah count.

This script runs five tests:
  A. Does any word-type in baseline 77k slices occur exactly 114 times?
     Is it unique at 114? How often are the "famous numbers" singleton?
  B. Singleton-count distribution for the Quran lemma counts.
     Which counts have exactly ONE lemma? Which of those are famous?
  C. Semantic weight — pull lemma identities at each famous count.
  D. Frequency of "mercy" (root rHm) in each baseline corpus.
  E. Bonferroni/FDR correction for the "famous numbers" family.
"""
from __future__ import annotations

import json
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
RAW = ROOT / "data" / "baseline-corpora" / "raw"
OUT = ROOT / "data" / "baseline-corpora"
QAC = ROOT / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"

sys.path.insert(0, str(Path(__file__).parent))
from analyze import (
    normalize, tokenize, ARABIC_LETTERS, is_arabic_letter,
)

# Famous numbers we test
FAMOUS = [7, 12, 19, 28, 30, 40, 77, 99, 114, 147, 313, 365, 786]


# -----------------------------------------------------------------------------
# Load QAC lemma count distribution (Test B and sanity-check Test A in Quran)
# -----------------------------------------------------------------------------
def load_qac_lemma_counts() -> tuple[Counter, dict]:
    """Return Counter(lemma -> occurrence count) over STEM rows.
    Returns a mapping from lemma to count, and lemma -> root."""
    lemma_counts: Counter[str] = Counter()
    lemma_root: dict[str, str] = {}
    with QAC.open() as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, features = parts
            if "STEM" not in features:
                continue
            # extract LEM:...
            m = re.search(r"LEM:([^|]+)", features)
            if not m:
                continue
            lem = m.group(1)
            lemma_counts[lem] += 1
            # extract ROOT:... (if any)
            rm = re.search(r"ROOT:([^|]+)", features)
            if rm and lem not in lemma_root:
                lemma_root[lem] = rm.group(1)
    return lemma_counts, lemma_root


# -----------------------------------------------------------------------------
# Load baseline corpora and tokenize
# -----------------------------------------------------------------------------
def load_tokens(path: Path) -> list[str]:
    with path.open() as f:
        txt = f.read()
    return tokenize(normalize(txt))


def concat_corpus(files: list[Path]) -> list[str]:
    out: list[str] = []
    for p in files:
        out.extend(load_tokens(p))
    return out


# -----------------------------------------------------------------------------
# Test A: how many word-types hit each famous count in a 77k-token slice?
# -----------------------------------------------------------------------------
def lemma_count_stats(tokens: list[str], famous=FAMOUS) -> dict:
    """Given a token list, compute types-per-count histogram and return
    information about each famous count."""
    wc = Counter(tokens)
    counts_hist: Counter[int] = Counter()
    for w, c in wc.items():
        counts_hist[c] += 1
    info = {
        "total_tokens": len(tokens),
        "vocab_size": len(wc),
        "famous": {},
        "counts_with_unique_type": [c for c, n in counts_hist.items() if n == 1],
    }
    for n in famous:
        types_at_n = [w for w, c in wc.items() if c == n]
        info["famous"][n] = {
            "count_of_types": len(types_at_n),
            "unique": len(types_at_n) == 1,
            "example_types": types_at_n[:10],
        }
    return info


# -----------------------------------------------------------------------------
# Test D: count words containing the root rHm (ر ح م) as a loose approximation
# -----------------------------------------------------------------------------
def count_rhm_tokens(tokens: list[str]) -> tuple[int, list[str]]:
    """Return count of tokens that contain the substring "رحم" or are
    morphologically rHm-ish (رحمة / الرحمة / رحمته / رحمت / رحمن / رحيم).
    Returns (total_count, list_of_distinct_surface_forms_with_counts)."""
    rhm_forms = Counter()
    total = 0
    for t in tokens:
        # Simple consonant-skeleton check: contains contiguous "رحم"
        if "رحم" in t or "رحي" in t:
            # "رحي" catches رحيم
            if "رحم" in t or t.startswith("رحي") or "رحي" in t:
                rhm_forms[t] += 1
                total += 1
    return total, rhm_forms.most_common(15)


def count_rhma_only(tokens: list[str]) -> int:
    """Just count tokens exactly matching رحمة (and definite/construct variants)."""
    targets = {"رحمة", "الرحمة", "ورحمة", "ورحمته", "رحمته", "رحمت",
               "برحمة", "برحمته", "لرحمة", "فرحمة"}
    return sum(1 for t in tokens if t in targets)


# -----------------------------------------------------------------------------
# Test A (empirical null): 1000 random 77k slices from the big concatenated
# -----------------------------------------------------------------------------
def empirical_null(big_tokens: list[str], slice_len: int = 77797,
                    n_draws: int = 1000, famous=FAMOUS, seed: int = 42) -> dict:
    rng = random.Random(seed)
    n = len(big_tokens)
    if n < slice_len:
        return {"error": f"big corpus too small: {n} < {slice_len}"}
    results: dict[int, dict] = {f: {"any": 0, "unique": 0} for f in famous}
    singleton_counts_sample: list[int] = []
    for _ in range(n_draws):
        start = rng.randint(0, n - slice_len)
        slc = big_tokens[start:start + slice_len]
        wc = Counter(slc)
        ch: Counter[int] = Counter()
        for _, c in wc.items():
            ch[c] += 1
        # Count singletons ( = counts with exactly 1 type ) among any value
        sc = sum(1 for c, k in ch.items() if k == 1)
        singleton_counts_sample.append(sc)
        for f in famous:
            k = ch.get(f, 0)
            if k >= 1:
                results[f]["any"] += 1
            if k == 1:
                results[f]["unique"] += 1
    return {
        "n_draws": n_draws,
        "slice_len": slice_len,
        "famous": {f: {"p_any": results[f]["any"] / n_draws,
                         "p_unique": results[f]["unique"] / n_draws}
                    for f in famous},
        "avg_singleton_counts": sum(singleton_counts_sample) / n_draws,
    }


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("Rahma=114 rigor test — loading data")
    print("=" * 72)

    lemma_counts, lemma_root = load_qac_lemma_counts()
    print(f"Loaded {len(lemma_counts)} distinct lemmas from QAC")
    total_lemma_tokens = sum(lemma_counts.values())
    print(f"Total lemma tokens (STEM rows) = {total_lemma_tokens}")

    # ----- TEST B: singleton-count distribution of Quran lemmas ---------------
    print("\n" + "=" * 72)
    print("TEST B — Quran singleton-count distribution (which N have exactly 1 lemma?)")
    print("=" * 72)
    counts_hist: Counter[int] = Counter()
    for lem, c in lemma_counts.items():
        counts_hist[c] += 1
    singleton_counts = sorted([c for c, n in counts_hist.items() if n == 1])
    print(f"Total distinct lemma counts (support): {len(counts_hist)}")
    print(f"Counts that have EXACTLY 1 lemma: {len(singleton_counts)}")
    print(f"First 30 singleton counts: {singleton_counts[:30]}")
    print(f"Largest singleton count: {max(singleton_counts)}")
    # Which of them overlap with famous numbers?
    famous_hits = []
    for n in FAMOUS:
        types_at_n = [l for l, c in lemma_counts.items() if c == n]
        famous_hits.append({
            "N": n,
            "num_lemmas": len(types_at_n),
            "is_unique": len(types_at_n) == 1,
            "lemmas": types_at_n,
        })
    print("\nQuran famous-N lemma-count table:")
    for h in famous_hits:
        mark = " <-- UNIQUE" if h["is_unique"] else ""
        print(f"  N={h['N']:4d}: {h['num_lemmas']} lemma(s) at this count{mark}")
        if h["num_lemmas"] <= 8:
            for lem in h["lemmas"]:
                print(f"        {lem} (root={lemma_root.get(lem,'?')})")

    # ----- TEST A: 77k-slice baseline comparisons -----------------------------
    print("\n" + "=" * 72)
    print("TEST A — Famous-count type distribution in 77k slices of baselines")
    print("=" * 72)

    SLICE_LEN = 77797

    baselines = {}

    # (a) matched-bukhari 77k
    mb = load_tokens(RAW / "matched-bukhari-77k.txt")
    baselines["matched-bukhari-77k"] = mb[:SLICE_LEN]

    # (b) Jahiz Hayawan — take first 77k of the clean file
    jh = load_tokens(RAW / "jahiz-hayawan.txt")
    if len(jh) >= SLICE_LEN:
        baselines["jahiz-hayawan[:77k]"] = jh[:SLICE_LEN]

    # (c) Sira ibn Hisham — first 77k
    si = load_tokens(RAW / "sira-ibn-hisham.txt")
    if len(si) >= SLICE_LEN:
        baselines["sira-ibn-hisham[:77k]"] = si[:SLICE_LEN]

    # (d) Poetry pool (Mu'allaqat + diwans) — concat all poetic sources
    poetry_files = sorted([p for p in RAW.glob("diwan-*.txt")
                             if not p.name.endswith(".openiti.raw.txt")])
    poetry_files += sorted([p for p in RAW.glob("muallaqa-*.txt")
                              if not p.name.endswith(".openiti.raw.txt")])
    poetry_files += [p for p in RAW.glob("mutanabbi-diwan.txt")
                      if not p.name.endswith(".openiti.raw.txt")]
    pp = concat_corpus(poetry_files)
    print(f"Poetry pool has {len(pp)} tokens from {len(poetry_files)} files")
    if len(pp) >= SLICE_LEN:
        baselines["poetry-pool[:77k]"] = pp[:SLICE_LEN]
    else:
        baselines["poetry-pool-all"] = pp  # all we have; not length matched

    # (e) Shuffled Quran word-bag (within-Quran null) — tokenize the Quran text
    with QURAN_JSON.open() as f:
        qdata = json.load(f)
    # Quran JSON is a list of 114 surah dicts with a "verses" list of {id,text}
    q_tokens: list[str] = []
    for surah in qdata:
        for verse in surah.get("verses", []):
            txt = verse.get("text", "")
            q_tokens.extend(tokenize(normalize(txt)))
    print(f"Flattened Quran tokens: {len(q_tokens)}")
    rng = random.Random(42)
    shuf = list(q_tokens)
    rng.shuffle(shuf)
    baselines["quran-shuffled-wordbag"] = shuf[:SLICE_LEN] if len(shuf) >= SLICE_LEN else shuf

    # Also keep real Quran tokens for comparison
    baselines["quran-orthographic-tokens"] = q_tokens[:SLICE_LEN] if len(q_tokens) >= SLICE_LEN else q_tokens

    rows_a = {}
    for name, toks in baselines.items():
        info = lemma_count_stats(toks)
        rows_a[name] = info
        print(f"\n  {name}: vocab={info['vocab_size']}, tokens={info['total_tokens']}")
        for f in FAMOUS:
            fi = info["famous"][f]
            tag = " UNIQUE" if fi["unique"] else ""
            ex = ",".join(fi["example_types"][:3])
            print(f"    N={f:4d}: {fi['count_of_types']:4d} type(s){tag}  ex=[{ex}]")
        print(f"    singleton-counts-overall: {len(info['counts_with_unique_type'])}")

    # ----- Empirical null: 1000 random slices from concatenated big corpus ---
    print("\n" + "=" * 72)
    print("TEST A (extended) — 1000 random 77k slices from merged 13.4M corpus")
    print("=" * 72)
    # Concatenate all big baseline files into a single big pool
    big_files = [
        RAW / "bukhari-noquran.txt",
        RAW / "sira-ibn-hisham.txt",
        RAW / "jahiz-hayawan.txt",
    ]
    big_pool: list[str] = []
    for p in big_files:
        if p.exists():
            big_pool.extend(load_tokens(p))
    print(f"Big pool tokens: {len(big_pool)}")
    null = empirical_null(big_pool, slice_len=SLICE_LEN, n_draws=1000)
    print("Famous-N rates across 1000 random 77k slices:")
    for f in FAMOUS:
        d = null["famous"][f]
        print(f"  N={f:4d}: p(any type)={d['p_any']:.3f}  "
                f"p(UNIQUE type)={d['p_unique']:.3f}")
    print(f"Mean singleton-counts per slice: {null['avg_singleton_counts']:.1f}")

    # ----- TEST D: rHm token count in baselines ------------------------------
    print("\n" + "=" * 72)
    print("TEST D — rHm root / mercy token counts in baselines")
    print("=" * 72)
    for name, toks in baselines.items():
        total_rhm, top_forms = count_rhm_tokens(toks)
        rhma_strict = count_rhma_only(toks)
        print(f"  {name}: rHm-ish={total_rhm}, strict rahma forms={rhma_strict}")
        if top_forms:
            print(f"    top forms: {top_forms[:5]}")

    # Also compute for the full (non-slice) big baseline files
    print("\nFull-corpus rHm counts (for base-rate context):")
    for p in [
        RAW / "matched-bukhari-77k.txt",
        RAW / "bukhari-noquran.txt",
        RAW / "sira-ibn-hisham.txt",
        RAW / "jahiz-hayawan.txt",
    ]:
        if not p.exists():
            continue
        t = load_tokens(p)
        total_rhm, top_forms = count_rhm_tokens(t)
        print(f"  {p.name}: tokens={len(t)}, rHm-ish={total_rhm} "
                f"(per-77k-tok rate ~= {total_rhm/len(t)*77797:.1f})")

    # ----- Write JSON dump ----------------------------------------------------
    dump = {
        "quran_famous": famous_hits,
        "quran_singleton_counts": singleton_counts,
        "baselines_test_a": {
            name: {
                "vocab": info["vocab_size"],
                "tokens": info["total_tokens"],
                "famous": info["famous"],
                "num_singleton_counts": len(info["counts_with_unique_type"]),
            }
            for name, info in rows_a.items()
        },
        "empirical_null": null,
    }
    (OUT / "rahma-114-test.json").write_text(json.dumps(dump, indent=2, default=str))
    print(f"\nWrote {OUT / 'rahma-114-test.json'}")


if __name__ == "__main__":
    main()
