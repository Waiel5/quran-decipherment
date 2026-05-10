#!/usr/bin/env python3
"""
Q032-F-05 — Friday-fajr (Bukhārī #870/#1037) + al-Munjiya nightly (Tirmidhī #2975) pair audit.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q032-al-sajda/Q032-F-05-friday-fajr-pair-prereg.md
SHA256:  eea6e10e756410f07dbd4667463fca9fe87d820aa8fbbb86d3614f173bd4afcb

Three cells: A) FR(Q32, Q76) ≤ mean-1σ; B) FR(Q32, Q67) ≤ mean-1σ; C) joint pair-mean perm null.
Plus MW-6 hadith on-disk attestation verification.
"""

from __future__ import annotations
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q032-al-sajda/Q032-F-05-friday-fajr-pair-prereg.md"
EXPECTED_SHA = "eea6e10e756410f07dbd4667463fca9fe87d820aa8fbbb86d3614f173bd4afcb"
OUT = ROOT / "surahs/Q032-al-sajda/csv/Q032-F-05.json"
SEED = 20260509
N_PERM = 10000


def sha_verify():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    return actual


def load_fr():
    with (ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json").open(encoding="utf-8") as f:
        d = json.load(f)
    fr = {}
    for a, b, v in d["D_matrix_upper_triangular"]:
        fr[(min(a, b), max(a, b))] = v
    return fr, d["distance_matrix_stats"]


def D(fr, a, b):
    return fr[(min(a, b), max(a, b))]


def verify_hadith(collection, idInBook, must_contain_substrings):
    path = ROOT / f"data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{collection}.json"
    with path.open(encoding="utf-8") as f:
        d = json.load(f)
    for h in d.get("hadiths", []):
        if h.get("idInBook") == idInBook:
            text = h.get("arabic", "")
            ok = all(sub in text for sub in must_contain_substrings)
            return {"found": True, "id": idInBook, "contains_all_substrings": ok,
                    "matched_substrings": [s for s in must_contain_substrings if s in text],
                    "text_preview": text[:300]}
    return {"found": False, "id": idInBook}


def main():
    sha_actual = sha_verify()
    fr, fr_stats = load_fr()
    mean_fr = fr_stats["mean"]
    # Compute corpus pairwise std
    distances = list(fr.values())
    import statistics
    std_fr = statistics.pstdev(distances)
    threshold_1sigma = mean_fr - std_fr

    # Cell A — Q 32 ↔ Q 76 (Friday-fajr, Bukhārī #870/#1037)
    d_32_76 = D(fr, 32, 76)
    pass_a = d_32_76 <= threshold_1sigma

    # Cell B — Q 32 ↔ Q 67 (al-Munjiya nightly, Tirmidhī #2975)
    d_32_67 = D(fr, 32, 67)
    pass_b = d_32_67 <= threshold_1sigma

    # Cell C — joint permutation null
    rng = random.Random(SEED)
    pool = [s for s in range(2, 115) if s != 32]  # non-Q1 non-Q32 surahs (we'll re-pair with Q32 partner-test)
    # Construct the joint test: mean of two FR(Q32, X) values for randomly chosen X1, X2
    joint_obs = (d_32_76 + d_32_67) / 2.0
    null_means = []
    for _ in range(N_PERM):
        x1, x2 = rng.sample(pool, 2)
        m = (D(fr, 32, x1) + D(fr, 32, x2)) / 2.0
        null_means.append(m)
    null_means.sort()
    p_c = sum(1 for v in null_means if v <= joint_obs) / N_PERM
    pct5_c = null_means[int(0.05 * N_PERM)]
    pass_c = p_c <= 0.017

    # MW-6 — hadith on-disk verification
    h_870 = verify_hadith("bukhari", 870, ["الم", "تنزيل", "هل أتى", "الجمعة", "الفجر"])
    h_1037 = verify_hadith("bukhari", 1037, ["الم", "تنزيل", "هل أتى"])
    h_2975 = verify_hadith("tirmidhi", 2975, ["الم", "تنزيل", "تبارك", "ينام"])
    # MW-6 sanity: confirm brief's claimed #2891/#2892 do NOT mention Sajda+Mulk
    h_2891 = verify_hadith("tirmidhi", 2891, ["الم", "تنزيل"])
    h_2892 = verify_hadith("tirmidhi", 2892, ["الم", "تنزيل"])

    # Overall verdict
    cells_passed = sum([pass_a, pass_b, pass_c])
    if cells_passed == 3:
        verdict = "PASS-DIRECTED 3/3 (both liturgical pairs FR-bound; joint permutation tight)"
    elif cells_passed == 2:
        verdict = f"PASS-DIRECTED 2/3"
    elif cells_passed == 1:
        verdict = f"PARTIAL 1/3"
    else:
        verdict = "NULL — DIRECTION REVERSED on all cells"

    out = {
        "test_id": "Q032-F-05",
        "title": "Friday-fajr Sajda+Insān (al-Bukhārī #870/#1037) + al-Munjiya nightly Sajda+Mulk (al-Tirmidhī #2975) FR-pair audit",
        "prereg_sha_expected": EXPECTED_SHA,
        "prereg_sha_actual": sha_actual,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": 0.017,
        "corpus_pairwise_FR_mean": mean_fr,
        "corpus_pairwise_FR_std": std_fr,
        "threshold_mean_minus_1sigma": threshold_1sigma,
        "cell_A_friday_fajr_Q32_Q76": {
            "FR_distance": d_32_76,
            "threshold": threshold_1sigma,
            "pass_direction": pass_a,
            "z_score": (d_32_76 - mean_fr) / std_fr,
        },
        "cell_B_munjiya_nightly_Q32_Q67": {
            "FR_distance": d_32_67,
            "threshold": threshold_1sigma,
            "pass_direction": pass_b,
            "z_score": (d_32_67 - mean_fr) / std_fr,
        },
        "cell_C_joint_perm_null": {
            "joint_obs_mean": joint_obs,
            "n_perm": N_PERM,
            "null_5pct": pct5_c,
            "p_one_sided_le": p_c,
            "pass_alpha_bon": pass_c,
        },
        "MW6_hadith_attestations": {
            "bukhari_870_friday_fajr": h_870,
            "bukhari_1037_friday_fajr_variant": h_1037,
            "tirmidhi_2975_munjiya_nightly": h_2975,
            "brief_error_tirmidhi_2891_check": h_2891,
            "brief_error_tirmidhi_2892_check": h_2892,
        },
        "verdict": verdict,
        "note": ("Brief specified al-Tirmidhī #2891/#2892 as Friday-fajr Q32+Q67. On-disk: 2891/2892 are clothing hadith; "
                 "the Q32+Q67 nightly pair is Tirmidhī #2975; Friday-fajr is Bukhārī #870/#1037 with Q32+Q76. "
                 "Tested both empirically anchored pairs."),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"WROTE {OUT}")
    print(f"verdict: {verdict}")
    print(f"  FR(Q32,Q76)={d_32_76:.4f} (z={(d_32_76-mean_fr)/std_fr:.2f}); pass_A={pass_a}")
    print(f"  FR(Q32,Q67)={d_32_67:.4f} (z={(d_32_67-mean_fr)/std_fr:.2f}); pass_B={pass_b}")
    print(f"  joint p_perm={p_c:.4f}; pass_C={pass_c}")


if __name__ == "__main__":
    main()
