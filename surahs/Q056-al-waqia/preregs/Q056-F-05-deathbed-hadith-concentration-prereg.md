---
test_id: Q056-F-05
title: Deathbed/death-moment hadith concentration — Q 56:88-94 verse-citation density across the 9 books and tafsir
date: 2026-05-07
phase: B+
status: PRE-REGISTERED
investigator: Q056-al-waqia-specialist
seed: 20260507
n_perm: 0
bonferroni_k: 1
bonferroni_family: Q056-F-05-deathbed-concentration
alpha_bon: 0.05
direction: Locked: among hadiths/tafsir-narratives that quote a SPECIFIC verse of Q 56 in a deathbed-or-death-moment context, the verse-distribution is enriched at vv 88-94 vs uniform-random
acceptance: ≥ 50% of deathbed-context Q 56 verse-citations fall in vv 83-96 (the death-and-moment-of-death block)
failure: < 50%
rules_tuple: NA (textual-citation analysis)
---

# Q056-F-05 Pre-Registration — Deathbed-hadith concentration

## Hypothesis

The classical "Ibn Masʿūd recited Q 56 on his deathbed" story (Ibn Kathīr citing Ibn ʿAsākir) and the broader association of Q 56 with poverty-protection / death-recitation should — if structurally meaningful — concentrate hadith/tafsir citations of Q 56 verses on the DEATH-MOMENT block (vv 83-96, especially 88-94 = the post-soul-departs descriptions).

**Pre-committed:** in canonical citations of specific Q 56 verses appearing in deathbed/death-moment contexts (across 9-book hadith + 7 tafsirs), ≥ 50% of citations target vv 83-96.

## Method

1. Search 9-book hadith JSON for Quranic-verse mentions of Q 56:N (specific verses).
2. Search tafsirs for deathbed/death-moment narrative segments citing Q 56 verses.
3. Build a frequency distribution over vv 1-96.
4. Compute fraction in vv 83-96.

## Acceptance / failure

- ≥ 50%: VINDICATED
- < 50%: NULL (Q 56's deathbed association is GENERAL, not verse-localized)

## Honest limits

Hadith corpus has only ~5-10 specific Q 56 verse-citations; small N makes this an exploratory test capped at single-test α=0.05 per MW-7.
