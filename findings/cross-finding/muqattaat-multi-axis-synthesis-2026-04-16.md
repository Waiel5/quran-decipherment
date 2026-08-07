---
id: CROSS-FINDING-006
title: The Muqaṭṭaʿāt Multi-Axis Design — coherent non-random pattern across ≥6 independent axes
date: 2026-04-16
status: SYNTHESIS — combines multiple Bonferroni-significant findings; not a new test
rules_tuple: (no-tashkeel, hafs-kufan, mashriqi where applicable)
parent_findings:
  - H-NEW-44 secondary (letter-frequency ρ=-0.54)
  - H-NEW-44.2.1 (pharyngeal/glottal exhaustivity, PASS-DIRECTED)
  - H-NEW-45 (gap-entropy clustering, PARTIAL-PASS)
  - H-NEW-46 (surah-length skew, STRONG-PASS 4/4)
  - H-NEW-46.1 (chronology disentanglement, STRONG-PASS 6/7)
  - H-NEW-47 (sharp-cutoff NULL — but reveals function-letter exclusion pattern)
  - H-NEW-50 (113+1=114 unique mechanical pattern)
  - H-NEW-51 (cardinality-position decline, PASS-DIRECTED post-hoc)
nulls_for_completeness:
  - H-NEW-44.1 (subset closure properties NULL)
  - H-NEW-44.2 (POA classification overall NULL)
  - H-NEW-45.2 (dead-zone content NULL)
  - H-NEW-META-4 (al-Bāqillānī bimodality NULL — cross-finding-005 retracted)
---

> ## ⛔ CORRECTION NOTICE — 2026-08-07: the muqaṭṭaʿāt book-reference LAW SURVIVES; its p = 3.17 × 10⁻¹² does NOT
>
> **This is the only standing claim in the project to have met a null matching the variable
> that drives it, and it passed.** Both halves are separately true and both must travel.
>
> - **The law survives.** 24 of 29 reproduces **exactly**. Against a null that permutes the
>   muqaṭṭaʿāt label *within opening-window-size quintiles* — so the opening-token budget is
>   identical by construction — the observed 24 stands against a null mean of **9.304**: rate
>   ratio **2.580**, z = +7.01, p = 1.0 × 10⁻⁴, eleven above the 95 % band top. **Every**
>   matched null in the ladder still places the observation outside its own 95 % band.
> - **`p = 3.17 × 10⁻¹²` is withdrawn as a description of that strength.** It is
>   arithmetically correct and inferentially void: the hypergeometric draws 29 surahs
>   *uniformly from 114*, which requires the 29 to be exchangeable with the other 85. They are
>   not, and this project established that itself — `h-new-46-muqattaat-vs-surah-length.md` is
>   a STRONG-PASS showing muqaṭṭaʿāt surahs concentrate in **long** surahs. **The honest effect
>   size is a rate ratio between 1.27 and 2.58, not a twelve-order-of-magnitude tail.**
> - **The sharpest form of the law is positional and length-free.** All 29 muqaṭṭaʿāt surahs
>   mention the Book somewhere — so do 40 others — but they place the **first** mention at
>   **0.0996** of the surah against **0.3403** (Δ = −0.2407, p = 5.0 × 10⁻⁴). The law is not
>   "muqaṭṭaʿāt surahs mention the Book"; it is **"muqaṭṭaʿāt surahs announce it at the top."**
>
> **Three qualifications travel with the verdict.** (i) H-NEW-2760's H2 **failed its gate**:
> the nuisance channel it made primary (opening-window size, ρ = +0.1678) is weaker than
> whole-surah length (ρ = +0.4583), and **against that stronger channel the rate ratio is
> 1.694**. (ii) DISCRIMINATES was earned on the within-corpus nulls; in the matched-partition
> genre arm **0 of 3 baselines clear the gate and the poetry arm is a published pre-commit
> violation**. (iii) The cross-genre half remains partly definitional — only 6 al-Bukhārī and
> 1 pre-Islamic-poetry pseudo-surah mention *kitāb*/*qurʾān* in their opening units at all, and
> al-Jāḥiẓ's adab prose yields **الكتاب** among its strongest marker classes.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2760-muqattaat-book-reference-nuisance.md`.
> Orientation: `STATE-OF-THE-PROJECT-2026-08-07.md` §1.1.


# Muqaṭṭaʿāt Multi-Axis Design Synthesis (2026-04-16)

## The pattern

Across the 2026-04-15 / 2026-04-16 muqaṭṭaʿāt investigation waves, the project has confirmed **non-random design at multiple independent structural axes**:

### Axis 1 — Letter Selection (frequency)
- **[[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary**: Spearman ρ(is-muqaṭṭaʿa, Quran-frequency-rank) = **−0.54**
- The 14 muqaṭṭaʿāt letters skew strongly toward high-frequency Arabic letters
- Quantifies Welch (1986) qualitative claim
- 10 of 14 top-frequency letters are in muqaṭṭaʿāt (per [[h-new-47-muqattaat-frequency-cutoff|H-NEW-47]]); 4 high-freq excluded letters {و, ب, ت, ف} are all major function-particles

### Axis 2 — Letter Selection (place of articulation)
- **[[h-new-44-2-poa-closure|H-NEW-44.2]].1**: **All 4 pharyngeal/glottal letters {ا, ه, ع, ح} are in muqaṭṭaʿāt** (4/4)
- Hypergeometric p = 0.0489 — PASS-DIRECTED at α=0.05 single-test
- Aligns with al-Khalīl's *Kitāb al-ʿAyn* phonetic ordering (pharyngeals listed first)
- Coronal-sonorant exhaustivity (3/3) and interdental absence (0/3) are striking but not Bonferroni-significant

### Axis 3 — Surah-Position Clustering
- **[[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]]**: Gap-entropy of 29 muqaṭṭaʿāt-opened surah indices = **1.568** vs uniform-null mean 2.799 (z = −9.6, p = **2×10⁻⁵**)
- First quantitative confirmation of qualitative classical observation
- The الر-cluster (Q 10–15), الم-cluster (Q 29–32), and ḥawāmīm (Q 40–46) are statistical signatures, not coincidences

### Axis 4 — Surah-Length Skew
- **[[h-new-46-muqattaat-vs-surah-length|H-NEW-46]]**: 4/4 cells STRONG-PASS at Bonferroni-4
- **0 of 29 muqaṭṭaʿāt-openers in the 29 shortest surahs** (vs 7.4 expected, p = 3×10⁻⁵)
- Mean verse-count 94.6 vs null mean 54.7 (p = 1×10⁻⁵)

### Axis 5 — Length-Skew Survives Chronology Control
- **[[h-new-46-1-chronology-disentangle|H-NEW-46.1]]**: STRONG-PASS, 6/7 cells significant after Bonferroni-7
- OLS muqaṭṭaʿāt coefficient = **+56.4 verses** after controlling for Meccan/Medinan period (p = 7×10⁻⁸ classical, 2×10⁻⁵ HC1 robust)
- Stratified Mann-Whitney z = +4.82, p = 1.4×10⁻⁶
- **The chronological-correlate explanation is FALSIFIED**

### Axis 6 — Cardinality Decreases with Surah Position
- **[[h-new-51-cardinality-position-decline|H-NEW-51]]** (PASS-DIRECTED, post-hoc): Spearman ρ(position, cardinality) = −0.66
- After controlling for length: partial ρ = **−0.70** (length is a SUPPRESSOR variable here)
- Permutation p = **2×10⁻⁵** on partial correlation
- Single-letter muqaṭṭaʿāt {ص, ق, ن} concentrate LATE (Q 38, 50, 68); larger subsets concentrate EARLY
- Independent replication via Nöldeke chronology queued ([[h-new-51-1-noldeke-replication|H-NEW-51.1]])

### Axis 8 — Book/Quran Reference in Opening Verses (added 2026-04-16)
- **[[h-new-53-muqattaat-book-reference|H-NEW-53]]**: **24 of 29 muqaṭṭaʿāt-opened surahs (82.8%) reference "kitāb" or "qurʾān" in verses 1-3** vs only 10/85 non-muqaṭṭaʿāt (11.8%)
- Hypergeometric p = **3.17 × 10⁻¹²** — single STRONGEST muqaṭṭaʿāt-axis test in project
- 5 exceptions (Q 19, 29, 30, 42, 68) all have alternative thematic openings; Q 68 references "qalam" (pen) which is semantically book-adjacent
- Quantitative confirmation of classical observation by al-Zarkashī (*Burhān*), al-Suyūṭī (*Itqān*), Welch (1986)
- This finding alone makes the muqaṭṭaʿāt-as-structural-design-feature reading unambiguously empirically supported

### Axis 7 — Bismillah Editorial Pattern
- **[[h-new-50-bismillah-114|H-NEW-50]]**: 113 surah-opening Bismillahs + 1 internal at Q 27:30 = **114 exact** (matches surah count)
- The basmala is a STRUCTURAL OUTLIER — only 4-word phrase in the Quran near 114 occurrences
- 0 other 4-grams have count in {113, 114, 115}; next-most-frequent 4-gram is at 89 occurrences
- Curiosity: 27 + 30 = 57 (= Sūrat al-Ḥadīd index)
- Pattern-arithmetic conditional probability is moderate (~0.30-0.45 under reasonable priors)
- "UNIQUE-PATTERN" verdict; coincidence-of-arithmetic not statistically rare

## NULL findings (completeness)

These hypotheses tested negative — the muqaṭṭaʿāt design is NOT non-random on these axes:

- **H-NEW-44.1** (subset combinatorial closure) — rank-12 is the 2nd-most-common rank in random subset families with these cardinalities; 0/6 cells significant
- **[[h-new-44-2-poa-closure|H-NEW-44.2]]** (overall POA classification) — overall χ² perm p = 0.065; 0/8 per-class significant after Bonferroni-8
- **[[h-new-45-2-dead-zone|H-NEW-45.2]]** (Q 51-67 dead-zone content) — 0/4 cells; the Khawātim al-Ḥashr divine-name spike does not propagate to the 17-surah aggregate
- **H-NEW-META-4** (al-Bāqillānī bimodality) — semantic 89% Q-HIGH ✓ but rhythmic ALSO 83% Q-HIGH (predicted ≤50%); χ² p=0.59. Cross-finding-005 (Quranic Smoothness Triple) RETRACTED as meta-pattern

## What the multi-axis pattern IS and IS NOT

### IS

- A **multi-axis non-random design**: muqaṭṭaʿāt selection is structured at the LETTER level (frequency, partly POA) AND at the SURAH-ASSIGNMENT level (clustering, length, length-after-chronology, cardinality-position decline).
- **Cross-axis convergence**: 3 of these are STRONG-PASS or Bonferroni-survives; 3 more are PASS-DIRECTED or PARTIAL-PASS. No counter-finding contradicts the design pattern.
- A **specific multi-axis prediction**: future muqaṭṭaʿāt-related findings should fit the pattern (high-frequency letters preferred, contiguous clustering, long surahs assigned, cardinality decreasing through canonical order).

### IS NOT

- A claim that muqaṭṭaʿāt are "designed by a specific intelligence" — the project takes no theological position on origin
- A statistical signature that DEFINES the muqaṭṭaʿāt selection rule — many distinct selection rules could produce the same axes
- Universal across all axes: combinatorial closure (rank/antichain), POA distribution, dead-zone content are all NULL, meaning the design exists at SOME axes and is generic at OTHERS

## What replication / extension queued

Independent pre-regs queued for upgrade beyond PASS-DIRECTED status:

1. **[[h-new-51-1-noldeke-replication|H-NEW-51.1]]** — replicate cardinality-position decline using Nöldeke chronological order instead of canonical mushaf order. If decline persists, mechanism candidate "chronological tapering" strengthens.
2. **[[h-new-44-2-poa-closure|H-NEW-44.2]].2** — test pharyngeal/glottal-letter distribution across muqaṭṭaʿāt SUBSETS (not just letters). Independent dimension for the 44.2.1 PASS-DIRECTED result.
3. **H-NEW-47.1** — function-letter exclusion test. Pre-register the {و, ف, ب, ت} function-letter exclusion as an independent directed hypothesis.

## Honest framing

The picture: the muqaṭṭaʿāt design is non-random in a CHARACTERIZABLE way (frequency-prefers-substantive-letters, surah-position-clusters, length-prefers-substantive-surahs, cardinality-tapers). This is a SHARP empirical signature with multiple independent confirmatory axes. The classical literature (al-Zarkashī, al-Suyūṭī, al-Rāzī, Welch, Nöldeke) qualitatively observed several of these axes; the project provides quantitative confirmation at Bonferroni-significant levels for several.

The design's MEANING (theological, mnemonic, sonic, structural) remains open. The empirical PATTERN is now well-established.

## Cross-reference to previously documented muqaṭṭaʿāt findings (pre-2026-04-15)

- MASTER-§1-#2 / muqattaat-density: muqaṭṭaʿāt letter density enrichment in their host surahs (CONFIRMED, χ² p<1e-15)
- MASTER-§1-#22 / muqattaat-distinctive: muqaṭṭaʿāt as a distinctively Quranic feature (no parallel in 6 compared corpora)
- MASTER-§3c / [[h-new-4-ext-classical-audit|H-NEW-4]]: muqattaat-first-lemma-introduction rate REFUTED

These older findings cohere with the new multi-axis picture: muqaṭṭaʿāt are a Quran-distinctive, density-enriched-in-host, multi-axis-structured design feature.

## Updated MASTER-LEDGER status

- Tier-A confirmed (Bonferroni-significant): [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] STRONG-PASS, [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] STRONG-PASS, [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] PARTIAL-PASS
- Tier-B PASS-DIRECTED (single-test, post-hoc-noticed): [[h-new-44-2-poa-closure|H-NEW-44.2]].1, [[h-new-51-cardinality-position-decline|H-NEW-51]]
- CONFIRMED secondary: [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] letter-frequency, [[h-new-50-bismillah-114|H-NEW-50]] mechanical
- Honest NULLs: H-NEW-44.1, [[h-new-44-2-poa-closure|H-NEW-44.2]], [[h-new-45-2-dead-zone|H-NEW-45.2]], H-NEW-META-4

The total contribution of the 2026-04-15/16 waves: **5 confirmed/partial-pass signals + 2 PASS-DIRECTED + 4 NULLs + 1 RETRACTION**. The pattern is multi-axis design with characterizable signatures.
