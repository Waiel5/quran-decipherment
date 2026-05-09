---
surah: 68
surah_name_ar: القلم
surah_name_translit: al-Qalam
surah_name_english: "The Pen"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — Nūn-singleton CORPUS-EXACT (1/29 muqaṭṭaʿāt); Q 96↔Q 68 FR-pair UNIDIRECTIONAL (Q 96 in Q 68's top-15, Q 68 NOT in Q 96's top-15 — honest pre-commit transparency); singleton-triplet FR-cluster NULL-LM (double-replicates Q050-F-04 NULL under length-matched null); 8 pre-registered tests run (Q068-F-01 through Q068-F-08).
---

# Q 68 al-Qalam — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 68 | canonical |
| Arabic name | القلم | canonical |
| Transliteration | al-Qalam | canonical |
| English meaning | The Pen | classical |
| Verse count | 52 | Hafs-Kufan (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` Q 68 record `total_verses`) |
| Position in mushaf | 68 | canonical |
| Type | Meccan | classical consensus (al-Suyūṭī, *al-Itqān*, nawʿ on Meccan/Medinan; al-Qurṭubī, opening of Sūrat al-Qalam) |
| Position in revelation order (al-Suyūṭī chronology) | 2 / 114 (after Q 96 al-ʿAlaq) | `/Users/grey/Downloads/quran/data/revelation-order.csv` |
| Position in revelation order (Nöldeke) | 2 (Early Meccan, First Period) | same source |
| Total QAC root-tokens | 508 | computed `Q068_F_06_qlm_density_rank.py` (`q68_root_tokens`) |
| Total Arabic letters (no-tashkeel) | 1,289 | computed `Q068_F_02_nun_letter_self_reference.py` (`q68_letter_total`) |
| Opening | `ن ۚ والقلم وما يسطرون` — "Nūn. By the Pen and what they inscribe." | Q 68:1, `quran-no-tashkeel.json` |
| Bismala status | Standard (counted only in Q 1 per default rules-tuple) | Protocol §1.4 |
| Length classification | mufaṣṣal-ṭiwāl (per al-Zarkashī *al-Burhān*, mufaṣṣal tripartition: Q 49→Q 85 ṭiwāl; Q 86→Q 98 awsāṭ; Q 99→Q 114 qiṣār) | classical |

## 2. ⭐ Unique structural property — the corpus-EXACT singleton Nūn-letter muqaṭṭaʿ + qalam-oath combination

Q 68 al-Qalam holds **two simultaneous corpus-EXACT structural distinctions** that no other surah carries:

### 2a. Sole Nūn-letter muqaṭṭaʿ opener (Q068-F-08 sub-test (a) VINDICATED)

Of the 29 muqaṭṭaʿāt-opener surahs in the corpus, **exactly one** opens with the single Arabic letter ن: Q 68. Verified by direct enumeration of the 29 muqaṭṭaʿāt verse-1 first-tokens (`csv/Q068-F-08.json` `sub_test_a_nun_uniqueness.nun_openers_found = [68]`).

This places Q 68 in the **singleton-letter muqaṭṭaʿāt cohort** alongside Q 38 (ص Ṣād) and Q 50 (ق Qāf) — the three smallest, most letter-isolated muqaṭṭaʿāt openers in the corpus.

### 2b. Sole muqaṭṭaʿ-letter + qalam-oath verse-1 combination

Q 68:1 *Nūn. wa-l-qalam wa-mā yasṭurūn* is the ONLY verse in the corpus that pairs a muqaṭṭaʿ-letter opening with an immediate oath on the *qalam* (pen). No other muqaṭṭaʿāt-surah swears by the pen in v.1. This is a literary-rhetorical singleton.

The structural significance: Ibn ʿAbbās's classical gloss (al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 68:1; al-Suyūṭī, *al-Durr al-manthūr* on Q 68:1) reads the muqaṭṭaʿ ن as functionally introducing the oath on the pen — the muqaṭṭaʿ + qalam-oath is a CONTENT-BEACON pair. This is empirically verified at the writing-vocabulary-density level in **Q068-F-01** (joint family p=0.0117, **VINDICATED**: see [[06-novel-findings]] §Q068-F-01).

## 3. ⭐ Q 68 ↔ Q 96 al-ʿAlaq — chronology-paired + qalam-paired

Q 68 al-Qalam (revelation #2) is paired with Q 96 al-ʿAlaq (revelation #1) on three shared axes:

1. **Chronology**: Q 96 #1, Q 68 #2 (al-Suyūṭī, *al-Itqān*, nawʿ on chronological order).
2. **Lexical key**: Q 96 v.4 *alladhī ʿallama bi-l-qalam* ("Who taught by the Pen") and Q 68 v.1 *wa-l-qalam* ("By the Pen") — they are 2 of only **4 surahs** in the entire corpus with any *qlm* root token (the other two are Q 3:44 *aqlāmahum* and Q 31:27 *aqlām*). Verified Q068-F-06 (`csv/Q068-F-06.json` `all_surahs_with_qlm_token`).
3. **Iqra-Pen pairing**: classical commentators (al-Ṭabarī on Q 96:1; Ibn Kathīr on Q 68:1) treat the *qalam* in both surahs as a single revelatory-instrumental complex — pen-as-medium of Allah's instruction.

### Empirical pair-test (Q068-F-07)

Direction-locked pre-commit: BIDIRECTIONAL — Q 96 in Q 68's FR-nearest top-15 AND Q 68 in Q 96's FR-nearest top-15.

**Result**:

| Direction | Rank | In top-15? |
|:--|:--|:--|
| Q 96 in Q 68's FR-nearest list | **6** / 113 | YES |
| Q 68 in Q 96's FR-nearest list | **46** / 113 | NO |

`d(Q 68, Q 96) = 0.73241` (verified in both directions, FR is symmetric). Verdict: **VINDICATED-UNIDIRECTIONAL** (one of two pre-committed directions met). The pre-commit BIDIRECTIONAL prediction is HONESTLY VIOLATED on the Q 96 side; reported with full prominence per Protocol §1.3.

### Honest pre-commit interpretation

The asymmetric rank pattern (rank 6 from Q 68's side, rank 46 from Q 96's side) reflects **neighborhood-density differences**. Q 96 (19 verses, position 96) sits in a dense short-mufaṣṣal terminal-tail cluster — Q 96's top-15 is saturated by Q 102, Q 107, Q 108, Q 100, Q 110, Q 106, Q 105, Q 113, Q 112, Q 103, Q 94, Q 111, Q 1, Q 95, Q 99 — almost all post-s=90 short surahs. Q 68 falls outside this saturation. From Q 68's side (52 verses, position 68 = mid-corpus), the neighborhood is sparser and Q 96 is comfortably in the top-15 (rank 6, alongside Q 100, Q 52, Q 105, Q 93, Q 108).

**Cross-finding implication**: this is a **first empirical instance** in the project of a directionally-asymmetric FR-pair where the chronology-shared and lexical-key-shared two surahs are mutually-close on one side but not the other. The asymmetry suggests that FR-pair "closeness" depends on the *neighborhood density* of each surah, not on a symmetric "similarity" property. This is a new cross-reference candidate for **cross-finding-014** (FR-roots-pair structural pairs).

## 4. ⭐ Singleton-letter muqaṭṭaʿāt cohort — content-cohesion DOUBLE-REPLICATION NULL

Q 68 is one of three singleton-letter muqaṭṭaʿāt openers: {Q 38 ص, Q 50 ق, Q 68 ن}. The Q 50 specialist's Q050-F-04 tested the triplet's FR-cohesion against a **random-3-surah null** and found NULL (p_low=0.267). Q068-F-08 sub-test (b) re-tests under a **length-matched null** (triplets drawn only from surahs with verse-count in [22.5, 132], a 51-surah pool) — MW-5 replication on different null distribution.

**Result**: triplet mean pairwise FR = 0.8699; length-matched null mean = 1.043; **p_low = 0.082** (NULL-LM).

This is **DOUBLE-REPLICATION NULL** on singleton-letter FR-cohesion. The singleton-letter cohort is form-coherent (Q050-F-01: all three open with muqaṭṭaʿ + oath-wāw + definite-article) but **NOT content-cohesive** under either random-3-surah OR length-matched nulls. The cohort-coherence is **letter-axis only**, vindicating cross-finding-026 §1 (letter-axis ⊥ content-axis empirical orthogonality) at the singleton-cohort scale under two independent null distributions.

## 5. Empirical architectural profile (Wave 2026-04-28 H-NEW pipeline)

| Metric | Value | Rank | Source |
|:--|:--|:--|:--|
| **UAS rank** | **86 / 114** (bottom-third) | 86 | `h-new-840.json` Q 68 entry, UAS=-1.0074 |
| Outlier-strength Δ-pp | -3.45 | rank 88/114 (cohesion-anchor side) | `h-new-590.json` X=68 (classification = `NULL`) |
| iʿjāz signature sig_A | -0.4131 | rank 74/114 | `h-new-750.json` Q 68 |
| iʿjāz signature sig_B | -0.9339 | rank 78/114 | `h-new-750.json` Q 68 |
| Mean content distance (window) | 0.9139 | z = -0.094 (near corpus mean) | `h-new-750.json` Q 68 |
| Rhyme entropy (Shannon, nats) | 0.4896 | LOW (corpus mean ≈ 1.7) | `h-new-750.json` Q 68 |
| Top final letter (rāwī) | ن | **80.77%** (42/52 verses) | `h-new-750.json` Q 68 |
| Q 67 → Q 68 adjacency cost (TSP) | 0.0962 (rank 71/113) | low-cost | `h-new-720.json` per_adjacency s=67 |
| Q 68 → Q 69 adjacency cost (TSP) | 0.1328 (rank 50/113) | mid-cost | `h-new-720.json` per_adjacency s=68 |
| FR-roots nearest top-5 | Q 100 (0.7156), Q 52 (0.7175), Q 105 (0.7257), Q 93 (0.7276), Q 108 (0.7320) | mufaṣṣal terminal-tail cluster | `h-new-111.json` |
| FR-roots distance to Q 96 | 0.7324 (rank 6 from Q 68 side) | top-15 | `h-new-111.json` |

Q 68 is **content-cohesive with the late-mufaṣṣal eschatological zone** (Q 100, Q 52, Q 105, Q 93, Q 108) — its FR-nearest-5 are mostly post-s=90 short surahs with one mid-corpus neighbor (Q 52). Like Q 50 (which is forward-cohesive to Q 78/86/112/79/110), Q 68's content-vocabulary projects **forward** into the mufaṣṣal-qiṣār terminal-tail rather than backward toward its actual mushaf-neighbors Q 67 al-Mulk or Q 69 al-Ḥāqqa. This is the **forward-cohesion pattern** that characterizes several singleton-letter and short-Meccan surahs.

The **low rhyme entropy (0.490 nats)** is striking: 80.8% of Q 68's verses end in ن. This is one of the lowest rhyme entropies in the corpus and reflects Q 68's tight ن-rāwī pattern (consistent with the opening ن muqaṭṭaʿ — the only singleton-letter surah where opener = dominant rāwī, per Q050-F-05 cohort table).

See [[01-empirical-profile]] for full integration.

## 6. Quick content structure (4 blocks)

Q 68's 52 verses unfold in four thematic blocks (per al-Biqāʿī, *Naẓm al-Durar*, on Sūrat al-Qalam):

- **Block 1 — Oath / affirmation of the Prophet (vv. 1-16)**: Nūn + qalam-oath (v.1); affirmation that the Prophet is not insane (v.2); his great character (*khuluqin ʿaẓīm*, v.4); polemic against an opponent (*ḥallāf mahīn... zanīm*, vv. 10-13); promise of branding on the snout (*sa-nasimuhu ʿalā al-khurṭūm*, v.16).
- **Block 2 — Garden of the two ḥakam (parable of the disinherited orchard-owners) (vv. 17-33)**: *innā balawnāhum ka-mā balawnā aṣḥāba al-jannah* (v.17); they plotted to harvest before the poor (vv. 18-25); a calamity struck at night (v.19); they found their garden destroyed (v.20); they repented (vv. 28-32); *ka-dhālika al-ʿadhāb wa-la-ʿadhābu al-ākhira akbar* (v.33).
- **Block 3 — Judgment-day scene (vv. 34-47)**: contrast believer/rejecter destinies (vv. 34-35); polemic against opponent's hypothetical scripture (vv. 36-41); the leg-uncovering / prostration scene (*yawma yukshafu ʿan sāq*, v.42); humiliation of those who refused to prostrate (vv. 43-47).
- **Block 4 — Yūnus close (vv. 48-52)**: *fa-ṣbir li-ḥukmi rabbika wa-lā takun ka-ṣāḥibi al-ḥūt* (v.48) — be patient and do not be like the companion of the fish (Yūnus); his rescue (vv. 49-50); the closing reminder *wa-mā huwa illā dhikrun li-l-ʿālamīn* (v.52).

See [[02-content-analysis]] for verse-by-verse.

## 7. Classical chronology — revelation #2 (the qalam-iqra pair)

Q 68 is universally placed by classical chronologists (al-Suyūṭī, *al-Itqān*, nawʿ on chronological order, ḥadīth #4–8; Nöldeke; Egyptian standard) as the **2nd surah revealed**, immediately after Q 96 al-ʿAlaq (revelation #1, the *iqraʾ* surah).

Both surahs are short Meccan units of the First Period (Nöldeke) / Early Meccan (al-Suyūṭī). The chronological pair-status, combined with the shared *qlm* lexical key and the *iqraʾ* / *qalam* thematic complex, makes Q 68 ↔ Q 96 the most evidenced chronological-pair in the early Meccan corpus.

See [[05-classical-claims-audit]] for the classical chronology audit and [[07-cross-references]] for the cross-finding-008 + cross-finding-014 integrations.

## 8. The "pen wrote everything" hadith — classical anchor

The *qalam* in Q 68:1 is the interpretive anchor for the classical "pen wrote everything" tradition: *inna awwala mā khalaqa Allāhu al-qalama fa-qāla lahu uktub fa-jarā bi-mā huwa kāʾin* ("Verily the first of what Allah created was the Pen. He said: 'Write.' So it wrote what will be."). Verified at:

- **Tirmidhī #3403** (chapter 47, *Sunan al-Tirmidhī*, *Tafsīr al-Qurʾān* commentary section, Q 68 commentary) — al-Walīd b. ʿUbāda b. al-Ṣāmit on the authority of his father.
- **Abū Dāwūd #4702** (chapter 42, *Sunan Abī Dāwūd*, *Kitāb al-Sunna*, *bāb fī al-qadar*) — same Walīd / ʿUbāda chain.
- **Tirmidhī #2223** (chapter 32, *Sunan al-Tirmidhī*, *Kitāb al-Qadar*) — ʿAbd al-Wāḥid b. Sulaym citing ʿAṭāʾ b. Abī Rabāḥ.

These are the project's primary-source-verified hadith citations on the "pen wrote everything" complex. See [[04-hadith-corpus]] for full chains and grading notes. **Pre-existing brief reference to "Aḥmad Musnad, Tirmidhī" is corrected**: the canonical sources are al-Tirmidhī (#3403 + #2223) and Abū Dāwūd (#4702); the Aḥmad *Musnad* corresponding chain is in the Walīd b. ʿUbāda b. al-Ṣāmit tradition but not located by substring match in the digitized `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/.../ahmed.json` corpus (NULL-DATA-GAP for direct Aḥmad citation; the Tirmidhī + Abū Dāwūd attestations are sufficient).

## 9. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 8 pre-registered tests (Q068-F-01 through Q068-F-08) with locked pre-regs + SHA-verified scripts + JSON outputs

## 10. Pre-reg / script / JSON inventory

| ID | Pre-reg SHA256 (head 12) | Script | JSON | Verdict |
|:--|:--|:--|:--|:--|
| Q068-F-01 | `052e5de24459` | `Q068_F_01_writing_vocabulary_density.py` | `Q068-F-01.json` | **VINDICATED** (joint p=0.0117; sTr passes Bonferroni-6) |
| Q068-F-02 | `506e0277dc25` | `Q068_F_02_nun_letter_self_reference.py` | `Q068-F-02.json` | **DIRECTIONAL** (p_perm=0.069; binom p=0.008) |
| Q068-F-03 | `ce90bfc4654b` | `Q068_F_03_singleton_cluster_wordlength_rootrarity.py` | `Q068-F-03.json` | **CLUSTER-NULL** on word-length and root-rarity |
| Q068-F-04 | `5df62b113d24` | `Q068_F_04_garden_owners_parable_isolation.py` | `Q068-F-04.json` | **NULL** (parable IS isolated but not corpus-extreme) |
| Q068-F-05 | `7b5e8990c846` | `Q068_F_05_pen_inkwell_hadith_intersection.py` | `Q068-F-05.json` | **NULL_DIRECTION_REVERSED** (Q 68:1 cited 0× in 9-book corpus by substring matching) |
| Q068-F-06 | `497822f6f771` | `Q068_F_06_qlm_density_rank.py` | `Q068-F-06.json` | **VINDICATED-TOP-3** (Q 68 rank 2; Q 96 rank 1) |
| Q068-F-07 | `c3154905fbd2` | `Q068_F_07_q68_q96_fr_pair.py` | `Q068-F-07.json` | **VINDICATED-UNIDIRECTIONAL** (Q 96 rank 6 in Q 68's nearest; Q 68 rank 46 in Q 96's nearest) |
| Q068-F-08 | `9cea3e52629e` | `Q068_F_08_nun_singleton_cluster_length_matched.py` | `Q068-F-08.json` | **VINDICATED + NULL-LM** (Nūn-opener unique; FR-cluster double-replication NULL) |
