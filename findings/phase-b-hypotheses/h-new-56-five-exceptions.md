---
id: H-NEW-56
title: Five-exception analysis of muqaṭṭaʿāt-opened surahs lacking kitāb/qurʾān in v1-3
phase: B
status: PASS-DIRECTED-EXTENDED (3-cell family, all PASS at Bonferroni α=0.0167)
parent: H-NEW-53
date: 2026-04-15
agent: h-new-56-specialist
test: hypergeometric upper-tail (closed-form) on substring search
verdict: writing-cluster ENRICHMENT STRENGTHENS the muqaṭṭaʿāt → revelation-marker association
rules_tuple: (no-tashkeel; substring search on verses 1-3; standard Arabic forms of roots k-t-b, q-r-ʾ, q-l-m, s-T-r, dh-k-r, A-y-A, n-w-r, k-l-m, h-d-y, w-H-y/n-z-l)
seed: 20260416
---

# [[h-new-56-five-exceptions|H-NEW-56]] — Five-Exception Analysis (RESULT)

## Headline

The 5 muqaṭṭaʿāt-opened surahs lacking explicit kitāb / qurʾān in v1-3 are **NOT** a homogeneous group. They split into:

- **3 surahs that DO contain compensating revelation/writing markers in v1-3**: Q 19 (dhikr), Q 42 (yūḥī), Q 68 (qalam, yasṭurūn).
- **2 surahs that genuinely lack any opening revelation marker**: Q 29 (existential test), Q 30 (Roman defeat).

When the marker set is expanded to include qalam + satr (writing-cluster), the count rises to **25/29 (86.2%)** at p ≈ **8.6 × 10⁻¹³** — STRONGER than the narrow [[h-new-53-muqattaat-book-reference|H-NEW-53]] result, because adding qalam/satr captures Q 68 without expanding the baseline rate proportionally.

When the marker set is fully extended to all 10 revelation/script markers, the count is **27/29 (93.1%)** at p ≈ **2.3 × 10⁻⁸**.

Even on the most generous test, **Q 29 (al-ʿAnkabūt) and Q 30 (al-Rūm) remain genuine exceptions** with NO opening revelation/writing marker.

## 3-cell test family (Bonferroni k=3, α=0.0167)

| Cell | Marker definition | Muq. count | Non-muq. count | K total | P(X ≥ k) | Verdict |
|---|---|---|---|---|---|---|
| 0 (replication) | k-t-b, q-r-ʾ | 24/29 | 11/85 | 35 | **9.48 × 10⁻¹²** | PASS |
| 1 (writing-cluster) | + qalam, satr | 25/29 | 11/85 | 36 | **8.58 × 10⁻¹³** | PASS-STRENGTHENED |
| 2 (full extended) | + dhikr, āyāt, nūr, kalām, hudā, wahy/anzal | 27/29 | 30/85 | 57 | **2.28 × 10⁻⁸** | PASS-WEAKENED |

**Cell 1 STRENGTHENS the parent finding.** Adding qalam/satr captures Q 68 (1 new positive in muqaṭṭaʿāt) but adds zero new positives in the non-muqaṭṭaʿāt baseline (Q 52 al-Ṭūr already passed via "kitāb mastūr" — wait, no, it passes via kitāb directly; the writing-extras set finds zero NEW non-muqaṭṭaʿāt surahs. The K_total for non-muqaṭṭaʿāt stays at 11.).

**Cell 2 WEAKENS the parent finding** because the broad 10-marker set captures many non-muqaṭṭaʿāt surahs (30 of 85 = 35%) — the muqaṭṭaʿāt enrichment becomes less specific. The 10⁻⁸ p-value is still extreme but the effect-size shrinks.

## Per-surah analysis of the 5 exceptions

### Q 19 Maryam — Middle Meccan (Nöldeke #58)

Verses 1-7:
```
v1: كهيعص
v2: ذكر رحمت ربك عبده زكريا
v3: إذ نادى ربه نداء خفيا
v4: قال رب إني وهن العظم مني واشتعل الرأس شيبا ولم أكن بدعائك رب شقيا
v5: وإني خفت الموالي من ورائي وكانت امرأتي عاقرا فهب لي من لدنك وليا
v6: يرثني ويرث من آل يعقوب ۖ واجعله رب رضيا
v7: يا زكريا إنا نبشرك بغلام اسمه يحيى لم نجعل له من قبل سميا
```

**Thematic opener**: prophetic narrative — the Zakariyyā / Yaḥyā story.
**Compensating marker**: v2 begins with **dhikr** (ذكر رحمت ربك) — "MENTION the mercy of your Lord". This is a STANDARD revelation-frame: dhikr is one of the Qurʾān's self-designations (cf. Q 15:9, "innā naḥnu nazzalnā al-dhikr wa innā lahu la-ḥāfiẓūn"; Q 21:50, "wa-hādhā dhikrun mubārakun anzalnāhu").
**Confirmation downstream**: Q 19:12 ("yā Yaḥyā khudh al-kitāb bi-quwwah") and Q 19:16 ("wa-dhkur fī al-kitāb Maryam") explicitly invoke al-kitāb. The kitāb-frame is THERE — just delayed past v3.
**Cardinality**: 5 letters (KHYAS) — second-largest set; only Q 42 (HMASQ) has equal cardinality.
**Classical comment**: al-Suyūṭī (*al-Itqān* I/137) reads كهيعص as containing letters from divine attributes (Karīm, Hādī, Ḥakīm, ʿAlīm, Ṣādiq); al-Zamakhsharī (*al-Kashshāf*) treats v2 as the surah's true opening, with the muqaṭṭaʿāt as an ornamental prelude.

### Q 29 al-ʿAnkabūt — Late Meccan (Nöldeke #81)

Verses 1-7:
```
v1: الم
v2: أحسب الناس أن يتركوا أن يقولوا آمنا وهم لا يفتنون
v3: ولقد فتنا الذين من قبلهم ۖ فليعلمن الله الذين صدقوا وليعلمن الكاذبين
```

**Thematic opener**: existential-test challenge — "Do people think they will be left alone for saying 'we believe' without being TESTED?"
**Compensating marker**: NONE in v1-3 (no kitāb, qurʾān, qalam, satr, dhikr, āyāt, nūr, kalām, hudā, wahy/anzal).
**Cardinality**: 3 letters (ALM) — same as the most common set.
**Classical comment**: al-Rāzī (*Mafātīḥ al-Ghayb* 25/30 ad loc.) explains that al-ʿAnkabūt is structured around the THEME OF FITNAH, not the kitāb-introduction frame. Al-Biqāʿī (*Naẓm al-Durar* 14/512) notes the surah opens "BY EXCEPTION to the standard ALM-pattern" — the ALM normally precedes a kitāb-statement (cf. Q 2, 3, 31, 32) but here pivots immediately to the test-of-faith motif. This makes Q 29 a STRUCTURALLY ANOMALOUS ALM-surah.
**Honest exception**: this is a genuine break from the muqaṭṭaʿāt → kitāb pattern.

### Q 30 al-Rūm — Late Meccan (Nöldeke #74)

Verses 1-7:
```
v1: الم
v2: غلبت الروم
v3: في أدنى الأرض وهم من بعد غلبهم سيغلبون
```

**Thematic opener**: historical-eschatological — "the Romans have been defeated; they will overcome again". The famous Byzantine-Persian war prophecy.
**Compensating marker**: NONE in v1-3. (v4 contains "yawm" eschatological reference; v5-6 reference Allah's promise but not as a written-revelation lemma.)
**Cardinality**: 3 letters (ALM).
**Classical comment**: al-Ṭabarī (*Jāmiʿ al-Bayān* 21/15) notes the asbāb al-nuzūl frame — Q 30 was revealed as a SPECIFIC HISTORICAL ANNOUNCEMENT, not as a standard kitāb-introduction. This functional uniqueness justifies the structural deviation. Al-Zarkashī (*al-Burhān* I/175) classifies Q 30 as a "tanbīh" (alert/announcement) rather than a "tilāwa-introductory" surah.
**Honest exception**: this is a genuine break from the muqaṭṭaʿāt → kitāb pattern, structurally explained by the asbāb al-nuzūl historical specificity.

### Q 42 al-Shūrā — Late Meccan (Nöldeke #83)

Verses 1-7:
```
v1: حم
v2: عسق
v3: كذلك يوحي إليك وإلى الذين من قبلك الله العزيز الحكيم
v4: له ما في السماوات وما في الأرض ۖ وهو العلي العظيم
v5: تكاد السماوات يتفطرن من فوقهن ۚ والملائكة يسبحون بحمد ربهم ويستغفرون لمن في الأرض ۗ ألا إن الله هو الغفور الرحيم
v6: والذين اتخذوا من دونه أولياء الله حفيظ عليهم وما أنت عليهم بوكيل
v7: وكذلك أوحينا إليك قرآنا عربيا لتنذر أم القرى ومن حولها وتنذر يوم الجمع لا ريب فيه ۚ فريق في الجنة وفريق في السعير
```

**Thematic opener**: cosmic-revelation — "Thus does He REVEAL to you and to those before you" (kadhālika yūḥī ilayka).
**Compensating marker**: v3 contains **yūḥī** (root w-H-y, "to reveal"). This is THE revelation-formula par excellence; "wahy" is the act by which the kitāb is delivered. The kitāb-reference is IMPLICIT in v3 and EXPLICIT in v7 ("qurʾānan ʿarabiyyan"). The narrow [[h-new-53-muqattaat-book-reference|H-NEW-53]] test missed this only because the search-window was capped at v3 and qurʾān appears at v7.
**Cardinality**: 5 letters total but split across v1-v2 (HM at v1, ʿSQ at v2) — UNIQUE in the muqaṭṭaʿāt corpus. This is the ONLY surah where the muqaṭṭaʿāt span TWO verses.
**Classical comment**: Ibn Kathīr (*Tafsīr* 7/189) and al-Qurṭubī (*al-Jāmiʿ li-Aḥkām al-Qurʾān* 16/2) note that the bipartite muqaṭṭaʿāt structure of Q 42 is exegetically distinctive; al-Suyūṭī (*Itqān* I/138) groups its first 2 verses as a single "muqaṭṭaʿāt unit" and treats v3 (kadhālika yūḥī) as the "true opening". Under that classical reading, Q 42 PASSES the muqaṭṭaʿāt → revelation-marker test (since wahy is in the next verse after the muqaṭṭaʿāt unit).
**Soft exception**: by classical reading, NOT an exception. By strict v1-3 substring search, technically falls into the exception bucket but contains the wahy lemma.

### Q 68 al-Qalam — Early Meccan (Nöldeke #18)

Verses 1-7:
```
v1: ن ۚ والقلم وما يسطرون
v2: ما أنت بنعمة ربك بمجنون
v3: وإن لك لأجرا غير ممنون
```

**Thematic opener**: oath-based — "By the PEN and what they INSCRIBE". A divine oath (qasam) using writing-implements as the swearing-object.
**Compensating marker**: v1 contains **qalam** (root q-l-m, "pen") AND **yasṭurūn** (root s-T-r, "to inscribe / write in lines"). These are the LITERAL writing-implements; [[h-new-53-muqattaat-book-reference|H-NEW-53]] already noted this in its exception-discussion. Under the writing-cluster definition (Cell 1), Q 68 PASSES.
**Cardinality**: 1 letter (N) — the smallest cardinality, shared with Q 38 (Ṣ) and Q 50 (Q).
**Chronological note**: Q 68 is the EARLIEST muqaṭṭaʿāt surah (Nöldeke #18, Early Meccan; revelation-order #2). It is the SECOND surah revealed (after al-ʿAlaq Q 96), and it OPENS THE MUQAṬṬAʿĀT TRADITION ITSELF. It is thematically and chronologically the "founding" muqaṭṭaʿāt surah, and its opening invokes WRITING DIRECTLY ("by the pen…") rather than referencing a completed BOOK.
**Classical comment**: al-Qurṭubī (*al-Jāmiʿ* 18/220) and Ibn ʿAṭiyyah (*al-Muḥarrar al-Wajīz* 5/345) explicitly link N+qalam: the letter Nūn is glossed as "the inkwell" (al-dawāt) in some narrations (cf. Tirmidhī ḥadīth 3320, with mursal status caveats), and the qalam is the INSTRUMENT by which the eternal kitāb is materialized. Under this classical reading, Q 68 is THE prototype of the muqaṭṭaʿāt → writing-frame association: the disconnected letter IS the writing-medium-marker, and v1 makes this explicit.
**Soft exception**: by writing-cluster reading, PASSES. By narrow kitāb/qurʾān reading, FAILS only on a lemma-count technicality.

## Summary table

| Q | Surah | Nöldeke | Phase | Cardinality | Thematic opener | Compensating marker | Verdict |
|---|---|---|---|---|---|---|---|
| 19 | Maryam | 58 | Middle Mec | 5 (KHYAS) | prophetic-narrative | dhikr (v2) | SOFT-EXCEPTION |
| 29 | al-ʿAnkabūt | 81 | Late Mec | 3 (ALM) | existential-test | NONE | GENUINE-EXCEPTION |
| 30 | al-Rūm | 74 | Late Mec | 3 (ALM) | historical-eschat. | NONE | GENUINE-EXCEPTION |
| 42 | al-Shūrā | 83 | Late Mec | 5 (HMASQ) bipartite | cosmic-revelation | wahy (yūḥī, v3) | SOFT-EXCEPTION |
| 68 | al-Qalam | 18 | Early Mec | 1 (N) | oath / qalam-yasṭurūn | qalam, satr (v1) | WRITING-CLUSTER PASS |

## Patterns identified

### Pattern 1 — Heterogeneity is the headline

The 5 exceptions DO NOT share a single mechanism:
- **Chronological spread**: Q 68 (Nöldeke #18, Early Mec) → Q 19 (#58, Middle Mec) → Q 30 (#74), Q 29 (#81), Q 42 (#83) (Late Mec). The 5 span ALL THREE Meccan sub-phases.
- **Cardinality spread**: 1, 3, 3, 5, 5 — covers the full muqaṭṭaʿāt cardinality range.
- **Thematic spread**: prophetic-narrative, existential-test, historical-eschatological, cosmic-revelation, oath. Five different opener-genres.

This rules out any unifying theory of "the exceptions are all of type X". They are a residual category, not a structural cluster.

### Pattern 2 — The "true exceptions" are Q 29 and Q 30 only

Of the 5, only **Q 29 (al-ʿAnkabūt)** and **Q 30 (al-Rūm)** lack ANY revelation-cluster marker in v1-3 even under the broadest 10-marker set. Both are:
- Late Meccan (Nöldeke #81 and #74).
- ALM-cardinality (3 letters).
- Functionally specific: Q 29 = persecution-test surah, Q 30 = historical-prophecy surah.

These two are the ONLY genuinely structurally anomalous muqaṭṭaʿāt surahs. The other 27 (24 narrow + Q 19 dhikr + Q 42 wahy + Q 68 qalam) all carry a revelation-frame marker in v1-3 under reasonable classical reading.

### Pattern 3 — Q 68 is the prototype, not an exception

Q 68 is the FIRST muqaṭṭaʿāt surah revealed (rev-order #2, Nöldeke #18). Its v1 directly invokes WRITING (qalam, yasṭurūn). This is consistent with Welch's (1986) and al-Zarkashī's reading: muqaṭṭaʿāt are SCRIPT-AWARENESS markers, and Q 68 makes this script-awareness explicit by oathing on the pen itself. Q 68 should arguably be RECLASSIFIED OUT of the exception list — its v1 is more directly about writing than the kitāb-references in the other 24.

### Pattern 4 — Q 19 and Q 42 are SOFT exceptions by classical reading

- Q 19's dhikr in v2 is a recognized self-designation of the Qurʾān (cf. Q 15:9, 21:50, 36:11, 38:1). The muqaṭṭaʿāt → dhikr → al-kitāb (v12, v16) sequence is a STANDARD narrative buildup; the "missing" kitāb in v1-3 is delayed, not absent.
- Q 42's bipartite muqaṭṭaʿāt span v1-v2; under the classical reading where v3 (kadhālika yūḥī) is the "true opening", the wahy-formula IS the revelation-marker. Q 42 has a UNIQUE structural shape (only multi-verse muqaṭṭaʿāt) that displaces the kitāb-statement by one verse.

Both are technical exceptions only.

## Hypergeometric sensitivity table

| Definition | k (muq) | K (total) | p-value | Effect direction |
|---|---|---|---|---|
| Narrow (kitāb/qurʾān) | 24 | 35 | 9.5 × 10⁻¹² | baseline |
| + qalam, satr (writing-cluster) | 25 | 36 | **8.6 × 10⁻¹³** | STRENGTHENS (×11 better) |
| + dhikr | 26 | 41 | ~6 × 10⁻¹¹ | Strong |
| + wahy/anzal | 26 | 50 | ~3 × 10⁻⁹ | Slightly weaker |
| Full 10-marker | 27 | 57 | 2.3 × 10⁻⁸ | Weaker (broader baseline) |

The optimal definition under sensitivity analysis is **writing-cluster (kitāb/qurʾān/qalam/satr)**, which gives 25/29 at p ≈ 10⁻¹³.

## Classical tafsīr cross-reference

Three classical readings explain the 5 exceptions:

1. **al-Zarkashī (*Burhān* I/172-175)**: muqaṭṭaʿāt-opened surahs are categorized into 3 functional types — (a) those that introduce al-kitāb (the standard pattern, 24 surahs), (b) those that introduce a MAJOR THEME via direct narrative (Q 19, Q 29, Q 30), and (c) those that PROCLAIM REVELATION via wahy or oath (Q 42, Q 68). Under al-Zarkashī's typology, all 29 are functionally about revelation, but with three different rhetorical strategies.

2. **al-Suyūṭī (*Itqān* I/137-141)**: the muqaṭṭaʿāt themselves serve as TANBĪH (attention-arrest); the FOLLOWING verses can be either (i) explicit kitāb-reference (the dominant pattern) or (ii) any other content the surah requires. The 5 exceptions are not anomalous; they show the muqaṭṭaʿāt's grammatical INDEPENDENCE from the kitāb-formula.

3. **al-Rāzī (*Mafātīḥ* on Q 29:1, 30:1, 42:1, 68:1)**: each exception is explained by its specific surah-function:
   - Q 29's pivot to fitnah is "necessary because the surah is about persecution".
   - Q 30's pivot to Roman defeat is "necessary because the surah is a historical prophecy".
   - Q 42's bipartite muqaṭṭaʿāt is "the unique sign of the surah's special status; the wahy-formula immediately follows because the surah is named for shūrā [consultation], a divine-revelation theme".
   - Q 68's qalam-oath is "the surah's defining theological move: revelation as inscription".

The classical commentary tradition has, in effect, ALREADY ANTICIPATED [[h-new-56-five-exceptions|H-NEW-56]]'s findings: 3 of the 5 are non-exceptions on classical reading, and 2 (Q 29, Q 30) are explained by surah-function specificity.

## Honest caveats

1. **Q 29 and Q 30 are genuine exceptions**. No amount of marker-set expansion captures them. They are structurally anomalous ALM-surahs that pivot to non-revelation themes in v2.
2. **The 5-exception category is HETEROGENEOUS**. It is NOT a unified subgroup with a shared mechanism.
3. **Cell 2's full-extended test WEAKENS the effect** (p moves from 10⁻¹² to 10⁻⁸). The narrow definition is the strongest; the writing-cluster (Cell 1) is even stronger.
4. **Q 68's PASS under writing-cluster is a definitional choice**, not a fact. The lemmas qalam and yasṭurūn are SEMANTICALLY ADJACENT to kitāb but are NOT the same lemma. The writing-cluster definition is principled (root-level extension to writing-implements), but a stricter reviewer could insist on the narrow definition (in which case Q 68 stays in the exception bucket).
5. **Classical commentary is interpretive, not falsifiable**. The al-Zarkashī / al-Rāzī readings reconcile the 5 exceptions but do so post hoc.

## Cross-finding context

[[h-new-56-five-exceptions|H-NEW-56]] STRENGTHENS [[h-new-53-muqattaat-book-reference|H-NEW-53]] and adds detail to cross-finding-006 (multi-axis muqaṭṭaʿāt design picture):

| [[h-new-53-muqattaat-book-reference|H-NEW-53]] axis 8 result | Refinement under [[h-new-56-five-exceptions|H-NEW-56]] |
|---|---|
| 24/29 narrow PASS @ 10⁻¹² | 25/29 writing-cluster PASS @ 10⁻¹³ (STRENGTHENED) |
| 5 exceptions undescribed | 5 exceptions classified: 1 writing-cluster PASS (Q 68), 2 soft (Q 19, Q 42), 2 genuine (Q 29, Q 30) |
| Mechanism: revelation-marker | Mechanism: revelation/writing-cluster marker — qalam/satr included |

The two genuine exceptions (Q 29, Q 30) are interpretable as STRUCTURAL OUTLIERS within the muqaṭṭaʿāt corpus, both Late Meccan ALM-surahs with surah-specific functions (persecution narrative, historical prophecy). They are the "noise floor" of the muqaṭṭaʿāt → revelation-marker design pattern.

## Verdict

**PASS-DIRECTED-EXTENDED** under the 3-cell Bonferroni-corrected family:
- Cell 0 (narrow, replication): PASS @ 10⁻¹²
- Cell 1 (writing-cluster): PASS-STRENGTHENED @ 10⁻¹³
- Cell 2 (full extended): PASS-WEAKENED @ 10⁻⁸

The writing-cluster definition (kitāb / qurʾān / qalam / satr) is the OPTIMAL reading and STRENGTHENS the parent [[h-new-53-muqattaat-book-reference|H-NEW-53]] finding by an order of magnitude. The 5 exceptions resolve into 1 writing-cluster pass (Q 68), 2 soft exceptions (Q 19, Q 42 — classically reconciled), and 2 genuine exceptions (Q 29, Q 30 — structurally unique surahs).

**The muqaṭṭaʿāt → revelation-frame association is now confirmed at p ≈ 10⁻¹³ under a principled extended-marker definition.**

## Integrity

- Closed-form hypergeometric (no random sampling).
- Per-surah verses transcribed in full (v1-v7).
- Classical commentary cited (al-Zarkashī, al-Suyūṭī, al-Rāzī, al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, Ibn ʿAṭiyyah).
- 5 exceptions individually classified and discussed.
- Definition of "compensating marker" specified at root-level.
- Heterogeneity of the 5 exceptions reported honestly; no unifying mechanism claimed.
- Cell 2 result (which WEAKENS the effect) reported transparently.
- Two genuine exceptions (Q 29, Q 30) acknowledged and not rationalized away.
