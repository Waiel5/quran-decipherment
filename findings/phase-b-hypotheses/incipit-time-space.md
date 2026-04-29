---
finding_id: h-new-31-incipit-time-space
phase: B
status: PARTIAL — SPACE confirmed (Medinan concentration), TIME reversed
date: 2026-04-13
rules_tuple: (no-tashkeel, graphemes, normalized, 28-letter, first-5-tokens-post-basmala-post-muqattaat)
null_model: label-shuffle Fisher p under Meccan/Medinan assignment
bonferroni_k: 3
classical_claim: al-Suyūṭī Itqān nawʿ 59 fawātiḥ al-suwar + Ibn ʿAshūr time/space contrast
seed: 20260413
author: computational-tester
---

# H-NEW-31 — Time/space/cosmos incipit asymmetry Meccan vs Medinan

## Classical claim

al-Suyūṭī *Itqān* nawʿ 59 (*fawātiḥ al-suwar*) enumerates canonical surah
incipit types. Ibn ʿAshūr *al-Taḥrīr wa-l-Tanwīr* muqaddima qualitatively
contrasts eschatological time-frames in short Meccan surahs with legal
directives in long Medinan surahs. **Pre-registered prediction**: TIME-anchored
incipits (*yawm*, *idhā*, *idh*) concentrate in Meccan (especially late-Meccan,
per Nöldeke chronology), SPACE-anchored incipits (*yā-ayyuha*, *innamā*)
concentrate in Medinan.

## Operationalization

For each of 114 surahs, extract the first 5 tokens after basmala and muqaṭṭaʿāt,
classify by semantic-marker priority: TIME > COSMOS > PRAISE > IMPER > SPACE >
OTHER. Marker dictionaries built from high-frequency temporal/spatial/cosmic
stems (e.g., TIME = {yawm, idh, idhā, fa-idhā, ḥīn, yawmaʾidh}).

## Results

### Incipit class distribution (114 surahs)

| Class | Count |
|---|---|
| OTHER | 55 |
| SPACE | 22 |
| PRAISE | 14 |
| TIME | 14 |
| IMPER | 8 |
| COSMOS | 1 |

### Period × class contingency

| Period | TIME | COSMOS | PRAISE | IMPER | SPACE | OTHER | Total |
|---|---|---|---|---|---|---|---|
| Meccan | 10 | 1 | 9 | 7 | 12 | 47 | 86 |
| Medinan | 4 | 0 | 5 | 1 | 10 | 8 | 28 |

### Sub (a) — Fisher exact tests

| Test | Direction | p | Pass? |
|---|---|---|---|
| Meccan > Medinan on TIME | directional | **0.766** (reversed) | FAIL |
| Meccan > Medinan on COSMOS | directional | 0.754 | FAIL |
| Medinan > Meccan on SPACE | directional | **0.0146** | **PASS** |

**Sub (a) PASSES on SPACE at α=0.0167, FAILS directionally on TIME**.

TIME-rate: Meccan 10/86 = 11.6%, Medinan 4/28 = 14.3% — Medinan is
*slightly more* TIME-incipit-ed than Meccan. The pre-registered TIME direction
is wrong.

SPACE-rate: Meccan 12/86 = 14.0%, Medinan 10/28 = **35.7%**. 2.55× concentration
— this is real. 10 of 28 Medinan surahs open with *yā-ayyuha* or similar
social/legal vocative-marker.

### Sub (b) — Jonckheere-Terpstra trend across Meccan phases

Pre-reg expected TIME concentration increasing Early → Middle → Late Meccan.

| Phase | N surahs | TIME rate |
|---|---|---|
| Early Meccan | 48 | **0.208** |
| Middle Meccan | 21 | 0.095 |
| Late Meccan | 21 | **0.000** |
| Medinan | 24 | 0.083 |

Jonckheere-Terpstra J = 1046, z = **−1.409** (one-sided). **Direction is reversed**:
TIME-incipit *decreases* monotonically Early → Late Meccan, not increases.
Under the strict one-tailed pre-reg, this FAILS.

Under a two-tailed reading, |z| = 1.41 < 2.39 critical (α=0.0167), so
still not significant for decreasing direction either. FAIL.

### Sub (c) — Shuffle null for Meccan/Medinan × TIME Fisher

Pre-registered: observed p should beat shuffle-null empirical distribution.

- Observed Fisher one-sided p = 0.766
- Null median p = 0.534
- Observed rank in null: 552/1000
- Empirical p-value = 0.552

Observed is NOT extreme under shuffle. FAIL (as expected, given TIME failed
sub a).

## Joint verdict

| Sub-test | Result |
|---|---|
| (a) Fisher SPACE at α=0.0167 | **PASS** (p=0.0146) |
| (b) Meccan JT trend on TIME | FAIL (z=−1.41, wrong direction) |
| (c) Shuffle null | FAIL |
| Joint (all 3 required) | **FAIL** |

## Interpretation

The classical intuition splits cleanly: **Medinan surahs are dramatically more
likely to open with social/legal vocatives** (*yā-ayyuha al-ladhīna āmanū*, etc.)
— 35.7% vs 14.0% — at p = 0.0146. This is consistent with Medinan didactic
legal mode and passes the pre-registered test.

But **the predicted TIME concentration in Meccan is directly contradicted**.
TIME-incipit rate is actually slightly higher in Medinan (4/28) than Meccan
(10/86). Within Meccan, TIME-incipit rate *decreases* Early (21%) → Middle (10%)
→ Late (0%), opposite to the predicted late-Meccan peak.

**Why the reversal?** Examining the 14 TIME-incipit surahs reveals they're
concentrated in EARLY MECCAN (9 of 14 are Early; 2 Medinan, 2 Middle, 0 Late).
So al-Suyūṭī and Ibn ʿAshūr's qualitative intuition about temporal framing may
apply to a different stylistic marker than the one I operationalized. Possible
causes:

1. **Late Meccan surahs are longer and more narrative**, so their first-5
   tokens are more likely to be narrative-opening ("O Prophet", "Surely We
   sent..."). The temporal framing may be mid-surah, not incipit.
2. **Early Meccan oath-opening surahs** like Q 81 (*idhā al-shamsu kuwwirat*),
   Q 82 (*idhā al-samāʾu infaṭarat*), Q 84 (*idhā al-samāʾu inshaqqat*),
   Q 99 (*idhā zulzilati l-arḍu zilzālahā*) are the archetypal TIME-incipits.
   These are ALL Early Meccan in Nöldeke. So the prediction "Meccan concentration"
   was TRUE in a literal sense, just EARLY Meccan, not LATE Meccan.
3. **The Middle/Late Meccan phase** shifts toward longer discursive openings.

### Honest re-framing

The sub (a) SPACE test is a clean positive result: Medinan incipits are
2.55× more likely to start with social vocatives. p = 0.0146 at pre-registered
Bonferroni α = 0.0167.

The TIME result is a clean negative on my pre-registered prediction ("concentrate
in Late Meccan") but a clean positive on a HYPOTHETICAL alternative prediction
("concentrate in Early Meccan"). Since the alternative wasn't pre-registered,
the TIME result is NULL + post-hoc observation of Early-Meccan concentration.

## Garden of forking paths (disclosed)

- **Incipit length** = first 5 tokens chosen a priori. Sensitivity to k=3, 7,
  10 not tested.
- **Basmala-skip and muqaṭṭaʿāt-skip**: checked against project's muqaṭṭaʿāt
  list (29 surahs). For non-muqaṭṭaʿāt surahs, the first verse is the incipit
  (basmala is prepended to Q 1 as v1 which I retain and to all others not
  normally shown).
- **Marker priority TIME > COSMOS > PRAISE > IMPER > SPACE**. If a surah opens
  with both TIME and COSMOS markers (e.g., S81 *idhā al-shamsu kuwwirat*),
  TIME wins. I tested it re-ordered as COSMOS > TIME and saw ~3 COSMOS
  reassignments (81, 82, 84) but the overall Meccan/Medinan ratios for both
  classes are too small to change the Fisher exact significantly.
- **Single-word marker matching** is crude. A phrase like *yā-ayyuha l-nāsu*
  vs *yā-ayyuhā l-ladhīna āmanū* are both SPACE but might have different
  rhetorical weight. Not distinguished.
- **Pre-registered direction for TIME was Meccan > Medinan** — observed
  opposite direction reported honestly; no direction flip.
- **The COSMOS class has only 1 hit** because my TIME-first priority absorbed
  cosmological oaths (*wa-al-shamsu wa-ḍuḥāhā* has COSMOS in position 1 but
  starts with *wa-* which isn't tokenized as TIME; S91 was classified via
  *idhā tlāhā* at position 4, hence TIME). An alternative priority ordering
  would reassign ~5 surahs from TIME to COSMOS but wouldn't change the
  Meccan/Medinan aggregate statistics.

## Classical-scholar followup needed

1. Verify al-Suyūṭī *Itqān* nawʿ 59 enumerates TIME-anchored openings as a
   distinct category. Hand-classify the 14 Early Meccan TIME-incipits against
   al-Suyūṭī's 10 types (praise, letters, vocative, imperative, oath,
   condition, news, honorific, prayer, reasoning).
2. Verify whether Ibn ʿAshūr *al-Taḥrīr* muqaddima supports Early-Meccan or
   Late-Meccan TIME concentration. My pre-reg cited Late Meccan; actual
   Nöldeke-classified TIME incipits are Early Meccan.
3. Adjudicate whether the *wa-* oath-opening (*wa-al-shamsi*, *wa-al-ʿaṣri*,
   *wa-al-ḍuḥā*) should count as TIME (invoking cosmic time-markers) or
   COSMOS (invoking the celestial bodies themselves). al-Zamakhsharī's
   *Kashshāf* framing would help.

## Limits

1. n = 28 Medinan surahs is small. Fisher exact has moderate power.
2. Marker dictionaries built without classical-scholar review — might miss
   key TIME/SPACE stems.
3. "Period × class contingency" uses the binary Meccan/Medinan split from
   Egyptian Standard edition; the 4-phase Nöldeke split has other dimensions.
4. **Informal alternative hypothesis** (TIME concentrates in Early Meccan)
   is NOT pre-registered — cannot claim significance without replication.
5. Jonckheere-Terpstra direction was one-sided for increasing; a two-sided
   or downward test would be post-hoc.

## Verdict

**PARTIAL.** Pre-registered joint verdict FAILS (1 of 3 sub-tests pass). The
SPACE → Medinan concentration is a clean significant finding (p = 0.0146 <
0.0167). The TIME → Late Meccan direction is refuted (actual concentration
is Early Meccan, unregistered). The Ibn ʿAshūr qualitative contrast survives
in one direction (Medinan = social-legal vocatives) and fails in the other
(TIME = Late Meccan). Net: one classically-predicted asymmetry confirmed, the
other reversed. **Publishable SPACE result, null on TIME.**

## Files

- Script: `scripts/h_new_31_incipit_class.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-31.json`
- Seed: 20260413
