---
audit_id: audit-001
finding_id: H-NEW-1
finding_title: Rhyme-break verses carry residual Markov-surprise
audited_by: skeptical-auditor
date: 2026-04-12
parent: null
status: NEEDS REVISION
---

# Audit memo — H-NEW-1 (Rhyme-break Markov-surprise residual)

## Verdict: NEEDS REVISION

The residual-corrected effect (z = 4.73, p < 10⁻⁴, robust to orthography) is real and survives the key confound that the raw z = 40 statistic was inflated by trivial letter-frequency asymmetry. Computational-tester's honesty in disclosing the post-hoc residual correction is commendable and the right call. However, **three remaining issues prevent a PASSED verdict**; they are individually fixable without re-running the full pipeline.

## Critique items

### 1. The rhyme set R = {ن,ا,م,ر,د} is data-dependent (unresolved)
The tester acknowledges the set was chosen because it "covers 90.2%" — this is a direct look at the data. Commitment happened before H-NEW-1 specifically, but the set itself is a researcher-DoF leaked from prior exploration. **Required**: rerun the entire residual test with (a) the classical rawī list from al-Khalīl / Ibn Rashīq *al-ʿUmda* and (b) a held-out set derived from odd-indexed surahs applied to even-indexed surahs. If the z-stat holds within ±25% across all three rhyme-set definitions, the finding is robust; if it collapses, it is set-specific and the effect is likely an artifact of the specific alphabet chosen.

### 2. Markov order only tested at 1
The pre-audit agreement was orders 1, 2, and 3. Arabic triliteral-root structure makes order = 2 the natural model; the signal may vanish at higher order (indicating the gap is merely local co-occurrence) or strengthen (indicating true long-range surprise). **Required**: report residual gap at orders 1, 2, and 3. A gap that disappears at order 2 is a letter-bigram artifact, not a phonetic-design signal.

### 3. No baseline comparison to rhymed Arabic poetry
The finding claims rhyme-break verses are "less within-class-predictable than rhyme-conforming verse-ends." Classical Arabic qaṣīda follows strict monorhyme; the identical statistic on Muʿallaqāt / Imruʾ al-Qays Dīwān should be computed. If Arabic rhymed poetry also exhibits this residual surprise gap, the finding reduces to "rhyme constraint in Arabic does this" — a linguistic-universal result, not a Quran-specific one. This baseline was explicitly agreed in pre-audit and is absent.

## Alternative-explanation audit

Several non-miraculous explanations fit the PARTIAL finding:

- **Content-driven break hypothesis** (already raised by computational-tester): rare terminal consonants get chosen when meaning/syntax demands it — nothing phonetically engineered. Unimodality supports this reading over the original "speed-bump" hypothesis.
- **Saj' prose convention**: pre-Islamic Arabian rhymed-prose conventions permit occasional rhyme-breaks for rhetorical weight. This is genre, not miracle.
- **Morphological attractor**: Arabic plural/verbal endings end in ـون / ـين / ـا with enormous frequency — break-class consists mostly of verbs in other moods or construct-state nouns, which are statistically rarer *word types*, not rarer *verse-end* choices. The residual gap may dissolve once word-class is controlled.

## Robustness requests

1. Rhyme-set sensitivity analysis (3 definitions: classical rawī list, held-out derivation, current {ن,ا,م,ر,د}).
2. Markov orders 1, 2, 3.
3. Baseline statistic on matched-length samples from Muʿallaqāt + Imruʾ al-Qays Dīwān + classical saj' prose.
4. Subset by Meccan/Madinan phase (rhyme conventions differ; residual gap might be a phase artifact).
5. Rerun after excluding verse-ends with alif-of-prolongation vs terminal ن — these are phonetically different and pooling them may inflate or deflate the gap.

## Family-size note

Counting the tests actually run and the sensitivity tests required: k ≥ 12 (2 orthographies × 3 Markov orders × 2 baseline-contrast tests). Bonferroni threshold at α = 0.05 → 0.00417; Holm step-down preferred. The current residual p < 10⁻⁴ survives Bonferroni at 12 tests, but only if the sensitivity battery is run and the effect does not collapse in the weakest cell.

## What would change the verdict

PASSED if: rhyme-set sensitivity shows z ≥ 3.0 in at least 2 of 3 definitions AND order-2 Markov shows residual gap ≥ 0.08 nats with z ≥ 3.0 AND matched-poetry baseline gap is less than half the Quranic gap (z-difference ≥ 2.5).

REFUTED if: rhyme-set sensitivity collapses the effect OR matched-Arabic-poetry baseline shows the same or larger gap.

## Separate note — Null B result (rhyme concentration)
The 22.7% vs 66.1% break-fraction gap is a striking, cleanly-interpretable finding on its own: verse-ends are dramatically more rhyme-concentrated than the surah's own non-terminal letter marginal. This is not news at the headline level (that the Quran has pervasive rhyme is textbook), but the magnitude of the concentration vs the surah's own phonology is a tight quantitative anchor. I recommend computational-tester separate this into its own finding (H-NEW-1B) rather than treating it as an aside. The null model is explicit, the effect is huge, and there is no forking-paths concern. That is a PASSED-grade result on its own merits.
