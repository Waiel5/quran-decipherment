"""H-NEW-113 — Letter-Position-within-Verse Distribution.

Tests whether the 14 muqaṭṭāʿat letters {ا ل م ص ر ك ه ي ع ط س ح ق ن} occupy
DIFFERENT positional distributions within verses vs the 14 complement letters.

Cells:
  1. KS 2-sample (primary, 2-sided)
  2. Per-bin relative risk (secondary, 1-sided on bin 10)
  3. Verse-initial letter binomial (secondary, 1-sided, circularity-excluded)

See pre-reg at findings/phase-b-hypotheses/h-new-113-letter-position-prereg.md
"""
from __future__ import annotations

import json
import math
import os
import sys
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, "/Users/grey/Downloads/quran")
from analysis.tools.loader import load_quran  # noqa: E402

SEED = 20260417
ALPHA_BON = 0.0167  # Bonferroni-3

ALPHA28 = [
    "ا", "ب", "ت", "ث", "ج", "ح", "خ", "د", "ذ", "ر",
    "ز", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف",
    "ق", "ك", "ل", "م", "ن", "ه", "و", "ي",
]
MUQ14 = {"ا", "ل", "م", "ص", "ر", "ك", "ه", "ي", "ع", "ط", "س", "ح", "ق", "ن"}
COMP14 = set(ALPHA28) - MUQ14
assert len(MUQ14) == 14 and len(COMP14) == 14

# 29 muqaṭṭāʿat-opened surahs (from cross-finding-008 / master ledger)
MUQ_SURAHS = {
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28,
    29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
}
assert len(MUQ_SURAHS) == 29

NORMALIZE_MAP = {
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ٱ": "ا",
    "ة": "ه",
    "ى": "ي",
    "ؤ": "و",
    "ئ": "ي",
}
EXCLUDED_MARKS = set("ۖۗۘۙۚۛۜ۞۩")


def normalize_verse(text: str) -> str:
    """Map to 28-letter alphabet and drop marks/spaces/standalone hamza."""
    out = []
    for ch in text:
        if ch == " " or ch in EXCLUDED_MARKS or ch == "ء":
            continue
        nc = NORMALIZE_MAP.get(ch, ch)
        if nc in ALPHA28:
            out.append(nc)
    return "".join(out)


def main() -> None:
    rng = np.random.default_rng(SEED)

    surahs = load_quran("no-tashkeel")

    # Collect per-letter positions (for 28 letters).
    # positions_by_letter[letter] = list of normalized positions in (0, 1)
    positions_by_letter: dict[str, list[float]] = {L: [] for L in ALPHA28}

    # Also track per-verse normalized strings and first-letters (for Cell 3).
    verse_records = []  # list of dicts {surah, verse, first_letter, length}

    total_letters = 0
    for sur in surahs:
        for v in sur.verses:
            norm = normalize_verse(v.text)
            L = len(norm)
            if L == 0:
                verse_records.append(
                    {"surah": sur.id, "verse": v.id, "first_letter": None, "length": 0}
                )
                continue
            first_letter = norm[0]
            verse_records.append(
                {"surah": sur.id, "verse": v.id, "first_letter": first_letter, "length": L}
            )
            for i, ch in enumerate(norm):
                p = (i + 0.5) / L
                positions_by_letter[ch].append(p)
                total_letters += 1

    # Per-letter counts
    counts_by_letter = {L: len(positions_by_letter[L]) for L in ALPHA28}

    # Aggregate MUQ vs COMP position arrays.
    pos_muq = np.concatenate(
        [np.array(positions_by_letter[L], dtype=float) for L in sorted(MUQ14)]
    )
    pos_comp = np.concatenate(
        [np.array(positions_by_letter[L], dtype=float) for L in sorted(COMP14)]
    )
    n_muq = len(pos_muq)
    n_comp = len(pos_comp)

    # ---------- Cell 1: KS 2-sample (primary) ----------
    ks_stat, ks_pvalue = stats.ks_2samp(pos_muq, pos_comp, alternative="two-sided")

    # Locate the x* at which |F_muq - F_comp| is maximized.
    all_pts = np.sort(np.concatenate([pos_muq, pos_comp]))
    cdf_muq = np.searchsorted(np.sort(pos_muq), all_pts, side="right") / n_muq
    cdf_comp = np.searchsorted(np.sort(pos_comp), all_pts, side="right") / n_comp
    diff = cdf_muq - cdf_comp
    idx = int(np.argmax(np.abs(diff)))
    x_star = float(all_pts[idx])
    signed_diff = float(diff[idx])  # positive => MUQ CDF above COMP (more early mass)

    # ---------- Cell 2: 10-bin relative risk ----------
    N_BINS = 10
    bin_edges = np.linspace(0.0, 1.0, N_BINS + 1)

    def per_letter_density(L_set: set[str]) -> np.ndarray:
        """For set of letters, return density vector over N_BINS = count_in_bin / count_total aggregated across all letters in set (count_total is sum across letters)."""
        totals = 0
        per_bin = np.zeros(N_BINS, dtype=float)
        for L in L_set:
            arr = np.asarray(positions_by_letter[L], dtype=float)
            if len(arr) == 0:
                continue
            hist, _ = np.histogram(arr, bins=bin_edges)
            per_bin += hist
            totals += len(arr)
        if totals == 0:
            return np.zeros(N_BINS)
        return per_bin / totals

    density_muq = per_letter_density(MUQ14)
    density_comp = per_letter_density(COMP14)
    rr_per_bin = density_muq / np.where(density_comp > 0, density_comp, np.nan)

    rr_bin10 = float(rr_per_bin[-1])
    rr_bin1 = float(rr_per_bin[0])

    # Bootstrap CI for RR_bin10 and RR_bin1 by resampling verses.
    B = 5000
    # For bootstrap, we need positions linked to verses. Rebuild as (letter, position, verse_idx).
    verse_ids = [(r["surah"], r["verse"]) for r in verse_records]
    verse_idx_map = {k: i for i, k in enumerate(verse_ids)}
    n_verses = len(verse_ids)
    # Build per-verse lists: letter-in-MUQ / letter-in-COMP counts per bin.
    muq_bin_counts = np.zeros((n_verses, N_BINS), dtype=np.int64)
    comp_bin_counts = np.zeros((n_verses, N_BINS), dtype=np.int64)
    muq_total_per_verse = np.zeros(n_verses, dtype=np.int64)
    comp_total_per_verse = np.zeros(n_verses, dtype=np.int64)

    # Rebuild by iterating verses again for correctness.
    for idx_v, sur in enumerate(surahs):
        pass
    # Simpler: rebuild positions tagged with verse index.
    verse_bin_tag: list[tuple[int, int, bool]] = []
    # Direct rebuild:
    k = 0
    for sur in surahs:
        for v in sur.verses:
            norm = normalize_verse(v.text)
            L = len(norm)
            vkey = (sur.id, v.id)
            v_i = verse_idx_map[vkey]
            if L == 0:
                k += 1
                continue
            for i, ch in enumerate(norm):
                p = (i + 0.5) / L
                b = min(int(p * N_BINS), N_BINS - 1)
                if ch in MUQ14:
                    muq_bin_counts[v_i, b] += 1
                    muq_total_per_verse[v_i] += 1
                elif ch in COMP14:
                    comp_bin_counts[v_i, b] += 1
                    comp_total_per_verse[v_i] += 1
            k += 1

    boot_rr_bin10 = np.zeros(B)
    boot_rr_bin1 = np.zeros(B)
    for b in range(B):
        samp = rng.integers(0, n_verses, size=n_verses)
        mb = muq_bin_counts[samp].sum(axis=0)
        cb = comp_bin_counts[samp].sum(axis=0)
        mt = muq_total_per_verse[samp].sum()
        ct = comp_total_per_verse[samp].sum()
        if mt == 0 or ct == 0:
            boot_rr_bin10[b] = np.nan
            boot_rr_bin1[b] = np.nan
            continue
        dm = mb / mt
        dc = cb / ct
        boot_rr_bin10[b] = dm[-1] / dc[-1] if dc[-1] > 0 else np.nan
        boot_rr_bin1[b] = dm[0] / dc[0] if dc[0] > 0 else np.nan

    ci_lo_10, ci_hi_10 = np.nanpercentile(boot_rr_bin10, [2.5, 97.5])
    ci_lo_1, ci_hi_1 = np.nanpercentile(boot_rr_bin1, [2.5, 97.5])

    # 1-sided p-value for RR_bin10 > 1: fraction of bootstrap draws ≤ 1.
    p_rr10_onesided = float(np.nanmean(boot_rr_bin10 <= 1.0))
    # For RR_bin1 >1 (interest-only, reported):
    p_rr1_onesided = float(np.nanmean(boot_rr_bin1 <= 1.0))

    # ---------- Cell 3: verse-initial excess ----------
    # Exclude verse 1 of the 29 muqaṭṭāʿat-opened surahs (circularity).
    excluded_ids = [(s, 1) for s in sorted(MUQ_SURAHS)]
    excluded_set = set(excluded_ids)
    n_muq_init = 0
    n_comp_init = 0
    n_excluded_used = 0
    first_letters_excluded = []
    for r in verse_records:
        if r["first_letter"] is None:
            continue
        if (r["surah"], r["verse"]) in excluded_set:
            first_letters_excluded.append((r["surah"], r["verse"], r["first_letter"]))
            n_excluded_used += 1
            continue
        fl = r["first_letter"]
        if fl in MUQ14:
            n_muq_init += 1
        elif fl in COMP14:
            n_comp_init += 1

    # Frequency-weighted null expectation: after excluding opener-verse-1 letters.
    # Recompute letter counts excluding verse 1 of the 29 opener surahs.
    freq_muq_adj = 0
    freq_comp_adj = 0
    for sur in surahs:
        for v in sur.verses:
            if (sur.id, v.id) in excluded_set:
                continue
            norm = normalize_verse(v.text)
            for ch in norm:
                if ch in MUQ14:
                    freq_muq_adj += 1
                elif ch in COMP14:
                    freq_comp_adj += 1
    p_null_muq = freq_muq_adj / (freq_muq_adj + freq_comp_adj)

    n_initial_total = n_muq_init + n_comp_init
    # 1-sided binomial: observed ≥ n_muq_init given n=n_initial_total, p=p_null_muq
    binom_res = stats.binomtest(n_muq_init, n_initial_total, p_null_muq, alternative="greater")
    initial_pvalue = float(binom_res.pvalue)
    observed_frac = n_muq_init / n_initial_total

    # ---------- MW-5 positive control: rhyme letters verse-final enrichment ----------
    mw5_results = {}
    for L in ["ن", "م", "ر", "ل", "ا", "ي"]:
        arr = np.asarray(positions_by_letter[L], dtype=float)
        hist, _ = np.histogram(arr, bins=bin_edges)
        dens = hist / len(arr) if len(arr) else hist
        mw5_results[L] = {
            "count": int(len(arr)),
            "density_per_bin": [float(x) for x in dens],
            "bin10_density": float(dens[-1]) if len(dens) else 0.0,
            "bin10_over_uniform": float(dens[-1] / 0.1) if len(dens) else 0.0,
        }

    # ---------- Build 28x10 per-letter matrix ----------
    per_letter_bins = {}
    for L in ALPHA28:
        arr = np.asarray(positions_by_letter[L], dtype=float)
        hist, _ = np.histogram(arr, bins=bin_edges)
        tot = int(len(arr))
        dens = (hist / tot).tolist() if tot > 0 else [0.0] * N_BINS
        per_letter_bins[L] = {
            "count": tot,
            "in_muqattaat": L in MUQ14,
            "density_per_bin": [float(x) for x in dens],
        }

    # ---------- Assemble output ----------
    result = {
        "meta": {
            "id": "H-NEW-113",
            "title": "Letter-position-within-verse distribution",
            "seed": SEED,
            "alpha_bon": ALPHA_BON,
            "bonferroni_k": 3,
            "bonferroni_family": "h-new-113-letter-position",
            "n_bins": N_BINS,
            "bin_edges": bin_edges.tolist(),
            "n_verses": n_verses,
            "n_letters_total": total_letters,
            "n_positions_muq": int(n_muq),
            "n_positions_comp": int(n_comp),
        },
        "cell_1_ks": {
            "ks_statistic": float(ks_stat),
            "ks_pvalue": float(ks_pvalue),
            "x_star": x_star,
            "signed_diff_at_xstar": signed_diff,
            "interpretation_sign": (
                "positive = MUQ CDF above COMP (MUQ mass earlier in verse)"
                " / negative = MUQ mass later"
            ),
            "pass": bool(ks_pvalue < ALPHA_BON),
        },
        "cell_2_rr": {
            "density_muq_per_bin": density_muq.tolist(),
            "density_comp_per_bin": density_comp.tolist(),
            "rr_per_bin": [
                float(x) if np.isfinite(x) else None for x in rr_per_bin
            ],
            "rr_bin10": rr_bin10,
            "rr_bin10_ci95": [float(ci_lo_10), float(ci_hi_10)],
            "rr_bin10_pvalue_onesided": p_rr10_onesided,
            "rr_bin1": rr_bin1,
            "rr_bin1_ci95": [float(ci_lo_1), float(ci_hi_1)],
            "rr_bin1_pvalue_onesided_gt1": p_rr1_onesided,
            "bootstrap_B": B,
            "pass_bin10": bool(
                (ci_lo_10 > 1.0) and (p_rr10_onesided < ALPHA_BON)
            ),
        },
        "cell_3_initial": {
            "n_excluded_opener_v1": n_excluded_used,
            "excluded_surahs": sorted(MUQ_SURAHS),
            "n_muq_initial": int(n_muq_init),
            "n_comp_initial": int(n_comp_init),
            "n_initial_total": int(n_initial_total),
            "observed_muq_initial_fraction": float(observed_frac),
            "null_muq_expected_fraction": float(p_null_muq),
            "binomial_pvalue_onesided_greater": initial_pvalue,
            "pass": bool(initial_pvalue < ALPHA_BON),
        },
        "mw5_positive_control": mw5_results,
        "per_letter_position_matrix": per_letter_bins,
        "letter_counts": {L: int(counts_by_letter[L]) for L in ALPHA28},
    }

    out_path = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-113.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, ensure_ascii=False)

    # Minimal human summary.
    print(f"Total letters normalized: {total_letters}")
    print(f"MUQ positions: {n_muq} | COMP positions: {n_comp}")
    print(f"KS statistic = {ks_stat:.6f}, p = {ks_pvalue:.3e}")
    print(f"KS max at x* = {x_star:.4f}, signed Δ = {signed_diff:+.4f}")
    print(f"RR_bin1  = {rr_bin1:.4f}  95% CI [{ci_lo_1:.4f}, {ci_hi_1:.4f}]  p(>1)={1 - p_rr1_onesided:.4f}")
    print(f"RR_bin10 = {rr_bin10:.4f} 95% CI [{ci_lo_10:.4f}, {ci_hi_10:.4f}] p(≤1)={p_rr10_onesided:.4f}")
    print(f"Initial: muq_init={n_muq_init}, comp_init={n_comp_init}, obs_frac={observed_frac:.4f}, null_frac={p_null_muq:.4f}")
    print(f"Initial 1-sided binomial p = {initial_pvalue:.3e}")
    print(f"MW-5 positive control (bin10 density, ideally ≫ 0.1):")
    for L, r in mw5_results.items():
        print(f"  {L}: bin10={r['bin10_density']:.4f} (over-uniform {r['bin10_over_uniform']:.2f}x)")
    print(f"Results written to {out_path}")


if __name__ == "__main__":
    main()
