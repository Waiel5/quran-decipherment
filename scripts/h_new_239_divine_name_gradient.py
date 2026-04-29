#!/usr/bin/env python3
"""H-NEW-239 — Divine-name density gradient across the 114-surah mushaf.

Pre-reg: findings/phase-b-hypotheses/h-new-239-divine-name-gradient-prereg.md
Seed: 20260419. Bonferroni k=4, alpha_per_cell=0.0125.

Cell A: Spearman(mushaf_position, per-surah name-density), 10k-perm two-sided p.
Cell B: Kruskal-Wallis across {ṭiwāl, ḥawāmīm, mufaṣṣal, other} on density.
Cell C: Mann-Whitney U juz'30 (Q 78-114) vs juz'1-29 density.
Cell D: Mann-Whitney U Meccan vs Medinan density.

MW-5 neg control: permute per-verse divine-name TOKEN COUNTS across verses,
re-aggregate to per-surah densities, rerun the 4 cells. Expected: null.

Outputs:
- findings/phase-b-hypotheses/csv/h-new-239.json
- findings/phase-b-hypotheses/csv/h-new-239-per-surah.tsv
"""
from __future__ import annotations

import csv
import json
import random
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy import stats as sstats

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
BONFERRONI_K = 4
ALPHA_PER_CELL = 0.05 / BONFERRONI_K

NAMES_CSV = ROOT / "findings/phase-b-hypotheses/divine-names-by-verse.csv"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
CHRON_CSV = ROOT / "data/revelation-order.csv"
OUT_DIR = ROOT / "findings/phase-b-hypotheses/csv"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_JSON = OUT_DIR / "h-new-239.json"
OUT_TSV = OUT_DIR / "h-new-239-per-surah.tsv"

# Block partition (locked pre-reg)
TIWAL = set(range(2, 10))               # Q 2..9
HAWAMIM = set(range(40, 47))            # Q 40..46
MUFASSAL = set(range(50, 115))          # Q 50..114
# "other" = Q 1 + Q 10..39 + Q 47..49
JUZ30 = set(range(78, 115))             # juz' 30 approx: Q 78..114


def block_of(surah: int) -> str:
    if surah in TIWAL:
        return "tiwal"
    if surah in HAWAMIM:
        return "hawamim"
    if surah in MUFASSAL:
        return "mufassal"
    return "other"


def load_surah_words() -> dict[int, int]:
    """Whitespace-split word count per surah (no-tashkeel), locking the denominator."""
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for s in data:
        sid = s["id"]
        total = 0
        for v in s["verses"]:
            total += len(v["text"].split())
        out[sid] = total
    return out


def load_meccan_flag() -> dict[int, str]:
    """Meccan/Medinan per surah — from quran-no-tashkeel.json 'type' field
    (tanzil canonical classification)."""
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    return {s["id"]: s["type"].lower() for s in data}


def load_per_verse_names() -> dict[tuple[int, int], int]:
    """Return (surah, verse) -> number of canonical divine names in that verse."""
    counts: dict[tuple[int, int], int] = {}
    with open(NAMES_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah"]); vid = int(row["verse"])
            n = int(row["num_names"])
            counts[(sid, vid)] = n
    return counts


def load_per_verse_name_set() -> dict[tuple[int, int], set[str]]:
    """Return (surah, verse) -> set of canonical name translit for diversity."""
    sets: dict[tuple[int, int], set[str]] = {}
    with open(NAMES_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sid = int(row["surah"]); vid = int(row["verse"])
            names = row["names_translit"].split("|") if row["names_translit"] else []
            sets[(sid, vid)] = set(n for n in names if n)
    return sets


def aggregate_per_surah(per_verse_counts, per_verse_sets, surah_words):
    rows = []
    by_surah_tokens: dict[int, int] = defaultdict(int)
    by_surah_verses_with_name: dict[int, int] = defaultdict(int)
    by_surah_name_set: dict[int, set[str]] = defaultdict(set)
    for (sid, vid), n in per_verse_counts.items():
        by_surah_tokens[sid] += n
        if n > 0:
            by_surah_verses_with_name[sid] += 1
    for (sid, vid), ns in per_verse_sets.items():
        by_surah_name_set[sid].update(ns)

    for sid in range(1, 115):
        words = surah_words.get(sid, 0)
        tokens = by_surah_tokens.get(sid, 0)
        diversity = len(by_surah_name_set.get(sid, set()))
        density = tokens / words if words > 0 else 0.0
        rows.append({
            "surah": sid,
            "words": words,
            "name_tokens": tokens,
            "name_diversity": diversity,
            "density": density,
            "block": block_of(sid),
            "juz30": sid in JUZ30,
        })
    return rows


# -------- Cell tests --------

def cell_A_spearman(rows, seed=SEED, n_perm=10000):
    pos = np.array([r["surah"] for r in rows], dtype=float)
    dens = np.array([r["density"] for r in rows], dtype=float)
    rho, _ = sstats.spearmanr(pos, dens)
    rng = np.random.default_rng(seed)
    null_rhos = np.empty(n_perm, dtype=float)
    for i in range(n_perm):
        perm = rng.permutation(dens)
        null_rhos[i], _ = sstats.spearmanr(pos, perm)
    p_two = (np.abs(null_rhos) >= abs(rho)).mean()
    return {"rho": float(rho), "p_two": float(p_two), "n_perm": n_perm}


def cell_B_kruskal(rows):
    groups: dict[str, list[float]] = defaultdict(list)
    for r in rows:
        groups[r["block"]].append(r["density"])
    H, p = sstats.kruskal(*[groups[b] for b in ["tiwal", "hawamim", "mufassal", "other"]])
    means = {b: float(np.mean(groups[b])) for b in groups}
    medians = {b: float(np.median(groups[b])) for b in groups}
    ns = {b: len(groups[b]) for b in groups}
    # Dunn post-hoc: pairwise MW-U with Bonferroni inside the cell
    pairs = [("tiwal", "hawamim"), ("tiwal", "mufassal"), ("tiwal", "other"),
             ("hawamim", "mufassal"), ("hawamim", "other"), ("mufassal", "other")]
    pair_stats = {}
    for a, b in pairs:
        u, p_ab = sstats.mannwhitneyu(groups[a], groups[b], alternative="two-sided")
        pair_stats[f"{a}_vs_{b}"] = {"U": float(u), "p": float(p_ab),
                                     "p_bonf_6": float(min(1.0, p_ab * 6))}
    return {"H": float(H), "p": float(p), "means": means, "medians": medians,
            "n_per_block": ns, "pairwise_mwu": pair_stats}


def cell_C_juz30(rows):
    a = [r["density"] for r in rows if r["juz30"]]
    b = [r["density"] for r in rows if not r["juz30"]]
    u, p_two = sstats.mannwhitneyu(a, b, alternative="two-sided")
    u_gt, p_gt = sstats.mannwhitneyu(a, b, alternative="greater")
    return {"U_two": float(u), "p_two": float(p_two),
            "U_greater": float(u_gt), "p_greater": float(p_gt),
            "mean_juz30": float(np.mean(a)), "mean_rest": float(np.mean(b)),
            "median_juz30": float(np.median(a)), "median_rest": float(np.median(b)),
            "n_juz30": len(a), "n_rest": len(b)}


def cell_D_meccan(rows, meccan_flag):
    mec = [r["density"] for r in rows if meccan_flag.get(r["surah"]) == "meccan"]
    med = [r["density"] for r in rows if meccan_flag.get(r["surah"]) == "medinan"]
    u, p_two = sstats.mannwhitneyu(mec, med, alternative="two-sided")
    u_gt, p_gt = sstats.mannwhitneyu(mec, med, alternative="greater")
    return {"U_two": float(u), "p_two": float(p_two),
            "U_greater": float(u_gt), "p_greater": float(p_gt),
            "mean_meccan": float(np.mean(mec)), "mean_medinan": float(np.mean(med)),
            "median_meccan": float(np.median(mec)), "median_medinan": float(np.median(med)),
            "n_meccan": len(mec), "n_medinan": len(med)}


def run_all_cells(rows, meccan_flag):
    return {
        "A_spearman": cell_A_spearman(rows),
        "B_kruskal_blocks": cell_B_kruskal(rows),
        "C_juz30_vs_rest": cell_C_juz30(rows),
        "D_meccan_vs_medinan": cell_D_meccan(rows, meccan_flag),
    }


# -------- MW-5 shuffle null --------

def mw5_shuffled_rows(per_verse_counts, per_verse_sets, surah_words, seed=SEED + 1):
    """Permute the per-verse token counts across ALL verses in the corpus.
    Re-aggregate per-surah. All counts preserved; placement destroyed."""
    rng = random.Random(seed)
    verse_keys = list(per_verse_counts.keys())  # only verses with at least one name
    # But the null must include zero-name verses too to properly randomize placement.
    # We instead assign token-counts across the full 6236-verse space.
    all_verses = []
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    for s in data:
        for v in s["verses"]:
            all_verses.append((s["id"], v["id"]))
    # Original full count vector (with zeros) plus the observed set
    counts_vec = [per_verse_counts.get(k, 0) for k in all_verses]
    rng.shuffle(counts_vec)
    shuffled_counts = dict(zip(all_verses, counts_vec))
    # Also shuffle the name-sets in parallel using the same permutation order.
    # We just shuffle the name_sets list in a second independent shuffle (for diversity).
    name_sets_list = [per_verse_sets.get(k, set()) for k in all_verses]
    rng2 = random.Random(seed + 2)
    rng2.shuffle(name_sets_list)
    shuffled_sets = dict(zip(all_verses, name_sets_list))
    return aggregate_per_surah(shuffled_counts, shuffled_sets, surah_words)


def main():
    random.seed(SEED)
    np.random.seed(SEED)

    surah_words = load_surah_words()
    meccan_flag = load_meccan_flag()
    per_verse_counts = load_per_verse_names()
    per_verse_sets = load_per_verse_name_set()

    rows = aggregate_per_surah(per_verse_counts, per_verse_sets, surah_words)

    # Write per-surah table
    with open(OUT_TSV, "w", encoding="utf-8") as f:
        f.write("surah\twords\tname_tokens\tname_diversity\tdensity\tblock\tjuz30\ttype\n")
        for r in rows:
            f.write(f"{r['surah']}\t{r['words']}\t{r['name_tokens']}\t{r['name_diversity']}"
                    f"\t{r['density']:.6f}\t{r['block']}\t{int(r['juz30'])}"
                    f"\t{meccan_flag.get(r['surah'], '?')}\n")

    results_real = run_all_cells(rows, meccan_flag)

    # MW-5 negative control
    shuffled_rows = mw5_shuffled_rows(per_verse_counts, per_verse_sets, surah_words)
    results_mw5 = run_all_cells(shuffled_rows, meccan_flag)

    # Top surahs for sanity
    top_density = sorted(rows, key=lambda r: -r["density"])[:15]
    top_diversity = sorted(rows, key=lambda r: -r["name_diversity"])[:15]
    top_tokens = sorted(rows, key=lambda r: -r["name_tokens"])[:15]

    # Bonferroni decisions
    def decide(p, alpha=ALPHA_PER_CELL):
        return "PASS" if p < alpha else "NULL"

    decisions = {
        "A": {"p": results_real["A_spearman"]["p_two"],
              "rho": results_real["A_spearman"]["rho"],
              "verdict": decide(results_real["A_spearman"]["p_two"])},
        "B": {"p": results_real["B_kruskal_blocks"]["p"],
              "H": results_real["B_kruskal_blocks"]["H"],
              "verdict": decide(results_real["B_kruskal_blocks"]["p"])},
        "C": {"p_directional": results_real["C_juz30_vs_rest"]["p_greater"],
              "p_two": results_real["C_juz30_vs_rest"]["p_two"],
              "verdict": decide(results_real["C_juz30_vs_rest"]["p_greater"])},
        "D": {"p_directional": results_real["D_meccan_vs_medinan"]["p_greater"],
              "p_two": results_real["D_meccan_vs_medinan"]["p_two"],
              "verdict": decide(results_real["D_meccan_vs_medinan"]["p_greater"])},
    }

    out = {
        "finding_id": "h-new-239",
        "seed": SEED,
        "bonferroni_k": BONFERRONI_K,
        "alpha_per_cell": ALPHA_PER_CELL,
        "n_surahs": 114,
        "real": results_real,
        "mw5_shuffle_null": results_mw5,
        "decisions": decisions,
        "top15_by_density": [{"surah": r["surah"], "density": r["density"],
                              "tokens": r["name_tokens"], "words": r["words"]}
                             for r in top_density],
        "top15_by_diversity": [{"surah": r["surah"], "diversity": r["name_diversity"]}
                               for r in top_diversity],
        "top15_by_tokens": [{"surah": r["surah"], "tokens": r["name_tokens"]}
                            for r in top_tokens],
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # Console summary
    print("=" * 72)
    print(f"H-NEW-239 divine-name density gradient — seed {SEED}, Bonf k={BONFERRONI_K}, α={ALPHA_PER_CELL}")
    print("=" * 72)
    a = results_real["A_spearman"]
    print(f"A Spearman(pos, density): rho={a['rho']:+.4f}  p_two={a['p_two']:.4g}  → {decisions['A']['verdict']}")
    b = results_real["B_kruskal_blocks"]
    print(f"B Kruskal-Wallis blocks : H={b['H']:.3f}  p={b['p']:.4g}  → {decisions['B']['verdict']}")
    print(f"   means: {b['means']}")
    c = results_real["C_juz30_vs_rest"]
    print(f"C juz30 vs rest (greater): U={c['U_greater']:.1f}  p={c['p_greater']:.4g}  mean_juz30={c['mean_juz30']:.4f}  mean_rest={c['mean_rest']:.4f} → {decisions['C']['verdict']}")
    d = results_real["D_meccan_vs_medinan"]
    print(f"D Meccan>Medinan (greater): U={d['U_greater']:.1f}  p={d['p_greater']:.4g}  mean_meccan={d['mean_meccan']:.4f}  mean_medinan={d['mean_medinan']:.4f} → {decisions['D']['verdict']}")
    print()
    print("MW-5 shuffle null (should all be NULL):")
    print(f" A'={results_mw5['A_spearman']['rho']:+.4f} p={results_mw5['A_spearman']['p_two']:.4g}")
    print(f" B'=H{results_mw5['B_kruskal_blocks']['H']:.2f} p={results_mw5['B_kruskal_blocks']['p']:.4g}")
    print(f" C' p_g={results_mw5['C_juz30_vs_rest']['p_greater']:.4g}")
    print(f" D' p_g={results_mw5['D_meccan_vs_medinan']['p_greater']:.4g}")
    print()
    print("Top 5 surahs by density:", [(r["surah"], f"{r['density']:.3f}") for r in top_density[:5]])
    print("Top 5 surahs by diversity:", [(r["surah"], r["name_diversity"]) for r in top_diversity[:5]])
    print(f"\nOutput: {OUT_JSON}")
    print(f"Per-surah TSV: {OUT_TSV}")


if __name__ == "__main__":
    main()
