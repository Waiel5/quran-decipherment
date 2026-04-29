---
date: 2026-04-13
analyst: meta-analyst
task: #126
status: live
inputs:
  - findings/phase-c-structures/h-meta-1-corpus-120.tsv (120-claim H-META-1 corpus)
  - findings/cross-finding/effect-size-inventory.tsv (158 row effect-size index)
  - findings/MASTER-FINDINGS-LEDGER.md (Tier-A/B/C verdicts + §4 refutations)
methodology:
  - Wilson 95% CI for binomial proportions (handles small-N + extreme p without pathology)
  - Per-scholar attribution from H-META-1 claim_source column; multi-attribution claims double-counted under each named scholar
  - "Convergence" defined per pair as: ≥2 named scholars predict the same phenomenon AND the prediction was tested as a single empirical target
  - Verdict mapping: CONFIRMED → C; REFUTED → R; PARTIAL/MIXED excluded from primary corpus
---

# Cross-scholar convergence tracker

For each classical and modern scholar cited as a project anchor: empirical hit rate (Wilson 95% CI), confirmed/refuted breakdown, multi-scholar convergence cases, and the shape of the per-scholar regime as it bears on the H-META-1 confirmable-signature classifier.

This is the meta-analyst counterpart to the H-META-1 corpus: H-META-1 asks "what *features* of a claim predict empirical confirmability?" — this tracker asks "what *people* are predictive, and is convergence between people informative beyond their individual track records?"

---

## 1. Per-scholar table (sorted by N descending)

Methodology note: a scholar gets credit for a claim if their work is the *named anchor* in the H-META-1 corpus claim_source. Claims attributed to "multi" with no named scholar (e.g., generic "classical tradition") are excluded from the per-scholar tally but counted in the §4 aggregate. Wilson 95% CI computed at z=1.96.

| Scholar | School / era | N | C | R | Confirmed rate | Wilson 95% CI |
|---|---|---:|---:|---:|---:|---|
| al-Suyūṭī | Shāfiʿī, classical-medieval | 8 | 6 | 2 | 0.75 | [0.41, 0.93] |
| al-Zarkashī | Shāfiʿī, classical-medieval | 7 | 6 | 1 | 0.86 | [0.49, 0.97] |
| al-Biqāʿī | Shāfiʿī, classical-medieval | 5 | 2 | 3 | 0.40 | [0.12, 0.77] |
| al-Kirmānī | Ashʿarī, classical-medieval | 3 | 2 | 1 | 0.67 | [0.21, 0.94] |
| al-Rāzī | Ashʿarī, classical-medieval | 3 | 2 | 1 | 0.67 | [0.21, 0.94] |
| al-Tirmidhī (ḥadīth) | classical-medieval | 3 | 3 | 0 | 1.00 | [0.44, 1.00] |
| Ibn Abī l-Iṣbaʿ | badīʿ, classical-medieval | 2 | 2 | 0 | 1.00 | [0.34, 1.00] |
| al-Dānī | qirāʾāt-Basran, classical-medieval | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| al-Jurjānī | Ashʿarī, classical-medieval | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| al-Bāqillānī | Ashʿarī, classical-medieval | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| al-Qurṭubī | Mālikī, classical-medieval | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| Abū Ḥayyān | Andalusian, classical-medieval | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| Ikhwān al-Ṣafāʾ | Ismāʿīlī, classical-medieval | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| Neuwirth/Wild | contemporary-academic, modern | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| Farrin | contemporary-academic, modern | 1 | 0 | 1 | 0.00 | [0.00, 0.79] |
| Cuypers | contemporary-academic, modern | 1 | 0 | 1 | 0.00 | [0.00, 0.79] |
| Khalifa | modern-numerology, modern | 1 | 0 | 1 | 0.00 | [0.00, 0.79] |
| al-Nursī | modern-apologetic, modern | 1 | 0 | 1 | 0.00 | [0.00, 0.79] |

**Key observation about CIs.** For all single-claim scholars (Wilson [0.21, 1.00] for C and [0.00, 0.79] for R), the per-scholar rate is *uninformative on its own*. They cannot be distinguished from each other or from the aggregate at any reasonable α. The aggregate trend (§4) is what carries the signal, not any individual single-claim row.

---

## 2. Mixed-directionality scholars (both confirmed and refuted entries)

These are the most diagnostic rows: a scholar whose claims partially confirm and partially refute lets us isolate *which kinds of claims* from that scholar are reliable.

### al-Biqāʿī (Naẓm al-Durar) — N=5, 2C / 3R, rate 0.40 [0.12, 0.77]

The most striking mixed pattern in the corpus. Local-scale claims pass; global-scale claims fail.

| Scope | Claim | Verdict |
|---|---|---|
| local seam | adjacent-surah munāsaba (LOCAL-SEAM Z=+10.06) | C-CL-18 CONFIRMED |
| local seam | chronology-free surah-adjacency recovery via T3 secondary | C-CL-41 CONFIRMED |
| whole-mushaf | macro-ring (Q1 ↔ Q114, Q2 ↔ Q113…) | R-CL-01 REFUTED (Z=−2.51 + Farrin z=−4.87) |
| whole-mushaf | last 9 surahs mirror first 9 | R-CL-04 REFUTED (z=−4.87) |
| inter-surah | munāsaba bayn al-suwar at gzip resolution | R-CL-11 REFUTED (p=0.87) |

**Pattern:** local pairwise = real; global symmetry = construction artifact. The 2/5 hit rate alone underrates al-Biqāʿī; the *conditional* hit rate is "100% on adjacency claims, 0% on macro-symmetry claims." This is a regime cut, not a calibration failure.

### al-Zarkashī (Burhān) — N=7, 6C / 1R, rate 0.86 [0.49, 0.97]

Highest confirmable-rate scholar by combined N+rate. Only one refutation:

| Claim | Verdict |
|---|---|
| iltifāt 6-type typology | C-CL-46 CONFIRMED (block framing z=−77) |
| sajʿ determinism in fawāṣil (nawʿ 52) | C-CL-11 CONFIRMED (RQA det z=+15.09) |
| al-maqṣūda li-ghayrihā fawāṣil mechanism (nawʿ 59) | C-CL-12 CONFIRMED (z=+10.61 p=7×10⁻²⁹) |
| al-Raḥmān = 57 occurrences | C-CL-02 CONFIRMED |
| Mūsā = 136 mentions (joint with al-Suyūṭī) | C-CL-23 CONFIRMED |
| muqāṭaʿat al-fawāṣil end-rhyme | C-CL-47 CONFIRMED |
| iltifāt catalog completeness | R-CL-07 REFUTED (under-inclusive by ~7×) |

**Pattern:** the iltifāt *typology* is right; the *catalog* is incomplete. The confirmable-vs-refuted split is *descriptive frame* (CONFIRMED) vs *enumerative completeness* (REFUTED). al-Zarkashī's frame-level work is project-survivable; his exhaustive lists are not.

### al-Suyūṭī (Itqān) — N=8, 6C / 2R, rate 0.75 [0.41, 0.93]

| Claim | Verdict |
|---|---|
| prophet-frequency table (Mūsā=136 etc.) | C-CL-01 CONFIRMED |
| 7 of 8 hapax claims exact | C-CL-03 CONFIRMED |
| fātiḥat al-sūra tadullu ʿalā khātimatihā | C-CL-16 CONFIRMED (p=8.9×10⁻¹¹) |
| takrār maʿa tanwīʿ (prophet-story variation) | C-CL-20 CONFIRMED |
| Mūsā = 136 mentions | C-CL-23 CONFIRMED |
| Muḥammad named 4 times | C-CL-31 CONFIRMED |
| istabraq as hapax | R-CL-06 REFUTED (occurs 4 times) |
| ḥusn al-ibtidāʾ/al-intihāʾ as 114-wide pattern | R-CL-12 REFUTED |

**Pattern:** structural-formal claims about counts (CONFIRMED), narrow generalizations to "all 114 surahs" (REFUTED). al-Suyūṭī's per-instance attestations work; his universal-quantifier extrapolations do not.

### al-Kirmānī — N=3, 2C / 1R, rate 0.67 [0.21, 0.94]

| Claim | Verdict |
|---|---|
| ~1,100 mutashābih pairs catalog | C-CL-04 CONFIRMED (detector at 1,085) |
| intra-Quranic cross-referential pairs | C-CL-39 CONFIRMED (H-NEW-18 replication) |
| mutashābih pair *directionality* | R-CL-13 REFUTED |

**Pattern:** the *existence* of mutashābih pairs is real; the *direction* of derivation (which member is "primary") is a post-hoc projection. This is the same enumerative-vs-interpretive cut as al-Zarkashī.

### al-Rāzī — N=3, 2C / 1R, rate 0.67 [0.21, 0.94]

| Claim | Verdict |
|---|---|
| 14 of 28 muqaṭṭaʿāt = half alphabet | C-CL-10 CONFIRMED |
| linear naẓm within-surah | C-CL-19 CONFIRMED (Z=+30.76; length-residualized +9.57) |
| muqaṭṭaʿāt = divine-names abbreviation | R-CL-08 REFUTED (0/78 survive shuffle) |

**Pattern:** observational claims survive; symbolic-interpretive claims fail. Same regime cut.

---

## 3. Cross-scholar convergence cases

A "convergence case" is one where ≥2 named scholars predicted the same phenomenon and the prediction was tested as a single empirical target. The question: does convergence boost confirmability above the per-scholar baseline?

### Convergence-CONFIRMED (multi-scholar predictions that survived audit)

| Phenomenon | Scholars | Tested as | Verdict |
|---|---|---|---|
| Mūsā = 136 mentions | al-Suyūṭī + al-Zarkashī (joint, C-CL-23) | prophet-frequency anchor | CONFIRMED |
| Local pairwise munāsaba | al-Biqāʿī (Naẓm) + Cuypers (modern attempt at semantic adjacency) | LOCAL-SEAM Z test | CONFIRMED at adjacent scale; REFUTED at macro scale (Cuypers' inferred macro extension fails) |
| Ism al-Aʿẓam in Khawātim al-Ḥashr / Q 3:2 / Q 112:2 | al-Tirmidhī + al-Qurṭubī + classical tradition | composite hypergeometric | CONFIRMED p=3.92×10⁻²⁰ (9 of 11 ḥadīth candidates in top-32) |
| Muqaṭṭaʿāt as Meccan-core | Abū Ḥayyān + classical consensus | surah-class test | CONFIRMED (with disclosed Medinan exceptions) |
| Mutashābih pair existence | al-Kirmānī + classical tafsir | detector cross-validation | CONFIRMED 1,085 ≈ 1,100 |

### Convergence-REFUTED (multi-scholar predictions that failed jointly)

| Phenomenon | Scholars | Tested as | Verdict |
|---|---|---|---|
| Whole-mushaf ring composition | al-Biqāʿī + Farrin + Cuypers | Q-k ↔ Q-(115-k) symmetry | REFUTED (z=−4.87, multiple independent baselines) |
| Mod-19 verse-final abjad clustering | Khalifa + downstream modern numerology lane | H-NEW-34 | REFUTED (6 of 6 sub-tests null; reverse-direction signal exploratory only) |
| Word-count symmetry universalism | al-Nursī + Al-Kaheel | broad word-count parity | REFUTED |

### Convergence non-effect

The most interesting finding here: **convergence does NOT systematically boost the per-scholar baseline**. Macro-ring claims converge across al-Biqāʿī, Farrin, and Cuypers — and *fail more decisively* than any single-scholar prediction would predict. The convergence tracks the *aesthetic* (large-scale symmetry intuitions) rather than the *empirical reality*.

This is consistent with H-META-1: the predictor is *substance type*, not *number of authorities*. A claim that is structural-formal and modest in scope confirms; a claim that is global-symmetry-numerical fails — and this holds *regardless* of how many scholars endorsed it.

**Concrete metric:** of the 5 convergence-CONFIRMED rows, all 5 are local/specific. Of the 3 convergence-REFUTED rows, all 3 are global/universal. This is a 5/5 vs 0/3 split on the local-vs-global dimension. Per Fisher exact, p ≈ 0.018 (small N caveat).

---

## 4. Aggregate verdicts by era / regime

This is the headline number that feeds into queue item #5 (classical-modern reliability ratio CI refinement).

### Classical-medieval named scholars (excluding modern lane)

- N = 38 named claims with verdicts (across 14 named scholars)
- Confirmed: 30
- Refuted: 8
- Rate: **0.789, Wilson 95% CI [0.637, 0.889]**

### Modern lane (post-1900 numerology + apologetic + structural-modern)

Note: "modern" here means modern-numerology + modern-apologetic + the two modern structuralists (Farrin, Cuypers) whose macro-ring proposals were tested and refuted. Neuwirth/Wild are listed separately in §1 because their kitāb-Medinan/qurʾān-Meccan finding *survived* — they are the contemporary-academic exception.

- N = 4 named claims (Farrin, Cuypers, Khalifa, al-Nursī) — only counts named-anchor claims
- Confirmed: 0
- Refuted: 4
- Rate: **0.000, Wilson 95% CI [0.000, 0.490]**

### Modern lane (broader, includes anonymous-modern + corpus rows)

If we include the unnamed modern-numerology refutations from H-META-1 (R-PR-04 through R-PR-18 = 15 rows: rahma=114, Yūsuf-sjn-12, 147-triple, Al-Kaheel pair symmetries, Fibonacci, golden-ratio, Pascal's, perfect-numbers, Hassab-Elnaby c, Al-Kawthar Catalan, embryology, Big Bang, fingerprints, atom, milk-digestion):

- Named-anchor modern (4) + unnamed modern (15) = 19 modern-lane refutations
- Plus Neuwirth/Wild (1 named-anchor modern CONFIRMED)
- N = 20, C = 1, R = 19
- Rate: **0.050, Wilson 95% CI [0.009, 0.236]**

### Classical-vs-modern reliability ratio

Point estimate: 0.789 / 0.050 = **15.8×** (broader modern denominator)
Point estimate: 0.789 / 0.000 = **undefined** (named-modern only; floor at 0)

Using the upper modern CI 0.236 as a conservative ceiling:
0.789 / 0.236 = **3.34×** (lower bound on ratio)

Using the lower classical CI 0.637 as a conservative floor:
0.637 / 0.236 = **2.70×** (most conservative defensible ratio)

The previously-circulated "~7×" figure sits comfortably inside this CI envelope. The **defensible point estimate is ~10-16× with conservative lower bound ~2.7×.** Queue item #5 will refine this with bootstrap CIs that respect the dependence structure.

**Caveat (and it's load-bearing):** the corpus is selected. Project tests were chosen partly *because* certain classical claims were credible-looking. The 0.789 classical rate is therefore an *upper bound* on the realistic confirmability of arbitrary classical claims; it specifically reflects the rate among *project-selected, named-author* claims. The modern rate is similarly upper-bounded but in the *opposite* direction — modern numerology was selected partly to demonstrate refutability. The true population ratio is somewhere inside this envelope, but the inventory cannot pin it without an independent random sample of unselected classical and modern claims (which would be a §5 follow-up project).

---

## 5. Per-school regime view

| School | N | C | R | Rate | CI |
|---|---:|---:|---:|---:|---|
| Shāfiʿī (al-Suyūṭī + al-Zarkashī + al-Biqāʿī) | 20 | 14 | 6 | 0.70 | [0.48, 0.85] |
| Ashʿarī (al-Kirmānī + al-Rāzī + al-Jurjānī + al-Bāqillānī) | 8 | 6 | 2 | 0.75 | [0.41, 0.93] |
| Mālikī / Andalusian / Basran (al-Qurṭubī + Abū Ḥayyān + al-Dānī) | 3 | 3 | 0 | 1.00 | [0.44, 1.00] |
| Ismāʿīlī (Ikhwān al-Ṣafāʾ) | 1 | 1 | 0 | 1.00 | [0.21, 1.00] |
| Modern lane (named only) | 4 | 0 | 4 | 0.00 | [0.00, 0.49] |

The Shāfiʿī and Ashʿarī CIs overlap heavily; no school-level discrimination is supported by current N. The signal lives in the *era* dimension, not the *school* dimension. This is consistent with H-META-1's finding that broad_hisab_claim and substance_type are the discriminating features — both era-correlated (modern lane is hisab-heavy), neither school-correlated.

---

## 6. Single-claim-only scholars: should they be down-weighted?

Eight of the named scholars have N=1. Their CIs are wide enough to be uninformative individually. Two options for how to use them:

1. **Treat each as one observation in the aggregate.** Adopted here (§4). Pros: no down-weighting; all evidence enters at face value. Cons: a single fluke can move a scholar from 0% to 100%.
2. **Bayesian shrinkage to the era prior.** Shrink each single-claim scholar toward 0.789 (classical aggregate) for classical, 0.05 (broad modern aggregate) for modern. Pros: handles small-N pathology. Cons: requires committing to the aggregate as a prior, which is partly what we are trying to estimate.

Neither approach changes the §4 verdict, because the §4 calculation uses the raw counts (option 1) and the aggregate CI is not driven by any single small-N outlier — al-Suyūṭī and al-Zarkashī alone (N=15 combined, 12 C / 3 R) give 0.80 [0.55, 0.93], essentially identical to the all-classical rate.

---

## 7. Findings flagged for downstream tasks

1. **Convergence is not a reliability multiplier** — flag for integrator: when a claim is endorsed by multiple scholars, do not treat that as independent evidence. The 5/5 vs 0/3 local-vs-global split (§3) suggests convergence tracks the *aesthetic* rather than the *empirical* axis. Recommend integrator add a footnote to any future "X scholars converge on Y" framing.

2. **al-Biqāʿī regime cut is the cleanest data point in the corpus** — local-scale CONFIRMED, global-scale REFUTED, same author. This is the strongest single-author evidence that "scope" is the discriminating axis. Recommend H-CLASSIC-44 (al-Zarkashī inter-surah munāsaba, currently pending task #95) consider an explicit local-vs-distant cut in its design — if munāsaba decays with canonical distance, the al-Biqāʿī regime cut is reproduced and confirmed.

3. **Wilson-CI conservatism** — the modern-lane rate of 0.05 [0.009, 0.236] has an upper bound (0.236) that is *higher* than typical readers expect. Flag: when reporting "modern numerology fails," include the CI; the failure is overwhelming but not unbounded.

4. **Reliability-ratio refinement (queue item #5)** — the 2.7×–16× envelope reported here is loose; queue item #5 should bootstrap this with the dependence structure (claims-tested-against-the-same-corpus are not independent samples) and report a tightened CI. Expected tightening: probably 4×–12× after bootstrap.

5. **al-Dānī = N=1 verbatim-VERIFIED CONFIRMED** — flag for MW-6 and integrator: al-Dānī is the single most-citation-verified anchor in the corpus (Bayān, ed. Ḥamad p.78). His one claim confirmed cleanly, supporting the verbatim-verification protocol's value but also illustrating that high citation confidence and small N can co-exist. Do not collapse al-Dānī into the aggregate without acknowledging the verbatim distinction.

---

## 8. Limits

- N = 38 named-classical claims; some scholars at N=1. Per-scholar discrimination is severely limited.
- Selection bias: project tests were chosen because some classical claims looked credible. The 0.789 classical rate is a *project-conditional* upper bound, not a population rate.
- "Convergence" is operationalized loosely — for some convergence cases (e.g., Ism al-Aʿẓam) the convergence is across genres (ḥadīth + tafsir + kalām) rather than across schools, and the multi-scholar status is partly a function of which claims got promoted to the corpus in the first place. A more rigorous convergence operationalization would predefine the multi-scholar threshold; this tracker is exploratory on that axis.
- "Modern lane" includes both numerology (Khalifa, Al-Kaheel) and academic-modern (Farrin, Cuypers, Neuwirth/Wild). Lumping these is conservative for the ratio but obscures the academic-modern subset, which contains the one-and-only contemporary-academic CONFIRMED row (Neuwirth/Wild kitāb-qurʾān shift). Disaggregation in queue item #5.
- Wilson CI assumes independence of trials. Project tests are not fully independent (shared corpus, shared baselines, shared tester). True CIs are wider.

---

## 9. Pointer to next deliverable

Queue item #5 (next): `findings/cross-finding/classical-modern-reliability-ratio.md` — bootstrap-CI refinement of the 2.7×–16× ratio reported in §4, with separate tracks for (a) named-classical vs named-modern, (b) named-classical vs all-modern (broad), (c) Shāfiʿī vs other school cuts. Will use this tracker as the input frequency table and the 120-claim H-META-1 corpus as the underlying data.

The convergence non-effect (§3) is the most novel observation in this tracker and will be cross-referenced from queue item #5 as a constraint on the bootstrap procedure: convergence cases must NOT be treated as independent observations.
