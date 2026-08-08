#!/usr/bin/env python3
"""H-NEW-2950: the sajdah glyph census, and an exact test of whether the loci are textually marked.

Two deliverables, deliberately separated (prereg §0):
  1. The U+06E9 census across every text variant on disk. Documentary; no null model.
  2. An exact permutation test over surah- and length-matched candidate pools. Prereg §§3-7.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-2950.py
      python3 findings/phase-b-hypotheses/scripts/h-new-2950.py --self-check
"""

import argparse
import hashlib
import json
import os
import platform
import random
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path

# Prereg §8 — embedded literals, verified at runtime; mismatch aborts before any run directory.
EXPECTED_PREREG_SHA = "1495116ef07920d7753ed217a491f3b574e79ec3b6d94730cf75d39a7bc52847"
EXPECTED_QAC_SHA = "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46"
EXPECTED_QURAN_SHA = "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a"

SAJDAH_GLYPH = "۩"  # ARABIC PLACE OF SAJDAH

SEED_PRIMARY = 20260509
SEED_REPLICATION = 20260519
N_MONTE_CARLO = 200_000

K_PRIMARY = 15  # prereg §5 — pool size m_i = K + 1 = 16
K_REPLICATION = 10  # prereg §7.4 — tighter match, m_i = 11

TESTS_IN_FAMILY = 3
ALPHA_BONFERRONI = 0.05 / TESTS_IN_FAMILY
NOVELTY_GATE = 0.005
RAW_NOVELTY_GATE = NOVELTY_GATE / TESTS_IN_FAMILY

LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
SECOND_PERSON_RE = re.compile(r"(?:^|\|)(?:PRON:)?2(?:MS|MP|FS|FP|D)(?:$|\|)")
DIVINE_LEMMAS = {"{ll~ah", "r~aHoma`n", "rab~"}  # prereg §4.2 F3

FEATURES = ("F1_imperative", "F2_second_person", "F3_divine_name")

# Prereg §4.2 — the census-derived locus set is asserted here so a corpus change breaks the run
# loudly rather than silently re-defining the test set.
EXPECTED_LOCI = (
    (7, 206), (13, 15), (16, 50), (17, 109), (19, 58), (22, 18), (22, 77), (25, 60),
    (27, 26), (32, 15), (38, 24), (41, 38), (53, 62), (84, 21), (96, 19),
)


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git_output(repo_root, *args):
    try:
        return subprocess.run(
            ["git", *args], cwd=repo_root, capture_output=True, text=True, check=True
        ).stdout.strip()
    except Exception:
        return None


# --------------------------------------------------------------------------------------
# Deliverable 1 — the census (prereg §0: documentary, no null model)
# --------------------------------------------------------------------------------------

def census_json(path):
    """Loci and glyph count for a surah-list JSON variant."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    loci, glyphs = [], 0
    for surah in data:
        for verse in surah["verses"]:
            count = verse["text"].count(SAJDAH_GLYPH)
            if count:
                loci.append([surah["id"], verse["id"], count])
                glyphs += count
    return {"loci": loci, "n_loci": len(loci), "n_glyphs": glyphs}


def census_tanzil(path):
    """Loci for a Tanzil `surah|verse|text` line file."""
    loci, glyphs = [], 0
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        parts = line.strip().split("|", 2)
        if len(parts) != 3 or not parts[0].isdigit():
            continue
        count = parts[2].count(SAJDAH_GLYPH)
        if count:
            loci.append([int(parts[0]), int(parts[1]), count])
            glyphs += count
    return {"loci": loci, "n_loci": len(loci), "n_glyphs": glyphs}


def census_flat(path, reference_json):
    """Glyph count for a flat concatenation, plus the truncation diagnostic.

    Two of these files are byte-truncated. The diagnostic locates the cut and reports which
    loci fall beyond it, so a low glyph count is explained rather than mistaken for a textual
    disagreement between variants.
    """
    raw = Path(path).read_bytes()
    text = Path(path).read_text(encoding="utf-8")
    header = ""
    if text.startswith("GROUP_CONCAT"):
        header, text = text.split("\n", 1)[0], text.split("\n", 1)[1]
    data = json.loads(Path(reference_json).read_text(encoding="utf-8"))
    reference = " ".join(v["text"] for s in data for v in s["verses"])
    cumulative, last_complete = 0, None
    for surah in data:
        for verse in surah["verses"]:
            cumulative += len(verse["text"]) + 1
            if cumulative <= len(text):
                last_complete = (surah["id"], verse["id"])
    beyond = [list(l) for l in EXPECTED_LOCI if last_complete and l > last_complete]
    body_bytes = len(raw) - len((header + "\n").encode()) if header else len(raw)
    return {
        "n_glyphs": text.count(SAJDAH_GLYPH),
        "file_bytes": len(raw),
        "header": header or None,
        "body_bytes": body_bytes,
        "body_is_exactly_1_mib": body_bytes == 1024 * 1024,
        "chars_present": len(text),
        "chars_in_reference_json": len(reference),
        "coverage_pct": round(100.0 * len(text) / len(reference), 2),
        "last_complete_verse": list(last_complete) if last_complete else None,
        "loci_beyond_cut": beyond,
        "n_loci_beyond_cut": len(beyond),
    }


def run_census(repo_root):
    json_variants = {
        "quran-text/quran-full-tashkeel.json": None,
        "quran-text/quran-min-tashkeel.json": None,
        "quran-text/quran-no-tashkeel.json": None,
        "data/alt-text/quran-uthmani-consonantal.json": None,
    }
    for rel in json_variants:
        json_variants[rel] = census_json(repo_root / rel)

    tanzil = {}
    for rel in sorted(str(p.relative_to(repo_root)) for p in (repo_root / "data/alt-text").glob("*-2.txt")):
        tanzil[rel] = census_tanzil(repo_root / rel)

    plain = {}
    for rel in sorted(
        str(p.relative_to(repo_root))
        for p in (repo_root / "data/alt-text").glob("*.txt")
        if not p.name.endswith("-2.txt")
    ):
        plain[rel] = {"n_glyphs": (repo_root / rel).read_text(encoding="utf-8").count(SAJDAH_GLYPH)}

    flat = {}
    for rel, ref in [
        ("quran-text/quran-flat-full-tashkeel.txt", "quran-text/quran-full-tashkeel.json"),
        ("quran-text/quran-flat-min-tashkeel.txt", "quran-text/quran-min-tashkeel.json"),
        ("quran-text/quran-flat-no-tashkeel.txt", "quran-text/quran-no-tashkeel.json"),
    ]:
        flat[rel] = census_flat(repo_root / rel, repo_root / ref)

    keyed = {rel: [tuple(l[:2]) for l in c["loci"]] for rel, c in json_variants.items() if c["n_loci"]}
    keyed.update({rel: [tuple(l[:2]) for l in c["loci"]] for rel, c in tanzil.items()})
    all_agree = all(tuple(v) == EXPECTED_LOCI for v in keyed.values())

    return {
        "glyph": "U+06E9 ARABIC PLACE OF SAJDAH",
        "json_variants": json_variants,
        "tanzil_keyed_variants": tanzil,
        "tanzil_plain_variants": plain,
        "flat_concatenations": flat,
        "locus_sets_identical_across_all_keyed_variants": all_agree,
        "n_variants_carrying_a_locus_set": len(keyed),
        "canonical_locus_set": [list(l) for l in EXPECTED_LOCI],
        "surah_support": sorted({s for s, _ in EXPECTED_LOCI}),
        "n_surahs": len({s for s, _ in EXPECTED_LOCI}),
    }


# --------------------------------------------------------------------------------------
# Deliverable 2 — the test
# --------------------------------------------------------------------------------------

def parse_qac(path):
    """Per-verse word counts and feature counts, with and without the ROOT:sjd exclusion."""
    words = defaultdict(set)
    counts = {
        excl: {feature: defaultdict(int) for feature in FEATURES}
        for excl in ("sjd_excluded", "sjd_included")
    }
    for line in open(path, encoding="utf-8"):
        if not line.startswith("("):
            continue
        fields = line.rstrip("\n").split("\t")
        if len(fields) != 4:
            continue
        location, _, _, feats = fields
        match = LOCATION_RE.fullmatch(location)
        if not match:
            continue
        surah, verse, word = int(match.group(1)), int(match.group(2)), int(match.group(3))
        key = (surah, verse)
        words[key].add(word)

        is_sjd = re.search(r"(?:^|\|)ROOT:sjd(?:$|\|)", feats) is not None
        lemma = re.search(r"(?:^|\|)LEM:([^|]+)", feats)
        hits = {
            "F1_imperative": "POS:V" in feats and re.search(r"(?:^|\|)IMPV(?:$|\|)", feats) is not None,
            "F2_second_person": SECOND_PERSON_RE.search(feats) is not None,
            "F3_divine_name": lemma is not None and lemma.group(1) in DIVINE_LEMMAS,
        }
        for feature, hit in hits.items():
            if not hit:
                continue
            counts["sjd_included"][feature][key] += 1
            if not is_sjd:
                counts["sjd_excluded"][feature][key] += 1
    return {k: len(v) for k, v in words.items()}, counts


def build_pools(word_count, loci, k):
    """Prereg §5 — pool_i = {verse i} + the K nearest-length non-sajdah verses of the same surah."""
    locus_set = set(loci)
    by_surah = defaultdict(list)
    for (surah, verse) in word_count:
        by_surah[surah].append(verse)
    pools = {}
    for locus in loci:
        surah, verse = locus
        target = word_count[locus]
        eligible = [
            v for v in sorted(by_surah[surah])
            if (surah, v) not in locus_set
        ]
        if len(eligible) < k:
            raise SystemExit(
                f"pool for {surah}:{verse} cannot be filled: {len(eligible)} eligible verses < K={k}"
            )
        eligible.sort(key=lambda v: (abs(word_count[(surah, v)] - target), v))
        pools[locus] = [locus] + [(surah, v) for v in eligible[:k]]
    return pools


def exact_convolution(pool_values):
    """Exact null pmf of S = sum of one uniformly drawn value per pool, as integer tuple counts.

    Returns (counts_by_sum, total_tuples). Both are exact integers: the DP enumerates the whole
    product space without sampling.
    """
    dp = {0: 1}
    for values in pool_values:
        nxt = defaultdict(int)
        for total, ways in dp.items():
            for value in values:
                nxt[total + value] += ways
        dp = dict(nxt)
    total = 1
    for values in pool_values:
        total *= len(values)
    assert sum(dp.values()) == total
    return dp, total


def monte_carlo_p(pool_values, observed, seed, draws):
    rng = random.Random(seed)
    hits = 0
    for _ in range(draws):
        if sum(rng.choice(values) for values in pool_values) >= observed:
            hits += 1
    return hits / draws, hits


def analyse_axis(feature, pools, loci, feature_counts, seed, monte_carlo):
    pool_values = [[feature_counts[v] for v in pools[locus]] for locus in loci]
    observed = sum(feature_counts[locus] for locus in loci)

    dp, total = exact_convolution(pool_values)
    tail = sum(ways for value, ways in dp.items() if value >= observed)
    p_exact = Fraction(tail, total)

    expected = sum(Fraction(sum(values), len(values)) for values in pool_values)
    p_min = Fraction(1, 1)
    for values in pool_values:
        p_min *= Fraction(sum(1 for v in values if v == max(values)), len(values))

    result = {
        "feature": feature,
        "observed_sum": observed,
        "null_expected_sum": float(expected),
        "null_min_sum": min(dp),
        "null_max_sum": max(dp),
        "p_exact_one_sided_upper": float(p_exact),
        "p_exact_fraction": f"{p_exact.numerator}/{p_exact.denominator}",
        "product_space_size": total,
        "direction_as_locked": observed > float(expected),
        "p_min_attainable_on_these_pools": float(p_min),
        "p_min_tie_free_floor": float(Fraction(1, total)),
        "per_locus": [
            {
                "locus": f"{s}:{v}",
                "observed": feature_counts[(s, v)],
                "pool_max": max(values),
                "pool_mean": round(sum(values) / len(values), 4),
                "n_pool_members_ge_observed": sum(1 for x in values if x >= feature_counts[(s, v)]),
                "pool_size": len(values),
            }
            for (s, v), values in zip(loci, pool_values)
        ],
    }
    result["passes_bonferroni"] = bool(
        result["p_exact_one_sided_upper"] < ALPHA_BONFERRONI and result["direction_as_locked"]
    )
    result["passes_novelty_gate"] = bool(
        min(1.0, TESTS_IN_FAMILY * result["p_exact_one_sided_upper"]) < NOVELTY_GATE
        and result["direction_as_locked"]
    )
    result["verdict"] = (
        "PASS-NOVELTY" if result["passes_novelty_gate"]
        else "PASS-DIRECTED" if result["passes_bonferroni"]
        else "REVERSED" if not result["direction_as_locked"]
        else "NULL"
    )

    if monte_carlo:
        p_mc, hits = monte_carlo_p(pool_values, observed, seed, N_MONTE_CARLO)
        p = result["p_exact_one_sided_upper"]
        tolerance = 5.0 * (p * (1.0 - p) / N_MONTE_CARLO) ** 0.5 + 3.0 / N_MONTE_CARLO
        if abs(p_mc - p) > tolerance:
            raise SystemExit(
                f"Monte Carlo cross-check failed for {feature}: "
                f"exact={p:.8f} mc={p_mc:.8f} tol={tolerance:.8f}"
            )
        result["monte_carlo_cross_check"] = {
            "seed": seed, "draws": N_MONTE_CARLO, "hits": hits, "p": p_mc,
            "tolerance": tolerance, "agrees": True,
        }
    return result


def run_arm(name, k, word_count, counts, loci, seed, exclusion, monte_carlo):
    pools = build_pools(word_count, loci, k)
    axes = {
        feature: analyse_axis(feature, pools, loci, counts[exclusion][feature], seed, monte_carlo)
        for feature in FEATURES
    }
    primary = axes["F1_imperative"]
    if primary["passes_novelty_gate"]:
        headline = "PASS-NOVELTY on primary F1"
    elif primary["passes_bonferroni"]:
        headline = "PASS-DIRECTED on primary F1"
    elif not primary["direction_as_locked"]:
        headline = "NULL — primary F1 REVERSED against the locked direction"
    else:
        headline = "NULL — primary F1 held direction but did not clear its gate"
    return {
        "arm": name,
        "K": k,
        "pool_size": k + 1,
        "sjd_exclusion": exclusion,
        "seed": seed,
        "axes": axes,
        "headline": headline,
        "pools": {
            f"{s}:{v}": {
                "word_count": word_count[(s, v)],
                "members": [f"{a}:{b}" for a, b in pools[(s, v)]],
                "member_word_counts": [word_count[m] for m in pools[(s, v)]],
            }
            for (s, v) in loci
        },
    }


def self_check():
    """Unit tests for the exact convolution and the pool builder."""
    dp, total = exact_convolution([[0, 1], [0, 1]])
    assert total == 4 and dp == {0: 1, 1: 2, 2: 1}, dp
    dp, total = exact_convolution([[0, 0, 3], [1, 2]])
    assert total == 6 and dp == {1: 2, 2: 2, 4: 1, 5: 1}, dp
    # a pool of identical values must give a point mass and p = 1
    dp, total = exact_convolution([[2, 2, 2]])
    assert dp == {2: 3} and total == 3
    wc = {(1, i): i for i in range(1, 11)}
    pools = build_pools(wc, [(1, 5)], 3)
    assert pools[(1, 5)][0] == (1, 5)
    assert set(pools[(1, 5)][1:]) == {(1, 4), (1, 6), (1, 3)}, pools
    print("self-check OK")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", help="Immutable run directory name; defaults to UTC timestamp")
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    if args.self_check:
        self_check()
        return

    repo_root = Path(__file__).resolve().parents[3]
    prereg = repo_root / "findings/phase-b-hypotheses/prereg-h-new-2950-sajdah-loci.md"
    qac = repo_root / "data/morphology/quranic-corpus-morphology-0.4.txt"
    quran = repo_root / "quran-text/quran-no-tashkeel.json"
    script = Path(__file__).resolve()

    hashes = {
        "prereg": sha256(prereg),
        "qac": sha256(qac),
        "quran_no_tashkeel": sha256(quran),
        "script": sha256(script),
    }
    expected = {
        "prereg": EXPECTED_PREREG_SHA,
        "qac": EXPECTED_QAC_SHA,
        "quran_no_tashkeel": EXPECTED_QURAN_SHA,
    }
    for key, want in expected.items():
        if hashes[key] != want:
            raise SystemExit(f"{key} SHA mismatch: expected {want}, found {hashes[key]}")

    # Prereg §8 — every gate below aborts BEFORE a run directory exists.
    census = run_census(repo_root)
    observed_loci = tuple(tuple(l[:2]) for l in census["json_variants"]["quran-text/quran-no-tashkeel.json"]["loci"])
    if observed_loci != EXPECTED_LOCI:
        raise SystemExit(f"census locus set changed: {observed_loci} != {EXPECTED_LOCI}")
    if not census["locus_sets_identical_across_all_keyed_variants"]:
        raise SystemExit("keyed text variants disagree on the locus set; inspect before testing")

    word_count, counts = parse_qac(qac)
    loci = list(EXPECTED_LOCI)
    missing = [l for l in loci if l not in word_count]
    if missing:
        raise SystemExit(f"QAC is missing sajdah verses: {missing}")

    run_id = args.run_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = repo_root / "findings/phase-b-hypotheses/runs/h-new-2950" / run_id
    os.makedirs(run_dir, exist_ok=False)

    primary = run_arm(
        "primary", K_PRIMARY, word_count, counts, loci, SEED_PRIMARY, "sjd_excluded", True
    )
    replication = run_arm(
        "replication", K_REPLICATION, word_count, counts, loci, SEED_REPLICATION, "sjd_excluded", True
    )
    diagnostic = run_arm(
        "diagnostic_NOT_GATED", K_PRIMARY, word_count, counts, loci, SEED_PRIMARY, "sjd_included", False
    )
    for axis in diagnostic["axes"].values():
        axis["verdict"] = "DIAGNOSTIC — NOT GATED, CANNOT SUPPORT A PASS (prereg §7.3)"
        axis["passes_bonferroni"] = False
        axis["passes_novelty_gate"] = False
    diagnostic["headline"] = "DIAGNOSTIC ONLY — quantifies the definitional component (prereg §7.3)"

    result = {
        "id": "H-NEW-2950",
        "n_loci": len(loci),
        "underpowered": (
            "n = 15. This test is underpowered. A NULL is not evidence that the loci are "
            "unmarked; it is evidence that any marking is not large enough for 15 verses to "
            "reveal it under a surah- and length-matched null (prereg §6.1)."
        ),
        "sign_test_floor_2_pow_minus_15": 2.0 ** -15,
        "tests_in_family": TESTS_IN_FAMILY,
        "alpha_bonferroni": ALPHA_BONFERRONI,
        "novelty_gate_corrected": NOVELTY_GATE,
        "novelty_gate_raw": RAW_NOVELTY_GATE,
        "census": census,
        "primary_arm": primary,
        "replication_arm": replication,
        "diagnostic_arm": diagnostic,
        "sajdah_verse_word_counts": {f"{s}:{v}": word_count[(s, v)] for s, v in loci},
        "verdict": primary["headline"],
    }

    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    manifest = {
        "id": "H-NEW-2950",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "command": shlex.join([sys.executable, *sys.argv]),
        "git_commit": git_output(repo_root, "rev-parse", "HEAD"),
        "git_status_porcelain": git_output(repo_root, "status", "--porcelain"),
        "hashes_sha256": hashes,
        "expected_hashes_sha256": expected,
        "input_paths_repo_relative": {
            "prereg": "findings/phase-b-hypotheses/prereg-h-new-2950-sajdah-loci.md",
            "qac": "data/morphology/quranic-corpus-morphology-0.4.txt",
            "quran_no_tashkeel": "quran-text/quran-no-tashkeel.json",
            "script": "findings/phase-b-hypotheses/scripts/h-new-2950.py",
        },
        "python": sys.version,
        "platform": platform.platform(),
        "seeds": {"primary": SEED_PRIMARY, "replication": SEED_REPLICATION},
        "n_monte_carlo_cross_check": N_MONTE_CARLO,
        "inference_is_exact": "p-values are exact convolutions over the full product space; Monte Carlo is a correctness check only",
        "run_directory": str(run_dir.relative_to(repo_root)),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")

    print(json.dumps({
        "run_dir": str(run_dir.relative_to(repo_root)),
        "census_n_glyphs_no_tashkeel": census["json_variants"]["quran-text/quran-no-tashkeel.json"]["n_glyphs"],
        "verdict": result["verdict"],
        "primary_p": {f: primary["axes"][f]["p_exact_one_sided_upper"] for f in FEATURES},
        "replication_p": {f: replication["axes"][f]["p_exact_one_sided_upper"] for f in FEATURES},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
