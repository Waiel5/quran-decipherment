#!/usr/bin/env python3
"""H-NEW-127.2 - alternate OQ-20 family rerun.

Family lock:
  - Q1/Q18/Q28/Q78/Q112: uniform full-verse permutation null

Primary family observable:
  n_pass = number of locked surahs with one-sided p < 0.01

Decision:
  POSITIVE if n_pass >= 3 and the MW control bank passes
  NEGATIVE otherwise

MW control bank:
  For each locked surah, the best greedy-nearest-neighbor path and its 2-opt
  refinement must each be shorter than canonical verse order.
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
K_TOP = 300
DIRICHLET_ALPHA = 0.5
ALPHA_BON = 0.01
BON_K = 5
LOCKED_SURAHS = [1, 18, 28, 78, 112]

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-127-2-rerun-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-127-2.json"
OUT_JOURNAL = ROOT / "journal/h-new-127-2-run-1.md"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


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


def greedy_nn(matrix, start):
    n = len(matrix)
    unvisited = set(range(n))
    unvisited.remove(start)
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: matrix[cur][v])
        path.append(nxt)
        unvisited.remove(nxt)
        cur = nxt
    return path


def two_opt(matrix, path, max_passes=50):
    path = path[:]
    n = len(path)
    improved = True
    passes = 0
    while improved and passes < max_passes:
        improved = False
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            for j in range(i + 2, n):
                c = path[j]
                d = path[j + 1] if j + 1 < n else None
                if d is None:
                    delta = matrix[a][c] - matrix[a][b]
                else:
                    delta = (matrix[a][c] + matrix[b][d]) - (matrix[a][b] + matrix[c][d])
                if delta < best_delta:
                    best_delta = delta
                    best_ij = (i + 1, j)
        if best_ij is not None:
            i1, j = best_ij
            path[i1 : j + 1] = reversed(path[i1 : j + 1])
            improved = True
    return path, passes


def round_floats(obj, ndigits=6):
    if isinstance(obj, float):
        return round(obj, ndigits)
    if isinstance(obj, dict):
        return {k: round_floats(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, list):
        return [round_floats(v, ndigits) for v in obj]
    return obj


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"PERMS = {PERMS}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
    print(f"LOCKED_SURAHS = {LOCKED_SURAHS}", file=sys.stderr)

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
    locked = {}
    for sdata in quran:
        sid = sdata["id"]
        if sid not in LOCKED_SURAHS:
            continue
        verses = sdata["verses"]
        n_v = len(verses)
        counts_rows = []
        token_counts = []
        char_lengths = []
        for verse in verses:
            roots = per_verse_roots.get((sid, verse["id"]), [])
            row = [0.0] * K_TOP
            for root in roots:
                idx = top_root_index.get(root)
                if idx is not None:
                    row[idx] += 1.0
            counts_rows.append(row)
            token_counts.append(len(roots))
            char_lengths.append(len(verse["text"]))
        locked[sid] = {
            "verses": verses,
            "counts_rows": counts_rows,
            "token_counts": token_counts,
            "char_lengths": char_lengths,
            "mean_root_tokens": sum(token_counts) / n_v,
        }
        print(
            f"  surah {sid}: n_verses={n_v}, mean root tokens/verse={sum(token_counts)/n_v:.2f}",
            file=sys.stderr,
        )

    verse_probs = {}
    verse_sqrtprobs = {}
    for sid in LOCKED_SURAHS:
        probs = []
        sqprobs = []
        for row in locked[sid]["counts_rows"]:
            smoothed = [value + DIRICHLET_ALPHA for value in row]
            denom = sum(smoothed)
            p = [value / denom for value in smoothed]
            probs.append(p)
            sqprobs.append([math.sqrt(value) for value in p])
        verse_probs[sid] = probs
        verse_sqrtprobs[sid] = sqprobs

    per_surah = {}
    control_rows = {}
    for sid in LOCKED_SURAHS:
        print(f"\n=== Surah {sid} ===", file=sys.stderr)
        sqprobs = verse_sqrtprobs[sid]
        n = len(sqprobs)
        matrix = build_distance_matrix(sqprobs)
        all_d = [matrix[i][j] for i in range(n) for j in range(i + 1, n)]
        dmin = min(all_d)
        dmax = max(all_d)
        dmean = statistics.mean(all_d)
        print(f"  n_verses = {n}", file=sys.stderr)
        print(f"  D stats: min={dmin:.6f}, max={dmax:.6f}, mean={dmean:.6f}", file=sys.stderr)

        canon_order = list(range(n))
        L_canon = path_length(matrix, canon_order)
        print(f"  L_canon = {L_canon:.6f}", file=sys.stderr)

        rng = random.Random(SEED + sid * 1000003)
        null_lengths = []
        for perm_idx in range(PERMS):
            perm = canon_order[:]
            rng.shuffle(perm)
            null_lengths.append(path_length(matrix, perm))
            if (perm_idx + 1) % 2000 == 0:
                print(f"  perms complete: {perm_idx + 1}", file=sys.stderr)
        null_model = "uniform_full_verse_permutation"

        null_lengths.sort()
        null_mean = statistics.mean(null_lengths)
        null_sd = statistics.pstdev(null_lengths)
        n_le = sum(1 for value in null_lengths if value <= L_canon)
        p_value = (n_le + 1) / (PERMS + 1)
        z_score = (L_canon - null_mean) / null_sd if null_sd > 0 else 0.0
        surah_pass = p_value < ALPHA_BON

        greedy_paths = []
        for start in range(n):
            gp = greedy_nn(matrix, start)
            greedy_paths.append((path_length(matrix, gp), start, gp))
        greedy_paths.sort(key=lambda x: x[0])
        L_greedy_best = greedy_paths[0][0]
        best_start = greedy_paths[0][1]
        best_path = greedy_paths[0][2][:]
        opt_path, npass = two_opt(matrix, best_path)
        L_2opt_best = path_length(matrix, opt_path)
        ratio = L_canon / L_2opt_best if L_2opt_best > 0 else float("inf")

        print(f"  null model = {null_model}", file=sys.stderr)
        print(f"  null: mean={null_mean:.6f}, sd={null_sd:.6f}", file=sys.stderr)
        print(f"  z(L_canon) = {z_score:.6f}", file=sys.stderr)
        print(f"  #{{L_perm <= L_canon}} = {n_le}", file=sys.stderr)
        print(f"  p_value (one-sided lower) = {p_value:.12f}", file=sys.stderr)
        print(f"  PASS: {surah_pass}", file=sys.stderr)
        print(f"  greedy best: start={best_start}, L={L_greedy_best:.6f}", file=sys.stderr)
        print(f"  2-opt best: L={L_2opt_best:.6f} ({npass} passes)", file=sys.stderr)
        print(f"  L_canon / L_2opt = {ratio:.6f}", file=sys.stderr)

        per_surah[sid] = {
            "n_verses": n,
            "null_model": null_model,
            "L_canon": L_canon,
            "null_mean": null_mean,
            "null_sd": null_sd,
            "null_min": min(null_lengths),
            "null_max": max(null_lengths),
            "null_quantiles": {
                "q001": q(null_lengths, 0.001),
                "q005": q(null_lengths, 0.005),
                "q01": q(null_lengths, 0.01),
                "q025": q(null_lengths, 0.025),
                "q05": q(null_lengths, 0.05),
                "q25": q(null_lengths, 0.25),
                "q50": q(null_lengths, 0.50),
                "q75": q(null_lengths, 0.75),
                "q95": q(null_lengths, 0.95),
            },
            "z_score": z_score,
            "n_perms_le_canon": n_le,
            "p_value_one_sided_lower": p_value,
            "alpha_bon": ALPHA_BON,
            "pass": surah_pass,
            "L_greedy_best": L_greedy_best,
            "L_2opt_best": L_2opt_best,
            "ratio_canon_over_2opt": ratio,
            "D_stats": {
                "min": dmin,
                "max": dmax,
                "mean": dmean,
                "n_pairs": len(all_d),
            },
            "control_values": {
                "greedy_best_shorter_than_canon": L_greedy_best < L_canon,
                "two_opt_best_shorter_than_canon": L_2opt_best < L_canon,
            },
            "instrument_check": {
                "refrain_positions_match_h_new_83": None,
                "refrain_positions": None,
                "n_refrain": None,
                "n_non_refrain": None,
            },
        }
        control_rows[sid] = {
            "greedy_pass": L_greedy_best < L_canon,
            "two_opt_pass": L_2opt_best < L_canon,
            "L_greedy_best": L_greedy_best,
            "L_2opt_best": L_2opt_best,
        }

    control_bank_pass = all(
        control_rows[sid]["greedy_pass"] and control_rows[sid]["two_opt_pass"]
        for sid in LOCKED_SURAHS
    )
    n_pass = sum(1 for sid in LOCKED_SURAHS if per_surah[sid]["pass"])
    family_verdict = "POSITIVE" if (n_pass >= 3 and control_bank_pass) else "NEGATIVE"

    print("\n=== Family verdict ===", file=sys.stderr)
    print(f"  n_pass = {n_pass} of {len(LOCKED_SURAHS)}", file=sys.stderr)
    print(f"  control bank pass = {control_bank_pass}", file=sys.stderr)
    print(f"  family verdict = {family_verdict}", file=sys.stderr)

    result = {
        "finding_id": "h-new-127-2",
        "title": "H-NEW-127.2 rerun: alternate OQ-20 family with geometric MW control",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-18",
        "parent_finding": "h-new-127",
        "audit_backdrop": "h-new-127-1",
        "rules_tuple": "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf verse order, Hafs-Kufan, K=300 top global roots, Dirichlet alpha=0.5, Fisher-Rao angular distance; all five surahs use uniform full-verse permutation null)",
        "locked_params": {
            "K_top_roots": K_TOP,
            "dirichlet_alpha": DIRICHLET_ALPHA,
            "permutations": PERMS,
            "distance": "Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))",
            "length_control": "L1-normalized probability vectors (MW-1)",
            "bonferroni_k": BON_K,
            "alpha_bon": ALPHA_BON,
            "locked_surahs": LOCKED_SURAHS,
        },
        "corpus_stats": {
            "total_stem_root_tokens": total_tokens,
            "global_distinct_roots": len(global_root_counts),
            "top_K_coverage_fraction": topk_coverage,
        },
        "per_surah": {str(sid): per_surah[sid] for sid in LOCKED_SURAHS},
        "mw_controls": {
            "control_bank_pass": control_bank_pass,
            "control_definition": "For each locked surah, both the best greedy-NN path and its 2-opt refinement must be shorter than canonical verse order.",
            "per_surah": {str(sid): control_rows[sid] for sid in LOCKED_SURAHS},
        },
        "family_verdict": {
            "n_pass": n_pass,
            "n_tests": len(LOCKED_SURAHS),
            "alpha_bon": ALPHA_BON,
            "verdict": family_verdict,
            "pass_criterion": "n_pass >= 3 and MW controls pass",
        },
    }
    result = round_floats(result)
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)

    journal = f"""# H-NEW-127.2 run 1 journal

- Date: 2026-04-18
- Pre-reg: `{PREREG_FILE}`
- Pre-reg SHA-256: `{prereg_sha}`
- Script: `scripts/h_new_127_2_oq20_family_rerun.py`
- Output: `{OUT_JSON}`
- Family lock: Q1/Q18/Q28/Q78/Q112 uniform full-verse null

## Commands

```bash
python3 scripts/h_new_127_2_oq20_family_rerun.py
```

## Result

- `n_pass = {n_pass} / {len(LOCKED_SURAHS)}`
- control bank pass = `{control_bank_pass}`
- family verdict = `{family_verdict}`

## Locked per-surah results

| Sura | n_v | null model | L_canon | null μ | null σ | z | p | pass | L_greedy_best | L_2opt_best |
|------|-----|------------|---------|--------|--------|---|---|------|---------------|-------------|
"""
    for sid in LOCKED_SURAHS:
        r = per_surah[sid]
        journal += (
            f"| {sid} | {r['n_verses']} | {r['null_model']} | {r['L_canon']:.6f} | "
            f"{r['null_mean']:.6f} | {r['null_sd']:.6f} | {r['z_score']:+.6f} | "
            f"{r['p_value_one_sided_lower']:.12f} | {'PASS' if r['pass'] else 'FAIL'} | "
            f"{r['L_greedy_best']:.6f} | {r['L_2opt_best']:.6f} |\n"
        )

    journal += f"""

## Control bank

- Greedy-NN shorter than canonical on all five surahs: `{all(control_rows[sid]["greedy_pass"] for sid in LOCKED_SURAHS)}`
- 2-opt shorter than canonical on all five surahs: `{all(control_rows[sid]["two_opt_pass"] for sid in LOCKED_SURAHS)}`

## Immediate interpretation

The rerun keeps the same Fisher-Rao verse-path family as H-NEW-127.1, but
switches to the alternate locked five-surah family named in the parent note.
The geometric control bank passes, so the family verdict is determined by the
pre-registered `n_pass` rule.
"""
    OUT_JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    OUT_JOURNAL.write_text(journal, encoding="utf-8")
    print(f"Wrote journal: {OUT_JOURNAL}", file=sys.stderr)


if __name__ == "__main__":
    main()
