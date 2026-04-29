#!/usr/bin/env python3
"""H-NEW-132: Q7/Q11 prophet-cycle parallelism."""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
MORPH_PATH = PROJECT_ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
TEXT_PATH = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
PREREG_PATH = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-132-prophet-cycle-parallelism-prereg.md"
)
OUTPUT_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-132.json"

SEED = 20260418
ALPHA_BON = 0.025
DIRICHLET_ALPHA = 0.5

BLOCKS = [
    {
        "prophet": "Noah",
        "q7": (59, 64),
        "q11": (25, 49),
    },
    {
        "prophet": "Hud",
        "q7": (65, 72),
        "q11": (50, 60),
    },
    {
        "prophet": "Salih",
        "q7": (73, 79),
        "q11": (61, 68),
    },
    {
        "prophet": "Lot",
        "q7": (80, 84),
        "q11": (77, 83),
    },
    {
        "prophet": "Shuayb",
        "q7": (85, 93),
        "q11": (84, 95),
    },
]

ROOT_RE = re.compile(r"ROOT:([^|\s]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")
POS_RE = re.compile(r"POS:([A-Z]+)")
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_text() -> dict[tuple[int, int], str]:
    verse_text: dict[tuple[int, int], str] = {}
    data = json.loads(TEXT_PATH.read_text())
    for surah in data:
        sid = int(surah.get("id", 0) or surah.get("index", 0))
        for verse in surah["verses"]:
            verse_text[(sid, int(verse["id"]))] = verse["text"]
    return verse_text


def load_morphology() -> tuple[dict[tuple[int, int], Counter], dict[tuple[int, int], Counter]]:
    roots_by_verse: dict[tuple[int, int], Counter] = defaultdict(Counter)
    pn_lemmas_by_verse: dict[tuple[int, int], Counter] = defaultdict(Counter)
    with MORPH_PATH.open() as handle:
        for raw_line in handle:
            if not raw_line.startswith("("):
                continue
            parts = raw_line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = LOC_RE.match(parts[0])
            if not loc:
                continue
            surah, verse, _word, _seg = map(int, loc.groups())
            feats = parts[3]
            pos_match = POS_RE.search(feats)
            pos = pos_match.group(1) if pos_match else None
            root_match = ROOT_RE.search(feats)
            lemma_match = LEM_RE.search(feats)

            if root_match and pos != "PN":
                roots_by_verse[(surah, verse)][root_match.group(1)] += 1
            if lemma_match and pos == "PN":
                pn_lemmas_by_verse[(surah, verse)][lemma_match.group(1)] += 1
    return roots_by_verse, pn_lemmas_by_verse


def window_counter(
    verse_counters: dict[tuple[int, int], Counter],
    surah: int,
    start: int,
    end: int,
) -> Counter:
    out: Counter = Counter()
    for verse in range(start, end + 1):
        out.update(verse_counters.get((surah, verse), Counter()))
    return out


def fisher_rao_distance(
    left: Counter,
    right: Counter,
    vocab: list[str],
    alpha: float,
) -> float:
    if not vocab:
        return 0.0
    left_total = sum(left.values()) + alpha * len(vocab)
    right_total = sum(right.values()) + alpha * len(vocab)
    bc = 0.0
    for token in vocab:
        p = (left.get(token, 0) + alpha) / left_total
        q = (right.get(token, 0) + alpha) / right_total
        bc += math.sqrt(p * q)
    bc = min(1.0, max(0.0, bc))
    return 2.0 * math.acos(bc)


def distance_matrix(
    q7_counts: list[Counter],
    q11_counts: list[Counter],
    alpha: float,
) -> tuple[list[list[float]], list[str]]:
    vocab = sorted({token for counter in (q7_counts + q11_counts) for token in counter})
    matrix: list[list[float]] = []
    for left in q7_counts:
        row = []
        for right in q11_counts:
            row.append(fisher_rao_distance(left, right, vocab, alpha))
        matrix.append(row)
    return matrix, vocab


def all_assignments(n: int) -> list[tuple[int, ...]]:
    return list(itertools.permutations(range(n)))


def assignment_sum(matrix: list[list[float]], perm: tuple[int, ...]) -> float:
    return sum(matrix[row_idx][col_idx] for row_idx, col_idx in enumerate(perm))


def nearest_neighbor_hits(matrix: list[list[float]], perm: tuple[int, ...]) -> tuple[int, list[int]]:
    argmins: list[int] = []
    for row in matrix:
        best_col = min(range(len(row)), key=lambda idx: (row[idx], idx))
        argmins.append(best_col)
    hits = sum(1 for row_idx, col_idx in enumerate(argmins) if col_idx == perm[row_idx])
    return hits, argmins


def summarize_assignment_test(
    matrix: list[list[float]],
    labels: list[str],
) -> dict:
    n = len(labels)
    perms = all_assignments(n)
    identity = tuple(range(n))
    observed = assignment_sum(matrix, identity)
    scored = []
    for perm in perms:
        scored.append(
            {
                "perm": perm,
                "sum_distance": assignment_sum(matrix, perm),
            }
        )
    scored.sort(key=lambda item: (item["sum_distance"], item["perm"]))
    rank = next(i for i, item in enumerate(scored, start=1) if item["perm"] == identity)
    count_le = sum(1 for item in scored if item["sum_distance"] <= observed + 1e-12)
    best_alt = next(item for item in scored if item["perm"] != identity)
    p_value = count_le / len(scored)
    return {
        "labels": labels,
        "n_permutations": len(scored),
        "observed_assignment": {labels[i]: labels[col] for i, col in enumerate(identity)},
        "observed_sum_distance": observed,
        "rank_among_all_assignments": rank,
        "count_assignments_le_observed": count_le,
        "p_exact_one_sided_lower": p_value,
        "runner_up_assignment": {labels[i]: labels[col] for i, col in enumerate(best_alt["perm"])},
        "runner_up_sum_distance": best_alt["sum_distance"],
        "margin_to_runner_up": best_alt["sum_distance"] - observed,
    }


def summarize_nn_test(
    matrix: list[list[float]],
    labels: list[str],
) -> dict:
    perms = all_assignments(len(labels))
    identity = tuple(range(len(labels)))
    observed_hits, argmins = nearest_neighbor_hits(matrix, identity)
    null_hits = []
    for perm in perms:
        hits, _ = nearest_neighbor_hits(matrix, perm)
        null_hits.append(hits)
    count_ge = sum(1 for value in null_hits if value >= observed_hits)
    nearest = {labels[row]: labels[col] for row, col in enumerate(argmins)}
    return {
        "rowwise_nearest_neighbors": nearest,
        "observed_hits": observed_hits,
        "max_possible_hits": len(labels),
        "p_exact_one_sided_upper": count_ge / len(perms),
        "count_permutations_ge_observed": count_ge,
    }


def matrix_to_labeled_rows(matrix: list[list[float]], labels: list[str]) -> list[dict]:
    rows = []
    for row_label, row in zip(labels, matrix):
        rows.append(
            {
                "row": row_label,
                "distances": {col_label: row[idx] for idx, col_label in enumerate(labels)},
            }
        )
    return rows


def top_items(counter: Counter, n: int = 10) -> list[list[object]]:
    return [[token, count] for token, count in counter.most_common(n)]


def main() -> None:
    verse_text = load_text()
    roots_by_verse, pn_lemmas_by_verse = load_morphology()
    labels = [block["prophet"] for block in BLOCKS]

    q7_root_counts = []
    q11_root_counts = []
    q7_pn_counts = []
    q11_pn_counts = []
    window_stats = []

    for block in BLOCKS:
        q7_start, q7_end = block["q7"]
        q11_start, q11_end = block["q11"]
        q7_roots = window_counter(roots_by_verse, 7, q7_start, q7_end)
        q11_roots = window_counter(roots_by_verse, 11, q11_start, q11_end)
        q7_pn = window_counter(pn_lemmas_by_verse, 7, q7_start, q7_end)
        q11_pn = window_counter(pn_lemmas_by_verse, 11, q11_start, q11_end)

        q7_root_counts.append(q7_roots)
        q11_root_counts.append(q11_roots)
        q7_pn_counts.append(q7_pn)
        q11_pn_counts.append(q11_pn)

        window_stats.append(
            {
                "prophet": block["prophet"],
                "q7": {
                    "surah": 7,
                    "start": q7_start,
                    "end": q7_end,
                    "verse_count": q7_end - q7_start + 1,
                    "root_token_count": sum(q7_roots.values()),
                    "unique_roots": len(q7_roots),
                    "top_roots": top_items(q7_roots),
                    "pn_lemmas": top_items(q7_pn),
                    "opening_text": verse_text[(7, q7_start)],
                    "closing_text": verse_text[(7, q7_end)],
                },
                "q11": {
                    "surah": 11,
                    "start": q11_start,
                    "end": q11_end,
                    "verse_count": q11_end - q11_start + 1,
                    "root_token_count": sum(q11_roots.values()),
                    "unique_roots": len(q11_roots),
                    "top_roots": top_items(q11_roots),
                    "pn_lemmas": top_items(q11_pn),
                    "opening_text": verse_text[(11, q11_start)],
                    "closing_text": verse_text[(11, q11_end)],
                },
            }
        )

    primary_matrix, primary_vocab = distance_matrix(
        q7_root_counts,
        q11_root_counts,
        alpha=DIRICHLET_ALPHA,
    )
    positive_matrix, positive_vocab = distance_matrix(
        q7_pn_counts,
        q11_pn_counts,
        alpha=DIRICHLET_ALPHA,
    )

    primary = summarize_assignment_test(primary_matrix, labels)
    secondary = summarize_nn_test(primary_matrix, labels)
    positive = summarize_assignment_test(positive_matrix, labels)

    positive_pass = positive["count_assignments_le_observed"] == 1
    primary_pass = primary["p_exact_one_sided_lower"] < ALPHA_BON
    secondary_pass = (
        secondary["p_exact_one_sided_upper"] < ALPHA_BON
        and secondary["observed_hits"] == len(labels)
    )

    if not positive_pass:
        verdict = "INSTRUMENT-BROKEN"
    elif primary_pass and secondary_pass:
        verdict = "PASS-DIRECTED"
    elif primary_pass:
        verdict = "PARTIAL-PASS"
    else:
        verdict = "NULL"

    diagonal_distances = {
        labels[i]: primary_matrix[i][i] for i in range(len(labels))
    }
    offdiag_values = [
        primary_matrix[i][j]
        for i in range(len(labels))
        for j in range(len(labels))
        if i != j
    ]
    diag_mean = sum(diagonal_distances.values()) / len(diagonal_distances)
    offdiag_mean = sum(offdiag_values) / len(offdiag_values)

    output = {
        "finding_id": "h-new-132",
        "title": "Q7 Al-A'raf vs Q11 Hud prophet-cycle parallelism",
        "date": "2026-04-18",
        "seed": SEED,
        "pre_reg_path": str(PREREG_PATH),
        "pre_reg_sha256": sha256_file(PREREG_PATH),
        "rules_tuple": "(QAC-v0.4 morphology roots; POS!=PN for primary/secondary, POS=PN lemmas for positive control; Hafs-Kufan verse numbering; basmala counted only in Surah 1; Fisher-Rao arccos-Bhattacharyya on L1-normalized window distributions; exact 5! assignment null)",
        "bonferroni_k": 2,
        "bonferroni_family": "h-new-132-q7-q11-prophet-cycle",
        "alpha_bon": ALPHA_BON,
        "dirichlet_alpha": DIRICHLET_ALPHA,
        "labels": labels,
        "windows": window_stats,
        "primary_distance_matrix_roots_no_pn": matrix_to_labeled_rows(primary_matrix, labels),
        "primary_root_vocab_size": len(primary_vocab),
        "primary": primary
        | {
            "diagonal_distances": diagonal_distances,
            "diagonal_mean_distance": diag_mean,
            "off_diagonal_mean_distance": offdiag_mean,
            "mean_gap_offdiag_minus_diag": offdiag_mean - diag_mean,
            "pass_primary": primary_pass,
        },
        "secondary": secondary | {"pass_secondary": secondary_pass},
        "positive_control_pn_only": positive
        | {
            "distance_matrix": matrix_to_labeled_rows(positive_matrix, labels),
            "pn_vocab_size": len(positive_vocab),
            "pass_positive_control": positive_pass,
        },
        "verdict": verdict,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False))

    print("=" * 72)
    print("H-NEW-132 — Q7/Q11 prophet-cycle parallelism")
    print("=" * 72)
    print(f"Verdict: {verdict}")
    print(f"Primary p_exact: {primary['p_exact_one_sided_lower']:.6f}")
    print(
        "Primary diagonal mean vs off-diagonal mean: "
        f"{diag_mean:.4f} vs {offdiag_mean:.4f}"
    )
    print(
        "Secondary nearest-neighbor hits: "
        f"{secondary['observed_hits']}/{secondary['max_possible_hits']} "
        f"(p={secondary['p_exact_one_sided_upper']:.6f})"
    )
    print(
        "Positive control p_exact: "
        f"{positive['p_exact_one_sided_lower']:.6f} "
        f"(unique min={positive_pass})"
    )
    print("Canonical diagonal distances:")
    for label in labels:
        print(f"  {label:7s} {diagonal_distances[label]:.4f}")
    print(f"Output JSON: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
