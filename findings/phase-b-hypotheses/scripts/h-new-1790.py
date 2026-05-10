#!/usr/bin/env python3
"""H-NEW-1790 — Refrain-architecture full corpus inventory.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1790-refrain-inventory.md
SHA256:  1687591022153584cf745bd83855fd907387ac0afa2978475131bb1e071dd3e4

Strict refrain : verse repeated verbatim >= 3 times within its surah.
Broad refrain  : verse repeated verbatim >= 2 times within its surah.

Outputs the complete inventory + saturation-ranked top-10 + cross-surah
refrain-pair table (post-hoc supplement, MW-7 single-test cap).
"""

import hashlib
import json
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1790-refrain-inventory.md"
EXPECTED_SHA = "1687591022153584cf745bd83855fd907387ac0afa2978475131bb1e071dd3e4"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-1790.json"


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}...")


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = " ".join(s.split())
    return s


def main() -> None:
    verify_prereg()
    text = json.loads(QURAN.read_text())
    verses_per_surah: dict[int, list[str]] = {}
    surah_names: dict[int, str] = {}
    for entry in text:
        s = int(entry["id"])
        verses_per_surah[s] = [normalize(v["text"]) for v in entry["verses"]]
        surah_names[s] = entry.get("transliteration", f"Q{s}")

    # ---- per-surah inventory ----
    per_surah: dict[int, dict] = {}
    for s in range(1, 115):
        vs = verses_per_surah[s]
        n_verses = len(vs)
        counter = Counter(vs)
        max_rc = max(counter.values()) if counter else 0
        # strict: verses with freq >= 3
        strict_refrains = [(v, c) for v, c in counter.items() if c >= 3]
        strict_refrains.sort(key=lambda x: (-x[1], x[0]))
        # broad: verses with freq >= 2
        broad_refrains = [(v, c) for v, c in counter.items() if c >= 2]
        broad_refrains.sort(key=lambda x: (-x[1], x[0]))
        saturation = max_rc / n_verses if n_verses else 0.0
        per_surah[s] = {
            "surah": s,
            "name": surah_names[s],
            "n_verses": n_verses,
            "max_repeat_count": max_rc,
            "saturation": saturation,
            "n_strict_refrains": len(strict_refrains),
            "n_broad_refrains": len(broad_refrains),
            "strict_refrains": [
                {"verse_text": v, "count": c} for v, c in strict_refrains
            ],
            "broad_refrains_count_only": [
                {"verse_text": v[:80], "count": c} for v, c in broad_refrains
            ],
            "broad_refrain_total_occurrences": sum(c for v, c in broad_refrains),
        }

    # ---- ranking by saturation (Cell A) ----
    ranking_sat = sorted(
        range(1, 115),
        key=lambda s: (-per_surah[s]["saturation"], -per_surah[s]["max_repeat_count"], s),
    )
    rank_q55_sat = ranking_sat.index(55) + 1
    q55_sat = per_surah[55]["saturation"]

    # ranking by absolute max_repeat (replicates H-NEW-1320 sanity check)
    ranking_count = sorted(
        range(1, 115),
        key=lambda s: (-per_surah[s]["max_repeat_count"], s),
    )

    # ---- Cell B: count of surahs with strict refrains ----
    strict_surahs = [s for s in range(1, 115) if per_surah[s]["n_strict_refrains"] >= 1]
    n_strict = len(strict_surahs)

    # ---- Verdicts ----
    cell_a_pass = rank_q55_sat == 1
    cell_b_pass = 5 <= n_strict <= 15

    if cell_a_pass and cell_b_pass:
        verdict = "PASS-DIRECTED FULL"
    elif cell_a_pass and not cell_b_pass:
        verdict = "PASS-DIRECTED CELL-A only"
    elif (not cell_a_pass) and cell_b_pass:
        verdict = "PARTIAL (Cell B only)"
    else:
        verdict = "NULL"

    # ---- Top-10 by saturation ----
    top10_sat = []
    for i, s in enumerate(ranking_sat[:10]):
        ps = per_surah[s]
        top_str = ""
        top_ct = ps["max_repeat_count"]
        if ps["broad_refrains_count_only"]:
            top_str = ps["broad_refrains_count_only"][0]["verse_text"]
        top10_sat.append(
            {
                "rank": i + 1,
                "surah": s,
                "name": ps["name"],
                "n_verses": ps["n_verses"],
                "max_repeat_count": top_ct,
                "saturation": ps["saturation"],
                "top_refrain_text": top_str,
                "n_strict_refrains": ps["n_strict_refrains"],
                "n_broad_refrains": ps["n_broad_refrains"],
            }
        )

    # ---- Top-10 by absolute count (replicates H-NEW-1320) ----
    top10_count = []
    for i, s in enumerate(ranking_count[:10]):
        ps = per_surah[s]
        top_str = ""
        top_ct = ps["max_repeat_count"]
        if ps["broad_refrains_count_only"]:
            top_str = ps["broad_refrains_count_only"][0]["verse_text"]
        top10_count.append(
            {
                "rank": i + 1,
                "surah": s,
                "name": ps["name"],
                "n_verses": ps["n_verses"],
                "max_repeat_count": top_ct,
                "saturation": ps["saturation"],
                "top_refrain_text": top_str,
            }
        )

    # ---- Cross-surah refrain-pair table (post-hoc supplement, MW-7) ----
    # Build: verse_text -> {surah: count} where the verse appears in >= 2 distinct surahs.
    cross_index: dict[str, dict[int, int]] = defaultdict(dict)
    for s in range(1, 115):
        c = Counter(verses_per_surah[s])
        for v, ct in c.items():
            cross_index[v][s] = ct
    # filter to verses present in >= 2 distinct surahs
    cross_surah_pairs = []
    for v, surah_counts in cross_index.items():
        if len(surah_counts) >= 2:
            total_occ = sum(surah_counts.values())
            cross_surah_pairs.append(
                {
                    "verse_text": v,
                    "verse_text_short": v[:80],
                    "n_surahs": len(surah_counts),
                    "total_occurrences": total_occ,
                    "surah_counts": dict(sorted(surah_counts.items())),
                }
            )
    cross_surah_pairs.sort(
        key=lambda x: (-x["n_surahs"], -x["total_occurrences"], x["verse_text_short"])
    )

    # ---- strict-refrain enumeration: each refrain-bearing surah's strict refrains ----
    strict_inventory = []
    for s in strict_surahs:
        ps = per_surah[s]
        strict_inventory.append(
            {
                "surah": s,
                "name": ps["name"],
                "n_verses": ps["n_verses"],
                "strict_refrains": ps["strict_refrains"],
                "max_repeat_count": ps["max_repeat_count"],
                "saturation": ps["saturation"],
            }
        )
    strict_inventory.sort(key=lambda x: (-x["max_repeat_count"], x["surah"]))

    # ---- compose output ----
    out = {
        "id": "H-NEW-1790",
        "title": "Refrain-architecture full corpus inventory",
        "prereg_sha": EXPECTED_SHA,
        "rules_tuple": {
            "orthography": "no-tashkeel",
            "verse_equality": "exact-NFC-whitespace-normalized",
            "basmala_policy": "data-file-driven (counted only where verse 1 carries it)",
            "reading_tradition": "hafs-kufan",
        },
        "cell_A_q55_saturation_rank_1": {
            "q55_saturation": q55_sat,
            "q55_rank_by_saturation": rank_q55_sat,
            "pass": cell_a_pass,
        },
        "cell_B_n_strict_in_5_to_15": {
            "n_strict_surahs": n_strict,
            "strict_surahs": strict_surahs,
            "window": [5, 15],
            "pass": cell_b_pass,
        },
        "verdict": verdict,
        "top10_by_saturation": top10_sat,
        "top10_by_absolute_count": top10_count,
        "strict_refrain_inventory": strict_inventory,
        "cross_surah_refrain_pairs": cross_surah_pairs,
        "n_cross_surah_pairs": len(cross_surah_pairs),
        "per_surah_summary": [
            {
                "surah": s,
                "n_verses": per_surah[s]["n_verses"],
                "max_repeat_count": per_surah[s]["max_repeat_count"],
                "saturation": per_surah[s]["saturation"],
                "n_strict_refrains": per_surah[s]["n_strict_refrains"],
                "n_broad_refrains": per_surah[s]["n_broad_refrains"],
                "broad_refrain_total_occurrences": per_surah[s]["broad_refrain_total_occurrences"],
            }
            for s in range(1, 115)
        ],
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nVerdict: {verdict}")
    print(f"Cell A — Q 55 saturation = {q55_sat:.4f}; rank = {rank_q55_sat}/114")
    print(f"Cell B — N_strict = {n_strict}; window [5, 15] -> pass = {cell_b_pass}")
    print(f"\nStrict-refrain surahs ({n_strict}): {strict_surahs}")
    print("\nTop-10 by saturation:")
    for r in top10_sat:
        print(
            f"  #{r['rank']:>2} Q {r['surah']:>3} {r['name'][:18]:>18}  "
            f"sat={r['saturation']:.3f}  max_rc={r['max_repeat_count']:>2}  "
            f"n_strict={r['n_strict_refrains']}  '{r['top_refrain_text'][:60]}'"
        )
    print("\nTop-10 by absolute count (H-NEW-1320 replication check):")
    for r in top10_count:
        print(
            f"  #{r['rank']:>2} Q {r['surah']:>3} {r['name'][:18]:>18}  "
            f"max_rc={r['max_repeat_count']:>2}  sat={r['saturation']:.3f}  "
            f"'{r['top_refrain_text'][:60]}'"
        )
    print(f"\nCross-surah refrain-pairs (verses present in >=2 surahs): {len(cross_surah_pairs)}")
    for cp in cross_surah_pairs[:15]:
        print(
            f"  surahs={list(cp['surah_counts'].keys())}  total={cp['total_occurrences']}  "
            f"'{cp['verse_text_short'][:60]}'"
        )
    print(f"\nWrote: {OUT_JSON}")


if __name__ == "__main__":
    main()
