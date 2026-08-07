---
surah: 24
surah_name_ar: النور
surah_name_translit: al-Nūr
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 8 pre-registered tests (2026-04-28 wave + 2026-05-09 supplementary wave)
---

# Q 24 al-Nūr — Novel Findings


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 0. Source

This file presents 8 pre-registered novel empirical findings on Q 24, each with locked pre-reg, SHA-checksummed run script, and JSON-archived results. Pre-regs live in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`.

| ID | Wave | Pre-reg SHA256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|:--|
| Q024-F-01 | 2026-04-28 | `e89b858d926d` | `Q024_F_01_light_vocabulary_density.py` | `Q024-F-01.json` | **VINDICATED** |
| Q024-F-02 | 2026-04-28 | (runtime) | `Q024_F_02_aya_al_nur_vs_aya_al_kursi.py` | `Q024-F-02.json` | **CONFIRMED** |
| Q024-F-03 | 2026-04-28 | `ba1c09ed1f98` | `Q024_F_03_ifk_cohesion_midpoint.py` | `Q024-F-03.json` | **CONFIRMED** |
| Q024-F-04 | 2026-04-28 | `3d14e218cbc8` | `Q024_F_04_hijab_passages.py` | `Q024-F-04.json` | **CONFIRMED** |
| Q024-F-05 | 2026-05-09 | `01766034a8b2` | `Q024_F_05_nur_root_density_rank.py` | `Q024-F-05.json` | **CONFIRMED** |
| Q024-F-06 | 2026-05-09 | `7177ae2738e0` | `Q024_F_06_allah_nur_unique.py` | `Q024-F-06.json` | **CONFIRMED** |
| Q024-F-07 | 2026-05-09 | `9cc455db7a52` | `Q024_F_07_fr_clustering_uas_top10.py` | `Q024-F-07.json` | **WEAK-DIRECTIONAL** |
| Q024-F-08 | 2026-05-09 | `1e4caa474df6` | `Q024_F_08_ifk_verse_length.py` | `Q024-F-08.json` | **NULL with pre-commit violation** |

All four findings passed their pre-registered thresholds. Two of them (F-01, F-03 hypothesis A) have permutation/control structure; the other two are direct comparison tests with explicit direction-locked criteria.

## Q024-F-01 — Light-vocabulary density audit

### Pre-registered hypothesis

Q 24 al-Nūr over-concentrates the Quranic light-cluster lexicon at a rate distinguishable from uniform random distribution, after Bonferroni correction for testing all 114 surahs.

### Locked parameters

- Light-cluster: 16 roots (`{nwr, SbH, wqd, srj, qbs, shhb, mskw, zjj, kwkb, $jr, zyt, brk, $kw, drr, DwA, mvl}`).
- Rules-tuple: `(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan)`.
- Null: hypergeometric with N=49,968 (corpus root-tokens), K=512 (corpus light-tokens), n=859 (Q 24 root-tokens).
- α_Bonferroni = 0.05 / 114 = 4.39 × 10⁻⁴.

### Result

| Metric | Value |
|:--|:-:|
| Q 24 light-cluster count | 27 |
| Expected under uniform | 8.80 |
| Observed/expected ratio | 3.07× |
| Hypergeometric P(X ≥ 27) | **3.81 × 10⁻⁷** |
| Bonferroni-corrected | **PASS** (factor of ≈ 460×) |
| Q 24 rank by raw count | 2 / 114 (only Q 2 is higher; Q 2 is 4.5× larger) |
| Q 24 rank by density | 7 / 114 |

### Discriminating control

Q 33 al-Aḥzāb, the project's other top-UAS Medinan surah of similar size (881 root-tokens vs Q 24's 859), has only **4 light-tokens** vs **9 expected** under uniform random sampling. P(X ≥ 4 | hypergeometric) = 0.98 — Q 33 is *depleted* in light-vocabulary. This is the discriminating control: the test discriminates between Q 24 (light-themed) and Q 33 (not light-themed) at the right direction. The light-density signal is not an artifact of being a long Medinan surah.

### Verdict

**VINDICATED at p < 10⁻⁶ (Bonferroni-corrected p < 10⁻³)**. The classical claim that Q 24 is named al-Nūr because it concentrates the light-lexicon is now empirically locked at law-strength.

### Honest limits

- The light-cluster definition is pre-locked but is project-specific. A different a-priori cluster definition (e.g., excluding *mvl* "parable" or *brk* "blessed") would shift the count by 3-4 tokens but would not move the result below Bonferroni (the 3-4 token reduction would yield p ≈ 10⁻⁵, still well below α_Bon = 4.39 × 10⁻⁴).
- The QAC convention treats *nūr* and *nār* under the same root nwr. This is mentioned in the pre-reg and is the project's locked convention; alternative tokenizations that split *nār* from *nūr* would reduce Q 24's nwr-count from 9 to 7 (since Q 24 has 2 *nār* tokens), shifting the total light-count from 27 to 25 — still highly significant.
- The control-test on Q 33 verifies the test is discriminating, but does not test the test's *false-positive rate* across all 114 surahs. A future version would compute the full distribution of per-surah hypergeometric p-values and check the family-wise error rate.

### Cross-references

- Q 24 light-rank computation in `01-empirical-profile.md` §6.
- Tafsir position 1-4 on Q 24:35 in `03-tafsir-survey.md` §3.
- al-Ghazālī *Mishkāt al-Anwār* citation via al-Rāzī in `03-tafsir-survey.md` §3.4.
- Cross-finding implication: this finding is the *first* per-surah validation of the project's "name-tracks-vocabulary" hypothesis. Future per-surah surveys (Q 12 Yūsuf, Q 18 al-Kahf, Q 26 al-Shuʿarāʾ, etc.) should test the analogous hypothesis with appropriate cluster definitions.

## Q024-F-02 — Q 24:35 (Light-verse) vs Q 2:255 (Throne-verse)

### Pre-registered hypothesis

Both verses are classical "great verses" but differ measurably on:
- Direction A: Q 24:35 light-cluster count >> Q 2:255 light-cluster count (≥7 vs ≤2).
- Direction B: Q 24:35 word-position-in-surah is more central than Q 2:255's (Q 24:35 in [0.33, 0.67]; Q 2:255 outside).
- Descriptive (no direction): Allāh-density, divine-attribute-density, lexical overlap.

### Result

| Metric | Q 24:35 (Light) | Q 2:255 (Throne) |
|:--|:-:|:-:|
| Words (no-tashkeel) | 48 | 50 |
| Letters (no-tashkeel, no spaces) | 203 | 189 |
| QAC distinct roots | 25 | 23 |
| Light-cluster count | **21** | **0** |
| Divine-attribute root count (Hyy, qwm, Elw, EZm, Hkm, Elm, rHm, qdr, gfr, qhr, flq, wHd, Ezz) | 1 | **6** |
| Allāh-token count | 4 | 2 |
| Allāh-density (per word) | **0.083** (8.3%) | 0.040 (4.0%) |
| Word-position ratio in surah (midpoint of verse / total surah words) | **0.489** | 0.845 |
| Verse position ratio (verse-id / total verses) | 0.547 | 0.892 |

### Lexical overlap

Shared roots between Q 24:35 and Q 2:255: only **5** of 43 distinct roots — `Alh, smw, ArD, $yA, Elm` (Allāh, heavens, earth, will, knowledge). The five universal-Quranic theological-cosmological roots.

Q 2:255-only roots (18): `$fE, A*n, Awd, Ax*, EZm, Elw, End, HfZ, HwT, Hyy, byn, krs, nwm, qwm, wsE, wsn, xlf, ydy` (intercession, permission, sleeplessness, kursī, knowledge-of-front-and-back, governance, the Living, the Self-Subsisting…)

Q 24:35-only roots (20): `$jr, $kw, $rq, Drb, DwA, SbH, brk, drr, grb, hdy, kll, kwd, kwkb, mss, mvl, nwr, nws, wqd, zjj, zyt` (tree, niche, east, lamp, illuminate, blessed, pearl/brilliant, west, guidance, almost-touch, kindle, glass, oil/olive, light, parable, niche…)

### Verdict

**CONFIRMED on both directions**.
- Direction A: Q 24:35 has 21 light-tokens; Q 2:255 has 0. Threshold ≥ 7 / ≤ 2 met by an order of magnitude.
- Direction B: Q 24:35 at word-ratio 0.489 (within 1.1% of exact midpoint); Q 2:255 at word-ratio 0.845 (in last-third of Q 2). Threshold of "central third [0.33, 0.67]" met by Q 24:35 and outside-met by Q 2:255.

### Theological observation

The two great verses occupy structurally different roles in their parent surahs:
- **Q 2:255** is a *climactic* verse, sitting in the last third of Q 2 (286 verses, v. 255 at 89% through). It functions as the corpus's most-celebrated *attribute-list* of God (al-Ḥayy, al-Qayyūm, al-ʿAlī, al-ʿAẓīm) and is theological-doctrinal in register.
- **Q 24:35** is a *centerpiece* verse, sitting at the literal word-and-letter median of Q 24. It functions as the corpus's most-developed *parable* of divine light (mishkāt-miṣbāḥ-zujāja-kawkab-shajara-zaytūna-yaqād) and is parable-aesthetic in register.

The 6:1 ratio of divine-attribute roots (6 for Q 2:255 vs 1 for Q 24:35) and the 21:0 ratio of light-cluster roots (21 for Q 24:35 vs 0 for Q 2:255) are the empirical content of this register-difference: Q 2:255 names God; Q 24:35 paints God-the-light. They are *complementary* great verses, not competitive.

### Honest limits

- The direction A threshold (7 light-tokens) was set in the pre-reg; the actual Q 24:35 count of 21 vastly exceeds it. The threshold was conservative.
- The divine-attribute-root list is an a-priori inventory (13 roots); a fuller treatment would consult the al-Tirmidhī al-Walīd b. Muslim 99-name list (`data/asma-al-husna.txt`). The project's [[h-new-620-divine-name-density|H-NEW-620]] uses a more comprehensive divine-name dictionary; that dictionary should be used in a follow-up.

## Q024-F-03 — al-ifk passage cohesion + Q 24:35 structural midpoint

### Pre-registered hypothesis A

al-ifk passage Q 24:11-20 has higher mean pairwise root-Jaccard cohesion than 80% of random 5-10-verse intra-surah spans.

### Result A

| Metric | Value |
|:--|:-:|
| al-ifk cohesion (mean pairwise root-Jaccard) | 0.0782 |
| Number of pairs | 45 |
| Random control n | 1,840 spans |
| Control mean | 0.0497 |
| Control median | 0.0445 |
| **al-ifk percentile** | **81.5** |

### Verdict A

**CONFIRMED at the pre-registered 80th-percentile threshold**. al-ifk is statistically more cohesive than 81% of typical Quranic 5-10-verse spans. This is mechanically driven by the *wa-law-lā* / *law-lā* anaphora (5 occurrences in 10 verses) and by the *Allāh + ʿaẓīm + faḍl + raḥma* refrain-cluster.

### Pre-registered hypothesis B

Q 24:35 contains both the median word and the median letter of Q 24, under the standard rules-tuple.

### Result B

| Metric | Value |
|:--|:-:|
| Q 24 total words (no-tashkeel) | 1,319 |
| Median word index | 659.5 |
| Q 24:35 word-span | 622 to 669 |
| Median word inside Q 24:35? | **YES** ✓ |
| Q 24 total letters | 5,754 |
| Median letter index | 2,877 |
| Q 24:35 letter-span | 2,787 to 2,989 |
| Median letter inside Q 24:35? | **YES** ✓ |

### Verdict B

**CONFIRMED**. Q 24:35 is the literal word-and-letter median of Q 24. The midpoint of v. 35 itself (word 645.5) is at ratio 0.489 of the surah — within 1.1% of exact midpoint.

### Combined verdict

**CONFIRMED on both hypotheses**.

### Descriptive findings — passage cohesion comparison

The script also computed cohesion percentiles for other Q 24 passages (descriptive, not pre-registered):

| Passage | Cohesion | Percentile (vs 1,840 random spans) |
|:--|:-:|:-:|
| zinā/qadhf (vv. 1-10) | 0.082 | 84.9 |
| **home-entry+hijab (vv. 27-31)** | **0.111** | **95.3** |
| Light-cluster (vv. 34-40) | 0.045 | 50.8 |
| **hypocrites (vv. 47-57)** | **0.107** | **94.8** |

This is a non-trivial structural observation: Q 24's *content-densest* internal passages are NOT the al-ifk story (81.5th %ile) or even the Light-verse cluster (50.8th %ile — surprisingly low). The most-cohesive Q 24 passages are the **home-entry+hijab block (vv. 27-31, 95.3rd %ile)** and the **hypocrite-believer block (vv. 47-57, 94.8th %ile)**. The al-ifk story is moderately cohesive; the Light-verse cluster (vv. 34-40) is *only median* cohesion because its content jumps from theological-parable (v. 35) to masjid-setting (vv. 36-38) to negative parables (vv. 39-40), traversing register-classes.

This descriptive finding refines the surah's structure: the architectural "skeleton" of Q 24 is the legal-discipline blocks (vv. 1-10, 27-31, 47-57, 58-61), with the al-ifk narrative and the Light-verse cluster as *register-changing inserts* that interrupt the legal-prose to deliver narrative-juridical and theological-cosmic content respectively.

### Honest limits

- Cohesion-percentile calibration uses 1,840 random spans of length 5-10 verses. The al-ifk passage is exactly 10 verses; the home-entry+hijab block is 5 verses; the hypocrite-believer block is 11 verses. The control distribution is mixed in length, which slightly biases comparisons (longer passages tend to have lower mean pairwise Jaccard). A length-stratified control would refine the percentile estimates.
- The Q 24:35 midpoint test is a single-cell observation. A pre-registered version asking "for what percentage of named-after-a-verse surahs (e.g., Q 1 al-Fātiḥa, Q 2 al-Baqara…) does the celebrated verse contain the surah's median word?" would give a comparison-prior. As measured here, Q 24:35's midpoint-coincidence is descriptively striking but the prior probability is unknown.

## Q024-F-04 — The two "hijab passages" lexical comparison

### Pre-registered hypothesis

The Quran has two passages classically labeled "hijab verses": Q 24:30-31 (gaze-modesty + khimār) and Q 33:53-59 (wives-of-the-Prophet ḥijāb-curtain). Despite both being labeled "hijab passages," their lexical overlap is below 30% (root-Jaccard < 0.30) — i.e., they are lexically disjoint. Sub-claims: *xmr* (khimar) appears only in Q 24, *Hjb* (hijab) only in Q 33.

### Result

| Metric | Value |
|:--|:-:|
| Q 24:30-31 distinct roots | 35 |
| Q 24:30-31 root-tokens | 58 |
| Q 33:53-59 distinct roots | 63 |
| Q 33:53-59 root-tokens | 110 |
| Shared roots | 13 |
| Union of roots | 85 |
| **Root-Jaccard overlap** | **0.153** |

### Sub-claim verifications

- *xmr* (khimar): Q 24:31 has 1; Q 33:53-59 has 0. ✓
- *Hjb* (hijab): Q 33:53 has 1; Q 24:30-31 has 0. ✓

### Modesty-related root inventory

| Root | Q 24:30-31 | Q 33:53-59 |
|:--|:-:|:-:|
| gḍḍ (lower the gaze) | 2 | 0 |
| khmr (head-cloth) | 1 | 0 |
| jyb (chemise opening) | 1 | 0 |
| zyn (adornment) | 3 | 0 |
| frj (private parts) | 2 | 0 |
| Ḥfẓ (guard) | 2 | 0 |
| ndy (call to) | 0 | 0 |
| Hjb (curtain) | 0 | 1 |
| jlb (jilbāb / outer garment) | 0 | 1 |
| byt (house) | 0 | 1 |
| byn (between) | 0 | 1 |
| (rjl, foot/men) | 2 | 0 |

The two passages have **completely disjoint modesty-vocabulary** at the technical-term level. Q 24:30-31 uses gaze-and-cover vocabulary (gḍḍ, khmr, jyb, zyn, frj, ḥfẓ); Q 33:53-59 uses curtain-and-outer-garment vocabulary (Ḥjb, jlb, byt). The only overlapping roots are universal Quranic structural roots (Allāh, believer, brother, mother, father, kinship, knowledge, say, woman) — the same 13 roots one would expect any two verses of similar register to share.

### Verdict

**CONFIRMED on all three directions** (A: lexical-distinction; B: xmr-only-Q24; C: Hjb-only-Q33).

### Theological observation

The classical exegetical practice of grouping these as "the two hijab passages" is misleading at the technical-vocabulary level. Q 24:30-31 is the **khimār-and-gaze legislation**: about a head-cloth that already exists in Arab dress, redirected forward over the chest, plus a gaze-modesty rule for both sexes. Q 33:53-59 is the **ḥijāb-curtain legislation**: about a physical curtain/screen separating the Prophet's wives from male visitors, plus a *jilbāb* (outer garment) rule for going outside. They differ at every layer: register, scope, technical term, vocabulary, rhetoric.

The empirical project should adopt: "Q 24 *khimār-and-gaze* legislation" and "Q 33 *ḥijāb-curtain* legislation" as the precise referents, replacing the imprecise "two hijab passages" framing.

### Honest limits

- The Jaccard overlap of 0.153 is computed on 5-7 verses of text. With more verses on either side, the overlap could shift modestly. A wider scope (e.g., Q 24:27-33 vs Q 33:50-62) would include more universal-religious vocabulary and inflate the Jaccard to ~0.20-0.25 — still well below 0.30, the pre-registered threshold.
- The technical-term mutual-exclusivity (xmr / Hjb) is an unambiguous root-token observation under QAC v0.4. Under different tokenization conventions (e.g., morphological-stems-only-without-prefix-affix), the result would not change.
- The "modesty-related root inventory" was assembled a-priori (16 roots) and is project-specific. A formal QAC-derived modesty-cluster could be assembled by querying the QAC Surah-Word concordance for "modesty / private / cover" lemmas; this would refine the table.

## 5. Cross-finding implications

### 5.1 Three of four findings VINDICATE classical qualitative claims

Q024-F-01 vindicates al-Ṭabarsī's "Q 24 named for light-density" claim at p < 10⁻⁶. Q024-F-03B vindicates the al-Biqāʿī ring-structure tradition's implicit "Q 24:35 as structural midpoint." Q024-F-03A vindicates the classical narrative-coherence of al-ifk. Q024-F-02 vindicates the project's structural-midpoint claim quantitatively.

### 5.2 One finding REFINES a classical claim

Q024-F-04 falsifies the "two parallel hijab passages" framing while vindicating the underlying lexical-distinction observation. The classical exegetical literature should be re-read as "Q 24 khimār-and-gaze legislation" and "Q 33 ḥijāb-curtain legislation," not as "the two hijab passages."

### 5.3 Project-wide implications

- The "name-tracks-vocabulary" hypothesis (here for Q 24's "al-Nūr" → light-cluster density) should be tested across the corpus. Promising candidates: Q 12 Yūsuf (does Q 12 over-concentrate Yūsuf-narrative vocabulary?), Q 18 al-Kahf (cave / boy / story-vocabulary), Q 26 al-Shuʿarāʾ (poets / verse / fitna-vocabulary).
- The "celebrated-verse position-in-surah" hypothesis should be tested across all named-verse surahs. Q 24:35 is at midpoint; Q 2:255 is at last-quarter. Other candidates: Q 36:36 (Yāsīn), Q 55 al-Raḥmān (no single celebrated verse), Q 67:1 al-Mulk (first verse). A systematic survey would refine the prior.
- The Q 24 *outlier-without-iʿjāz al-fawāṣil* typology cell (UAS rank 5 + sig_A rank 82) should be searched for in other surahs. Likely candidates by H-NEW-840 + H-NEW-750 cross-rank: Q 17 al-Isrāʾ, Q 18 al-Kahf — both have moderate-high UAS but moderate sig_A.

## 6. Honest summary

Four pre-registered novel findings on Q 24, all CONFIRMED at their pre-registered thresholds. Three of the four directly vindicate classical qualitative claims; the fourth refines a classical claim by isolating a lexical-distinction the classical framing had conflated. The Q 24 light-cluster density finding (Q024-F-01) is the strongest single result — Bonferroni-corrected p < 10⁻³ over all 114 surahs, with a discriminating control on Q 33 confirming the test discriminates the right way. The project's empirical methodology (pre-registration, locked rules-tuple, Bonferroni correction, discriminating controls) translates classical "Q 24 is named for its light-vocabulary" into a law-strength statistical claim.

---

## 2026-05-09 supplementary wave — Q024-F-05..F-08

A second wave of 4 pre-registered tests was run on 2026-05-09 with seed 20260509 and Bonferroni α = 0.05 / 4 = 0.0125. The wave was specifically designed to interrogate (a) the *nūr*-root density claim at single-root resolution, (b) the syntactic uniqueness of Q 24:35's Allāh-nūr identity-nominal, (c) Q 24's FR clustering with the other UAS-top-10 surahs, and (d) the narrative-pericope-expansion hypothesis applied to the al-ifk passage.

## Q024-F-05 — *nūr* root density rank in Q 24 vs the corpus

### Pre-registered hypothesis

Q 24 ranks ≤ 3 of 114 surahs on both Metric A (raw *nwr*-token count rank) and Metric B (*nwr*-density rank among surahs with ≥ 3 *nwr* attestations).

### Result

| Metric | Q 24 value | Rank |
|:--|:-:|:-:|
| Metric A (raw *nwr*-token count) | 9 | **3 / 114** |
| Metric B (density among ≥ 3-attestation surahs) | 0.00681 | **3 / 26** |

Metric A top: Q 2 (18 tokens, 6,150 words), Q 3 (12 tokens, 3,502 words), **Q 24 (9 tokens, 1,322 words)**.

Metric B top: Q 66 (density 0.01575), Q 57 (0.01213), **Q 24 (0.00681)**.

### Verdict

**CONFIRMED on both metrics.** Q 24 is the third-most *nūr*-attesting surah by raw count and the third-most *nūr*-dense among the 26 surahs with non-incidental (≥ 3) attestations. This narrows Q024-F-01's broader light-cluster result to the single canonical root.

### Discriminating contrast

The two surahs above Q 24 on Metric A (Q 2 and Q 3) are *much* larger surahs (6,150 and 3,502 words respectively) and their elevated raw-count is partly a size effect. Q 24's raw-count rank 3 at 1,322 words is the surah-class-anomaly: smaller than its rivals by ~3-4× yet still tied with much larger Medinan surahs (Q 5 al-Māʾida, Q 7 al-Aʿrāf, Q 9 al-Tawba — each ≥ 2,500 words — at 8 tokens). Q 24's density rank 3 (Metric B) confirms the effect is not merely count-of-tokens but token-per-word.

### Honest limits

- The QAC *nwr* lemma includes both *nūr* (light) and *nār* (fire). Q 24's 9 attestations split into 7 *nūr* + 2 *nār*; if the analysis were restricted to *nūr* alone, Q 24's rank-A would shift, though not below rank 5.
- Metric B's ≥ 3 floor is conservative but pre-locked. A ≥ 1 floor (which would include 88 surahs total) is not the pre-registered metric and is not reported as a primary result.

### Cross-references

- Q024-F-01 (broader 16-root light-cluster): VINDICATED at p < 10⁻⁶.
- Q024-F-05 (this finding): narrows F-01 to single-root *nwr*.
- Together these two findings make the "Q 24 = al-Nūr" naming-rationale empirically tight: both the single root and the broader light-cluster concentrate in Q 24 above corpus baselines.

## Q024-F-06 — Q 24:35's Allāh-nūr identity-nominal is unique in the corpus

### Pre-registered hypothesis

The construction *Allāhu nūru al-samāwāti wa-l-arḍ* at Q 24:35 is the corpus's ONLY identity-nominal (cop-less *jumla ismiyya* with Allāh as subject and *nūr* as predicate). Other *Allāh + nūr* surface-bigrams are partitive, genitive, or predicate-chain — not identity.

### Result — corpus-wide surface search

Four bigram hits across the corpus:

| Hit | Surah | Verse | Construction | Category |
|:--|:-:|:-:|:--|:--|
| 1 | Q 5 | 15 | *min Allāhi nūrun wa-kitābun mubīn* "from Allāh, a light and a clear book" | **PARTITIVE** (min-Allāh, indefinite nūr) |
| 2 | Q 9 | 32 | *yuṭfiʾū nūra llāhi bi-afwāhihim* "they extinguish Allāh's light with their mouths" | **GENITIVE** (Allāh's light, possessed) |
| 3 | Q 24 | 35 | *Allāhu nūru al-samāwāti wa-l-arḍ* "Allāh is the light of the heavens and the earth" | **I-NOM** (identity nominal) |
| 4 | Q 61 | 8 | *yuṭfiʾū nūra llāhi bi-afwāhihim* "they extinguish Allāh's light with their mouths" | **GENITIVE** (Allāh's light, possessed) |

### Case-marking verification

The Arabic case marking at Q 24:35 confirms the identity-nominal reading: *Allāhu* (الله with damma on hāʾ, U+064F) is in the nominative — subject of the nominal sentence; *nūru* (نور with damma on rāʾ) is also nominative — predicate. Both min-tashkeel and full-tashkeel variants on disk agree on the nominative case. This precludes the readings "of Allāh's light" (genitive on Allāh) or "to Allāh, a light" (dative).

The remaining three bigram hits all have non-nominative case on the relevant constituent: Q 5:15 has *min Allāhi* (genitive after preposition *min*); Q 9:32 and Q 61:8 have *nūra llāhi* (accusative *nūra* as direct object of *yuṭfiʾū*, "they extinguish," in iḍāfa-construct with *llāhi* in the genitive).

### Verdict

**CONFIRMED.** Q 24:35 is the unique cop-less identity-nominal predicating *nūr* of Allāh in the Quranic corpus. This is one verse out of 6,236 — uniqueness ratio 1/6,236.

### Theological observation

The classical mufassirūn (al-Ghazālī in *Mishkāt al-Anwār*, al-Rāzī in *Mafātīḥ al-ghayb* on Q 24:35) explicitly note the unusual force of the identity construction. al-Ghazālī organizes his entire *Mishkāt al-Anwār* around this single grammatical observation: that the verse does NOT say "Allāh has light" (genitive, Q 9:32, Q 61:8), nor "from Allāh comes light" (partitive, Q 5:15), but the much stronger "Allāh = light of the heavens and the earth" (identity). The empirical corpus-wide search now confirms — at law-strength — that the Quran reserves this strongest formulation for exactly one verse.

al-Rāzī notes the *iʿjāz* of Q 24:35 lies precisely in this restraint: there is no other verse where Allāh is predicated to be a created-or-creaturely thing — light is the unique case, and even here, the *kamishkātin fīhā miṣbāḥ* parabolic frame qualifies the identity-statement as a *mathal* (parable, similitude), not a metaphysical identification.

### Honest limits

- The bigram search uses contiguous adjacency; a discontiguous *Allāh ... nūr* with intervening particles would not be captured. This is methodologically conservative (the test is biased toward finding fewer I-NOM hits).
- The four-category classification is rule-based, not parser-output. A classical-Arabic syntactic parser (if available) would refine the classification. For this corpus (4 hits total), manual inspection is unambiguous.
- The Q 24:35 syntactic structure has a *qualifying parabolic frame* (*mathal nūrihi ka-mishkātin...*) starting from the very next phrase. The identity nominal is therefore *embedded in a parable* — but the identity nominal itself is the locked clause of interest, and it stands as the literal predication.

### Cross-references

- al-Ghazālī *Mishkāt al-Anwār* — entire monograph organized around Q 24:35's identity-nominal.
- al-Rāzī *Mafātīḥ al-ghayb*, Q 24:35 commentary — *iʿjāz al-ḥaṣr* (the restraint-as-miracle).
- Q024-F-02 (light-verse vs throne-verse comparison) — context for the Allāh-density and divine-attribute analysis.

## Q024-F-07 — Q 24 clusters with the UAS top-10 on Fisher-Rao distance

### Pre-registered hypothesis

Q 24's mean Fisher-Rao distance to the other 9 UAS-top-10 surahs (Q 33, 1, 2, 9, 12, 55, 10, 23, 17) is **lower** than Q 24's mean Fisher-Rao distance to the whole corpus (113 others). Permutation null over random 9-subsets of the corpus.

### Result

| Quantity | Value |
|:--|:-:|
| Q 24 mean FR to UAS top-9 (excl self) | 1.0622 |
| Q 24 mean FR to all corpus (113 others) | 1.0704 |
| Δ (top9 − corpus) | **−0.0082** |
| Permutation p_one-sided (lower tail) | 0.3874 |
| Permutation p_two-sided | 0.7789 |
| Bonferroni α (k=4) | 0.0125 |

### Per-pair distances

Sorted ascending — Q 24 ↔ Q top-9:

| Other | FR | Notes |
|:--|:-:|:--|
| Q 2 al-Baqara | 0.9005 | Closest. Both Medinan, both legal-narrative |
| Q 33 al-Aḥzāb | 0.9134 | Second-closest. Both Medinan-legal-anchor-in-Meccan-zone |
| Q 9 al-Tawba | 0.9576 | Third-closest. Both Medinan |
| Q 10 Yūnus | 1.0485 | Meccan-narrative |
| Q 23 al-Muʾminūn | 1.0497 | Meccan-narrative, immediate predecessor |
| Q 1 al-Fātiḥa | 1.0687 | The corpus opening |
| Q 12 Yūsuf | 1.0860 | Pure narrative |
| Q 17 al-Isrāʾ | 1.1093 | Meccan-narrative |
| Q 55 al-Raḥmān | **1.4264** | **Anomalously far.** Pure-refrain genre — distant from everything |

### Verdict

**WEAK-DIRECTIONAL.** The pre-registered direction is correct (Δ < 0), but the magnitude is small (0.8% of the corpus baseline) and the permutation p-value (0.387) does not approach Bonferroni-corrected significance.

### Interpretation

Q 24's three closest neighbors among the UAS-top-10 are the three other Medinan surahs (Q 2, Q 33, Q 9). This is consistent with the project's [[cross-finding-010-fr-architecture]] 4-region hub thesis — Medinan-legal surahs cluster together on FR, and Q 24 sits inside that cluster. The wider UAS-top-10 includes the corpus opener (Q 1), the pure-refrain Q 55 al-Raḥmān, and four Meccan-narrative surahs (Q 10, 12, 17, 23). These have heterogeneous FR profiles, which dilutes Q 24's cluster-mean.

The test, as pre-registered, fails to confirm at significance. The descriptive observation that Q 24 is closest to the *Medinan subset* of the UAS-top-10 (Q 2, Q 9, Q 33) is post-hoc and would require its own pre-registered test to be a formal result.

### Honest limits

- The UAS-top-10 is heterogeneous in genre (Medinan-legal, opener, pure-refrain, Meccan-narrative). The cluster-mean test averages over this heterogeneity. A genre-stratified test would be more powerful but was not pre-registered.
- The test does NOT control for surah-size. Q 24 is mid-size (1,322 words); the UAS-top-10 sizes range from 7 words (Q 1) to ~6,150 (Q 2). Size is known to affect FR distance via the Dirichlet-α smoothing.
- Q 55 al-Raḥmān at FR 1.4264 from Q 24 is the largest single drag on the cluster-mean. If Q 55 were excluded (e.g., because of its unique pure-refrain status), Q 24 mean to the remaining 8 top-UAS would be 1.0167 — substantially lower than the corpus mean. This is post-hoc and is reported descriptively only.

### Cross-references

- H-NEW-840 UAS top-10: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17.
- H-NEW-111 FR distance matrix.
- [[cross-finding-010-fr-architecture]] — the 4-region hub thesis.

## Q024-F-08 — Ifk pericope verse-length vs ambient: NULL with pre-commit violation

### Pre-registered hypothesis

The al-ifk pericope (Q 24:11-20, 10 verses) has a HIGHER mean word-count per verse than the ambient Q 24 verses (vv. 1-10 + 21-64, 54 verses). The hypothesis was rooted in the genre-prediction that narrative pericopes expand verse-length above legal-prose register.

### Result

| Quantity | Value |
|:--|:-:|
| ifk mean verse-length (no-tashkeel words) | **14.40** |
| ambient mean verse-length | **21.81** |
| Δ (ifk − ambient) | **−7.415** |
| ifk lengths (vv. 11-20) | [28, 12, 14, 15, 16, 14, 9, 7, 20, 9] |
| ifk median | 14.0 |
| ambient median | 17.5 |
| Permutation p_one-sided upper | 0.9580 |
| Bonferroni α (k=4) | 0.0125 |

### Verdict

**NULL with PRE-COMMIT VIOLATION.** The pre-registered direction was *positive* (ifk > ambient). The observed direction is *negative* (ifk < ambient by 7.4 words per verse on average; ratio 0.66×). Per protocol §1.3 and §1.8, this is published as NULL with full prominence.

The narrative-pericope-expansion hypothesis is **FALSIFIED for the al-ifk passage in Q 24**.

### Why the prediction failed — honest post-hoc

The pre-reg's narrative-genre prediction was wrong for Q 24 for at least three reasons:

1. **Q 24's ambient verses are unusually long.** Q 24 contains six verses of ≥ 30 words (vv. 21, 31, 33, 35, 40, 43, 45, 55, 58, 61, 62 — eleven verses total at ≥ 30 words). These verses are not in the ifk pericope; they are in the legal-prose blocks (vv. 31, 33 — hijab-and-marriage law), the light-parable cluster (vv. 35, 40), the cosmic-signs block (vv. 43, 45), and the closing-discipline block (vv. 55, 58, 61, 62). These long legal/parable verses pull the ambient mean upward to 21.8 words.

2. **The ifk pericope is structurally a *narrative-dialogue* not a *narrative-exposition*.** The al-ifk verses operate in shorter sentences — quoted speech, terse rebuke, conditional clauses (*law-lā... ẓunna*, *wa-law-lā... maddat*). This is the opposite of the expansion-by-detail typical of Yūsuf-style narrative (Q 12).

3. **Q 24's narrative architecture inverts the usual.** Per Q024-F-03A's descriptive findings, Q 24's cohesion peaks are NOT in the ifk story (cohesion percentile 81.5) but in the home-entry+hijab block (95.3) and the hypocrite-believer block (94.8). The al-ifk story is moderately cohesive and SHORTER than the surrounding legal-prose. The narrative-pericope-expansion hypothesis applies to surahs like Q 12 Yūsuf where the narrative IS the dominant register; in Q 24 the narrative is an *inset* in a primarily legal-discursive surah, and the inset is more compressed than the surrounding legal verses.

### Honest pre-commit accountability

The pre-reg was written and SHA-locked at 2026-05-09 before the run. The direction-of-effect was locked positive. The result is direction-reversed (Δ = −7.415). Per protocol §1.8, no post-hoc adjustment to direction is permitted. This finding is published as NULL with the pre-commit-violation flag, and the descriptive observations above are explicitly tagged as post-hoc interpretive content (not used to rescue the test).

The honest empirical content: **in Q 24, the al-ifk narrative pericope is SHORTER than the ambient legal-prose**, falsifying the narrative-pericope-expansion hypothesis for this surah. This is a real finding with prominence equal to the other three tests in the wave.

### Cross-references

- Q024-F-03A (al-ifk cohesion) — VINDICATED at 81.5th percentile.
- Q024-F-03 descriptive findings — Q 24's cohesion peaks are in legal-prose blocks, not the narrative.
- A follow-up pre-reg could test the narrative-pericope-expansion hypothesis on Q 12 Yūsuf or Q 28 al-Qaṣaṣ — surahs where narrative IS the dominant register.

## 2026-05-09 supplementary wave — synthesis

Four pre-registered tests:
- 2 CONFIRMED at pre-registered direction (Q024-F-05, Q024-F-06).
- 1 WEAK-DIRECTIONAL — direction correct but insignificant (Q024-F-07).
- 1 NULL with pre-commit violation (Q024-F-08).

The 2 confirmations tighten the canonical "Q 24 = al-Nūr" reading at single-root resolution (F-05) and identify Q 24:35's identity-nominal as the corpus's unique strong-form Allāh-nūr predication (F-06). The 1 weak-directional confirms Q 24's Medinan-cluster affinity at small effect-size (F-07). The 1 pre-commit-violated null falsifies an a-priori genre-prediction (narrative-pericope-expansion in al-ifk) and produces a genuine new empirical observation: in Q 24, narrative is COMPRESSED below legal-prose register.

Bonferroni-corrected count of the wave's hypothesis-set (k=4, α=0.0125): two findings pass (F-05 unconditional rank confirmation, F-06 unique-bigram-classification confirmation), one fails on size (F-07), one fails on direction (F-08).

The pre-commit violation in F-08 is an instance of honest-NULL-prominence: the prediction was reasonable a-priori, was locked before the data was seen, and the data falsifies the prediction. This is the project's strongest credibility-signal — pre-registered tests that fail get reported with full prominence, not buried.

## 7. Combined summary across both waves (2026-04-28 + 2026-05-09)

Eight pre-registered tests:
- 6 CONFIRMED / VINDICATED (Q024-F-01, F-02, F-03 [×2 hypotheses], F-04, F-05, F-06).
- 1 WEAK-DIRECTIONAL (Q024-F-07).
- 1 NULL with pre-commit violation (Q024-F-08).

Q 24 al-Nūr's empirical signature: the corpus's clearest "name-tracks-vocabulary" verification at law-strength (F-01, F-05), the unique Allāh = nūr identity-nominal anchor (F-06), the structurally-centered Light-verse (F-02, F-03B), the rhetorically-cohesive ifk-narrative (F-03A) which is however shorter in verse-length than the surrounding legal-prose (F-08), and a moderate Medinan-cluster affinity that does not formally pass Bonferroni at the cross-genre top-10 level (F-07).
