#!/usr/bin/env python3
"""H-NEW-68 — Friday-recitation cluster cohesion test.

Pre-reg: findings/phase-b-hypotheses/h-new-68-friday-cluster-prereg.md

Friday-cluster (locked):
  Q 18 al-Kahf      (recited every Friday)
  Q 32 al-Sajda     (Fajr Friday)
  Q 62 al-Jumuʿah   ("the Friday")
  Q 76 al-Insān     (Fajr Friday, paired w/ al-Sajda)

4 axes (locked):
  A1 mean-pairwise-shared-prefix  (chars; 6 pairs averaged)
  A2 mean-pairwise-root-jaccard   (QAC stems; 6 pairs averaged)
  A3 length-cohesion-verse-count  (1 / (1 + CV(verse_counts)))
  A4 divine-density-cohesion      (1 / (1 + CV(divine_density)))

Null: 10 000 random 4-surah subsets (excluding the exact Friday set).
Bonferroni k=4, α_bon = 0.0125. Seed 20260416.

PASS criterion: ≥ 2 of 4 axes significant at α_bon.
MARGINAL: 1 axis significant.
NULL: 0 axes significant.

Secondary: Q 18 ↔ Q 62 specific pairwise test on A1, A2 vs any-pair null
with Bonferroni-2.

MW-5: musabbiḥāt cluster instrument validated by H-NEW-58c (p=0.0001).
"""
from __future__ import annotations

import csv
import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260416
N_NULL = 10_000
ALPHA_BON = 0.05 / 4   # = 0.0125
ALPHA_BON_PAIR = 0.05 / 2  # = 0.025 (Q18-Q62 secondary, 2 axes)
N_AXES = 4

FRIDAY_CLUSTER = [18, 32, 62, 76]
CLUSTER_LABEL = "Friday-recitation"

AXES = ["A1_pair_prefix_mean", "A2_pair_root_jaccard_mean",
        "A3_length_cohesion", "A4_divine_density_cohesion"]


# ---------------- Loaders ----------------

def load_quran_no_tashkeel():
    path = REPO / "quran-text" / "quran-no-tashkeel.json"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def load_qac_roots_per_surah():
    """Return dict surah_id -> set of distinct root strings (per stem-token)."""
    per_surah: dict[int, list[str]] = defaultdict(list)
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
            per_surah[sid].append(rm.group(1))
    return {sid: set(rs) for sid, rs in per_surah.items()}


def load_divine_density(quran):
    """Return dict surah_id -> divine-name density per verse."""
    csv_path = REPO / "findings" / "phase-b-hypotheses" / "divine-names-by-verse.csv"
    name_sum: Counter = Counter()
    with csv_path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            sid = int(row["surah"])
            name_sum[sid] += int(row["num_names"])
    densities = {}
    for s in quran:
        sid = s["id"]
        n_verses = len(s["verses"])
        densities[sid] = name_sum.get(sid, 0) / max(1, n_verses)
    return densities


def get_first_verse_text(quran):
    """Return dict surah_id -> first verse no-tashkeel text (stripped)."""
    out = {}
    for s in quran:
        sid = s["id"]
        verses = s["verses"]
        if verses:
            out[sid] = verses[0]["text"].strip()
        else:
            out[sid] = ""
    return out


def get_verse_counts(quran):
    return {s["id"]: len(s["verses"]) for s in quran}


# ---------------- Pair / cluster metrics ----------------

def shared_prefix(a: str, b: str) -> int:
    """Length of longest common character prefix."""
    n = min(len(a), len(b))
    i = 0
    while i < n and a[i] == b[i]:
        i += 1
    return i


def jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / max(1, union)


def cv(values):
    """Coefficient of variation = std / mean."""
    if not values:
        return 0.0
    mean = sum(values) / len(values)
    if mean == 0:
        return 0.0
    if len(values) < 2:
        return 0.0
    var = sum((v - mean) ** 2 for v in values) / len(values)
    std = math.sqrt(var)
    return std / mean


def cohesion_inv_cv(values):
    """1 / (1 + CV). Bounded in (0, 1]. Higher = more cohesive."""
    return 1.0 / (1.0 + cv(values))


def cluster_cohesion(subset, first_verse, root_set, verse_counts, divine_density):
    """Compute the 4 cohesion scalars for a 4-surah subset."""
    pairs = list(combinations(subset, 2))
    # A1
    prefixes = [shared_prefix(first_verse[a], first_verse[b]) for a, b in pairs]
    a1 = sum(prefixes) / len(prefixes)
    # A2
    jaccards = [jaccard(root_set.get(a, set()), root_set.get(b, set()))
                for a, b in pairs]
    a2 = sum(jaccards) / len(jaccards)
    # A3
    vcs = [verse_counts[s] for s in subset]
    a3 = cohesion_inv_cv(vcs)
    # A4
    dds = [divine_density.get(s, 0.0) for s in subset]
    a4 = cohesion_inv_cv(dds)
    return {
        "A1_pair_prefix_mean": a1,
        "A2_pair_root_jaccard_mean": a2,
        "A3_length_cohesion": a3,
        "A4_divine_density_cohesion": a4,
        "_pairwise_prefixes": prefixes,
        "_pairwise_jaccards": jaccards,
        "_verse_counts": vcs,
        "_divine_densities": dds,
    }


# ---------------- Null distributions ----------------

def build_cluster_null(first_verse, root_set, verse_counts, divine_density,
                       exclude_set, n_draws, rng):
    """Random 4-surah subsets, excluding exact Friday set. Sample with replacement."""
    exclude_frozen = frozenset(exclude_set)
    sims = {ax: [] for ax in AXES}
    surahs = list(range(1, 115))
    for _ in range(n_draws):
        while True:
            subset = tuple(sorted(rng.sample(surahs, 4)))
            if frozenset(subset) != exclude_frozen:
                break
        c = cluster_cohesion(list(subset), first_verse, root_set, verse_counts,
                             divine_density)
        for ax in AXES:
            sims[ax].append(c[ax])
    return sims


def build_pair_null(first_verse, root_set, exclude_pair, n_draws, rng):
    """Random (i, j) pairs (i!=j) excluding the test pair. With replacement."""
    a, b = sorted(exclude_pair)
    sims = {"P_prefix": [], "P_jaccard": []}
    for _ in range(n_draws):
        while True:
            i = rng.randint(1, 114)
            j = rng.randint(1, 114)
            if i == j:
                continue
            i, j = sorted([i, j])
            if (i, j) == (a, b):
                continue
            break
        p = shared_prefix(first_verse[i], first_verse[j])
        jac = jaccard(root_set.get(i, set()), root_set.get(j, set()))
        sims["P_prefix"].append(p)
        sims["P_jaccard"].append(jac)
    return sims


def upper_tail_p(observed, null_samples):
    """One-sided p = (1 + |{null >= observed}|) / (1 + N_null)."""
    n = len(null_samples)
    n_ge = sum(1 for v in null_samples if v >= observed)
    return (1 + n_ge) / (1 + n)


def percentile(samples, p):
    s = sorted(samples)
    idx = int(p * len(s))
    if idx >= len(s):
        idx = len(s) - 1
    return s[idx]


# ---------------- Main ----------------

def main():
    rng = random.Random(SEED)

    print("Loading Quran (no-tashkeel)...", file=sys.stderr)
    quran = load_quran_no_tashkeel()
    print("Loading QAC morphology (roots per surah)...", file=sys.stderr)
    root_set = load_qac_roots_per_surah()
    print("Loading divine-name density...", file=sys.stderr)
    divine_density = load_divine_density(quran)
    print("Computing per-surah scalars...", file=sys.stderr)
    first_verse = get_first_verse_text(quran)
    verse_counts = get_verse_counts(quran)

    # ---- Observed Friday-cluster cohesion ----
    print(f"Friday cluster: {FRIDAY_CLUSTER}", file=sys.stderr)
    obs = cluster_cohesion(FRIDAY_CLUSTER, first_verse, root_set, verse_counts,
                           divine_density)

    # ---- Build cluster null ----
    print(f"Building 4-subset cluster null (N={N_NULL})...", file=sys.stderr)
    null = build_cluster_null(first_verse, root_set, verse_counts, divine_density,
                              FRIDAY_CLUSTER, N_NULL, rng)

    # ---- Per-axis stats ----
    cell = {}
    for ax in AXES:
        p = upper_tail_p(obs[ax], null[ax])
        cell[ax] = {
            "observed": obs[ax],
            "null_mean": sum(null[ax]) / N_NULL,
            "null_median": percentile(null[ax], 0.50),
            "null_q05": percentile(null[ax], 0.05),
            "null_q95": percentile(null[ax], 0.95),
            "null_q99": percentile(null[ax], 0.99),
            "null_max": max(null[ax]),
            "p_one_sided": p,
            "bonferroni_significant": p <= ALPHA_BON,
            "uncorrected_significant": p <= 0.05,
        }

    n_sig = sum(1 for ax in AXES if cell[ax]["bonferroni_significant"])
    n_uncorr_sig = sum(1 for ax in AXES if cell[ax]["uncorrected_significant"])
    if n_sig >= 2:
        verdict = "PASS"
    elif n_sig == 1:
        verdict = "MARGINAL"
    else:
        verdict = "NULL"

    # ---- Q 18 ↔ Q 62 secondary pair test ----
    print("Running Q18-Q62 secondary pair test (any-pair null)...", file=sys.stderr)
    pair_obs_prefix = shared_prefix(first_verse[18], first_verse[62])
    pair_obs_jaccard = jaccard(root_set.get(18, set()), root_set.get(62, set()))
    pair_null = build_pair_null(first_verse, root_set, (18, 62), N_NULL, rng)
    p_prefix = upper_tail_p(pair_obs_prefix, pair_null["P_prefix"])
    p_jaccard = upper_tail_p(pair_obs_jaccard, pair_null["P_jaccard"])

    pair_secondary = {
        "P_prefix": {
            "observed": pair_obs_prefix,
            "null_mean": sum(pair_null["P_prefix"]) / N_NULL,
            "null_median": percentile(pair_null["P_prefix"], 0.50),
            "null_q95": percentile(pair_null["P_prefix"], 0.95),
            "null_q99": percentile(pair_null["P_prefix"], 0.99),
            "p_one_sided": p_prefix,
            "bonferroni_significant_k2": p_prefix <= ALPHA_BON_PAIR,
        },
        "P_jaccard": {
            "observed": pair_obs_jaccard,
            "null_mean": sum(pair_null["P_jaccard"]) / N_NULL,
            "null_median": percentile(pair_null["P_jaccard"], 0.50),
            "null_q95": percentile(pair_null["P_jaccard"], 0.95),
            "null_q99": percentile(pair_null["P_jaccard"], 0.99),
            "p_one_sided": p_jaccard,
            "bonferroni_significant_k2": p_jaccard <= ALPHA_BON_PAIR,
        },
    }

    # ---- Friday cluster pair details ----
    pairs = list(combinations(FRIDAY_CLUSTER, 2))
    pair_details = []
    for a, b in pairs:
        pair_details.append({
            "a": a, "b": b,
            "first_verse_a": first_verse[a],
            "first_verse_b": first_verse[b],
            "shared_prefix_chars": shared_prefix(first_verse[a], first_verse[b]),
            "root_jaccard": jaccard(root_set.get(a, set()), root_set.get(b, set())),
            "root_intersection_size": len(root_set.get(a, set()) & root_set.get(b, set())),
            "root_union_size": len(root_set.get(a, set()) | root_set.get(b, set())),
        })

    # ---- Surah-level scalars ----
    surah_scalars = {}
    for s in FRIDAY_CLUSTER:
        surah_scalars[s] = {
            "first_verse": first_verse[s],
            "verse_count": verse_counts[s],
            "divine_density": divine_density.get(s, 0.0),
            "n_distinct_roots": len(root_set.get(s, set())),
        }

    # ---- Output ----
    out = {
        "id": "H-NEW-68",
        "title": "Friday-recitation cluster cohesion test (Q18, Q32, Q62, Q76)",
        "seed": SEED,
        "n_null_per_axis": N_NULL,
        "null_construction": "random 4-surah subsets (without replacement within "
                             "subset; with replacement across draws); the EXACT "
                             "Friday set excluded",
        "alpha_bonferroni": ALPHA_BON,
        "bonferroni_k": 4,
        "axes": AXES,
        "friday_cluster": FRIDAY_CLUSTER,
        "observed_cluster_cohesion": {ax: cell[ax]["observed"] for ax in AXES},
        "results": {
            "axes": cell,
            "n_axes_bonferroni_significant": n_sig,
            "n_axes_uncorrected_significant": n_uncorr_sig,
            "verdict": verdict,
        },
        "pair_details": pair_details,
        "surah_scalars": surah_scalars,
        "secondary_q18_q62_pair_test": {
            "purpose": "PRE-REGISTERED secondary test of Q18-Q62 specific link "
                       "(both surahs are most unambiguously Friday-specific by "
                       "tradition).",
            "alpha_bonferroni_k2": ALPHA_BON_PAIR,
            "results": pair_secondary,
        },
        "mw5_instrument_validation": {
            "definition": "Shared-prefix cluster instrument (A1) was independently "
                          "validated in H-NEW-58c on the musabbiḥāt cluster "
                          "(Q57, 59, 61, 62, 64) at p=0.0001. Same metric used here.",
            "status": "Instrument-validated (no fresh MW-5 needed).",
        },
        "pass_criterion": "≥2 of 4 axes Bonferroni-significant at α=0.0125 → PASS; "
                          "1 → MARGINAL; 0 → NULL.",
    }

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-68.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)

    # ---- Console summary ----
    print()
    print(f"{CLUSTER_LABEL} cluster cohesion (Bonferroni α={ALPHA_BON}):")
    print()
    print(f"{'axis':<32} {'observed':<12} {'null_mean':<12} {'null_q95':<12} "
          f"{'null_q99':<12} {'p':<10} {'sig?':<6}")
    for ax in AXES:
        c = cell[ax]
        sig = "*" if c["bonferroni_significant"] else (
              "(uncorr)" if c["uncorrected_significant"] else "")
        print(f"{ax:<32} {c['observed']:<12.4f} {c['null_mean']:<12.4f} "
              f"{c['null_q95']:<12.4f} {c['null_q99']:<12.4f} "
              f"{c['p_one_sided']:<10.4f} {sig:<6}")
    print()
    print(f"H-NEW-68 verdict: {verdict}  "
          f"(Bonferroni-sig axes = {n_sig}/4; uncorrected-sig = {n_uncorr_sig}/4)")
    print()
    print("Pairwise details (Friday cluster):")
    for p in pair_details:
        print(f"  Q{p['a']:<3}-Q{p['b']:<3}: prefix={p['shared_prefix_chars']:>3} "
              f"chars  jaccard={p['root_jaccard']:.4f}  "
              f"({p['root_intersection_size']}/{p['root_union_size']} roots)")
    print()
    print("Q 18 ↔ Q 62 secondary test (any-pair null, Bonferroni-2 α=0.025):")
    pp = pair_secondary["P_prefix"]
    pj = pair_secondary["P_jaccard"]
    sig_p = "*" if pp["bonferroni_significant_k2"] else ""
    sig_j = "*" if pj["bonferroni_significant_k2"] else ""
    print(f"  prefix:  obs={pp['observed']:>3} chars  null_mean={pp['null_mean']:.3f}  "
          f"null_q95={pp['null_q95']:.0f}  null_q99={pp['null_q99']:.0f}  "
          f"p={pp['p_one_sided']:.4f} {sig_p}")
    print(f"  jaccard: obs={pj['observed']:.4f}    null_mean={pj['null_mean']:.4f}  "
          f"null_q95={pj['null_q95']:.4f}  null_q99={pj['null_q99']:.4f}  "
          f"p={pj['p_one_sided']:.4f} {sig_j}")


if __name__ == "__main__":
    main()
