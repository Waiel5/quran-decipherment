---
finding_id: H-NEW-1740
type: pre-registration
date_locked: 2026-05-10
phase: B
status: PRE-REGISTERED
seed: 20260509
n_perms: 10000
parent_findings:
  - H-NEW-1600 (al-Khalifa 5-sub-claim audit; 1 CONFIRMED + 1 TRIVIAL + 3 FALSIFIED)
  - H-NEW-1530 (formal al-Khalifa 5-sub-claim; 3 CONFIRMED + 2 FALSIFIED)
  - H-NEW-1720 (al-Raḥmān + al-Raḥīm corpus distribution; 2 FALSIFIED)
  - H-NEW-1730 (inline muqaṭṭāʿat letter-count audit; 2 EXACT + 2 falsifies, sample-of-4)
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)
data_source: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
---

# Pre-Registration — H-NEW-1740 COMPLETE 29-Surah al-Khalifa Muqaṭṭāʿat Letter-Count Audit

## 1. Background and motivation

H-NEW-1730 (inline, §10.62 of MASTER-FINDINGS-LEDGER) sampled four of al-Khalifa's muqaṭṭāʿat-letter divisibility-by-19 claims:

| Surah | Letter(s) | Observed | Khalifa claim | Verdict |
|---|---|---|---|---|
| Q 50 | ق | 57 | 57 = 19×3 | EXACT verify |
| Q 38+7+19 (combined) | ص | 152 | 152 = 19×8 | EXACT verify |
| Q 68 | ن | 131 | div 19 | FALSIFIED (mod = 17) |
| Q 38 (alone) | ص | 29 | div 19 | FALSIFIED (mod = 10) |
| Q 42 | ع+س+ق | 208 | div 19 | FALSIFIED (mod = 18) |

That sample gave 2 EXACT / 4 named sub-claims, an outwardly suspicious 50% rate against a uniform-null expectation of ~5.3%. But sample-of-four is too small to distinguish "real partial pattern" from "selection-effect cherry-pick".

H-NEW-1740 closes that gap by enumerating ALL 29 muqaṭṭāʿat-bearing surahs in the Hafs-Kūfan canonical mushaf, and computing the count of the surah's named muqaṭṭāʿ letter(s) inside that surah.

## 2. Hypothesis (PRE-COMMIT)

**Null hypothesis (H₀, the project's default):** the count of named-muqaṭṭāʿ-letter(s) in each surah is not designed to be divisible by 19. Under uniform null, P(count mod 19 = 0) = 1/19 ≈ 0.05263, so the expected number of hits across 29 independent sub-claims is **29 / 19 ≈ 1.526**.

**Alternative hypothesis (H_A, al-Khalifa's hypothesis):** the Quran's muqaṭṭāʿat letter-count system is uniformly divisible by 19, so the expected number of hits is **29/29 = 29** (all verify).

**Direction (LOCKED):** observed-hits > 1.526 in the direction of more-than-chance. Test is one-tailed (only "exceeds-chance" counts as evidence for H_A; below-chance simply corroborates H₀).

## 3. Decision rule (PRE-COMMIT)

Three-bucket pre-registration (threshold for the 29-surah catalogue, scaled from the 14-letter framing in the dispatch — 29 sub-claims, exp 1.53 under null):

| Observed hits k | Verdict |
|---|---|
| k ≥ 5 | **PATTERN** — observed substantially exceeds chance; promote to formal Code-19 partial-rehabilitation; pre-register a follow-up replication test under alternative rules-tuples |
| k = 3 or 4 | **AMBIGUOUS** — above chance but within range where multiple comparisons could be cherry-picked; publish as DIRECTIONAL with explicit pre-commit-honoring statement |
| k ≤ 2 | **NULL** — observed is at or near chance expectation; the al-Khalifa "miracle of 19" muqaṭṭāʿat-letter thesis is FALSIFIED on the complete catalogue |

**Garden-of-forking-paths note:** these thresholds are set BEFORE running. The two H-NEW-1730 confirmed hits (Q 50 and combined Q 7+19+38 ص) are pre-existing within the catalogue; they enter the count if and only if reproduced on the rules-tuple specified above.

## 4. Permutation null and p-value computation

For each of the 29 sub-claims, compute:
1. **Letter inventory** of the surah under the locked rules-tuple (no-tashkeel, no whitespace, no diacritics).
2. **Observed count** of the named muqaṭṭāʿ letter(s).
3. **Hit indicator** = 1 if (observed mod 19 == 0), else 0.

Aggregate:
- **Total hits k_obs** across the 29 sub-claims.

For the permutation null (MW-2 compliance), permute the letter-positions within the full Quran corpus 10,000 times under a uniform null, redrawing each surah's letters from the corpus-wide letter-frequency distribution scaled to the surah's total letter-count. For each permutation, recompute k. Report the proportion of permutations with k ≥ k_obs as the permutation p-value.

Seed = 20260509 (project-standard seed for 2026-05-09 dispatch wave; locks reproducibility).

## 5. The 29-surah catalogue (LOCKED before computation)

| # | Surah | Muqaṭṭaʿ | Named letter(s) (unique) |
|---|---|---|---|
| 1 | Q 2 | الم | ا, ل, م |
| 2 | Q 3 | الم | ا, ل, م |
| 3 | Q 7 | المص | ا, ل, م, ص |
| 4 | Q 10 | الر | ا, ل, ر |
| 5 | Q 11 | الر | ا, ل, ر |
| 6 | Q 12 | الر | ا, ل, ر |
| 7 | Q 13 | المر | ا, ل, م, ر |
| 8 | Q 14 | الر | ا, ل, ر |
| 9 | Q 15 | الر | ا, ل, ر |
| 10 | Q 19 | كهيعص | ك, ه, ي, ع, ص |
| 11 | Q 20 | طه | ط, ه |
| 12 | Q 26 | طسم | ط, س, م |
| 13 | Q 27 | طس | ط, س |
| 14 | Q 28 | طسم | ط, س, م |
| 15 | Q 29 | الم | ا, ل, م |
| 16 | Q 30 | الم | ا, ل, م |
| 17 | Q 31 | الم | ا, ل, م |
| 18 | Q 32 | الم | ا, ل, م |
| 19 | Q 36 | يس | ي, س |
| 20 | Q 38 | ص | ص |
| 21 | Q 40 | حم | ح, م |
| 22 | Q 41 | حم | ح, م |
| 23 | Q 42 | حم عسق | ح, م, ع, س, ق |
| 24 | Q 43 | حم | ح, م |
| 25 | Q 44 | حم | ح, م |
| 26 | Q 45 | حم | ح, م |
| 27 | Q 46 | حم | ح, م |
| 28 | Q 50 | ق | ق |
| 29 | Q 68 | ن | ن |

**Letter-orthography note:** ا (bare alif) ≠ أ / إ / آ. Per the rules-tuple, no-tashkeel is the source text; counts are over orthographic graphemes as they appear in the no-tashkeel text. Hamzated and madda-alif variants are NOT folded into bare alif unless the no-tashkeel text already renders them as bare ا. This decision is LOCKED before computation.

**Alif variants (sensitivity check):** to be honest about the orthographic ambiguity in the alif family, the script will also report a sensitivity column with ا folded across {ا, أ, إ, آ, ٱ}. The PRIMARY verdict uses strict-grapheme; the folded-alif column is REPORTED but does not enter the primary k_obs.

## 6. Secondary analyses (PRE-COMMIT but NOT part of primary verdict)

### 6.1 "Compound count" / cross-surah aggregation (per dispatch directive)

For each unique muqaṭṭaʿ letter (or letter-combo), sum its count across all surahs whose opening muqaṭṭaʿ contains it:

| Family | Surahs | Letter(s) summed |
|---|---|---|
| الم-family | Q 2, 3, 29, 30, 31, 32 | ا + ل + م across all six |
| المص (Q 7 alone) | Q 7 | ا + ل + م + ص |
| الر-family | Q 10, 11, 12, 14, 15 | ا + ل + ر across all five |
| المر (Q 13 alone) | Q 13 | ا + ل + م + ر |
| كهيعص (Q 19 alone) | Q 19 | ك + ه + ي + ع + ص |
| طه (Q 20 alone) | Q 20 | ط + ه |
| طسم-family | Q 26, 28 | ط + س + م across both |
| طس (Q 27 alone) | Q 27 | ط + س |
| يس (Q 36 alone) | Q 36 | ي + س |
| ص (Q 38 alone) | Q 38 | ص |
| ص-combined (H-NEW-1730) | Q 7, 19, 38 | ص across all three |
| حم-family | Q 40, 41, 42, 43, 44, 45, 46 | ح + م across all seven |
| حم عسق (Q 42 alone) | Q 42 | ح + م + ع + س + ق |
| ق (Q 50 alone) | Q 50 | ق |
| ن (Q 68 alone) | Q 68 | ن |

Each family-aggregate is reported with its mod-19 residue. The compound analysis is **DESCRIPTIVE / REPORTED but NOT part of the primary 29-surah hit count**; it is an exploratory layer for honest reporting.

### 6.2 Sensitivity: hamza-folded alif

For all الم / الر / المص / المر / كهيعص counts that include ا, also report counts under the folded set {ا, أ, إ, آ, ٱ}. Whichever direction the hits shift, both numbers are tabulated for honest disclosure.

## 7. Pre-committed honesty constraints

- All 29 sub-claims are computed and tabulated, regardless of which way each verdict falls.
- The 2 prior H-NEW-1730 hits (Q 50 and ص-combined) are NOT counted twice; the catalogue treats Q 50 as one sub-claim (ق) and Q 7, Q 19, Q 38 each individually as sub-claims for their own opener letters (not pre-combined). The ص-combined family aggregate appears in section 6.1, separately.
- The full mod-19 residue distribution across the 29 sub-claims is reported. The shape of that distribution is checked against the uniform expectation (1.53 per residue class on average).
- Honest limit: **even k=5 does not prove design** under multiple-comparison considerations across the al-Khalifa corpus of claims; it would warrant only a follow-up rules-tuple stability test.
- Equal NULL prominence: if k ≤ 2, the cumulative al-Khalifa verdict (now spanning H-NEW-1600 + 1530 + 1720 + 1730 + 1740) is reported as a single concluding paragraph with at least 4 falsified components named.

## 8. Reproducibility

- Script: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/scripts/h-new-1740.py`
- JSON output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-1740.json`
- Finding: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-1740-khalifa-muqattaat-complete-audit.md`
- Pre-reg SHA embedded in script header; script computes its own re-hash and fails fast on mismatch.

## 9. Cross-references (anchor priors)

- al-Khalifa, *Quran: Visual Presentation of the Miracle* (1982); *Quran: The Final Testament* (1989) — primary-source claims.
- Bilal Philips, *The Qur'an's Numerical Miracle: Hoax and Heresy* (1987) — counter-critique.
- H-META-1 (modern-numerology era, 0/10 confirmations; numerical-gematric substance 32% confirmation vs structural-formal 72%).
- [[h-new-600-letter-families|H-NEW-600]] — muqaṭṭāʿat letter-family content-cohesion NULL.
- [[h-new-1730-muqattaat-letter-count-audit|H-NEW-1730]] — direct parent finding.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
