---
finding_id: Q020-F-05
title: Q 20:14 divine-name density vs Q 20 mean — ʿUmar-conversion hadith verse-location signature test
date: 2026-05-07
seed: 20260507
phase: B+
specialist: Q020-ta-ha-specialist
bonferroni_k: 1
bonferroni_family: "Q020-v14-divine-name-density (single test)"
alpha_bon: 0.05
direction_locked: greater (Q 20:14 divine-name density > Q 20 verse-mean)
status: PRE-REGISTERED
---

# Q020-F-05 — Q 20:14 divine-name density test (ʿUmar-conversion verse signature)

## Background (classical claim)

al-Bayhaqī, *Dalāʾil al-nubuwwa*, and al-Suyūṭī, *al-Durr al-manthūr* on Q 20:1, report the ʿUmar-conversion narrative: ʿUmar b. al-Khaṭṭāb, on his way to harm the Prophet, hears his sister Fāṭima reciting Q 20 and is arrested by the recitation. The verse most-emphasized in the strongest variants is Q 20:14: *innanī anā Allāhu lā ilāha illā anā fa-ʿbudnī wa-aqim al-ṣalāta li-dhikrī* — "Indeed I, I am Allāh; there is no god but I; so worship Me and establish prayer for My remembrance."

The verse contains 5 first-person divine self-references (ـنـي, أنا, أنا, ـني, ذكري) and the divine name اللّه + the profession lā ilāha illā ana — the densest single-verse self-affirmation in Q 20.

## Hypothesis (direction-locked)

Q 20:14's divine-name + 1sg-divine-pronoun density (combined) is GREATER than the Q 20 per-verse mean for the same metric.

Operationalization: divine_density(verse) = (# of `الله` + `أنا` + 1sg-divine-suffix `ـني` after divine context) / word_count(verse).

We use a simple operational metric:
- Count occurrences of: `الله` (whole-word), `إله` (whole-word), `هو` (whole-word, when in divine-self-reference context — approximate by counting all), `أنا` (whole-word), and ـني (final 2 chars on a token of length ≥ 4 — proxy for 1sg accusative-objective suffix when subject is divine — which is noisy but UNIFORMLY noisy across all 135 verses).
- Divide by word count of the verse.

## Pre-committed thresholds

- **PASS (CONFIRMED)**: Q 20:14 density rank in top-3 of 135 verses, AND permutation p ≤ 0.05.
- **DIRECTIONAL**: rank 4-13 (top decile).
- **NULL**: rank > 13.

## Null model

Permutation: 10000 shuffles of word-tokens across Q 20 verses (preserving per-verse word-counts); recompute Q 20:14 density rank. Seed 20260507.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## Honest limits

- The ʿUmar-conversion narrative has multiple variants — al-Bayhaqī, al-Ṭabarānī, al-Bazzār, ibn Hishām — each emphasizing slightly different verses (some Q 20:1-8, some Q 20:14, some Q 20:13-16). al-Bayhaqī's Q 20:14 emphasis is the strongest single-verse claim.
- A high divine-name density at v.14 is at most CIRCUMSTANTIALLY consistent with the hadith — it is NOT proof the hadith is historically authentic; it shows the verse-location pre-naming has empirical content.
- The proxy ـني-suffix counting catches some non-divine 1sg pronouns; this is uniform noise across all 135 verses.
