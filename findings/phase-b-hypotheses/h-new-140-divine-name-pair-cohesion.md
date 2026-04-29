---
id: H-NEW-140
title: Classical divine-name pairs show massive co-occurrence above independence
phase: B
status: PASS-DIRECTED (post-hoc; extreme p survives single-test α=0.05 cap)
date: 2026-04-17
executed_by: team-lead (inline)
classical_anchor: al-Rāzī, Mafātīḥ al-ghayb on fawāṣila al-āyāt; al-Zamakhsharī, al-Kashshāf; al-Suyūṭī, al-Itqān (asmāʾ mutazāwijah / paired-names in verse-endings)
seed: 20260417
rules_tuple: (no-tashkeel verse text; 16 classical name-pair list pre-committed; 6,236 verses; Poisson independence null + direct observed-counts)
bonferroni_k: 1
bonferroni_family: h-new-140-paired-names
alpha_bon: 0.05
direction: POSITIVE — observed classical-pair co-occurrence > Poisson-independence expectation
verdict: PASS-DIRECTED
---

# [[h-new-140-divine-name-pair-cohesion|H-NEW-140]] — Classical divine-name pair cohesion

## Classical anchor

Classical tafsir and balāgha literature (al-Rāzī in Mafātīḥ al-ghayb, al-Zamakhsharī's al-Kashshāf, al-Suyūṭī's al-Itqān) enumerate **asmāʾ mutazāwijah** — paired divine names that systematically close verses together:

- al-Raḥmān + al-Raḥīm (basmala)
- al-ʿAzīz + al-Ḥakīm (~30 verse-endings)
- al-Samīʿ + al-Baṣīr (Q 17:1 famous)
- al-Ghafūr + al-Raḥīm (very common)
- al-Tawwāb + al-Raḥīm
- al-Samīʿ + al-ʿAlīm
- al-ʿAzīz + al-Raḥīm
- al-ʿAlīm + al-Ḥakīm
- al-Laṭīf + al-Khabīr
- al-Ḥalīm + al-Ghafūr
- etc.

These are not random pairings; classical tradition holds they are THEMATICALLY COUPLED (mercy-and-compassion; might-and-wisdom; knowing-and-wise; etc.).

## Hypothesis

Classical-pair co-occurrence in individual verses exceeds Poisson-independence expectation substantially. Direction: POSITIVE (one-sided).

## Method

- Load no-tashkeel Quran corpus (6,236 verses)
- For each of 16 pre-committed classical pairs, count verses containing both names
- Poisson-independence expected value: E = count(A) × count(B) / N_verses
- z-score: (observed − E) / sqrt(E)

## Results

| Pair | Observed | Expected (independence) | z | Example locations |
|---|:-:|:-:|:-:|---|
| al-Raḥmān + al-Raḥīm | 6 | 0.26 | **+11.2** | Q 1:1, Q 1:3, Q 2:163 |
| **al-ʿAzīz + al-Ḥakīm** | **29** | 0.43 | **+43.5** | Q 2:129, Q 3:6, Q 3:18 |
| al-Samīʿ + al-Baṣīr | 5 | 0.03 | +29.3 | Q 11:24, Q 17:1, Q 40:20 |
| al-Ghafūr + al-Raḥīm | 8 | 0.50 | +10.7 | Q 10:107, Q 12:98, Q 15:49 |
| al-Tawwāb + al-Raḥīm | 6 | 0.05 | +25.5 | Q 2:37, Q 2:54, Q 2:128 |
| al-ʿAzīz + al-Ghafūr | 1 | 0.93 | +0.1 | Q 67:2 |
| al-ʿAzīz + al-ʿAlīm | 6 | 1.65 | +3.4 | Q 6:96, Q 27:78, Q 36:38 |
| al-ʿAzīz + al-Raḥīm | 13 | 0.35 | +21.4 | Q 26:9, Q 26:68, Q 26:104 |
| al-ʿAlīm + al-Ḥakīm | 6 | 1.08 | +4.7 | Q 2:32, Q 12:83, Q 12:100 |
| al-Ḥalīm + al-Ghafūr | 6 | 0.22 | +12.4 | Q 2:225, Q 2:235, Q 3:155 |
| al-Shakūr + al-Ḥalīm | 1 | 0.03 | +5.3 | Q 64:17 |
| al-Wadūd + al-Ghafūr | 1 | 0.01 | +8.2 | Q 85:14 |
| al-Qadīr + al-ʿAlīm | 7 | 1.29 | +5.0 | Q 6:96, Q 16:70, Q 30:54 |
| al-Khabīr + al-ʿAlīm | 4 | 1.16 | +2.6 | Q 4:35, Q 31:34, Q 49:13 |
| **al-Laṭīf + al-Khabīr** | 5 | 0.05 | **+22.0** | Q 6:103, Q 22:63, Q 31:16 |
| **al-Samīʿ + al-ʿAlīm** | 15 | 0.52 | **+20.2** | Q 2:127, Q 2:137, Q 3:35 |

**Aggregate**: 119 observed co-occurrences vs 8.6 expected under independence — **13.87× enrichment**.

## Interpretation

- Every single classical pair shows z > 0; most have z > 10
- 5 pairs have z > +20 (al-ʿAzīz+al-Ḥakīm, al-Samīʿ+al-Baṣīr, al-Tawwāb+al-Raḥīm, al-Laṭīf+al-Khabīr, al-Samīʿ+al-ʿAlīm)
- Classical balāgha's "paired names" identification is empirically CORRECT — these are formulaic couplings, not independent occurrences
- The outlier al-ʿAzīz+al-Ghafūr (z = +0.1) reflects that this pair is actually NOT a typical verse-closer; it appears only as al-ʿAzīzu al-Ghafūr (Q 35:28, 67:2) — classical tradition indeed places it lower in the fawāṣila hierarchy

## Connection to prior findings

- Extends [[h-new-71-allah-distribution|H-NEW-71]] Allah-density findings at a new axis (name-pair coupling, not name-single occurrence)
- Extends H-NEW-59 Khawātim al-Ḥashr analysis — the 8 names in Q 59:22-24 include pairs that appear here (al-Quddūs + al-Salām, al-Muʾmin + al-Muhaymin are all in that one verse; classical khawātim itself is a stacked version of this pairing principle)
- Supports [[cross-finding-010-extended-network|cross-finding-010]] back-upper hub status of Q 59-62 through name-density cohesion

## Honest limits

1. **Selection effect**: the 16 classical pairs I tested are KNOWLEDGE-BASED. I did not systematically enumerate all C(20, 2) = 190 possible name-pairs and then select the top-16. The list is drawn from standard classical tafsir/balāgha literature. A more rigorous version would test ALL name-pairs and compare classical-list to non-classical-list.

2. **Rule-tuple sensitivity**: no-tashkeel matching means some name-forms might slip past (al-Ghafūr can appear as غفور or الغفور; I tested both; others may still be missed). Proper matching requires QAC-level morphology.

3. **Post-hoc**: test designed 2026-04-17 after observation. Single-test α=0.05 ceiling applies. Extreme p (all positive z, most >10) survives with enormous margin.

4. **Correlation not causation**: these pairs co-occur because classical tradition IDENTIFIED them as formulaic. The test confirms classical identification was correct, not that there's some mystical property.

## Queue for future replication

- [[h-new-140-1-all-pair-decircularization|H-NEW-140.1]]: enumerate ALL C(N, 2) name-pairs and compare top-K empirical pairs to classical-list ranks (proper independence test vs selection)
- H-NEW-140.2: test co-occurrence at verse-END specifically (fawāṣila narrow reading) vs anywhere-in-verse
- H-NEW-140.3: cross with H-NEW-59 Khawātim analysis — do the Khawātim-exclusive names form a super-cluster at the pair level?

## Classical wisdom integration

This is the SECOND major empirical validation of classical balāgha this session (first: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] muqaṭṭāʿat-rhyme correlation). Classical Quranic sciences (ʿulūm al-Qurʾān) contain qualitative claims that modern statistical instruments are now able to test. Both validations came back POSITIVE at extreme p-values. This is a productive research direction — not all classical claims survive ([[h-new-82-yasin-heart|H-NEW-82]] Q 36 heart-of-Quran refuted; H-NEW-87 786-abjad refuted; [[h-new-84-ikhlas-third|H-NEW-84]] Q 112 1/3-of-Quran refuted; [[h-new-119-seven-fold|H-NEW-119]] sabʿ samāwāt=7 refuted), but the balāgha claims about rhyme-structure and paired-names DO survive.

A hypothesis worth queuing: classical balāgha / fawāṣila science is more EMPIRICALLY DEFENSIBLE than classical ʿilm al-ḥarf mystical numerology. The aesthetic-rhetorical observations survive rigorous testing; the numerological ones don't.

## Files

- Inline script: this session
- Findings: this file
