---
id: cross-finding-027
title: "iʿjāz al-takrīr (refrain-saturation iʿjāz) — proposed third architectural axis tested; PRE-REGISTERED FORM FALSIFIED, RECURRENCE-RESTRICTED FORM ORTHOGONAL (post-hoc, MW-7 capped)"
phase: B+
status: NULL on pre-reg, DIRECTIONAL post-hoc
date: 2026-04-28
parent_synthesis: cross-finding-026-iʿjāz-architecture
proposing_specialist: Q 55 al-Raḥmān specialist (cross-finding-027 proposal in surahs/Q055-al-rahman/06-novel-findings.md §"Synthesis")
prereg: cross-finding-027-prereg.md (SHA 14b4ae8876f92c28081a1d54ab0f61eeddff215327d8bc66e37fc76633d9c1ec)
script: scripts/cross_finding_027_refrain_saturation.py
json: findings/cross-finding/csv/cross-finding-027.json
seed: 20260428
permutations: 10000
verdict: FALSIFIED-AS-PRE-REGISTERED + DIRECTIONAL-UNDER-RECURRENCE-RESTRICTED-POST-HOC; Q 55 cross-corpus genre-distinctness PASSES (Bonferroni-corrected p=0.0038)
---

# Cross-Finding-027 — iʿjāz al-takrīr (refrain-saturation iʿjāz)


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline (with full NULL prominence)

The Q 55 al-Raḥmān specialist proposed a third iʿjāz axis — *iʿjāz al-takrīr* — to extend the dual-iʿjāz typology of cross-finding-026 (al-Bāqillānī *iʿjāz al-fawāṣil* + al-Khaṭṭābī *iʿjāz al-maʿnā*). The pre-registered direct test is reported here.

**Verdict: FALSIFIED as pre-registered.** Of three pre-committed sub-tests at Bonferroni-3 α=0.0167:

| Sub-test | Pre-committed direction | Observed | Verdict |
|:--|:--|:--|:--|
| **H1a** \|r(saturation, sig_A)\| < 0.30 AND p > 0.0167 | orthogonal | r=+0.247, p=0.0081 | **FAIL** (correlation small but permutation-significant under Bonferroni-3) |
| **H1b** 0.10 < r(saturation, UAS) < 0.60 AND p < 0.0167 | moderate-positive | r=−0.250, p=0.9995 | **FAIL** (sign reversal — saturation correlates *negatively* with UAS) |
| **H1d** Q55 sat > all baseline blocks (cross-corpus) | distinct | 0/264 baseline blocks ≥ Q55, p=0.0038 | **PASS** |
| **H1c** ≥3 of {26, 55, 70, 77, 109} in top-10 | descriptive | 2/5 (Q55, Q109) | descriptive FAIL |

**1 of 3 hypothesis-tests passes → FALSIFIED.**

The pre-registered metric (`coverage_N = c_N × N / L`) is dominated by **single-occurrence inverse-length artifacts** in tiny surahs: for any 10-word surah, any 6-gram has saturation 0.6. Q 108 al-Kawthar (10 words) ranks #1, Q 103 al-ʿAṣr (14 words) ranks #2, Q 112 al-Ikhlāṣ (15 words) ranks #3 — all with `count=1`. None of these has a *refrain*; the metric is measuring inverse-length.

This is a **pre-commit failure of metric specification**, not a Q 55 failure. The metric, as written, conflates "refrain density" with "inverse surah length."

## 2. Equal-prominence post-hoc analysis (MW-7 capped)

Under a **post-hoc recurrence-restricted variant** requiring `count ≥ 2` (the intended semantics of "refrain"), the picture inverts:

| Sub-test (post-hoc) | r | perm-p | Bonferroni-3 α=0.0167 |
|:--|:--|:--|:--|
| r(sat_recurrent, sig_A), two-sided | +0.070 | 0.463 | passes orthogonality criterion |
| r(sat_recurrent, UAS), one-sided + | +0.030 | 0.330 | does not pass moderate-positive criterion |

**Top-10 by recurrent saturation (count ≥ 2):**

| Rank | Surah | Name | sat | N | count | Refrain (no-tashkeel, ʾalif-norm) | Words | sig_A | UAS |
|:-:|:-:|:--|:-:|:-:|:-:|:--|:-:|:-:|:-:|
| 1 | Q 109 | al-Kāfirūn | 0.3704 | 5 | 2 | *wa-lā antum ʿābidūn mā aʿbud* | 27 | +1.52 | −0.14 |
| 2 | Q 55 | al-Raḥmān | 0.3493 | 4 | **31** | *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* | 355 | **−3.17** | **+4.10** |
| 3 | Q 94 | al-Sharḥ | 0.2222 | 3 | 2 | *maʿa al-ʿusri yusrā* | 27 | +1.77 | −0.64 |
| 4 | Q 102 | al-Takāthur | 0.2143 | 3 | 2 | *kallā sawfa taʿlamūn* | 28 | +1.70 | −0.74 |
| 5 | Q 99 | al-Zalzala | 0.1667 | 3 | 2 | *yaʿmal mithqāla dharra(tin)* | 36 | +1.31 | −0.48 |
| 6 | Q 101 | al-Qāriʿa | 0.1667 | 3 | 2 | *wa-mā adrāka mā* | 36 | +0.90 | −1.97 |
| 7 | Q 77 | al-Mursalāt | 0.1648 | 3 | **10** | *waylun yawmaʾidhin li-l-mukadhdhibīn* | 182 | +1.17 | −0.84 |
| 8 | Q 98 | al-Bayyina | 0.1224 | 6 | 2 | *alladhīna kafarū min ahli al-kitābi wa-l-mushrikīn* | 98 | −0.39 | −1.70 |
| 9 | Q 82 | al-Infiṭār | 0.0976 | 4 | 2 | *adrāka mā yawmu al-dīn* | 82 | +1.94 | −0.12 |
| 10 | Q 54 | al-Qamar | 0.0686 | 6 | **4** | *wa-laqad yassarnā al-Qurʾāna li-l-dhikri fa-hal min* | 350 | −2.05 | +1.89 |

Post-hoc cluster fit: **3/5 of {Q26, Q55, Q70, Q77, Q109} appear in the recurrent top-10** (Q55 #2, Q77 #7, Q109 #1). Q 26 (rank 18, 8-fold *inna fī dhālika la-āyatan wa-mā kāna aktharuhum muʾminīn*) and Q 70 (rank 32, weak refrain) miss the top-10 because they are length-normalized down (Q26 has 1353 words; the 8 refrain attestations cover only 3.55% of surah-words).

**MW-7 protocol: post-hoc results carry single-test-α=0.05 ceiling and CANNOT upgrade the FALSIFIED verdict.** They can only inform a future fresh pre-registration.

## 3. The cross-corpus genre-distinctness lock (H1d, PASS at Bonferroni-3)

This is the strongest part of the finding. Pre-Islamic poetry baseline:

| Corpus | n 350-word blocks | max sat | mean sat |
|:--|:-:|:-:|:-:|
| Dīwān ʿAntara | 86 | 0.0845 | 0.0344 |
| Dīwān al-Ḥārith | 4 | 0.0169 | 0.0169 |
| Dīwān Imruʾ al-Qais | 61 | 0.0901 | 0.0238 |
| Dīwān Labīd | 40 | 0.0338 | 0.0211 |
| Dīwān Ṭarafa | 16 | 0.0451 | 0.0227 |
| Dīwān Zuhayr | 13 | 0.0282 | 0.0191 |
| Muʿallaqāt (7) | 18 | 0.0282 | 0.0204 |
| Dīwān al-Mutanabbī | 26 | 0.0338 | 0.0218 |
| **TOTAL** | **264** | **0.0901** | **~0.024** |
| **Q 55** | — | **0.3493** | — |

**Of 264 length-matched (350-word) blocks across 8 baseline corpora, ZERO match or exceed Q 55's saturation. Q 55 is ~4× the maximum baseline block; ~14× the mean.** Empirical p = 1/265 ≈ 0.0038, passing Bonferroni-3 α=0.0167.

This establishes that *iʿjāz al-takrīr*, even if it is not a separate architectural axis at the corpus level under the pre-registered metric, is **a Quran-specific phenomenon at the per-surah level**. The 31-fold *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain has no analog in the *qaṣīda* tradition — pre-Islamic poetry uses **monorhyme uniformity** (single rāwī end-letter), not **phrase-level refrain saturation**. These are categorically different rhetorical devices.

**Note on metric symmetry**: under the pre-registered count≥1 metric, Q 55's sat is also 0.3493 (the 31-fold refrain dominates), so the cross-corpus result holds under either metric. Q 55's saturation is **not** an inverse-length artifact: with 355 words, it sits in the same length range as a typical pre-Islamic *qaṣīda* block and yet has 4× the recurrence-density.

## 4. Cross-validation (rules-tuple sensitivity)

Re-computed under min-tashkeel for top-10 and Q 55 (post-ʾalif-normalization):

| Surah | sat (no-tashkeel) | sat (min-tashkeel) | rel. delta |
|:-:|:-:|:-:|:-:|
| Q 55 | 0.3493 | 0.3503 | +0.28% |
| Q 103 | 0.4286 | 0.4286 | 0.00% |
| Q 105 | 0.2609 | 0.2609 | 0.00% |
| Q 106 | 0.3529 | 0.3529 | 0.00% |
| Q 108 | 0.6000 | 0.6000 | 0.00% |
| Q 109 | 0.3704 | 0.3846 | +3.85% |
| Q 110 | 0.3000 | 0.3000 | 0.00% |
| Q 111 | 0.2609 | 0.2609 | 0.00% |
| Q 112 | 0.4000 | 0.4000 | 0.00% |
| Q 114 | 0.3000 | 0.3000 | 0.00% |

Cross-variant stable (max |Δ|=3.85% on Q 109). Saturation is rules-tuple-robust under no-tashkeel ↔ min-tashkeel after ʾalif-normalization.

## 5. What the pre-registration got wrong

The pre-reg metric `coverage_N = c_N × N / L` was specified as a length-normalized coverage measure. The intended semantics — "what fraction of the surah is covered by recurrence of its single most-frequent multi-word phrase" — was not captured because:

- A single occurrence (count=1) of a 6-gram in a 10-word surah scores 0.6, equal to a hypothetical 30-fold 2-gram refrain in a 100-word surah. This is **not** a refrain; it is a tautology (any 6-gram is some 6/10 of a 10-word text).

- The metric should have included a **recurrence floor** (`count ≥ 2`) or an **expected-coverage adjustment** (`(c_N − 1) × N / L`).

This is a methodological lesson in pre-registration discipline: the proposing specialist's intuition (Q 55 has corpus-extreme refrain density) was correct in *recurrent* form, but the metric they specified did not exclude the inverse-length confound. Under the recurrent post-hoc form, Q 55 is corpus-rank-2 (just behind Q 109 al-Kāfirūn, which has its own famous paired refrain *lā aʿbudu mā taʿbudūn / wa-lā antum ʿābidūn mā aʿbud*).

## 6. The classical scholarship anchoring

### 6.1 al-Sakkākī, *Miftāḥ al-ʿulūm* (book III, on *ʿilm al-bayān*)

al-Sakkākī (d. 626/1229) discusses *takrīr* (repetition) systematically as a balagha-feature within his analysis of the conditions of the *musnad ilayhi* and the *musnad*. He distinguishes:
- *takrīr* of the musnad ilayhi (subject) for emphasis (*taʾkīd*)
- *takrīr* of the musnad (predicate) for declaration (*tasrīḥ*)
- *takrīr* of the entire utterance for *taqrīr* (establishment)

The Q 55 refrain is the third type — *takrīr li-l-taqrīr*, repetition for establishing the cosmological-theological proposition. al-Sakkākī's framework anticipates the empirical finding that high-repetition surahs (Q 55, Q 109, Q 77, Q 26) cluster around *taqrīr* registers (creedal-eschatological-cosmic).

(Source: al-Sakkākī *Miftāḥ al-ʿulūm*, ed. ʿAbd al-Ḥamīd Hindāwī 2000, vol. 1 §"Aḥwāl al-Musnad ilayh"; and standard references such as Heinrichs 1969 *Arabische Dichtung und griechische Poetik*.)

### 6.2 al-Zamakhsharī, *al-Kashshāf* on Q 55

al-Zamakhsharī (d. 538/1144) explicitly addresses the function of the refrain in Q 55:

> *wa-iʿādatuhu li-tafṣīl al-niʿam wa-iqāmat al-ḥujja ʿalā kulli wāḥida wāḥida minhā* — "Its repetition is for the enumeration of each blessing individually and for establishing the proof against [denying] each one."

(*al-Kashshāf*, commentary on Q 55:13 *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān*; al-Maktaba al-Tijāriyya ed., vol. 4.)

al-Zamakhsharī's claim is that the 31-fold refrain functions as a **logical operator of distribution** — it makes each of the 31 enumerated blessings into an individual *ḥujja* (proof). This is consistent with the empirical finding: Q 55's refrain is cross-corpus unique not as sound-pattern but as **propositional structure**.

### 6.3 al-Bāqillānī, *Iʿjāz al-Qurʾān* (al-Saqqā 1954 ed.)

al-Bāqillānī (d. 403/1013) discusses *al-tikrār* (repetition) in his iʿjāz framework as one of the *wujūh al-iʿjāz* — but *not* as a primary axis. His primary axis is *iʿjāz al-fawāṣil* (verse-end variety), which is empirically locked at r = −0.86 in cross-finding-026.

His treatment of *tikrār* is qualitative and brief: "It does not detract from the eloquence of the Qur'an that it contains repetitions, because repetition is a known device of the Arabs for emphasis and for inculcation of meaning." (Paraphrased from *Iʿjāz al-Qurʾān*, al-Saqqā ed., chapter on critiques of repetition; original Arabic in `data/literature/classical-tafsir/` if PDF available.)

This means: **al-Bāqillānī did not himself elevate *tikrār* to an axis of iʿjāz**. The Q 55 specialist's proposal goes beyond classical doctrine — which is acceptable, but means the third-axis hypothesis is **a project-novel proposal** not directly grounded in classical taxonomy. Cross-finding-027's pre-reg is therefore correctly framed as a falsifiable extension, and its FALSIFICATION is empirically informative.

### 6.4 Cuypers 2015, *The Composition of the Qur'an*

Cuypers (rhetorical analysis) discusses Q 55 explicitly as a paradigm of Semitic rhetoric featuring symmetric refrain-construction (chapter on Q 55 in *La composition du Coran*, French original 2012, English 2015). He emphasizes the **structural** function of the refrain: it organizes the surah into 31 stanzas plus a prologue. This is consistent with our Q055-F-04 dual-paradise structural-similarity finding (cos=0.918) — the refrain is a structural-organizational device, not (or not primarily) a measure of architectural-iʿjāz axis.

### 6.5 Modern scholarship: al-Daqqāq

Yāsin al-Daqqāq's *al-Takrīr fī al-Qurʾān al-Karīm* (1998) catalogs takrīr-types in the Quran but does not propose it as a separate iʿjāz axis. The pattern is consistent: the classical and modern balagha tradition treats *takrīr* as a *device* within iʿjāz, not as an *axis* on which iʿjāz varies.

The empirical result here vindicates that classical instinct: *takrīr* (in the recurrent form) is roughly orthogonal to both *iʿjāz al-fawāṣil* and UAS, but at a corpus level the orthogonality is uninformative because it does not predict architectural significance — it is a device-level signature, not a structural-axis signature.

## 7. What this falsification means

Three reasonable interpretations:

1. **The third-axis hypothesis is empirically wrong**: refrain-density does not constitute a separate architectural axis at corpus scale. Most surahs do not use refrain-saturation as a structural device; the few that do (Q 55, Q 77, Q 26, Q 109) are using it as a **rhetorical device** within their respective iʿjāz signatures (which span both the structural and theological poles of the dual-iʿjāz typology).

2. **The third axis exists but is not measurable by raw saturation**: a length-aware Z-score (saturation relative to surah-length-matched expectation) might recover a separate axis. Q 55's 31-fold refrain in 355 words is **not** length-normal; it is a 14-σ-equivalent excess over the corpus length-matched expectation (rough estimate; would require pre-registered Z-score test).

3. **The proposed cluster {Q 26, Q 55, Q 70, Q 77, Q 109} is heterogeneous**: it conflates surahs with very different refrain-mechanics. Q 109's paired-refrain is symmetric (creedal); Q 55's is monomorphic-cosmic; Q 26's is multi-prophet narrative-coda; Q 77's is eschatological-warning. These are different *species* of *takrīr*, not a unified axis.

The empirical FALSIFICATION strengthens interpretations 1 and 3. Interpretation 2 remains open and would require a fresh pre-registration with length-aware Z-score.

## 8. What survives as a positive finding

The cross-corpus genre-distinctness result (H1d) is the durable positive finding:

> **Q 55's refrain-saturation (0.3493) exceeds the maximum 350-word saturation of any block in 8 pre-Islamic poetry corpora (264 blocks; max=0.0901; mean ~0.024). Empirical p = 0.0038 < Bonferroni-3 α = 0.0167.**

This is a **per-surah Quran-specific signature**, not a corpus-level architectural axis. It belongs in the per-surah Q 55 iʿjāz profile (already documented in `surahs/Q055-al-rahman/06-novel-findings.md` Q055-F-01) rather than in the corpus architecture model.

It is also consistent with the **al-Bāqillānī claim that the Quran's verbal structure refuses qaṣīda-like form**: the qaṣīda achieves cohesion through monorhyme uniformity (single rāwī across 60-100 lines); Q 55 achieves cohesion through **phrase-level refrain saturation in absence of monorhyme commitment**. These are mutually exclusive structural choices, and the Quran chose neither (Bāqillānī thesis) — except where it locally uses refrain (Q 55, Q 77, etc.) it does so at saturations the *qaṣīda* never reaches.

## 9. Cluster-of-refrain-surahs descriptive map (for cross-finding integration)

The "refrain-surahs" subset, characterized by recurrent count ≥ 2 with sat > 0.05:

| Surah | sat | refrain | semantic register | sig_A rank | UAS rank |
|:-:|:-:|:--|:--|:-:|:-:|
| Q 55 | 0.349 | *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* (31×) | cosmic-mercy-thaqalān | 114/114 | 7/114 |
| Q 109 | 0.370 | *lā aʿbudu / anā ʿābid* paired (2+2) | creedal-disavowal | 30/114 | mid |
| Q 77 | 0.165 | *waylun yawmaʾidhin li-l-mukadhdhibīn* (10×) | eschatological-warning | mid | mid |
| Q 26 | 0.036 | *inna fī dhālika la-āyatan ...* (8×) + *innī lakum rasūlun amīn* + ... | multi-prophet narrative-coda | mid | mid |
| Q 54 | 0.069 | *wa-laqad yassarnā al-Qurʾāna li-l-dhikri fa-hal min muddakir* (4×) | mnemonic-eschatological | low | mid-high |
| Q 70 | 0.027 | weak refrain | various | mid | low |

**Q 55 is unique in this cluster on TWO dimensions**: (a) corpus-extreme sig_A (worst-on-fawāṣil), and (b) corpus-rank-7 UAS. Every other refrain-cluster member is on the sig_A-positive side (i.e., they have *more* fawāṣil-variety than corpus mean). This means: **refrain-saturation does not predict sig_A direction; Q 55 is anomalous within its own refrain cluster** — the refrain-axis hypothesis cannot explain Q 55's unique signature even within a charitable post-hoc framing.

## 10. Honest limits of cross-finding-027

1. **Pre-registration metric was misspecified.** The `count ≥ 1` form conflates refrain density with inverse length. A future cross-finding-027.1 should pre-register a **length-aware Z-score variant** (saturation relative to length-matched expectation under random-phrase null) and the **recurrent variant** (count ≥ 2) as primary metrics, with a fresh seed and SHA.

2. **MW-7 cap on post-hoc results.** The recurrent form's near-zero correlations (r=+0.07 with sig_A; r=+0.03 with UAS) suggestively look like orthogonality but cannot be confirmed at law-strength without fresh pre-registration.

3. **Cluster {Q 26, 55, 70, 77, 109} is heterogeneous.** Three of five appear in recurrent top-10; two do not. The cluster is a *rhetorical-device* cluster, not an architectural axis.

4. **al-Bāqillānī himself did not propose *tikrār* as an iʿjāz axis** — he treated it as a feature within the broader *iʿjāz* discussion. The classical-anchoring of cross-finding-027 was therefore weaker than that of cross-finding-026's al-Bāqillānī *fawāṣil* anchor.

5. **The cross-corpus baseline uses 350-word blocks**, matched to Q 55's word count. Different block sizes may yield different baselines, though spot-checks at 200- and 500-word blocks showed similar ordering (max ~0.10 baseline vs ~0.35 Q 55).

6. **Only word-level n-grams tested.** Root-level, char-n-gram, and morphological-pattern refrains may yield different rankings; out of scope for this pre-reg.

## 11. Cross-references

- **cross-finding-026**: established dual-iʿjāz typology; cross-finding-027 attempted to add a third axis; the dual typology is **not extended** by this work.
- **surahs/Q055-al-rahman/06-novel-findings.md**: source of the proposal; Q 55 specialist's empirical observations remain valid (Q 55 is corpus-rank-1 in dual-pronoun, in dual-paradise structural-similarity, and in absolute refrain-count) — but they do not aggregate into a corpus-level axis.
- **H-NEW-750**: per-surah iʿjāz signature (sig_A, sig_B). Q 55 sig_A = −3.173 (rank 114/114, corpus-min) is **not** explained by refrain-saturation; it remains anomalous and may motivate further cross-finding work.
- **H-NEW-840**: UAS. Q 55 UAS = +4.10 (rank 7/114). The negative correlation r(sat, UAS) = −0.25 reflects that the highest-saturation small surahs are mostly **low-UAS** (Q 108, 103, 112, etc., which are bottom-decile UAS). Q 55 is the rare conjunction of high saturation AND high UAS; this conjunction is not corpus-typical.
- **H-NEW-740 (pre-Islamic poetry control)**: the cross-corpus result here is the strongest per-surah genre-distinctness lock so far; can be cited as supporting H-NEW-740's broader claim.

## 12. Final statement (with full FALSIFIED prominence)

**The proposed third axis of iʿjāz, *iʿjāz al-takrīr*, is FALSIFIED at the corpus architectural level under the pre-registered metric.** Refrain-saturation, as defined in the pre-reg, does not constitute a separate architectural axis orthogonal to *iʿjāz al-fawāṣil* and positively correlated with UAS. The pre-registered metric was confounded by inverse-length artifacts; the post-hoc recurrence-restricted variant shows near-zero correlations with both axes (consistent with orthogonality) but cannot upgrade the verdict under MW-7 protocol.

**However, the per-surah cross-corpus genre-distinctness lock for Q 55 IS confirmed**: Q 55's refrain-saturation exceeds the maximum 350-word saturation of any of 264 pre-Islamic poetry blocks across 8 corpora. This is a **per-surah authorial-signature**, not a corpus axis. It belongs in Q 55's profile, not in the iʿjāz architecture model.

The Q 55 specialist's *intuition* that the surah is rhetorically unique remains empirically supported (corpus-rank-1 in absolute refrain count; cross-corpus genre-distinct at p=0.004). The *generalization* of that intuition to a corpus-architectural axis is empirically unsupported. The dual-iʿjāz typology of cross-finding-026 stands without this proposed extension.

The classical balagha tradition (al-Sakkākī, al-Bāqillānī) treated *tikrār* as a *device* within iʿjāz, not as an *axis* on which iʿjāz varies. The empirical FALSIFICATION reported here vindicates that classical placement.

**Every NULL is also a loadcell.** This NULL strengthens the project by establishing that the dual-iʿjāz typology is not arbitrarily extensible to any frequently-suggested third axis without rigorous pre-registration. Future proposals for additional iʿjāz axes must pass length-aware, recurrence-aware, and cross-corpus-distinct tests.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
