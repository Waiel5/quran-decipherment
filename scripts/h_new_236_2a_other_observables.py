#!/usr/bin/env python3
"""H-NEW-236.2a - broader observable coverage under the landed M_H top-100 scaffold.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-2a-other-observables-prereg.md

This run reuses the H-NEW-236.1b M_H top-100 simulator family as directly as
possible. The only new logic is:
  1. capture simulated tours
  2. compute extra order-sensitive observables on those tours
  3. judge whether the empirical mushaf remains inside the M_H simulator
     envelope on those external observables
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from scipy import stats as sstats

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
SCRIPTS_DIR = PROJECT_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import h_new_236_1b_mufassal_terminal as h2361b

SEED = 20260422
N_SIM = 1000
N_RANDOM = 1000

PREREG = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-236-2a-other-observables-prereg.md"
PARENT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1b.json"
OUT_JSON = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-236-2a.json"

QURAN_JSON = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
H239_TSV = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-239-per-surah.tsv"
H172_CSV = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-172-per-surah.csv"


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def percentile_of(value: float, distribution: list[float]) -> float:
    rank = sum(1 for v in distribution if v <= value)
    return 100.0 * rank / len(distribution)


def ci_95(distribution: list[float]) -> tuple[float, float]:
    ordered = sorted(distribution)
    n = len(ordered)
    lo_idx = int(0.025 * n)
    hi_idx = max(int(0.975 * n) - 1, 0)
    return ordered[lo_idx], ordered[hi_idx]


def summarize_distribution(values: list[float]) -> dict:
    lo, hi = ci_95(values)
    return {
        "mean": statistics.mean(values),
        "stdev": statistics.pstdev(values),
        "min": min(values),
        "max": max(values),
        "q025": lo,
        "q975": hi,
    }


def analyze_scalar(empirical: float, sim_values: list[float], rand_values: list[float]) -> dict:
    sim_lo, sim_hi = ci_95(sim_values)
    rand_lo, rand_hi = ci_95(rand_values)
    sim_mean = statistics.mean(sim_values)
    sim_std = statistics.pstdev(sim_values)
    rand_mean = statistics.mean(rand_values)
    rand_std = statistics.pstdev(rand_values)
    return {
        "empirical": empirical,
        "sim_mean": sim_mean,
        "sim_std": sim_std,
        "sim_ci_lo": sim_lo,
        "sim_ci_hi": sim_hi,
        "sim_percentile_of_empirical": percentile_of(empirical, sim_values),
        "sim_inside_95ci": sim_lo <= empirical <= sim_hi,
        "sim_z": (empirical - sim_mean) / sim_std if sim_std > 0 else (0.0 if empirical == sim_mean else math.copysign(float("inf"), empirical - sim_mean)),
        "rand_mean": rand_mean,
        "rand_std": rand_std,
        "rand_ci_lo": rand_lo,
        "rand_ci_hi": rand_hi,
        "rand_percentile_of_empirical": percentile_of(empirical, rand_values),
        "rand_inside_95ci": rand_lo <= empirical <= rand_hi,
        "rand_z": (empirical - rand_mean) / rand_std if rand_std > 0 else (0.0 if empirical == rand_mean else math.copysign(float("inf"), empirical - rand_mean)),
    }


def load_divine_name_density() -> dict[int, float]:
    out: dict[int, float] = {}
    with H239_TSV.open() as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            out[int(row["surah"])] = float(row["density"])
    if sorted(out) != list(range(1, 115)):
        raise AssertionError("H-NEW-239 density table must cover all 114 surahs")
    return out


def load_kl_from_corpus() -> dict[int, float]:
    with QURAN_JSON.open() as f:
        quran = json.load(f)

    corpus_counts: Counter[str] = Counter()
    per_surah_counts: dict[int, Counter[str]] = {}
    for surah in quran:
        sid = int(surah["id"])
        counts: Counter[str] = Counter()
        for verse in surah.get("verses", []):
            counts.update(verse.get("text", "").split())
        per_surah_counts[sid] = counts
        corpus_counts.update(counts)

    vocab = list(corpus_counts)
    vocab_size = len(vocab)
    alpha = 0.5
    total_corpus = sum(corpus_counts.values())
    denom_corpus = total_corpus + alpha * vocab_size

    out: dict[int, float] = {}
    for sid in range(1, 115):
        counts = per_surah_counts[sid]
        total = sum(counts.values())
        denom_surah = total + alpha * vocab_size
        kl = 0.0
        for token in vocab:
            p_surah = (counts.get(token, 0) + alpha) / denom_surah
            p_corpus = (corpus_counts[token] + alpha) / denom_corpus
            kl += p_surah * math.log(p_surah / p_corpus)
        out[sid] = kl
    return out


def load_alpha_beta_residuals() -> tuple[dict[int, float], list[int]]:
    out: dict[int, float] = {}
    with H172_CSV.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah_id"])
            alpha = float(row["alpha"])
            beta = float(row["beta_h159"])
            if not (math.isfinite(alpha) and math.isfinite(beta)):
                continue
            out[sid] = alpha - (-3.526 * beta + 3.689)
    eligible = sorted(out)
    if len(eligible) != 79:
        raise AssertionError(f"Expected 79 finite H-NEW-178 residual surahs, found {len(eligible)}")
    return out, eligible


def spearman_position_metric(
    tour: list[int],
    values_by_surah: dict[int, float],
    eligible_surahs: list[int] | None = None,
) -> float:
    pos_by_surah = {surah0 + 1: idx + 1 for idx, surah0 in enumerate(tour)}
    surahs = eligible_surahs if eligible_surahs is not None else sorted(values_by_surah)
    positions = [pos_by_surah[sid] for sid in surahs]
    values = [values_by_surah[sid] for sid in surahs]
    rho, _ = sstats.spearmanr(positions, values)
    return float(rho)


def simulate_mh_top100_tours(dmat: list[list[float]]) -> tuple[list[list[int]], list[dict], list[dict]]:
    hinges_1indexed = h2361b.build_cell_M_H(dmat)
    within_hinges, cross_hinges = h2361b.classify_hinges(hinges_1indexed)
    hinges_0indexed = [(a - 1, b - 1) for a, b in hinges_1indexed]
    hinge_set = set(hinges_0indexed)
    valid_pairs = h2361b.valid_pairs_for_sa()

    tours: list[list[int]] = []
    obs_rows: list[dict] = []
    sa_rows: list[dict] = []

    for sim_idx in range(N_SIM):
        rng = random.Random(SEED + 100_000 + sim_idx)
        init = h2361b.initial_hinge_respecting_tour(
            rng,
            within_hinges,
            cross_hinges,
            hinges_0indexed,
            mufassal_sub_blocks_1indexed=None,
        )
        final, stats = h2361b.sa_with_constraints(init, dmat, rng, hinge_set, valid_pairs)
        if not h2361b.all_hinges_ok(final, hinges_0indexed):
            failed = {k: v for k, v in h2361b.verify_hinges(final, hinges_0indexed).items() if not v}
            raise AssertionError(f"M_H hinge verification failed on sim {sim_idx}: {failed}")
        tours.append(final)
        obs = h2361b.compute_observables(final, dmat)
        obs["sim_idx"] = sim_idx
        obs_rows.append(obs)
        sa_rows.append(stats)

    return tours, obs_rows, sa_rows


def simulate_random_tours(dmat: list[list[float]]) -> tuple[list[list[int]], list[dict]]:
    tours: list[list[int]] = []
    obs_rows: list[dict] = []
    for rand_idx in range(N_RANDOM):
        rng = random.Random(SEED + 900_000 + rand_idx)
        perm = list(range(114))
        rng.shuffle(perm)
        tours.append(perm)
        obs = h2361b.compute_observables(perm, dmat)
        obs["rand_idx"] = rand_idx
        obs_rows.append(obs)
    return tours, obs_rows


def load_parent_mh_z() -> float:
    with PARENT_JSON.open() as f:
        data = json.load(f)
    return float(data["cells"]["cell_M_H_top100"]["block_chi2"]["per_block"]["L_mufassal_short"]["sim_z"])


def verdict_from_count(pass_count: int, mw6_ok: bool) -> str:
    if not mw6_ok:
        return "INVALID-RUN"
    if pass_count == 3:
        return "BROAD-GENERALIZATION"
    if pass_count == 2:
        return "PARTIAL-GENERALIZATION"
    if pass_count == 1:
        return "WEAK-GENERALIZATION / MOSTLY-NARROW"
    return "NARROW / INSTRUMENT-BOUND"


def main() -> None:
    print("=" * 78)
    print("H-NEW-236.2a - Broader observable coverage under landed M_H top-100")
    print("=" * 78)
    print(f"Pre-reg SHA-256: {prereg_sha256()}")
    print(f"Seed={SEED}  N_sim={N_SIM}  N_random={N_RANDOM}")

    dmat = h2361b.load_d_matrix()
    empirical_tour = list(range(114))
    empirical_original = h2361b.compute_observables(empirical_tour, dmat)
    parent_mh_z = load_parent_mh_z()

    print("\nLoading external observable series...")
    density_by_surah = load_divine_name_density()
    kl_by_surah = load_kl_from_corpus()
    ab_resid_by_surah, ab_eligible = load_alpha_beta_residuals()

    print("Simulating M_H top-100 tours...")
    sim_tours, sim_original_rows, sa_rows = simulate_mh_top100_tours(dmat)

    print("Simulating random-order baseline...")
    rand_tours, rand_original_rows = simulate_random_tours(dmat)

    print("Running MW-6 positive control...")
    original_family_analysis = {
        key: h2361b.observable_analysis(
            empirical_original[key],
            [row[key] for row in sim_original_rows],
            [row[key] for row in rand_original_rows],
        )
        for key in ["L_path", "W_wrap", "L_tiwal", "L_hawamim", "L_mufassal_short", "L_tail_91_114"]
    }
    block_stat = h2361b.block_chi2(empirical_original, sim_original_rows, rand_original_rows)
    reproduced_z = block_stat["per_block"]["L_mufassal_short"]["sim_z"]
    mw6_ok = bool(
        original_family_analysis["L_path"]["sim_inside_95ci"]
        and original_family_analysis["W_wrap"]["sim_inside_95ci"]
        and original_family_analysis["L_tail_91_114"]["sim_inside_95ci"]
        and block_stat["sim_inside_95ci"]
        and math.isfinite(reproduced_z)
        and abs(reproduced_z - parent_mh_z) <= 2.0
    )
    print(
        "MW-6 positive control:",
        "PASS" if mw6_ok else "FAIL",
        f"(mufassal z {reproduced_z:+.3f}; parent {parent_mh_z:+.3f})",
    )

    print("\nEvaluating extra observables...")
    empirical_density_rho = spearman_position_metric(empirical_tour, density_by_surah)
    sim_density_rhos = [spearman_position_metric(tour, density_by_surah) for tour in sim_tours]
    rand_density_rhos = [spearman_position_metric(tour, density_by_surah) for tour in rand_tours]

    empirical_kl_rho = spearman_position_metric(empirical_tour, kl_by_surah)
    sim_kl_rhos = [spearman_position_metric(tour, kl_by_surah) for tour in sim_tours]
    rand_kl_rhos = [spearman_position_metric(tour, kl_by_surah) for tour in rand_tours]

    empirical_ab_rho = spearman_position_metric(empirical_tour, ab_resid_by_surah, eligible_surahs=ab_eligible)
    sim_ab_rhos = [spearman_position_metric(tour, ab_resid_by_surah, eligible_surahs=ab_eligible) for tour in sim_tours]
    rand_ab_rhos = [spearman_position_metric(tour, ab_resid_by_surah, eligible_surahs=ab_eligible) for tour in rand_tours]

    extra_cells = {
        "cell_A_density_gradient_rho": {
            "label": "Spearman(position, divine_name_density) over 114 surahs",
            "source": "h-new-239-per-surah.tsv",
            "n_surahs": 114,
            "analysis": analyze_scalar(empirical_density_rho, sim_density_rhos, rand_density_rhos),
        },
        "cell_B_kl_gradient_rho": {
            "label": "Spearman(position, KL_from_corpus) over 114 surahs",
            "source": "inline H-NEW-231 recompute from quran-no-tashkeel.json (Dirichlet alpha=0.5)",
            "n_surahs": 114,
            "analysis": analyze_scalar(empirical_kl_rho, sim_kl_rhos, rand_kl_rhos),
        },
        "cell_C_alpha_beta_residual_gradient_rho": {
            "label": "Spearman(position, alpha_beta_residual) over the fixed finite-residual H-NEW-178 subset",
            "source": "h-new-172-per-surah.csv + H-NEW-178 fitted line",
            "n_surahs": len(ab_eligible),
            "eligible_surahs_1indexed": ab_eligible,
            "analysis": analyze_scalar(empirical_ab_rho, sim_ab_rhos, rand_ab_rhos),
        },
    }

    pass_count = sum(1 for cell in extra_cells.values() if cell["analysis"]["sim_inside_95ci"])
    overall_verdict = verdict_from_count(pass_count, mw6_ok)

    for cell_name, cell in extra_cells.items():
        analysis = cell["analysis"]
        status = "PASS" if analysis["sim_inside_95ci"] else ("LOW-OUTSIDE" if analysis["empirical"] < analysis["sim_ci_lo"] else "HIGH-OUTSIDE")
        print(
            f"  {cell_name}: {status:12s} "
            f"emp={analysis['empirical']:+.4f} "
            f"sim_mean={analysis['sim_mean']:+.4f} "
            f"sim95=[{analysis['sim_ci_lo']:+.4f}, {analysis['sim_ci_hi']:+.4f}] "
            f"pct={analysis['sim_percentile_of_empirical']:.1f}"
        )

    print(f"\nPrimary extra-observable pass count: {pass_count}/3")
    print(f"Overall verdict: {overall_verdict}")

    output = {
        "finding_id": "h-new-236-2a",
        "title": "Broader observable coverage under the landed M_H top-100 scaffold",
        "pre_reg_sha256": prereg_sha256(),
        "parent": "h-new-236-1b",
        "related": ["h-new-239", "h-new-231", "h-new-178"],
        "seed": SEED,
        "n_sim": N_SIM,
        "n_random": N_RANDOM,
        "rules_tuple": (
            "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, "
            "H-NEW-236.1b imported M_H top-100 hinge scaffold, stochastic 2-opt "
            "with classical-block + Q1-lock + length-stratification + M2-muq, "
            "external observables from H-NEW-239 / H-NEW-231 / H-NEW-178, seed 20260422)"
        ),
        "mw6_positive_control": {
            "pass": mw6_ok,
            "parent_mufassal_short_z": parent_mh_z,
            "reproduced_mufassal_short_z": reproduced_z,
            "delta_z": reproduced_z - parent_mh_z,
            "original_family_analysis": original_family_analysis,
            "block_chi2": block_stat,
        },
        "original_family_empirical": empirical_original,
        "simulator_sa_summary": {
            "accepted_mean": statistics.mean(row["accepted"] for row in sa_rows),
            "accepted_min": min(row["accepted"] for row in sa_rows),
            "accepted_max": max(row["accepted"] for row in sa_rows),
            "rejected_by_hinge_mean": statistics.mean(row["rejected_by_hinge"] for row in sa_rows),
            "rejected_by_sa_mean": statistics.mean(row["rejected_by_sa"] for row in sa_rows),
        },
        "extra_observables": extra_cells,
        "extra_observable_sim_summaries": {
            "rho_pos_density_114": summarize_distribution(sim_density_rhos),
            "rho_pos_kl_114": summarize_distribution(sim_kl_rhos),
            "rho_pos_alpha_beta_residual_finite": summarize_distribution(sim_ab_rhos),
        },
        "extra_observable_random_summaries": {
            "rho_pos_density_114": summarize_distribution(rand_density_rhos),
            "rho_pos_kl_114": summarize_distribution(rand_kl_rhos),
            "rho_pos_alpha_beta_residual_finite": summarize_distribution(rand_ab_rhos),
        },
        "pass_count": pass_count,
        "overall_verdict": overall_verdict,
        "implementation_limits": [
            "H-NEW-178 alpha-beta residual is evaluated only on the finite 79-surah subset of the parent N >= 50 file domain.",
            "The imported generator fixes the classical block partition, so block-membership-heavy gradients are partly inherited rather than freely regenerated.",
            "H-NEW-231 KL values are recomputed inline because no standalone per-surah CSV exists in the repo.",
        ],
    }

    OUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
