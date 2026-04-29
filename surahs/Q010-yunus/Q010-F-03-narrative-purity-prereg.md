---
finding_id: Q010-F-03
title: Narrative-purity index for Q 10 vs the corpus
date_locked: 2026-04-28
seed: 1042900
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q010-F-03 — Narrative-purity index for Q 10

## Hypothesis (DIRECTION-LOCKED)
Q 10 Yūnus has **substantially LOWER narrative-purity** than Q 12 Yūsuf. Q 12 is rank 1/114 by narrative-purity per Q012-F-01.

Direction-locked: Q 10 narrative-purity score ≪ Q 12 narrative-purity score, and Q 10 ranks well outside the top-10 narrative-pure surahs.

## Operationalisation
Narrative-purity proxy (same definition as Q012-F-01):
- Token counts of *qaṣaṣ-cluster* roots: `قص` (q-ṣ-ṣ → narrate), past-tense narrative verbs (forms with prefix-tā, suffix-ū, etc.).
- Specifically: count occurrences of {`قال`, `قالوا`, `قلنا` proper-noun-followed-form indicators}, plus the named-character density {Yūnus, Mūsā, Nūḥ, Hūd, Ṣāliḥ, Yūsuf, Pharaoh, etc.}.
- Or: simpler proxy = density of `َ`-suffix (perfect-tense) verbs and bare proper-noun mentions.

Implementation choice (locked): use **proper-noun density** = count of {يونس, موسى, نوح, هود, صالح, شعيب, لوط, ابراهيم, اسحاق, يعقوب, اسماعيل, يوسف, فرعون, عيسى, داود, سليمان} tokens, normalised by total words. This is the narrative-foreground density.

## Test
1. Compute proper-noun density for each surah.
2. Rank surahs.
3. Verdict CONFIRMED if Q 10's rank > rank 30 (i.e., NOT a top-30 narrative-pure surah).
4. Verdict NULL if Q 10 ranks top-30.

## Direction lock
Q 10 is predicted to be NOT-narrative-pure (rank > 30). This pre-commits a particular interpretation: the surah named *Yūnus* is dominantly THEOLOGICAL-POLEMICAL, not narrative.

## Bonferroni
Single test → α=0.05.

## Honest expectation
From eyeballing Q 10's content (most verses are about God's signs, qiyāma, polemic with mushrikīn; only vv. 71-93 deal with Mūsā/Nūḥ; only v. 98 mentions Yūnus's people), Q 10 should rank far below narrative-dominated surahs (Q 12 Yūsuf, Q 28 al-Qaṣaṣ, Q 7 al-Aʿrāf, Q 11 Hūd). The pre-committed direction predicts this.
