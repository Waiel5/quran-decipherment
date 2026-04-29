# [[h-new-139-1-freq-weighted|H-NEW-139.1]] — Frequency-weighted null replication of [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]

**Finding ID**: [[h-new-139-1-freq-weighted|h-new-139-1]]
**Date**: 2026-04-17
**Specialist**: specialist-a (audit-037 adversarial-flag follow-up)
**Parent**: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (PASS-DIRECTED under uniform null at z=+5.96)
**Pre-reg**: `findings/phase-b-hypotheses/h-new-139-1-prereg.md`
**Verdict**: **NULL — direction REVERSED under frequency-weighted null. [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s PASS-DIRECTED verdict is a NULL-MODEL ARTIFACT.**

## Headline

**[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] fails under the correct null.** The observed 21/29 muq-opening ∩ top-3-fāṣila match rate is actually SLIGHTLY BELOW chance (z = −2.43, p_upper = 0.995) when the null is drawn from the actual fāṣila-letter frequency distribution instead of a uniform 28-letter alphabet.

audit-037 predicted z would drop from +5.96 to +3..+4 but still pass. **Actual**: z dropped to **−2.43**, a swing of 8.39. **[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s classical-munāsabāt validation of al-Suyūṭī's rhyme-prefiguration claim is RETRACTED.**

## Why the uniform null was wrong

The fāṣila-letter frequency distribution is massively skewed:

| letter | fāṣila count | share |
|:---:|---:|---:|
| ن | 3118 | **50.0%** |
| ا | 945 | 15.2% |
| م | 664 | 10.6% |
| ر | 450 | 7.2% |
| ى | 241 | 3.9% |
| ل | 66 | 1.1% |
| others (23 letters) | — | 11.0% combined |

Top-3 fāṣila letters are almost always drawn from {ن, م, ر, ل, ا, ى} across all 29 muq surahs. Under the UNIFORM 28-letter-alphabet null, a random 3-letter subset has probability ≈ 6/28 × 5/27 × 4/26 × 6 = 0.016 of including any letter from this 6-letter set. That's why the uniform null gave z = +5.96.

Under the FREQUENCY-WEIGHTED null, random draws are much more likely to include ن, م, ر, ل, ا. Specifically, drawing 2 letters weighted by fāṣila-frequency includes ن with probability ~75%.

## Numbers

| Quantity | Parent [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (uniform null) | [[h-new-139-1-freq-weighted|H-NEW-139.1]] (weighted null) |
|---|---:|---:|
| Observed matches | 21/29 (72.4%) | 21/29 (72.4%) |
| Null mean | 7.30 | **24.76** |
| Null SD | 2.30 | 1.55 |
| Null max | 16 | 29 (ceiling reached) |
| z-score | **+5.96** | **−2.43** |
| p_one-sided upper | < 0.0001 | **0.9946** |
| Pass α=0.05 | ✓ | ✗ |

**Interpretation**: random draws from the fāṣila distribution match the TOP-3 of each muq surah about 85% of the time. The muq openings match only 72%. The muq openings are, if anything, SLIGHTLY LESS aligned with their surahs' rhymes than chance would predict.

## What this means for [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]

### The PASS-DIRECTED verdict is RETRACTED

[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s extreme p-value was entirely a NULL-MODEL ARTIFACT. The uniform null was the wrong reference distribution for this test: the question isn't "do muq letters match the top-3 more than if the fāṣila distribution were uniform", but "do muq letters match the top-3 more than if the LETTERS WERE DRAWN FROM THE ACTUAL FĀṢILA DISTRIBUTION".

[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s classical-munāsabāt anchoring (al-Suyūṭī's rhyme-prefiguration claim) remains a CLASSICAL CLAIM but is NOT empirically supported by this test.

### Does this refute al-Suyūṭī's rhyme-prefiguration claim?

**No, carefully.** This test is binary at the top-3 level and cannot distinguish:
1. Muq letters are INDEPENDENT of rhyme choice (no relationship).
2. Muq letters and rhyme are BOTH driven by the global fāṣila frequency distribution (common-cause, not direct prefiguration).
3. Muq letters ARE rhyme-prefiguring but the effect is smaller than the common-fāṣila baseline.

[[h-new-139-1-freq-weighted|H-NEW-139.1]] PRECISELY rejects one operationalization. A more sensitive test (e.g., "do muq letters prefigure more than SHUFFLING which letters each surah rhymes on") might reveal a genuine signal at a more delicate level.

### Action items

1. **[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] findings file**: update verdict from PASS-DIRECTED to NULL-MODEL-ARTIFACT (done via cross-reference).
2. **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]] classical-validation**: remove [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] from the al-Suyūṭī rhyme-prefiguration validation list (flag to synthesizer).
3. **MASTER-LEDGER**: integrator should downgrade [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s row.
4. **Queue [[h-new-139-2-shuffle-null|H-NEW-139.2]]**: a better-designed rhyme-prefiguration test. Suggested design: shuffle which TOP-3 goes with which surah, compute match count; compare actual to shuffle. This is a WITHIN-CORPUS test that controls for both the muq-letter-set distribution AND the fāṣila distribution simultaneously.

## Honest limits

1. **Choice of weighted-null sampling method**: weighted-reservoir without replacement. Alternative (weighted-independent with rejection) gives slightly different results; pre-committed to reservoir in pre-reg.

2. **Global fāṣila frequency as reference**: alternative references include muq-only corpus frequency (which would be less favorable to the null). Pre-committed to global.

3. **Ceiling reached**: weighted-null maximum is 29 of 29 (probability ~0 in practice but achievable under the ~75%-per-surah hit-rate × 29 surahs). This means the weighted null is a realistic distribution where 100% match is possible; 21/29 is in the lower tail.

4. **This is NOT a test of the CAUSAL claim** that muq letters prefigure rhymes. It tests "do muq openings match top-3 rhymes MORE than random draws from the fāṣila distribution would". A negative answer to that is consistent with the muq letters being chosen independently of rhyme-choice; both being driven by the same underlying phonological register; OR muq letters being genuinely NOT rhyme-prefiguring.

## Connections

- **[[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]** (parent): verdict retracted.
- **audit-037** (source of flag): validation of adversarial-audit discipline. The flag was empirically confirmed.
- **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]** (classical-scholarship validation synthesis): one item removed.
- **cross-finding-008** (muq as book-markers): UNAFFECTED — this is a different axis.
- **[[h-new-113-letter-position|H-NEW-113]]** (muq letters verse-final enriched overall): UNAFFECTED — that test is about muq-letter frequency in final position across the corpus, not about per-surah alignment.
- **cross-finding-006** (13+ muq design axes): RHYME-PREFIGURATION axis (newly added in [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]) is REMOVED; count drops to 13.

## Classical-scholarship-validation ledger update

Session-wide classical-scholarship-validations list (per [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]) must be updated to REMOVE al-Suyūṭī's rhyme-prefiguration from the "empirically validated" list. Validated classical claims remaining:

- al-Bāqillānī's iʿjāz-at-verse-length ([[h-new-48-poetic-meter|H-NEW-48]]): CONFIRMED
- al-Zarkashī's muqaṭṭāʿat-as-book-markers (cross-finding-008): CONFIRMED
- Classical 7-ṭiwāl / mufaṣṣal segmentation ([[h-new-67-sab-tiwal-mathani|H-NEW-67]], [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]): CONFIRMED
- al-Biqāʿī's munāsabāt-bridges ([[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]], partial [[h-new-143-1-root-bridge|H-NEW-143.1]]): EXEMPLAR-LEVEL at Q 56→57 only
- **al-Suyūṭī's rhyme-prefiguration ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]])**: **RETRACTED** (null-model artifact)

## Verdict

**NULL with DIRECTION-REVERSAL** under correct frequency-weighted null. [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s PASS-DIRECTED is retracted to NULL-MODEL-ARTIFACT. audit-037's flag is CONFIRMED as a legitimate adversarial catch. Classical balāgha claim is NOT empirically supported by this operationalization.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-139-1-prereg.md`
- Script: `scripts/h_new_139_1_freq_weighted_null.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-139-1.json`
- This findings file.
- Parent (retracted): `[[h-new-139-muq-opening-vs-rhyme|h-new-139]]-muq-opening-vs-rhyme.md`
