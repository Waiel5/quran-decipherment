# H-NEW-123 Run 1 — Journal

**Date**: 2026-04-17
**Specialist**: h-new-123-specialist
**Task**: Heap's-law exponent β for Quran vs matched Arabic corpora

## Timeline

1. Read HANDOFF/01-WHAT-WE-KNOW, HANDOFF/04-DISCIPLINE, HANDOFF/05-OPEN-QUESTIONS briefly
2. Inventoried `data/baseline-corpora/raw/`: confirmed `matched-bukhari-77k.txt` (77,797 words), `jahiz-hayawan.txt` (362K words), and 7 cleaned `muallaqa-*.txt` files (~7,300 words total)
3. Reused normalization logic from `data/baseline-corpora/analyze.py` (tashkeel strip, recitation-mark strip, whitespace split) to match H-NEW-48 baselines exactly — preserves MW-1 length-match consistency
4. Wrote pre-reg at `findings/phase-b-hypotheses/h-new-123-heap-law-prereg.md` with:
   - k=4 Bonferroni family (3 baseline cells + 1 shuffled-Quran cell)
   - α_Bon = 0.0125
   - Direction locked: β_Quran < β_baseline (one-sided); β_Quran ≠ β_shuffled (two-sided)
   - Fit locked: log-log OLS, step=50, start=100, block-bootstrap block=100, 1000 resamples
   - Positive controls locked: IID-uniform expects β<0.5; all-unique expects β≈1.0
5. Wrote `scripts/h_new_123_heap_law.py`; ran.
6. Results:
   - MW-5 positive controls PASS (β_iid=0.285, β_unique=1.000)
   - β_Quran = 0.7468; β_Bukhari = 0.7472 (tied); β_Jahiz = 0.8023; β_Muallaqat = 0.8313; β_shuffled = 0.7072
   - Cell A1 (Q<Bukhari): p = 0.38 — FAIL (contrary to classical claim)
   - Cell A2 (Q<Jahiz): p = 0.001 — PASS
   - Cell A3 (Q<Muallaqat): p = 0.001 — PASS (length caveat: Muallaqat only 7.3K)
   - Cell B (Q vs shuffled): p = 0.33 — NULL; β is shuffle-invariant
7. Per-surah: restricted to N≥200 (noise filter, disclosed in pre-reg as "flagged post-hoc for short surahs"). Top compressed = surah 55 Ar-Rahman (refrain surah, β=0.731). Top diverse = surah 32 As-Sajda (muqaṭṭāʿat, β=0.950).
8. Secondary muq vs nonmuq: p=0.25, NULL.
9. Wrote findings `findings/phase-b-hypotheses/h-new-123-heap-law.md` with honest 2/4 PASS, 1/4 FAIL, 1/4 NULL summary.

## Deviations from pre-reg

- Per-surah ranking restricted to N≥200 (same filter applied to muq/nonmuq Mann-Whitney). This was foreshadowed in the pre-reg ("β noisy for small surahs") but the specific N≥200 threshold was set during script-writing before viewing results. Minor; the exploratory tertiary cell's sign is unchanged at thresholds 100, 200, 500.

## Key methodological notes

- Muʿallaqāt vs Quran is NOT length-matched (7.3K vs 77.8K); this is the length-curvature artifact (MW-1 concern) and flagged in the findings caveats.
- Shuffled Quran used seed 20260417 (declared in pre-reg).
- Bootstrap is paired-by-resample-index (each baseline's resamples are independent of Quran's, but paired with the same seed offset). This is the standard approach for cross-corpus bootstrap β comparison.

## What this finding does and does not show

Does show: the Quran's type-token growth rate is lower than Jāḥiẓ and Muʿallaqāt but indistinguishable from Bukhārī; the compression is carried entirely by token frequency distribution, not by ordering.

Does NOT show: that the Quran is "uniquely" compact, nor that its ordering is trivial (it does not test ordering at Markov or syntactic levels; it only tests Heap's law). A higher-sensitivity ordering test (e.g., n-gram entropy, trigram perplexity) could still detect ordering effects invisible to Heap.

## Verdict

PASS-DIRECTED on the two Bonferroni-surviving cells (A2, A3); FAIL on A1; NULL on B. Honestly mixed result. Replication queued (MATTR or Yule's K on same corpora).
