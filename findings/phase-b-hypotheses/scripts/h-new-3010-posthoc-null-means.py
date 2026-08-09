#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-3010 — POST-HOC DIAGNOSTIC (not pre-registered, changes no verdict).

The primary run (runs/h-new-3010/20260809T065744Z) returned NULL: every one of the
12 tests carries the locked sign, and none clears alpha_bon = 0.05/12 against the
worst of its 12 length controls.  For the primary cell the binding control is
mean-verse-length stratification, which is also the STRONGEST nuisance channel
(Spearman rho = +0.5467 between the LEGAL indicator and mean verse length).

This script answers the one question the verdict does not: *how much of the
observed contrast does length alone reproduce?*  Under a permutation stratified on
a channel that predicts the outcome, permuted groups inherit the real group's
length profile, so the NULL MEAN shifts toward the observed value by exactly the
amount length explains.  Reporting that shift is the decisive cheap diagnostic of
UNIT-DRIFT-DEFECT.md sec 6.

It reuses the locked script's own loaders and statistics verbatim (imported, not
reimplemented) and writes to its OWN directory.  It never touches the immutable
run directory.
"""

import os
import sys
import json
import math
import random
import datetime
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

spec = importlib.util.spec_from_file_location("h3010", os.path.join(HERE, "h-new-3010.py"))
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

M.verify_prereg()   # the locked prereg must still hash correctly

cond, wc, vc, vwl = M.load_qac(os.path.join(REPO, M.DATA_QAC))
genre = M.load_genre(os.path.join(REPO, M.DATA_TSV))
vecs, vqb, vqs = M.build_vectors(cond, vwl)
totals = {t: [sum(vecs[t][s][j] for s in range(1, 115)) for j in range(M.VEC_LEN)]
          for t in M.TUPLE_ORDER}
labels = {m: [M.MAPPERS[m](genre[s]["sinai"]) for s in range(1, 115)] for m in M.MAPPINGS}

chan = {
    "log_word_count":    [math.log(wc[s]) for s in range(1, 115)],
    "verse_count":       [float(vc[s]) for s in range(1, 115)],
    "mean_verse_length": [wc[s] / vc[s] for s in range(1, 115)],
    "UNSTRATIFIED":      None,
}

N = M.N_PERM
out = {"note": "POST-HOC, not pre-registered. Changes no verdict. Reports the null "
               "MEAN of the permutation distribution under each stratification, which "
               "measures how much of the observed contrast the length channel alone "
               "reproduces.",
       "n_perm": N, "seed": M.SEED, "cells": {}}

for m, t in M.CELLS:
    obs = M.all_statistics(labels[m], vecs, totals)
    for h in M.HYPOTHESES:
        key = "%s|%s|%s" % (h, m, t)
        o = obs[(t, "D_pooled", h)]
        row = {"observed_D_pooled": o, "by_channel": {}}
        for cname, cvals in chan.items():
            for b in ([5, 10] if cvals is not None else [1]):
                strata = ([list(range(114))] if cvals is None
                          else M.make_strata(cvals, b))
                rng = random.Random(M.SEED)
                cur = list(labels[m])
                draws = []
                for _ in range(N):
                    for st in strata:
                        v = [cur[i] for i in st]
                        rng.shuffle(v)
                        for i, x in zip(st, v):
                            cur[i] = x
                    draws.append(M.all_statistics(cur, vecs, totals)[(t, "D_pooled", h)])
                mu = sum(draws) / N
                sd = math.sqrt(sum((d - mu) ** 2 for d in draws) / (N - 1))
                row["by_channel"]["%s|bins=%d" % (cname, b)] = {
                    "null_mean": mu, "null_sd": sd,
                    "fraction_of_observed_reproduced_by_null_mean":
                        (mu / o) if o not in (0, None) else None,
                    "z_observed_vs_null": ((o - mu) / sd) if sd > 0 else None,
                }
        out["cells"][key] = row
        sys.stderr.write("  posthoc done: %s\n" % key)

ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
d = os.path.join(REPO, "findings/phase-b-hypotheses/runs/h-new-3010",
                 "POSTHOC-%s-null-means" % ts)
os.makedirs(d, exist_ok=False)
with open(os.path.join(d, "posthoc-null-means.json"), "x", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)

for key in ("H1|M1|T1", "H2|M1|T1", "H3|M1|T1"):
    r = out["cells"][key]
    print("\n%s   observed D_pooled = %+.5f" % (key, r["observed_D_pooled"]))
    for c, v in r["by_channel"].items():
        print("   %-28s null_mean=%+.5f sd=%.5f  reproduced=%6.1f%%  z=%+.2f"
              % (c, v["null_mean"], v["null_sd"],
                 100 * v["fraction_of_observed_reproduced_by_null_mean"],
                 v["z_observed_vs_null"]))
print("\nposthoc dir: %s" % d)
