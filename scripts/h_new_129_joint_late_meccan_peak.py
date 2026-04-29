#!/usr/bin/env python3
"""H-NEW-129 — formal joint Late-Meccan peak across 5 Pattern-B axes.

Pre-reg:
  findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak-prereg.md

Primary test:
  Using the locked 4-phase H-NEW-125 schema, test whether all 5 pre-locked
  Pattern-B axes have a unique phase maximum at Late Meccan.

  Pattern-B axes:
    - qul_density
    - book_reference_density
    - eschatological_density
    - muq_cardinality
    - loanword_density

  Null:
    Permute phase labels across the 114 surahs while preserving the observed
    phase counts. Recompute the exact 5-of-5 Late-Meccan hit. One-sided
    permutation p = (1 + hits) / (1 + N_PERM).

MW-5 positive control:
  The same machinery must recover a known 5-axis Medinan peak bundle from
  H-NEW-125:
    - allah_density
    - legal_term_density
    - personal_pronoun_density
    - mean_verse_length
    - divine_name_density

Bonferroni family:
  k = 1, alpha_bon = 0.01. MW-5 is diagnostic and does not consume a slot.
"""
from __future__ import annotations

import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
UPSTREAM_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-125.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-129.json"

SEED = 20260418
N_PERM = 10_000
BON_K = 1
ALPHA_BON = 0.01

PHASE_ORDER = [
    "Early Meccan",
    "Middle Meccan",
    "Late Meccan",
    "Medinan",
]
PHASE_TO_INDEX = {phase: idx for idx, phase in enumerate(PHASE_ORDER)}

PATTERN_B_AXES = [
    "qul_density",
    "book_reference_density",
    "eschatological_density",
    "muq_cardinality",
    "loanword_density",
]
PATTERN_A_MW5_AXES = [
    "allah_density",
    "legal_term_density",
    "personal_pronoun_density",
    "mean_verse_length",
    "divine_name_density",
]


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else float("nan")


def phase_means(values: list[float], phase_idx: list[int]) -> list[float]:
    buckets: list[list[float]] = [[] for _ in PHASE_ORDER]
    for value, idx in zip(values, phase_idx, strict=True):
        buckets[idx].append(value)
    return [mean(bucket) for bucket in buckets]


def unique_peak_index(means: list[float], tol: float = 1e-12) -> int | None:
    max_val = max(means)
    winners = [idx for idx, value in enumerate(means) if math.isclose(value, max_val, abs_tol=tol, rel_tol=0.0)]
    if len(winners) != 1:
        return None
    return winners[0]


def summarize_bundle(
    axis_vectors: dict[str, list[float]],
    axis_names: list[str],
    phase_idx: list[int],
    target_phase: str,
) -> dict:
    target_idx = PHASE_TO_INDEX[target_phase]
    per_axis = {}
    n_target = 0
    for axis_name in axis_names:
        means = phase_means(axis_vectors[axis_name], phase_idx)
        peak_idx = unique_peak_index(means)
        peak_phase = PHASE_ORDER[peak_idx] if peak_idx is not None else None
        target_hit = peak_idx == target_idx
        if target_hit:
            n_target += 1
        per_axis[axis_name] = {
            "phase_means": {phase: float(means[i]) for i, phase in enumerate(PHASE_ORDER)},
            "peak_phase": peak_phase,
            "peak_phase_unique": peak_idx is not None,
            "target_hit": target_hit,
        }
    return {
        "target_phase": target_phase,
        "n_axes": len(axis_names),
        "n_target_phase_peaks": n_target,
        "joint_hit": n_target == len(axis_names),
        "per_axis": per_axis,
    }


def bundle_hit_count(
    axis_vectors: dict[str, list[float]],
    axis_names: list[str],
    phase_idx: list[int],
    target_phase: str,
) -> int:
    target_idx = PHASE_TO_INDEX[target_phase]
    n_target = 0
    for axis_name in axis_names:
        peak_idx = unique_peak_index(phase_means(axis_vectors[axis_name], phase_idx))
        if peak_idx == target_idx:
            n_target += 1
    return n_target


with open(UPSTREAM_JSON, encoding="utf-8") as f:
    upstream = json.load(f)

per_surah = upstream["per_surah_axis_values"]
sids = sorted(int(sid) for sid in per_surah.keys())
assert sids == list(range(1, 115)), "expected contiguous surah ids 1..114"

phase_labels = [per_surah[str(sid)]["noldeke_phase"] for sid in sids]
phase_idx = [PHASE_TO_INDEX[label] for label in phase_labels]
phase_counts = Counter(phase_labels)
expected_counts = {
    "Early Meccan": 48,
    "Middle Meccan": 21,
    "Late Meccan": 21,
    "Medinan": 24,
}
assert dict(phase_counts) == expected_counts, f"unexpected phase counts: {phase_counts}"

axis_vectors = {}
for axis_name in PATTERN_B_AXES + PATTERN_A_MW5_AXES:
    axis_vectors[axis_name] = [
        float(per_surah[str(sid)]["axis_values"][axis_name])
        for sid in sids
    ]

primary_obs = summarize_bundle(axis_vectors, PATTERN_B_AXES, phase_idx, "Late Meccan")
mw5_obs = summarize_bundle(axis_vectors, PATTERN_A_MW5_AXES, phase_idx, "Medinan")

print("[H-NEW-129] Observed primary bundle:", file=sys.stderr)
for axis_name in PATTERN_B_AXES:
    axis_info = primary_obs["per_axis"][axis_name]
    print(
        f"  {axis_name}: peak={axis_info['peak_phase']} "
        f"target_hit={axis_info['target_hit']}",
        file=sys.stderr,
    )
print(
    f"  n_late_meccan_peaks={primary_obs['n_target_phase_peaks']}/5 "
    f"joint_hit={primary_obs['joint_hit']}",
    file=sys.stderr,
)

print("[H-NEW-129] Observed MW-5 bundle:", file=sys.stderr)
for axis_name in PATTERN_A_MW5_AXES:
    axis_info = mw5_obs["per_axis"][axis_name]
    print(
        f"  {axis_name}: peak={axis_info['peak_phase']} "
        f"target_hit={axis_info['target_hit']}",
        file=sys.stderr,
    )
print(
    f"  n_medinan_peaks={mw5_obs['n_target_phase_peaks']}/5 "
    f"joint_hit={mw5_obs['joint_hit']}",
    file=sys.stderr,
)

rng = random.Random(SEED)
perm_primary_joint_hits = 0
perm_mw5_joint_hits = 0
perm_primary_peak_count_dist = Counter()
perm_mw5_peak_count_dist = Counter()

print(f"[H-NEW-129] Running {N_PERM} phase-label permutations (seed={SEED})", file=sys.stderr)
for perm_idx in range(N_PERM):
    perm_phase_idx = phase_idx[:]
    rng.shuffle(perm_phase_idx)

    primary_count = bundle_hit_count(axis_vectors, PATTERN_B_AXES, perm_phase_idx, "Late Meccan")
    mw5_count = bundle_hit_count(axis_vectors, PATTERN_A_MW5_AXES, perm_phase_idx, "Medinan")

    perm_primary_peak_count_dist[primary_count] += 1
    perm_mw5_peak_count_dist[mw5_count] += 1

    if primary_count == len(PATTERN_B_AXES):
        perm_primary_joint_hits += 1
    if mw5_count == len(PATTERN_A_MW5_AXES):
        perm_mw5_joint_hits += 1

    if (perm_idx + 1) % 2000 == 0:
        print(f"  [H-NEW-129] perm {perm_idx + 1}/{N_PERM}", file=sys.stderr)

p_primary = (1 + perm_primary_joint_hits) / (1 + N_PERM)
p_mw5 = (1 + perm_mw5_joint_hits) / (1 + N_PERM)

primary_pass = primary_obs["joint_hit"] and (p_primary < ALPHA_BON)
mw5_pass = mw5_obs["joint_hit"] and (p_mw5 < ALPHA_BON)

if not mw5_pass:
    overall_verdict = "NULL-BROKEN"
elif primary_pass:
    overall_verdict = "PASS-DIRECTED"
else:
    overall_verdict = "NULL"

print("[H-NEW-129] Results:", file=sys.stderr)
print(
    f"  Primary: observed={primary_obs['n_target_phase_peaks']}/5 "
    f"p_perm={p_primary:.6f} pass={primary_pass}",
    file=sys.stderr,
)
print(
    f"  MW-5: observed={mw5_obs['n_target_phase_peaks']}/5 "
    f"p_perm={p_mw5:.6f} pass={mw5_pass}",
    file=sys.stderr,
)
print(f"  Verdict: {overall_verdict}", file=sys.stderr)

result = {
    "id": "H-NEW-129",
    "title": "Formal joint Late-Meccan peak across the 5 Pattern-B axes",
    "bonferroni_family": "h-new-129-joint-late-meccan-peak",
    "bonferroni_k": BON_K,
    "alpha_bon": ALPHA_BON,
    "alpha_raw": ALPHA_BON,
    "direction": "Late Meccan only; exact 5-of-5 unique-max joint peak",
    "n_perm": N_PERM,
    "seed": SEED,
    "phase_order": PHASE_ORDER,
    "phase_counts": dict(phase_counts),
    "upstream_json": str(UPSTREAM_JSON.relative_to(ROOT)),
    "pre_reg": "findings/phase-b-hypotheses/h-new-129-joint-late-meccan-peak-prereg.md",
    "naive_equal_phase_independence_reference": 1.0 / (len(PHASE_ORDER) ** len(PATTERN_B_AXES)),
    "notes": [
        "Primary inference is the empirical phase-label permutation p-value, not the naive equal-phase heuristic.",
        "MW-5 uses a known Medinan-peak 5-axis bundle from H-NEW-125 and does not consume a Bonferroni slot.",
    ],
    "primary_pattern_b": {
        "axes": PATTERN_B_AXES,
        "target_phase": "Late Meccan",
        "observed_n_target_phase_peaks": primary_obs["n_target_phase_peaks"],
        "observed_joint_hit": primary_obs["joint_hit"],
        "perm_joint_hits": perm_primary_joint_hits,
        "p_perm_one_sided": p_primary,
        "passes_alpha_bon": primary_pass,
        "per_axis": primary_obs["per_axis"],
        "perm_n_target_phase_peaks_distribution": {
            str(k): perm_primary_peak_count_dist.get(k, 0)
            for k in range(len(PATTERN_B_AXES) + 1)
        },
    },
    "mw5_positive_control": {
        "axes": PATTERN_A_MW5_AXES,
        "target_phase": "Medinan",
        "observed_n_target_phase_peaks": mw5_obs["n_target_phase_peaks"],
        "observed_joint_hit": mw5_obs["joint_hit"],
        "perm_joint_hits": perm_mw5_joint_hits,
        "p_perm_one_sided": p_mw5,
        "mw5_pass": mw5_pass,
        "per_axis": mw5_obs["per_axis"],
        "perm_n_target_phase_peaks_distribution": {
            str(k): perm_mw5_peak_count_dist.get(k, 0)
            for k in range(len(PATTERN_A_MW5_AXES) + 1)
        },
    },
    "verdict": {
        "primary_pass": primary_pass,
        "mw5_pass": mw5_pass,
        "overall": overall_verdict,
        "verdict_ceiling": "PASS-DIRECTED only; axis bundle was selected from prior H-NEW-125 results.",
    },
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f"[H-NEW-129] Wrote {OUT_JSON.relative_to(ROOT)}", file=sys.stderr)
