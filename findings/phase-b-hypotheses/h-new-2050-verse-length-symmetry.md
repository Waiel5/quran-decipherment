---
finding_id: H-NEW-2050
title: Within-surah verse-length symmetry + central-pivot — palindrome/pivot NULL, monotone-gradient CONFIRMED
phase: B
status: DIRECTIONAL — H1 (palindrome/pivot) NULL; H2 (monotone-gradient) PASS
date: 2026-05-29
executed_by: specialist-H-NEW-2050
seed: 20260509
rules_tuple: (no-tashkeel, word=whitespace-token, words-per-verse, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)
n_perm: 10000
bonferroni_family: 3 statistics × 109 eligible surahs
alpha_bonferroni: 1.529e-04
prereg_sha256: a3215dc92eb91c8519aa3ba12eddebb729731400705e1d0d1707ef361f79221a
parent_findings:
  - H-NEW-35 (corpus ACF(1) z=+13.13)
  - H-NEW-181 (per-surah Ljung-Box rhythm)
  - H-NEW-43 (verse-length FFT)
  - H-NEW-770 (verse-length compression-tail kink-50)
  - H-NEW-1790 (refrain inventory)
---

# H-NEW-2050 — Within-surah verse-length symmetry + central-pivot detection

## Verdict

**DIRECTIONAL.** Of the two primary legs:

- **H1 (length-palindrome OR central-pivot) — NULL.** Across all 114 surahs (103 eligible for palindrome,
  109 for pivot), **not a single surah** reaches the Bonferroni-corrected threshold α = 1.529×10⁻⁴ on either
  the mirror-correlation statistic S_pal or the central-pivot statistic S_piv, in the pre-committed direction.
  The Quran's verse-length profiles are NOT mirror-symmetric, and the longest/shortest verse is NOT
  centre-located beyond chance.
- **H2 (within-surah monotone length-gradient) — PASS.** Exactly **6 surahs** clear the corrected threshold
  (the pre-committed bar was ≥3): Q 2 al-Baqara, Q 15 al-Ḥijr, Q 20 Ṭāhā, Q 51 al-Dhāriyāt, Q 52 al-Ṭūr,
  Q 77 al-Mursalāt. All 6 replicate at a second seed AND on letters-per-verse (MW-5). Five of the six are a
  systematic *lengthening* gradient; Q 15 al-Ḥijr is a *shortening* gradient.

Because exactly one of the two legs fires, the locked decision rule returns **DIRECTIONAL**. The honest
reading: the corpus carries a real within-surah verse-length *gradient* architecture, but no positional
*symmetry* (palindrome) or *central-pivot* architecture at the length-series level.

## Statistics (locked before computation)

For verse-length vector L = (L₁,…,Lₙ), Lᵢ = whitespace-token count of verse i (no-tashkeel):

| Stat | Definition | Eligibility | Direction-locked |
|---|---|---|---|
| `S_pal` | Pearson r between L and reverse(L) | n ≥ 7 (k=103) | obs > shuffle-null |
| `S_piv` | 1 − min(centre-dist of longest, of shortest), normalised | n ≥ 5 (k=109) | obs > shuffle-null |
| `S_grad` | \|Spearman ρ(index, length)\| | n ≥ 5 (k=109) | obs > shuffle-null |

Null = **verse-order shuffle** (same length multiset, scrambled order), 10,000 perms per surah, seed 20260509,
one global RNG, surahs in canonical id order. One-tailed p = (1 + #{null ≥ obs}) / (n_perm + 1). Bonferroni
denominator = 3 · k_max = 3 · 109 = 327; α = 0.05/327 = **1.529×10⁻⁴**.

## H2 — the monotone-gradient hits

| Q | Name | n | S_grad | p (raw) | direction | seed2 p | letters p |
|---:|---|---:|---:|---:|:--|---:|---:|
| 2 | al-Baqara | 286 | 0.355 | 1.0×10⁻⁴ | lengthening | 1.0×10⁻⁴ | 1.0×10⁻⁴ |
| 15 | al-Ḥijr | 99 | 0.417 | 1.0×10⁻⁴ | **shortening** | 1.0×10⁻⁴ | 6.0×10⁻⁴ |
| 20 | Ṭāhā | 135 | 0.465 | 1.0×10⁻⁴ | lengthening | 1.0×10⁻⁴ | 1.0×10⁻⁴ |
| 51 | al-Dhāriyāt | 60 | 0.615 | 1.0×10⁻⁴ | lengthening | 1.0×10⁻⁴ | 1.0×10⁻⁴ |
| 52 | al-Ṭūr | 49 | 0.653 | 1.0×10⁻⁴ | lengthening | 1.0×10⁻⁴ | 1.0×10⁻⁴ |
| 77 | al-Mursalāt | 50 | 0.558 | 1.0×10⁻⁴ | lengthening | 1.0×10⁻⁴ | 1.0×10⁻⁴ |

p = 1.0×10⁻⁴ is the floor (0 of 10,000 shuffles matched/beat the observed |ρ|). The gradient is robust: every
hit survives a different seed and the orthogonal letters-per-verse instrument.

**Structural reading.** The dominant shape is *lengthening* — verses get longer as the surah proceeds. This is
the within-surah analogue of, but logically independent from, the cross-surah compression-tail (H-NEW-770).
Q 51 al-Dhāriyāt and Q 52 al-Ṭūr — both short oath-opening Meccan surahs — carry the strongest gradients
(S_grad 0.62, 0.65): they open with terse oath-clusters (*wa-l-dhāriyāti dharwan…*) and broaden into longer
declarative/narrative verses, exactly the rising cadence. Notably Q 51 and Q 52 were also the top-2 most
rhythmic surahs under H-NEW-181's position-blind Ljung-Box test — the gradient is part of why. Q 15 al-Ḥijr is
the lone *shortening* gradient: it opens with longer expository verses and tapers, the inverse profile.

These 6 surahs overlap heavily with H-NEW-181's top-rhythm set (Q 51, 52, 20, 2 all appear in both), confirming
that the position-blind autocorrelation signal and the position-dependent gradient signal are partly the same
underlying length-organisation seen through two instruments.

## H1 — why palindrome and pivot are NULL

**Palindrome (S_pal).** The single most mirror-symmetric surah is Q 89 al-Fajr (S_pal = 0.644) but at raw
p = 0.0044 it is two orders of magnitude away from the corrected threshold; Q 34 Saba (p = 0.0108) and Q 96
al-ʿAlaq (p = 0.0789) follow. No surah's verse-length profile reads the same forwards and backwards beyond
chance. The named refrain surah Q 55 has S_pal = −0.098 (anti-symmetric) — flatly NULL.

**Central-pivot (S_piv).** Four surahs achieve the geometric maximum S_piv = 1.0 — an extremal verse sitting
exactly at centre: Q 35 Fāṭir (longest verse dead-centre), Q 92 al-Layl, Q 107 al-Māʿūn, Q 113 al-Falaq. But a
single extremum landing centrally is a 1-degree-of-freedom event; the shuffle-null shows this happens readily
by chance (Q 35 p = 0.11, Q 92 p = 0.39). None approaches the corrected threshold. The eschatological refrain
surahs (Q 56, 53, 74, 77) cluster near S_piv ≈ 0.98 but all NULL.

This NULL is substantive. It distinguishes the project's empirically-supported length-laws (local memory,
H-NEW-35; cross-surah compression-tail, H-NEW-770; within-surah gradient, this finding) from a **ring-/
concentric-composition** reading at the length-series level. Cuypers 2015 (*The Composition of the Qurʾan*) and
Farrin 2010 argue for chiastic/concentric architecture with a central pivot; whatever footprint that structure
leaves, it is **NOT in the verse-length series**. Concentric composition, where it exists, is carried by lexical
/ thematic mirroring, not by verses growing or shrinking symmetrically about a midpoint. The length series sees
gradient, not chiasmus.

## Named targets (pre-committed, reported regardless)

| Q | Name | n | S_pal (p) | S_piv (p) | S_grad (p) | note |
|---:|---|---:|:--|:--|:--|:--|
| 55 | al-Raḥmān | 78 | −0.098 (0.74) | 0.831 (0.45) | 0.135 (0.24) | flat NULL on all three |
| 78 | al-Nabaʾ | 40 | −0.169 (0.77) | 0.923 (0.74) | 0.414 (0.0076) | gradient direction-locked, misses Bonferroni |
| 81 | al-Takwīr | 29 | −0.266 (0.90) | 0.929 (0.29) | 0.531 (0.0031) | gradient direction-locked, misses Bonferroni |

- **Q 55 al-Raḥmān — NULL on all three.** The pre-registered prediction (refrain → length-rhythm) is FALSIFIED
  for symmetry/pivot/gradient. The 31× *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain is near-constant
  length and *levels* the profile rather than shaping a gradient: S_grad = 0.135 (the corpus's weakest tail),
  S_pal slightly negative. The refrain produces local periodicity (which an ACF/FFT instrument sees, H-NEW-43)
  but no global positional architecture. This is the cleanest demonstration in the run that refrain ≠ symmetry.
- **Q 78 al-Nabaʾ and Q 81 al-Takwīr — directional but sub-threshold.** Both show a real lengthening gradient
  in the locked direction (p = 0.0076, 0.0031) that replicates at seed2 and on letters, but neither clears the
  conservative family-wise α = 1.5×10⁻⁴. Reported as descriptive-directional under MW-7. The eschatological
  cadence is a *rising* cadence — short staccato *idhā…* openers broadening to longer declaratives — consistent
  with H2's lengthening shape, just not strong enough at corpus-corrected significance.

## Methodology walls

- **MW-1 instrument-prior:** S_pal, S_piv, S_grad all locked in the pre-reg §2 before any computation.
- **MW-2 corpus-prior:** 10,000-perm verse-order-shuffle null, seed 20260509.
- **MW-3 alternative-models:** words-per-verse (primary) + letters-per-verse (sensitivity); pivot tested on
  both longest- and shortest-extremum. All 6 H2 hits hold on letters-per-verse.
- **MW-4 over-fitting:** parameter-free statistics; eligibility thresholds n≥7/n≥5 pre-locked.
- **MW-5 replication:** all 6 H2 hits + 3 named targets re-run at seed 20260510 and on letters — H2 hits stable
  at the p-floor; Q 55 stays NULL; Q 78/81 stay directional-sub-threshold.
- **MW-6 instrument-control:** 20 synthetic surahs with verse-lengths drawn i.i.d. from the corpus length
  distribution — min-p across all three statistics: pal 0.023, piv 0.060, grad 0.102; **none fires at
  Bonferroni**. The instrument does not manufacture significance from a length-distribution alone; the H2
  signal is a property of the *actual ordering* of Quranic verses.
- **MW-7 post-hoc cap:** Q 78/81 gradient (named but sub-threshold) and the pivot-1.0 surahs (Q 35, 92, 107,
  113) are reported descriptively only.

## Honest limits

- The central-pivot statistic with a single extremum is intrinsically weak (1 d.o.f.); a stronger concentric
  test would correlate full flanking-pair lengths. We pre-committed to the simple pivot and it returns NULL;
  a future test could use a windowed mirror-residual to probe partial chiasmus. That is a different
  pre-registration.
- Palindrome eligibility (n≥7) excludes much of juzʾ ʿamma; the very short surahs are not in the palindrome
  leg. This was disclosed in the pre-reg.
- DIRECTIONAL, not CONFIRMED: only one of two legs fired. Per the quality gates, this is reported as
  DIRECTIONAL with full NULL prominence for the palindrome/pivot leg.

## Cross-references

- H-NEW-35 — corpus verse-length ACF(1) z=+13.13 (position-blind long-memory; complementary to the gradient)
- H-NEW-181 — per-surah Ljung-Box rhythm; top-10 share Q 51, 52, 20, 2 with this finding's H2 hits
- H-NEW-43 — verse-length FFT periodicity (what Q 55's refrain DOES show, vs the symmetry it does NOT)
- H-NEW-770 — cross-surah verse-length compression-tail kink-50; the *within*-surah lengthening gradient here
  is its logically-independent intra-surah companion
- H-NEW-1790 — refrain inventory (Q 26, 55, 77): Q 55's refrain levels its gradient to NULL; Q 77 al-Mursalāt's
  refrain coexists with a significant lengthening gradient
- Cuypers 2015 + Farrin 2010 (`data/literature/farrin-cuypers/`) — concentric/ring-composition central-pivot
  thesis, **not supported at the verse-length-series level** by this test
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 59 (al-fawāṣil)

## Reproducibility

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2050-verse-length-symmetry.md` (SHA-256 above; embedded in
  script, verified fail-fast at runtime)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2050.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2050.json`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
