---
surah: 6
test_id: Q006-F-02
title: Livestock-vocabulary cluster density — corpus rank for {anʿām, ḍaʾn, maʿz, ibl, baqar}
file_type: pre-registration
date_locked: 2026-05-07
seed: 20260507
bonferroni_k: 2
bonferroni_family: Q006-F-02-livestock-density
alpha_bon: 0.025
direction_locked: MAX
---

# Q006-F-02 — Pre-registration: Livestock-vocabulary cluster density

## 1. Hypothesis (locked before observation)

**H1 (one-tailed):** Q 6 al-Anʿām is the corpus-MAXIMUM on a 5-element livestock-cluster lexical-density metric using the canonical pre-Islamic livestock vocabulary {أنعام (anʿām), ضأن (ḍaʾn), معز (maʿz), إبل (ibl), بقر (baqar)}. The surah is named al-Anʿām after this lexical cluster; vv. 142-144 list the 8 paired-creature classifications (4 species × 2 sexes). H1 predicts the eponym is empirically anchored.

**Direction:** MAX (LOCKED) on both cells.

**H0:** Q 6 ranks ≥ rank 3 on livestock-vocabulary density.

## 2. Operational definition

**Lexical cluster (5 root-strings, locked surface-form regex with word-boundary):**
- أنعام / النعام / للأنعام / بالأنعام (lemma `nEm` family — surface variants of أنعام)
- ضأن / الضأن
- معز / المعز
- إبل / الإبل
- بقر / البقر / البقرة (excluding Q 2 al-Baqara as a self-eponym; we'll handle that note in §5)

**Per-surah metrics:**
- Cell A: `livestock_token_count` = total occurrences of any of the 5 cluster-terms.
- Cell B: `livestock_token_density` = livestock_token_count / total_words_in_surah (per-word density).

Bonferroni k=2, α_bon = 0.025.

## 3. Test statistic / Success / Failure

- **CONFIRMED:** Q 6 ranks 1/114 on EITHER Cell A or Cell B (with the other in top-3).
- **DIRECTIONAL:** Q 6 in top-3 on both.
- **NULL:** Q 6 ≥ rank 5 on the higher-ranked cell.
- **Pre-commit violation:** Q 6 ≥ rank 10 on the higher-ranked cell.

## 4. Garden-of-forking-paths log (BEFORE observation)

Author has read Q 6:142-144 (the paired-creature inventory) by eye. The 5 cluster-terms are confirmed present in those verses. Author has NOT computed corpus-wide rankings before this lock. The 5-element cluster is a literary-canonical set traceable to al-Ṭabarī's tafsir on Q 6:143 (cattle, sheep, goats, camels). Note: ḍaʾn / maʿz / ibl appear in very few corpus verses; the count statistic will be dominated by أنعام and بقر.

The pre-reg test does NOT include the Q 5:103 jāhilī-categories (baḥīra, sāʾiba, waṣīla, ḥām) — those are Q 5 hapaxes (per Q 6 overview §8) and are a separate lexical phenomenon.

## 5. Honest limits known a priori

- بقر (baqar) appears in Q 2 al-Baqara as the surah's own eponym; this may give Q 2 high livestock-density. Q 2's lexical density is therefore an a priori competitor on Cell A but Q 2 has 6,140 words vs Q 6's ~3,300, so density-per-word (Cell B) corrects for length. Test takes both cells.
- Surface-form regex misses inflectional forms (definite article variants, possessive suffixes); the regex is conservative (anchors on key roots).
- Single-token short surahs (e.g., Q 88, Q 105) might artificially win Cell B by length. We mitigate by requiring ≥ 3 tokens for Cell B ranking eligibility; surahs with <3 tokens are demoted to "tied at rank-bottom" for Cell B.

## 6. Rules-tuple

`(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. SHA256 lock

Computed at pre-reg-completion. Embedded into `surahs/scripts/Q006_F_02_livestock_density.py`.
