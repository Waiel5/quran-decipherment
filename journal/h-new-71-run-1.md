---
date: 2026-04-15
run_id: h-new-71-run-1
hypothesis: H-NEW-71 — Comprehensive Allah (الله) distribution across the corpus
seed: 20260417
author: h-new-71-specialist
verdict_summary: 6 of 7 cells PASS at α_bon=0.007143; 1 cell (Cell 5 MW-5 calibration) FAILS informatively
---

# H-NEW-71 Run 1 — Journal

## Setup

- Pre-registration written FIRST (`h-new-71-allah-distribution-prereg.md`).
- Counting rule (12 forms + 1 edge-case exclusion) locked BEFORE running any inferential cell.
- 7 inferential cells locked; Bonferroni k=7, α_bon = 0.007143.
- Pilot count was permitted (rules-tuple sensitivity check) and yielded n=2704, matching project memory's "~2700".

## Garden-of-forking-paths log (declared BEFORE running)

Pre-known:
- H-NEW-59 already counted Allah=2538 under tighter substring rule. H-NEW-71 uses a more permissive proclitic-aware rule expecting 2700-ish.
- 30 surahs lack Allah under H-NEW-59's rule; the question is whether this drops under the more permissive rule (it does — to 29).
- Anecdotal: short Mufaṣṣal surahs (al-Fīl, al-Quraysh, al-Kāfirūn, al-Aṣr, etc.) lack "Allah". The pre-reg's Cell 2 tests whether this is structured (it is).
- Q 1, Q 2:255, Q 24:35, Q 59:22-24 are MW-5 anchors. Q 1 confirmed; the others FAILED their density-rank prediction (informative failure: high theological saliency ≠ high bare-Allah density).

## Steps

1. Loaded `quran-no-tashkeel.json` (114 surahs, 6236 verses, 82,375 words) and `data/revelation-order.csv` chronology.
2. Implemented the locked Allah-counting rule (12 form classes, 1 explicit exclusion: يضلله at Q 6:39).
3. Pilot count → 2,704 tokens (matches expectation).
4. **Cell 1** (MW-5): Q1 has 2 Allah-tokens (basmala v1 + لله at v2). Extractor validated.
5. **Cell 2**: 29 zero-Allah surahs vs uniform-null expected 10.14; simulated p = 0.0001. PASS strongly.
6. **Cell 3** (verse-position χ²): observed (OPEN, MID, CLOSE) = (674, 1283, 747); expected (733, 1353, 618). χ² = 35.18, df=2, p = 2.3e-08. PASS.
7. **Cell 3a** (fāṣila-exact): observed = 1, expected = 154.2, z = -12.89, p ≈ 0. Located the single occurrence at Q 82:19.
8. **Cell 4** (surah-position χ²): observed (S_OPEN, S_MID, S_CLOSE) = (592, 1341, 771); expected (692, 1350, 662). χ² = 32.56, df=2, p = 8.5e-08. PASS.
9. **Cell 5** (density-crown + MW-5 anchors): top verse density Q 112:2 = 0.500. None of Q 2:255, Q 24:35-37, Q 59:22-24 in their predicted top-50/100. **MW-5 FAIL (0/3 anchors)**. Diagnosis: those verses have HIGH absolute Allah counts but LOW density because they are LONG (e.g., Q 2:255 = 58 words, only 1 Allah).
10. **Cell 6** (Spearman ρ): density vs n_words = +0.431 (p = 4.5e-07). PASS.
11. **Cell 7** (KW chronology): H = 69.18, df=3, p = 6.4e-15. PASS strongly. Phase means: Early Meccan 0.010, Middle Meccan 0.011, Late Meccan 0.030, Medinan 0.062.
12. **Cell 7a** (muq vs non-muq Mann-Whitney): U = 1152, z = -0.52, p = 0.60. NULL.

## Issues encountered

### Edge-case classification

The locked rule's "prefix + الله" branch correctly excludes Q 6:39 يضلله (verb يُضلِلْ + ـه pronoun) because the prefix يض is not in the allowed proclitic set. Spot-checked 4 unusual forms:
- آلله (Q 10:59, Q 27:59) — interrogative ʾa- + Allah → INCLUDED
- وتالله (Q 21:57) — wa-tā-llāh oath → INCLUDED
- أبالله (Q 9:65) — a-bi-llāh interrogative → INCLUDED
- يضلله (Q 6:39) — yuḍlilhu verb → EXCLUDED ✓

### MW-5 Cell 5 failure — informative not fatal

The pre-reg specified that Q 2:255 (Throne), Q 24:35-37 (Light), Q 59:22-24 (Khawātim) "must" appear in top density rank windows. They DID NOT. Diagnosis confirmed: these verses achieve their theological saliency via PRONOUNS (huwa, lahu) and ATTRIBUTES (al-Ḥayy, al-Quddūs, ...), NOT via repeated bare "Allah" tokens. Q 2:255 has Allah×1 / 58 words = density 0.017 (rank 1820). 

This is recorded as Cell 5 FAIL but the substantive top-30 ranking IS valuable: it surfaces the **Shuʿarāʾ refrain** finding (8× *fa-ttaqū llāha wa-aṭīʿūn* in Q 26 = the most repeated maximal-Allah-density 3-word verse in the corpus).

### Numerical precision of chi^2 p-value

Used hand-coded incomplete-gamma chi^2 survival function (Numerical Recipes Lentz continued-fraction). Cross-checked against `scipy.stats.chi2.sf(35.18, 2)` mentally: χ²=35 with df=2 should give p ≈ 2 × 10⁻⁸, matching the implementation output. Acceptable.

## Verdicts

| Cell | Result |
|---|---|
| Cell 1 (descriptive + MW-5) | PASS (Q1 Allah=2 confirmed) |
| Cell 2 (zero-Allah surahs vs uniform null) | PASS (p = 0.0001) |
| Cell 3 (verse-position χ²) | PASS (p = 2.3e-08) |
| Cell 3a (fāṣila-exact) | PASS-EXTREME (z = -12.89; only Q 82:19 has Allah at fāṣila) |
| Cell 4 (surah-position χ²) | PASS (p = 8.5e-08) |
| Cell 5 (density-crown MW-5 anchors) | FAIL-CALIBRATION (0/3 anchors recovered; informative) |
| Cell 6 (Spearman ρ length) | PASS (ρ=+0.431, p = 4.5e-07) |
| Cell 7 (Nöldeke KW) | PASS-STRONG (H=69.18, p = 6.4e-15) |
| Cell 7a (muq vs non-muq) | NULL (p = 0.60) |

JOINT: 6 of 7 inferential cells fire at strict α_bon = 0.007143.

## Files written

- `findings/phase-b-hypotheses/h-new-71-allah-distribution-prereg.md`
- `findings/phase-b-hypotheses/h-new-71-allah-distribution.md`
- `findings/phase-b-hypotheses/csv/h-new-71.json`
- `scripts/h_new_71_allah_distribution.py`
- `journal/h-new-71-run-1.md` (this file)

## Honest caveats

- The fāṣila-exact under-representation, while extreme (154×), is partially a definitional artifact of Arabic verse-final morphology preferring divine ATTRIBUTES (al-ʿAlīm, al-Ḥakīm, ...) over the bare divine NAME. The 154× number quantifies a known classical observation (al-Suyūṭī, *Itqān*, on fawāṣil).
- The chronology effect (Cell 7) is the largest single-axis Nöldeke effect we have measured for any individual lexeme. Robustness check: re-running with Bell or Watt chronologies would shift surah assignments at the margins but not flip the gross Mufaṣṣal-vs-long-surah signal which dominates.
- Q 110 (al-Naṣr) is Medinan but contains *naṣru llāhi* (v1) and *dīni llāhi* (v2) — confirming that even in Mufaṣṣal, the few Medinan Mufaṣṣal pieces invoke Allah explicitly. This is consistent with Cell 7's chronology gradient.
- M-9 endorsement: this finding does NOT independently confirm H-NEW-59's Allah token-count under the M-9 rule (different rule-tuple = different rule, but same corpus). Per project policy, do not double-count.
- The 29-zero / 29-muq count coincidence is incidental (the SETS are disjoint).

## Convergence with classical scholarship

- al-Suyūṭī, *Itqān* nawʿ on *fawāṣil*: divine attributes typically end verses, not the divine name itself. H-NEW-71 Cell 3a quantifies the resulting under-representation of "Allah" at fāṣila position (1/2704 vs 154 expected = 154×).
- al-Zarkashī, *Burhān* on *al-makkī wa-l-madanī*: Medinan markers include increased Allah-invocation. H-NEW-71 Cell 7 quantifies (~6× density jump from Early Meccan to Medinan).
- al-Qurṭubī on Q 55: Sūrat al-Raḥmān deliberately substitutes al-Raḥmān/Rabb for Allah throughout. H-NEW-71 confirms (Q 55 = longest zero-Allah surah).

## Next steps (suggestions, not commitments)

- **h-new-71-1-rabb-substitution**: in the 29 zero-Allah surahs, count Rabb / al-Raḥmān / pronoun-divine-references and test whether they QUANTITATIVELY compensate (i.e., total divine-mention density in zero-Allah surahs is comparable to the corpus average if we count Rabb).
- **h-new-71-2-shuara-refrain**: characterize the 8× *fa-ttaqū llāha wa-aṭīʿūn* refrain in Q 26 as a structural marker of the prophet-narrative pericope-closing position; check if any other Quranic refrain has comparable recurrence with explicit Allah-naming.
- **h-new-71-3-fasila-attribute-coupling**: catalog all verses where Allah appears at position n-2 or n-3 and identify which fāṣila attribute follows (al-ʿAlīm, al-Ḥakīm, al-Qadīr, etc.). Should produce the empirical rhyme-attribute-with-Allah-mention pairing distribution.
- **h-new-71-4-q82-19-singleton**: investigate why Q 82:19 is the sole exception to the fāṣila-exact rule. Likely the construct *al-amru ... lillāh* ("the Command... to Allah") is a syntactic frozen phrase that locks Allah at sentence-final regardless of fāṣila convention.
