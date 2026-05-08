#!/usr/bin/env python3
"""
Q007-al-Araf — pre-registered novel-finding tests F-01..F-05.

SHA-locked at runtime; fail-fast on any pre-reg drift.
Stdlib only. Seed 20260507. 10,000 perms.

Outputs JSON per-test to /Users/grey/Downloads/quran/surahs/Q007-al-araf/csv/Q007-F-NN.json
and a journal trace to JOURNAL.md (appended).
"""

import json
import math
import os
import random
import re
import hashlib
from collections import Counter, defaultdict

# ---------- LOCKED PRE-REG SHAS ----------
PREREG_DIR = "/Users/grey/Downloads/quran/surahs/Q007-al-araf"
EXPECTED_SHAS = {
    "Q007-F-01-prophet-cycle-parallelism-prereg.md":
        "03a92d7d12b85c5739f4bde19e80b0c12b5a6d56a32f2d3603f85e89dc616f9c",
    "Q007-F-02-mim-sad-cluster-position-prereg.md":
        "e46a503f8ebed24d911fbf0d9dd4d57c5ee997dcd5ea03396809ecaee5d65eb6",
    "Q007-F-03-araf-hapax-prereg.md":
        "ade0c117904d2f49f68937b8df1ca08b955b06b043778a398deb826613faa180",
    "Q007-F-04-adam-twin-prereg.md":
        "23e40a3b2f9b4414fb26edd1bd887a5a84facfda434b0b4c7624b7ed769cb58e",
    "Q007-F-05-prophet-order-primary-prereg.md":
        "370244294d4e82b2cb4576de8712d0dd804973572ad0463e1b993fdd90bad098",
}

SEED = 20260507
N_PERM = 10000

QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
ROOT_INDEX = "/Users/grey/Downloads/quran/data/morphology/root-index.json"
H_NEW_111 = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUTDIR = os.path.join(PREREG_DIR, "csv")
JOURNAL = os.path.join(PREREG_DIR, "JOURNAL.md")

os.makedirs(OUTDIR, exist_ok=True)


def sha256_file(path):
    with open(path, "rb") as fp:
        return hashlib.sha256(fp.read()).hexdigest()


def verify_pre_regs():
    print("=== SHA verification ===")
    failed = []
    for fname, expected in EXPECTED_SHAS.items():
        actual = sha256_file(os.path.join(PREREG_DIR, fname))
        ok = (actual == expected)
        marker = "OK" if ok else "FAIL"
        print(f"  {marker}  {fname}  {actual}")
        if not ok:
            failed.append((fname, expected, actual))
    if failed:
        raise SystemExit(f"PRE-REG SHA MISMATCH — fail-fast. {failed}")
    return True


# ---------- DATA LOADING ----------

def load_quran():
    with open(QURAN_NO_TASHKEEL) as fp:
        q = json.load(fp)
    # q is a list of 114 surah dicts
    return q


def load_roots_per_verse():
    with open(ROOT_INDEX) as fp:
        ri = json.load(fp)
    # build (s,v) -> list[root]
    vroots = defaultdict(list)
    for r, occs in ri.items():
        for occ in occs:
            s, v, w = occ
            vroots[(s, v)].append(r)
    return vroots, ri


def load_fr_matrix():
    with open(H_NEW_111) as fp:
        d = json.load(fp)
    mat_list = d["D_matrix_upper_triangular"]
    N = 114
    D = [[0.0] * N for _ in range(N)]
    for i, j, v in mat_list:
        D[i - 1][j - 1] = v
        D[j - 1][i - 1] = v
    return D


# ---------- F-01: Prophet-cycle parallelism via 4-feature vectors ----------

# Block boundaries — locked from pre-reg
Q7_BLOCKS = {
    "Adam":    (7, 11, 25),
    "Nuh":     (7, 59, 64),
    "Hud":     (7, 65, 72),
    "Salih":   (7, 73, 79),
    "Lut":     (7, 80, 84),
    "Shuayb":  (7, 85, 93),
    "Musa":    (7, 103, 137),
}
Q7_ORDER = ["Adam", "Nuh", "Hud", "Salih", "Lut", "Shuayb", "Musa"]

Q11_BLOCKS = {
    "Nuh":    (11, 25, 48),
    "Hud":    (11, 50, 60),
    "Salih":  (11, 61, 68),
    "Lut":    (11, 69, 83),
    "Shuayb": (11, 84, 95),
}
Q11_ORDER = ["Nuh", "Hud", "Salih", "Lut", "Shuayb"]

Q26_BLOCKS = {
    "Musa":    (26, 10, 68),
    "Ibrahim": (26, 69, 104),
    "Nuh":     (26, 105, 122),
    "Hud":     (26, 123, 140),
    "Salih":   (26, 141, 159),
    "Lut":     (26, 160, 175),
    "Shuayb":  (26, 176, 191),
}
Q26_ORDER = ["Musa", "Ibrahim", "Nuh", "Hud", "Salih", "Lut", "Shuayb"]

Q21_BLOCKS = {
    "MusaHarun":  (21, 48, 50),
    "Ibrahim":    (21, 51, 73),
    "Lut":        (21, 74, 75),
    "Nuh":        (21, 76, 77),
    "DawudSulay": (21, 78, 82),
    "Ayyub":      (21, 83, 84),
    "Ismail":     (21, 85, 86),
}
Q21_ORDER = ["MusaHarun", "Ibrahim", "Lut", "Nuh", "DawudSulay", "Ayyub", "Ismail"]


def text_of_block(qtext_list, surah_idx_zero, v_start, v_end):
    """Concat raw verse-texts for [v_start, v_end] inclusive."""
    s = qtext_list[surah_idx_zero - 1]  # 1-indexed surah -> 0-indexed list
    out = []
    for v in s["verses"]:
        if v_start <= v["id"] <= v_end:
            out.append(v["text"])
    return " ".join(out)


def roots_of_block(vroots, surah, v_start, v_end):
    out = []
    for v in range(v_start, v_end + 1):
        out.extend(vroots.get((surah, v), []))
    return out


def f1_introductory_formula(text):
    """F1: 'wa-ila [tribe] akhahum' OR 'laqad arsalna' OR 'idh qala' OR
    'wa-X idh qala'"""
    p = [
        r"وإلى\s+\w+\s+أخا",
        r"لقد\s+أرسلنا",
        r"إذ\s+قال",
        r"\bأرسلنا\b",
        r"بعثنا",
        r"\bو\w+ا\s+إذ\s+قال",
        r"^وإذ\s+قال",
    ]
    for pat in p:
        if re.search(pat, text):
            return 1
    return 0


def f2_miracle_sign(text, root_list):
    """F2: presence of bayyina (byn) AND/OR named miracle root."""
    miracle_roots = {"byn", "Ayy", "rsl", "ESw", "nwq", "swA", "qAlb"}
    if any(r in miracle_roots for r in root_list):
        return 1
    if re.search(r"بينة|آيات|آية|ناقة|عصاه", text):
        return 1
    return 0


def f3_opposition(text, root_list):
    """F3: opposition narrative: 'qala al-malau', 'qalu', kfr/k*b/Aly roots."""
    opp_roots = {"kfr", "k*b", "AlA"}
    if any(r in opp_roots for r in root_list):
        return 1
    if re.search(r"قال\s+الملأ|قالوا\s+(يا|إنا|ما)|كذبو", text):
        return 1
    return 0


def f4_destruction(text, root_list):
    """F4: destruction-event verb."""
    destruct_roots = {"grq", "rjf", "mTr", "hlk", "Ax*", "njw", "njy", "Ahl",
                      "qDD", "rwH", "ESf", "*xx", "wqE"}
    if any(r in destruct_roots for r in root_list):
        return 1
    if re.search(r"أغرقن|الرجفة|أمطرن|أهلكن|أنجين|دمرنا|عذاب|الطوفان", text):
        return 1
    return 0


def feature_vector_for_block(qtext_list, vroots, surah, v_start, v_end):
    text = text_of_block(qtext_list, surah, v_start, v_end)
    root_list = roots_of_block(vroots, surah, v_start, v_end)
    return [
        f1_introductory_formula(text),
        f2_miracle_sign(text, root_list),
        f3_opposition(text, root_list),
        f4_destruction(text, root_list),
    ]


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def mean_pairwise_sim(vectors):
    n = len(vectors)
    if n < 2:
        return 0.0
    sims = []
    L = len(vectors[0])
    for i in range(n):
        for j in range(i + 1, n):
            s = (L - hamming(vectors[i], vectors[j])) / L
            sims.append(s)
    return sum(sims) / len(sims)


def run_F01(qtext_list, vroots):
    print("\n=== Q007-F-01: Prophet-cycle parallelism ===")
    rng = random.Random(SEED)

    def vectors_for(blocks, order):
        return [
            feature_vector_for_block(qtext_list, vroots, *blocks[name])
            for name in order
        ]

    v_q7 = vectors_for(Q7_BLOCKS, Q7_ORDER)
    v_q11 = vectors_for(Q11_BLOCKS, Q11_ORDER)
    v_q26 = vectors_for(Q26_BLOCKS, Q26_ORDER)
    v_q21 = vectors_for(Q21_BLOCKS, Q21_ORDER)

    s_q7 = mean_pairwise_sim(v_q7)
    s_q11 = mean_pairwise_sim(v_q11)
    s_q26 = mean_pairwise_sim(v_q26)
    s_q21 = mean_pairwise_sim(v_q21)

    print("Q7 prophet feature vectors:")
    for n, v in zip(Q7_ORDER, v_q7):
        print(f"  {n:8s}: {v}")
    print(f"Q7 mean S = {s_q7:.4f}")
    print(f"Q11 mean S = {s_q11:.4f}")
    print(f"Q26 mean S = {s_q26:.4f}")
    print(f"Q21 mean S = {s_q21:.4f}")

    # Permutation null on Q7: shuffle the assignment of feature-vectors among prophet
    # positions. This preserves marginals (which 4-feature combos exist) and tests
    # whether the OBSERVED arrangement is special.
    null_count_ge = 0
    for _ in range(N_PERM):
        perm = list(v_q7)
        rng.shuffle(perm)
        s = mean_pairwise_sim(perm)
        # Note: pairwise mean is INVARIANT to permutation — this null is degenerate.
        # We instead use a *vocabulary-permutation* null: randomly flip each bit
        # under marginal-preserving sampling. (Documented in honest-limits.)
        # Marginal-preserving Bernoulli null on the 4 features:
        # For each feature j, count of 1s in observed Q7 (m_j) of n=7 blocks;
        # randomly assign m_j 1s to 7 positions; recompute S.
        if False:  # left for clarity
            pass
        if s >= s_q7:
            null_count_ge += 1
    # Instead use marginal-preserving per-feature null
    rng2 = random.Random(SEED)
    L = 4
    n = len(v_q7)
    marginals = [sum(v[j] for v in v_q7) for j in range(L)]
    null_S = []
    for _ in range(N_PERM):
        new_vs = [[0] * L for _ in range(n)]
        for j in range(L):
            positions = list(range(n))
            rng2.shuffle(positions)
            for k in range(marginals[j]):
                new_vs[positions[k]][j] = 1
        null_S.append(mean_pairwise_sim(new_vs))
    p_perm = sum(1 for x in null_S if x >= s_q7) / N_PERM

    # Bonferroni-3 outer comparison vs Q11/Q26/Q21 — rank Q7 among 4
    surah_means = [("Q7", s_q7), ("Q11", s_q11), ("Q26", s_q26), ("Q21", s_q21)]
    surah_means.sort(key=lambda x: -x[1])
    q7_rank = next(i for i, t in enumerate(surah_means) if t[0] == "Q7") + 1

    print(f"p_perm (marginal-preserving null) = {p_perm:.4f}")
    print(f"Q7 rank in {{Q7, Q11, Q26, Q21}} = {q7_rank}/4")
    print("Sorted by mean S:", surah_means)

    result = {
        "id": "Q007-F-01",
        "prereg_sha_expected": EXPECTED_SHAS["Q007-F-01-prophet-cycle-parallelism-prereg.md"],
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": 0.0125,
        "Q7_feature_vectors": {n: v for n, v in zip(Q7_ORDER, v_q7)},
        "Q11_feature_vectors": {n: v for n, v in zip(Q11_ORDER, v_q11)},
        "Q26_feature_vectors": {n: v for n, v in zip(Q26_ORDER, v_q26)},
        "Q21_feature_vectors": {n: v for n, v in zip(Q21_ORDER, v_q21)},
        "Q7_mean_pairwise_S": s_q7,
        "Q11_mean_pairwise_S": s_q11,
        "Q26_mean_pairwise_S": s_q26,
        "Q21_mean_pairwise_S": s_q21,
        "Q7_rank_4": q7_rank,
        "p_perm_marginal_preserving": p_perm,
        "ranking": surah_means,
    }

    if q7_rank == 1 and p_perm <= 0.0125:
        result["verdict"] = "CONFIRMED"
    elif q7_rank == 1 or p_perm <= 0.05:
        result["verdict"] = "DIRECTIONAL"
    elif q7_rank >= 3:
        result["verdict"] = "NULL"
    else:
        result["verdict"] = "INCONCLUSIVE"
    print(f"VERDICT: {result['verdict']}")
    return result


# ---------- F-02: المص cluster-position ----------

ALM_SET = [2, 3, 29, 30, 31, 32]   # ALM-6
ALR_SET = [10, 11, 12, 14, 15]     # ALR-5
MUQ_29 = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
          36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]


def run_F02(D):
    print("\n=== Q007-F-02: المص cluster position ===")
    rng = random.Random(SEED + 2)

    def cent_dist(target, group):
        vals = [D[target - 1][g - 1] for g in group if g != target]
        return sum(vals) / len(vals)

    d_alm = cent_dist(7, ALM_SET)
    d_alr = cent_dist(7, ALR_SET)
    combined = (d_alm + d_alr) / 2.0

    # rank Q7's combined among 114
    combined_all = []
    for s in range(1, 115):
        a = cent_dist(s, ALM_SET)
        b = cent_dist(s, ALR_SET)
        combined_all.append((s, (a + b) / 2.0, a, b))
    combined_all_sorted = sorted(combined_all, key=lambda x: x[1])
    q7_rank = next(i for i, x in enumerate(combined_all_sorted) if x[0] == 7) + 1

    print(f"Q7 d(ALM-cent) = {d_alm:.4f}")
    print(f"Q7 d(ALR-cent) = {d_alr:.4f}")
    print(f"Q7 combined    = {combined:.4f}")
    print(f"Q7 |d_ALM - d_ALR| = {abs(d_alm - d_alr):.4f}")
    print(f"Q7 rank on combined = {q7_rank}/114")
    print(f"Top-10 closest to mid-ALM-ALR: {combined_all_sorted[:10]}")

    # Permutation null: random 11-surah subsets of muqaṭṭaʿ-29
    null_ranks = []
    for _ in range(N_PERM):
        subset = rng.sample(MUQ_29, 11)
        a = cent_dist(7, subset)
        # split into two random halves
        half_a = subset[:6]
        half_b = subset[6:]
        d_a = cent_dist(7, half_a)
        d_b = cent_dist(7, half_b)
        c_q7 = (d_a + d_b) / 2.0
        # rank vs all 114 using same split-cluster approach:
        ranks_under = sum(1 for s in range(1, 115) if s != 7 and (
            (cent_dist(s, half_a) + cent_dist(s, half_b)) / 2.0 < c_q7
        ))
        null_ranks.append(ranks_under + 1)
    p_perm_top15 = sum(1 for r in null_ranks if r <= 15) / N_PERM
    p_perm_observed = sum(1 for r in null_ranks if r <= q7_rank) / N_PERM

    result = {
        "id": "Q007-F-02",
        "prereg_sha_expected": EXPECTED_SHAS["Q007-F-02-mim-sad-cluster-position-prereg.md"],
        "seed": SEED + 2,
        "n_perm": N_PERM,
        "alpha_bon": 0.0125,
        "d_ALM_centroid": d_alm,
        "d_ALR_centroid": d_alr,
        "combined": combined,
        "abs_diff_ALM_minus_ALR": abs(d_alm - d_alr),
        "Q7_rank_on_combined": q7_rank,
        "top10_combined": [
            {"surah": s, "combined": c, "d_alm": a, "d_alr": b}
            for (s, c, a, b) in combined_all_sorted[:10]
        ],
        "p_perm_random_split_observed_or_better": p_perm_observed,
        "p_perm_random_subsets_top15_baseline": p_perm_top15,
    }

    # Verdict
    is_top15 = q7_rank <= 15
    is_equidistant = abs(d_alm - d_alr) <= 0.10
    if is_top15 and is_equidistant and p_perm_observed <= 0.0125:
        result["verdict"] = "CONFIRMED"
    elif (is_top15 and is_equidistant) or p_perm_observed <= 0.05:
        result["verdict"] = "DIRECTIONAL"
    elif q7_rank > 100:
        result["verdict"] = "PRE-COMMIT-VIOLATION"
    else:
        result["verdict"] = "NULL"

    # Honest direction-of-effect note
    closer_to = "ALM" if d_alm < d_alr else ("ALR" if d_alr < d_alm else "TIE")
    result["closer_to"] = closer_to
    print(f"Q7 closer to: {closer_to} (gap={abs(d_alm-d_alr):.4f})")
    print(f"VERDICT: {result['verdict']}")
    return result


# ---------- F-03: aʿrāf-hapax ----------

def run_F03(qtext_list):
    print("\n=== Q007-F-03: aʿrāf-hapax ===")
    n_orth = 0
    n_q7 = 0
    locations = []
    for s in qtext_list:
        for v in s["verses"]:
            if "الأعراف" in v["text"]:
                n_orth += 1
                locations.append((s["id"], v["id"], v["text"][:120]))
                if s["id"] == 7:
                    n_q7 += 1

    # 'aṣḥāb al-aʿrāf' check
    n_ashab = 0
    for s in qtext_list:
        for v in s["verses"]:
            if "أصحاب الأعراف" in v["text"]:
                n_ashab += 1

    # analytic null: probability that 2 token-occurrences both fall in same surah
    # under length-weighted random allocation
    surah_word_counts = []
    total_words = 0
    for s in qtext_list:
        sw = sum(len(v["text"].split()) for v in s["verses"])
        surah_word_counts.append(sw)
        total_words += sw
    p_q7 = surah_word_counts[6] / total_words
    # P(both 2 tokens in same surah) = sum_s p_s^2 ; P(both in Q7) = p_q7^2
    p_both_same = sum(p ** 2 for p in (sw / total_words for sw in surah_word_counts))
    p_both_q7 = p_q7 ** 2

    print(f"n_orthographic 'الأعراف': {n_orth}")
    print(f"n_Q7: {n_q7}")
    print(f"locations: {locations}")
    print(f"n 'أصحاب الأعراف': {n_ashab}")
    print(f"analytic null P(both in same surah | length-weighted) = {p_both_same:.6f}")
    print(f"analytic null P(both in Q7) = {p_both_q7:.6f}")

    surah_unique = (n_orth == n_q7)
    is_hapax_2 = (n_orth <= 2)
    confirmed = surah_unique and is_hapax_2 and p_both_q7 <= 0.0125
    result = {
        "id": "Q007-F-03",
        "prereg_sha_expected": EXPECTED_SHAS["Q007-F-03-araf-hapax-prereg.md"],
        "n_orthographic_alaaraaf": n_orth,
        "n_Q7": n_q7,
        "n_ashab_alaaraaf": n_ashab,
        "locations": locations,
        "surah_unique": surah_unique,
        "is_hapax_2_or_less": is_hapax_2,
        "analytic_null_p_both_same_surah": p_both_same,
        "analytic_null_p_both_in_Q7": p_both_q7,
    }
    if confirmed:
        result["verdict"] = "CONFIRMED"
    elif surah_unique:
        result["verdict"] = "DIRECTIONAL"
    else:
        result["verdict"] = "NULL"
    print(f"VERDICT: {result['verdict']}")
    return result


# ---------- F-04: Adam-twin ----------

def block_root_tf(vroots, surah, v_start, v_end):
    bag = Counter()
    for v in range(v_start, v_end + 1):
        for r in vroots.get((surah, v), []):
            bag[r] += 1
    return bag


def cosine_distance(c1, c2):
    keys = set(c1) | set(c2)
    dot = sum(c1[k] * c2[k] for k in keys)
    n1 = math.sqrt(sum(v * v for v in c1.values()))
    n2 = math.sqrt(sum(v * v for v in c2.values()))
    if n1 == 0 or n2 == 0:
        return 1.0
    return 1.0 - dot / (n1 * n2)


def run_F04(vroots):
    print("\n=== Q007-F-04: Adam-twin ===")
    rng = random.Random(SEED + 4)
    Q7_adam = block_root_tf(vroots, 7, 11, 25)
    Q2_adam = block_root_tf(vroots, 2, 30, 39)
    Q20_adam = block_root_tf(vroots, 20, 115, 126)

    d_7_2 = cosine_distance(Q7_adam, Q2_adam)
    d_7_20 = cosine_distance(Q7_adam, Q20_adam)
    d_2_20 = cosine_distance(Q2_adam, Q20_adam)
    margin = min(d_7_20, d_2_20) - d_7_2

    n_q7 = sum(Q7_adam.values())
    n_q2 = sum(Q2_adam.values())
    n_q20 = sum(Q20_adam.values())

    print(f"Q7-Adam tokens: {n_q7}")
    print(f"Q2-Adam tokens: {n_q2}")
    print(f"Q20-Adam tokens: {n_q20}")
    print(f"d(Q7-Adam, Q2-Adam)  = {d_7_2:.4f}")
    print(f"d(Q7-Adam, Q20-Adam) = {d_7_20:.4f}")
    print(f"d(Q2-Adam, Q20-Adam) = {d_2_20:.4f}")
    print(f"margin = min(d(7,20),d(2,20)) - d(7,2) = {margin:.4f}")

    # Permutation null: pool the union vocabulary, randomly partition into 3
    # blocks preserving sizes
    union = Q7_adam + Q2_adam + Q20_adam
    flat_tokens = []
    for r, c in union.items():
        flat_tokens.extend([r] * c)
    n_total = len(flat_tokens)
    null_margins = []
    for _ in range(N_PERM):
        rng.shuffle(flat_tokens)
        b1 = Counter(flat_tokens[:n_q7])
        b2 = Counter(flat_tokens[n_q7:n_q7 + n_q2])
        b3 = Counter(flat_tokens[n_q7 + n_q2:])
        d12 = cosine_distance(b1, b2)
        d13 = cosine_distance(b1, b3)
        d23 = cosine_distance(b2, b3)
        m = min(d13, d23) - d12
        null_margins.append(m)
    p_perm = sum(1 for m in null_margins if m >= margin) / N_PERM

    result = {
        "id": "Q007-F-04",
        "prereg_sha_expected": EXPECTED_SHAS["Q007-F-04-adam-twin-prereg.md"],
        "seed": SEED + 4,
        "n_perm": N_PERM,
        "alpha_bon": 0.0125,
        "Q7_Adam_tokens": n_q7,
        "Q2_Adam_tokens": n_q2,
        "Q20_Adam_tokens": n_q20,
        "d_Q7_Q2": d_7_2,
        "d_Q7_Q20": d_7_20,
        "d_Q2_Q20": d_2_20,
        "margin": margin,
        "p_perm_one_sided": p_perm,
    }
    if margin > 0 and p_perm <= 0.0125:
        result["verdict"] = "CONFIRMED"
    elif margin > 0 and p_perm <= 0.05:
        result["verdict"] = "DIRECTIONAL"
    elif margin < 0 and p_perm >= 0.95:
        result["verdict"] = "PRE-COMMIT-VIOLATION"
    else:
        result["verdict"] = "NULL"
    print(f"p_perm (one-sided upper-tail) = {p_perm:.4f}")
    print(f"VERDICT: {result['verdict']}")
    return result


# ---------- F-05: Q 7 prophet-order primary ----------

# H-NEW-940 catalog (locked)
H940_ORDER_Q7 = ["Adam", "Nuh", "Hud", "Salih", "Lut", "Shuayb", "Musa", "Harun"]
H940_ORDER_Q11 = ["Musa", "Nuh", "Hud", "Salih", "Ibrahim", "Lut", "Ishaq",
                  "Yaqub", "Shuayb"]
H940_ORDER_Q26 = ["Musa", "Harun", "Ibrahim", "Nuh", "Hud", "Salih", "Lut",
                  "Shuayb"]
H940_ORDER_Q21 = ["Musa", "Harun", "Ibrahim", "Lut", "Ishaq", "Yaqub", "Nuh",
                  "Dawud", "Sulayman", "Ayyub", "Ismail", "Idris", "Kifl",
                  "Zakariya", "Yahya"]


def kendall_tau(a, b):
    """Kendall-τ on two orderings of the same set."""
    common = [x for x in a if x in b]
    rank_a = {x: i for i, x in enumerate([x for x in a if x in b])}
    rank_b = {x: i for i, x in enumerate([x for x in b if x in a])}
    if len(common) < 2:
        return None
    n = len(common)
    concordant = 0
    discordant = 0
    for i in range(n):
        for j in range(i + 1, n):
            x, y = common[i], common[j]
            ra_i, ra_j = rank_a[x], rank_a[y]
            rb_i, rb_j = rank_b[x], rank_b[y]
            if (ra_i - ra_j) * (rb_i - rb_j) > 0:
                concordant += 1
            elif (ra_i - ra_j) * (rb_i - rb_j) < 0:
                discordant += 1
    pairs = n * (n - 1) // 2
    return (concordant - discordant) / pairs if pairs else None


def run_F05():
    print("\n=== Q007-F-05: Q7 prophet-order primary ===")
    rng = random.Random(SEED + 5)
    q7set = set(H940_ORDER_Q7)

    targets = {"Q11": H940_ORDER_Q11, "Q26": H940_ORDER_Q26, "Q21": H940_ORDER_Q21}
    results_per = {}
    for name, order in targets.items():
        restricted = [x for x in order if x in q7set]
        # Q7 restricted to intersection with this surah's set
        intersection_set = set(restricted)
        q7_restricted = [x for x in H940_ORDER_Q7 if x in intersection_set]
        tau = kendall_tau(q7_restricted, restricted)

        n = len(restricted)
        # null: shuffle restricted ordering, recompute tau
        if n >= 2:
            null_geq = 0
            for _ in range(N_PERM):
                shuffled = list(restricted)
                rng.shuffle(shuffled)
                t = kendall_tau(q7_restricted, shuffled)
                if t is not None and t >= tau:
                    null_geq += 1
            p_perm = null_geq / N_PERM
        else:
            p_perm = None
        results_per[name] = {
            "intersection_size": n,
            "Q7_restricted": q7_restricted,
            "target_restricted": restricted,
            "tau": tau,
            "p_perm": p_perm,
        }
        print(f"  {name}: intersection_size={n}, tau={tau}, p_perm={p_perm}")

    n_passing = sum(
        1 for v in results_per.values()
        if v["tau"] == 1.0 and v["p_perm"] is not None and v["p_perm"] <= 0.01
    )
    if n_passing == 3:
        verdict = "PRIMARY-CONFIRMED"
    elif n_passing == 2:
        verdict = "PARTIAL-PRIMARY"
    else:
        verdict = "NULL"
    print(f"n_passing = {n_passing}/3 -> VERDICT: {verdict}")
    return {
        "id": "Q007-F-05",
        "prereg_sha_expected": EXPECTED_SHAS["Q007-F-05-prophet-order-primary-prereg.md"],
        "seed": SEED + 5,
        "n_perm": N_PERM,
        "alpha_bon": 0.01,
        "Q7_full_order": H940_ORDER_Q7,
        "per_surah": results_per,
        "n_passing": n_passing,
        "verdict": verdict,
    }


# ---------- MAIN ----------

def main():
    verify_pre_regs()

    qtext_list = load_quran()
    vroots, ri = load_roots_per_verse()
    D = load_fr_matrix()

    out = {}
    out["F01"] = run_F01(qtext_list, vroots)
    out["F02"] = run_F02(D)
    out["F03"] = run_F03(qtext_list)
    out["F04"] = run_F04(vroots)
    out["F05"] = run_F05()

    for k, v in out.items():
        with open(os.path.join(OUTDIR, f"Q007-F-{k[1:]}.json"), "w") as fp:
            json.dump(v, fp, indent=2, ensure_ascii=False)

    # Append journal trace
    with open(JOURNAL, "a") as fp:
        fp.write("\n\n## Run trace 2026-05-07 — Q007 F-01..F-05\n")
        for k, v in out.items():
            fp.write(f"\n- {v['id']}: verdict={v.get('verdict','?')}\n")
            fp.write(f"  - SHA expected: {v.get('prereg_sha_expected','?')}\n")

    print("\n\n=== SUMMARY ===")
    for k, v in out.items():
        print(f"  {v['id']}: {v.get('verdict','?')}")


if __name__ == "__main__":
    main()
