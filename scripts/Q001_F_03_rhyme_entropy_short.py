"""
Q001-F-03 — Rhyme-entropy of Q 1 vs short-surah baseline.

Pre-reg: surahs/Q001-al-fatiha/Q001-F-03-rhyme-entropy-vs-7-verse-prereg.md
Pre-reg SHA256: 55bfd37747f5db86a1af15e854dab28eaab67563d8c3bc17c83f21c28e94fa1e
"""
import json
import hashlib
import os
import math
import random
import statistics

PROJECT = "/Users/grey/Downloads/quran"
PREREG_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/Q001-F-03-rhyme-entropy-vs-7-verse-prereg.md"
PREREG_SHA_EXPECTED = "55bfd37747f5db86a1af15e854dab28eaab67563d8c3bc17c83f21c28e94fa1e"
OUT_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/csv/Q001-F-03.json"
SEED = 14103


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    sha = sha256_file(PREREG_PATH)
    assert sha == PREREG_SHA_EXPECTED, f"SHA mismatch {sha}"

    h750 = json.load(open(f"{PROJECT}/findings/phase-b-hypotheses/csv/h-new-750.json"))
    per_surah = h750["per_surah"]

    # surah_id -> rhyme_entropy_nats and n_verses
    table = {r["surah"]: {"rh_ent": r["rhyme_entropy_nats"], "n_verses": r["n_verses"]} for r in per_surah}

    q1_ent = table[1]["rh_ent"]

    # set A: short surahs (n_verses <= 10)
    set_A = {sid: row for sid, row in table.items() if row["n_verses"] <= 10}
    set_A_ents = sorted([row["rh_ent"] for row in set_A.values()])
    set_A_others = [row["rh_ent"] for sid, row in set_A.items() if sid != 1]

    # set B: 7-verse exactly
    set_B = {sid: row for sid, row in table.items() if row["n_verses"] == 7}

    mu_A = statistics.fmean(set_A_others)
    sigma_A = statistics.pstdev(set_A_others)
    z_A = (q1_ent - mu_A) / sigma_A if sigma_A > 0 else float("nan")

    # bootstrap two-tailed p
    rng = random.Random(SEED)
    n_boot = 10000
    boot_means = []
    boot_extreme = 0
    others = list(set_A_others)
    for _ in range(n_boot):
        sample = [rng.choice(others) for _ in range(len(others))]
        bm = statistics.fmean(sample)
        boot_means.append(bm)
    # Two-tailed permutation: probability of seeing |q1 - mu| under null of being-from-A
    # We approximate by checking how many surahs in A are at least as extreme as Q1
    delta_obs = abs(q1_ent - mu_A)
    n_extreme_in_A = sum(1 for x in others if abs(x - mu_A) >= delta_obs)
    perm_p = (n_extreme_in_A + 1) / (len(others) + 1)

    out = {
        "test_id": "Q001-F-03",
        "prereg_sha": sha,
        "rules_tuple": {"tashkeel": "min-tashkeel (per H-NEW-750 pipeline)", "token": "verse-final letter", "basmala": "counted-V1"},
        "q1_rhyme_entropy_nats": q1_ent,
        "set_A_def": "n_verses <= 10",
        "set_A_size_excl_q1": len(set_A_others),
        "set_A_mean": mu_A,
        "set_A_pstd": sigma_A,
        "z_q1_in_A": z_A,
        "perm_p_two_tailed": perm_p,
        "set_B_7_verse": {str(k): v for k, v in set_B.items()},
        "ranking_in_set_A": (sorted(set_A_ents).index(q1_ent) + 1, len(set_A_ents)),
        "verdict": ("DIRECTIONAL_DISTINCT" if abs(z_A) > 1.5 else ("BORDERLINE" if abs(z_A) > 1.0 else "NULL")),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q1 rhyme entropy: {q1_ent:.4f}")
    print(f"Set A (short, n<=10) size (excl Q1): {len(set_A_others)}")
    print(f"Set A mean: {mu_A:.4f} ± {sigma_A:.4f}")
    print(f"z = {z_A:.3f}, perm_p = {perm_p:.4f}")
    print(f"7-verse surahs (set B): {set_B}")
    print(f"Verdict: {out['verdict']}")
    print(f"Output: {OUT_PATH}")


if __name__ == "__main__":
    main()
