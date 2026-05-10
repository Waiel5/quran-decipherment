---
surah: 32
test_id: Q032-F-05
title: Friday-fajr classical-claim audit (al-Bukhārī #870, #1037) — Q 32 + Q 76 ↔ FR pair-distance + Q 32 + Q 67 al-Munjiya nightly anchor
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 3
alpha_bon: 0.017
verdict_ceiling: PASS-DIRECTED (single planned replication required for promotion)
classical_anchor:
  - al-Bukhārī, *Ṣaḥīḥ*, idInBook 870 (project ahmedbaset-json convention): the Prophet recited Alif-Lām-Mīm-Tanzīl (Q 32) and Hal-atā-ʿalā-l-Insān (Q 76) in the Fajr prayer of Friday.
  - al-Bukhārī, *Ṣaḥīḥ*, idInBook 1037 (variant chain, same content).
  - al-Tirmidhī, *Sunan*, idInBook 2975 (project ahmedbaset-json convention): the Prophet would not sleep until he recited Alif-Lām-Mīm-Tanzīl (Q 32) and Tabāraka-lladhī-bi-yadihi-l-Mulk (Q 67) — al-Munjiya nightly recitation.
  - al-Tirmidhī, *Sunan*, idInBook 2974 (companion hadith: Q 67 alone, 30 verses, intercedes for the reciter).
classical_anchor_note: "The brief specified al-Tirmidhī #2891/#2892 for the Friday-fajr Q 32 + Q 67 pair. On-disk verification against `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` shows idInBook 2891 is about clothing (burdān akhḍarān) and idInBook 2892 is about clothing (mirṭ aswad) — NEITHER matches the Friday-fajr or Sajda+Mulk content. The actual on-disk attestation is: Bukhārī #870 + #1037 for Friday-fajr (Sajda + Insān = Q 32 + Q 76, NOT Q 32 + Q 67) and Tirmidhī #2975 for nightly Sajda+Mulk (Q 32 + Q 67, NOT a Friday-fajr practice). The brief's hadith numbering contains TWO errors; this pre-reg corrects them on-disk and tests BOTH attested pairings."
direction_of_effect: LOCKED — FR(Q 32, Q 76) < corpus pairwise mean (0.9235) by ≥ 1σ (Cell A — Friday-fajr pair); FR(Q 32, Q 67) < corpus pairwise mean by ≥ 1σ (Cell B — al-Munjiya nightly pair); and the average of (Friday-fajr + al-Munjiya) pair-distances is below the joint corpus pair-distance distribution.
rules_tuple:
  orthography: no-tashkeel
  word_definition: QAC stem-roots
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  hadith_source: data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/
  hadith_numbering: idInBook (per-collection sequential; NOT sunnah.com / Beirut canonical numbering)
  instrument: H-NEW-111 D_matrix_upper_triangular (Fisher-Rao on QAC stem-root TF distributions)
---

# Q032-F-05 — Pre-registration: Friday-fajr + al-Munjiya pair-distance audit

## 1. Origin

The brief specifies "al-Tirmidhī #2891/#2892 narrate the Prophet recited Q 32 + Q 67 in fajr (Friday-morning tradition)." On-disk hadith verification against `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` (using the project's idInBook numbering convention) finds:
- idInBook 2891: clothing hadith (burdān akhḍarān; ḥasan gharīb).
- idInBook 2892: clothing hadith (mirṭ aswad; ḥasan gharīb ṣaḥīḥ).
- idInBook 2974: Q 67 (Tabārak) intercedes for the reciter (30-verse surah).
- idInBook 2975: al-Munjiya pre-sleep recitation pair Q 32 (Sajda) + Q 67 (Mulk).

And against `bukhari.json`:
- idInBook 870: Friday-fajr — Q 32 (Sajda) + Q 76 (Insān).
- idInBook 1037: same Friday-fajr practice, variant chain.

The brief contains TWO factual errors: (1) Tirmidhī #2891/#2892 are NOT about Friday-fajr or Sajda+anything; (2) the Friday-fajr classical pair is Sajda + INSĀN (Q 76), NOT Sajda + Mulk (Q 67). The Sajda + Mulk pair is the al-Munjiya NIGHTLY pair (al-Tirmidhī #2975).

This pre-reg corrects both errors on-disk and tests BOTH liturgical pairings empirically.

## 2. Hypotheses

**H1 (Cell A — Friday-fajr Sajda + Insān, per al-Bukhārī #870, #1037):**
FR(Q 32, Q 76) < corpus pairwise mean (0.9235) by ≥ 1σ.

**H1 (Cell B — al-Munjiya nightly Sajda + Mulk, per al-Tirmidhī #2975):**
FR(Q 32, Q 67) < corpus pairwise mean by ≥ 1σ.

**H1 (Cell C — joint pair test):**
The mean of {FR(Q32, Q76), FR(Q32, Q67)} is below the 5th percentile of permutation-null pair-means (10,000 random pair-mean samples from non-Q1 corpus).

**H0 (all cells):** Q 32's liturgical-pair distances are corpus-typical (no information-geodesic binding).

**Direction:** all three cells direction-locked.

## 3. Test design

### Cell A — Friday-fajr pair distance

From `findings/phase-b-hypotheses/csv/h-new-111.json` `D_matrix_upper_triangular`, retrieve FR(Q 32, Q 76). Compare against corpus pairwise stats (mean = 0.9235, std ≈ 0.117 from distance_matrix_stats).

**Direction-locked:** FR(Q 32, Q 76) ≤ mean - 1σ ≈ 0.806.

PASS if direction met.

### Cell B — al-Munjiya nightly pair distance

Retrieve FR(Q 32, Q 67). **Direction-locked:** FR(Q 32, Q 67) ≤ mean - 1σ ≈ 0.806.

PASS if direction met.

### Cell C — joint permutation null

Pre-committed direction: mean({FR(32, 76), FR(32, 67)}) below the 5th percentile of a permutation null built by sampling 10,000 pair-pair tuples from non-Q1 surah pairs.

PASS at α_bon = 0.017 if p_perm ≤ 0.017.

## 4. MW-6 control — hadith on-disk verification

Each cell carries an explicit hadith-attestation requirement: the pair MUST be attested in the on-disk hadith corpus with the cited collection + idInBook. The script checks:
- Bukhari idInBook 870 contains "الم تنزيل" and "هل أتى" and "الجمعة" and "الفجر" — Cell A attestation.
- Bukhari idInBook 1037 contains the same content — Cell A replication.
- Tirmidhī idInBook 2975 contains "الم تنزيل" and "تبارك" and a non-sleep verb (لا ينام / حتى يقرأ) — Cell B attestation.

If any attestation fails, the corresponding cell is flagged NULL-DATA-GAP.

## 5. Bonferroni and significance

**Bonferroni-k = 3** (Cells A, B, C). α_bon = 0.05/3 ≈ 0.017.

## 6. Pre-commit context — cross-finding-028

Cross-finding-028 (liturgical-pair FR-cohesion) reports that Q 32 is unique in being dual-paired (Friday-fajr with Q 76 AND nightly with Q 67) — a previously-established CONFIRMED finding at the aggregate-6-pair scale. This pre-reg replicates cross-finding-028 pairings P2 and P6 at the individual-pair scale, independently of the aggregate test.

This is NOT a self-test of cross-finding-028; it is an independent per-pair direction-lock check that the two Q 32-anchored pairs hold individually.

## 7. Honest limits

- The brief's hadith-numbering errors are documented and the on-disk numbers used. This is an MW-6 instrument-control: the test ANCHOR (the hadith attestation) is verified from disk, not from prompt.
- FR-distance is a root-distribution similarity instrument and does NOT measure liturgical recitational similarity (which would require phoneme/recitation-tempo data). The "binding" tested here is information-geometric, not phonological.
- Both Q 76 and Q 67 are surahs that the Prophet is reported to have favored across multiple contexts; this pre-reg does not establish exclusivity of Q 32's liturgical pairings.

## 8. Pre-commit violations

If FR(Q 32, Q 76) or FR(Q 32, Q 67) > corpus mean + 1σ (DIRECTION REVERSED), or if the joint Cell C exceeds the null 50th percentile, the finding is published as NULL — DIRECTION REVERSED with full prominence.
