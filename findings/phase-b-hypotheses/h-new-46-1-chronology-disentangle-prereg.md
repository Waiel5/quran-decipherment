---
id: H-NEW-46.1
title: Disentangle H-NEW-46 muqaṭṭaʿāt-vs-length finding from Meccan/Medinan chronology
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running null model and BEFORE OLS regression)
parent_finding: H-NEW-46 (STRONG-PASS, 4/4 cells, p ≤ 1.6×10⁻⁴)
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended-Disentangle
bonferroni_k: 7
alpha_bon: 0.00714286   # = 0.05 / 7
rules_tuple: (no-tashkeel, hafs-kufan, verse-count metric, period-strata)
chronology_source: Tanzil Egyptian Standard period field (Meccan/Medinan); aligns with al-Suyūṭī al-Itqān nawʿ 9 standard 86 Meccan / 28 Medinan split
chronology_file: data/revelation-order.csv (column 'period')
primary_data: 114 surah lengths (verse counts) + 29 muqaṭṭaʿāt-opened indicator + period stratum
seed: 20260416
---

# [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] — Chronology Disentanglement Pre-Registration

## Question

Does muqaṭṭaʿāt presence still predict surah length AFTER controlling for Meccan-vs-Medinan revelation period?

[[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] established 4/4 Bonferroni-4 PASS that muqaṭṭaʿāt-opened surahs are dramatically longer than uniform random selection would predict. The dominant nuisance hypothesis is **chronological confounding**: most muqaṭṭaʿāt are Meccan (or Medinan), and Meccan/Medinan surahs have known length differences (Medinan tend to be longer on average; Meccan vary, with late-Meccan also long). If the muqaṭṭaʿāt-length signal vanishes after stratifying by period, then [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] reduces to "muqaṭṭaʿāt are concentrated in middle/late-Meccan, which is also where long surahs live."

If it survives stratification → muqaṭṭaʿāt independently predict length even within period.

## Garden-of-forking-paths disclosure

The eyeball at [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] stage was Q 2 (Medinan, 286 v.), Q 7 (Meccan, 206 v.), Q 26 (Meccan, 227 v.) all open with muqaṭṭaʿāt. This eyeball is bidirectional w.r.t. chronology: Q 2 is Medinan, Q 7 and Q 26 are Meccan. So no chronology-specific bias was introduced in cell selection.

Pre-cleared with the parent author: this disentanglement was named in [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]'s Mechanism section (mechanism #1 "chronological correlate, most plausible"). [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] is the locked test of that mechanism.

## Chronology source — locked

**Tanzil Egyptian Standard** (Meccan / Medinan column in `data/revelation-order.csv`).
This file is the project's canonical source for revelation-period classification. It uses the standard Egyptian-edition split (86 Meccan / 28 Medinan) which corresponds to **al-Suyūṭī's al-Itqān fī ʿulūm al-Qurʾān, nawʿ 9** (the chapter on Meccan vs Medinan classification). Document: `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`.

Where Tanzil and al-Suyūṭī's al-Itqān nawʿ 9 differ for individual surahs (small set: Q 13, 47, 55, 76, 99, 13, 98 are debated), Tanzil follows the Egyptian-edition consensus. We use Tanzil as the canonical chronology because:
(a) it is the project's already-existing reference file, and
(b) it matches the standard 86/28 split cited in al-Itqān as the dominant view.

**Locked split:** 86 Meccan + 28 Medinan = 114.

**Locked muqaṭṭaʿāt-by-period** (computed BEFORE running statistical tests):
- Muqaṭṭaʿāt Meccan (26): {7, 10, 11, 12, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
- Muqaṭṭaʿāt Medinan (3): {2, 3, 13}

Note Q 13 (al-Raʿd) is the only borderline case in the standard split — Tanzil/Egyptian consensus marks it Medinan; Nöldeke marks it late-Meccan. We use Tanzil's classification as locked. A sensitivity-analysis variant treating Q 13 as Meccan is pre-disclosed in §"Sensitivity" below.

## The 7 pre-registered cells

For each, locked α_bon = 0.05/7 = 0.00714.

### Stratum cells — within Meccan only

#### Cell A1 — Mean verse-count enrichment, Meccan stratum

Test: mean verse-count of 26 muq-Meccan surahs vs uniform random 26-from-86 sampling within the Meccan subset; one-sided upper.

#### Cell A2 — Top-K representation, Meccan stratum

Define top-K = top-26 longest Meccan surahs. Test: how many of the 26 muq-Meccan are in this top-26? One-sided upper.

### Stratum cells — within Medinan only

#### Cell B1 — Mean verse-count enrichment, Medinan stratum

Test: mean verse-count of 3 muq-Medinan vs uniform random 3-from-28 sampling within the Medinan subset; one-sided upper.

#### Cell B2 — Top-K representation, Medinan stratum

Define top-K = top-3 longest Medinan surahs. Test: how many of the 3 muq-Medinan are in this top-3? One-sided upper.

### Combined / mixed cells

#### Cell C1 — Stratified Mann-Whitney by period

Compute the Mann-Whitney U statistic for muq-vs-non-muq within each stratum; combine across strata via stratified-MW pooled-z (van Elteren method). Two-sided p.

#### Cell C2 — OLS coefficient on muqaṭṭaʿāt indicator after period control

Linear model: `verse_count ~ 1 + I(period=Medinan) + I(muqaṭṭaʿāt)`. Report coefficient on muqaṭṭaʿāt with t-test p (two-sided). NB: heteroskedastic, so we ALSO report HC1 robust SE p-value, and the headline p is the more conservative of the two.

#### Cell C3 — Permutation residualized null

Residualize length on period (subtract within-period mean). Then test mean-residual for muq vs non-muq via uniform-random 29-from-114 permutation null on residuals (10⁵ perms). One-sided upper.

This is the **MW-1 length-residualization equivalent**: matches the standard residualization battery applied across the project. Pre-cleared as the canonical disentanglement test.

## Null model

For cells A1, A2: 10⁵ uniform random samples of 26-from-86 (within Meccan subset). Seed = 20260416.
For cells B1, B2: ALL C(28,3) = 3276 combinations enumerated exactly (combinatorial null, no permutation needed because n is small). Seed not used; exact.
For cell C1: standard van Elteren stratified-MW (analytic + 10⁵ permutation cross-check). Seed = 20260416.
For cell C2: OLS with two p-values reported (classical t-test + HC1 robust). No permutation needed; report both, headline = conservative.
For cell C3: 10⁵ uniform random 29-from-114 permutation null on residualized lengths. Seed = 20260416.

## MW-5 positive control

Plant the 26 longest Meccan surahs as fake-muq-Meccan; cell A1 should give p ≈ 1/(N+1) ≈ 1×10⁻⁵.
Plant the 3 longest Medinan surahs as fake-muq-Medinan; cell B1 should give p = 1/3276 ≈ 3.05×10⁻⁴ (combinatorial floor for 3-from-28 with 3 longest exact, since the 3 longest is exactly one combination out of C(28,3)).

If either positive control fails, flag pipeline as broken.

## MW-7 internal-error gate

Sanity-check: muq-Meccan length distribution must produce mean = exact mean of {len(s) for s in {7,10,...}} from no-tashkeel verse-count list. If it doesn't match a manual recompute, error.

## Pre-committed verdict table

Verdict is a 2-d label: (cell-count, OLS coefficient sign+significance).

| Outcome on cells A1,A2,B1,B2,C1,C3 + OLS-C2 | Verdict |
|---|---|
| 0 of 7 cells significant at α_bon | NULL — [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] fully explained by chronology |
| 1-2 of 7 cells significant | EXPLORATORY — chronology absorbs most signal |
| 3-5 of 7 cells significant + OLS coef positive | PARTIAL-PASS — muq independently predicts length within period |
| 6-7 of 7 cells significant + OLS coef positive at p<α_bon | STRONG-PASS — muq predicts length INDEPENDENT of chronology |

Headline OLS coefficient comparison: the headline number is the muq coefficient from cell C2 (verse-count units). Report alongside the unstratified [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] effect (94.59 − 41.08 = ~53.5 verses gross gap).

## Sensitivity (pre-disclosed)

If headline verdict is sensitive to whether Q 13 is classified Meccan or Medinan (the only standard-list borderline case), report both classifications. We label the Tanzil/Egyptian "Q 13 = Medinan" as the LOCKED variant; the "Q 13 = Meccan" recomputation is a sensitivity check, NOT a verdict-altering rerun.

## Mechanism interpretation (pre-stated)

- **NULL outcome interpretation**: [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]'s effect would be a chronology artifact. Long surahs ARE Medinan or middle/late-Meccan; muqaṭṭaʿāt cluster in those same chronological cohorts. The classical literature has long-noted muqaṭṭaʿāt are absent from early-Meccan and short surahs; this would just confirm that observation without adding independent structure.
- **PARTIAL/STRONG-PASS interpretation**: muqaṭṭaʿāt predict length over and above chronology. This would mean there is a length-dimension to the muqaṭṭaʿāt-assignment process that is not subsumed by Meccan/Medinan period. Mechanism candidates remain: (i) structural authority hypothesis (long surahs marked with distinctive opener), (ii) mnemonic/recitation anchor for long surahs, (iii) a now-lost compositional convention.

## Integrity

- Chronology source LOCKED before any computation. All cells declared before null. Bonferroni-7 declared before null.
- All 7 cells published whether PASS or NULL (rules: publish PASS/NULL identically).
- Cell C2 reports BOTH classical-t and HC1-robust p; headline = max (more conservative).
- Cell C3 is the MW-1 residualization equivalent.
- Cell A1, B1 use stratified random null (not full 29-from-114) so the test is "muq longer than other surahs in the SAME period?", which is the disentanglement question.
- Q 13 sensitivity pre-disclosed; locked answer is Tanzil/Egyptian "Q 13 = Medinan".
- Bonferroni-7 includes the 4 stratum cells (A1, A2, B1, B2) + 3 combined cells (C1, C2, C3).
- Family name: 2026-04-16-Wave-Muqattaat-Extended-Disentangle (separate from parent [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] family to avoid double-counting).

## Reproducibility

- Seed: 20260416 (matches [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]/46 wave)
- N_PERM: 100,000 for cells A1, C3; exact enumeration for B1, B2; analytic+perm for C1; analytic for C2.
- Loader: `analysis.tools.loader.load_quran('no-tashkeel')`
- Chronology: `data/revelation-order.csv` (Tanzil Egyptian Standard)
- Pre-reg SHA-256 captured into JSON output as `prereg_sha256`.

## Files

- This pre-reg: `findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle-prereg.md`
- Script: `scripts/h_new_46_1_chronology_disentangle.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-46-1.json`
- Findings: `findings/phase-b-hypotheses/h-new-46-1-chronology-disentangle.md`
- Journal: `journal/h-new-46-1-run-1.md`
