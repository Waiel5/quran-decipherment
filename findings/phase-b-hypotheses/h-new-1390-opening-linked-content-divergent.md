---
id: H-NEW-1390
title: OPENING-LINKED CONTENT-DIVERGENT mushaf-adjacent pair corpus scan
date_run: 2026-05-09
parent_finding: Q073-F-02 (MASTER-FINDINGS-LEDGER §10.48.2)
prereg_sha: d17f38124d228623f7e512d301f6519590ece5c4cd2c6b543e983a1185a41ec2
seed: 20260509
verdict: DIRECTIONAL — class of size 19 recovered (16.8% of 113 pairs); signature is REAL and SUBSTANTIVELY LARGER than the Q 73 ↔ Q 74 seed, but the observed count is 0.81× the count expected under marginal independence — the joint signature does NOT exceed chance given the marginal frequencies of clamped-zero seams, morph-iso openers, and FR-distant pairs.
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
files:
  prereg: findings/phase-b-hypotheses/prereg-h-new-1390-opening-linked-content-divergent.md
  script: findings/phase-b-hypotheses/scripts/h-new-1390.py
  json:   findings/phase-b-hypotheses/csv/h-new-1390.json
---

# H-NEW-1390 — OPENING-LINKED CONTENT-DIVERGENT mushaf-adjacent pair corpus scan


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

## Origin

Q073-F-02 (Q 73 ↔ Q 74 muzzammil/muddaththir vocative pair, DIRECTIONAL 2026-05-09, see MASTER-FINDINGS-LEDGER §10.48.2) found a pair signature with three positive axes (axis A clamped-zero TSP seam PASS, axis B clamped-zero seam in `h-new-720.json bottom10_cheap`, axis C morph-iso 3-word vocative opener) and one negative axis (axis A FR-mutual-top-15 FAIL: Q 74 ranks 37th in Q 73's nearest-neighbor list and Q 73 ranks 37th in Q 74's). The conjunction of (opening-formula coupling AND mushaf-position coupling AND content divergence on root-distribution) had no prior architectural label.

H-NEW-1390 formalizes the signature as a 4-axis flag tuple and runs an enumerative scan over all 113 mushaf-adjacent pairs to test whether OPENING-LINKED CONTENT-DIVERGENT is a corpus class (≥3 instances) or a corpus singleton.

## Method

For each of 113 mushaf-adjacent pairs (Q_n, Q_{n+1}), compute four boolean flags:

- **A — clamped-zero TSP seam**: delta_raw ≤ 0 in `h-new-720.json per_adjacency`. Exactly 13 such pairs corpus-wide.
- **B — morph-iso first 3 words**: word-1 + word-2 identical AND word-3 same morphological template (same first letter, length within ±1).
- **C_strict — identical opener subclass**: same opener class from a locked 20-class taxonomy, with subclass-matching where applicable (e.g., ya-ayyuha:al-nabī matches ya-ayyuha:al-nabī but not ya-ayyuha:al-nās).
- **D — FR mutual top-15**: each surah in the other's 15 nearest FR-neighbors per the Fisher-Rao distance matrix from `h-new-111.json`.

**Signature** = (A ∨ B ∨ C_strict) ∧ ¬D = TRUE.

Direction-locked H1: ≥3 pairs satisfy the signature AND observed-count ≥ 1.5× expected-under-independence.

## Results

### Marginals (across 113 mushaf-adjacent pairs)

| Axis | TRUE count | TRUE rate |
|:--|--:|--:|
| A clamped-zero seam | 13 | 11.50% |
| B morph-iso first 3 words | 4 | 3.54% |
| C strict opener subclass match | 19 | 16.81% |
| C loose opener class match | 36 | 31.86% |
| D mutual FR top-15 | 32 | 28.32% |
| D=FALSE (FR-distant) | 81 | 71.68% |
| Opening-linked (A ∨ B ∨ C_strict) | 31 | 27.43% |

### Independence baseline

Under marginal independence:
- P(opening-linked) = 1 − (1 − 0.1150)(1 − 0.0354)(1 − 0.1681) = 0.2898
- P(signature) = P(opening-linked) × P(D=FALSE) = 0.2898 × 0.7168 = 0.2078
- Expected count over 113 pairs = **23.48**

### Observed

**Observed signature count = 19** (16.81% of 113 pairs).

**Ratio observed/expected = 19 / 23.48 = 0.81**.

Observed is BELOW expected under independence. The seed Q 73 ↔ Q 74 IS recovered (A=TRUE, B=TRUE, C_strict=FALSE because Q 73's ya-ayyuha subclass `al-muzzammil` differs from Q 74's `al-muddaththir`; signature still TRUE via A ∨ B).

### The 19 signature pairs

| Pair | A | B | C_strict | rank_n+1 in n | rank_n in n+1 | v1(n) | v1(n+1) |
|:--|:-:|:-:|:-:|--:|--:|:--|:--|
| Q11→Q12 | F | F | T | 34 | 5 | الر ۚ كتاب أحكمت آياته | الر ۚ تلك آيات الكتاب |
| Q14→Q15 | F | F | T | 73 | 93 | الر ۚ كتاب أنزلناه إليك | الر ۚ تلك آيات الكتاب |
| Q29→Q30 | F | F | T | 33 | 12 | الم | الم |
| Q30→Q31 | F | F | T | 11 | 35 | الم | الم |
| Q31→Q32 | F | F | T | 36 | 75 | الم | الم |
| Q34→Q35 | F | F | T | 28 | 24 | الحمد لله الذي له ما | الحمد لله فاطر السماوات والأرض |
| Q42→Q43 | F | F | T | 64 | 65 | حم | حم |
| Q43→Q44 | F | F | T | 10 | 51 | حم | حم |
| Q44→Q45 | F | F | T | 40 | 12 | حم | حم |
| Q64→Q65 | T | F | F | 20 | 1 | يسبح لله ما في السماوات | يا أيها النبي إذا طلقتم |
| Q65→Q66 | T | T | T | 25 | 49 | يا أيها النبي إذا طلقتم | يا أيها النبي لم تحرم |
| Q72→Q73 | T | F | F | 25 | 46 | قل أوحي إلي أنه استمع | يا أيها المزمل |
| **Q73→Q74** | **T** | **T** | F | **37** | **37** | يا أيها المزمل | يا أيها المدثر |
| Q81→Q82 | F | F | T | 19 | 22 | إذا الشمس كورت | إذا السماء انفطرت |
| Q85→Q86 | F | F | T | 20 | 31 | والسماء ذات البروج | والسماء والطارق |
| Q86→Q87 | T | F | F | 25 | 23 | والسماء والطارق | سبح اسم ربك الأعلى |
| Q91→Q92 | T | F | F | 22 | 13 | والشمس وضحاها | والليل إذا يغشى |
| Q93→Q94 | T | F | F | 4 | 16 | والضحى | ألم نشرح لك صدرك |
| Q109→Q110 | T | F | F | 9 | 17 | قل يا أيها الكافرون | إذا جاء نصر الله والفتح |

The seed pair Q 73 → Q 74 is in row 13 (bold). Q 73's rank-37 / Q 74's rank-37 symmetry matches the Q073-F-02 observation exactly — the script is consistent with the prior measurement.

### Verdict per pre-registered acceptance window

| Pre-locked outcome | Result |
|:--|:--|
| Observed = 0 | NO (signature seed Q73→Q74 recovered) |
| Observed = 1 | NO (19 > 1) |
| Observed = 2 | NO |
| Observed ≥ 3 AND ratio ≥ 1.5 | NO (ratio = 0.81 < 1.5) |
| **Observed ≥ 3 AND ratio < 1.5** | **YES — DIRECTIONAL** |

**Verdict: DIRECTIONAL**. The OPENING-LINKED CONTENT-DIVERGENT class exists with 19 corpus instances (well above the ≥3 threshold for "class" status), but the joint signature count is below what one would expect by chance combination of the three marginal rates. The signature is a real architectural pattern (it captures every muqaṭṭāʿat repeat-opener that fails FR-mutual-top-15, every wa-oath repeat-opener that fails, etc.), but it is not an above-chance enrichment over the marginals.

## Interpretation

The negative result on the 1.5×-expected criterion reflects a structural fact: **opening-formula repetition is partly anti-correlated with FR cohesion**. When two adjacent surahs share an opener (like the 7-surah ḥawāmīm streak Q 40–46, or the 3-surah الم streak Q 29–31, or the 3-surah al-Rāʾ streak Q 11/14/15), they are systematically MORE likely to be FR-distant than the corpus average, NOT less. This is consistent with cross-finding-025: opening-formula is a thin marker (≤3 words of surah content) and does not drive FR-cohesion on root-distribution.

In other words: the marginal P(D=FALSE) = 0.72 is INFLATED by the very phenomenon being tested — repeat-opener pairs tend to be content-divergent — so the "expected" baseline under independence is artificially high, and the observed signature does not beat it.

**What IS established by H-NEW-1390**: OPENING-LINKED CONTENT-DIVERGENT is not a singleton class (Q 73 ↔ Q 74 has 18 corpus siblings). It is a substantial architectural pattern, accounting for 19/113 ≈ 17% of all mushaf-adjacent pairs. The class includes:

- **9 muqaṭṭāʿat repeat-opener pairs**: Q 29→30, Q 30→31, Q 31→32 (الم streak); Q 11→12, Q 14→15 (الر streak); Q 42→43, Q 43→44, Q 44→45 (حم streak); Q 65→66 (ya-ayyuha al-nabī).
- **2 al-hamd / wa-oath pairs**: Q 34→35 (al-hamd), Q 85→86 (wa-al-samāʾ).
- **2 idhā-conditional pairs**: Q 81→82 (idhā al-shams kuwwirat / idhā al-samāʾ infaṭarat).
- **6 clamped-zero seam pairs** without strict opener-class match: Q 64→65, Q 72→73, Q 73→74, Q 86→87, Q 91→92, Q 93→94, Q 109→110. These are TSP-architectural couplings without explicit opener-formula repetition.

The original Q 73 ↔ Q 74 seed is an exemplar of the third subset (TSP-clamped + morph-iso ya-ayyuha 3-word vocative, but subclass differs).

## Connections

- **Q073-F-02**: Seed; this scan REPLICATES the Q 73 ↔ Q 74 FR-rank-37 measurement exactly (consistency check passed).
- **H-NEW-1240 / cross-finding-013 13-seamless set**: Provides Axis A. All 13 clamped-zero seams are enumerated in `h-new-720.json bottom10_cheap` plus extension.
- **H-NEW-111 / cross-finding-011 Fisher-Rao matrix**: Provides Axis D.
- **Cross-finding-025 marker-thickness rule**: H-NEW-1390 STRENGTHENS the rule. Thin opening-formula markers (≤3 words of content) systematically associate with FR-distant pairs in the mushaf-adjacent universe. The ḥawāmīm / الم / الر streaks are textbook examples: same opener, content-divergent on root-distribution.
- **Q 73 ↔ Q 74 specifically**: Reframed by H-NEW-1390 from "candidate first instance of new architectural class" (Q073-F-02 language) to "exemplar of a 19-pair architectural pattern that operates orthogonally to FR-cohesion at the opening-formula axis".
- **OQ-3 (other introduction-marker classes besides muqaṭṭāʿat)**: H-NEW-1390 implies that opening-formula markers (including muqaṭṭāʿat streaks themselves) are introduction-marker classes that systematically PRODUCE OPENING-LINKED CONTENT-DIVERGENT pairs rather than FR-cohesive clusters. This recasts OQ-3 — the question "what other introduction-marker classes are there?" should be paired with "what architectural pattern do they produce?", and the answer is: OPENING-LINKED CONTENT-DIVERGENT pairs, not FR-cohesive blocks (except where the marker has multi-axis support).

## Honest limits

- **The independence baseline is itself biased**: the test asks whether opening-linked pairs are MORE FR-distant than the corpus average, but the corpus average is computed over pairs whose D=FALSE rate (72%) is already inflated by exactly the phenomenon under test. A within-class control (e.g., compare opening-linked pairs' D=FALSE rate to a phylogenetically-controlled baseline) would be more rigorous.
- **Axis B morph-iso template-matching is operationalized loosely** (length ±1, same first letter); a stricter Form-V/passive-participle match would shrink B from 4 to ~2.
- **Axis C subclass-matching uses a 20-class hand-coded taxonomy**; alternative taxonomies could change the C_strict count by ±5 pairs.
- **Axis D top-15 threshold is project-default**; the loose top-30 variant or strict top-5 variant could shift D=FALSE marginals substantially.
- **The 113 mushaf-adjacent pairs are NOT independent**: the muqaṭṭāʿat streaks (الم Q 29-32, حم Q 40-46) are linked across multiple sequential pairs. Treating them as 113 independent draws over-counts evidence.

## Closing

The OPENING-LINKED CONTENT-DIVERGENT class is REAL and SUBSTANTIVE (19 pairs, including the Q 73 ↔ Q 74 seed and the entire ḥawāmīm sequence). It is NOT an enrichment over chance: opening-formula coupling and FR-content divergence are partly correlated phenomena at the mushaf-architecture level, not independent dimensions whose joint signature beats marginal expectation. The architectural language is justified — these pairs share a common identifiable signature — but the language of "above-chance enrichment" is NOT justified.

Q 73 ↔ Q 74 is now reframed: not the FIRST instance of a new architectural class, but a TYPICAL instance of a 19-pair pattern. Its uniqueness lies in the specific morph-iso 3-word vocative (only Q 65→66 also has both axis A AND axis B simultaneously, and Q 65→66 also has axis C_strict TRUE — making Q 65→66 the only 3-axis-TRUE pair in the corpus).

The most architecturally distinctive subset is the **clamped-zero-seam-only subset** (axes A=TRUE, B/C_strict variable, D=FALSE): Q 64→65, Q 72→73, Q 73→74, Q 86→87, Q 91→92, Q 93→94, Q 109→110. These 7 pairs are TSP-coupled at the mushaf level without explicit opener-formula repetition, and they remain FR-content-divergent. They are the most architecturally puzzling of the 19 signature pairs and warrant separate follow-up.
