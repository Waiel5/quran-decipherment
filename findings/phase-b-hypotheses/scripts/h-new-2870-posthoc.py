#!/usr/bin/env python3
"""
H-NEW-2870 POST-HOC diagnostic. Declared as post-hoc; gates nothing.

The run returned a split: under each rime definition one matched-collapse null is
cleared and the other is not, and they are opposite nulls. This asks the one question
that settles which null to believe:

    Are the upper-tail draws of N1-a -- the ones that beat the observed pausal
    agreement -- over-collapsed relative to the real pausal partition?

If they are, N1-a's upper tail is not "a random merge as coarse as waqf"; it is a
random merge COARSER than waqf, and beating the observed value with it proves nothing.
Measured by each draw's own chance floor sum(p_i^2) against the observed pausal floor.

Also reports the arithmetic/compositional decomposition of the delta.
"""
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)
sys.argv = [sys.argv[0], "--smoke"]          # load the instrument only; writes nothing

src = open("findings/phase-b-hypotheses/scripts/h-new-2870.py", encoding="utf-8").read()
cut = src.index("# ---------------------------------------------------------------- 7. the analysis")
ns = {"__name__": "instrument",
      "__file__": "findings/phase-b-hypotheses/scripts/h-new-2870.py"}
exec(compile(src[:cut], "h-new-2870-instrument", "exec"), ns)

SURAHS, N_VERSES = ns["SURAHS"], ns["N_VERSES"]
rime_of, flat = ns["rime_of"], ns["flat"]
SEED, N_PERM = ns["SEED"], 10000

PAIRS = [(sid, i) for sid, _, _, vs in SURAHS for i in range(len(vs) - 1)]
N_PAIRS = len(PAIRS)
print(f"loaded instrument: {N_VERSES} verses, {N_PAIRS} adjacent within-surah pairs\n")


def run(variant):
    ns["RIME_VARIANT"] = variant
    import builtins
    # rime_of closes over the module global, so set it in the module namespace
    exec(f"RIME_VARIANT = {variant!r}", ns)
    LAB = {c: {sid: [ns['rime_of'](t, c) for t in vs] for sid, _, _, vs in SURAHS}
           for c in ("C", "P1")}
    FL = {c: [x for sid, _, _, _ in SURAHS for x in LAB[c][sid]] for c in ("C", "P1")}
    A = {c: sum(1 for sid, i in PAIRS if LAB[c][sid][i] == LAB[c][sid][i + 1]) / N_PAIRS
         for c in ("C", "P1")}
    fl = {c: sum((v / N_VERSES) ** 2 for v in Counter(FL[c]).values()) for c in ("C", "P1")}

    print(f"=== {variant} ===")
    print(f"  K(C)={len(set(FL['C']))}  K(P1)={len(set(FL['P1']))}")
    print(f"  A(C)={A['C']:.4f}  A(P1)={A['P1']:.4f}  Δ={A['P1'] - A['C']:+.4f}")
    print(f"  chance floor: C={fl['C']:.4f}  P1={fl['P1']:.4f}   "
          f"free gain from concentration = {fl['P1'] - fl['C']:+.4f}")
    d = A["P1"] - A["C"]
    arith = fl["P1"] - fl["C"]
    print(f"  DECOMPOSITION of Δ={d:+.4f}:  arithmetic (chance-collision) {arith:+.4f} "
          f"= {100 * arith / d:.1f}%   |   compositional (excess) "
          f"{d - arith:+.4f} = {100 * (d - arith) / d:.1f}%")

    # --- N1-a upper-tail diagnostic
    cit = sorted(set(FL["C"]))
    CIDX = {t: i for i, t in enumerate(cit)}
    M = len(cit)
    size = [0] * M
    for t in FL["C"]:
        size[CIDX[t]] += 1
    SZ = np.asarray(size, dtype=np.float64)
    PA = np.array([CIDX[LAB["C"][sid][i]] for sid, i in PAIRS], dtype=np.int32)
    PB = np.array([CIDX[LAB["C"][sid][i + 1]] for sid, i in PAIRS], dtype=np.int32)
    tgt = sorted(Counter(FL["P1"]).values(), reverse=True)
    K = len(tgt)
    import heapq
    rng = random.Random(SEED)
    order = list(range(M))
    draws = []
    for _ in range(N_PERM):
        rng.shuffle(order)
        heap = [(-tgt[k], k) for k in range(K)]
        heapq.heapify(heap)
        blk = [0] * M
        for t in order:
            nr, k = heapq.heappop(heap)
            blk[t] = k
            heapq.heappush(heap, (nr + size[t], k))
        used = Counter(blk)
        empty = [k for k in range(K) if used[k] == 0]
        if empty:
            donors = [t for t in order if used[blk[t]] > 1]
            for k in empty:
                if not donors:
                    break
                t = donors.pop()
                used[blk[t]] -= 1
                blk[t] = k
                used[k] += 1
        b = np.asarray(blk, dtype=np.int32)
        sz = np.bincount(b, weights=SZ, minlength=K)
        draws.append((float(np.count_nonzero(b[PA] == b[PB])) / N_PAIRS,
                      float(((sz / N_VERSES) ** 2).sum()),
                      int((sz > 0).sum())))
    beat = [x for x in draws if x[0] >= A["P1"]]
    rest = [x for x in draws if x[0] < A["P1"]]
    print(f"  N1-a: {len(beat)}/{N_PERM} draws reach or beat the observed A(P1)={A['P1']:.4f}")
    if beat:
        print(f"        those draws' own chance floor: mean={sum(x[1] for x in beat) / len(beat):.4f}"
              f"  min={min(x[1] for x in beat):.4f}  max={max(x[1] for x in beat):.4f}")
    print(f"        all other draws' chance floor: mean={sum(x[1] for x in rest) / len(rest):.4f}")
    print(f"        the REAL pausal partition's chance floor: {fl['P1']:.4f}")
    if beat:
        over = sum(1 for x in beat if x[1] > fl["P1"])
        print(f"        -> {over}/{len(beat)} of the winning draws are MORE concentrated "
              f"than the real pausal partition ({100 * over / len(beat):.0f}%)")
    r = np.corrcoef([x[0] for x in draws], [x[1] for x in draws])[0, 1]
    print(f"        corr(A_null, floor_null) over all {N_PERM} draws = {r:+.4f}")
    print()
    return {"variant": variant, "A": A, "floor": fl, "delta": d,
            "arithmetic_share": arith / d, "n_beat": len(beat),
            "beat_floor_mean": (sum(x[1] for x in beat) / len(beat)) if beat else None,
            "beat_more_concentrated": (sum(1 for x in beat if x[1] > fl["P1"])) if beat else 0,
            "corr_A_floor": float(r), "observed_floor_P1": fl["P1"]}


res = [run("R1"), run("R2")]
os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2870-posthoc.json", "w", encoding="utf-8") as f:
    json.dump({"note": "POST-HOC diagnostic; gates nothing", "n_perm": N_PERM,
               "seed": SEED, "results": res}, f, ensure_ascii=False, indent=2)
print("[WROTE] findings/phase-b-hypotheses/csv/h-new-2870-posthoc.json")
