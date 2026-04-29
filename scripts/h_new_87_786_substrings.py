"""H-NEW-87 — Other 786-abjad multi-word substrings in the Quran.

Pre-reg: findings/phase-b-hypotheses/h-new-87-786-substrings-prereg.md
Anchor : Bismillah 'بسم الله الرحمن الرحيم' = 786 (mashriqi).

Sliding-window mashriqi abjad sums for w ∈ {3,4,5,6} across the entire
canonical-order Quran word stream (no-tashkeel). Catalog all hits at 786.
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import List, Tuple

REPO = Path("/Users/grey/Downloads/quran")
sys.path.insert(0, str(REPO / "analysis"))

from tools.gematria import word_value, text_value  # noqa: E402

ANCHOR = "بسم الله الرحمن الرحيم"
ANCHOR_VALUE = 786
WINDOWS = [3, 4, 5, 6]
NEIGHBOUR_RADIUS = 20

OUTPUT_MD = REPO / "findings/phase-b-hypotheses/h-new-87-786-substrings.md"
OUTPUT_TSV = REPO / "findings/phase-b-hypotheses/h-new-87-786-catalog.tsv"


def load_word_stream() -> List[Tuple[int, int, int, str]]:
    """Return (surah_id, verse_id, word_idx_in_verse, word) tuples in mushaf order."""
    path = REPO / "quran-text/quran-no-tashkeel.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    stream: List[Tuple[int, int, int, str]] = []
    for s in raw:
        sid = s["id"]
        for v in s["verses"]:
            vid = v["id"]
            words = v["text"].split()
            for i, w in enumerate(words):
                stream.append((sid, vid, i, w))
    return stream


def main() -> None:
    # Sanity: anchor value
    av = text_value(ANCHOR, "mashriqi")
    assert av == ANCHOR_VALUE, f"Bismillah mashriqi != 786 (got {av})"
    print(f"[sanity] Bismillah mashriqi = {av}", flush=True)

    stream = load_word_stream()
    n_words = len(stream)
    print(f"[corpus] words in stream = {n_words}", flush=True)

    # Per-word values once
    word_vals = [word_value(w[3], "mashriqi") for w in stream]

    # Per-window sliding sums + 786 catalog
    catalog_rows: List[dict] = []
    summaries: List[dict] = []
    distributions = {}

    for w in WINDOWS:
        # rolling sum
        cur = sum(word_vals[:w])
        sums = [cur]
        for i in range(1, n_words - w + 1):
            cur += word_vals[i + w - 1] - word_vals[i - 1]
            sums.append(cur)

        cnt = Counter(sums)
        distributions[w] = cnt

        # collect 786 hits
        n786 = cnt[ANCHOR_VALUE]
        # neighbour density ratio (excluding 786 itself, ±20)
        neigh_vals = [
            cnt[v] for v in range(ANCHOR_VALUE - NEIGHBOUR_RADIUS, ANCHOR_VALUE + NEIGHBOUR_RADIUS + 1)
            if v != ANCHOR_VALUE
        ]
        neigh_mean = sum(neigh_vals) / len(neigh_vals) if neigh_vals else 0
        ratio = (neigh_mean / n786) if n786 > 0 else float("inf")

        # most-common values for context
        top_5 = cnt.most_common(5)
        # rank of 786 (from top, 1 = most common)
        ranked = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))
        rank_786 = next(
            (i + 1 for i, (v, _) in enumerate(ranked) if v == ANCHOR_VALUE),
            None,
        )

        # full catalog
        for i, s in enumerate(sums):
            if s == ANCHOR_VALUE:
                window_words = stream[i:i + w]
                start_sid, start_vid, start_widx, _ = window_words[0]
                end_sid, end_vid, end_widx, _ = window_words[-1]
                phrase = " ".join(t[3] for t in window_words)
                cross_verse = not (start_sid == end_sid and start_vid == end_vid)
                catalog_rows.append({
                    "window": w,
                    "start_surah": start_sid,
                    "start_verse": start_vid,
                    "start_word_idx": start_widx,
                    "end_surah": end_sid,
                    "end_verse": end_vid,
                    "end_word_idx": end_widx,
                    "cross_verse": cross_verse,
                    "phrase": phrase,
                })

        # neighbour ratios at alternative radii
        def ratio_at(radius: int) -> float:
            nv = [
                cnt[v] for v in range(ANCHOR_VALUE - radius, ANCHOR_VALUE + radius + 1)
                if v != ANCHOR_VALUE
            ]
            nm = sum(nv) / len(nv) if nv else 0
            return (nm / n786) if n786 > 0 else float("inf")

        summaries.append({
            "window": w,
            "n_windows": len(sums),
            "n_786": n786,
            "neighbour_ratio_r20": ratio,
            "neighbour_ratio_r10": ratio_at(10),
            "neighbour_ratio_r50": ratio_at(50),
            "rank_786": rank_786,
            "n_distinct_values": len(cnt),
            "max_count": max(cnt.values()),
            "top5": top_5,
        })

    # --- write TSV catalog ---
    with OUTPUT_TSV.open("w", encoding="utf-8") as f:
        f.write("window\tstart_surah\tstart_verse\tstart_word_idx\tend_surah\tend_verse\tend_word_idx\tcross_verse\tphrase\n")
        for r in catalog_rows:
            f.write(f"{r['window']}\t{r['start_surah']}\t{r['start_verse']}\t{r['start_word_idx']}\t"
                    f"{r['end_surah']}\t{r['end_verse']}\t{r['end_word_idx']}\t{r['cross_verse']}\t{r['phrase']}\n")
    print(f"[write] catalog -> {OUTPUT_TSV} ({len(catalog_rows)} rows)", flush=True)

    # --- write decision verdict ---
    w4_summary = next(s for s in summaries if s["window"] == 4)
    n_w4 = w4_summary["n_786"]
    ratio_w4 = w4_summary["neighbour_ratio_r20"]
    if n_w4 in (1, 2) and ratio_w4 >= 5:
        verdict = "CONFIRMED H1 (uniqueness): 786 is sharply singled out at w=4."
    elif n_w4 >= 3 and ratio_w4 >= 2:
        verdict = "PARTIAL: 786 is rare but not unique at w=4."
    elif n_w4 >= 3 and ratio_w4 < 1:
        verdict = "CONTRADICTED H1: 786 is no rarer than nearby values at w=4."
    else:
        verdict = "UNDERDETERMINED."

    # --- write markdown report ---
    lines: List[str] = []
    lines.append("# H-NEW-87 — Other 786-abjad Multi-word Substrings in the Quran")
    lines.append("")
    lines.append("**Status:** EXECUTED.")
    lines.append("**Pre-reg:** `findings/phase-b-hypotheses/h-new-87-786-substrings-prereg.md`.")
    lines.append("**Date:** 2026-04-15.")
    lines.append("**Anchor:** mashriqī abjad of `بسم الله الرحمن الرحيم` = **786**.")
    lines.append("")
    lines.append(f"## Verdict (primary, w=4)")
    lines.append("")
    lines.append(f"**{verdict}**")
    lines.append("")
    lines.append(f"- 786-substrings at w=4: **{n_w4}**")
    lines.append(f"- neighbour density ratio (mean count of values 786±20 excluding 786, divided by count[786]): **{ratio_w4:.3f}**")
    lines.append(f"  - r=10: {w4_summary['neighbour_ratio_r10']:.3f}, r=50: {w4_summary['neighbour_ratio_r50']:.3f}")
    lines.append(f"- 786 rank in distribution: **{w4_summary['rank_786']}** out of {w4_summary['n_distinct_values']} distinct values")
    lines.append(f"- max count of any single value at w=4: {w4_summary['max_count']}")
    lines.append(f"- top-5 most-common values at w=4: {w4_summary['top5']}")
    lines.append("")
    lines.append("## Summary by window size")
    lines.append("")
    lines.append("| w | n_windows | n_786 | rank_786 | ratio(r=20) | ratio(r=10) | ratio(r=50) |")
    lines.append("|---|-----------|-------|----------|-------------|-------------|-------------|")
    for s in summaries:
        lines.append(
            f"| {s['window']} | {s['n_windows']} | {s['n_786']} | {s['rank_786']} | "
            f"{s['neighbour_ratio_r20']:.3f} | {s['neighbour_ratio_r10']:.3f} | {s['neighbour_ratio_r50']:.3f} |"
        )
    lines.append("")
    lines.append("Interpretation: ratio > 1 means 786 is *rarer* than its neighbours; ratio < 1 means it is *commoner*; ratio ≈ 1 means typical density.")
    lines.append("")

    # --- 786 hits sectioned by w ---
    for w in WINDOWS:
        w_rows = [r for r in catalog_rows if r["window"] == w]
        lines.append(f"## w={w}: {len(w_rows)} substrings summing to 786")
        lines.append("")
        if not w_rows:
            lines.append("(none)")
            lines.append("")
            continue
        # show all if reasonable count, else first 50 + last 10
        show = w_rows if len(w_rows) <= 100 else (w_rows[:60] + [{"phrase": "…", "start_surah": 0, "start_verse": 0, "start_word_idx": 0, "end_surah": 0, "end_verse": 0, "end_word_idx": 0, "cross_verse": False}] + w_rows[-10:])
        lines.append("| # | start (S:V[w]) | end (S:V[w]) | cross_verse | phrase |")
        lines.append("|---|---------------|--------------|-------------|--------|")
        for idx, r in enumerate(show):
            if r["phrase"] == "…":
                lines.append("| … | … | … | … | … |")
                continue
            lines.append(
                f"| {idx + 1} | {r['start_surah']}:{r['start_verse']}[{r['start_word_idx']}] | "
                f"{r['end_surah']}:{r['end_verse']}[{r['end_word_idx']}] | {r['cross_verse']} | {r['phrase']} |"
            )
        lines.append("")

    # --- meaningfulness pass: flag substrings that are *within a single verse* and contain divine names ---
    DIVINE_TOKENS = {"الله", "الرحمن", "الرحيم", "ربك", "ربكم", "ربنا", "ربي", "ربه", "ربها", "ربهم", "رب", "اللهم"}
    BISMILLAH_FULL = {"بسم", "الله", "الرحمن", "الرحيم"}
    flagged: List[dict] = []
    for r in catalog_rows:
        toks = set(r["phrase"].split())
        if r["cross_verse"]:
            continue
        # contains at least one divine token, and is not literally the Bismillah (we'll list those separately)
        is_bismillah = (toks == BISMILLAH_FULL and r["window"] == 4)
        if is_bismillah:
            r["bismillah"] = True
            flagged.append(r)
            continue
        if toks & DIVINE_TOKENS:
            r["bismillah"] = False
            flagged.append(r)

    lines.append("## Meaningfulness pass — single-verse 786-substrings containing divine names or being literal Bismillah")
    lines.append("")
    lines.append(f"Total flagged: **{len(flagged)}** (across all w).")
    lines.append("")
    if flagged:
        lines.append("| w | location | bismillah? | phrase |")
        lines.append("|---|----------|------------|--------|")
        for r in flagged:
            loc = f"{r['start_surah']}:{r['start_verse']}[{r['start_word_idx']}-{r['end_word_idx']}]"
            lines.append(f"| {r['window']} | {loc} | {r.get('bismillah', False)} | {r['phrase']} |")
        lines.append("")

    # --- final note ---
    lines.append("## Notes")
    lines.append("")
    lines.append("- Cross-verse windows are allowed, per pre-reg, to avoid inflating uniqueness.")
    lines.append("- Mashriqī abjad table; tashkeel and hamza-carriers contribute 0.")
    lines.append("- Catalog TSV: `findings/phase-b-hypotheses/h-new-87-786-catalog.tsv`.")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"[write] report  -> {OUTPUT_MD}", flush=True)


if __name__ == "__main__":
    main()
