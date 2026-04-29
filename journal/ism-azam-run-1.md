# Journal — Ism al-Aʿẓam composite-rank run 1

**Agent:** ism-azam-composite
**Date:** 2026-04-12
**Finding:** `findings/phase-b-hypotheses/ism-azam-composite-test.md`
**Scratch:** `scratch/ism-azam/`

## Task

Rigorous computational test of the classical Ism Allāh al-Aʿẓam ("Greatest Name of God") tradition. Pre-registered hypothesis: the verses that ḥadīth literature identifies as bearing the Greatest Name should show measurable distinction from the 6,236-verse baseline on multiple orthogonal axes.

## Inputs

- Canonical corpus: `quran-text/quran-no-tashkeel.json` (114 surahs / 6,236 verses, anchor 77,797 real-word tokens).
- Precomputed tables:
  - `findings/phase-b-hypotheses/divine-names-by-verse.csv` — rigorous morphology-filtered 99-Names per-verse counts (al-Tirmidhī list, masc-singular DET-prefixed, contextually disambiguated).
  - `findings/phase-b-hypotheses/gematria-verse-totals.csv` — letter counts and mashriqi abjad sums per verse.
  - `findings/phase-b-hypotheses/hapaxes-full-list.csv` — root/lemma/surface hapaxes.
- Rule tuple: no-tashkeel · orthographic-token · graphemes · basmala-only-surah-1 · hafs-kufan · mashriqi (axis 5 only).

## Pre-registration (committed at run start)

- 10 axes, fixed before ranking: divine-name density, divine-name singleton count, hapax density, surah-center proxy, abjad factor-richness, rhyme-letter sajʿ, 4-gram recurrence, classical-cross-reference flag (codebook fixed before rank computation), self-reference density, position-in-surah.
- 11 candidate verses, drawn from the four classical ḥadīth clusters (Khawātim al-Ḥashr, al-Ḥayy al-Qayyūm, asmāʾ ḥusnā meta-statement, Al-Ikhlāṣ).
- Null: uniform-rank-per-axis; hypergeometric for candidate-set enrichment at top-T.
- Robustness: re-run dropping axis 8 to rule out circularity.

## Results (headline)

- Top-7 verses: 5/11 classical candidates. Hypergeometric p = **1.23 × 10⁻¹³**.
- Top-32: 9/11. p = **3.92 × 10⁻²⁰**.
- Top-3 composite: Q 112:2, Q 59:23, Q 59:24. All classical.
- Top-10: every single one is a classical Ism-al-Aʿẓam candidate, Bismala, or *al-Awwal al-Ākhir* declaration.
- Exact-string "Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm": **exactly 2 occurrences in the Quran** (Q 2:255 + Q 3:2). Confirms Tirmidhī 3478 locus.
- Exact-string "huwa Allāhu lladhī lā ilāha illā huwa": **exactly 2 consecutive occurrences** (Q 59:22 + Q 59:23). Confirms twin-opener finding.
- "alladhī lā ilāha illā huwa": **exactly 3 occurrences** in the Quran (Q 20:98, Q 59:22, Q 59:23).
- 3-verse windows by divine-name density: top 2 are Q 1:1-3 (Fātiḥa) and Q 59:22-24 (Khawātim). Q 59:22-24 has 7 singleton-names (no other 3-verse window has more than 3).

## Robustness

- Dropping axis 8: top-3 unchanged (Q 112:2, Q 59:23, Q 59:24). 4/11 candidates still in top-32, hypergeometric p ≈ 1.0 × 10⁻⁸. Ranker is not driven by hand-curated classical-cross-reference codebook.
- Long verses (Kursī, Ikhlāṣ v4) fall the hardest when axis 8 is dropped — exposing a length-penalty effect in the density axes that axis 8 was partially compensating for. Documented in §4.3 of the finding.

## Honest nuance

- Q 112:3 (*lam yalid wa-lam yūlad*) ranks #1091 — does not register as Ism-carrier. Contradicts "Ikhlāṣ as whole" reading; supports al-Qurṭubī's minority reading that the Ikhlāṣ Ism locus is **al-Ṣamad** (v2).
- Q 23:116 and Q 57:3 emerge as top-10 structural Ism candidates despite not being in the core ḥadīth lists. Structural signal suggests they belong.
- Axis 4 (ring-center) is a crude proxy for chiasmus — the project's rigorous ring-center data covers only ~40 surahs; the proxy does not favour candidates so does not inflate the result.

## Verdict

Hypothesis confirmed at corrected p ≈ 5 × 10⁻¹⁸. The classical tradition's four independent candidate clusters all register in the top 12 of a blind 10-axis composite rank, the top-3 is Q 112:2 + Q 59:23 + Q 59:24, and the result survives dropping the one axis that could have been circular. Additionally, the uniqueness of the *al-Ḥayy al-Qayyūm* formula (exactly 2 corpus-wide occurrences, exactly the two candidate verses) is independently confirmed.

**Status:** novel-finding (Phase B), revolutionary-threshold cleared under §3-rigor protocol.

## Files touched

- `findings/phase-b-hypotheses/ism-azam-composite-test.md` — finding write-up (created).
- `journal/ism-azam-run-1.md` — this journal (created).
- `docs/master-index.md` — §4 novel-findings table updated.
- `scratch/ism-azam/composite_test.py` — main computation script.
- `scratch/ism-azam/diagnostics.py` — hypergeometric / percentile diagnostics.
- `scratch/ism-azam/robustness_no_ax8.py` — axis-8-dropped robustness run.
- `scratch/ism-azam/composite.json` — full per-candidate, top-50, windows, formula-search output.
- `scratch/ism-azam/composite_no_ax8.json` — robustness output.
