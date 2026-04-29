"""H-NEW-94 — Q 16-25 cluster-empty zone deep-dive.

Pre-reg: findings/phase-b-hypotheses/h-new-94-q16-q25-zone-prereg.md
Family:  h-new-94-cluster-empty-zone
Bonferroni k=2, α_bon=0.025.
N_PERM=10,000.
Seed=20260417.

Two test cells:
  Cell A — isolate-count reconciliation (descriptive). Rerun H-NEW-89's
    exact cluster-membership rule set and report the isolate list,
    highlighting whether Q 19, Q 20 are correctly classified under the
    ≥2-surah classical multi-surah cluster rule.
  Cell B — shadow-cluster hunt (primary inferential). Build a pairwise
    surah similarity matrix (S1 root-Jaccard, S2 char 5-gram Dice,
    S3 H-NEW-66 verse-twin edge count) and rank-average to S_agg.
    Observed test statistic T = mean S_agg over 45 pairs in Q 16-25.
    Null = 10,000 contiguous 10-surah windows (seed 20260417).

MW-5 positive controls:
  - Q 57-64 (musabbiḥāt stretch, 8-surah window vs 8-surah null)
  - Q 40-46 (ḥawāmīm, 7-surah window vs 7-surah null)

Outputs:
  - findings/phase-b-hypotheses/csv/h-new-94.json
  - stdout summary
"""
from __future__ import annotations

import collections
import json
import random
import sys
import time
from pathlib import Path
from statistics import mean, median

sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran  # noqa: E402

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260417
N_PERM = 10_000
N_SURAHS = 114

BONFERRONI_K = 2
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.025

ZONE_Q16_Q25 = list(range(16, 26))  # 10 surahs

# MW-5 positive controls
POSITIVE_CONTROLS = {
    "Q57-64_musabbihat": list(range(57, 65)),  # 8-surah window
    "Q40-46_hawamim":    list(range(40, 47)),  # 7-surah window
}

# H-NEW-89 locked clusters (verbatim)
CLUSTERS_H89 = {
    "C1_alif_lam_mim":      {"label": "الم muqaṭṭāʿat",      "members": frozenset({2, 3, 29, 30, 31, 32})},
    "C2_alif_lam_ra":       {"label": "الر muqaṭṭāʿat",      "members": frozenset({10, 11, 12, 14, 15})},
    "C3_ha_mim":            {"label": "ḥm muqaṭṭāʿat",       "members": frozenset({40, 41, 42, 43, 44, 45, 46})},
    "C4_ta_sin_mim":        {"label": "طسم muqaṭṭāʿat",      "members": frozenset({26, 27, 28})},
    "C5_musabbihat":        {"label": "musabbiḥāt",          "members": frozenset({57, 59, 61, 62, 64})},
    "C6_sab_al_tiwal":      {"label": "al-sabʿ al-ṭiwāl",    "members": frozenset({2, 3, 4, 5, 6, 7, 9})},
    "C7_friday":            {"label": "Friday liturgy",      "members": frozenset({18, 32, 62, 76})},
    "C8_khawatim_extended": {"label": "Khawātim al-Ḥashr",   "members": frozenset({59, 62})},
    "C9_muawwidhatan":      {"label": "al-muʿawwidhatān",    "members": frozenset({113, 114})},
    "C10_zahrawan":         {"label": "al-Zahrāwān",         "members": frozenset({2, 3})},
    "C11_mufassal":         {"label": "al-mufaṣṣal",         "members": frozenset(range(49, 115))},
}

RECITATION_MARKS = set(chr(c) for c in range(0x06D6, 0x06EE))
NGRAM_N = 5


# -----------------------------------------------------------------------------
# Cell A — isolate-count reconciliation
# -----------------------------------------------------------------------------

def compute_degrees(clusters: dict) -> dict[int, int]:
    deg = {s: 0 for s in range(1, N_SURAHS + 1)}
    for cname, cdef in clusters.items():
        for s in cdef["members"]:
            deg[s] += 1
    return deg


def cell_a_reconciliation() -> dict:
    deg = compute_degrees(CLUSTERS_H89)
    isolates = sorted(s for s, d in deg.items() if d == 0)
    zone_isolates = [s for s in ZONE_Q16_Q25 if deg[s] == 0]
    zone_non_isolates = [(s, [c for c, cd in CLUSTERS_H89.items() if s in cd["members"]])
                         for s in ZONE_Q16_Q25 if deg[s] > 0]
    # Check H-NEW-89 stated isolate count (21 total, 8 in Q 16-25)
    h89_stated_total = 21
    h89_stated_zone = 8

    # Singleton-muqaṭṭāʿat alternative: under a ruleset that admits
    # single-surah muqaṭṭāʿat self-clusters {13}, {19}, {20}, {36}, {38},
    # {50}, {68}, those singletons would gain a cluster membership.
    # NOTE: Q 7 (المص) and Q 13 (المر) and others are also singletons if
    # pure-letter-sequence identity is required; the H-NEW-89 exclusion
    # specifically lists Q 13, 19, 20, 36, 38 as muqaṭṭāʿat-singletons.
    # Q 50 ق, Q 68 ن are also singletons.
    all_muqattaat_singletons = {13, 19, 20, 36, 38, 50, 68}
    # Q 7 المص is also a unique sequence but is in al-sabʿ al-ṭiwāl C6
    # so already has degree ≥ 1 in H89.
    # Q 42 عسق is part of the ḥm cluster already via ح م as its first two letters?
    # No: Q 42 = حم عسق — classified in C3 ḥm. Already degree ≥ 1.
    alt_isolates = sorted(s for s in isolates if s not in all_muqattaat_singletons)
    # Under the alternative ruleset, Q 19 and Q 20 would gain degree 1.
    alt_zone_isolates = [s for s in ZONE_Q16_Q25 if (s not in all_muqattaat_singletons) and deg[s] == 0]

    return {
        "clusters_H89_locked": {c: sorted(cd["members"]) for c, cd in CLUSTERS_H89.items()},
        "degrees_by_surah": deg,
        "all_isolates_H89_rule": isolates,
        "n_isolates_H89_rule": len(isolates),
        "zone_Q16_Q25_members": ZONE_Q16_Q25,
        "zone_Q16_Q25_isolates_H89_rule": zone_isolates,
        "n_zone_isolates_H89_rule": len(zone_isolates),
        "zone_Q16_Q25_non_isolates_H89_rule": [
            {"surah": s, "clusters": cs} for s, cs in zone_non_isolates
        ],
        "H89_stated_count_total": h89_stated_total,
        "H89_stated_count_zone": h89_stated_zone,
        "discrepancy_H89_stated_vs_recomputed_total": len(isolates) - h89_stated_total,
        "discrepancy_H89_stated_vs_recomputed_zone": len(zone_isolates) - h89_stated_zone,
        "alt_rule_singleton_muqattaat_promoted": sorted(all_muqattaat_singletons),
        "alt_rule_isolates_total": alt_isolates,
        "alt_rule_n_isolates_total": len(alt_isolates),
        "alt_rule_zone_isolates": alt_zone_isolates,
        "alt_rule_n_zone_isolates": len(alt_zone_isolates),
        "notes": (
            "Under H-NEW-89's locked ≥2-surah classical multi-surah cluster rule, "
            "Q 19 (كهيعص) and Q 20 (طه) are classical singletons (no other surah "
            "shares their opener sequence) and therefore correctly belong to no "
            "multi-member muqaṭṭāʿat cluster. Their isolate status is a faithful "
            "consequence of the H-NEW-89 rule, not an error. Under an alternative "
            "ruleset that admits singleton muqaṭṭāʿat self-clusters, they would "
            "gain degree 1 and leave the isolate list."
        ),
    }


# -----------------------------------------------------------------------------
# Cell B — shadow-cluster hunt
# -----------------------------------------------------------------------------

def normalize_text(text: str) -> str:
    chars = [ch for ch in text if ch not in RECITATION_MARKS]
    return " ".join("".join(chars).split()).strip()


def build_surah_root_sets() -> dict[int, frozenset]:
    """Return {surah_id: frozenset(root_strings)} from morphology graph."""
    path = REPO / "data" / "morphology" / "surah-root-graph.json"
    with path.open("r", encoding="utf-8") as fh:
        d = json.load(fh)
    out = {}
    for s_str, roots_dict in d["surahs"].items():
        out[int(s_str)] = frozenset(roots_dict.keys())
    # Validate coverage
    assert all(s in out for s in range(1, N_SURAHS + 1)), "missing surahs in root graph"
    return out


def build_surah_char_ngram_multisets() -> tuple[dict[int, collections.Counter], dict[int, int]]:
    """Return ({surah: Counter of 5-gram counts}, {surah: |multiset|})."""
    surahs = load_quran("no-tashkeel")
    out = {}
    lens = {}
    for s in surahs:
        concat = " ".join(normalize_text(v.text) for v in s.verses)
        cnt = collections.Counter(concat[i:i + NGRAM_N] for i in range(len(concat) - NGRAM_N + 1))
        out[s.id] = cnt
        lens[s.id] = sum(cnt.values())
    return out, lens


def multiset_intersection_size(a: collections.Counter, b: collections.Counter) -> int:
    if len(a) > len(b):
        a, b = b, a
    total = 0
    for k, va in a.items():
        vb = b.get(k)
        if vb is not None:
            total += va if va < vb else vb
    return total


def build_verse_twin_surah_counts() -> dict[tuple[int, int], int]:
    """From H-NEW-66 top-50 edges, build {(min,max): edge_count}."""
    path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-66.json"
    with path.open("r", encoding="utf-8") as fh:
        h66 = json.load(fh)
    counts = collections.Counter()
    for e in h66["top_50_edges"]:
        a, b = e["a"]["surah"], e["b"]["surah"]
        if a == b:
            continue  # skip intra-surah (shouldn't happen but be safe)
        key = (min(a, b), max(a, b))
        counts[key] += 1
    return dict(counts)


def build_similarity_matrices() -> dict:
    """Compute S1 (root-Jaccard), S2 (char 5-gram Dice), S3 (H-NEW-66 edges)
    for all C(114,2) pairs.

    Returns a dict with:
      - 'pairs': list[(i, j)] for i<j in 1..114
      - 's1'/'s2'/'s3': list[float] aligned to pairs
      - 'rank_s1', 'rank_s2', 'rank_s3': list[float] rank-of-pair (average ties)
      - 's_agg': list[float] = mean of the 3 ranks
    """
    root_sets = build_surah_root_sets()
    char_multisets, char_lens = build_surah_char_ngram_multisets()
    twin_edges = build_verse_twin_surah_counts()

    pairs = []
    s1 = []
    s2 = []
    s3 = []
    for i in range(1, N_SURAHS + 1):
        for j in range(i + 1, N_SURAHS + 1):
            pairs.append((i, j))
            # S1 root-Jaccard
            ri, rj = root_sets[i], root_sets[j]
            inter = len(ri & rj)
            union = len(ri | rj)
            s1.append(inter / union if union > 0 else 0.0)
            # S2 char 5-gram Dice
            ai, aj = char_multisets[i], char_multisets[j]
            inter_m = multiset_intersection_size(ai, aj)
            size_sum = char_lens[i] + char_lens[j]
            s2.append((2 * inter_m / size_sum) if size_sum > 0 else 0.0)
            # S3 verse-twin edge count
            s3.append(float(twin_edges.get((i, j), 0)))

    rank_s1 = average_ranks(s1)
    rank_s2 = average_ranks(s2)
    rank_s3 = average_ranks(s3)

    s_agg = [(rank_s1[k] + rank_s2[k] + rank_s3[k]) / 3.0 for k in range(len(pairs))]

    pair_index = {p: k for k, p in enumerate(pairs)}

    return {
        "pairs": pairs,
        "s1": s1,
        "s2": s2,
        "s3": s3,
        "rank_s1": rank_s1,
        "rank_s2": rank_s2,
        "rank_s3": rank_s3,
        "s_agg": s_agg,
        "pair_index": pair_index,
    }


def average_ranks(vals: list[float]) -> list[float]:
    """Return average ranks (1-indexed, ties averaged, higher value = higher rank)."""
    n = len(vals)
    indexed = sorted(enumerate(vals), key=lambda iv: iv[1])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and indexed[j + 1][1] == indexed[i][1]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0  # 1-indexed; mid of [i+1, j+1]
        for k in range(i, j + 1):
            ranks[indexed[k][0]] = avg_rank
        i = j + 1
    return ranks


def window_mean_s_agg(window_surahs: list[int], sim: dict) -> float:
    pair_index = sim["pair_index"]
    s_agg = sim["s_agg"]
    ws = sorted(window_surahs)
    scores = []
    for i in range(len(ws)):
        for j in range(i + 1, len(ws)):
            key = (ws[i], ws[j])
            scores.append(s_agg[pair_index[key]])
    return mean(scores)


def run_null_contiguous(window_size: int, sim: dict, n_perm: int, rng: random.Random, exclude_start: int = None) -> list[float]:
    """Draw n_perm contiguous windows of given size, compute T for each.

    exclude_start: if provided, skip windows starting at this position (to exclude
    the OBSERVED window from the null distribution).
    """
    max_start = N_SURAHS - window_size + 1  # e.g., 105 for size 10
    out = []
    while len(out) < n_perm:
        a = rng.randint(1, max_start)
        if exclude_start is not None and a == exclude_start:
            continue
        window = list(range(a, a + window_size))
        out.append(window_mean_s_agg(window, sim))
    return out


def cell_b_shadow_cluster(sim: dict) -> dict:
    rng = random.Random(SEED)
    # Observed
    t_obs = window_mean_s_agg(ZONE_Q16_Q25, sim)
    # Null — contiguous 10-surah windows, excluding start=16
    null_t = run_null_contiguous(10, sim, N_PERM, rng, exclude_start=16)
    k_ge = sum(1 for v in null_t if v >= t_obs)
    p_one_sided_upper = (1 + k_ge) / (1 + len(null_t))
    # Pair-level detail for Q 16-25
    ws = sorted(ZONE_Q16_Q25)
    pair_details = []
    for i in range(len(ws)):
        for j in range(i + 1, len(ws)):
            key = (ws[i], ws[j])
            k = sim["pair_index"][key]
            pair_details.append({
                "a": ws[i], "b": ws[j],
                "s1_root_jaccard": sim["s1"][k],
                "s2_char5_dice": sim["s2"][k],
                "s3_h66_edges": sim["s3"][k],
                "rank_s1": sim["rank_s1"][k],
                "rank_s2": sim["rank_s2"][k],
                "rank_s3": sim["rank_s3"][k],
                "s_agg": sim["s_agg"][k],
            })
    # Top-5 pairs inside the zone by S_agg
    pair_details_sorted = sorted(pair_details, key=lambda d: -d["s_agg"])

    return {
        "zone": ZONE_Q16_Q25,
        "window_size": 10,
        "n_perm": N_PERM,
        "seed": SEED,
        "observed_T_mean_s_agg": t_obs,
        "null_mean_T": mean(null_t),
        "null_median_T": median(null_t),
        "null_min_T": min(null_t),
        "null_max_T": max(null_t),
        "p_one_sided_upper": p_one_sided_upper,
        "alpha_bon": ALPHA_BON,
        "bonferroni_pass": p_one_sided_upper <= ALPHA_BON,
        "pair_details_sorted_desc": pair_details_sorted,
    }


def mw5_positive_controls(sim: dict) -> dict:
    out = {}
    for name, window in POSITIVE_CONTROLS.items():
        rng = random.Random(SEED + hash(name) % 1000)
        t_obs = window_mean_s_agg(window, sim)
        null_t = run_null_contiguous(len(window), sim, N_PERM, rng, exclude_start=window[0])
        k_ge = sum(1 for v in null_t if v >= t_obs)
        p = (1 + k_ge) / (1 + len(null_t))
        out[name] = {
            "window": window,
            "window_size": len(window),
            "observed_T": t_obs,
            "null_mean_T": mean(null_t),
            "null_median_T": median(null_t),
            "p_one_sided_upper": p,
            "fires_at_alpha_0.05": p <= 0.05,
        }
    return out


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------

def main() -> None:
    t0 = time.time()
    print(f"H-NEW-94 — Q 16-25 cluster-empty zone deep-dive (seed {SEED})")
    print(f"Bonferroni k={BONFERRONI_K}, α_bon={ALPHA_BON}")
    print()

    # -------------------------------
    # Cell A
    # -------------------------------
    print("=== Cell A — isolate-count reconciliation ===")
    cell_a = cell_a_reconciliation()
    print(f"All isolates (H-NEW-89 rule): n={cell_a['n_isolates_H89_rule']}")
    print(f"  {cell_a['all_isolates_H89_rule']}")
    print(f"Zone Q 16-25 isolates: n={cell_a['n_zone_isolates_H89_rule']}")
    print(f"  {cell_a['zone_Q16_Q25_isolates_H89_rule']}")
    print("Zone Q 16-25 non-isolates:")
    for item in cell_a["zone_Q16_Q25_non_isolates_H89_rule"]:
        print(f"  Q {item['surah']:>3}: {item['clusters']}")
    print(f"H89-stated vs recomputed (total):  {cell_a['H89_stated_count_total']} vs {cell_a['n_isolates_H89_rule']} "
          f"(discrepancy {cell_a['discrepancy_H89_stated_vs_recomputed_total']})")
    print(f"H89-stated vs recomputed (zone):   {cell_a['H89_stated_count_zone']} vs {cell_a['n_zone_isolates_H89_rule']} "
          f"(discrepancy {cell_a['discrepancy_H89_stated_vs_recomputed_zone']})")
    print(f"Alternative-rule (promoting singleton muqaṭṭāʿat): total isolates n={cell_a['alt_rule_n_isolates_total']}, zone n={cell_a['alt_rule_n_zone_isolates']}")
    print()

    # -------------------------------
    # Build similarity matrices
    # -------------------------------
    print("Building similarity matrices (S1 root-Jaccard, S2 char-5-gram Dice, S3 H-NEW-66 twins)...")
    sim = build_similarity_matrices()
    print(f"  n_pairs = {len(sim['pairs'])}")
    print(f"  S1 range: [{min(sim['s1']):.4f}, {max(sim['s1']):.4f}], mean={mean(sim['s1']):.4f}")
    print(f"  S2 range: [{min(sim['s2']):.4f}, {max(sim['s2']):.4f}], mean={mean(sim['s2']):.4f}")
    print(f"  S3 range: [{min(sim['s3']):.2f}, {max(sim['s3']):.2f}], mean={mean(sim['s3']):.4f}")
    print()

    # -------------------------------
    # Cell B
    # -------------------------------
    print("=== Cell B — shadow-cluster hunt (10-surah contiguous window null, 10K perms) ===")
    cell_b = cell_b_shadow_cluster(sim)
    print(f"Observed T (Q 16-25 mean S_agg): {cell_b['observed_T_mean_s_agg']:.3f}")
    print(f"Null mean T:  {cell_b['null_mean_T']:.3f} (median {cell_b['null_median_T']:.3f})")
    print(f"Null range:   [{cell_b['null_min_T']:.3f}, {cell_b['null_max_T']:.3f}]")
    print(f"p (one-sided upper): {cell_b['p_one_sided_upper']:.5f}")
    print(f"α_bon = {ALPHA_BON}; Bonferroni-PASS: {cell_b['bonferroni_pass']}")
    print()
    print("Top-5 Q 16-25 internal pairs by S_agg:")
    for pd in cell_b["pair_details_sorted_desc"][:5]:
        print(f"  Q{pd['a']:>3}↔Q{pd['b']:>3}  S_agg={pd['s_agg']:.1f}  "
              f"[J={pd['s1_root_jaccard']:.3f} Dice={pd['s2_char5_dice']:.4f} twins={int(pd['s3_h66_edges'])}]")
    print()

    # -------------------------------
    # MW-5 positive controls
    # -------------------------------
    print("=== MW-5 positive controls ===")
    pc = mw5_positive_controls(sim)
    for name, d in pc.items():
        status = "✓ fires" if d["fires_at_alpha_0.05"] else "✗ NULL-BROKEN"
        print(f"{name}: obs={d['observed_T']:.3f} null-mean={d['null_mean_T']:.3f} p={d['p_one_sided_upper']:.5f}  {status}")
    print()

    # -------------------------------
    # Verdict
    # -------------------------------
    pc_all_fire = all(d["fires_at_alpha_0.05"] for d in pc.values())
    if not pc_all_fire:
        verdict_b = "NULL-BROKEN (MW-5 failed)"
    elif cell_b["bonferroni_pass"]:
        verdict_b = "PASS"
    else:
        verdict_b = "NULL"
    print(f"=== Verdict ===")
    print(f"Cell A: DESCRIPTIVE (isolate count reconciled; see JSON)")
    print(f"Cell B: {verdict_b}")
    print(f"elapsed: {time.time() - t0:.1f}s")

    # -------------------------------
    # JSON output
    # -------------------------------
    # The full pair_index is large; drop it to keep JSON compact; also drop rank arrays
    out = {
        "id": "H-NEW-94",
        "date": "2026-04-17",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "bonferroni_family": "h-new-94-cluster-empty-zone",
        "cell_A_descriptive_reconciliation": cell_a,
        "cell_B_primary_shadow_cluster": {k: v for k, v in cell_b.items()},
        "mw5_positive_controls": pc,
        "verdict_cell_B": verdict_b,
        "verdict_cell_A": "DESCRIPTIVE (see cell_A_descriptive_reconciliation.notes)",
        "elapsed_sec": time.time() - t0,
    }
    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-94.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=str)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
