# H-NEW-244 run-1 journal — Q 1 as *umm al-kitāb* compression test

Date: 2026-04-17
Specialist: specialist-B (autonomous compression cell)
Seed: 20260419
Pre-reg SHA-256: `02208c5f561c15185daf1d1cc27e2dd66cb8a636944d2e6f94f3f9e12436d1b6`

## Run sequence

1. Read H-NEW-231 (per-surah KL, ρ=-0.967 length dominance) to lock
   smoothing at Dirichlet α=0.5.
2. Read H-NEW-155 (Q 1 sui-generis, dispersion 50.4%) to lock Cell B
   root-stemmer (QAC v0.4 STEM) and align null design.
3. Read H-NEW-192 (Q 1 Δ=−104 position residual) for context on
   expected Cell A/C direction.
4. Wrote pre-reg `h-new-244-fatiha-umm-al-kitab-prereg.md` with
   direction UP (top-5%) on each cell, Bonferroni-3 α_bon=0.0167.
5. Wrote `scripts/h_new_244_fatiha_compression.py`; ran once at
   seed 20260419.

## Environment

- Python 3 (system).
- Corpus: `quran-text/quran-no-tashkeel.json` (6236 verses, 114
  surahs).
- QAC: `data/morphology/quranic-corpus-morphology-0.4.txt` (1642
  STEM roots).

## Run notes

- Script runtime: ~60 sec for 6230 windows at VSIZE=36,653 4-grams.
- Cell A computed straightforwardly as KL(p_window || p_rest) with
  Dirichlet α=0.5 on global 4-gram vocabulary.
- Cell B replicated H-NEW-155 dispersion logic (QAC STEM roots) at
  slightly different normalisation — same qualitative outcome
  (50.0% vs H-NEW-155's 50.4%).
- Cell C computed as KL(p_surah || p_rest) / verse_count for each
  of 114 surahs, ranked Q 1.

## Result summary

| Cell | Direction | Rank | Verdict |
|---|---|---|---|
| A — window KL rank | top-5% | 4920/6230 = 79%ile | **NULL** |
| B — cross-surah root presence | upper tail | p=0.002 | **PASS** (α_bon=0.0167) |
| C — per-verse KL rank | top-5% | 102/114 = 89%ile | **NULL** |

**MW-5 cheat controls PASSED** — random 7-verse windows land
mid-distribution (47-87%ile), confirming instrument discriminates.

## Pre-reg compliance

- Direction UP pre-committed all 3 cells before execution.
- Bonferroni k=3 α_bon=0.0167 applied.
- No deviation from pre-reg rules tuple.
- Cell B p-value (0.002) < 0.0167 → PASS.
- Cell A + C percentiles (79, 89) far from 5% threshold → NULL.
- Verdict: MIXED-SUPPORT (1 PASS, 2 NULL).

## Interpretive turn

The surprising result is Cell A/C NULL. The classical *umm al-kitāb*
claim is confirmed at the ROOT level (Cell B) but refuted at the
CHAR-4-GRAM DISTRIBUTION level. This is coherent with:
- H-NEW-231 length dominance (short surahs diverge character-wise).
- H-NEW-192 Q 1 residual Δ=−104 (Q 1 distributionally belongs at
  position ~100-114, not position 1).
- H-NEW-238 Q 1→Q 2 edge rank 114/114 (these two surahs are
  distributionally very different at char-4-gram).
- H-NEW-155 sui-generis (Q 1's dispersion is root-level, not
  distribution-level).

The classical tradition (al-Suyūṭī, al-Ghazālī, al-Rāzī) actually
frames *umm al-kitāb* thematically/root-wise, not distributionally —
so Cell B PASS + Cells A/C NULL is a precision-sharpening of the
classical claim rather than a refutation.

## Files emitted

- `findings/phase-b-hypotheses/h-new-244-fatiha-umm-al-kitab-prereg.md`
- `scripts/h_new_244_fatiha_compression.py`
- `findings/phase-b-hypotheses/csv/h-new-244.json`
- `findings/phase-b-hypotheses/h-new-244-fatiha-umm-al-kitab.md`
- `journal/h-new-244-run-1.md` (this file)
- MASTER-LEDGER Wave-4 addendum (next commit).

## Honest limits flagged for downstream

- Char-4-gram is ONE encoding. Fisher-Rao on root frequency would
  likely favour Q 1 (H-NEW-244.1 queued).
- Dirichlet α=0.5 chosen to match H-NEW-231; α-sensitivity not
  tested inline (signal size should be robust).
- 7-verse windows cross surah boundaries; top-representative windows
  are predictably Baqarah-dominant.
- No out-of-corpus Arabic control.
