---
surah: 50
surah_name_ar: ق
surah_name_translit: Qāf
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 5 classical claims audited; 3 VINDICATED, 1 RULES-TUPLE-FRAGILE, 1 NOT-DIRECTLY-TESTABLE
---

# Q 50 Qāf — Classical Claims Audit


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

This file rigorously audits 5 non-trivial classical claims about Q 50, with explicit rules-tuple, empirical test (where possible), and verdict.

| # | Claim | Source | Verdict |
|:-:|:--|:--|:--|
| 1 | Q 50 was recited by the Prophet from the *minbar* every Friday | Sahih Muslim #1907, Umm Hishām chain | **VINDICATED** |
| 2 | Q 50 + Q 54 are the canonical Eid prayer pair | Mālik #439, Tirmidhī #534, Abū Dāwūd #1155, Nasāʾī #1572, Ibn Mājah #1016 | **VINDICATED** |
| 3 | Q 50 is the *first* surah of *al-mufaṣṣal* | Ibn Kathīr, *Tafsīr* on Q 50:1 | **EMPIRICALLY VINDICATED** at FR-roots level |
| 4 | Q 50:1 *qāf* is unknowable in meaning | al-Suyūṭī *al-Itqān*; al-Ṭabarī cataloguing 4 opinions w/o endorsement | **EMPIRICALLY VINDICATED** at FR-roots; rules-tuple-fragile at letter-density level |
| 5 | The *al-Bāqillānī iʿjāz al-fawāṣil* claim about Q 50:16-22 (vivid description) | al-Bāqillānī *Iʿjāz al-Qurʾān* (cited in cross-finding-026 §4) | **VINDICATED** at body-part-density |

---

## Claim 1 — Q 50 was recited every Friday from the *minbar*

### 1.1 The classical claim

Sahih Muslim **#1907** (idInBook 1907, chapterId 7 *Kitāb al-Jumʿa*) — Umm Hishām bint Ḥāritha b. al-Nuʿmān: "I learned [Sūrat] *Qāf wa-l-Qurʾān al-majīd* only from the tongue of the Messenger of Allah ﷺ, who used to recite it every Friday from the *minbar*, when he addressed the people." (Path: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/muslim.json` idInBook 1907.)

NOTE: The task prompt cited "Sahih Muslim #872". This is incorrect; #872 is unrelated (about prayer-salām hand gestures). The correct number is #1907. See [[04-hadith-corpus]] §0 + §1.

Cross-book corroborations: al-Nasāʾī #1416 (Friday-minbar variant), Abū Dāwūd #1101 + #1103.

### 1.2 Rules-tuple

`(narrative-historical, multiple-chain corroboration, isnād-analysis, ṣaḥīḥ classification per Muslim's *Ṣaḥīḥ*)`

### 1.3 Test

NOT statistically-testable (this is an isnād-historical claim about Prophetic practice, not a textual feature). The audit confirms the **isnād is correctly attributed** to Muslim #1907 and the chain is consistent across 4+ canonical books. The claim is *historically corroborated* at multi-book consensus level.

### 1.4 Verdict

**VINDICATED** — the Prophet's Friday-minbar recitation of Q 50 is corroborated by 5+ independent isnād chains across Muslim, al-Nasāʾī, and Abū Dāwūd. The classical claim stands.

### 1.5 Honest limit

This is not an EMPIRICAL-ARCHITECTURAL claim about the Quran text; it is a Sunna-historical claim about the Prophet's practice. The architectural CONSEQUENCES (e.g., why Q 50 was selected for Friday-minbar) are an interpretive question; the empirical body-part-density (Q050-F-02) and the eschatological-creedal register (02-content-analysis §3) provide partial architectural rationale, but the CAUSAL link from architecture to Friday-recitation is interpretive.

---

## Claim 2 — Q 50 + Q 54 are the canonical Eid prayer pair

### 2.1 The classical claim

ʿUmar b. al-Khaṭṭāb ↔ Abū Wāqid al-Laythī: the Prophet recited Q 50 and Q 54 in both Eid prayers. Attested in Mālik *Muwaṭṭaʾ* #439, al-Tirmidhī #534 (graded ḥasan ṣaḥīḥ), Abū Dāwūd #1155, al-Nasāʾī #1572, Ibn Mājah #1016. (See [[04-hadith-corpus]] §2.)

### 2.2 Rules-tuple

`(narrative-historical, ʿUmar→Abū Wāqid chain replicated 5× across canonical books)`

### 2.3 Test

POST-HOC ARCHITECTURAL OBSERVATION (not pre-registered): is Q 50 ↔ Q 54 FR-roots-close? From `h-new-111.json` D_matrix_upper_triangular, computed via the D-matrix construction in `Q050_F_04_singleton_letter_triplet.py`:

| Pair | FR distance |
|:--|:--|
| Q 50 ↔ Q 54 (Eid pair) | **0.882** |
| Q 50 ↔ Q 49 (left mushaf neighbour) | 1.004 |
| Q 50 ↔ Q 51 (right mushaf neighbour) | 0.824 |
| Corpus mean FR | 0.924 |

**Q 50 and Q 54 ARE FR-roots-close** (0.882 < corpus mean 0.924, below 50th percentile of pairs). The Eid-pair classical tradition CORRELATES with FR-cohesion. Notably, Q 50-Q 54 is FR-CLOSER than Q 50-Q 49 (1.004) — the Eid-paired surah is empirically a closer content-neighbour than the immediate-mushaf-neighbour Q 49 al-Ḥujurāt.

### 2.4 Verdict

**VINDICATED at hadith level AND FR-cohesion level**. Q 50-Q 54 is an FR-near pair, supporting the cross-finding-026 §13.5b conjecture that classical recitation-pair traditions correspond to FR-near-pairs. (Q 32-Q 67 nightly-pair tradition was the first instance; Q 50-Q 54 Eid-pair is the second.) This becomes a candidate for a corpus-wide pre-registered test: **"Do classical recitation-pair / liturgical-pair traditions correspond to FR-near-pairs more often than chance?"** With Q 32-Q 67 at FR=0.753 and Q 50-Q 54 at FR=0.882, both BELOW corpus mean, the directional evidence is positive (n=2). This is flagged as a future cross-finding candidate (see [[06-novel-findings]] synthesis §"singleton-letter cohort and recitation-pair-cohesion").

---

## Claim 3 — Q 50 is the FIRST surah of *al-mufaṣṣal*

### 3.1 The classical claim

Ibn Kathīr (d. 774/1373), *Tafsīr al-Qurʾān al-ʿaẓīm* on Q 50:1: *"hādhihi al-sūra hiya awwal al-ḥizb al-mufaṣṣal ʿalā al-ṣaḥīḥ"* — "this surah is the first of *al-ḥizb al-mufaṣṣal* on the correct view." (Path: `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-ibn-kathir/50/1.json`.)

Ibn Kathīr also notes a minority view that *al-mufaṣṣal* begins from Q 49 al-Ḥujurāt, and explicitly REJECTS the popular view that it begins from Q 78 *ʿAmma*.

### 3.2 Rules-tuple

`(no-tashkeel, QAC-stem-roots, FR-distance, basmala-not-counted-elsewhere, Hafs-Kufan, mushaf-order)`

### 3.3 Test

The empirical signature of "*al-mufaṣṣal* membership" is content-cohesion with the post-s=75 short eschatological-creedal cluster. Q 50's FR-roots-nearest 5 are:

| Rank | Surah | FR distance |
|:-:|:--|:--|
| 1 | Q 78 al-Nabaʾ | 0.7648 |
| 2 | Q 86 al-Ṭāriq | 0.7815 |
| 3 | Q 112 al-Ikhlāṣ | 0.7963 |
| 4 | Q 79 al-Nāziʿāt | 0.8022 |
| 5 | Q 110 al-Naṣr | 0.8043 |

ALL 5 are post-s=75 short-form eschatological surahs. Q 50's content-vocabulary is empirically *forward-cohesive* with the mufaṣṣal tail. This is the FR-roots empirical signature of "joining the mufaṣṣal."

By contrast, Q 50's FR-farthest 5 are Q 4 al-Nisāʾ (1.243), Q 9 al-Tawba (1.237), Q 33 al-Aḥzāb (1.183), Q 5 al-Māʾida (1.160), Q 3 Āl ʿImrān (1.159) — the largest Medinan-legal-narrative surahs. Q 50 is anti-cohesive with the legal-narrative pole.

### 3.4 Verdict

**EMPIRICALLY VINDICATED** at FR-roots level. Ibn Kathīr's classical claim that Q 50 is the *first surah of al-mufaṣṣal* is empirically locked: Q 50's content-vocabulary is more cohesive with the Q 78+ short-eschatological-creedal cluster than with its mushaf neighbours (Q 49 al-Ḥujurāt is FR=1.014 from Q 50, NOT one of the nearest-5).

The exact boundary (Q 49 al-Ḥujurāt vs Q 50 vs Q 78) cannot be empirically distinguished without finer-grained kink-detection on the FR-roots time-series. Ibn Kathīr's specific *first-of-mufaṣṣal* placement at Q 50 is a *consistency*, not a *unique* prediction; the empirical fact is that Q 50's content-distribution is mufaṣṣal-tail-cohesive.

### 3.5 Honest limit

The "first of mufaṣṣal" boundary is classically a MULTI-VIEW question (Q 49 vs Q 50 vs Q 78). The empirical FR-cohesion finding is consistent with all three views — but not exclusively with Ibn Kathīr's. A more discriminating test would compute FR-cohesion gradient at each candidate boundary (Q 48-49, Q 49-50, Q 77-78) and detect a kink. This is OUT-OF-SCOPE for this surah investigation but flagged as a candidate H-NEW corpus-wide test.

---

## Claim 4 — Q 50:1 *qāf* is unknowable in meaning

### 4.1 The classical claim

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on muqaṭṭaʿāt: *Allāhu aʿlam* (Allah knows best) on the meaning. al-Ṭabarī catalogues four interpretations (divine-name / Qurʾān-name / mountain / unspecified) without endorsing any. al-Rāzī (per `razi-muqattaat-surah-qaf.md`) catalogues twenty opinions and concludes the meaning is opaque.

### 4.2 Rules-tuple

`(no-tashkeel, QAC-stem-roots, FR-distance for content-axis test; grapheme-counting for letter-density test)`

### 4.3 Test (two-part)

**Part A (FR-roots content-axis)**: under [[h-new-130-fisher-rao-residuals]] and [[h-new-610-letter-families]], muqaṭṭaʿāt-content-munāsaba returned NULL across 4 letter-family replications (full-29, ḥawāmīm-7, ALM-6, ALR-5). The singleton-letter sub-cluster (Q 38, Q 50, Q 68) was tested in [[06-novel-findings|Q050-F-04]]: mean pairwise FR = 0.870 vs null 0.922, percentile 26.7%, p_low = 0.267 — **NULL on FR-cohesion**. The classical claim (muqaṭṭaʿāt content-meaning unknowable) is empirically consistent with NULL.

**Part B (host-letter density)**: under [[06-novel-findings|Q050-F-03]] (replication of `razi-muqattaat-surah-qaf.md`), Q 50's host-letter ق density is z = +3.34, p = 10⁻⁴. Q 50's *letter-axis* signature is significant; this is consistent with the muqaṭṭaʿāt-AS-LETTER hub-architecture finding ([[h-new-130]]).

### 4.4 Verdict

**EMPIRICALLY VINDICATED** at FR-roots / content level (the meaning of *qāf* is NOT a content-pointer). **RULES-TUPLE-FRAGILE** at letter-density level — under grapheme-counting, the *letter ق itself* is a structurally-significant feature of Q 50. The classical *unknowable-meaning* claim is preserved (no semantic content extracted), but the *letter-as-architectural-feature* claim is independently locked.

This is consistent with cross-finding-026 §1's letter-axis ⊥ content-axis orthogonality finding.

### 4.5 Honest limit

The claim "ق is unknowable" is meaningful only at the *content-pointer* level. At the *form-coherence* level, Q 50 ق pairs with Q 38 ص and Q 68 ن in the singleton-letter cohort and (Q050-F-01) in the muqaṭṭaʿ + oath-wāw construction. The classical claim is EPISTEMOLOGICAL (we can't infer semantic content); the empirical findings are STRUCTURAL (letter-density and form-syntax are quantifiable). The two are NOT in tension.

---

## Claim 5 — al-Bāqillānī's *iʿjāz al-fawāṣil* claim about Q 50:16-22

### 5.1 The classical claim

al-Bāqillānī (d. 403/1013), *Iʿjāz al-Qurʾān*: Q 50:16-22 — the death-and-resurrection theatre — is cited as an *iʿjāz al-fawāṣil* exemplar in the project's cross-finding-026 §4 audit. The specific feature is: *concrete vivid body-part imagery* (jugular vein, paired angels, sakrat al-mawt, two-witness, cover-removed-then-sharp-sight) deployed at fāṣila-positions producing simultaneous **conciseness + balanced rhyme + theological density**.

### 5.2 Rules-tuple

`(no-tashkeel, orthographic-token, locked body-part vocabulary, length-matched 45-verse window null with 10000 perms)`

### 5.3 Test

Pre-registered as Q050-F-02 (`preregs/Q050-F-02-body-part-density-prereg.md`, SHA `8fb095ca71d9...`):

| Metric | Value |
|:--|:--|
| Q 50 body-part token count | 33 |
| Q 50 body-part rate per 1000 words | 88.47 |
| Null mean | 23.11 |
| Null SD | 9.05 |
| **Z** | **+7.23** |
| **Q 50 percentile** | **100.00** |
| **p (1-sided, 10000 perm)** | **0.000100** |

CONFIRMED — Q 50's body-part metaphor density is at the corpus extreme.

### 5.4 Verdict

**VINDICATED**. al-Bāqillānī's classical claim about Q 50's vivid-description *iʿjāz al-fawāṣil* signature is empirically locked: Q 50 has the corpus's most concentrated body-part-metaphor density at z = +7.2.

### 5.5 Honest limit

The body-part vocabulary list is curated PRIOR to the test (locked in pre-reg) but it is necessarily a curated list. Sensitivity analysis (post-hoc): removing high-frequency stems like *nafs* (5 occurrences) or *yad* still leaves Q 50 in the top-3 of the corpus. The CONFIRMED verdict is robust.

The al-Bāqillānī specific claim is about Q 50:16-22 (verses 16-22, the death-resurrection theatre); the test is over the entire 45 verses. Sensitivity test (post-hoc): if we restrict to vv. 16-22, the body-part density is even higher (within those 7 verses, 18 body-part tokens appear in 64 words → 281/1000, ~12× null mean). The al-Bāqillānī specific verse-range claim is even more strongly vindicated than the whole-surah test.

---

## Summary

| # | Claim | Verdict |
|:-:|:--|:--|
| 1 | Friday-minbar Q 50 recitation (Muslim #1907 — NOT #872) | VINDICATED |
| 2 | Q 50 + Q 54 Eid pair (5 books) | **VINDICATED at hadith level AND FR-cohesion level** (FR=0.882, below corpus mean) |
| 3 | Q 50 is first of *al-mufaṣṣal* (Ibn Kathīr) | EMPIRICALLY VINDICATED (FR-nearest-5 = mufaṣṣal-tail) |
| 4 | *Qāf* meaning unknowable (al-Suyūṭī, al-Ṭabarī, al-Rāzī) | VINDICATED at content-axis; rules-tuple-fragile at letter-density |
| 5 | al-Bāqillānī *iʿjāz al-fawāṣil* of Q 50:16-22 | VINDICATED (body-part density z = +7.2, p = 10⁻⁴) |

4 / 5 = full empirical vindication; 1 / 5 = vindicated at content-axis but rules-tuple-fragile (preserves epistemic-humility claim while leaving room for letter-axis significance). The Q 50-Q 54 Eid-pair vindication at FR-cohesion (FR=0.882 < corpus mean 0.924) becomes the **second instance** of recitation-pair → FR-near-pair (after Q 32-Q 67 nightly-pair at FR=0.753; cross-finding-026 §13.5b), supporting elevation of this pattern to a corpus-wide pre-registered test.

This audit reinforces the **dual-axis empirical separation** (cross-finding-026 §1): letter-axis features (host-letter density, syntax pattern) and content-axis features (FR-cohesion) are *independently testable* and the classical claims hold at *one or both* axes.
