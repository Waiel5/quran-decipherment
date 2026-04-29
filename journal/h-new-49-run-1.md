---
date: 2026-04-15
agent: h-new-49-specialist
hypothesis: H-NEW-49 surah-name semantic classification
status: COMPLETED, PARTIAL-PASS
---

# H-NEW-49 — run 1 journal

## Order of operations (integrity)

1. Read environment context (cwd, repo layout, prior H-NEW format conventions).
2. Inspected only the JSON STRUCTURE of `quran-no-tashkeel.json` (saw the schema and Q1 al-Fātiḥa name + first verse of Q2 al-Baqara). NO surah-name list inspected before the next step.
3. WROTE pre-registration `h-new-49-surah-name-class-prereg.md` from memory of canonical 114-surah list. Locked 9-class taxonomy and assignment principles in the pre-reg.
4. Wrote `scripts/h_new_49_surah_name_class.py` with the SURAH_CLASS dict freshly populated from memory + locked-tie-breaker rules. The class+root assignment was committed in code BEFORE running.
5. Ran the script. Saved JSON output.
6. Wrote findings document.

## Key results

| Cell | Statistic | p | Verdict |
|---|---|---|---|
| 1 | 9-class distribution | n/a | descriptive |
| 2 | χ² muq×class (pooled, df=6) | 0.0159 | TREND, fails α_bon=0.01 |
| 3 | MUQATTAAT_LETTER perm | 0.00364 | PASS (tautology, MW-5 wiring control) |
| 4 | Long/short mufaṣṣal Fisher | 1.000 | NULL (as pre-registered for Q59) |
| 5 | Lexical centrality | 18/110 sig | EXPLORATORY (16% < 33% threshold) |

## Pre-reg honesty notes

1. **MW-5 mis-prediction recorded**: I pre-registered "Q71 Nūḥ should be the most extreme outlier in Cell 5" based on memory that Nūḥ is named ~28 times. Actual: only 3 explicit "نوح" tokens in Q71 (most references are pronominal/verbal). The MW-5 still passes in DIRECTION (21× rest-corpus enrichment, p=4e-4) but is NOT the most extreme outlier — Q12 Yūsuf is, with 25 hits and p≈1e-59. I corrected this in the findings doc rather than amending the pre-reg.

2. **Q59 al-Ḥashr was correctly pre-classified as EVENT_ESCHATOLOGICAL** with the explicit pre-reg note that the Khawātim al-Ḥashr divine-names CONTENT is not the SURAH-NAME. This NULL was honestly predicted.

3. **Cell 2 fails α_bon by ~1.6×**. I report raw p and Bonferroni-adjusted both. Directional pattern (PROPHET_PERSON 7/11=64% muq-opener vs EVENT_ESCH 1/18=6%) is striking and consistent with known long-Meccan-narrative pattern.

4. **Taxonomy single-shot**: I did not test sensitivity to taxonomy. A binary partition (PROPHET_PERSON vs all-else) would likely clear α_bon. This is a follow-up.

## Garden-of-forking-paths log (BEFORE running)

Recorded in pre-reg: I knew Q2 (Baqara, animal) opens with muqaṭṭaʿāt; I knew Q12, Q19, Q20, Q36, Q38, Q50 are name-IS-or-near-muqaṭṭaʿāt; I predicted ANIMAL and PROPHET classes would be muqaṭṭaʿāt-enriched; I predicted Q59 al-Ḥashr name would NOT be DIVINE_ATTRIBUTE.

Outcome: PROPHET_PERSON enrichment confirmed (7/11), ANIMAL enrichment partial (5/13 = 38% > 25% baseline but not striking), Q59 NULL confirmed.

## Compute

- 10⁵ permutations for Cell 3 ran in ~10s.
- Cell 5 ran 110 binomial tests in ~5s.
- Total runtime ~30s.

## Files

- `findings/phase-b-hypotheses/h-new-49-surah-name-class-prereg.md`
- `scripts/h_new_49_surah_name_class.py`
- `findings/phase-b-hypotheses/csv/h-new-49.json`
- `findings/phase-b-hypotheses/h-new-49-surah-name-class.md`

## Verdict

PARTIAL-PASS. The taxonomy + per-surah class assignments are now a permanent locked artefact for downstream H-NEW hypotheses (e.g., name-class × verse-length, name-class × chronological-order, name-class × abjad-residue). The most striking single result is Q12 Yūsuf as the cleanest name→content lexical predictor in the entire corpus (p ≈ 1e-59).
