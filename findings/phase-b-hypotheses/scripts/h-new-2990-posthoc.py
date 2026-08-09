#!/usr/bin/env python3
"""H-NEW-2990 post-hoc: three diagnostics on the delivered instrument.

NOT part of the pre-registered build. It computes nothing new for the deliverable and
changes no column. It reads findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv
and answers three questions the registered run raised but did not answer:

  D1  Why is rho(struct_z_composite_resid, n_words) = +0.238 LARGER in magnitude than
      rho(struct_z_composite, n_words) = -0.182? An OLS residual on rank(n_words) should
      reduce the length association, not enlarge it.
  D2  What does each non-length column actually look like across the length range?
      Decile means, so a downstream user can see the shape a single rho compresses.
  D3  A worked example: the full profile of four verses a reader already knows, so the
      instrument can be sanity-checked by inspection rather than trusted.

Writes to runs/h-new-2990-posthoc/<UTC>/ -- a directory separate from the registered run,
which is not touched.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-2990-posthoc.py
"""

import csv
import json
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import rankdata

REPO = Path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")))
os.chdir(REPO)

PROFILE = "findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv"

NON_LENGTH_NUMERIC = [
    "frac_hapax_root_tokens", "frac_hapax_lemma_tokens",
    "mean_log10_root_freq", "median_log10_root_freq", "min_root_freq",
    "mean_root_surprisal_bits", "frac_root_tokens_freq_le5",
    "ttr_root", "root_simpson_repeat",
    "rime_class_size", "fasila_readable",
    "share_nominal", "share_verbal", "share_pronominal", "share_particle",
    "segments_per_word", "frac_derived_stems",
    "struct_z_composite", "struct_z_composite_resid",
]

WORKED_EXAMPLES = [(1, 1), (2, 255), (108, 1), (112, 1)]


def say(*a):
    print(" ".join(str(x) for x in a), flush=True)


def git_output(*args):
    try:
        return subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    return float(np.corrcoef(rankdata(x[ok]), rankdata(y[ok]))[0, 1])


def pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    ok = np.isfinite(x) & np.isfinite(y)
    return float(np.corrcoef(x[ok], y[ok])[0, 1])


def main():
    rows = list(csv.DictReader(open(PROFILE, encoding="utf-8")))
    say(f"[LOAD] {len(rows)} verses from {PROFILE}")

    def num(name):
        return np.array([float(r[name]) if r[name] != "" else np.nan for r in rows])

    n_words = num("n_words")
    rank_w = rankdata(n_words)

    # ---------------------------------------------------------------- D1
    comp = num("struct_z_composite")
    resid = num("struct_z_composite_resid")
    ok = np.isfinite(comp)
    d1 = {
        "spearman_composite_vs_n_words": spearman(comp, n_words),
        "spearman_resid_vs_n_words": spearman(resid, n_words),
        "pearson_composite_vs_rank_n_words": pearson(comp, rank_w),
        "pearson_resid_vs_rank_n_words": pearson(resid, rank_w),
        "pearson_resid_vs_n_words_raw": pearson(resid, n_words),
        "composite_skew": float(((comp[ok] - comp[ok].mean()) ** 3).mean()
                                / comp[ok].std() ** 3),
        "composite_excess_kurtosis": float(((comp[ok] - comp[ok].mean()) ** 4).mean()
                                           / comp[ok].std() ** 4 - 3.0),
    }
    # the shape a single rho compresses: composite mean and MEDIAN by n_words decile
    edges = np.nanpercentile(n_words, np.arange(0, 101, 10))
    bins = np.clip(np.digitize(n_words, edges[1:-1]), 0, 9)
    d1["composite_by_n_words_decile"] = []
    for b in range(10):
        sel = (bins == b) & ok
        if sel.sum() == 0:
            continue
        d1["composite_by_n_words_decile"].append({
            "decile": b + 1,
            "n": int(sel.sum()),
            "n_words_min": float(np.nanmin(n_words[sel])),
            "n_words_max": float(np.nanmax(n_words[sel])),
            "composite_mean": round(float(comp[sel].mean()), 4),
            "composite_median": round(float(np.median(comp[sel])), 4),
            "resid_mean": round(float(np.nanmean(resid[sel])), 4),
            "resid_median": round(float(np.nanmedian(resid[sel])), 4),
        })
    say(f"[D1] pearson(resid, rank n_words) = {d1['pearson_resid_vs_rank_n_words']:+.6f} "
        f"(OLS target: 0)   spearman(resid, n_words) = {d1['spearman_resid_vs_n_words']:+.4f}")

    # ---------------------------------------------------------------- D2
    d2 = {}
    for name in NON_LENGTH_NUMERIC:
        v = num(name)
        prof = []
        for b in range(10):
            sel = (bins == b) & np.isfinite(v)
            if sel.sum() == 0:
                continue
            prof.append({"decile": b + 1, "n": int(sel.sum()),
                         "mean": round(float(v[sel].mean()), 5),
                         "median": round(float(np.median(v[sel])), 5)})
        d2[name] = {"spearman_vs_n_words": round(spearman(v, n_words), 4),
                    "decile_profile": prof,
                    "monotone_in_decile_means": bool(
                        all(prof[i + 1]["mean"] >= prof[i]["mean"] for i in range(len(prof) - 1))
                        or all(prof[i + 1]["mean"] <= prof[i]["mean"] for i in range(len(prof) - 1)))}
    n_monotone = sum(1 for k in d2 if d2[k]["monotone_in_decile_means"])
    say(f"[D2] {n_monotone} of {len(d2)} columns are monotone in decile means")

    # ---------------------------------------------------------------- D3
    index = {(int(r["surah"]), int(r["verse"])): r for r in rows}
    d3 = {f"{s}:{v}": index[(s, v)] for s, v in WORKED_EXAMPLES if (s, v) in index}
    say(f"[D3] worked examples: {', '.join(d3)}")

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-2990-posthoc" / run_id
    os.makedirs(run_dir, exist_ok=False)
    payload = {
        "hypothesis": "H-NEW-2990 post-hoc",
        "status": "NOT pre-registered; diagnostics on the delivered instrument only",
        "registered_run_is_separate_and_untouched": "findings/phase-b-hypotheses/runs/h-new-2990/",
        "D1_composite_residual": d1,
        "D2_decile_profiles": d2,
        "D3_worked_examples": d3,
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump({
            "run_id": run_id,
            "run_directory": str(run_dir.relative_to(REPO)),
            "script": str(Path(__file__).resolve().relative_to(REPO)),
            "input": PROFILE,
            "git_commit": git_output("rev-parse", "HEAD"),
            "python": sys.version,
            "platform": platform.platform(),
            "utc": datetime.now(timezone.utc).isoformat(),
        }, handle, ensure_ascii=False, indent=2, sort_keys=True)
    say(f"[RUN DIR] {run_dir.relative_to(REPO)}")


if __name__ == "__main__":
    main()
