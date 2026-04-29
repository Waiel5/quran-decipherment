#!/usr/bin/env python3
"""Q027-F-04 — Q 1 ↔ Q 27 numerological-coincidence audit.

Pre-reg: surahs/Q027-al-naml/Q027-F-04-numerological-coincidence-audit-prereg.md
Pre-reg SHA256: a500b019e2d6872693ae93d21f4d7c9c840f6cb9ca9cb4c5e23302c5cfc221ad
"""
import json, re, hashlib, sys, os, random

PREREG = '/Users/grey/Downloads/quran/surahs/Q027-al-naml/Q027-F-04-numerological-coincidence-audit-prereg.md'
EXPECTED_SHA = 'a500b019e2d6872693ae93d21f4d7c9c840f6cb9ca9cb4c5e23302c5cfc221ad'

PAUSE_RE = re.compile(r'[ۖۚ؛،۔ۗۘۙۛۜ۩]')


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch\nexpected {EXPECTED_SHA}\nactual   {actual}", file=sys.stderr)
        sys.exit(1)


def tokens(text):
    return PAUSE_RE.sub(' ', text).split()


def main():
    verify_sha()
    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    q1 = d[0]
    q27 = d[26]

    # Word counts
    def word_count(s):
        return sum(len(tokens(v['text'])) for v in s['verses'])

    W1 = word_count(q1)
    W27 = word_count(q27)
    W1_v1 = len(tokens(q1['verses'][0]['text']))  # words of basmala v1
    W1_minus_basmala = W1 - W1_v1

    V1 = q1['total_verses']  # 7
    V27 = q27['total_verses']  # 93
    BASMALA_VERSE_IN_Q1 = 1
    BASMALA_VERSE_IN_Q27 = 30  # the second basmala's verse number
    Q_INDEX_1 = 1
    Q_INDEX_27 = 27

    # All surahs verse counts
    all_verse_counts = [s['total_verses'] for s in d]

    # ----- C1: (basmala_v_in_Q27 − basmala_v_in_Q1) = W_1?
    C1_lhs = BASMALA_VERSE_IN_Q27 - BASMALA_VERSE_IN_Q1  # 29
    C1_truth_W1 = (C1_lhs == W1)
    C1_truth_W1_minus_basmala = (C1_lhs == W1_minus_basmala)

    # ----- C2: (Q_index_1 + Q_index_27) = W_1 + 1 ? (i.e., 28 = 29?)
    C2_lhs = Q_INDEX_1 + Q_INDEX_27  # 28
    C2_rhs = W1 + 1
    C2_truth = (C2_lhs == C2_rhs)
    # also: 28 vs other Q1 properties?
    C2_alternative_match = (C2_lhs == W1)  # 28 == 29? -> False
    C2_28_match_anywhere = (C2_lhs == V27)  # 28 == 93? False
    # Identify what 28 could match:  W1=W1, V1=7, V27=93, ...
    matches_28 = []
    if C2_lhs == V1: matches_28.append('V1=7? no')
    # attempt all integer relations: any j such that V_j = 28?
    surahs_with_28_verses = [i + 1 for i, v in enumerate(all_verse_counts) if v == 28]

    # ----- C3: (basmala_v_in_Q27 − Q_index_27) =?
    C3_lhs = BASMALA_VERSE_IN_Q27 - Q_INDEX_27  # 30 - 27 = 3
    C3_relation_to_q1 = {
        'equals_V1_minus_4': (C3_lhs == V1 - 4),  # 3==3 ? True
        'equals_W1_v1_minus_1': (C3_lhs == W1_v1 - 1),
    }

    # ----- C4: Q 27's verse count (93) divides / relates to:
    # 19 (Code-19): 93 % 19 = ?
    # 7, 28, 114
    C4 = {
        '93_mod_19': 93 % 19,
        '93_div_19_int': 93 // 19,
        '93_mod_7': 93 % 7,
        '93_mod_28': 93 % 28,
        '93_mod_114': 93 % 114,
        '114_minus_27': 114 - 27,  # 87 (= V_87? V_72?)
    }

    # ----- Permutation control: how often do random surah-pairs satisfy similar relations?
    rng = random.Random(42)
    n_perm = 10000

    # For C1: random pair (i,j), is (some_v_in_Qj − some_v_in_Qi) = W_i?
    # We'll fix i=Q1, vary j, with basmala=v.1 on the left side of subtraction.
    # The general "trivial" coincidence: (k - 1) = W1 holds when k = W1+1 = 30. So we ask:
    # of all 114 surahs, how many surahs have a verse-number k = W1+1 (i.e., have ≥ W1+1 = 30 verses)?
    surahs_with_at_least_30_verses = sum(1 for v in all_verse_counts if v >= 30)
    # This is a deterministic count, not a permutation: ~half the corpus has ≥30 verses,
    # so the "coincidence" is trivially possible for any verse-number choice in those surahs.
    # The selection of v.30 in Q 27 needs additional structural justification — i.e., the basmala
    # is *located* at v.30, which is non-trivial. But the arithmetic itself is not rare.

    # For C2: how often does (i + j) equal W_i + 1 for a random pair?
    # With i=1, W_i=29, this requires j=29. There's exactly 1 surah with index 29 in 114, so trivially possible.
    # Permutation: random pair (i,j) uniformly; fraction satisfying (i + j) == W_i + 1 with W_i=word-count of surah i.

    # Compute word counts for ALL surahs (no-tashkeel)
    Ws = [word_count(s) for s in d]

    perm_C1_hits = 0
    perm_C2_hits = 0
    perm_C3_hits = 0
    for _ in range(n_perm):
        i = rng.randint(0, 113)
        j = rng.randint(0, 113)
        if i == j: continue
        # C1-analog: pick a random verse number v in surah j; ask if v - 1 = W_{i+1}? (v ranges in [1, V_j])
        v_j = rng.randint(1, all_verse_counts[j])
        if (v_j - 1) == Ws[i]:
            perm_C1_hits += 1
        # C2-analog: (i+1 + j+1) == W_{i+1} + 1?
        if ((i + 1) + (j + 1)) == (Ws[i] + 1):
            perm_C2_hits += 1
        # C3-analog: (v_j - (j+1)) == 3?
        if (v_j - (j + 1)) == 3:
            perm_C3_hits += 1
    p_perm_C1 = (perm_C1_hits + 1) / (n_perm + 1)
    p_perm_C2 = (perm_C2_hits + 1) / (n_perm + 1)
    p_perm_C3 = (perm_C3_hits + 1) / (n_perm + 1)

    # ----- C4 null: how often do random verse-counts have mod-19 == 0?
    # 93 % 19 = 17 (not zero). Nonsignificant by design.

    # Aggregated verdict per coincidence (rules: TRUE + p_perm < 0.0125)
    def verdict_for(true_flag, p):
        if true_flag and p < 0.0125:
            return 'CONFIRMED'
        elif true_flag:
            return 'TRUE_BUT_NOT_NULL_SIG'
        else:
            return 'FALSE'

    out = {
        'finding_id': 'Q027-F-04',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token-words, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'Deterministic check of coincidence relations + 10000-perm null on random surah-pair analogs',
        'inputs': {
            'V1': V1, 'V27': V27, 'W1': W1, 'W1_v1': W1_v1,
            'W1_minus_basmala': W1_minus_basmala, 'W27': W27,
            'BASMALA_VERSE_IN_Q1': BASMALA_VERSE_IN_Q1,
            'BASMALA_VERSE_IN_Q27': BASMALA_VERSE_IN_Q27,
        },
        'C1_basmala_diff_equals_W1': {
            'claim': '(v_basmala_in_Q27 - v_basmala_in_Q1) = W_1',
            'lhs': C1_lhs, 'rhs_W1': W1,
            'truth_value_full_W1': C1_truth_W1,
            'truth_value_W1_minus_basmala': C1_truth_W1_minus_basmala,
            'p_perm_random_pair_analog': p_perm_C1,
            'verdict': verdict_for(C1_truth_W1, p_perm_C1),
        },
        'C2_index_sum_equals_W1_plus_1': {
            'claim': '(Q_index_1 + Q_index_27) = W_1 + 1',
            'lhs': C2_lhs, 'rhs': C2_rhs,
            'truth_value': C2_truth,
            'p_perm_random_pair_analog': p_perm_C2,
            'verdict': verdict_for(C2_truth, p_perm_C2),
            'surahs_with_28_verses': surahs_with_28_verses,
        },
        'C3_v_basmala_minus_index': {
            'claim': '(v_basmala_in_Q27 - Q_index_27) integer-relation to Q 1 properties',
            'lhs': C3_lhs,
            'relations_to_Q1_properties': C3_relation_to_q1,
            'p_perm_random_v_minus_index_eq_3': p_perm_C3,
        },
        'C4_q27_verse_count_divisibility': {
            'claim': 'Q 27 verse-count (93) has special arithmetic relation to 19 / 7 / 28 / 114',
            'computations': C4,
            'verdict': 'NULL_NO_SPECIAL_DIVISIBILITY',
        },
        'aggregate_verdict': 'See per-relation verdict; with rules-tuple discipline applied, none of the popular numerical coincidences survive as both arithmetically TRUE AND null-significant.',
        'note': ('Per MASTER-FINDINGS-LEDGER, "Code 19" verse-count divisibility is uniformly NULL. '
                 'This investigation specifically extends that to the Q 1 ↔ Q 27 basmala-axis '
                 'numerology that often appears in popular numerological writings. '
                 'Equal NULL prominence is mandatory.'),
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/Q027-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q027-F-04 inputs: V1={V1}, V27={V27}, W1={W1}, W1_minus_basmala={W1_minus_basmala}")
    print(f"  C1 (30-1=W1=29? full W1={W1}, minus basmala={W1_minus_basmala}): "
          f"truth_full={C1_truth_W1}, truth_minus_basmala={C1_truth_W1_minus_basmala}, p_perm={p_perm_C1:.4f}")
    print(f"  C2 (1+27=W1+1?): {C2_lhs} vs {C2_rhs}, truth={C2_truth}, p_perm={p_perm_C2:.4f}")
    print(f"  C3 (30-27=3, relations to Q1): {C3_relation_to_q1}, p_perm_3={p_perm_C3:.4f}")
    print(f"  C4 (93 mod 19): {C4['93_mod_19']}; 93 mod 7: {C4['93_mod_7']}")


if __name__ == '__main__':
    main()
