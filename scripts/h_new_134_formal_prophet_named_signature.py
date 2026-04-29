#!/usr/bin/env python3
"""H-NEW-134-FORMAL — prophet-named surah signature beyond name-root enrichment.

Primary family:
  A. vocative particle share (`يا`)
  B. narrative-sequencer share (`اذ`, `واذ`, `ثم`, `فلما`, `لما`)

Null:
  exact slot-matched permutation by
    revelation type × verse-count band × muq status

Outputs:
  findings/phase-b-hypotheses/csv/h-new-134-formal.json
"""
from __future__ import annotations

import hashlib
import json
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
PREREG_MD = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-134-formal-prophet-named-signature-prereg.md"
)
OUTPUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-134-formal.json"

SEED = 20260418
N_PERM = 100000
BONFERRONI_K = 2
ALPHA_BON = 0.05 / BONFERRONI_K
MW5_THRESHOLD = 0.01

STRICT_IDS = [10, 11, 12, 14, 47, 71]
EXPANDED_IDS = [10, 11, 12, 14, 19, 31, 47, 71]
MUQ_SURAHS = {
    2,
    3,
    7,
    10,
    11,
    12,
    13,
    14,
    15,
    19,
    20,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    36,
    38,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    50,
    68,
}

VOCATIVE_TOKEN = "يا"
SEQUENCER_TOKENS = {"اذ", "واذ", "ثم", "فلما", "لما"}
SPEECH_TOKENS = {
    "قال",
    "قالوا",
    "قالت",
    "قالا",
    "قيل",
    "قل",
    "قلنا",
    "يقول",
    "يقولون",
    "تقول",
    "نقول",
}


def verse_band(total_verses: int) -> str:
    if total_verses >= 100:
        return "100+"
    if total_verses >= 50:
        return "50-99"
    if total_verses >= 20:
        return "20-49"
    return "1-19"


def mean(values: list[float]) -> float:
    return statistics.mean(values) if values else 0.0


def stdev(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def build_surah_rows() -> list[dict]:
    corpus = json.loads(QURAN_JSON.read_text(encoding="utf-8"))
    rows = []
    for surah in corpus:
        sid = surah["id"]
        verses = surah["verses"]
        n_verses = len(verses)
        vocative_hits = 0
        sequencer_hits = 0
        speech_hits = 0

        for verse in verses:
            tokens = verse["text"].split()
            token_set = set(tokens)
            if VOCATIVE_TOKEN in token_set:
                vocative_hits += 1
            if token_set & SEQUENCER_TOKENS:
                sequencer_hits += 1
            if token_set & SPEECH_TOKENS:
                speech_hits += 1

        rows.append(
            {
                "sid": sid,
                "name_ar": surah["name"],
                "name_tl": surah["transliteration"],
                "type": surah["type"],
                "total_verses": n_verses,
                "band": verse_band(n_verses),
                "muq_status": "muq" if sid in MUQ_SURAHS else "nonmuq",
                "vocative_count": vocative_hits,
                "vocative_share": vocative_hits / n_verses,
                "sequencer_count": sequencer_hits,
                "sequencer_share": sequencer_hits / n_verses,
                "speech_count": speech_hits,
                "speech_share": speech_hits / n_verses,
            }
        )
    return rows


def slot_key(row: dict) -> tuple[str, str, str]:
    return row["type"], row["band"], row["muq_status"]


def slot_counter(rows: list[dict]) -> dict[str, int]:
    counts = Counter(slot_key(row) for row in rows)
    return {
        f"{key[0]}|{key[1]}|{key[2]}": value
        for key, value in sorted(counts.items(), key=lambda item: item[0])
    }


def slot_pool_sizes(
    all_rows: list[dict], target_rows: list[dict]
) -> dict[str, dict[str, int]]:
    target_ids = {row["sid"] for row in target_rows}
    counts = Counter(slot_key(row) for row in target_rows)
    out = {}
    for key, need in sorted(counts.items(), key=lambda item: item[0]):
        available = sum(
            1
            for row in all_rows
            if slot_key(row) == key and row["sid"] not in target_ids
        )
        out[f"{key[0]}|{key[1]}|{key[2]}"] = {
            "needed": need,
            "available_non_target": available,
        }
    return out


def permutation_axis(
    all_rows: list[dict],
    target_rows: list[dict],
    feature_name: str,
    seed: int,
) -> dict:
    target_ids = {row["sid"] for row in target_rows}
    target_slots = [slot_key(row) for row in target_rows]
    pools = defaultdict(list)
    for row in all_rows:
        if row["sid"] in target_ids:
            continue
        pools[slot_key(row)].append(row)

    observed = mean([row[feature_name] for row in target_rows])
    null_means: list[float] = []
    rng = random.Random(seed)

    for _ in range(N_PERM):
        used = set()
        chosen_values = []
        for key in target_slots:
            pool = pools[key]
            idx = rng.randrange(len(pool))
            while pool[idx]["sid"] in used:
                idx = rng.randrange(len(pool))
            used.add(pool[idx]["sid"])
            chosen_values.append(pool[idx][feature_name])
        null_means.append(mean(chosen_values))

    ge_count = sum(1 for value in null_means if value >= observed)
    p_upper = (ge_count + 1) / (N_PERM + 1)
    null_mean = mean(null_means)
    null_sd = stdev(null_means)
    z = (observed - null_mean) / null_sd if null_sd else 0.0

    return {
        "feature": feature_name,
        "observed_mean": observed,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "z_vs_null": z,
        "p_upper": p_upper,
        "n_perm": N_PERM,
        "passes_alpha_bon": p_upper < ALPHA_BON,
    }


def evaluate_set(
    all_rows: list[dict],
    ids: list[int],
    axis_features: list[str],
    speech_seed_offset: int,
) -> dict:
    id_set = set(ids)
    target_rows = [row for row in all_rows if row["sid"] in id_set]
    target_rows.sort(key=lambda row: row["sid"])

    axes = {}
    for idx, feature in enumerate(axis_features):
        axes[feature] = permutation_axis(
            all_rows=all_rows,
            target_rows=target_rows,
            feature_name=feature,
            seed=SEED + speech_seed_offset + idx,
        )

    speech = permutation_axis(
        all_rows=all_rows,
        target_rows=target_rows,
        feature_name="speech_share",
        seed=SEED + speech_seed_offset + 50,
    )

    return {
        "surah_ids": ids,
        "surah_table": [
            {
                "sid": row["sid"],
                "name_tl": row["name_tl"],
                "type": row["type"],
                "total_verses": row["total_verses"],
                "band": row["band"],
                "muq_status": row["muq_status"],
                "vocative_share": row["vocative_share"],
                "sequencer_share": row["sequencer_share"],
                "speech_share": row["speech_share"],
            }
            for row in target_rows
        ],
        "slot_profile": slot_counter(target_rows),
        "slot_pool_sizes": slot_pool_sizes(all_rows, target_rows),
        "primary_axes": axes,
        "speech_auxiliary": speech,
    }


def build_mw5_planted(all_rows: list[dict]) -> dict:
    strict_rows = [row for row in all_rows if row["sid"] in set(STRICT_IDS)]
    counts = Counter(slot_key(row) for row in strict_rows)
    strict_id_set = set(STRICT_IDS)

    planted = []
    for key, need in sorted(counts.items(), key=lambda item: item[0]):
        candidates = [
            row
            for row in all_rows
            if slot_key(row) == key and row["sid"] not in strict_id_set
        ]
        candidates.sort(
            key=lambda row: (
                row["vocative_share"] + row["sequencer_share"],
                row["sequencer_share"],
                row["vocative_share"],
                -row["sid"],
            ),
            reverse=True,
        )
        planted.extend(candidates[:need])

    planted.sort(key=lambda row: row["sid"])
    planted_ids = [row["sid"] for row in planted]
    evaluation = evaluate_set(
        all_rows=all_rows,
        ids=planted_ids,
        axis_features=["vocative_share", "sequencer_share"],
        speech_seed_offset=200,
    )

    return {
        "planted_ids": planted_ids,
        "planted_table": [
            {
                "sid": row["sid"],
                "name_tl": row["name_tl"],
                "slot": f"{row['type']}|{row['band']}|{row['muq_status']}",
                "vocative_share": row["vocative_share"],
                "sequencer_share": row["sequencer_share"],
                "composite": row["vocative_share"] + row["sequencer_share"],
            }
            for row in planted
        ],
        "evaluation": evaluation,
    }


def primary_verdict(primary_axes: dict, mw5: dict) -> str:
    mw5_axes = mw5["evaluation"]["primary_axes"]
    mw5_ok = all(axis["p_upper"] < MW5_THRESHOLD for axis in mw5_axes.values())
    if not mw5_ok:
        return "INSTRUMENT-BROKEN"

    pass_count = sum(1 for axis in primary_axes.values() if axis["passes_alpha_bon"])
    if pass_count == 2:
        return "PASS-DIRECTED"
    if pass_count == 1:
        return "PARTIAL-PASS-DIRECTED"
    return "NULL"


def main() -> None:
    prereg_sha = hashlib.sha256(PREREG_MD.read_bytes()).hexdigest()
    all_rows = build_surah_rows()

    strict = evaluate_set(
        all_rows=all_rows,
        ids=STRICT_IDS,
        axis_features=["vocative_share", "sequencer_share"],
        speech_seed_offset=0,
    )
    expanded = evaluate_set(
        all_rows=all_rows,
        ids=EXPANDED_IDS,
        axis_features=["vocative_share", "sequencer_share"],
        speech_seed_offset=100,
    )
    mw5 = build_mw5_planted(all_rows)

    verdict = primary_verdict(strict["primary_axes"], mw5)

    payload = {
        "id": "H-NEW-134-FORMAL",
        "title": (
            "Prophet-named surahs show a conservative surface-form narrative "
            "signature beyond name-root enrichment"
        ),
        "date": "2026-04-18",
        "seed": SEED,
        "n_perm": N_PERM,
        "prereg_sha256": prereg_sha,
        "bonferroni": {
            "family": "h-new-134-formal-prophet-named-signature",
            "k": BONFERRONI_K,
            "alpha_bon": ALPHA_BON,
        },
        "primary_set": {
            "definition": "strict explicit prophet-name titles only",
            "surah_ids": STRICT_IDS,
            "n": len(STRICT_IDS),
        },
        "sensitivity_set": {
            "definition": "expanded named-human-figure sensitivity",
            "surah_ids": EXPANDED_IDS,
            "n": len(EXPANDED_IDS),
        },
        "marker_definitions": {
            "vocative_share": sorted([VOCATIVE_TOKEN]),
            "sequencer_share": sorted(SEQUENCER_TOKENS),
            "speech_share_auxiliary": sorted(SPEECH_TOKENS),
        },
        "strict_primary": strict,
        "expanded_sensitivity": expanded,
        "mw5_positive_control": mw5,
        "verdict": verdict,
    }

    OUTPUT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"[H-NEW-134-FORMAL] prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(
        f"[H-NEW-134-FORMAL] strict vocative p={strict['primary_axes']['vocative_share']['p_upper']:.6f}",
        file=sys.stderr,
    )
    print(
        f"[H-NEW-134-FORMAL] strict sequencer p={strict['primary_axes']['sequencer_share']['p_upper']:.6f}",
        file=sys.stderr,
    )
    print(
        f"[H-NEW-134-FORMAL] verdict={verdict}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
