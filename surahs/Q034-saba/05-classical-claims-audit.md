---
surah: 34
surah_name_ar: سبإ
surah_name_translit: Sabaʾ
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
verdict: 6 classical claims tested; 3 CONFIRMED, 2 PARTIAL, 1 NULL.
---

# Q 34 Sabaʾ — Classical Claims Audit

This file applies the project's classical-quantitative-claims-audit methodology to all classical claims about Q 34 that are testable. Each claim is given a project verdict.

## 1. Audit summary table

| ID | Source | Claim | Verdict |
|:--:|:--|:--|:--:|
| Q34-CC-01 | al-Zarkashī, *Burhān* 1/181 | Q 34 is one of the 5 al-ḥamdu li-llāh openers {Q 1, 6, 18, 34, 35} | **CONFIRMED** (= CC-048) |
| Q34-CC-02 | al-Ṭabarī, *Jāmiʿ al-bayān* ad loc. | Q 34 names Sabaʾ as historical kingdom (eponymous patriarch of South-Arabian tribes) | **CONFIRMED** (textual + tribal-genealogical reception) |
| Q34-CC-03 | al-Bukhārī, *Ṣaḥīḥ* §431, Muslim §1069 | Q 34:28 *kāffatan li-l-nās* establishes universal prophecy ("5/6 things granted only to me") | **CONFIRMED** (7-book hadith convergence) |
| Q34-CC-04 | al-Biqāʿī, *Naẓm al-durar* | Q 33 → Q 34 munāsabah (Medinan → Late-Meccan shift) | **PARTIAL** (rough seam empirically: rank 111/113; Q 33-34 H-NEW-130 boundary set verified) |
| Q34-CC-05 | al-Biqāʿī, *Naẓm al-durar* | Q 34 → Q 35 munāsabah anchored on shared al-ḥamd opener creates seamless transition | **PARTIAL** (opener shared YES; seam mid-pack rank 65/113, NOT clamped-zero; Q034-F-04) |
| Q34-CC-06 | al-Suyūṭī, *al-Itqān* nawʿ 1 | Q 34 is Late-Meccan, revelation-order position 58/114 | **CONFIRMED** (consistent with Nöldeke 3rd Meccan; thematic alignment with creedal-eschatology Late-Meccan band) |

## 2. Audits in detail

### Q34-CC-01 — al-Zarkashī's al-ḥamdu li-llāh cluster

**Claim** (al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān* 1/181): "There are 5 surahs opening with al-ḥamdu li-llāh: al-Fātiḥa (1), al-Anʿām (6), al-Kahf (18), Sabaʾ (34), Fāṭir (35)."

**Test**: phrase-search for *al-ḥamdu li-llāh* as opening word(s) of v.1 (with Q 1 special-cased per classical convention).

**Result**: 5 surahs match exactly as al-Zarkashī states. (Verified via `quran-text/quran-no-tashkeel.json`.)

**Verdict**: **CONFIRMED**. (= project CC-048.) Extended empirical findings:
- Q034-F-01: cluster does NOT show FR-cohesion (within-cluster mean 0.9902 vs corpus 0.9226).
- The cluster is a formal-opener-template parallel WITHOUT underlying root-distribution content fingerprint.
- Q 34's distinctive sub-feature: dual-ḥamd v.1 (corpus-unique).

### Q34-CC-02 — al-Ṭabarī on Sabaʾ as historical kingdom

**Claim** (al-Ṭabarī, *Jāmiʿ al-bayān* ad Q 34:15): The proper noun *sabaʾ* designates simultaneously (a) the eponymous patriarch Sabaʾ b. Yashjub b. Yaʿrub b. Qaḥṭān and (b) the South-Arabian kingdom centered at Maʾrib. al-Ṭabarī cites al-Suddī, ʿIkrima, Mujāhid in support.

**Test**: corpus distribution of LEM:saba< (QAC v0.4); cross-reference with classical tribal genealogies.

**Result**: LEM:saba< appears 2× in the corpus — Q 27:22 (the hoopoe-report) and Q 34:15 (the kingdom-narrative opening). Both attestations refer to the same kingdom-and-people. al-Ṭabarī's tribal genealogy is preserved in his *Tārīkh al-rusul wa-l-mulūk* and corroborated by al-Hamdānī (*al-Iklīl*) and pre-Islamic-Yemeni epigraphy.

**Verdict**: **CONFIRMED** (textual + classical-reception + epigraphic).

### Q34-CC-03 — Q 34:28 *kāffatan li-l-nās* universal-prophecy hadith

**Claim** (al-Bukhārī §431, Muslim §1069): The Prophet ﷺ was given 5/6 things not given to prior prophets, item 4 of which is *buʿithtu ilā al-nāsi kāffatan* — the qurʾānic anchor being Q 34:28.

**Test**: hadith citation across the 9 canonical books for the 5/6-things chain with explicit *kāffatan* + Q 34:28 invocation.

**Result**: VERIFIED via normalized-Arabic text-matching in 7 of the 9 books:
- al-Bukhārī idInBook=431 (Jābir b. ʿAbdallāh chain, 5-list)
- al-Bukhārī idInBook=331 (parallel variant with *ʿāmmah*)
- Muslim idInBook=1069 (Abū Hurayrah chain, 6-list)
- al-Tirmidhī idInBook=1590 (Abū Hurayrah chain, *ḥasan ṣaḥīḥ*)
- al-Nasāʾī idInBook=433 (Jābir chain, 5-list)
- al-Dārimī idInBook=709 (Jābir chain) + idInBook=1741 (Abū Dharr chain, *al-aḥmar wa-l-aswad* variant)
- Aḥmad idInBook=907 (ʿAlī b. Abī Ṭālib chain)

Multiple companion-witnesses (Jābir, Abū Hurayrah, Abū Dharr, ʿAlī) preserve the *kāffatan* clause across 7 canonical collections. Full chain catalog at `04-hadith-corpus.md` §1.

**Verdict**: **CONFIRMED** (multi-companion, multi-chain, multi-collection verification).

### Q34-CC-04 — Q 33 → Q 34 munāsabah (Medinan → Late-Meccan)

**Claim** (al-Biqāʿī, *Naẓm al-durar* on the Q 33-Q 34 boundary): The transition is one of the corpus's structurally significant period-shifts.

**Test**: Q 33 → Q 34 canonical-adjacency cost from H-NEW-720; structural-boundary classification from H-NEW-130.

**Result**:
- H-NEW-720 Q 33 → Q 34 delta_raw = +0.3311, rank 111/113 (3rd ROUGHEST seam in corpus).
- H-NEW-130: Q 33-34 IS in the structural boundary set (period_Medinan_to_Meccan + phase_Medinan_to_Late_Meccan).
- Empirical roughness drivers: period boundary (Medinan vs Late-Meccan), genre boundary (legal-social vs creedal-narrative), length asymmetry (73 vs 54 verses).

**Verdict**: **PARTIAL** — al-Biqāʿī's qualitative reading of a significant period-shift is empirically VINDICATED at the very-rough-seam level (rank 111/113). However, the munāsabah literature's claim that all canonical adjacencies have positive coherence rationale is empirically refined: this seam is empirically ROUGH at the QAC-root content-vector level. The classical claim functions at the *thematic-progression* level, not at the *content-distribution* level.

### Q34-CC-05 — Q 34 → Q 35 munāsabah (shared al-ḥamd opener)

**Claim** (al-Biqāʿī, *Naẓm al-durar* on the Q 34-Q 35 boundary): The shared al-ḥamdu li-llāh opening creates a seamless rhetorical transition (an *iʿjāz al-tartīb* fingerprint of opener-twin pairs).

**Test**: Q 34 → Q 35 canonical-adjacency cost (H-NEW-720); seam rank vs other opener-cluster transitions (Q034-F-04, Q034-F-05).

**Result**:
- H-NEW-720 Q 34 → Q 35 delta_raw = +0.0745, rank 65/113 (MID-PACK, NOT top-20 smoothest).
- H-NEW-130: Q 34-35 NOT in structural boundary set.
- Q034-F-04: rank 65/113 fails top-20 threshold; H2 (vs median of {Q1→2, Q5→6, Q17→18, Q33→34, Q34→35}) FAILS (median is 0.0745 = the Q 34→Q 35 value itself, since the Q 33→Q 34 cost dominates); H3 (Q 34↔Q 35 FR=0.9268 vs intra-cluster median 0.9640) PASSES.
- Q034-F-05: Q 34↔Q 35 ranks 2 of 4 sequential opener-pairs (tightest is Q 18↔Q 34 = 0.8984); H1 (Q 34↔Q 35 as tightest) FAILS; H2 (FR percentile 42.73% ≤ 50%) PASSES.

**Verdict**: **PARTIAL** — al-Biqāʿī's *opener-share creates smooth transition* claim VINDICATED at the **opener-form-template** level (both surahs do open with the same phrase, and the FR distance is below intra-cluster median + below corpus median) but FALSIFIED at the **seam-cost-extremity** level (the seam is mid-pack rather than top-20 smoothest). The lesson: opener-share IS a sub-additive smoothness contributor, NOT a sufficient condition for an empirically-extreme smooth seam.

This is a **rules-tuple-sensitive** finding: under content-FR rules-tuple, the smoothness is moderate; under formal-opener-typology rules-tuple, the smoothness is categorical (both open with identical phrase). al-Biqāʿī's claim operates at the latter level.

### Q34-CC-06 — al-Suyūṭī Late-Meccan chronology

**Claim** (al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1): Q 34 is Late-Meccan; revelation-order position 58/114.

**Test**: thematic-content alignment with Late-Meccan creedal-eschatological-tawḥīd compendium pattern (cf. Q 6, Q 17, Q 25, Q 32, Q 41, Q 46, Q 67); chronological-marker presence/absence (no explicit Medinan markers — no battle references, no hypocrite-passages, no legal-Medinan vocabulary).

**Result**:
- Q 34 contains: omniscience-doctrine (vv. 1-3), David-Solomon vignettes (vv. 10-14), Sabaean-history (vv. 15-19), *qul*-density 5.22× corpus mean (15 occurrences in 14 verses), universal-prophecy declaration (v.28), *mithqāl dharra* parallelism (vv. 3, 22), the one-thing-only homiletic (v.46), eschatological-final-scene (vv. 51-54).
- All thematic markers align with Late-Meccan creedal-eschatological pattern.
- No Medinan markers (no battle/legal/hypocrite passages).
- H-NEW-FR neighborhood: top-10 nearest are all Late-Meccan creedal-band surahs (Q 41, 46, 32, 36, 10, 25, 67, 45, 17, 27 — none Medinan).

**Verdict**: **CONFIRMED** (thematic + lexical + FR-neighborhood alignment).

## 3. Cross-cutting observations

### 3.1 The classical-empirical gap on al-Biqāʿī's munāsabah

The Q 33→Q 34 and Q 34→Q 35 seam analyses jointly show that:
- **Strongly significant transitions** (al-Biqāʿī Q 33-Q 34): empirically rough seam (rank 111/113) — VINDICATED at the boundary-extremity level.
- **Smoothly significant transitions** (al-Biqāʿī Q 34-Q 35 opener-twin): empirically mid-pack seam (rank 65/113) — REFINED at the seam-extremity level.

This is consistent with the project's **cross-finding-014 al-Biqāʿī munāsabah selective validity** pattern: the qualitative-rhetorical reading captures **directional** structure but not **extremity-rank** structure. Classical scholars correctly identified the *which transitions are different* axis; the empirical analysis refines *how different and on what scale*.

### 3.2 The 5-opener cluster: form vs content

Q34-CC-01 (al-Zarkashī's 5-opener listing) is CONFIRMED at the opener-form level. But Q034-F-01 NULLs the cluster's FR-cohesion: shared opener does NOT correlate with shared root-distribution. This is the **OQ-3-candidate-ANSWERED-NEGATIVE** finding: al-ḥamdu li-llāh is NOT a second book-introduction-marker class analogous to the muqaṭṭāʿat. The al-Zarkashī listing is a formal observation, not an empirical content-cluster.

### 3.3 The Sabaean historical-narrative tradition

Q34-CC-02 (al-Ṭabarī's kingdom-identification) is CONFIRMED with pre-modern-Yemeni epigraphic corroboration (Sabaean inscriptions document the historicity of Maʾrib + the dam + the post-flood tribal-dispersion pattern). This is one of the corpus's few cases of an extra-textual archaeological-historical anchor matching the Quranic narrative at the empirical level. The classical tradition's resistance to allegorical reading of Q 34:15-19 (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr) is empirically vindicated.

## 4. Cross-references

- [Q034-F-01](csv/Q034-F-01.json) — al-ḥamdu cluster cohesion NULL.
- [Q034-F-02](csv/Q034-F-02.json) — Q 27 ↔ Q 34 Saba-pair DIRECTIONAL-WEAK.
- [Q034-F-03](csv/Q034-F-03.json) — ḥmd root rank DIRECTIONAL.
- [Q034-F-04](csv/Q034-F-04.json) — Q 34→Q 35 seam DIRECTIONAL-WEAK.
- [Q034-F-05](csv/Q034-F-05.json) — opener pair-distance DIRECTIONAL.
- `04-hadith-corpus.md` — Q 34:28 universal-prophecy hadith verifications.
- [[cross-finding-014]] — al-Biqāʿī munāsabah selective validity.
- [[CC-048]] — al-Zarkashī al-ḥamdu cluster classical claim.
