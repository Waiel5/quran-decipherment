#!/usr/bin/env python3
"""H-NEW-3000 POST-HOC 3. NOT pre-registered. NO verdict rests on anything here.

D6 left exactly one arm standing under an exact, length-stratified, same-statistic null:
I6, -log10(rime_class_size), at partial rho = +0.0883. D3 also measured that
rime_class_size is the MOST surah-loaded column in the instrument (eta^2 = 0.411 by surah).

Those two facts are in tension, and D7 cannot resolve it: a within-surah permutation leaves
the BETWEEN-surah component of a globally-computed statistic fixed across every draw, so for
a surah-loaded column it makes the observation look extreme close to by construction. D7 is
not a control for surah-level confounding.

D8 settles it directly by re-cutting the column instead of the null: replace each verse's
-log10(rime_class_size) by its deviation from its own surah's mean. If the association is
verse-level it survives; if it is a property of which surah the verse is in, it collapses.
The composite is centred the same way as a comparison.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3000-posthoc-3.py
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
    rx, ry, rz = rankdata(values), rankdata(outcome), rankdata(control)
    obs = partial_from_ranks(rx, ry, rz)
    rng = np.random.default_rng(seed)
    groups = [np.where(blocks == b)[0] for b in sorted(set(blocks.tolist()))]
    work = ry.copy()
    ge = 0
    draws = np.empty(n_perm)
    for j in range(n_perm):
        for idx in groups:
            work[idx] = ry[idx][rng.permutation(len(idx))]
        r = partial_from_ranks(rx, work, rz)
        draws[j] = r
        ge += r >= obs
    return {"partial_rho_obs": obs, "p_pos": (1 + int(ge)) / (1 + n_perm),
            "null_mean": float(draws.mean()), "null_sd": float(draws.std(ddof=1)), "seed": seed}


def main():
    profile = {(int(r["surah"]), int(r["verse"])): r for r in csv.DictReader(open(PROFILE, encoding="utf-8"))}
    weights = {(int(r["sura"]), int(r["aya"])): r for r in csv.DictReader(open(WEIGHTS, encoding="utf-8"))}
    keys = [k for k in sorted(profile, key=lambda k: int(profile[k]["mushaf_index"]))
            if weights[k]["eligible"] == "1"]
    n = len(keys)
    comp = np.array([float(profile[k]["struct_z_composite"]) for k in keys])
    rcs = -np.log10(np.array([float(profile[k]["rime_class_size"]) for k in keys]))
    nh = np.array([int(weights[k]["n_hadith"]) for k in keys], dtype=float)
    nw = np.array([int(profile[k]["n_words"]) for k in keys], dtype=float)
    surah = np.array([k[0] for k in keys])
    qs = np.quantile(nw, [i / K for i in range(1, K)])
    dec = np.searchsorted(np.array(sorted(set(float(q) for q in qs)), dtype=float), nw, side="left")

    def centre_within(v, labels):
        out = v.copy()
        for lab in set(labels.tolist()):
            m = labels == lab
            out[m] = v[m] - v[m].mean()
        return out

    say("\n[D8] surah-mean-centred columns, exact length-stratified null, partial statistic")
    say(f"     {'arm':<44s} {'partial rho':>11s} {'exact p(+)':>11s} {'rep':>8s}  clears a=0.00833")
    d8 = {}
    for label, vals in [
        ("I6 -log10(rime_class_size)  [as locked]", rcs),
        ("I6 the same, surah-mean-centred", centre_within(rcs, surah)),
        ("I1 struct_z_composite  [as locked]", comp),
        ("I1 the same, surah-mean-centred", centre_within(comp, surah)),
    ]:
        a = perm_partial(vals, nh, nw, dec, SEED_PRIMARY)
        b = perm_partial(vals, nh, nw, dec, SEED_REPLICATION)
        clears = bool(a["p_pos"] < ALPHA and b["p_pos"] < ALPHA)
        d8[label] = {"partial_rho": a["partial_rho_obs"], "exact_seed_20260509": a,
                     "exact_seed_20260519": b, "clears_alpha": clears}
        say(f"     {label:<44s} {a['partial_rho_obs']:+11.4f} {a['p_pos']:11.4f} {b['p_pos']:8.4f}"
            f"  {'YES' if clears else 'no'}")

    # how much of each column survives the centring at all
    say("\n[D8b] variance retained after surah-mean-centring")
    for label, v in [("-log10(rime_class_size)", rcs), ("struct_z_composite", comp)]:
        c = centre_within(v, surah)
        say(f"     {label:<32s} var {v.var():.5f} -> {c.var():.5f}  ({100*c.var()/v.var():.1f}% retained)")
    d8["variance_retained"] = {
        "-log10(rime_class_size)": float(centre_within(rcs, surah).var() / rcs.var()),
        "struct_z_composite": float(centre_within(comp, surah).var() / comp.var())}

    out = {"n": n, "alpha": ALPHA,
           "note": "POST-HOC 3. Not pre-registered. No verdict rests on anything here.",
           "D8_surah_mean_centred": d8}

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-3000" / (run_id + "-posthoc-3")
    os.makedirs(run_dir, exist_ok=False)
    with open(run_dir / "result.json", "x", encoding="utf-8") as h:
        json.dump(out, h, ensure_ascii=False, indent=2, sort_keys=True, default=float)
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as h:
        json.dump({"hypothesis": "H-NEW-3000", "kind": "POST-HOC 3 -- not pre-registered",
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
