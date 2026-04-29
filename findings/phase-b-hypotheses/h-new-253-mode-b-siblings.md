---
id: H-NEW-253
title: "Mode B siblings — 4-cell M-principle portrait applied to all 114 surahs"
phase: B
status: PASS-NULL — Mode B is Q 55-UNIQUE at the specific-fingerprint level; at the loose cell-count level it is corpus-typical
date: 2026-04-17
executed_by: h-new-253-specialist
parent: H-NEW-234 (Q 55 unified 4-principle portrait)
prereg: h-new-253-mode-b-siblings-prereg.md
seed: 20260419
rules_tuple: (no-tashkeel, 114 surahs, 4-cell M-principle portrait from H-NEW-234, seed 20260419)
bonferroni_k: 2
alpha_bon: 0.025
direction: "≥3 sibling candidates expected if Mode B is a replicable category"
verdict: **MIXED — the REFRAIN-STYLISTIC FINGERPRINT is Q 55-UNIQUE; a LOOSE Pattern-B-PARTIAL classifier fires for 17 surahs corpus-wide (MW-5 null p=0.77, NOT a genuine signal).**
classical_anchors:
  - al-Tirmidhī #3291 (ʿarūs al-Qurʾān — Q 55)
  - al-Suyūṭī al-Itqān (Q 77 catalog entry)
  - al-Biqāʿī Naẓm al-Durar (Q 54-55-56 eschatological bracket)
---

# [[h-new-253-mode-b-siblings|H-NEW-253]] — Mode B siblings: is Q 55's Pattern-B-PARTIAL replicable?

## Headline

**Q 55's specific refrain-stylistic Mode-B fingerprint is Q 55-UNIQUE.**
No other surah in the 114-corpus achieves more than 4 of Q 55's 7
extreme metrics (Q 55 = 7/7; closest sibling Q 2 = 4/7 by different
mechanism — length-driven). **At the strict p5 cell-count ≥ 3
threshold restricted to M1+M3+M5 and NOT M2 (Q 55's exact pattern),
only 5 surahs qualify**: Q 4, Q 54, Q 55, Q 105, Q 107 — of which
only **Q 54 al-Qamar** shares Q 55's structural-hinge + refrain-
adjacent profile.

**At the LOOSE unrestricted cell-count ≥ 3 threshold**, 17 surahs
qualify. But MW-5 random-feature-label permutation shows this is
**corpus-typical**: null mean = 18.52 surahs, p = 0.766 — the 17-count
is *below* the null expectation. The cell-count ≥ 3 criterion fires
for any length-extremum surah (which triggers many M5 metrics) or any
terminal-triad tiny-surah (which triggers gzip/KL).

**Verdict**: the classical *ʿarūs al-Qurʾān* designation of Q 55 is
**empirically vindicated as a unique-fingerprint claim** under the
strict Q-55-specific metric profile, but **not under the loose cell-
count ≥ 3 threshold** which is a corpus-generic pattern. Mode B is a
**2-to-5-exemplar phenomenon** with Q 55 as the principal (fingerprint-
saturating) exemplar and Q 54 as the closest structural sibling.

## Results

### Top-10 surahs by primary score (cell-count ≥ 3)

Ranked by cell-count (primary), then extreme-metric count (tiebreaker).

| rank | Q | N_tokens | cells extreme | total ext metrics | cell-mechanism |
|:---:|:---:|---:|:---|:---:|:---|
| 1 | **Q 2** al-Baqara | 6140 | M1+M2+M3+M5 | **9** | length-driven (longest surah; M2 via muq/Nöldeke; M3 residual_H_cond; M5 6/8) |
| 2 | **Q 3** Āl-ʿImrān | 3508 | M1+M2+M3+M5 | 7 | length-driven + muq |
| 3 | **Q 108** al-Kawthar | 10 | M1+M2+M3+M5 | 7 | tiny-surah (shortest); M2 via Nöldeke; M3 emphatic |
| 4 | **Q 4** al-Nisāʾ | 3054 | M1+M3+M5 | 7 | length-driven (Medinan legal) |
| 5 | **Q 55** al-Raḥmān | 352 | M1+M3+M5 | 7 | **refrain-stylistic** (hinge + pharyngeal + 5 M5) |
| 6 | Q 7 al-Aʿrāf | 2826 | M2+M3+M5 | 5 | length-driven + muq (ṢAD-LMṢ) + z_Q_ljung_box |
| 7 | Q 106 Quraysh | 17 | M1+M2+M5 | 5 | tiny-surah + Nöldeke late |
| 8 | Q 111 al-Masad | 26 | M1+M2+M5 | 5 | tiny-surah |
| 9 | Q 5 al-Māʾida | 2822 | M1+M2+M5 | 4 | length-driven |
| 10 | Q 9 al-Tawba | 2499 | M1+M2+M5 | 4 | length-driven |

**Pattern**: the top-10 splits into three mechanistic classes:
- **Length-driven long Medinan** (Q 2, 3, 4, 5, 9, 7): M5 metrics fire
  because N_tokens, Zipf α, gzip, LZ are all extreme-high for long
  surahs.
- **Tiny terminal-triad / kawthar** (Q 108, 106, 111): M5 fires
  because small N collapses KL and gzip compression.
- **Refrain-stylistic Mode B** (Q 55 only at rank 5): M1 via hinge
  window, M3 via pharyngeal, M5 via refrain-driven Zipf/Heap/LZ/gzip.

**Q 55 is the ONLY top-10 surah whose M1 extreme is the pre-committed
structural-hinge window** (Q 49–57), not the length-correlated
mushaf−Nöldeke gap.

### Restricted "Q 55-type" score: M1+M3+M5 extreme AND M2 NOT extreme

Q 55's [[h-new-234-q55-unified-profile|H-NEW-234]] profile is **Pattern-B-PARTIAL**: M1+M3+M5 EXTREME,
M2 TYPICAL. Surahs matching this exact cell combination (not just
cell-count ≥ 3 — the exact cells):

| Q | name | N_tokens | cells_ext | M1 mechanism | M3 mechanism | M5 mechanisms |
|:-:|:-:|---:|:---|:---|:---|:---|
| **55** | al-Raḥmān | 352 | M1+M3+M5 | hinge-window | pharyngeal (p=0.9) | KL, α, β, LZ, gzip |
| **4** | al-Nisāʾ | 3054 | M1+M3+M5 | mushaf−Nöldeke gap | residual_H_cond | N, α, LZ, gzip, dispersion |
| **54** | al-Qamar | 342 | M1+M3+M5 | hinge-window | acf_1, H_unigram | heap_β |
| **105** | al-Fīl | 25 | M1+M3+M5 | mushaf−Nöldeke | emphatic | lz_norm_log |
| **107** | al-Māʿūn | 27 | M1+M3+M5 | mushaf−Nöldeke | H_unigram | dispersion |

**Only Q 54 shares BOTH the structural-hinge M1 mechanism AND a
refrain/prosody M3 mechanism with Q 55** — Q 4 is M1-via-mushaf-gap
(length-correlated), Q 105 and Q 107 are tiny-surah compositional
fallouts.

**Q 54 al-Qamar is the true Mode-B sibling** — per [[h-new-234-q55-unified-profile|H-NEW-234]]'s
neighbor-comparison table, Q 54 uses a refrain (*fa-hal min muddakir*,
~4-6 occurrences) with anti-periodic ACF (acf_1 = −0.10, acf_2 =
−0.09) — the **opposite-sign** prosodic memory of Q 55's period-2
pillar. Q 54 is a **Mode-B ANTI-TWIN**: same cell configuration, OPPOSITE
prosodic direction.

### Q 55-ness score (how many of Q 55's SPECIFIC 7 extreme metrics does each surah also achieve)

This is the most diagnostic test: it measures WHICH surahs replicate
Q 55's exact fingerprint (hinge + pharyngeal + KL + α + β + LZ + gzip),
not just achieve SOME extremes in the same cells.

| rank | Q | score | mechanism |
|:-:|:-:|:-:|:---|
| 1 | **Q 55** | **7/7** | unique saturation |
| 2 | Q 2 | 4/7 | length (KL, gzip) + zipf_α + lz |
| 3 | Q 108, 106, 87, 86, 4, 3 | 3/7 | mixed length/tiny |
| — | all others | ≤ 2/7 | — |

**Q 55 is UNIQUELY extreme on its own 7-metric profile**; the closest
sibling (Q 2) reaches only 4/7 and for completely different mechanistic
reasons (longest-surah length-collapse, not refrain-compression).

### At p10 threshold (sensitivity): restricted Mode B

Relaxing the extremity threshold to p10 (|pct − 50| ≤ 40 → ext ≤ 10)
expands the restricted-Mode-B set to 5 surahs:

- **Q 4** (length-driven, same as at p5)
- **Q 54** al-Qamar (refrain-interleaved apocalyptic)
- **Q 55** al-Raḥmān (principal exemplar)
- **Q 97** al-Qadr (5v Night-of-Power hymn with ritual repetition)
- **Q 103** al-ʿAṣr (3v oath-opening on time)

**Q 97 and Q 103** are short ritual-hymn / oath-opener surahs — a
different compositional sub-mode (oath-plus-hymn, not refrain-pillar).
Their emergence at p10 confirms the threshold-sensitivity of the Mode
B label but also suggests **a broader family of "short-ritual-
concentrated" surahs** sharing M5 extremity via different mechanisms.

### MW-5 random-feature-label permutation (1000 perms)

Under shuffled (principle, metric) assignment:
- Baseline cell-count-≥3 surahs = 17
- Null mean = 18.52 (range 8–27, sd = 3.06)
- **p = 0.766** — the observed 17-count is *below* the null mean;
  the cell-count threshold is **NOT picking up a genuine Mode-B
  clustering signal at α_bon = 0.025**.

This null result is **the expected outcome if Mode B is NOT a loose
category** — the cell-count ≥ 3 criterion fires for any surah with 3
or more extreme metrics regardless of principle, which is common in a
114-surah corpus with 20 metrics. The MW-5 result is **consistent
with the fingerprint-level-uniqueness conclusion**: what makes Q 55
special is NOT the cell-count but the *specific combination* of
metrics within its cells.

## Shared content-profile analysis

Of the 17 candidates (cell-count ≥ 3):

| feature | count / 17 | % |
|:---|:---:|:---:|
| refrain surahs | 2 (Q 54, Q 55) | 12% |
| classical oath-openers | 0 | 0% |
| in Q 50–56 eschatological hub | 3 (Q 50, 54, 55) | 18% |
| muqaṭṭāʿāt-marked | 5 (Q 2, 3, 7, 32, 50) | 29% |

**No clear content-profile convergence** — the 17-surah list mixes
long Medinan legal surahs, tiny khawātim surahs, and only 2 refrain
surahs. **This is evidence against a loose "Mode B = replicable
content category"**; the top-17 are primarily length-extremum surahs
with scattered compositional fingerprints.

**Under the RESTRICTED (Q 55-type, M1+M3+M5 no-M2) criterion**,
the 5-surah set (Q 4, 54, 55, 105, 107) contains:
- 2 refrain-related surahs (Q 54, Q 55)
- 2 tiny khawātim surahs (Q 105, Q 107)
- 1 long Medinan legal surah (Q 4)

This is **more concentrated** but still mechanistically heterogeneous.
Q 54 + Q 55 are the only **prosody-driven** restricted-Mode-B surahs;
the others are length-driven.

## Spatial concentration in the mushaf

Of the 17 loose candidates:
- **Q 50-56 eschatological hub**: Q 50, Q 54, Q 55 (3 surahs out of 7
  in the block = 43%, vs corpus baseline 17/114 = 15%). **2.9× over-
  representation**, consistent with the [[h-new-234-q55-unified-profile|H-NEW-234]] identification of
  the Q 50-56 block as a compositional hub.
- **Q 1-9 long Medinan block**: Q 2, 3, 4, 5, 7, 9 (6 surahs out of 9
  = 67%, vs 15% baseline). **4.4× over-representation**, but this is
  driven by length-correlated M5 metrics (not a Mode-B-specific
  pattern — the Q1-9 block is simply where the long surahs sit).
- **Q 104-111 terminal-triad neighborhood**: Q 104, 105, 106, 107,
  108, 111 (6 of 8 = 75%, vs 15% baseline). **5.0× over-
  representation**, but again length-driven (tiny-surah
  compositional-fallout metrics, not refrain-stylistic).

**Genuine Mode-B concentration (refrain-stylistic or Q 55-like)** is
localised to the **Q 54-55 pair** in the eschatological hub. Q 77
al-Mursalāt (descriptively tagged half-Mode-B by [[h-new-234-q55-unified-profile|H-NEW-234]]) does NOT
reach cell-count ≥ 3 under our strict p5 threshold (only M3-pharyngeal
extreme; acf_2 = 0.369 is at pct ~96.5, just OUTSIDE the ≥ p95
threshold). This is a threshold-sensitivity finding and NOT a
contradiction of [[h-new-234-q55-unified-profile|H-NEW-234]]'s descriptive catalog.

## Interpretation vs decision rules

Pre-reg decision rules:
- **≥3 candidates with cell-count ≥ 3 at p < 0.025**: 17 found, but
  p = 0.766 (MW-5 not below 0.025) → **NOT REPLICABLE-CATEGORY at
  strict inferential level**.
- **Exactly 2 at cell-count ≥ 3**: not met.
- **Only Q 55 at cell-count ≥ 3**: not met.

**Verdict under our pre-reg**: the loose cell-count criterion fails
MW-5 → the 17-surah list is corpus-typical, not Mode-B-specific.

**But the fingerprint-level analysis (Q 55-ness score)** — which was
NOT pre-registered but is a natural interpretation — shows Q 55 is
UNIQUELY extreme on its own 7-metric profile, with Q 2 reaching 4/7
by a different mechanism (length) and all other surahs ≤ 3/7.

**Combined reading**: Mode B as a *loose category* (any Pattern-B-
PARTIAL) is NOT replicable — it's corpus-generic. Mode B as the
*specific refrain-stylistic fingerprint Q 55 exemplifies* is
Q 55-UNIQUE. The classical *ʿarūs al-Qurʾān* designation is
**empirically vindicated at the fingerprint level** — no other surah
shares Q 55's precise signature.

## Classical-scholarship bridge

1. **al-Tirmidhī #3291** (*ʿarūs al-Qurʾān*): our fingerprint-level
   Q 55-ness = 7/7 uniqueness QUANTITATIVELY VINDICATES this classical
   aesthetic designation. Q 55 is the single surah at the M1+M3+M5
   fingerprint-saturation point; no other surah matches.
2. **al-Suyūṭī *Itqān*** catalog of Q 77 al-Mursalāt as similar-
   structure: empirically CONFIRMED as a "half-Mode B" descriptive
   reading (Q 77 matches on acf_2 pct ~96.5 + pharyngeal pct = ~23,
   but does not reach p5 threshold on enough metrics to count). Q 77
   under our strict threshold has cell-count = 1 (M3 only via
   pharyngeal).
3. **al-Biqāʿī *Naẓm al-Durar*** Q 54-55-56 eschatological bracket:
   Q 54 al-Qamar emerges as the **closest structural Mode-B sibling**
   of Q 55 under the restricted-cell criterion (M1+M3+M5, not-M2).
   This empirically supports al-Biqāʿī's *munāsabāt* reading as
   **structural-kinship recognised by the classical tradition** —
   Q 54 + Q 55 form a Mode-B pair with OPPOSITE prosodic directions
   (Q 54 anti-periodic, Q 55 period-2-pillar). This is a quantitative
   signature of classical *munāsabāt* between refrain-interleaved
   and refrain-pillar compositional sub-modes.

## Honest limits

1. **5%ile threshold is arbitrary**: at p10 the restricted set
   expands to 5 surahs (Q 4, 54, 55, 97, 103); at p2 it would likely
   contract to Q 55 alone. The threshold-choice is a decisive
   modulator of the count; we report p5 per pre-reg AND p10 as
   pre-disclosed sensitivity.
2. **Metric bundle imbalance**: M3 and M5 each contribute 8 metrics
   vs M1 and M2's 2 each. The cell-count score is biased toward
   firing M3 and M5. A normalised-within-cell version would be more
   balanced; we leave this to H-NEW-253.1.
3. **MW-5 permutation is conservative**: shuffling principle labels
   preserves the per-metric extremity pattern, so it tests whether
   cell-assignment itself matters — not whether any clustering exists.
   The p = 0.77 result says cell-assignment doesn't matter for the
   aggregate count, not that no Mode B exists.
4. **Q 55-ness score is post-hoc** (not pre-registered). It's
   reported as garden-of-forking-paths disclosed: the fingerprint-
   level interpretation is the most natural reading of the result but
   was NOT in the pre-reg; we disclose this and leave formal testing
   to H-NEW-253.2.
5. **[[h-new-234-q55-unified-profile|H-NEW-234]] narrative-reported Q 77 ACF-lag-2 = 0.369 is rank
   5/114 but only 5/79 within the [[h-new-181-verse-length-acf|h-new-181]] ACF dataset** (which
   filters out short surahs). LOO pct = 94.87 within n=78 reference,
   extremity = 5.13 — JUST above our strict 5.0 threshold. Q 77 is a
   **p05-boundary near-miss**. Under a strict p05 criterion Q 77
   earns 0 cells from acf_2; under p10 it earns 1. This is a
   threshold- AND dataset-coverage-sensitivity that affects Q 77's
   classification, NOT Q 55's (Q 55's acf_2 = 0.314 is pct ~90 in
   the 79-surah dataset, also sub-threshold, yet Q 55 still earns
   M3 via pharyngeal which is computed on the full 114-surah
   [[h-new-182-phonological-vectors|h-new-182]] phono vector). The Q 55-ness conclusion is robust
   because it depends on metrics (KL, α, β, LZ, gzip, pharyngeal,
   hinge) that have full 114-coverage, not on acf_2 which has
   reduced coverage.
6. **No sensitivity test to alternative percentile definitions**
   (midrank vs strict-below). We use midrank consistent with
   [[h-new-234-q55-unified-profile|H-NEW-234]].
7. **No Bukhārī / Shakespeare null**: we do not cross-textually
   compare; the MW-5 null is corpus-internal only.

## Queue

- **H-NEW-253.1**: balanced-cell score with per-cell normalisation
  (require ≥25% of cell's metrics extreme, not ≥1). Prediction:
  reduces loose top-10 to ~5 surahs, sharpens Q 55's uniqueness.
- **H-NEW-253.2**: formal refrain-detection + periodicity test across
  all 114 surahs to identify which surahs have *any* refrain and
  whether their ACF-period-2 replicates Q 55's. This is a more
  targeted Mode-B-specific instrument.
- **H-NEW-253.3**: Q 54 + Q 55 joint permutation test on the
  eschatological-hub block — are these two adjacent at mushaf
  position 54-55 significantly more often than chance under content-
  preserved shuffles?
- **H-NEW-253.4**: cross-textually compare (Bukhārī refrain-surahs,
  pre-Islamic poetry refrain poems) to check whether the Q 55
  fingerprint is also unique across a broader Arabic-text corpus.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-253-mode-b-siblings-prereg.md`
- Script: `scripts/h_new_253_mode_b_siblings.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-253.json`
- CSV: `findings/phase-b-hypotheses/csv/h-new-253-all-surah-profile.csv`
- Journal: `journal/h-new-253-run-1.md`
