#!/usr/bin/env python3
"""
H-NEW-2570 — POST-HOC MECHANISM DIAGNOSTICS. NO INFERENCE. MW-7 CAPPED.

This script computes NO p-values and tests NO hypothesis. It exists only to localise, on the
token axis, where the registered statistics of h-new-2570.py get their values from, so the
findings document can explain the observed dissociation between J (local roughness) and
A (global Heaps fidelity) rather than merely assert it.

Everything here is descriptive and was written AFTER the registered run. It carries no
evidential weight and is labelled as such wherever it is cited.

Author: Waiel Al-Shujaa.
"""

import csv
import json
import math
import os
from bisect import bisect_left

ROOT = "/Users/grey/Downloads/quran"
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2570-diagnostics.json")

import importlib.util

spec = importlib.util.spec_from_file_location(
    "h2570", os.path.join(ROOT, "findings/phase-b-hypotheses/scripts/h-new-2570.py")
)
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)


def main():
    seq_root, seq_lem = H.load_qac()
    tup = H.Tuple_("T1_ROOT", seq_root)
    rows = list(csv.DictReader(open(os.path.join(ROOT, "data/revelation-order.csv"), encoding="utf-8")))
    mushaf = list(range(1, 115))
    revelation = [int(r["mushaf_order"]) for r in sorted(rows, key=lambda r: int(r["revelation_order"]))]
    noldeke = [int(r["mushaf_order"]) for r in sorted(rows, key=lambda r: int(r["noldeke_order"]))]

    out = {"note": "POST-HOC DESCRIPTIVE DIAGNOSTICS ONLY — no inference, MW-7 capped",
           "tuple": "T1_ROOT", "n_tokens": tup.ntokens, "n_types": tup.ntypes}

    grid = H.geometric_grid(tup.ntokens, 50, 500)
    out["grid_M50_N500"] = grid

    # which surah covers each grid point, per ordering
    for oname, order in (("mushaf", mushaf), ("revelation", revelation), ("noldeke", noldeke)):
        pos = tup.first_positions(order)
        V = [bisect_left(pos, n) for n in grid]
        ys = [math.log(v) for v in V]
        xs = [math.log(n) for n in grid]
        beta, logk, r2, resid = H.ols(xs, ys)
        d2 = [None] + [ys[j + 1] - 2 * ys[j] + ys[j - 1] for j in range(1, len(ys) - 1)] + [None]

        # cumulative offsets -> which surah each grid point falls inside
        bounds, off = [], 0
        for s in order:
            off += tup.length[s]
            bounds.append(off)
        host = [order[bisect_left(bounds, n)] if n < tup.ntokens else order[-1] for n in grid]

        # per-position new-root contribution (how many unseen roots each surah adds)
        seen = bytearray(tup.ntypes)
        contrib = []
        for s in order:
            c = 0
            for _, tid in tup.firsts[s]:
                if not seen[tid]:
                    seen[tid] = 1
                    c += 1
            contrib.append({"surah": s, "tokens": tup.length[s], "new_roots": c})

        top_jerk = sorted(
            [{"grid_index": j, "N": grid[j], "V": V[j], "host_surah": host[j], "d2_logV": d2[j]}
             for j in range(1, len(ys) - 1)],
            key=lambda d: -abs(d["d2_logV"]),
        )[:8]

        out[oname] = {
            "V_at_grid": V,
            "beta": beta, "K": math.exp(logk), "R2": r2,
            "A": sum(abs(r) for r in resid) / len(resid),
            "J": sum(x * x for x in d2 if x is not None),
            "signed_residuals_first10": resid[:10],
            "signed_residuals_last10": resid[-10:],
            "top8_jerk_contributions": top_jerk,
            "first12_positions": contrib[:12],
            "new_roots_first10_positions": sum(c["new_roots"] for c in contrib[:10]),
            "tokens_first10_positions": sum(c["tokens"] for c in contrib[:10]),
            "new_roots_last30_positions": sum(c["new_roots"] for c in contrib[-30:]),
            "tokens_last30_positions": sum(c["tokens"] for c in contrib[-30:]),
        }

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)

    for o in ("mushaf", "revelation", "noldeke"):
        d = out[o]
        print(f"{o:11s} J={d['J']:.6f} A={d['A']:.6f} beta={d['beta']:.5f} R2={d['R2']:.5f}")
        print(f"            first-10 positions: {d['tokens_first10_positions']:6d} tokens -> "
              f"{d['new_roots_first10_positions']:5d} new roots")
        print(f"            last-30  positions: {d['tokens_last30_positions']:6d} tokens -> "
              f"{d['new_roots_last30_positions']:5d} new roots")
        print(f"            top jerk points: "
              + ", ".join(f"N={t['N']}(Q{t['host_surah']},d2={t['d2_logV']:+.4f})"
                          for t in d["top8_jerk_contributions"][:4]))
    print(f"[written] {OUT}")


if __name__ == "__main__":
    main()
