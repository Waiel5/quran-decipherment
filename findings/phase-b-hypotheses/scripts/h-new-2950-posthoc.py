#!/usr/bin/env python3
"""H-NEW-2950 POST-HOC diagnostics. NOT pre-registered. Cannot create or upgrade any PASS.

Two questions the pre-registered run did not answer:

  D1. Did the matching actually match? Reports the word-count gap between each sajdah verse and
      its pool members -- the STATE-OF-THE-PROJECT §0 "does the null ever draw a comparison set
      like the observed one on the nuisance channel?" check, applied to verse length.

  D2. How much of the F3 divine-name enrichment is the grammatical complement of the prostration
      verb? Removing ROOT:sjd (prereg §2) deletes the verb "prostrate" but leaves its object
      ("...to God"). This re-runs F3 with divine-name tokens adjacent to a ROOT:sjd token also
      removed. It can only WEAKEN an observation that is already not a pass.

Writes to runs/h-new-2950-posthoc/<UTC>/ -- a directory separate from the registered run, which
is immutable and is not touched.
"""

import importlib.util
import json
import os
import platform
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

# The registered script has a hyphenated filename, so it is loaded by path rather than imported.
_spec = importlib.util.spec_from_file_location(
    "h_new_2950", Path(__file__).resolve().parent / "h-new-2950.py"
)
h2950 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(h2950)

ADJACENCY = 2  # word positions either side of a ROOT:sjd token


def divine_tokens_by_verse(qac_path):
    """Divine-name and ROOT:sjd word indices per verse."""
    divine = defaultdict(list)
    sjd = defaultdict(set)
    for line in open(qac_path, encoding="utf-8"):
        if not line.startswith("("):
            continue
        fields = line.rstrip("\n").split("\t")
        if len(fields) != 4:
            continue
        match = h2950.LOCATION_RE.fullmatch(fields[0])
        if not match:
            continue
        key = (int(match.group(1)), int(match.group(2)))
        word = int(match.group(3))
        feats = fields[3]
        if re.search(r"(?:^|\|)ROOT:sjd(?:$|\|)", feats):
            sjd[key].add(word)
        lemma = re.search(r"(?:^|\|)LEM:([^|]+)", feats)
        if lemma and lemma.group(1) in h2950.DIVINE_LEMMAS:
            divine[key].append(word)
    return divine, sjd


def main():
    repo_root = Path(__file__).resolve().parents[3]
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"
    if h2950.sha256(qac) != h2950.EXPECTED_QAC_SHA:
        raise SystemExit("QAC SHA mismatch")

    word_count, _ = h2950.parse_qac(qac)
    loci = list(h2950.EXPECTED_LOCI)
    pools = h2950.build_pools(word_count, loci, h2950.K_PRIMARY)

    # D1 -- did the matching match?
    gaps = []
    per_locus_gap = {}
    for locus in loci:
        target = word_count[locus]
        deltas = [abs(word_count[m] - target) for m in pools[locus][1:]]
        per_locus_gap[f"{locus[0]}:{locus[1]}"] = {
            "sajdah_verse_words": target,
            "pool_word_counts": sorted(word_count[m] for m in pools[locus][1:]),
            "max_abs_delta": max(deltas),
            "mean_abs_delta": round(sum(deltas) / len(deltas), 3),
        }
        gaps.extend(deltas)
    d1 = {
        "question": "does the null draw comparison verses of comparable length?",
        "n_pool_members_total": len(gaps),
        "mean_abs_word_count_delta": round(sum(gaps) / len(gaps), 3),
        "max_abs_word_count_delta": max(gaps),
        "pct_within_2_words": round(100.0 * sum(1 for g in gaps if g <= 2) / len(gaps), 1),
        "pct_within_5_words": round(100.0 * sum(1 for g in gaps if g <= 5) / len(gaps), 1),
        "per_locus": per_locus_gap,
    }

    # D2 -- strip divine names adjacent to a prostration verb
    divine, sjd = divine_tokens_by_verse(qac)
    stripped = {}
    removed_detail = {}
    for key, words in divine.items():
        near = [w for w in words if any(abs(w - s) <= ADJACENCY for s in sjd.get(key, ()))]
        stripped[key] = len(words) - len(near)
        if near and key in set(loci):
            removed_detail[f"{key[0]}:{key[1]}"] = {"total": len(words), "removed_as_adjacent": len(near)}
    counts = defaultdict(int, stripped)
    axis = h2950.analyse_axis("F3_divine_name_sjd_adjacent_also_removed", pools, loci, counts, 0, False)
    axis["verdict"] = "POST-HOC DIAGNOSTIC — NOT REGISTERED, CANNOT SUPPORT A PASS"
    axis["passes_bonferroni"] = False
    axis["passes_novelty_gate"] = False

    original = sum(len(divine.get(l, [])) for l in loci)
    remaining = sum(counts[l] for l in loci)
    d2 = {
        "question": "how much of F3 is the grammatical complement of the prostration verb?",
        "adjacency_window_words": ADJACENCY,
        "divine_name_tokens_at_loci_before": original,
        "divine_name_tokens_at_loci_after": remaining,
        "tokens_removed_as_sjd_adjacent": original - remaining,
        "removed_by_locus": removed_detail,
        "axis": axis,
    }

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-2950-posthoc" / run_id
    os.makedirs(run_dir, exist_ok=False)

    result = {
        "id": "H-NEW-2950-POSTHOC",
        "status": "POST-HOC — NOT PRE-REGISTERED. Cannot create, upgrade or rescue any verdict.",
        "registered_run_is_separate_and_untouched": "findings/phase-b-hypotheses/runs/h-new-2950/",
        "D1_length_matching": d1,
        "D2_f3_residual_circularity": d2,
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump({
            "id": "H-NEW-2950-POSTHOC",
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "command": shlex.join([sys.executable, *sys.argv]),
            "git_commit": h2950.git_output(repo_root, "rev-parse", "HEAD"),
            "hashes_sha256": {
                "qac": h2950.sha256(qac),
                "script": h2950.sha256(Path(__file__).resolve()),
                "registered_script": h2950.sha256(
                    repo_root / "findings/phase-b-hypotheses/scripts/h-new-2950.py"
                ),
            },
            "python": sys.version,
            "platform": platform.platform(),
            "run_directory": str(run_dir.relative_to(repo_root)),
        }, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "run_dir": str(run_dir.relative_to(repo_root)),
        "D1_mean_abs_delta_words": d1["mean_abs_word_count_delta"],
        "D1_max_abs_delta_words": d1["max_abs_word_count_delta"],
        "D1_pct_within_2_words": d1["pct_within_2_words"],
        "D2_tokens_before": original,
        "D2_tokens_after": remaining,
        "D2_p_exact": axis["p_exact_one_sided_upper"],
        "D2_observed": axis["observed_sum"],
        "D2_expected": axis["null_expected_sum"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
