---
id: H-NEW-44.2
title: al-Khalīl POA-closure test — do the 14 muqaṭṭaʿāt letters distribute non-randomly across classical place-of-articulation classes?
status: PRE-REGISTERED (decisions locked BEFORE running)
registered: 2026-04-15
spec_locked_at: 2026-04-15
parent_finding: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure.md
bonferroni_family: 2026-04-15-Fresh-Wave-3b
bonferroni_k: 8 (one per POA class — see §4)
alpha_family: 0.05
alpha_per_class: 0.00625 (= 0.05 / 8, two-sided not applicable; one-sided enrichment per class)
seed: 20260416
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json (universe of letters only — no corpus-frequency claims here)
---

# [[h-new-44-2-poa-closure|H-NEW-44.2]] — al-Khalīl Place-of-Articulation Closure Test

## 1. Fixed prior fact (carried over from [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] observed)

The 29 muqaṭṭaʿāt-opening surahs draw their disconnected letters from a closed universe of **exactly 14 letters**:

```
U_muq = {ا, ح, ر, س, ص, ط, ع, ق, ك, ل, م, ن, ه, ي}
```

This is exactly half the 28-letter Arabic alphabet:

```
A_28 = {ا, ب, ت, ث, ج, ح, خ, د, ذ, ر, ز, س, ش, ص, ض, ط, ظ, ع, غ, ف, ق, ك, ل, م, ن, ه, و, ي}
```

The fact "exactly 14 of 28" is universally agreed (al-Zarkashī, al-Suyūṭī, Nöldeke, Welch).

## 2. Question

Are the 14 letters in `U_muq` distributed across al-Khalīl's classical place-of-articulation (POA) classes uniformly, or do certain POA classes contain disproportionately MORE (or FEWER) muqaṭṭaʿāt letters than expected under uniform 14-of-28 random selection?

## 3. POA scheme — LOCKED BEFORE viewing letter-class assignments

### 3.1 Source and authority

The POA classification adopted is the standard 8-class scheme attributed to **al-Khalīl b. Aḥmad al-Farāhīdī** (*Kitāb al-ʿAyn*, ~790 CE, vol. 1 introduction, "Bāb al-makhārij") and canonized by **Sibawayh** (*al-Kitāb*, ed. ʿAbd al-Salām Hārūn, 1988, vol. 4, ch. 565 "Hādhā bāb ʿadad al-ḥurūf al-ʿArabiyya wa-makhārijihā wa-ṣifātihā"). This is the classification taught in standard Arabic phonetics references (Bakalla 1984; al-Nassir 1993 *Sibawayh the Phonologist*; Versteegh 1997 *Landmarks in Linguistic Thought III*).

The 8 classes are named by the articulating organ + locative suffix `-iyya`:

| # | Class name | Articulation | Letters (per Sibawayh / al-Khalīl) | Class size |
|---|---|---|---|---|
| C1 | ḥalqiyya (الحلقية) | throat / pharynx / larynx | ء ه ع ح غ خ | 6 |
| C2 | lahawiyya (اللهوية) | uvula | ق ك | 2 |
| C3 | shajariyya (الشجرية) | mid-tongue / palate | ج ش ض ي | 4 |
| C4 | asaliyya (الأسلية) | tongue-tip + sibilants | ص س ز | 3 |
| C5 | naṭʿiyya (النطعية) | alveolar / "palate-roof" stops | ط د ت | 3 |
| C6 | lithawiyya (اللثوية) | interdental / gum-line fricatives | ظ ذ ث | 3 |
| C7 | dhalqiyya (الذلقية) | tongue-tip sonorants + apical-labial | ر ل ن | 3 |
| C8 | shafawiyya (الشفوية) | labial | ف ب م و | 4 |

Total = 6+2+4+3+3+3+3+4 = **28**. Every letter is in exactly one class; covers the full 28-letter alphabet.

### 3.2 Variant-scheme considerations (LOCKED OUT)

al-Khalīl's introduction to *Kitāb al-ʿAyn* sometimes presents a **6-class** version (collapsing C2 lahawiyya into C1 ḥalqiyya as deep-back, and merging C7 dhalqiyya + C8 shafawiyya as "ḥurūf al-dhalq wa-l-shafa"). Sibawayh (and Ibn Jinnī, *Sirr al-Ṣināʿa*) split these into 8. Some modern handbooks (e.g. Owens 1990) reduce to 7 by collapsing C7+C8 only. **We pre-commit to the 8-class Sibawayh-canonized version.** No post-hoc collapse permitted.

### 3.3 The 14 letters in `U_muq` were NOT consulted in choosing this scheme

The scheme above was chosen for its canonical authority (Sibawayh = the most-cited Arabic phonological reference) and its match to the task statement. The choice was made BEFORE counting how many of `U_muq` fall into each class.

### 3.4 Hamza/alif policy (rules-tuple-conditional)

The letter `ا` ("alif") in `U_muq` is the orthographic alif (often written for the underlying hamza in opening "ا ل م"). In Sibawayh's POA scheme:
- `ء` (hamza) is in C1 ḥalqiyya.
- `ا` (alif madda, long /aː/) is the post-vocalic "soft alif" with no consonantal POA — sometimes assigned to C1 (laryngeal) by extension since it's the seat of the glottal stop, sometimes to "ḥurūf al-jawf" (cavity-vowel letters: ا و ي).

**Pre-committed rule.** For this test, the muqaṭṭaʿāt-opening "ا" is treated as **C1 ḥalqiyya** (Sibawayh treats alif-as-seat-of-hamza in the laryngeal class; this is the classical default when alif is functioning as a discrete letter and not as a long vowel). This is consistent with how `Kitāb al-ʿAyn` orders al-hamza/al-alif together at the back-most articulation. Sensitivity check: also re-run with `ا` assigned to a virtual "C0 jawf" (cavity) class — report both, but PRIMARY result uses `ا` ∈ C1.

## 4. Test — hypergeometric enrichment per POA class

Let:
- N = 28 (alphabet size)
- K = 14 (size of `U_muq`)
- For each class C_i with size c_i, let k_i = #{letters of `U_muq` in C_i}.

Under the null `H0: U_muq is a uniform random 14-element subset of the 28-letter alphabet`, the count k_i in class C_i of size c_i is hypergeometric:

```
k_i ~ Hypergeom(N=28, K=14, n=c_i)
```

with expected value E[k_i] = (14 × c_i) / 28 = c_i / 2 and pmf:

```
P(k_i = k) = C(c_i, k) × C(28 - c_i, 14 - k) / C(28, 14)
```

For each class, we compute:
- **Observed k_i**
- **Expected E[k_i] = c_i / 2**
- **Enrichment ratio** = k_i / E[k_i]
- **Two-sided p_i** = sum of P(k_i = k) over all k where P(k_i = k) ≤ P(k_i = observed) (the standard exact-test "double the smaller tail" or "method of small p" — we use the **doubled-smaller-tail** convention: `p = min(2 × min(P(K ≥ k_obs), P(K ≤ k_obs)), 1.0)`).

We also report one-sided `p_enrich = P(K ≥ k_obs)` and one-sided `p_deplete = P(K ≤ k_obs)`.

### Bonferroni

- `k_bonf = 8` (one test per POA class)
- `α_per_class = 0.05 / 8 = 0.00625`
- A class is declared "significantly over- or under-represented" iff its two-sided exact p < 0.00625.

### Aggregation — global goodness-of-fit

We additionally compute a single multinomial goodness-of-fit chi-square / exact multivariate-hypergeometric test:

```
χ² = Σ_i (k_i - E[k_i])² / E[k_i]
```

with df = 8 - 1 - 0 = 7 (no parameters fit; total N and K fixed). Under the null, χ² ~ approx. χ²₇. For the exact test, we Monte-Carlo simulate 100,000 uniform 14-of-28 samples (seed = 20260416) and compute the empirical p-value of observed χ² vs the null distribution. This is a SECOND test; it is also Bonferroni-counted (so the family expands to k_bonf = 9, α = 0.00556 — pre-committed).

**Re-locked Bonferroni.** k_bonf = 9, α_per_test = 0.05 / 9 = 0.005555... (Bonferroni TIGHTENING relative to the "8 classes" naive count is pre-locked.)

## 5. MW-5 positive control (planted-signal pipeline check)

Construct a synthetic universe `U_planted` of 14 letters drawn entirely from a single POA class plus padding from the smallest classes:

- `U_planted_v1` = take all 8 letters of {C1 ḥalqiyya ∪ C2 lahawiyya} (= 6 + 2 = 8) plus all 6 letters of C8 shafawiyya. But |C8| = 4, so we get 8+4 = 12, not 14. We pad with 2 letters from C7 dhalqiyya. Final: 14 letters concentrated in {C1, C2, C8, partial-C7}.

- Expected pipeline behavior: classes C1, C2, C8 should be significantly enriched at α = 0.005556 (very small p-values under hypergeometric); class C3, C5, C6 should be significantly **depleted** (k=0 in classes of size 3-4).

If the pipeline fails to detect this planted signal, the pipeline is broken → NULL-BROKEN verdict.

A second positive control (MW-5b) constructs `U_planted_v2` = uniform 14-of-28 random under seed 20260416-ALT (a different seed reserved for null demo). For this synthetic, we expect ~no class significant after Bonferroni (rate ≤ α_per_test = 0.005556 in expectation, for k_bonf = 9 tests this means P(any class significant) ≤ 0.05). If the pipeline reports significance >>0.05 of the time on uniform-random `U_planted_v2`, that's a Type-I-rate inflation → NULL-BROKEN.

## 6. Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| ≥1 class significant after Bonferroni AND multinomial χ² also significant after Bonferroni | STRONG-NON-UNIFORM — `U_muq` is biased across POA classes |
| Either ≥1 class OR multinomial χ² significant (but not both) | EXPLORATORY-hit — partial evidence of non-uniformity |
| Neither significant | NULL — `U_muq` is POA-class-uniform under hypergeometric null |
| Positive control fails | NULL-BROKEN — re-run required |

Each individual class is also reported with its enrichment direction (over / under / null) and its Bonferroni-corrected status, regardless of overall verdict.

## 7. Mechanism interpretation (pre-committed reading rules)

- **STRONG-NON-UNIFORM with C1 ḥalqiyya OR C2 lahawiyya enriched**: muqaṭṭaʿāt are biased toward back-of-mouth (throat / uvula) sounds — consistent with the recitative / esoteric "deep-throat opening" tradition (cf. al-Suyūṭī, *Itqān*, nawʿ 41 on the muqaṭṭaʿāt's recitative quality).
- **STRONG-NON-UNIFORM with C8 shafawiyya enriched**: muqaṭṭaʿāt are biased toward labial sounds (and `ا ل م` would be the marker, since `ا` is laryngeal but `ل ن ر م` are dhalqiyya/shafawiyya).
- **STRONG-NON-UNIFORM with depletion of fricative classes (C4/C5/C6)**: muqaṭṭaʿāt avoid sibilant/dental-fricative sounds — would be a phonetic-aesthetic preference.
- **NULL**: the 14-letter selection is POA-class-uniform under hypergeometric null; the muqaṭṭaʿāt's "exactly half" property is NOT POA-driven.

## 8. Garden-of-forking-paths log (pre-run)

Decisions made BEFORE viewing data:

1. POA scheme = Sibawayh's 8-class (NOT al-Khalīl's 6-class, NOT modern IPA). LOCKED.
2. Hamza/alif policy: `ا` ∈ C1 ḥalqiyya. LOCKED. (Sensitivity: also re-run with `ا` ∈ "C0 jawf" — reported but not primary.)
3. Bonferroni k_bonf = 9 (8 classes + 1 multinomial χ²). LOCKED.
4. Two-sided exact hypergeometric p-value via doubled-smaller-tail. LOCKED.
5. MW-5 positive control = `U_planted_v1` defined above. LOCKED.
6. MW-5b uniform-null Type-I check = `U_planted_v2` under seed 20260416-ALT (= 20260417). LOCKED.
7. Multinomial χ² Monte Carlo = 100,000 samples under seed 20260416. LOCKED.
8. NO post-hoc class merging permitted.
9. NO swap of POA scheme (e.g., to 6-class) post-results permitted.
10. Universe `A_28` = {ا, ب, ت, ث, ج, ح, خ, د, ذ, ر, ز, س, ش, ص, ض, ط, ظ, ع, غ, ف, ق, ك, ل, م, ن, ه, و, ي} (omits hamza ء as a separate letter — `ء` is treated as already-merged with `ا` in the orthographic 28-letter alphabet). This matches the standard Arabic orthographic alphabet (28 letters, alif first, yāʾ last). The phonological 29th letter `ء` is folded into `ا` for this test, consistent with the rules-tuple's "no-tashkeel orthographic" stance. LOCKED.

(Item 10 note: Sibawayh's phonological alphabet is 29 with hamza separate. The orthographic alphabet is 28 with alif representing the seat. Since the muqaṭṭaʿāt are written orthographically with `ا` and our rules-tuple is `orthographic-token`, the 28-letter orthographic alphabet is the natural universe. This locks the population N=28 unambiguously.)

## 9. Prior art / classical anchoring

- **al-Khalīl b. Aḥmad al-Farāhīdī**, *Kitāb al-ʿAyn*, ed. Mahdī al-Makhzūmī & Ibrāhīm al-Sāmarrāʾī, vol. 1, pp. 47–58 — POA classification (al-makhārij).
- **Sibawayh**, *al-Kitāb*, ed. ʿAbd al-Salām Muḥammad Hārūn, Cairo, 1988, vol. 4, ch. 565 — canonized 8-class POA scheme.
- **Ibn Jinnī**, *Sirr Ṣināʿat al-Iʿrāb*, ed. Ḥasan al-Hindāwī, Damascus 1985, vol. 1 — refines POA into 16 sub-makhārij; 8-class super-grouping retained.
- **Bakalla, M. H.** (1984) *Arabic Linguistics: An Introduction and Bibliography*, Mansell — modern reference on POA classification.
- **al-Nassir, A. A.** (1993) *Sibawayh the Phonologist*, Kegan Paul International — standard English-language reference.
- **No classical or modern source I can locate has tested whether the 14 muqaṭṭaʿāt letters distribute non-uniformly across POA classes.** This is the project's novel test on this axis.

## 10. Integrity commitment

- Publish ALL 8 per-class p-values (over/under/two-sided) regardless of significance.
- Publish the multinomial χ² result regardless of significance.
- Publish the MW-5 positive-control result.
- Publish the MW-5b Type-I rate result.
- If any decision (1)–(10) above is amended after viewing data, the amendment is logged in the findings file with reasoning AND the original verdict from the locked spec is also published.
- Seed 20260416 is fixed for both Monte Carlo (100K) and any randomness in the test.

## 11. Reproducibility

Script: `scripts/h_new_44_2_poa_closure.py`
JSON output: `findings/phase-b-hypotheses/csv/h-new-44-2.json`
Findings: `findings/phase-b-hypotheses/h-new-44-2-poa-closure.md`
Journal: `journal/h-new-44-2-run-1.md`

The test is fully analytic (closed-form hypergeometric) for the per-class tests; only the multinomial χ² uses Monte Carlo (100K, seed 20260416). Runtime expected < 30 seconds.
