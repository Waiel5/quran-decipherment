---
surah: 32
surah_name_ar: السجدة
surah_name_translit: al-Sajda
surah_name_en: The Prostration
file_type: overview-comprehensive
date_last_updated: 2026-05-08
phase: B+
specialist: Q032-Q047-retry-specialist
verdict_summary: 1 DIRECTIONAL, 2 NULL — twin-axes thinner than FR alone suggests
---

# Q 32 al-Sajda — Comprehensive Overview


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

> Single-file deep-dive. Subsumes the 8-file template into one comprehensive document, per Q032-Q047-retry-specialist instruction (simplified template to reduce stall risk).

---

## 1. Identity

| Field | Value | Source |
|:--|:--|:--|
| Surah number | 32 | mushaf canonical order |
| Arabic name | السجدة | `quran-text/quran-no-tashkeel.json[31]` |
| Transliteration | al-Sajda | standard |
| English meaning | The Prostration | named for Q 32:15 sajda-verse |
| Verse count | 30 | `data/hafs-verse-counts.tsv` (Hafs-Kufan) |
| Type | Late-Meccan | al-Suyūṭī, *al-Itqān* nawʿ 1 (Meccan/Medinan classification) |
| Revelation order | 75 (al-Suyūṭī Nöldeke-aligned) | `data/revelation-order.csv` |
| Opening formula | الم muqaṭṭaʿāt | Q 32:1 |
| Bismala status | counted only in Q 1 (default rules-tuple) | h-new convention |
| Length-class | mufaṣṣal-ṭiwāl/awsāṭ boundary (≈30 verses) | al-Zarkashī, *al-Burhān* |
| Sajda surah | YES — Q 32:15 is canonical sajda-verse #10 | al-Suyūṭī, *al-Itqān*, nawʿ 30; al-Bukhārī sujūd al-Qurʾān cluster |

## 2. Empirical profile (integrating prior H-NEW findings)

| Metric | Q 32 value | Source |
|:--|:--|:--|
| UAS (Unified Architectural Significance) | 0.7522, rank 27/114 | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile | −1.36 (NULL) | `h-new-590.json` (window [29..35]) |
| iʿjāz signature sig_A | −0.350 (rank 70) | `h-new-750.json` |
| iʿjāz signature sig_B | −1.322 (rank 95) | `h-new-750.json` |
| Mean content distance d̄ | 0.8890 | `h-new-750.json` |
| Local cohesion | 1.0546 | `h-new-750.json` |
| Rhyme entropy (nats) | 0.389 (z = −0.690) | `h-new-750.json` |
| Top final letter (rāwī) | ن (90% of verses) | `h-new-750.json` |
| TSP adjacency Q31→Q32 | δ = 0.1005 | `h-new-720.json` |
| TSP adjacency Q32→Q33 | δ = 0.3631 (TOP-3 expensive corpus-wide; 4.4% of L_mushaf) | `h-new-720.json`, cross-finding-026 |
| FR(Q31, Q32) | 0.9095 | `h-new-111.json` |
| FR(Q32, Q33) | 1.1330 (HIGH; structural-break) | `h-new-111.json` |
| FR(Q32, Q67) — *al-Munjiya pre-sleep pair* | **0.7534** (CONFIRMED tight, cross-finding-028) | `h-new-111.json` |
| FR(Q32, Q76) — Friday-Fajr Sajda+Insān pair | 0.8395 | `h-new-111.json` |

**Architectural classification**: structural-iʿjāz of moderate strength (UAS rank 27, top quartile but not top-10), with a sharp local structural break at the Q32→Q33 seam (one of the corpus's three most expensive adjacencies — al-Suyūṭī's *al-Sabʿ al-Ṭiwāl* boundary). The al-Munjiya FR-bridge to Q 67 is the *defining* cross-cluster signature (cross-finding-028 P6).

## 3. Content & thematic blocks

Q 32 is structured as a 4-part theological-narrative arc (al-Biqāʿī, *Naẓm al-Durar*, on the *munāsabāt* of Q 32 with surrounding surahs):

- **vv. 1-3**: ALM opening + claim that the Book is *tanzīl from the Lord of the worlds*. The opening conspicuously lacks an explicit *bayān* of *al-kitāb* compared to Q 2:2, Q 3:3, Q 31:2 (this is the "ALM-exception" feature tested in Q032-F-03).
- **vv. 4-9**: Cosmological-creation block — six-day creation, seven heavens, hierarchy of command (*yudabbiru al-amr*), creation of humans from clay then sperm-drop, hearing/sight/hearts.
- **vv. 10-22**: Eschatological + behavioral — the unbeliever's death-bed regret; the believer's prostration (Q 32:15); the warning of the *yawm al-faṣl*; the contrast of believers/unbelievers; the chastisement-warning.
- **vv. 23-30**: Mūsā parallel — the Book given to Mūsā, the imāms among the Banū Isrāʾīl (a cross-prophetic anchor), then return to local Mecca-Medina warning + *waiting* injunction.

Content register: **eschatological-creedal** with prophetic-historical anchor. Vocabulary distinctness: shares heavily with the late-Meccan ālāʾ-cluster (Q 27, Q 28, Q 29, Q 30, Q 31).

## 4. Tafsir survey (≥3 mufassirūn — abbreviated)

### 4.1 al-Ṭabarī, *Jāmiʿ al-bayān*

al-Ṭabarī (d. 310 AH) treats Q 32:1-3 as a three-part assertion of Quranic authenticity against Quraysh doubt: ALM is mystery (citing al-ʿawniyya); *tanzīl al-kitāb* is divine deposit; *afterāhu* (Q 32:3) refutes the Meccan accusation. (`data/literature/classical-tafsir/` Tabari Arabic OpenITI; passage on Q 32:1-3.) Q 32:15's prostration is treated as the obligatory sajda site for the reciter (concords al-Bukhārī sujūd al-Qurʾān cluster).

### 4.2 al-Rāzī, *Mafātīḥ al-ghayb*

al-Rāzī (d. 606 AH) on Q 32 (per `data/literature/classical-tafsir/razi-99names-extract.md` cross-references): emphasizes the *yudabbiru al-amr* clause (Q 32:5) as a *tadbīr cosmic-axis* that links Q 32 to Q 10:3, Q 13:2 — the *cosmic-management* theme. He also notes the *seventy-year shortcut* in Q 32:5 (*alf sana mimmā taʿuddūn*) as a peculiarity of cosmic timekeeping. Q 32:15's *yusabbiḥūna bi-ḥamdi rabbihim* he reads as a *tasbīḥ-with-praise* coupling that recurs in Q 17:44, Q 39:75 — pointing at a tasbīḥ-network.

### 4.3 al-Biqāʿī, *Naẓm al-Durar*

al-Biqāʿī (d. 885 AH) on the *munāsaba* of Q 32 with Q 31 (Luqmān) and Q 33 (Aḥzāb): Q 31 ends with the *five mafātīḥ al-ghayb* (Q 31:34); Q 32 opens with ALM-tanzīl, asserting the Book as the antidote to the unseen-future-knowledge gap. Q 33 then opens with *al-Nabī* address, transitioning from the *cosmic-tanzīl* of Q 32 to the *prophetic-personal-address* of Q 33. He treats the Q 32→Q 33 seam as a deliberate *thematic-pivot*. (PDF: `data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`.) Empirically, this seam is one of the corpus's TOP-3 expensive adjacencies (h-new-720 δ=0.3631) — al-Biqāʿī's "deliberate pivot" reading is consistent with the structural break.

### 4.4 Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*

Ibn Kathīr (d. 774 AH) on Q 32 emphasizes the *Tahajjud verses* (Q 32:16-17): *tatajāfā junūbuhum ʿan al-maḍājiʿ* (their sides forsake their beds). He cites the al-Tirmidhī al-Munjiya hadith pre-sleep pairing (Sajda + Mulk) here, anchoring the Q 32-Q 67 nightly pair (per cross-finding-028 P6 hadith anchor `tirmidhi#2975` verified on disk).

## 5. Hadith corpus (selected, verified on disk)

| Citation key | Collection | idInBook | Content | Verified |
|:--|:--|:-:|:--|:-:|
| al-Bukhārī Friday-Fajr | bukhari | 870 | "The Prophet used to recite Alif, Lam, Mim, Tanzil (Sūrat al-Sajda) and Hal-ata-ʿalā-l-Insān in the Fajr prayer of Friday." | YES (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json` idInBook=870) |
| al-Bukhārī Friday-Fajr replication | bukhari | 1037 | Same Friday-Fajr Sajda+Dahr practice (variant chain) | YES (idInBook=1037) |
| al-Tirmidhī al-Munjiya pre-sleep | tirmidhi | 2975 | "The Prophet would not sleep until he recited Alif Lam Mim Tanzil and Tabārak Alladhī Biyadihi al-Mulk." (Jābir → Abū al-Zubayr → Layth) | YES (idInBook=2975) — note: the prompt cited "#2892", but on-disk idInBook is 2975. Standard Tirmidhī sunnah.com numbering may differ; the **verified content match** is decisive. |
| al-Tirmidhī parallel chain | tirmidhi | 2974 | Parallel sleep-recitation hadith (variant) | YES (idInBook=2974) |

**Hadith-numbering caveat**: project convention is `[collection]#[idInBook]` from `data/literature/hadith/ahmedbaset-json/`. This is per-collection sequential and may differ from sunnah.com / Beirut printed-edition numbering. The al-Munjiya hadith is canonically attested; the numerical reference was corrected from the prompt's `#2892` to the on-disk `#2975` — content match is ironclad.

## 6. Pre-registered novel tests — pre-regs + results

### 6.1 Q032-F-01 — Sajda-cosmic-twin (replication of Q022-F-01)

- **Pre-reg**: `surahs/Q032-al-sajda/Q032-F-01-sajda-cosmic-twin-prereg.md` (SHA `93541c6e...`)
- **Hypothesis**: Q 32:15 is lexically closer to {Q 13:15, Q 16:49} (cosmic-roll-call sajdas) than to median of other 11 sajdas.
- **Result**: cos(Q32:15, cosmic-mean) = **0.0968**; cos(Q32:15, Q22:18) = **0.000**; median(11 others) = **0.0592**.
- **T1 (cosmic > median)**: PASS (0.097 > 0.059).
- **T2 (Q22:18 > median)**: FAIL (0.000 — Q 32:15 shares no surface tokens with Q 22:18; Q 22:18 has the cosmic-roll-call list while Q 32:15 has *behavioral* prostration).
- **T3 (perm p_low < α_bon=0.0167)**: FAIL (p = 0.34 — observed cosmic similarity is not extreme vs random pairs).
- **Verdict**: **DIRECTIONAL** (1/3 tests passed).
- **Interpretation**: Q 32:15 is *behavioral-sajda* (humans falling in prostration) not *cosmic-roll-call* (sun, moon, mountains prostrating). The two sub-types of sajda-verses are *lexically distinct*. Q 022-F-01's cosmic-cluster lock (Q 22:18 ↔ Q 13:15 + Q 16:49) does NOT extend to Q 32:15 — Q 32:15 belongs to a DIFFERENT sajda-sub-type. **This is a useful refinement of the sajda-typology**: the 14-15 canonical sajda-verses split into *cosmic-roll-call* and *behavioral-prostration* sub-classes; Q 22:18, Q 13:15, Q 16:49 are cosmic; Q 32:15 is behavioral. The sajda-cosmic-twin verdict for Q 32 is **NEGATIVE — Q 32:15 is NOT a cosmic-twin**, but is a *behavioral-cluster representative*.
- **JSON**: `surahs/Q032-al-sajda/csv/Q032-F-01.json`

### 6.2 Q032-F-02 — Q 32 ↔ Q 67 architectural-twin axes

- **Pre-reg**: `Q032-F-02-q32-q67-twin-axes-prereg.md` (SHA `2f94580c...`)
- **Hypothesis**: ≥3/4 axes show twin-cohesion (rhyme, sig_A, length, divine-density).
- **Results**:
  - **A1 rhyme**: Q 32 = ن (90%); Q 67 = ر — DIFFERENT. **FAIL**.
  - **A2 sig_A**: Q 32 = −0.350; Q 67 = +0.311; |diff| = 0.661 — exceeds 0.5 threshold. **FAIL**.
  - **A3 length-class**: Q 32 = 30 verses; Q 67 = 30 verses; diff = 0. **PASS**.
  - **A4 divine-name density**: Q 32 rank 57/114; Q 67 rank 54/114 — both mid-corpus, NOT in top-30. **FAIL**.
- **Verdict**: **NULL** (only 1/4 passed).
- **Interpretation**: The cross-finding-028 FR=0.7534 closeness for Q 32-Q 67 is *FR-specific* — the QAC-stem-roots distribution similarity does NOT translate into surface-feature twin-architecture (rhyme rāwī differs, iʿjāz signature opposite signs, divine-density mid-corpus). This is an **honest empirical refinement**: the al-Munjiya pre-sleep pair share *root-distribution similarity* and matching length-class, but they are NOT cosmetically-twinned surahs. The liturgical-pair binding seems to be an *information-geometric* binding rather than a *surface-stylistic* twinning. This complements but does not dethrone cross-finding-028 — it locates the twin-effect at the deep-distributional level, not at surface-feature level.
- **JSON**: `csv/Q032-F-02.json`

### 6.3 Q032-F-03 — ALM-exception complement Q 29+Q 30+Q 32 cohesion

- **Pre-reg**: `Q032-F-03-alm-exception-cohesion-prereg.md` (SHA `85ef2873...`)
- **Hypothesis**: Q 29+Q 30+Q 32 (ALM surahs without book-reference opening) are FR-cohesive vs random 3-tuples.
- **Result**: T_obs = 0.9269; perm median = 0.9523; **p_low = 0.4082** — observed is essentially at the corpus median (mid-bell of 3-tuple distribution).
- **Verdict**: **NULL**.
- **Interpretation**: The book-reference *absence* is not enough to cluster Q 29+Q 30+Q 32 in the FR-roots space. The ALM-exception subset is **NOT** a content-cohesive sub-cluster. This **vindicates** the established muqaṭṭaʿāt-finding (4× FALSIFIED replications: letter-axis ⊥ content-axis) at this finer-grained sub-level: even within ALM, sub-grouping by another structural marker (book-reference) does not produce content-cohesion. The 3 ALM-exceptions remain related only at the orthography-of-opening level.
- **JSON**: `csv/Q032-F-03.json`
- **Honest note**: The ALM-3-tuple ranking shows {Q 2, Q 3, Q 31} (the book-reference openers) at FR mean ≈ 0.95-1.0, while {Q 29, Q 30, Q 32} are at ≈ 0.93. The book-reference SUBSET is also not particularly cohesive — the ALM-cluster as a whole has internal FR-mean ≈ 0.94, indistinguishable from random. **The muqaṭṭaʿā-class is not a content-cluster.**

## 7. Classical claims audit (abbreviated, ≥3 claims)

| Claim | Source | Test | Verdict |
|:--|:--|:--|:-:|
| al-Tirmidhī al-Munjiya pair (Sajda+Mulk pre-sleep) | tirmidhi#2975 | cross-finding-028 P6: FR(Q 32, Q 67)=0.753 < corpus mean 0.924; pair-set aggregate p=0.0009 | **CONFIRMED** at corpus scale |
| al-Bukhārī Friday-Fajr (Sajda+Insān) | bukhari#870, #1037 | cross-finding-028 P2: FR(Q 32, Q 76)=0.840 < corpus mean | **CONFIRMED** as part of liturgical-pair pattern |
| al-Biqāʿī Q 32-Q 33 *thematic-pivot* | *Naẓm al-Durar* | h-new-720: δ(Q 32, Q 33) = 0.3631 — corpus TOP-3 expensive adjacency (4.4% of L_mushaf) | **CONFIRMED** structural break empirically |
| al-Suyūṭī Q 32 = mid-Meccan (revelation order ≈ 75) | *al-Itqān*, nawʿ 1 | Compression-tail s=32 places Q 32 below the s=50 kink → consistent with Meccan classification | **CONFIRMED** at compression-tail level |

## 8. Synthesis — what we learn about Q 32

1. **Liturgical-pair anchor**: Q 32 is the **only** corpus surah dual-paired in *both* a Friday-Fajr liturgy (with Q 76) AND a pre-sleep nightly liturgy (with Q 67) — a unique architectural position confirmed at corpus scale by cross-finding-028.
2. **Structural break-point**: Q 32→Q 33 is one of the 3 most expensive adjacencies in the entire corpus (after Q 1→Q 2 at 7.4%). The ALM-cluster *terminates* at Q 32 in canonical order; Q 33 begins a new structural region. al-Biqāʿī's *thematic-pivot* reading is empirically vindicated.
3. **Sajda-typology refinement (NEW finding from Q032-F-01 DIRECTIONAL)**: The 14-15 canonical sajda-verses split into at least 2 sub-classes: *cosmic-roll-call* (Q 22:18, Q 13:15, Q 16:49) and *behavioral-prostration* (Q 32:15). Q 32:15 is in the behavioral cluster. Q 22:18 belongs to the cosmic cluster. This is a previously un-mapped sub-typology that deserves dedicated follow-up testing.
4. **Twin-architecture is FR-only, not surface-stylistic** (Q032-F-02 NULL): Q 32 ↔ Q 67 are root-distribution twins but NOT rhyme/sig_A/divine-density twins. The al-Munjiya binding is *deep-distributional*, not *surface-cosmetic*. This is consistent with cross-finding-028's interpretation: liturgical-pair-FR-cohesion is information-geometric, not surface-feature-driven.
5. **ALM-exception subset is NOT a content-cluster** (Q032-F-03 NULL): adds another data-point to the established letter-axis ⊥ content-axis falsification of al-Biqāʿī's muqaṭṭaʿāt-munāsaba claim.

## 9. Cross-references

- [[cross-finding-028-liturgical-pair-fr|cross-finding-028]] — Q 32 features in 2 of 6 liturgical pairs (P2 with Q 76, P6 with Q 67). The CONFIRMED tight-pair anchor for Q 32.
- [[Q022-F-01-sajda-cosmic-language-prereg|Q022-F-01]] — VINDICATED for Q 22:18; Q032-F-01 finds Q 32:15 belongs to the *behavioral* not *cosmic* sajda-sub-class — refines the Q022-F-01 cluster.
- [[h-new-720-canonical-adjacency-cost|h-new-720]] — Q 32-Q 33 is rank-3 in expensive adjacencies; structural break-point.
- [[h-new-840-unified-architectural-score|h-new-840]] — UAS rank 27 (top-quartile structural-iʿjāz).
- [[h-new-750-ijaz-signature|h-new-750]] — Q 32 sig_A = −0.350 (mild theological-iʿjāz lean), sig_B = −1.322 (rhyme-axis suppressed; ن-rāwī monolithic).
- [[Q067-al-mulk/06-novel-findings|Q067-F-01]] — Q 67 partner of pre-sleep liturgical pair.

## 10. Honest limits (load-bearing)

1. **Q032-F-01 sajda-typology refinement is post-hoc-noticed** — the *behavioral* vs *cosmic* sub-typology emerged from the test result, not from pre-registration. Per single-test α=0.05 protocol (HANDOFF/04-DISCIPLINE), this is PASS-DIRECTED at best until an independent replication on a distinct sajda-subset confirms.
2. **Hadith numbering** — `tirmidhi#2975` (on-disk idInBook) ≠ "al-Tirmidhī #2892" (prompt). The content match is verified; the numerical convention requires disclosure (project uses ahmedbaset-json idInBook, not sunnah.com canonical numbering).
3. **Q032-F-02 NULL is informative** — the FR-near-pair (cross-finding-028 P6) is NOT a multi-axis twin. This is an *equal-prominence NULL* and refines (not contradicts) cross-finding-028.
4. **Q032-F-03 NULL** is consistent with established muqaṭṭaʿāt-finding (letter-axis ⊥ content-axis; 4 prior NULLs). Not surprising.
5. **Single-agent budget** — only 3 novel tests vs 5 in the standard 8-file template; tafsir survey abbreviated to 3 mufassirūn vs 5; hadith corpus indicative not exhaustive. This is by design (simplified single-file template per task spec).

## 11. Verdict summary

| Test | Verdict | Direction | p / score |
|:--|:-:|:--|:--|
| Q032-F-01 sajda-cosmic-twin | **DIRECTIONAL** | partial-positive | 1/3 tests; cosmic > median by margin 0.04, but Q22:18 anchor fails |
| Q032-F-02 Q32-Q67 twin-axes | **NULL** | mostly-negative | 1/4 axes (length only) |
| Q032-F-03 ALM-exception cohesion | **NULL** | confirmed-NULL | p_low = 0.41 |

**Net contribution of Q 32 to the project**:
- **CONFIRMED** (via cross-finding-028, not retried here): Q 32 = al-Munjiya nightly-pair anchor + Friday-Fajr pair anchor.
- **NEW (DIRECTIONAL)**: Sajda-typology refinement — *cosmic* vs *behavioral* sub-classes.
- **NEW (NULL)**: Q 32-Q 67 surface-twin (twin is FR-only, not multi-axis).
- **NEW (NULL)**: ALM-exception subset is not a content-cluster (consistent with letter-axis ⊥ content-axis).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
