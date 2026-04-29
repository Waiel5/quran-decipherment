#!/usr/bin/env python3
"""H-NEW-620 — Divine-name density as candidate 6th cohesion factor.

Tests whether per-subset divine-name density features (within-subset
coefficient-of-variation + mean) predict residual content-cohesion %ile
beyond the cross-finding-024 5-factor model.

Pre-reg: findings/phase-b-hypotheses/h-new-620-divine-name-density-prereg.md
Pre-reg SHA256: 73dfb7f5e48c6ea3ec72db82b00fb6add51fe457526f6c2da80b37bc32c1034c

Seed: 20260501
Bonferroni k=3, α_bon = 0.01667.
Three gates:
  1) ΔR²(B - A) > 0.05
  2) Permutation p on ΔR² ≤ 0.01667
  3) β(dn_variance) > 0  (pre-committed direction)

Rules tuple:
  no-tashkeel; whitespace-tokenized; CORE-DN list locked in pre-reg;
  proclitic-strip ∈ {و, ف, ب, ل, ك, س, فب, وب, فل, ول, وس, فس};
  per-surah density = #DN-occurrences / #words; 12 training subsets locked.
"""
import hashlib
import json
import math
import random
import sys
from pathlib import Path
from itertools import combinations

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-620-divine-name-density-prereg.md"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
ASMA_TXT = ROOT / "data/asma-al-husna.txt"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-620.json"

SEED = 20260501
N_PERM = 10000
BONF_K = 3
ALPHA_BON = 0.05 / BONF_K  # 0.01667
EXPECTED_PREREG_SHA = "73dfb7f5e48c6ea3ec72db82b00fb6add51fe457526f6c2da80b37bc32c1034c"

# ---------- CORE-DN list (locked) ----------
CORE_DN_FORMS = [
    "الله", "الرحمن", "الرحيم",
    "رب", "ربك", "ربكم", "ربنا", "ربه", "ربها", "ربهم", "ربي",
    "الإله",  # mapped to الله
]
ALIAS_MAP = {"الإله": "الله"}

PROCLITIC_PREFIXES = [
    "و", "ف", "ب", "ل", "ك", "س",
    "فب", "وب", "فل", "ول", "وس", "فس",
]

# ---------- 12 training subsets (locked from cross-finding-024 §3) ----------
SUBSETS = [
    {"rank": 1,  "name": "Q 107-114 terminal-tail",      "surahs": list(range(107, 115)), "pct": 0.0,
     "block": 1, "register": 1, "chrono": 1, "formula": 0, "no_outlier": 1},
    {"rank": 2,  "name": "Q 98-114 terminal-17",         "surahs": list(range(98, 115)),  "pct": 0.0,
     "block": 1, "register": 1, "chrono": 1, "formula": 0, "no_outlier": 1},
    {"rank": 3,  "name": "Medinan half Q 57-66",         "surahs": list(range(57, 67)),   "pct": 4.8,
     "block": 1, "register": 1, "chrono": 1, "formula": 0, "no_outlier": 1},
    {"rank": 4,  "name": "Mufaṣṣal-awsāṭ Q 67-77",        "surahs": list(range(67, 78)),   "pct": 7.1,
     "block": 1, "register": 1, "chrono": 1, "formula": 0, "no_outlier": 1},
    {"rank": 5,  "name": "Musabbiḥāt block-subset",      "surahs": [57, 59, 61, 62, 64],   "pct": 8.1,
     "block": 1, "register": 1, "chrono": 1, "formula": 1, "no_outlier": 1},
    {"rank": 6,  "name": "Ṭiwāl Q 2-9",                  "surahs": list(range(2, 10)),    "pct": 17.3,
     "block": 1, "register": 0, "chrono": 0, "formula": 0, "no_outlier": 1},
    {"rank": 7,  "name": "Ḥawāmīm 5-6",                  "surahs": [40, 41, 42, 43, 44, 45], "pct": 21.5,
     "block": 1, "register": 0, "chrono": 1, "formula": 1, "no_outlier": 1},
    {"rank": 8,  "name": "Musabbiḥāt Q 50-56 minus Q 55", "surahs": [50, 51, 52, 53, 54, 56], "pct": 37.5,
     "block": 1, "register": 0, "chrono": 1, "formula": 0, "no_outlier": 1},
    {"rank": 9,  "name": "Mufaṣṣal-ṭiwāl Q 50-66",        "surahs": list(range(50, 67)),   "pct": 50.1,
     "block": 1, "register": 0, "chrono": 0, "formula": 0, "no_outlier": 0},
    {"rank": 10, "name": "Meccan half Q 50-56",          "surahs": list(range(50, 57)),   "pct": 70.1,
     "block": 1, "register": 0, "chrono": 1, "formula": 0, "no_outlier": 0},
    {"rank": 11, "name": "al-Ḥāmidāt",                   "surahs": [1, 6, 18, 34, 35],     "pct": 75.0,
     "block": 0, "register": 0, "chrono": 0, "formula": 1, "no_outlier": 1},
    {"rank": 12, "name": "Q 1 + Q 27 Basmala-pair",      "surahs": [1, 27],                "pct": 81.0,
     "block": 0, "register": 0, "chrono": 0, "formula": 1, "no_outlier": 1},
]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_corpus():
    with open(QURAN_JSON, encoding="utf-8") as f:
        return json.load(f)


def load_full_dn():
    names = []
    with open(ASMA_TXT, encoding="utf-8") as f:
        for line in f:
            ln = line.strip()
            if not ln or ln.startswith("#"):
                continue
            names.append(ln)
    return names


def word_matches_form(word: str, form: str) -> bool:
    """Exact match or proclitic-prefix + form == word."""
    if word == form:
        return True
    for pre in PROCLITIC_PREFIXES:
        if word == pre + form:
            return True
    return False


def count_core_dn_in_words(words):
    """Count CORE-DN occurrences in a token list. Apply alias-mapping."""
    counts = {}
    for w in words:
        for form in CORE_DN_FORMS:
            if word_matches_form(w, form):
                key = ALIAS_MAP.get(form, form)
                counts[key] = counts.get(key, 0) + 1
                break  # first-match wins; forms are non-overlapping by construction
    return counts


def count_full_dn_in_text(words, text, full_names):
    """Count FULL-DN list occurrences. Single-word names use word_matches_form;
    multi-word names use whitespace-bounded substring on the joined text."""
    total = 0
    for name in full_names:
        if " " in name:
            target = " " + name + " "
            haystack = " " + " ".join(words) + " "
            i = 0
            while True:
                p = haystack.find(target, i)
                if p == -1:
                    break
                total += 1
                i = p + 1
        else:
            for w in words:
                if word_matches_form(w, name):
                    total += 1
    return total


def compute_per_surah(corpus, full_names):
    """Returns dict surah_id → {core_dn, full_dn, words, core_density, full_density}."""
    per = {}
    for s in corpus:
        sid = s["id"]
        all_words = []
        for v in s["verses"]:
            all_words.extend(v["text"].split())
        # Tatweel / non-Arabic-letter cleanup not applied; corpus is pre-cleaned.
        wcount = len(all_words)
        core_counts = count_core_dn_in_words(all_words)
        core_total = sum(core_counts.values())
        full_total = count_full_dn_in_text(all_words, " ".join(all_words), full_names)
        per[sid] = {
            "words": wcount,
            "core_dn": core_total,
            "core_dn_breakdown": core_counts,
            "full_dn": full_total,
            "core_density": core_total / wcount if wcount else 0.0,
            "full_density": full_total / wcount if wcount else 0.0,
        }
    return per


def subset_dn_features(per_surah, subset_surahs, key="core_density"):
    """Return (mean, cv) where cv = stddev / mean (population stddev). 0 if mean=0."""
    vals = [per_surah[s][key] for s in subset_surahs]
    n = len(vals)
    mu = sum(vals) / n
    if n < 2:
        return mu, 0.0
    var = sum((v - mu) ** 2 for v in vals) / n
    sd = math.sqrt(var)
    cv = sd / mu if mu > 0 else 0.0
    return mu, cv


# ---------- OLS via numpy if available; fallback to pure-Python ----------
def ols_r2(X, y):
    """Compute OLS R². X is N×P design matrix (with intercept column), y is length-N."""
    import numpy as np
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    yhat = X @ beta
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return r2, beta.tolist()


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-620 (Divine-name density as 6th cohesion factor) ===")
    print(f"Pre-reg: {PREREG.name}")
    print(f"Pre-reg SHA256: {prereg_sha}")
    if prereg_sha != EXPECTED_PREREG_SHA:
        print(f"WARNING: pre-reg SHA mismatch! expected {EXPECTED_PREREG_SHA}", file=sys.stderr)
        # Hard stop because the run-script's gates depend on the exact pre-reg.
        sys.exit(1)
    print(f"Seed: {SEED}; perms: {N_PERM}; α_bon: {ALPHA_BON:.5f}\n")

    corpus = load_corpus()
    assert len(corpus) == 114
    full_names = load_full_dn()
    assert len(full_names) == 99, f"Expected 99 names, got {len(full_names)}"
    print(f"Corpus: {len(corpus)} surahs; FULL-DN list: {len(full_names)} names")

    print("\n--- Per-surah DN density (core list) ---")
    per_surah = compute_per_surah(corpus, full_names)
    # Sort by density for descriptive top-10/bottom-10
    sorted_by_core = sorted(per_surah.items(), key=lambda kv: kv[1]["core_density"], reverse=True)
    print("Top-10 surahs by core_density:")
    for sid, info in sorted_by_core[:10]:
        print(f"   Q {sid:3d}: density={info['core_density']:.4f}  core_dn={info['core_dn']:4d}  words={info['words']:5d}")
    print("Bottom-10 surahs by core_density:")
    for sid, info in sorted_by_core[-10:]:
        print(f"   Q {sid:3d}: density={info['core_density']:.4f}  core_dn={info['core_dn']:4d}  words={info['words']:5d}")

    # ---------- Compute per-subset features ----------
    print("\n--- Per-subset DN-density features ---")
    print(f"{'Rank':>4} {'Pct':>6} {'N':>3} {'core_mean':>10} {'core_cv':>8} {'full_mean':>10} {'full_cv':>8}  Subset")
    for sub in SUBSETS:
        mu_c, cv_c = subset_dn_features(per_surah, sub["surahs"], key="core_density")
        mu_f, cv_f = subset_dn_features(per_surah, sub["surahs"], key="full_density")
        sub["core_mean"] = mu_c
        sub["core_cv"] = cv_c
        sub["full_mean"] = mu_f
        sub["full_cv"] = cv_f
        print(f"{sub['rank']:>4} {sub['pct']:>6.1f} {len(sub['surahs']):>3d} "
              f"{mu_c:>10.5f} {cv_c:>8.4f} {mu_f:>10.5f} {cv_f:>8.4f}  {sub['name']}")

    # ---------- Build design matrices ----------
    y = [s["pct"] for s in SUBSETS]
    X_A = [[1.0, s["block"], s["register"], s["chrono"], s["formula"], s["no_outlier"]] for s in SUBSETS]
    X_B = [[1.0, s["block"], s["register"], s["chrono"], s["formula"], s["no_outlier"],
            s["core_cv"], s["core_mean"]] for s in SUBSETS]

    r2_A, beta_A = ols_r2(X_A, y)
    r2_B, beta_B = ols_r2(X_B, y)
    delta_r2 = r2_B - r2_A
    print(f"\n--- Regression results ---")
    print(f"Model A R²            = {r2_A:.5f}")
    print(f"Model B R² (5+core_cv+core_mean) = {r2_B:.5f}")
    print(f"ΔR² (B − A)           = {delta_r2:.5f}")
    print(f"Model A betas        = [intercept, block, register, chrono, formula, no_outlier]")
    print(f"                       {[round(b,3) for b in beta_A]}")
    print(f"Model B betas        = [intercept, block, register, chrono, formula, no_outlier, dn_cv, dn_mean]")
    print(f"                       {[round(b,3) for b in beta_B]}")
    beta_dn_cv = beta_B[6]
    beta_dn_mean = beta_B[7]
    print(f"β(dn_variance/cv)    = {beta_dn_cv:+.4f}  (pre-committed sign: POSITIVE)")
    print(f"β(dn_mean)           = {beta_dn_mean:+.4f}  (exploratory)")

    # ---------- Permutation test on ΔR² ----------
    print(f"\n--- Permutation test on ΔR² (n={N_PERM}, seed={SEED}) ---")
    rng = random.Random(SEED)
    pairs = [(s["core_cv"], s["core_mean"]) for s in SUBSETS]
    n_subsets = len(SUBSETS)
    null_deltas = []
    perm_ge = 0
    for _ in range(N_PERM):
        perm_idx = list(range(n_subsets))
        rng.shuffle(perm_idx)
        X_B_perm = []
        for i, s in enumerate(SUBSETS):
            cv_p, mu_p = pairs[perm_idx[i]]
            X_B_perm.append([1.0, s["block"], s["register"], s["chrono"], s["formula"], s["no_outlier"], cv_p, mu_p])
        r2_perm, _ = ols_r2(X_B_perm, y)
        d_perm = r2_perm - r2_A
        null_deltas.append(d_perm)
        if d_perm >= delta_r2:
            perm_ge += 1
    perm_p = perm_ge / N_PERM
    null_deltas.sort()
    print(f"  ΔR²_obs = {delta_r2:.5f}")
    print(f"  Null mean = {sum(null_deltas)/len(null_deltas):.5f}, null max = {null_deltas[-1]:.5f}, null p95 = {null_deltas[int(0.95*N_PERM)]:.5f}")
    print(f"  Permutation p (one-sided ΔR²_perm ≥ ΔR²_obs) = {perm_p:.5f}")

    # ---------- Bonferroni gates ----------
    gate1 = delta_r2 > 0.05
    gate2 = perm_p <= ALPHA_BON
    gate3 = beta_dn_cv > 0
    h1_pass = gate1 and gate2 and gate3
    print(f"\n--- Bonferroni gates (α_bon = {ALPHA_BON:.5f}) ---")
    print(f"  Gate 1: ΔR² > 0.05            -> {gate1}  (ΔR² = {delta_r2:.5f})")
    print(f"  Gate 2: perm p ≤ {ALPHA_BON:.5f}     -> {gate2}  (p = {perm_p:.5f})")
    print(f"  Gate 3: β(dn_variance) > 0    -> {gate3}  (β = {beta_dn_cv:+.5f})")
    print(f"  AGGREGATE H1 (6th-factor): {'PASS' if h1_pass else 'NULL'}")

    # ---------- Spearman descriptive ----------
    print("\n--- Spearman ρ: per-surah core_density vs inherited cohesion-rank ---")
    surah_pct = {}
    for sub in SUBSETS:
        for sid in sub["surahs"]:
            if sid not in surah_pct:
                surah_pct[sid] = sub["pct"]  # first subset in list (by rank order) wins
    densities, pcts = [], []
    for sid, p in surah_pct.items():
        densities.append(per_surah[sid]["core_density"])
        pcts.append(p)
    n = len(densities)

    def spearman(x, y):
        n = len(x)
        rx = [r + 1 for r in sorted(range(n), key=lambda i: x[i])]
        ry = [r + 1 for r in sorted(range(n), key=lambda i: y[i])]
        # convert sort-indices to ranks
        rank_x = [0] * n
        rank_y = [0] * n
        sx = sorted(range(n), key=lambda i: x[i])
        for r, i in enumerate(sx, start=1):
            rank_x[i] = r
        sy = sorted(range(n), key=lambda i: y[i])
        for r, i in enumerate(sy, start=1):
            rank_y[i] = r
        mx = sum(rank_x) / n
        my = sum(rank_y) / n
        num = sum((rank_x[i] - mx) * (rank_y[i] - my) for i in range(n))
        dx = math.sqrt(sum((rank_x[i] - mx) ** 2 for i in range(n)))
        dy = math.sqrt(sum((rank_y[i] - my) ** 2 for i in range(n)))
        return num / (dx * dy) if dx * dy > 0 else 0.0

    rho = spearman(densities, pcts)
    print(f"  N (covered surahs) = {n}; Spearman ρ = {rho:+.4f}  (descriptive only)")

    # ---------- Save JSON ----------
    out = {
        "id": "H-NEW-620",
        "title": "Divine-name density as candidate 6th cohesion factor",
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONF_K,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel; whitespace-tokenized; CORE-DN locked; proclitic-strip ∈ {و, ف, ب, ل, ك, س, +bigrams}; mushaf 114; 12 training subsets locked from cross-finding-024 §3)",
        "core_dn_forms": CORE_DN_FORMS,
        "alias_map": ALIAS_MAP,
        "subsets": SUBSETS,
        "per_surah_density": {sid: per_surah[sid] for sid in sorted(per_surah)},
        "model_A": {"r2": r2_A, "betas": beta_A,
                    "design_columns": ["intercept","block","register","chrono","formula","no_outlier"]},
        "model_B": {"r2": r2_B, "betas": beta_B,
                    "design_columns": ["intercept","block","register","chrono","formula","no_outlier","dn_cv","dn_mean"]},
        "delta_r2": delta_r2,
        "perm_p": perm_p,
        "perm_null_summary": {
            "n": N_PERM,
            "mean": sum(null_deltas)/len(null_deltas),
            "min": null_deltas[0],
            "max": null_deltas[-1],
            "p95": null_deltas[int(0.95*N_PERM)],
            "p99": null_deltas[int(0.99*N_PERM)],
        },
        "gates": {
            "gate1_delta_r2_gt_005": gate1,
            "gate2_perm_p_le_alpha_bon": gate2,
            "gate3_beta_dn_cv_positive": gate3,
            "aggregate_h1_pass": h1_pass,
        },
        "spearman_descriptive": {
            "n": n,
            "rho_per_surah_core_density_vs_inherited_pct": rho,
        },
        "verdict": "6TH-FACTOR CONFIRMED" if h1_pass else "NULL — 5-factor model TERMINAL",
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUT_JSON}")
    print(f"\n=== VERDICT: {out['verdict']} ===")
    return out


if __name__ == "__main__":
    main()
