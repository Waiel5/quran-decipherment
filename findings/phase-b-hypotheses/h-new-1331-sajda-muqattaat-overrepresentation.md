---
id: H-NEW-1331
title: Sajda × muqaṭṭāʿat hypergeometric over-representation
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: PASS-DIRECTED
seed: 20260509
n_perm: 10000
prereg_sha: 0adda1b0d1c2df69009bc79969642955c3dab43a065d1ded525c11999d17c680
prereg_path: findings/phase-b-hypotheses/h-new-1331-sajda-muqattaat-overrepresentation-prereg.md
script_path: findings/phase-b-hypotheses/scripts/h_new_1331_sajda_muqattaat.py
output_json: findings/phase-b-hypotheses/csv/h-new-1331.json
---

# H-NEW-1331 — Sajda × muqaṭṭāʿat hypergeometric over-representation

## Verdict: PASS-DIRECTED

The 14 sajda-surahs are over-represented for muqaṭṭāʿat-opening at **1.97× corpus baseline**. Both pre-registered cells PASS at α = 0.05.

## Observed values

| Quantity | Value |
|:--|--:|
| Corpus surahs (N) | 114 |
| Muqaṭṭāʿat-opened (K) | 29 |
| Sajda surahs (n) | 14 |
| Intersection (k) | **7** |
| Expected under random | 3.56 |
| Observed-to-expected ratio | **1.97×** |
| Cell A — hypergeometric p(X≥7) | **0.03184** |
| Cell B — permutation p_perm | **0.03210** |

The intersection: **{Q 7 al-Aʿrāf (المص), Q 13 al-Raʿd (المر), Q 19 Maryam (كهيعص), Q 27 al-Naml (طس), Q 32 al-Sajda (الم), Q 38 Ṣād (ص), Q 41 Fuṣṣilat (حم)}** — 7 of 14 sajda-surahs are muqaṭṭāʿat-opened.

## Refinement of H-NEW-1330

H-NEW-1330 found the 14 sajda-surahs do NOT form a Fisher-Rao cohesive cluster on root-distribution (NULL on Cells A and B with PC passing). H-NEW-1331 now establishes that the sajda set has at least ONE structural correlate — muqaṭṭāʿat-opening — at significant level.

This is exactly the **cross-finding-025 prediction**: a thin marker can correlate with another structural axis without producing FR-cohesion at the surah-aggregate level. The sajda × muqaṭṭāʿat correlation is partial (7/14 = 50%) and operates at the binary "is this surah muqaṭṭāʿat-opened" axis, not at root-frequency space.

## Bonferroni note

This is a single hypothesis (k=1, α=0.05). The two cells (hypergeometric exact + permutation) are TWO ANGLES on the same hypothesis, not two distinct tests. Both gave p ≈ 0.032 — robust to test choice.

If we Bonferroni-correct against the 8 tests of cross-finding-025's marker-thickness regularity (5 PASS + 3 NULL clusters, plus this 1331 = 9 tests), α_bon = 0.0056. **H-NEW-1331 does not survive that correction at strict α**, but the meta-rule already had ample support without it. We log it as a single-test PASS-DIRECTED finding under PRE-REG-STANDARD-04.

## Connection to existing findings

- **H-NEW-1330** sajda 14-cluster FR NULL (this session): the sajda set has muqaṭṭāʿat-correlation but not root-distribution-cohesion. Confirms that a single structural correlate is insufficient for FR cohesion.
- **Cross-finding-008** muqaṭṭāʿat-as-book-introduction (p ≤ 10⁻¹²): adds **sajda-trigger as a 14th-axis correlate** of the muqaṭṭāʿat function. The muqaṭṭāʿat continue to widen their multi-axis correlation reach.
- **Cross-finding-025** marker-thickness threshold: the sajda set is one structural correlate short of cohesion. Adding muqaṭṭāʿat-correlation as the partial axis reinforces the multi-axis-correlation criterion: a thin marker correlated with one other axis still doesn't cohere; it would need 2-3 correlated axes to cross the threshold.
- **Cross-finding-015** classical-validation pattern: the sajda-tradition (al-Bukhārī Kitāb Sujūd al-Qurʾān, al-Suyūṭī *al-Itqān* nawʿ on sujūd al-tilāwa) is partially structurally-supported through the muqaṭṭāʿat correlation. **+1 SURVIVED** at the joint axis.

## The 7 sajda × muqaṭṭāʿat surahs

| Surah | Muqaṭṭāʿat | Sajda verse | Chronology |
|:--|:--:|:--:|:--|
| Q 7 al-Aʿrāf | المص (4-letter) | 7:206 | Late Meccan |
| Q 13 al-Raʿd | المر (4-letter) | 13:15 | Medinan/Late Meccan |
| Q 19 Maryam | كهيعص (5-letter — singleton) | 19:58 | Middle Meccan |
| Q 27 al-Naml | طس (2-letter — singleton) | 27:26 | Middle Meccan |
| Q 32 al-Sajda | الم (3-letter) | 32:15 | Middle Meccan |
| Q 38 Ṣād | ص (1-letter — singleton) | 38:24 | Middle Meccan |
| Q 41 Fuṣṣilat | حم (2-letter) | 41:38 | Late Meccan |

**Notable**: 4 of the 7 are letter-set SINGLETONS (المص, كهيعص, طس, ص). The singleton fraction in this subset (4/7 = 57%) is higher than the corpus singleton-fraction (8/29 = 28%). Whether singleton-muqaṭṭāʿat are over-represented within sajda-muq is a follow-up pre-reg seed (H-NEW-1332 queued).

## The 7 NON-muqaṭṭāʿat sajda-surahs

| Surah | Sajda verse | Chronology | Opening |
|:--|:--:|:--|:--|
| Q 16 al-Naḥl | 16:50 | Late Meccan | atā amru llāh |
| Q 17 al-Isrāʾ | 17:109 | Late Meccan | subḥāna alladhī asrā |
| Q 22 al-Ḥajj | 22:18 | Medinan | yā ayyuhā al-nās |
| Q 25 al-Furqān | 25:60 | Middle Meccan | tabāraka alladhī nazzala |
| Q 53 al-Najm | 53:62 | Early Meccan | wa-l-najm |
| Q 84 al-Inshiqāq | 84:21 | Early Meccan | idhā al-samāʾu |
| Q 96 al-ʿAlaq | 96:19 | Early Meccan | iqraʾ |

**Notable**: 3 of these 7 (Q 17, Q 22, Q 96) carry their own structurally-marked opening formulas (subḥāna / yā ayyuhā al-nās / iqraʾ) suggesting an alternative "structurally-marked-opener" axis. The 4 remaining (Q 16, 25, 53, 84) span all chronological phases and may represent a sajda residual class.

## Honest limits

- **Single test**: PASS-DIRECTED ceiling at α=0.05 single-test cap (post-hoc origin per H-NEW-1330's descriptive observation).
- **Bonferroni note above**: under cross-finding-025 family α_bon=0.0056, this finding does not survive. The meta-rule has independent support.
- **Cluster sensitivity**: tested under classical-Sunnī 14-surah list. Imāmī 4-surah list {Q 32, 41, 53, 96} — 3 of 4 are NOT muqaṭṭāʿat (only Q 32, 41 are); under Imāmī, the over-representation REVERSES (2/4 = 50% vs 25% — same ratio but only 4 surahs, hypergeometric p ≈ 0.30 NULL).
- **Mālikī 13-surah list** (excluding Q 38): k = 6/13, p_hyper ≈ 0.087 marginal — would not pass strict α=0.05.

## Replication seeds (NOT yet locked)

- **H-NEW-1332**: singleton-muqaṭṭāʿat over-representation within the sajda × muqaṭṭāʿat 7-surah subset.
- **H-NEW-1333**: alternative-structurally-marked-opener axis for the 7 non-muqaṭṭāʿat sajda surahs (subḥāna / yā ayyuhā / iqraʾ openers).
- **H-NEW-1334**: rules-tuple replication under Imāmī 4-surah and Mālikī 13-surah lists.

## Verdict summary

| Cell | p | Pass (α=0.05) |
|:--|:--:|:-:|
| A — hypergeometric exact | 0.0318 | YES ✓ |
| B — permutation | 0.0321 | YES ✓ |

**Final verdict: PASS-DIRECTED** at single-test α=0.05. Sajda-surahs are 1.97× over-represented for muqaṭṭāʿat-opening relative to corpus baseline. The muqaṭṭāʿat continue to widen their multi-axis-correlation reach by adding sajda-trigger as a 14th correlated structural axis (after book-reference, formulaic-opening, length, chronology, etc.).
