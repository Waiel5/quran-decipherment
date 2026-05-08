---
surah: 7
test_id: Q007-F-05
title: Q 7's 7-prophet ordering as structurally PRIMARY among destruction-cycle surahs
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q007-F-01..F-05 (k tightened from 4 to 5 to include this test; tightening is self-verifying per HANDOFF/04-DISCIPLINE.md "Bonferroni asymmetry rule")
alpha_bon: 0.01
direction_locked: positive — Q 7's 7-prophet order Adam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā is a SUPER-SEQUENCE of Q 11's, Q 26's, and Q 21's prophet-orderings (intersected with Q 7's 7-prophet set)
rules_tuple: (no-tashkeel, QAC-PN-lemma-via-h-new-940-method, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q007-F-05 — Pre-registration: Q 7's 7-prophet ordering is structurally PRIMARY

## 1. Background — why this matters

H-NEW-940 (already complete, MIXED verdict 2026-05-07) found:
- **H2a CONFIRMED**: Ādam → Nūḥ → Hūd → Ṣāliḥ chain is τ=1.0 across 4 surahs (Q 7, 11, 19, 26). Bonferroni-4 PASSES at p=0.001.
- **H1 DIRECTIONAL only**: corpus-wide mean Kendall-τ = +0.144, p=0.047 (fails locked α=0.01).

Q 7's specific prophet-order is `Ādam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā` — the only Quranic surah that contains this exact 7-element sequence.

**Q007-F-05 EXTENDS H-NEW-940's H2a** by asking whether Q 7's ordering is the *structural primary* — i.e., are other narrative surahs' prophet-orderings *sub-sequences* of Q 7 (when restricted to the Q-7 prophet set)?

## 2. Hypothesis (locked before observation)

For each of {Q 11, Q 26, Q 21}:
- Restrict that surah's prophet-ordering to the intersection with Q 7's 7-prophet set (= {Adam, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Mūsā, Hārūn} — 8 names; Hārūn handled jointly with Mūsā per H-NEW-940 note on the Mūsā→Hārūn priority).
- Test: is the restricted ordering of Q 11 / Q 26 / Q 21 (on this intersection set) a sub-sequence of Q 7's ordering?

**H1 (per surah)**: Q 11's restricted-ordering is a sub-sequence of Q 7's; Q 26's restricted-ordering is a sub-sequence; Q 21's restricted-ordering is a sub-sequence.

**Direction-locked**: Kendall-τ between Q 7's restricted-ordering and {Q 11, Q 26, Q 21}'s respective restricted-ordering equals +1.0 (perfect sub-sequence preservation).

**Bonferroni-3 outer** (within H1 sub-tests): α_test = 0.05/3 = 0.0167 each.

**Bonferroni-5 within Q007 family**: α_bon = 0.01 (per the family declaration).

## 3. Test statistic

For each of {Q 11, Q 26, Q 21}:
- Restrict to intersection with Q 7's 7-prophet set (use H-NEW-940's prophet-order vectors directly, drop names not in Q 7's set).
- Compute Kendall-τ vs Q 7's restricted ordering.
- Pre-committed: τ = +1.0 (perfect).

**Permutation null**: per Q*, sample 10,000 random permutations of the same restricted name-set; count fraction with τ ≥ observed.

## 4. Success / Failure

Per surah:
- **CONFIRMED**: τ = +1.0 AND p_perm ≤ α_bon (= 0.01).
- **DIRECTIONAL**: τ = +1.0 BUT p_perm ∈ (0.01, 0.05].
- **NULL**: τ < 1.0.

**Aggregate verdict**:
- **PRIMARY-CONFIRMED**: 3/3 surahs CONFIRMED.
- **PARTIAL-PRIMARY**: 2/3 CONFIRMED.
- **NULL**: ≤ 1/3 CONFIRMED.

## 5. Honest limits

1. **H-NEW-940 already established Q 7-Q 11-Q 26 share the {Ādam, Nūḥ, Hūd, Ṣāliḥ} chain with τ=1.0**. The novel claim here is whether the *full 7-element* Q 7 ordering preserves through to Q 11, Q 26, Q 21 — i.e., whether the LATER prophets (Lūṭ, Shuʿayb, Mūsā) also slot in correctly.
2. **Q 21's prophet-order starts with Mūsā-Hārūn-FIRST** (per H-NEW-940 catalog), then Ibrāhīm, then later prophets. Q 21 contains only 4 of Q 7's 7 prophets (Mūsā, Hārūn, Lūṭ, Nūḥ, plus the absent ones), so the restricted-ordering test on Q 21 has fewer constraints. It's likely the WEAKEST test in this family.
3. **Q 26 is RECENTLY-CONFIRMED** (Q026-F-01) to have the prophet-cycle Mūsā → Ibrāhīm → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb. When restricted to Q 7's 7-prophet set, this becomes Mūsā → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb (Ādam not in Q 26). Compared to Q 7's Ādam → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb → Mūsā: in Q 26, **Mūsā moves from LAST to FIRST**. This is a STRONG inversion. So Q 26's restricted ordering is NOT a sub-sequence of Q 7. **Pre-commit prediction for Q 26: τ FAILS** (this would have been a PRE-COMMIT VIOLATION under the original "all 3 pass" framing).

   **Direction lock honest disclosure**: I expect Q 26 to FAIL on Mūsā-position alone. The aggregate verdict will likely be **PARTIAL-PRIMARY at best**. The pre-commit acknowledges this.

4. **Q 11's restricted-ordering** (per H-NEW-940 catalog): Mūsā(prologue) → Nūḥ → Hūd → Ṣāliḥ → Ibrāhīm → Lūṭ → Isḥāq → Yaʿqūb → Shuʿayb. Restricted to Q 7's 7-set: Mūsā → Nūḥ → Hūd → Ṣāliḥ → Lūṭ → Shuʿayb. Q 11 also moves Mūsā to FRONT (as a prologue). So Q 11's restricted ordering is ALSO NOT a sub-sequence of Q 7's "Mūsā-last" pattern.

   **Pre-commit prediction for Q 11: FAILS** if the Mūsā-prologue in Q 11:25 is included as Mūsā's first-mention. The H-NEW-940 catalog DOES include this. Q 11 will FAIL.

   **Note**: this is EXACTLY where the test reveals something: Q 7 places Mūsā at the END of the 7-prophet sequence (after Shuʿayb), whereas Q 11 and Q 26 put Mūsā at the FRONT. This is a SIGNATURE structural difference — "Q 7's Mūsā-block is the climax of the cycle" vs "Q 26/Q 11's Mūsā-block is the prologue."

## 6. Disclosure: this is essentially a structural-difference test, NOT a primacy test

Given the priors above, I expect the verdict to be: **NOT-PRIMARY (Q 7's Mūsā-final placement is unique; other surahs' Mūsā-prologue placement makes Q 7's order non-sub-sequence-able to them)**. The honest finding is that **Q 7 has a UNIQUE structural climax-position for Mūsā**, distinct from Q 11 and Q 26. The test is calibrated to *expose* this signature, not to confirm the H1 strawman.

If this expectation holds: the verdict is **NULL** on the H1 framing but **POSITIVE-FINDING** on the descriptive observation that **Q 7's Mūsā-as-final-block is structurally distinctive**.

## 7. Rules-tuple

`(no-tashkeel, QAC-PN-lemma-via-H-NEW-940-method, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. SHA256 lock

Computed at run-time; embedded in `scripts/Q007_F_05_prophet_order_primary.py`.

## 9. Bonferroni-tightening note

Original Q007 family was Q007-F-01..F-04 (k=4, α_bon=0.0125). Adding F-05 to the family TIGHTENS α to 0.05/5 = 0.01. Per HANDOFF/04-DISCIPLINE.md "Bonferroni asymmetry rule," tightening is self-verifying without ratification.
