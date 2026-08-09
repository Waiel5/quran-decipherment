#!/usr/bin/env python3
"""H-NEW-3000 POST-HOC diagnostics. NOT pre-registered. NO verdict rests on anything here.

Occasioned by a disagreement inside the locked run: the ONE inference carrying an exact
permutation null (I2, p = 0.0085) and the parametric partial-Spearman on the same
relationship (I1, p = 0.0001) differ by ~100x. n_hadith is 86% tied at zero, and the
t-approximation behind every parametric p in the locked run is not trustworthy on that.

D1  exact stratified permutation nulls for I3-I6 -- the arms the locked run tested only
    parametrically. The direct analogue of I2.
D2  within-SURAH permutation null -- holds every surah-level property fixed. Diagnostic for
    whether rime_class_size (I6, the strongest arm) is a surah property read at verse level.
D3  eta^2 by surah -- how much of each structural column is between-surah variance.
D4  the binary decomposition -- S5 showed the graded reception signal is dead among cited
    verses (rho = +0.006, p = 0.87), so the association must live entirely in cited-vs-not.
D5  effect sizes as R^2.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3000-posthoc.py
"""

import csv
import hashlib
import json
import math
import os
import platform
import sys
from collections import Counter, defaultdict
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

SEED_PRIMARY = 20260509
SEED_REPLICATION = 20260519
N_PERM = 10000
ALPHA = 0.05 / 6
K = 10

MEMBERS = [("frac_hapax_root_tokens", +1), ("mean_root_surprisal_bits", +1),
           ("frac_root_tokens_freq_le5", +1), ("rime_class_size", -1)]


def sha256_file(path):
    d = hashlib.sha256()
    with open(path, "rb") as h:
        for c in iter(lambda: h.read(1 << 20), b""):
            d.update(c)
    return d.hexdigest()


def die(m):
    print("ABORT: " + m, file=sys.stderr)
    sys.exit(2)


def say(*a):
    print(" ".join(str(x) for x in a), flush=True)


if sha256_file(PARENT_PREREG) != PARENT_PREREG_SHA:
    die("parent pre-registration has changed since the locked run -- it must never be edited")
say(f"[SHA-OK] parent pre-registration unchanged: {PARENT_PREREG_SHA}")


def spearman(x, y):
    return float(np.corrcoef(rankdata(x), rankdata(y))[0, 1])


def partial_spearman(x, y, z):
    rxy, rxz, ryz = spearman(x, y), spearman(x, z), spearman(y, z)
    return (rxy - rxz * ryz) / math.sqrt((1 - rxz ** 2) * (1 - ryz ** 2))


def partial_p(rho, n, k=1):
    df = n - 2 - k
    s = rho * math.sqrt(df / (1 - rho ** 2))
    return float(tdist.sf(s, df)), float(tdist.cdf(s, df))


def strat_perm(values, outcome, blocks, seed, n_perm=N_PERM):
    """Permute the outcome within blocks. Ranks are permuted directly -- an identity, since
    within-block permutation leaves the outcome's multiset unchanged."""
    rho_obs = spearman(values, outcome)
    rng = np.random.default_rng(seed)
    groups = [np.where(blocks == b)[0] for b in sorted(set(blocks.tolist()))]
    rv = rankdata(values)
    rv = (rv - rv.mean()) / rv.std()
    ro = rankdata(outcome)
    work = ro.copy()
    ge = le = 0
    draws = np.empty(n_perm)
    for j in range(n_perm):
        for idx in groups:
            work[idx] = ro[idx][rng.permutation(len(idx))]
        c = work - work.mean()
        r = float((rv @ c) / (len(rv) * c.std()))
        draws[j] = r
        ge += r >= rho_obs
        le += r <= rho_obs
    return {"rho_obs": rho_obs, "p_pos": (1 + int(ge)) / (1 + n_perm),
            "p_neg": (1 + int(le)) / (1 + n_perm), "null_mean": float(draws.mean()),
            "null_sd": float(draws.std(ddof=1)), "n_blocks": len(groups), "seed": seed}


def eta_squared(values, labels):
    v = np.asarray(values, dtype=float)
    total = ((v - v.mean()) ** 2).sum()
    within = 0.0
    for lab in set(labels.tolist()):
        g = v[labels == lab]
        within += ((g - g.mean()) ** 2).sum()
    return float((total - within) / total) if total > 0 else float("nan")


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
    cited = (nh > 0).astype(float)

    qs = np.quantile(nw, [i / K for i in range(1, K)])
    edges = sorted(set(float(q) for q in qs))
    dec = np.searchsorted(np.array(edges, dtype=float), nw, side="left")

    member_vals = {}
    for name, sign in MEMBERS:
        raw = np.array([float(profile[k][name]) for k in keys])
        member_vals[name] = sign * (np.log10(raw) if name == "rime_class_size" else raw)

    out = {"n": n, "note": "POST-HOC. Not pre-registered. No verdict rests on anything here."}

    # ---- D1: exact permutation nulls for the arms the locked run tested only parametrically
    say("\n[D1] exact stratified permutation nulls (k = 10) for the four member arms")
    say(f"     {'arm':<32s} {'rho':>8s} {'param p(+)':>11s} {'perm p(+)':>10s} {'perm p(+) rep':>14s}  clears a=0.00833")
    d1 = {}
    named = [("I1 struct_z_composite", comp)] + \
            [(f"I{i} {'-log10(' + nm + ')' if nm == 'rime_class_size' else '+' + nm}", member_vals[nm])
             for i, (nm, _s) in zip([3, 4, 5, 6], MEMBERS)]
    for label, vals in named:
        rho_p = partial_spearman(vals, nh, nw)
        p_par, _ = partial_p(rho_p, n)
        a = strat_perm(vals, nh, dec, SEED_PRIMARY)
        b = strat_perm(vals, nh, dec, SEED_REPLICATION)
        d1[label] = {"partial_rho": rho_p, "param_p_pos": p_par,
                     "perm_seed_20260509": a, "perm_seed_20260519": b,
                     "perm_clears_alpha": bool(a["p_pos"] < ALPHA and b["p_pos"] < ALPHA)}
        say(f"     {label:<32s} {a['rho_obs']:+8.4f} {p_par:11.5f} {a['p_pos']:10.4f} {b['p_pos']:14.4f}"
            f"  {'YES' if d1[label]['perm_clears_alpha'] else 'no'}")
    out["D1_exact_permutation_nulls"] = d1

    # ---- D2: within-surah permutation -- holds every surah-level property fixed
    say("\n[D2] within-SURAH permutation null (surah-level properties held fixed)")
    d2 = {}
    for label, vals in named:
        a = strat_perm(vals, nh, surah, SEED_PRIMARY)
        d2[label] = a
        say(f"     {label:<32s} rho = {a['rho_obs']:+.4f}  p(+) = {a['p_pos']:.4f}  "
            f"({a['n_blocks']} surah blocks)")
    out["D2_within_surah_permutation"] = d2

    # ---- D3: how much of each column is between-surah variance
    say("\n[D3] eta^2 by surah -- share of variance that is BETWEEN surahs")
    d3 = {"struct_z_composite": eta_squared(comp, surah), "n_words": eta_squared(nw, surah),
          "n_hadith": eta_squared(nh, surah)}
    for nm, _s in MEMBERS:
        d3[nm] = eta_squared(np.array([float(profile[k][nm]) for k in keys]), surah)
    for nm, v in sorted(d3.items(), key=lambda kv: -kv[1]):
        say(f"     {nm:<32s} {v:.4f}")
    out["D3_eta_squared_by_surah"] = d3

    # ---- D4: the binary decomposition
    say("\n[D4] binary decomposition -- cited at all (n=%d) vs graded among the cited (n=%d)"
        % (int(cited.sum()), int(cited.sum())))
    d4 = {}
    rho_bin = partial_spearman(comp, cited, nw)
    p_pos_bin, _ = partial_p(rho_bin, n)
    perm_bin = strat_perm(comp, cited, dec, SEED_PRIMARY)
    perm_bin_rep = strat_perm(comp, cited, dec, SEED_REPLICATION)
    d4["binary_cited_vs_not"] = {"partial_rho": rho_bin, "param_p_pos": p_pos_bin,
                                 "perm_seed_20260509": perm_bin, "perm_seed_20260519": perm_bin_rep}
    say(f"     composite vs 1[cited]      partial rho = {rho_bin:+.4f}  param p(+) = {p_pos_bin:.5f}  "
        f"perm p(+) = {perm_bin['p_pos']:.4f} / {perm_bin_rep['p_pos']:.4f}")
    sub = cited > 0
    rho_graded = partial_spearman(comp[sub], nh[sub], nw[sub])
    p_pos_g, _ = partial_p(rho_graded, int(sub.sum()))
    d4["graded_among_cited"] = {"n": int(sub.sum()), "partial_rho": rho_graded, "param_p_pos": p_pos_g}
    say(f"     composite vs n_hadith | cited   partial rho = {rho_graded:+.4f}  param p(+) = {p_pos_g:.4f}   (n = {int(sub.sum())})")

    # cited rate by structural quintile, within length decile -- descriptive, rank-defined bins
    q = np.zeros(n, dtype=int)
    for b in sorted(set(dec.tolist())):
        idx = np.where(dec == b)[0]
        pct = (rankdata(comp[idx]) - 0.5) / len(idx)
        q[idx] = np.clip((pct * 5).astype(int), 0, 4)
    rates = {int(i + 1): {"n": int((q == i).sum()), "n_cited": int(cited[q == i].sum()),
                          "cited_rate": float(cited[q == i].mean())} for i in range(5)}
    d4["cited_rate_by_structural_quintile_within_length_decile"] = rates
    say("     cited rate by within-decile structural quintile (1 = most ordinary, 5 = most unusual):")
    for i in range(1, 6):
        r = rates[i]
        say(f"        Q{i}: {r['n_cited']:4d}/{r['n']:5d} = {100*r['cited_rate']:5.2f}%")
    out["D4_binary_decomposition"] = d4

    # ---- D5: effect sizes
    d5 = {label: {"partial_rho": d1[label]["partial_rho"],
                  "R2_percent": 100 * d1[label]["partial_rho"] ** 2} for label in d1}
    say("\n[D5] effect sizes")
    for label, v in d5.items():
        say(f"     {label:<32s} rho = {v['partial_rho']:+.4f}   R^2 = {v['R2_percent']:.3f}%")
    out["D5_effect_sizes"] = d5

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-3000" / (run_id + "-posthoc")
    os.makedirs(run_dir, exist_ok=False)
    with open(run_dir / "result.json", "x", encoding="utf-8") as h:
        json.dump(out, h, ensure_ascii=False, indent=2, sort_keys=True, default=float)
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as h:
        json.dump({"hypothesis": "H-NEW-3000", "kind": "POST-HOC -- not pre-registered",
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
