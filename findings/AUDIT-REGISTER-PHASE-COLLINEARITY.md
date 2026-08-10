# Audit: "control for register" is undefined against phase for 43% of the corpus

**Date:** 2026-08-09
**Status:** STRUCTURAL CONSTRAINT. Applies to every test that stratifies on Neuwirth–Sinai register
while testing against Meccan/Medinan phase.
**Found:** in F-20's Step-0 report; independently recomputed here before publication.

---


> ## ⚠ CORRECTION, 2026-08-10 — three errors in this file's own arithmetic
>
> Caught by the F-20 lane during reconciliation, verified here before amending.
>
> 1. **The "115 rows / one spurious row" claim was wrong.** The extra row is the **header line**.
>    The TSV's column-name row does not begin with `#`, so a comment-strip leaves it in. There are
>    **114 surah rows**, exactly as there should be. My §4 limit guessed at a malformed record; the
>    real cause was a parse that never checked whether its first field was a number.
> 2. **§1's table sums to 113, not 115.** Two rows are missing from it. The underlying tabulation
>    had **four** phase columns — `Meccan`, `Medinan`, plus a `liturgical` value and a malformed
>    `neuwirth_p` — and I published only the first two without saying where the rest went. That is
>    a table that does not add up, printed without checking that it adds up.
> 3. **The 43% figure is coarsening-dependent and sits at the LOW end of its range.** Recomputed
>    across four coarsenings on a verified 114-row parse: **36.8%** (6-class) · **40.4%** (this
>    file's coarsening, correctly parsed) · **43%** (as published) · **57.0%** (finer head-term,
>    oath split before eschatological). §4 predicted this and it is confirmed — but the prediction
>    does not excuse quoting a single number as though it were stable.
>
> **The structural conclusion survives and is the reason this file still stands.** On a verified
> 114-row parse, `legal` reproduces exactly at 0 Meccan / 15 Medinan, `oath` exactly at 8 / 0, and
> `narrative` remains single-phase (23 / 0 rather than 26 / 0). The three degenerate strata are
> real; only the cell counts and the headline percentage were wrong.
>
> **The transferable point is now sharper than the one this file was written to make:** the
> *coarsening choice is itself a deciding parameter* in the sense of
> [[cross-finding-029-the-deciding-parameter]], and it belongs in any register-stratified
> pre-registration alongside the length channel. Named consumers of this label file, for whoever
> audits them: `h-new-3010`, `h-new-3040`, `h-new-3080`, and the `h-new-127-*` family.

## 1. The crosstab

`findings/classical-sources/neuwirth-sinai-genre-labels.tsv`, 115 surah rows, genre coarsened to its
head term, phase reduced to Meccan/Medinan:

| register | Meccan | Medinan | |
|:--|--:|--:|:--|
| eschatological | 24 | 1 | |
| hymn | 6 | 1 | |
| **legal** | **0** | **15** | **← occurs in one phase only** |
| **narrative** | **26** | **0** | **← occurs in one phase only** |
| **oath** | **8** | **0** | **← occurs in one phase only** |
| polemic | 5 | 3 | |
| other | 18 | 6 | |

**49 of 115 surahs (43%) sit in a register that occurs in only one phase.**

## 2. Why this matters, stated precisely

A register-stratified permutation test against phase permutes labels *within* each register stratum.
A stratum containing only one phase has **nothing to permute** — every permutation returns the
observed value. Those 49 surahs contribute **zero information** to the null distribution while still
appearing in the sample size.

So a test reporting *"n = 115, stratified on register"* is, against phase, effectively running on
**66 surahs** — and the remaining strata are themselves lopsided (the mixed registers skew Meccan).
The reported n is not the effective n.

This is not a claim that such tests are wrong. It is a claim that **their power is smaller than
their sample size implies, and none of them have said so.**

## 3. The deeper problem: the confound is not separable

The three collinear registers are exactly the ones the Meccan/Medinan confound is *about*. Legal
discourse **is** Medinan; narrative and oath openings **are** Meccan. That is not a sampling
accident — it is the substantive content of the periodisation itself.

**Therefore "does X track phase independently of register?" is not answerable for those 49 surahs by
any amount of stratification.** No estimator recovers a within-stratum contrast from a stratum with
one level. The honest options are:

1. **Ablation** — drop the collinear registers and test on the 66 that carry information, reporting
   the reduced n and its MDE.
2. **Reframe** — accept that register and phase are partly the same variable here and stop claiming
   to separate them.

What is not available is the third option everyone reaches for: run the stratified test, get a
number, and report it as though register had been controlled.

## 4. Honest limits on this audit

- **The coarsening is mine.** Genres were reduced to head terms (`legal`, `narrative`, `oath`,
  `hymn`, `eschat`, `polemic`, `other`). A finer partition splits these cells and could change which
  strata are degenerate — though it can only make strata *smaller*, so degeneracy will generally
  increase, not decrease.
- **The TSV carries a `liturgical` value and one malformed row** that my parse bucketed to `other`;
  115 rows parsed against 114 surahs, so one row is spurious. Neither affects the three collinear
  registers, whose counts are large and unambiguous.
- **F-20's independent count differed slightly** (27 narrative vs my 26) — a coarsening difference,
  not a disagreement about the structure. Both found legal and narrative perfectly collinear; this
  recount additionally found **oath**.

## 5. What should happen

Any existing finding that stratifies on Neuwirth–Sinai register while testing against phase should
state its **effective** n — the count of surahs in strata containing both phases — alongside its
nominal n. That is a one-line addition and it changes no verdict; it only stops a reader inferring
power that was never there.

This is the register instance of the same lesson as
[[cross-finding-029-the-deciding-parameter]] and [[AUDIT-LENGTH-CHANNEL-EXPOSURE]]: **a control
that is named but not examined can fail silently, and nothing downstream announces it.** A degenerate
stratum produces a perfectly well-formed p-value.

Related: [[AUDIT-LENGTH-CHANNEL-EXPOSURE]] · [[cross-finding-029-the-deciding-parameter]] ·
[[ABSENCE-CLAIMS]] · [[UNIT-DRIFT-DEFECT]]
