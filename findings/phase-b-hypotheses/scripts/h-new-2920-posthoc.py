#!/usr/bin/env python3
"""H-NEW-2920 POST-HOC — diagnostics on T1, run after the locked arms were declared.

Nothing here changes any locked verdict. It answers three questions the locked run raised:

  A. does H-NEW-150's published residual arm (rho = 0.0859) reproduce, and what does
     residualising a variable with 87 zeros against log length actually do?
  B. where exactly does the liturgical score disagree with the formal naming count?
  C. which heavily-named surahs does the score fail to select at all?

Writes to its own run directory. Nothing inside any run directory is rewritten or deleted.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
import sys
from datetime import datetime, timezone

import numpy as np
from scipy import stats

ROOT = "/Users/grey/Downloads/quran"
LOCKED_RUN = os.path.join(ROOT, "runs/h-new-2920/20260807T225701Z")
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-posthoc"
RUNDIR = os.path.join(ROOT, "runs/h-new-2920", STAMP)
os.makedirs(RUNDIR, exist_ok=False)

_c: list[str] = []


def say(*a):
    line = " ".join(str(x) for x in a)
    _c.append(line)
    print(line, flush=True)


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as fh:
        for ch in iter(lambda: fh.read(1 << 20), b""):
            h.update(ch)
    return h.hexdigest()


SUR = list(range(1, 115))
h150 = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-150.json")))
lit = {int(k): float(v) for k, v in h150["liturgical_scores"].items()}
deg = {int(k): float(v) for k, v in h150["cluster_degrees"].items()}
r8601 = json.load(open(os.path.join(ROOT, "runs/h-new-860-1/20260807T221459Z/result.json")))
sc = {int(k): v for k, v in r8601["surah_counts"].items()}
F1 = {s: float(sc[s]["naming"]) for s in SUR}
QUO = {s: float(sc[s]["quotation"]) for s in SUR}
UNI = {s: float(sc[s]["union"]) for s in SUR}
VER = {s: float(sc[s]["verses"]) for s in SUR}
LOGV = {s: math.log(VER[s]) for s in SUR}
names = {}
with open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv"),
          encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        names[int(row["sura"])] = row["surah_name"]

OUT: dict = {"id": "H-NEW-2920-posthoc", "run": STAMP,
             "locked_run": os.path.relpath(LOCKED_RUN, ROOT),
             "status": "POST-HOC — changes no locked verdict"}


def resid(y, x):
    y = np.asarray(y, float)
    x = np.asarray(x, float)
    b, a = np.polyfit(x, y, 1)
    return y - (b * x + a)


# ---------------------------------------------------------------- A. the residual arm
say("=" * 88)
say("A. does H-NEW-150's residual arm reproduce, and what is it measuring?")
say("=" * 88)
lv = [LOGV[s] for s in SUR]
rl = resid([lit[s] for s in SUR], lv)
rd = resid([deg[s] for s in SUR], lv)
rho_res = float(stats.spearmanr(rl, rd).statistic)
say(f"published residual rho = {h150['secondary_length_residualized']['rho_residual']:+.4f}")
say(f"reproduced here        = {rho_res:+.4f}   "
    f"(delta {rho_res - h150['secondary_length_residualized']['rho_residual']:+.6f})")
rho_raw = float(stats.spearmanr([lit[s] for s in SUR], [deg[s] for s in SUR]).statistic)
say(f"raw rho reproduced     = {rho_raw:+.4f}  (published "
    f"{h150['primary']['rho_spearman']:+.4f})")

# what residualisation does to 87 tied zeros
zeros = [s for s in SUR if lit[s] == 0]
rl_map = {s: rl[i] for i, s in enumerate(SUR)}
zr = [rl_map[s] for s in zeros]
say("")
say(f"the score has {len(zeros)} tied zeros out of 114.")
say(f"  before residualising they are ONE tied rank; after, they occupy "
    f"{len(set(np.round(zr, 12)))} distinct values,")
say(f"  spanning {min(zr):+.4f} to {max(zr):+.4f}, ordered "
    f"rho = {float(stats.spearmanr(zr, [LOGV[s] for s in zeros]).statistic):+.4f} with log verses.")
say("  Residualising a zero-inflated score against length therefore REPLACES the ties with a")
say("  pure length ordering, and the residual correlation is then partly a length-vs-degree")
say("  correlation on 87 surahs that carry no liturgical information at all.")
prho, pp = stats.spearmanr([lit[s] for s in SUR], [deg[s] for s in SUR])
# rank-based partial, which does not manufacture order among ties
rx = stats.rankdata([lit[s] for s in SUR])
ry = stats.rankdata([deg[s] for s in SUR])
rz = stats.rankdata(lv)
Z = np.column_stack([np.ones_like(rz), rz])
ex = rx - Z @ np.linalg.lstsq(Z, rx, rcond=None)[0]
ey = ry - Z @ np.linalg.lstsq(Z, ry, rcond=None)[0]
part_r, part_p = stats.pearsonr(ex, ey)
say("")
say(f"  rank-based partial Spearman controlling log verses = {part_r:+.4f} (p={part_p:.4f})")
say(f"  against the published OLS-on-raw-values residual of "
    f"{h150['secondary_length_residualized']['rho_residual']:+.4f}")
say("  The two disagree, and the rank-based one does not manufacture order among the ties.")
OUT["A_residual_arm"] = {
    "published_residual_rho": h150["secondary_length_residualized"]["rho_residual"],
    "reproduced_residual_rho": rho_res,
    "reproduced_raw_rho": rho_raw,
    "published_raw_rho": h150["primary"]["rho_spearman"],
    "n_zero_scores": len(zeros),
    "zeros_residual_rho_with_log_verses":
        float(stats.spearmanr(zr, [LOGV[s] for s in zeros]).statistic),
    "rank_based_partial_rho": float(part_r), "rank_based_partial_p": float(part_p),
}

# same, with the formal count substituted
say("")
for lbl, v in [("F1_naming", F1), ("quotation", QUO), ("union", UNI)]:
    rr = float(stats.spearmanr(resid([v[s] for s in SUR], lv), rd).statistic)
    raw = float(stats.spearmanr([v[s] for s in SUR], [deg[s] for s in SUR]).statistic)
    say(f"  formal substitution {lbl:12s}: raw rho={raw:+.4f}  residual rho={rr:+.4f}")
    OUT.setdefault("A_formal_substitution", {})[lbl] = {"raw": raw, "residual": rr}

# ---------------------------------------------------------------- B. the disagreements
say("")
say("=" * 88)
say("B. where the liturgical score and the formal naming count disagree")
say("=" * 88)
OPS = sorted([s for s in SUR if lit[s] > 0])
lit_rank = {s: r for s, r in zip(sorted(OPS, key=lambda s: -lit[s]),
                                 range(1, len(OPS) + 1))}
f_rank_all = {s: r for s, r in zip(sorted(SUR, key=lambda s: (-F1[s], s)), range(1, 115))}
rows = []
for s in OPS:
    rows.append({"surah": s, "name": names[s], "score": lit[s], "score_rank": lit_rank[s],
                 "naming": F1[s], "naming_rank_all114": f_rank_all[s], "quotation": QUO[s]})
over = sorted(rows, key=lambda r: r["naming_rank_all114"] - r["score_rank"], reverse=True)[:10]
under = sorted(rows, key=lambda r: r["naming_rank_all114"] - r["score_rank"])[:10]
say(f"{'surah':>6} {'score':>6} {'score rk':>9} {'naming':>7} {'naming rk':>10}   name")
say("-- score over-rates (high score, little naming) " + "-" * 34)
for r in over:
    say(f"Q{r['surah']:>5} {r['score']:>6.0f} {r['score_rank']:>9} {r['naming']:>7.0f} "
        f"{r['naming_rank_all114']:>10}   {r['name']}")
say("-- score under-rates (much naming, low score) " + "-" * 36)
for r in under:
    say(f"Q{r['surah']:>5} {r['score']:>6.0f} {r['score_rank']:>9} {r['naming']:>7.0f} "
        f"{r['naming_rank_all114']:>10}   {r['name']}")
OUT["B_disagreements"] = {"over_rated": over, "under_rated": under, "all_scored": rows}

t10_lit = [s for s in sorted(OPS, key=lambda s: (-lit[s], s))][:10]
t10_f1 = [s for s in sorted(SUR, key=lambda s: (-F1[s], s))][:10]
t10_q = [s for s in sorted(SUR, key=lambda s: (-QUO[s], s))][:10]
say("")
say(f"top-10 by liturgical score : {t10_lit}")
say(f"top-10 by formal naming    : {t10_f1}   overlap {len(set(t10_lit) & set(t10_f1))}/10")
say(f"top-10 by formal quotation : {t10_q}   overlap {len(set(t10_lit) & set(t10_q))}/10")
OUT["B_top10"] = {"liturgical": t10_lit, "naming": t10_f1, "quotation": t10_q,
                  "overlap_naming": len(set(t10_lit) & set(t10_f1)),
                  "overlap_quotation": len(set(t10_lit) & set(t10_q))}

# ---------------------------------------------------------------- C. the selection failure
say("")
say("=" * 88)
say("C. the selection failure — heavily named surahs the score never scored")
say("=" * 88)
missed = sorted([s for s in SUR if lit[s] == 0 and F1[s] > 0],
                key=lambda s: -F1[s])
say(f"{len(missed)} surahs carry a formal naming count and a liturgical score of 0.")
say(f"{'surah':>6} {'naming':>7} {'quotation':>10}   name")
for s in missed[:15]:
    say(f"Q{s:>5} {F1[s]:>7.0f} {QUO[s]:>10.0f}   {names[s]}")
say("")
scored_naming = sum(F1[s] for s in OPS)
total_naming = sum(F1.values())
say(f"share of all naming links captured by the 27 scored surahs: "
    f"{scored_naming:.0f}/{total_naming:.0f} = {100*scored_naming/total_naming:.1f} %")
zero_named = [s for s in OPS if F1[s] == 0]
say(f"scored surahs with ZERO formal naming links: {len(zero_named)} of 27 -> {zero_named}")
OUT["C_selection"] = {"n_missed": len(missed),
                      "missed_top15": [{"surah": s, "naming": F1[s], "quotation": QUO[s],
                                        "name": names[s]} for s in missed[:15]],
                      "naming_share_captured": float(scored_naming / total_naming),
                      "scored_with_zero_naming": zero_named}

with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as fh:
    json.dump(OUT, fh, ensure_ascii=False, indent=2)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as fh:
    fh.write("\n".join(_c) + "\n")
print(f"\nwritten: {RUNDIR}")
