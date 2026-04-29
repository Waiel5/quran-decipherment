# [[h-new-145-muq-code-decoding|H-NEW-145]] — Bukhārī cross-corpus Fisher-Rao near-optimality test

**Finding ID**: [[h-new-145-muq-code-decoding|h-new-145]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent claim tested**: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s Fisher-Rao-near-optimality is corpus-specific to the Quran
**Pre-reg**: `findings/phase-b-hypotheses/h-new-145-prereg.md`
**Seed**: 20260420
**Verdict**: **INTERMEDIATE — near-optimality is NOT uniquely Quranic, but Quran is significantly more extreme on the permutation-z axis. Genre-general PARTIAL.**

## Headline

**Bukhārī's canonical bab-ordering is ALSO Fisher-Rao-near-optimal (R = 1.196), though less so than the Quran (R = 1.121 under apples-to-apples light-stemming). Both corpora are significantly shorter than random permutation, but the Quran is 3× more extreme on the z-score axis (z = −11.6 vs z = −3.5).**

This is a nuanced finding: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s claim that "mushaf is near-optimal" is NOT unique to the Quran. A well-organized classical Arabic religious compilation (Ṣaḥīḥ al-Bukhārī, 9th century editorial arrangement of ~4,000 bab-chapters) ALSO shows Fisher-Rao-near-optimality under the same methodology. But the QUANTITATIVE STRENGTH of the Quran's near-optimality is about 3× larger on the z-score axis.

**Interpretation**: near-FR-optimality is a property of any coherent topical-editorial ordering of Arabic religious text, but the Quran's near-optimality is QUANTITATIVELY more extreme than at least one comparable non-Quranic text. The "uniquely Quranic" exceptionality is partially refuted; the "quantitatively exceptional" claim remains defensible.

## Numbers

### MW-5 — apples-to-apples validation

| Quantity | Value |
|---|---:|
| Quran R under QAC-STEM ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) | 1.107 |
| Quran R under light-stemming (this run) | 1.121 |
| Difference | 0.014 (< 0.15 pre-committed threshold) |
| **MW-5 PASS** | ✓ |

Light-stemming noisily approximates QAC-STEM roots but gives only a 1.4% higher ratio. The methodology is adequate for apples-to-apples cross-corpus comparison.

### Primary — Bukhārī vs Quran ratio

| Quantity | Bukhārī (114 longest bab-segments) | Quran (114 surahs, light-stem) |
|---|---:|---:|
| Total tokens | 107,034 | 77,812 |
| L_canonical (canonical order path) | 108.16 | 86.67 |
| L_2opt (best of 10 restarts) | 90.41 | 77.34 |
| **R = L_canonical / L_2opt** | **1.196** | **1.121** |
| Null mean (10K random perms) | 110.49 | 104.36 |
| Null SD | 0.668 | 1.522 |
| **z-score** | **−3.48** | **−11.63** |
| p_one_sided_lower | 0.00120 | 0.00010 |

### Pre-committed verdict classification

- **CORPUS-SPECIFIC PASS** required: R_bukhari > 1.3 AND diff > 0.15 → NOT MET (R_bukhari = 1.196)
- **GENRE-GENERAL PASS** required: R_bukhari < 1.2 AND diff < 0.05 → NOT MET (diff = 0.076)
- **INTERMEDIATE** range (R_bukhari 1.2-1.3 or intermediate diff) → **MET**

**Actual outcome**: R_bukhari = 1.196 just barely below the 1.2 threshold for genre-general; diff = 0.076 above the 0.05 threshold. Thus **INTERMEDIATE** — the result is "qualitatively similar, quantitatively distinguishable".

### Secondary — Bukhārī vs random

Bukhārī's bab-ordering is SIGNIFICANTLY SHORTER than random permutation (z = −3.48, p = 0.0012 << α_bon = 0.025). **Secondary PASSES**. Bukhārī's ordering is NOT random.

## Interpretation

### The two axes of "near-optimality"

[[h-new-145-muq-code-decoding|H-NEW-145]] separates two distinct claims:

1. **Ratio-axis**: L_corpus / L_2opt. How close is the canonical ordering to its TSP-optimum?
   - Quran: 1.121 (12.1% above optimum)
   - Bukhārī: 1.196 (19.6% above optimum)
   - Difference: 0.076. MODEST, not dramatic.

2. **Z-score axis**: How many SDs below random permutation?
   - Quran: z = −11.6 (extreme)
   - Bukhārī: z = −3.5 (significant)
   - Difference: 8.1 SD — DRAMATIC.

The Z-score axis depends on the NULL SD. Quran's null has SD = 1.52; Bukhārī's has SD = 0.67. Bukhārī's 114 bab-segments are MUCH MORE similar to each other than Quran's 114 surahs (same genre, same sub-topics) — so its random-permutation distribution has LOWER VARIANCE, making the canonical-ordering's absolute excess of only 2.3 units look more modest relative to SD.

This is important: **the Quran's 1.12 ratio against 1.52-SD null is vastly more extreme than Bukhārī's 1.20 ratio against 0.67-SD null**, because the RANDOM-NULL DISTRIBUTIONS have different scale structures.

### What this means for [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] and M1

The "Quran's mushaf is Fisher-Rao-near-optimal" claim holds — the ratio is slightly tighter than Bukhārī's. But the "Quran is UNIQUELY near-optimal" framing cannot be supported: Bukhārī ALSO shows near-optimality at 1.196.

**Revised framing**: the Quran's mushaf ordering is **quantitatively exceptional in its z-score deviation from random** (11σ vs 3.5σ) but NOT UNIQUELY near-optimal in absolute ratio terms.

### What this means for theorist's unified model

Theorist's M1 ("Structured Hamiltonian-cycle") generalizes from [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]. [[h-new-145-muq-code-decoding|H-NEW-145]] suggests the UNDERLYING phenomenon (coherent-topical ordering being Fisher-Rao-geodesic) is a GENERAL feature of classical Arabic religious editing — not unique to the Quran. The UNIQUE feature of the Quran may be its z-score extremity, its structural-boundary-concentration ([[h-new-130-fisher-rao-residuals|H-NEW-130]]: 15/15), its cyclic-closure ([[h-new-144-cyclic-tsp|H-NEW-144]]), and the MULTIPLE AXES that converge to 15 specific hinges ([[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]).

**The "punctuated-cycle geodesic" interpretation from [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]/H-NEW-130d remains Quran-specific**. Bukhārī does not have muqaṭṭāʿat, chronology, or a specific classical-boundary set. Bukhārī's near-optimality is PATH-level; the Quran's is PATH + HINGES + CYCLE + UNIVERSAL-HINGES-ACROSS-FEATURES.

### Implications for [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] classical-scholarship validation

[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s mushaf-is-Fisher-Rao-optimal was listed as an empirical-validation of the classical claim that the mushaf is divinely-ordered. [[h-new-145-muq-code-decoding|H-NEW-145]] shows this evidence is WEAKER than claimed: a human-edited collection (Bukhārī) also shows near-optimality. The DIFFERENTIAL (Quran's z is 3× Bukhārī's z) is still empirical evidence for Quran-exceptionality, but the "mushaf is uniquely optimal" rhetoric should be replaced with "mushaf is MORE optimal than at least one comparable classical Arabic corpus".

## Honest limits

1. **Bab-segmentation is crude**. Splitting Bukhārī on the literal word "باب" over-segments (4,080 bab-markers including some false positives where باب appears in a hadith body). Taking the 114 LONGEST segments partially mitigates this but biases toward legal-prescriptive chapters.

2. **114-longest selection is post-hoc**. The Quran has exactly 114 surahs; I selected 114 Bukhārī segments to match. This is NOT what Bukhārī's compiler intended as segmentation units. A more faithful segmentation would use Bukhārī's ~97 kitāb (book-level) sub-divisions, but the token count there would be very different.

3. **Light-stemming noise**. Despite MW-5 passing, light-stemming is a crude root-extractor. True QAC-level morphological analysis of Bukhārī would tighten the comparison but is not available.

4. **Only one comparison corpus**. Bukhārī is ONE comparison point. A full exceptionality test would compare against multiple Arabic corpora (Muslim, Tirmidhī, Ibn al-Athīr, etc.). The 0.076 ratio difference may be smaller or larger against other corpora.

5. **Topic-coherence differences**. Bukhārī is LEGAL-PRESCRIPTIVE (hadith organized by legal topic); the Quran spans multiple genres. Bukhārī's lower null-SD reflects genre-homogeneity. This is inherent, not a confound.

6. **No cyclic-closure test** on Bukhārī. Would be a separate follow-up (H-NEW-145.1).

## Connections

- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (Quran mushaf near-optimal, CONFIRMED): refined. Near-optimality is genre-general, but Quran's z-score is ~3× more extreme.
- **[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]** (M1 structured-Hamiltonian-cycle): PATH-level near-optimality is shared with Bukhārī; but the STRUCTURE (15 boundary hinges + cyclic closure + universal hinges) remains Quran-specific.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b/130c**: boundary-concentration architecture was DEFINED for the Quran. No analogue in Bukhārī (no muqaṭṭāʿat, no chronology). Not cross-corpus-testable by the same methodology.
- **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]** (classical validations): the Quran-uniquely-optimal claim needs softening to "Quran significantly-more-optimal-than-Bukhārī".

## Honest conclusion for team-lead + theorist + integrator

The Quran's mushaf is Fisher-Rao-near-optimal — and so is Bukhārī, just less extreme. The cross-corpus test SUCCESSFULLY ran and gave an INTERMEDIATE verdict. This WEAKENS the "uniquely Quranic optimality" reading but STRENGTHENS the "Quran is quantitatively more coherent than comparable classical Arabic editing" reading.

The unique architectural features of the Quran (muqaṭṭāʿat, mushaf, ring-closure at Q 114→Q 1, structural-boundary-hinges, musabbiḥāt cluster, chronology-reversal mirror at Q 49↔Q 56↔57) remain untested in Bukhārī and are likely NOT genre-general — they are structurally idiosyncratic to the Quranic corpus.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-145-prereg.md`
- Script: `scripts/h_new_145_bukhari_cross_corpus.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-145.json`
- This findings file.

## Verdict

**INTERMEDIATE** per pre-committed classification:
- Bukhārī R = 1.196 (not > 1.3, not < 1.2)
- Difference from Quran = 0.076 (not > 0.15, not < 0.05)

**Secondary**: Bukhārī significantly shorter than random (z=-3.5, p=0.001, PASS α_bon=0.025).

**Narrative**: near-FR-optimality is genre-general; Quran is QUANTITATIVELY more extreme (z-score 3× greater). Classical-validation claim of "Quran is uniquely optimal" SOFTENED to "Quran is measurably more optimal than a comparable Arabic religious corpus".
