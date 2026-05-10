#!/usr/bin/env python3
"""H-NEW-1560 — 99 asmāʾ al-ḥusnā corpus-wide distribution + top-10-by-density Fisher-Rao cluster cohesion.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1560-divine-names-distribution.md
SHA256:  6d751b87bb6cdda175217d42601c3b1cca03f5c333bcfe964766dc9cf9566c0b

Rules-tuple: (no-tashkeel, orthographic-token, per-name substring match,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""

import hashlib
import json
import os
import random
import re
import sys
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1560-divine-names-distribution.md"
EXPECTED_SHA = "6d751b87bb6cdda175217d42601c3b1cca03f5c333bcfe964766dc9cf9566c0b"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
NAMES_PATH = ROOT / "data/asma-al-husna.txt"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-1560.json"

SEED_A = 20260509
SEED_B = 20260511
SEED_PC = 20260512
N_PERM = 10_000

# MW-5 positive control: 10-surah sub-sample of H-NEW-1200 eschatology cluster.
H1200_FULL = [56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104]
PC_CLUSTER = H1200_FULL[:10]  # first 10 by sid → {56, 69, 74, 77, 81, 82, 83, 84, 86, 90}

CLUSTER_SIZE = 10
LENGTH_MATCH_TOL = 0.15  # ±15%


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH:\n  expected={EXPECTED_SHA}\n  actual  ={actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}…")


def load_names() -> list[str]:
    """Read the 99-names list from data/asma-al-husna.txt.

    One name per line; lines starting with '#' or empty are ignored.
    Internal whitespace in multi-token names (مالك الملك, ذو الجلال والإكرام)
    is normalized to single space.
    """
    names: list[str] = []
    for raw in NAMES_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        # Normalize internal whitespace
        norm = " ".join(line.split())
        names.append(norm)
    return names


def normalize_text(s: str) -> str:
    """Collapse all whitespace to single spaces for substring matching."""
    return " ".join(s.split())


def load_corpus():
    return json.loads(QURAN_PATH.read_text(encoding="utf-8"))


def load_fr_matrix() -> list[list[float]]:
    """Load 114×114 FR distance matrix from h-new-111.json (upper-triangular packed)."""
    h111 = json.loads(FR_MATRIX.read_text(encoding="utf-8"))
    D = [[0.0] * 115 for _ in range(115)]
    for a, b, dist in h111["D_matrix_upper_triangular"]:
        D[a][b] = dist
        D[b][a] = dist
    return D


def per_verse_match_count(name: str, verse_text_norm: str) -> int:
    """Count non-overlapping substring occurrences of name in normalized verse text."""
    if not name:
        return 0
    # str.count for non-overlapping count is appropriate (names don't self-overlap in Arabic forms here).
    return verse_text_norm.count(name)


def per_surah_density(surahs, names: list[str]):
    """Compute per-surah word-count, total name-attestations, density, and per-name corpus totals.

    Returns:
      per_surah: list of dicts with sid, n_verses, n_words, total_name_attestations, density
      per_name:  list of dicts with name, total_corpus_count, n_surahs_attested, n_verses_attested,
                 first_attestation (sid, ayah)
    """
    per_surah = []
    # name-level corpus accumulators
    name_total_count = {n: 0 for n in names}
    name_surah_set = {n: set() for n in names}
    name_verse_count = {n: 0 for n in names}
    name_first = {n: None for n in names}

    for s in surahs:
        sid = int(s["id"])
        verses = s["verses"]
        n_verses = len(verses)
        n_words = 0
        total_name = 0
        for v in verses:
            ayah_no = int(v.get("id") or v.get("ayah") or 0)
            text = normalize_text(v["text"])
            # word count = whitespace-split tokens, excluding pure-rasm pause-marks
            toks = [t for t in text.split() if not all(c in "۞ۖۗۚ۟ۘ۠ۤۛ" for c in t)]
            n_words += len(toks)
            for name in names:
                c = per_verse_match_count(name, text)
                if c > 0:
                    name_total_count[name] += c
                    name_surah_set[name].add(sid)
                    name_verse_count[name] += 1
                    total_name += c
                    if name_first[name] is None:
                        name_first[name] = (sid, ayah_no)
        density = (total_name / n_words) if n_words else 0.0
        per_surah.append({
            "sid": sid,
            "n_verses": n_verses,
            "n_words": n_words,
            "total_name_attestations": total_name,
            "density": density,
        })

    per_name = []
    for name in names:
        per_name.append({
            "name": name,
            "total_corpus_count": name_total_count[name],
            "n_surahs_attested": len(name_surah_set[name]),
            "n_verses_attested": name_verse_count[name],
            "first_attestation": name_first[name],
        })

    return per_surah, per_name


def mean_intra(D, group):
    pairs = [D[a][b] for i, a in enumerate(group) for b in group[i + 1:]]
    return mean(pairs)


def main() -> None:
    verify_sha()
    names = load_names()
    print(f"Loaded {len(names)} names from {NAMES_PATH.name}")
    surahs = load_corpus()
    print(f"Loaded {len(surahs)} surahs from {QURAN_PATH.name}")
    D = load_fr_matrix()
    print(f"Loaded FR matrix from {FR_MATRIX.name}")

    # Per-surah + per-name distribution
    per_surah, per_name = per_surah_density(surahs, names)

    # Names that do NOT appear (substring rule)
    names_absent = [r["name"] for r in per_name if r["total_corpus_count"] == 0]
    names_present = [r["name"] for r in per_name if r["total_corpus_count"] > 0]
    print(f"\nName-attestation (substring rule on no-tashkeel):")
    print(f"  present: {len(names_present)}/99")
    print(f"  absent:  {len(names_absent)}/99")
    if names_absent:
        print(f"  absent list: {names_absent}")

    # Corpus-rank by density (descending; tie-break sid ascending)
    ranked = sorted(per_surah, key=lambda r: (-r["density"], r["sid"]))
    rank_map = {r["sid"]: i + 1 for i, r in enumerate(ranked)}
    for r in per_surah:
        r["corpus_rank"] = rank_map[r["sid"]]
    top10 = ranked[:CLUSTER_SIZE]
    top10_sids = [r["sid"] for r in top10]
    print(f"\nTop-10 by per-word divine-name density: {top10_sids}")
    for r in top10:
        print(f"  Q {r['sid']:>3}  density={r['density']:.5f}  "
              f"({r['total_name_attestations']}/{r['n_words']})  rank={r['corpus_rank']}")

    # Bottom-10 for descriptive output
    bottom10 = ranked[-10:]

    # ----- Cluster cohesion test on top-10 cluster -----
    obs = mean_intra(D, top10_sids)
    cluster_total_words = sum(r["n_words"] for r in top10)
    print(f"\nObserved intra-cluster FR mean (top-10): {obs:.5f}")
    print(f"Cluster total words: {cluster_total_words}")

    pool_no_q1 = list(range(2, 115))

    # word-count by sid for length-matching
    words_by_sid = {r["sid"]: r["n_words"] for r in per_surah}

    # Cell A — uniform null
    rng_a = random.Random(SEED_A)
    a_nulls = [mean_intra(D, rng_a.sample(pool_no_q1, CLUSTER_SIZE)) for _ in range(N_PERM)]
    p_a = sum(1 for x in a_nulls if x <= obs) / N_PERM

    # Cell B — length-matched ±15% on total word-count
    lo = cluster_total_words * (1 - LENGTH_MATCH_TOL)
    hi = cluster_total_words * (1 + LENGTH_MATCH_TOL)
    rng_b = random.Random(SEED_B)
    b_nulls: list[float] = []
    tries = 0
    cap = N_PERM * 200
    while len(b_nulls) < N_PERM and tries < cap:
        sample = rng_b.sample(pool_no_q1, CLUSTER_SIZE)
        total = sum(words_by_sid[s] for s in sample)
        if lo <= total <= hi:
            b_nulls.append(mean_intra(D, sample))
        tries += 1
    p_b = sum(1 for x in b_nulls if x <= obs) / max(1, len(b_nulls))

    # MW-5 PC — 10-of-H-NEW-1200 sub-sample, uniform null
    pc_obs = mean_intra(D, PC_CLUSTER)
    rng_pc = random.Random(SEED_PC)
    pc_nulls = [mean_intra(D, rng_pc.sample(pool_no_q1, CLUSTER_SIZE)) for _ in range(N_PERM)]
    p_pc = sum(1 for x in pc_nulls if x <= pc_obs) / N_PERM

    cell_a_pass = p_a <= 0.025
    cell_b_pass = p_b <= 0.025
    pc_pass = p_pc <= 0.05

    if not pc_pass:
        verdict = "NULL-BROKEN (positive control failed)"
    elif cell_a_pass and cell_b_pass:
        verdict = "PASS-DIRECTED"
    elif cell_a_pass and not cell_b_pass:
        verdict = "DESCRIPTIVE-ONLY (length-confound suspected)"
    elif not cell_a_pass and cell_b_pass:
        verdict = "PARTIAL (length-matched only)"
    else:
        verdict = "NULL"

    # ----- Sanity: top-name corpus-counts -----
    names_ranked = sorted(per_name, key=lambda r: (-r["total_corpus_count"], r["name"]))
    top5_names = names_ranked[:5]

    # Per-period density (descriptive)
    # Load chronology
    import csv as _csv
    chron_path = ROOT / "data/revelation-order.csv"
    period_by_sid = {}
    with chron_path.open() as f:
        for row in _csv.DictReader(f):
            period_by_sid[int(row["mushaf_order"])] = row["period"].strip()
    for r in per_surah:
        r["period"] = period_by_sid.get(r["sid"], "UNKNOWN")

    meccan_d = [r["density"] for r in per_surah if r["period"] == "Meccan"]
    medinan_d = [r["density"] for r in per_surah if r["period"] == "Medinan"]
    period_summary = {
        "n_meccan": len(meccan_d),
        "n_medinan": len(medinan_d),
        "mean_meccan_density": (sum(meccan_d) / len(meccan_d)) if meccan_d else 0.0,
        "mean_medinan_density": (sum(medinan_d) / len(medinan_d)) if medinan_d else 0.0,
    }

    # Period composition of top-10
    top10_meccan = sum(1 for r in top10 if r.get("period") == "Meccan")
    top10_medinan = sum(1 for r in top10 if r.get("period") == "Medinan")

    out = {
        "finding_id": "H-NEW-1560",
        "title": "99 asmāʾ al-ḥusnā corpus-wide distribution + top-10-by-density Fisher-Rao cluster cohesion",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed_A": SEED_A,
        "seed_B": SEED_B,
        "seed_PC": SEED_PC,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-token, per-name substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "name_list_source": "data/asma-al-husna.txt (al-Tirmidhī #3507 / al-Walīd b. Muslim, gharīb)",
        "name_count_locked": len(names),
        "fr_instrument": "h-new-111 (114×114 FR distance on QAC stem-roots, no-tashkeel)",
        "names_present_count": len(names_present),
        "names_absent_count": len(names_absent),
        "names_absent_list": names_absent,
        "top_5_names_by_corpus_count": [
            {"name": r["name"], "corpus_count": r["total_corpus_count"],
             "n_surahs_attested": r["n_surahs_attested"], "n_verses_attested": r["n_verses_attested"]}
            for r in top5_names
        ],
        "per_name_table_full": per_name,
        "per_surah_table_full": per_surah,
        "top_10_by_density": [
            {"rank": i + 1, "sid": r["sid"], "n_words": r["n_words"],
             "total_name_attestations": r["total_name_attestations"], "density": r["density"],
             "period": r["period"]}
            for i, r in enumerate(top10)
        ],
        "bottom_10_by_density": [
            {"rank": 114 - 9 + i, "sid": r["sid"], "n_words": r["n_words"],
             "total_name_attestations": r["total_name_attestations"], "density": r["density"],
             "period": r["period"]}
            for i, r in enumerate(bottom10)
        ],
        "cluster_sids": top10_sids,
        "cluster_total_words": cluster_total_words,
        "cluster_period_composition": {"meccan": top10_meccan, "medinan": top10_medinan},
        "obs_intra_cluster_FR_mean": obs,
        "cell_A_uniform_null": {
            "n_perm": len(a_nulls),
            "null_mean": mean(a_nulls),
            "null_p5": sorted(a_nulls)[int(0.05 * len(a_nulls))],
            "null_p25": sorted(a_nulls)[int(0.25 * len(a_nulls))],
            "p_perm": p_a,
            "pass": cell_a_pass,
        },
        "cell_B_length_matched_null": {
            "lo_total_words": lo,
            "hi_total_words": hi,
            "n_perm": len(b_nulls),
            "null_mean": (mean(b_nulls) if b_nulls else None),
            "null_p5": (sorted(b_nulls)[int(0.05 * len(b_nulls))] if b_nulls else None),
            "p_perm": p_b,
            "pass": cell_b_pass,
        },
        "MW5_positive_control": {
            "source": "H-NEW-1200 first-10-by-sid sub-sample {56, 69, 74, 77, 81, 82, 83, 84, 86, 90}",
            "cluster": PC_CLUSTER,
            "pc_obs_mean": pc_obs,
            "pc_null_mean": mean(pc_nulls),
            "pc_null_p5": sorted(pc_nulls)[int(0.05 * len(pc_nulls))],
            "p_pc": p_pc,
            "pc_pass": pc_pass,
        },
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
        "period_distribution_descriptive": period_summary,
    }

    os.makedirs(OUT_PATH.parent, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nVerdict: {verdict}")
    print(f"Cell A uniform:        p={p_a:.5f}  obs={obs:.5f}  null_mean={mean(a_nulls):.5f}  null_p5={sorted(a_nulls)[int(0.05*len(a_nulls))]:.5f}")
    if b_nulls:
        print(f"Cell B length-matched: p={p_b:.5f}  null_mean={mean(b_nulls):.5f}  null_p5={sorted(b_nulls)[int(0.05*len(b_nulls))]:.5f}  (n_valid={len(b_nulls)})")
    print(f"MW-5 PC (10-of-H1200): pc_obs={pc_obs:.5f}  p_pc={p_pc:.5f}  pass={pc_pass}")
    print(f"\nTop-5 names by corpus substring count:")
    for r in top5_names:
        print(f"  {r['name']}: {r['total_corpus_count']} occurrences, {r['n_surahs_attested']} surahs, {r['n_verses_attested']} verses")
    print(f"\nTop-10 cluster period composition: {top10_meccan} Meccan / {top10_medinan} Medinan")
    print(f"\nWrote: {OUT_PATH}")


if __name__ == "__main__":
    main()
