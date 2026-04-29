# [[h-new-139-2-shuffle-null|H-NEW-139.2]] — Shuffle-pair null for [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (most rigorous test)

**Finding ID**: [[h-new-139-2-shuffle-null|h-new-139-2]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent**: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (RETRACTED via [[h-new-139-1-freq-weighted|H-NEW-139.1]] freq-weighted null)
**Type**: ratification test of the RETRACTION via the most-rigorous possible within-corpus null
**Seed**: 20260420
**Verdict**: **NULL at α=0.05** (p = 0.084, direction positive but non-significant)

## Headline

**The most rigorous within-corpus null possible (shuffle which top-3-fāṣila pairs with which muq-surah) gives p = 0.084.** The al-Suyūṭī rhyme-prefiguration claim fails even this most-faithful test. Direction is positive (observed 21/29 > null mean 18.47), so there's a small latent signal, but it does NOT reach α=0.05.

This TRIANGULATES the RETRACTION of [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] via three different null models:

| Null model | z | p | verdict |
|---|---:|---:|---|
| Uniform 28-letter alphabet ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] original) | +5.96 | < 10⁻⁴ | PASS-DIRECTED → RETRACTED |
| Frequency-weighted ([[h-new-139-1-freq-weighted|H-NEW-139.1]]) | **−2.43** | 0.995 | NULL, direction reversed |
| Shuffle-pair (this test, [[h-new-139-2-shuffle-null|H-NEW-139.2]]) | +1.70 | 0.084 | NULL, direction positive but NS |

The three nulls give different answers:
- Uniform null UNDER-samples the common fāṣila letters (ن, م, ر, ل) → overstates rarity of match → inflated +5.96 z.
- Weighted null OVER-samples the common letters to include them in random draws (esp. ن at 50%) → understates rarity of match → reversed -2.43 z.
- Shuffle-pair null preserves BOTH distributions exactly; only the pairing is shuffled → correct test → +1.70 z, p = 0.084.

The shuffle-pair result is the most faithful and confirms: **the muq openings do slightly align with their surah's fāṣila top-3, but not beyond α=0.05 chance**. Classical al-Suyūṭī rhyme-prefiguration is NOT empirically validated by this operationalization; RETRACTION confirmed.

## Why this null is the most rigorous

The shuffle null: given 29 fixed muq-opening-sets {OPEN(s)} and 29 fixed top-3-rhyme-sets {TOP3(s)}, randomly permute which TOP3 goes with which OPEN, compute Σ 1{OPEN ∩ TOP3 ≠ ∅}. 

**What this controls for that prior nulls did not**:
- Distribution of muq-opening-set SIZES (counts: 13 surahs with 3-letter openings, 9 with 2-letter, etc.). Preserved exactly.
- Distribution of muq-opening LETTER FREQUENCIES (e.g., ال is in 12 openings; م in 17; ح in 7). Preserved exactly.
- Distribution of TOP3 SETS across the 29 surahs. Preserved exactly.
- The marginal probability P(any given letter in any given TOP3). Preserved exactly.

Only the PAIRING changes. This is the cleanest way to ask "do these 29 muq openings and 29 top-3 sets align MORE than arbitrary re-pairing would suggest?" Answer: yes slightly, but p = 0.084 is not sufficient at α = 0.05.

## Method

- 29 muq-surahs: fixed from [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] original.
- Openings: fixed from MUQ dictionary.
- Top-3: computed same way as parent (most frequent verse-final letter across verses 2..end; exclude v1 muq-opening verse).
- Observed match count: 21.
- Null: 10,000 random permutations of the top-3 list (each shuffle pairs each muq-surah with a randomly-drawn top-3 set from the 29-pool without replacement).
- Seed: 20260417 + 3 offset.

## Results

| Quantity | Value |
|---|---:|
| Observed matches | 21 / 29 |
| Null mean | 18.47 |
| Null SD | 1.49 |
| Null range | [13, 23] |
| z | +1.70 |
| p_one_sided_upper | **0.0838** |
| α threshold | 0.05 |
| **Verdict** | **NULL** (direction positive, non-significant) |

## Triangulation of retraction

[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] parent (PASS-DIRECTED uniform) → [[h-new-139-1-freq-weighted|H-NEW-139.1]] (NULL freq-weighted) → [[h-new-139-2-shuffle-null|H-NEW-139.2]] (NULL shuffle-pair) form a consistent RETRACTION trajectory:

- Parent null was the wrong reference distribution (uniform alphabet was too permissive).
- Freq-weighted overcorrected (ن = 50% of fāṣilas; draws include ن so often that random matches the top-3 ~85% of the time).
- Shuffle-pair is the correct reference: hold the two MARGINAL distributions constant; test only their JOINT alignment.

Shuffle result (p = 0.084, direction positive) suggests a SMALL effect that was INFLATED to z = 5.96 by the uniform null and REVERSED to z = −2.43 by the freq-weighted null. The true effect is ~1-2 SD, not ~6 SD.

**[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] retraction ratified**: at α = 0.05 under the most rigorous null, al-Suyūṭī's rhyme-prefiguration claim does NOT pass. Ceiling drops from PASS-DIRECTED to NULL.

**Secondary observation**: the DIRECTIONAL positive-small effect (z = +1.70) is not 0. A test with larger n (more muq surahs) or different operationalization might find a genuine small signal. The current 29 surahs give underpowered evidence.

## Action for classical-scholarship-validation list

[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] should treat al-Suyūṭī rhyme-prefiguration as **UNVALIDATED** (neither CONFIRMED nor REFUTED — direction positive, magnitude insufficient). A more sensitive instrument (e.g., top-5 rhyme letters, or full rhyme-distribution divergence) could revisit but not within this test's Bonferroni family.

## Honest limits

1. **N = 29 is small**. Shuffle-pair null on 29 items has limited power to detect small effects.
2. **Top-3 is one operationalization**; top-5 or full distribution might give different results. Feature locked per [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] parent to allow apples-to-apples ratification.
3. **Match = {|OPEN ∩ TOP3| ≥ 1} is binary**; a continuous metric (|OPEN ∩ TOP3| / |OPEN|) might reveal graded signal. Reserved as possible H-NEW-139.3 if warranted.
4. **Original uniform null was defensibly designed** at the time — the NULL-MODEL-ARTIFACT finding is a methodological lesson, not a blame assignment.

## Connections

- **[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]** (parent, PASS-DIRECTED under uniform): **RETRACTED** (already); [[h-new-139-2-shuffle-null|H-NEW-139.2]] ratifies via the most rigorous null.
- **[[h-new-139-1-freq-weighted|H-NEW-139.1]]** (freq-weighted NULL): direction reversed; the OTHER extreme of the null-model continuum.
- **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]** classical-validations: al-Suyūṭī rhyme-prefiguration stays OFF the validated list.
- **audit-037**: adversarial catch confirmed AND ratified by this independent null.

## Files

- Script: inline (no standalone .py file; reproducible from ad-hoc Python in journal)
- JSON: not written (single-test, small output; data is the 21-observed + null distribution which is reproducible at seed 20260420)
- Pre-reg: not written (retraction-ratification test; single-test α=0.05, k=1; pre-reg implicit in task description + prior [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]/139.1 context)
- This findings file.
- Parent retraction chain: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] → [[h-new-139-1-freq-weighted|H-NEW-139.1]] → [[h-new-139-2-shuffle-null|H-NEW-139.2]] (this).

## Verdict

**NULL** at α=0.05 (p=0.084). Direction positive (z=+1.70, observed > null mean) but below significance threshold.

**RETRACTION of [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] is RATIFIED** via the most rigorous within-corpus null possible. Three independent null specifications (uniform, freq-weighted, shuffle-pair) converge on the conclusion that the parent effect was a null-model artifact under uniform; corrected nulls give NULL or DIRECTIONAL-NS.

**Classical claim status**: al-Suyūṭī's rhyme-prefiguration remains UNVALIDATED. Neither CONFIRMED nor definitively REFUTED — a small true effect cannot be ruled out, but this operationalization does not detect it at α=0.05.
