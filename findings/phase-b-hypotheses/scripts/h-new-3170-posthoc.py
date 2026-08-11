#!/usr/bin/env python3
"""
H-NEW-3170 POST-HOC DIAGNOSTIC -- NOT A CONFIRMATORY CELL, NOT BLIND.

The pre-registered run 2026-08-09T110750Z is VOID on gate S4 (9.73% of tokens excluded
against a 1% limit). Independently, its C4 merger instrument was found DEFECTIVE: it
scored a consonant contrast as PRESERVED whenever the two words' whole Latin forms
differed, so vowel differences masked consonant mergers (cross-finding-030 mechanism 1,
in this lane's own design).

This script does ONE thing: it recovers the transliteration's character map EXACTLY,
by solving the counting identity that any deterministic character-level transliteration
must satisfy, and reports the true consonant merger partition. It runs no hypothesis
test and produces no verdict. Everything here is DESCRIPTIVE and was written after the
outcomes of the void run were seen.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import random
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path("/Users/grey/Downloads/quran")
VOID_RUN = "2026-08-09T110750Z"
UTC = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
RUN = REPO / "findings/phase-b-hypotheses/runs/h-new-3170-posthoc" / UTC
os.makedirs(RUN, exist_ok=False)
print(f"post-hoc run dir: {RUN}")

# Reuse the locked run's constants and phonemiser verbatim: take the source between the
# phonemiser header and the data-load header, which is exactly sections 1 and 2 (the
# ported h-new-2990 phonemiser, the classical sets, ALPHABET28, CARRIER_NORM, skeleton).
# No gate and no data load is executed by this splice.
_src = (REPO / "findings/phase-b-hypotheses/scripts/h-new-3170.py").read_text(encoding="utf-8")
_seg = _src.split("# 1. The phonemiser", 1)[1].split("# 3. Load, keyed by `id`", 1)[0]
exec(compile("# 1. The phonemiser" + _seg, "<h-new-3170 sections 1-2>", "exec"))
assert len(ALPHABET28) == 28 and TANWIN_REMAP and TARGET and SONORANT


def load_by_id(rel):
    return {s["id"]: s for s in json.loads((REPO / rel).read_text(encoding="utf-8"))}


T = load_by_id("quran-text/quran-transliteration.json")
A = load_by_id("quran-text/quran-full-tashkeel.json")

pairs = []
for sid in range(1, 115):
    for va, vt in zip(A[sid]["verses"], T[sid]["verses"]):
        la, lt = va["text"].split(), vt["text"].split()
        if len(la) == len(lt):
            pairs.extend(zip(la, lt))
print(f"aligned tokens: {len(pairs)}")

# ------------------------------------------------------------------------------------
# 1. Recover the character map by the counting identity.
#    For a deterministic character-level transliteration, for EVERY token:
#        count(latin char l) = sum over source symbols s of  M[s][l] * count(s)
#    Solving this over 70k tokens recovers M. The residual is the validity check.
# ------------------------------------------------------------------------------------
SRC = ALPHABET28 + ["V:a", "V:i", "V:u", "VV:a", "VV:i", "VV:u"]
LAT = sorted({c for _, t in pairs for c in t if not c.isspace()})
si = {s: i for i, s in enumerate(SRC)}
li = {c: i for i, c in enumerate(LAT)}

X = np.zeros((len(pairs), len(SRC)))
Y = np.zeros((len(pairs), len(LAT)))
for r, (a, t) in enumerate(pairs):
    for kind, val, _ in phonemes(a):
        if kind == "C":
            c = CARRIER_NORM.get(val, val)
            if c in si:
                X[r, si[c]] += 1
        else:
            X[r, si[f"{kind}:{val}"]] += 1
    for c in t:
        if not c.isspace():
            Y[r, li[c]] += 1

M, *_ = np.linalg.lstsq(X, Y, rcond=None)
Mr = np.round(M, 2)
resid = float(np.abs(X @ M - Y).mean())
print(f"mean |residual| per (token, latin char) cell: {resid:.4f}")

# image vector of each consonant, rounded to 1 dp; two consonants MERGE iff identical
img = {}
for c in ALPHABET28:
    v = Mr[si[c]]
    img[c] = tuple(sorted((LAT[j], round(float(v[j]), 1))
                          for j in range(len(LAT)) if abs(v[j]) >= 0.5))

by_img = defaultdict(list)
for c in ALPHABET28:
    by_img[img[c]].append(c)
merged_classes = [sorted(v) for v in by_img.values() if len(v) > 1]
merged_cons = sorted({c for cl in merged_classes for c in cl})

print("\n=== recovered consonant images ===")
for c in ALPHABET28:
    s = "".join(f"{k}×{n:g} " for k, n in img[c]) or "(none recovered)"
    print(f"  {c} -> {s}")
print("\n=== MERGER PARTITION (identical image vectors) ===")
for cl in merged_classes:
    print(f"  {{{''.join(cl)}}} -> {''.join(k for k, _ in img[cl[0]])}")
print(f"merged consonants: {''.join(merged_cons)}  ({len(merged_cons)} of 28)")
print(f"of which in mustaliya u halq: {''.join(sorted(set(merged_cons) & TARGET))}")
print(f"of which sonorant:            {''.join(sorted(set(merged_cons) & SONORANT))}")

# ------------------------------------------------------------------------------------
# 2. The C4 statistic, recomputed on the corrected partition. DESCRIPTIVE ONLY.
# ------------------------------------------------------------------------------------
cons_freq = Counter()
for sid in range(1, 115):
    for v in A[sid]["verses"]:
        for w in v["text"].split():
            for kind, val, _ in phonemes(w):
                if kind == "C":
                    cons_freq[CARRIER_NORM.get(val, val)] += 1


def F_stat(ms):
    tot = sum(cons_freq.get(c, 0) for c in ms)
    return sum(cons_freq.get(c, 0) for c in ms if c in TARGET) / tot if tot else 0.0


ranked = sorted(ALPHABET28, key=lambda c: cons_freq.get(c, 0))
QUART = {c: min(3, (i * 4) // 28) for i, c in enumerate(ranked)}
by_q = defaultdict(list)
for c in ALPHABET28:
    by_q[QUART[c]].append(c)
need = Counter(QUART[c] for c in merged_cons)

F_obs = F_stat(merged_cons)
combos = [list(itertools.combinations(by_q[q], k)) for q, k in sorted(need.items())]
n_cfg = math.prod(len(x) for x in combos)
vals = [F_stat([c for part in combo for c in part]) for combo in itertools.product(*combos)]
ge = sum(1 for x in vals if x >= F_obs - 1e-12)
eq = sum(1 for x in vals if abs(x - F_obs) < 1e-12)
print(f"\n=== C4 statistic on the CORRECTED partition (descriptive) ===")
print(f"  F_obs = {F_obs:.4f}   exact null over {n_cfg} frequency-stratified configurations")
print(f"  p_exact = {ge / n_cfg:.5f}   tie fraction = {eq / n_cfg:.4f}")
print(f"  null mean {sum(vals) / n_cfg:.4f}  min {min(vals):.4f}  max {max(vals):.4f}")
print(f"  (void run's defective partition gave F_obs = 0.1450, p = 0.8209)")

# ------------------------------------------------------------------------------------
# 3. Was C5's control degenerate?  Under the void run NO sonorant was ever merged, so
#    T_son == P_son identically and rho_son == 1.0000 by construction, in all 9 cells.
# ------------------------------------------------------------------------------------
son_merged = sorted(set(merged_cons) & SONORANT)
print(f"\n=== C5 control diagnostic ===")
print(f"  sonorants in the corrected merger set: {son_merged or 'NONE'}")
print(f"  => rho_sonorant(P,T) is {'still ' if not son_merged else 'no longer '}"
      f"identically 1.0 by construction"
      f"{'; the C5 control CANNOT discriminate' if not son_merged else ''}")

out = {
    "type": "POST-HOC DIAGNOSTIC -- descriptive, non-blind, no verdict",
    "void_run": VOID_RUN,
    "utc": UTC,
    "aligned_tokens": len(pairs),
    "counting_identity_mean_abs_residual": resid,
    "consonant_images": {c: [[k, n] for k, n in img[c]] for c in ALPHABET28},
    "merger_classes": merged_classes,
    "merged_consonants": merged_cons,
    "merged_in_target": sorted(set(merged_cons) & TARGET),
    "merged_sonorants": son_merged,
    "C4_corrected": {"F_obs": F_obs, "n_configurations": n_cfg,
                     "p_exact": ge / n_cfg, "tie_fraction": eq / n_cfg,
                     "null_mean": sum(vals) / n_cfg,
                     "null_min": min(vals), "null_max": max(vals)},
    "C4_void_run_defective": {"F_obs": 0.14495565410199557, "p": 0.8209179082091791},
    "C5_control_degenerate": not son_merged,
}
with open(RUN / "result.json", "x") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\nwritten to {RUN}")
