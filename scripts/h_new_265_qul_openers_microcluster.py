#!/usr/bin/env python3
"""H-NEW-265 — opener-stripped micro-cluster test for the five v1-w1 qul-openers.

Pre-reg:
  findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster-prereg.md

Three inferential cells, all one-sided upper:
  A. v1 after dropping w1            -> mean pairwise root-set Jaccard
  B. v1-v3 after dropping v1-w1      -> mean pairwise root-set Jaccard
  C. whole surah excluding opener root
     (qwl for target, sbH for MW-5)  -> mean pairwise root-set Jaccard

Null:
  10,000 random 5-sets matched at the cell level on nearest-12
  log-token-mass neighbors, sampled without replacement.
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-265-qul-openers-microcluster-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-265.json"

SEED = 20260418
N_PERM = 10_000
MATCH_K = 12
ALPHA_BON = 0.05 / 3

TARGET = [72, 109, 112, 113, 114]
MW5 = [57, 59, 61, 62, 64]

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def load_quran_meta() -> dict[int, dict]:
    with QURAN_JSON.open(encoding="utf-8") as fh:
        quran = json.load(fh)
    out = {}
    for s in quran:
        out[s["id"]] = {
            "name": s["name"],
            "transliteration": s["transliteration"],
            "type": s["type"],
            "verse_count": len(s["verses"]),
        }
    assert len(out) == 114
    return out


def load_qac_roots():
    per_word = defaultdict(set)   # (sid, vid, wid) -> {root, ...}
    per_surah = defaultdict(list)  # sid -> [root, ...] with token multiplicity
    with QAC_FILE.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid, vid, wid = int(m.group(1)), int(m.group(2)), int(m.group(3))
            feats = parts[3]
            if "STEM" not in feats:
                continue
            rm = ROOT_RE.search(feats)
            if not rm:
                continue
            root = rm.group(1)
            per_word[(sid, vid, wid)].add(root)
            per_surah[sid].append(root)
    assert len(per_surah) == 114

    by_surah_word = defaultdict(list)
    for (sid, vid, wid), roots in per_word.items():
        by_surah_word[sid].append((vid, wid, frozenset(roots)))
    for sid in range(1, 115):
        by_surah_word[sid].sort()
    return by_surah_word, per_surah


def build_window_sets(
    by_surah_word: dict[int, list[tuple[int, int, frozenset[str]]]],
    include_fn,
    exclude_roots: set[str] | None = None,
):
    exclude_roots = exclude_roots or set()
    root_sets = {}
    token_mass = {}
    for sid in range(1, 115):
        roots_here = set()
        mass_here = 0
        for vid, wid, roots in by_surah_word.get(sid, []):
            if not include_fn(vid, wid):
                continue
            kept = [r for r in roots if r not in exclude_roots]
            if not kept:
                continue
            roots_here.update(kept)
            mass_here += len(kept)
        root_sets[sid] = roots_here
        token_mass[sid] = mass_here
    return root_sets, token_mass


def build_full_surah_sets(
    per_surah_roots: dict[int, list[str]],
    exclude_roots: set[str],
):
    root_sets = {}
    token_mass = {}
    for sid in range(1, 115):
        kept = [r for r in per_surah_roots[sid] if r not in exclude_roots]
        root_sets[sid] = set(kept)
        token_mass[sid] = len(kept)
    return root_sets, token_mass


def jaccard(a: set[str], b: set[str]) -> float:
    union = a | b
    if not union:
        return 0.0
    return len(a & b) / len(union)


def pairwise_scores(ids: list[int], root_sets: dict[int, set[str]]):
    rows = []
    for a, b in combinations(ids, 2):
        rows.append({"pair": [a, b], "jaccard": jaccard(root_sets[a], root_sets[b])})
    return rows


def mean_pairwise_jaccard(ids: list[int], root_sets: dict[int, set[str]]) -> float:
    vals = [row["jaccard"] for row in pairwise_scores(ids, root_sets)]
    return statistics.mean(vals) if vals else 0.0


def build_candidate_lists(token_mass: dict[int, int]) -> dict[int, list[int]]:
    candidates = {}
    for sid in range(1, 115):
        others = [o for o in range(1, 115) if o != sid]
        others.sort(
            key=lambda o: (
                abs(math.log(token_mass[o] + 1) - math.log(token_mass[sid] + 1)),
                abs(token_mass[o] - token_mass[sid]),
                o,
            )
        )
        candidates[sid] = others[:MATCH_K]
    return candidates


def sample_matched_set(
    ref_ids: list[int],
    candidates: dict[int, list[int]],
    rng: random.Random,
    max_attempts: int = 100,
):
    base_used = set(ref_ids)
    for _ in range(max_attempts):
        used = set(base_used)
        out = []
        remaining = list(ref_ids)
        ok = True
        while remaining:
            remaining.sort(key=lambda sid: sum(1 for c in candidates[sid] if c not in used))
            sid = remaining.pop(0)
            choices = [c for c in candidates[sid] if c not in used]
            if not choices:
                ok = False
                break
            pick = rng.choice(choices)
            out.append(pick)
            used.add(pick)
        if ok:
            return out
    return None


def candidate_preview(ref_ids, token_mass, candidates, meta, n=5):
    preview = {}
    for sid in ref_ids:
        preview[str(sid)] = [
            {
                "surah": cand,
                "name": meta[cand]["transliteration"],
                "token_mass": token_mass[cand],
            }
            for cand in candidates[sid][:n]
        ]
    return preview


def permutation_test(
    ids: list[int],
    root_sets: dict[int, set[str]],
    token_mass: dict[int, int],
    seed: int,
):
    candidates = build_candidate_lists(token_mass)
    rng = random.Random(seed)
    observed = mean_pairwise_jaccard(ids, root_sets)

    null = []
    failures = 0
    for _ in range(N_PERM):
        sample = sample_matched_set(ids, candidates, rng)
        if sample is None:
            failures += 1
            continue
        null.append(mean_pairwise_jaccard(sample, root_sets))

    if not null:
        raise RuntimeError("matched null failed: zero successful draws")

    null_mean = statistics.mean(null)
    null_sd = statistics.stdev(null) if len(null) > 1 else 0.0
    p_upper = (1 + sum(v >= observed for v in null)) / (1 + len(null))
    z = (observed - null_mean) / null_sd if null_sd > 0 else 0.0

    return {
        "observed": observed,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "null_median": statistics.median(null),
        "p_perm_upper": p_upper,
        "z_vs_null": z,
        "successful_draws": len(null),
        "failed_draws": failures,
        "candidate_lists": candidates,
    }


def run_cell(
    cell_id: str,
    description: str,
    target_root_sets: dict[int, set[str]],
    target_token_mass: dict[int, int],
    mw5_root_sets: dict[int, set[str]],
    mw5_token_mass: dict[int, int],
    meta: dict[int, dict],
    seed_offset: int,
):
    target_test = permutation_test(TARGET, target_root_sets, target_token_mass, SEED + seed_offset)
    mw5_test = permutation_test(MW5, mw5_root_sets, mw5_token_mass, SEED + seed_offset + 1)

    target_pairs = pairwise_scores(TARGET, target_root_sets)
    mw5_pairs = pairwise_scores(MW5, mw5_root_sets)

    result = {
        "cell": cell_id,
        "description": description,
        "direction": "one-sided upper",
        "target": {
            "members": TARGET,
            "token_mass": {str(s): target_token_mass[s] for s in TARGET},
            "pairwise_jaccard": target_pairs,
            "observed": target_test["observed"],
            "null_mean": target_test["null_mean"],
            "null_sd": target_test["null_sd"],
            "null_median": target_test["null_median"],
            "z_vs_null": target_test["z_vs_null"],
            "p_perm_upper": target_test["p_perm_upper"],
            "candidate_preview": candidate_preview(
                TARGET, target_token_mass, target_test["candidate_lists"], meta
            ),
            "successful_draws": target_test["successful_draws"],
            "failed_draws": target_test["failed_draws"],
            "pass_alpha_bon": target_test["p_perm_upper"] < ALPHA_BON,
        },
        "mw5_positive_control": {
            "members": MW5,
            "token_mass": {str(s): mw5_token_mass[s] for s in MW5},
            "pairwise_jaccard": mw5_pairs,
            "observed": mw5_test["observed"],
            "null_mean": mw5_test["null_mean"],
            "null_sd": mw5_test["null_sd"],
            "null_median": mw5_test["null_median"],
            "z_vs_null": mw5_test["z_vs_null"],
            "p_perm_upper": mw5_test["p_perm_upper"],
            "candidate_preview": candidate_preview(
                MW5, mw5_token_mass, mw5_test["candidate_lists"], meta
            ),
            "pass_nominal_0_05": mw5_test["p_perm_upper"] < 0.05,
            "successful_draws": mw5_test["successful_draws"],
            "failed_draws": mw5_test["failed_draws"],
        },
    }
    return result


def round_nested(obj):
    if isinstance(obj, float):
        return round(obj, 6)
    if isinstance(obj, list):
        return [round_nested(x) for x in obj]
    if isinstance(obj, dict):
        return {k: round_nested(v) for k, v in obj.items()}
    return obj


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED={SEED} N_PERM={N_PERM} MATCH_K={MATCH_K}", file=sys.stderr)

    meta = load_quran_meta()
    by_surah_word, per_surah_roots = load_qac_roots()
    print("Loaded QAC roots for all 114 surahs", file=sys.stderr)

    cell_a_sets, cell_a_mass = build_window_sets(
        by_surah_word,
        include_fn=lambda vid, wid: vid == 1 and wid >= 2,
    )
    cell_b_sets, cell_b_mass = build_window_sets(
        by_surah_word,
        include_fn=lambda vid, wid: vid <= 3 and not (vid == 1 and wid == 1),
    )
    cell_c_target_sets, cell_c_target_mass = build_full_surah_sets(per_surah_roots, {"qwl"})
    cell_c_mw5_sets, cell_c_mw5_mass = build_full_surah_sets(per_surah_roots, {"sbH"})

    print("[1/3] Cell A...", file=sys.stderr)
    cell_a = run_cell(
        "A",
        "v1 residual root-set Jaccard after dropping w1",
        cell_a_sets,
        cell_a_mass,
        cell_a_sets,
        cell_a_mass,
        meta,
        10,
    )
    print(
        f"  target p={cell_a['target']['p_perm_upper']:.6f} "
        f"MW5 p={cell_a['mw5_positive_control']['p_perm_upper']:.6f}",
        file=sys.stderr,
    )

    print("[2/3] Cell B...", file=sys.stderr)
    cell_b = run_cell(
        "B",
        "v1-v3 residual root-set Jaccard after dropping v1-w1",
        cell_b_sets,
        cell_b_mass,
        cell_b_sets,
        cell_b_mass,
        meta,
        20,
    )
    print(
        f"  target p={cell_b['target']['p_perm_upper']:.6f} "
        f"MW5 p={cell_b['mw5_positive_control']['p_perm_upper']:.6f}",
        file=sys.stderr,
    )

    print("[3/3] Cell C...", file=sys.stderr)
    cell_c = run_cell(
        "C",
        "whole-surah root-set Jaccard excluding trivial opener root (qwl / sbH)",
        cell_c_target_sets,
        cell_c_target_mass,
        cell_c_mw5_sets,
        cell_c_mw5_mass,
        meta,
        30,
    )
    print(
        f"  target p={cell_c['target']['p_perm_upper']:.6f} "
        f"MW5 p={cell_c['mw5_positive_control']['p_perm_upper']:.6f}",
        file=sys.stderr,
    )

    cells = [cell_a, cell_b, cell_c]
    mw5_ok = all(c["mw5_positive_control"]["pass_nominal_0_05"] for c in cells)
    n_pass = sum(1 for c in cells if c["target"]["pass_alpha_bon"])

    if not mw5_ok:
        verdict = "NULL-BROKEN"
    elif n_pass == 0:
        verdict = "NULL"
    elif n_pass == 1:
        verdict = "DIMENSION-SPECIFIC"
    else:
        verdict = "PASS-DIRECTED"

    summary = {
        "id": "H-NEW-265",
        "prereg_file": str(PREREG_FILE.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "match_k_nearest": MATCH_K,
        "bonferroni_family": "h-new-265-qul-openers-microcluster",
        "bonferroni_k": 3,
        "alpha_bon": ALPHA_BON,
        "question": (
            "Do Q72/Q109/Q112/Q113/Q114 remain a coherent family after stripping the "
            "trivial opener itself?"
        ),
        "target_set": TARGET,
        "mw5_positive_control": MW5,
        "cell_results": cells,
        "mw5_all_cells_pass_nominal": mw5_ok,
        "n_target_cells_pass_alpha_bon": n_pass,
        "verdict": verdict,
    }

    OUT_JSON.write_text(
        json.dumps(round_nested(summary), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUT_JSON}", file=sys.stderr)
    print(f"VERDICT = {verdict}  ({n_pass}/3 Bonferroni cells; MW-5={mw5_ok})", file=sys.stderr)


if __name__ == "__main__":
    main()
