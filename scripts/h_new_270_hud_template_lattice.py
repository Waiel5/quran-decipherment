#!/usr/bin/env python3
"""H-NEW-270 — formal Q11 Hud opener-template lattice test."""

from __future__ import annotations

import hashlib
import json
import random
import re
import statistics
from collections import Counter
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
TEXT_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG_PATH = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-270-hud-template-lattice-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-270.json"

SEED = 20260418
N_PERM = 10_000
MATCH_K = 12
BON_K = 3
ALPHA_BON = 0.05 / BON_K

ARABIC_TOKEN_RE = re.compile(r"[\u0621-\u064A\u0671]+")

PROPHET_TOKENS = {
    "نوحا",
    "هودا",
    "صالحا",
    "شعيبا",
    "إبراهيم",
    "لوطا",
    "موسى",
    "نوح",
    "هود",
    "صالح",
    "شعيب",
    "لوط",
}

TRIBE_TOKENS = {
    "عاد",
    "ثمود",
    "مدين",
}

TARGET = {
    "surah": 11,
    "name": "Hud",
    "opener_verse_ids": [25, 50, 61, 69, 77, 84, 96],
}

MW5 = {
    "surah": 7,
    "name": "Al-A'raf",
    "opener_verse_ids": [59, 65, 73, 80, 85, 103],
}

COMPARATORS = [
    {
        "surah": 26,
        "name": "Ash-Shu'ara",
        "opener_verse_ids": [10, 69, 105, 123, 141, 160, 176],
    },
    {
        "surah": 54,
        "name": "Al-Qamar",
        "opener_verse_ids": [9, 18, 23, 33, 41],
    },
    {
        "surah": 71,
        "name": "Nuh",
        "opener_verse_ids": [1],
    },
]

CELLS = [
    {
        "cell": "A",
        "prefix_len": 4,
        "label": "bare slot-template stem",
        "template_gloss": "wa-ila [TRIBE] akhahum [PROPHET]",
    },
    {
        "cell": "B",
        "prefix_len": 8,
        "label": "vocative-imperative continuation",
        "template_gloss": "wa-ila [TRIBE] akhahum [PROPHET] qala ya qawm u'budu",
    },
    {
        "cell": "C",
        "prefix_len": 12,
        "label": "monotheism-clause continuation",
        "template_gloss": (
            "wa-ila [TRIBE] akhahum [PROPHET] qala ya qawm u'budu Allah ma lakum min"
        ),
    },
]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_surahs() -> dict[int, dict]:
    data = json.loads(TEXT_PATH.read_text(encoding="utf-8"))
    surahs = {}
    for surah in data:
        sid = int(surah["id"])
        verses = {}
        for verse in surah["verses"]:
            vid = int(verse["id"])
            raw_tokens = ARABIC_TOKEN_RE.findall(verse["text"])
            abstract_tokens = []
            for tok in raw_tokens:
                if tok in PROPHET_TOKENS:
                    abstract_tokens.append("[PROPHET]")
                elif tok in TRIBE_TOKENS:
                    abstract_tokens.append("[TRIBE]")
                else:
                    abstract_tokens.append(tok)
            verses[vid] = {
                "text": verse["text"],
                "raw_tokens": raw_tokens,
                "abstract_tokens": abstract_tokens,
                "token_count": len(raw_tokens),
            }
        surahs[sid] = {
            "name": surah["transliteration"],
            "verse_count": len(surah["verses"]),
            "verses": verses,
        }
    return surahs


def build_candidate_lists(
    surah_data: dict,
    opener_ids: list[int],
    match_k: int,
) -> dict[int, list[int]]:
    verse_meta = surah_data["verses"]
    out = {}
    for opener_vid in opener_ids:
        target_len = verse_meta[opener_vid]["token_count"]
        others = [vid for vid in verse_meta if vid not in opener_ids]
        others.sort(
            key=lambda vid: (
                abs(verse_meta[vid]["token_count"] - target_len),
                abs(vid - opener_vid),
                vid,
            )
        )
        out[opener_vid] = others[:match_k]
    return out


def sample_matched_set(
    opener_ids: list[int],
    candidate_lists: dict[int, list[int]],
    rng: random.Random,
    max_attempts: int = 200,
) -> list[int] | None:
    for _ in range(max_attempts):
        used = set()
        chosen = []
        remaining = list(opener_ids)
        ok = True
        while remaining:
            remaining.sort(
                key=lambda vid: (
                    sum(1 for cand in candidate_lists[vid] if cand not in used),
                    vid,
                )
            )
            opener_vid = remaining.pop(0)
            choices = [cand for cand in candidate_lists[opener_vid] if cand not in used]
            if not choices:
                ok = False
                break
            pick = rng.choice(choices)
            used.add(pick)
            chosen.append(pick)
        if ok:
            return chosen
    return None


def template_counts_for_prefix_len(
    surah_data: dict,
    verse_ids: list[int],
    prefix_len: int,
) -> Counter:
    counts = Counter()
    for vid in verse_ids:
        prefix = tuple(surah_data["verses"][vid]["abstract_tokens"][:prefix_len])
        counts[prefix] += 1
    return counts


def winning_templates(
    surah_id: int,
    surah_data: dict,
    verse_ids: list[int],
    prefix_len: int,
) -> list[dict]:
    counts = template_counts_for_prefix_len(surah_data, verse_ids, prefix_len)
    if not counts:
        return []
    max_count = max(counts.values())
    winners = []
    for template in sorted(counts):
        if counts[template] != max_count:
            continue
        member_ids = []
        for vid in verse_ids:
            prefix = tuple(surah_data["verses"][vid]["abstract_tokens"][:prefix_len])
            if prefix == template:
                member_ids.append(vid)
        winners.append(
            {
                "template_tokens": list(template),
                "template_string": " ".join(template),
                "count": counts[template],
                "member_verse_ids": member_ids,
                "member_texts": [
                    {
                        "verse": f"{surah_id}:{vid}",
                        "text": surah_data["verses"][vid]["text"],
                    }
                    for vid in member_ids
                ],
            }
        )
    return winners


def max_template_multiplicity(
    surah_data: dict,
    verse_ids: list[int],
    prefix_len: int,
) -> int:
    counts = template_counts_for_prefix_len(surah_data, verse_ids, prefix_len)
    return max(counts.values()) if counts else 0


def null_test(
    surah_id: int,
    opener_ids: list[int],
    prefix_len: int,
    surahs: dict[int, dict],
    seed: int,
) -> dict:
    surah_data = surahs[surah_id]
    candidate_lists = build_candidate_lists(surah_data, opener_ids, MATCH_K)
    rng = random.Random(seed)

    observed = max_template_multiplicity(surah_data, opener_ids, prefix_len)
    null_values = []
    failures = 0

    for _ in range(N_PERM):
        sample = sample_matched_set(opener_ids, candidate_lists, rng)
        if sample is None:
            failures += 1
            continue
        null_values.append(max_template_multiplicity(surah_data, sample, prefix_len))

    if not null_values:
        raise RuntimeError(f"Zero successful matched draws for surah {surah_id}")

    null_mean = statistics.mean(null_values)
    null_sd = statistics.stdev(null_values) if len(null_values) > 1 else 0.0
    null_counts = Counter(null_values)
    p_upper = (1 + sum(v >= observed for v in null_values)) / (1 + len(null_values))
    q95_index = max(0, int(0.95 * len(null_values)) - 1)
    q95 = sorted(null_values)[q95_index]

    return {
        "surah_id": surah_id,
        "surah_name": surah_data["name"],
        "opener_verse_ids": opener_ids,
        "opener_texts": [
            {"verse": f"{surah_id}:{vid}", "text": surah_data["verses"][vid]["text"]}
            for vid in opener_ids
        ],
        "candidate_lists": {
            str(vid): candidate_lists[vid] for vid in opener_ids
        },
        "observed_max_template_count": observed,
        "null_mean": null_mean,
        "null_median": statistics.median(null_values),
        "null_q95": q95,
        "null_sd": null_sd,
        "p_perm_upper": p_upper,
        "z_vs_null": (
            (observed - null_mean) / null_sd if null_sd > 0 else None
        ),
        "null_count_histogram": {
            str(key): value for key, value in sorted(null_counts.items())
        },
        "successful_draws": len(null_values),
        "failed_draws": failures,
        "winning_templates": winning_templates(
            surah_id,
            surah_data,
            opener_ids,
            prefix_len,
        ),
    }


def build_cell_result(
    surah_id: int,
    opener_ids: list[int],
    cell_spec: dict,
    surahs: dict[int, dict],
    seed_offset: int,
) -> dict:
    res = null_test(
        surah_id=surah_id,
        opener_ids=opener_ids,
        prefix_len=cell_spec["prefix_len"],
        surahs=surahs,
        seed=SEED + seed_offset,
    )
    return {
        "cell": cell_spec["cell"],
        "prefix_len": cell_spec["prefix_len"],
        "label": cell_spec["label"],
        "template_gloss": cell_spec["template_gloss"],
        "observed_max_template_count": res["observed_max_template_count"],
        "null_mean": res["null_mean"],
        "null_median": res["null_median"],
        "null_q95": res["null_q95"],
        "null_sd": res["null_sd"],
        "p_perm_upper": res["p_perm_upper"],
        "z_vs_null": res["z_vs_null"],
        "pass_alpha_bon": res["p_perm_upper"] < ALPHA_BON,
        "successful_draws": res["successful_draws"],
        "failed_draws": res["failed_draws"],
        "winning_templates": res["winning_templates"],
        "opener_texts": res["opener_texts"],
        "candidate_lists": res["candidate_lists"],
        "null_count_histogram": res["null_count_histogram"],
    }


def summary_row_from_cells(label: str, cells: list[dict]) -> dict:
    row = {"label": label}
    for cell in cells:
        row[cell["cell"]] = {
            "observed_max_template_count": cell["observed_max_template_count"],
            "p_perm_upper": cell["p_perm_upper"],
            "z_vs_null": cell["z_vs_null"],
        }
    return row


def main() -> None:
    surahs = load_surahs()

    target_cells = [
        build_cell_result(
            surah_id=TARGET["surah"],
            opener_ids=TARGET["opener_verse_ids"],
            cell_spec=cell,
            surahs=surahs,
            seed_offset=100 * idx + 1,
        )
        for idx, cell in enumerate(CELLS)
    ]

    mw5_cells = [
        build_cell_result(
            surah_id=MW5["surah"],
            opener_ids=MW5["opener_verse_ids"],
            cell_spec=cell,
            surahs=surahs,
            seed_offset=100 * idx + 1001,
        )
        for idx, cell in enumerate(CELLS)
    ]

    comparator_rows = []
    for comp_idx, comp in enumerate(COMPARATORS):
        comp_cells = [
            build_cell_result(
                surah_id=comp["surah"],
                opener_ids=comp["opener_verse_ids"],
                cell_spec=cell,
                surahs=surahs,
                seed_offset=10_000 + 1000 * comp_idx + 100 * idx + 1,
            )
            for idx, cell in enumerate(CELLS)
        ]
        comparator_rows.append(
            {
                "surah": comp["surah"],
                "name": comp["name"],
                "opener_verse_ids": comp["opener_verse_ids"],
                "cells": comp_cells,
            }
        )

    n_pass = sum(1 for cell in target_cells if cell["pass_alpha_bon"])
    mw5_valid = all(cell["p_perm_upper"] < 0.05 for cell in mw5_cells)

    if not mw5_valid:
        verdict = "NULL-BROKEN"
    elif n_pass == len(CELLS):
        verdict = "PASS-DIRECTED"
    elif n_pass > 0:
        verdict = "PARTIAL-PASS"
    else:
        verdict = "NULL"

    payload = {
        "id": "H-NEW-270",
        "title": "Q11 Hud opener-template lattice",
        "date": "2026-04-18",
        "seed": SEED,
        "prereg_file": str(PREREG_PATH.relative_to(ROOT)),
        "prereg_sha256": sha256_file(PREREG_PATH),
        "script_file": "scripts/h_new_270_hud_template_lattice.py",
        "bonferroni_family": "h-new-270-hud-template-lattice",
        "bonferroni_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "n_perm": N_PERM,
        "match_k_nearest": MATCH_K,
        "question": (
            "Do the frozen Q11 narrative-chain opener verses contain a non-random "
            "slot-template clique of the wa-ila [TRIBE] akhahum [PROPHET] type, "
            "measured at three fixed prefix depths against a within-surah "
            "length-matched verse-set null?"
        ),
        "rules_tuple": (
            "(quran-no-tashkeel; frozen Q11 opener verses 11:25/50/61/69/77/84/96; "
            "Arabic-token extraction by regex; slot abstraction on prophet names "
            "and tribe ethnonyms only; statistic = max multiplicity of identical "
            "abstracted prefix among opener verses; matched null = 12 nearest "
            "non-opener verses by token count within same surah, sampled without "
            "replacement; N_PERM=10000; seed=20260418)"
        ),
        "target": TARGET,
        "mw5_positive_control": MW5,
        "cells": target_cells,
        "mw5_cells": mw5_cells,
        "comparators": comparator_rows,
        "summary_rows": [
            summary_row_from_cells("Q11 target", target_cells),
            summary_row_from_cells("Q7 MW-5", mw5_cells),
            *[
                summary_row_from_cells(
                    f'Q{row["surah"]} {row["name"]}',
                    row["cells"],
                )
                for row in comparator_rows
            ],
        ],
        "n_target_cells_pass_alpha_bon": n_pass,
        "mw5_all_cells_pass_nominal": mw5_valid,
        "verdict": verdict,
        "verdict_ceiling": "PASS-DIRECTED",
        "post_hoc_scope_note": (
            "This is a formal follow-up to the already-noticed H-NEW-90/HANDOFF "
            "Q11 opener-lattice signal. The target family was not discovered here."
        ),
    }

    OUT_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print("H-NEW-270 — Q11 Hud opener-template lattice")
    print(f"  verdict: {verdict}")
    print(f"  target cells passing Bonferroni: {n_pass}/{len(CELLS)}")
    for cell in target_cells:
        z_text = "n/a" if cell["z_vs_null"] is None else f'{cell["z_vs_null"]:.3f}'
        print(
            f'  cell {cell["cell"]}: obs={cell["observed_max_template_count"]} '
            f'p={cell["p_perm_upper"]:.4g} z={z_text}'
        )
    print(f"  MW-5 valid: {mw5_valid}")


if __name__ == "__main__":
    main()
