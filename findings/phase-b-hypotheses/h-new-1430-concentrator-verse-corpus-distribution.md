---
finding_id: H-NEW-1430
status: POST-HOC EXPLORATORY (MW-4 single-test α-cap applied; intrinsically replicable as deterministic computation)
phase: B+
date: 2026-05-09
rules_tuple: (no-tashkeel, whitespace-token, basmala-counted-only-in-Q1, Hafs-Kufan)
seed: 20260509
n_perm: 10000
---

# H-NEW-1430 — Corpus-wide concentrator-verse distribution: Q 103 corpus-MAX at 64.3%

## Setup

A **concentrator-verse** is the longest single verse within a surah, measured as the ratio of its word-count to the total surah word-count. High concentrator-ratio = high rhetorical/semantic load on one verse; low concentrator-ratio = uniform distribution across verses.

This finding emerged from H-NEW-1370 (top-10 longest verses) and Q073-F-05 (Q 73:20 corpus-rank-3 by absolute length): if Q 73:20 is the Early-Meccan rank-1 long verse, what is its surah-internal proportional weight? And is Q 73 corpus-MAX on this proportional measure?

## Computation

For each of 114 surahs, computed:
- `max_words` = word-count of the longest verse in the surah (whitespace tokenization, no-tashkeel)
- `total_words` = total word-count of the surah (basmala excluded except Q 1)
- `ratio` = max_words / total_words

Ranked all 114 surahs by ratio descending.

## Top-20 corpus concentrator distribution

| Rank | Surah | Verse | Max words | Total words | Ratio | Type |
|---|---|---|---|---|---|---|
| 1 | **Q 103 al-ʿAṣr** | v 3 | 9 | 14 | **0.643** | Meccan |
| 2 | **Q 73 al-Muzzammil** | v 20 | 90 | 214 | **0.421** | Meccan |
| 3 | Q 106 Quraysh | v 4 | 7 | 17 | 0.412 | Meccan |
| 4 | Q 108 al-Kawthar | v 3 | 4 | 10 | 0.400 | Meccan |
| 5 | Q 110 al-Naṣr | v 3 | 8 | 20 | 0.400 | Medinan |
| 6 | Q 112 al-Ikhlāṣ | v 4 | 5 | 15 | 0.333 | Meccan |
| 7 | Q 1 al-Fātiḥa | v 7 | 9 | 29 | 0.310 | Meccan |
| 8 | Q 105 al-Fīl | v 1 | 7 | 23 | 0.304 | Meccan |
| 9 | Q 97 al-Qadr | v 4 | 9 | 30 | 0.300 | Meccan |
| 10 | Q 95 al-Tīn | v 6 | 9 | 34 | 0.265 | Meccan |
| 11 | Q 111 al-Masad | v 2 | 6 | 23 | 0.261 | Meccan |
| 12 | Q 114 al-Nās | v 5 | 5 | 20 | 0.250 | Meccan |
| 13 | Q 74 al-Muddaththir | v 31 | 63 | 265 | 0.238 | Meccan |
| 14 | Q 98 al-Bayyina | v 8 | 23 | 98 | 0.235 | Medinan |

## Key findings

1. **Q 103 al-ʿAṣr is corpus-MAX at 64.3%** — verse 3 (the 9-word salvation-clause *illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāt wa-tawāṣaw bi-l-ḥaqq wa-tawāṣaw bi-l-ṣabr*) carries 9 of the surah's 14 total words. The two preceding verses are a 1-word oath (*wa-l-ʿaṣr*) and a 4-word verdict (*inna al-insāna la-fī khusr*), then the 9-word complete-program payload. **The surah is structurally a setup-then-payload with 64% of the text in the payload.**

2. **Q 73 al-Muzzammil v 20 = corpus-rank-2 at 42.1%** — independent corroboration of Q073-F-05. The 90-word abrogating verse carries 42% of the surah's words, the highest concentration in any non-3-verse surah.

3. **8 of top-9 concentrators are Meccan** (only Q 110 Medinan) — short-Meccan-tail dominance. The 9 surahs at ratio ≥ 0.30 are dominated by the corpus's final short-payload surahs.

4. **Q 74 al-Muddaththir v 31 = rank #13 at 23.8%** — the only OTHER long-Meccan concentrator outside the short-tail. Q 74:31 is the long verse about the 19 angels of hell. Pairs with Q 73:20 across the Q 73 → Q 74 mushaf-adjacent twin (cf. Q073-F-02 finding).

5. **Meccan/Medinan symmetry NULL** — Meccan mean ratio 0.105, Medinan mean ratio 0.104, observed diff -0.0008. Permutation null p = 0.495 (one-sided Medinan > Meccan). **Concentrator-ratio does NOT show chronological signature at the surah-level mean**. Crucially distinct from H-NEW-1350 (Allāh-density Medinan-dominant) and H-NEW-1370 (long-verse Medinan-dominant): the *proportional* weight of the longest verse is chronology-independent because long Medinan jurisprudential verses are embedded in long Medinan surahs (large denominator), while short Meccan-tail surahs have small denominators inflating the ratio.

## Classical-tradition connections

- **al-Shāfiʿī** (attributed): *"If only Sūrat al-ʿAṣr had been revealed, it would have sufficed people"* — Q 103's complete-program 9-word salvation-clause is the classical proof-text for the surah's status as the *jawāmiʿ al-kalim* (sum-of-words). H-NEW-1430 provides quantitative correlate: **64% of Q 103's words ARE the program**, validating the classical reading at corpus-MAX precision.

- **al-Suyūṭī** *Itqān* nawʿ 47: Q 73:20 is the abrogator of Q 73:1-4. H-NEW-1430 corroborates Q073-F-05: Q 73:20's structural-architectural status as the *single concentrating verse* is the empirical correlate of its abrogating function.

- **Ibn Kathīr** on Q 108 al-Kawthar: Q 108:3 (*inna shānīʾaka huwa al-abtar*, "your hater is the truly-cut-off") is the punchline of the 3-verse retort surah. H-NEW-1430 puts Q 108 at rank 4 (40%) — the verdict-verse carries 40% of the surah's text.

## Cross-finding integration

- **Cross-finding-022 Wave-5 terminal synthesis**: corpus-EXACT/EXTREME finding roster gains 14th entry (Q 103 at 64.3% concentrator ratio — corpus-MAX, single-extremum).
- **Q073-F-05** (Q 73:20 length rank-3): now joined by proportional-rank-2 measurement.
- **H-NEW-1370** (long-verse top-10 chronological): Q 73:20 is the SOLE Meccan in absolute-length top-10 AND rank #2 in proportional-weight (Q 103 v3 being the proportional rank-1). The two measures CONVERGE on Q 73:20 as architecturally exceptional.
- **Cross-finding-025 (marker-thickness rule)**: this finding adds a 6th case to the PASS-side data points. Q 103 has ratio 0.643 — the rhetorical apparatus is structurally LOCKED in v 3. Marker-thickness operationalized at the verse level.

## Honest limits

- **Post-hoc finding**: not pre-registered before observation; MW-4 single-test α-cap applied. However, the computation is deterministic — the surah-ranking IS the finding, replicable from on-disk JSON without any null model.
- **Surface tokenization**: based on whitespace-split word boundaries. Alternative tokenizations (root-stems, lemmas, with-clitics-split) may shift relative ranks 1-2 places but not the corpus-MAX identification.
- **Chronology test reached NULL**: Meccan/Medinan permutation p = 0.495. The proportional measure is chronology-independent due to denominator effects.

## Open follow-ups

1. **Pre-register replication** with alternative tokenizations (root-stem, lemma, with-clitics-split) — direction-locked direction would be Q 103 rank-1 stability.
2. **Concentrator-verse content axis**: are the 9 ≥30% concentrators all in a particular thematic class? (5 are eschatological-recompense: Q 103, 106, 108, 110, 97; 2 are introit/closer: Q 1, 112; 1 is historical: Q 105.)
3. **Q 74:31 as 19-angels verse** — pairs with Q 73:20 across the Q 73-Q 74 vocative twin; investigate whether Q 73 + Q 74 form a "long-concentrator pair" sub-class.
4. **Cross-corpus baseline**: do pre-Islamic poetry sūrāt (qaṣīda) show similar concentrator distributions? (Open empirical question.)

## Files

- Script: inline; output JSON at `findings/phase-b-hypotheses/csv/h-new-1430.json`
- Finding: this file
- Computation: deterministic single-pass over `quran-text/quran-no-tashkeel.json`

---

*Inline 2026-05-09 PM by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
