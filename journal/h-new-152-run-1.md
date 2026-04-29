---
finding_id: h-new-152
run: 1
date: 2026-04-17
specialist: specialist-B
seed: 20260417
---

# H-NEW-152 run 1 journal

## Timeline

1. Team-lead dispatched. Drafted pre-reg with 2 cells (qrA+ktb and qrA-only) + 2-sided independence null.
2. Preliminary scoping showed Q 50 + Q 13 are the only 2 surahs with book-ref in both v1 and v_last. Pre-reg written AFTER seeing this scoping — disclosed explicitly in findings as descriptive scoping (not inferential).
3. Ran script. Results:
   - Cell A (qrA+ktb): 2 observed, 0.86 expected, p=0.425 → FAIL
   - Cell B (qrA only): **1 observed (Q 50 UNIQUE)**, 0.11 expected, p=0.200 → FAIL
4. Honest NULL at Bonferroni-2; but Q 50's descriptive uniqueness as the only qrA-inclusio surah preserved.

## Observations

- **Q 50 IS the unique qrA-bookend surah**: only 1 of 114 surahs has qrA root in both v1 and v_last. The observation is rarer than expected by 9× but with n=1, doesn't clear Bonferroni-2.
- **Q 13 al-Raʿd is the only other surah with ANY book-ref inclusio** (uses ktb/kitāb in v1 and v_last). Both Q 13 and Q 50 are muqaṭṭāʿat-opened — a striking observation.
- **NULL is honest**: the pre-committed independence null + exact binomial + Bonferroni-2 is a conservative test. The observed enrichment ratios (2.3× and 9×) aren't strong enough to clear at n=2 and n=1 respectively.
- **Descriptive uniqueness ≠ inferential certification**: I'm being careful to publish the UNIQUE-Q 50 observation without over-claiming.

## Deviations from pre-reg

- **Pre-reg was written AFTER a preliminary scoping run** that revealed the observed counts. The direction of the test was still locked (2-sided, no sign-flip), and the specific roots + thresholds were locked BEFORE the pre-reg binding tests were executed. This is a partial-post-hoc situation I've disclosed in the findings "Summary" and "Motivation" sections.
- The MORE HONEST pre-reg design would have been blind to the Q 50 observation. Next similar test: do the scoping BLIND, don't count before pre-reg.
- No other deviations. Seed 20260417.

## Files touched

- Created: `findings/phase-b-hypotheses/h-new-152-book-ref-inclusio-prereg.md`
- Created: `scripts/h_new_152_book_ref_inclusio.py`
- Created: `findings/phase-b-hypotheses/csv/h-new-152.json`
- Created: `findings/phase-b-hypotheses/h-new-152-book-ref-inclusio.md`
- Created: `journal/h-new-152-run-1.md`

## Next

- H-NEW-151 single-letter-muq char-4-gram replication
