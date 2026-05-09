#!/usr/bin/env python3
"""Q077-F-01 — Refrain architecture replication (3-cell test).

Pre-reg: surahs/Q077-al-mursalat/preregs/Q077-F-01-refrain-replication-prereg.md
SHA256: f7539758c75931ea4935da7bedb6c198494fbf19c57aa77ae3cf499b158e0f73

Cell A: count(refrain in Q 77) == 10, cross-tashkeel-consistent.
Cell B: rank Q 77 in corpus by max identical-verse-repeat-count == 2.
Cell C: 10 of corpus_total exact-string-matches concentrate in Q 77 (≥ 90.9%).
"""

import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q077-al-mursalat/preregs/Q077-F-01-refrain-replication-prereg.md"
EXPECTED_SHA = "f7539758c75931ea4935da7bedb6c198494fbf19c57aa77ae3cf499b158e0f73"
QURAN_NT = ROOT / "quran-text/quran-no-tashkeel.json"
QURAN_MIN = ROOT / "quran-text/quran-min-tashkeel.json"
QURAN_FULL = ROOT / "quran-text/quran-full-tashkeel.json"
OUT = ROOT / "surahs/Q077-al-mursalat/csv/Q077-F-01.json"

REFRAIN_NT = "ويل يومئذ للمكذبين"


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def normalize_nt(s: str) -> str:
    """No-tashkeel normalization: NFC + collapse whitespace."""
    s = unicodedata.normalize("NFC", s)
    return " ".join(s.split())


def normalize_variant(s: str) -> str:
    """Normalize across tashkeel variants → reduce to no-tashkeel form.

    Strategy: NFC-recompose first (so ئ stays as a single Lo codepoint U+0626),
    then strip all category=Mn (combining marks). This preserves structural
    hamza-on-yāʾ but removes every fatḥa/kasra/ḍamma/sukūn/shadda/tanwīn/
    alif-khanjariyya/Quranic-annotation mark.
    """
    s = unicodedata.normalize("NFC", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(s.split())


def main() -> None:
    verify_prereg()

    out = {
        "id": "Q077-F-01",
        "title": "Q 77 refrain architecture replication",
        "prereg_sha": EXPECTED_SHA,
        "rules_tuple": "(no-tashkeel, orthographic-token-exact, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    }

    # ---- Cell A: cross-variant exact count in Q 77 ----
    counts_per_variant: dict[str, int] = {}
    refrain_positions: dict[str, list[int]] = {}
    for variant_name, path in [
        ("no-tashkeel", QURAN_NT),
        ("min-tashkeel", QURAN_MIN),
        ("full-tashkeel", QURAN_FULL),
    ]:
        data = json.loads(path.read_text())
        q77 = next(s for s in data if s["id"] == 77)
        positions = []
        for v in q77["verses"]:
            if normalize_variant(v["text"]) == REFRAIN_NT:
                positions.append(v["id"])
        counts_per_variant[variant_name] = len(positions)
        refrain_positions[variant_name] = positions

    cross_consistent = len(set(counts_per_variant.values())) == 1
    cell_A_count_match = counts_per_variant["no-tashkeel"] == 10
    cell_A_pass = cell_A_count_match and cross_consistent

    out["cell_A"] = {
        "target_count": 10,
        "counts_by_variant": counts_per_variant,
        "cross_variant_consistent": cross_consistent,
        "refrain_positions_no_tashkeel": refrain_positions["no-tashkeel"],
        "match_target_10": cell_A_count_match,
        "pass": cell_A_pass,
    }

    # ---- Cell B: corpus rank by max identical-verse-repeat-count ----
    nt_data = json.loads(QURAN_NT.read_text())
    per_surah_max: dict[int, int] = {}
    per_surah_top_string: dict[int, str] = {}
    for s in nt_data:
        verses = [normalize_nt(v["text"]) for v in s["verses"]]
        if verses:
            counter = Counter(verses)
            top, count = counter.most_common(1)[0]
        else:
            top, count = "", 0
        per_surah_max[s["id"]] = count
        per_surah_top_string[s["id"]] = top

    ranking = sorted(range(1, 115), key=lambda s: (-per_surah_max[s], s))
    rank_q77 = ranking.index(77) + 1
    rank_q55 = ranking.index(55) + 1
    rank_q26 = ranking.index(26) + 1

    cell_B_pass = rank_q77 == 2

    out["cell_B"] = {
        "target_rank": 2,
        "obs_rank_q77": rank_q77,
        "obs_max_count_q77": per_surah_max[77],
        "rank_q55_ref": rank_q55,
        "rank_q26_ref": rank_q26,
        "max_count_q55_ref": per_surah_max[55],
        "max_count_q26_ref": per_surah_max[26],
        "top_5_ranking": [
            {"rank": i + 1, "surah": s, "max_count": per_surah_max[s], "top_string": per_surah_top_string[s][:80]}
            for i, s in enumerate(ranking[:5])
        ],
        "match_target_2": cell_B_pass,
        "pass": cell_B_pass,
    }

    # ---- Cell C: corpus-wide refrain concentration in Q 77 ----
    corpus_exact_count = 0
    corpus_exact_locations: list[dict] = []
    for s in nt_data:
        for v in s["verses"]:
            if normalize_nt(v["text"]) == REFRAIN_NT:
                corpus_exact_count += 1
                corpus_exact_locations.append({"surah": s["id"], "verse": v["id"]})

    q77_exact = sum(1 for loc in corpus_exact_locations if loc["surah"] == 77)
    concentration = q77_exact / corpus_exact_count if corpus_exact_count else 0.0
    cell_C_pass = concentration >= 0.909  # ≥ 10/11

    # Also: prefix-fa near-echo check
    prefix_fa_echoes: list[dict] = []
    for s in nt_data:
        for v in s["verses"]:
            nv = normalize_nt(v["text"])
            if nv == "فويل يومئذ للمكذبين":
                prefix_fa_echoes.append({"surah": s["id"], "verse": v["id"], "text": nv})

    out["cell_C"] = {
        "target_concentration_min": 0.909,
        "corpus_exact_total": corpus_exact_count,
        "q77_exact_count": q77_exact,
        "concentration_q77": concentration,
        "all_exact_locations": corpus_exact_locations,
        "prefix_fa_near_echoes": prefix_fa_echoes,
        "pass": cell_C_pass,
    }

    # ---- Combined verdict ----
    n_pass = int(cell_A_pass) + int(cell_B_pass) + int(cell_C_pass)
    if n_pass == 3:
        verdict = "PASS-DIRECTED FULL (replication of H-NEW-1320)"
    elif n_pass == 2:
        verdict = "PASS-DIRECTED PARTIAL (2/3)"
    elif n_pass == 1:
        verdict = "NULL-DIRECTED (1/3)"
    else:
        verdict = "NULL"

    out["verdict_summary"] = {
        "n_cells_pass": n_pass,
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Cell A (count==10, cross-variant): {counts_per_variant} consistent={cross_consistent}")
    print(f"Cell B (rank==2): rank_q77={rank_q77}, max_count={per_surah_max[77]}")
    print(f"Cell C (concentration ≥ 0.909): {q77_exact}/{corpus_exact_count} = {concentration:.4f}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
