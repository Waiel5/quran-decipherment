#!/usr/bin/env python3
"""
H-NEW-274 — empirical-vs-classical a-priori reassignment test for
Q36 YS and Q42 HMASQ.

Pre-reg:
  findings/phase-b-hypotheses/h-new-274-empirical-vs-classical-singleton-reassignment-prereg.md
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = (
    ROOT
    / "findings/phase-b-hypotheses"
    / "h-new-274-empirical-vs-classical-singleton-reassignment-prereg.md"
)
H232_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-232.json"
H252_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-252.json"
H1652_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-165-2.json"
OUTPUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-274.json"

PRIMARY_ALPHA = 0.025
MIN_MATERIAL_DELTA = 6
SINGLETON_ORDER = (
    "ALMS",
    "ALMR",
    "KHYAS",
    "TH",
    "TS",
    "YS",
    "S",
    "HMASQ",
    "Q",
    "N",
)
DISPUTED = ("YS", "HMASQ")

CLASSICAL_APRIORI = {
    "ALMS": {"ALM"},
    "ALMR": {"ALM", "ALR"},
    "KHYAS": {"HM", "TSM"},
    "TH": {"TSM"},
    "TS": {"TSM"},
    "YS": {"ALM", "ALR"},
    "S": {"TSM"},
    "HMASQ": {"HM"},
    "Q": {"HM", "TSM"},
    "N": {"ALM", "ALR"},
}


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_one_sided_binom_tail(successes: int, trials: int) -> float:
    if trials <= 0:
        return 1.0
    numer = sum(math.comb(trials, i) for i in range(successes, trials + 1))
    return numer / (2**trials)


def canonicalize_table(table: dict[str, set[str]]) -> dict[str, list[str]]:
    return {key: sorted(values) for key, values in sorted(table.items())}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def load_h232_discovery() -> tuple[dict[str, object], dict[str, str]]:
    data = load_json(H232_JSON)
    rows: dict[str, dict[str, object]] = {}
    for row in data["per_singleton_results"]:
        rows[row["truth_set"]] = {
            "surah": int(row["surah"]),
            "nearest": str(row["nearest_centroid_cluster"]),
            "distances": {k: float(v) for k, v in row["distances_to_centroids"].items()},
        }

    empirical_replacements = {truth: rows[truth]["nearest"] for truth in DISPUTED}
    return (
        {
            "space_id": "h232_discovery_baseline",
            "split": "discovery",
            "source": "h-new-232.json",
            "source_field": "per_singleton_results",
            "rows": rows,
            "observed_matches": int(data["observed_matches"]),
            "permutation_p": float(data["null_stats"]["p_value"]),
        },
        empirical_replacements,
    )


def load_h252_joint() -> dict[str, object]:
    data = load_json(H252_JSON)
    rows: dict[str, dict[str, object]] = {}
    for truth in SINGLETON_ORDER:
        row = data["joint_results"][truth]
        rows[truth] = {
            "surah": int(row["surah"]),
            "nearest": str(row["nearest"]),
            "distances": {k: float(v) for k, v in row["all_distances"].items()},
        }
    return {
        "space_id": "h252_joint_phon_alphabeta",
        "split": "holdout",
        "source": "h-new-252.json",
        "source_field": "joint_results",
        "rows": rows,
        "observed_matches": int(data["joint_phon_alphabeta_matches"]),
        "permutation_p": float(data["perm_p_joint"]),
    }


def load_h1652_holdouts() -> list[dict[str, object]]:
    data = load_json(H1652_JSON)
    locked_variant_ids = (
        "watson_modern_voice",
        "strict_pharyngeal_split",
        "holes_glottal_ha_ayn",
    )
    variants = {variant["id"]: variant for variant in data["variants"]}

    out = []
    for variant_id in locked_variant_ids:
        variant = variants[variant_id]
        rows: dict[str, dict[str, object]] = {}
        for row in variant["singleton_geometry"]["rows"]:
            rows[row["truth_set"]] = {
                "surah": int(row["surah"]),
                "nearest": str(row["nearest_centroid_cluster"]),
                "distances": {
                    key: float(value) for key, value in row["distances_to_centroids"].items()
                },
            }
        out.append(
            {
                "space_id": f"h1652_{variant_id}",
                "split": "holdout",
                "source": "h-new-165-2.json",
                "source_field": f"variants[{variant_id}].singleton_geometry.rows",
                "rows": rows,
                "observed_matches": int(variant["singleton_geometry"]["matches"]),
                "permutation_p": float(variant["singleton_geometry"]["permutation_null"]["p_value"]),
            }
        )
    return out


def build_empirical_table(empirical_replacements: dict[str, str]) -> dict[str, set[str]]:
    table = {truth: set(accepted) for truth, accepted in CLASSICAL_APRIORI.items()}
    for truth, cluster in empirical_replacements.items():
        table[truth] = {cluster}
    return table


def score_space_rows(
    rows: dict[str, dict[str, object]],
    table: dict[str, set[str]],
) -> tuple[int, dict[str, dict[str, object]]]:
    matches = 0
    per_singleton: dict[str, dict[str, object]] = {}
    for truth in SINGLETON_ORDER:
        nearest = str(rows[truth]["nearest"])
        accepted = set(table[truth])
        match = nearest in accepted
        if match:
            matches += 1
        per_singleton[truth] = {
            "surah": int(rows[truth]["surah"]),
            "nearest": nearest,
            "accepted": sorted(accepted),
            "match": bool(match),
        }
    return matches, per_singleton


def disputed_margin(truth: str, distances: dict[str, float]) -> float:
    if truth == "YS":
        return min(distances["ALM"], distances["ALR"]) - distances["HM"]
    if truth == "HMASQ":
        return distances["HM"] - distances["TSM"]
    raise ValueError(f"Unexpected disputed singleton: {truth}")


def evaluate_space(
    space: dict[str, object],
    classical_table: dict[str, set[str]],
    empirical_table: dict[str, set[str]],
) -> dict[str, object]:
    rows = space["rows"]
    classical_matches, classical_detail = score_space_rows(rows, classical_table)
    empirical_matches, empirical_detail = score_space_rows(rows, empirical_table)

    disputed = {}
    for truth in DISPUTED:
        disputed[truth] = {
            "surah": int(rows[truth]["surah"]),
            "nearest": str(rows[truth]["nearest"]),
            "distances": {k: float(v) for k, v in rows[truth]["distances"].items()},
            "margin_empirical_over_classical": float(disputed_margin(truth, rows[truth]["distances"])),
        }

    return {
        "space_id": space["space_id"],
        "split": space["split"],
        "source": space["source"],
        "source_field": space["source_field"],
        "observed_matches_parent": int(space["observed_matches"]),
        "permutation_p_parent": float(space["permutation_p"]),
        "classical_matches": int(classical_matches),
        "empirical_matches": int(empirical_matches),
        "delta_matches": int(empirical_matches - classical_matches),
        "classical_per_singleton": classical_detail,
        "empirical_per_singleton": empirical_detail,
        "disputed_singletons": disputed,
    }


def aggregate_holdout_primary(
    evaluated_spaces: list[dict[str, object]],
) -> dict[str, object]:
    improved = []
    worsened = []
    unchanged = 0
    classical_total = 0
    empirical_total = 0

    for space in evaluated_spaces:
        if space["split"] != "holdout":
            continue
        classical_total += int(space["classical_matches"])
        empirical_total += int(space["empirical_matches"])
        for truth in SINGLETON_ORDER:
            classical_match = bool(space["classical_per_singleton"][truth]["match"])
            empirical_match = bool(space["empirical_per_singleton"][truth]["match"])
            cell = {
                "space_id": space["space_id"],
                "singleton": truth,
                "surah": int(space["classical_per_singleton"][truth]["surah"]),
                "nearest": str(space["classical_per_singleton"][truth]["nearest"]),
            }
            if empirical_match and not classical_match:
                improved.append(cell)
            elif classical_match and not empirical_match:
                worsened.append(cell)
            else:
                unchanged += 1

    discordant = len(improved) + len(worsened)
    p_value = exact_one_sided_binom_tail(len(improved), discordant)
    delta_matches = empirical_total - classical_total
    pass_primary = (
        delta_matches >= MIN_MATERIAL_DELTA
        and len(worsened) == 0
        and p_value < PRIMARY_ALPHA
    )

    return {
        "n_holdout_spaces": sum(1 for space in evaluated_spaces if space["split"] == "holdout"),
        "n_singleton_cells": sum(
            len(SINGLETON_ORDER) for space in evaluated_spaces if space["split"] == "holdout"
        ),
        "classical_total_matches": int(classical_total),
        "empirical_total_matches": int(empirical_total),
        "delta_matches": int(delta_matches),
        "improved_cells": improved,
        "worsened_cells": worsened,
        "unchanged_cell_count": int(unchanged),
        "discordant_cell_count": int(discordant),
        "exact_one_sided_p": float(p_value),
        "alpha_primary": float(PRIMARY_ALPHA),
        "min_material_delta": int(MIN_MATERIAL_DELTA),
        "pass_primary": bool(pass_primary),
    }


def summarize_margins(evaluated_spaces: list[dict[str, object]]) -> dict[str, object]:
    out: dict[str, object] = {}
    for truth in DISPUTED:
        per_space = []
        for space in evaluated_spaces:
            if space["split"] != "holdout":
                continue
            per_space.append(
                {
                    "space_id": space["space_id"],
                    "margin_empirical_over_classical": float(
                        space["disputed_singletons"][truth]["margin_empirical_over_classical"]
                    ),
                }
            )
        margins = [row["margin_empirical_over_classical"] for row in per_space]
        out[truth] = {
            "per_space": per_space,
            "mean_margin": float(sum(margins) / len(margins)),
            "min_margin": float(min(margins)),
            "all_positive": bool(all(value > 0 for value in margins)),
        }
    return out


def main() -> None:
    print("=== H-NEW-274 empirical-vs-classical singleton reassignment ===", flush=True)

    discovery_space, empirical_replacements = load_h232_discovery()
    empirical_table = build_empirical_table(empirical_replacements)
    spaces = [discovery_space, load_h252_joint(), *load_h1652_holdouts()]

    evaluated_spaces = [
        evaluate_space(space, CLASSICAL_APRIORI, empirical_table) for space in spaces
    ]
    primary = aggregate_holdout_primary(evaluated_spaces)
    margins = summarize_margins(evaluated_spaces)

    discovery_eval = next(space for space in evaluated_spaces if space["split"] == "discovery")
    all_spaces_classical = sum(int(space["classical_matches"]) for space in evaluated_spaces)
    all_spaces_empirical = sum(int(space["empirical_matches"]) for space in evaluated_spaces)

    if primary["pass_primary"]:
        verdict = "PASS-HOLDOUT-STRONGER"
    elif primary["delta_matches"] > 0:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-274",
        "title": "Empirical-vs-classical a-priori reassignment test for Q36 YS and Q42 HMASQ",
        "prereg_sha256": sha256_file(PREREG_PATH),
        "discovery_source": {
            "space_id": discovery_space["space_id"],
            "source": discovery_space["source"],
            "source_field": discovery_space["source_field"],
            "empirical_replacements": empirical_replacements,
        },
        "tables": {
            "classical": canonicalize_table(CLASSICAL_APRIORI),
            "empirical": canonicalize_table(empirical_table),
        },
        "spaces": evaluated_spaces,
        "primary_holdout_test": primary,
        "margin_summary": margins,
        "summary": {
            "discovery_classical_matches": int(discovery_eval["classical_matches"]),
            "discovery_empirical_matches": int(discovery_eval["empirical_matches"]),
            "all_spaces_classical_matches": int(all_spaces_classical),
            "all_spaces_empirical_matches": int(all_spaces_empirical),
            "all_spaces_delta": int(all_spaces_empirical - all_spaces_classical),
            "verdict": verdict,
        },
    }

    OUTPUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    print(
        "holdout classical={classical} empirical={empirical} delta={delta} "
        "discordant={discordant} p={p:.8f} verdict={verdict}".format(
            classical=primary["classical_total_matches"],
            empirical=primary["empirical_total_matches"],
            delta=primary["delta_matches"],
            discordant=primary["discordant_cell_count"],
            p=primary["exact_one_sided_p"],
            verdict=verdict,
        ),
        flush=True,
    )


if __name__ == "__main__":
    main()
