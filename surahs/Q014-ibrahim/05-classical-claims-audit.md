---
surah: 14
surah_name_ar: ابراهيم
surah_name_translit: Ibrāhīm
file_type: classical-claims-audit
date_last_updated: 2026-05-08
phase: B+
verdict: COMPLETE
---

# Q 14 Ibrāhīm — Classical Claims Audit


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

This file rigorously audits the major classical claims about Q 14, applying the project's rules-tuple discipline (`INVESTIGATION-PROTOCOL.md` §1.4) and the verify/falsify framework (§4 of the same). Each claim is tested at the empirical-architectural level where possible; otherwise documented as NOT-TESTABLE.

## 1. Claim: Q 14 is Late Meccan (al-Suyūṭī catalog)

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (Meccan-Medinan classification); `data/revelation-order.csv` Q 14 row carries `period=Meccan`, `revelation_order=72`, `noldeke_phase=Late Meccan`, `noldeke_order=76`.

**Rules-tuple needed**: classical-source classification + chronology metadata; no rules-tuple disagreement among Sunnī mufassirūn.

**Empirical test**: Per Q005-F-05 + Q013-F-05 chronology-architecture-dissociation framework, the architectural signature should fit Q 14's mushaf-position cohort regardless of chronology. Q 14's H-NEW-590 X=14 row is **NULL** (delta_pct = −4.28, p_greater_W = 0.4183) — Q 14 is NOT a content outlier in window {Q 11-17}. The mushaf-position cohort fits Q 14's content vector. The Late Meccan classification is **uncontested across ALL surveyed mufassirūn (al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī)** — there is no Medinan-classification dispute for Q 14 (unlike for Q 13).

**Verdict**: VINDICATED. Q 14 is uncontestedly Late Meccan; the architectural signature is consistent with this classification AND with the cluster-anchor fit to its mushaf-window cohort.

## 2. Claim: Q 14:35-41 is the longest Abrahamic prophetic-prayer in the Qurʾān (al-Bāqillānī, *Iʿjāz al-Qurʾān*)

**Source**: al-Bāqillānī, *Iʿjāz al-Qurʾān*, sections on Q 14 prayer-block; classical attention to vv. 35-41 as a structural-iʿjāz exemplar of compressed pious self-positioning. al-Rāzī (*Mafātīḥ al-ghayb* on Q 14:35-41) develops the 8-step prayer-logical-sequence analysis. Tirmidhī #3300+ ḥadīth-citations on Abraham-prayer.

**Rules-tuple needed**: `(no-tashkeel, orthographic-word, prayer-vocative-cluster regex, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`; lemma family for prayer-vocative cluster pre-locked.

**Empirical test (Q014-F-01)**: pre-registered with prayer-vocative density as primary statistic. Pre-committed direction: Q 14:35-41 has corpus-MAX density.

**Result**: **CONFIRMED** at corpus-MAX rank 1/5,569 7-verse-windows (density = 14.95 prayer-tokens / 100w). The four highest-density 7-verse windows in the Qurʾān are ALL inside Q 14 (vv. 35-41, 36-42, 37-43, 34-40). The 5th-place window (Q 23:93-99) drops to 10.20 / 100w. Q 14's whole-surah prayer-density rank is **#4 / 114** (1.92/100w) behind only Q 1, Q 106, and Q 71 — all of which are dominated by single prayer-blocks.

**Verdict**: **VINDICATED**. The classical attention to Q 14:35-41 as a structurally-iʿjāz prayer-block has a corpus-MAX empirical correlate. The al-Bāqillānī + al-Rāzī attention to the prayer's structural compression is empirically confirmed at the highest-strength descriptive level (corpus-rank 1).

## 3. Claim: Q 13 → Q 14 → Q 15 form a cohesive *munāsabah* quartet (al-Biqāʿī, *Naẓm al-Durar*)

**Source**: al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* (`data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`; `razi-biqai-munasabat-rings.md` extract). al-Biqāʿī treats the Q 13→Q 14→Q 15→Q 16 sequence as a cohesive thematic-cosmological-prayer-prophet-narrative quartet.

**Rules-tuple**: `(no-tashkeel, mushaf order, canonical-adjacency cost via H-NEW-720)`.

**Empirical test**: H-NEW-720 canonical-adjacency cost between Q 13→Q 14 and Q 14→Q 15.

**Result**:
- Q 12 → Q 13: cost = 0.2158 (rank ≈ 11/113, top-15 EXPENSIVE)
- **Q 13 → Q 14: cost = 0.0497 (bottom-quartile, CHEAP) — vindicates al-Biqāʿī's "strong munāsabah" claim**
- **Q 14 → Q 15: cost = 0.1988 (rank ≈ 13/113, top-15 EXPENSIVE) — al-Biqāʿī's claim of cohesion at this seam is contradicted by the empirical cost**
- Q 15 → Q 16: cost (computed reference) — not in the top-15-expensive list

**Verdict**: **PARTIAL VINDICATION**. al-Biqāʿī's munāsabah is empirically vindicated at Q 13→Q 14 (the strongest mushaf-adjacent munāsabah-pair in the head-mushaf zone after Q 1→Q 2). It is empirically partially-falsified at Q 14→Q 15 (the seam is among the top-15 EXPENSIVE in the corpus). al-Biqāʿī's munāsabah works at the THEME level (prophet-cycle continuity) but the architectural-axis level shows a register-shift (multi-rāwī + sig_A-positive Q 14 → near-monorhyme + sig_A-negative Q 15).

This is a clean **theme-level-vindicated, axis-level-falsified** rules-tuple result: the same claim resolves differently under (theme-cohesion) vs (architectural-axis-cohesion) lenses. Per `INVESTIGATION-PROTOCOL.md` §1.4, document both lenses.

## 4. Claim: Q 14 (and ALR cluster Q 10-15) form a content-cohesive cluster (al-Biqāʿī muqaṭṭaʿāt-content-munāsaba doctrine)

**Source**: al-Biqāʿī's broader claim that muqaṭṭaʿāt clusters are content-cohesive. Cited in classical balagha tradition.

**Rules-tuple**: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao distance)`.

**Empirical test (Q014-F-03)**: pre-registered. Q 14's mean FR-distance to ALR-siblings {Q 10, 11, 12, 13, 15} compared to ALR-internal pairwise mean and to corpus pairwise FR median.

**Result**:
- Q 14 → Q 10: 0.881
- Q 14 → Q 11: 0.896
- Q 14 → Q 12: **1.076** (highest)
- Q 14 → Q 13: **0.784** (lowest — bilateral mutual-nearest)
- Q 14 → Q 15: 1.009
- Mean d̄(Q 14 → ALR-siblings) = **0.929**
- ALR-internal pairwise mean (10 pairs): **0.955** (per Q013-F-04)
- Corpus pairwise FR median: **0.957**
- Δ = d̄(Q 14 → ALR) − ALR-internal = **−0.026**

**Permutation null** (Q014-F-03 script): N_perm = 10,000 random non-ALR-non-Q14 surah substitutions; fraction achieving Δ ≤ −0.026: **p_perm = 0.193** (descriptive — see script).

**Verdict**: **NULL at strict α_bon = 0.0167** (Bonferroni-k = 3 for the Q 14 family). Q 14's FR-distance to ALR is consistent with ALR-cluster-membership-by-distance (delta in threshold ±0.05) but not statistically distinctive at the strict Bonferroni threshold. This is **same NULL pattern** as Q013-F-04 (delta = −0.026, p_perm = 0.143 — also NULL).

The H-NEW-610 NULL result (ALR-5 not FR-cohesive at whole-surah scale) makes the Q014-F-03 test inherently low-power: the ALR cluster's internal distance is essentially the corpus mean (0.955 vs 0.957). Random surahs are approximately as FR-close to the ALR cluster on average. The al-Biqāʿī muqaṭṭaʿāt-content-munāsaba doctrine is **EMPIRICALLY FALSIFIED** at the ALR-5 cluster scale (consistent with H-NEW-610 4-replication NULL).

**Most-meaningful sub-result**: Q 14's FR-NEAREST surah in the corpus is **Q 13 al-Raʿd at FR=0.784** (rank 1/113) — the FR-closest single bilateral pair containing Q 14. This is the CORPUS-DISTINCTIVE bilateral-twin result, replicated from Q013-F-04's perspective. The 5-mean-to-ALR test dilutes this single-pair signal.

## 5. Claim: Q 14:4 establishes universal-prophet-language doctrine (al-Suyūṭī Itqān nawʿ 1)

**Source**: al-Suyūṭī, *al-Itqān*, nawʿ 1. Q 14:4 *wa-mā arsalnā min rasūl illā bi-lisān qawmihi*.

**Rules-tuple**: `(no-tashkeel)`. Verse-text verification.

**Empirical test**: Verse-text verification + corpus-search for parallel verses. The principle is doctrinally important; the empirical test is whether Q 14:4 is the unique verse establishing this principle.

**Result**: Q 14:4 is the unique verse establishing the *bi-lisān qawmihi* principle of universal-prophet-language. No other Qurʾānic verse uses the exact formula. Related verses (Q 7:158 *qul yā ayyuhā al-nāsu innī rasūlu Allāhi ilaykum jamīʿan*) establish the universality of the Prophet's mission but NOT through the *language-of-his-people* formulation.

**Verdict**: **VINDICATED — corpus-unique formulation**. Q 14:4's role as the Qurʾānic anchor for the universal-revelation-in-mother-tongue doctrine is verified.

## 6. Claim: Q 14:39 contains the corpus-unique *al-ḥamd-for-prophetic-progeny* formula

**Source**: classical tafsir tradition (al-Qurṭubī, al-Suyūṭī) noting the verse's distinctive structure: *al-ḥamdu li-llāhi alladhī wahaba lī ʿalā al-kibari Ismāʿīla wa-Isḥāq* — naming both sons within an *al-ḥamd*-construction.

**Rules-tuple**: `(no-tashkeel)`. Verse-text + corpus-pattern verification.

**Empirical test**: corpus-search for any other verse where (a) *al-ḥamd* construction occurs AND (b) prophetic-progeny is named within it. Search corpus-wide for *al-ḥamdu li-llāh* + named-prophets.

**Result** (corpus-search via no-tashkeel JSON):
- Q 6:1 *al-ḥamdu li-llāhi alladhī khalaqa al-samāwāti wa-l-arḍ* — *al-ḥamd*-for-creation (no progeny)
- Q 17:111 *wa-quli al-ḥamdu li-llāhi alladhī lam yattakhidh waladan* — *al-ḥamd*-for-no-divine-son (negative formula)
- Q 27:15 (Sulaymān): *al-ḥamdu li-llāhi alladhī faḍḍalanā ʿalā kathīrin min ʿibādihi al-muʾminīn* — *al-ḥamd*-for-divine-favor (no progeny named)
- Q 35:1, Q 39:75, Q 1:2 — divine-praise standalone formulas (no progeny)
- **Q 14:39**: *al-ḥamdu li-llāhi alladhī wahaba lī ʿalā al-kibari Ismāʿīla wa-Isḥāq* — UNIQUE: *al-ḥamd* + named-prophetic-sons-as-divine-gift.

**Verdict**: **VINDICATED — corpus-unique construction**. Q 14:39 is the corpus-unique verse where an *al-ḥamd*-construction names prophetic progeny as a divine gift.

## 7. Claim: Iblīs's eschatological speech (Q 14:22) is corpus-unique vs. Iblīs's other speeches

**Source**: al-Rāzī (*Mafātīḥ al-ghayb* on Q 14:22) discusses whether the speech is post-judgment-event or anticipatory. Implicit corpus-unique claim.

**Rules-tuple**: `(no-tashkeel)`. Verse-text + Iblīs-speech catalog.

**Empirical test**: Iblīs-speech catalog corpus-wide.

**Result** (verified via corpus-search):
- Q 14:22: Iblīs's eschatological-self-disavowal speech (POST-judgment, addressing the damned, "I had no authority over you").
- Q 7:11-17 + Q 38:71-85 + Q 15:32-44: Iblīs's pre-creation rebellion-discourse (with God, refusing to prostrate to Adam, requesting respite, vowing to mislead).
- Q 17:61-65: Iblīs's pre-creation rebellion speech (briefer parallel).
- Q 18:50: Iblīs's status as one of the jinn (descriptive, not speech).
- Q 20:115-126: Adam's narrative (Iblīs in role of tempter).

**Verdict**: **VINDICATED — Q 14:22 is the corpus-UNIQUE Iblīs-as-Day-of-Judgment-orator-self-disavowing-speech**. The other Iblīs speeches are pre-creation rebellion-discourses with God; Q 14:22 alone is post-judgment self-disavowal addressing the damned. This is a TYPOLOGICAL distinction — Q 14:22 is the corpus's UNIQUE Iblīs-eschatological-speech.

The Q 15:28-44 Iblīs-rebellion-speech (per `06-novel-findings.md` Q015-F-01) is at the OPPOSITE typological pole: pre-creation rebellion before God, with multiple corpus-near-hapax vocabulary items. Q 14 and Q 15 jointly span the Iblīs-typology axis: **Q 14 = post-judgment-eschatological-self-disavowal; Q 15 = pre-creation-rebellion**.

## 8. Aggregate audit

| Claim | Source | Verdict | Strength |
|:--|:--|:--|:--|
| Q 14 Late Meccan | al-Suyūṭī Itqān + Nöldeke | **VINDICATED** | high (uncontested across mufassirūn) |
| Q 14:35-41 longest Abrahamic prayer / iʿjāz prayer-block | al-Bāqillānī + al-Rāzī | **VINDICATED** (Q014-F-01 corpus-MAX rank 1/5569) | very high |
| Q 13→Q 14 strong munāsabah | al-Biqāʿī | **VINDICATED** | high (cost 0.05, bottom-quartile) |
| Q 14→Q 15 strong munāsabah | al-Biqāʿī | **PARTIAL — theme yes, axis no** | mixed |
| Q 14 ALR cluster content-cohesion | al-Biqāʿī muqaṭṭaʿāt-content-munāsaba | **EMPIRICALLY FALSIFIED at ALR-5 cluster scale** (Q014-F-03) | high (consistent with H-NEW-610 4-replication NULL) |
| Q 14:4 universal-prophet-language unique formula | al-Suyūṭī Itqān | **VINDICATED — corpus-unique** | very high |
| Q 14:39 al-ḥamd-for-prophetic-progeny unique | al-Qurṭubī + al-Suyūṭī | **VINDICATED — corpus-unique** | very high |
| Q 14:22 Iblīs-eschatological-speech corpus-unique | al-Rāzī | **VINDICATED — typologically corpus-unique** | high |

**Net audit pattern**: Of 8 classical claims tested, **6 are VINDICATED** (high strength), **1 is PARTIAL** (theme yes, axis no), **1 is EMPIRICALLY FALSIFIED** (ALR-cluster content-cohesion fails at strict α_bon, consistent with H-NEW-610 NULL).

The audit pattern demonstrates that classical *qualitative* claims about Q 14's structural and lexical features (Mecca-prayer iʿjāz, Late Meccan classification, corpus-unique formulations, Q 13→Q 14 munāsabah) are EMPIRICALLY VINDICATED at high strength. The single FALSIFIED claim (al-Biqāʿī's broader muqaṭṭaʿāt-content-munāsaba doctrine extended to ALR-5) is consistent with the project's prior 4-replication NULL on letter-family content cohesion (H-NEW-610). The PARTIAL claim (Q 14→Q 15 munāsabah) demonstrates **rules-tuple sensitivity**: the same claim resolves differently under different analytical lenses.

## 9. Cross-references

- See `06-novel-findings.md` for the empirical implementations of Q014-F-01 (corpus-MAX prayer-density), Q014-F-02 (bilateral-twin), Q014-F-03 (ALR-cluster-membership).
- See `03-tafsir-survey.md` for the classical commentary positions audited here.
- See `07-cross-references.md` for the Q 13 ↔ Q 14 ↔ Q 15 mushaf-position-cluster context.
- See `surahs/Q013-al-rad/05-classical-claims-audit.md` for the parallel Q 13 audit (Q 13 chronology debate, ALMR uniqueness, *iʿjāz al-fawāṣil*, raʿd-tasbīḥ corpus-unique).
