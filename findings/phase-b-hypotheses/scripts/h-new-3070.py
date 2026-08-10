#!/usr/bin/env python3
"""H-NEW-3070 — does the proximal/distal deictic balance shift across the Noldeke phases?

Tests clause 2 of frontier item F-4 ONLY. Clause 1 (deixis x eschatological reference) was
executed by H-NEW-2960 on 2026-08-08 and returned NULL; it is not re-run here.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-3070-deictic-gradient.md
The SHA-256 of that file is embedded below and re-verified before the run directory is created.
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np
from scipy.stats import rankdata, norm

# ---------------------------------------------------------------- prereg lock
EXPECTED_PREREG_SHA = "83bdecc61c8e82df366f05f1112121ff23678d17d0c6bf25c4e39955e9a17bee"
PREREG_PATH = "findings/phase-b-hypotheses/prereg-h-new-3070-deictic-gradient.md"

# ---------------------------------------------------------------- locked constants (prereg SS4, SS5, SS8)
SEED_PRIMARY = 20260509
N_PERM = 10_000
ALPHA_BONFERRONI = 0.05 / 2          # prereg SS8: k = 2 verdict-bearing hypotheses
BIN_WIDTHS = {"quintile": 5, "decile": 10}
CHANNELS = ["L1_verse_count", "L2_word_count", "L3_mean_verse_length", "L4_dem_count"]
D3_TOP_M = 10                        # prereg SS6 arm A3

QAC_PATH = "data/morphology/quranic-corpus-morphology-0.4.txt"
CHRON_PATH = "data/revelation-order.csv"
RUN_ROOT = "findings/phase-b-hypotheses/runs/h-new-3070"

# prereg SS2.1 — H-NEW-2960's validated rule, adopted verbatim
KAF_KHITAB_RE = re.compile(r"(?:ka|ki|kumo|kumu|kumaA|kum|kun~a)$")
# prereg SS7 R3 — the independent lemma partition, used as an alternative rules-tuple
LEMMA_PROXIMAL = {"ha`*aA", "*aA", "ha`*a`n", "ha`tayon", "hunaA", "ha`ka*aA"}
LEMMA_DISTAL = {"*a`lik", ">uwla`^}ik", ">uwlaA^'", "tilokum", "*a`nik"}

PHASE_ORDINAL = {"Early Meccan": 1, "Middle Meccan": 2, "Late Meccan": 3, "Medinan": 4}
PERIOD_ORDINAL = {"Meccan": 1, "Medinan": 2}

LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")


# ---------------------------------------------------------------- loading
def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    actual = sha256_of(PREREG_PATH)
    if actual != EXPECTED_PREREG_SHA:
        raise SystemExit(
            f"PREREG SHA MISMATCH — refusing to run.\n"
            f"  expected {EXPECTED_PREREG_SHA}\n  actual   {actual}\n"
            f"  path     {PREREG_PATH}")
    return actual


def load_qac():
    rows = []
    with open(QAC_PATH, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOCATION_RE.match(parts[0])
            if not m:
                continue
            s, v, w, g = (int(x) for x in m.groups())
            rows.append({"s": s, "v": v, "w": w, "g": g, "form": parts[1], "feat": parts[3]})
    return rows


def load_chronology():
    chron = {}
    with open(CHRON_PATH, encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            chron[int(r["mushaf_order"])] = {
                "noldeke_phase": r["noldeke_phase"],
                "noldeke_phase_ord": PHASE_ORDINAL[r["noldeke_phase"]],
                "revelation_order": int(r["revelation_order"]),
                "noldeke_order": int(r["noldeke_order"]),
                "period_ord": PERIOD_ORDINAL[r["period"]],
            }
    return chron


def has_pos(feat, tag):
    return re.search(rf"(^|\|)POS:{tag}(\||$)", feat) is not None


def lemma_of(feat):
    m = re.search(r"LEM:([^|]*)", feat)
    return m.group(1) if m else None


# ---------------------------------------------------------------- instruments
def deixis_kaf(form):
    """prereg SS2.1 — DISTAL iff the FORM ends in the addressee-kaf enclitic."""
    return "DISTAL" if KAF_KHITAB_RE.search(form) else "PROXIMAL"


def deixis_lemma(feat):
    """prereg SS7 R3 — the independent lemma partition."""
    lem = lemma_of(feat)
    if lem in LEMMA_PROXIMAL:
        return "PROXIMAL"
    if lem in LEMMA_DISTAL:
        return "DISTAL"
    return None


def surah_channels(rows):
    """prereg SS5 — per-surah length channels, all computed from QAC."""
    verses = defaultdict(set)
    words = set()
    for r in rows:
        verses[r["s"]].add(r["v"])
        words.add((r["s"], r["v"], r["w"]))
    wc = Counter(s for (s, _v, _w) in words)
    ch = {}
    for s in verses:
        nv, nw = len(verses[s]), wc[s]
        ch[s] = {"L1_verse_count": float(nv), "L2_word_count": float(nw),
                 "L3_mean_verse_length": nw / nv}
    return ch


def phrase_types(dem, rows):
    """prereg SS6 A3 — (DEM form, next word's first STEM form), ranked CORPUS-WIDE."""
    stems = defaultdict(list)
    for r in rows:
        if "STEM" in r["feat"]:
            stems[(r["s"], r["v"], r["w"])].append(r)
    types, counts = {}, Counter()
    for r in dem:
        nxt = stems.get((r["s"], r["v"], r["w"] + 1))
        follower = min(nxt, key=lambda x: x["g"])["form"] if nxt else "∅"
        key = (r["form"], follower)
        types[(r["s"], r["v"], r["w"], r["g"])] = key
        counts[key] += 1
    return types, counts


# ---------------------------------------------------------------- statistics
def token_table(tokens, deixis_field):
    """Per-surah (n_distal, n_proximal) over the supplied token list."""
    d, p = Counter(), Counter()
    for t in tokens:
        if t[deixis_field] == "DISTAL":
            d[t["s"]] += 1
        elif t[deixis_field] == "PROXIMAL":
            p[t["s"]] += 1
    surahs = sorted(set(d) | set(p))
    return (np.array(surahs, dtype=int),
            np.array([d[s] for s in surahs], dtype=float),
            np.array([p[s] for s in surahs], dtype=float))


def s1_weights(nd, npx):
    """S1 = mean(phase|DISTAL) - mean(phase|PROXIMAL) = sum_s phase_s * w_s.

    D and P are invariant under a surah-label permutation, so S1 is LINEAR in the
    permuted phase vector. That is what makes the 10,000-permutation sweep cheap.
    """
    D, P = nd.sum(), npx.sum()
    if D == 0 or P == 0:
        return None
    return nd / D - npx / P


def strata_of(values, n_bins):
    """prereg SS5 — rank-bin the surahs; ties broken deterministically by ascending index."""
    order = np.lexsort((np.arange(len(values)), values))
    ranks = np.empty(len(values), dtype=int)
    ranks[order] = np.arange(len(values))
    return (ranks * n_bins) // len(values)


def permute_within(labels, strata, n_perm, rng):
    """Vectorised within-stratum permutation of `labels`. Returns (n_perm, n) array."""
    n = len(labels)
    if strata is None:
        strata = np.zeros(n, dtype=int)
    grouped = np.argsort(strata, kind="stable")
    keys = strata[None, :].astype(float) + rng.random((n_perm, n))
    order = np.argsort(keys, axis=1)
    out = np.empty((n_perm, n), dtype=float)
    out[:, grouped] = labels[order]
    return out


def informative_strata(strata, labels):
    """prereg SS5 — how much permutation freedom the stratification actually leaves."""
    if strata is None:
        return {"n_strata": 1, "n_informative": int(len(set(labels.tolist())) > 1),
                "share_surahs_informative": 1.0 if len(set(labels.tolist())) > 1 else 0.0}
    n_inf, n_surah_inf = 0, 0
    for st in np.unique(strata):
        mask = strata == st
        if len(np.unique(labels[mask])) > 1:
            n_inf += 1
            n_surah_inf += int(mask.sum())
    return {"n_strata": int(len(np.unique(strata))), "n_informative": n_inf,
            "share_surahs_informative": n_surah_inf / len(labels)}


def perm_p(obs, null):
    """prereg SS4 — one-sided upper, p = (1 + #{null >= obs}) / (1 + n_perm)."""
    return (1.0 + float(np.sum(null >= obs))) / (1.0 + len(null))


def tie_diagnostic(obs, null):
    """prereg SS4 — required null-distribution tie diagnostic."""
    return {"n_distinct_null_values": int(len(np.unique(null))),
            "frac_null_exactly_equal_obs": float(np.mean(np.isclose(null, obs)))}


def run_cell(hyp, phase, nd, npx, strata, n_perm, rng):
    """One (hypothesis, channel-setting) cell. Returns obs, p, null summary."""
    if hyp == "H1":
        w = s1_weights(nd, npx)
        if w is None:
            return None
        obs = float(np.dot(phase, w))
        perms = permute_within(phase, strata, n_perm, rng)
        null = perms @ w
    else:  # H2 — Spearman rho(phase, per-surah distal share), tie-corrected average ranks
        share = nd / (nd + npx)
        r_share = rankdata(share)
        r_phase = rankdata(phase)
        rs = r_share - r_share.mean()
        rp_c = r_phase - r_phase.mean()
        denom = np.sqrt((rs ** 2).sum() * (rp_c ** 2).sum())
        if denom == 0:
            return None
        obs = float(np.dot(rp_c, rs) / denom)
        # the MULTISET of average ranks is invariant under permutation, so mean and sd
        # of r_phase are fixed and the null is linear in the permuted rank vector.
        perms = permute_within(r_phase, strata, n_perm, rng)
        null = (perms - r_phase.mean()) @ rs / denom
    return {"obs": obs, "p": perm_p(obs, null),
            "null_mean": float(null.mean()), "null_sd": float(null.std(ddof=1)),
            "null_q975": float(np.quantile(null, 1 - ALPHA_BONFERRONI)),
            **tie_diagnostic(obs, null)}


# ---------------------------------------------------------------- power / MDE (prereg SS9)
def s_max_attainable(phase_pool, nd, npx):
    """Largest S1 reachable by ANY assignment of the observed phase multiset to surahs.

    S1 is linear with weights w_s, so the maximum is the greedy pairing of the largest
    phase values with the largest weights (rearrangement inequality).
    """
    w = s1_weights(nd, npx)
    if w is None:
        return None
    return float(np.dot(np.sort(phase_pool), np.sort(w)))


def simulate_power(phase, nd, npx, slope, base, n_sim, rng, s_star_h1, s_star_h2):
    """Re-draw every token's deixis with P(distal | phase) = base + slope*(phase - pbar).

    Keeps the surah/phase/exposure structure exactly as observed and varies only the
    deixis labels, so the binomial variance is the real one rather than a normal proxy.
    """
    n_tok = (nd + npx).astype(int)
    pbar = float(np.dot(phase, n_tok) / n_tok.sum())
    pr = np.clip(base + slope * (phase - pbar), 1e-9, 1 - 1e-9)
    draws = rng.binomial(n_tok[None, :].repeat(n_sim, axis=0), pr[None, :])
    d_sim = draws.astype(float)
    p_sim = n_tok[None, :] - d_sim
    D = d_sim.sum(axis=1)
    P = p_sim.sum(axis=1)
    ok = (D > 0) & (P > 0)
    s1 = np.full(n_sim, np.nan)
    s1[ok] = (d_sim[ok] @ phase) / D[ok] - (p_sim[ok] @ phase) / P[ok]
    share = np.divide(d_sim, n_tok[None, :], out=np.zeros_like(d_sim),
                      where=n_tok[None, :] > 0)
    r_phase = rankdata(phase)
    rp = r_phase - r_phase.mean()
    s2 = np.full(n_sim, np.nan)
    for i in range(n_sim):
        rs = rankdata(share[i])
        rs = rs - rs.mean()
        den = np.sqrt((rs ** 2).sum() * (rp ** 2).sum())
        if den > 0:
            s2[i] = float(np.dot(rp, rs) / den)
    return {"mean_s1": float(np.nanmean(s1)),
            "power_h1": float(np.nanmean(s1 >= s_star_h1)),
            "power_h2": float(np.nanmean(s2 >= s_star_h2))}


def slope_for_target(phase, nd, npx, target, base):
    """Bisection: find the slope whose expected S1 equals `target`."""
    n_tok = (nd + npx).astype(float)
    pbar = float(np.dot(phase, n_tok) / n_tok.sum())

    def expected_s1(slope):
        pr = np.clip(base + slope * (phase - pbar), 1e-9, 1 - 1e-9)
        d, p = n_tok * pr, n_tok * (1 - pr)
        if d.sum() == 0 or p.sum() == 0:
            return np.nan
        return float(np.dot(phase, d) / d.sum() - np.dot(phase, p) / p.sum())

    lo, hi = 0.0, 1.0
    for _ in range(200):
        if expected_s1(hi) >= target or hi > 1e6:
            break
        hi *= 2
    for _ in range(200):
        mid = (lo + hi) / 2
        if expected_s1(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def power_block(phase, nd, npx, s_star_h1, s_star_h2, sd_h1, rng, n_sim=2000):
    """prereg SS9 — S*, S_max, the untestable branch, MDE at 80% power, power at 0.25."""
    base = float(nd.sum() / (nd.sum() + npx.sum()))
    smax = s_max_attainable(phase, nd, npx)
    out = {"S_star_H1": s_star_h1, "S_star_H2": s_star_h2, "S_max_H1": smax,
           "untestable_at_this_n": bool(smax is not None and s_star_h1 > smax),
           "normal_approx_MDE_H1": float(s_star_h1 + norm.ppf(0.80) * sd_h1)}
    out["power_at_delta_0.25"] = simulate_power(
        phase, nd, npx, slope_for_target(phase, nd, npx, 0.25, base), base,
        n_sim, rng, s_star_h1, s_star_h2)
    lo, hi, mde = 0.0, 3.0, None
    for _ in range(14):
        mid = (lo + hi) / 2
        pw = simulate_power(phase, nd, npx, slope_for_target(phase, nd, npx, mid, base),
                            base, 600, rng, s_star_h1, s_star_h2)["power_h1"]
        if pw < 0.80:
            lo = mid
        else:
            hi = mid
            mde = mid
    out["MDE_H1_simulated_80pct_power"] = mde if mde is not None else float("nan")
    return out


# ---------------------------------------------------------------- self-check
def self_check():
    assert deixis_kaf("ha`ka*aA") == "PROXIMAL", "hakadha: its kaf is not final"
    assert deixis_kaf("*a`lika") == "DISTAL"
    assert deixis_kaf("ha`^&ulaA^'i") == "PROXIMAL"
    assert deixis_kaf(">uw@la`^}ikumo") == "DISTAL"
    # permutation p on a hand-computable case: obs at the maximum of a 4-point null
    null = np.array([1.0, 2.0, 3.0, 4.0])
    assert abs(perm_p(4.0, null) - (1 + 1) / (1 + 4)) < 1e-12
    assert abs(perm_p(0.0, null) - (1 + 4) / (1 + 4)) < 1e-12
    # strata: 10 values into 5 bins -> 2 per bin, monotone
    st = strata_of(np.array([5.0, 1, 9, 3, 7, 2, 8, 4, 6, 0]), 5)
    assert sorted(Counter(st.tolist()).values()) == [2, 2, 2, 2, 2]
    # within-stratum permutation never moves a label across strata
    rng = np.random.default_rng(0)
    lab = np.arange(10, dtype=float)
    perms = permute_within(lab, st, 200, rng)
    for row in perms:
        # the label that lands at position j must have come from j's own stratum
        assert all(st[int(row[j])] == st[j] for j in range(10))
        assert sorted(row.tolist()) == list(range(10))
    # rearrangement inequality: phase [1,2], w = [1,-1] -> max is 2*1 + 1*(-1) = 1
    assert abs(s_max_attainable(np.array([1.0, 2.0]), np.array([1.0, 0.0]),
                                np.array([0.0, 1.0])) - 1.0) < 1e-12
    print("self-check OK")


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()
    if args.self_check:
        self_check()
        return

    self_check()
    prereg_sha = verify_prereg()

    rows = load_qac()
    chron = load_chronology()
    channels = surah_channels(rows)

    dem = [r for r in rows if has_pos(r["feat"], "DEM")]
    for r in dem:
        r["deixis_kaf"] = deixis_kaf(r["form"])
        r["deixis_lemma"] = deixis_lemma(r["feat"])

    census = {
        "n_dem": len(dem),
        "n_loc": sum(1 for r in rows if has_pos(r["feat"], "LOC")),
        "n_t": sum(1 for r in rows if has_pos(r["feat"], "T")),
        "n_distal_kaf": sum(1 for r in dem if r["deixis_kaf"] == "DISTAL"),
        "n_proximal_kaf": sum(1 for r in dem if r["deixis_kaf"] == "PROXIMAL"),
        "kaf_vs_lemma_disagreements": sum(
            1 for r in dem if r["deixis_lemma"] and r["deixis_lemma"] != r["deixis_kaf"]),
        "n_lemma_unclassified": sum(1 for r in dem if r["deixis_lemma"] is None),
    }

    # ---- arms (prereg SS6)
    by_word = defaultdict(list)
    for r in rows:
        by_word[(r["s"], r["v"], r["w"])].append(r)
    inl_surahs = sorted({r["s"] for r in rows if has_pos(r["feat"], "INL")})
    ptypes, pcounts = phrase_types(dem, rows)
    ranked = [t for t, _ in pcounts.most_common()]
    top_m = set(ranked[:D3_TOP_M])

    def key_of(r):
        return (r["s"], r["v"], r["w"], r["g"])

    open_set = {key_of(r) for r in dem if r["s"] in inl_surahs and r["v"] <= 3}
    ka_set = {key_of(r) for r in dem
              if any("ka+" in x["feat"] for x in by_word[(r["s"], r["v"], r["w"])]
                     if x["g"] < r["g"])}
    a3_set = {key_of(r) for r in dem if ptypes[key_of(r)] in top_m}

    arms = {
        "A0_full": dem,
        "A1_no_muqattaat_openings": [r for r in dem if key_of(r) not in open_set],
        "A2_no_ka_prefixed": [r for r in dem if key_of(r) not in ka_set],
        f"A3_no_top{D3_TOP_M}_phrase_types": [r for r in dem if key_of(r) not in a3_set],
        "A4_no_openings_no_ka_no_top10": [
            r for r in dem
            if key_of(r) not in open_set and key_of(r) not in ka_set and key_of(r) not in a3_set],
    }

    tuples = {
        "R1_noldeke_phase_kaf": ("noldeke_phase_ord", "deixis_kaf"),
        "R2_revelation_order_kaf": ("revelation_order", "deixis_kaf"),
        "R3_noldeke_phase_lemma": ("noldeke_phase_ord", "deixis_lemma"),
        "R4_period_kaf": ("period_ord", "deixis_kaf"),
    }

    results, diagnostics = {}, {}
    for tname, (chron_field, dfield) in tuples.items():
        for aname, tokens in arms.items():
            surahs, nd, npx = token_table(tokens, dfield)
            if len(surahs) == 0:
                continue
            phase = np.array([chron[s][chron_field] for s in surahs], dtype=float)
            ch_vals = {c: np.array([channels[s][c] for s in surahs], dtype=float)
                       for c in CHANNELS[:3]}
            ch_vals["L4_dem_count"] = nd + npx

            settings = [("L0_unstratified", None)]
            for c in CHANNELS:
                for bname, nb in BIN_WIDTHS.items():
                    settings.append((f"{c}|{bname}", strata_of(ch_vals[c], nb)))

            for hyp in ("H1", "H2"):
                for sname, strata in settings:
                    rng = np.random.default_rng(SEED_PRIMARY)
                    cell = run_cell(hyp, phase, nd, npx, strata, N_PERM, rng)
                    if cell is None:
                        continue
                    cell["informative_strata"] = informative_strata(strata, phase)
                    results[f"{tname}|{aname}|{hyp}|{sname}"] = cell
            diagnostics[f"{tname}|{aname}"] = {
                "n_surahs": len(surahs), "n_tokens": int((nd + npx).sum()),
                "n_distal": int(nd.sum()), "n_proximal": int(npx.sum()),
            }

    # ---- verdict, transcribed line by line from prereg SS8
    def p_worst(hyp, arm, tup):
        ps = [v["p"] for k, v in results.items()
              if k.startswith(f"{tup}|{arm}|{hyp}|")]
        return max(ps) if ps else None

    def obs_at(hyp, arm, tup, setting="L0_unstratified"):
        return results.get(f"{tup}|{arm}|{hyp}|{setting}", {}).get("obs")

    pw_h1 = p_worst("H1", "A0_full", "R1_noldeke_phase_kaf")
    pw_h2 = p_worst("H2", "A0_full", "R1_noldeke_phase_kaf")
    o_h1 = obs_at("H1", "A0_full", "R1_noldeke_phase_kaf")
    o_h2 = obs_at("H2", "A0_full", "R1_noldeke_phase_kaf")

    direction_ok = (o_h1 is not None and o_h1 > 0) and (o_h2 is not None and o_h2 > 0)
    passes = (pw_h1 is not None and pw_h1 < ALPHA_BONFERRONI
              and pw_h2 is not None and pw_h2 < ALPHA_BONFERRONI
              and direction_ok)

    verdict = "PASS" if passes else "NULL"
    formulaic = None
    if passes:
        # prereg SS8 — the formula read happens IF AND ONLY IF the verdict is PASS
        a1 = (p_worst("H1", "A1_no_muqattaat_openings", "R1_noldeke_phase_kaf"),
              p_worst("H2", "A1_no_muqattaat_openings", "R1_noldeke_phase_kaf"))
        a4 = (p_worst("H1", "A4_no_openings_no_ka_no_top10", "R1_noldeke_phase_kaf"),
              p_worst("H2", "A4_no_openings_no_ka_no_top10", "R1_noldeke_phase_kaf"))
        a1_fail = any(p is None or p >= ALPHA_BONFERRONI for p in a1)
        a4_fail = any(p is None or p >= ALPHA_BONFERRONI for p in a4)
        formulaic = {"A1_worst": a1, "A4_worst": a4, "A1_fails": a1_fail, "A4_fails": a4_fail}
        if a1_fail or a4_fail:
            verdict = "CONFIRMED-BUT-FORMULAIC"

    # ---- which channel is DOMINANT (the brief's explicit ask)
    dominant = {}
    for hyp in ("H1", "H2"):
        cells = {k.split("|", 3)[3]: v["p"] for k, v in results.items()
                 if k.startswith(f"R1_noldeke_phase_kaf|A0_full|{hyp}|")}
        if cells:
            dominant[hyp] = {"worst_setting": max(cells, key=cells.get),
                             "worst_p": max(cells.values()),
                             "best_setting": min(cells, key=cells.get),
                             "best_p": min(cells.values()),
                             "p_swing_ratio": max(cells.values()) / min(cells.values()),
                             "all": cells}

    # ---- power / MDE (prereg SS9) — required on NULL, computed regardless
    surahs0, nd0, npx0 = token_table(arms["A0_full"], "deixis_kaf")
    phase0 = np.array([chron[s]["noldeke_phase_ord"] for s in surahs0], dtype=float)
    worst_h1_key = f"R1_noldeke_phase_kaf|A0_full|H1|{dominant['H1']['worst_setting']}"
    worst_h2_key = f"R1_noldeke_phase_kaf|A0_full|H2|{dominant['H2']['worst_setting']}"
    power = {
        "at_worst_channel": power_block(
            phase0, nd0, npx0,
            results[worst_h1_key]["null_q975"], results[worst_h2_key]["null_q975"],
            results[worst_h1_key]["null_sd"], np.random.default_rng(SEED_PRIMARY)),
        "at_L0_unstratified": power_block(
            phase0, nd0, npx0,
            results["R1_noldeke_phase_kaf|A0_full|H1|L0_unstratified"]["null_q975"],
            results["R1_noldeke_phase_kaf|A0_full|H2|L0_unstratified"]["null_q975"],
            results["R1_noldeke_phase_kaf|A0_full|H1|L0_unstratified"]["null_sd"],
            np.random.default_rng(SEED_PRIMARY)),
        "worst_channel_H1": dominant["H1"]["worst_setting"],
        "worst_channel_H2": dominant["H2"]["worst_setting"],
    }

    # ---- descriptive: distal share by phase (reported, carries no p-value)
    descriptive = {}
    for ph, ordv in PHASE_ORDINAL.items():
        mask = phase0 == ordv
        descriptive[ph] = {
            "n_surahs_with_dem": int(mask.sum()),
            "n_tokens": int((nd0 + npx0)[mask].sum()),
            "n_distal": int(nd0[mask].sum()),
            "token_level_distal_share": float(nd0[mask].sum() / (nd0 + npx0)[mask].sum()),
            "mean_per_surah_distal_share": float(
                np.mean((nd0 / (nd0 + npx0))[mask])),
        }

    run_dir = os.path.join(RUN_ROOT, datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    os.makedirs(run_dir, exist_ok=False)

    payload = {
        "hypothesis": "H-NEW-3070",
        "scope": "F-4 clause 2 ONLY (chronological gradient). Clause 1 answered by H-NEW-2960.",
        "prereg_sha256": prereg_sha,
        "seed": SEED_PRIMARY, "n_permutations": N_PERM,
        "alpha_bonferroni": ALPHA_BONFERRONI,
        "census": census,
        "muqattaat_surahs_from_POS_INL": inl_surahs,
        "n_dropped_by_arm": {k: len(dem) - len(v) for k, v in arms.items()},
        "top_phrase_types": [{"dem_form": t[0], "next_form": t[1], "n": n}
                             for t, n in pcounts.most_common(D3_TOP_M)],
        "descriptive_by_phase": descriptive,
        "diagnostics": diagnostics,
        "dominant_channel": dominant,
        "results": results,
        "power_and_mde": power,
        "verdict": {
            "verdict": verdict,
            "p_worst_H1_A0_R1": pw_h1, "p_worst_H2_A0_R1": pw_h2,
            "obs_H1_L0": o_h1, "obs_H2_L0": o_h2,
            "direction_as_locked": direction_ok,
            "formulaic_read": formulaic,
        },
    }
    with open(os.path.join(run_dir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    with open(os.path.join(run_dir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump({
            "script_sha256": sha256_of(__file__),
            "prereg_sha256": prereg_sha,
            "qac_sha256": sha256_of(QAC_PATH),
            "chronology_sha256": sha256_of(CHRON_PATH),
            "python": sys.version, "numpy": np.__version__,
            "utc": datetime.now(timezone.utc).isoformat(),
        }, fh, indent=2)

    print(f"run dir: {run_dir}")
    print(f"census: DEM={census['n_dem']} distal={census['n_distal_kaf']} "
          f"proximal={census['n_proximal_kaf']} "
          f"kaf-vs-lemma disagreements={census['kaf_vs_lemma_disagreements']}")
    print(f"VERDICT: {verdict}")
    print(f"  H1 obs={o_h1:.5f} p_worst={pw_h1:.5f}   (worst {dominant['H1']['worst_setting']})")
    print(f"  H2 obs={o_h2:.5f} p_worst={pw_h2:.5f}   (worst {dominant['H2']['worst_setting']})")
    print(f"  alpha={ALPHA_BONFERRONI}")


if __name__ == "__main__":
    main()
