---
finding_id: h-new-254
run: 1
date: 2026-04-17
agent: h-new-254-specialist
parent: h-new-239
seed: 20260419
verdict: COMPOSITIONAL_CHOICE (Stouffer Z=-2.159, p=0.0154 < α=0.05)
---

# H-NEW-254 run 1 journal

## Brief

Parent H-NEW-239 reported mufaṣṣal block (Q 50-114) as lowest-density
of 4 pre-registered blocks (mean density 0.020 vs ṭiwāl 0.034,
ḥawāmīm 0.030, other 0.032) and contributed the dominant signal to
the ρ=−0.476 mushaf-position gradient. Q-NEW-254 was commissioned to
test whether this depletion is (a) a genuine compositional choice or
(b) a length-normalization artifact due to short mufaṣṣal surahs
inflating the denominator.

## Method

Pre-registered per-surah length-matched Bernoulli null:
- Corpus p = N_name_tokens / N_words = 2358 / 82375 = 0.028625.
- For each mufaṣṣal surah s, draw B=10000 bootstrap samples of N_s
  word-indicators each Bernoulli(p_corpus). Record null density dist.
- One-tailed per-surah p_less = P(null ≤ observed), converted to
  z_i = Φ⁻¹(p_i). Stouffer combine Z = Σz_i/√65.
- α_bon = 0.05 (k=1; single pre-committed test).
- MW-5 instrument checks: verse-shuffle (H-NEW-239 style, diagnostic)
  and word-shuffle (proper per-word null; Z should ≈ 0).

## Forking paths disclosed pre-run

- Mufaṣṣal = Q 50-114 (Zarkashī; locked from H-NEW-239).
- Null = per-word independent Bernoulli(p_corpus). Alternative
  conditional/context-preserving samplers NOT run as primary.
- Per-surah bootstrap: 10000 samples each.
- Primary direction: one-tailed less-than (pre-committed H1 =
  compositional choice, observed < null).
- Stouffer weighting: uniform across 65 surahs. Word-weighted
  Stouffer logged as deferred variant.

## Execution

- `scripts/h_new_254_mufassal_depletion.py` executed at 2026-04-17.
- Runtime < 2s on laptop.
- Output: `findings/phase-b-hypotheses/csv/h-new-254.json` +
  `h-new-254-per-surah.tsv`.

## Key numbers

- Stouffer's Z_combined = **−2.1591**
- One-tailed p_less = **0.01542**
- Two-tailed p_two = 0.03084
- Mean observed mufaṣṣal density = 0.02015
- Mean null mufaṣṣal density = 0.02867 (30% shortfall)
- Per-surah z: mean −0.457, median −0.898, min −3.37 (Q 56),
  max +5.53 (Q 59)
- frac(z<0) = 0.723; frac(z<−1) = 0.462; frac(z<−2) = 0.200 —
  large left-tail excess vs Normal null.
- MW-5a verse-shuffle Z = +15.52 (diagnostic: verse-shuffle
  mechanically inflates mufaṣṣal per-word density because mufaṣṣal
  has short verses).
- MW-5b word-shuffle Z = +1.29 (proper null ≈ 0; instrument is sound).

## Verdict

**COMPOSITIONAL CHOICE** — observed < null significantly at α=0.05.
Mufaṣṣal depletion is not explained by per-surah length-normalization
artifact. The block genuinely avoids divine-name tokens on a per-word
basis compared to what corpus-average marginals would produce at
mufaṣṣal's lengths.

## Noteworthy sub-findings

- **Bimodal z-distribution within mufaṣṣal**:
  - 23/65 surahs (35%) have literally ZERO divine-name tokens
    (eschatological/oath saj' spine).
  - 8/10 top-enriched are Medinan short-mid cluster Q 57-66 (legal-
    cadence verse-terminal name-pair saturation).
- **Q 1 al-Fātiḥa and Q 112 al-Ikhlāṣ classical-anchor surahs**:
  Q 112 confirmed as enriched (z=+3.99) even at N=15. Q 1 is not in
  mufaṣṣal (class=other in H-NEW-239) — NOT part of this family.
- **Most-depleted spine**: Q 54 al-Qamar, Q 55 al-Raḥmān, Q 56
  al-Wāqiʿah, Q 68 al-Qalam, Q 50 Qāf — classical mufaṣṣal openers;
  all are per-word name-sparse despite thematic-theological density.
- **Q 55 al-Raḥmān special case**: the surah NAMED *al-Raḥmān*
  invokes that attribute once at v1, then uses pronouns for 77
  verses. Its observed density 0.0028 corresponds to 1 token across
  355 words, z = −2.93.

## Honest limits

1. Per-word Bernoulli null is context-insensitive.
2. p_corpus is a single scalar; richer Meccan/Medinan conditioning
   would test a DIFFERENT hypothesis.
3. Uniform Stouffer weighting favors depletion signal (many small
   zero-density surahs) over enrichment (fewer, longer Medinan
   cluster). Word-weighted variant would probably be less significant
   because the long Medinan enrichments carry more tokens.
4. Small-N surahs have coarse discrete null distributions; absorbed
   by Stouffer across 65 surahs.

## Integration notes

- Reinforces H-NEW-239 depletion signal as SUBSTANTIVE not artifactual.
- Refines cross-finding-018 M1 4-region "mufaṣṣal peripheral + sparse"
  reading to "mufaṣṣal bimodal with Medinan Q 57-66 enriched cluster,
  Meccan Q 50-56/68-77 depleted spine."
- The length-matched null complements H-NEW-239's corpus-wide
  verse-shuffle MW-5, providing the per-surah matched complement.
- Classical synthesis: quantitatively confirms al-Suyūṭī's *Itqān* nawʿ 8
  reading of mufaṣṣal rhetorical mode and al-Zarkashī's *Burhān*
  prosodic-structure claim.

## Deliverables status

- [x] Pre-reg: `h-new-254-mufassal-depletion-mechanism-prereg.md`
- [x] Script: `scripts/h_new_254_mufassal_depletion.py`
- [x] JSON + TSV: `csv/h-new-254.json`, `csv/h-new-254-per-surah.tsv`
- [x] Findings doc: `h-new-254-mufassal-depletion-mechanism.md`
- [x] Journal: this file
- [x] MASTER-LEDGER Wave-5 entry
