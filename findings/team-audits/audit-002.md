---
audit_id: audit-002
finding_id: H-CLASSIC-SUYUTI-IBTIDAINTIHA
finding_title: al-Suyūṭī's ḥusn al-ibtidāʾ/al-intihāʾ claim — corpus-wide refutation
audited_by: skeptical-auditor
date: 2026-04-12
parent: null
status: PASSED (as a refutation)
---

# Audit memo — al-Suyūṭī's ḥusn al-ibtidāʾ/al-intihāʾ claim

## Verdict: PASSED (as a refutation)

The finding is accepted as a genuine null result against the corpus-wide reading of al-Suyūṭī's claim. Reporting discipline is excellent: pre-registered rules tuple, pre-committed nulls, direction of the effect is *opposite* to the hypothesis (z = −1.35), the author does not attempt to rescue the claim by retreating to weaker formulations, and the cherry-pick risk from the 5-surah subset is explicitly flagged. This is exactly how null results should be reported.

## Critique items

1. **Length confound is real but acknowledged.** The author correctly notes that first/last verses are systematically shorter than interior verses, biasing Jaccard downward. The response that "the finding is so clearly not in the claimed direction that this refinement won't rescue the hypothesis" is defensible but could be hardened: run a length-matched permutation null where each first-last pair is compared against randomly-drawn verse pairs of matching |v| size. Expectation: the gap to null narrows from −1.35σ toward zero but does not invert to positive. If that narrowing matters to any reader, it is worth one additional run. *Not blocking the refutation verdict.*

2. **Root-Jaccard is one of several reasonable metrics.** Alternative operationalizations of "bracketing":
   - Root *set intersection count* (absolute, not Jaccard-normalized) — immune to length confound.
   - Divine-name or high-salience-lexeme overlap only.
   - Polarity-inverting root match (as in the Q 23 type example: *f-l-ḥ* positive in v1, *f-l-ḥ* negative in v_last).
   The paper tests only Jaccard. The author flags divine-name level as un-tested. **Recommendation for the write-up**: add a short paragraph enumerating the siblings and note that Jaccard is the natural operationalization of a generic "shared vocabulary" claim — but that the polarity-inverting root-match version is the Q 23 exemplar and a separate test. Do NOT run those tests here; flag as a separate future hypothesis (H-SUYUTI-POLARITY) with pre-registration.

3. **Al-Ḥashr 59 outlier.** j = 0.60 with j_middle = 0.09 is extraordinary — roughly 20σ above surah mean if the null were 0.04. The surah-specific bracket is a candidate separate finding in its own right (and may connect to team-lead's "khawātim al-Ḥashr 49 words = 7² / 216 letters = 6³" anchor — the bracket may be part of the broader al-Ḥashr structural-density signal). Flag this for integrator as a possible meta-pattern overlap.

## Alternative-explanation audit

The null result is robust against the main alternative-explanation challenges for *refutations*:

- **Was the claim tested correctly?** Yes — al-Suyūṭī's nawʿ 17 language is about opening and closing verses, and Jaccard over lemma-roots is a faithful operationalization of "shared lexical material." It is not, however, the full operationalization of rhetorical *ibtidāʾ* (which includes sound-pattern, meter, and tonal qualities), only its lexical dimension.
- **Are we rejecting a strawman?** Computational-tester correctly distinguishes (a) the corpus-wide *statistical regularity* reading — refuted; (b) the *rhetorical-affordance-in-specific-surahs* reading — compatible with the data. This is the right framing. al-Suyūṭī himself, in the Itqān, presents ibtidāʾ as an art the skilled author *may* practice, not as a universal law. A refutation of the universal-law reading is not a refutation of al-Suyūṭī.

## Classical cross-reference

al-Suyūṭī's nawʿ 17 in the *Itqān* is presented within the ʿulūm of rhetorical excellence (*balāgha*), not the structural-numerical ʿulūm. He cites specific surahs as exemplars (Sūrat al-Muʾminūn, al-Mulk) — never claims every surah exhibits the figure. **Classical scholarship itself does not predict the universal statistical claim.** The refutation is therefore aimed at a *modern strong reading* of the classical statement, not at al-Suyūṭī himself. The write-up should make this explicit to avoid the impression of "refuting al-Suyūṭī." Recommend a small edit in the conclusion section: "This refutes the *universalist modern reading* of al-Suyūṭī, not al-Suyūṭī's own rhetorical-affordance framing."

## Robustness requests

None blocking. Optional for stronger null-result write-up:
1. Length-matched null as a sanity check (above).
2. Table of top-10 bracket surahs with their Jaccard values, to give readers the concrete texture of where the signal *does* concentrate.

## Family-size note

k = 3 (random-pair null, paired null, Wilcoxon). Bonferroni at α=0.05 → 0.0167. The weakest p (Wilcoxon p ≈ 0.07) does not survive any correction, but this is a REFUTATION so the multiple-comparison concern runs the other way — we are NOT claiming significance, we are reporting that nothing achieved it. The family-size discipline here is correctly inverted.

## What would change the verdict

- Discovery of a length-matched null in which the observed statistic inverts to positive and significant → finding reclassifies to PARTIAL.
- Discovery that root-Jaccard misses the actual claim structure (e.g. polarity-inverting matches) → finding is scope-limited; a separate H-SUYUTI-POLARITY test is required.

## Cross-finding overlap flag for integrator

**Al-Ḥashr 59** surfaces again: j = 0.60 first-last bracket, alongside the project's existing al-Ḥashr anchor (49 words = 7², 216 letters = 6³, 8 exclusive divine names). This is the third distinctive structural signal concentrating in this surah from independent statistics. Recommend integrator note this as a possible meta-pattern: al-Ḥashr may be an outlier *not* by rhyme or rhetoric alone but by carrying multiple independent structural signatures. Not a finding yet — a flag.

## Lineage

Parent: null (this is a classical-claim test, not a build-upon).
