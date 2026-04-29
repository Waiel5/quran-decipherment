#!/usr/bin/env python3
"""H-NEW-58 — empirical structural twinning of classically-paired surahs.

Pre-reg: findings/phase-b-hypotheses/h-new-58-surah-pair-twinning-prereg.md

4 classical pairs (locked):
  P_zahrawan       Q  2 + Q  3   (al-Zahrāwān; both الم openers)
  P_anfal_tawba    Q  8 + Q  9   (al-Tawba lacks basmala)
  P_muawwidhatan   Q113 + Q114   (al-muʿawwidhatān)
  P_muzz_mudd      Q 73 + Q 74   (al-Muzzammil + al-Muddaththir)

5 axes (locked):
  A1 lexical-root-jaccard
  A2 mean-verse-length-similarity
  A3 rhyme-class-entropy-similarity
  A4 divine-name-density-similarity
  A5 hapax-density-similarity

Bonferroni-20 (4 pairs × 5 axes), α_bon = 0.0025.
Null = 10 000 random adjacent surah pairs (i, i+1), excluding the actual
pair under test. Seed 20260416.

PASS criterion: ≥ 2 of 4 pairs significant on ≥ 2 of 5 axes at α_bon.
MW-5: P_muawwidhatan must show p < 0.001 on ≥ 2 axes (else instrument
bug; do not declare H-NEW-58 PASS or NULL).
"""
from __future__ import annotations

import csv
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260416
N_NULL = 10_000
ALPHA_BON = 0.05 / 20  # = 0.0025
N_PAIRS = 4
N_AXES = 5

CLASSICAL_PAIRS = [
    ("P_zahrawan",     2,   3),
    ("P_anfal_tawba",  8,   9),
    ("P_muawwidhatan", 113, 114),
    ("P_muzz_mudd",    73,  74),
]

AXES = ["A1_root_jaccard", "A2_verse_len", "A3_rhyme_entropy",
        "A4_divine_density", "A5_hapax_density"]


# ---------------- Loaders ----------------

def load_quran_no_tashkeel():
    path = REPO / "quran-text" / "quran-no-tashkeel.json"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def load_qac_roots_per_surah():
    """Return dict surah_id -> list of root strings (one per stem-token).

    Also return corpus-wide root count Counter for hapax detection.
    """
    per_surah: dict[int, list[str]] = defaultdict(list)
    corpus_count: Counter = Counter()
    path = REPO / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            feat = parts[3]
            if "STEM" not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            per_surah[sid].append(root)
            corpus_count[root] += 1
    return per_surah, corpus_count


def load_divine_density():
    """Return dict surah_id -> divine-name density (sum num_names / verse count)."""
    csv_path = REPO / "findings" / "phase-b-hypotheses" / "divine-names-by-verse.csv"
    name_sum: Counter = Counter()
    verse_set: dict[int, set[int]] = defaultdict(set)
    with csv_path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            sid = int(row["surah"])
            vid = int(row["verse"])
            name_sum[sid] += int(row["num_names"])
            verse_set[sid].add(vid)
    # Note: divine-names-by-verse.csv only contains rows for verses with
    # ≥1 name. Per-verse density must use the FULL surah verse count.
    return name_sum


# ---------------- Per-surah feature extraction ----------------

def strip_basmala_in_q1(quran):
    """Match the project rule: basmala is verse 1 of surah 1 only;
    other surahs' basmala is NOT in the JSON. Nothing to strip globally."""
    return quran


def per_surah_features(quran, qac_per_surah, corpus_root_count, divine_sum):
    """Compute per-surah scalars for each axis.

    Returns:
      verse_len_mean[sid]  -- A2
      rhyme_entropy[sid]   -- A3 (entropy in bits)
      divine_density[sid]  -- A4 (= name_sum/verse_count)
      hapax_density[sid]   -- A5 (frac of distinct surah-roots that are corpus-hapax)
      root_set[sid]        -- A1 (set of distinct roots)
    """
    verse_len_mean = {}
    rhyme_entropy = {}
    divine_density = {}
    hapax_density = {}
    root_set = {}

    for s in quran:
        sid = s["id"]
        verses = s["verses"]
        n_verses = len(verses)

        # Verse lengths (no-tashkeel char count, including spaces).
        # Strip leading/trailing whitespace; do NOT strip basmala (only Q1:1).
        lengths = [len(v["text"].strip()) for v in verses]
        verse_len_mean[sid] = sum(lengths) / max(1, n_verses)

        # Rhyme: last 2 chars (no-tashkeel) of each verse, after stripping
        # trailing whitespace. If verse < 2 chars, use the whole stripped string.
        suffixes = []
        for v in verses:
            t = v["text"].strip()
            if len(t) >= 2:
                suffixes.append(t[-2:])
            elif t:
                suffixes.append(t)
        if suffixes:
            counts = Counter(suffixes)
            total = sum(counts.values())
            H = 0.0
            for c in counts.values():
                p = c / total
                if p > 0:
                    H -= p * math.log2(p)
            rhyme_entropy[sid] = H
        else:
            rhyme_entropy[sid] = 0.0

        # Divine density (per-verse rate)
        divine_density[sid] = divine_sum.get(sid, 0) / max(1, n_verses)

        # Roots
        roots_here = qac_per_surah.get(sid, [])
        distinct = set(roots_here)
        root_set[sid] = distinct
        if distinct:
            n_hapax = sum(1 for r in distinct if corpus_root_count[r] == 1)
            hapax_density[sid] = n_hapax / len(distinct)
        else:
            hapax_density[sid] = 0.0

    return {
        "verse_len_mean": verse_len_mean,
        "rhyme_entropy": rhyme_entropy,
        "divine_density": divine_density,
        "hapax_density": hapax_density,
        "root_set": root_set,
    }


# ---------------- Pair similarity ----------------

def sim_jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / max(1, union)


def sim_scalar(a, b):
    """Symmetric scalar similarity in [0, 1]: 1 - |a-b|/max(|a|,|b|,eps)."""
    denom = max(abs(a), abs(b), 1e-9)
    return 1.0 - abs(a - b) / denom


def pair_similarity(sid_a, sid_b, feats):
    return {
        "A1_root_jaccard":  sim_jaccard(feats["root_set"][sid_a],
                                         feats["root_set"][sid_b]),
        "A2_verse_len":     sim_scalar(feats["verse_len_mean"][sid_a],
                                        feats["verse_len_mean"][sid_b]),
        "A3_rhyme_entropy": sim_scalar(feats["rhyme_entropy"][sid_a],
                                        feats["rhyme_entropy"][sid_b]),
        "A4_divine_density": sim_scalar(feats["divine_density"][sid_a],
                                         feats["divine_density"][sid_b]),
        "A5_hapax_density":  sim_scalar(feats["hapax_density"][sid_a],
                                         feats["hapax_density"][sid_b]),
    }


# ---------------- Null distribution ----------------

def build_null(feats, exclude_pair, n_draws, rng):
    """Draw n_draws random adjacent (i, i+1) surah pairs (1≤i≤113) excluding
    the (a, b) pair under test (matched on adjacency). Sample WITH replacement."""
    a, b = exclude_pair
    sims = {ax: [] for ax in AXES}
    for _ in range(n_draws):
        while True:
            i = rng.randint(1, 113)  # inclusive
            if (i, i + 1) == (a, b):
                continue
            break
        sim = pair_similarity(i, i + 1, feats)
        for ax in AXES:
            sims[ax].append(sim[ax])
    return sims


def build_null_any_pair(feats, exclude_pair, n_draws, rng):
    """POST-HOC SECONDARY diagnostic null: random (i, j) surah pairs with
    1≤i<j≤114 — NOT restricted to adjacency. Used only as a diagnostic to
    explain why the pre-registered adjacent-pair null is unusually tight
    (canonical mushaf order clusters similar surahs as neighbors). Does NOT
    enter the PASS/NULL declaration for H-NEW-58."""
    a, b = exclude_pair
    sims = {ax: [] for ax in AXES}
    for _ in range(n_draws):
        while True:
            i = rng.randint(1, 113)
            j = rng.randint(i + 1, 114)
            if (i, j) == (a, b):
                continue
            break
        sim = pair_similarity(i, j, feats)
        for ax in AXES:
            sims[ax].append(sim[ax])
    return sims


def upper_tail_p(observed, null_samples):
    """One-sided p = (1 + |{null >= observed}|) / (1 + N_null)."""
    n = len(null_samples)
    n_ge = sum(1 for v in null_samples if v >= observed)
    return (1 + n_ge) / (1 + n)


# ---------------- Main ----------------

def main():
    rng = random.Random(SEED)

    print("Loading Quran (no-tashkeel)...", file=sys.stderr)
    quran = load_quran_no_tashkeel()
    print("Loading QAC morphology (roots per surah)...", file=sys.stderr)
    qac_per_surah, corpus_root_count = load_qac_roots_per_surah()
    print("Loading divine-name density...", file=sys.stderr)
    divine_sum = load_divine_density()

    print("Computing per-surah features...", file=sys.stderr)
    feats = per_surah_features(quran, qac_per_surah, corpus_root_count, divine_sum)

    # Per-pair observed similarity + null + p
    results = {}
    null_caches = {}  # for reproducibility/inspection
    secondary_any_pair_p = {}
    for label, a, b in CLASSICAL_PAIRS:
        obs = pair_similarity(a, b, feats)

        # Per-pair null (to ensure exclusion of the test pair from its own null)
        null = build_null(feats, (a, b), N_NULL, rng)
        # Secondary diagnostic null: any-(i,j) pair
        null_any = build_null_any_pair(feats, (a, b), N_NULL, rng)

        cell = {}
        secondary_cell = {}
        for ax in AXES:
            p = upper_tail_p(obs[ax], null[ax])
            cell[ax] = {
                "observed": obs[ax],
                "null_mean": sum(null[ax]) / N_NULL,
                "null_median": sorted(null[ax])[N_NULL // 2],
                "p_one_sided": p,
                "bonferroni_significant": p <= ALPHA_BON,
            }
            p_any = upper_tail_p(obs[ax], null_any[ax])
            secondary_cell[ax] = {
                "p_one_sided_any_pair": p_any,
                "null_any_mean": sum(null_any[ax]) / N_NULL,
                "null_any_median": sorted(null_any[ax])[N_NULL // 2],
            }
        secondary_any_pair_p[label] = secondary_cell
        # Per-pair "n_axes_significant"
        n_sig = sum(1 for ax in AXES if cell[ax]["bonferroni_significant"])
        results[label] = {
            "surah_a": a,
            "surah_b": b,
            "axes": cell,
            "n_axes_significant_at_alpha_bon": n_sig,
        }
        null_caches[label] = {
            ax: {
                "mean": sum(null[ax]) / N_NULL,
                "median": sorted(null[ax])[N_NULL // 2],
                "q01": sorted(null[ax])[int(0.01 * N_NULL)],
                "q05": sorted(null[ax])[int(0.05 * N_NULL)],
                "q95": sorted(null[ax])[int(0.95 * N_NULL)],
                "q99": sorted(null[ax])[int(0.99 * N_NULL)],
                "max": max(null[ax]),
            }
            for ax in AXES
        }

    # PASS criterion
    n_pairs_with_geq2_sig = sum(
        1 for label in results
        if results[label]["n_axes_significant_at_alpha_bon"] >= 2
    )
    h_new_58_pass = n_pairs_with_geq2_sig >= 2

    # MW-5 instrument check
    mw_axes_p = results["P_muawwidhatan"]["axes"]
    mw_n_under_001 = sum(1 for ax in AXES if mw_axes_p[ax]["p_one_sided"] < 0.001)
    mw5_pass = mw_n_under_001 >= 2

    # Per-pair raw observed feature scalars (helpful for the findings file)
    feat_dump = {}
    for label, a, b in CLASSICAL_PAIRS:
        feat_dump[label] = {
            "surah_a": a, "surah_b": b,
            "verse_len_mean_a": feats["verse_len_mean"][a],
            "verse_len_mean_b": feats["verse_len_mean"][b],
            "rhyme_entropy_a": feats["rhyme_entropy"][a],
            "rhyme_entropy_b": feats["rhyme_entropy"][b],
            "divine_density_a": feats["divine_density"][a],
            "divine_density_b": feats["divine_density"][b],
            "hapax_density_a": feats["hapax_density"][a],
            "hapax_density_b": feats["hapax_density"][b],
            "root_set_size_a": len(feats["root_set"][a]),
            "root_set_size_b": len(feats["root_set"][b]),
            "root_intersection": len(feats["root_set"][a] & feats["root_set"][b]),
            "root_union": len(feats["root_set"][a] | feats["root_set"][b]),
        }

    # Re-evaluate PASS/NULL declaration honestly given MW-5 outcome.
    if mw5_pass:
        overall = "PASS" if h_new_58_pass else "NULL"
    else:
        # Per pre-reg: do not declare H-NEW-58 PASS or NULL when instrument
        # fails. Log INSTRUMENT_FAIL and report cell table honestly.
        overall = "INSTRUMENT_FAIL_NO_DECLARATION"

    out = {
        "id": "H-NEW-58",
        "title": "Empirical structural twinning of classically-paired surahs",
        "seed": SEED,
        "n_null_per_pair": N_NULL,
        "null_construction": "random adjacent (i, i+1) surah pairs, "
                             "excluding the test pair from its own null",
        "alpha_bonferroni": ALPHA_BON,
        "bonferroni_k": 20,
        "axes": AXES,
        "pairs": [{"label": l, "a": a, "b": b} for l, a, b in CLASSICAL_PAIRS],
        "results": results,
        "null_distribution_summary": null_caches,
        "feature_scalars": feat_dump,
        "pass_criterion": "≥2 of 4 pairs significant on ≥2 of 5 axes at "
                          "α_bon=0.0025",
        "n_pairs_with_geq_2_axes_sig": n_pairs_with_geq2_sig,
        "h_new_58_overall": overall,
        "mw5_instrument_check": {
            "definition": "MW-5: P_muawwidhatan must have ≥2 axes with p<0.001",
            "n_axes_under_0.001": mw_n_under_001,
            "result": "PASS" if mw5_pass else "INSTRUMENT_FAIL",
        },
        "secondary_any_pair_null_diagnostic": {
            "purpose": "POST-HOC diagnostic ONLY (does not enter PASS/NULL "
                       "declaration). Compares observed similarity to a null "
                       "of any (i, j) surah pair to show whether adjacent-"
                       "pair null is unusually tight.",
            "results": secondary_any_pair_p,
        },
    }

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-58.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)

    # Console summary table
    print()
    print("Pair × Axis observed-similarity / one-sided p (Bonferroni α=0.0025):")
    print()
    header = f"{'pair':<18} " + " ".join(f"{ax:<22}" for ax in AXES)
    print(header)
    for label, a, b in CLASSICAL_PAIRS:
        row = [f"{label:<18}"]
        for ax in AXES:
            cell = results[label]["axes"][ax]
            star = "*" if cell["bonferroni_significant"] else " "
            row.append(f"sim={cell['observed']:.3f} p={cell['p_one_sided']:.4f}{star}")
        # padding
        line = " ".join(row)
        print(line)
    print()
    print(f"H-NEW-58 overall: {out['h_new_58_overall']}  "
          f"(pairs with ≥2 sig axes = {n_pairs_with_geq2_sig}/4)")
    print(f"MW-5: {out['mw5_instrument_check']['result']}  "
          f"(P_muawwidhatan axes with p<0.001 = {mw_n_under_001}/5)")
    print()
    print("SECONDARY (post-hoc diagnostic) — any-pair null p-values:")
    for label, _, _ in CLASSICAL_PAIRS:
        line = [f"{label:<18}"]
        for ax in AXES:
            p = secondary_any_pair_p[label][ax]["p_one_sided_any_pair"]
            line.append(f"{ax}={p:.4f}")
        print("  " + "  ".join(line))


if __name__ == "__main__":
    main()
