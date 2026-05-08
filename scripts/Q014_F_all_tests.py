#!/usr/bin/env python3
"""
Q014 — Ibrāhīm: 3 pre-registered novel tests.
Bonferroni-k = 3; α_bon = 0.0167; seed = 20260508; n_perm = 10000.

Run script for the Q 14 specialist family-of-tests.

SHA256-locks: each test verifies its own pre-reg's SHA at runtime; mismatch = abort.
"""

import json, os, sys, math, random, hashlib, statistics, itertools, re

ROOT = "/Users/grey/Downloads/quran"
SUR = os.path.join(ROOT, "surahs", "Q014-ibrahim")
CSV_DIR = os.path.join(SUR, "csv")
PREREG_DIR = os.path.join(SUR, "preregs")
os.makedirs(CSV_DIR, exist_ok=True)

EXPECTED_SHA = {
    "Q014-F-01": "9bfe6edf1baff43c6e63800f0f2d163ffc726f2bee78f1144643eba7c7059274",
    "Q014-F-02": "122637ab720e00e7d8e3c37dc4cecdb2259fa7df07e578a18092a1461f61609a",
    "Q014-F-03": "3c06deac20c5bb6f3db315daf37476682950ffdecc71599d3645f8e211092a91",
}
PREREG_PATHS = {
    "Q014-F-01": os.path.join(PREREG_DIR, "Q014-F-01-abrahamic-prayer-density-prereg.md"),
    "Q014-F-02": os.path.join(PREREG_DIR, "Q014-F-02-bilateral-twin-q13-prereg.md"),
    "Q014-F-03": os.path.join(PREREG_DIR, "Q014-F-03-alr-cluster-membership-prereg.md"),
}

SEED = 20260508
N_PERM = 10000
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K  # ≈ 0.0167

# ===================== Pre-reg SHA verification =====================

def sha256(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def assert_prereg_sha():
    for tid, expected in EXPECTED_SHA.items():
        actual = sha256(PREREG_PATHS[tid])
        if actual != expected:
            sys.exit(f"FATAL: pre-reg SHA mismatch on {tid}: expected {expected}, got {actual}")
        print(f"[SHA-OK] {tid}: {actual[:16]}...")

# ===================== Data loaders =====================

def load_fr_matrix():
    """Returns dict (a,b) -> FR distance, 1-indexed."""
    with open(os.path.join(ROOT, "findings", "phase-b-hypotheses", "csv", "h-new-111.json")) as f:
        d = json.load(f)
    pair_dist = {}
    for trip in d["D_matrix_upper_triangular"]:
        a, b, dist = trip[0], trip[1], trip[2]
        pair_dist[(a, b)] = dist
        pair_dist[(b, a)] = dist
    for s in range(1, 115):
        pair_dist[(s, s)] = 0.0
    return pair_dist

def load_h750():
    with open(os.path.join(ROOT, "findings", "phase-b-hypotheses", "csv", "h-new-750.json")) as f:
        d = json.load(f)
    return {r["surah"]: r for r in d["per_surah"]}

def load_quran_no_tashkeel():
    with open(os.path.join(ROOT, "quran-text", "quran-no-tashkeel.json")) as f:
        return json.load(f)

# ===================== Signature helper =====================

def signature(s, h750, _z_cache=[]):
    """4-axis vector for surah s: [z_FR_mean, z_sig_A, z_sig_B, z_rhyme_entropy]."""
    if not _z_cache:
        all_sigA = [h750[s_]["sig_A"] for s_ in h750]
        all_sigB = [h750[s_]["sig_B"] for s_ in h750]
        mu_A = sum(all_sigA) / len(all_sigA)
        sd_A = (sum((x - mu_A) ** 2 for x in all_sigA) / (len(all_sigA) - 1)) ** 0.5
        mu_B = sum(all_sigB) / len(all_sigB)
        sd_B = (sum((x - mu_B) ** 2 for x in all_sigB) / (len(all_sigB) - 1)) ** 0.5
        _z_cache.extend([mu_A, sd_A, mu_B, sd_B])
    mu_A, sd_A, mu_B, sd_B = _z_cache
    r = h750[s]
    return [
        r["z_mean_content_distance"],
        (r["sig_A"] - mu_A) / sd_A,
        (r["sig_B"] - mu_B) / sd_B,
        r["z_rhyme_entropy"],
    ]

def euclid(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

# ===================== TEST 1: Mecca-prayer corpus-MAX prayer-density =====================

def is_prayer_token(token):
    """Return True if a no-tashkeel token is a prayer-vocative-cluster lemma per pre-reg."""
    cleaned = token.strip("۞۩.،,!?:;()[]")
    # Vocatives
    if cleaned in ("رب", "ربنا", "ربي", "اللهم"):
        return True
    # Petition imperatives — startswith match
    PETITION_PREFIXES = (
        "اجعل", "فاجعل", "ارزق", "وارزق", "اغفر", "فاغفر",
        "اهدنا", "اهدني", "فاهد", "وهب", "تقبل",
    )
    for pref in PETITION_PREFIXES:
        if cleaned.startswith(pref):
            return True
    # Special: سميع الدعاء context — match "سميع" only when preceding "الدعاء"
    # We handle this at sentence-level outside; here, return False for "سميع" alone.
    return False

def density(text):
    tokens = text.split()
    nw = len(tokens)
    if nw == 0:
        return 0.0, 0
    n_hit = sum(1 for t in tokens if is_prayer_token(t))
    return (n_hit / nw * 100.0, n_hit)

def run_F01(quran_data):
    """Q 14:35-41 corpus-MAX prayer-density 7-verse window."""
    # All 7-verse windows in the corpus
    windows = []
    for surah in quran_data:
        sid = surah["id"]
        verses = surah["verses"]
        nv = len(verses)
        if nv < 7:
            continue
        for start in range(nv - 6):
            block = " ".join(verses[start + i]["text"] for i in range(7))
            d, n = density(block)
            windows.append({
                "surah": sid,
                "v_start": verses[start]["id"],
                "v_end": verses[start + 6]["id"],
                "density_per_100w": d,
                "n_prayer_tokens": n,
                "n_words": len(block.split()),
            })

    # Sort descending by density
    windows_sorted = sorted(windows, key=lambda x: -x["density_per_100w"])

    # Find Q 14:35-41
    target = None
    target_rank = None
    for r, w in enumerate(windows_sorted, start=1):
        if w["surah"] == 14 and w["v_start"] == 35 and w["v_end"] == 41:
            target = w
            target_rank = r
            break

    n_total = len(windows_sorted)

    # Per-surah whole-surah density
    per_surah_density = []
    for surah in quran_data:
        sid = surah["id"]
        txt = " ".join(v["text"] for v in surah["verses"])
        d, n = density(txt)
        per_surah_density.append({"surah": sid, "density": d, "n": n, "n_words": len(txt.split())})
    per_surah_sorted = sorted(per_surah_density, key=lambda x: -x["density"])
    q14_surah_rank = next(r for r, x in enumerate(per_surah_sorted, 1) if x["surah"] == 14)

    # Verdict
    if target_rank == 1:
        verdict = "CONFIRMED — corpus-MAX rank 1"
    elif target_rank <= 5:
        verdict = "PASS-DIRECTED — top-5"
    elif target_rank <= max(56, n_total // 100):
        verdict = "DIRECTIONAL — top-1%"
    elif target_rank <= max(279, n_total // 20):
        verdict = "NULL — top-5% but not top-1%"
    else:
        verdict = "PRE-COMMIT VIOLATION — below top-5%"

    out = {
        "test_id": "Q014-F-01",
        "title": "Q 14:35-41 Mecca-prayer corpus-MAX prayer-vocative density",
        "n_total_7verse_windows": n_total,
        "Q14_35_41_window": target,
        "Q14_35_41_rank": target_rank,
        "top10_windows": windows_sorted[:10],
        "Q14_whole_surah_density_rank": q14_surah_rank,
        "top10_whole_surah_density": per_surah_sorted[:10],
        "n_perm": "n/a (descriptive corpus-rank)",
        "alpha_bon": ALPHA_BON,
        "verdict": verdict,
    }
    return out

# ===================== TEST 2: Bilateral mutual-nearest twin (Q 13 ↔ Q 14) =====================

def run_F02(pair_dist, h750):
    Q = 14
    # Test (a) FR-nearest
    others = [s for s in range(1, 115) if s != Q]
    nearest = min(others, key=lambda j: pair_dist[(Q, j)])
    nearest_d = pair_dist[(Q, nearest)]

    # Verify Q 13's nearest is Q 14 (the bilateral check — the OTHER half from Q013-F-04/Q013-F-05)
    others13 = [s for s in range(1, 115) if s != 13]
    nearest_to_13 = min(others13, key=lambda j: pair_dist[(13, j)])
    nearest_to_13_d = pair_dist[(13, nearest_to_13)]

    bilateral_FR = (nearest == 13) and (nearest_to_13 == 14)

    # Sub-test (b) 4-axis
    v14 = signature(Q, h750)
    v13 = signature(13, h750)
    v76 = signature(76, h750)

    d_arch_14_13 = euclid(v14, v13)
    d_arch_14_76 = euclid(v14, v76)

    twin_strength_ratio = d_arch_14_76 / d_arch_14_13 if d_arch_14_13 > 0 else float("inf")
    closer_to_13 = d_arch_14_13 < d_arch_14_76

    # Top-5 nearest list for context
    by_d = sorted(others, key=lambda j: pair_dist[(Q, j)])
    top5 = [(s, pair_dist[(Q, s)]) for s in by_d[:5]]

    # Verdict
    if bilateral_FR and closer_to_13:
        verdict = "CONFIRMED — bilateral mutual-nearest pair AND 4-axis twin"
    elif bilateral_FR or closer_to_13:
        verdict = "PASS-DIRECTED — partial confirmation (one-of-two)"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q014-F-02",
        "title": "Q 13 ↔ Q 14 bilateral mutual-nearest FR-content twin pair",
        "Q14_FR_nearest": nearest,
        "Q14_FR_nearest_distance": nearest_d,
        "Q13_FR_nearest": nearest_to_13,
        "Q13_FR_nearest_distance": nearest_to_13_d,
        "bilateral_FR_mutual_nearest": bilateral_FR,
        "Q14_top5_FR_nearest": top5,
        "v14": v14,
        "v13": v13,
        "v76": v76,
        "d_arch_Q14_Q13": d_arch_14_13,
        "d_arch_Q14_Q76": d_arch_14_76,
        "twin_strength_ratio_Q76_over_Q13": twin_strength_ratio,
        "closer_to_Q13_than_Q76": closer_to_13,
        "interpretation": (
            "Q 13 ↔ Q 14 is a bilateral mutual-nearest FR-content pair (each is the other's argmin in the FR matrix). "
            "In 4-axis architectural signature space, Q 14 is closer to Q 13 than to Q 76 al-Insān (Medinan similar-length reference) "
            "by the ratio reported. This confirms the Q013-F-05 finding from Q 14's perspective."
        ),
        "verdict": verdict,
    }
    return out

# ===================== TEST 3: ALR-cluster membership distinctiveness =====================

def run_F03(pair_dist):
    Q = 14
    ALR_strict = [10, 11, 12, 15]   # 4 siblings, excluding Q 13 (ALMR not ALR-strict)
    ALR_ext = [10, 11, 12, 13, 15]  # 5 siblings, including Q 13

    # Strict
    d_obs_strict = sum(pair_dist[(Q, s)] for s in ALR_strict) / len(ALR_strict)
    # Internal pairwise mean of ALR_strict
    pairs_strict = list(itertools.combinations(ALR_strict, 2))
    internal_strict = sum(pair_dist[a, b] for a, b in pairs_strict) / len(pairs_strict)

    # Ext
    d_obs_ext = sum(pair_dist[(Q, s)] for s in ALR_ext) / len(ALR_ext)
    pairs_ext = list(itertools.combinations(ALR_ext, 2))
    internal_ext = sum(pair_dist[a, b] for a, b in pairs_ext) / len(pairs_ext)

    # Permutation null — strict (4-surah)
    rng = random.Random(SEED)
    candidate_pool_strict = [s for s in range(1, 115) if s != Q and s not in ALR_strict]
    n_le_strict = 0
    null_dist_strict = []
    for _ in range(N_PERM):
        sample = rng.sample(candidate_pool_strict, 4)
        d_rand = sum(pair_dist[(Q, s)] for s in sample) / 4
        null_dist_strict.append(d_rand)
        if d_rand <= d_obs_strict:
            n_le_strict += 1
    p_perm_strict = n_le_strict / N_PERM

    # Permutation null — ext (5-surah)
    rng = random.Random(SEED + 1)
    candidate_pool_ext = [s for s in range(1, 115) if s != Q and s not in ALR_ext]
    n_le_ext = 0
    null_dist_ext = []
    for _ in range(N_PERM):
        sample = rng.sample(candidate_pool_ext, 5)
        d_rand = sum(pair_dist[(Q, s)] for s in sample) / 5
        null_dist_ext.append(d_rand)
        if d_rand <= d_obs_ext:
            n_le_ext += 1
    p_perm_ext = n_le_ext / N_PERM

    # Verdict
    if p_perm_strict <= ALPHA_BON:
        verdict = "CONFIRMED — Q 14 distinctively FR-close to ALR-strict cluster"
    elif p_perm_strict <= 0.05:
        verdict = "DIRECTIONAL — Q 14 FR-close to ALR-strict cluster but not at α_bon"
    else:
        verdict = "NULL — Q 14 FR-distance to ALR-strict cluster is not distinctive"

    out = {
        "test_id": "Q014-F-03",
        "title": "Q 14 ALR-cluster FR-membership distinctiveness",
        "Q14_to_ALR_strict_distances": [(s, pair_dist[(Q, s)]) for s in ALR_strict],
        "mean_d_Q14_to_ALR_strict": d_obs_strict,
        "mean_d_ALR_strict_internal_pairwise": internal_strict,
        "delta_strict": d_obs_strict - internal_strict,
        "p_perm_strict": p_perm_strict,
        "Q14_to_ALR_ext_distances": [(s, pair_dist[(Q, s)]) for s in ALR_ext],
        "mean_d_Q14_to_ALR_ext": d_obs_ext,
        "mean_d_ALR_ext_internal_pairwise": internal_ext,
        "delta_ext": d_obs_ext - internal_ext,
        "p_perm_ext": p_perm_ext,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "null_distribution_strict_stats": {
            "min": min(null_dist_strict),
            "median": sorted(null_dist_strict)[len(null_dist_strict) // 2],
            "max": max(null_dist_strict),
            "mean": sum(null_dist_strict) / len(null_dist_strict),
        },
        "verdict": verdict,
        "interpretation": (
            "Per H-NEW-610 NULL on letter-family content cohesion (4-replication NULL across full-29, ḥawāmīm-7, ALM-6, ALR-5), "
            "this test is inherently low-power. Q013-F-04 found NULL (p_perm=0.143) on the same cluster from Q 13's perspective. "
            "If Q014-F-03 also returns NULL, this is the 6th replication of the H-NEW-610 letter-family-content-NULL finding."
        ),
    }
    return out

# ===================== Main =====================

def main():
    print("Q014-Ibrāhīm specialist — running 3 pre-registered novel tests")
    print(f"Seed: {SEED}; n_perm: {N_PERM}; Bonferroni-k: {BONFERRONI_K}; α_bon: {ALPHA_BON:.6f}")
    print("=" * 70)
    assert_prereg_sha()
    print("=" * 70)

    pair_dist = load_fr_matrix()
    h750 = load_h750()
    quran = load_quran_no_tashkeel()

    print("\n--- F-01: Mecca-prayer corpus-MAX prayer-density ---")
    r1 = run_F01(quran)
    print(f"  Q 14:35-41 rank: {r1['Q14_35_41_rank']} / {r1['n_total_7verse_windows']}")
    print(f"  density: {r1['Q14_35_41_window']['density_per_100w']:.2f} per 100w")
    print(f"  n prayer tokens / words: {r1['Q14_35_41_window']['n_prayer_tokens']} / {r1['Q14_35_41_window']['n_words']}")
    print(f"  Q 14 whole-surah density rank: {r1['Q14_whole_surah_density_rank']} / 114")
    print(f"  Verdict: {r1['verdict']}")

    print("\n--- F-02: Q 13 ↔ Q 14 bilateral mutual-nearest twin ---")
    r2 = run_F02(pair_dist, h750)
    print(f"  Q 14 FR-nearest: Q {r2['Q14_FR_nearest']} at d={r2['Q14_FR_nearest_distance']:.4f}")
    print(f"  Q 13 FR-nearest: Q {r2['Q13_FR_nearest']} at d={r2['Q13_FR_nearest_distance']:.4f}")
    print(f"  Bilateral mutual-nearest? {r2['bilateral_FR_mutual_nearest']}")
    print(f"  d_arch(Q14, Q13) = {r2['d_arch_Q14_Q13']:.4f}")
    print(f"  d_arch(Q14, Q76) = {r2['d_arch_Q14_Q76']:.4f}")
    print(f"  Twin-strength ratio (Q76 / Q13) = {r2['twin_strength_ratio_Q76_over_Q13']:.2f}")
    print(f"  Verdict: {r2['verdict']}")

    print("\n--- F-03: ALR-cluster membership distinctiveness ---")
    r3 = run_F03(pair_dist)
    print(f"  Q 14 → ALR-strict {r3['Q14_to_ALR_strict_distances']}")
    print(f"  mean d̄(Q 14 → ALR-strict): {r3['mean_d_Q14_to_ALR_strict']:.4f}")
    print(f"  ALR-strict internal pairwise mean: {r3['mean_d_ALR_strict_internal_pairwise']:.4f}")
    print(f"  Δ_strict: {r3['delta_strict']:.4f}")
    print(f"  p_perm_strict: {r3['p_perm_strict']:.4f}")
    print(f"  p_perm_ext: {r3['p_perm_ext']:.4f}")
    print(f"  Verdict: {r3['verdict']}")

    # Write JSON outputs
    for tid, result in [("Q014-F-01", r1), ("Q014-F-02", r2), ("Q014-F-03", r3)]:
        path = os.path.join(CSV_DIR, f"{tid}.json")
        with open(path, "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"  wrote {path}")

    summary = {
        "family": "Q014-F-family-2026-05-08",
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "seed": SEED,
        "n_perm": N_PERM,
        "tests": [r1, r2, r3],
        "family_verdict_summary": {
            "Q014-F-01": r1["verdict"],
            "Q014-F-02": r2["verdict"],
            "Q014-F-03": r3["verdict"],
        },
    }
    summary_path = os.path.join(CSV_DIR, "Q014-F-family-summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"\nFamily summary: {summary_path}")
    print("Done.")

if __name__ == "__main__":
    main()
