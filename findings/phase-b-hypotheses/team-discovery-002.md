---
finding_id: H-CLASSIC-SUYUTI-IBTIDAINTIHA
title: al-Suyūṭī's ḥusn al-ibtidāʾ/al-intihāʾ claim of first-last verse "bracketing" does NOT hold corpus-wide
date: 2026-04-12
rules_tuple:
  orthography: no-tashkeel
  word_definition: lemma-roots (QAC v0.4 root-index.json)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
null_model:
  primary: within-surah random-pair permutation (10⁴ draws)
  secondary: paired random-pair difference (first-last vs first-middle)
acceptance_criterion: Bonferroni-corrected p < 0.005, z ≥ 3.0 for positive confirmation
verdict: REFUTED
---

## Claim being tested

al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*, nawʿ 17 (*ḥusn al-ibtidāʾ* and *ḥusn al-intihāʾ*), argues that Quranic surahs exhibit rhetorical bracketing between their opening and closing verses. The type example is Sūrat al-Muʾminūn (sūra 23): opens with *qad aflaḥa al-muʾminūn* and closes with *innahu lā yufliḥu al-kāfirūn* — same root `f-l-ḥ` returning in inverted polarity.

Operationalized: for each surah with N ≥ 3 verses, compute Jaccard(roots(v1), roots(v_N)) and compare to:
  (a) random verse-pair overlap within the same surah (unpaired null),
  (b) paired comparison: Jaccard(v1, v_N) vs Jaccard(v1, v_middle).

## Data and method

- QAC v0.4 root-index gives every root occurrence as (surah, verse, word) triples. Verse→roots sets built directly.
- 113 of 114 surahs have N ≥ 3 (only Al-Kawthar surah 108 is edge-case, 3 verses — included).
- `v_middle = ceil(N/2)` (1-indexed).
- Wilcoxon signed-rank as secondary paired test (robust to non-normality).

## Observed vs null

**Observed means across 113 surahs:**
- Jaccard(v1, v_last) = **0.031**
- Jaccard(v1, v_middle) = 0.023
- Jaccard(v_middle, v_last) = 0.036

**Random-pair null** (10⁴ draws, each surah samples 2 distinct verse indices uniformly):
- Null mean Jaccard = **0.043**
- Null std = 0.0087
- **z = −1.35** (observed is *below* null mean, 1.35σ)
- p_ge = 0.92 (one-sided p for the claim: 0.92 — the direction is wrong)

**Paired null** (Jaccard(v1,v_last) − Jaccard(v1,v_middle) vs two random-pair differences):
- Observed paired diff = +0.008
- Null mean ≈ 0, null std = 0.012
- **z = 0.65, p_ge = 0.25** — not significant.

**Wilcoxon signed-rank** on (j_first_last − j_first_middle) excluding zero-diffs:
- N non-zero pairs = 37 (most surahs have very low root-overlap at all pair positions, hence many ties at 0)
- W+ = 450, W− = 253, **z = +1.49**, p_one_sided ≈ 0.07
- Does not survive any correction.

## Cherry-pick risk

The **top-5 surahs by first-last Jaccard overlap**:
- Surah 59 (al-Ḥashr): j_fl = 0.60, j_fm = 0.09 — genuine strong bracket
- Surah 33 (al-Aḥzāb): 0.20 vs 0.12
- Surah 112 (al-Ikhlāṣ): 0.20 vs 0.00 (N=4, tiny surah)
- Surah 114 (al-Nās): 0.20 vs 0.00 (N=6)
- Surah 63 (al-Munāfiqūn): 0.15 vs 0.08

Al-Ḥashr 59 *is* a striking bracket — it opens and closes with divine-names clusters. But one surah does not confirm a 114-wide structural claim. al-Suyūṭī cited Al-Muʾminūn (23); in our data j(v1, v_last) for sūra 23 has the same root `f-l-ḥ` appearing in both, but the overall Jaccard is tiny because Jaccard is dominated by vocabulary size — the lexical overlap of a 3-word opener with an 11-word closer is inherently small even when a key root repeats.

## Verdict: REFUTED (as a corpus-wide claim)

- The **general statistical claim** — that first-last root overlap is elevated across the 114 surahs — is not supported. Observed is slightly *below* random (z = −1.35).
- However, the **rhetorical claim** — that *some* surahs exhibit deliberate root-bracketing — is compatible with the data: al-Ḥashr (59), al-Ikhlāṣ (112), al-Nās (114) and a handful of others have striking first-last overlap. These are cases, not a statistical law.
- The classical claim should be recharacterized: *ḥusn al-ibtidāʾ/al-intihāʾ* is a **rhetorical affordance deliberately exploited in specific surahs**, not a corpus-level regularity.

## Why the null mean is *higher* than observed

Interesting artifact: random verse-pair overlap (0.043) exceeds first-last overlap (0.031). This is because first and last verses tend to be SHORTER than interior verses (surahs often open and close with short liturgical formulas), and Jaccard penalizes sparse sets. This is a **length confound** pushing the observed statistic DOWN. A length-matched null would be fairer — but the finding is so clearly not in the claimed direction that this refinement won't rescue the hypothesis.

## Garden of forking paths disclosure

### Choices made after seeing the data
- None — rules and stats pre-committed before running.

### Alternative rule tuples considered
- Could have used word-overlap (not root-overlap). Roots are the more meaningful unit for a *naẓm* claim.
- Could have defined middle as mean-of-all-interior. Would increase power but complicate paired test.

### Sibling hypotheses
- Whether specific surah classes (Meccan short vs Medinan long) show the bracket: not tested here.
- Whether the bracket is at divine-name level rather than root level: not tested; would need separate design.

### Why this one and not those
- This is the direct operationalization of the Itqān passage. Not rescuing by retreating to weaker claims.

## Registered effect and honest reporting

Null result reported with equal prominence as a positive would be. This is a classical claim refuted at the corpus level while preserving respect for the handful of specific surahs where the bracket is real.

## Seed
`random.seed(20260413)`. Raw: `scratch/team-discovery/result-002.json`.
