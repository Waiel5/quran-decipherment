#!/usr/bin/env python3
"""
H-NEW-2460 — the minimal-surah structural class + the {Q103,Q108} rā'-twin.
Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2460-minimal-surah-class.md (SHA-256 verified at runtime).
Seed 20260509, 10000 perms (Arm C-H2 only). Stdlib only.

Arm A — {Q103,Q108} rā'-twin within the 3-verse sub-class (deterministic + 1/3 exact null, power-limited).
Arm B — rhyme-class ⊥ FR-proximity control (Q54 al-Qamar) (deterministic).
Arm C — minimal-class profile + FR-central extreme (descriptive + random-subset cohesion permutation).
"""
import json, hashlib, random, os, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2460-minimal-surah-class.md")
EXPECTED_SHA = "5eef084af1009fccb3142c8100ebc23d429b36f38981ed8efd5883a7a4b0b833"
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2460.json")
SEED = 20260509
N_PERM = 10000

ARABIC_LETTERS = set("ابتثجحخدذرزسشصضطظعغفقكلمنهوياءأإآؤئىة")


def verify_sha():
    h = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if h != EXPECTED_SHA:
        sys.exit(f"FAIL-FAST: pre-reg SHA mismatch\n expected {EXPECTED_SHA}\n got      {h}")
    return h


def letters_only(s):
    return [c for c in s if c in ARABIC_LETTERS]


def main():
    sha = verify_sha()
    qt = json.load(open(os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")))
    byid = {s["id"]: s for s in qt}

    # ---- FR matrix (1-indexed, symmetric) ----
    fr = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-111.json")))
    D = {}
    for i, j, d in fr["D_matrix_upper_triangular"]:
        D[(i, j)] = d
        D[(j, i)] = d

    def dist(a, b):
        return D[(a, b)]

    # ---- verse-finals + perfect-monorhyme census (strict last-grapheme) ----
    def finals_of(sid):
        out = []
        for v in byid[sid]["verses"]:
            toks = v["text"].split()
            lt = letters_only(toks[-1])
            out.append(lt[-1] if lt else None)
        return out

    perfect_mono = {}   # sid -> final letter, for all 114 strict-monorhyme surahs
    for s in qt:
        f = finals_of(s["id"])
        if f and len(set(f)) == 1:
            perfect_mono[s["id"]] = f[0]

    # ---- class definitions ----
    vtier = {sid: byid[sid]["total_verses"] for sid in byid}
    primary_class = sorted([sid for sid in byid if vtier[sid] <= 4])      # <=4 verses
    extended_class = sorted([sid for sid in byid if vtier[sid] <= 6])     # <=6 verses
    three_verse = sorted([sid for sid in byid if vtier[sid] == 3])        # {103,108,110}

    # ===== ARM A — {Q103,Q108} rā'-twin within the 3-verse sub-class =====
    ra_3verse = sorted([sid for sid in three_verse if perfect_mono.get(sid) == "ر"])
    A_H1 = (ra_3verse == [103, 108])
    d_103_108 = dist(103, 108)
    d_103_110 = dist(103, 110)
    d_108_110 = dist(108, 110)
    min_edge_is_103_108 = (d_103_108 < d_103_110 and d_103_108 < d_108_110)
    A_H2 = min_edge_is_103_108
    exact_null_p = 1.0 / 3.0  # honest: P(named edge = triangle minimum) under random labeling
    arm_A = "CONFIRMED" if (A_H1 and A_H2) else "NULL (pre-commit violation)"

    # mutual-nearest honesty check (NOT pre-registered as pass/fail — reported)
    nn = {}
    for s in (103, 108):
        others = [k for k in range(1, 115) if k != s]
        nn[s] = sorted(others, key=lambda k: dist(s, k))[0]
    mutually_nearest = (nn[103] == 108 and nn[108] == 103)

    # ===== ARM B — rhyme-class ⊥ FR-proximity (Q54 control) =====
    ra_corpus = sorted([sid for sid, ltr in perfect_mono.items() if ltr == "ر"])
    B_H1 = (ra_corpus == [54, 97, 103, 108])
    ra_pairs = {}
    for i, a in enumerate(ra_corpus):
        for b in ra_corpus[i + 1:]:
            ra_pairs[f"{a}-{b}"] = round(dist(a, b), 4)
    min_ra_pair = min(ra_pairs, key=ra_pairs.get)
    q54_mean_to_short = sum(dist(54, x) for x in (97, 103, 108)) / 3.0
    B_H2 = (min_ra_pair == "103-108" and q54_mean_to_short > 0.70 and d_103_108 < 0.30)
    arm_B = "CONFIRMED" if (B_H1 and B_H2) else "NULL"

    # ===== ARM C — minimal-class profile + FR-central extreme =====
    # per-surah mean FR to all 113 others, and corpus rank (ascending = most central)
    permean = {a: sum(dist(a, b) for b in range(1, 115) if b != a) / 113.0 for a in range(1, 115)}
    rank_asc = {a: r for r, a in enumerate(sorted(range(1, 115), key=lambda k: permean[k]), 1)}

    def shape_of(sid):
        first = byid[sid]["verses"][0]["text"].split()[0]
        if first == "قل":
            return "command (qul-imperative)"
        if first == "والعصر":
            return "oath (wāw-qasam)"
        if first == "إذا":
            return "conditional-temporal"
        if first in ("إنا", "انا"):
            return "declaration (innā)"
        if first.startswith("ألم"):
            return "interrogative-rebuke"
        if first.startswith("تبت"):
            return "imprecation"
        if first.startswith("لإيلاف"):
            return "causal-declaration (li-)"
        return "other"

    profile = []
    for sid in extended_class:
        f = finals_of(sid)
        profile.append({
            "surah": sid,
            "name": byid[sid]["transliteration"],
            "verses": vtier[sid],
            "type": byid[sid]["type"],
            "verse_finals": "".join(c if c else "?" for c in f),
            "perfect_monorhyme": sid in perfect_mono,
            "rhyme_letter": perfect_mono.get(sid),
            "shape": shape_of(sid),
            "mean_fr_to_all113": round(permean[sid], 4),
            "corpus_fr_central_rank": rank_asc[sid],  # 1 = most FR-central
        })

    # within-class FR matrix (extended, 11 members)
    within_matrix = {}
    within_pairs = []
    for i, a in enumerate(extended_class):
        for b in extended_class[i + 1:]:
            within_matrix[f"{a}-{b}"] = round(dist(a, b), 4)
            within_pairs.append(dist(a, b))
    within_mean = sum(within_pairs) / len(within_pairs)

    # corpus-wide pairwise mean
    corpus_pairs = [D[(i, j)] for i in range(1, 115) for j in range(i + 1, 115)]
    corpus_mean = sum(corpus_pairs) / len(corpus_pairs)

    # C-H2 clause 1: within-class mean < corpus mean
    C_H2a = within_mean < corpus_mean
    # C-H2 clause 2: majority (>=6/11) of members rank in corpus lower half (<=57)
    n_central = sum(1 for sid in extended_class if rank_asc[sid] <= 57)
    C_H2b = n_central >= 6

    # C-H2 permutation: random size-11 subset mean pairwise FR null (seed-locked)
    rng = random.Random(SEED)
    all_surahs = list(range(1, 115))
    null_means = []
    k = len(extended_class)  # 11
    for _ in range(N_PERM):
        subset = rng.sample(all_surahs, k)
        sp = [dist(subset[x], subset[y]) for x in range(k) for y in range(x + 1, k)]
        null_means.append(sum(sp) / len(sp))
    nm_mean = sum(null_means) / len(null_means)
    nm_std = (sum((v - nm_mean) ** 2 for v in null_means) / len(null_means)) ** 0.5
    n_le = sum(1 for v in null_means if v <= within_mean)
    p_perm = (n_le + 1) / (N_PERM + 1)
    z_C = (within_mean - nm_mean) / nm_std if nm_std else float("nan")
    direction_ok_C = within_mean < nm_mean

    if not direction_ok_C:
        arm_C = "NULL (pre-commit violation)"
    elif C_H2a and C_H2b and p_perm < 0.05:
        arm_C = "CONFIRMED"
    elif C_H2a and C_H2b:
        arm_C = "DIRECTIONAL"
    else:
        arm_C = "NULL"

    result = {
        "finding_id": "H-NEW-2460",
        "prereg_sha256": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "class_definition": {
            "primary_le4": primary_class,
            "extended_le6": extended_class,
            "three_verse_subclass": three_verse,
            "verse_tier_counts": dict(Counter(vtier[s] for s in extended_class)),
        },
        "arm_A_ra_twin": {
            "ra_monorhyme_3verse": ra_3verse,
            "A_H1_pair_is_103_108": A_H1,
            "d_103_108": round(d_103_108, 4),
            "d_103_110": round(d_103_110, 4),
            "d_108_110": round(d_108_110, 4),
            "min_edge_is_103_108": min_edge_is_103_108,
            "A_H2_min_edge_locked": A_H2,
            "exact_null_p_min_edge": round(exact_null_p, 4),
            "q103_fr_nn1": nn[103],
            "q108_fr_nn1": nn[108],
            "mutually_nearest": mutually_nearest,
            "power_note": "3-node class; locked-direction A-H2 carries P=1/3 exact floor. Reported as EXACT corpus fact, NOT a significant permutation result.",
            "verdict": arm_A,
        },
        "arm_B_rhyme_perp_fr": {
            "corpus_ra_monorhymes": ra_corpus,
            "B_H1_set_is_54_97_103_108": B_H1,
            "ra_pair_fr": ra_pairs,
            "min_ra_pair": min_ra_pair,
            "q54_mean_fr_to_97_103_108": round(q54_mean_to_short, 4),
            "B_H2_rhyme_not_fr_cluster": B_H2,
            "verdict": arm_B,
        },
        "arm_C_class_profile": {
            "profile": profile,
            "within_class_mean_fr": round(within_mean, 4),
            "corpus_pairwise_mean_fr": round(corpus_mean, 4),
            "C_H2a_within_lt_corpus": C_H2a,
            "n_members_fr_central_rank_le57": n_central,
            "C_H2b_majority_central": C_H2b,
            "perm_null_mean": round(nm_mean, 4),
            "perm_null_std": round(nm_std, 4),
            "z": round(z_C, 3),
            "p_perm_subset_cohesion": round(p_perm, 5),
            "direction_within_lt_null": direction_ok_C,
            "within_class_fr_matrix": within_matrix,
            "verdict": arm_C,
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
