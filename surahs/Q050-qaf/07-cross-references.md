---
surah: 50
surah_name_ar: ق
surah_name_translit: Qāf
file_type: cross-references
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE
---

# Q 50 Qāf — Cross-References


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

## 1. Mushaf neighbours

| Adjacency | δ (Fisher-Rao) | Rank | Note |
|:--|:--|:--|:--|
| Q 49 al-Ḥujurāt → Q 50 Qāf | **0.177** | rank 17 / 113 | top-15% expensive; Medinan→Meccan + social-conduct→eschatology jump |
| Q 50 Qāf → Q 51 al-Dhāriyāt | **0.119** | rank 25 / 113 | mid-cost; both Middle-Meccan eschatological oath-openers |

Source: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency`. Q 50 sits at a **chronology-and-register transition** point on its left side; the right side is a smoother continuation of the Middle-Meccan eschatological-oath cluster.

## 2. The singleton-letter cohort (Q 38, Q 50, Q 68)

| Surah | Opener | Verses | Rev. order | Noldeke phase | Rāwī | UAS rank | sig_A |
|:-:|:-:|:-:|:-:|:--|:-:|:-:|:--|
| **Q 38** | ص (Ṣād) | 88 | #38 | Middle Meccan | ب (40%) | 59/114 | +1.286 |
| **Q 50** | ق (Qāf) | 45 | #34 | Middle Meccan | د (60%) | 40/114 | +0.891 |
| **Q 68** | ن (Nūn) | 52 | #2 | Early Meccan | ن (81%) | 76/114 | -0.413 |

Cohort coherence axes (per Q050-F-01..F-05):
- **Form** (verse-1 syntax): COHERENT (3/3 muqaṭṭaʿ + oath-wāw + al-)
- **Content** (FR-roots): NOT COHERENT (NULL at p=0.27, percentile 26.7)
- **Rāwī** (opener-rāwī alignment): NOT COHERENT (1/3 = baseline)

## 3. Adjacency cluster (Q 47-Q 53)

The Q 50 outlier-strength window (per H-NEW-590) is [Q 47, 48, 49, 50, 51, 52, 53]:

- Q 47 Muḥammad — Medinan, social-political (51 verses)
- Q 48 al-Fatḥ — Medinan, military-victory (29 verses)
- Q 49 al-Ḥujurāt — Medinan, social-conduct (18 verses)
- **Q 50 Qāf** — Meccan, eschatological-creedal (45 verses)
- Q 51 al-Dhāriyāt — Meccan, eschatological-oath (60 verses)
- Q 52 al-Ṭūr — Meccan, eschatological-oath (49 verses)
- Q 53 al-Najm — Meccan, prophetic-cosmology (62 verses)

Q 50's left context (Q 47-49) is Medinan; its right context (Q 51-53) is Meccan. Q 50 sits at the **Hijra-kink boundary at s=50**.

The +5.42 pp WEAK_OUTLIER status reflects this transition; the local content-distance window-d̄ moves from 0.94 (with Q 50) → 0.94 (without Q 50, marginal change). Q 50 is NOT a STRONG_OUTLIER (which would require Δ ≥ +20 pp like Q 33).

## 4. Compression-tail position

| Law | Equation | Predicted at s=50 | Observed |
|:--|:--|:--|:--|
| Content compression | d̄(s) ≈ 0.96 − 0.012·max(0, s−50) | 0.960 | 0.928 (within 0.04) |
| Rhyme dispersion | d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | 0.360 | rhyme entropy 1.286 nats |
| Phoneme dispersion | d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75) | 0.001 (kink-75 not yet) | — |

Q 50 sits **exactly at the s=50 Hijra-kink** of the compression-tail law (al-Suyūṭī chronology empirical lock; cross-finding-026 §2). The compression-tail prediction at s=50 is at the head-plateau (d̄ = 0.96). Q 50's observed mean_content_distance = 0.928 is slightly below — consistent with FR-roots cohesion to the post-s=75 mufaṣṣal-qiṣār tail (FR-nearest-5 = Q 78, 86, 112, 79, 110).

## 5. FR-nearest 5 + FR-farthest 5

**FR-nearest 5** (Q 50's content-cohesion cluster):

| Rank | Surah | FR | Note |
|:-:|:--|:--|:--|
| 1 | Q 78 al-Nabaʾ | 0.7648 | post-s=75 short eschatological |
| 2 | Q 86 al-Ṭāriq | 0.7815 | post-s=75 short eschatological |
| 3 | Q 112 al-Ikhlāṣ | 0.7963 | terminal-tail creedal |
| 4 | Q 79 al-Nāziʿāt | 0.8022 | post-s=75 short eschatological |
| 5 | Q 110 al-Naṣr | 0.8043 | post-s=75 short closure |

ALL 5 are post-s=75 short surahs. Q 50 is empirically *forward-cohesive* with the mufaṣṣal-tail.

**FR-farthest 5** (Q 50's anti-cohesion):

| Surah | FR |
|:--|:--|
| Q 4 al-Nisāʾ | 1.2434 |
| Q 9 al-Tawba | 1.2375 |
| Q 33 al-Aḥzāb | 1.1835 |
| Q 5 al-Māʾida | 1.1598 |
| Q 3 Āl ʿImrān | 1.1589 |

ALL 5 are large Medinan-legal-narrative surahs. Q 50 is empirically *anti-cohesive* with the legal-narrative pole.

## 6. Cluster membership

- *al-mufaṣṣal* (per Ibn Kathīr, *first* surah of) — empirically vindicated at FR-roots.
- *singleton-letter muqaṭṭaʿāt cohort* (with Q 38 ص, Q 68 ن) — form-coherent but not content-coherent.
- *Middle Meccan eschatological-oath cluster* (with Q 51, 52, 53) — content-cohesive within window.
- *Friday/Eid/Fajr recitation tradition* (with Q 32, 36, 67, 18, 112, 18) — high *fadāʾil*-density tradition.

## 7. Verse-twin / cross-surah verse references

Q 50:38 (six-day creation) ↔ doctrinal parallels at Q 7:54, Q 10:3, Q 11:7, Q 25:59, Q 32:4, Q 41:9-12, Q 57:4. (Note: Q 50:38 is the lone verse classified by Ibn ʿAbbās + Qatāda as Medinan; the surah is otherwise unanimously Meccan per al-Ḥasan, ʿAṭāʾ, ʿIkrima, Jābir.)

Q 50:30 (*hal min mazīd*) ↔ doctrinal parallel at Q 7:18, Q 11:119, Q 32:13 (Hell will be filled with mankind and jinn).

Q 50:1 (singleton-letter + oath-wāw) ↔ Q 38:1 (ص + oath-wāw), Q 68:1 (ن + oath-wāw). Per Q050-F-01 these are EXACTLY the 3 muqaṭṭaʿāt-opener verses with this construction.

Q 50:45 (*fa-dhakkir bi-l-Qurʾāni man yakhāfu waʿīd*) ↔ Q 51:55, Q 87:9, Q 88:21 (the *fa-dhakkir* family of late-Meccan closures).

Q 50:16 (*ḥabl al-warīd*) — corpus-singleton phrase (no other verse in the Quran uses this body-part metaphor; verified by direct corpus enumeration). This is a *unique-to-Q-50* lexical mark.

## 8. Role in cross-finding syntheses

| Cross-finding | Q 50's role |
|:--|:--|
| [[cross-finding-001-muqattaat-overview]] | Q 50 is one of 14 muqaṭṭaʿāt opener letters (the singleton ق); part of the 29-surah opener cohort. |
| [[cross-finding-008-muqattaat-book-reference]] | Q 50 is the COUNTER-EXAMPLE to the dominant 23/29 muqaṭṭaʿāt + book-reference pattern; instead Q 50 (with Q 38, Q 68) follows the complementary 3/29 muqaṭṭaʿāt + oath-wāw pattern. |
| [[cross-finding-011-mushaf-fisher-rao-confirmed]] | Q 50 is FR-roots-cohesive with mufaṣṣal-tail (Q 78+); contributes to the TSP-residual decomposition's al-mufaṣṣal cluster. |
| [[cross-finding-026-iʿjāz-architecture]] §13.6 | Q 50 = *iʿjāz-al-fawāṣil-pure* cell exemplar (sig_A = +0.891 positive, mid-UAS, body-part density extreme); also DUAL-CELL with *iʿjāz-al-maʿnā (mild)* via high *fadāʾil* density. |
| [[cross-finding-027-ijaz-al-takrir]] | Q 50 NOT a *takrīr-iʿjāz* candidate (refrain density not corpus-extreme; *waʿīd* refrain 4× is moderate). |

## 9. H-NEW links (full inventory)

| H-NEW | Q 50 metric |
|:--|:--|
| H-NEW-111 | mean_d = 0.928; nearest = Q 78 (0.765); farthest = Q 4 (1.243) |
| H-NEW-130 | host-letter ق density z = +3.34 (replicated under locked rules-tuple) |
| H-NEW-590 | +5.42 pp WEAK_OUTLIER; rank 13/114 by abs_outlier |
| H-NEW-610 | letter-family content-cohesion NULL (extends to singleton-letter cohort, Q050-F-04) |
| H-NEW-660 | s=50 Hijra-kink position; predicted 0.96, observed 0.928 (within 0.04) |
| H-NEW-700 | rhyme entropy 1.286 nats, top letter د (60%); phoneme density data not extracted |
| H-NEW-720 | Q 49→50 = 0.177 (rank 17); Q 50→51 = 0.119 (rank 25) |
| H-NEW-750 | sig_A = +0.891, rank 37/114; sig_B = +0.316, rank 50/114 |
| H-NEW-840 | UAS = 0.380, rank 40/114 (mid-pack) |
| H-NEW-860 | high *fadāʾil*-recitation density (Friday, Eid, Fajr) consistent with mid-UAS pattern |

## 10. Future test candidates flagged

1. **H-NEW-1010-CANDIDATE** (Singleton-letter cohort verse-1 form-coherence): elevate Q050-F-01 to corpus-wide; tighten tokenization to test 3/29 vs 4/29 (with Q 36 yā-sīn).
2. **CROSS-FINDING-028-CANDIDATE** (Recitation-pair → FR-near-pair conjecture): Q 50/Q 54 Eid-pair (FR=0.882) + Q 32/Q 67 nightly-pair (FR=0.753) + systematic search for other recitation-pair traditions; corpus-wide test.
3. **al-mufaṣṣal-onset-FR-kink test**: locate the FR-roots-cohesion kink at the Q 49 / Q 50 / Q 78 boundaries to discriminate Ibn Kathīr's *first-of-mufaṣṣal* placement at Q 50 vs alternative views.
4. **Q 050:16 *ḥabl al-warīd* corpus-singleton phrase audit**: pre-register exact-substring search across the Quran for the *ḥabl* + *warīd* construction (predicted: 1 occurrence only, at Q 50:16).
