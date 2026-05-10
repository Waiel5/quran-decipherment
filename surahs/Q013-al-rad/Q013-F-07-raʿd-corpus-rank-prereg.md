---
surah: 13
test_id: Q013-F-07
title: raʿd-substring corpus rank — pre-registered direction that Q 13 ranks #1 among 114 surahs on raʿd-density
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
verdict_ceiling: PASS-DIRECTED (single replication required for promotion)
classical_anchor: al-Rāzī, *Mafātīḥ al-ghayb* on Q 13:13 *yusabbiḥu al-raʿdu bi-ḥamdihi* — the surah is NAMED for the al-raʿd lexeme via this verse; classical naming conventions treat the eponymous lexeme as the surah's signature.
direction_of_effect: LOCKED — Q 13 ranks #1 among all 114 surahs on (count of رعد substring matches) and #1 on (count / surah-word-count). The corpus contains only 2 attestations of the substring; both pre-reg cells must place Q 13 at rank-1.
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  text_source: quran-text/quran-no-tashkeel.json
  basmala_policy: counted-only-in-surah-1
---

# Q013-F-07 — Pre-registration: raʿd-substring corpus rank

## 1. Origin

al-Raʿd (الرعد) is the surah's eponymous lexeme. The brief asks for a corpus-rank test: in 6,236 verses across 114 surahs, where does Q 13 rank on (a) raw raʿd-substring count and (b) length-normalized raʿd-density?

The hypothesis is that the eponymous-naming convention is empirically anchored: the surah is named for a lexeme that is corpus-rare and concentrated in the surah itself. This is a TYPE-A eponymous test (per the project's naming-survey schema).

## 2. Hypothesis

**H1 (Cell A — raw count):** Q 13 has the highest raw count of رعد substring matches across all 114 surahs.

**H1 (Cell B — length-normalized):** Q 13 has the highest (raʿd-count / surah-word-count-no-tashkeel) across all 114 surahs.

**H0:** Some other surah has higher raw count or higher density.

**Direction (both cells):** Q 13 = rank 1. LOCKED.

## 3. Cluster definition

- Target lexeme: substring `رعد` in the no-tashkeel verse text.
- Surahs scanned: all 114.
- Word count denominator: count of whitespace-delimited orthographic tokens in `quran-text/quran-no-tashkeel.json` for each surah.

## 4. Test design

### Cell A — raw count

For each surah s ∈ {1..114}, compute `count_s = Σ_verses (count of 'رعد' substring matches)`. Pre-committed direction: Q 13 has the corpus-maximum.

### Cell B — length-normalized density

For each surah s, compute `density_s = count_s / words_s × 1000` (raʿd-occurrences per 1,000 words). Pre-committed direction: Q 13 has the corpus-maximum density.

### Cell C — permutation null (to dramatize the asymmetry)

The lexeme is corpus-rare: prior inspection finds 2 corpus attestations. Run a uniform-shuffle null: permute the 6,236 verses' raʿd-status across surahs 10,000 times, holding the verse-count distribution fixed. For each permutation, compute the rank of Q 13 on Cell A. Report the fraction of permutations with rank-of-Q-13 ≤ 1.

This is an MW-6 instrument-control: it quantifies whether Q 13's rank-1 status would be expected by chance given the rarity of the lexeme.

## 5. Bonferroni and significance

**Bonferroni-k = 2** (Cell A raw count + Cell B density). α_bon = 0.025 per cell.

For Cells A and B: direction-pass requires Q 13 = rank-1; significance is by descriptive corpus enumeration (the rarity of the lexeme makes this a near-deterministic test if direction holds).

For Cell C: PASS if p_perm(rank ≤ 1) ≤ 0.025.

## 6. Honest limits

- The raʿd lexeme is *rare* corpus-wide (substring `رعد` ≤ 2 occurrences anticipated). A rank-1 finding for Q 13 is interesting more for its absolute concentration than for marginal advantage over a runner-up — there is essentially no runner-up.
- The eponymous-naming convention is a *classical sociology* of surah-naming, not an inherent textual property. The finding tests whether the convention is empirically grounded for Q 13 specifically.
- The substring search captures `رعد` (raʿd, thunder) but does NOT distinguish derivational forms (e.g., possessive endings). Q 13:13 contains `الرعد` (the article-prefixed form); Q 2:19 contains `ورعد` (the wa-conjunction-prefixed form). Both forms contain the substring `رعد`.

## 7. Pre-commit violations

If Q 13 does NOT achieve rank-1 in either Cell A or Cell B, the pre-committed direction has failed and the finding is published as NULL — DIRECTION REVERSED with full prominence.
