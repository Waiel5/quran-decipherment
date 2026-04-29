#!/usr/bin/env python3
"""H-NEW-266 — per-surah phonological signature test.

Pre-reg:
  findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature-prereg.md

Seed: 20260418
Bonferroni family: k=5, alpha_bon=0.01

Tight implementation:
  - lock 4 classical-tajwid-relevant class densities
  - test one omnibus + four class-specific dispersion cells
  - exact length-matched repartition null via sequential multivariate
    hypergeometric sampling on 6 disjoint categories
  - synthetic MW-5 positive control
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-266-per-surah-phonological-signature-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-266.json"

SEED = 20260418
N_PERMS = 5000
MW5_N_PERMS = 1000
ALPHA_BON = 0.01

ALPHABET28 = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
ALPHABET_SET = set(ALPHABET28)

NORMALIZE_MAP = {
    "ٱ": "ا",
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ؤ": "و",
    "ئ": "ي",
    "ة": "ه",
    "ى": "ي",
}

STRIP_CODEPOINTS = set(range(0x064B, 0x0653))
STRIP_CODEPOINTS.add(0x0640)
STRIP_CODEPOINTS.update(range(0x06D6, 0x06EE))

CATEGORY_NAMES = [
    "sad_shared",
    "emphatic_only",
    "throat",
    "sibilant_only",
    "sonorant",
    "other",
]

CLASS_NAMES = [
    "core_emphatic",
    "strict_throat",
    "safir_sibilant",
    "idgham_sonorant",
]

CELL_NAMES = [
    "omnibus_l2",
    "core_emphatic_mad",
    "strict_throat_mad",
    "safir_sibilant_mad",
    "idgham_sonorant_mad",
]

CELL_TO_CLASS = {
    "core_emphatic_mad": "core_emphatic",
    "strict_throat_mad": "strict_throat",
    "safir_sibilant_mad": "safir_sibilant",
    "idgham_sonorant_mad": "idgham_sonorant",
}

CLASS_DEFINITIONS = {
    "core_emphatic": ["ص", "ض", "ط", "ظ"],
    "strict_throat": ["ع", "ح", "خ", "غ"],
    "safir_sibilant": ["س", "ز", "ص"],
    "idgham_sonorant": ["ي", "ر", "م", "ل", "و", "ن"],
}


def normalize_letters(text: str) -> list[str]:
    letters: list[str] = []
    for ch in text:
        if ord(ch) in STRIP_CODEPOINTS:
            continue
        ch = NORMALIZE_MAP.get(ch, ch)
        if ch in ALPHABET_SET:
            letters.append(ch)
    return letters


def letter_to_category(letter: str) -> int:
    if letter == "ص":
        return 0
    if letter in {"ض", "ط", "ظ"}:
        return 1
    if letter in {"ع", "ح", "خ", "غ"}:
        return 2
    if letter in {"س", "ز"}:
        return 3
    if letter in {"ي", "ر", "م", "ل", "و", "ن"}:
        return 4
    return 5


def categories_to_class_counts(cat_counts: np.ndarray) -> np.ndarray:
    counts = np.asarray(cat_counts, dtype=np.int64)
    out = np.zeros((counts.shape[0], 4), dtype=np.int64)
    out[:, 0] = counts[:, 0] + counts[:, 1]
    out[:, 1] = counts[:, 2]
    out[:, 2] = counts[:, 0] + counts[:, 3]
    out[:, 3] = counts[:, 4]
    return out


def compute_cell_vector(densities: np.ndarray, global_density: np.ndarray) -> np.ndarray:
    diff = densities - global_density[None, :]
    omnibus = np.linalg.norm(diff, axis=1).mean()
    class_mads = np.abs(diff).mean(axis=0)
    return np.concatenate(([float(omnibus)], class_mads.astype(float)))


def sample_partition(
    lengths: np.ndarray,
    total_cat_counts: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    remaining = np.array(total_cat_counts, dtype=np.int64, copy=True)
    out = np.zeros((len(lengths), 6), dtype=np.int64)

    for i, seg_len in enumerate(lengths):
        available = remaining.copy()
        seg_remaining = int(seg_len)
        for cat_idx in range(5):
            if seg_remaining == 0:
                break
            good = int(available[cat_idx])
            bad = int(available[cat_idx + 1 :].sum())
            if good == 0:
                draw = 0
            elif bad == 0:
                draw = seg_remaining
            else:
                draw = int(rng.hypergeometric(good, bad, seg_remaining))
            out[i, cat_idx] = draw
            available[cat_idx] = 0
            seg_remaining -= draw
        out[i, 5] = seg_remaining
        remaining -= out[i]

    if np.any(remaining != 0):
        raise RuntimeError("Partition sampler failed to exhaust category inventory.")
    return out


def empirical_p_upper(null_values: np.ndarray, observed: np.ndarray) -> np.ndarray:
    return (1.0 + (null_values >= observed[None, :]).sum(axis=0)) / (len(null_values) + 1.0)


def summarize_top_outliers(
    surah_meta: list[dict],
    observed_density: np.ndarray,
    null_mean: np.ndarray,
    null_sd: np.ndarray,
    p_two_sided: np.ndarray,
    k: int = 5,
) -> dict[str, dict[str, list[dict]]]:
    z = np.divide(
        observed_density - null_mean,
        null_sd,
        out=np.zeros_like(observed_density),
        where=null_sd > 0,
    )

    out: dict[str, dict[str, list[dict]]] = {}
    for class_idx, class_name in enumerate(CLASS_NAMES):
        hi = np.argsort(-z[:, class_idx])[:k]
        lo = np.argsort(z[:, class_idx])[:k]

        def row(ix: int) -> dict:
            meta = surah_meta[int(ix)]
            return {
                "surah": int(meta["surah"]),
                "name": meta["name"],
                "type": meta["type"],
                "letters": int(meta["letters"]),
                "density": round(float(observed_density[ix, class_idx]), 6),
                "null_mean": round(float(null_mean[ix, class_idx]), 6),
                "z": round(float(z[ix, class_idx]), 3),
                "p_two_sided": round(float(p_two_sided[ix, class_idx]), 4),
            }

        out[class_name] = {
            "highest": [row(int(ix)) for ix in hi],
            "lowest": [row(int(ix)) for ix in lo],
        }
    return out


def largest_remainder_counts(length: int, probs: np.ndarray) -> np.ndarray:
    raw = probs * float(length)
    base = np.floor(raw).astype(np.int64)
    shortfall = int(length - base.sum())
    if shortfall > 0:
        order = np.argsort(-(raw - base))
        base[order[:shortfall]] += 1
    return base


def build_mw5_synthetic(lengths: np.ndarray, base_probs: np.ndarray) -> np.ndarray:
    block_probs: list[np.ndarray] = []
    for block in range(4):
        probs = base_probs.astype(float).copy()
        if block == 0:
            probs[0] += 0.015
            probs[1] += 0.045
            probs[5] -= 0.060
        elif block == 1:
            probs[2] += 0.060
            probs[5] -= 0.060
        elif block == 2:
            probs[0] += 0.015
            probs[3] += 0.045
            probs[5] -= 0.060
        elif block == 3:
            probs[4] += 0.080
            probs[5] -= 0.080
        if probs.min() <= 0:
            raise RuntimeError("MW-5 block probabilities went non-positive.")
        block_probs.append(probs)

    synth = np.zeros((len(lengths), 6), dtype=np.int64)
    for ix, length in enumerate(lengths):
        synth[ix] = largest_remainder_counts(int(length), block_probs[ix % 4])
    return synth


def run_null(
    observed_cat_counts: np.ndarray,
    lengths: np.ndarray,
    n_perms: int,
    seed: int,
    track_per_surah: bool,
) -> dict:
    total_cat_counts = observed_cat_counts.sum(axis=0)
    observed_class_counts = categories_to_class_counts(observed_cat_counts)
    global_density = observed_class_counts.sum(axis=0) / float(lengths.sum())
    observed_density = observed_class_counts / lengths[:, None]
    observed_cells = compute_cell_vector(observed_density, global_density)

    rng = np.random.default_rng(seed)
    null_cells = np.zeros((n_perms, 5), dtype=np.float64)

    if track_per_surah:
        null_sum = np.zeros_like(observed_density, dtype=np.float64)
        null_sumsq = np.zeros_like(observed_density, dtype=np.float64)
        null_extreme = np.zeros_like(observed_class_counts, dtype=np.int64)
        observed_dev = np.abs(observed_density - global_density[None, :])
    else:
        null_sum = None
        null_sumsq = None
        null_extreme = None
        observed_dev = None

    for perm_ix in range(n_perms):
        sim_cat_counts = sample_partition(lengths, total_cat_counts, rng)
        sim_class_counts = categories_to_class_counts(sim_cat_counts)
        sim_density = sim_class_counts / lengths[:, None]
        null_cells[perm_ix] = compute_cell_vector(sim_density, global_density)

        if track_per_surah:
            null_sum += sim_density
            null_sumsq += sim_density * sim_density
            null_extreme += (np.abs(sim_density - global_density[None, :]) >= observed_dev).astype(np.int64)

        if (perm_ix + 1) % 500 == 0 or perm_ix == 0:
            print(
                f"  perm {perm_ix + 1}/{n_perms} "
                f"null_omnibus_mean={null_cells[: perm_ix + 1, 0].mean():.6f}",
                file=sys.stderr,
            )

    p_values = empirical_p_upper(null_cells, observed_cells)
    q95 = np.quantile(null_cells, 0.95, axis=0)
    passes = (observed_cells > q95) & (p_values < ALPHA_BON)

    result = {
        "observed_cat_counts": observed_cat_counts,
        "observed_class_counts": observed_class_counts,
        "observed_density": observed_density,
        "global_density": global_density,
        "observed_cells": observed_cells,
        "null_cells": null_cells,
        "p_values": p_values,
        "q95": q95,
        "passes": passes,
    }

    if track_per_surah:
        null_mean = null_sum / float(n_perms)
        null_var = np.maximum(null_sumsq / float(n_perms) - null_mean * null_mean, 0.0)
        null_sd = np.sqrt(null_var)
        p_two_sided = (1.0 + null_extreme) / (n_perms + 1.0)
        result.update(
            {
                "per_surah_null_mean": null_mean,
                "per_surah_null_sd": null_sd,
                "per_surah_p_two_sided": p_two_sided,
            }
        )

    return result


def main() -> None:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

    quran = json.loads(QURAN_JSON.read_text(encoding="utf-8"))
    if len(quran) != 114:
        raise RuntimeError(f"Expected 114 surahs, got {len(quran)}")

    surah_meta: list[dict] = []
    observed_cat_counts = np.zeros((114, 6), dtype=np.int64)

    for row_idx, surah in enumerate(quran):
        text = "".join(verse["text"] for verse in surah["verses"])
        letters = normalize_letters(text)
        if not letters:
            raise RuntimeError(f"Surah {surah['id']} normalized to zero retained letters.")
        counts = np.zeros(6, dtype=np.int64)
        for ch in letters:
            counts[letter_to_category(ch)] += 1
        observed_cat_counts[row_idx] = counts
        surah_meta.append(
            {
                "surah": int(surah["id"]),
                "name": surah["name"],
                "type": surah["type"],
                "letters": int(len(letters)),
            }
        )

    lengths = observed_cat_counts.sum(axis=1)
    total_letters = int(lengths.sum())
    print(
        f"Loaded 114 surahs; retained-letter total={total_letters}; "
        f"min={int(lengths.min())}; max={int(lengths.max())}",
        file=sys.stderr,
    )

    print("[1/3] Running observed Quran vs null...", file=sys.stderr)
    observed_result = run_null(
        observed_cat_counts=observed_cat_counts,
        lengths=lengths,
        n_perms=N_PERMS,
        seed=SEED,
        track_per_surah=True,
    )

    print("[2/3] Running MW-5 planted positive control...", file=sys.stderr)
    base_probs = observed_cat_counts.sum(axis=0).astype(np.float64) / float(total_letters)
    synthetic_cat_counts = build_mw5_synthetic(lengths, base_probs)
    mw5_result = run_null(
        observed_cat_counts=synthetic_cat_counts,
        lengths=lengths,
        n_perms=MW5_N_PERMS,
        seed=SEED + 1,
        track_per_surah=False,
    )

    mw5_pass = bool(mw5_result["passes"][0] and mw5_result["passes"][1:].sum() >= 3)
    observed_passes = observed_result["passes"]

    if not mw5_pass:
        verdict = "NULL-BROKEN"
    elif observed_passes[0]:
        verdict = "PASS-DIRECTED"
    elif observed_passes[1:].any():
        verdict = "PARTIAL-CLASS-ONLY"
    else:
        verdict = "NULL"

    print("[3/3] Packaging JSON...", file=sys.stderr)
    outliers = summarize_top_outliers(
        surah_meta=surah_meta,
        observed_density=observed_result["observed_density"],
        null_mean=observed_result["per_surah_null_mean"],
        null_sd=observed_result["per_surah_null_sd"],
        p_two_sided=observed_result["per_surah_p_two_sided"],
    )

    cells = {}
    for ix, cell_name in enumerate(CELL_NAMES):
        cells[cell_name] = {
            "observed": round(float(observed_result["observed_cells"][ix]), 6),
            "null_mean": round(float(observed_result["null_cells"][:, ix].mean()), 6),
            "null_sd": round(float(observed_result["null_cells"][:, ix].std(ddof=1)), 6),
            "null_q95": round(float(observed_result["q95"][ix]), 6),
            "p_perm_upper": round(float(observed_result["p_values"][ix]), 6),
            "pass": bool(observed_result["passes"][ix]),
        }

    mw5_cells = {}
    for ix, cell_name in enumerate(CELL_NAMES):
        mw5_cells[cell_name] = {
            "observed": round(float(mw5_result["observed_cells"][ix]), 6),
            "null_mean": round(float(mw5_result["null_cells"][:, ix].mean()), 6),
            "null_sd": round(float(mw5_result["null_cells"][:, ix].std(ddof=1)), 6),
            "null_q95": round(float(mw5_result["q95"][ix]), 6),
            "p_perm_upper": round(float(mw5_result["p_values"][ix]), 6),
            "pass": bool(mw5_result["passes"][ix]),
        }

    per_surah_rows = []
    z_matrix = np.divide(
        observed_result["observed_density"] - observed_result["per_surah_null_mean"],
        observed_result["per_surah_null_sd"],
        out=np.zeros_like(observed_result["observed_density"]),
        where=observed_result["per_surah_null_sd"] > 0,
    )

    for ix, meta in enumerate(surah_meta):
        row = {
            "surah": int(meta["surah"]),
            "name": meta["name"],
            "type": meta["type"],
            "letters": int(meta["letters"]),
            "densities": {},
            "null_mean": {},
            "z": {},
            "p_two_sided": {},
        }
        for class_idx, class_name in enumerate(CLASS_NAMES):
            row["densities"][class_name] = round(
                float(observed_result["observed_density"][ix, class_idx]), 6
            )
            row["null_mean"][class_name] = round(
                float(observed_result["per_surah_null_mean"][ix, class_idx]), 6
            )
            row["z"][class_name] = round(float(z_matrix[ix, class_idx]), 3)
            row["p_two_sided"][class_name] = round(
                float(observed_result["per_surah_p_two_sided"][ix, class_idx]), 6
            )
        per_surah_rows.append(row)

    payload = {
        "id": "h-new-266",
        "title": "Per-surah phonological signature test",
        "date": "2026-04-18",
        "seed": SEED,
        "prereg": str(PREREG_FILE.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "bonferroni_family": "h-new-266-per-surah-phonological-signature",
        "bonferroni_k": 5,
        "alpha_bon": ALPHA_BON,
        "n_perms": N_PERMS,
        "mw5_n_perms": MW5_N_PERMS,
        "rules_tuple": (
            "quran-no-tashkeel, 28-letter orthographic normalization, exact surah "
            "letter counts preserved, 114 surahs, Hafs-Kufan"
        ),
        "normalization": {
            "alphabet28": ALPHABET28,
            "map": NORMALIZE_MAP,
            "drop_non_alphabet": True,
        },
        "class_definitions": CLASS_DEFINITIONS,
        "category_definitions": {
            "sad_shared": ["ص"],
            "emphatic_only": ["ض", "ط", "ظ"],
            "throat": ["ع", "ح", "خ", "غ"],
            "sibilant_only": ["س", "ز"],
            "sonorant": ["ي", "ر", "م", "ل", "و", "ن"],
            "other": "all remaining normalized letters",
        },
        "corpus": {
            "n_surahs": 114,
            "total_retained_letters": total_letters,
            "min_surah_letters": int(lengths.min()),
            "max_surah_letters": int(lengths.max()),
            "global_density": {
                class_name: round(float(observed_result["global_density"][ix]), 6)
                for ix, class_name in enumerate(CLASS_NAMES)
            },
        },
        "cells": cells,
        "top_outliers": outliers,
        "per_surah": per_surah_rows,
        "mw5": {
            "description": (
                "Synthetic planted four-block control with deterministic category "
                "boosts transferred from other-mass."
            ),
            "pass_rule": "omnibus PASS and at least 3/4 class cells PASS at alpha_bon=0.01",
            "global_density": {
                class_name: round(float(mw5_result["global_density"][ix]), 6)
                for ix, class_name in enumerate(CLASS_NAMES)
            },
            "cells": mw5_cells,
            "pass": mw5_pass,
        },
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON}", file=sys.stderr)
    print(f"verdict: {verdict}", file=sys.stderr)


if __name__ == "__main__":
    main()
