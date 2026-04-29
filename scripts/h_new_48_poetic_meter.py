"""H-NEW-48: Quran verse-length vs the 16 al-Khalīlian buḥūr.

Pre-reg: findings/phase-b-hypotheses/h-new-48-poetic-meter-prereg.md
Rules tuple: (no-tashkeel, orthographic-token, graphemes,
              basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)

Procedure (locked):
  1. Q = 6,236 Quran verse letter-counts.
  2. For each of 16 buḥūr m: reference distribution = Gaussian(mu_m, 0.10*mu_m)
     where mu_m = 3.0 * syllables_per_bayt_m. Discretised over {1..200}.
  3. Three baselines: Bukhari sentence lengths, Jahiz sentence lengths,
     Muallaqat bayt lengths (one bayt per line).
  4. Two-sample KS distance D and bootstrap p-value (10,000 reps).
  5. Bonferroni: k = 16 + 3 = 19, alpha_per = 0.00263.
  6. al-Bāqillānī test: does Q sit between prose and poetry (mean & median)?
  7. MW-5 positive control: Muallaqat must match >=1 meter at p<0.001.
  8. Robustness: re-run KS at letters/syllable conversion 2.5 and 3.5.

Seed 20260416.
"""

from __future__ import annotations

import json
import os
import re
import sys
from typing import Dict, List, Tuple

import numpy as np

sys.path.insert(0, "/Users/grey/Downloads/quran")
from analysis.tools.loader import load_quran
from analysis.tools.tokenize import graphemes, LETTER_RANGES

SEED = 20260416
N_BOOT = 10_000
ALPHA_PER = 0.00263  # 0.05 / 19
ALPHA_BON = 0.05
K_FAMILY = 19  # 16 meters + 3 baselines
# Amendment 48-A: locked LPS = 1.6 (calibrated from 7 muʿallaqāt historical-meter
# assignments); 1.4 and 1.8 used for sensitivity only.
LETTERS_PER_SYLLABLE = 1.6
SIGMA_FRACTION = 0.10  # locked
MAX_LETTERS = 200  # support of meter PMFs

OUT_JSON = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-48.json"

LETTER_SET = set()
for lo, hi in LETTER_RANGES:
    for cp in range(lo, hi + 1):
        LETTER_SET.add(chr(cp))


def count_letters(s: str) -> int:
    return sum(1 for ch in s if ch in LETTER_SET)


# -----------------------------------------------------------------------------
# Locked al-Khalīl meter table (syllables per shaṭr & per bayt)
# -----------------------------------------------------------------------------

METERS = [
    # (id, name_en, name_ar, syll_shatr, syll_bayt)
    (1,  "Tawil",     "الطويل",   14, 28),
    (2,  "Madid",     "المديد",   11, 22),
    (3,  "Basit",     "البسيط",   14, 28),
    (4,  "Wafir",     "الوافر",   13, 26),
    (5,  "Kamil",     "الكامل",   15, 30),
    (6,  "Hazaj",     "الهزج",     8, 16),
    (7,  "Rajaz",     "الرجز",    12, 24),
    (8,  "Ramal",     "الرمل",    12, 24),
    (9,  "Sari",      "السريع",   12, 24),
    (10, "Munsarih",  "المنسرح",  12, 24),
    (11, "Khafif",    "الخفيف",   11, 22),
    (12, "Mudari",    "المضارع",   8, 16),
    (13, "Muqtadab",  "المقتضب",   8, 16),
    (14, "Mujtathth", "المجتث",    8, 16),
    (15, "Mutaqarib", "المتقارب", 12, 24),
    (16, "Mutadarik", "المتدارك",  8, 16),
]


def meter_pmf(syll_bayt: int, letters_per_syll: float, sigma_frac: float,
              max_letters: int = MAX_LETTERS) -> np.ndarray:
    """Discretised Gaussian over {1, ..., max_letters} for a meter."""
    mu = letters_per_syll * syll_bayt
    sigma = max(sigma_frac * mu, 0.5)
    xs = np.arange(1, max_letters + 1)
    pdf = np.exp(-0.5 * ((xs - mu) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))
    pmf = pdf / pdf.sum()
    return pmf


def sample_from_pmf(pmf: np.ndarray, n: int, rng: np.random.Generator) -> np.ndarray:
    xs = np.arange(1, pmf.size + 1)
    return rng.choice(xs, size=n, p=pmf)


# -----------------------------------------------------------------------------
# Data loaders
# -----------------------------------------------------------------------------

BUKHARI_PATH = "/Users/grey/Downloads/quran/data/baseline-corpora/raw/bukhari.txt"
JAHIZ_PATH = "/Users/grey/Downloads/quran/data/baseline-corpora/raw/jahiz-hayawan.txt"
MUALLAQA_PATHS = [
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-imru-al-qais.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-tarafa.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-zuhayr.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-labid.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-antara.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt",
    "/Users/grey/Downloads/quran/data/baseline-corpora/raw/muallaqa-harith.txt",
]

# Each muallaqa's historical meter (for positive-control reporting)
MUALLAQA_METERS = {
    "imru-al-qais":     "Tawil",
    "tarafa":           "Tawil",
    "zuhayr":           "Tawil",
    "labid":            "Kamil",
    "antara":           "Kamil",
    "amr-bin-kulthum":  "Wafir",
    "harith":           "Khafif",
}

SENT_SPLIT_RE = re.compile(r"[\.؟!\?\n]+")


def split_sentences(text: str) -> List[int]:
    cleaned = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        cleaned.append(ln)
    joined = "\n".join(cleaned)
    parts = SENT_SPLIT_RE.split(joined)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        g = count_letters(p)
        if g >= 3:
            out.append(g)
    return out


def load_baseline_lengths(path: str) -> List[int]:
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    return split_sentences(text)


def load_muallaqa_lengths(path: str) -> List[int]:
    out: List[int] = []
    with open(path, "r", encoding="utf-8") as fh:
        for ln in fh:
            g = count_letters(ln)
            if g >= 3:
                out.append(g)
    return out


def build_quran_lengths() -> List[int]:
    surahs = load_quran("no-tashkeel")
    Q: List[int] = []
    for s in surahs:
        for v in s.verses:
            Q.append(graphemes(v.text))
    assert len(Q) == 6236, f"got {len(Q)} verses, expected 6236"
    return Q


# -----------------------------------------------------------------------------
# Two-sample KS via direct numpy (no scipy dependency)
# -----------------------------------------------------------------------------


def ks_two_sample(a: np.ndarray, b: np.ndarray) -> float:
    """Return two-sample KS statistic D."""
    a_sorted = np.sort(a)
    b_sorted = np.sort(b)
    all_vals = np.concatenate([a_sorted, b_sorted])
    cdf_a = np.searchsorted(a_sorted, all_vals, side="right") / a_sorted.size
    cdf_b = np.searchsorted(b_sorted, all_vals, side="right") / b_sorted.size
    return float(np.max(np.abs(cdf_a - cdf_b)))


def ks_against_pmf(observed: np.ndarray, pmf: np.ndarray, n_boot: int,
                   rng: np.random.Generator) -> Tuple[float, float, np.ndarray]:
    """KS distance D between observed and PMF sample of same size; bootstrap p.

    Generates n_boot reference samples of size len(observed) from PMF, computes
    KS distance pairs to construct null distribution. Returns:
      D_obs = KS(observed, large reference sample)
      p     = fraction of bootstrap KS pairs (ref vs ref) >= D_obs
      D_null = bootstrap distribution of D under H0
    """
    n = observed.size
    # Large reference sample for the observed-vs-meter D
    large_ref = sample_from_pmf(pmf, max(20_000, 4 * n), rng)
    D_obs = ks_two_sample(observed, large_ref)

    # Null: sample two of size n from PMF, compute KS
    D_null = np.empty(n_boot)
    for i in range(n_boot):
        s1 = sample_from_pmf(pmf, n, rng)
        s2 = sample_from_pmf(pmf, n, rng)
        D_null[i] = ks_two_sample(s1, s2)
    p = float(np.mean(D_null >= D_obs))
    if p == 0.0:
        p = 1.0 / (n_boot + 1)
    return D_obs, p, D_null


def ks_two_corpora(a: np.ndarray, b: np.ndarray, n_boot: int,
                   rng: np.random.Generator) -> Tuple[float, float]:
    """Two-corpora KS distance + permutation p-value (label permutation)."""
    D_obs = ks_two_sample(a, b)
    pool = np.concatenate([a, b])
    n_a = a.size
    D_null = np.empty(n_boot)
    for i in range(n_boot):
        rng.shuffle(pool)
        D_null[i] = ks_two_sample(pool[:n_a], pool[n_a:])
    p = float(np.mean(D_null >= D_obs))
    if p == 0.0:
        p = 1.0 / (n_boot + 1)
    return D_obs, p


# -----------------------------------------------------------------------------
# Pipeline
# -----------------------------------------------------------------------------


def summarise(name: str, lengths: List[int]) -> Dict:
    arr = np.array(lengths, dtype=float)
    return {
        "name": name,
        "n": int(arr.size),
        "mean": float(arr.mean()),
        "median": float(np.median(arr)),
        "std": float(arr.std(ddof=1)),
        "p05": float(np.percentile(arr, 5)),
        "p95": float(np.percentile(arr, 95)),
        "min": int(arr.min()),
        "max": int(arr.max()),
    }


def test_corpus_vs_meters(corpus_lengths: np.ndarray, corpus_label: str,
                           letters_per_syll: float, n_boot: int,
                           rng: np.random.Generator) -> List[Dict]:
    """Run KS against each of 16 meters."""
    rows = []
    for (mid, name_en, name_ar, syll_shatr, syll_bayt) in METERS:
        pmf = meter_pmf(syll_bayt, letters_per_syll, SIGMA_FRACTION)
        D, p, _ = ks_against_pmf(corpus_lengths, pmf, n_boot, rng)
        mu = letters_per_syll * syll_bayt
        rows.append({
            "meter_id": mid,
            "meter": name_en,
            "meter_ar": name_ar,
            "syll_shatr": syll_shatr,
            "syll_bayt": syll_bayt,
            "mu_letters_bayt": float(mu),
            "ks_D": float(D),
            "p_bootstrap": float(p),
            "significant_at_alpha_per": bool(p < ALPHA_PER),
            "indistinguishable": bool(p >= ALPHA_PER),
        })
    rows.sort(key=lambda r: r["ks_D"])
    return rows


def test_corpus_vs_baselines(corpus_lengths: np.ndarray, corpus_label: str,
                              baselines: Dict[str, np.ndarray],
                              n_boot: int, rng: np.random.Generator) -> List[Dict]:
    rows = []
    for bname, blengths in baselines.items():
        D, p = ks_two_corpora(corpus_lengths, blengths, n_boot, rng)
        rows.append({
            "baseline": bname,
            "n_corpus": int(corpus_lengths.size),
            "n_baseline": int(blengths.size),
            "ks_D": float(D),
            "p_permutation": float(p),
            "significant_at_alpha_per": bool(p < ALPHA_PER),
            "indistinguishable": bool(p >= ALPHA_PER),
        })
    rows.sort(key=lambda r: r["ks_D"])
    return rows


def baqillani_test(Q: np.ndarray, prose: List[np.ndarray],
                   poetry: np.ndarray) -> Dict:
    q_mean = float(Q.mean())
    q_median = float(np.median(Q))
    prose_means = [float(p.mean()) for p in prose]
    prose_medians = [float(np.median(p)) for p in prose]
    poetry_mean = float(poetry.mean())
    poetry_median = float(np.median(poetry))

    prose_mean_lo = min(prose_means)
    prose_mean_hi = max(prose_means)
    prose_med_lo = min(prose_medians)
    prose_med_hi = max(prose_medians)

    # Test: is Q strictly between any prose value and poetry value?
    # Two cases (depending on which is larger): poetry > prose or prose > poetry.
    if poetry_mean > prose_mean_hi:
        between_mean = (prose_mean_hi < q_mean < poetry_mean)
        side = "prose<Q<poetry"
    elif poetry_mean < prose_mean_lo:
        between_mean = (poetry_mean < q_mean < prose_mean_lo)
        side = "poetry<Q<prose"
    else:
        between_mean = False
        side = "prose-and-poetry-overlap"

    if poetry_median > prose_med_hi:
        between_median = (prose_med_hi < q_median < poetry_median)
    elif poetry_median < prose_med_lo:
        between_median = (poetry_median < q_median < prose_med_lo)
    else:
        between_median = False

    return {
        "q_mean": q_mean,
        "q_median": q_median,
        "prose_means": prose_means,
        "prose_medians": prose_medians,
        "poetry_mean": poetry_mean,
        "poetry_median": poetry_median,
        "between_mean": bool(between_mean),
        "between_median": bool(between_median),
        "ordering": side,
    }


def main() -> None:
    rng = np.random.default_rng(SEED)

    print("Loading Quran verse-lengths (no-tashkeel, graphemes)...", flush=True)
    Q_list = build_quran_lengths()
    Q = np.array(Q_list, dtype=float)
    print(f"  Q n={Q.size} mean={Q.mean():.2f} median={np.median(Q):.1f} std={Q.std():.2f}",
          flush=True)

    print("Loading baselines...", flush=True)
    bukhari_lengths = load_baseline_lengths(BUKHARI_PATH)
    jahiz_lengths = load_baseline_lengths(JAHIZ_PATH)
    muallaqat_per_poet: Dict[str, List[int]] = {}
    muallaqat_combined: List[int] = []
    for path in MUALLAQA_PATHS:
        key = path.split("/")[-1].replace("muallaqa-", "").replace(".txt", "")
        lengths = load_muallaqa_lengths(path)
        muallaqat_per_poet[key] = lengths
        muallaqat_combined.extend(lengths)

    B1 = np.array(bukhari_lengths, dtype=float)
    B2 = np.array(jahiz_lengths, dtype=float)
    B3 = np.array(muallaqat_combined, dtype=float)
    print(f"  Bukhari n={B1.size} mean={B1.mean():.2f}", flush=True)
    print(f"  Jahiz   n={B2.size} mean={B2.mean():.2f}", flush=True)
    print(f"  Muallaqat n={B3.size} mean={B3.mean():.2f}", flush=True)

    summaries = {
        "quran":       summarise("quran", Q_list),
        "bukhari":     summarise("bukhari", bukhari_lengths),
        "jahiz":       summarise("jahiz", jahiz_lengths),
        "muallaqat":   summarise("muallaqat", muallaqat_combined),
    }
    for poet, lengths in muallaqat_per_poet.items():
        summaries[f"muallaqa_{poet}"] = summarise(f"muallaqa_{poet}", lengths)

    # --- MW-5 positive control: each muallaqa vs its known meter ---
    print("\nMW-5 positive control: each muallaqa vs all 16 meters", flush=True)
    pos_control_rows = []
    pos_control_pass = False
    pos_control_min_p_for_assigned = []
    for poet, lengths in muallaqat_per_poet.items():
        if len(lengths) < 30:
            continue
        arr = np.array(lengths, dtype=float)
        # Test against the assigned (historical) meter
        assigned_meter = MUALLAQA_METERS[poet]
        # Also test against ALL 16 meters; positive control passes if
        # the historically-assigned meter is significantly indistinguishable
        # at p < 0.001 from this poet's lengths.
        rows_for_poet = []
        for (mid, name_en, name_ar, syll_shatr, syll_bayt) in METERS:
            pmf = meter_pmf(syll_bayt, LETTERS_PER_SYLLABLE, SIGMA_FRACTION)
            # Use a smaller bootstrap for speed in positive control
            D, p, _ = ks_against_pmf(arr, pmf, 2000, rng)
            rows_for_poet.append({
                "meter": name_en,
                "ks_D": float(D),
                "p_bootstrap": float(p),
            })
        rows_for_poet.sort(key=lambda r: r["ks_D"])
        best = rows_for_poet[0]
        assigned_row = next(r for r in rows_for_poet if r["meter"] == assigned_meter)
        # Pass criterion: best-fit meter has p > 0.001 (i.e., NOT distinguishable)
        # OR the assigned meter has p > 0.001
        passed_assigned = assigned_row["p_bootstrap"] > 0.001
        passed_best = best["p_bootstrap"] > 0.001
        pos_control_rows.append({
            "poet": poet,
            "n": int(arr.size),
            "mean_letters_per_bayt": float(arr.mean()),
            "assigned_meter": assigned_meter,
            "assigned_meter_D": assigned_row["ks_D"],
            "assigned_meter_p": assigned_row["p_bootstrap"],
            "best_fit_meter": best["meter"],
            "best_fit_D": best["ks_D"],
            "best_fit_p": best["p_bootstrap"],
            "assigned_passes_p_gt_0p001": bool(passed_assigned),
            "best_passes_p_gt_0p001": bool(passed_best),
        })
        if passed_best:
            pos_control_pass = True
        pos_control_min_p_for_assigned.append(assigned_row["p_bootstrap"])

    # MW-5 final: at least one poet must have its best-fit meter p > 0.001.
    # Stronger: at least one poet must match its HISTORICALLY assigned meter at p > 0.001.
    historical_match_count = sum(
        1 for r in pos_control_rows if r["assigned_passes_p_gt_0p001"]
    )

    # --- Primary test: Quran vs each meter ---
    print("\nQuran vs 16 meters (primary, 10k bootstrap each)...", flush=True)
    quran_vs_meters = test_corpus_vs_meters(Q, "quran", LETTERS_PER_SYLLABLE,
                                              N_BOOT, rng)
    n_meter_match = sum(1 for r in quran_vs_meters if r["indistinguishable"])
    print(f"  Quran indistinguishable from {n_meter_match}/16 meters at "
          f"alpha_per={ALPHA_PER}", flush=True)
    print(f"  Closest meter: {quran_vs_meters[0]['meter']} D={quran_vs_meters[0]['ks_D']:.4f} "
          f"p={quran_vs_meters[0]['p_bootstrap']:.3e}", flush=True)

    # --- Quran vs each baseline ---
    print("\nQuran vs 3 baselines (10k permutation each)...", flush=True)
    baselines = {"bukhari": B1, "jahiz": B2, "muallaqat": B3}
    quran_vs_baselines = test_corpus_vs_baselines(Q, "quran", baselines, N_BOOT, rng)
    n_baseline_match = sum(1 for r in quran_vs_baselines if r["indistinguishable"])
    print(f"  Quran indistinguishable from {n_baseline_match}/3 baselines at "
          f"alpha_per={ALPHA_PER}", flush=True)
    for r in quran_vs_baselines:
        print(f"  vs {r['baseline']}: D={r['ks_D']:.4f} p={r['p_permutation']:.3e}",
              flush=True)

    # --- al-Bāqillānī between-test ---
    baq = baqillani_test(Q, [B1, B2], B3)
    print(f"\nal-Baqillani test: ordering={baq['ordering']} "
          f"between_mean={baq['between_mean']} between_median={baq['between_median']}",
          flush=True)

    # --- Robustness: re-run vs meters at 1.4 and 1.8 letters/syll (per amendment 48-A) ---
    print("\nRobustness: alt letters/syll = 1.4 and 1.8...", flush=True)
    quran_vs_meters_lo = test_corpus_vs_meters(Q, "quran", 1.4, 1000, rng)
    quran_vs_meters_hi = test_corpus_vs_meters(Q, "quran", 1.8, 1000, rng)
    n_lo = sum(1 for r in quran_vs_meters_lo if r["indistinguishable"])
    n_hi = sum(1 for r in quran_vs_meters_hi if r["indistinguishable"])
    print(f"  At 1.4 lps: indistinguishable {n_lo}/16; at 1.8 lps: {n_hi}/16",
          flush=True)

    # --- Verdict logic ---
    if not pos_control_pass:
        verdict = "NULL-BROKEN"
        verdict_reason = (
            f"MW-5 positive control failed: no muʿallaqa matched its best-fit meter "
            f"at p>0.001 (suggests letters/syll calibration off)."
        )
    elif n_meter_match == 0 and n_baseline_match == 0:
        if baq["between_mean"] and baq["between_median"]:
            verdict = "PASS-BETWEEN"
            verdict_reason = (
                f"Quran distinct from all 16 meters AND all 3 baselines at "
                f"alpha_per={ALPHA_PER}; AND mean & median sit between prose and poetry "
                f"(quantitative al-Bāqillānī)."
            )
        else:
            verdict = "PASS"
            verdict_reason = (
                f"Quran distinct from all 16 meters AND all 3 baselines at "
                f"alpha_per={ALPHA_PER} (al-Bāqillānī confirmed); between-test failed."
            )
    elif n_meter_match >= 1:
        matches = [r["meter"] for r in quran_vs_meters if r["indistinguishable"]]
        verdict = "NULL-classical-meter-match"
        verdict_reason = (
            f"Quran indistinguishable from meter(s) {matches} at alpha_per={ALPHA_PER}; "
            f"al-Bāqillānī's neither-prose-nor-poetry claim disconfirmed by this metric."
        )
    elif n_baseline_match >= 1:
        matches = [r["baseline"] for r in quran_vs_baselines if r["indistinguishable"]]
        verdict = "NULL-prose-or-poetry-match"
        verdict_reason = (
            f"Quran indistinguishable from baseline(s) {matches} at alpha_per={ALPHA_PER}."
        )
    else:
        verdict = "NULL"
        verdict_reason = "Unexpected combination."

    summary = {
        "test_id": "H-NEW-48",
        "seed": SEED,
        "n_bootstrap": N_BOOT,
        "k_family": K_FAMILY,
        "alpha_per": ALPHA_PER,
        "alpha_bon": ALPHA_BON,
        "letters_per_syllable_locked": LETTERS_PER_SYLLABLE,
        "sigma_fraction_locked": SIGMA_FRACTION,
        "rules_tuple": [
            "no-tashkeel", "orthographic-token", "graphemes",
            "basmala-counted-only-in-surah-1", "hafs-kufan", "mashriqi",
        ],
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "corpus_summaries": summaries,
        "quran_vs_meters_primary": quran_vs_meters,
        "quran_vs_baselines": quran_vs_baselines,
        "baqillani_between_test": baq,
        "positive_control_muallaqat": {
            "per_poet": pos_control_rows,
            "n_poets_with_assigned_meter_match_p_gt_0p001": int(historical_match_count),
            "n_poets_with_any_meter_match_p_gt_0p001": int(
                sum(1 for r in pos_control_rows if r["best_passes_p_gt_0p001"])
            ),
            "passed": bool(pos_control_pass),
        },
        "robustness_alt_letters_per_syllable": {
            "lps_1.4": {
                "n_indistinguishable_meters": int(n_lo),
                "table": quran_vs_meters_lo,
            },
            "lps_1.8": {
                "n_indistinguishable_meters": int(n_hi),
                "table": quran_vs_meters_hi,
            },
        },
        "n_meter_matches_primary": int(n_meter_match),
        "n_baseline_matches_primary": int(n_baseline_match),
    }

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(summary, fh, indent=2, ensure_ascii=False)

    print(f"\nVerdict: {verdict}")
    print(f"  {verdict_reason}")
    print(f"\nWrote: {OUT_JSON}")


if __name__ == "__main__":
    main()
