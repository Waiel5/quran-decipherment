---
audit_id: audit-016
target_finding: team-discovery-015 (H-SUYUTI-BRACKETING)
auditor: skeptical-auditor
date: 2026-04-12
verdict: PASSED AS NULL (finding honestly reported; framing needs tightening)
parent_finding: task #3 al-Suyūṭī ḥusn al-ibtidāʾ/al-intihāʾ pre-reg
cc: integrator
---

# Audit-016 — al-Suyūṭī ḥusn al-ibtidāʾ/intihāʾ: null result accepted

## Verdict: PASSED AS NULL

Sub-A's pre-registered test — within-surah verse-order permutation null — is exactly the right null for the bracketing claim (it preserves length, topic, and verse-set, isolating only positional specificity). The Stouffer Z = -0.024 against this null is a genuinely null result: v_1↔v_last root-Jaccard matches what you'd expect if (v_1, v_N) were a random pair within the surah. No blockers, but framing needs tightening on two axes and Sub-B1/B2 should be de-weighted.

## Why this null passes where H-NEW-1's did not

Critical contrast for the ledger. audit-015 just corrected audit-001 where the null retrained the model on shuffled data. **This null does not retrain anything.** It shuffles verse order within a surah and recomputes the exact same Jaccard statistic. That is a clean positional-permutation null: if the classical claim ("positions 1 and N have elevated overlap") is true, the real v_1↔v_N Jaccard should exceed the v_i↔v_j Jaccard at random positions (i, j). It doesn't. The null is valid and the result is interpretable.

**Positive-control sanity check (non-blocking recommendation):** run the same test on a corpus known to have bracket structure — e.g., a hand-selected 100-line text with deliberate anaphora/inclusio. If Stouffer Z > 0 there, the null passes positive-control. I recommend this be done once and reused across future bracketing-style tests. Q1 (which is excluded here) is actually the known-positive case in the Quran itself; Sub-C's hand-tagging of Q1 would double as positive control.

## Blockers: none

## Framing edits requested (non-blocking but should land before ledger write)

**F1. The "REFUTED" headline overclaims.** Pre-reg direction was positive (bracket > interior); observed Stouffer Z = -0.024 is *null*, not *anti-bracket*. Sub-A permutation null correctly accounts for this. The Wilcoxon z=-3.02 is measured against zero (not against permutation), so it reflects "the average delta is slightly negative" — but this is expected under null by the mean-of-one-pair vs mean-of-many-pairs variance asymmetry (see F2), not evidence of anti-bracketing. Suggested headline:

> "al-Suyūṭī's ḥusn al-ibtidāʾ/intihāʾ **not detected at root-Jaccard level** (Stouffer Z = -0.024). The positional-permutation null is exactly matched — v_1↔v_N root-overlap is indistinguishable from random same-surah pairs."

**F2. Wilcoxon z=-3.02 is a statistical artifact, not a finding.** The deltas are `J(v_1, v_N) - mean(J(v_i, v_j) over ~N²/2 interior pairs)`. A single-pair-minus-mean-of-many-pairs statistic is skewed negative by construction: the distribution of a single Jaccard sample has heavier right tail than its mean, so the difference skews left even under the null. Wilcoxon against zero picks this up. Recommend removing "significantly below zero — anti-bracket direction" framing and noting the construction artifact explicitly. Permutation Stouffer Z is the correct statistic and it says null.

**F3. Sub-B1/B2 should be de-weighted as underpowered, not as failures.**
- Sub-B1 (negation density): tests whether first+last have elevated negation vs interior pairs. Same single-pair-vs-many asymmetry as F2; z=-1.41 is consistent with null under that asymmetry. Non-informative.
- Sub-B2 (antonym bridges): 27-pair catalog with 0 observed bridges. This is a **power failure**, not a refutation. Most surahs' first and last verses don't contain root tokens from a 27-pair hand-selected list — this is expected even if antonym bracketing is common at a broader semantic level. The finding correctly notes "either catalog too small or instrument mismatched" but the headline framing ("3 sub-tests all fail Bonferroni") treats B2 as evidence when it's truly uninformative.

Recommend reporting Sub-A as the principal adjudication, and treating B1/B2 as "test not decisive under this instrument." Keep the Bonferroni k=3 for honesty, but note that B2 has zero observations so it contributes essentially no independent evidence.

## The differential-pattern headline is strong and should be emphasized

The differential pattern computational-tester flagged is the most important finding here, not the Suyūṭī result itself:

- al-Rāzī linear adjacent-verse overlap: Z = +30.76 (CONFIRMED, pending block-null audit-011 revision)
- al-Biqāʿī seam adjacent-surah-boundary overlap: Z = +10.06 (CONFIRMED audit-014)
- al-Suyūṭī first↔last-verse bracket overlap: Z = -0.024 (NULL — this finding)

**Quran has local lexical cohesion; it does NOT have long-range intra-surah lexical bracket cohesion at root-Jaccard level.** This is a genuinely non-obvious empirical pattern and is the principal scientific content of team-discovery-015. Recommend this be the headline, not the Suyūṭī refutation.

## Classical-scholarship framing (M-5-relevant)

This is a third instance of the M-5 pattern (classical doctrine operationalized one way, fails; reformulation required):

- al-Suyūṭī's *Itqān* nawʿ 58-59 exemplars are rhetorical figures (anaphora, radd al-ʿajuz ilā al-ṣadr, envelope-structure), NOT lexical-root recurrence. The literal "ḥamd ... ḍāllīn" bracket in Q1 is itself a *semantic-field* bracket (praise/guidance), not necessarily a root-overlap bracket.
- The current test operationalizes "bracketing" as root-Jaccard similarity, which is an instrument choice the classical source does not make.
- Under M-5: the literal root-Jaccard operationalization is REFUTED; reformulation as rhetorical-figure tagging (Sub-C, delegated to classical-scholar) or as semantic-field overlap (LLM-judge version) may yet survive.

**M-5 CANDIDATE implication:** if classical-scholar's Sub-C rubric-tagging confirms the rhetorical-form bracketing in a subset of surahs, this becomes the third closed literal-refutation-plus-reformulation-survival loop (after al-Biqāʿī ring→seam and pending Kirmānī aṣl/farʿ), crossing the 2-loop promotion gate by itself if Sub-C confirms before Task #40.

Recommend Sub-C be prioritized.

## Strengths (logged)

- Null model is correct for the claim as operationalized; no null-artifact risk.
- Pre-registered criteria, clean Bonferroni k=3.
- Honest handling of B2 sparsity (catalog-too-small vs instrument-mismatch disjunction).
- Differential framing against al-Rāzī and al-Biqāʿī seam is exactly the right scientific framing — this is the second within-project differential adjudication after team-discovery-013's Biqāʿī ring-vs-seam.
- Q1 exclusion honest with sensitivity note (Q108 inclusion doesn't change result).

## What would change the verdict (none, but clarifying)

There is no "PASSED" upgrade for a null result — null is null. But the following would convert this from "NULL under root-Jaccard operationalization" to positive evidence in the *other* direction:

1. **Sub-C rhetorical-rubric bracketing** (classical-scholar): if ≥ 40% of surahs show Suyūṭī-rubric-detectable bracketing, the rhetorical form survives even as the lexical form doesn't — which is the M-5 reformulation-survival path.
2. **LLM-judge semantic-field bracketing**: Q1 ḥamd↔ḍāllīn is a clear positive; a semantic-similarity version would pick it up where root-Jaccard doesn't.
3. **Include Q1 explicitly**: exclusion of Q1 removes the strongest a priori case. A sensitivity run including Q1 + Q108 + Q112 should be computed and reported (author notes Q108 inclusion barely shifts numbers but doesn't report Q1).

## Meta-pattern notes

**M-1 (surah-outlier registry):** possible candidate for "surahs that DO show bracketing." If some individual surah z-scores are > +2.58 under the permutation null, those are M-1 candidates. Recommend computational-tester extract the per-surah z-score distribution from `null_stouffer_z_per_surah` and identify the right-tail.

**M-6 (pericope-block substrate):** orthogonal — this is a surah-scale long-range claim, not a within-surah chain claim.

**M-5 (classical-doctrine operationalization vs recovery):** strengthened. Three literal-refutation instances now (Biqāʿī ring, Kirmānī directionality, Suyūṭī lexical bracket). Two reformulation-survival paths partially open (Biqāʿī seam closed, Suyūṭī Sub-C rhetorical not yet run, Kirmānī Task #40 not yet run).

## Action for computational-tester

1. Update finding headline to "NULL under root-Jaccard operationalization" rather than "REFUTED."
2. Note Wilcoxon z=-3.02 as statistical artifact of single-pair-vs-mean-of-many-pairs asymmetry, not anti-bracket direction.
3. De-emphasize Sub-B2 — it is underpowered, not a refutation.
4. Promote the differential-pattern headline (local yes, long-range-intra-surah no) to the lead.
5. Add sensitivity run including Q1.
6. Extract per-surah right-tail z-scores for M-1 candidate surahs.

## Action for integrator

1. Log as NULL (not REFUTED) under MASTER:suyuti-bracketing.
2. Register differential pattern (local cohesion YES, intra-surah long-range bracketing NO) as a candidate §1 entry — this is a second within-project differential after Biqāʿī ring-vs-seam.
3. Route Sub-C (rhetorical-rubric tagging) to classical-scholar as high priority — it's the potential M-5 loop closure.
4. Add Q1 sensitivity run as follow-up task.
