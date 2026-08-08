#!/usr/bin/env python3
"""
H-NEW-2910 — the vocalised-prose control extended from two books to all nine.

H-NEW-2890 returned CONTROL PASSES on a margin of 0.00010 under one reading of its own
locked threshold, from an estimate resting on two books. This runs the identical pipeline
on all nine and replaces the point estimate with a distribution.

The instrument is H-NEW-2890's, loaded unmodified and SHA-pinned; it in turn pins
H-NEW-2880's, which pins H-NEW-2870's. No parameter of the instrument, the null or the
statistic is changed.

Pre-registration locked at
  findings/phase-b-hypotheses/prereg-h-new-2910-nine-book-prose.md
  SHA-256 86aa22f76203001f03442976a729797a96b3dc74d89433efd3af98f2777833a8
verified at runtime.

Two execution changes, both declared in prereg §4 and neither statistical:
  - the 108 exact-null arms run in parallel processes; each builds its own
    random.Random(seed) and is self-contained, so output is bit-identical to serial.
  - CHECKPOINTS ARE WRITTEN PER ARM, not per stage -- the defect found in H-NEW-2890's
    own runner, where a 22-minute stage wrote nothing and looked like a hang.

Waiel Al-Shujaa, 2026-08-07.
"""
import hashlib
import io
import json
import math
import os
import platform
import random
import sys
import contextlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
import multiprocessing

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)

PREREG = "findings/phase-b-hypotheses/prereg-h-new-2910-nine-book-prose.md"
PREREG_SHA256 = "86aa22f76203001f03442976a729797a96b3dc74d89433efd3af98f2777833a8"
PARENT = "findings/phase-b-hypotheses/scripts/h-new-2890.py"
FROZEN = {
    PARENT: "ac6f83465aa32b7a761f622f0010ed414329eb654bc60cb0bbed516e90edea73",
    "findings/phase-b-hypotheses/scripts/h-new-2880.py":
        "c9577870b2a4bc3451344031f46f192795534af0ef56f4f46be57f07db7c7074",
}

BOOKS = ["bukhari", "muslim", "abudawud", "tirmidhi", "nasai", "ibnmajah",
         "malik", "ahmed", "darimi"]
SETTINGS = ["S5", "S3", "S0"]
TUPLES = ["P1", "P2"]
SEED, SEED_REP = 20260509, 20260519
N_PERM = 10000
N_PROSE_CUT = 200
BONFERRONI_K = 108
ALPHA = 0.05 / BONFERRONI_K
ALPHA_2890 = 0.05 / 36                 # for comparability of D-P3 arm counts

# prereg §3
VOC_MIN = 0.90
MIN_READABLE_PAIRS = 500
# prereg §5 — H-NEW-2890's own published threshold and its near-threshold cell
T_QUARTER = 0.25 * 0.18686703691604045
BUKHARI_S0_P2_PUBLISHED = 0.04681562547499621
QURAN_DELTA_P1 = 0.18686703691604045
QURAN_DELTA_P2 = 0.1880104540999673
QURAN_RECUT_DELTA_P1 = 0.0284

NPROC = min(8, max(1, (os.cpu_count() or 4) - 2))

SMOKE = "--smoke" in sys.argv
if SMOKE:
    N_PERM, N_PROSE_CUT = 200, 5

CHECKPOINT_DIR = os.path.join("scratch", "h-new-2910-checkpoints")   # OUTSIDE the run dir
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def die(m):
    say(f"[FATAL] {m}")
    raise SystemExit(1)


def checkpoint(tag, obj):
    """prereg §4/§9 — PER ARM, outside the run directory, write-once."""
    if SMOKE:
        return
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    p = os.path.join(CHECKPOINT_DIR, f"arm-{tag}.json")
    if os.path.exists(p):
        return
    with open(p, "x", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, default=float)


# ---------------------------------------------------------------- 0. gates
_a = sha256_file(PREREG)
if _a != PREREG_SHA256:
    die(f"pre-reg SHA mismatch\n  expected {PREREG_SHA256}\n  actual   {_a}")
say(f"[SHA-OK] pre-reg locked: {_a}")
for p, want in FROZEN.items():
    g = sha256_file(p)
    if g != want:
        die(f"frozen input mismatch {p}\n  expected {want}\n  actual {g}")
say(f"[SHA-OK] {len(FROZEN)} frozen inputs verified (the parent runners)")

# ---------------------------------------------------------------- 1. instrument
say("\n" + "=" * 78)
say("INSTRUMENT — H-NEW-2890's machinery, loaded unmodified (prereg §4).")
say("=" * 78)
# H-NEW-2890 interleaves function definitions with execution, so the machinery is loaded
# as four DEFINITION-ONLY slices: its setup and census, then the three blocks of defs. None
# of its RESULT sections is re-executed. Slice boundaries are literal anchors in a file
# whose SHA-256 is pinned above.
_src = open(PARENT, encoding="utf-8").read()
_A = _src.index("# ---------------------------------------------------------------- 3. prose analysis")
_B = _src.index('say("\\n" + "=" * 78)\nsay("RESULT 2 — CLASS-COLLAPSE MAGNITUDE FOR PROSE')
_C = _src.index("def label_exchange(")
_D = _src.index("TESTS = {}")
_E = _src.index("class ProseTuple:")
_F = _src.index("# ---------------------------------------------------------------- 5. verdict")
_F2 = _src.rindex("for book in PRIMARY_TEXTS:", _E, _F)   # stop before its D-P3 loop
SLICES = [_src[:_A], _src[_A:_B], _src[_C:_D], _src[_E:_F2]]
NS = {"__name__": "instrument-2890", "__file__": PARENT}
_argv = sys.argv
sys.argv = [_argv[0], "--smoke"]
_buf = io.StringIO()
try:
    with contextlib.redirect_stdout(_buf):
        for _i, _sl in enumerate(SLICES):
            exec(compile(_sl, f"h-new-2890-slice{_i}", "exec"), NS)
finally:
    sys.argv = _argv
say("   (parent SHA gates and Gates A/B ran and passed; its output is in the run log)")
_G = NS["NS"]                                  # the H-NEW-2880 namespace
if not _G["GATE_A"]["pass"] or _G["GATE_B"]["n_pass"] != 6:
    die("inherited gate failed")

BOOKS_DATA = NS["BOOKS"]
INNER = NS["INNER"]
apply_convention, phonemes, PUNCT = NS["apply_convention"], NS["phonemes"], NS["PUNCT"]
set_variant = NS["set_variant"]
strip_mask, prose_arm_B, prose_arm_A = NS["strip_mask"], NS["prose_arm_B"], NS["prose_arm_A"]
ProseTuple, prose_exact_null = NS["ProseTuple"], NS["prose_exact_null"]
label_exchange, QGAIN = NS["label_exchange"], NS["QGAIN"]
CONVS = NS["CONVS"]
if abs(NS["QDELTA"]["R2"]["P1"] - QURAN_DELTA_P1) > 1e-9:
    die("the recomputed corpus delta differs from the value locked in prereg §2")
say(f"   [OK] corpus Δ(P1) recomputed = {NS['QDELTA']['R2']['P1']:.6f}, matches the lock")
say(f"   parallelism: {NPROC} worker processes over {len(BOOKS)*len(SETTINGS)*len(TUPLES)*2} "
    f"exact-null arms (bit-identical to serial; prereg §4)")

# ---------------------------------------------------------------- 2. census / inclusion
say("\n" + "=" * 78)
say("RESULT 1 — THE NINE-BOOK CENSUS AND THE INCLUSION GATE (prereg §3)")
say("=" * 78)
say(f"   gate: unit-final vocalisation >= {VOC_MIN}, readable pairs >= {MIN_READABLE_PAIRS}, "
    f"pausal partition a coarsening of the citation partition")
CENSUS, ADMIT = {}, []
say(f"   {'book':10s} {'units':>6s} {'chap':>5s} {'har/ch':>7s} {'unitfinal':>10s} "
    f"{'pairs':>6s} {'readable':>8s} {'coarsen':>8s} {'admit'}")
LABCACHE = {}
for b in BOOKS:
    bd = BOOKS_DATA[b]
    r, lab, pairs, keepr = prose_arm_B(b, "S5", "R2")
    LABCACHE[(b, "S5")] = (r, lab, pairs, keepr)
    coars = True
    for conv in TUPLES:
        m = defaultdict(set)
        for a, p in zip(lab["C"], lab[conv]):
            m[a].add(p)
        if any(len(v) > 1 for v in m.values()):
            coars = False
    rfull, _, pfull, kfull = prose_arm_B(b, "S0", "R2")
    ok = (bd["unit_final_vocalised"] >= VOC_MIN and len(kfull) >= MIN_READABLE_PAIRS and coars)
    CENSUS[b] = {"units": bd["n"], "chapters": bd["n_chapters"], "density": bd["density"],
                 "unit_final_vocalised": bd["unit_final_vocalised"],
                 "pairs": len(pfull), "readable_pairs": len(kfull),
                 "coarsening": coars, "admitted": bool(ok),
                 "mean_unit_len": bd["mean_len"],
                 "contam3": bd["contam3"], "contam5": bd["contam5"]}
    if ok:
        ADMIT.append(b)
    say(f"   {b:10s} {bd['n']:6d} {bd['n_chapters']:5d} {bd['density']:7.4f} "
        f"{bd['unit_final_vocalised']:10.4f} {len(pfull):6d} {len(kfull):8d} "
        f"{str(coars):>8s} {'PASS' if ok else 'FAIL'}")
say(f"   admitted: {len(ADMIT)}/9 — {', '.join(ADMIT)}")
if not ADMIT:
    die("no admissible book (prereg §7)")
checkpoint("000-census", CENSUS)

# ---------------------------------------------------------------- 3. Arm B deltas
say("\n" + "=" * 78)
say("RESULT 2 — ARM B: THE Δ DISTRIBUTION ACROSS BOOKS (prereg §4). PRIMARY.")
say("=" * 78)
ARMB = {}
for b in ADMIT:
    for s in SETTINGS:
        if (b, s) not in LABCACHE:
            LABCACHE[(b, s)] = prose_arm_B(b, s, "R2")
        r = LABCACHE[(b, s)][0]
        ARMB[f"{b}_{s}"] = r
say(f"   {'book':10s} {'set':>4s} {'n_read':>7s} {'A(C)':>7s} {'A(P1)':>7s} "
    f"{'Δ(P1)':>9s} {'Δ(P2)':>9s} {'K(C)->K(P1)':>13s}")
for b in ADMIT:
    for s in SETTINGS:
        r = ARMB[f"{b}_{s}"]
        say(f"   {b:10s} {s:>4s} {r['n_pairs_readable']:7d} {r['A_readable']['C']:7.4f} "
            f"{r['A_readable']['P1']:7.4f} {r['delta_readable']['P1']:+9.5f} "
            f"{r['delta_readable']['P2']:+9.5f} {r['K']['C']:6d}->{r['K']['P1']:<6d}")
checkpoint("001-armB", {k: {kk: vv for kk, vv in v.items()} for k, v in ARMB.items()})

D_P1 = [ARMB[f"{b}_{s}"]["delta_readable"]["P1"] for b in ADMIT for s in SETTINGS]
D_P2 = [ARMB[f"{b}_{s}"]["delta_readable"]["P2"] for b in ADMIT for s in SETTINGS]
CELLS = D_P1 + D_P2


def desc(x):
    a = np.asarray(x)
    return {"n": int(a.size), "mean": float(a.mean()), "sd": float(a.std(ddof=1)),
            "min": float(a.min()), "q25": float(np.percentile(a, 25)),
            "median": float(np.median(a)), "q75": float(np.percentile(a, 75)),
            "q90": float(np.percentile(a, 90)), "max": float(a.max())}


DIST = {"P1": desc(D_P1), "P2": desc(D_P2), "both_tuples": desc(CELLS)}
say("\n   DISTRIBUTION of Δ (Arm B, readable, R2), over admitted books x 3 settings:")
for k in ("P1", "P2", "both_tuples"):
    d = DIST[k]
    say(f"      {k:12s} n={d['n']:3d}  mean={d['mean']:+.5f}  sd={d['sd']:.5f}  "
        f"min={d['min']:+.5f}  median={d['median']:+.5f}  q90={d['q90']:+.5f}  "
        f"max={d['max']:+.5f}")
say(f"   this corpus: Δ(P1)={QURAN_DELTA_P1:+.5f}  Δ(P2)={QURAN_DELTA_P2:+.5f}")
_sd = DIST["both_tuples"]["sd"]
say(f"   this corpus sits {(QURAN_DELTA_P1 - DIST['both_tuples']['mean']) / _sd:+.1f} sd above "
    f"the prose cell mean, and {QURAN_DELTA_P1 / DIST['both_tuples']['max']:.1f}x its maximum")

# ---- the §5 margin question
n_ge = sum(1 for x in CELLS if x >= T_QUARTER)
f_ge = n_ge / len(CELLS)
pct_bukhari = float((np.asarray(CELLS) < BUKHARI_S0_P2_PUBLISHED).mean() * 100)
say(f"\n   === THE MARGIN QUESTION (prereg §5) ===")
say(f"   threshold T = {T_QUARTER:+.5f} (H-NEW-2890's quarter threshold)")
say(f"   cells at or above T: {n_ge}/{len(CELLS)}  ->  f = {f_ge:.4f}")
say(f"   al-Bukhārī S0 P2 (+{BUKHARI_S0_P2_PUBLISHED:.5f}) sits at the "
    f"{pct_bukhari:.1f}th percentile of the {len(CELLS)}-cell distribution")
checkpoint("002-distribution", {"dist": DIST, "n_ge_T": n_ge, "f": f_ge,
                                "bukhari_s0_p2_percentile": pct_bukhari,
                                "T": T_QUARTER, "cells": CELLS})

# ---------------------------------------------------------------- 4. Arm A
say("\n" + "=" * 78)
say(f"RESULT 3 — ARM A: length-matched cuts, vs this corpus's own re-cut Δ = "
    f"{QURAN_RECUT_DELTA_P1:+.4f}")
say("=" * 78)
ARMA = {}
for b in ADMIT:
    for s in SETTINGS:
        a = prose_arm_A(b, s, "R2", SEED, N_PROSE_CUT)
        ARMA[f"{b}_{s}"] = a
        say(f"   {b:10s} {s:>3s}  Δ(P1) mean={a['P1']['mean']:+.5f} sd={a['P1']['sd']:.5f} "
            f"max={a['P1']['max']:+.5f}   Δ(P2) mean={a['P2']['mean']:+.5f}")
    checkpoint(f"003-armA-{b}", {k: v for k, v in ARMA.items() if k.startswith(b)})

# ---------------------------------------------------------------- 5. the 108 arms
say("\n" + "=" * 78)
say("RESULT 4 — THE REGISTERED TESTS (prereg §6)")
say("=" * 78)


def _dp1(args):
    b, s, p = args
    r, lab, pairs, keepr = LABCACHE[(b, s)]
    pg = np.array([(lab[p][i] == lab[p][i + 1]) - (lab["C"][i] == lab["C"][i + 1])
                   for i in keepr], dtype=np.float64)
    o, pv = label_exchange(QGAIN[p], pg, SEED, N_PERM)
    _, pv2 = label_exchange(QGAIN[p], pg, SEED_REP, N_PERM)
    return (b, s, p, {"obs_diff": o, "p": pv, "p_replication": pv2,
                      "delta_prose": float(pg.mean()),
                      "delta_quran": float(QGAIN[p].mean()),
                      "pass": pv < ALPHA})


def _dp3(args):
    b, s, p = args
    r, lab, pairs, keepr = LABCACHE[(b, s)]
    T = ProseTuple(lab, keepr, p)
    if not T.coarsening:
        return (b, s, p, {"undefined": True})
    res = prose_exact_null(T, SEED, N_PERM)
    res2 = prose_exact_null(T, SEED_REP, N_PERM)
    res["p_replication"] = res2["p_E"]
    res["z_replication"] = res2["z_E"]
    res["pass"] = res["p_E"] < ALPHA
    res["pass_at_2890_alpha"] = res["p_E"] < ALPHA_2890
    return (b, s, p, res)


JOBS = [(b, s, p) for b in ADMIT for s in SETTINGS for p in TUPLES]
say(f"   D-P1 — {len(JOBS)} arms, label exchange, 10,000 perms x 2 seeds")
DP1 = {}
for b, s, p, v in map(_dp1, JOBS):
    DP1[f"{b}_{s}_{p}"] = v
    checkpoint(f"004-dp1-{b}-{s}-{p}", v)
nfail = sum(1 for v in DP1.values() if not v["pass"])
say(f"   D-P1: {len(DP1) - nfail}/{len(DP1)} arms PASS at alpha={ALPHA:.8f}"
    + ("" if nfail == 0 else f"   FAILING: "
       + ", ".join(k for k, v in DP1.items() if not v["pass"])))

say(f"\n   D-P3 — {len(JOBS)} arms against each book's OWN exact null, "
    f"{NPROC} processes, per-arm checkpoints")
DP3 = {}
with multiprocessing.get_context("fork").Pool(NPROC) as pool:
    for i, (b, s, p, v) in enumerate(pool.imap_unordered(_dp3, JOBS), 1):
        DP3[f"{b}_{s}_{p}"] = v
        checkpoint(f"005-dp3-{b}-{s}-{p}", v)
        if v.get("undefined"):
            say(f"      [{i:3d}/{len(JOBS)}] {b:10s} {s} {p}: exact null UNDEFINED "
                f"(not a coarsening)")
        else:
            say(f"      [{i:3d}/{len(JOBS)}] {b:10s} {s} {p}: E={v['observed_E']:.4f} "
                f"z={v['z_E']:+.2f} p={v['p_E']:.5f} (rep {v['p_replication']:.5f}) "
                f"floordev={v['null_floor_max_abs_dev']:.0e} "
                f"{'CLEARS' if v['pass'] else '-'}")

# G1 exactness across every prose null
bad = [k for k, v in DP3.items() if not v.get("undefined")
       and (v["null_floor_max_abs_dev"] != 0.0
            or v["redraws"] / max(N_PERM + v["redraws"], 1) >= 0.01)]
say(f"\n   G1 exactness across all {len(DP3)} prose nulls: "
    f"{'PASS' if not bad else 'FAIL — ' + ', '.join(bad)}")
if bad:
    die("prose exact null lost floor exactness (prereg §7)")

# D-P3 pattern across books
BOOKFAIL = {b: sum(1 for s in SETTINGS for p in TUPLES
                   if DP3[f"{b}_{s}_{p}"].get("pass")) for b in ADMIT}
BOOKFAIL_2890 = {b: sum(1 for s in SETTINGS for p in TUPLES
                        if DP3[f"{b}_{s}_{p}"].get("pass_at_2890_alpha")) for b in ADMIT}
n_books_any = sum(1 for b in ADMIT if BOOKFAIL[b] > 0)
say(f"\n   D-P3 arms clearing alpha, per book (of 6 each):")
for b in ADMIT:
    say(f"      {b:10s} {BOOKFAIL[b]}/6 at alpha={ALPHA:.6f}   "
        f"{BOOKFAIL_2890[b]}/6 at H-NEW-2890's alpha={ALPHA_2890:.6f}")
say(f"   books with >=1 clearing arm: {n_books_any}/{len(ADMIT)} "
    f"({100 * n_books_any / len(ADMIT):.0f}%)  -> "
    f"{'GENERAL to the genre' if n_books_any > len(ADMIT) / 2 else 'BOOK-SPECIFIC'} "
    f"(prereg §6 threshold: >50%)")

# ---------------------------------------------------------------- 6. verdict
say("\n" + "=" * 78)
say("VERDICT — logic diffed against prereg §5/§6, printed before declaration.")
say("=" * 78)
say("   prereg §5, verbatim:")
say("     f < 0.10                      -> 2890 ROBUST")
say("     0.10 <= f < 0.25              -> BORDERLINE, strengthen 2890 §7.1")
say("     f >= 0.25                     -> 2890 RE-VERDICTED TO PARTIAL")
say("     Bukhari S0 P2 >= 90th pctile  -> outlier, consistent with ROBUST")
say("     Bukhari S0 P2 <= 75th pctile  -> typical; at least BORDERLINE regardless of f")
say("     both triggers evaluated; the STRICTER outcome is taken")
say(f"\n   f = {f_ge:.4f} ({n_ge}/{len(CELLS)} cells >= T)")
say(f"   al-Bukhārī S0 P2 percentile = {pct_bukhari:.1f}")

v_f = "ROBUST" if f_ge < 0.10 else ("BORDERLINE" if f_ge < 0.25 else "PARTIAL")
if pct_bukhari >= 90:
    v_p = "ROBUST"
elif pct_bukhari <= 75:
    v_p = "BORDERLINE"
else:
    v_p = "ROBUST"
rank = {"ROBUST": 0, "BORDERLINE": 1, "PARTIAL": 2}
VERDICT = v_f if rank[v_f] >= rank[v_p] else v_p
say(f"   trigger 1 (f): {v_f}    trigger 2 (percentile): {v_p}    stricter: {VERDICT}")
FINAL = {"ROBUST": "H-NEW-2890 ROBUST — its verdict stands as published",
         "BORDERLINE": "BORDERLINE — H-NEW-2890 stands, its §7.1 disclosure must be strengthened",
         "PARTIAL": "H-NEW-2890 RE-VERDICTED TO PARTIAL"}[VERDICT]
say(f"\n   VERDICT: {FINAL}")

# ---------------------------------------------------------------- 7. write
if SMOKE:
    say("\n[SMOKE] no run directory written. Exiting.")
    raise SystemExit(0)
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-2910", STAMP)
os.makedirs(RUNDIR, exist_ok=False)
out = {
    "id": "H-NEW-2910", "run_utc": STAMP, "prereg": PREREG,
    "prereg_sha256": PREREG_SHA256, "parent": "H-NEW-2890", "frozen_inputs": FROZEN,
    "seed": SEED, "seed_replication": SEED_REP, "n_perm": N_PERM,
    "n_prose_cut": N_PROSE_CUT, "bonferroni_k": BONFERRONI_K, "alpha": ALPHA,
    "alpha_2890": ALPHA_2890, "n_workers": NPROC,
    "python": sys.version.split()[0], "platform": platform.platform(),
    "census": CENSUS, "admitted": ADMIT,
    "arm_B": ARMB, "arm_A": ARMA, "distribution": DIST,
    "margin": {"T": T_QUARTER, "n_ge_T": n_ge, "n_cells": len(CELLS), "f": f_ge,
               "bukhari_s0_p2": BUKHARI_S0_P2_PUBLISHED,
               "bukhari_s0_p2_percentile": pct_bukhari,
               "trigger_f": v_f, "trigger_percentile": v_p},
    "quran": {"delta_P1": QURAN_DELTA_P1, "delta_P2": QURAN_DELTA_P2,
              "recut_delta_P1": QURAN_RECUT_DELTA_P1},
    "tests_DP1": DP1, "tests_DP3": DP3,
    "dp3_per_book": BOOKFAIL, "dp3_per_book_at_2890_alpha": BOOKFAIL_2890,
    "dp3_books_with_any_clearing": n_books_any,
    "dp3_pattern": "GENERAL" if n_books_any > len(ADMIT) / 2 else "BOOK-SPECIFIC",
    "verdict_code": VERDICT, "verdict": FINAL,
}
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as f:
    f.write(f"H-NEW-2910 run {STAMP}\nprereg {PREREG} {PREREG_SHA256}\n"
            f"script findings/phase-b-hypotheses/scripts/h-new-2910.py "
            f"{sha256_file('findings/phase-b-hypotheses/scripts/h-new-2910.py')}\n")
    for p, s in FROZEN.items():
        f.write(f"input {p} {s}\n")
    f.write("source-manifest data/literature/hadith/VOCALISED-HADITH-SOURCE.md\n")
    for b in BOOKS:
        f.write(f"input data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{b}.json\n")
    f.write(f"output {RUNDIR}/result.json\noutput {RUNDIR}/console.log\n")
    f.write(f"checkpoints {CHECKPOINT_DIR}/  (OUTSIDE the run directory, PER ARM, write-once)\n")
os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2910.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
print(f"\n[WROTE] {RUNDIR}/result.json")
print(f"[WROTE] findings/phase-b-hypotheses/csv/h-new-2910.json")
