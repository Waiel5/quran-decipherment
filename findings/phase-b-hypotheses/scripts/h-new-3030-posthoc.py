#!/usr/bin/env python3
"""H-NEW-3030 POST-HOC — NOT PRE-REGISTERED. Cannot create, upgrade or rescue any verdict.

Three diagnostics, run after the registered run at runs/h-new-3030/20260809T065545Z/, which was
not touched:

  D1. The C2 tie-break defect, measured. Prereg §10 decision 7 broke ties in |dlength| by
      (surah, verse) ascending to avoid introducing a seed. Corpus-wide there are hundreds of
      EXACT length matches per locus, so the tie-break -- not the length criterion -- selects the
      pool, and "earliest in the mushaf" means al-Baqara. This quantifies the resulting skew.

  D2. A REPAIRED corpus-wide null. Each null draw takes a verse uniformly at random from ALL
      non-sajdah verses within +/-1 word of the target, so no ordering bias can enter. This is
      what C2 should have been.

  D3. The B3 lit-locus decomposition -- which four loci the power calculation requires to light up.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-3030-posthoc.py
"""

import importlib.util
import json
import os
import random
import shlex
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SEED = 20260509
N_DRAWS = 200_000
WINDOW = 1  # +/- words, for the repaired length-matched pool

spec = importlib.util.spec_from_file_location("h3030", Path(__file__).parent / "h-new-3030.py")
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)


def git_output(*args):
    try:
        return subprocess.run(["git", *args], cwd=REPO, capture_output=True, text=True,
                              check=True).stdout.strip()
    except Exception:
        return None


def main():
    word_count, counts = H.parse_qac(REPO / "data/morphology/quranic-corpus-morphology-0.4.txt")
    loci = list(H.EXPECTED_LOCI)
    locus_set = set(loci)
    tables = counts["sjd_excluded"]

    # ---------------- D1: the tie-break defect, measured ----------------
    pools_c2 = H.build_pools_corpus_wide(word_count, loci, H.K_PRIMARY)
    origin = Counter()
    per_locus = []
    for locus in loci:
        members = pools_c2[locus][1:]
        for member in members:
            origin[member[0]] += 1
        target = word_count[locus]
        exact = sum(1 for v in word_count if v not in locus_set and word_count[v] == target)
        per_locus.append({
            "locus": f"{locus[0]}:{locus[1]}",
            "words": target,
            "n_exact_length_candidates_corpus_wide": exact,
            "pool_source_surahs": sorted({s for s, _ in members}),
            "pool_all_from_one_surah": len({s for s, _ in members}) == 1,
            "max_abs_delta_in_pool": max(abs(word_count[m] - target) for m in members),
        })
    total_members = sum(origin.values())
    d1 = {
        "what_this_shows": (
            "The length criterion is almost never binding corpus-wide: every locus has between 18 "
            "and 417 EXACT length matches. The deterministic (surah, verse) tie-break of prereg "
            "§10 decision 7 therefore selects the pool, and it selects from the start of the "
            "mushaf. C2's null is not 'length-matched corpus verses'; it is 'length-matched verses "
            "from al-Baqara and its neighbours'."
        ),
        "pool_member_origin_surah_counts": dict(origin.most_common()),
        "n_pool_members": total_members,
        "share_from_surah_2": round(origin[2] / total_members, 4),
        "n_distinct_source_surahs": len(origin),
        "n_loci_whose_entire_pool_is_one_surah": sum(1 for r in per_locus if r["pool_all_from_one_surah"]),
        "per_locus": per_locus,
    }

    # ---------------- D2: the repaired corpus-wide null ----------------
    by_length = defaultdict(list)
    for verse, n_words in word_count.items():
        if verse not in locus_set:
            by_length[n_words].append(verse)
    candidates = {}
    for locus in loci:
        target = word_count[locus]
        pool = [v for d in range(-WINDOW, WINDOW + 1) for v in by_length.get(target + d, [])]
        candidates[locus] = sorted(pool)

    d2 = {
        "design": (
            f"Each null draw takes one verse uniformly at random from ALL non-sajdah verses within "
            f"+/-{WINDOW} word of the locus. No ordering enters. Monte Carlo, {N_DRAWS:,} draws, "
            f"seed {SEED}. POST-HOC: not gated, cannot support a PASS."
        ),
        "candidate_pool_sizes": {f"{s}:{v}": len(candidates[(s, v)]) for s, v in loci},
        "axes": {},
    }
    for feature in H.FEATURES:
        table = tables[feature]
        observed = sum(table[locus] for locus in loci)
        expected = sum(sum(table[c] for c in candidates[l]) / len(candidates[l]) for l in loci)
        rng = random.Random(SEED)
        hits = 0
        for _ in range(N_DRAWS):
            if sum(table[rng.choice(candidates[l])] for l in loci) >= observed:
                hits += 1
        d2["axes"][feature] = {
            "observed_sum": observed,
            "null_expected_sum": round(expected, 4),
            "p_monte_carlo_one_sided_upper": hits / N_DRAWS,
            "direction_as_locked": observed > expected,
            "ratio_observed_over_expected": round(observed / expected, 4),
        }

    # ---------------- D3: which loci the power calculation needs ----------------
    pools_c1 = H.build_pools_within_surah(word_count, loci, H.K_PRIMARY)
    table = tables["F1_imperative"]
    rows = []
    for locus in loci:
        values = [table[m] for m in pools_c1[locus]]
        rows.append({
            "locus": f"{locus[0]}:{locus[1]}",
            "observed": table[locus],
            "pool_max": max(values),
            "pool_mode": max(sorted(Counter(values)), key=lambda v: Counter(values)[v]),
            "n_nonzero_in_pool": sum(1 for v in values if v > 0),
            "pool_size": len(values),
        })
    ranked = sorted(rows, key=lambda r: -(r["pool_max"] - r["pool_mode"]))
    running, needed = 0, []
    for row in ranked:
        if running >= 12:
            break
        running += row["pool_max"] - row["pool_mode"]
        needed.append(row["locus"])
    d3 = {
        "S_star": 12,
        "observed_S": sum(table[l] for l in loci),
        "all_pool_modes_are_zero": all(r["pool_mode"] == 0 for r in rows),
        "loci_that_must_reach_their_pool_maximum": needed,
        "sum_of_their_pool_maxima": running,
        "per_locus": rows,
        "n_loci_with_zero_imperatives_observed": sum(1 for r in rows if r["observed"] == 0),
    }

    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-3030-posthoc" / \
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    os.makedirs(run_dir, exist_ok=False)
    result = {
        "id": "H-NEW-3030-POSTHOC",
        "status": "POST-HOC — NOT PRE-REGISTERED — cannot create, upgrade or rescue any verdict",
        "registered_run_not_touched": "findings/phase-b-hypotheses/runs/h-new-3030/20260809T065545Z",
        "D1_c2_tiebreak_defect": d1,
        "D2_repaired_corpus_wide_null": d2,
        "D3_lit_locus_decomposition": d3,
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump({
            "id": "H-NEW-3030-POSTHOC",
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "command": shlex.join([sys.executable, *sys.argv]),
            "git_commit": git_output("rev-parse", "HEAD"),
            "git_status_porcelain": git_output("status", "--porcelain"),
            "seed": SEED,
            "n_draws": N_DRAWS,
            "window_words": WINDOW,
            "run_directory": str(run_dir.relative_to(REPO)),
        }, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "run_dir": str(run_dir.relative_to(REPO)),
        "D1_share_from_surah_2": d1["share_from_surah_2"],
        "D1_loci_with_single_surah_pool": d1["n_loci_whose_entire_pool_is_one_surah"],
        "D2": {f: d2["axes"][f] for f in H.FEATURES},
        "D3_loci_needed": d3["loci_that_must_reach_their_pool_maximum"],
        "D3_zero_imperative_loci": d3["n_loci_with_zero_imperatives_observed"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
