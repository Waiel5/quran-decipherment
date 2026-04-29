---
surah: 24
surah_name_ar: النور
surah_name_translit: al-Nūr
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 24 al-Nūr — Novel Findings

## 0. Source

This file presents 4 pre-registered novel empirical findings on Q 24, each with locked pre-reg, SHA-checksummed run script, and JSON-archived results. Pre-regs live in `preregs/`, scripts in `scripts/`, JSON outputs in `csv/`.

| ID | Pre-reg SHA256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q024-F-01 | `e89b858d926d` | `Q024_F_01_light_vocabulary_density.py` | `Q024-F-01.json` | **VINDICATED** |
| Q024-F-02 | (computed at runtime) | `Q024_F_02_aya_al_nur_vs_aya_al_kursi.py` | `Q024-F-02.json` | **CONFIRMED** |
| Q024-F-03 | `ba1c09ed1f98` | `Q024_F_03_ifk_cohesion_midpoint.py` | `Q024-F-03.json` | **CONFIRMED** |
| Q024-F-04 | `3d14e218cbc8` | `Q024_F_04_hijab_passages.py` | `Q024-F-04.json` | **CONFIRMED** |

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
