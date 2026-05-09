---
finding: Q052-F-02
title: "Q 52 al-Ṭūr non-muqaṭṭāʿat surah carries corpus-rare writing-cluster vocabulary in vv. 2-3 with corpus-hapax tokens *raqq* + *manshūr*-as-parchment-qualifier"
seed: 20260509
date_locked: 2026-05-09
prereg_locked_before_results: true
bonferroni_k: 2
bonferroni_family: Q052-F-02-writing-cluster
alpha_bon: 0.025
direction_pre_registered: true
---

# Q052-F-02 PRE-REG: Q 52's vv. 2-3 *kitāb masṭūr fī raqqin manshūr* is a corpus-EXACT writing-medium description in a non-muqaṭṭāʿat surah

## 1. Hypothesis (pre-locked)

**H1**: The 4-token combination *kitāb* + *masṭūr* + *raqq* + *manshūr* in Q 52:2-3 is **corpus-unique** — appearing nowhere else in the Quran in this combined form.

**H2**: At least one of {*raqq*, *manshūr* (in writing-medium sense)} is a CORPUS-HAPAX surface-form across 6,236 verses.

**H1, H2 → JOINT FINDING**: Q 52 belongs in the cross-finding-008 / H-NEW-53 book-introduction-marker exception class — it is a non-muqaṭṭāʿat surah that carries scripture-self-reference vocabulary in vv. 2-3 at exceptional density (containing 1+ corpus-hapax + a corpus-unique 4-token combination).

## 2. Test statistic and operationalization

### H1 — corpus-uniqueness of 4-token combination

For each verse v in the corpus, check whether v.text contains all 4 of: {*kitāb*, *masṭūr*, *raqq*, *manshūr*} as substring matches (no-tashkeel). Count the number of verses where all 4 substrings appear. PASS if count == 1 (i.e. only Q 52:2-3 jointly contain the 4-token cluster).

Alternative formulation: across the 6,236 verses, look for the substring sequence *masṭūr* + *raqq* + *manshūr* (since *kitāb* is too common — 261 occurrences). PASS if Q 52:2-3 is the ONLY verse-pair containing all 3 of {masṭūr, raqq, manshūr}.

### H2 — corpus-hapax check

For each of {*raqq*, *manshūr*} as surface-token (no-tashkeel; with all wa-/fa-/al-/bi- prefixes stripped to base form), count corpus occurrences. PASS if at least one of the two has count ≤ 1 (i.e. corpus-hapax) OR if both have count ≤ 3 (i.e. corpus-rare).

## 3. Pass criteria

- **H1**: PASS if combined 4-token cluster appears in ≥ 0 verses outside Q 52:2-3 — strictly corpus-unique to Q 52:2-3 sequence.
- **H2**: PASS if at least one of {*raqq*, *manshūr*} is corpus-hapax (count == 1) OR both are corpus-rare (count ≤ 3).

Joint H1+H2 PASS = the writing-cluster vocabulary in Q 52:2-3 is corpus-EXACT in this combination AND involves at least one corpus-hapax. Both must pass for the CONFIRMED verdict.

## 4. Rules tuple

- text source: `quran-text/quran-no-tashkeel.json`
- substring search: case-insensitive, no-tashkeel; all wa-/fa-/al-/bi-/li- prefixes considered as boundary-prefixes.
- definition of *raqq*: the standalone word رق (in v.3 as the writing-medium = parchment).
- definition of *manshūr*: the standalone word منشور OR root-derivatives in writing-context (n-sh-r is broader; we look at surface form منشور only for H2 hapax-test).
- inclusion: all 114 surahs, all 6,236 verses.

## 5. Bonferroni declaration

- bonferroni_k: 2 (H1 + H2)
- bonferroni_family: Q052-F-02-writing-cluster
- alpha_bon: 0.025 (single-test α=0.05 / k=2)
- pre-committed acceptance window: H1 PASS iff joint-token-cluster corpus-count == 1; H2 PASS iff hapax-or-rare on at least one of {raqq, manshūr}.

## 6. Direction pre-registered

H1 direction: Q 52:2-3 is the SOLE verse-pair with the 4-token cluster (NOT shared with any other verse).
H2 direction: at least one of {*raqq*, *manshūr*} is corpus-hapax.

## 7. Garden-of-forking-paths

- Pre-registration origin: the hypothesis emerged during initial verse-text review of Q 52:1-3 in `00-overview.md` §3 + §6. The extreme-corpus-rarity of *raqq* (parchment) and *manshūr* (unrolled) as a writing-medium description was **noticed by inspection** but the corpus-rank/hapax check is mechanical and pre-registered before run.
- 2 tests pre-locked; 4-token combination + hapax-check.
- No alternative cells considered post-hoc.

## 8. Empirical anchor

This test directly extends cross-finding-008 (muqaṭṭāʿat as book-introduction markers) at the **non-muqaṭṭāʿat exception** level. Q 52 is a non-muqaṭṭāʿat surah that nonetheless carries explicit scripture-self-reference vocabulary in its opening verses. Combined with the empirical hapax-density of vv. 2-3, Q 52 is testably one of the strongest non-muqaṭṭāʿat book-introduction-marker exceptions.

## 9. Pre-reg SHA-256 lock

Locked at script-runtime; recorded in `csv/Q052-F-02.json`.

## 10. Author

waiel — pre-reg locked 2026-05-09.
