#!/usr/bin/env python3
"""
Q026-F-07: Q 26 FR-distance to TSM sisters {Q 27, Q 28} vs Q 26 FR-distance
to ḥawāmīm cluster {Q 40-46}.

Pre-reg SHA locked: 4f15c979b511ef2604838dd31f8ab348238038609b7fb8ebb4b134f0c6695252
Pre-reg file: surahs/Q026-al-shuara/Q026-F-07-tsm-vs-hawamim-prereg.md
Seed: 20260509.

Direction-locked: mean d_FR(Q26, {Q27,Q28}) < mean d_FR(Q26, {Q40..Q46}).
This pre-reg predicts TSM-family is CLOSER than ḥawāmīm-family on the
content-axis. NULL extends the H-NEW-600 muqaṭṭaʿ-content-orthogonality
streak; PASS would be a rare PASS for muqaṭṭaʿ-content-cohesion at 3-letter
scale.

Outputs to surahs/Q026-al-shuara/csv/Q026-F-07.json
"""

import hashlib
import json
import os
import random
import sys

BASE = "/Users/grey/Downloads/quran"
SEED = 20260509
N_PERM = 10000

PREREG = os.path.join(BASE, "surahs/Q026-al-shuara/Q026-F-07-tsm-vs-hawamim-prereg.md")
EXPECTED_SHA = "4f15c979b511ef2604838dd31f8ab348238038609b7fb8ebb4b134f0c6695252"
OUT = os.path.join(BASE, "surahs/Q026-al-shuara/csv/Q026-F-07.json")

TSM_SISTERS = [27, 28]
HAWAMIM = [40, 41, 42, 43, 44, 45, 46]
ANCHOR = 26


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    actual = sha256_file(PREREG)
    if actual != EXPECTED_SHA:
        sys.stderr.write(f"SHA MISMATCH Q026-F-07: expected {EXPECTED_SHA}, got {actual}\n")
        sys.exit(2)
    print(f"[OK] Q026-F-07 pre-reg SHA verified: {actual[:16]}...")


def load_fr_matrix():
    """h-new-111.json stores D as upper-triangular sparse list of [i, j, d]
    (1-indexed). Returns a full 114x114 list-of-lists with zero diagonal."""
    path = os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-111.json")
    with open(path) as f:
        d = json.load(f)
    triples = d["D_matrix_upper_triangular"]
    m = [[0.0] * 114 for _ in range(114)]
    for entry in triples:
        i, j, val = entry[0], entry[1], entry[2]
        m[i - 1][j - 1] = val
        m[j - 1][i - 1] = val
    return m


def d(m, a, b):
    """1-indexed Fisher-Rao distance lookup."""
    return m[a - 1][b - 1]


def main():
    verify_prereg()
    rng = random.Random(SEED)
    m = load_fr_matrix()

    # Observed
    d_tsm_list = [d(m, ANCHOR, k) for k in TSM_SISTERS]
    d_hm_list = [d(m, ANCHOR, k) for k in HAWAMIM]
    d_tsm = sum(d_tsm_list) / len(d_tsm_list)
    d_hm = sum(d_hm_list) / len(d_hm_list)
    delta_obs = d_tsm - d_hm

    # Null: random pair + random 7-tuple from {1..114} \ {26}
    candidates = [s for s in range(1, 115) if s != ANCHOR]
    null_delta = []
    for _ in range(N_PERM):
        pair = rng.sample(candidates, 2)
        sept_pool = [s for s in candidates if s not in pair]
        sept = rng.sample(sept_pool, 7)
        d_p = sum(d(m, ANCHOR, k) for k in pair) / 2.0
        d_s = sum(d(m, ANCHOR, k) for k in sept) / 7.0
        null_delta.append(d_p - d_s)

    null_mean = sum(null_delta) / N_PERM
    null_sd = (sum((x - null_mean) ** 2 for x in null_delta) / N_PERM) ** 0.5
    # one-sided lower-tail p
    p_perm = sum(1 for x in null_delta if x <= delta_obs) / N_PERM

    direction_passed = (delta_obs < 0)  # pre-committed: TSM closer than HM
    pass_criterion = (delta_obs < 0 and p_perm < 0.025)
    if not direction_passed:
        verdict = (f"PRE-COMMIT VIOLATION / FALSIFIED: Δ = d_TSM - d_HM = {delta_obs:+.4f} > 0 "
                   f"(TSM-family is FURTHER than ḥawāmīm-family). Extends H-NEW-600 NULL streak.")
    elif pass_criterion:
        verdict = (f"CONFIRMED: d_TSM={d_tsm:.4f} < d_HM={d_hm:.4f}, Δ={delta_obs:+.4f}, p_perm={p_perm:.4f} < 0.025")
    else:
        verdict = (f"NULL: Δ_obs={delta_obs:+.4f}, direction passed but p_perm={p_perm:.4f} ≥ 0.025")

    result = {
        "test_id": "Q026-F-07",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "anchor": ANCHOR,
        "tsm_sisters": TSM_SISTERS,
        "hawamim": HAWAMIM,
        "d_FR_Q26_to_Q27": d(m, ANCHOR, 27),
        "d_FR_Q26_to_Q28": d(m, ANCHOR, 28),
        "d_FR_Q26_to_hawamim_individual": {f"Q{k}": d(m, ANCHOR, k) for k in HAWAMIM},
        "mean_d_TSM": d_tsm,
        "mean_d_HM": d_hm,
        "delta_obs": delta_obs,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "p_perm_one_sided_lower": p_perm,
        "alpha_bonferroni": 0.025,
        "direction_passed": direction_passed,
        "pass_criterion_met": pass_criterion,
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
