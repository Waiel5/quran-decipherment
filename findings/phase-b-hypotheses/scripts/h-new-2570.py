#!/usr/bin/env python3
"""
H-NEW-2570 — Is the mushaf order a lexical curriculum? Vocabulary-introduction geometry.

Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md
Pre-reg SHA-256 verified at runtime; the script aborts on mismatch.

PRIMARY NULL IS LENGTH-PRESERVING (N2). The uniform null (N1) is registered but declared
insufficient in the pre-reg: the mushaf is roughly long-to-short ordered, so any
length-sensitive statistic separates it from a uniform permutation trivially.

Directions locked before computation (pre-reg §5):
  J (power-law-residual jerk)   mushaf/revelation LOWER than N1, N2 ; mushaf HIGHER than N3
  A (mean |log-residual| Heaps) mushaf/revelation LOWER than N1, N2 ; mushaf HIGHER than N3
  beta (Heaps exponent)         mushaf HIGHER than N1, N2   (deferral of hapax-rich surahs)
Bonferroni k = 12, alpha = 0.05/12 = 0.0041667.

Seeds 20260509 (primary) / 20260519 (replication). 10,000 permutations per null.
Stdlib only (Investigation Protocol section 7.1).

Author: Waiel Al-Shujaa.
"""

import csv
import glob
import hashlib
import json
import math
import os
import random
import re
import unicodedata
from bisect import bisect_left

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2570-lexical-curriculum.md")
EXPECTED_SHA = "6a1cab4cddb21d0621ffff6d9d57aa974bf7eaa76b865da67ac830a3f1f4e29b"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
REVCSV = os.path.join(ROOT, "data/revelation-order.csv")
QURAN_NT = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
BASE_RAW = os.path.join(ROOT, "data/baseline-corpora/raw")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2570.json")

SEED_PRIMARY, SEED_REPLICATION = 20260509, 20260519
NPERM = 10000
BONF_K = 12
ALPHA = 0.05 / BONF_K

# Evaluation grids (M, N0). (50, 500) is the pre-registered primary.
GRIDS = [(50, 500), (30, 500), (80, 500), (50, 200), (50, 1000)]
GRID_PRIMARY = (50, 500)
BLOCKS_LIN = [100, 200, 400]      # J_lin robustness variant (equal-N blocks)
STRATUM_PRIMARY = 6               # 19 strata of 6
STRATUM_LOOSE = 19                # 6 strata of 19
N_COMMON_T3 = 77000               # matched-N for cross-corpus Heaps fits

# ---------------------------------------------------------------- pre-reg gate
with open(PREREG, "rb") as fh:
    actual_sha = hashlib.sha256(fh.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    raise SystemExit(f"PRE-REG TAMPERED: {actual_sha} != {EXPECTED_SHA}")
print(f"[ok] pre-reg SHA-256 verified: {actual_sha}")


# ---------------------------------------------------------------- QAC loading
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")


def load_qac():
    """Per-surah token sequences under tuple T1 (ROOT) and T2 (LEM), in (verse, word, segment) order."""
    seq_root = {s: [] for s in range(1, 115)}
    seq_lem = {s: [] for s in range(1, 115)}
    with open(MORPH, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = LOC_RE.match(parts[0])
            if not loc:
                continue
            s = int(loc.group(1))
            rm = ROOT_RE.search(parts[3])
            lm = LEM_RE.search(parts[3])
            if rm:
                seq_root[s].append(rm.group(1).strip())
            if lm:
                seq_lem[s].append(lm.group(1).strip())
    return seq_root, seq_lem


class Tuple_:
    """One rules-tuple: integer-coded per-surah token sequences plus the first-occurrence index."""

    def __init__(self, name, seq):
        self.name = name
        ids = {}
        for s in range(1, 115):
            for tok in seq[s]:
                if tok not in ids:
                    ids[tok] = len(ids)
        self.ntypes = len(ids)
        self.vocab = ids
        # firsts[s] = [(within-surah index of first occurrence, type id), ...] ascending by index
        self.firsts, self.length, self.stream = {}, {}, {}
        for s in range(1, 115):
            seen, lst = set(), []
            for i, tok in enumerate(seq[s]):
                if tok not in seen:
                    seen.add(tok)
                    lst.append((i, ids[tok]))
            self.firsts[s] = lst
            self.length[s] = len(seq[s])
            self.stream[s] = [ids[t] for t in seq[s]]
        self.ntokens = sum(self.length.values())
        self.offsets_cache = {}

    def first_positions(self, order):
        """Global 0-indexed positions of each type's first occurrence, ascending."""
        seen = bytearray(self.ntypes)
        pos, off = [], 0
        for s in order:
            for i, tid in self.firsts[s]:
                if not seen[tid]:
                    seen[tid] = 1
                    pos.append(off + i)
            off += self.length[s]
        return pos

    def first_positions_stream(self, toks):
        seen = bytearray(self.ntypes)
        pos = []
        for i, tid in enumerate(toks):
            if not seen[tid]:
                seen[tid] = 1
                pos.append(i)
        return pos

    def full_stream(self, order):
        out = []
        for s in order:
            out.extend(self.stream[s])
        return out


# ---------------------------------------------------------------- statistics
def geometric_grid(n_tot, m, n0):
    r = (n_tot / n0) ** (1.0 / (m - 1))
    pts, prev = [], 0
    for j in range(m):
        n = int(round(n0 * (r ** j)))
        n = min(n, n_tot)
        if n <= prev:            # keep the grid strictly increasing
            n = prev + 1
        pts.append(n)
        prev = n
    pts[-1] = n_tot
    return pts


def ols(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    beta = sxy / sxx
    logk = my - beta * mx
    resid = [y - (logk + beta * x) for x, y in zip(xs, ys)]
    sse = sum(r * r for r in resid)
    sst = sum((y - my) ** 2 for y in ys)
    r2 = 1.0 - sse / sst if sst > 0 else float("nan")
    return beta, logk, r2, resid


def stats_from_pos(pos, grid_pts_log, grid_pts, lin_boundaries):
    """All registered statistic variants for one ordering, from its first-occurrence positions."""
    out = {}
    for key, pts in grid_pts.items():
        ys = [math.log(bisect_left(pos, n)) for n in pts]
        xs = grid_pts_log[key]
        jerk = sum((ys[j + 1] - 2.0 * ys[j] + ys[j - 1]) ** 2 for j in range(1, len(ys) - 1))
        beta, logk, r2, resid = ols(xs, ys)
        area = sum(abs(r) for r in resid) / len(resid)
        out[f"J@{key}"] = jerk
        out[f"A@{key}"] = area
        out[f"beta@{key}"] = beta
        out[f"logK@{key}"] = logk
        out[f"R2@{key}"] = r2
    for b, bounds in lin_boundaries.items():
        vs = [bisect_left(pos, n) for n in bounds]
        out[f"Jlin@{b}"] = float(
            sum((vs[j + 1] - 2 * vs[j] + vs[j - 1]) ** 2 for j in range(1, len(vs) - 1))
        )
    return out


def make_grids(n_tot):
    pts, pts_log, lin = {}, {}, {}
    for m, n0 in GRIDS:
        key = f"M{m}_N{n0}"
        g = geometric_grid(n_tot, m, n0)
        pts[key] = g
        pts_log[key] = [math.log(n) for n in g]
    for b in BLOCKS_LIN:
        lin[b] = [((j + 1) * n_tot) // b for j in range(b)]
    return pts, pts_log, lin


# ---------------------------------------------------------------- null models
def strata_map(tup, size):
    """Length strata: surahs sorted by token count descending, cut into contiguous blocks."""
    order = sorted(range(1, 115), key=lambda s: (-tup.length[s], s))
    return {s: order.index(s) // size for s in order}


def length_stratified_draw(base, gmap, rng):
    """Permute surahs only among positions held by their own length stratum."""
    slots = {}
    for i, s in enumerate(base):
        slots.setdefault(gmap[s], []).append(i)
    out = list(base)
    for g, positions in slots.items():
        members = [base[i] for i in positions]
        rng.shuffle(members)
        for i, s in zip(positions, members):
            out[i] = s
    return out


def run_null(tup, kind, base, seed, nperm, grids, glog, lin, stratum_size=STRATUM_PRIMARY):
    """Return {stat_name: [nperm values]} for one null model."""
    rng = random.Random(seed)
    acc = None
    gmap = strata_map(tup, stratum_size) if kind in ("N2",) else None
    stream = tup.full_stream(list(range(1, 115))) if kind == "N3" else None
    for _ in range(nperm):
        if kind == "N1":
            order = list(range(1, 115))
            rng.shuffle(order)
            pos = tup.first_positions(order)
        elif kind == "N2":
            pos = tup.first_positions(length_stratified_draw(base, gmap, rng))
        elif kind == "N3":
            rng.shuffle(stream)
            pos = tup.first_positions_stream(stream)
        else:
            raise ValueError(kind)
        st = stats_from_pos(pos, glog, grids, lin)
        if acc is None:
            acc = {k: [] for k in st}
        for k, v in st.items():
            acc[k].append(v)
    return acc


def pval(obs, nullvals, direction):
    n = len(nullvals)
    if direction == "lower":
        hits = sum(1 for v in nullvals if v <= obs)
    else:
        hits = sum(1 for v in nullvals if v >= obs)
    return (1 + hits) / (1 + n)


def summarize(obs, nullvals, direction):
    n = len(nullvals)
    mu = sum(nullvals) / n
    var = sum((v - mu) ** 2 for v in nullvals) / (n - 1)
    sd = math.sqrt(var)
    return {
        "observed": obs,
        "null_mean": mu,
        "null_sd": sd,
        "null_min": min(nullvals),
        "null_max": max(nullvals),
        "z": (obs - mu) / sd if sd > 0 else float("nan"),
        "direction_locked": direction,
        "p": pval(obs, nullvals, direction),
        "passes_bonferroni": pval(obs, nullvals, direction) <= ALPHA,
        "direction_held": (obs < mu) if direction == "lower" else (obs > mu),
    }


# ---------------------------------------------------------------- T3 surface corpora
DIA = dict.fromkeys(
    list(range(0x0610, 0x061B))
    + list(range(0x064B, 0x0660))
    + [0x0670]
    + list(range(0x06D6, 0x06EE))
    + [0x0640],
    None,
)
TRANS = {0x0622: 0x0627, 0x0623: 0x0627, 0x0625: 0x0627, 0x0671: 0x0627, 0x0649: 0x064A}
ARAB_RE = re.compile(r"[ء-ي]+")


def norm_tokens(text):
    return ARAB_RE.findall(unicodedata.normalize("NFC", text).translate(DIA).translate(TRANS))


def heaps_fit_stream(tokens, n0=500, m=50, n_max=None):
    n_tot = len(tokens) if n_max is None else min(n_max, len(tokens))
    seen, pos = set(), []
    for i, t in enumerate(tokens[:n_tot]):
        if t not in seen:
            seen.add(t)
            pos.append(i)
    g = geometric_grid(n_tot, m, n0)
    xs = [math.log(n) for n in g]
    ys = [math.log(bisect_left(pos, n)) for n in g]
    beta, logk, r2, resid = ols(xs, ys)
    jerk = sum((ys[j + 1] - 2 * ys[j] + ys[j - 1]) ** 2 for j in range(1, len(ys) - 1))
    return {
        "n_tokens": n_tot,
        "n_types": len(seen),
        "beta": beta,
        "K": math.exp(logk),
        "R2": r2,
        "A": sum(abs(r) for r in resid) / len(resid),
        "J": jerk,
    }


# ---------------------------------------------------------------- main
def main():
    print("[load] QAC v0.4 …")
    seq_root, seq_lem = load_qac()
    tuples = {"T1_ROOT": Tuple_("T1_ROOT", seq_root), "T2_LEMMA": Tuple_("T2_LEMMA", seq_lem)}
    for name, t in tuples.items():
        print(f"  {name}: {t.ntokens} tokens, {t.ntypes} types")

    rows = list(csv.DictReader(open(REVCSV, encoding="utf-8")))
    mushaf = list(range(1, 115))
    revelation = [int(r["mushaf_order"]) for r in sorted(rows, key=lambda r: int(r["revelation_order"]))]
    noldeke = [int(r["mushaf_order"]) for r in sorted(rows, key=lambda r: int(r["noldeke_order"]))]
    orderings = {"mushaf": mushaf, "revelation": revelation, "noldeke": noldeke}
    assert sorted(revelation) == mushaf and sorted(noldeke) == mushaf

    results = {
        "finding_id": "H-NEW-2570",
        "prereg_sha256": actual_sha,
        "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION},
        "n_perm": NPERM,
        "bonferroni_k": BONF_K,
        "alpha_corrected": ALPHA,
        "grid_primary": f"M{GRID_PRIMARY[0]}_N{GRID_PRIMARY[1]}",
        "tuples": {},
        "observed": {},
        "cells": {},
        "sign_predictions": {},
        "robustness": {},
        "heaps_cross_corpus": {},
    }

    gk = f"M{GRID_PRIMARY[0]}_N{GRID_PRIMARY[1]}"

    for tname, tup in tuples.items():
        print(f"\n===== tuple {tname} =====")
        grids, glog, lin = make_grids(tup.ntokens)
        results["tuples"][tname] = {"n_tokens": tup.ntokens, "n_types": tup.ntypes}

        obs = {}
        for oname, order in orderings.items():
            obs[oname] = stats_from_pos(tup.first_positions(order), glog, grids, lin)
        results["observed"][tname] = obs
        for oname in orderings:
            print(
                f"  {oname:11s} J={obs[oname]['J@'+gk]:.6f}  A={obs[oname]['A@'+gk]:.6f}  "
                f"beta={obs[oname]['beta@'+gk]:.5f}  R2={obs[oname]['R2@'+gk]:.5f}"
            )

        nulls = {}
        for seed_label, seed in (("primary", SEED_PRIMARY), ("replication", SEED_REPLICATION)):
            for kind, base, label in (
                ("N1", mushaf, "N1_uniform"),
                ("N2", mushaf, "N2_lengthstrat_mushaf"),
                ("N2", revelation, "N2_lengthstrat_revelation"),
                ("N3", mushaf, "N3_scrambled"),
            ):
                key = (seed_label, label)
                print(f"  [null] {label} seed={seed_label} …", flush=True)
                nulls[key] = run_null(tup, kind, base, seed, NPERM, grids, glog, lin)

        # robustness nulls, primary seed only
        print("  [null] N2 loose strata (6x19), mushaf …", flush=True)
        nulls[("primary", "N2_loose_mushaf")] = run_null(
            tup, "N2", mushaf, SEED_PRIMARY, NPERM, grids, glog, lin, stratum_size=STRATUM_LOOSE
        )
        print("  [null] N2 length-strat, noldeke …", flush=True)
        nulls[("primary", "N2_lengthstrat_noldeke")] = run_null(
            tup, "N2", noldeke, SEED_PRIMARY, NPERM, grids, glog, lin
        )

        # ---- the 12 registered cells
        cells = {}
        spec = [
            (1, "J", "mushaf", "N2_lengthstrat_mushaf", "lower", "H1 PRIMARY (length-preserving)"),
            (2, "J", "mushaf", "N1_uniform", "lower", "H1 naive"),
            (3, "J", "revelation", "N1_uniform", "lower", "H2"),
            (4, "J", "revelation", "N2_lengthstrat_revelation", "lower", "H2 length-preserving"),
            (5, "J", "mushaf", "N3_scrambled", "higher", "MW-6 instrument control"),
            (6, "A", "mushaf", "N2_lengthstrat_mushaf", "lower", "H1"),
            (7, "A", "mushaf", "N1_uniform", "lower", "H1 naive"),
            (8, "A", "revelation", "N1_uniform", "lower", "H2"),
            (9, "A", "revelation", "N2_lengthstrat_revelation", "lower", "H2 length-preserving"),
            (10, "A", "mushaf", "N3_scrambled", "higher", "MW-6 instrument control"),
            (11, "beta", "mushaf", "N2_lengthstrat_mushaf", "higher", "H-DEFER length-preserving"),
            (12, "beta", "mushaf", "N1_uniform", "higher", "H-DEFER naive"),
        ]
        for cid, stat, oname, nullname, direction, note in spec:
            entry = {"statistic": stat, "ordering": oname, "null": nullname, "note": note}
            for seed_label in ("primary", "replication"):
                nv = nulls[(seed_label, nullname)][f"{stat}@{gk}"]
                entry[seed_label] = summarize(obs[oname][f"{stat}@{gk}"], nv, direction)
            cells[str(cid)] = entry
            p = entry["primary"]
            print(
                f"  cell {cid:2d} {stat:4s} {oname:11s} vs {nullname:26s} "
                f"obs={p['observed']:.6f} null={p['null_mean']:.6f} z={p['z']:+8.2f} "
                f"p={p['p']:.5f} {'PASS' if p['passes_bonferroni'] else 'fail'}"
            )
        results["cells"][tname] = cells

        # ---- locked sign predictions
        zj_m = cells["1"]["primary"]["z"]
        nv_rev = nulls[("primary", "N2_lengthstrat_revelation")][f"J@{gk}"]
        zj_r = summarize(obs["revelation"][f"J@{gk}"], nv_rev, "lower")["z"]
        signs = {
            "S1_J_mushaf_lt_revelation": {
                "mushaf": obs["mushaf"][f"J@{gk}"],
                "revelation": obs["revelation"][f"J@{gk}"],
                "held": obs["mushaf"][f"J@{gk}"] < obs["revelation"][f"J@{gk}"],
            },
            "S2_A_mushaf_lt_revelation": {
                "mushaf": obs["mushaf"][f"A@{gk}"],
                "revelation": obs["revelation"][f"A@{gk}"],
                "held": obs["mushaf"][f"A@{gk}"] < obs["revelation"][f"A@{gk}"],
            },
            "S3_beta_mushaf_gt_revelation": {
                "mushaf": obs["mushaf"][f"beta@{gk}"],
                "revelation": obs["revelation"][f"beta@{gk}"],
                "held": obs["mushaf"][f"beta@{gk}"] > obs["revelation"][f"beta@{gk}"],
            },
            "S4_zJ_mushaf_lt_zJ_revelation": {
                "z_mushaf_vs_own_lengthnull": zj_m,
                "z_revelation_vs_own_lengthnull": zj_r,
                "held": zj_m < zj_r,
            },
        }
        # Noldeke replication of the sign predictions
        nv_nold = nulls[("primary", "N2_lengthstrat_noldeke")][f"J@{gk}"]
        zj_n = summarize(obs["noldeke"][f"J@{gk}"], nv_nold, "lower")["z"]
        signs["noldeke_replication"] = {
            "S1_held": obs["mushaf"][f"J@{gk}"] < obs["noldeke"][f"J@{gk}"],
            "S2_held": obs["mushaf"][f"A@{gk}"] < obs["noldeke"][f"A@{gk}"],
            "S3_held": obs["mushaf"][f"beta@{gk}"] > obs["noldeke"][f"beta@{gk}"],
            "S4_held": zj_m < zj_n,
            "z_noldeke_vs_own_lengthnull": zj_n,
            "J_noldeke": obs["noldeke"][f"J@{gk}"],
            "A_noldeke": obs["noldeke"][f"A@{gk}"],
            "beta_noldeke": obs["noldeke"][f"beta@{gk}"],
        }
        results["sign_predictions"][tname] = signs
        for k, v in signs.items():
            if k != "noldeke_replication":
                print(f"  sign {k}: {'HELD' if v['held'] else 'VIOLATED'}")

        # ---- robustness sweep on the primary cell (cell 1) and the H2 sign S1/S4
        rob = {}
        for m, n0 in GRIDS:
            key = f"M{m}_N{n0}"
            for stat, direction in (("J", "lower"), ("A", "lower"), ("beta", "higher")):
                nv = nulls[("primary", "N2_lengthstrat_mushaf")][f"{stat}@{key}"]
                s = summarize(obs["mushaf"][f"{stat}@{key}"], nv, direction)
                rob[f"grid_{key}_{stat}_vs_N2"] = {
                    "p": s["p"], "z": s["z"], "direction_held": s["direction_held"],
                    "passes_bonferroni": s["passes_bonferroni"],
                }
            rob[f"grid_{key}_S1_held"] = obs["mushaf"][f"J@{key}"] < obs["revelation"][f"J@{key}"]
            rob[f"grid_{key}_S3_held"] = obs["mushaf"][f"beta@{key}"] > obs["revelation"][f"beta@{key}"]
        for b in BLOCKS_LIN:
            nv2 = nulls[("primary", "N2_lengthstrat_mushaf")][f"Jlin@{b}"]
            nv1 = nulls[("primary", "N1_uniform")][f"Jlin@{b}"]
            s2 = summarize(obs["mushaf"][f"Jlin@{b}"], nv2, "lower")
            s1 = summarize(obs["mushaf"][f"Jlin@{b}"], nv1, "lower")
            rob[f"Jlin_B{b}_vs_N2"] = {"p": s2["p"], "z": s2["z"], "direction_held": s2["direction_held"]}
            rob[f"Jlin_B{b}_vs_N1"] = {"p": s1["p"], "z": s1["z"], "direction_held": s1["direction_held"]}
            rob[f"Jlin_B{b}_S1_held"] = obs["mushaf"][f"Jlin@{b}"] < obs["revelation"][f"Jlin@{b}"]
        for stat, direction in (("J", "lower"), ("A", "lower"), ("beta", "higher")):
            nvl = nulls[("primary", "N2_loose_mushaf")][f"{stat}@{gk}"]
            s = summarize(obs["mushaf"][f"{stat}@{gk}"], nvl, direction)
            rob[f"loose_strata_{stat}_vs_N2"] = {
                "p": s["p"], "z": s["z"], "direction_held": s["direction_held"],
                "passes_bonferroni": s["passes_bonferroni"],
            }
        results["robustness"][tname] = rob

    # ---------------------------------------------------------- cross-corpus Heaps (descriptive)
    print("\n===== cross-corpus Heaps exponents (descriptive, MW-7 capped) =====")
    quran = json.load(open(QURAN_NT, encoding="utf-8"))
    q_surface = []
    for s in quran:
        for v in s["verses"]:
            q_surface.extend(norm_tokens(v["text"]))
    poetry_files = sorted(
        f for f in glob.glob(os.path.join(BASE_RAW, "muallaqa-*.txt")) + glob.glob(os.path.join(BASE_RAW, "diwan-*.txt"))
        if ".raw." not in f and ".openiti." not in f
    )
    poetry = []
    for f in poetry_files:
        poetry.extend(norm_tokens(open(f, encoding="utf-8").read()))
    bukhari = norm_tokens(open(os.path.join(BASE_RAW, "bukhari-noquran.txt"), encoding="utf-8").read())

    hc = {"poetry_files": [os.path.basename(f) for f in poetry_files], "matched_N": N_COMMON_T3}
    for label, toks in (("quran_T3_surface", q_surface), ("preislamic_poetry_T3_surface", poetry),
                        ("bukhari_noquran_T3_surface", bukhari)):
        hc[label + "_matchedN"] = heaps_fit_stream(toks, n_max=N_COMMON_T3)
        hc[label + "_full"] = heaps_fit_stream(toks)
        m = hc[label + "_matchedN"]
        print(f"  {label:32s} matched-N beta={m['beta']:.4f} K={m['K']:.3f} R2={m['R2']:.5f} "
              f"types={m['n_types']}")
    for tname, tup in tuples.items():
        toks = tup.full_stream(mushaf)
        hc[f"quran_{tname}_mushaf_full"] = heaps_fit_stream(toks)
        f = hc[f"quran_{tname}_mushaf_full"]
        print(f"  quran_{tname:10s} (QAC, full)      beta={f['beta']:.4f} K={f['K']:.3f} "
              f"R2={f['R2']:.5f} types={f['n_types']}")
        rev_toks = tup.full_stream(revelation)
        hc[f"quran_{tname}_revelation_full"] = heaps_fit_stream(rev_toks)
    results["heaps_cross_corpus"] = hc

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(results, fh, ensure_ascii=False, indent=1)
    print(f"\n[written] {OUT_JSON}")


if __name__ == "__main__":
    main()
