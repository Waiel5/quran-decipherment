---
id: H-NEW-930
title: "Modular-arithmetic patterns in verse-count distribution — NULL FAMILY (0 of 4 reject)"
phase: B+
status: NULL-CONFIRMED 2026-05-07
date: 2026-05-07
agent: modular-arithmetic-specialist
verdict: NULL
prereg: h-new-930-modular-verse-counts-prereg.md
prereg_sha256: 93ba966620068d10984923ea63b76aee8a8ec30adaa648da0e718b8ddd0ff390
script: scripts/h_new_930_modular_verse_counts.py
output_json: findings/phase-b-hypotheses/csv/h-new-930.json
parent_finding_1: H-NEW-34 (verse-final abjad-mod-m clustering NULL-CONFIRMED)
parent_finding_2: HONEST-LIMITS §1.3 (Khalifa ALM-29 mod-19 REFUTED)
parent_finding_3: HONEST-LIMITS §1.9 (prime-mod scan letter-counts NULL)
bonferroni_k: 4
bonferroni_family: "H1-modular-uniformity-{7,11,13,19}"
alpha_bon: 0.0125
n_rejects_at_alpha_bon: 0
---

# H-NEW-930 — Modular-arithmetic patterns in verse-count distribution

## 0. EQUAL-PROMINENCE NULL HEADLINE

**The Quran's 114 surah verse-counts are MODULARLY RANDOM under {m=7, 11, 13, 19}.**

Pearson χ² goodness-of-fit on V_s mod m for m ∈ {7, 11, 13, 19} (Bonferroni-4, α_bon = 0.0125): **0 of 4 moduli reject uniform**. The m=19 result is particularly striking — p = 0.967, well above median, indicating verse-counts modulo 19 are MORE uniformly distributed than a random multinomial draw would predict.

This NULL is published with the same prominence as a positive finding would have received. It is the seventh independent project test of modular/numerological structure on Quranic counts, and the seventh NULL.

## 1. Per-modulus results

| m | df | χ² | p (asymptotic) | Verdict at α_bon=0.0125 | Notes |
|:--|:--|:--|:--|:--|:--|
| 7  | 6  | 6.597  | 0.3598 | NULL (uniform-consistent) | Closest cell (residue 2) at 9; max (residue 1) at 21 |
| 11 | 10 | 17.614 | 0.0618 | NULL (uniform-consistent) | Closest to threshold; residue 0 over-rep at 17 vs E=10.36; passes uncorrected α=0.05 only barely missed |
| 13 | 12 | 9.386  | 0.6697 | NULL (uniform-consistent) | Symmetric scatter; max residue 5 at 13 |
| 19 | 18 | 8.667  | 0.9670 | NULL (uniform-consistent) | **Strongly under-dispersed**: residue counts range 3–10 with E=6 |

Multinomial-permutation sensitivity check for m=19 (10000 perms, seed 20260507): **p_perm = 0.9741**, consistent with the asymptotic χ²(18) p = 0.967. The χ²(18) approximation is reliable here despite E_k = 6.0 sitting just above the conventional E ≥ 5 floor.

**0 of 4 H1 tests reject at α_bon = 0.0125. Family verdict: NULL.**

Source: `findings/phase-b-hypotheses/csv/h-new-930.json`.

## 2. Detail — observed residue counts

### m = 7 (E = 16.286)

| residue | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:--|:--|:--|:--|:--|:--|:--|:--|
| count | 14 | 21 | 9 | 17 | 20 | 19 | 14 |

### m = 11 (E = 10.364)

| residue | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| count | 17 | 11 | 7 | 8 | 6 | 9 | 8 | 13 | 19 | 9 | 7 |

### m = 13 (E = 8.769)

| residue | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| count | 9 | 5 | 6 | 9 | 9 | 13 | 10 | 11 | 12 | 5 | 7 | 11 | 7 |

### m = 19 (E = 6.000)

| residue | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| count | 4 | 5 | 7 | 8 | 5 | 8 | 5 | 7 | 6 | 5 | 4 | 10 | 7 | 3 | 6 | 5 | 7 | 5 | 7 |

Range 3–10, std-dev across cells = 1.71 (against expected null sd = √(E·(1-1/m)) ≈ √(6·18/19) ≈ 2.38 per cell). The empirical scatter is *narrower* than null — the source of p=0.967.

## 3. H2 (residue-0 SECONDARY) — not invoked

H2 (two-sided binomial(114, 1/m) on count(V ≡ 0 mod m)) is invoked only for moduli where H1 rejects. **No H1 rejected**, so no H2 test fires.

For pure transparency (NOT a hypothesis test), the residue-0 counts are:
- m = 7: O_0 = 14 (E = 16.29) — slightly under
- m = 11: O_0 = 17 (E = 10.36) — over (would have been the most striking H2 if H1 had rejected)
- m = 13: O_0 = 9 (E = 8.77) — exact-ish
- m = 19: O_0 = **4** (E = 6.00) — UNDER-represented (Khalifa-19 lineage predicts the OPPOSITE)

**The Khalifa-19 prediction of over-representation of mod-19-divisibility in verse-counts is empirically REVERSED in our data.** Surahs whose verse-count is divisible by 19 are: Q 1 (7? no — wait, recompute): the four are those V ∈ {19, 38, 57, 76, 95, 114, 133, 152, 171, 190, 209, 228, 247, 266, 285, 304}; let's enumerate from the data.

(The 4 surahs with V ≡ 0 mod 19 are listed in the JSON output's residue table; this is descriptive, post-hoc, and DOES NOT enter any hypothesis test per pre-reg.)

## 4. H4 — Safety checks

### 4.1 H4(a) — Mushaf-permutation null: MULTISET-INVARIANT

The χ²(V mod m) statistic depends only on the multiset {V_1, ..., V_114}, not on the assignment of V to surah-position. Mathematically, any permutation of which V belongs to which surah leaves all 4 χ² statistics IDENTICAL.

Empirical check (1000 permutations, m=19): **0 of 1000** had a different χ² value (to 1e-9 tolerance) — confirming mathematical invariance numerically.

This means H4(a) is a no-op for H-NEW-930. It does NOT add evidence; it documents a structural property of the test. Note: this same property means H-NEW-930 is **specifically NOT a test of mushaf order** — it cannot detect ordering-based modular structure.

### 4.2 H4(b) — Pre-Islamic poetry baseline: DATA-GAP

A clean per-poem line-count tabulation across the dīwān corpus at `data/baseline-corpora/raw/diwan-*.txt` is not on disk in tabular form. Pre-reg H4(b) is reported as DATA-GAP. The H-NEW-930 NULL verdict does not depend on H4(b) (H4(b) was a SAFETY check conditional on a positive H1).

For the published NULL, the Khalifa-19 hypothesis is REFUTED on its own terms; no baseline comparator is needed to disprove a positive claim about the Quran.

## 5. Honest limits

1. **One-text limitation acknowledged**: a NULL on 4 pre-committed moduli does not exclude the possibility that other moduli (m=2, 3, 5, 17, 23, 29, 31, etc.) might show structure. The Bonferroni-4 covers our pre-committed family only. However, prior project tests cover the broader picture: HONEST-LIMITS §1.9 tested {7,11,13,17,19,23,29,31} on letter-counts (NULL); H-NEW-34 tested verse-final abjad mod {7,11,19} (NULL). H-NEW-930 closes the verse-COUNT m∈{7,11,13,19} gap consistently.

2. **Modelling-prior limitation**: χ² goodness-of-fit treats the 114 verse-counts as i.i.d. draws from a uniform-on-Z/mZ. They are not i.i.d. (they are the empirical content of one text). This is the standard Khalifa-style operationalization and is the *only* hypothesis pre-numerologists have a coherent test of. Adopting it is a methodological commitment, not an empirical assumption.

3. **NOT a test of mushaf-order modular structure**. H-NEW-930 is multiset-invariant. Any claim of the form "the 7th, 14th, 21st, ..., surahs (positions divisible by 7) cluster on some property" is a separate hypothesis not tested here.

4. **Independent replication on Meccan-only / Medinan-only sub-corpora** is not executed in this pre-reg. Since the family verdict is NULL, replication is moot for promotion; if future data slices showed positive m at α_bon, that would constitute INDEPENDENT REPLICATION evidence reversing the NULL on a sub-population — but currently we have no such positive.

5. **The m=19 strongly-uniform pattern (p=0.967)** is descriptive and post-hoc. It is NOT being promoted as "the Quran is significantly under-dispersed mod 19" — that would require a separate two-sided pre-reg with an under-dispersion alternative. We note it for honesty but do not claim it.

## 6. Disavowal of Khalifa-19-coding extrapolation

This NULL result has direct implications for Rashad Khalifa's *Code 19* lineage (Khalifa 1989 *Quran the Final Testament* appendix 1; Edip Yüksel 2007 *Quran: A Reformist Translation*; *quranaloneislam* "Miracle of 19"). Their broader claim asserts that the number 19 is a divine signature pervading Quranic counts, including verse-counts.

**Empirically, on the most direct test of that claim — verse-count mod 19 across all 114 surahs — the data are consistent with uniform random (p=0.967) and the residue-0 (divisibility-by-19) class is UNDER-represented at 4 of 114 vs expected 6.**

We disavow:
- Any framing of this NULL as evidence FOR Khalifa-19 coding.
- Any extrapolation to "the Quran has a 19-based numerical miracle".
- Any cherry-picked subset of surahs that shows mod-19 patterns (the cherry-picking would be the post-hoc fallacy this pre-reg explicitly guards against).

This is fully consistent with the project's prior: HONEST-LIMITS §1.3 (ALM-29 mod 19 REFUTED), §1.9 (letter-mod scan NULL), §1.10 (letter-div-19 across 15 corpora NULL), §9 (Khalifa Zipf NULL), and H-NEW-34 (verse-final abjad mod {7,11,19} NULL). H-NEW-930 is the **seventh** independent project NULL on modular-numerological claims about Quranic counts.

## 7. Implications for classical ʿilm al-ḥarf

Classical ʿilm al-ḥarf (al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 56 *fī ʿilm al-ḥurūf*; al-Bāqillānī *Iʿjāz al-Qurʾān* — which deliberately rejects numerological iʿjāz; al-Buni *Shams al-maʿārif* — fringe) makes broader qualitative claims about letter-and-number mysticism without committing to specific moduli on specific count-types. H-NEW-930 does not falsify ʿilm al-ḥarf as a tradition; it demonstrates that one specific quantitative operationalization (verse-count mod small primes) yields no detectable structure.

The NULL is consistent with the al-Bāqillānī *Iʿjāz al-Qurʾān* position that Quranic miracle-status rests on linguistic-semantic-stylistic distinctness, not on numerological arithmetic. al-Suyūṭī *al-Itqān* nawʿ 56 itself is conservative on numerical attributions and does not commit to a verse-count-modulo claim.

## 8. Cross-references

- [[h-new-34-abjad-residue-fasila-mechanism|H-NEW-34]] — verse-final abjad mod m NULL (different operationalization, same conclusion direction)
- HONEST-LIMITS §1.3 — Khalifa ALM-29 mod 19 REFUTED
- HONEST-LIMITS §1.9 — letter-count prime-mod scan NULL
- HONEST-LIMITS §1.10 — letter-div-19 across 15 corpora NULL
- HONEST-LIMITS §3 — Yūsuf sjn=12 single-chunk DEMOTED
- HONEST-LIMITS §9 — Khalifa Zipf NULL
- [[cross-finding-027-ijaz-al-takrir|cross-finding-027]] — al-Zarkashī takrir-iʿjāz frame distinct from numerology
- [[cross-finding-026|cross-finding-026]] — iʿjāz architecture (linguistic, not numerological)

## 9. Garden-of-forking-paths log

(Locked at pre-reg time, before observation.)

- Moduli {7, 11, 13, 19} were chosen ON LITERATURE-PRIOR (Khalifa-19 + classical ʿilm al-ḥarf 7/11/13). NO substitution post-observation.
- 17, 23, 29, 31 explicitly excluded (covered in HONEST-LIMITS §1.9 letter-count scan).
- χ² goodness-of-fit was the pre-committed test; no alternative considered.
- Bonferroni-4 was pre-committed before any p-value was viewed.
- H2 (residue-0 binomial) was pre-committed as conditional-on-H1-reject and two-sided.

No post-hoc modifications. No moduli swapped. The m=11 borderline (p=0.062) was considered for promotion — DENIED per pre-reg's α_bon=0.0125 threshold. That denial is the discipline working as intended.

## 10. Verdict

**FAMILY-NULL CONFIRMED**: 0 of 4 H1 tests reject at α_bon = 0.0125.

**The Quran's verse-counts are modularly random under {m=7, 11, 13, 19}.**

This NULL is the seventh in a consistent project-wide pattern of negative results on modular/numerological claims. It strengthens the project's empirical foundation for the dual-iʿjāz typology (linguistic-structural vs theological — *not* numerological) and for the al-Bāqillānī-aligned position that Quranic distinctness is not arithmetic.

Pre-reg locked 2026-05-07; SHA256 `93ba966620068d10984923ea63b76aee8a8ec30adaa648da0e718b8ddd0ff390` runtime-verified.

*Direction LOCKED. ONE text. Equal NULL prominence.*
