#!/usr/bin/env python3
"""H-NEW-257a — formal Biqa'i Medinan inclusio rerun from primary text.

Primary source:
  data/literature/classical-tafsir/raw/biqai-nazm-al-durar.ShamAY.raw.txt

The script implements the locked post-inspection prereg in:
  findings/phase-b-hypotheses/h-new-257a-biqai-primary-text-rerun-prereg.md
"""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
BIQAI_SHAMAY = (
    ROOT / "data" / "literature" / "classical-tafsir" / "raw"
    / "biqai-nazm-al-durar.ShamAY.raw.txt"
)
PREREG = (
    ROOT / "findings" / "phase-b-hypotheses"
    / "h-new-257a-biqai-primary-text-rerun-prereg.md"
)
OUT_JSON = (
    ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-257a.json"
)

TARGET_SET = {3, 4, 8, 9, 33, 47, 59, 60, 63, 65, 98}
TARGET_ORDER = [3, 4, 8, 9, 33, 47, 59, 60, 63, 65, 98]

MUQ_SURAHS = {
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
}

ALIASES = {
    9: ["التوبة", "براءة"],
    14: ["ابراهيم", "إبراهيم"],
    17: ["الإسراء", "بني إسرائيل"],
    40: ["غافر", "المؤمن"],
    41: ["فصلت", "حم السجدة"],
    76: ["الإنسان", "الانسان", "الدهر"],
    78: ["النبإ", "النبأ"],
    82: ["الإنفطار", "الانفطار"],
    84: ["الإنشقاق", "الانشقاق"],
    94: ["الشرح", "الانشراح"],
    111: ["المسد", "اللهب"],
}

BASIC_STOPWORDS = {
    "من", "في", "على", "الى", "إلى", "عن", "ما", "لا", "لم", "لن", "ثم", "قد",
    "هو", "هي", "هم", "هذا", "هذه", "ذلك", "تلك", "كان", "كانت", "إن", "أن",
    "إنه", "أنه", "كل", "كما", "يا", "أي", "أو", "بل", "اذا", "إذا", "وهو",
    "وهي", "وهم", "له", "لهم", "بهم", "بها", "عليهم", "عليه", "فيه", "فيها",
    "بين", "بعد", "قبل", "ربكم", "ربهم",
}

DEFORMULAIZE = {
    "الله", "والله", "الذين", "ايها", "يايها", "امنوا", "ومن", "وكان", "كانت",
}

BRIDGE_PATTERNS = {
    "radd_almaqtae_ala_almatlae": re.compile(r"رد\s+المقطع\s+على\s+المطلع"),
    "radd_alkhitam_ala_aliftitah": re.compile(r"رد\s+الختام\s+على\s+الافتتاح"),
    "akhiruha_dalil_ala_awwaliha": re.compile(
        r"كان\s+اخرها\s+دليلا\s+على\s+اولها"
    ),
    "waffa_matlauha_maqtauha": re.compile(r"وف[ىي]\s+مطلعها\s+مقطعها"),
    "inaatafa_ala_iftitahiha_wakhitamiha": re.compile(
        r"انعطف\s+على\s+افتتاحها\s+وختامها"
    ),
    "anaqa_ibtidauha_tamamaha": re.compile(r"عانق\s+ابتداو?ها\s+تمامها"),
    "rajaa_awwal_alsurah_ila_akhiriha": re.compile(
        r"رجع\s+بذلك\s+اول\s+السوره\s+الى\s+اخرها"
    ),
    "khatama_iftataha": re.compile(r"ختم[^\n]{0,80}افتتح"),
    "akhiruha_awwaliha": re.compile(r"اخر(?:ها|\s+السوره)?[^\n]{0,80}اول(?:ها|\s+السوره)"),
    "awwaliha_akhiruha": re.compile(r"اول(?:ها|\s+السوره)[^\n]{0,80}اخر(?:ها|\s+السوره)"),
}

START_CUE = re.compile(r"افتتح|افتتحت|اولها|اول\s+السوره|مطلع|مقصودها")
END_CUE = re.compile(r"ختم|ختمت|اخرها|اخر\s+السوره|مقطع|ختامها|تمامها")


def normalize_arabic(text: str) -> str:
    text = re.sub(r"[\u064B-\u065F\u0670]", "", text)
    text = (
        text.replace("أ", "ا")
        .replace("إ", "ا")
        .replace("آ", "ا")
        .replace("ٱ", "ا")
        .replace("ى", "ي")
        .replace("ة", "ه")
        .replace("ؤ", "و")
        .replace("ئ", "ي")
    )
    return text


def tokenize_surface(text: str) -> list[str]:
    tokens = re.findall(r"[\u0621-\u064A]+", normalize_arabic(text))
    return [
        tok for tok in tokens
        if len(tok) >= 3
        and tok not in BASIC_STOPWORDS
        and tok not in DEFORMULAIZE
    ]


def prereg_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def heading_patterns(name: str) -> list[re.Pattern[str]]:
    return [
        re.compile(
            rf"^#+.*سورة(?:\s+ms\d+)?\s+{re.escape(name)}"
            rf"(?:\s+ms\d+)?(?:\s*:.*)?$",
            re.M,
        ),
        re.compile(rf"^# \( سورة {re.escape(name)} \)$", re.M),
    ]


def parse_biqai_sections(
    quran_rows: list[dict],
    raw_text: str,
) -> tuple[dict[int, str], dict[int, dict]]:
    cursor = 0
    headings: list[tuple[int, int, str]] = []

    for row in quran_rows:
        sid = int(row["id"])
        names = ALIASES.get(sid, [row["name"]])
        best_match = None

        for name in names:
            for pat in heading_patterns(name):
                match = pat.search(raw_text, cursor)
                if not match:
                    continue
                candidate = (match.start(), match.end(), name)
                if best_match is None or candidate[0] < best_match[0]:
                    best_match = candidate

        if best_match is None:
            raise RuntimeError(f"Could not find Biqa'i heading for surah {sid}")

        headings.append(best_match)
        cursor = best_match[0] + 1

    sections: dict[int, str] = {}
    parser_meta: dict[int, dict] = {}
    for idx, row in enumerate(quran_rows):
        sid = int(row["id"])
        start = headings[idx][1]
        end = headings[idx + 1][0] if idx + 1 < len(headings) else len(raw_text)
        sections[sid] = raw_text[start:end]
        parser_meta[sid] = {
            "matched_heading_name": headings[idx][2],
            "heading_start": headings[idx][0],
            "heading_end": headings[idx][1],
            "section_start": start,
            "section_end": end,
        }
    return sections, parser_meta


def first_content_verse_id(surah_id: int, verses: list[dict]) -> int:
    if surah_id in MUQ_SURAHS and len(verses) >= 2:
        return 2
    return 1


def shared_endpoint_tokens(surah_row: dict) -> list[str]:
    verses = surah_row["verses"]
    v_first = verses[first_content_verse_id(int(surah_row["id"]), verses) - 1]["text"]
    v_last = verses[-1]["text"]
    return sorted(set(tokenize_surface(v_first)) & set(tokenize_surface(v_last)))


def exact_fisher_one_sided(target_pos: int, target_total: int, bg_pos: int, bg_total: int) -> float:
    total_success = target_pos + bg_pos
    total_n = target_total + bg_total
    numer = 0
    for x in range(target_pos, min(total_success, target_total) + 1):
        numer += math.comb(total_success, x) * math.comb(
            total_n - total_success, target_total - x
        )
    denom = math.comb(total_n, target_total)
    return numer / denom


def odds_ratio(target_pos: int, target_neg: int, bg_pos: int, bg_neg: int) -> float:
    if bg_pos == 0 or target_neg == 0:
        # Haldane-Anscombe style continuity correction for reporting only.
        return ((target_pos + 0.5) * (bg_neg + 0.5)) / (
            (target_neg + 0.5) * (bg_pos + 0.5)
        )
    return (target_pos * bg_neg) / (target_neg * bg_pos)


def collect_hits(shared_tokens: list[str], span_text: str) -> list[str]:
    seen = []
    for token in shared_tokens:
        if token in span_text:
            seen.append(token)
    return seen


def bridge_hits(section_norm: str) -> list[str]:
    matched = []
    for label, pattern in BRIDGE_PATTERNS.items():
        if pattern.search(section_norm):
            matched.append(label)
    return matched


def snippet(text: str, limit: int = 360) -> str:
    squashed = re.sub(r"\s+", " ", text).strip()
    return squashed[:limit]


def surah_record(surah_row: dict, section_text: str, parser_meta: dict) -> dict:
    sid = int(surah_row["id"])
    section_norm = normalize_arabic(section_text)
    opening_span = section_norm[:1500]
    closing_span = section_norm[-1500:]
    shared = shared_endpoint_tokens(surah_row)
    open_hits = collect_hits(shared, opening_span)
    close_hits = collect_hits(shared, closing_span)
    bridge = bridge_hits(section_norm)
    start_cue = bool(START_CUE.search(section_norm))
    end_cue = bool(END_CUE.search(section_norm))
    combined_hits = sorted(set(open_hits) | set(close_hits))

    explicit_support = bool(bridge and combined_hits)
    material_support = bool(
        explicit_support
        or (open_hits and close_hits)
        or (bridge and len(combined_hits) >= 2)
        or (start_cue and end_cue and len(combined_hits) >= 2)
    )
    support_positive = explicit_support or material_support

    return {
        "surah": sid,
        "name_ar": surah_row["name"],
        "name_tl": surah_row["transliteration"],
        "is_target": sid in TARGET_SET,
        "first_content_verse": first_content_verse_id(sid, surah_row["verses"]),
        "last_verse": int(surah_row["total_verses"]),
        "shared_endpoint_tokens": shared,
        "opening_hits": open_hits,
        "closing_hits": close_hits,
        "combined_hits": combined_hits,
        "bridge_cues": bridge,
        "start_cue": start_cue,
        "end_cue": end_cue,
        "explicit_support": explicit_support,
        "material_support": material_support,
        "support_positive": support_positive,
        "opening_span_excerpt": snippet(section_text[:900]),
        "closing_span_excerpt": snippet(section_text[-900:]),
        "parser": parser_meta,
    }


def main() -> None:
    quran_rows = json.loads(QURAN_JSON.read_text())
    raw_text = BIQAI_SHAMAY.read_text(encoding="utf-8", errors="ignore")
    sections, parser_meta = parse_biqai_sections(quran_rows, raw_text)

    records = []
    for row in quran_rows:
        sid = int(row["id"])
        records.append(surah_record(row, sections[sid], parser_meta[sid]))

    target_records = [r for r in records if r["is_target"]]
    bg_records = [r for r in records if not r["is_target"]]

    target_support_pos = sum(int(r["support_positive"]) for r in target_records)
    target_support_neg = len(target_records) - target_support_pos
    bg_support_pos = sum(int(r["support_positive"]) for r in bg_records)
    bg_support_neg = len(bg_records) - bg_support_pos

    target_explicit_pos = sum(int(r["explicit_support"]) for r in target_records)
    bg_explicit_pos = sum(int(r["explicit_support"]) for r in bg_records)

    p_primary = exact_fisher_one_sided(
        target_support_pos, len(target_records), bg_support_pos, len(bg_records)
    )
    or_primary = odds_ratio(
        target_support_pos, target_support_neg, bg_support_pos, bg_support_neg
    )

    expected_target_hits = len(target_records) * (
        (target_support_pos + bg_support_pos) / len(records)
    )
    support_hit_ids = [r["surah"] for r in target_records if r["support_positive"]]
    explicit_hit_ids = [r["surah"] for r in target_records if r["explicit_support"]]
    background_support_hits = [
        {
            "surah": r["surah"],
            "name_ar": r["name_ar"],
            "shared_endpoint_tokens": r["shared_endpoint_tokens"],
            "combined_hits": r["combined_hits"],
            "bridge_cues": r["bridge_cues"],
        }
        for r in bg_records
        if r["support_positive"]
    ]

    out = {
        "finding_id": "h-new-257a",
        "title": "Formal Biqa'i Medinan inclusio rerun from primary text",
        "pre_reg_sha256": prereg_sha256(PREREG),
        "sources": {
            "primary": str(BIQAI_SHAMAY),
            "secondary_inspected": str(
                ROOT
                / "data" / "literature" / "classical-tafsir" / "raw"
                / "biqai-nazm-al-durar.openiti.raw.txt"
            ),
            "quran": str(QURAN_JSON),
        },
        "parser": {
            "n_surahs_parsed": len(records),
            "opening_span_chars": 1500,
            "closing_span_chars": 1500,
            "target_set": TARGET_ORDER,
            "muq_surahs": sorted(MUQ_SURAHS),
            "alias_map": ALIASES,
        },
        "scoring_rule": {
            "basic_stopwords": sorted(BASIC_STOPWORDS),
            "deformulaize": sorted(DEFORMULAIZE),
            "bridge_patterns": sorted(BRIDGE_PATTERNS),
            "primary_binary": "support_positive = explicit_support OR material_support",
        },
        "primary_result": {
            "target_support_positive": target_support_pos,
            "target_total": len(target_records),
            "background_support_positive": bg_support_pos,
            "background_total": len(bg_records),
            "odds_ratio": or_primary,
            "fisher_one_sided_p": p_primary,
            "expected_target_hits_under_global_rate": expected_target_hits,
            "lift_vs_expectation": (
                target_support_pos / expected_target_hits
                if expected_target_hits
                else None
            ),
            "verdict": (
                "PASS"
                if p_primary < 0.05
                else "NULL"
            ),
        },
        "secondary_result": {
            "target_explicit_support": target_explicit_pos,
            "background_explicit_support": bg_explicit_pos,
            "target_support_hit_surahs": support_hit_ids,
            "target_explicit_hit_surahs": explicit_hit_ids,
            "background_support_hits": background_support_hits,
        },
        "target_records": [
            r for r in records if r["surah"] in TARGET_SET
        ],
    }

    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2))

    print("H-NEW-257a")
    print(f"  target support-positive: {target_support_pos}/{len(target_records)}")
    print(f"  background support-positive: {bg_support_pos}/{len(bg_records)}")
    print(f"  Fisher one-sided p: {p_primary:.6f}")
    print(f"  Odds ratio: {or_primary:.4f}")
    print(f"  Verdict: {out['primary_result']['verdict']}")
    print(f"  Target support hits: {support_hit_ids}")
    print(f"  Target explicit hits: {explicit_hit_ids}")
    print(f"  Wrote: {OUT_JSON}")


if __name__ == "__main__":
    main()
