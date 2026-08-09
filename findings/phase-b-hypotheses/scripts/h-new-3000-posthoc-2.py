#!/usr/bin/env python3
"""H-NEW-3000 POST-HOC 2. NOT pre-registered. NO verdict rests on anything here.

Occasioned by a defect in POST-HOC 1's own diagnostic, found by reading its output.

D1 judged the parametric arms I1 and I3-I6 against a stratified permutation null whose test
statistic is the BARE Spearman -- the statistic the pre-registration locked for I2. For I4
that comparison is unfair in a way that matters: bare rho = +0.0020 while partial rho =
+0.0328, so the partialling is where I4's association lives, and a null built on the bare
statistic cannot see it. A null and the statistic it judges must be the same quantity.

D6 therefore re-runs the stratified permutation with the PARTIAL Spearman as the test
statistic -- the exact, apples-to-apples test of the locked parametric arms. This is the
number that decides what a reader should believe about the locked SUPPORTED verdict.

D7 repeats it against the within-surah blocks.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3000-posthoc-2.py
"""

import csv
import hashlib
import json
import math
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import rankdata, t as tdist

REPO = Path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")))
os.chdir(REPO)

PARENT_PREREG = "findings/phase-b-hypotheses/prereg-h-new-3000-reception-residual-rosters.md"
PARENT_PREREG_SHA = "6515fe1a12ebf742e3ab72d5c6e18e8c5a82d1c0a4f4fd894aa9397eed344789"
PROFILE = "findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv"
WEIGHTS = "findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv"

SEED_PRIMARY, SEED_REPLICATION, N_PERM, ALPHA, K = 20260509, 20260519, 10000, 0.05 / 6, 10
MEMBERS = [("frac_hapax_root_tokens", +1), ("mean_root_surprisal_bits", +1),
           ("frac_root_tokens_freq_le5", +1), ("rime_class_size", -1)]


def sha256_file(p):
    d = hashlib.sha256()
    with open(p, "rb") as h:
        for c in iter(lambda: h.read(1 << 20), b""):
            d.update(c)
    return d.hexdigest()


def say(*a):
    print(" ".join(str(x) for x in a), flush=True)


if sha256_file(PARENT_PREREG) != PARENT_PREREG_SHA:
    print("ABORT: parent pre-registration changed", file=sys.stderr)
    sys.exit(2)
say(f"[SHA-OK] parent pre-registration unchanged: {PARENT_PREREG_SHA}")


def corr(a, b):
    return float(np.corrcoef(a, b)[0, 1])


def partial_from_ranks(rx, ry, rz):
    rxy, rxz, ryz = corr(rx, ry), corr(rx, rz), corr(ry, rz)
    return (rxy - rxz * ryz) / math.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))


def perm_partial(values, outcome, control, blocks, seed, n_perm=N_PERM):
    """Stratified permutation with the PARTIAL Spearman as the test statistic.

    Within-block permutation leaves the outcome's multiset unchanged, so its ranks are
    permuted rather than recomputed -- an identity, verified against the literal route on
    the first 25 draws."""
    rx, ry, rz = rankdata(values), rankdata(outcome), rankdata(control)
    obs = partial_from_ranks(rx, ry, rz)
    rng = np.random.default_rng(seed)
    groups = [np.where(blocks == b)[0] for b in sorted(set(blocks.tolist()))]
    work_rank, work_val = ry.copy(), np.asarray(outcome, dtype=float).copy()
    ge = le = 0
    draws = np.empty(n_perm)
    for j in range(n_perm):
        for idx in groups:
            p = rng.permutation(len(idx))
            work_rank[idx] = ry[idx][p]
            if j < 25:
                work_val[idx] = np.asarray(outcome, dtype=float)[idx][p]
        r = partial_from_ranks(rx, work_rank, rz)
        if j < 25:
            slow = partial_from_ranks(rx, rankdata(work_val), rz)
            if abs(r - slow) > 1e-9:
                print(f"ABORT: fast route disagreed {r} vs {slow}", file=sys.stderr)
                sys.exit(2)
        draws[j] = r
        ge += r >= obs
        le += r <= obs
    return {"partial_rho_obs": obs, "p_pos": (1 + int(ge)) / (1 + n_perm),
            "p_neg": (1 + int(le)) / (1 + n_perm), "null_mean": float(draws.mean()),
            "null_sd": float(draws.std(ddof=1)), "n_blocks": len(groups), "seed": seed}


def main():
    profile = {(int(r["surah"]), int(r["verse"])): r for r in csv.DictReader(open(PROFILE, encoding="utf-8"))}
    weights = {(int(r["sura"]), int(r["aya"])): r for r in csv.DictReader(open(WEIGHTS, encoding="utf-8"))}
    keys = [k for k in sorted(profile, key=lambda k: int(profile[k]["mushaf_index"]))
            if weights[k]["eligible"] == "1"]
    n = len(keys)
    comp = np.array([float(profile[k]["struct_z_composite"]) for k in keys])
    nh = np.array([int(weights[k]["n_hadith"]) for k in keys], dtype=float)
    nw = np.array([int(profile[k]["n_words"]) for k in keys], dtype=float)
    surah = np.array([k[0] for k in keys])
    qs = np.quantile(nw, [i / K for i in range(1, K)])
    dec = np.searchsorted(np.array(sorted(set(float(q) for q in qs)), dtype=float), nw, side="left")

    arms = [("I1 struct_z_composite", comp)]
    for i, (nm, sg) in zip([3, 4, 5, 6], MEMBERS):
        raw = np.array([float(profile[k][nm]) for k in keys])
        arms.append((f"I{i} {'-log10(' + nm + ')' if nm == 'rime_class_size' else '+' + nm}",
                     sg * (np.log10(raw) if nm == "rime_class_size" else raw)))

    out = {"n": n, "note": "POST-HOC 2. Not pre-registered. No verdict rests on anything here.",
           "alpha": ALPHA}

    say("\n[D6] stratified permutation (k=10) with the PARTIAL Spearman as the test statistic")
    say(f"     {'arm':<32s} {'partial rho':>11s} {'param p(+)':>11s} {'exact p(+)':>11s} {'rep':>8s}  clears a=0.00833")
    d6 = {}
    for label, vals in arms:
        a = perm_partial(vals, nh, nw, dec, SEED_PRIMARY)
        b = perm_partial(vals, nh, nw, dec, SEED_REPLICATION)
        df = n - 3
        s = a["partial_rho_obs"] * math.sqrt(df / (1 - a["partial_rho_obs"] ** 2))
        p_par = float(tdist.sf(s, df))
        clears = bool(a["p_pos"] < ALPHA and b["p_pos"] < ALPHA)
        d6[label] = {"partial_rho": a["partial_rho_obs"], "param_p_pos": p_par,
                     "exact_seed_20260509": a, "exact_seed_20260519": b, "clears_alpha": clears}
        say(f"     {label:<32s} {a['partial_rho_obs']:+11.4f} {p_par:11.5f} {a['p_pos']:11.4f} {b['p_pos']:8.4f}"
            f"  {'YES' if clears else 'no'}")
    out["D6_exact_partial_statistic_length_strata"] = d6

    say("\n[D7] the same, with WITHIN-SURAH blocks (surah-level properties held fixed)")
    d7 = {}
    for label, vals in arms:
        a = perm_partial(vals, nh, nw, surah, SEED_PRIMARY)
        d7[label] = a
        say(f"     {label:<32s} partial rho = {a['partial_rho_obs']:+.4f}  exact p(+) = {a['p_pos']:.4f}  "
            f"null sd = {a['null_sd']:.4f}")
    out["D7_exact_partial_statistic_surah_blocks"] = d7

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-3000" / (run_id + "-posthoc-2")
    os.makedirs(run_dir, exist_ok=False)
    with open(run_dir / "result.json", "x", encoding="utf-8") as h:
        json.dump(out, h, ensure_ascii=False, indent=2, sort_keys=True, default=float)
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as h:
        json.dump({"hypothesis": "H-NEW-3000", "kind": "POST-HOC 2 -- not pre-registered",
                   "run_directory": str(run_dir.relative_to(REPO)),
                   "script": str(Path(__file__).resolve().relative_to(REPO)),
                   "parent_prereg": PARENT_PREREG, "parent_prereg_sha256": PARENT_PREREG_SHA,
                   "inputs": [{"path": p, "sha256": sha256_file(p)} for p in (PROFILE, WEIGHTS)],
                   "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION},
                   "n_permutations": N_PERM, "python": sys.version, "numpy": np.__version__,
                   "platform": platform.platform(),
                   "utc": datetime.now(timezone.utc).isoformat()}, h, indent=2, sort_keys=True)
    say(f"\n[RUN DIR] {run_dir.relative_to(REPO)}")


if __name__ == "__main__":
    main()
