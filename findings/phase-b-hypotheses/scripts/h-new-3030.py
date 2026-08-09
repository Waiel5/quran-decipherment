#!/usr/bin/env python3
"""H-NEW-3030: the power the sajdah-locus test actually had, and the surah-level confound contrast.

H-NEW-2950 executed F-8 and returned NULL. It asserted that n = 15 left the design underpowered
but never computed power: the three quantities it reported are p-value FLOORS, which describe
resolution, not power. This script computes the minimum detectable effect exactly, and runs the
two nulls the F-8 brief named that H-NEW-2950 did not (corpus-wide, and surah-level).

Three deliverables, deliberately separated (prereg §0):
  A. Independent replication of the U+06E9 census. Documentary; no null model; no p-value.
  B. The power computation. Exact MDE under a quantile alternative (primary), an exponential
     tilt (secondary, rate-ratio form), and a model-free lit-locus count. No p-value.
  C. The confound contrast: within-surah (replication) vs corpus-wide vs surah-level. Exact p.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3030.py
      python3 findings/phase-b-hypotheses/scripts/h-new-3030.py --self-check
"""

import argparse
import hashlib
import json
import math
import os
import platform
import random
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

# Prereg §8 — embedded literals, verified at runtime; mismatch aborts before any run directory.
EXPECTED_PREREG_SHA = "712a98af0126158bd6a283790aeea8778cacd0049ff6573dee090df88d293009"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_QURAN_NO_TASHKEEL_SHA = "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"
EXPECTED_QURAN_FULL_TASHKEEL_SHA = "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715"

SAJDAH_GLYPH = "۩"  # ARABIC PLACE OF SAJDAH

SEED = 20260509
N_MONTE_CARLO = 200_000

K_PRIMARY = 15        # prereg §7.1 — verse pools, m = 16
K_SENSITIVITY = 10    # prereg §3 second tuple, m = 11
K_SURAH = 7           # prereg §7.1 / §10 decision 6 — surah pools, m = 8

# Prereg §7.3 — family = {C1,C2,C3} x {F1,F2}
TESTS_IN_FAMILY = 6
ALPHA_BONFERRONI = 0.05 / TESTS_IN_FAMILY  # 0.008333...
NOVELTY_GATE = 0.005                       # prereg §7.5

POWER_TARGET = 0.80                        # prereg §6.2 / §10 decision 4

LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
SECOND_PERSON_RE = re.compile(r"(?:^|\|)(?:PRON:)?2(?:MS|MP|FS|FP|D)(?:$|\|)")
SJD_RE = re.compile(r"(?:^|\|)ROOT:sjd(?:$|\|)")
IMPV_RE = re.compile(r"(?:^|\|)IMPV(?:$|\|)")

FEATURES = ("F1_imperative", "F2_second_person")  # prereg §4 — F3 dropped, a tightening

# Prereg §4 — asserted so a corpus change breaks the run loudly rather than silently redefining
# the test set. Independently re-derived in run_census() and compared.
EXPECTED_LOCI = (
    (7, 206), (13, 15), (16, 50), (17, 109), (19, 58), (22, 18), (22, 77), (25, 60),
    (27, 26), (32, 15), (38, 24), (41, 38), (53, 62), (84, 21), (96, 19),
)


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(repo_root, *args):
    try:
        return subprocess.run(
            ["git", *args], cwd=repo_root, capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception:
        return None


# --------------------------------------------------------------------------------------
# Deliverable A — the census (prereg §0: documentary, no null model)
# --------------------------------------------------------------------------------------

def census_json(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    loci, glyphs = [], 0
    for surah in data:
        for verse in surah["verses"]:
            count = verse["text"].count(SAJDAH_GLYPH)
            if count:
                loci.append([surah["id"], verse["id"], count])
                glyphs += count
    return {"loci": loci, "n_loci": len(loci), "n_glyphs": glyphs}


def run_census(repo_root):
    """Independent re-derivation of the locus set from the keyed variants (prereg §11)."""
    variants = {}
    for rel in (
        "quran-text/quran-full-tashkeel.json",
        "quran-text/quran-min-tashkeel.json",
        "quran-text/quran-no-tashkeel.json",
    ):
        variants[rel] = census_json(repo_root / rel)

    raw_counts = {}
    for pattern in ("quran-text/*.txt", "data/alt-text/*.txt"):
        for path in sorted(repo_root.glob(pattern)):
            rel = str(path.relative_to(repo_root))
            raw_counts[rel] = path.read_text(encoding="utf-8", errors="replace").count(SAJDAH_GLYPH)

    keyed = {rel: tuple(tuple(l[:2]) for l in c["loci"]) for rel, c in variants.items()}
    return {
        "glyph": "U+06E9 ARABIC PLACE OF SAJDAH",
        "keyed_variants": variants,
        "raw_glyph_counts_all_flat_files": raw_counts,
        "locus_sets_identical_across_keyed_variants": len(set(keyed.values())) == 1,
        "matches_h_new_2950_locus_set": all(v == EXPECTED_LOCI for v in keyed.values()),
        "canonical_locus_set": [list(l) for l in EXPECTED_LOCI],
        "surah_support": sorted({s for s, _ in EXPECTED_LOCI}),
        "n_surahs": len({s for s, _ in EXPECTED_LOCI}),
        "n_verses": len(EXPECTED_LOCI),
    }


# --------------------------------------------------------------------------------------
# Instrument (prereg §4) — identical to H-NEW-2950 so that C1 is a true replication
# --------------------------------------------------------------------------------------

def parse_qac(path):
    words = defaultdict(set)
    counts = {
        excl: {feature: defaultdict(int) for feature in FEATURES}
        for excl in ("sjd_excluded", "sjd_included")
    }
    for line in open(path, encoding="utf-8"):
        if not line.startswith("("):
            continue
        fields = line.rstrip("\n").split("\t")
        if len(fields) != 4:
            continue
        location, _, _, feats = fields
        match = LOCATION_RE.fullmatch(location)
        if not match:
            continue
        surah, verse, word = int(match.group(1)), int(match.group(2)), int(match.group(3))
        key = (surah, verse)
        words[key].add(word)

        is_sjd = SJD_RE.search(feats) is not None
        hits = {
            "F1_imperative": "POS:V" in feats and IMPV_RE.search(feats) is not None,
            "F2_second_person": SECOND_PERSON_RE.search(feats) is not None,
        }
        for feature, hit in hits.items():
            if not hit:
                continue
            counts["sjd_included"][feature][key] += 1
            if not is_sjd:
                counts["sjd_excluded"][feature][key] += 1
    return {k: len(v) for k, v in words.items()}, counts


def tie_fractions(word_count, counts):
    """Prereg §5 — restated at runtime from the same data the test uses."""
    verses = sorted(word_count)
    out = {}
    for feature in FEATURES:
        table = counts["sjd_excluded"][feature]
        zeros = sum(1 for v in verses if table[v] == 0)
        out[feature] = {
            "n_verses": len(verses),
            "n_tied_at_zero": zeros,
            "tie_fraction": round(zeros / len(verses), 4),
            "exceeds_50pct_threshold": zeros / len(verses) > 0.50,
        }
    return out


# --------------------------------------------------------------------------------------
# Pools (prereg §7.1)
# --------------------------------------------------------------------------------------

def build_pools_within_surah(word_count, loci, k):
    """C1 — {verse i} + K nearest-length non-sajdah verses OF THE SAME SURAH.

    Byte-for-byte the rule H-NEW-2950 used, so C1 is a replication rather than a new design.
    """
    locus_set = set(loci)
    by_surah = defaultdict(list)
    for (surah, verse) in word_count:
        by_surah[surah].append(verse)
    pools = {}
    for locus in loci:
        surah, _ = locus
        target = word_count[locus]
        eligible = [v for v in sorted(by_surah[surah]) if (surah, v) not in locus_set]
        if len(eligible) < k:
            raise SystemExit(f"pool for {locus} cannot be filled: {len(eligible)} < K={k}")
        eligible.sort(key=lambda v: (abs(word_count[(surah, v)] - target), v))
        pools[locus] = [locus] + [(surah, v) for v in eligible[:k]]
    return pools


def build_pools_corpus_wide(word_count, loci, k):
    """C2 — {verse i} + K nearest-length non-sajdah verses FROM THE WHOLE CORPUS.

    Controls length more tightly than C1 and leaves surah free. Ties in |dlength| broken
    deterministically by (surah, verse) ascending — no seed enters pool construction
    (prereg §10 decision 7).
    """
    locus_set = set(loci)
    eligible = sorted(v for v in word_count if v not in locus_set)
    pools = {}
    for locus in loci:
        target = word_count[locus]
        ranked = sorted(eligible, key=lambda v: (abs(word_count[v] - target), v[0], v[1]))
        pools[locus] = [locus] + ranked[:k]
    return pools


def build_pools_surah_level(surah_words, sajdah_surahs, k):
    """C3 — {surah i} + K nearest-length non-sajdah SURAHS."""
    sajdah = set(sajdah_surahs)
    eligible = sorted(s for s in surah_words if s not in sajdah)
    pools = {}
    for surah in sajdah_surahs:
        target = surah_words[surah]
        ranked = sorted(eligible, key=lambda s: (abs(surah_words[s] - target), s))
        if len(ranked) < k:
            raise SystemExit(f"surah pool for {surah} cannot be filled")
        pools[surah] = [surah] + ranked[:k]
    return pools


# --------------------------------------------------------------------------------------
# Exact null, and the exact power machinery (prereg §6)
# --------------------------------------------------------------------------------------

def exact_convolution(pool_values):
    """Exact null pmf of S = sum of one uniformly drawn value per pool, as integer tuple counts."""
    dp = {0: 1}
    for values in pool_values:
        nxt = defaultdict(int)
        for total, ways in dp.items():
            for value in values:
                nxt[total + value] += ways
        dp = dict(nxt)
    total = 1
    for values in pool_values:
        total *= len(values)
    assert sum(dp.values()) == total
    return dp, total


def convolve_weighted(pool_pmfs):
    """Exact pmf of S under arbitrary per-pool float pmfs {value: prob}."""
    dp = {0: 1.0}
    for pmf in pool_pmfs:
        nxt = defaultdict(float)
        for total, prob in dp.items():
            for value, weight in pmf.items():
                nxt[total + value] += prob * weight
        dp = dict(nxt)
    return dp


def upper_tail(pmf, threshold):
    return sum(prob for value, prob in pmf.items() if value >= threshold)


def critical_value(dp, total, alpha):
    """Prereg §6.1 — S* := min{ s : P_0(S >= s) < alpha }."""
    for s in sorted(dp):
        tail = Fraction(sum(w for v, w in dp.items() if v >= s), total)
        if tail < alpha:
            return s, float(tail)
    # Unreachable in practice: the tail at max(dp)+1 is 0 < alpha.
    return max(dp) + 1, 0.0


def quantile_alternative_pmf(values, t):
    """Prereg §6.2 — uniform over the top t members of the pool by value (sorted ascending)."""
    ordered = sorted(values)
    t = max(1, min(t, len(ordered)))
    top = ordered[len(ordered) - t:]
    pmf = defaultdict(float)
    for value in top:
        pmf[value] += 1.0 / t
    return dict(pmf)


def tilted_pmf(values, theta):
    """Prereg §6.3 — p_theta(x) proportional to p_0(x) * exp(theta * x), on the multiset."""
    peak = max(values)
    weights = defaultdict(float)
    for value in values:
        weights[value] += math.exp(theta * (value - peak))  # shift for numerical stability
    norm = sum(weights.values())
    return {value: weight / norm for value, weight in weights.items()}


def power_analysis(pool_values, alpha, target):
    """Deliverable B, all four quantities. Depends on the NULL only — never on the observation."""
    dp, total = exact_convolution(pool_values)
    s_star, tail_at_star = critical_value(dp, total, alpha)
    s_max = sum(max(v) for v in pool_values)
    m = len(pool_values[0])

    fatal = s_star > s_max

    # B1 — quantile alternative. Power is a step function of t = ceil(q*m); enumerate all t.
    curve = []
    for t in range(1, m + 1):
        pmf = convolve_weighted([quantile_alternative_pmf(v, t) for v in pool_values])
        curve.append({
            "t_top_members": t,
            "q": round(t / m, 6),
            "power": upper_tail(pmf, s_star),
        })
    attaining = [row for row in curve if row["power"] >= target]
    mde_q = max((row["q"] for row in attaining), default=None)
    mde_t = max((row["t_top_members"] for row in attaining), default=None)

    # B2 — exponential tilt, bisection on theta (power is increasing in theta).
    def power_at(theta):
        return upper_tail(convolve_weighted([tilted_pmf(v, theta) for v in pool_values]), s_star)

    def mean_at(theta):
        return sum(sum(x * p for x, p in tilted_pmf(v, theta).items()) for v in pool_values)

    null_mean = sum(sum(v) / len(v) for v in pool_values)
    lo, hi = 0.0, 1.0
    while power_at(hi) < target and hi < 1e6:
        hi *= 2.0
    theta_star, mde_rr = None, None
    if power_at(hi) >= target:
        for _ in range(60):  # well past double precision; each step is a full convolution
            mid = 0.5 * (lo + hi)
            if power_at(mid) >= target:
                hi = mid
            else:
                lo = mid
        theta_star = hi
        mde_rr = mean_at(theta_star) / null_mean if null_mean > 0 else None

    # B3 — lit-locus count: promote loci from pool mode to pool max, greedily, until S >= S*.
    modes, gains = [], []
    for values in pool_values:
        tally = defaultdict(int)
        for value in values:
            tally[value] += 1
        mode = max(sorted(tally), key=lambda v: tally[v])
        modes.append(mode)
        gains.append(max(values) - mode)
    running = sum(modes)
    j_star = 0
    for gain in sorted(gains, reverse=True):
        if running >= s_star:
            break
        running += gain
        j_star += 1
    j_star_reaches = running >= s_star

    return {
        "alpha": alpha,
        "power_target": target,
        "pool_size_m": m,
        "null_mean_S": round(null_mean, 4),
        "null_min_S": min(dp),
        "null_max_S": max(dp),
        "attainable_ceiling_S_max": s_max,
        "S_star_critical_value": s_star,
        "P0_S_ge_S_star": tail_at_star,
        "largest_null_atom": max(dp.values()) / total,
        "design_can_ever_reject": not fatal,
        "B1_quantile_power_curve": curve,
        "B1_MDE_q": mde_q,
        "B1_MDE_top_t_members": mde_t,
        "B2_theta_star": theta_star,
        "B2_MDE_rate_ratio": mde_rr,
        "B3_lit_locus_count_j_star": j_star,
        "B3_reaches_S_star": j_star_reaches,
        "B3_pool_modes": modes,
    }


def power_verdict(power):
    """Prereg §6.5 — transcribed line by line. Where the two criteria disagree, take the more severe."""
    if not power["design_can_ever_reject"]:
        return "UNDERPOWERED-FATAL", {"reason": "S_star exceeds the attainable ceiling"}

    q, rr = power["B1_MDE_q"], power["B2_MDE_rate_ratio"]

    # q-criterion
    if q is None or q <= 0.10:
        sev_q = 2  # SEVERE
    elif q <= 0.25:
        sev_q = 1  # MODERATE
    else:
        sev_q = 0  # ADEQUATE

    # rate-ratio criterion
    if rr is None or rr >= 3.0:
        sev_rr = 2
    elif rr >= 2.0:
        sev_rr = 1
    else:
        sev_rr = 0

    label = {0: "ADEQUATE", 1: "UNDERPOWERED-MODERATE", 2: "UNDERPOWERED-SEVERE"}
    severity = max(sev_q, sev_rr)
    return label[severity], {
        "q_criterion": label[sev_q],
        "rate_ratio_criterion": label[sev_rr],
        "criteria_agree": sev_q == sev_rr,
        "more_severe_taken": label[severity],
    }


# --------------------------------------------------------------------------------------
# Deliverable C — the inferential arms (prereg §7)
# --------------------------------------------------------------------------------------

def monte_carlo_p(pool_values, observed, seed, draws):
    rng = random.Random(seed)
    hits = sum(
        1 for _ in range(draws)
        if sum(rng.choice(values) for values in pool_values) >= observed
    )
    return hits / draws, hits


def analyse_axis(feature, pool_values, observed, labels, seed, monte_carlo, with_power):
    dp, total = exact_convolution(pool_values)
    tail = sum(ways for value, ways in dp.items() if value >= observed)
    p_exact = Fraction(tail, total)
    expected = sum(Fraction(sum(v), len(v)) for v in pool_values)

    result = {
        "feature": feature,
        "observed_sum": observed,
        "null_expected_sum": float(expected),
        "null_min_sum": min(dp),
        "null_max_sum": max(dp),
        "p_exact_raw": float(p_exact),
        "p_exact_fraction": f"{p_exact.numerator}/{p_exact.denominator}",
        "p_bonferroni_corrected": min(1.0, TESTS_IN_FAMILY * float(p_exact)),
        "product_space_size": total,
        "direction_as_locked": observed > float(expected),
        "per_unit": [
            {
                "unit": label,
                "observed": values[0],
                "pool_max": max(values),
                "pool_mean": round(sum(values) / len(values), 4),
                "pool_size": len(values),
            }
            for label, values in zip(labels, pool_values)
        ],
    }
    # Prereg §7.4 — PASS(arm, axis) := dir AND p_raw < alpha
    result["PASS"] = bool(result["direction_as_locked"] and result["p_exact_raw"] < ALPHA_BONFERRONI)
    # Prereg §7.5 — novelty gate
    result["passes_novelty_gate"] = bool(
        result["PASS"] and min(1.0, TESTS_IN_FAMILY * result["p_exact_raw"]) < NOVELTY_GATE
    )
    result["verdict"] = (
        "PASS-NOVELTY" if result["passes_novelty_gate"]
        else "PASS-DIRECTED" if result["PASS"]
        else "REVERSED" if not result["direction_as_locked"]
        else "NULL"
    )

    if monte_carlo:
        p_mc, hits = monte_carlo_p(pool_values, observed, seed, N_MONTE_CARLO)
        p = result["p_exact_raw"]
        tolerance = 5.0 * (p * (1.0 - p) / N_MONTE_CARLO) ** 0.5 + 3.0 / N_MONTE_CARLO
        if abs(p_mc - p) > tolerance:
            raise SystemExit(
                f"Monte Carlo cross-check failed for {feature}: exact={p:.8f} mc={p_mc:.8f}"
            )
        result["monte_carlo_cross_check"] = {
            "seed": seed, "draws": N_MONTE_CARLO, "hits": hits, "p": p_mc, "agrees": True,
        }

    if with_power:
        result["power"] = power_analysis(pool_values, ALPHA_BONFERRONI, POWER_TARGET)
        label, detail = power_verdict(result["power"])
        result["power_verdict"] = label
        result["power_verdict_detail"] = detail
    return result


def match_quality(pools, size_of, labels):
    deltas = []
    for unit in labels:
        target = size_of[unit]
        deltas.extend(abs(size_of[m] - target) for m in pools[unit][1:])
    return {
        "mean_abs_delta_length": round(sum(deltas) / len(deltas), 4),
        "max_abs_delta_length": max(deltas),
        "pct_within_2": round(100.0 * sum(1 for d in deltas if d <= 2) / len(deltas), 2),
    }


def run_arm(name, pools, units, feature_tables, size_of, seed, monte_carlo, with_power):
    axes = {}
    for feature in FEATURES:
        table = feature_tables[feature]
        pool_values = [[table[member] for member in pools[unit]] for unit in units]
        observed = sum(table[unit] for unit in units)
        labels = [f"{u[0]}:{u[1]}" if isinstance(u, tuple) else f"Q{u}" for u in units]
        axes[feature] = analyse_axis(
            feature, pool_values, observed, labels, seed, monte_carlo, with_power
        )
    return {
        "arm": name,
        "n_units": len(units),
        "pool_size": len(pools[units[0]]),
        "length_match_quality": match_quality(pools, size_of, units),
        "axes": axes,
    }


def headline_verdict(c1, c2, c3):
    """Prereg §7.4 — transcribed line by line, first match wins. DO NOT EDIT WITHOUT THE PREREG."""
    def P(arm, axis):
        return arm["axes"][axis]["PASS"]

    def d(arm, axis):
        return arm["axes"][axis]["direction_as_locked"]

    if P(c1, "F1_imperative") and P(c1, "F2_second_person"):
        return "SUPPORTED-BOTH-AXES"
    elif P(c1, "F1_imperative"):
        return "SUPPORTED-PRIMARY"
    elif not d(c1, "F1_imperative"):
        return "NULL - PRE-COMMIT VIOLATION (reversed)"
    elif (P(c2, "F1_imperative") or P(c2, "F2_second_person")
          or P(c3, "F1_imperative") or P(c3, "F2_second_person")):
        return "CONFOUND-EXPLAINED"
    else:
        return "NULL"


# --------------------------------------------------------------------------------------

def self_check():
    dp, total = exact_convolution([[0, 1], [0, 1]])
    assert total == 4 and dp == {0: 1, 1: 2, 2: 1}, dp
    dp, total = exact_convolution([[0, 0, 3], [1, 2]])
    assert total == 6 and dp == {1: 2, 2: 2, 4: 1, 5: 1}, dp

    # critical value: pmf of one draw from [0,0,0,1]; P(S>=1)=1/4, P(S>=2)=0
    dp, total = exact_convolution([[0, 0, 0, 1]])
    assert critical_value(dp, total, 0.5)[0] == 1
    assert critical_value(dp, total, 0.1)[0] == 2

    # quantile alternative: top-1 of [0,0,1,3] is {3}; top-2 is {1,3}
    assert quantile_alternative_pmf([0, 0, 1, 3], 1) == {3: 1.0}
    assert quantile_alternative_pmf([0, 0, 1, 3], 2) == {1: 0.5, 3: 0.5}
    assert quantile_alternative_pmf([0, 0, 1, 3], 99) == {0: 0.5, 1: 0.25, 3: 0.25}

    # tilt: theta=0 recovers the empirical multiset pmf; large theta concentrates on the max
    flat = tilted_pmf([0, 0, 1, 3], 0.0)
    assert abs(flat[0] - 0.5) < 1e-12 and abs(flat[1] - 0.25) < 1e-12
    assert tilted_pmf([0, 0, 1, 3], 50.0)[3] > 0.999999

    # weighted convolution agrees with the uniform exact one
    pools = [[0, 0, 1], [2, 5]]
    dp, total = exact_convolution(pools)
    weighted = convolve_weighted([tilted_pmf(v, 0.0) for v in pools])
    for value, ways in dp.items():
        assert abs(weighted[value] - ways / total) < 1e-12, (value, weighted[value], ways / total)

    # pool builders
    wc = {(1, i): i for i in range(1, 11)}
    pools = build_pools_within_surah(wc, [(1, 5)], 3)
    assert pools[(1, 5)][0] == (1, 5) and set(pools[(1, 5)][1:]) == {(1, 4), (1, 6), (1, 3)}
    wc2 = {(1, 1): 5, (1, 2): 9, (2, 1): 5, (2, 2): 6}
    pools = build_pools_corpus_wide(wc2, [(1, 1)], 2)
    assert pools[(1, 1)] == [(1, 1), (2, 1), (2, 2)], pools

    # power: a design whose ceiling cannot reach S* is FATAL
    tiny = power_analysis([[0, 1]], 0.001, 0.8)
    assert not tiny["design_can_ever_reject"]
    assert power_verdict(tiny)[0] == "UNDERPOWERED-FATAL"

    # headline verdict, all five branches of prereg §7.4
    def arm(f1_pass, f2_pass, f1_dir=True):
        return {"axes": {
            "F1_imperative": {"PASS": f1_pass, "direction_as_locked": f1_dir},
            "F2_second_person": {"PASS": f2_pass, "direction_as_locked": True},
        }}
    dead = arm(False, False)
    assert headline_verdict(arm(True, True), dead, dead) == "SUPPORTED-BOTH-AXES"
    assert headline_verdict(arm(True, False), dead, dead) == "SUPPORTED-PRIMARY"
    assert headline_verdict(arm(False, False, False), dead, dead).startswith("NULL - PRE-COMMIT")
    assert headline_verdict(dead, arm(True, False), dead) == "CONFOUND-EXPLAINED"
    assert headline_verdict(dead, dead, arm(False, True)) == "CONFOUND-EXPLAINED"
    assert headline_verdict(dead, dead, dead) == "NULL"
    print("self-check OK")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return

    repo_root = Path(__file__).resolve().parents[3]
    prereg = repo_root / "findings/phase-b-hypotheses/prereg-h-new-3030-sajdah-glyph.md"
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"

    hashes = {
        "prereg": sha256(prereg),
        "qac": sha256(qac),
        "quran_no_tashkeel": sha256(repo_root / "quran-text/quran-no-tashkeel.json"),
        "quran_full_tashkeel": sha256(repo_root / "quran-text/quran-full-tashkeel.json"),
        "script": sha256(Path(__file__).resolve()),
    }
    expected = {
        "prereg": EXPECTED_PREREG_SHA,
        "qac": EXPECTED_QAC_SHA,
        "quran_no_tashkeel": EXPECTED_QURAN_NO_TASHKEEL_SHA,
        "quran_full_tashkeel": EXPECTED_QURAN_FULL_TASHKEEL_SHA,
    }
    for key, want in expected.items():
        if hashes[key] != want:
            raise SystemExit(f"{key} SHA mismatch: expected {want}, found {hashes[key]}")

    # Prereg §8 — every gate aborts BEFORE a run directory exists.
    census = run_census(repo_root)
    if not census["locus_sets_identical_across_keyed_variants"]:
        raise SystemExit("keyed text variants disagree on the locus set; inspect before testing")
    if not census["matches_h_new_2950_locus_set"]:
        raise SystemExit("census locus set differs from H-NEW-2950's; this is a correction, not a run")

    word_count, counts = parse_qac(qac)
    loci = list(EXPECTED_LOCI)
    missing = [l for l in loci if l not in word_count]
    if missing:
        raise SystemExit(f"QAC is missing sajdah verses: {missing}")

    surah_words = defaultdict(int)
    surah_counts = {
        excl: {feature: defaultdict(int) for feature in FEATURES}
        for excl in ("sjd_excluded", "sjd_included")
    }
    for (surah, verse), n_words in word_count.items():
        surah_words[surah] += n_words
        for excl in surah_counts:
            for feature in FEATURES:
                surah_counts[excl][feature][surah] += counts[excl][feature][(surah, verse)]
    surah_words = dict(surah_words)
    sajdah_surahs = sorted({s for s, _ in EXPECTED_LOCI})

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-3030" / run_id
    os.makedirs(run_dir, exist_ok=False)

    arms = {}
    for k_label, k in (("K15", K_PRIMARY), ("K10", K_SENSITIVITY)):
        arms[f"C1_within_surah_{k_label}"] = run_arm(
            f"C1 within-surah (replication of H-NEW-2950), K={k}",
            build_pools_within_surah(word_count, loci, k), loci,
            counts["sjd_excluded"], word_count, SEED,
            monte_carlo=(k == K_PRIMARY), with_power=True,
        )
        arms[f"C2_corpus_wide_{k_label}"] = run_arm(
            f"C2 corpus-wide, K={k}",
            build_pools_corpus_wide(word_count, loci, k), loci,
            counts["sjd_excluded"], word_count, SEED,
            monte_carlo=(k == K_PRIMARY), with_power=True,
        )
    arms["C3_surah_level_K7"] = run_arm(
        f"C3 surah-level, K={K_SURAH}",
        build_pools_surah_level(surah_words, sajdah_surahs, K_SURAH), sajdah_surahs,
        surah_counts["sjd_excluded"], surah_words, SEED,
        monte_carlo=True, with_power=True,
    )

    # Prereg §3 third tuple — diagnostic, NOT gated, cannot support a PASS.
    diagnostic = run_arm(
        "DIAGNOSTIC sjd-INCLUDED within-surah K=15 (circular form)",
        build_pools_within_surah(word_count, loci, K_PRIMARY), loci,
        counts["sjd_included"], word_count, SEED, monte_carlo=False, with_power=False,
    )
    for axis in diagnostic["axes"].values():
        axis["PASS"] = False
        axis["passes_novelty_gate"] = False
        axis["verdict"] = "DIAGNOSTIC - NOT GATED, CANNOT SUPPORT A PASS (prereg §3)"

    headline = headline_verdict(
        arms["C1_within_surah_K15"], arms["C2_corpus_wide_K15"], arms["C3_surah_level_K7"]
    )
    primary_power = arms["C1_within_surah_K15"]["axes"]["F1_imperative"]

    result = {
        "id": "H-NEW-3030",
        "prereg_sha256": EXPECTED_PREREG_SHA,
        "n_loci": len(loci),
        "tests_in_family": TESTS_IN_FAMILY,
        "alpha_bonferroni": ALPHA_BONFERRONI,
        "novelty_gate": NOVELTY_GATE,
        "power_target": POWER_TARGET,
        "tie_fractions_prereg_s5": tie_fractions(word_count, counts),
        "census_deliverable_A": census,
        "arms_deliverable_C": arms,
        "diagnostic_arm_not_gated": diagnostic,
        "headline_verdict": headline,
        "power_verdict_deliverable_B": primary_power["power_verdict"],
        "power_verdict_detail": primary_power["power_verdict_detail"],
        "h_new_2950_published_p": {
            "F1_imperative_K15": 0.4335, "F2_second_person_K15": 0.3588,
            "F1_imperative_K10": 0.5065, "F2_second_person_K10": 0.3836,
        },
        "inference_is_exact": (
            "Every p is an exact convolution over the full product space. No parametric test "
            "appears anywhere in this design (prereg §5: tie fraction 0.7965 on F1)."
        ),
    }

    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    manifest = {
        "id": "H-NEW-3030",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "git_commit": git_output(repo_root, "rev-parse", "HEAD"),
        "git_status_porcelain": git_output(repo_root, "status", "--porcelain"),
        "hashes_sha256": hashes,
        "expected_hashes_sha256": expected,
        "input_paths_repo_relative": {
            "prereg": "findings/phase-b-hypotheses/prereg-h-new-3030-sajdah-glyph.md",
            "qac": "data/morphology/quranic-corpus-morphology-0.4.txt",
            "quran_no_tashkeel": "quran-text/quran-no-tashkeel.json",
            "quran_full_tashkeel": "quran-text/quran-full-tashkeel.json",
            "script": "findings/phase-b-hypotheses/scripts/h-new-3030.py",
        },
        "python": sys.version,
        "platform": platform.platform(),
        "seed": SEED,
        "seed_role": "Monte-Carlo correctness cross-check only; the inference is exact and deterministic",
        "n_monte_carlo_cross_check": N_MONTE_CARLO,
        "run_directory": str(run_dir.relative_to(repo_root)),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "run_dir": str(run_dir.relative_to(repo_root)),
        "census_n_loci": census["n_verses"],
        "census_matches_2950": census["matches_h_new_2950_locus_set"],
        "headline_verdict": headline,
        "power_verdict": primary_power["power_verdict"],
        "S_star": primary_power["power"]["S_star_critical_value"],
        "observed": primary_power["observed_sum"],
        "MDE_q": primary_power["power"]["B1_MDE_q"],
        "MDE_rate_ratio": primary_power["power"]["B2_MDE_rate_ratio"],
        "j_star": primary_power["power"]["B3_lit_locus_count_j_star"],
        "p_raw": {
            name: {f: arm["axes"][f]["p_exact_raw"] for f in FEATURES}
            for name, arm in arms.items()
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
