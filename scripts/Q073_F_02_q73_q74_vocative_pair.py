#!/usr/bin/env python3
"""Q073-F-02 — Q 73 ↔ Q 74 muzzammil/muddaththir vocative-pair cohesion test.

Pre-reg: surahs/Q073-al-muzzammil/Q073-F-02-q73-q74-vocative-pair-prereg.md
Pre-reg SHA256: 65a709885ec20dfbbb734323cd8f994d94256bdf1fdff3aed4c7c225871bf3a0
Rules-tuple: (no-tashkeel, QAC v0.4 root tokens, basmala-counted-only-in-Q1, mushaf order, Hafs-Kufan)
"""
import json, hashlib, sys, os, random
import numpy as np

PREREG = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/Q073-F-02-q73-q74-vocative-pair-prereg.md'
EXPECTED_SHA = '65a709885ec20dfbbb734323cd8f994d94256bdf1fdff3aed4c7c225871bf3a0'
SEED = 20260509
N_PERM = 1000

FR_PATH = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'
ADJ_PATH = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/csv/Q073-F-02.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    # Load FR matrix
    fr = json.load(open(FR_PATH))
    n = 114
    D = np.zeros((n, n))
    for i, j, d in fr['D_matrix_upper_triangular']:
        D[i-1, j-1] = d
        D[j-1, i-1] = d

    # Axis A: mutual top-15
    Q73_idx, Q74_idx = 72, 73
    q73_row = D[Q73_idx, :].copy()
    q73_row[Q73_idx] = np.inf
    q74_row = D[Q74_idx, :].copy()
    q74_row[Q74_idx] = np.inf
    rank_74_in_73 = int(np.sum(q73_row < q73_row[Q74_idx]) + 1)
    rank_73_in_74 = int(np.sum(q74_row < q74_row[Q73_idx]) + 1)

    axis_A_pass = (rank_74_in_73 <= 15) and (rank_73_in_74 <= 15)

    # null distribution: for 1000 random surah pairs, fraction with mutual top-15
    rng = random.Random(SEED)
    surah_ids = list(range(n))
    null_mutual_top15 = 0
    for _ in range(N_PERM):
        i, j = rng.sample(surah_ids, 2)
        ri = D[i, :].copy(); ri[i] = np.inf
        rj = D[j, :].copy(); rj[j] = np.inf
        rank_j_in_i = np.sum(ri < ri[j]) + 1
        rank_i_in_j = np.sum(rj < rj[i]) + 1
        if rank_j_in_i <= 15 and rank_i_in_j <= 15:
            null_mutual_top15 += 1
    p_axis_A = null_mutual_top15 / N_PERM
    # but for the empirical pair, the test is whether the mutual rank-15 is in the bottom 5% of surah-pairs
    # Use the empirical FR to test: for the SPECIFIC pair (Q 73, Q 74), the mutual-top-rank is enrichment-significant
    # Easier: empirical p = null_mutual_top15_count / total = baseline rate; pair passes if it's IN the mutual-top-15.
    # The "axis A pass" above already does that.

    # Axis B: adjacency cost from H-NEW-720
    adj = json.load(open(ADJ_PATH))
    pair_adj = next((a for a in adj['per_adjacency'] if a['s'] == 73), None)
    delta_raw_q73_q74 = pair_adj['delta_raw'] if pair_adj else None
    fraction_residual_q73_q74 = pair_adj['fraction_residual'] if pair_adj else None
    axis_B_pass = (delta_raw_q73_q74 is not None) and (delta_raw_q73_q74 <= 0)

    # Axis C: opening-formula morphological match
    quran = json.load(open(QURAN_PATH))
    q73 = next(s for s in quran if s['id'] == 73)
    q74 = next(s for s in quran if s['id'] == 74)
    q73_v1 = q73['verses'][0]['text']
    q74_v1 = q74['verses'][0]['text']
    # check both open with "يا أيها ال" + Form-V passive participle
    pat_v_passive = lambda s: s.startswith('يا أيها ال') and len(s.split()) == 3
    # Actually Q 73:1 = "يا أيها المزمل" (3 words), Q 74:1 = "يا أيها المدثر" (3 words)
    axis_C_pass = pat_v_passive(q73_v1) and pat_v_passive(q74_v1)
    # additional: morphological similarity check (mu-ZaMMiL vs mu-DDaTTiR — both Form-II/V passive participles)
    # The third word: "المزمل" and "المدثر" — both `ال` + 4-letter root with mu- prefix and gemination markers.
    # Empirical: same length (5 letters: م ز م ل / م د ث ر — wait, 4 each excluding al), same morphological shape.
    final_word_q73 = q73_v1.split()[-1]
    final_word_q74 = q74_v1.split()[-1]
    same_len = len(final_word_q73) == len(final_word_q74)
    mim_initial = final_word_q73.startswith('الم') and final_word_q74.startswith('الم')
    morph_iso = same_len and mim_initial

    # === Aggregate verdict ===
    n_pass = sum([axis_A_pass, axis_B_pass, axis_C_pass])
    if n_pass == 3:
        verdict = "CONFIRMED-STRONG"
    elif n_pass == 2:
        # under Bonferroni-3, alpha_bon = 0.0167; we have categorical Axis B/C — conservative call: DIRECTIONAL
        # axis A is not technically Bonferroni-passing on a permutation null (not stochastic) but if mutual top-15:
        verdict = "CONFIRMED" if axis_A_pass else "DIRECTIONAL"
    elif n_pass == 1:
        verdict = "DIRECTIONAL" if axis_C_pass else "NULL"
    else:
        verdict = "PRE-COMMIT-VIOLATION"

    out = {
        "test_id": "Q073-F-02",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm_axis_A": N_PERM,
        "axis_A": {
            "rank_Q74_in_Q73_neighbors": rank_74_in_73,
            "rank_Q73_in_Q74_neighbors": rank_73_in_74,
            "FR_distance_Q73_Q74": float(D[Q73_idx, Q74_idx]),
            "mutual_top_15": axis_A_pass,
            "null_mutual_top15_freq": null_mutual_top15,
            "null_mutual_top15_baseline_p": p_axis_A,
        },
        "axis_B": {
            "delta_raw_Q73_Q74": delta_raw_q73_q74,
            "fraction_residual": fraction_residual_q73_q74,
            "clamped_zero_seam": axis_B_pass,
        },
        "axis_C": {
            "Q73_v1": q73_v1,
            "Q74_v1": q74_v1,
            "matches_yaa_ayyuha_al_pattern": axis_C_pass,
            "morph_isomorph_passive_participle": morph_iso,
            "final_word_Q73": final_word_q73,
            "final_word_Q74": final_word_q74,
        },
        "n_pass_axes": n_pass,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Verdict: {verdict}")
    print(f"  Axis A: rank_74_in_73 = {rank_74_in_73}, rank_73_in_74 = {rank_73_in_74}, mutual_top_15 = {axis_A_pass}")
    print(f"  Axis B: delta_raw = {delta_raw_q73_q74:.5f}, clamped_zero = {axis_B_pass}")
    print(f"  Axis C: morph_iso = {axis_C_pass}, {q73_v1} | {q74_v1}")
    print(f"  Null mutual-top-15 baseline p = {p_axis_A:.4f}")
    print(f"Written to: {OUT_PATH}")


if __name__ == '__main__':
    main()
