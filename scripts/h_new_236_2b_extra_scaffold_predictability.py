#!/usr/bin/env python3
"""H-NEW-236.2b - held-out predictability of the extra scaffold edges.

Pre-reg:
  findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability-prereg.md

Design locked from the session brief:
  - Universe = all 113 canonical consecutive edges (Q i -> Q i+1).
  - Positive set P = H100 \\ H50 from h-new-236-1d.json.
  - Negative set N = E \\ H100.
  - Analysis pool = P union N = 63 edges.
  - Features = 9 locked binary indicators sourced from H-NEW-130 / H-NEW-236.1b.
  - Model = L2 logistic regression, C=1.0, class_weight='balanced',
    deterministic solver='newton-cholesky'.
  - Validation = LOOCV on the 63-edge pool.
  - Primary statistic = ROC AUC on held-out probabilities.
  - Null = 10,000 class-count-preserving label permutations.
  - Positive control (descriptive only) = H-NEW-130 top-15 jump problem on all
    113 canonical edges under the same feature family + model + LOOCV pipeline.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

ROOT = Path("/Users/grey/Downloads/quran")
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import h_new_130_fisher_rao_residuals as h130
import h_new_236_1b_mufassal_terminal as h2361b

SEED = 20260419
N_PERM = 10_000
SOLVER = "newton-cholesky"
MAX_ITER = 1000

PREREG = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-236-2b-extra-scaffold-predictability-prereg.md"
)
H2361D_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-236-1d.json"
H130_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-130.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-236-2b.json"

FEATURE_NAMES = [
    "classical_length_boundary",
    "period_transition",
    "phase_transition",
    "muq_presence_change",
    "muq_letterset_change",
    "within_hawamim",
    "within_mufassal_short",
    "same_rhyme_class",
    "liturgical_pair",
]


def prereg_sha256() -> str:
    return hashlib.sha256(PREREG.read_bytes()).hexdigest()


def round_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def load_h_sets() -> tuple[list[tuple[int, int]], set[tuple[int, int]], set[tuple[int, int]]]:
    payload = json.loads(H2361D_JSON.read_text(encoding="utf-8"))
    h50 = {tuple(edge) for edge in payload["cells"]["mw5_positive_control_top50"]["hinges_1indexed"]}
    h100 = {tuple(edge) for edge in payload["cells"]["cell_top100"]["hinges_1indexed"]}
    universe = [(i, i + 1) for i in range(1, 114)]

    if len(h50) != 50 or len(h100) != 100:
        raise RuntimeError(f"Unexpected hinge counts: |H50|={len(h50)} |H100|={len(h100)}")
    if not h50 <= h100:
        raise RuntimeError("Expected H50 to be a subset of H100.")

    return universe, h50, h100


def load_h130_top15() -> set[tuple[int, int]]:
    payload = json.loads(H130_JSON.read_text(encoding="utf-8"))
    top15 = {(row["i"], row["j"]) for row in payload["top15_largest_jumps"]}
    if len(top15) != 15:
        raise RuntimeError(f"Expected 15 top-jump edges, found {len(top15)}")
    return top15


def binary_feature_context() -> dict:
    period_by_sid, phase_by_sid = h130.load_period_phase()

    hawamim_members = set(h2361b.BLOCKS_1INDEXED["hawamim"])
    mufassal_short_members = set(h2361b.BLOCKS_1INDEXED["mufassal_short"])

    return {
        "period_by_sid": period_by_sid,
        "phase_by_sid": phase_by_sid,
        "length_boundary_slots": set(h130.LENGTH_BOUNDARIES),
        "muq_set": set(h130.MUQ_SET),
        "muq_letter": dict(h130.MUQ_LETTER),
        "hawamim_members": hawamim_members,
        "mufassal_short_members": mufassal_short_members,
        "rhyme_classes": dict(h2361b.RHYME_CLASSES_MUFASSAL_SHORT),
        "liturgical_pairs": set(h2361b.M_L_PAIRS_1INDEXED),
    }


def feature_row(edge: tuple[int, int], ctx: dict) -> dict[str, int]:
    a, b = edge
    muq_a = a in ctx["muq_set"]
    muq_b = b in ctx["muq_set"]

    return {
        "classical_length_boundary": int(a in ctx["length_boundary_slots"]),
        "period_transition": int(ctx["period_by_sid"][a] != ctx["period_by_sid"][b]),
        "phase_transition": int(ctx["phase_by_sid"][a] != ctx["phase_by_sid"][b]),
        "muq_presence_change": int(muq_a != muq_b),
        "muq_letterset_change": int(
            muq_a and muq_b and ctx["muq_letter"][a] != ctx["muq_letter"][b]
        ),
        "within_hawamim": int(a in ctx["hawamim_members"] and b in ctx["hawamim_members"]),
        "within_mufassal_short": int(
            a in ctx["mufassal_short_members"] and b in ctx["mufassal_short_members"]
        ),
        "same_rhyme_class": int(
            ctx["rhyme_classes"].get(a) is not None
            and ctx["rhyme_classes"].get(a) == ctx["rhyme_classes"].get(b)
        ),
        "liturgical_pair": int(edge in ctx["liturgical_pairs"]),
    }


def edge_table(
    edges: list[tuple[int, int]],
    positive_edges: set[tuple[int, int]],
    ctx: dict,
) -> list[dict]:
    rows = []
    for edge in edges:
        feature_map = feature_row(edge, ctx)
        row = {
            "edge": [edge[0], edge[1]],
            "label": int(edge in positive_edges),
        }
        row.update(feature_map)
        rows.append(row)
    return rows


def rows_to_matrix(rows: list[dict]) -> tuple[np.ndarray, np.ndarray]:
    x = np.array([[row[name] for name in FEATURE_NAMES] for row in rows], dtype=float)
    y = np.array([row["label"] for row in rows], dtype=int)
    return x, y


def fold_indices(n_rows: int) -> list[tuple[np.ndarray, np.ndarray]]:
    return [
        (
            np.array([idx for idx in range(n_rows) if idx != holdout], dtype=np.int64),
            np.array([holdout], dtype=np.int64),
        )
        for holdout in range(n_rows)
    ]


def logistic_factory() -> LogisticRegression:
    return LogisticRegression(
        C=1.0,
        class_weight="balanced",
        solver=SOLVER,
        max_iter=MAX_ITER,
    )


def loocv_probabilities(
    x: np.ndarray,
    y: np.ndarray,
    folds: list[tuple[np.ndarray, np.ndarray]],
) -> np.ndarray:
    probs = np.zeros(len(y), dtype=float)
    for train_idx, test_idx in folds:
        clf = logistic_factory()
        clf.fit(x[train_idx], y[train_idx])
        probs[test_idx[0]] = clf.predict_proba(x[test_idx])[0, 1]
    return probs


def confusion_at_half(y_true: np.ndarray, y_prob: np.ndarray) -> dict[str, int | float]:
    y_hat = (y_prob >= 0.5).astype(int)
    tp = int(((y_true == 1) & (y_hat == 1)).sum())
    tn = int(((y_true == 0) & (y_hat == 0)).sum())
    fp = int(((y_true == 0) & (y_hat == 1)).sum())
    fn = int(((y_true == 1) & (y_hat == 0)).sum())
    sens = tp / (tp + fn) if (tp + fn) else 0.0
    spec = tn / (tn + fp) if (tn + fp) else 0.0
    return {
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "accuracy": round_float((tp + tn) / len(y_true)),
        "sensitivity": round_float(sens),
        "specificity": round_float(spec),
        "balanced_accuracy": round_float((sens + spec) / 2.0),
    }


def fit_full_model(x: np.ndarray, y: np.ndarray) -> dict:
    clf = logistic_factory()
    clf.fit(x, y)
    return {
        "intercept": round_float(clf.intercept_[0]),
        "coefficients": {
            name: round_float(coef)
            for name, coef in zip(FEATURE_NAMES, clf.coef_[0], strict=True)
        },
    }


def permutation_null(
    x: np.ndarray,
    y: np.ndarray,
    folds: list[tuple[np.ndarray, np.ndarray]],
    observed_auc: float,
) -> dict:
    rng = np.random.default_rng(SEED)
    aucs = np.zeros(N_PERM, dtype=float)
    ge_count = 0

    for perm_idx in range(N_PERM):
        y_perm = rng.permutation(y)
        probs = loocv_probabilities(x, y_perm, folds)
        auc = float(roc_auc_score(y_perm, probs))
        aucs[perm_idx] = auc
        if auc >= observed_auc:
            ge_count += 1

        if (perm_idx + 1) % 1000 == 0:
            print(
                f"[perm] {perm_idx + 1:>5}/{N_PERM} complete"
                f"  current_ge={ge_count}",
                flush=True,
            )

    return {
        "n_perm": N_PERM,
        "p_value": round_float((1 + ge_count) / (N_PERM + 1), 6),
        "ge_count": int(ge_count),
        "null_auc_mean": round_float(aucs.mean()),
        "null_auc_std": round_float(aucs.std()),
        "null_auc_q95": round_float(np.quantile(aucs, 0.95)),
        "null_auc_q99": round_float(np.quantile(aucs, 0.99)),
        "null_auc_max": round_float(aucs.max()),
        "null_auc_min": round_float(aucs.min()),
    }


def feature_prevalence(rows: list[dict]) -> dict[str, dict[str, int]]:
    pos_rows = [row for row in rows if row["label"] == 1]
    neg_rows = [row for row in rows if row["label"] == 0]
    out = {}
    for name in FEATURE_NAMES:
        out[name] = {
            "all": int(sum(row[name] for row in rows)),
            "positive": int(sum(row[name] for row in pos_rows)),
            "negative": int(sum(row[name] for row in neg_rows)),
        }
    return out


def descriptive_strength_band(auc: float) -> str:
    if auc >= 0.80:
        return "strong"
    if auc >= 0.65:
        return "moderate"
    if auc >= 0.55:
        return "weak"
    return "near-null"


def inferential_verdict(auc: float, p_value: float) -> str:
    if p_value < 0.05:
        return f"PASS-DIRECTED ({descriptive_strength_band(auc)})"
    return f"NULL ({descriptive_strength_band(auc)} descriptive lift only)"


def main() -> None:
    print("=" * 78)
    print("H-NEW-236.2b - extra scaffold held-out predictability")
    print("=" * 78)
    print(f"Pre-reg SHA-256: {prereg_sha256()}")
    print(f"Seed={SEED}  Solver={SOLVER}  N_perm={N_PERM}")

    universe, h50, h100 = load_h_sets()
    positives = h100 - h50
    negatives = set(universe) - h100
    excluded_midband = h50
    if len(positives) != 50 or len(negatives) != 13:
        raise RuntimeError(
            f"Unexpected pool counts: |P|={len(positives)} |N|={len(negatives)}"
        )

    analysis_edges = [edge for edge in universe if edge in positives or edge in negatives]
    if len(analysis_edges) != 63:
        raise RuntimeError(f"Expected 63 analysis edges, found {len(analysis_edges)}")

    ctx = binary_feature_context()
    analysis_rows = edge_table(analysis_edges, positives, ctx)
    x_main, y_main = rows_to_matrix(analysis_rows)
    folds_main = fold_indices(len(analysis_rows))

    print(
        f"\nAnalysis pool: {len(analysis_rows)} edges"
        f"  positives={int(y_main.sum())}"
        f"  negatives={int((y_main == 0).sum())}"
    )

    probs_main = loocv_probabilities(x_main, y_main, folds_main)
    auc_main = float(roc_auc_score(y_main, probs_main))
    confusion_main = confusion_at_half(y_main, probs_main)
    null_main = permutation_null(x_main, y_main, folds_main, auc_main)
    full_main = fit_full_model(x_main, y_main)

    for row, prob in zip(analysis_rows, probs_main, strict=True):
        row["loocv_p_positive"] = round_float(prob)

    print(
        "\nPrimary result:"
        f"  AUC_LOOCV={auc_main:.6f}"
        f"  p_perm={null_main['p_value']:.6f}"
        f"  balanced_acc={confusion_main['balanced_accuracy']:.6f}"
    )

    top15_positive = load_h130_top15()
    control_rows = edge_table(universe, top15_positive, ctx)
    x_pc, y_pc = rows_to_matrix(control_rows)
    folds_pc = fold_indices(len(control_rows))
    probs_pc = loocv_probabilities(x_pc, y_pc, folds_pc)
    auc_pc = float(roc_auc_score(y_pc, probs_pc))
    confusion_pc = confusion_at_half(y_pc, probs_pc)
    full_pc = fit_full_model(x_pc, y_pc)

    for row, prob in zip(control_rows, probs_pc, strict=True):
        row["loocv_p_positive"] = round_float(prob)

    print(
        "Positive control (descriptive only):"
        f"  AUC_LOOCV={auc_pc:.6f}"
        f"  balanced_acc={confusion_pc['balanced_accuracy']:.6f}"
    )

    payload = {
        "finding_id": "h-new-236-2b",
        "title": "Held-out predictability of the extra scaffold edges under locked boundary features",
        "date": "2026-04-19",
        "seed": SEED,
        "pre_reg_sha256": prereg_sha256(),
        "rules_tuple": (
            "(113 canonical consecutive edges; H100 and H50 imported directly from "
            "h-new-236-1d.json; positive=P=H100\\\\H50; negative=N=E\\\\H100; 9 locked "
            "binary features from H-NEW-130 / H-NEW-236.1b; LOOCV logistic "
            f"C=1.0 class_weight=balanced solver={SOLVER}; 10000 label permutations; "
            "descriptive H-NEW-130 top-15 positive control)"
        ),
        "feature_names": FEATURE_NAMES,
        "universe": {
            "canonical_edge_count": len(universe),
            "h50_count": len(h50),
            "h100_count": len(h100),
            "analysis_pool_count": len(analysis_edges),
            "positive_count": int(y_main.sum()),
            "negative_count": int((y_main == 0).sum()),
            "excluded_h50_count": len(excluded_midband),
            "positive_edges": [list(edge) for edge in sorted(positives)],
            "negative_edges": [list(edge) for edge in sorted(negatives)],
            "excluded_h50_edges": [list(edge) for edge in sorted(excluded_midband)],
        },
        "main_analysis": {
            "auc_loocv": round_float(auc_main),
            "descriptive_strength_band": descriptive_strength_band(auc_main),
            "verdict": inferential_verdict(auc_main, float(null_main["p_value"])),
            "accuracy_at_0_5": confusion_main["accuracy"],
            "balanced_accuracy_at_0_5": confusion_main["balanced_accuracy"],
            "confusion_at_0_5": confusion_main,
            "permutation_null": null_main,
            "feature_prevalence": feature_prevalence(analysis_rows),
            "full_model": full_main,
            "rows": analysis_rows,
        },
        "positive_control_h130_top15_descriptive": {
            "edge_count": len(universe),
            "positive_count": int(y_pc.sum()),
            "negative_count": int((y_pc == 0).sum()),
            "auc_loocv": round_float(auc_pc),
            "descriptive_strength_band": descriptive_strength_band(auc_pc),
            "accuracy_at_0_5": confusion_pc["accuracy"],
            "balanced_accuracy_at_0_5": confusion_pc["balanced_accuracy"],
            "confusion_at_0_5": confusion_pc,
            "full_model": full_pc,
            "rows": control_rows,
        },
    }

    OUT_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
