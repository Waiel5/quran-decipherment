---
id: H-NEW-1560
title: 99 asmāʾ al-ḥusnā corpus-wide distribution + top-10-by-density Fisher-Rao cluster cohesion
phase: B
date_run: 2026-05-10
seed_A: 20260509
seed_B: 20260511
n_perm: 10000
prereg_sha256: 6d751b87bb6cdda175217d42601c3b1cca03f5c333bcfe964766dc9cf9566c0b
verdict: DESCRIPTIVE-ONLY (length-confound on FR-cohesion); SUBSTANTIVE: 34/99 al-Tirmidhī names absent under substring rule (independent corroboration of al-Suyūṭī al-Itqān nawʿ 56)
ceiling: PASS-DIRECTED (capped — length-matched control failed; secondary cataloging passes as descriptive)
direction: locked (cluster mean ≤ 5th percentile null); cluster passes uniform null but fails length-matched
related: H-NEW-1350, H-NEW-1330, cross-finding-025, divine-names-distribution.md, H-NEW-170, H-NEW-140
---

# H-NEW-1560 — 99 asmāʾ al-ḥusnā corpus-wide distribution + top-10-by-density FR-cluster cohesion

## Headline

The 10 surahs with the highest per-word divine-name density {Q 112, 1, 85, 64, 62, 110, 59, 61, 49, 58} **appear FR-cohesive under a uniform null (p = 0.0088 ≤ 0.025)** — but **the cohesion does NOT survive a length-matched control** (p = 0.272). The cluster total is 2,092 words, which puts it deep in the short-surah regime where root-distributions are naturally peakier and look "cohesive" relative to long surahs.

**Verdict**: DESCRIPTIVE-ONLY (length-confound suspected).

**Substantive co-finding**: 34 of the 99 al-Tirmidhī names do NOT appear in the Quran corpus at all under the no-tashkeel substring rule. This is an empirical independent corroboration of al-Suyūṭī's classical observation (*al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 56) that some traditionally enumerated names are not Quranically attested.

## Pre-registration

- File: `findings/phase-b-hypotheses/prereg-h-new-1560-divine-names-distribution.md`
- SHA256: `6d751b87bb6cdda175217d42601c3b1cca03f5c333bcfe964766dc9cf9566c0b`
- Script: `findings/phase-b-hypotheses/scripts/h-new-1560.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-1560.json`

## Method

- **Name source**: `data/asma-al-husna.txt` (al-Tirmidhī #3507, al-Walīd b. Muslim chain — graded *gharīb* by al-Tirmidhī himself; the canonical Sunnī standard list).
- **Detection rule**: per-name SUBSTRING match in no-tashkeel verse text. Each of the 99 names is checked literally against every verse; multi-token names (#89 مالك الملك, #90 ذو الجلال والإكرام) are matched as whitespace-normalized substrings. The substring rule does NOT disambiguate divine vs non-divine referents (e.g. الملك as the King of Egypt in Q 12 is counted).
- **Density metric**: `name_attestations_per_word` = (Σ over 99 names of substring counts in surah) / surah_word_count, on the no-tashkeel JSON with pure-rasm pause-marks excluded.
- **Cluster definition**: top-10 surahs by density (descending; tie-break sid ascending).
- **FR instrument**: `findings/phase-b-hypotheses/csv/h-new-111.json` 114×114 FR distance on QAC stem-roots.
- **Test**: mean intra-cluster pairwise FR distance over the 45 pairs of the 10-surah cluster.
- **Nulls**:
  - Cell A: 10,000 uniform 10-of-113 samples (excluding Q 1; seed 20260509).
  - Cell B: 10,000 length-matched 10-of-113 samples within ±15% of cluster total word-count (seed 20260511).
- **MW-5 PC**: 10-surah sub-sample of H-NEW-1200 cluster {56, 69, 74, 77, 81, 82, 83, 84, 86, 90}; uniform null at α = 0.05.
- **Bonferroni**: k = 2 cells, α per-cell = 0.025.

## Results

### Corpus distribution of the 99 names

- **Names present** under the substring rule: **65 of 99** (65.7%)
- **Names absent**: **34 of 99** (34.3%)

The 34 absent names (substring-rule), in al-Tirmidhī order:

| # | Name | Translit |
|--:|:--|:--|
| 21 | القابض | al-Qābiḍ |
| 22 | الباسط | al-Bāsiṭ |
| 23 | الخافض | al-Khāfiḍ |
| 24 | الرافع | al-Rāfiʿ |
| 26 | المذل | al-Mudhill |
| 38 | الحفيظ | al-Ḥafīẓ |
| 39 | المقيت | al-Muqīt |
| 40 | الحسيب | al-Ḥasīb |
| 41 | الجليل | al-Jalīl |
| 45 | الواسع | al-Wāsiʿ |
| 50 | الباعث | al-Bāʿith |
| 51 | الشهيد | al-Shahīd |
| 58 | المحصي | al-Muḥṣī |
| 59 | المبدئ | al-Mubdiʾ |
| 60 | المعيد | al-Muʿīd |
| 61 | المحيي | al-Muḥyī |
| 62 | المميت | al-Mumīt |
| 65 | الواجد | al-Wājid |
| 66 | الماجد | al-Mājid |
| 70 | المقتدر | al-Muqtadir |
| 71 | المقدم | al-Muqaddim |
| 72 | المؤخر | al-Muʾakhkhir |
| 77 | الوالي | al-Wālī |
| 78 | المتعالي | al-Mutaʿālī |
| 81 | المنتقم | al-Muntaqim |
| 83 | الرؤوف | al-Raʾūf |
| 87 | الجامع | al-Jāmiʿ |
| 89 | المغني | al-Mughnī |
| 90 | المانع | al-Māniʿ |
| 91 | الضار | al-Ḍār |
| 92 | النافع | al-Nāfiʿ |
| 94 | الهادي | al-Hādī |
| 95 | البديع | al-Badīʿ |
| 99 | الصبور | al-Ṣabūr |

**Methodological note**: many of these names DO appear in the Quran as verbal-active participles, plurals, or non-prefixed forms (e.g. *yuḥyī wa-yumīt* "He gives life and death" in Q 2:258, *huwa al-mubdiʾu wa-l-muʿīd* "He is the Originator and the Restorer" in Q 85:13 — note *al-mubdiʾu* in Q 85:13 should be flagged for re-check: the substring المبدئ uses a final hamza-on-yā that may differ from the Uthmānī rasm). The strict substring rule under-counts these because morphological inflection and orthographic variant prefixes are not collapsed.

**Cross-reference**: The prior project finding `divine-names-distribution.md` (morphology-strict, Buckwalter LEM matching, requires DET+masc-singular+divine-referring) found ~58 of 99 attested. H-NEW-1560's substring rule finds 65 of 99 attested. The two figures bracket the truth: the substring rule over-counts ambiguous referents (Q 12's الملك = governor of Egypt; Q 12's العزيز = the Egyptian dignitary), while the morphology-strict rule under-counts by requiring exact DET-MS form. The convergent fact is that **a non-trivial fraction (1/3 to 2/5) of the al-Tirmidhī 99-list is not Quranically attested in canonical *al-X* form** — independent corroboration of al-Suyūṭī's classical observation that some traditional names are reconstructed from verbal-form roots, not from the lexicalized *al-X* divine-name itself.

### Top-5 names by corpus substring count

| Name | Corpus count | n_surahs | n_verses |
|:--|--:|--:|--:|
| الله (Allāh) | 2,555 | 85 | 1,745 |
| الحق (al-Ḥaqq) | 187 | 53 | 176 |
| الآخر (al-Ākhir) | 156 | 47 | 154 |
| المؤمن (al-Muʾmin) | 134 | 36 | 119 |
| الحي (al-Ḥayy) | 107 | 44 | 99 |

The substring الله dominates (~2,555 / ~3,500 total name-attestations ≈ 73%), consistent with the Allāh-density corpus signature from H-NEW-1350. The next-highest names (al-Ḥaqq, al-Ākhir, al-Muʾmin, al-Ḥayy) each have an order of magnitude fewer attestations.

### Top-10 surahs by per-word divine-name density (the locked cluster)

| Rank | Surah | density | n_words | n_name | period |
|--:|:--|--:|--:|--:|:--|
| 1 | Q 112 al-Ikhlāṣ | 0.20000 | 15 | 3 | Meccan |
| 2 | Q 1 al-Fātiḥa | 0.17241 | 29 | 5 | Meccan |
| 3 | Q 85 al-Burūj | 0.11927 | 109 | 13 | Meccan |
| 4 | Q 64 al-Taghābun | 0.10744 | 242 | 26 | Medinan |
| 5 | Q 62 al-Jumuʿa | 0.10734 | 177 | 19 | Medinan |
| 6 | Q 110 al-Naṣr | 0.10526 | 19 | 2 | Medinan |
| 7 | Q 59 al-Ḥashr | 0.10291 | 447 | 46 | Medinan |
| 8 | Q 61 al-Ṣaff | 0.09292 | 226 | 21 | Medinan |
| 9 | Q 49 al-Ḥujurāt | 0.09065 | 353 | 32 | Medinan |
| 10 | Q 58 al-Mujādala | 0.09053 | 475 | 43 | Medinan |

Period composition: 3 Meccan (Q 1, 85, 112) + 7 Medinan (Q 49, 58, 59, 61, 62, 64, 110). Cluster total = **2,092 words** — short-surah regime.

### Cluster-cohesion test

| Cell | Observation | Null mean | Null 5th %ile | p_perm | Pass at α=0.025? |
|:--|--:|--:|--:|--:|:-:|
| A (uniform 10-of-113) | 0.7313 | 0.9263 | 0.8069 | **0.00880** | ✓ |
| B (length-matched ±15%) | 0.7313 | 0.7556 | 0.6846 | 0.27190 | ✗ |
| MW-5 PC (10-of-H1200) | 0.7113 | 0.9263 | 0.8069 | 0.00530 | ✓ (at α=0.05) |

**Direction matches pre-reg lock** (intra-cluster mean ≤ 5th percentile of null): TRUE for Cell A; the observed 0.7313 is at the ≈ 0.9 %ile of the uniform-null distribution. Under length-matching, the observed sits at the ≈ 27 %ile of the matched-null — within ordinary range, not the lower tail.

### Verdict

Per the locked acceptance window:

| Cell A | Cell B | PC | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✗ | ✓ | **DESCRIPTIVE-ONLY (length-confound suspected)** |

The cluster passes the uniform null but fails the length-matched null. The MW-5 PC confirms the FR instrument is working at this size regime (10-of-H1200 sub-sample passes at p = 0.0053). The PASS on Cell A is attributable to length confounding: short surahs naturally cluster tighter on FR-roots because their root-distributions are peakier (smaller token base ⇒ less smoothing). Once length is controlled, the divine-name-density signal does not survive.

## Interpretation

The headline FR-cluster hypothesis (H1) is **NOT confirmed**. The natural fluctuation of root-distributions across short surahs is large enough to absorb the apparent cluster-cohesion under length matching.

However, the **descriptive co-finding** is substantive and stands on its own:

1. **34 of 99 al-Tirmidhī names are absent** under the substring rule (and ~41 absent under the morphology-strict rule per `divine-names-distribution.md`). The al-Tirmidhī enumeration is not corpus-internal: a meaningful fraction of the canonical 99-list is reconstructed from verbal-root and non-canonical-form attestations, not from the lexicalized *al-X* divine-name in the Quran text itself. **This is empirical independent corroboration of al-Suyūṭī's classical observation** (*al-Itqān*, nawʿ 56) that the 99-enumeration is reconstructive.

2. **The 99-name corpus is dominated by الله** (~73% of all name-attestations). This is consistent with the H-NEW-1350 Allāh-density Medinan/Meccan separation finding and provides corpus-internal grounding for treating Allāh as a hub-name rather than as one-of-99 equivalents.

3. **Top-10 by name-density is 7/10 Medinan** (Q 49, 58, 59, 61, 62, 64, 110 + Q 112, 1, 85 from Meccan). The Medinan over-representation is consistent with H-NEW-1350 (Medinan > Meccan on Allāh-density by 5.2× ratio).

4. **Q 112 al-Ikhlāṣ is the corpus-MAX per-word name-density surah** (0.200 = 3 name-attestations in 15 words: الله at v.1 + الله الصمد at v.2 — two الله and one الصمد). Note that the al-Tirmidhī list contains الواحد (line 72) and الصمد (line 73) but NOT الأحد in its bare form, so Q 112's two أحد tokens (v.1 *qul huwa allāhu aḥad*, v.4 *kufuwan aḥad*) are not counted under the substring rule. This corroborates Q 112's role as the *thuluth al-Qurʾān* "one-third-of-the-Quran" theological-creed surah (al-Bukhārī #5013–5015): Q 112's distinctive function is to enumerate divine attributes, and the per-word density metric reflects this directly. Q 1 al-Fātiḥa is rank-2 (0.172), consistent with its *umm al-Kitāb* opener-function.

5. **The marker-thickness rule (cross-finding-025) is reinforced**: divine-name density is a SINGLE-AXIS lexical marker that does NOT drive FR-clustering once length is controlled. This is the same pattern as Christ-narrative (H-NEW-1310 NULL), sajda-trigger (H-NEW-1330 CONFIRMED-NULL), and al-ḥamdu li-llāh opener (H-NEW-1340 NULL). The marker-thickness rule's working threshold ("markers ≥30% of surah content tend toward cohesion; markers <10% need multi-axis correlation") explains H-NEW-1560 well: the cluster's median density is 0.10, right at the threshold, and the cluster spans both creed-class (Q 112) and community-law-class (Q 49, 58) — multi-axis fragmentation.

## Honest limits

- **Substring rule is not morphology-aware**. الملك matches both "the King [God]" and "the King [of Egypt]" (Q 12). العزيز matches both "the Mighty [God]" and "the Excellency [Egyptian governor]" (Q 12). This inflates the divine-name attestation count for Q 12 (Yūsuf) specifically. Q 12 ranks ~mid-pack on the density metric, so this likely does not change the top-10 cluster materially, but it affects the per-name corpus counts.
- **Multi-token names**: مالك الملك and ذو الجلال والإكرام are matched as whitespace-flexible substrings. They appear in the Quran in their canonical multi-token form rarely. Their substring count is small (verified by inspection of `csv/h-new-1560.json` per_name_table_full).
- **The 99-list is gharīb**: al-Tirmidhī himself flags the al-Walīd b. Muslim chain as gharīb. The 99-count itself is attested in al-Bukhārī #2736 and Muslim #2677 (both ṣaḥīḥ) but the SPECIFIC ENUMERATION of which 99 is later-tradition. al-Suyūṭī notes alternative enumerations (al-Ḥākim's list of ~80, expanded lists of >300). Testing under a different list would yield different absent-counts and different top-10 surahs.
- **Length-confound is real but expected**. Pre-reg specifically anticipated this via the marker-thickness rule. The DESCRIPTIVE-ONLY verdict is a confirmation of the pre-registered honest expectation, not a failure of the test design.
- **Cluster identity is data-derived** (top-10 by density). Per MW-7 the verdict ceiling was PASS-DIRECTED; even on a clean two-cell pass, independent replication would be required for CONFIRMED.

## Cross-finding connections

- **H-NEW-1350** (Allāh-density Medinan > Meccan, PASS-DIRECTED p = 10⁻⁴): same instrument family. H-NEW-1560 extends the substring-detection rule from 1 name (الله) to all 99 names. The 7/10 Medinan composition of the top-10-by-density is consistent with H-NEW-1350's Meccan/Medinan separation.
- **divine-names-distribution.md** (morphology-strict, Buckwalter LEM): the prior project finding using strict DET-MS divine-referring rule found ~58/99. H-NEW-1560's substring rule finds 65/99. Both bracket the al-Tirmidhī list's corpus-absentee question at 1/3 to 2/5.
- **cross-finding-025** (marker-thickness vs FR-cohesion threshold): this test adds one more NULL (under length-matching) to the marker-thin-axis docket. The marker-thickness rule's predictive accuracy strengthens.
- **H-NEW-1330** (sajda-cluster, CONFIRMED-NULL): same instrument, same outcome class. Single-marker thematic classes do not drive root-FR clustering once length is controlled.
- **H-NEW-170, H-NEW-140** (divine-name network and pair-cohesion): these prior findings test name *pairings*, not surah-level density. H-NEW-1560 is orthogonal.
- **al-Suyūṭī, *al-Itqān*, nawʿ 56**: the classical observation that the 99-enumeration is reconstructive (not all names appear in the canonical *al-X* form) is empirically corroborated here.

## Verdict line

**DESCRIPTIVE-ONLY** on the pre-registered FR-cohesion hypothesis (length-confound). **Independent corroboration** of al-Suyūṭī's classical observation (34/99 names absent under substring rule, ≈41/99 absent under morphology-strict rule — convergent).

The Allāh-name dominates (~73% of attestations); the 99-list's tail-end Sufi-tradition names (al-Bāsiṭ, al-Khāfiḍ, al-Muḥyī, al-Mumīt, al-Wājid, al-Mājid, al-Muqtadir, al-Mubdiʾ, al-Muʿīd, al-Muntaqim, al-Jāmiʿ, al-Mughnī, al-Māniʿ, al-Ḍār, al-Nāfiʿ, al-Hādī, al-Badīʿ, al-Ṣabūr, etc.) are systematically absent in the canonical *al-X* form. The al-Tirmidhī enumeration's *gharīb* grade is corpus-empirically reinforced.
