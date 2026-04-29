---
id: H-NEW-56
run: 1
date: 2026-04-15
agent: h-new-56-specialist
seed: 20260416
parent: H-NEW-53
verdict: PASS-DIRECTED-EXTENDED (3-cell, all PASS at Bonferroni α=0.0167)
---

# H-NEW-56 — run-1 journal

## Task

Analyze the 5 muqaṭṭaʿāt-opened surahs that LACK kitāb/qurʾān in v1-3 (per H-NEW-53):
Q 19 (Maryam), Q 29 (al-ʿAnkabūt), Q 30 (al-Rūm), Q 42 (al-Shūrā), Q 68 (al-Qalam).

Four questions per parent task:
1. Thematic features distinguishing these 5
2. Common revelatory period / audience / function
3. Compensating revelation-theme markers (qalam, satr, dhikr, āyāt, nūr, kalām)
4. Classical tafsīr explanation

## Procedure

1. Read v1-7 of each exception surah from `quran-no-tashkeel.json`.
2. Cross-referenced with `revelation-order.csv` for Nöldeke chronology.
3. Built 3-cell hypergeometric test family (Bonferroni k=3):
   - Cell 0: narrow (kitāb/qurʾān) — replication
   - Cell 1: writing-cluster (+ qalam, satr)
   - Cell 2: full extended (10 markers: + dhikr, āyāt, nūr, kalām, hudā, wahy/anzal)
4. Per-surah thematic classification (5 categories).
5. Cross-referenced classical tafsīr (al-Zarkashī, al-Suyūṭī, al-Rāzī, al-Ṭabarī, etc.).
6. Pre-registered before running.

## Garden-of-forking-paths log

Pre-existing knowledge BEFORE running:
- H-NEW-53.md already noted Q 68's qalam/yasṭurūn (semantically adjacent) and Q 19's later kitāb references (v12, v16). It also noted Q 42's bipartite muqaṭṭaʿāt structure.
- The expanded-marker test was suggested as a follow-up by H-NEW-53.
- Q 29 and Q 30 were flagged as "interesting in their own right" but no compensating marker was identified.

Pre-committed expectations (locked at prereg):
- Cell 1 will RECLASSIFY Q 68 as PASS (qalam/satr in v1).
- Cell 2 will RECLASSIFY Q 19 (dhikr v2) and Q 42 (yūḥī v3) as PASS.
- Q 29 and Q 30 will REMAIN exceptions even under the broadest 10-marker set.
- Effect-size will WEAKEN under Cell 2 (broader baseline).

All 4 expectations were CONFIRMED in execution.

## Key results

| Cell | Definition | k/29 | K (total) | p-value | Verdict |
|---|---|---|---|---|---|
| 0 | k-t-b, q-r-ʾ (replicates H-NEW-53) | 24 | 35 | 9.48e-12 | PASS |
| 1 | + qalam, satr (writing-cluster) | 25 | 36 | **8.58e-13** | PASS-STRENGTHENED |
| 2 | + dhikr, āyāt, nūr, kalām, hudā, wahy/anzal | 27 | 57 | 2.28e-08 | PASS-WEAKENED |

## Surprise findings

1. **Cell 1 is STRONGER than the parent H-NEW-53 narrow result.** Adding qalam + satr to the marker set increased k by 1 (Q 68) but added ZERO new positives in the non-muqaṭṭaʿāt baseline (because al-Ṭūr Q 52, which famously has "kitābin masṭūr", already PASSED via kitāb in narrow). Net effect: enrichment improves by ~11×.

2. **Q 68 is the EARLIEST muqaṭṭaʿāt surah** (Nöldeke #18, revelation-order #2 — second after al-ʿAlaq). Its v1 invokes qalam + yasṭurūn — making the FIRST muqaṭṭaʿāt surah ever revealed an explicit script-awareness oath. Q 68 is arguably the PROTOTYPE of the muqaṭṭaʿāt-as-script-marker reading, not an exception to it.

3. **Only Q 29 and Q 30 are genuine exceptions** under any reasonable marker definition. Both are Late Meccan ALM-surahs with surah-specific functions (persecution-test, Roman-defeat-prophecy). The other 3 are reconciled by classical reading.

4. **The 5 exceptions are HETEROGENEOUS** — they span all three Meccan sub-phases (Early/Middle/Late), all cardinality classes (1/3/5), and 5 different opener-genres. This rules out any single-mechanism explanation.

## Classical anchors used

- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān* I/172-175
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān* I/137-141
- al-Rāzī, *Mafātīḥ al-Ghayb* (loci ad Q 29:1, Q 30:1, Q 42:1, Q 68:1)
- al-Ṭabarī, *Jāmiʿ al-Bayān* 21/15 (on Q 30 asbāb)
- Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿAẓīm* 7/189 (on Q 42)
- al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān* 16/2, 18/220
- Ibn ʿAṭiyyah, *al-Muḥarrar al-Wajīz* 5/345 (on Q 68 N + qalam)
- al-Zamakhsharī, *al-Kashshāf* (on Q 19:2 dhikr-as-revelation-frame)
- al-Biqāʿī, *Naẓm al-Durar* 14/512 (on Q 29 ALM-anomaly)
- Welch, A. T. (1986). "al-Ḳurʾān". *Encyclopedia of Islam*, 2nd ed.

## Files written

1. `findings/phase-b-hypotheses/h-new-56-five-exceptions-prereg.md` — pre-registration with 3-cell test family
2. `scripts/h_new_56_five_exceptions.py` — analysis script (closed-form hypergeometric)
3. `findings/phase-b-hypotheses/csv/h-new-56.json` — per-cell results + per-exception markers
4. `findings/phase-b-hypotheses/h-new-56-five-exceptions.md` — findings document
5. `journal/h-new-56-run-1.md` — this journal

## Honest limitations

1. The Q 68 reclassification (Cell 1 PASS) depends on the writing-cluster definition. A stricter reviewer could insist on narrow lemma-matching, in which case Q 68 stays in the exception bucket.
2. Q 19's dhikr in v2 is a recognized Qurʾānic self-designation but is also a common verb (dhakara = "to mention"). The semantic-extras inclusion of dhikr is principled but could be debated.
3. Q 42's wahy in v3 is unambiguous as a revelation marker, but only PASSES under the 10-marker extended set, which has a weaker (10⁻⁸) p-value than narrow.
4. Q 29 and Q 30 remain genuine exceptions. The classical commentary "rationalizes" them by surah-specific function, but this is post-hoc interpretation.
5. The 5-exception category is HETEROGENEOUS. There is NO single mechanism that explains all 5; the analysis simply shows that 3 of 5 have compensating markers under reasonable extension, leaving 2 as residual outliers.

## Status

Run 1 complete. Verdict: PASS-DIRECTED-EXTENDED. The writing-cluster definition (kitāb/qurʾān/qalam/satr) STRENGTHENS H-NEW-53 by an order of magnitude (10⁻¹² → 10⁻¹³).

Recommend: H-NEW-53 cross-finding-006 axis-8 entry should be UPDATED to reference H-NEW-56 and use the writing-cluster k=25/29 figure as the primary result.

The 2 genuine exceptions (Q 29 al-ʿAnkabūt, Q 30 al-Rūm) deserve targeted follow-up — both are Late Meccan ALM-surahs with surah-specific functions; they may form a small "structural-outlier" sub-cluster within the muqaṭṭaʿāt corpus worth investigating in H-NEW-57+.
