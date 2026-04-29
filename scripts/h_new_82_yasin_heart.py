#!/usr/bin/env python3
"""H-NEW-82 — Yā-Sīn (Q 36) as the "heart of the Quran".

Pre-reg: findings/phase-b-hypotheses/h-new-82-yasin-heart-prereg.md

6 axes (locked):
  A1 mushaf-position-median           (closest to 57.5)
  A2 verse-count-median               (closest to median verse count)
  A3 letter-count-median              (closest to median letter count)
  A4 lexical-centroid                 (max mean root-Jaccard to all others)
  A5 eigenvector-centrality           (principal eigenvector of root-Jaccard matrix)
  A6 theme-centroid                   (cosine to corpus-mean theme vector)

Bonferroni-6, α_bon = 0.05/6 = 0.00833. Seed 20260417.

PASS criterion: Q 36 is rank #1 on ≥ 3 axes, OR top-5 on ≥ 5 axes.

MW-5: ≥ 1 of {Q1, Q114} must rank > 57 on ≥ 4 of 6 axes (else INSTRUMENT_FAIL).
"""
from __future__ import annotations

import csv
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260417
N_NULL_CENTRALITY = 10_000
ALPHA_BON = 0.05 / 6  # = 0.00833...
N_AXES = 6

AXES = [
    "A1_mushaf_position_median",
    "A2_verse_count_median",
    "A3_letter_count_median",
    "A4_lexical_centroid",
    "A5_eigenvector_centrality",
    "A6_theme_centroid",
]

TARGET_SURAH = 36          # Yā-Sīn
CONTROL_SURAHS = [1, 114]  # MW-5 negative controls (Fātiḥa, al-Nās)
EXTRA_REPORT_SURAHS = [2, 18, 50, 55, 57, 58, 67]  # diagnostic ensemble (D1)

# Theme palette T1..T8 (locked BEFORE inspecting Q 36 morphology) — Buckwalter
# QAC ROOT strings. The QAC encodes Arabic roots in Buckwalter; below are the
# Buckwalter equivalents of the Arabic roots in the prereg.
#  Arabic letter -> Buckwalter
#   ا -> A,   ب -> b,   ت -> t,   ث -> v,   ج -> j,   ح -> H,   خ -> x
#   د -> d,   ذ -> *,   ر -> r,   ز -> z,   س -> s,   ش -> $,   ص -> S
#   ض -> D,   ط -> T,   ظ -> Z,   ع -> E,   غ -> g,   ف -> f,   ق -> q
#   ك -> k,   ل -> l,   م -> m,   ن -> n,   ه -> h,   و -> w,   ي -> y
#   ء -> '

THEME_ROOTS = {
    "T1_tawhid":         {"Alh", "rbb", "Alh", "rHm", "Alh"},  # only distinct: Alh, rbb, rHm
    "T2_prophet":        {"rsl", "nbA", "Hmd", "rsl"},
    "T3_resurrection":   {"qwm", "bEv", "jzy", "jnn", "nwr", "jHm", "Hsr", "vwb", "Es*"},
    "T4_belief":         {"Amn", "kfr", "$rk", "nfq", "ymn"},
    "T5_creation":       {"xlq", "smw", "ArD", "$ms", "qmr", "lyl", "nhr"},
    "T6_narrative":      {"qwm", "qry", "Ahl", "mlk", "rsl"},
    "T7_law":            {"Amr", "nhy", "Hll", "Hrm", "ktb", "Hkm"},
    "T8_reflection":     {"Eql", "fkr", "Elm", "*kr", "Ayy", "fhm", "lbb"},
}
# Note: distinct sets — duplicates collapse via set semantics already.

# ---------------- Loaders ----------------

def load_quran_no_tashkeel():
    path = REPO / "quran-text" / "quran-no-tashkeel.json"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def load_qac_roots_per_surah():
    """Return (per_surah_roots, corpus_root_count, per_surah_word_count).

    per_surah_roots[sid]    = list of root-strings for STEM tokens
    corpus_root_count       = Counter over corpus
    per_surah_word_count[sid] = number of STEM tokens in that surah
        (used as denominator for theme-rate)
    """
    per_surah: dict[int, list[str]] = defaultdict(list)
    corpus_count: Counter = Counter()
    per_surah_words: Counter = Counter()
    path = REPO / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            feat = parts[3]
            if "STEM" not in feat:
                continue
            per_surah_words[sid] += 1
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            per_surah[sid].append(root)
            corpus_count[root] += 1
    return per_surah, corpus_count, per_surah_words


def load_divine_density():
    """Return dict surah_id -> divine-name density (sum num_names / verse count)."""
    csv_path = REPO / "findings" / "phase-b-hypotheses" / "divine-names-by-verse.csv"
    name_sum: Counter = Counter()
    with csv_path.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            sid = int(row["surah"])
            name_sum[sid] += int(row["num_names"])
    return name_sum


# ---------------- Per-surah scalars ----------------

def per_surah_scalars(quran):
    """Return dicts:
       verse_count[sid], letter_count[sid] (no-tashkeel chars, spaces excluded)
       letter_count_with_spaces[sid] also.
    """
    verse_count = {}
    letter_count = {}
    for s in quran:
        sid = s["id"]
        verses = s["verses"]
        verse_count[sid] = len(verses)
        # letter count = total non-space chars across all verses (no-tashkeel)
        n_chars = 0
        for v in verses:
            t = v["text"].strip()
            n_chars += sum(1 for c in t if not c.isspace())
        letter_count[sid] = n_chars
    return verse_count, letter_count


# ---------------- Similarity matrix ----------------

def root_set_per_surah(qac_per_surah):
    return {sid: set(roots) for sid, roots in qac_per_surah.items()}


def jaccard_matrix(root_sets):
    """Build 114x114 Jaccard matrix as nested dict.
       S[i][j] = jaccard(R_i, R_j); S[i][i] = 0 (zero diagonal)."""
    sids = sorted(root_sets.keys())
    S = {i: {j: 0.0 for j in sids} for i in sids}
    for idx_i, i in enumerate(sids):
        ri = root_sets[i]
        for j in sids[idx_i + 1:]:
            rj = root_sets[j]
            if not ri and not rj:
                v = 0.0
            else:
                inter = len(ri & rj)
                union = len(ri | rj)
                v = inter / max(1, union)
            S[i][j] = v
            S[j][i] = v
        # diagonal stays 0
    return S, sids


def mean_similarity_per_surah(S, sids):
    """Mean of S[i][j] over j != i."""
    out = {}
    n = len(sids)
    for i in sids:
        s = sum(S[i][j] for j in sids if j != i)
        out[i] = s / max(1, n - 1)
    return out


def eigenvector_centrality(S, sids, n_iter=2000, tol=1e-12):
    """Power iteration on the dense symmetric S to find the principal
       eigenvector. Returns dict sid -> centrality (L2-normalised, all positive
       since S is non-negative and the graph is connected enough for Jaccard
       on this corpus)."""
    n = len(sids)
    # initial vector: uniform
    v = {i: 1.0 / math.sqrt(n) for i in sids}
    for _ in range(n_iter):
        # w = S v
        w = {i: 0.0 for i in sids}
        for i in sids:
            row = S[i]
            wi = 0.0
            for j in sids:
                wi += row[j] * v[j]
            w[i] = wi
        # normalize w
        norm = math.sqrt(sum(x * x for x in w.values()))
        if norm < 1e-30:
            break
        new_v = {i: w[i] / norm for i in sids}
        # convergence check
        diff = math.sqrt(sum((new_v[i] - v[i]) ** 2 for i in sids))
        v = new_v
        if diff < tol:
            break
    # Make signs positive (Perron-Frobenius for non-negative matrix gives
    # non-negative eigenvector; but with float drift sign can flip).
    if sum(v.values()) < 0:
        v = {i: -x for i, x in v.items()}
    return v


# ---------------- Theme vectors ----------------

def theme_vector_for_surah(roots_in_surah, n_words):
    """8-D vector; component k = (count of distinct roots from theme-k present
       in surah) / n_words * 100. Unique-distinct so we don't double-count
       repetition; rate per-100-words for size-normalisation."""
    distinct_roots = set(roots_in_surah)
    vec = []
    for theme_name, theme_roots in THEME_ROOTS.items():
        # count of distinct theme-roots present
        present = distinct_roots & theme_roots
        rate = (len(present) / max(1, n_words)) * 100.0
        vec.append(rate)
    return vec


def l2_normalize(vec):
    norm = math.sqrt(sum(v * v for v in vec))
    if norm < 1e-30:
        return [0.0 for _ in vec]
    return [v / norm for v in vec]


def cosine(a, b):
    return sum(x * y for x, y in zip(a, b))


# ---------------- Axis scoring ----------------

def axis_scores(quran, qac_per_surah, S, mean_sim, eig_cent, theme_vecs, theme_centroid,
                verse_count, letter_count):
    """Return per-surah scores for each axis. Higher = "more heart-like"."""
    sids = sorted(verse_count.keys())
    scores = {ax: {} for ax in AXES}
    median_pos = 57.5
    median_vc = sorted(verse_count.values())[len(verse_count) // 2]
    median_lc = sorted(letter_count.values())[len(letter_count) // 2]

    for sid in sids:
        # A1: mushaf position closest to 57.5 (max score = -|pos - 57.5|)
        scores["A1_mushaf_position_median"][sid] = -abs(sid - median_pos)
        # A2: verse-count closest to median (max score = -|vc - median|)
        scores["A2_verse_count_median"][sid] = -abs(verse_count[sid] - median_vc)
        # A3: letter-count closest to median
        scores["A3_letter_count_median"][sid] = -abs(letter_count[sid] - median_lc)
        # A4: mean-sim
        scores["A4_lexical_centroid"][sid] = mean_sim[sid]
        # A5: eigenvector centrality
        scores["A5_eigenvector_centrality"][sid] = eig_cent[sid]
        # A6: cosine of theme vector to corpus theme centroid
        scores["A6_theme_centroid"][sid] = cosine(theme_vecs[sid], theme_centroid)

    return scores, median_vc, median_lc


def rank_of(target_sid, scores_for_axis, sids):
    """Return 1-indexed rank where 1 = highest score. Ties broken by sid."""
    sorted_sids = sorted(sids, key=lambda s: (-scores_for_axis[s], s))
    return sorted_sids.index(target_sid) + 1, sorted_sids[:5]


# ---------------- Main ----------------

def main():
    rng = random.Random(SEED)

    print("Loading Quran (no-tashkeel)...", file=sys.stderr)
    quran = load_quran_no_tashkeel()
    print("Loading QAC morphology...", file=sys.stderr)
    qac_per_surah, corpus_root_count, qac_word_count = load_qac_roots_per_surah()
    print("Loading divine-names CSV...", file=sys.stderr)
    divine_sum = load_divine_density()

    print("Computing per-surah scalars (verse_count, letter_count)...", file=sys.stderr)
    verse_count, letter_count = per_surah_scalars(quran)

    print("Computing root sets and similarity matrix...", file=sys.stderr)
    root_sets = root_set_per_surah(qac_per_surah)
    # Make sure all 114 sids are present
    for sid in range(1, 115):
        root_sets.setdefault(sid, set())
        qac_word_count.setdefault(sid, 0)
    S, sids = jaccard_matrix(root_sets)

    print("Computing mean similarity per surah (A4)...", file=sys.stderr)
    mean_sim = mean_similarity_per_surah(S, sids)

    print("Computing eigenvector centrality (A5)...", file=sys.stderr)
    eig_cent = eigenvector_centrality(S, sids)

    print("Computing theme vectors (A6)...", file=sys.stderr)
    theme_vecs_raw = {sid: theme_vector_for_surah(qac_per_surah.get(sid, []),
                                                   qac_word_count.get(sid, 0))
                       for sid in sids}
    theme_vecs = {sid: l2_normalize(theme_vecs_raw[sid]) for sid in sids}
    # Corpus mean (of L2-normalised vectors), then re-normalise
    n_themes = len(THEME_ROOTS)
    sum_vec = [0.0] * n_themes
    for sid in sids:
        for k in range(n_themes):
            sum_vec[k] += theme_vecs[sid][k]
    mean_vec = [v / len(sids) for v in sum_vec]
    theme_centroid = l2_normalize(mean_vec)

    print("Scoring all 6 axes...", file=sys.stderr)
    scores, median_vc, median_lc = axis_scores(
        quran, qac_per_surah, S, mean_sim, eig_cent, theme_vecs, theme_centroid,
        verse_count, letter_count
    )

    # ---- Ranks for Q 36 + controls + diagnostics ----
    surahs_to_report = [TARGET_SURAH] + CONTROL_SURAHS + EXTRA_REPORT_SURAHS
    rank_table = {}
    for sid in surahs_to_report:
        per_axis = {}
        for ax in AXES:
            r, top5 = rank_of(sid, scores[ax], sids)
            per_axis[ax] = {
                "rank_of_surah_1to114": r,
                "score": scores[ax][sid],
                "top_5_surahs": top5,
                "p_one_sided_discrete": r / 114.0,
            }
        rank_table[sid] = per_axis

    # ---- A5 position-matched null ----
    # The score is fixed per-surah; the null draws random surah indices and
    # reports the centrality at that index. p = fraction with eig_cent ≥ obs.
    print("Building A5 position-matched null (n=10,000)...", file=sys.stderr)
    obs_q36_eig = eig_cent[TARGET_SURAH]
    n_ge = 0
    null_samples = []
    for _ in range(N_NULL_CENTRALITY):
        sid = rng.randint(1, 114)
        v = eig_cent[sid]
        null_samples.append(v)
        if v >= obs_q36_eig:
            n_ge += 1
    p_a5_null = (1 + n_ge) / (1 + N_NULL_CENTRALITY)

    # ---- PASS criterion eval ----
    q36_ranks = [rank_table[TARGET_SURAH][ax]["rank_of_surah_1to114"] for ax in AXES]
    n_rank1 = sum(1 for r in q36_ranks if r == 1)
    n_top5 = sum(1 for r in q36_ranks if r <= 5)
    if n_rank1 >= 3 or n_top5 >= 5:
        h_new_82 = "PASS"
    elif 3 <= n_top5 <= 4:
        h_new_82 = "PARTIAL"
    else:
        h_new_82 = "NULL"

    # ---- MW-5: at least one of {Q1, Q114} ranks > 57 on ≥ 4 of 6 axes ----
    mw5_per_control = {}
    mw5_ok = False
    for sid in CONTROL_SURAHS:
        ranks_c = [rank_table[sid][ax]["rank_of_surah_1to114"] for ax in AXES]
        n_bottom = sum(1 for r in ranks_c if r > 57)
        mw5_per_control[sid] = {
            "ranks": dict(zip(AXES, ranks_c)),
            "n_axes_in_bottom_half": n_bottom,
            "passes_mw5_solo": n_bottom >= 4,
        }
        if n_bottom >= 4:
            mw5_ok = True
    mw5_outcome = "PASS" if mw5_ok else "INSTRUMENT_FAIL"

    # If MW-5 fails, do not declare H-NEW-82 either way.
    overall = h_new_82 if mw5_ok else "INSTRUMENT_FAIL_NO_DECLARATION"

    # ---- Output ----
    out = {
        "id": "H-NEW-82",
        "title": "Yā-Sīn (Q 36) as the heart of the Quran — multi-axis test",
        "seed": SEED,
        "alpha_bonferroni": ALPHA_BON,
        "bonferroni_k": N_AXES,
        "axes": AXES,
        "median_verse_count_corpus": median_vc,
        "median_letter_count_corpus": median_lc,
        "q36_per_axis": rank_table[TARGET_SURAH],
        "control_surahs_per_axis": {sid: rank_table[sid] for sid in CONTROL_SURAHS},
        "diagnostic_surahs_per_axis": {sid: rank_table[sid] for sid in EXTRA_REPORT_SURAHS},
        "q36_n_rank_1": n_rank1,
        "q36_n_top_5": n_top5,
        "q36_ranks": dict(zip(AXES, q36_ranks)),
        "a5_position_matched_null": {
            "n_null": N_NULL_CENTRALITY,
            "observed_q36_centrality": obs_q36_eig,
            "p_one_sided": p_a5_null,
            "bonferroni_significant": p_a5_null <= ALPHA_BON,
            "null_mean": sum(null_samples) / len(null_samples),
            "null_max": max(null_samples),
        },
        "h_new_82_pass_criterion": "Q36 rank=1 on ≥3 axes OR top-5 on ≥5 axes",
        "h_new_82_pre_mw5_outcome": h_new_82,
        "mw5_per_control": mw5_per_control,
        "mw5_outcome": mw5_outcome,
        "h_new_82_overall": overall,
    }

    # Also include the full per-surah score lists for the headline axes
    # (compact representation: top-10 for each axis).
    top10_per_axis = {}
    for ax in AXES:
        sorted_sids = sorted(sids, key=lambda s: (-scores[ax][s], s))
        top10_per_axis[ax] = [
            {"rank": i + 1, "surah": sid, "score": scores[ax][sid]}
            for i, sid in enumerate(sorted_sids[:10])
        ]
    out["top_10_per_axis"] = top10_per_axis

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-82.json"
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)

    # ---- Console summary ----
    print()
    print("=" * 80)
    print("H-NEW-82 — Yā-Sīn (Q 36) as 'heart of the Quran'")
    print("=" * 80)
    print()
    print(f"Median verse count: {median_vc}    Median letter count: {median_lc}")
    print()
    print(f"{'axis':<32} {'Q36 rank':<10} {'top score':<14} {'top surah':<10} {'top-5':<25}")
    print("-" * 100)
    for ax in AXES:
        r36 = rank_table[TARGET_SURAH][ax]["rank_of_surah_1to114"]
        s36 = rank_table[TARGET_SURAH][ax]["score"]
        top1_sid = top10_per_axis[ax][0]["surah"]
        top1_score = top10_per_axis[ax][0]["score"]
        top5 = [t["surah"] for t in top10_per_axis[ax][:5]]
        print(f"{ax:<32} {r36:<10} {s36:<14.4f} Q{top1_sid:<9} {top5}")
    print()
    print(f"Q 36 has rank-1 on {n_rank1} axes; top-5 on {n_top5} axes.")
    print()
    print(f"A5 position-matched null: observed centrality = {obs_q36_eig:.6f}, "
          f"p = {p_a5_null:.4f}")
    print()
    print("MW-5 controls (Q1, Q114) — pre-locked: ≥1 must be in bottom-half on ≥4 axes:")
    for sid, rec in mw5_per_control.items():
        print(f"  Q{sid}: n_axes_in_bottom_half = {rec['n_axes_in_bottom_half']}/6  "
              f"-> {'PASS' if rec['passes_mw5_solo'] else 'fail'}")
    print(f"MW-5 overall: {mw5_outcome}")
    print()
    print(f"H-NEW-82 overall verdict: {overall}")


if __name__ == "__main__":
    main()
