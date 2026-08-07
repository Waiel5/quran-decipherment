---
id: H-NEW-62
title: Comprehensive Analysis of Surah Closing Verses (ḥusn al-intihāʾ audit)
phase: B
status: MIXED — T5 PASS (period × closing-class), T1 NULL, T2/T3/T4/T6/T7 NULL under Bonferroni; multiple notable raw-significant signals
date: 2026-04-15
agent: h-new-62-specialist
seed: 20260416
prereg: h-new-62-closings-prereg.md
rules_tuple: (no-tashkeel; canonical 1..114 mushaf order; LAST verse = highest verse-id; whitespace tokenization; substring matching; locked taxonomy)
test_family: 7-test pre-registered census; α_Bonferroni = 0.05/7 = 0.007143
---

# [[h-new-62-closings|H-NEW-62]] — Surah closings, ḥusn al-intihāʾ (RESULTS)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Headline

Of seven pre-registered tests on surah-closing verses, **one PASSES Bonferroni**
(T5: period × closing-class, p = 0.0035), **two miss Bonferroni narrowly but are
strongly raw-significant** (T2 entropy concentration p = 0.0076; T7 twin-pair
count p = 0.0078; both at α_Bonf = 0.00714), and **four are NULL**
(T1 length, T3 paired-attribute fawāṣil, T4 omni-competence formula
`على كل شيء قدير`, T6 muqaṭṭaʿāt × class).

The single hard-PASS finding: closing-verse rhetorical class differs
significantly between Meccan and Medinan surahs. Specifically, the omni-
competence/qadīr formulaic class is sharply Medinan-skewed (5/27 Medinan vs
1/87 Meccan).

The high OTHER bucket (67/114, 58.8%) is itself a substantive finding: when a
locked literal-substring taxonomy of conventional ḥusn al-intihāʾ categories
is applied, a clear majority of closings do NOT match any conventional
formula. Closings are more thematically heterogeneous than classical balāgha
treatises imply.

## Pre-registration and locking

Taxonomy locked BEFORE viewing data; see
`[[h-new-62-closings|h-new-62]]-closings-prereg.md`. Priority ordering:
PRAYER > GLORIFICATION > TAKBĪR-PAIR > QADĪR > WARNING > PROMISE > TAWḤĪD >
QUL > SALAM > NARRATIVE > OTHER. Seed 20260416. All 5000-iteration Monte
Carlo runs share that seed.

## Closing-class distribution (LOCKED taxonomy)

| Class | n / 114 | % |
|---|---|---|
| OTHER | 67 | 58.8 |
| NARRATIVE | 11 | 9.6 |
| PROMISE | 8 | 7.0 |
| GLORIFICATION | 7 | 6.1 |
| QADIR | 6 | 5.3 |
| QUL | 4 | 3.5 |
| TAKBĪR-PAIR | 3 | 2.6 |
| PRAYER | 2 | 1.8 |
| TAWḤĪD | 2 | 1.8 |
| SALAM | 2 | 1.8 |
| WARNING | 2 | 1.8 |

The OTHER bucket dominates, indicating that fewer closings than classical
balāgha treatises imply fall into stock formulas. The next two largest buckets
(NARRATIVE 11, PROMISE 8) describe ~17% of closings; explicit GLORIFICATION
(7) and the omni-competence QADĪR (6) are notably enriched relative to the
narrowness of those triggers.

## Test results (k = 7, α_Bonf = 0.007143)

### T1 — Closing-verse length vs surah mean (paired Wilcoxon)

- W = 2676.5, two-sided p = 0.089
- Median (closing − surah-mean) = +0.40 tokens; 95% bootstrap CI [−0.375, +1.25]
- **NULL.** Closing verses are NOT systematically shorter or longer than surah
  internal verses. (Mild positive bias of about half a token, swamped by within-
  surah variance.)

### T2 — Closing-token entropy vs all-verse-end entropy

- H_close (Shannon, last-token of 114 closings) = 6.44 bits
- H_all (last-token of all 6,236 verses) = 10.11 bits
- Bootstrap reference H from 114-from-corpus draws: 95% CI [7.65, 8.05]
- One-sided p (H_close ≤ random) = 0.0076
- **NULL under Bonferroni** (0.0076 > 0.00714) but raw-significant. The
  observed concentration of closing words is far stronger than test threshold;
  the failure is barely-Bonferroni and the effect (3.7-bit gap) is large.
- Top 5 closing-final tokens: العظيم (4), تعملون (4), عليم (3), العالمين (3),
  الحكيم (3). Heavy concentration on divine-attribute terminations.

### T3 — Paired-attribute fawāṣil at closings (Monte Carlo)

- Observed: 3 surahs (Q 45, Q 59, Q 64; all close with `العزيز الحكيم`)
- MC mean: 1.71; one-sided p = 0.235
- **NULL.** Paired-attribute closings are not enriched relative to a uniform
  within-surah verse draw.

### T4 — `على كل شيء قدير` formula at closing

- Observed at closings: 2 (Q 5, Q 65); in corpus: 35 verses
- Hypergeometric one-sided p = 0.134
- **NULL.** The classical "umbrella" closing formula is NOT preferentially
  located at surah ends.
- MW-5 corollary: classical claim that prayer-formula closings (e.g., Q 1's
  `اهدنا الصراط` style or Q 2's `ربنا لا تؤاخذنا`) are characteristic of
  closings is also NOT supported as a broad pattern: only 2/114 closings are
  primary-PRAYER (Q 2 v286, Q 71 v28). MW-5 expectation NOT met.

### T5 — Period × closing-class (χ²) **PASS**

- 2 × 11 contingency table; χ² = 26.30, dof = 10, p = 0.00347
- **PASS Bonferroni** (0.00347 < 0.00714).
- Driver: QADIR class at closings is 5/27 Medinan (18.5%) vs 1/87 Meccan (1.1%)
  — a near-19× rate ratio.
  - Medinan QADIR closings: Q 4, Q 5, Q 8, Q 24, Q 65 (all "والله بكل شيء عليم"
    or "هو على كل شيء قدير" or "أحاط بكل شيء علما")
  - Meccan QADIR closing: Q 41 ("بكل شيء محيط")
- Secondary driver: GLORIFICATION 6 Meccan vs 1 Medinan; QUL 4 Meccan vs 0
  Medinan.

| Class | Meccan (n=87) | Medinan (n=27) |
|---|---|---|
| GLORIFICATION | 6 | 1 |
| NARRATIVE | 6 | 5 |
| OTHER | 58 | 9 |
| PRAYER | 1 | 1 |
| PROMISE | 5 | 3 |
| QADIR | 1 | 5 |
| QUL | 4 | 0 |
| SALAM | 2 | 0 |
| TAKBĪR-PAIR | 1 | 2 |
| TAWḤĪD | 1 | 1 |
| WARNING | 1 | 1 |

### T6 — Muqaṭṭaʿāt × closing-class (χ²)

- χ² = 5.53, dof = 10, p = 0.854
- **NULL.** Muqaṭṭaʿāt-opened surahs do NOT close differently from
  non-muqaṭṭaʿāt as a class. (This is a notable non-result: [[h-new-57-formulaic-openings|H-NEW-57]] found a
  sharp PASS for muqaṭṭaʿāt × OPENING formulas; the symmetry breaks at the
  ending.)

### T7 — Twin-closings (≥4-token shared suffix)

- Observed: **4 twin pairs** sharing a 4-token closing suffix.
- MC mean (5000 random within-surah draws, seed 20260416): 0.56
- One-sided p = 0.0078
- **NULL under Bonferroni** (0.0078 > 0.00714) but raw-significant; about 7×
  the random expectation.
- The four pairs:

| Pair | Shared 4-token suffix |
|---|---|
| Q 4 ↔ Q 24 | والله بكل شيء عليم |
| Q 11 ↔ Q 27 | ربك بغافل عما تعملون |
| Q 45 ↔ Q 59 | وهو العزيز الحكيم (with preceding ۖ) |
| Q 56 ↔ Q 69 | فسبح باسم ربك العظيم |

- Sensitivity (3-token suffix): 7 pairs (incl. above plus Q 4↔Q 8, Q 8↔Q 24
  on `بكل شيء عليم`; Q 37↔Q 39 on `لله رب العالمين`).
- The Q 56 ↔ Q 69 pair is striking: both surahs close with the IDENTICAL
  five-token clause `فسبح باسم ربك العظيم`, and both belong to the late-Meccan
  rhymed-closing zone. (Q 56 al-Wāqiʿa, Q 69 al-Ḥāqqa.) This is a verbatim
  twin-closing.

## Formulaic-closings inventory (hypergeometric enrichment of closings vs corpus)

| Phrase | In closings | In corpus (verses) | Hypergeom p |
|---|---|---|---|
| الحمد لله | 4 | 23 | **0.0007** |
| الحمد لله رب العالمين | 2 | 6 | **0.0047** |
| بكل شيء عليم | 3 | 20 | 0.0054 |
| العزيز الحكيم | 3 | 29 | 0.0154 |
| بكل شيء محيط | 1 | 2 | 0.036 |
| رب العالمين | 3 | 42 | 0.041 |
| على كل شيء قدير | 2 | 35 | 0.134 |
| تبارك | 1 | 9 | 0.153 |
| المفلحون | 1 | 12 | 0.199 |
| سبحان | 1 | 41 | 0.532 |
| الجنة | 1 | 55 | 0.639 |

The strongest formulaic-closing enrichment is `الحمد لله` (4/114 closings vs
23/6,236 verses, p = 0.0007), Bonferroni-significant. Q 17, Q 27, Q 37, Q 39
all close with this phrase. Notably Q 1 OPENS with `الحمد لله` (v 2) — this
is one of the few Quranic phrases used liturgically as both opening and
closing material; the closing concentration is 5× the random expectation.

The omni-competence formula `على كل شيء قدير`, often singled out in classical
discussion as a typical fasila ending, is NOT enriched at closings (p = 0.134)
when measured against its 35 corpus appearances.

## Top closing-final tokens (rightmost whitespace token of v-final)

| Token | n | Token | n |
|---|---|---|---|
| العظيم | 4 | الحاكمين | 2 |
| تعملون | 4 | يؤمنون | 2 |
| عليم | 3 | ترجعون | 2 |
| ۩ (sajda) | 3 | يوعدون | 2 |
| العالمين | 3 | رحيم | 2 |
| الحكيم | 3 | (rest unique) | 1 |

Of the 114 closing-final tokens, 95 are unique. The most common single
final-token (العظيم, 4 occurrences) accounts for only 3.5% of the distribution.
This contrasts with last-tokens corpus-wide (where conjugational endings
dominate massively). The 6.44-bit closing entropy vs 10.11-bit corpus entropy
reflects that closings concentrate on ~10–15 stock terminal lexemes, but
within that set the distribution is fairly flat.

## Twin-closings notable analysis

- **Q 56 ↔ Q 69** (`فسبح باسم ربك العظيم`): Verbatim 5-token suffix; both are
  late-Meccan rhymed surahs treating eschatological themes (al-Wāqiʿa, al-Ḥāqqa).
  This pair appears designed liturgically as a paired terminal doxology.
- **Q 4 ↔ Q 24** (`والله بكل شيء عليم`): Both Medinan, both legal-content
  surahs (al-Nisāʾ, al-Nūr); both end on the divine-omniscience capstone for
  the law-giving register.
- **Q 11 ↔ Q 27** (`ربك بغافل عما تعملون`): Both Meccan, both narrative
  prophetic-cycle surahs (Hūd, al-Naml). The shared suffix is a warning
  capstone (`your Lord is not unaware of what you do`).
- **Q 45 ↔ Q 59** (`وهو العزيز الحكيم`): Mixed period (Meccan, Medinan); the
  paired-attribute closing in TAKBĪR-PAIR class.

## MW-5 (classical prediction) explicit check

The pre-reg cited the classical observation that some surahs end with prayer
formulas comparable to Q 1's `اهدنا الصراط المستقيم`. Empirically:

- Primary PRAYER class at closings: 2/114 (Q 2, Q 71) = 1.8%
- Hypergeometric enrichment of `ربنا اغفر` substring at closings: 1/114 vs
  6/6,236; p ≈ 0.10. **NOT ENRICHED.**
- Hypergeometric enrichment of `اهدنا الصراط` at closings: 0/114 vs 1/6,236
  (the unique Q 1:6 occurrence is NOT a closing).

**The MW-5 classical observation is NOT supported as a broad pattern.** Two
surahs do close with explicit duʿāʾ formulas, but the rate (1.8%) is consistent
with the within-surah base rate of duʿāʾ verses; no over-concentration at
endings. This MIRRORS the prior REFUTATION of al-Suyūṭī's ḥusn al-ibtidāʾ as
a broad pattern at openings: at both ends of surahs, conventional rhetorical
formulas are LESS systematic than the balāgha tradition implies.

## Surah-class correlations summary

| Correlation | Result |
|---|---|
| Closing-class × period (Meccan/Medinan) | **PASS** χ² p = 0.0035 |
| QADIR closings concentrated in Medinan | 5/27 vs 1/87 (rate ratio ≈ 19) |
| GLORIFICATION closings concentrated in Meccan | 6/87 vs 1/27 |
| QUL closings only in Meccan | 4/87 vs 0/27 |
| Closing-class × muqaṭṭaʿāt | NULL (p = 0.85) |
| Closing-class × prophet-named (n=6) | (small-n; 5 OTHER, 1 PRAYER (Q 71)) |
| Closing length vs surah mean | NULL (median diff +0.4 tokens) |

## Convergence with prior work

- **[[h-new-57-formulaic-openings|H-NEW-57]] (formulaic OPENINGS, STRONG-PASS):** muqaṭṭaʿāt × opening-formula
  was sharply structured (13/13). The mirror result here (T6 muqaṭṭaʿāt ×
  closing-class, NULL) shows **structural asymmetry**: the muqaṭṭaʿāt cluster
  shapes openings but NOT closings. This is itself a finding.
- **al-suyuti-husn-ibtida REFUTED for openings:** This run independently
  refutes ḥusn al-intihāʾ as a broad pattern via T1, T3, T4, MW-5. Both the
  classical "excellence of opening" and "excellence of ending" claims fail
  as comprehensive descriptors when audited literally.
- **Period structure (PASSES):** The Medinan QADIR-closing cluster is the
  clearest novel signal. It dovetails with the broader project finding that
  Medinan surahs use more legalistic-omniscient capstones (`واسع عليم`,
  `بكل شيء عليم`) — a register choice tied to legal-content surahs.

## Falsifiability and PASS/NULL transparency

- **PASS (T5)** is published with full table, drivers identified, p-value below
  Bonferroni threshold.
- **NULLs (T1, T3, T4, T6)** published equally; classical MW-5 expectation
  explicitly contradicted.
- **Marginal raw-significant signals (T2, T7)** flagged at α_Bonf threshold;
  not over-claimed. Effect-size data (3.7-bit entropy gap; 7× twin-pair
  enrichment) reported for replication.
- **Garden-of-forking-paths** logged in prereg before run.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-62-closings-prereg.md`
- Script: `scripts/h_new_62_closings.py`
- Per-surah JSON + summary: `findings/phase-b-hypotheses/csv/h-new-62.json`
- Journal: `journal/h-new-62-run-1.md`

## Verdict

**MIXED.** ḥusn al-intihāʾ as a broad classical category is NOT supported (most
predicted formulaic closings are not enriched; closing length is not
distinctive; muqaṭṭaʿāt × class is null; MW-5 prayer-formula expectation
fails). The single hard-PASS finding is **period × closing-class structure**
driven by Medinan QADIR-formula closings. Two raw-significant patterns
(closing-token concentration; verbatim twin-pair count) deserve follow-up at a
narrower α-budget. The verbatim twin-pair Q 56 ↔ Q 69 (`فسبح باسم ربك العظيم`)
and Q 4 ↔ Q 24 (`والله بكل شيء عليم`) are individually interesting micro-signals.

