---
finding_id: H-NEW-2050
type: pre-registration
date_locked: 2026-05-29
phase: B
status: PRE-REGISTERED
seed: 20260509
rules_tuple: (no-tashkeel, word=whitespace-token, words-per-verse, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)
data_source: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
parent_findings:
  - H-NEW-35 (corpus verse-length ACF(1) z=+13.13 — long-memory in length-sequence)
  - H-NEW-181 (per-surah verse-length Ljung-Box rhythm; top-10 muq-or-Meccan)
  - H-NEW-43 (verse-length FFT periodicity)
  - H-NEW-770 (verse-length compression-tail kink-50 law, R²=0.81)
  - H-NEW-1790 (refrain-architecture inventory — Q 55, Q 26, Q 77 refrain surahs)
---

# Pre-Registration — H-NEW-2050 Within-Surah Verse-Length Symmetry + Central-Pivot Detection

## 1. Background and motivation

Prior verse-length work on this project established that the corpus length-sequence carries strong
short-range memory (H-NEW-35: ACF(1) z=+13.13 against a phase-shuffle null), that the long-memory is
multifractal with a within/between-surah crossover near n≈50–100 (H-NEW-166), that per-surah Ljung-Box
rhythm is concentrated in muqaṭṭaʿāt-prefixed and Meccan chapters (H-NEW-181), and that the *mean* verse
length drops across the canonical order with a kink near surah 50 (H-NEW-770, R²=0.81).

**None of these tests addressed positional symmetry of the length profile.** Autocorrelation and Fourier
power are translation-invariant: they detect periodicity and local memory, but they are blind to whether a
surah's longest (or shortest) verse sits at its *geometric centre*, or whether the length sequence reads the
same forwards and backwards (a length-palindrome), or whether it gradients monotonically. These are
distinct architectural claims and have never been tested on this corpus.

The motivation is classical. Concentric / ring-composition (chiasmus, *taʿqīd* by mirroring) is the central
structural thesis of Cuypers 2015 (*The Composition of the Qurʾan: Rhetorical Analysis*,
`data/literature/farrin-cuypers/`) and of Farrin 2010 on al-Baqara. Ring composition predicts a *central
pivot* — a structurally privileged middle unit — and *symmetric flanking*. If such concentric architecture
leaves a measurable footprint in the verse-length series, then (a) some surahs should show a longest- or
shortest-verse at their centre beyond chance, and (b) some surahs should show length(i) ≈ length(n+1−i)
across the whole profile. al-Biqāʿī's *Naẓm al-Durar* (verse-by-verse munāsaba) and al-Suyūṭī's *Itqān*
nawʿ 59 (fawāṣil) make the weaker companion prediction that fāṣila/clausula structure produces ordered
length patterns. H-NEW-2050 tests all three positional shapes — palindrome, central-pivot, monotone-gradient
— against a verse-order-shuffle null.

This is a genuinely new instrument. It is NOT a re-derivation of H-NEW-181 (Ljung-Box autocorrelation,
position-blind) nor H-NEW-43 (FFT, position-blind). Symmetry, pivot-centrality, and gradient are all
position-dependent statistics that the prior instruments cannot see.

## 2. Statistics (LOCKED — instrument-prior MW-1)

For a surah with verse-length vector L = (L₁, …, Lₙ), Lᵢ = whitespace-token count of verse i
(no-tashkeel), n = surah verse count (Hafs-Kūfan; for Q 1 the basmala v.1 counts; for Q 2–114 the opening
basmala is part of v.1 only in the numbering and is not an extra verse), three position-statistics:

**(a) Length-palindrome statistic — `S_pal`.**
Mirror-symmetry of the profile about its midpoint. Standard normalised mirror correlation:

  S_pal = Pearson r between L and its reverse L_rev, where L_rev = (Lₙ, …, L₁).

Equivalently the negative mean-squared mirror residual could be used; we lock the Pearson-r form because it
is scale- and offset-invariant (a surah whose verses all lengthen toward the end is NOT a palindrome, and r
correctly penalises that). Direction-locked: **observed S_pal > shuffle-null S_pal** (more mirror-symmetric
than a random ordering of the same multiset of verse-lengths). Defined only for n ≥ 7 (need ≥3 mirror pairs
plus a centre).

**(b) Central-pivot statistic — `S_piv`.**
Is the extremal (longest OR shortest) verse near the geometric centre? Let p* = argmax_i Lᵢ
(longest-pivot) and q* = argmin_i Lᵢ (shortest-pivot), centre c = (n+1)/2. Normalised centre-distance:

  d_long = |p* − c| / ((n−1)/2)   ∈ [0,1],  0 = dead-centre, 1 = at an edge
  d_short = |q* − c| / ((n−1)/2)
  S_piv = 1 − min(d_long, d_short)     (1 = an extremum sits exactly at centre)

We report both d_long and d_short separately; the primary pivot statistic takes the *closer-to-centre* of the
two extrema (a surah is "pivoted" if EITHER its longest or its shortest verse is central). Ties in argmax/argmin
broken by the candidate closest to the centre (conservative — biases toward finding centrality, so the
shuffle-null calibration absorbs the same tie-rule and the comparison stays honest). Direction-locked:
**observed S_piv > shuffle-null S_piv**. Defined for n ≥ 5.

**(c) Monotone-gradient statistic — `S_grad`.**
Do verses systematically lengthen or shorten across the surah? Spearman rank correlation between verse
*index* (1…n) and verse *length*:

  S_grad = |ρ_Spearman(index, length)|   ∈ [0,1]

Absolute value because either a lengthening or a shortening gradient counts as an architecture; the sign is
reported descriptively. Direction-locked: **observed |S_grad| > shuffle-null |S_grad|** (the actual ordering
is more gradient-aligned than a random ordering). Defined for n ≥ 5. NB: H-NEW-770's kink-50 law is a
*cross-surah* gradient; S_grad is a *within-surah* gradient and is logically independent of it.

All three statistics are computed on words-per-verse. A sensitivity replication on letters-per-verse
(graphemes-per-verse, no-tashkeel) is REPORTED for the headline surahs but is NOT part of the primary verdict.

## 3. Hypothesis (PRE-COMMIT)

**Primary hypothesis H1 (corpus-level existence, direction-locked):**
At least **3 surahs** show a statistically significant verse-length **palindrome** (S_pal) OR **central-pivot**
(S_piv) structure at the Bonferroni-corrected per-surah threshold, with effect in the pre-committed direction
(observed > shuffle-null).

**Secondary hypothesis H2 (gradient, direction-locked):**
At least **3 surahs** show a significant within-surah monotone length-gradient (S_grad) at the same corrected
threshold.

**Named-surah sub-claims (descriptive, MW-7 single-test cap unless they clear the corrected threshold):**
- Q 55 al-Raḥmān — refrain-structured (the 31× *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain), predicted to
  show a length-rhythm; tested for all three shapes.
- Q 78 al-Nabaʾ — eschatological cadence.
- Q 81 al-Takwīr — eschatological cadence (the *idhā* … staccato openers).

These three named surahs are pre-committed targets; their verdicts are reported whether or not they reach the
corrected threshold, with explicit labelling.

## 4. Decision rule (PRE-COMMIT)

| Outcome | H1 (≥3 surahs sig. palindrome OR pivot) | H2 (≥3 surahs sig. gradient) | Verdict |
|---|---|---|---|
| Both fire | ✓ | ✓ | **PASS — within-surah length-architecture CONFIRMED** |
| Exactly one fires | mixed | mixed | **DIRECTIONAL** |
| Neither fires | — | — | **NULL** (no within-surah positional length-architecture beyond chance) |

Reversed direction on any leg (observed < null with significant magnitude) = pre-commit violation, published
as NULL with explicit flag.

## 5. Null model (MW-2) and multiple-comparison correction (§1.5)

**Null = verse-order shuffle.** For each surah independently, permute the order of its own verse-length
multiset (the exact same lengths, re-ordered) and recompute S_pal, S_piv, S_grad. This destroys any positional
architecture while preserving the length distribution exactly — the correct null for a *positional* claim.
- n_perm = 10,000 per surah
- seed = 20260509 (one global RNG, surahs processed in canonical id order so the run is fully reproducible)
- one-tailed p per surah per statistic: p = (1 + #{perm_stat ≥ obs_stat}) / (n_perm + 1)

**Eligible surahs:** those with n ≥ 7 for S_pal, n ≥ 5 for S_piv and S_grad. The palindrome statistic is
undefined for the very short surahs; they are excluded from H1's palindrome leg and that exclusion is reported.

**Bonferroni (family-wise):** the test family is {three statistics} × {eligible surahs}. We pre-commit to the
per-statistic family size = number of eligible surahs for that statistic (call it k_stat). α_corrected for a
single surah-statistic cell = 0.05 / (3 · k_max), where k_max is the largest eligible set (the most
conservative single denominator across the three statistics; tightening, which self-verifies per project
policy). Both raw and Bonferroni-corrected p are reported. A surah "fires" for H1/H2 only if its corrected p
< α_corrected in the locked direction.

## 6. Methodology walls

- **MW-1 instrument-prior:** S_pal (mirror Pearson r), S_piv (centre-distance of nearest extremum), S_grad
  (|Spearman ρ| index×length) all locked above before any computation.
- **MW-2 corpus-prior:** 10,000-perm verse-order-shuffle null, seed 20260509.
- **MW-3 alternative-models:** primary statistic = words-per-verse; alternative = letters-per-verse
  (reported for headline surahs). For pivot, both longest- and shortest-extremum variants computed.
- **MW-4 over-fitting:** no fitted free parameters; the statistics are parameter-free. Threshold n≥7 / n≥5
  pre-locked.
- **MW-5 replication:** re-run the named-surah sub-claims at a second seed (20260510) and on letters-per-verse;
  report stability of p.
- **MW-6 instrument-control:** the shuffle-null is itself the matched control (same multiset, scrambled order).
  Additionally a *random-length-multiset* control surah (lengths drawn i.i.d. from the corpus length
  distribution) is run as a negative control — it must NOT fire.
- **MW-7 post-hoc cap:** any surah noticed only after seeing results (not in the named set, not surfaced by the
  pre-committed ranking) carries single-test α = 0.05 and is labelled post-hoc.

## 7. Honest disclosures (pre-committed)

- Short surahs (n < 7) cannot have a meaningful palindrome statistic and are excluded from that leg; this
  removes much of juzʾ ʿamma from the palindrome test and is acknowledged up front.
- Q 55's refrain is expected to inflate any within-surah periodicity statistic by construction; the refrain
  verses are near-constant length, so the question for Q 55 is specifically whether the *non-refrain* verses
  arrange symmetrically. The refrain-driven result is reported but flagged as construction-expected.
- Central-pivot with a single extremum is a weak (1-degree-of-freedom) statistic; the shuffle-null calibrates
  it correctly but a single surah firing on S_piv alone is weaker evidence than one firing on S_pal across the
  whole profile. This is stated in the verdict.
- Equal NULL prominence: if neither H1 nor H2 fires, the published thesis is that the Quran's verse-length
  architecture is one of *local rhythm and global compression-tail* (H-NEW-35/181/770) but NOT one of
  *within-surah positional symmetry* — a substantive negative result distinguishing the project's
  empirically-supported length-laws from the ring-composition reading of Cuypers/Farrin at the length-series
  level.

## 8. Cross-references (anchor priors)

- H-NEW-35 — corpus verse-length ACF(1) z=+13.13 (long-memory; position-blind)
- H-NEW-181 — per-surah Ljung-Box rhythm; top-10 muqaṭṭaʿāt/Meccan (position-blind)
- H-NEW-43 — verse-length FFT periodicity (position-blind)
- H-NEW-770 — verse-length compression-tail kink-50 (cross-surah mean-gradient, R²=0.81)
- H-NEW-1790 — refrain-architecture inventory (Q 26, 55, 77 strict-refrain surahs)
- Cuypers 2015, *The Composition of the Qurʾan: Rhetorical Analysis* (`data/literature/farrin-cuypers/`) — ring/concentric composition, central-pivot thesis
- Farrin 2010, al-Baqara concentric structure (`data/literature/farrin-cuypers/`)
- al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* — verse-by-verse munāsaba
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 59 (al-fawāṣil — verse-clausula structure)

## 9. Reproducibility

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/prereg-h-new-2050-verse-length-symmetry.md`
- Script: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/scripts/h-new-2050.py`
- JSON output: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-2050.json`
- Finding: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-2050-verse-length-symmetry.md`
- Pre-reg SHA-256 embedded in script header; script fails fast on mismatch.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
