---
finding_id: H-NEW-1810
title: Corpus-wide Arabic letter frequency + muqaṭṭāʿat-14 overlap audit
phase: B+
date: 2026-05-10
rules_tuple: (no-tashkeel, grapheme-count, Hafs-Kūfan, basmala-as-v.1-of-Q1-only)
seed: 20260509
prereg_sha256: b6b4eeac2b8015cf447805c2494070d2042b7af2a71b9157f4580c941b61533f
verdict: MIXED — T1 PASS, T2-strong FALSIFIED (10/14, not 14/14), T2-weak NULL after Bonferroni (p=0.0285 > α_bon=0.0167), T3 PASS
---

# H-NEW-1810 — Corpus-wide Arabic letter frequency + muqaṭṭāʿat-14 overlap audit

## Headline

The al-Suyūṭī strong-form claim that the 14 muqaṭṭāʿat letters are EXACTLY the top-14 letters of the Qurʾānic corpus by frequency is **FALSIFIED**. Empirical overlap is **10/14**, not 14/14. Four muqaṭṭāʿat letters (**ح س ص ط**) sit OUTSIDE the corpus top-14, and four non-muqaṭṭāʿat letters (**ب ت ف و**) sit INSIDE it. Under Bonferroni-corrected α=0.0167 (k=3 family), the hypergeometric one-tailed p=0.0285 also fails to reject the null of random 14-from-28 sampling.

The **weaker form** of the claim — that muqaṭṭāʿat letters are predominantly from the high-frequency end — is empirically supported: T1 confirms the corpus is highly non-uniform (top-3 = 37.9% of mass) and T3 confirms the muqaṭṭāʿat-14 collectively cover 74.4% of all letter-graphemes in the corpus despite being only 50% of the alphabet. This is a real concentration in absolute terms (1.49× over uniform expectation) but it is NOT a Qurʾān-specific signature: cross-corpus baselines (al-Bukhārī ḥadīth, Ibn Hishām *Sīra*, al-Jāḥiẓ *Ḥayawān*, al-Mutanabbī, Imruʾ al-Qays) all show muqaṭṭāʿat-14 cumulative frequencies of 71.6%-73.6% with 9-10 letter overlaps to the muqaṭṭāʿat-14 set. The pattern is a property of **Arabic language**, not the Qurʾān specifically.

## Pre-registered tests and verdicts

| Test | Description | Threshold | Observed | Verdict |
|:--|:--|:--|:--|:--|
| **T1** | Top-3 letters' summed rel freq > 0.25 (LOCKED HIGH) | > 0.25 | **0.3790** | **PASS** |
| **T2 strong** | muqaṭṭāʿat-14 ≡ top-14 (set-identity) | k=14 | **k=10** | **FALSIFIED** |
| **T2 weak** | hypergeom P(X ≥ k=10 \| N=28,K=14,n=14), α_bon=0.0167 | p < 0.0167 | **p=0.0285** | **NULL** |
| **T3** | muqaṭṭāʿat-14 summed rel freq > 0.50 (LOCKED HIGH) | > 0.50 | **0.7441** | **PASS** |

## Corpus-wide letter frequency table (no-tashkeel, Hafs-Kūfan, normalized 28-letter)

**Total**: 329,131 letter-graphemes across 6,236 verses, 114 surahs. Standalone hamza ء = 1,578 (tracked separately, not in 28-letter alphabet per al-Suyūṭī Itqān convention).

| Rank | Letter | Count | Rel freq | In muqaṭṭāʿat-14? |
|:-:|:-:|:-:|:-:|:-:|
| 1 | ا (alif) | 59,280 | 0.1801 | ✓ |
| 2 | ل (lām) | 38,191 | 0.1160 | ✓ |
| 3 | ن (nūn) | 27,270 | 0.0829 | ✓ |
| 4 | م (mīm) | 26,735 | 0.0812 | ✓ |
| 5 | ي (yāʾ) | 25,747 | 0.0782 | ✓ |
| 6 | و (wāw) | 25,486 | 0.0774 | ✗ |
| 7 | ه (hāʾ) | 14,850 | 0.0451 | ✓ |
| 8 | ت (tāʾ) | 12,864 | 0.0391 | ✗ |
| 9 | ر (rāʾ) | 12,403 | 0.0377 | ✓ |
| 10 | ب (bāʾ) | 11,491 | 0.0349 | ✗ |
| 11 | ك (kāf) | 10,497 | 0.0319 | ✓ |
| 12 | ع (ʿayn) | 9,405 | 0.0286 | ✓ |
| 13 | ف (fāʾ) | 8,747 | 0.0266 | ✗ |
| 14 | ق (qāf) | 7,034 | 0.0214 | ✓ |
| 15 | س (sīn) | 6,012 | 0.0183 | **✓ muq, OUT** |
| 16 | د (dāl) | 5,991 | 0.0182 | ✗ |
| 17 | ذ (dhāl) | 4,932 | 0.0150 | ✗ |
| 18 | ح (ḥāʾ) | 4,140 | 0.0126 | **✓ muq, OUT** |
| 19 | ج (jīm) | 3,317 | 0.0101 | ✗ |
| 20 | خ (khāʾ) | 2,497 | 0.0076 | ✗ |
| 21 | ش (shīn) | 2,124 | 0.0065 | ✗ |
| 22 | ص (ṣād) | 2,072 | 0.0063 | **✓ muq, OUT** |
| 23 | ض (ḍād) | 1,686 | 0.0051 | ✗ |
| 24 | ز (zāy) | 1,599 | 0.0049 | ✗ |
| 25 | ث (thāʾ) | 1,414 | 0.0043 | ✗ |
| 26 | ط (ṭāʾ) | 1,273 | 0.0039 | **✓ muq, OUT** |
| 27 | غ (ghayn) | 1,221 | 0.0037 | ✗ |
| 28 | ظ (ẓāʾ) | 853 | 0.0026 | ✗ |

## The 4 displacements (where al-Suyūṭī's strong claim breaks)

| Muqaṭṭāʿat letter OUT of top-14 (rank > 14) | Non-muqaṭṭāʿat letter IN top-14 (rank ≤ 14) |
|:--|:--|
| س (sīn) — rank 15, 0.0183 | و (wāw) — rank 6, 0.0774 |
| ح (ḥāʾ) — rank 18, 0.0126 | ت (tāʾ) — rank 8, 0.0391 |
| ص (ṣād) — rank 22, 0.0063 | ب (bāʾ) — rank 10, 0.0349 |
| ط (ṭāʾ) — rank 26, 0.0039 | ف (fāʾ) — rank 13, 0.0266 |

The displacements are NOT marginal. و and ت outrank multiple muqaṭṭāʿat letters by 4-12× in absolute frequency. ط in particular sits at rank 26 of 28 — near the absolute bottom of the corpus, yet it opens Q 20 (ṭāhā), Q 26 (ṭāsīm), Q 27 (ṭāsīn), Q 28 (ṭāsīm).

The al-Suyūṭī claim, in its strong reading, predicts the muqaṭṭāʿat letters were SELECTED for their high frequency. The empirical reality is that several muqaṭṭāʿat letters are LOW-frequency, and several high-frequency letters are NEVER muqaṭṭāʿat. The selection criterion, if any, is therefore NOT pure corpus frequency.

## Cross-corpus descriptive context (NOT pre-committed)

For each of 5 reference corpora from `data/baseline-corpora/letter-freqs.csv`, normalized to the same canonical 28-letter alphabet:

| Corpus | k_overlap (muq-14 ∩ top-14) | muq-14 cumulative freq | Top-14 letters |
|:--|:-:|:-:|:--|
| **Qurʾān (this work)** | **10/14** | **0.7441** | ا ل ن م ي و ه ت ر ب ك ع ف ق |
| Bukhārī (no-Qurʾān) | 9/14 | 0.7359 | ا ل ن ي ب م ع ر و ه ت د ق ف |
| Ibn Hishām *Sīra* | 9/14 | 0.7343 | ا ل ي ن م ب و ه ر ت ع ف ق د |
| al-Jāḥiẓ *Ḥayawān* | 10/14 | 0.7208 | ا ل ي و ن م ر ت ب ه ع ف ق ك |
| al-Mutanabbī | 9/14 | 0.7188 | ا ل ي م و ن ت ر ب ه ف ك ع د |
| Imruʾ al-Qays | 9/14 | 0.7159 | ا ل ي م ت ن ر و ب ع ف ه ك د |

**Key observation**: The Qurʾān shows the HIGHEST muq-14 cumulative freq (0.7441) and ties with al-Jāḥiẓ for HIGHEST overlap (10/14). But the gap from the Bukhārī / poetry baseline is 1-3 percentage points — a margin of degree, not a categorical Qurʾān-specific signature. The muq-14 set is a property of the Arabic *language* (specifically: ا ل م ن ي ه ر ك ع ق are core to almost any Arabic text), and the muqaṭṭāʿat selection captures most of them.

What does NOT carry over: the 4 displaced muqaṭṭāʿat letters (ح س ص ط) are low-frequency in ALL corpora — not just the Qurʾān. So al-Suyūṭī's strong claim fails universally on classical Arabic, not just here.

## Interpretation

The al-Suyūṭī observation in *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 6 — that the 14 muqaṭṭāʿat letters are "half the alphabet" representing "the high-frequency letters" — is partially correct:

- **Vindicated**: the 14 muqaṭṭāʿat letters cover 74.4% of total grapheme mass (well above the 50% uniform baseline); the Qurʾān is highly non-uniform; the top-3 alone capture 37.9% of mass.
- **Falsified**: the muqaṭṭāʿat-14 set is NOT the top-14 by frequency in the Qurʾān. Four medium-low-frequency letters (ح س ص ط) are included; four high-frequency letters (ب ت ف و) are excluded.

The 4-displacement structure suggests the muqaṭṭāʿat letter selection was driven by some criterion OTHER than (or IN ADDITION to) pure frequency. Candidates:
1. **Phonetic-articulation balance**: the 14 letters span a deliberate range of articulation points (pharyngeal ح ع ʿ, emphatic ص ط, sibilants س ص, etc.) such that no major articulation point is omitted.
2. **Specific theological-semiotic associations** of individual letters (e.g., ق with judgment in Q 50, ص with Ṣād, ن with ink/calamus per Q 68).
3. **Numerical-abjad constraints** (the 14 letters sum to specific abjad values).
4. **Pre-Islamic alphabetic-magical tradition** (cf. Welch 1957, Goossens 1923 — the 14 may track an older Aramaic/Syriac-derived 14-letter mystical-alphabet substrate; OUTSIDE-DATA, flagged as such).

This finding does NOT resolve which of these alternatives is correct. It DOES rule out the simplest "the 14 are the most-common letters" reading.

## Honest limits

1. **Normalization sensitivity**: Reasonable alternative normalizations (e.g., counting ة separately from ت, counting ى separately from ي, counting hamza-bearers as letters distinct from ا/و/ي) could shift 1-2 letters in/out of the top-14. The locked normalization follows al-Suyūṭī Itqān nawʿ 6 alphabetic convention (28 letters; hamza-bearers consolidated with their seats).
2. **The al-Suyūṭī claim is qualitative**: the strict set-equality reading is the strongest empirical instantiation; al-Suyūṭī may have meant something weaker (e.g., "the muqaṭṭāʿat draw heavily from the high-frequency portion of the alphabet"), which IS supported.
3. **The hypergeometric weak-form is borderline**: p=0.0285 fails Bonferroni α=0.0167 (k=3 family) but would pass single-test α=0.05. The 10/14 overlap is genuinely informative as a descriptive fact, even if the formal null-rejection fails after correction.
4. **Cross-corpus shows the pattern is Arabic-general**: this is the most important honest-limit. The high cumulative-frequency of muq-14 in the Qurʾān is shared with classical Arabic prose and pre-Islamic poetry. The muqaṭṭāʿat selection captures a property of the language, not of the text.
5. **Per-surah and per-revelation-period letter-frequency tables** are NOT computed here; they may show more structure (e.g., per-Meccan-period or per-rhyme-class shifts in letter inventory).

## Cross-finding integration

- **H-NEW-1730** (al-Khalifa muqaṭṭāʿat letter-count audit MIXED): the 2 confirmed-EXACT counts (Q 50 ق=57=19×3; Q 7+19+38 ṣ=152=19×8) involve letters ق (rank 14, the cusp) and ص (rank 22, low). The al-Khalifa div-by-19 claims attach to specific muqaṭṭāʿat-letter counts; the present finding does not bear on the div-by-19 question but it does establish that ص is structurally low-frequency in the corpus.
- **H-NEW-1600 / H-NEW-1530 / H-NEW-1720 / H-NEW-1740** (Code-19 falsification series): consistent with the present falsification of the strong-form al-Suyūṭī claim — both showcase that simple frequency-equality claims about the Qurʾān often fail at strict precision.
- **H-NEW-113 (letter-position), H-NEW-151 (single-letter-muq char-4gram), H-NEW-600 (letter families), H-NEW-88 (letter-set predictor), H-NEW-97 (name-letter joint), H-NEW-24 (letter-ordering suppression)**: the letter-axis findings cluster. H-NEW-1810 provides the foundational frequency anchor; the rank-1 ا (alif) at 18% and rank-2 ل (lām) at 11.6% are the dominant features.
- **al-Biqāʿī muqaṭṭāʿat content-munāsaba**: already FALSIFIED in 4 replications. H-NEW-1810 adds independent evidence that the muqaṭṭāʿat letter-axis is NOT a frequency-axis either.

## Pre-commit compliance

- Pre-reg SHA `b6b4eeac2b8015cf447805c2494070d2042b7af2a71b9157f4580c941b61533f` verified at runtime.
- T1 direction LOCKED HIGH; observed HIGH; PASS.
- T2 strong-form k=14 LOCKED; observed k=10; FALSIFIED — no direction reversal (overlap is a count, not a signed quantity); strong-form NULL is the honest verdict.
- T3 direction LOCKED HIGH; observed HIGH; PASS.
- No post-hoc threshold adjustments.

## Cross-references

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 6 (al-ḥurūf al-muqaṭṭaʿa) — primary source for the strong-form claim tested.
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, kitāb 23 — secondary corroboration of the 14-letter set membership.
- `data/baseline-corpora/letter-freqs.csv` — pre-computed cross-corpus letter frequencies; cross-checked against this run.
- [[h-new-1730-muqattaat-letter-count-audit|H-NEW-1730]] — Khalifa muqaṭṭāʿat-letter-count audit MIXED.
- [[h-new-1600-khalifa-six-claims|H-NEW-1600]], [[h-new-1530-khalifa-allah-count|H-NEW-1530]], [[h-new-1720-khalifa-divine-names|H-NEW-1720]] — Code-19 falsification series.
- [[h-new-113-letter-position|H-NEW-113]], [[h-new-151-single-letter-muq-char4gram|H-NEW-151]], [[h-new-600-letter-families|H-NEW-600]] — adjacent letter-axis findings.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
