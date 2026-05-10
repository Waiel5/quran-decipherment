---
finding_id: H-NEW-1740
title: COMPLETE 29-Surah al-Khalifa Muqaṭṭāʿat-Letter Audit — NULL
date: 2026-05-10
phase: B
verdict: NULL (al-Khalifa muqaṭṭāʿat-letter thesis FALSIFIED on complete catalogue)
pre_reg_sha: 5aae04c37cdb05742df2c78e292c89f98a6aede3068700f64cdd655a236b0516
seed: 20260509
n_perms: 10000
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)
data_source: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
parent_findings:
  - H-NEW-1600 (al-Khalifa 5-sub-claim audit; 1 CONFIRMED + 1 TRIVIAL + 3 FALSIFIED)
  - H-NEW-1530 (formal al-Khalifa 5-sub-claim audit; 3 CONFIRMED + 2 FALSIFIED)
  - H-NEW-1720 (al-Raḥmān + al-Raḥīm corpus distribution; 2 FALSIFIED)
  - H-NEW-1730 (inline muqaṭṭāʿat letter-count audit; 2 EXACT + 2 falsifies on sample-of-4)
---

# H-NEW-1740 — COMPLETE 29-Surah al-Khalifa Muqaṭṭāʿat-Letter Audit

## TL;DR

Across all **29 muqaṭṭāʿat-bearing surahs** in the Hafs-Kūfan canonical mushaf, the count of each surah's named muqaṭṭāʿ letter(s) is divisible by 19 in **1 out of 29 cases**. Expected under uniform null is **1.526**. Permutation p-value (10,000 perms) is **p = 0.7909**. The observed result is statistically indistinguishable from chance and, in fact, falls *below* the null expectation in nominal terms.

**Verdict: NULL.** Under the pre-registered three-bucket rule (k ≥ 5 = PATTERN, k = 3–4 = AMBIGUOUS, k ≤ 2 = NULL), the al-Khalifa muqaṭṭāʿat-letter-divisibility thesis is **decisively FALSIFIED on the complete catalogue**.

The H-NEW-1730 inline result (2 EXACT verifies from a sample of 4) was a **selection-effect cherry-pick** — al-Khalifa's published catalogue, when audited at full scope, contains exactly one true verify (Q 50 ق = 57 = 19×3), which is what one would expect from chance across 29 sub-claims.

## 1. The 29-surah catalogue and results

Counts under the locked rules-tuple (no-tashkeel, no whitespace, strict graphemes; alif ا strictly literal, no folding of أ/إ/آ/ٱ).

| # | Surah | Muqaṭṭaʿ | Letter(s) | Count | mod 19 | Hit? |
|---|-------|----------|-----------|------:|-------:|:----:|
| 1 | Q 2 | الم | ا,ل,م | 8,937 | 7 | – |
| 2 | Q 3 | الم | ا,ل,م | 5,143 | 13 | – |
| 3 | Q 7 | المص | ا,ل,م,ص | 4,742 | 11 | – |
| 4 | Q 10 | الر | ا,ل,ر | 2,158 | 11 | – |
| 5 | Q 11 | الر | ا,ل,ر | 2,095 | 5 | – |
| 6 | Q 12 | الر | ا,ل,ر | 2,000 | 5 | – |
| 7 | Q 13 | المر | ا,ل,م,ر | 1,339 | 9 | – |
| 8 | Q 14 | الر | ا,ل,ر | 1,061 | 16 | – |
| 9 | Q 15 | الر | ا,ل,ر | 787 | 8 | – |
| 10 | Q 19 | كهيعص | ك,ه,ي,ع,ص | 740 | 18 | – |
| 11 | Q 20 | طه | ط,ه | 242 | 14 | – |
| 12 | Q 26 | طسم | ط,س,م | 607 | 18 | – |
| 13 | Q 27 | طس | ط,س | 120 | 6 | – |
| 14 | Q 28 | طسم | ط,س,م | 577 | 7 | – |
| 15 | Q 29 | الم | ا,ل,م | 1,494 | 12 | – |
| 16 | Q 30 | الم | ا,ل,م | 1,119 | 17 | – |
| 17 | Q 31 | الم | ا,ل,م | 748 | 7 | – |
| 18 | Q 32 | الم | ا,ل,م | 511 | 17 | – |
| 19 | Q 36 | يس | ي,س | 261 | 14 | – |
| 20 | Q 38 | ص | ص | 29 | 10 | – |
| 21 | Q 40 | حم | ح,م | 439 | 2 | – |
| 22 | Q 41 | حم | ح,م | 319 | 15 | – |
| 23 | Q 42 | حم عسق | ح,م,ع,س,ق | 556 | 5 | – |
| 24 | Q 43 | حم | ح,م | 363 | 2 | – |
| 25 | Q 44 | حم | ح,م | 161 | 9 | – |
| 26 | Q 45 | حم | ح,م | 226 | 17 | – |
| 27 | Q 46 | حم | ح,م | 256 | 9 | – |
| 28 | **Q 50** | **ق** | **ق** | **57** | **0** | **YES** |
| 29 | Q 68 | ن | ن | 131 | 17 | – |

**Hit count: 1/29** (Q 50 ق = 57 = 19 × 3).

The folded-alif sensitivity column produced an identical 1/29 result (no الف-family count flips its mod-19 residue under the {ا,أ,إ,آ,ٱ} folding).

## 2. Observed-vs-expected statistical comparison

Under the uniform null P(count mod 19 = 0) = 1/19 ≈ 0.0526, the number of hits across 29 independent sub-claims follows a Binomial(29, 1/19) distribution with mean **1.526** and standard deviation **1.20**. The al-Khalifa hypothesis predicts 29/29 = all hits.

| Source | Expected hits | Observed |
|---|---:|---:|
| **Uniform null (1/19)** | **1.526** | — |
| **al-Khalifa "miracle of 19"** | **29** | — |
| **Observed in this audit** | — | **1** |

The observed value falls **slightly BELOW** the uniform-null expectation. Under a Binomial(29, 1/19) cumulative distribution, P(k ≤ 1) = 0.557, so observing 1 or fewer hits is unsurprising. The permutation null — which replaces the i.i.d. Binomial assumption with corpus-frequency-weighted letter draws preserving each surah's letter-length — also returns **p = 0.7909** for P(k_perm ≥ k_obs = 1), confirming the observed result is in the bulk of the null distribution.

**Permutation null hit-count distribution (10,000 perms):**

| k | Count | % |
|---:|------:|---:|
| 0 | 2,091 | 20.9% |
| 1 | 3,280 | 32.8% |
| 2 | 2,591 | 25.9% |
| 3 | 1,361 | 13.6% |
| 4 | 490 | 4.9% |
| 5 | 154 | 1.5% |
| 6 | 26 | 0.3% |
| 7 | 5 | 0.05% |
| 8 | 2 | 0.02% |
| ≥9 | 0 | 0.00% |

Observed k = 1 sits at the mode of the null. To clear the pre-registered PATTERN threshold (k ≥ 5), the audit would need to observe ~3× the null mean — and that threshold has empirical permutation-p < 0.02. The observed result clears no threshold.

## 3. Compound (cross-surah aggregate) counts

The dispatch directive included a secondary "compound count" analysis where letters are summed across all surahs whose muqaṭṭaʿ contains them (e.g., Q 2 + Q 3 + Q 29 + Q 30 + Q 31 + Q 32 for the الم-family, etc.).

| Family | Surahs | Letters | Total | mod 19 | Hit? |
|---|---|---|------:|-------:|:----:|
| الم-family | Q 2, 3, 29, 30, 31, 32 | ا,ل,م | 17,952 | 16 | – |
| المص (alone) | Q 7 | ا,ل,م,ص | 4,742 | 11 | – |
| الر-family | Q 10, 11, 12, 14, 15 | ا,ل,ر | 8,101 | 7 | – |
| المر (alone) | Q 13 | ا,ل,م,ر | 1,339 | 9 | – |
| كهيعص (alone) | Q 19 | ك,ه,ي,ع,ص | 740 | 18 | – |
| طه (alone) | Q 20 | ط,ه | 242 | 14 | – |
| طسم-family | Q 26, 28 | ط,س,م | 1,184 | 6 | – |
| طس (alone) | Q 27 | ط,س | 120 | 6 | – |
| يس (alone) | Q 36 | ي,س | 261 | 14 | – |
| ص (alone) | Q 38 | ص | 29 | 10 | – |
| **ص-combined** | **Q 7, 19, 38** | **ص** | **152** | **0** | **YES** |
| حم-family | Q 40–46 | ح,م | 2,112 | 3 | – |
| حم عسق (alone) | Q 42 | ح,م,ع,س,ق | 556 | 5 | – |
| **ق (alone)** | **Q 50** | **ق** | **57** | **0** | **YES** |
| ن (alone) | Q 68 | ن | 131 | 17 | – |

**Family hit count: 2/15** (Q 50 ق = 57 and ص-combined = 152, the two H-NEW-1730 reproductions).

Under uniform null with 15 family aggregates, expected hits = 15/19 = 0.79; observed 2/15 maps to Binomial(15, 1/19) one-tailed p ≈ 0.21. Compound aggregates also yield no statistically significant excess.

**Notably absent**: the الم-family (6 surahs combined: 17,952 letters) does NOT divide by 19; nor does the حم-family (7 surahs: 2,112). If al-Khalifa's claim were systematic, these large compound aggregates would be the most-stable targets and would most likely confirm. They do not.

## 4. Honest assessment — cherry-picking vs partial design vs chance

The H-NEW-1730 inline finding sampled four of al-Khalifa's claims and observed two EXACT verifies (Q 50 ق = 57 and ص-combined = 152). That looked like a partial pattern at the sample-of-4 level. The full 29-surah audit reveals:

1. **Only one surah-level claim verifies.** Q 50 ق = 57 = 19 × 3 is real. None of the other 28 sub-claims verifies.
2. **Only one cross-surah compound verifies.** ص-combined across Q 7 + Q 19 + Q 38 = 152 = 19 × 8 is real. None of the other 14 family aggregates verifies.
3. **Both H-NEW-1730 verifies survive replication;** they are reproducible facts, but they are isolated facts.
4. **The full catalogue is statistically chance-level.** Observed 1/29 sits at the mode of the permutation null distribution; the same is true of the family-level result (2/15 vs expected 0.79).

This pattern is the textbook signature of **selection-effect cherry-picking**: a numerologist surveying ~29–44 candidate facts and reporting only the ~2 that satisfy a numerical predicate. Under chance, ~1.5 of 29 will satisfy any random-modulus predicate; al-Khalifa's published catalogue retains the 2 that do, omits the 27 that do not, and presents the survivors as "the miracle".

**The Q 50 ق = 57 fact remains real, reproducible, and curious** — it has a structural explanation (Q 50 is highly ق-saturated thematically; see Q050-F-07 finding noting Q 50's ق-density rank 2/20 in the corpus). Q 50's count of ق happening to equal 19 × 3 may be an accidental harmonic of that thematic saturation, or it may be one of those individual instances of partial design that survives a chance-level catalogue. The data alone cannot distinguish.

**What the data CAN say definitively**: the al-Khalifa thesis — that the muqaṭṭāʿat-letter-counts are *systematically* organized as multiples of 19 — is FALSIFIED. The thesis predicts 29/29; observed is 1/29. The thesis is rejected at any reasonable significance threshold.

## 5. Cumulative al-Khalifa audit (H-NEW-1600 + 1530 + 1720 + 1730 + 1740)

| Sub-claim category | Cumulative empirical result |
|---|---|
| Pre-existing classical facts (basmala 19 letters, Q 1 = 29 words, 114 = 19×6) | 3/3 CONFIRMED (trivial / tautological) |
| Corpus-wide token counts (Allāh, al-Raḥmān, al-Raḥīm, Q 96 words, 6,236 verses div-19) | 0/5 — all FALSIFIED |
| Muqaṭṭāʿat surah-letter counts (this audit) | **1/29 — chance-level** |
| Muqaṭṭāʿat compound family-aggregate counts (this audit) | 2/15 — chance-level |

**Cumulative cumulative verdict**: 3 trivial-CONFIRMED + 0/5 corpus-wide-VERIFIED + 1/29 muqaṭṭāʿat-VERIFIED + 2/15 family-VERIFIED. **Total novel verifications: 1 surah-level + 1 family-level. Total novel falsifications: 33.** The al-Khalifa "miracle of 19" thesis is **decisively rejected** on its complete published catalogue.

This converges with H-META-1 (modern-numerology era: 0/10 confirmations; numerical-gematric substance type: 32% confirmation vs structural-formal 72%). H-NEW-1740 is the most-comprehensive empirical test of the al-Khalifa thesis in the project's audit history, and it returns chance-level results.

## 6. Garden-of-forking-paths log

- Pre-reg locked 2026-05-10; SHA `5aae04c37cdb05742df2c78e292c89f98a6aede3068700f64cdd655a236b0516`.
- Decision rule (≥5 PATTERN, 3–4 AMBIGUOUS, ≤2 NULL) was set BEFORE running any 29-letter count.
- Direction was locked: only excess-over-1.53 counted as evidence for H_A. Observed result was BELOW that, so no direction-flip is possible.
- Folded-alif sensitivity check (Section 6.2 of pre-reg) returned identical 1/29 — no rules-tuple sensitivity.
- The two H-NEW-1730 hits (Q 50 ق = 57 and ص-combined = 152) replicate; both enter the audit as designed.
- No mid-run methodology shifts.

## 7. MW-1..MW-7 compliance

- **MW-1 (instrument-prior):** letter-count metric and 1/19 null specified in pre-reg.
- **MW-2 (corpus-prior):** 10,000 permutations under corpus-frequency-weighted null. ✓
- **MW-3 (alternative-models):** strict-grapheme vs folded-alif sensitivity reported. ✓
- **MW-4 (over-fitting):** no fitted parameters; mod-19 is the only operation. ✓
- **MW-5 (replication):** H-NEW-1730's 2 EXACT verifies reproduce exactly. ✓
- **MW-6 (instrument-control):** the permutation null IS the instrument-control (corpus-distribution-matched, not the muqaṭṭāʿat-targets). ✓
- **MW-7 (post-hoc cap):** k_obs = 1 is the unambiguous outcome; no post-hoc tweaking possible. ✓

## 8. Cross-references and challenging priors

- [[h-new-1730-muqattaat-letter-count-audit|H-NEW-1730]] — sample-of-4 parent finding. H-NEW-1740 extends from 4 to 29 and changes the verdict from "MIXED" to "NULL".
- [[h-new-600-letter-families|H-NEW-600]] — muqaṭṭāʿat letter-family content-cohesion NULL. Convergent: muqaṭṭāʿat letters do NOT carry coherent content-cluster signature.
- [[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]] + Q050-F-07 — Q 50 is highly ق-saturated by thematic content (rank 2/20 in corpus ق-density). Q 50's ق-count being 57 = 19 × 3 may reflect that thematic saturation accidentally meeting a modulus condition.
- al-Khalifa, Rashad. *Quran: Visual Presentation of the Miracle* (Tucson: Islamic Productions, 1982); *Quran: The Final Testament* (1989).
- Philips, Bilal. *The Qurʾan's Numerical Miracle: Hoax and Heresy* (1987).
- H-META-1 — modern-numerology era 0/10 confirmation pattern.

## 9. Honest limits

- The audit is restricted to the strict Hafs-Kūfan no-tashkeel orthography. Alternative scripts (Warsh, Qālūn, Risan-recension) might yield slightly different counts at the margin; the audit DOES NOT exclude that al-Khalifa's original tabulations used a different reading-tradition for the variable letters. However: even granting al-Khalifa his preferred reading-tradition, the burden-of-proof is on him to specify it BEFORE counting, not after.
- Q 50 ق = 57 IS a real, reproducible fact under the audit's rules-tuple. It is not falsified. What is falsified is the **systematic** claim across the 29-surah catalogue.
- The ص-combined = 152 cross-surah fact is also real and reproducible. It is one of 15 family aggregates, all 14 others of which fail.
- The audit does not test al-Khalifa's full ~150-claim numerological corpus; it tests his muqaṭṭāʿat-letter sub-thesis. Other sub-claims (e.g., chapter-position numerical relationships) are addressed in prior findings H-NEW-1600 + 1530 + 1720.

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-1740-khalifa-muqattaat-complete-audit.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-1740.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1740.json`
- This finding: `findings/phase-b-hypotheses/h-new-1740-khalifa-muqattaat-complete-audit.md`
- Ledger entry: MASTER-FINDINGS-LEDGER.md §10.63

*Bismillāhi al-Raḥmāni al-Raḥīm.*
