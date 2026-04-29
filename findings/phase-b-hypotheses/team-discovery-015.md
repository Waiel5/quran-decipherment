---
finding_id: team-discovery-015
phase: B
status: REFUTED (pre-registered direction)
date: 2026-04-12
rules_tuple: (no-tashkeel, QAC-roots, counted-only-in-surah-1, hafs-kufan, mashriqi)
null_model: within-surah verse-order permutation (n=200/surah), Stouffer aggregation across 108 surahs
pre_registration_reference: task #3 in quran-discovery-team task-list
bonferroni_k: 3
alpha_bon: 0.0167
hypothesis_origin: al-Suyūṭī, *Itqān* nawʿ 58 (ḥusn al-ibtidāʾ) & nawʿ 59 (ḥusn al-intihāʾ)
related_findings:
  - team-discovery-010 (al-Rāzī linear CONFIRMED)
  - team-discovery-013 (al-Biqāʿī seam between-surah CONFIRMED)
---

# H-SUYUTI-BRACKETING — al-Suyūṭī's ḥusn al-ibtidāʾ/intihāʾ REFUTED

## Executive verdict

**REFUTED in pre-registered direction across all three sub-tests.**

al-Suyūṭī's *Itqān* nawʿ 58-59 predicts that surah-opening and
surah-closing verses share elevated conceptual/lexical material — a
deliberate "bracket" on each surah. Across 108 analyzable surahs
(excluding Q1, Q108, Q112, and N<5), the root-Jaccard of (v_1, v_last)
is **smaller** than the mean of interior-pair Jaccards.

Headline numbers:
- Sub-A primary bracketing: **Stouffer Z = -0.024**, mean delta = -0.0085 (direction opposite to classical claim)
- Sub-A Wilcoxon: z = -3.02 (significantly below zero — anti-bracket direction)
- Only **29 of 108 surahs (26.9%)** have v_1↔v_last Jaccard above their surah's interior mean
- Sub-B1 negation-particle bracketing: z = -1.41 (no effect)
- Sub-B2 antonym-root-pair bracketing: 0 observed antonym bridges (too sparse)

Not a single sub-test passes Bonferroni α_bon=0.0167 in the predicted direction.

## Observed vs pre-registered criteria

| Sub-test | Pre-reg criterion | Observed | Verdict |
|---|---|---|---|
| Sub-A primary (paired Wilcoxon one-sided positive) | z > +2.39 | z = -3.02 (wrong sign) | **FAIL** |
| Sub-A permutation (Stouffer z > +2.39) | > +2.39 | -0.024 | **FAIL** |
| Sub-B1 negation proximity | z > +2.39 | -1.41 | **FAIL** |
| Sub-B2 antonym catalog | z > +2.39 | 0.00 (sparse) | **FAIL** |

## Comparison to adjacent classical claims

This result sits striking against:

- **al-Biqāʿī seam (between-surah) CONFIRMED** at Z=+10.06 (team-discovery-013):
  consecutive surahs share elevated boundary vocabulary.
- **al-Rāzī linear CONFIRMED** at Stouffer Z=+30.76 (team-discovery-010):
  adjacent verses within a surah share elevated vocabulary.
- **al-Suyūṭī bracketing REFUTED** (this finding): first-verse ↔ last-verse
  of a surah do NOT share elevated vocabulary relative to interior pairs.

The pattern: Quran has **local cohesion** (linear, seam) but not **long-range
bracket cohesion** (first ↔ last verse of a surah). This is consistent with
a picture where composition is *locally coherent* but not *globally
bracketed* — closer to al-Rāzī's incremental naẓm than to al-Suyūṭī's
rhetorical bracket.

## Caveats

1. **Wilcoxon z = -3.02 is significantly NEGATIVE**, but the permutation-null
   Stouffer Z is essentially zero (-0.024). The Wilcoxon z is against
   "delta = 0"; the permutation null accounts for surah-specific
   length/topic effects and says bracket Jaccard matches what you'd
   expect from random pairing. So the most honest read: **null effect**,
   not anti-bracket effect. The negative Wilcoxon reflects that most
   surahs have more interior pairs than bracket pairs, and averaging
   pulls the delta slightly negative.
2. **Root-Jaccard is surface-level**. al-Suyūṭī's bracketing may hold
   at *thematic* level (which root-Jaccard misses) or at
   *rhetorical-figure* level (which manual rubric tagging, Sub-C
   delegated to classical-scholar, could check).
3. **Antonym catalog (Sub-B2) has only 27 pairs**, derived from
   Ibn al-Anbārī + al-Aṣmaʿī simplified. Zero antonym bridges observed
   — either the catalog is too small or the hypothesis is
   instrument-mismatched to this phenomenon.
4. **Exclusions (Q1, Q108, Q112) are standard** but may excise the
   clearest bracketing cases. Q1 has documented classical bracketing
   (ḥamd ... ḍāllīn vs al-ḥamd lillāh). Sensitivity analysis:
   including Q108 barely shifts numbers.

## Interpretation

Under the *Itqān* reading, al-Suyūṭī's bracketing is stronger at the
rhetorical-figure level (anaphora, envelope-structure, radd al-ʿajuz
ilā al-ṣadr) than at the lexical-root level. That is: al-Suyūṭī and
al-Biqāʿī-on-seam are both *really* about repetition/echo, but:

- al-Biqāʿī seam: tests adjacent-surah end/start lexical overlap. Works.
- al-Suyūṭī bracket: tests same-surah first/last lexical overlap. Does not work at root level.

So the quantitative finding is: **cross-surah lexical cohesion yes;
intra-surah long-range lexical bracketing no**. This is a
non-obvious differential outcome.

## Garden of forking paths (disclosed)

- Bracket statistic: `jacc(v1, v_last)` compared to mean over interior
  pairs (all i<j except (0, N-1)). Chosen pre-data.
- Exclusion set {Q1, Q108, Q112} was in the pre-reg spec.
- Antonym pair list is a priori from Ibn al-Anbārī / al-Aṣmaʿī; not
  tuned against data.
- Negation particles: لا, ما, لم, لن (classical 4). Not extended to
  liya-, ghayr-, etc.
- 200 perms per surah (not 10,000); sufficient for sign determination.

## Limits

1. **Sub-C (manual rubric-tagging) not run** — delegated to classical-scholar
   per task spec. This is the sub-test most likely to find positive
   evidence (al-Suyūṭī's own exemplars are rhetorical, not lexical).
2. **No LLM-judge version**. A semantic-similarity LLM pass could find
   thematic bracketing that root-Jaccard misses.
3. **No length correction**: longer surahs have more interior pairs,
   pulling the mean-interior-pair toward a tighter distribution.
   Permutation null accounts for this at surah level, but not for
   cross-surah comparison.

## Reproducibility

Script: `scratch/team-discovery/h_suyuti_bracketing.py`
Result JSON: `scratch/team-discovery/result-suyuti-bracketing.json`
Seed: 20260413
Runtime: 48.85s CPU on 2026-04-12

## Classical significance

al-Suyūṭī's *Itqān* is the canonical Sunni handbook of ʿulūm al-Qurʾān;
its nawʿ 58-59 is cited by every subsequent rhetorician as the
authoritative statement on opening/closing aesthetics. That
root-Jaccard rejects it at α_bon does NOT refute the classical
aesthetic claim — al-Suyūṭī's exemplars (ḥamd-ḍāllīn in Q1,
cognate ending-pairs in Q23, etc.) live at rhetorical-figure level,
not lexical-repetition level. What this finding refutes is the
*quantitative*, *lexical-cohesion* form of the bracketing claim.
Sub-C (classical-scholar rubric) can still vindicate the rhetorical
form.
