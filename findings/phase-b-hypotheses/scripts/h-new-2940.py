#!/usr/bin/env python3
"""
H-NEW-2940 — the inverse re-cut.

H-NEW-2930 corrected the pausal cross-corpus headline from 5.3x to 3.63x by EXTRAPOLATING a
nine-point linear fit 0.86 prose-ranges below the shortest book in its baseline. This runner
replaces that extrapolation with a measurement requiring no baseline text: merge this corpus's
own adjacent verses into longer units matching prose unit lengths, and measure how far the
delta moves toward the prose value. At ~65 words the comparison sits INSIDE the 49-91 word
prose range, so nothing is extrapolated.

Pre-registration locked at
  findings/phase-b-hypotheses/prereg-h-new-2940-inverse-recut.md
  SHA-256 27a2d9cdf54fa2c9d73450fc831823abbaed21641204f6b52b2de2e432d51257
verified at runtime below. Frozen inputs SHA-256 verified, the parent runner among them:
sections 0-6 of h-new-2870.py are executed VERBATIM as the instrument, so the rime extractors
and pausal tuples cannot drift from the published delta.

There is no p-value in this test and none is invented. It is a magnitude comparison; the
decision rule of prereg section 8 is on the fraction of the gap closed.

Waiel Al-Shujaa, 2026-08-08.
"""
import hashlib
import json
import math
import os
import platform
import random
import sys
from datetime import datetime, timezone

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)

PREREG = "findings/phase-b-hypotheses/prereg-h-new-2940-inverse-recut.md"
PREREG_SHA256 = "27a2d9cdf54fa2c9d73450fc831823abbaed21641204f6b52b2de2e432d51257"
PARENT = "findings/phase-b-hypotheses/scripts/h-new-2870.py"
NINEBOOK = "findings/phase-b-hypotheses/csv/h-new-2910.json"

FROZEN = {
    PARENT:
        "9765a448256a93dc740ceb1dcd56ffbb58f33aa8a6192f855ad3579af07d2dde",
    "findings/phase-b-hypotheses/scripts/h-new-2880.py":
        "c9577870b2a4bc3451344031f46f192795534af0ef56f4f46be57f07db7c7074",
    "findings/phase-b-hypotheses/scripts/h-new-2890.py":
        "ac6f83465aa32b7a761f622f0010ed414329eb654bc60cb0bbed516e90edea73",
    NINEBOOK:
        "b5f005fa8fd1550e84bf10f34f6c987a846f36d43fa266559303753a76da4fd1",
    "quran-text/quran-full-tashkeel.json":
        "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    "data/alt-text/quran-uthmani-txt.txt":
        "e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8",
    "data/baseline-corpora/raw/muallaqa-imru-al-qais.txt":
        "06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14",
    "data/baseline-corpora/raw/muallaqa-zuhayr.txt":
        "9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2",
    "data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt":
        "d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720",
    "data/baseline-corpora/raw/bukhari-noquran.txt":
        "0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100",
    "data/baseline-corpora/raw/jahiz-hayawan.txt":
        "419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd",
}

# prereg §3 — the published native delta this run must reproduce before anything else.
DELTA_PUBLISHED = 0.18686703691604045
REPRO_TOL = 1e-12

# prereg §7 — the "~0.030" the decision rule was written against.
PROSE_TARGET_2930 = 0.0304878

# prereg §6
TARGET_PRIMARY = 65
TARGETS_SECONDARY = (50, 75, 91)

# prereg §7 fit gate — H-NEW-2930's own published coefficients.
FIT_SLOPE_2930 = -0.000398
FIT_INTERCEPT_2930 = 0.05679

# prereg §9
SEED = 20260509
SEED_REP = 20260519
N_RANDSEG = 200

# H-NEW-2930's printed nine-book table, re-keyed here ONLY so that the reconstruction of it
# from the frozen H-NEW-2910 result can be gated against it (prereg §7).
TABLE_2930 = {
    "darimi": (49.2, 0.02835), "ibnmajah": (58.5, 0.04134), "nasai": (59.0, 0.03257),
    "malik": (63.0, 0.03768), "abudawud": (63.1, 0.02761), "muslim": (64.6, 0.03249),
    "bukhari": (73.2, 0.03180), "ahmed": (73.6, 0.02632), "tirmidhi": (91.1, 0.01623),
}

SMOKE = "--smoke" in sys.argv
CHECKPOINT_DIR = os.path.join("scratch", "h-new-2940-checkpoints")   # OUTSIDE the run dir
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


_ck = [0]


def checkpoint(tag, obj):
    """prereg §10 — per arm, OUTSIDE the run directory, write-once."""
    if SMOKE:
        return
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    _ck[0] += 1
    p = os.path.join(CHECKPOINT_DIR, f"snapshot-{_ck[0]:03d}-{tag}.json")
    if os.path.exists(p):
        return
    with open(p, "x", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, default=float)


# ---------------------------------------------------------------- 0. SHA gates
_a = sha256_file(PREREG)
if _a != PREREG_SHA256:
    die(f"pre-reg SHA mismatch\n  expected {PREREG_SHA256}\n  actual   {_a}")
say(f"[SHA-OK] pre-reg locked: {_a}")
for p, want in FROZEN.items():
    g = sha256_file(p)
    if g != want:
        die(f"frozen input mismatch {p}\n  expected {want}\n  actual {g}")
say(f"[SHA-OK] {len(FROZEN)} frozen inputs verified (the parent runner among them)")

# ---------------------------------------------------------------- 1. the instrument
say("\n" + "=" * 78)
say("INSTRUMENT — sections 0-6 of the pinned parent runner, executed verbatim.")
say("Its GATE A (orthography) and GATE B (instrument validation) are re-run below.")
say("=" * 78)
_src = open(PARENT, encoding="utf-8").read()
_cut = _src.index("# ---------------------------------------------------------------- 7. the analysis")
NS = {"__name__": "instrument", "__file__": PARENT}
_captured = []


class _Tee:
    def __init__(self, real):
        self.real = real

    def write(self, s):
        self.real.write(s)
        _captured.append(s)

    def flush(self):
        self.real.flush()


_old = sys.stdout
sys.stdout = _Tee(_old)
try:
    exec(compile(_src[:_cut], "h-new-2870-instrument", "exec"), NS)
finally:
    sys.stdout = _old
LOG.extend("".join(_captured).rstrip("\n").split("\n"))

SURAHS, N_VERSES = NS["SURAHS"], NS["N_VERSES"]
GATE_A = {"checks": NS["gate_a"], "pass": NS["gate_a_pass"]}
GATE_B = {"checks": NS["gate_b"], "n_pass": NS["gate_b_pass"]}
if not GATE_A["pass"] or GATE_B["n_pass"] != 6:
    die("parent gate failed — instrument broken (prereg §2)")

exec("RIME_VARIANT = 'R2'", NS)          # prereg §2 — R2 is primary
rime_of = NS["rime_of"]


def arabic_words(t):
    """prereg §4 — verbatim from h-new-2890.py, the tokeniser the nine prose books'
    unit lengths were measured with."""
    return [w for w in t.split() if any("ء" <= c <= "ي" for c in w)]


VERSES = [vs for _, _, _, vs in SURAHS]
WLEN = [[len(arabic_words(t)) for t in vs] for vs in VERSES]
TOTAL_WORDS = sum(sum(x) for x in WLEN)
NATIVE_LEN = TOTAL_WORDS / N_VERSES

# ---------------------------------------------------------------- 2. reproduction gate
say("\n" + "=" * 78)
say("GATE 1 — REPRODUCTION OF THE PUBLISHED NATIVE DELTA (prereg §3). Runs first.")
say("=" * 78)
LAB = {c: [[rime_of(t, c) for t in vs] for vs in VERSES] for c in ("C", "P1")}
n_pairs_native = sum(len(vs) - 1 for vs in VERSES)
A_native = {c: sum(1 for s in range(len(VERSES)) for i in range(len(VERSES[s]) - 1)
                   if LAB[c][s][i] == LAB[c][s][i + 1]) / n_pairs_native
            for c in ("C", "P1")}
DELTA_NATIVE = A_native["P1"] - A_native["C"]
say(f"   verses={N_VERSES}  adjacent pairs={n_pairs_native}")
say(f"   A(C)={A_native['C']:.8f}   A(P1)={A_native['P1']:.8f}")
say(f"   Δ native (R2, P1) = {DELTA_NATIVE:.17f}")
say(f"   published          = {DELTA_PUBLISHED:.17f}")
say(f"   |difference|       = {abs(DELTA_NATIVE - DELTA_PUBLISHED):.3e}   tolerance {REPRO_TOL:.0e}")
if abs(DELTA_NATIVE - DELTA_PUBLISHED) > REPRO_TOL:
    die("REPRODUCTION FAILED — the published Δ is not reproduced. Everything downstream is "
        "void and nothing below may be cited (prereg §3).")
say("   GATE 1: PASS — exact reproduction.")
say(f"   (H-NEW-2930 and the brief write this as 0.18690; that is {DELTA_PUBLISHED:.6f} at 4 dp.)")

# ---------------------------------------------------------------- 3. the unit-length axis
say("\n" + "=" * 78)
say("THE AXIS (prereg §4) — a correction declared before the run, not after it.")
say("=" * 78)
say(f"   this corpus under arabic_words(): {TOTAL_WORDS} words / {N_VERSES} verses "
    f"= {NATIVE_LEN:.4f} words per verse")
say("   h-new-2890.py prints this same figure for this corpus, as '12.4', on the same "
    "tokeniser it measured the nine prose books with.")
_tanzil = open("data/alt-text/quran-uthmani-txt.txt", encoding="utf-8").read().split("\n")[:N_VERSES]
_tanzil_w = sum(len(l.split()) for l in _tanzil)
say(f"   H-NEW-2930 instead used {_tanzil_w} words / {N_VERSES} = {_tanzil_w / N_VERSES:.4f} "
    f"from the Tanzil .txt — a different file with different word splitting, plugged into a "
    f"fit calibrated on arabic_words lengths.")
AXIS = {"total_words_arabic_words": TOTAL_WORDS, "native_mean_unit_len": NATIVE_LEN,
        "tanzil_txt_words": _tanzil_w, "tanzil_mean": _tanzil_w / N_VERSES,
        "value_used_by_2930": 13.21}

# ---------------------------------------------------------------- 4. the nine-book baseline
say("\n" + "=" * 78)
say("THE PROSE BASELINE — reconstructed from the frozen H-NEW-2910 result (prereg §7).")
say("=" * 78)
NB = json.load(open(NINEBOOK, encoding="utf-8"))
CENSUS, ARMB = NB["census"], NB["arm_B"]
BOOKS = list(TABLE_2930)

recon = {}
say(f"   {'book':10s} {'len':>7s} | {'S5_all':>8s} {'S5_rd':>8s} {'S3_all':>8s} {'S3_rd':>8s} "
    f"{'S0_all':>8s} {'S0_rd':>8s} | {'max':>8s} {'2930':>8s}")
for b in BOOKS:
    cells = {}
    for s in ("S5", "S3", "S0"):
        e = ARMB[f"{b}_{s}"]
        cells[f"{s}_all"] = e["delta_all"]["P1"]
        cells[f"{s}_readable"] = e["delta_readable"]["P1"]
    mx = max(cells.values())
    L = CENSUS[b]["mean_unit_len"]
    recon[b] = {"mean_unit_len": L, "cells": cells, "max": mx,
                "which_max": max(cells, key=cells.get), "table_2930": TABLE_2930[b][1]}
    say(f"   {b:10s} {L:7.2f} | " + " ".join(f"{cells[k]:8.5f}" for k in
        ("S5_all", "S5_readable", "S3_all", "S3_readable", "S0_all", "S0_readable")) +
        f" | {mx:8.5f} {TABLE_2930[b][1]:8.5f}")

bad = [b for b in BOOKS if abs(recon[b]["max"] - TABLE_2930[b][1]) > 5e-6]
if bad:
    die(f"could not reconstruct H-NEW-2930's table from the frozen H-NEW-2910 result: {bad}")
say(f"\n   Every one of H-NEW-2930's nine values is the MAXIMUM over that book's six cells "
    f"({{S5,S3,S0}} x {{all,readable}}); H-NEW-2910 designates no primary segmentation.")
say(f"   Cells selected: " + ", ".join(f"{b}:{recon[b]['which_max']}" for b in BOOKS))
say("   That selection INFLATES the prose baseline, so it makes the residual CONSERVATIVE.")


def fit(pts):
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    m = sxy / sxx
    return m, my - m * mx, my


SETS = {"2930_max": [(recon[b]["mean_unit_len"], recon[b]["max"]) for b in BOOKS]}
for s in ("S5", "S3", "S0"):
    SETS[f"{s}_readable"] = [(recon[b]["mean_unit_len"], recon[b]["cells"][f"{s}_readable"])
                             for b in BOOKS]
FITS = {}
say(f"\n   {'set':14s} {'slope':>11s} {'intercept':>10s} {'mean Δ':>9s}")
for k, pts in SETS.items():
    m, c, my = fit(pts)
    FITS[k] = {"slope": m, "intercept": c, "mean_delta": my,
               "pred_at_native": c + m * NATIVE_LEN}
    say(f"   {k:14s} {m:11.8f} {c:10.5f} {my:9.5f}")

_m, _c = FITS["2930_max"]["slope"], FITS["2930_max"]["intercept"]
if round(_m, 6) != FIT_SLOPE_2930 or round(_c, 5) != FIT_INTERCEPT_2930:
    die(f"FIT GATE failed — refit of H-NEW-2930's table gives slope {_m:.8f} / intercept "
        f"{_c:.6f}, not its published {FIT_SLOPE_2930} / {FIT_INTERCEPT_2930} (prereg §7)")
say(f"\n   FIT GATE: PASS — refit reproduces H-NEW-2930's published "
    f"slope {FIT_SLOPE_2930} and intercept {FIT_INTERCEPT_2930}.")
say(f"   mean Δ of the 2930 table = {FITS['2930_max']['mean_delta']:.7f} "
    f"(the '~0.030' of the decision rule; prereg §7 primary target {PROSE_TARGET_2930})")
say(f"   2930 predicted Δ at its off-axis 13.21 : {_c + _m * 13.21:.5f} "
    f"-> residual {DELTA_NATIVE / (_c + _m * 13.21):.3f}x  (its published 3.63x)")
say(f"   on-axis prediction at {NATIVE_LEN:.4f}        : {FITS['2930_max']['pred_at_native']:.5f} "
    f"-> residual {DELTA_NATIVE / FITS['2930_max']['pred_at_native']:.3f}x")
checkpoint("baseline", {"axis": AXIS, "recon": recon, "fits": FITS,
                        "delta_native": DELTA_NATIVE})

# ---------------------------------------------------------------- 5. merge machinery
say("\n" + "=" * 78)
say("THE MERGE (prereg §5). Units never span a surah; a unit's label is the label of the "
    "JOINED text, gated against the label of its last constituent verse.")
say("=" * 78)


def seg_greedy(T):
    """M1 — accumulate verses until the unit reaches T words; trailing remainder is a unit."""
    out = []
    for s, lens in enumerate(WLEN):
        units, cur, acc = [], [], 0
        for i, L in enumerate(lens):
            cur.append(i)
            acc += L
            if acc >= T:
                units.append(cur)
                cur, acc = [], 0
        if cur:
            units.append(cur)
        out.append(units)
    return out


def seg_fixed(g):
    """M2 — consecutive blocks of exactly g verses; a surah's final block may be shorter."""
    return [[list(range(i, min(i + g, len(lens)))) for i in range(0, len(lens), g)]
            for lens in WLEN]


def seg_stats(seg):
    nu = sum(len(u) for u in seg)
    npair = sum(max(len(u) - 1, 0) for u in seg)
    return nu, TOTAL_WORDS / nu, npair, sum(1 for u in seg if len(u) >= 2)


def pick(make, lo, hi, target):
    """prereg §5 — Δ-free selection: the integer minimising |achieved mean − target|."""
    return min(range(lo, hi + 1), key=lambda k: abs(seg_stats(make(k))[1] - target))


MERGE_GATE = {"checked": 0, "mismatches": 0}


def delta_of(seg, gate=True):
    """Δ = A(P1) − A(C) over adjacent merged-unit pairs, pooled within surah."""
    agree = {"C": 0, "P1": 0}
    tot = 0
    for s, units in enumerate(seg):
        if len(units) < 2:
            continue
        lab = {"C": [], "P1": []}
        for u in units:
            joined = " ".join(VERSES[s][i] for i in u)
            for c in ("C", "P1"):
                v = rime_of(joined, c)
                lab[c].append(v)
                if gate:
                    MERGE_GATE["checked"] += 1
                    if v != LAB[c][s][u[-1]]:
                        MERGE_GATE["mismatches"] += 1
        for i in range(len(units) - 1):
            tot += 1
            for c in ("C", "P1"):
                agree[c] += (lab[c][i] == lab[c][i + 1])
    return {"A_C": agree["C"] / tot, "A_P1": agree["P1"] / tot,
            "delta": (agree["P1"] - agree["C"]) / tot, "n_pairs": tot}


def native_delta_on(seg):
    """Diagnostic — native Δ restricted to the surahs that survive this merge."""
    keep = [s for s, u in enumerate(seg) if len(u) >= 2]
    agree = {"C": 0, "P1": 0}
    tot = 0
    for s in keep:
        for i in range(len(VERSES[s]) - 1):
            tot += 1
            for c in ("C", "P1"):
                agree[c] += (LAB[c][s][i] == LAB[c][s][i + 1])
    return {"delta": (agree["P1"] - agree["C"]) / tot, "n_pairs": tot, "n_surahs": len(keep)}


def frac_closed(dm, prose):
    return (DELTA_NATIVE - dm) / (DELTA_NATIVE - prose)


ARMS = {}


def run_arm(target, primary):
    T = pick(seg_greedy, 1, 200, target)
    g = pick(seg_fixed, 1, 40, target)
    a = {"target": target, "primary_arm": primary, "T": T, "g": g}
    for tag, seg in (("M1_greedy", seg_greedy(T)), ("M2_fixed", seg_fixed(g))):
        nu, ml, npair, nsur = seg_stats(seg)
        d = delta_of(seg)
        rec = {"n_units": nu, "mean_unit_len": ml, "n_pairs_expected": npair,
               "n_surahs_ge2units": nsur, **d,
               "native_delta_same_surahs": native_delta_on(seg)}
        for k, F in FITS.items():
            pred = F["intercept"] + F["slope"] * ml
            rec[f"pred_{k}"] = pred
            rec[f"residual_ratio_{k}"] = d["delta"] / pred
            rec[f"f_vs_fit_{k}"] = frac_closed(d["delta"], pred)
            rec[f"f_vs_mean_{k}"] = frac_closed(d["delta"], F["mean_delta"])
        rec["f_primary"] = frac_closed(d["delta"], PROSE_TARGET_2930)
        a[tag] = rec
        say(f"   target {target:3d}  {tag:9s}  {'T=' + str(T) if tag.startswith('M1') else 'g=' + str(g):6s} "
            f"units={nu:5d} len={ml:7.3f} pairs={d['n_pairs']:5d} | "
            f"A(C)={d['A_C']:.5f} A(P1)={d['A_P1']:.5f} Δ={d['delta']:.5f}")
        say(f"                          fit pred at that length = {rec['pred_2930_max']:.5f} "
            f"-> residual {rec['residual_ratio_2930_max']:.3f}x | "
            f"f vs {PROSE_TARGET_2930} = {rec['f_primary']:+.4f}")
    ARMS[target] = a
    checkpoint(f"arm-{target}", a)
    return a


say(f"\n   PRIMARY ARM — target {TARGET_PRIMARY} words")
run_arm(TARGET_PRIMARY, True)

if MERGE_GATE["mismatches"]:
    die(f"MERGE GATE failed — {MERGE_GATE['mismatches']}/{MERGE_GATE['checked']} unit labels "
        f"differ from their last constituent verse's label (prereg §5).")
say(f"\n   MERGE GATE: PASS — {MERGE_GATE['checked']} unit labels checked, 0 mismatches; "
    f"merging is exactly a thinning of the ending sequence.")

P = ARMS[TARGET_PRIMARY]["M1_greedy"]
clean = (abs(P["mean_unit_len"] - TARGET_PRIMARY) <= 2.0 and P["n_pairs"] > 500)
say(f"   primary arm landed cleanly (|len-{TARGET_PRIMARY}| <= 2.0 and pairs > 500): {clean}")
if clean:
    say(f"\n   SECONDARY ARMS — {TARGETS_SECONDARY} (prereg §6; these gate nothing)")
    for t in TARGETS_SECONDARY:
        run_arm(t, False)
else:
    say("   secondary arms NOT run — the primary did not land cleanly (prereg §6).")

# ---------------------------------------------------------------- 6. diagnostics
say("\n" + "=" * 78)
say("DIAGNOSTICS (prereg §9) — declared, non-gating. None can change the verdict.")
say("=" * 78)
DIAG = {}

g0 = ARMS[TARGET_PRIMARY]["g"]
ph = []
for off in range(g0):
    seg = []
    for lens in WLEN:
        n = len(lens)
        b = ([list(range(0, min(off, n)))] if off else []) + \
            [list(range(i, min(i + g0, n))) for i in range(off, n, g0)]
        seg.append([u for u in b if u])
    d = delta_of(seg, gate=False)
    ph.append({"offset": off, "mean_unit_len": seg_stats(seg)[1], **d})
    say(f"   M2 phase offset {off}/{g0}: len={ph[-1]['mean_unit_len']:7.3f} "
        f"Δ={d['delta']:.5f} pairs={d['n_pairs']}")
DIAG["phases"] = {"g": g0, "arms": ph,
                  "mean_delta": sum(x["delta"] for x in ph) / len(ph),
                  "sd_delta": math.sqrt(sum((x["delta"] - sum(y["delta"] for y in ph) / len(ph)) ** 2
                                            for x in ph) / len(ph))}
say(f"   phase mean Δ = {DIAG['phases']['mean_delta']:.5f} "
    f"sd = {DIAG['phases']['sd_delta']:.5f}")

say("\n   Δ at verse lag L, no merging — isolates distance decay from the merge grid:")
DIAG["lag"] = []
for L in (1, 2, 3, 4, 5, 6, 8, 10):
    agree = {"C": 0, "P1": 0}
    tot = 0
    for s in range(len(VERSES)):
        for i in range(len(VERSES[s]) - L):
            tot += 1
            for c in ("C", "P1"):
                agree[c] += (LAB[c][s][i] == LAB[c][s][i + L])
    d = (agree["P1"] - agree["C"]) / tot
    DIAG["lag"].append({"lag": L, "delta": d, "n_pairs": tot,
                        "approx_word_distance": L * NATIVE_LEN})
    say(f"      lag {L:2d} (~{L * NATIVE_LEN:6.2f} words apart): Δ={d:.5f}  pairs={tot}")

say(f"\n   randomised segmentation, geometric boundaries at the same mean length "
    f"(seeds {SEED} / {SEED_REP}):")
DIAG["random_segmentation"] = {}
for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
    rng = random.Random(sd)
    p = NATIVE_LEN / TARGET_PRIMARY
    ds, lens_ = [], []
    for _ in range(N_RANDSEG if not SMOKE else 5):
        seg = []
        for lens in WLEN:
            units, cur = [], []
            for i in range(len(lens)):
                cur.append(i)
                if rng.random() < p:
                    units.append(cur)
                    cur = []
            if cur:
                units.append(cur)
            seg.append(units)
        d = delta_of(seg, gate=False)
        ds.append(d["delta"])
        lens_.append(seg_stats(seg)[1])
    mu = sum(ds) / len(ds)
    DIAG["random_segmentation"][tag] = {
        "seed": sd, "p_boundary": p, "n_draws": len(ds), "mean_delta": mu,
        "sd_delta": math.sqrt(sum((x - mu) ** 2 for x in ds) / len(ds)),
        "mean_unit_len": sum(lens_) / len(lens_),
        "f_primary": frac_closed(mu, PROSE_TARGET_2930)}
    r = DIAG["random_segmentation"][tag]
    say(f"      [{tag}] len={r['mean_unit_len']:.3f} mean Δ={mu:.5f} sd={r['sd_delta']:.5f} "
        f"f={r['f_primary']:+.4f}")
checkpoint("diagnostics", DIAG)

# ---------------------------------------------------------------- 7. verdict
say("\n" + "=" * 78)
say("VERDICT — prereg §8, printed against its own grid.")
say("=" * 78)
P = ARMS[TARGET_PRIMARY]["M1_greedy"]
F_PRIMARY = P["f_primary"]
say(f"   Δ native              = {DELTA_NATIVE:.5f}   (published, reproduced exactly)")
say(f"   Δ merged at {P['mean_unit_len']:.3f} w  = {P['delta']:.5f}")
say(f"   prose target          = {PROSE_TARGET_2930:.5f}  (mean of H-NEW-2930's nine-book table)")
say(f"   gap                   = {DELTA_NATIVE - PROSE_TARGET_2930:.5f}")
say(f"   gap closed            = {DELTA_NATIVE - P['delta']:.5f}")
say(f"\n   f = FRACTION OF THE GAP CLOSED = {F_PRIMARY:.4f}  ({100 * F_PRIMARY:.2f}%)")
say("\n   f against the internally consistent alternatives (prereg §7):")
for k in ("2930_max", "S5_readable", "S3_readable", "S0_readable"):
    say(f"      vs mean of {k:14s} ({FITS[k]['mean_delta']:.5f}) : f = {P[f'f_vs_mean_{k}']:+.4f}"
        f"   | vs fit at {P['mean_unit_len']:.1f}w ({P[f'pred_{k}']:.5f}) : f = {P[f'f_vs_fit_{k}']:+.4f}"
        f"   residual {P[f'residual_ratio_{k}']:.3f}x")
say(f"\n   IN-RANGE RESIDUAL RATIO (the successor to 2930's extrapolated 3.63x):")
say(f"      Δ_merged / fit prediction at {P['mean_unit_len']:.3f} words = "
    f"{P['residual_ratio_2930_max']:.3f}x  — no extrapolation; {P['mean_unit_len']:.1f} sits "
    f"inside the 49.2-91.1 word prose range.")

say("\n   prereg §8 grid, verbatim:")
say("      f >= 0.75          -> FINISHED AND WITHDRAWN (Δ is a unit-length effect)")
say("      f <= 0.25          -> RESIDUAL REAL AND LARGER than 2930's extrapolation suggested")
say("      0.25 < f < 0.75    -> PARTIAL, no headline either way")
if F_PRIMARY >= 0.75:
    VERDICT = "FINISHED AND WITHDRAWN — the cross-corpus magnitude claim is a unit-length effect"
elif F_PRIMARY <= 0.25:
    VERDICT = "RESIDUAL REAL AND LARGER than H-NEW-2930's extrapolation suggested"
else:
    VERDICT = "PARTIAL — re-cutting closes an intermediate share of the gap"
say(f"\n   VERDICT: {VERDICT}")
say("\n   NOT AT STAKE, restated: H-NEW-2880's within-corpus null (z = +15.03, 0/10,000, floor "
    "variance 0.00 across 160,000 draws) is untouched. No cross-corpus unit length enters it.")

# ---------------------------------------------------------------- 8. write
if SMOKE:
    say("\n[SMOKE] no run directory written, no JSON written. Exiting.")
    raise SystemExit(0)
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-2940", STAMP)
os.makedirs(RUNDIR, exist_ok=False)
out = {
    "id": "H-NEW-2940",
    "title": "The inverse re-cut — merge this corpus's own verses to prose unit lengths",
    "run_utc": STAMP, "prereg": PREREG, "prereg_sha256": PREREG_SHA256,
    "parent": "H-NEW-2930", "instrument": "H-NEW-2870 sections 0-6, executed verbatim",
    "frozen_inputs": FROZEN,
    "python": sys.version.split()[0], "platform": platform.platform(),
    "seed": SEED, "seed_replication": SEED_REP, "n_randseg": N_RANDSEG,
    "n_verses": N_VERSES, "n_pairs_native": n_pairs_native,
    "gate_a_orthography": GATE_A, "gate_b_instrument": GATE_B,
    "reproduction": {"delta_native": DELTA_NATIVE, "published": DELTA_PUBLISHED,
                     "abs_diff": abs(DELTA_NATIVE - DELTA_PUBLISHED), "tolerance": REPRO_TOL,
                     "pass": True, "A_native": A_native},
    "axis": AXIS,
    "prose_baseline": {"reconstruction": recon, "fits": FITS,
                       "table_2930_is_per_book_max": True,
                       "prose_target_primary": PROSE_TARGET_2930},
    "merge_gate": MERGE_GATE,
    "arms": ARMS,
    "diagnostics": DIAG,
    "f_primary": F_PRIMARY,
    "in_range_residual_ratio": P["residual_ratio_2930_max"],
    "verdict": VERDICT,
}
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as f:
    f.write(f"H-NEW-2940 run {STAMP}\nprereg {PREREG} {PREREG_SHA256}\n"
            f"script findings/phase-b-hypotheses/scripts/h-new-2940.py "
            f"{sha256_file('findings/phase-b-hypotheses/scripts/h-new-2940.py')}\n")
    for p, s in FROZEN.items():
        f.write(f"input {p} {s}\n")
    f.write(f"output {RUNDIR}/result.json\noutput {RUNDIR}/console.log\n")
    f.write(f"checkpoints {CHECKPOINT_DIR}/  (OUTSIDE the run directory, write-once)\n")
os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2940.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
print(f"\n[WROTE] {RUNDIR}/result.json")
print(f"[WROTE] findings/phase-b-hypotheses/csv/h-new-2940.json")
