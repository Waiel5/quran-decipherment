"""
Q045-F-03: HM-B sub-block FR-roots cohesion vs HM-A; Q 45 leave-one-out role.

Pre-reg SHA256: 70a5d56912f1c9421faefa9cd3f07eabaa49f1e79250598efe16882f7939de40
Pre-reg path: surahs/Q045-al-jathiyah/preregs/Q045-F-03-hmb-vs-hma-cohesion-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys
import random

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/preregs/Q045-F-03-hmb-vs-hma-cohesion-prereg.md"
EXPECTED_SHA = "70a5d56912f1c9421faefa9cd3f07eabaa49f1e79250598efe16882f7939de40"
H_NEW_111_PATH = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q045-al-jathiyah/csv/Q045-F-03.json"

HM_A = [40, 41, 42]
HM_B = [43, 44, 45, 46]
HM_B_NO_45 = [43, 44, 46]
N_PERM = 10000
SEED = 20260428


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def load_fr_matrix():
    with open(H_NEW_111_PATH) as f:
        d = json.load(f)
    fr = {}
    for entry in d["D_matrix_upper_triangular"]:
        i, j, dist = entry[0], entry[1], entry[2]
        fr[(i, j)] = dist
        fr[(j, i)] = dist
    return fr


def mean_pair(group, fr):
    pairs = []
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            a, b = group[i], group[j]
            pairs.append(fr[(a, b)])
    return sum(pairs) / len(pairs) if pairs else None, pairs


def perm_null(size, fr, n_perm, seed):
    rng = random.Random(seed)
    surahs = list(range(1, 115))
    out = []
    for _ in range(n_perm):
        sample = rng.sample(surahs, size)
        m, _ = mean_pair(sample, fr)
        out.append(m)
    return out


def main():
    verify_prereg()
    fr = load_fr_matrix()

    d_hma, pairs_hma = mean_pair(HM_A, fr)
    d_hmb, pairs_hmb = mean_pair(HM_B, fr)
    d_hmb_no45, pairs_hmb_no45 = mean_pair(HM_B_NO_45, fr)

    # Permutation null distributions
    null_3 = perm_null(3, fr, N_PERM, SEED)
    null_4 = perm_null(4, fr, N_PERM, SEED + 1)

    pct_hma = sum(1 for x in null_3 if x <= d_hma) / N_PERM * 100
    pct_hmb = sum(1 for x in null_4 if x <= d_hmb) / N_PERM * 100
    pct_hmb_no45 = sum(1 for x in null_3 if x <= d_hmb_no45) / N_PERM * 100

    # H1: HM-A < HM-B?
    h1_dir_ok = d_hma < d_hmb
    p_perm_h1 = pct_hma / 100  # one-sided cohesion-tighter is left-tail in null distribution
    h1_pass = h1_dir_ok and p_perm_h1 < 0.025

    # H1b: HM-B-no-45 > HM-B (i.e., removing Q 45 loosens)?
    h1b_dir_ok = d_hmb_no45 > d_hmb

    if h1_pass and h1b_dir_ok:
        verdict = "VINDICATED"
    elif h1_dir_ok and h1b_dir_ok:
        verdict = "DIRECTIONAL"
    elif not h1_dir_ok:
        verdict = "PRECOMMIT_VIOLATION_H1"
    elif not h1b_dir_ok:
        verdict = "PRECOMMIT_VIOLATION_H1b"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q045-F-03",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-token, FR-roots-QAC-stem, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "hm_a": HM_A,
        "hm_b": HM_B,
        "hm_b_no_45": HM_B_NO_45,
        "d_hm_a": round(d_hma, 6),
        "d_hm_b": round(d_hmb, 6),
        "d_hm_b_no_45": round(d_hmb_no45, 6),
        "pairs_hm_a": [round(x, 6) for x in pairs_hma],
        "pairs_hm_b": [round(x, 6) for x in pairs_hmb],
        "pairs_hm_b_no_45": [round(x, 6) for x in pairs_hmb_no45],
        "null_3_mean": round(sum(null_3) / len(null_3), 6),
        "null_4_mean": round(sum(null_4) / len(null_4), 6),
        "pct_hm_a_in_null3": round(pct_hma, 4),
        "pct_hm_b_in_null4": round(pct_hmb, 4),
        "pct_hm_b_no_45_in_null3": round(pct_hmb_no45, 4),
        "h1_direction_ok": h1_dir_ok,
        "h1_p_perm": round(p_perm_h1, 6),
        "h1_pass": h1_pass,
        "h1b_direction_ok": h1b_dir_ok,
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
