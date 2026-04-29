#!/usr/bin/env python3
"""H-NEW-280 - Q55 constrained-null Fisher-Rao salvage.

Bounded follow-up to H-NEW-127. Reuses the same QAC -> top-K roots ->
Dirichlet smoothing -> Fisher-Rao distance pipeline, but only for Q55 and
with a constrained null:

  - keep the 31 exact refrain positions fixed
  - permute only the 47 non-refrain verses across non-refrain slots
  - compute the same full 78-verse path length

This does not reopen the broader 5-surah verse-fractal family.
"""

import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260418
PERMS = 10000
SURAH_ID = 55
K_TOP = 300
DIRICHLET_ALPHA = 0.5
ALPHA_RAW = 0.05

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-280-q55-refrain-constrained-fr-null-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-280.json"

EXPECTED_REFRAIN_POSITIONS = [
    13,
    16,
    18,
    21,
    23,
    25,
    28,
    30,
    32,
    34,
    36,
    38,
    40,
    42,
    45,
    47,
    49,
    51,
    53,
    55,
    57,
    59,
    61,
    63,
    65,
    67,
    69,
    71,
    73,
    75,
    77,
]

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def norm(text):
    text = re.sub(r"[\u200c\u200d\u200e\u200f]", "", text)
    table = {
        "إ": "ا",
        "أ": "ا",
        "آ": "ا",
        "ٱ": "ا",
        "ى": "ي",
        "ة": "ه",
        "ؤ": "و",
        "ئ": "ي",
        "ء": "",
    }
    text = "".join(table.get(ch, ch) for ch in text)
    return re.sub(r"\s+", " ", text).strip()


def q(sorted_values, frac):
    n = len(sorted_values)
    idx = max(0, min(n - 1, int(math.floor(frac * n))))
    return sorted_values[idx]


def build_distance_matrix(sqrt_probs):
    n = len(sqrt_probs)
    matrix = [[0.0] * n for _ in range(n)]
    for i in range(n):
        row_i = sqrt_probs[i]
        for j in range(i + 1, n):
            row_j = sqrt_probs[j]
            bc = 0.0
            for k in range(K_TOP):
                bc += row_i[k] * row_j[k]
            bc = max(-1.0, min(1.0, bc))
            dist = 2.0 * math.acos(bc)
            matrix[i][j] = dist
            matrix[j][i] = dist
    return matrix


def path_length(matrix, order):
    total = 0.0
    for i in range(len(order) - 1):
        total += matrix[order[i]][order[i + 1]]
    return total


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"PERMS = {PERMS}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)

    per_verse_roots = defaultdict(list)
    global_root_counts = Counter()
    with open(QAC_FILE, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            match = LOC_RE.match(parts[0])
            if not match:
                continue
            sid = int(match.group(1))
            vid = int(match.group(2))
            feats = parts[3]
            if "STEM" not in feats:
                continue
            root_match = ROOT_RE.search(feats)
            if not root_match:
                continue
            root = root_match.group(1)
            per_verse_roots[(sid, vid)].append(root)
            global_root_counts[root] += 1

    total_tokens = sum(global_root_counts.values())
    top_roots = [root for root, _ in global_root_counts.most_common(K_TOP)]
    top_root_index = {root: idx for idx, root in enumerate(top_roots)}
    topk_coverage = sum(global_root_counts[root] for root in top_roots) / total_tokens
    print(f"total STEM root tokens = {total_tokens}", file=sys.stderr)
    print(f"global distinct roots = {len(global_root_counts)}", file=sys.stderr)
    print(f"top-K coverage = {topk_coverage:.6f}", file=sys.stderr)

    quran = json.loads(QURAN_JSON.read_text())
    surah = quran[SURAH_ID - 1]
    assert surah["id"] == SURAH_ID
    verses = surah["verses"]
    assert len(verses) == 78

    refrain_norm = norm(verses[12]["text"])
    refrain_positions = [verse["id"] for verse in verses if norm(verse["text"]) == refrain_norm]
    if refrain_positions != EXPECTED_REFRAIN_POSITIONS:
        raise RuntimeError(
            f"Refrain positions mismatch: expected {EXPECTED_REFRAIN_POSITIONS}, got {refrain_positions}"
        )

    non_refrain_positions = [
        verse["id"] for verse in verses if verse["id"] not in set(refrain_positions)
    ]
    print(f"refrain positions = {refrain_positions}", file=sys.stderr)
    print(f"non-refrain count = {len(non_refrain_positions)}", file=sys.stderr)

    sqrt_probs = []
    token_counts = []
    for verse in verses:
        roots = per_verse_roots.get((SURAH_ID, verse["id"]), [])
        row = [0.0] * K_TOP
        for root in roots:
            idx = top_root_index.get(root)
            if idx is not None:
                row[idx] += 1.0
        smoothed = [value + DIRICHLET_ALPHA for value in row]
        total = sum(smoothed)
        sqrt_probs.append([math.sqrt(value / total) for value in smoothed])
        token_counts.append(len(roots))

    matrix = build_distance_matrix(sqrt_probs)
    all_distances = [
        matrix[i][j] for i in range(len(matrix)) for j in range(i + 1, len(matrix))
    ]
    d_stats = {
        "min": min(all_distances),
        "max": max(all_distances),
        "mean": statistics.mean(all_distances),
        "n_pairs": len(all_distances),
    }

    canon_order = list(range(len(verses)))
    L_canon = path_length(matrix, canon_order)
    print(f"L_canon = {L_canon:.6f}", file=sys.stderr)

    refrain_slots = [position - 1 for position in refrain_positions]
    non_refrain_slots = [position - 1 for position in non_refrain_positions]
    refrain_verse_ids = refrain_slots[:]
    non_refrain_verse_ids = non_refrain_slots[:]

    rng = random.Random(SEED)
    null_lengths = []
    for perm_idx in range(PERMS):
        permuted_non_refrain = non_refrain_verse_ids[:]
        rng.shuffle(permuted_non_refrain)
        order = [None] * len(verses)
        for slot, verse_idx in zip(refrain_slots, refrain_verse_ids):
            order[slot] = verse_idx
        for slot, verse_idx in zip(non_refrain_slots, permuted_non_refrain):
            order[slot] = verse_idx
        null_lengths.append(path_length(matrix, order))
        if (perm_idx + 1) % 2000 == 0:
            print(f"  perms complete: {perm_idx + 1}", file=sys.stderr)

    null_lengths.sort()
    null_mean = statistics.mean(null_lengths)
    null_sd = statistics.pstdev(null_lengths)
    n_perms_le_canon = sum(1 for value in null_lengths if value <= L_canon)
    p_value = (n_perms_le_canon + 1) / (PERMS + 1)
    z_score = (L_canon - null_mean) / null_sd if null_sd > 0 else 0.0
    pass_primary = p_value < ALPHA_RAW
    anti_geodesic = z_score > 0

    print(
        (
            "constrained null: "
            f"mean={null_mean:.6f} sd={null_sd:.6f} "
            f"z={z_score:.6f} p={p_value:.6f} "
            f"anti_geodesic={anti_geodesic}"
        ),
        file=sys.stderr,
    )

    result = {
        "finding_id": "h-new-280",
        "title": "Q55 Fisher-Rao constrained-null salvage: fixed refrain slots, shuffled non-refrain verses",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-18",
        "parent_backdrop": ["h-new-127", "h-new-83"],
        "scope_note": (
            "Q55 only. Fixed 31 refrain slots; permute only the 47 non-refrain verses "
            "across the 47 non-refrain slots; compute the same full 78-verse Fisher-Rao path."
        ),
        "rules_tuple": (
            "(Q55 only; no-tashkeel; QAC-STEM root tokens; QAC v0.4; Hafs-Kufan; "
            "K=300 top global roots; Dirichlet alpha=0.5; Fisher-Rao angular distance; "
            "full 78-verse path length)"
        ),
        "locked_params": {
            "surah_id": SURAH_ID,
            "K_top_roots": K_TOP,
            "dirichlet_alpha": DIRICHLET_ALPHA,
            "permutations": PERMS,
            "alpha_raw": ALPHA_RAW,
            "distance": "Fisher-Rao angular = 2*arccos(sum sqrt(p_i*p_j))",
            "refrain_positions": refrain_positions,
            "n_refrain": len(refrain_positions),
            "n_non_refrain": len(non_refrain_positions),
        },
        "corpus_stats": {
            "total_stem_root_tokens": total_tokens,
            "global_distinct_roots": len(global_root_counts),
            "top_K_coverage_fraction": round(topk_coverage, 6),
        },
        "instrument_checks": {
            "refrain_positions_match_h_new_83": True,
            "n_verses_q55": len(verses),
            "mean_root_tokens_per_verse": round(sum(token_counts) / len(token_counts), 6),
        },
        "q55": {
            "L_canon": round(L_canon, 6),
            "null_mean": round(null_mean, 6),
            "null_sd": round(null_sd, 6),
            "delta_canon_minus_null_mean": round(L_canon - null_mean, 6),
            "z_score": round(z_score, 6),
            "n_perms_le_canon": n_perms_le_canon,
            "p_value_one_sided_lower": round(p_value, 12),
            "pass_primary": pass_primary,
            "anti_geodesic_under_constrained_null": anti_geodesic,
            "canonical_shorter_than_null_mean": L_canon < null_mean,
            "null_min": round(min(null_lengths), 6),
            "null_max": round(max(null_lengths), 6),
            "null_quantiles": {
                "q001": round(q(null_lengths, 0.001), 6),
                "q005": round(q(null_lengths, 0.005), 6),
                "q01": round(q(null_lengths, 0.01), 6),
                "q025": round(q(null_lengths, 0.025), 6),
                "q05": round(q(null_lengths, 0.05), 6),
                "q25": round(q(null_lengths, 0.25), 6),
                "q50": round(q(null_lengths, 0.50), 6),
                "q75": round(q(null_lengths, 0.75), 6),
                "q95": round(q(null_lengths, 0.95), 6),
            },
            "D_stats": {
                "min": round(d_stats["min"], 6),
                "max": round(d_stats["max"], 6),
                "mean": round(d_stats["mean"], 6),
                "n_pairs": d_stats["n_pairs"],
            },
        },
        "verdict": "PASS-BOUNDED" if pass_primary else "NULL",
    }

    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=True) + "\n")
    print(f"wrote {OUT_JSON}", file=sys.stderr)


if __name__ == "__main__":
    main()
