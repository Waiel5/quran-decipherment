#!/usr/bin/env python3
"""H-NEW-92 — Q 24:35 (Āyat al-Nūr / Light Verse) multi-axis structural uniqueness audit.

Pre-registration: findings/phase-b-hypotheses/h-new-92-light-verse-prereg.md
Locked rules tuple:
    (no-tashkeel; orthographic-token via real_words; graphemes; hafs-kufan;
     6236 verses; basmala-counted-only-in-surah-1; mashriqi)

For each of 8 axes, scores Q 24:35 against the full 6236-verse corpus distribution.
Bonferroni alpha = 0.05 / 8 = 0.00625. Two-sided percentile rank.
Comparators (Q 1:1, Q 2:255, Q 112:1-4) are descriptive only.

Output:
- findings/phase-b-hypotheses/csv/h-new-92.json
- console summary

Usage: python3 scripts/h_new_92_light_verse.py
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

# Locate analysis tools
ROOT = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(ROOT, "analysis"))
from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words, graphemes  # noqa: E402
from tools.gematria import text_value  # noqa: E402

# ---------------------------------------------------------------------------
# Config (locked in prereg)
# ---------------------------------------------------------------------------

ALPHA = 0.05
BONF_K = 8
ALPHA_BON = ALPHA / BONF_K  # 0.00625
TARGET = (24, 35)
CORPUS_TOTAL = 6236

# Light vocabulary roots (locked in prereg)
LIGHT_ROOTS = {"nwr", "DwA", "srj", "qbs", "Swr", "wqd", "nfx", "shhb",
               "rmd", "SbH", "Dwq"}

# Morphology source
MORPH_PATH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")

# Output paths
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-92.json")


# ---------------------------------------------------------------------------
# Morphology loader
# ---------------------------------------------------------------------------

def parse_features(features: str) -> Dict[str, str]:
    """Parse FEATURES column into key:value dict.

    Uses ':' as separator for keyed features (LEM:foo, ROOT:bar). Bare
    flags (M, F, NOM, etc.) are stored as key=flag, value="".
    """
    out: Dict[str, str] = {}
    for part in features.split("|"):
        if ":" in part:
            k, _, v = part.partition(":")
            out[k] = v
        else:
            out[part] = ""
    return out


def load_morphology() -> Dict[Tuple[int, int], List[Dict]]:
    """Return {(surah, verse): [seg_dict, ...]} from QAC v0.4.

    Each seg_dict has: location, form, tag, lem, root.
    """
    by_verse: Dict[Tuple[int, int], List[Dict]] = defaultdict(list)
    with open(MORPH_PATH, "r", encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            # loc = (surah:verse:word:seg)
            inner = loc.strip("()")
            try:
                s, v, w, seg = inner.split(":")
                s_i, v_i = int(s), int(v)
            except ValueError:
                continue
            f = parse_features(feats)
            by_verse[(s_i, v_i)].append({
                "loc": loc,
                "form": form,
                "tag": tag,
                "lem": f.get("LEM", ""),
                "root": f.get("ROOT", ""),
            })
    return dict(by_verse)


def lemma_global_counts(morph_by_verse: Dict[Tuple[int, int], List[Dict]]) -> Counter:
    """Global counts of all lemmas across the corpus."""
    counts: Counter = Counter()
    for segs in morph_by_verse.values():
        for s in segs:
            if s["lem"]:
                counts[s["lem"]] += 1
    return counts


# ---------------------------------------------------------------------------
# Per-verse axis computations
# ---------------------------------------------------------------------------

def verse_letters(text: str) -> int:
    return graphemes(text)


def verse_words(text: str) -> int:
    return len(real_words(text))


def verse_distinct_lemmas(segs: List[Dict]) -> int:
    return len({s["lem"] for s in segs if s["lem"]})


def verse_hapax_density(segs: List[Dict], global_counts: Counter) -> float:
    """Fraction of verse's content lemmas that are corpus-hapax (count==1)."""
    lems = [s["lem"] for s in segs if s["lem"]]
    if not lems:
        return 0.0
    distinct = set(lems)
    if not distinct:
        return 0.0
    hapax = sum(1 for l in distinct if global_counts.get(l, 0) == 1)
    return hapax / len(distinct)


# Divine-name lemmas (the seven "Allah-class" lemmas in QAC)
DIVINE_LEMMAS = {
    "{ll~ah",       # Allah
    "{l~ah",        # Allah variant
    "rab~",         # Rabb
    "r~aHoma`n",    # al-Rahman
    "r~aHiym",      # al-Rahim
    "ra'uwf",       # al-Ra'uf (often divine context)
    "raHoma`n",     # variant
}


def verse_divine_density(segs: List[Dict]) -> float:
    """Divine-name lemma occurrences per word (using QAC word-positions).

    A word index is the third component of the location tuple. Counts
    distinct word positions whose stem segment carries a divine lemma.
    """
    div_words: set = set()
    total_words: set = set()
    for s in segs:
        loc = s["loc"].strip("()").split(":")
        if len(loc) < 3:
            continue
        w = int(loc[2])
        total_words.add(w)
        if s["lem"] in DIVINE_LEMMAS:
            div_words.add(w)
    if not total_words:
        return 0.0
    return len(div_words) / len(total_words)


def verse_light_density(segs: List[Dict]) -> float:
    """Per-word density of light-root tokens (any of LIGHT_ROOTS)."""
    light_words: set = set()
    total_words: set = set()
    for s in segs:
        loc = s["loc"].strip("()").split(":")
        if len(loc) < 3:
            continue
        w = int(loc[2])
        total_words.add(w)
        if s["root"] in LIGHT_ROOTS:
            light_words.add(w)
    if not total_words:
        return 0.0
    return len(light_words) / len(total_words)


def verse_ttr(segs: List[Dict]) -> float:
    """Type-token ratio over QAC words: distinct lemmas / number of word slots."""
    word_lems: Dict[int, str] = {}
    for s in segs:
        loc = s["loc"].strip("()").split(":")
        if len(loc) < 3:
            continue
        w = int(loc[2])
        if s["lem"] and w not in word_lems:
            word_lems[w] = s["lem"]
    if not word_lems:
        return 0.0
    return len(set(word_lems.values())) / len(word_lems)


def verse_abjad(text: str) -> int:
    return text_value(text, table="mashriqi")


# ---------------------------------------------------------------------------
# Percentile helper
# ---------------------------------------------------------------------------

def percentile_and_p(value: float, distribution: List[float]) -> Dict:
    """Compute rank percentile + two-sided p-value.

    Reports:
      - rank (1-indexed, count of verses with value <= target_value, ties = same rank)
      - n_strict_below: count of verses strictly below
      - n_equal: count of verses equal (including target itself)
      - n_strict_above: count strictly above
      - pct_top: 1 - (n_strict_below + n_equal/2)/N    (right-tail percentile)
      - pct_bot: (n_strict_below + n_equal/2)/N         (left-tail percentile)
      - p_two: 2 * min(pct_top, pct_bot), capped at 1.0
    """
    N = len(distribution)
    n_strict_below = sum(1 for v in distribution if v < value)
    n_equal = sum(1 for v in distribution if v == value)
    n_strict_above = N - n_strict_below - n_equal
    # mid-rank percentile (Hazen-style)
    rank_mid = n_strict_below + n_equal / 2
    pct_bot = rank_mid / N            # fraction at or below
    pct_top = 1.0 - pct_bot           # fraction at or above
    p_two = min(1.0, 2.0 * min(pct_top, pct_bot))
    return {
        "value": value,
        "N": N,
        "n_strict_below": n_strict_below,
        "n_equal": n_equal,
        "n_strict_above": n_strict_above,
        "rank_from_top_1indexed": n_strict_above + 1,  # how many beat it + 1
        "pct_top": pct_top,
        "pct_bot": pct_bot,
        "p_two_sided": p_two,
    }


def classify(p_two: float, n_strict_above: int, N: int) -> str:
    """STRONG-PASS / PASS-DIRECTED / NULL per prereg pass criteria."""
    rank_from_top = n_strict_above + 1
    rank_from_bot = N - n_strict_above
    extreme_tail_n = max(1, N // 100)  # ~62 for N=6236
    moderate_tail_n = max(1, N // 20)  # ~311 for N=6236
    in_extreme = rank_from_top <= extreme_tail_n or rank_from_bot <= extreme_tail_n
    in_moderate = rank_from_top <= moderate_tail_n or rank_from_bot <= moderate_tail_n
    if p_two < ALPHA_BON and in_extreme:
        return "STRONG-PASS"
    if p_two < ALPHA and in_moderate:
        return "PASS-DIRECTED"
    return "NULL"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 70)
    print("H-NEW-92 — Āyat al-Nūr (Q 24:35) multi-axis structural audit")
    print("=" * 70)

    print("\n[1/4] Loading corpus + morphology...")
    surahs = load_quran("no-tashkeel")
    morph_by_verse = load_morphology()
    g_counts = lemma_global_counts(morph_by_verse)

    # Build per-verse text lookup
    verse_text: Dict[Tuple[int, int], str] = {}
    for s in surahs:
        for v in s.verses:
            verse_text[(s.id, v.id)] = v.text

    print(f"    loaded {len(verse_text)} verses, {len(morph_by_verse)} morph entries")
    print(f"    total distinct lemmas in corpus: {len(g_counts)}")
    print(f"    corpus hapax lemmas (count==1): {sum(1 for c in g_counts.values() if c == 1)}")

    # Verify our axis computations on a known anchor: Q 1:1 = 19 letters / 4 words
    bism_text = verse_text[(1, 1)]
    bism_let = verse_letters(bism_text)
    bism_w = verse_words(bism_text)
    bism_abjad = verse_abjad(bism_text)
    print(f"    anchor check Q 1:1: letters={bism_let} (expect 19), "
          f"words={bism_w} (expect 4), abjad={bism_abjad} (expect 786)")
    assert bism_let == 19, f"FAIL anchor letters {bism_let}"
    assert bism_w == 4, f"FAIL anchor words {bism_w}"
    assert bism_abjad == 786, f"FAIL anchor abjad {bism_abjad}"

    # ------------------------------------------------------------------
    print("\n[2/4] Computing 8 axis distributions over all 6236 verses...")
    axes = ["length_letters", "length_words", "distinct_lemmas",
            "hapax_density", "divine_density", "light_density",
            "ttr", "abjad_total"]
    dist: Dict[str, List[float]] = {ax: [] for ax in axes}
    per_verse_scores: Dict[Tuple[int, int], Dict[str, float]] = {}

    for (s_id, v_id), txt in verse_text.items():
        segs = morph_by_verse.get((s_id, v_id), [])
        scores = {
            "length_letters": float(verse_letters(txt)),
            "length_words": float(verse_words(txt)),
            "distinct_lemmas": float(verse_distinct_lemmas(segs)),
            "hapax_density": verse_hapax_density(segs, g_counts),
            "divine_density": verse_divine_density(segs),
            "light_density": verse_light_density(segs),
            "ttr": verse_ttr(segs),
            "abjad_total": float(verse_abjad(txt)),
        }
        for ax, val in scores.items():
            dist[ax].append(val)
        per_verse_scores[(s_id, v_id)] = scores

    print(f"    distributions built, N = {len(dist['length_letters'])}")
    assert len(dist["length_letters"]) == CORPUS_TOTAL

    # ------------------------------------------------------------------
    print("\n[3/4] Scoring Q 24:35 + comparators...")
    target_scores = per_verse_scores[TARGET]
    comparators = {
        "Q 1:1 (Bismillah)": per_verse_scores[(1, 1)],
        "Q 2:255 (Ayat al-Kursi)": per_verse_scores[(2, 255)],
        "Q 112 (sum of v1-4)": {
            ax: sum(per_verse_scores[(112, v)][ax] for v in range(1, 5))
            for ax in axes
        },
        # For density axes, sum doesn't make sense; recompute as mean
    }
    # Override density axes for Q 112 with mean over its 4 verses
    for ax in ("hapax_density", "divine_density", "light_density", "ttr"):
        comparators["Q 112 (sum of v1-4)"][ax] = (
            sum(per_verse_scores[(112, v)][ax] for v in range(1, 5)) / 4
        )

    # Per-axis stats for the target
    results: Dict[str, Dict] = {}
    for ax in axes:
        stats = percentile_and_p(target_scores[ax], dist[ax])
        verdict = classify(stats["p_two_sided"], stats["n_strict_above"], stats["N"])
        results[ax] = {**stats, "verdict": verdict}

    # Print headline table
    print("\n" + "-" * 70)
    print(f"Q 24:35 axis percentiles (Bonferroni α = {ALPHA_BON:.5f})")
    print("-" * 70)
    print(f"{'AXIS':<22} {'VALUE':>10} {'RANK':>8} {'PCT_TOP':>10} {'P_TWO':>10}  VERDICT")
    for ax in axes:
        r = results[ax]
        rank = r["rank_from_top_1indexed"]
        print(f"{ax:<22} {r['value']:>10.4f} {rank:>8} "
              f"{r['pct_top']*100:>9.3f}% {r['p_two_sided']:>10.4f}  {r['verdict']}")

    # Comparator rows
    print("\nComparator scores (descriptive, no p-value):")
    print(f"{'AXIS':<22} {'Q1:1':>12} {'Q2:255':>12} {'Q112(1-4)':>14} {'Q24:35':>12}")
    for ax in axes:
        print(f"{ax:<22} "
              f"{comparators['Q 1:1 (Bismillah)'][ax]:>12.4f} "
              f"{comparators['Q 2:255 (Ayat al-Kursi)'][ax]:>12.4f} "
              f"{comparators['Q 112 (sum of v1-4)'][ax]:>14.4f} "
              f"{target_scores[ax]:>12.4f}")

    # Numerological position observations (descriptive)
    print("\nNumerological position observations (Axis 9, descriptive only):")
    print(f"  Surah 24 = 2^3 * 3 (composite); 24 verses-of-surah-1 = no, surah-24 has 64 verses")
    print(f"  Verse 35 = 5 * 7 (composite, semiprime)")
    print(f"  Position 35 / 64 = {35/64:.4f} (post-midpoint)")
    print(f"  Reverse position = 64 - 35 + 1 = 30 = 2 * 3 * 5")
    print(f"  Cumulative verse index in canonical mushaf (Q 24:35):")
    cum = 0
    for s in surahs:
        if s.id < 24:
            cum += s.total_verses
        else:
            break
    cum += 35
    print(f"     verses 1..(24:35) = {cum}")
    print(f"  Surah 24 length = 64 verses; midpoint = 32.5; verse 35 sits +2.5 past midpoint")

    # Top-N verse winners per axis (small audit)
    print("\nTop-3 verses per axis (rank 1, 2, 3 from top):")
    for ax in axes:
        order = sorted(per_verse_scores.items(),
                       key=lambda kv: kv[1][ax], reverse=True)
        print(f"  {ax:<22}", end=" ")
        for (s_id, v_id), sc in order[:3]:
            mark = "  <-- Q 24:35" if (s_id, v_id) == TARGET else ""
            print(f" {s_id}:{v_id}={sc[ax]:.3f}", end="")
        # show Q 24:35 rank if not in top 3
        rank_pos = next(i for i, (k, _) in enumerate(order, 1) if k == TARGET)
        print(f"   [Q 24:35 ranks {rank_pos}/{CORPUS_TOTAL}]")

    # Light-density specific: rank Q 24:36..40 too
    print("\nLight-density context — Q 24:35..40:")
    for v_id in range(35, 41):
        if (24, v_id) in per_verse_scores:
            ld = per_verse_scores[(24, v_id)]["light_density"]
            wc = per_verse_scores[(24, v_id)]["length_words"]
            print(f"  Q 24:{v_id}: light_density={ld:.4f}  words={int(wc)}")

    # ------------------------------------------------------------------
    print("\n[4/4] Writing JSON output...")
    out = {
        "id": "H-NEW-92",
        "target": "Q 24:35",
        "alpha": ALPHA,
        "bonferroni_k": BONF_K,
        "alpha_bonferroni": ALPHA_BON,
        "rules_tuple": "no-tashkeel; orthographic-token-real-words; graphemes; "
                       "hafs-kufan; 6236; basmala-counted-only-in-surah-1; mashriqi",
        "target_scores": target_scores,
        "axes_results": results,
        "comparators": {
            label: {ax: scores[ax] for ax in axes}
            for label, scores in comparators.items()
        },
        "verdict_per_axis": {ax: results[ax]["verdict"] for ax in axes},
        "n_strong_pass": sum(1 for ax in axes if results[ax]["verdict"] == "STRONG-PASS"),
        "n_pass_directed": sum(1 for ax in axes
                               if results[ax]["verdict"] == "PASS-DIRECTED"),
        "n_null": sum(1 for ax in axes if results[ax]["verdict"] == "NULL"),
        "top_3_per_axis": {
            ax: [
                {"verse": f"{k[0]}:{k[1]}", "score": v[ax]}
                for k, v in sorted(per_verse_scores.items(),
                                   key=lambda kv: kv[1][ax], reverse=True)[:3]
            ]
            for ax in axes
        },
        "rank_per_axis_from_top": {
            ax: next(i for i, (k, _) in
                     enumerate(sorted(per_verse_scores.items(),
                                      key=lambda kv: kv[1][ax],
                                      reverse=True), 1) if k == TARGET)
            for ax in axes
        },
    }
    # Per-axis overall verdict
    n_sp = out["n_strong_pass"]
    n_pd = out["n_pass_directed"]
    light_v = results["light_density"]["verdict"]
    distinct_v = results["distinct_lemmas"]["verdict"]
    if (n_sp >= 3 and light_v == "STRONG-PASS"
            and distinct_v in ("STRONG-PASS", "PASS-DIRECTED")):
        overall = "UNIQUE"
    elif n_sp >= 1 or n_pd >= 4:
        overall = "NOTABLE"
    else:
        overall = "EXEGETICALLY-CARRIED"
    out["overall_verdict"] = overall
    print(f"\nOVERALL VERDICT: {overall}")
    print(f"  STRONG-PASS axes: {n_sp}/{BONF_K}")
    print(f"  PASS-DIRECTED axes: {n_pd}/{BONF_K}")
    print(f"  NULL axes: {out['n_null']}/{BONF_K}")

    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, "w") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    print(f"  wrote {OUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
