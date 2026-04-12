#!/usr/bin/env python3
"""
Phase B / H14: per-surah Zipf alpha fit and its correlation with revelation order.

Rules tuple:
    orthography: no-tashkeel (QAC lemma data are source-canonical; independent
                 of Arabic-letter orthography at lemma level)
    word_definition: lemma (QAC 0.4 LEM field)
    letter_definition: not-applicable
    basmala_policy: counted-only-in-surah-1 (QAC default; basmala of surah 1
                    is in the morphology file, other basmalas are not)
    verse_numbering: hafs-kufan
    abjad_table: not-applicable
    null_model: 1.5 permutation of revelation-order labels (n=10000) for
                Spearman rho significance; bootstrap 95% CI for each alpha

Inputs:
    /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
    /Users/grey/Downloads/quran/data/revelation-order.csv

Outputs:
    /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/zipf-per-surah.csv
    /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/zipf-per-surah-results.json

Fit rule (matches info_theory_run.py task4_zipf exactly):
    - lemmas = each STEM line with LEM: field, one token per segment
    - per surah: rank distinct lemmas by descending freq, break ties arbitrarily
    - OLS log-log: x = log(rank) with rank starting at 1 (so x_min = log(1) = 0),
      y = log(freq); slope = -alpha
"""
from __future__ import annotations

import csv
import json
import math
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
MORPH_PATH = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
REV_ORDER_PATH = ROOT / "data/revelation-order.csv"
OUT_DIR = ROOT / "findings/phase-b-hypotheses/csv"
OUT_DIR.mkdir(parents=True, exist_ok=True)

MIN_DISTINCT_LEMMAS = 50  # per task spec
N_BOOTSTRAP = 1000
N_PERM = 10000
SEED = 17  # reproducible


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------


def parse_morphology(path: Path):
    """Yield (surah, verse, word, seg, lemma) for each STEM line that has a LEM:."""
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.strip() or line.startswith("#"):
                continue
            if line.startswith("LOCATION"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0].strip("()").split(":")
            try:
                s, v, w, seg = (int(x) for x in loc)
            except ValueError:
                continue
            feats = parts[3]
            if "STEM" not in feats:
                continue
            if "LEM:" not in feats:
                continue
            lemma = None
            for f in feats.split("|"):
                if f.startswith("LEM:"):
                    lemma = f[4:]
                    break
            if lemma is None:
                continue
            yield s, v, w, seg, lemma


def load_revelation_order(path: Path) -> dict:
    """mushaf_id -> dict with revelation_order / period / name / noldeke_phase."""
    out = {}
    with path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            sid = int(row["mushaf_order"])
            out[sid] = {
                "revelation_order": int(row["revelation_order"]),
                "mushaf_order": sid,
                "name_ar": row["surah_name_ar"],
                "name_tl": row["surah_name_tl"],
                "period": row["period"],
                "noldeke_order": int(row["noldeke_order"]) if row["noldeke_order"] else None,
                "noldeke_phase": row["noldeke_phase"],
            }
    return out


# ---------------------------------------------------------------------------
# Zipf fit: OLS log-log, rank-1-based (matches info_theory_run.py)
# ---------------------------------------------------------------------------


def zipf_fit_from_counts(counts: list[int]):
    """OLS log-log fit of Zipf: slope on log(rank_1_based) vs log(freq)."""
    if len(counts) < 2:
        return None
    freqs = sorted(counts, reverse=True)
    n = len(freqs)
    xs = [math.log(r + 1) for r in range(n)]  # r=0 -> log(1)=0
    ys = [math.log(f) for f in freqs]
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    sxx = sum((xs[i] - mx) ** 2 for i in range(n))
    syy = sum((ys[i] - my) ** 2 for i in range(n))
    if sxx == 0 or syy == 0:
        return None
    slope = sxy / sxx
    intercept = my - slope * mx
    r2 = (sxy ** 2) / (sxx * syy)
    alpha = -slope
    return {"alpha": alpha, "intercept": intercept, "r2": r2, "n": n}


def zipf_fit_from_lemmas(lemma_tokens: list[str]):
    counter = Counter(lemma_tokens)
    return zipf_fit_from_counts(list(counter.values())), len(counter), len(lemma_tokens)


# ---------------------------------------------------------------------------
# Bootstrap CI for alpha
# ---------------------------------------------------------------------------


def bootstrap_alpha(lemma_tokens: list[str], n_boot: int, rng: random.Random):
    n = len(lemma_tokens)
    alphas = []
    for _ in range(n_boot):
        sample = [lemma_tokens[rng.randrange(n)] for _ in range(n)]
        counter = Counter(sample)
        if len(counter) < 2:
            continue
        fit = zipf_fit_from_counts(list(counter.values()))
        if fit is None:
            continue
        alphas.append(fit["alpha"])
    if not alphas:
        return None, None, None
    alphas.sort()
    lo = alphas[int(0.025 * len(alphas))]
    hi = alphas[int(0.975 * len(alphas)) - 1]
    median = alphas[len(alphas) // 2]
    return lo, hi, median


# ---------------------------------------------------------------------------
# Spearman rho (no scipy)
# ---------------------------------------------------------------------------


def rank_with_ties(xs):
    """Average-rank handling of ties; returns list of float ranks."""
    paired = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(paired):
        j = i
        while j + 1 < len(paired) and xs[paired[j + 1]] == xs[paired[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1  # 1-based average rank
        for k in range(i, j + 1):
            ranks[paired[k]] = avg
        i = j + 1
    return ranks


def spearman_rho(xs, ys):
    rx = rank_with_ties(xs)
    ry = rank_with_ties(ys)
    n = len(xs)
    mx = sum(rx) / n
    my = sum(ry) / n
    sxy = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    sxx = sum((rx[i] - mx) ** 2 for i in range(n))
    syy = sum((ry[i] - my) ** 2 for i in range(n))
    if sxx == 0 or syy == 0:
        return 0.0
    return sxy / math.sqrt(sxx * syy)


def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    sxx = sum((xs[i] - mx) ** 2 for i in range(n))
    syy = sum((ys[i] - my) ** 2 for i in range(n))
    if sxx == 0 or syy == 0:
        return 0.0
    return sxy / math.sqrt(sxx * syy)


def point_biserial(binary, xs):
    # binary: 0/1 list; xs: continuous. Equivalent to Pearson(binary, xs).
    return pearson([float(b) for b in binary], xs)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    rng = random.Random(SEED)

    rev = load_revelation_order(REV_ORDER_PATH)

    # Collect lemmas per surah
    per_surah_lemmas: dict[int, list[str]] = defaultdict(list)
    total_tokens = 0
    for s, v, w, seg, lemma in parse_morphology(MORPH_PATH):
        per_surah_lemmas[s].append(lemma)
        total_tokens += 1

    print(f"Total lemma tokens parsed: {total_tokens}")
    print(f"Surahs with lemma data: {len(per_surah_lemmas)}")

    # Whole-Quran Zipf (sanity check against info-theory 1.318)
    all_lemmas = [lem for s in per_surah_lemmas.values() for lem in s]
    whole_fit = zipf_fit_from_counts(list(Counter(all_lemmas).values()))
    print(
        f"Whole-Quran Zipf (lemma): alpha={whole_fit['alpha']:.4f} "
        f"R^2={whole_fit['r2']:.4f} n_distinct={whole_fit['n']}"
    )

    # Per-surah fit
    rows = []
    valid_rows = []
    for sid in sorted(per_surah_lemmas.keys()):
        tokens = per_surah_lemmas[sid]
        counter = Counter(tokens)
        n_distinct = len(counter)
        n_tokens = len(tokens)
        info = rev.get(sid, {})
        row = {
            "mushaf_order": sid,
            "name_tl": info.get("name_tl", ""),
            "name_ar": info.get("name_ar", ""),
            "period": info.get("period", ""),
            "revelation_order": info.get("revelation_order", None),
            "noldeke_order": info.get("noldeke_order", None),
            "noldeke_phase": info.get("noldeke_phase", ""),
            "n_lemma_tokens": n_tokens,
            "n_distinct_lemmas": n_distinct,
        }
        if n_distinct < MIN_DISTINCT_LEMMAS:
            row["status"] = "insufficient-data"
            row["zipf_alpha"] = None
            row["r_squared"] = None
            row["boot_alpha_lo"] = None
            row["boot_alpha_hi"] = None
            row["boot_alpha_median"] = None
        else:
            fit = zipf_fit_from_counts(list(counter.values()))
            lo, hi, med = bootstrap_alpha(tokens, N_BOOTSTRAP, rng)
            row["status"] = "ok"
            row["zipf_alpha"] = round(fit["alpha"], 6)
            row["r_squared"] = round(fit["r2"], 6)
            row["boot_alpha_lo"] = round(lo, 6) if lo is not None else None
            row["boot_alpha_hi"] = round(hi, 6) if hi is not None else None
            row["boot_alpha_median"] = round(med, 6) if med is not None else None
            valid_rows.append(row)
        rows.append(row)

    print(f"Valid (>= {MIN_DISTINCT_LEMMAS} distinct lemmas): {len(valid_rows)}")
    print(f"Insufficient: {len(rows) - len(valid_rows)}")

    # Correlations (only among valid rows)
    alphas = [r["zipf_alpha"] for r in valid_rows]
    rev_orders = [r["revelation_order"] for r in valid_rows]
    nold_orders = [r["noldeke_order"] for r in valid_rows]
    is_medinan = [1 if r["period"] == "Medinan" else 0 for r in valid_rows]
    n_distincts = [r["n_distinct_lemmas"] for r in valid_rows]
    n_tokens_list = [r["n_lemma_tokens"] for r in valid_rows]
    log_tokens = [math.log(n) for n in n_tokens_list]

    rho_rev = spearman_rho(alphas, rev_orders)
    rho_nold = spearman_rho(alphas, nold_orders)
    rho_tokens = spearman_rho(alphas, n_tokens_list)
    rho_distinct = spearman_rho(alphas, n_distincts)
    pb_medinan = point_biserial(is_medinan, alphas)

    print(f"Spearman rho(alpha, revelation_order) = {rho_rev:.4f}")
    print(f"Spearman rho(alpha, noldeke_order)    = {rho_nold:.4f}")
    print(f"Spearman rho(alpha, n_lemma_tokens)   = {rho_tokens:.4f}")
    print(f"Spearman rho(alpha, n_distinct)       = {rho_distinct:.4f}")
    print(f"Point-biserial r(Medinan, alpha)      = {pb_medinan:.4f}")

    # Permutation test for rho_rev
    def perm_p(obs_rho, ys):
        """Two-sided empirical p via permuting ys."""
        rng2 = random.Random(SEED + 1)
        hits = 0
        shuffled = list(ys)
        for _ in range(N_PERM):
            rng2.shuffle(shuffled)
            r = spearman_rho(alphas, shuffled)
            if abs(r) >= abs(obs_rho):
                hits += 1
        return (hits + 1) / (N_PERM + 1)

    p_rev = perm_p(rho_rev, rev_orders)
    p_nold = perm_p(rho_nold, nold_orders)
    print(f"Perm p (n={N_PERM}) rho_rev  = {p_rev:.4f}")
    print(f"Perm p (n={N_PERM}) rho_nold = {p_nold:.4f}")

    # Partial correlation of alpha vs revelation order controlling for log_tokens
    # via residualization (Pearson-based).
    def residuals(y, x):
        n = len(y)
        mx = sum(x) / n
        my = sum(y) / n
        sxy = sum((x[i] - mx) * (y[i] - my) for i in range(n))
        sxx = sum((x[i] - mx) ** 2 for i in range(n))
        slope = sxy / sxx if sxx else 0.0
        intercept = my - slope * mx
        return [y[i] - (slope * x[i] + intercept) for i in range(n)]

    alpha_resid = residuals(alphas, log_tokens)
    rev_resid = residuals(rev_orders, log_tokens)
    rho_rev_partial = spearman_rho(alpha_resid, rev_resid)
    pearson_rev_partial = pearson(alpha_resid, rev_resid)
    print(
        f"Partial Spearman rho(alpha|log_tokens, rev|log_tokens) = {rho_rev_partial:.4f}"
    )
    print(
        f"Partial Pearson  r  (alpha|log_tokens, rev|log_tokens) = {pearson_rev_partial:.4f}"
    )

    # Length-bin analysis: deciles of log_tokens, then spearman within each decile
    sorted_idx = sorted(range(len(valid_rows)), key=lambda i: n_tokens_list[i])
    n_v = len(valid_rows)
    bins = 5
    bin_size = n_v // bins
    bin_rhos = []
    bin_info = []
    for b in range(bins):
        lo = b * bin_size
        hi = (b + 1) * bin_size if b < bins - 1 else n_v
        idxs = sorted_idx[lo:hi]
        a_b = [alphas[i] for i in idxs]
        r_b = [rev_orders[i] for i in idxs]
        nt = [n_tokens_list[i] for i in idxs]
        rho_b = spearman_rho(a_b, r_b) if len(a_b) >= 3 else 0.0
        bin_rhos.append(rho_b)
        bin_info.append({
            "bin": b,
            "n": len(idxs),
            "n_tokens_range": [min(nt), max(nt)],
            "mean_alpha": sum(a_b) / len(a_b),
            "spearman_rho_alpha_revorder": rho_b,
        })
        print(
            f"  bin {b}: n={len(idxs)} tokens {min(nt)}-{max(nt)} "
            f"mean_alpha={sum(a_b)/len(a_b):.4f} rho={rho_b:.4f}"
        )

    # Phase means
    phase_order = ["Early Meccan", "Middle Meccan", "Late Meccan", "Medinan"]
    by_phase = defaultdict(list)
    for r in valid_rows:
        by_phase[r["noldeke_phase"]].append(r["zipf_alpha"])
    phase_means = {}
    for p in phase_order:
        xs = by_phase.get(p, [])
        if xs:
            phase_means[p] = {
                "n": len(xs),
                "mean_alpha": sum(xs) / len(xs),
                "min": min(xs),
                "max": max(xs),
            }
        else:
            phase_means[p] = {"n": 0, "mean_alpha": None}

    # Meccan/Medinan means
    mec_alphas = [r["zipf_alpha"] for r in valid_rows if r["period"] == "Meccan"]
    med_alphas = [r["zipf_alpha"] for r in valid_rows if r["period"] == "Medinan"]
    period_means = {
        "Meccan": {
            "n": len(mec_alphas),
            "mean_alpha": sum(mec_alphas) / len(mec_alphas) if mec_alphas else None,
            "sd_alpha": (
                math.sqrt(
                    sum(
                        (a - sum(mec_alphas) / len(mec_alphas)) ** 2
                        for a in mec_alphas
                    )
                    / (len(mec_alphas) - 1)
                )
                if len(mec_alphas) > 1
                else None
            ),
        },
        "Medinan": {
            "n": len(med_alphas),
            "mean_alpha": sum(med_alphas) / len(med_alphas) if med_alphas else None,
            "sd_alpha": (
                math.sqrt(
                    sum(
                        (a - sum(med_alphas) / len(med_alphas)) ** 2
                        for a in med_alphas
                    )
                    / (len(med_alphas) - 1)
                )
                if len(med_alphas) > 1
                else None
            ),
        },
    }

    # Extremes
    sorted_by_alpha = sorted(valid_rows, key=lambda r: r["zipf_alpha"], reverse=True)
    top_alpha = sorted_by_alpha[:10]
    bot_alpha = sorted_by_alpha[-10:][::-1]

    # Write CSV
    csv_path = OUT_DIR / "zipf-per-surah.csv"
    fieldnames = [
        "mushaf_order",
        "name_tl",
        "period",
        "revelation_order",
        "noldeke_order",
        "noldeke_phase",
        "n_lemma_tokens",
        "n_distinct_lemmas",
        "zipf_alpha",
        "r_squared",
        "boot_alpha_lo",
        "boot_alpha_hi",
        "boot_alpha_median",
        "status",
    ]
    with csv_path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in fieldnames})

    # Write JSON summary
    results = {
        "n_valid_surahs": len(valid_rows),
        "n_insufficient_surahs": len(rows) - len(valid_rows),
        "min_distinct_lemmas_threshold": MIN_DISTINCT_LEMMAS,
        "whole_quran_zipf": {
            "alpha": whole_fit["alpha"],
            "r2": whole_fit["r2"],
            "n_distinct_lemmas": whole_fit["n"],
            "n_lemma_tokens": total_tokens,
        },
        "correlations": {
            "spearman_rho_alpha_revelation_order": rho_rev,
            "spearman_rho_alpha_noldeke_order": rho_nold,
            "spearman_rho_alpha_n_tokens": rho_tokens,
            "spearman_rho_alpha_n_distinct": rho_distinct,
            "point_biserial_medinan_alpha": pb_medinan,
            "partial_spearman_alpha_revorder_given_logtokens": rho_rev_partial,
            "partial_pearson_alpha_revorder_given_logtokens": pearson_rev_partial,
            "perm_p_rho_revelation": p_rev,
            "perm_p_rho_noldeke": p_nold,
            "n_perm": N_PERM,
        },
        "length_bins": bin_info,
        "noldeke_phase_means": phase_means,
        "period_means": period_means,
        "top10_alpha": [
            {
                "mushaf_order": r["mushaf_order"],
                "name_tl": r["name_tl"],
                "period": r["period"],
                "revelation_order": r["revelation_order"],
                "n_distinct_lemmas": r["n_distinct_lemmas"],
                "zipf_alpha": r["zipf_alpha"],
                "r_squared": r["r_squared"],
                "boot_95ci": [r["boot_alpha_lo"], r["boot_alpha_hi"]],
            }
            for r in top_alpha
        ],
        "bot10_alpha": [
            {
                "mushaf_order": r["mushaf_order"],
                "name_tl": r["name_tl"],
                "period": r["period"],
                "revelation_order": r["revelation_order"],
                "n_distinct_lemmas": r["n_distinct_lemmas"],
                "zipf_alpha": r["zipf_alpha"],
                "r_squared": r["r_squared"],
                "boot_95ci": [r["boot_alpha_lo"], r["boot_alpha_hi"]],
            }
            for r in bot_alpha
        ],
        "seed": SEED,
        "n_bootstrap": N_BOOTSTRAP,
    }

    json_path = OUT_DIR / "zipf-per-surah-results.json"
    with json_path.open("w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, ensure_ascii=False)

    print(f"\nWrote: {csv_path}")
    print(f"Wrote: {json_path}")

    # Print headline verdict
    print()
    print("Period means:")
    for k, v in period_means.items():
        print(f"  {k}: n={v['n']} mean_alpha={v['mean_alpha']:.4f}")
    print("Noldeke phase means:")
    for p in phase_order:
        pm = phase_means[p]
        if pm["n"]:
            print(f"  {p}: n={pm['n']} mean_alpha={pm['mean_alpha']:.4f}")
    print("Top 5 alpha (most concentrated):")
    for r in top_alpha[:5]:
        print(
            f"  #{r['mushaf_order']:3d} {r['name_tl']:20s} "
            f"period={r['period']:7s} alpha={r['zipf_alpha']:.3f} "
            f"(CI {r['boot_alpha_lo']:.3f}-{r['boot_alpha_hi']:.3f}) "
            f"n_distinct={r['n_distinct_lemmas']}"
        )
    print("Bottom 5 alpha (flattest):")
    for r in bot_alpha[:5]:
        print(
            f"  #{r['mushaf_order']:3d} {r['name_tl']:20s} "
            f"period={r['period']:7s} alpha={r['zipf_alpha']:.3f} "
            f"(CI {r['boot_alpha_lo']:.3f}-{r['boot_alpha_hi']:.3f}) "
            f"n_distinct={r['n_distinct_lemmas']}"
        )


if __name__ == "__main__":
    main()
