#!/usr/bin/env python3
"""H-NEW-273 — Q1<->Q108 twin liturgical-anchor test.

Single landed cell:
  Surah score S(s) = sqrt(D(s) * I(s))
    D(s) = share of QAC STEM-root tokens in {Alh, rbb, rHm}
    I(s) = imperative density = IMPV tokens / verse

  Pair score T(a,b) = S(a) + S(b)

Primary target:
  Q1 + Q108

Exact matched null:
  all unordered Early-Meccan pairs with verse bins {5-7, 3-4}

Descriptive contrast:
  Q113 + Q114 under Early-Meccan pairs with verse bins {5-7, 5-7}
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import statistics
from itertools import combinations
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
PREREG = (
    ROOT
    / "findings"
    / "phase-b-hypotheses"
    / "h-new-273-q1-q108-twin-liturgical-anchor-prereg.md"
)
ROOT_GRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
IMPERATIVES_CSV = (
    ROOT / "findings" / "phase-b-hypotheses" / "csv" / "imperatives-per-surah.csv"
)
REVELATION_CSV = ROOT / "data" / "revelation-order.csv"
VERSE_COUNTS = ROOT / "data" / "hafs-verse-counts.tsv"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-273.json"

DIVINE_ROOTS = {"Alh", "rbb", "rHm"}
TARGET_PAIR = (1, 108)
CONTRAST_PAIR = (113, 114)


def len_bin(n_verses: int) -> str:
    if n_verses <= 4:
        return "3_4"
    if n_verses <= 7:
        return "5_7"
    if n_verses <= 10:
        return "8_10"
    if n_verses <= 30:
        return "11_30"
    if n_verses <= 80:
        return "31_80"
    return "81p"


def exact_upper_p(null_values: list[float], observed: float) -> float:
    ge = sum(1 for x in null_values if x >= observed)
    return (1 + ge) / (1 + len(null_values))


def z_score(observed: float, null_values: list[float]) -> float:
    if len(null_values) < 2:
        return 0.0
    mu = statistics.mean(null_values)
    sd = statistics.stdev(null_values)
    if sd == 0:
        return 0.0
    return (observed - mu) / sd


def load_root_counts() -> dict[int, dict[str, int]]:
    payload = json.loads(ROOT_GRAPH.read_text(encoding="utf-8"))
    return {int(k): dict(v) for k, v in payload["surahs"].items()}


def load_imperative_density() -> dict[int, float]:
    out: dict[int, float] = {}
    with IMPERATIVES_CSV.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            out[int(row["surah"])] = float(row["impv_per_verse"])
    return out


def load_phase() -> dict[int, str]:
    out: dict[int, str] = {}
    with REVELATION_CSV.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            out[int(row["mushaf_order"])] = row["noldeke_phase"].strip()
    return out


def load_verse_counts() -> dict[int, int]:
    out: dict[int, int] = {}
    with VERSE_COUNTS.open(encoding="utf-8") as fh:
        for line in fh:
            sid, n = line.strip().split("\t")
            out[int(sid)] = int(n)
    return out


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

    root_counts = load_root_counts()
    imperative_density = load_imperative_density()
    phase = load_phase()
    verse_counts = load_verse_counts()

    def divine_share(sid: int) -> float:
        counts = root_counts[sid]
        total = sum(counts.values())
        if total == 0:
            return 0.0
        divine = sum(counts.get(root, 0) for root in DIVINE_ROOTS)
        return divine / total

    def surah_score(sid: int) -> float:
        d = divine_share(sid)
        i = imperative_density[sid]
        return math.sqrt(d * i)

    def pair_score(a: int, b: int) -> float:
        return surah_score(a) + surah_score(b)

    def matched_pairs_for(target_a: int, target_b: int) -> list[tuple[int, int]]:
        bins = sorted([len_bin(verse_counts[target_a]), len_bin(verse_counts[target_b])])
        phases = sorted([phase[target_a], phase[target_b]])
        out: list[tuple[int, int]] = []
        for a, b in combinations(range(1, 115), 2):
            if sorted([len_bin(verse_counts[a]), len_bin(verse_counts[b])]) != bins:
                continue
            if sorted([phase[a], phase[b]]) != phases:
                continue
            out.append((a, b))
        return out

    target_null_pairs = [
        pair for pair in matched_pairs_for(*TARGET_PAIR) if set(pair) != set(TARGET_PAIR)
    ]
    target_null_scores = [pair_score(*pair) for pair in target_null_pairs]
    target_obs = pair_score(*TARGET_PAIR)
    target_rank_desc = 1 + sum(1 for x in target_null_scores if x > target_obs)

    contrast_null_pairs = [
        pair for pair in matched_pairs_for(*CONTRAST_PAIR) if set(pair) != set(CONTRAST_PAIR)
    ]
    contrast_null_scores = [pair_score(*pair) for pair in contrast_null_pairs]
    contrast_obs = pair_score(*CONTRAST_PAIR)
    contrast_rank_desc = 1 + sum(1 for x in contrast_null_scores if x > contrast_obs)

    out = {
        "id": "H-NEW-273",
        "title": "Q1<->Q108 twin liturgical-anchor test",
        "date": "2026-04-18",
        "seed": 20260418,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_273_q1_q108_twin_liturgical_anchor.py",
        "rules_tuple": (
            "(QAC v0.4 STEM roots via surah-root-graph.json; imperative density via "
            "imperatives-per-surah.csv; divine-reference root set {Alh,rbb,rHm}; "
            "surah score sqrt(divine_share * imperative_density); exact matched-null "
            "over Early-Meccan pairs with target verse bins)"
        ),
        "divine_roots": sorted(DIVINE_ROOTS),
        "surah_scores": {
            str(sid): {
                "divine_share": divine_share(sid),
                "imperative_density_per_verse": imperative_density[sid],
                "score": surah_score(sid),
                "n_root_tokens": sum(root_counts[sid].values()),
                "verse_count": verse_counts[sid],
                "noldeke_phase": phase[sid],
            }
            for sid in sorted({*TARGET_PAIR, *CONTRAST_PAIR, 106, 112})
        },
        "primary_target": {
            "pair": list(TARGET_PAIR),
            "pair_score_obs": target_obs,
            "null_n_pairs": len(target_null_pairs),
            "null_mean": statistics.mean(target_null_scores),
            "null_sd": statistics.stdev(target_null_scores),
            "z_vs_null": z_score(target_obs, target_null_scores),
            "p_exact_upper": exact_upper_p(target_null_scores, target_obs),
            "rank_desc": target_rank_desc,
            "top_null_pairs": [
                {
                    "pair": [a, b],
                    "score": pair_score(a, b),
                }
                for a, b in sorted(
                    target_null_pairs, key=lambda pair: (-pair_score(*pair), pair[0], pair[1])
                )[:10]
            ],
            "matched_pair_space": {
                "phases": sorted([phase[TARGET_PAIR[0]], phase[TARGET_PAIR[1]]]),
                "verse_bins": sorted(
                    [len_bin(verse_counts[TARGET_PAIR[0]]), len_bin(verse_counts[TARGET_PAIR[1]])]
                ),
                "members_by_bin": {
                    "3_4": [
                        sid
                        for sid in range(1, 115)
                        if phase[sid] == "Early Meccan" and len_bin(verse_counts[sid]) == "3_4"
                    ],
                    "5_7": [
                        sid
                        for sid in range(1, 115)
                        if phase[sid] == "Early Meccan" and len_bin(verse_counts[sid]) == "5_7"
                    ],
                },
            },
        },
        "descriptive_contrast": {
            "pair": list(CONTRAST_PAIR),
            "pair_score_obs": contrast_obs,
            "null_n_pairs": len(contrast_null_pairs),
            "null_mean": statistics.mean(contrast_null_scores),
            "null_sd": statistics.stdev(contrast_null_scores),
            "z_vs_null": z_score(contrast_obs, contrast_null_scores),
            "p_exact_upper": exact_upper_p(contrast_null_scores, contrast_obs),
            "rank_desc": contrast_rank_desc,
            "top_null_pairs": [
                {
                    "pair": [a, b],
                    "score": pair_score(a, b),
                }
                for a, b in sorted(
                    contrast_null_pairs,
                    key=lambda pair: (-pair_score(*pair), pair[0], pair[1]),
                )[:10]
            ],
        },
    }

    p_target = out["primary_target"]["p_exact_upper"]
    p_contrast = out["descriptive_contrast"]["p_exact_upper"]
    if p_target < 0.05 and p_contrast < 0.05:
        verdict = "PASS-GENERIC"
    elif p_target < 0.05:
        verdict = "PASS-NARROW"
    else:
        verdict = "NULL"
    out["verdict"] = verdict
    out["verdict_note"] = (
        "Primary target is exact-upper-tail on the matched null. Contrast pair is "
        "reported only to bound genericity; it does not ratify the primary cell."
    )

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print(
        "target",
        f"pair={TARGET_PAIR}",
        f"score={target_obs:.6f}",
        f"p_exact={p_target:.6f}",
        f"rank={target_rank_desc}/{len(target_null_pairs) + 1}",
    )
    print(
        "contrast",
        f"pair={CONTRAST_PAIR}",
        f"score={contrast_obs:.6f}",
        f"p_exact={p_contrast:.6f}",
        f"rank={contrast_rank_desc}/{len(contrast_null_pairs) + 1}",
    )
    print(f"verdict={verdict}")
    print(f"wrote {OUT_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
