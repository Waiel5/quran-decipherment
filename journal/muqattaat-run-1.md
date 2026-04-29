# Muqatta'at run 1 — Phase B novelty agent journal

**Date:** 2026-04-12
**Agent:** phase-b-novelty (muqatta'at deep dive)
**Output:** `findings/phase-b-hypotheses/muqattaat-analysis.md`
**Code dump:** `/tmp/muqattaat/{analyze,mc,markov2,write_report}.py`, results JSONs

## What I did

1. Read the methodology, statistical-rigor protocol, and integration notes. Locked the rules tuple to no-tashkeel JSON, hamza variants normalized to alif, ى→ي, mashriqi abjad, basmala counted only in surah 1 (the amrayn convention).
2. Built the canonical 29-row muqatta'at table from the JSON. Verified the 14 unique combos match the literature. Surah 42 is the special case where verse 1 (حم) and verse 2 (عسق) together form the 5-letter combo حمعسق.
3. Per-surah letter frequencies for each opening letter (raw counts and rates per 100).
4. Chi-squared (Yates-corrected) for each of the 14 luminous letters comparing rate in muqatta'at surahs vs non-muqatta'at surahs. Bonferroni-corrected for k=14.
5. Khalifa divisibility test: combined opening-letter count mod 19 for each of the 29 surahs. Spot-checked Khalifa's two famous specific claims (Q in surah 50, N in surah 68).
6. Abjad gematria: per-combo and totals for the 14 unique combinations and the 29 surah openings.
7. Order/position pattern: gaps, mod-19 residues, primes among the 29 mushaf indices.
8. Compared the 14 luminous letters to the 14 highest-frequency Quranic letters; checked makharij distribution.
9. Per-surah signature test (combined opening letters fraction) under TWO nulls:
   - Hypergeometric (analytic, equivalent to within-Quran shuffle)
   - 3-gram letter Markov surrogate with word boundaries (1000 surrogates × 29 surahs)
   - Stouffer combination across all 29 surahs.
10. Wrote the report with full per-surah tables, p-values, garden-of-forking-paths disclosure, and verdict.

## Headline numbers

- **Surah 50 (Q): ق = 57 = 19×3 EXACTLY.** Khalifa's most famous specific claim is replicated under both raw and normalized counting. Robust.
- **Surah 68 (N): ن = 131, NOT 133.** Khalifa's claim fails in our text. He achieved 133 by spelling the muqatta'at letter as نون (a non-attested edit). Bilal Philips' 1987 critique is empirically validated.
- **Only 1 of 29 muqatta'at surahs** has a combined opening-letter count divisible by 19. Random chance predicts ~1.5/29.
- **Per-letter chi-squared (Bonferroni at k=14, α=0.0036)**: 4/14 letters significant. ق over (p=9e-10), ن over (p=4e-06), ه under (p=1e-05), ر under (p=0.0036).
- **Per-surah signature, hypergeometric null, Stouffer Z = +4.30**, one-tailed p ≈ 8.6e-06. 19/29 enriched.
- **Per-surah signature, 3-gram Markov null, Stouffer Z = +4.48**, one-tailed p ≈ 3.8e-06. 19/29 enriched.
- **Bonferroni-significant individual surahs** under the Markov null: Surah 2 (الم, z=+3.43), Surah 29 (الم, z=+2.74 — fails Bonf strict but close), Surah 50 (ق, z=+4.68). The signal is **driven by ALM and Q**.
- **No abjad sum** of muqatta'at openings hits 19, 114, 786, or 6236. Sum-of-14-unique = 1757; sum-of-29 = 3385.
- **9 of 14** luminous letters are in the top 14 most frequent Quran letters. The luminous selection is biased toward frequent letters. The non-luminous 14 are dominated by emphatic/dental/sibilant low-frequency consonants (ث ذ ض ظ ز ج خ ش غ).

## Key methodological choice

I used a **3-gram letter Markov model with word-boundary tokens** as the stringent null (statistical-rigor §1.3). This controls for local letter co-occurrence (Arabic morphology) — the "Arabic just works that way" defence is partially absorbed. The signal still survives at p ≈ 4e-06.

I did NOT run null 1.4 (length-matched comparable Arabic corpus). This is the obvious next step. Until then I am classifying the finding as "passes 1.1 + 1.3 but not 1.4 yet."

## Honest assessment

The signature test passes the Phase B threshold (corrected p < 0.005 under two nulls), but with major caveats:

1. The signal is concentrated in 3 of 29 surahs. The other 26 are at noise level or anti-enriched.
2. The luminous letters are heavily biased toward frequent letters, which makes them disproportionately easy to find inside any text. The Markov null partly controls for this.
3. Khalifa's STRONG claim ("every initial letter is divisible by 19") is **falsified** — only 1 of 29 surahs satisfies it.
4. Khalifa's WEAK claim ("the muqatta'at have some statistical relationship to their surahs") is **supported**.

The truth is in between. There IS a real statistical signature, but it is much weaker and patchier than the Code-19 literature claims. The most striking single result is Surah 50, which is BOTH the cleanest enrichment case AND happens to satisfy the 57=19×3 claim exactly.

## Surprises

- Surah 38 (ص): the saad letter occurs only 29 times, vs ~19 expected. Significant under both nulls (raw p≈0.01) but tiny absolute effect.
- Surah 7 (المص), Surah 30 (الم), Surah 11 (الر), Surah 40 (حم) are *anti-enriched* — meaning, their opening letters are *less* common in their bodies than in the rest of the Quran. This is the opposite of what Khalifa would predict.
- Surah 113 (al-Falaq) has the highest ق-rate (8.2%) of any surah, despite not being a muqatta'at surah and being only 73 letters long. Small-N artifact, but a useful reminder that Q-rate is not unique to Surah 50 in absolute rate (only in raw count).

## What I'd do differently

- Run a comparable-Arabic null (Sahih Bukhari sample) to make this a Phase B "novel finding" rather than "exploratory."
- Pre-register a clean 1-hypothesis test of "ALM and Q surahs are enriched in their opening letters" on the mushaf index, then test on Tanzil Uthmani for replication.
- The 14-letter selection-bias result (luminous = frequent) is worth its own write-up; it almost certainly contributes to *why* the muqatta'at look like a signature.

## Outputs

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/muqattaat-analysis.md` (32k chars, 576 lines)
- `/tmp/muqattaat/all_results.json` (combined data dump)
- `/tmp/muqattaat/{analyze,mc,markov2}.py` (analysis scripts)

## Next agents could pick up

- Comparable-Arabic null run (need a clean Bukhari/Muslim corpus with quoted Quran stripped).
- Replication on Tanzil Uthmani text (currently using amrayn no-tashkeel JSON).
- Test register increment (this is the first Phase B finding to log).
- Investigation of Surah 50 specifically: why is ق so over-represented? Is it because the surah is thematically about resurrection (qiyāma) and uses many ق-rooted words? (Morphological corpus could answer this.)
