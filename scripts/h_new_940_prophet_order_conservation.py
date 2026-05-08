#!/usr/bin/env python3
"""H-NEW-940 — Prophet-cycle order conservation across 8 narrative surahs.

Pre-registration:  findings/phase-b-hypotheses/h-new-940-prophet-order-conservation-prereg.md
Pre-reg SHA256:   2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66
Seed:             20260507
Permutations:     10000
Bonferroni-k:     4 (H2 sub-axes)
Direction-locked: positive mean Kendall-tau

stdlib-only.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import re
import sys
from collections import defaultdict
from itertools import combinations
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = (
    PROJECT_ROOT
    / "findings/phase-b-hypotheses/h-new-940-prophet-order-conservation-prereg.md"
)
EXPECTED_PREREG_SHA = (
    "2351e2c7569e3ce22054edd709b127b234ac662ca23879dc41f62be494b27f66"
)
MORPH_PATH = PROJECT_ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
CHRONO_PATH = PROJECT_ROOT / "data/revelation-order.csv"
OUT_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-940.json"

SEED = 20260507
N_PERM = 10_000
ALPHA_BON = 0.0125
SURAH_SET = [6, 7, 11, 19, 21, 26, 37, 38]

# Locked prophet → QAC LEM mapping (verified against morphology file)
PROPHET_LEMMAS = {
    "Adam": "A^dam",
    "Idris": "<idoriys",
    "Nuh": "nuwH",
    "Hud": "huwd",  # NOT huwd2 (= "Jews")
    "Salih": "Sa`liH2",
    "Ibrahim": "<iboraAhiym",
    "Lut": "luwT",
    "Ismail": "<isomaAEiyl",
    "Ishaq": "<isoHaAq",
    "Yaqub": "yaEoquwb",
    "Yusuf": "yuwsuf",
    "Shuayb": "$uEayob",
    "Musa": "muwsaY`",
    "Harun": "ha`ruwn",
    "Yunus": "yuwnus",
    "Dawud": "daAwud",
    "Sulayman": "sulayoma`n",
    "Ayyub": ">ay~uwb",
    "Ilyas": "<iloyaAs",
    "Yasa": "{loyasaEa",
    # Dhu al-Kifl handled via verse-anchors (not a single lemma)
    "Zakariyya": "zakariy~aA",
    "Yahya": "yaHoyaY`",
    "Isa": "EiysaY",
    "Muhammad": "muHam~ad",
    # Ahmad (Q 61:6) merges to Muhammad — but Q 61 not in 8-surah set
}
# Verse-anchored prophets (no single LEM)
DHU_AL_KIFL_LOCS = {
    21: (85, 4, 2),  # Q 21:85 word-pos 4 segment 2 (lemma="kifol")
    38: (48, 5, 2),  # Q 38:48 word-pos 5 segment 2 (lemma="kifol")
}


# ---------------------------- helpers ---------------------------- #


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
LEM_RE = re.compile(r"LEM:([^|]+)")
POS_RE = re.compile(r"POS:([A-Z]+)")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def extract_prophet_first_locs():
    """For each surah in SURAH_SET, return dict[prophet_name] -> (verse, word, seg) of FIRST occurrence."""
    # First, collect ALL prophet attestations across the corpus
    # Map LEM -> prophet name (reverse the dict)
    lem_to_prophet = {lem: name for name, lem in PROPHET_LEMMAS.items()}

    # per-surah per-prophet list of locs
    by_surah: dict[int, dict[str, list[tuple[int, int, int]]]] = {
        s: defaultdict(list) for s in SURAH_SET
    }

    with MORPH_PATH.open() as fh:
        for raw in fh:
            if not raw.startswith("("):
                continue
            parts = raw.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc_match = LOC_RE.match(parts[0])
            if not loc_match:
                continue
            surah, verse, word, seg = (int(x) for x in loc_match.groups())
            if surah not in SURAH_SET:
                continue
            feats = parts[3]
            pos = (POS_RE.search(feats) or [None, None])[1] if POS_RE.search(feats) else None
            lem_match = LEM_RE.search(feats)
            lem = lem_match.group(1) if lem_match else None

            # PN-lemma based prophet detection
            if pos == "PN" and lem in lem_to_prophet:
                prophet = lem_to_prophet[lem]
                by_surah[surah][prophet].append((verse, word, seg))

            # Dhū al-Kifl verse-anchor detection
            anchor = DHU_AL_KIFL_LOCS.get(surah)
            if anchor and (verse, word, seg) == anchor:
                # Check ROOT is kfl as a sanity cross-check
                root_match = ROOT_RE.search(feats)
                if root_match and root_match.group(1) == "kfl":
                    by_surah[surah]["DhuAlKifl"].append((verse, word, seg))

    # Reduce to first-loc per prophet per surah
    first_locs: dict[int, dict[str, tuple[int, int, int]]] = {}
    for s in SURAH_SET:
        first_locs[s] = {p: min(locs) for p, locs in by_surah[s].items() if locs}
    return first_locs


def order_vector(first_locs_for_surah: dict[str, tuple[int, int, int]]) -> list[str]:
    """Return list of prophet names sorted by (verse, word, seg) of first occurrence."""
    return sorted(first_locs_for_surah, key=lambda p: first_locs_for_surah[p])


def kendall_tau_on_pair(order_a: list[str], order_b: list[str]) -> tuple[float, int]:
    """Kendall's τ on the SHARED-prophet subset of two ordered lists.

    Returns (tau, n_shared). If n_shared < 2, returns (nan, n_shared).
    Uses plain (concordant - discordant) / (n*(n-1)/2) (tau-a, no tie correction needed
    since orderings are strict — first-occurrence locations are unique tuples within a surah).
    """
    set_a = set(order_a)
    shared = [p for p in order_a if p in set(order_b)]
    n = len(shared)
    if n < 2:
        return float("nan"), n
    rank_a = {p: i for i, p in enumerate(order_a) if p in shared}
    rank_b = {p: i for i, p in enumerate(order_b) if p in shared}
    concordant = 0
    discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            p, q = shared[i], shared[j]
            sign_a = rank_a[p] - rank_a[q]
            sign_b = rank_b[p] - rank_b[q]
            if sign_a * sign_b > 0:
                concordant += 1
            elif sign_a * sign_b < 0:
                discordant += 1
    total = n * (n - 1) // 2
    return (concordant - discordant) / total, n


def mean_tau(orders: dict[int, list[str]]) -> tuple[float, list[dict]]:
    """Mean Kendall-tau across all C(K,2) pairs with |shared| >= 2."""
    pairs_info: list[dict] = []
    taus: list[float] = []
    for a, b in combinations(sorted(orders.keys()), 2):
        tau, n = kendall_tau_on_pair(orders[a], orders[b])
        pairs_info.append(
            {
                "surah_a": a,
                "surah_b": b,
                "n_shared": n,
                "kendall_tau": tau if not math.isnan(tau) else None,
            }
        )
        if not math.isnan(tau):
            taus.append(tau)
    return (sum(taus) / len(taus) if taus else float("nan")), pairs_info


# --------------------- H2 sub-tests --------------------- #


def kendall_tau_against_canonical(
    surah_order: list[str], canonical: list[str]
) -> tuple[float, int]:
    """τ between this surah's order and the canonical chain order, on shared prophets."""
    return kendall_tau_on_pair(surah_order, canonical)


def h2a_test(orders, rng):
    """Adam → Nuh → Hud → Salih chain conservation."""
    canonical = ["Adam", "Nuh", "Hud", "Salih"]
    obs_taus = []
    qualifying = []
    for s, ord_s in orders.items():
        present = [p for p in canonical if p in ord_s]
        if len(present) >= 2:
            sub_order = [p for p in ord_s if p in present]
            tau, n = kendall_tau_on_pair(sub_order, [p for p in canonical if p in present])
            if not math.isnan(tau):
                obs_taus.append(tau)
                qualifying.append({"surah": s, "present": present, "sub_order": sub_order, "tau": tau})
    obs_mean = sum(obs_taus) / len(obs_taus) if obs_taus else float("nan")

    # Permutation null: for each qualifying surah, shuffle the sub-order
    null_means = []
    for _ in range(N_PERM):
        nulls = []
        for q in qualifying:
            sub = list(q["sub_order"])
            rng.shuffle(sub)
            tau, _ = kendall_tau_on_pair(sub, [p for p in canonical if p in q["present"]])
            if not math.isnan(tau):
                nulls.append(tau)
        if nulls:
            null_means.append(sum(nulls) / len(nulls))
    p = (sum(1 for n in null_means if n >= obs_mean) + 1) / (len(null_means) + 1) if not math.isnan(obs_mean) else float("nan")
    return {
        "test": "H2a",
        "canonical": canonical,
        "qualifying": qualifying,
        "obs_mean_tau": obs_mean,
        "perm_p_one_tailed": p,
        "n_perm": len(null_means),
        "alpha_bon": ALPHA_BON,
        "passes": (not math.isnan(p)) and (obs_mean > 0) and (p < ALPHA_BON),
    }


def h2b_test(orders, rng):
    """Ibrahim → Ismail → Ishaq chain conservation."""
    canonical = ["Ibrahim", "Ismail", "Ishaq"]
    obs_taus = []
    qualifying = []
    for s, ord_s in orders.items():
        present = [p for p in canonical if p in ord_s]
        if len(present) >= 2:
            sub_order = [p for p in ord_s if p in present]
            tau, n = kendall_tau_on_pair(sub_order, [p for p in canonical if p in present])
            if not math.isnan(tau):
                obs_taus.append(tau)
                qualifying.append({"surah": s, "present": present, "sub_order": sub_order, "tau": tau})
    obs_mean = sum(obs_taus) / len(obs_taus) if obs_taus else float("nan")
    null_means = []
    for _ in range(N_PERM):
        nulls = []
        for q in qualifying:
            sub = list(q["sub_order"])
            rng.shuffle(sub)
            tau, _ = kendall_tau_on_pair(sub, [p for p in canonical if p in q["present"]])
            if not math.isnan(tau):
                nulls.append(tau)
        if nulls:
            null_means.append(sum(nulls) / len(nulls))
    p = (sum(1 for n in null_means if n >= obs_mean) + 1) / (len(null_means) + 1) if not math.isnan(obs_mean) else float("nan")
    return {
        "test": "H2b",
        "canonical": canonical,
        "qualifying": qualifying,
        "obs_mean_tau": obs_mean,
        "perm_p_one_tailed": p,
        "n_perm": len(null_means),
        "alpha_bon": ALPHA_BON,
        "passes": (not math.isnan(p)) and (obs_mean > 0) and (p < ALPHA_BON),
    }


def h2c_test(orders):
    """Mūsā → Hārūn binomial test (one-tailed, p_null = 0.5)."""
    qualifying = []
    musa_first = 0
    for s, ord_s in orders.items():
        if "Musa" in ord_s and "Harun" in ord_s:
            i_m = ord_s.index("Musa")
            i_h = ord_s.index("Harun")
            qualifying.append(
                {"surah": s, "musa_pos": i_m, "harun_pos": i_h, "musa_first": i_m < i_h}
            )
            if i_m < i_h:
                musa_first += 1
    n = len(qualifying)
    # Exact binomial one-tailed (alternative: > 0.5)
    if n == 0:
        return {"test": "H2c", "n": 0, "passes": False, "p_one_tailed": float("nan")}
    # P(X >= musa_first | p=0.5) = sum_{k=musa_first}^n C(n,k) * 0.5^n
    from math import comb

    p_val = sum(comb(n, k) for k in range(musa_first, n + 1)) / (2 ** n)
    return {
        "test": "H2c",
        "qualifying": qualifying,
        "n": n,
        "musa_first_count": musa_first,
        "proportion": musa_first / n,
        "p_one_tailed": p_val,
        "alpha_bon": ALPHA_BON,
        "passes": p_val < ALPHA_BON and (musa_first / n) > 0.5,
    }


def h2d_test(orders, rng):
    """Q 21 prophet-list vs Q 6:83-87 prophet-list — Kendall-tau."""
    # Need to extract Q 6's prophet-order RESTRICTED to verses 83-87
    # Re-derive from raw morphology
    lem_to_prophet = {lem: name for name, lem in PROPHET_LEMMAS.items()}
    q6_subset_locs: dict[str, tuple[int, int, int]] = {}
    with MORPH_PATH.open() as fh:
        for raw in fh:
            if not raw.startswith("("):
                continue
            parts = raw.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc_match = LOC_RE.match(parts[0])
            if not loc_match:
                continue
            s, v, w, seg = (int(x) for x in loc_match.groups())
            if s != 6 or not (83 <= v <= 87):
                continue
            feats = parts[3]
            pos_m = POS_RE.search(feats)
            pos = pos_m.group(1) if pos_m else None
            lem_m = LEM_RE.search(feats)
            lem = lem_m.group(1) if lem_m else None
            if pos == "PN" and lem in lem_to_prophet:
                p = lem_to_prophet[lem]
                if p not in q6_subset_locs:
                    q6_subset_locs[p] = (v, w, seg)
                else:
                    q6_subset_locs[p] = min(q6_subset_locs[p], (v, w, seg))
    q6_order = sorted(q6_subset_locs, key=lambda p: q6_subset_locs[p])
    q21_order = orders[21]
    tau, n = kendall_tau_on_pair(q6_order, q21_order)
    # Permutation null: shuffle one of the two
    null_taus = []
    for _ in range(N_PERM):
        shuffled = list(q21_order)
        rng.shuffle(shuffled)
        t, _ = kendall_tau_on_pair(q6_order, shuffled)
        if not math.isnan(t):
            null_taus.append(t)
    p = (sum(1 for x in null_taus if x >= tau) + 1) / (len(null_taus) + 1) if not math.isnan(tau) else float("nan")
    return {
        "test": "H2d",
        "q6_subset_order": q6_order,
        "q21_order": q21_order,
        "n_shared": n,
        "obs_tau": tau,
        "perm_p_one_tailed": p,
        "alpha_bon": ALPHA_BON,
        "threshold_tau": 0.7,
        "passes": (not math.isnan(tau)) and (tau > 0.7) and (p < ALPHA_BON),
    }


# --------------------- H3 typology --------------------- #


def consensus_order(orders):
    """Build consensus order via mean rank across surahs (only prophets in >=2 surahs)."""
    rank_sums: dict[str, list[float]] = defaultdict(list)
    for s, ord_s in orders.items():
        K = len(ord_s)
        for i, p in enumerate(ord_s):
            rank_sums[p].append(i / max(K - 1, 1))  # normalized rank in [0, 1]
    mean_ranks = {p: sum(rs) / len(rs) for p, rs in rank_sums.items() if len(rs) >= 2}
    consensus = sorted(mean_ranks, key=lambda p: mean_ranks[p])
    # Solo prophets (only in 1 surah) appended at end of consensus, ordered by mean rank too
    solo = {p: sum(rs) / len(rs) for p, rs in rank_sums.items() if len(rs) == 1}
    consensus_full = consensus + sorted(solo, key=lambda p: solo[p])
    return consensus, consensus_full, mean_ranks, rank_sums


def per_surah_consensus_deviation(orders, consensus_full):
    devs = {}
    for s, ord_s in orders.items():
        tau, n = kendall_tau_on_pair(ord_s, consensus_full)
        devs[s] = {"tau_to_consensus": tau, "n_shared": n}
    return devs


def load_chronology():
    """Return surah → noldeke_phase mapping."""
    phases = {}
    if not CHRONO_PATH.exists():
        return phases
    with CHRONO_PATH.open() as fh:
        header = fh.readline().rstrip("\n").split(",")
        # find columns (mushaf_order is the canonical surah-id column)
        sura_col = -1
        for cand in ("mushaf_order", "sura", "surah"):
            if cand in header:
                sura_col = header.index(cand)
                break
        if sura_col < 0:
            sura_col = 1  # fallback: column 1 in the project's revelation-order.csv
        try:
            phase_col = header.index("noldeke_phase")
        except ValueError:
            try:
                phase_col = header.index("nöldeke_phase")
            except ValueError:
                phase_col = -1
        if phase_col < 0:
            return phases
        for line in fh:
            parts = line.rstrip("\n").split(",")
            if len(parts) > max(sura_col, phase_col):
                try:
                    phases[int(parts[sura_col])] = parts[phase_col].strip()
                except ValueError:
                    pass
    return phases


# --------------------- main --------------------- #


def main():
    actual_sha = sha256_file(PREREG_PATH)
    if actual_sha != EXPECTED_PREREG_SHA:
        print(
            f"ABORT: pre-reg SHA mismatch.\n  expected: {EXPECTED_PREREG_SHA}\n  actual:   {actual_sha}",
            file=sys.stderr,
        )
        sys.exit(1)

    rng = random.Random(SEED)

    # ---- Step 1: extract per-surah first-locations ----
    first_locs = extract_prophet_first_locs()
    orders = {s: order_vector(first_locs[s]) for s in SURAH_SET}

    # Sanity-print
    print("=== PER-SURAH PROPHET ORDERINGS ===")
    for s in SURAH_SET:
        print(f"Q{s} (K={len(orders[s])}): {orders[s]}")
    print()

    # ---- Step 2: pairwise Kendall-tau ----
    obs_mean, pair_info = mean_tau(orders)
    print(f"OBSERVED mean Kendall-tau across pairs: {obs_mean:.4f}")
    n_pairs_used = sum(1 for p in pair_info if p["kendall_tau"] is not None)
    print(f"  using {n_pairs_used}/{len(pair_info)} pairs (|shared| >= 2)")

    # ---- Step 3: permutation null ----
    print(f"\nRunning {N_PERM} permutations (seed={SEED})...")
    null_means = []
    for i in range(N_PERM):
        shuffled = {}
        for s, ord_s in orders.items():
            tmp = list(ord_s)
            rng.shuffle(tmp)
            shuffled[s] = tmp
        m, _ = mean_tau(shuffled)
        if not math.isnan(m):
            null_means.append(m)
    null_mean_avg = sum(null_means) / len(null_means)
    null_mean_std = (sum((x - null_mean_avg) ** 2 for x in null_means) / len(null_means)) ** 0.5
    p_h1 = (sum(1 for n in null_means if n >= obs_mean) + 1) / (len(null_means) + 1)
    z_h1 = (obs_mean - null_mean_avg) / null_mean_std if null_mean_std > 0 else float("nan")
    print(f"  null mean: {null_mean_avg:.4f} ± {null_mean_std:.4f}")
    print(f"  H1 p (one-tailed, positive): {p_h1:.6f}")
    print(f"  H1 z: {z_h1:.3f}")
    h1_pass = obs_mean > 0 and p_h1 < 0.01

    # ---- Step 4: H2 sub-tests (independent rng for each to avoid cross-pollution) ----
    rng_a = random.Random(SEED + 1)
    rng_b = random.Random(SEED + 2)
    rng_d = random.Random(SEED + 3)
    print("\n=== H2a: Adam-Nuh-Hud-Salih chain ===")
    h2a = h2a_test(orders, rng_a)
    print(f"  obs mean tau: {h2a['obs_mean_tau']:.4f}, perm p: {h2a['perm_p_one_tailed']:.4f}, passes: {h2a['passes']}")

    print("\n=== H2b: Ibrahim-Ismail-Ishaq chain ===")
    h2b = h2b_test(orders, rng_b)
    print(f"  obs mean tau: {h2b['obs_mean_tau']:.4f}, perm p: {h2b['perm_p_one_tailed']:.4f}, passes: {h2b['passes']}")

    print("\n=== H2c: Musa-Harun binomial ===")
    h2c = h2c_test(orders)
    print(f"  n qualifying: {h2c['n']}, musa-first: {h2c['musa_first_count']}, p (1-tail): {h2c['p_one_tailed']:.4f}")

    print("\n=== H2d: Q21 vs Q6:83-87 ===")
    h2d = h2d_test(orders, rng_d)
    print(f"  obs tau: {h2d['obs_tau']:.4f}, n_shared: {h2d['n_shared']}, perm p: {h2d['perm_p_one_tailed']:.4f}")

    # ---- Step 5: H3 consensus + deviation typology ----
    cons_inner, cons_full, mean_ranks, rank_sums = consensus_order(orders)
    devs = per_surah_consensus_deviation(orders, cons_full)
    chronology = load_chronology()

    print("\n=== H3 CONSENSUS ORDER ===")
    print(f"  (>=2 surahs): {cons_inner}")
    print("  per-surah deviation (tau to consensus):")
    for s in SURAH_SET:
        phase = chronology.get(s, "?")
        print(f"    Q{s} ({phase}): tau={devs[s]['tau_to_consensus']:.3f}")

    # ---- Step 6: write JSON output ----
    output = {
        "finding_id": "h-new-940",
        "prereg_sha256": EXPECTED_PREREG_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "surah_set": SURAH_SET,
        "rules_tuple": {
            "tashkeel": "no-tashkeel",
            "token": "QAC-PN-lemma",
            "letter": "graphemes",
            "basmala": "counted-only-in-Q1",
            "reading": "Hafs-Kufan",
            "script": "Mashriqi",
        },
        "prophet_lemmas": PROPHET_LEMMAS,
        "per_surah_orders": {str(s): orders[s] for s in SURAH_SET},
        "per_surah_first_locs": {
            str(s): {p: list(loc) for p, loc in first_locs[s].items()} for s in SURAH_SET
        },
        "h1": {
            "obs_mean_kendall_tau": obs_mean,
            "null_mean": null_mean_avg,
            "null_std": null_mean_std,
            "perm_p_one_tailed": p_h1,
            "perm_z": z_h1,
            "n_pairs_used": n_pairs_used,
            "n_pairs_total": len(pair_info),
            "alpha": 0.01,
            "passes": h1_pass,
            "pairs": pair_info,
        },
        "h2a": h2a,
        "h2b": h2b,
        "h2c": h2c,
        "h2d": h2d,
        "h3": {
            "consensus_order_appearing_in_2plus_surahs": cons_inner,
            "consensus_full": cons_full,
            "mean_normalized_rank_per_prophet": mean_ranks,
            "n_attestations_per_prophet": {p: len(rs) for p, rs in rank_sums.items()},
            "per_surah_tau_to_consensus": {str(s): devs[s] for s in SURAH_SET},
            "noldeke_phase": {str(s): chronology.get(s, "?") for s in SURAH_SET},
        },
        "summary": {
            "h1_pass": h1_pass,
            "h2a_pass": h2a["passes"],
            "h2b_pass": h2b["passes"],
            "h2c_pass": h2c["passes"],
            "h2d_pass": h2d["passes"],
            "bonferroni_h2_count_pass": sum(
                [h2a["passes"], h2b["passes"], h2c["passes"], h2d["passes"]]
            ),
        },
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\nWrote {OUT_PATH}")
    return output


if __name__ == "__main__":
    main()
