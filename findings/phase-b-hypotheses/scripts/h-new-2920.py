#!/usr/bin/env python3
"""H-NEW-2920 Part 2 — validating three hand-assigned quantities against computed alternatives.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-2920-proxy-validation.md
SHA-256 (locked)  adb194fb759d72f88ffb4600448c84b4faa14bf9236b34e9d5dbea534b4e4cdb

T1  H-NEW-150's hand-coded liturgical-prominence score vs a formal hadith naming count.
T2  the Noldeke chronology rank vs the Egyptian standard revelation order (rater swap).
T3  Q036-F-01's reconstructed 860 rubric vs the published 860 rubric and the formal count.

Run hygiene per prereg §7 and findings/UNIT-DRIFT-DEFECT.md §7:
  - run directory created with exist_ok=False, written ONCE at completion,
  - no file inside a run directory is ever rewritten or deleted,
  - checkpoints, if any, go outside the run directory.

Arabic character classes are built from integer codepoints and norm() is self-tested at
runtime, per H-NEW-860.1 §2.1 (bidi reordering of literal ranges destroys silently).
"""
from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import math
import os
import re
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone

import numpy as np
from scipy import stats

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2920-proxy-validation.md")
PREREG_SHA = "adb194fb759d72f88ffb4600448c84b4faa14bf9236b34e9d5dbea534b4e4cdb"
SEED = 20260808
SEED_REP = 20260818
N_PERM = 10_000

# prereg §6 — locked classification thresholds
RHO_NOISE = 0.20
RHO_CARRIES = 0.60

RUNS = os.path.join(ROOT, "runs/h-new-2920")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join(RUNS, STAMP)
os.makedirs(RUNS, exist_ok=True)
os.makedirs(RUNDIR, exist_ok=False)

_console: list[str] = []


def say(*a):
    line = " ".join(str(x) for x in a)
    _console.append(line)
    print(line, flush=True)


# ----------------------------------------------------------------------------------
# 0. integrity
# ----------------------------------------------------------------------------------
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


got = sha256(PREREG)
if got != PREREG_SHA:
    sys.exit(f"PREREG SHA MISMATCH\n  expected {PREREG_SHA}\n  got      {got}")
say(f"prereg SHA-256 verified: {got}")
say(f"run directory: {RUNDIR}")
say("")

# ----------------------------------------------------------------------------------
# 1. normalisation — codepoints only, self-tested (H-NEW-860.1 §2.1)
# ----------------------------------------------------------------------------------
_DELETE = set()
for lo, hi in [(0x0610, 0x061A), (0x064B, 0x065F), (0x0670, 0x0670),
               (0x06D6, 0x06ED), (0x0640, 0x0640)]:
    _DELETE.update(range(lo, hi + 1))
_MAP = {0x0622: 0x0627, 0x0623: 0x0627, 0x0625: 0x0627, 0x0671: 0x0627,
        0x0649: 0x064A, 0x0629: 0x0647, 0x0624: 0x0648, 0x0626: 0x064A}
_KEEP = set(range(0x0621, 0x064B)) | {0x20}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    out = []
    for ch in s:
        cp = ord(ch)
        if cp in _DELETE:
            continue
        cp = _MAP.get(cp, cp)
        out.append(chr(cp) if cp in _KEEP else " ")
    return re.sub(r"\s+", " ", "".join(out)).strip()


# self-test: a fully vocalised basmala must reduce to its skeleton, and must NOT vanish
_BASMALA_VOC = "بِسْمِ اللَّهِ " \
               "الرَّحْمَٰنِ " \
               "الرَّحِيمِ"
_BASMALA_EXP = "بسم الله الرحمن " \
               "الرحيم"
_t = norm(_BASMALA_VOC)
assert _t == _BASMALA_EXP, f"norm() self-test FAILED: {_t!r}"
assert len(norm("أمَّةٌ")) == 3
say(f"norm() self-test PASSED  ({_BASMALA_EXP})")

# prereg §3.2 F2 chapter stems, written as \u escapes so no bidi reordering can touch them
LITURGICAL_STEMS_RAW = [
    "صلا",                                     # sala- (salah / musalla)
    "جمع",                                     # jumu'a
    "عيد",                                     # 'id
    "وتر",                                     # witr
    "تهجد",                               # tahajjud
    "قيام",                               # qiyam
    "أذان",                               # adhan
    "سجود",                               # sujud
    "فضائل القرآن",   # fada'il al-qur'an
    "فضل القرآن",               # fadl al-qur'an
    "دعا",                                     # du'a
    "ذكر",                                     # dhikr
    "تراويح",                   # tarawih
    "رمضان",                         # ramadan
]
LITURGICAL_STEMS = [norm(s) for s in LITURGICAL_STEMS_RAW]
say("F2 liturgical chapter stems (normalised): " + " | ".join(LITURGICAL_STEMS))
say("")


# ----------------------------------------------------------------------------------
# 2. statistics helpers
# ----------------------------------------------------------------------------------
def spearman(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    r, p = stats.spearmanr(x, y)
    return float(r), float(p)


def perm_p_two_sided(x, y, seed, n=N_PERM):
    """Permutation p for |Spearman rho|, vectorised on ranks (ties handled by rankdata)."""
    rx = stats.rankdata(np.asarray(x, float))
    ry = stats.rankdata(np.asarray(y, float))
    rx = (rx - rx.mean()) / rx.std()
    ry = (ry - ry.mean()) / ry.std()
    k = len(rx)
    obs = abs(float(rx @ ry) / k)
    rng = np.random.default_rng(seed)
    idx = np.argsort(rng.random((n, k)), axis=1)
    draws = np.abs((ry[idx] @ rx) / k)
    return float((np.sum(draws >= obs - 1e-12) + 1) / (n + 1))


def partial_spearman(x, y, z):
    """Spearman partial correlation of x,y controlling z (rank-then-residualise)."""
    rx = stats.rankdata(x)
    ry = stats.rankdata(y)
    rz = stats.rankdata(z)
    Z = np.column_stack([np.ones_like(rz), rz])
    ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
    ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
    r, p = stats.pearsonr(ex, ey)
    return float(r), float(p)


def classify(rho_op, headline_reproduces):
    """prereg §6, verbatim."""
    if abs(rho_op) < RHO_NOISE and not headline_reproduces:
        return "NOISE"
    if rho_op >= RHO_CARRIES and headline_reproduces:
        return "CARRIES INFORMATION"
    return "PARTIAL"


RESULT: dict = {
    "id": "H-NEW-2920",
    "run": STAMP,
    "prereg": os.path.relpath(PREREG, ROOT),
    "prereg_sha256": PREREG_SHA,
    "seed": SEED,
    "seed_replication": SEED_REP,
    "n_perm": N_PERM,
    "classification_thresholds": {"noise_below": RHO_NOISE, "carries_at_or_above": RHO_CARRIES},
    "python": sys.version.split()[0],
    "numpy": np.__version__,
    "scipy": stats.__name__ and __import__("scipy").__version__,
}

# ==================================================================================
# T1 — H-NEW-150's liturgical-prominence score
# ==================================================================================
say("=" * 88)
say("T1 — H-NEW-150 liturgical-prominence score vs formal hadith naming count")
say("=" * 88)

h150 = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-150.json")))
lit = {int(k): float(v) for k, v in h150["liturgical_scores"].items()}
deg = {int(k): float(v) for k, v in h150["cluster_degrees"].items()}
assert len(lit) == 114 and len(deg) == 114

r8601 = json.load(open(os.path.join(
    ROOT, "runs/h-new-860-1/20260807T221459Z/result.json")))
sc = {int(k): v for k, v in r8601["surah_counts"].items()}
assert len(sc) == 114

SUR = list(range(1, 115))
F1 = {s: float(sc[s]["naming"]) for s in SUR}          # PRIMARY: naming count, 9 books
QUO = {s: float(sc[s]["quotation"]) for s in SUR}
UNI = {s: float(sc[s]["union"]) for s in SUR}
WORDS = {s: float(sc[s]["words"]) for s in SUR}
LOGW = {s: math.log(WORDS[s]) for s in SUR}

OPS = sorted([s for s in SUR if lit[s] > 0])           # the proxy's operating range
say(f"proxy operating range: {len(OPS)} surahs with non-zero liturgical score")
say(f"  {OPS}")
say(f"published H-NEW-150 primary : rho = {h150['primary']['rho_spearman']:+.4f}, "
    f"p_perm = {h150['primary']['p_perm_one_sided']}")
say(f"published H-NEW-150 residual: rho = "
    f"{h150['secondary_length_residualized']['rho_residual']:+.4f}, "
    f"p_perm = {h150['secondary_length_residualized']['p_perm_one_sided']}")
say("")

# ---- independent re-implementation of the naming instrument (positive control + F2 base)
BOOKS9 = ["bukhari", "muslim", "abudawud", "tirmidhi", "nasai",
          "ibnmajah", "malik", "ahmed", "darimi"]
DB9 = os.path.join(ROOT, "data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books")

names = {}
with open(os.path.join(ROOT,
          "findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv"),
          encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        names[int(row["sura"])] = row["surah_name"]
assert len(names) == 114

AL = "ال"
SURA_TOK = norm("سورة")          # "surat", normalised -> ...h


def name_variants(nm: str):
    nm = norm(nm)
    v = {nm}
    if nm.startswith(AL):
        v.add(nm[2:])
    else:
        v.add(AL + nm)
    return sorted(v, key=len, reverse=True)


NAME_RX = {}
for s in SUR:
    alts = "|".join(re.escape(v) for v in name_variants(names[s]))
    NAME_RX[s] = re.compile(r"(?<![^\s])" + re.escape(SURA_TOK) + r"\s+(?:" + alts + r")(?![^\s])")

naming_mine = {s: 0 for s in SUR}
naming_liturgical = {s: 0 for s in SUR}
chapters_hit, chapters_total = set(), set()
n_records = 0
for b in BOOKS9:
    d = json.load(open(os.path.join(DB9, b + ".json"), encoding="utf-8"))
    chap = {}
    for c in d["chapters"]:
        t = norm(c.get("arabic", "") or "")
        chap[c["id"]] = t
        chapters_total.add((b, c["id"]))
    lit_chaps = {cid for cid, t in chap.items()
                 if any(st in t for st in LITURGICAL_STEMS)}
    chapters_hit |= {(b, c) for c in lit_chaps}
    for h in d["hadiths"]:
        n_records += 1
        txt = norm(h.get("arabic", "") or "")
        if SURA_TOK not in txt:
            continue
        inlit = h.get("chapterId") in lit_chaps
        for s in SUR:
            if NAME_RX[s].search(txt):
                naming_mine[s] += 1
                if inlit:
                    naming_liturgical[s] += 1

tot_mine = sum(naming_mine.values())
tot_pub = int(r8601["instrument"]["naming_links"])
say(f"instrument positive control — records scanned: {n_records} (published 40943)")
say(f"  naming links, my re-implementation : {tot_mine} over "
    f"{sum(1 for s in SUR if naming_mine[s] > 0)} surahs")
say(f"  naming links, published H-NEW-860.1: {tot_pub} over 58 surahs")
say(f"  agreement rho(mine, published)     : "
    f"{spearman([naming_mine[s] for s in SUR], [F1[s] for s in SUR])[0]:+.4f}")
say(f"  liturgical chapters matched by the §3.2 stem list: "
    f"{len(chapters_hit)} of {len(chapters_total)}")
F2 = {s: float(naming_liturgical[s]) for s in SUR}
say(f"  F2 naming links inside liturgical chapters: {int(sum(F2.values()))}")
say("")

# ---- agreement coefficients
def agree(prox, formal, keys):
    x = [prox[s] for s in keys]
    y = [formal[s] for s in keys]
    r, p = spearman(x, y)
    t = stats.kendalltau(x, y)
    return {"n": len(keys), "rho": r, "p": p, "tau": float(t.statistic)}


T1 = {"published": {"rho": h150["primary"]["rho_spearman"],
                    "p_perm": h150["primary"]["p_perm_one_sided"],
                    "rho_residual": h150["secondary_length_residualized"]["rho_residual"]},
      "operating_range_n": len(OPS), "operating_range": OPS,
      "agreement": {}}

for label, formal in [("F1_naming", F1), ("F2_naming_liturgical_chapters", F2),
                      ("quotation", QUO), ("union", UNI)]:
    T1["agreement"][label] = {
        "operating_range": agree(lit, formal, OPS),
        "full_114": agree(lit, formal, SUR),
    }
    a = T1["agreement"][label]
    say(f"agreement  liturgical_score x {label:32s}"
        f"  op-range(n={a['operating_range']['n']:3d}) rho={a['operating_range']['rho']:+.4f} "
        f"p={a['operating_range']['p']:.4f}   full(114) rho={a['full_114']['rho']:+.4f} "
        f"p={a['full_114']['p']:.3g}")
say("")

# ---- headline re-run
T1["headline_rerun"] = {}
for label, formal in [("F1_naming", F1), ("quotation", QUO), ("union", UNI)]:
    x = [formal[s] for s in SUR]
    y = [deg[s] for s in SUR]
    r, p = spearman(x, y)
    pp = perm_p_two_sided(x, y, SEED)
    pp2 = perm_p_two_sided(x, y, SEED_REP)
    pr, ppar = partial_spearman(x, y, [LOGW[s] for s in SUR])
    T1["headline_rerun"][label] = {"rho": r, "p_scipy": p, "p_perm_seed1": pp,
                                   "p_perm_seed2": pp2,
                                   "partial_rho_ctrl_logwords": pr, "partial_p": ppar}
    say(f"headline re-run  rho({label}, cluster_degree) = {r:+.4f}  p={p:.4g}  "
        f"p_perm={pp:.4f}/{pp2:.4f}   partial|log words = {pr:+.4f} (p={ppar:.4f})")

xr, pr_ = spearman([lit[s] for s in SUR], [deg[s] for s in SUR])
say(f"  (proxy itself reproduced here: rho(liturgical_score, degree) = {xr:+.4f}, "
    f"published {h150['primary']['rho_spearman']:+.4f})")
T1["proxy_headline_reproduced"] = {"rho": xr, "published": h150["primary"]["rho_spearman"]}
say("")

# ---- UNIT-DRIFT §5: declare the drift of every variable
T1["drift_vs_log_surah_words"] = {}
for label, v in [("liturgical_score", lit), ("cluster_degree", deg), ("F1_naming", F1),
                 ("F2_liturgical_chapters", F2), ("quotation", QUO), ("union", UNI)]:
    r, p = spearman([v[s] for s in SUR], [LOGW[s] for s in SUR])
    T1["drift_vs_log_surah_words"][label] = {"rho": r, "p": p}
    say(f"drift  rho({label:24s}, log surah word count) = {r:+.4f}  (p={p:.3g})")

# H-NEW-150 residualised against log(n_verses), not log(words) — measured here too, and with
# it the LENGTH-EXTREMITY channel, because the finding's own §"Why the length-residualization
# kills the signal" describes a U-shape that a monotone rho cannot see. POST-HOC, DESCRIPTIVE.
VERSES = {s: float(sc[s]["verses"]) for s in SUR}
LOGV = {s: math.log(VERSES[s]) for s in SUR}
med = float(np.median([LOGV[s] for s in SUR]))
EXTREM = {s: abs(LOGV[s] - med) for s in SUR}
T1["posthoc_length_extremity"] = {"median_log_verses": med}
for label, v in [("liturgical_score", lit), ("cluster_degree", deg), ("F1_naming", F1),
                 ("quotation", QUO)]:
    rv, pvv = spearman([v[s] for s in SUR], [LOGV[s] for s in SUR])
    rx, px = spearman([v[s] for s in SUR], [EXTREM[s] for s in SUR])
    T1["posthoc_length_extremity"][label] = {"rho_log_verses": rv, "p_log_verses": pvv,
                                             "rho_abs_dev_from_median": rx, "p": px}
    say(f"POST-HOC  {label:20s} rho(.,log verses)={rv:+.4f} (p={pvv:.3g})   "
        f"rho(.,|log verses - median|)={rx:+.4f} (p={px:.3g})")
say("")

# ---- classification (prereg §6)
rho_op = T1["agreement"]["F1_naming"]["operating_range"]["rho"]
hr = T1["headline_rerun"]["F1_naming"]
headline_reproduces = (hr["rho"] > 0) and (hr["p_perm_seed1"] < 0.025)   # host's own bar
say("classification inputs (prereg §6):")
say(f"  rho_op                 = {rho_op:+.4f}   (NOISE if |rho|<{RHO_NOISE}, "
    f"CARRIES if >={RHO_CARRIES})")
say(f"  headline reproduces    = {headline_reproduces}  "
    f"(rho={hr['rho']:+.4f} > 0 and p_perm={hr['p_perm_seed1']:.4f} < 0.025)")
T1["classification"] = classify(rho_op, headline_reproduces)
T1["classification_inputs"] = {"rho_op": rho_op, "headline_reproduces": headline_reproduces}
say(f"  ==> T1 CLASSIFICATION: {T1['classification']}")
say("")
RESULT["T1_h_new_150_liturgical_score"] = T1

# ==================================================================================
# T2 — the chronology rank
# ==================================================================================
say("=" * 88)
say("T2 — Noldeke rank vs the Egyptian standard revelation order (rater swap)")
say("=" * 88)

nold, egy = {}, {}
with open(os.path.join(ROOT, "data/revelation-order.csv"), encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        m = int(row["mushaf_order"])
        nold[m] = int(row["noldeke_order"])
        egy[m] = int(row["revelation_order"])
assert len(nold) == 114 and len(egy) == 114
assert sorted(nold.values()) == list(range(1, 115))
assert sorted(egy.values()) == list(range(1, 115))

r_nn, p_nn = spearman([nold[s] for s in SUR], [egy[s] for s in SUR])
tau_nn = float(stats.kendalltau([nold[s] for s in SUR], [egy[s] for s in SUR]).statistic)
gaps = sorted(((abs(nold[s] - egy[s]), s) for s in SUR), reverse=True)
n_gt20 = sum(1 for g, _ in gaps if g > 20)
say(f"rho(Noldeke, Egyptian standard) = {r_nn:+.4f}  (p={p_nn:.3g}, Kendall tau={tau_nn:+.4f})")
say(f"surahs whose two ranks differ by more than 20 places: {n_gt20} of 114")
say("  largest disagreements (|delta rank|, surah):  " +
    ", ".join(f"Q{s}:{g}" for g, s in gaps[:12]))
T2 = {"rho_noldeke_vs_egyptian": r_nn, "p": p_nn, "kendall_tau": tau_nn,
      "n_rank_gap_gt_20": n_gt20,
      "largest_gaps": [{"surah": s, "gap": g, "noldeke": nold[s], "egyptian": egy[s]}
                       for g, s in gaps[:15]]}
say("")

h125 = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-125.json")))
pv = {int(k): v for k, v in h125["per_surah_axis_values"].items()}
axes = h125["axes_tested"]
alpha125 = h125["alpha_bon"]
say(f"H-NEW-125 axis re-scoring under the alternative rater "
    f"(published values used verbatim; alpha_bon = {alpha125})")
say(f"{'axis':30s} {'rho|Noldeke':>12s} {'rho|Egyptian':>13s} {'delta':>8s} "
    f"{'p|Nold':>10s} {'p|Egy':>10s}  survives")
T2["axes"] = {}
set_n, set_e = set(), set()
for ax in axes:
    v = [float(pv[s]["axis_values"][ax]) for s in SUR]
    rn, _ = spearman(v, [nold[s] for s in SUR])
    re_, _ = spearman(v, [egy[s] for s in SUR])
    pn = perm_p_two_sided(v, [nold[s] for s in SUR], SEED)
    pe = perm_p_two_sided(v, [egy[s] for s in SUR], SEED)
    sn, se = pn < alpha125, pe < alpha125
    if sn:
        set_n.add(ax)
    if se:
        set_e.add(ax)
    T2["axes"][ax] = {"rho_noldeke": rn, "p_perm_noldeke": pn, "survives_noldeke": bool(sn),
                      "rho_egyptian": re_, "p_perm_egyptian": pe, "survives_egyptian": bool(se),
                      "published_rho_noldeke": h125["per_axis_results"][ax]["rho_spearman"],
                      "sign_agrees": bool((rn > 0) == (re_ > 0))}
    say(f"{ax:30s} {rn:+12.4f} {re_:+13.4f} {re_-rn:+8.4f} {pn:10.4f} {pe:10.4f}"
        f"   {'N' if sn else '-'}{'E' if se else '-'}")
surv_n, surv_e = len(set_n), len(set_e)
say(f"axes surviving alpha_bon: Noldeke {surv_n}/15   Egyptian standard {surv_e}/15")
say(f"published H-NEW-125 count: {h125['n_axes_passing_bonferroni']}/15")
say(f"  published passing set reproduced under Noldeke here: "
    f"{sorted(set_n) == sorted(h125['axes_passing'])}")
say(f"  survivor set identical across raters: {set_n == set_e}")
if set_n != set_e:
    say(f"    only under Noldeke : {sorted(set_n - set_e)}")
    say(f"    only under Egyptian: {sorted(set_e - set_n)}")
sign_agree = sum(1 for a in T2["axes"].values() if a["sign_agrees"])
say(f"sign agreement across raters: {sign_agree}/15 axes")
T2["n_survive_noldeke"] = int(surv_n)
T2["n_survive_egyptian"] = int(surv_e)
T2["survivors_noldeke"] = sorted(set_n)
T2["survivors_egyptian"] = sorted(set_e)
T2["survivor_set_identical"] = bool(set_n == set_e)
T2["reproduces_published_passing_set"] = bool(sorted(set_n) == sorted(h125["axes_passing"]))
T2["n_published"] = h125["n_axes_passing_bonferroni"]
T2["n_sign_agree"] = int(sign_agree)
say("")

# drift channels under both orderings
mvl = {s: float(pv[s]["axis_values"]["mean_verse_length"]) for s in SUR}
vc = {s: float(pv[s]["axis_values"]["surah_length"]) for s in SUR}
T2["drift_channels"] = {}
for label, v in [("mean_verse_length", mvl), ("verse_count", vc), ("log_surah_words", LOGW)]:
    rn, _ = spearman([v[s] for s in SUR], [nold[s] for s in SUR])
    re_, _ = spearman([v[s] for s in SUR], [egy[s] for s in SUR])
    T2["drift_channels"][label] = {"rho_noldeke": rn, "rho_egyptian": re_}
    say(f"drift channel {label:20s} rho|Noldeke={rn:+.4f}   rho|Egyptian={re_:+.4f}")

# "the headline" for T2 is H-NEW-125's PASSING SET. The parameter-free reading of
# "reproduces" is: the same axes survive under the alternative rater. Reported alongside
# the counts so a reader can apply a looser reading if they prefer; the strict one is used.
T2["classification_inputs"] = {
    "rho_op": r_nn,
    "headline_reproduces": bool(set_n == set_e),
    "note": "headline = H-NEW-125's Bonferroni-surviving axis SET; reproduces iff identical "
            "under the alternative rater. This operationalisation was fixed at run time, not "
            "at lock time, and is disclosed as such.",
}
T2["classification"] = classify(r_nn, T2["classification_inputs"]["headline_reproduces"])
say("")
say(f"  ==> T2 CLASSIFICATION: {T2['classification']}  "
    f"(rho_op={r_nn:+.4f}, headline_reproduces="
    f"{T2['classification_inputs']['headline_reproduces']})")
say("")
RESULT["T2_chronology_rank"] = T2

# ==================================================================================
# T3 — Q036-F-01's reconstructed rubric
# ==================================================================================
say("=" * 88)
say("T3 — Q036-F-01's reconstructed 860 rubric vs the published rubric and the formal count")
say("=" * 88)

qpath = os.path.join(
    ROOT, "surahs/Q036-yasin/scripts/Q036_F_01_recitation_frequency_weighted_centrality.py")
spec = importlib.util.spec_from_file_location("q036f01", qpath)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
recon = {int(k): float(v) for k, v in mod.load_h_new_860_rubric().items()}
assert len(recon) == 114

# H-NEW-860's rubric scores 36 surahs 1..10; the other 78 are null, NOT zero. The support is
# defined by non-null, and the unlisted-as-zero reading is used only for the coefficient.
sup_p = sorted([s for s in SUR if sc[s]["rubric"] is not None])
pub = {s: float(sc[s]["rubric"] or 0) for s in SUR}
sup_r = sorted([s for s in SUR if recon[s] > 0])
union_sup = sorted(set(sup_r) | set(sup_p))
say(f"reconstruction scores {len(sup_r)} surahs; published rubric scores {len(sup_p)}")
say(f"  dropped by the reconstruction: {sorted(set(sup_p) - set(sup_r))}")
say(f"  invented by the reconstruction: {sorted(set(sup_r) - set(sup_p))}")
disagree = [(s, recon[s], pub[s]) for s in union_sup if recon[s] != pub[s]]
say(f"  surahs where the two differ: {len(disagree)} of {len(union_sup)} in the union support")

r_ru, p_ru = spearman([recon[s] for s in union_sup], [pub[s] for s in union_sup])
r_rp, p_rp = spearman([recon[s] for s in sup_p], [pub[s] for s in sup_p])
r_r18n, p_r18n = spearman([recon[s] for s in sup_r], [F1[s] for s in sup_r])
r_r18q, p_r18q = spearman([recon[s] for s in sup_r], [QUO[s] for s in sup_r])
say(f"rho(reconstruction, published rubric) over the union support (n={len(union_sup)}) "
    f"= {r_ru:+.4f}  p={p_ru:.4g}")
say(f"rho(reconstruction, published rubric) over the published 36  (n={len(sup_p)}) "
    f"= {r_rp:+.4f}  p={p_rp:.4g}")
say(f"rho(reconstruction, formal naming)    over its own {len(sup_r)}      "
    f"= {r_r18n:+.4f}  p={p_r18n:.4g}")
say(f"rho(reconstruction, formal quotation) over its own {len(sup_r)}      "
    f"= {r_r18q:+.4f}  p={p_r18q:.4g}")

T3 = {"n_support_reconstruction": len(sup_r), "n_support_published": len(sup_p),
      "dropped_by_reconstruction": sorted(set(sup_p) - set(sup_r)),
      "invented_by_reconstruction": sorted(set(sup_r) - set(sup_p)),
      "n_disagree_in_union": len(disagree),
      "disagreements": [{"surah": s, "reconstruction": a, "published": b}
                        for s, a, b in disagree],
      "rho_recon_vs_published_union": {"n": len(union_sup), "rho": r_ru, "p": p_ru},
      "rho_recon_vs_published_on_36": {"n": len(sup_p), "rho": r_rp, "p": p_rp},
      "rho_recon_vs_formal_naming_on_own": {"n": len(sup_r), "rho": r_r18n, "p": p_r18n},
      "rho_recon_vs_formal_quotation_on_own": {"n": len(sup_r), "rho": r_r18q, "p": p_r18q}}
T3["classification_inputs"] = {"rho_op": r_r18q, "headline_reproduces": False,
                               "note": "the parent rubric is already measured as carrying no "
                                       "discriminative information (H-NEW-860.1 §5, rho=+0.055); "
                                       "T3 asks only whether the derived table reproduces its "
                                       "declared source"}
T3["classification"] = classify(r_r18q, False)
say("")
say(f"  ==> T3 CLASSIFICATION: {T3['classification']}  (rho_op={r_r18q:+.4f} against the "
    f"formal quotation count over its own support)")
say("")
RESULT["T3_q036f01_reconstructed_rubric"] = T3

# ==================================================================================
say("=" * 88)
say("SUMMARY")
say("=" * 88)
for k, lbl in [("T1_h_new_150_liturgical_score", "T1  H-NEW-150 liturgical-prominence score"),
               ("T2_chronology_rank", "T2  Noldeke chronology rank"),
               ("T3_q036f01_reconstructed_rubric", "T3  Q036-F-01 reconstructed rubric")]:
    say(f"{lbl:48s} -> {RESULT[k]['classification']}")

# write ONCE, at completion (UNIT-DRIFT §7)
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as fh:
    json.dump(RESULT, fh, ensure_ascii=False, indent=2)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as fh:
    fh.write("\n".join(_console) + "\n")

INPUTS = [PREREG, qpath,
          os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-150.json"),
          os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-125.json"),
          os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv"),
          os.path.join(ROOT, "runs/h-new-860-1/20260807T221459Z/result.json"),
          os.path.join(ROOT, "data/revelation-order.csv")] + \
         [os.path.join(DB9, b + ".json") for b in BOOKS9]
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as fh:
    fh.write(f"H-NEW-2920 run {STAMP}\n\nINPUTS\n")
    for p in INPUTS:
        fh.write(f"{sha256(p)}  {os.path.relpath(p, ROOT)}\n")
    fh.write("\nOUTPUTS\n")
    for o in ("result.json", "console.log"):
        fh.write(f"{sha256(os.path.join(RUNDIR, o))}  {o}\n")
print(f"\nwritten: {RUNDIR}")
