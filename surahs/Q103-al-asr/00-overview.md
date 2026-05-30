---
surah: 103
surah_name_ar: العصر
surah_name_translit: al-ʿAṣr
surah_name_english: "Time / The Declining Day"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 1 pre-registered 3-arm test landed — Arm A CONFIRMED (minimal-surah rā'-twin) + Arm B DIRECTIONAL (emphatic-iconicity, p=0.070) + Arm C CONFIRMED (minimal tripartite qasam skeleton)
---

# Q 103 al-ʿAṣr — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 103 | canonical |
| Arabic name | العصر | canonical (the sworn object of v 1, *al-ʿaṣr*) |
| Transliteration | al-ʿAṣr | `quran-text/quran-no-tashkeel.json` (id 103, transliteration "Al-'Asr") |
| English meaning | "Time / The Age / The Declining Day / The Afternoon" | the four classical glosses of *ʿaṣr* (al-Ṭabarī, al-Qurṭubī) |
| Verse count | 3 | Hafs-Kufan (`data/hafs-verse-counts.tsv` line 103 = "103⇥3"); al-Qurṭubī "وهي ثلاث آيات" |
| Position in mushaf | 103 | canonical |
| Revelation order | #13 (Tanzil Egyptian Standard); Nöldeke phase "Early Meccan" #21 | `data/revelation-order.csv` (row "13,103,العصر,Al-Asr,Meccan,21,Early Meccan") |
| Type | Meccan ("مكية") by the majority; Qatāda alone said Medinan | al-Qurṭubī on v 1 ("وهي مكية . وقال قتادة مدنية وروي عن ابن عباس"); al-Baghawī "مكية" |
| Word count (no-tashkeel, marks stripped) | 14 | computed (`scripts/Q103_F_01_asr_minimal.py` pipeline) |
| Letter count (no-tashkeel) | 73 (v1=6, v2=15, v3=52) | computed |
| Distinct QAC roots | 9 (10 root-tokens; w-ṣ-y appears twice) | `data/morphology/quranic-corpus-morphology-0.4.txt` surah-103 lines |
| Opening | والعصر — wāw-qasam (oath) | the *wa-l-ʿaṣr* temporal oath (H-NEW-2210 cluster, kind "waaw") |
| Bismala status | not counted as a verse (Hafs-Kufan; counted only in Q 1) | rules-tuple |
| Predominant rhyme (rāwī) | ر (rā'), 3/3 verses — **perfect monorhyme**, entropy 0.0 nats | `h-new-750.json` (Q103: rhyme_entropy_nats 0.0, top_final_letter ر, frac 1.0) |
| Length class | al-mufaṣṣal qiṣār (the short detached surahs; one of the three 3-verse surahs) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 103 matters for the project

1. **The minimal-architecture exemplar.** At 3 verses / 14 words / 73 letters, Q 103 is one of the
   corpus's shortest surahs, yet it carries a complete tripartite rhetorical arc: **oath →
   answer-of-oath → exception** (*wa-l-ʿaṣr* → *inna al-insāna la-fī khusr* → *illā alladhīna āmanū…*).
   It is the cleanest test-bed in the corpus for the question al-Shāfiʿī raised qualitatively
   («لو تدبر الناس هذه السورة لوسعتهم» — "if people pondered this surah it would suffice them",
   Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 103): maximal meaning in minimal form.

2. **A matched minimal-surah rā'-twin (Q103-F-01 Arm A, CONFIRMED).** Of the corpus's exactly three
   3-verse surahs {Q 103 al-ʿAṣr, Q 108 al-Kawthar, Q 110 al-Naṣr}, **exactly two — Q 103 and Q 108 —
   are perfect rā'-monorhymes** (every verse-final letter = ر). And Q 108 al-Kawthar is Q 103's
   **rank-1 Fisher-Rao nearest neighbor** (FR 0.2399 of 113). The two shortest rā'-rhyming surahs are
   also each other's closest content-geometry neighbours — a minimal-surah structural twin.

3. **Corpus #2 in emphatic (istiʿlāʾ) density (Q103-F-01 Arm B, DIRECTIONAL).** H-NEW-2340 ranks
   Q 103 **#2 of all 114 surahs in heavy-istiʿlāʾ letter density (0.0959)**, behind only Q 113
   al-Falaq (0.1212). The emphatic load is **ṣād-driven** (5 of 7 heavy letters are ص), carried by the
   surah's lexical spine — al-ʿa**Ṣ**r, al-**Ṣ**āliḥāt, al-**Ṣ**abr. The phonetic "heaviness" of the
   surah about loss (khusr) and patience (ṣabr) is in the locked direction (z = +1.83) but does **not**
   clear α = 0.05 against a length-matched corpus-window null (p_perm = 0.070) — honest **DIRECTIONAL**.

4. **A minimal tripartite qasam skeleton (Q103-F-01 Arm C, CONFIRMED).** Per H-NEW-2210, Q 103's
   wāw-oath on a *temporal* sworn object is answered (jawāb, inna) at v 2 — **qasam→jawāb verse-distance
   = 1**, the minimal value (11 of 44 corpus qasam-clusters share this) — and v 3 opens with the
   exception particle *illā* (QAC POS:EXP at 103:3:1:1). Its `local_cohesion` (H-NEW-750) is **rank
   10/114** (top decile), and its rhyme entropy is the corpus floor (0.0). Q 103 is one of the most
   locally-self-cohesive surahs in the corpus despite — or because of — its brevity.

5. **A low-UAS "anti-iʿjāz" / FR-dense surah (honest counter-weight).** Q 103's UAS is rank **106/114**
   (H-NEW-840) — the protocol's §3.3 bottom-10 list includes Q 103. Its content-FR mean is 0.787 (far
   below corpus 0.9235), its outlier-strength is NULL (delta_pct 0.0, H-NEW-590), and its TSP seams are
   cheap. By the project's whole-surah-dispersion instruments Q 103 is architecturally *quiet*; its
   interest is **micro-structural and phonological**, not dispersion-extreme. This is the same
   structural-vs-theological-iʿjāz orthogonality the project has documented (al-Khaṭṭābī *iʿjāz
   al-maʿnā* vs al-Bāqillānī *iʿjāz al-fawāṣil*): a surah classical scholars revered for its *meaning*
   sits low on the structural-dispersion axis.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.787 (well below corpus mean 0.9235) | `h-new-111.json` (Q103 row) |
| Top-3 FR neighbors | Q 108 (0.240), Q 106 (0.263), Q 111 (0.280) | `h-new-111.json` |
| 5 farthest | Q 2, Q 6, Q 4, Q 9, Q 3 (the long Medinan surahs) | `h-new-111.json` |
| Q 102 (prev) rank in Q 103's FR list | 15/113 (FR 0.3448) | `h-new-111.json` |
| Q 104 (next) rank in Q 103's FR list | 10/113 (FR 0.3119) | `h-new-111.json` |
| Q 102 → Q 103 seam | delta_raw +0.04795, ascending-rank 44/113 | `h-new-720.json` |
| Q 103 → Q 104 seam | delta_raw +0.11570, ascending-rank 88/113 | `h-new-720.json` |
| H-NEW-590 outlier | delta_pct 0.0, **NULL** (window {100-106}, d_W 0.330) | `h-new-590.json` |
| H-NEW-750 rhyme | ر (rā'), 3/3 = **perfect monorhyme**, entropy 0.0 nats | `h-new-750.json` |
| H-NEW-750 local_cohesion | 3.070 (z +2.112), rank 10/114 | `h-new-750.json` |
| H-NEW-750 sig_A | −0.0473 (rank 61/114) | `h-new-750.json` |
| H-NEW-750 sig_B | +0.7180 (rank 38/114) | `h-new-750.json` |
| H-NEW-840 UAS | −2.244 (rank 106/114) | `h-new-840.json` |
| H-NEW-2340 istiʿlāʾ density | **0.0959, rank #2/114** (behind Q 113) | `h-new-2340.json` |
| H-NEW-2210 qasam | wāw-oath, *temporal* object, jawāb dist = 1 | `h-new-2210.json` |

## 4. Surface structure

| Verse | Text (no-tashkeel) | Function |
|---|---|---|
| 1 | والعصر | **qasam** — wāw-oath on *al-ʿaṣr* (time / the age / the afternoon) |
| 2 | إن الإنسان لفي خسر | **jawāb al-qasam** — the universal-loss claim: *inna al-insāna la-fī khusr* |
| 3 | إلا الذين آمنوا وعملوا الصالحات وتواصوا بالحق وتواصوا بالصبر | **istithnāʾ** — the fourfold exception: faith + righteous deeds + mutual-enjoining-of-truth + mutual-enjoining-of-patience |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q103-F-01 Arm A | **CONFIRMED** | {Q 103, Q 108} are the only two 3-verse rā'-monorhymes; Q 108 is Q 103's rank-1 FR neighbor (0.2399) |
| Q103-F-01 Arm B | **DIRECTIONAL** | istiʿlāʾ density 0.0959 (#2/114), ṣād-driven (5/7), obs > null (z +1.83) but p_perm 0.070 — does not clear α=0.05 |
| Q103-F-01 Arm C | **CONFIRMED** | minimal tripartite oath→jawāb (dist 1)→istithnāʾ; local_cohesion rank 10/114; perfect rā'-monorhyme |

## 6. Cross-references

- **H-NEW-2340** (emphatic-iconicity) — Q 103 ranks #2 in heavy-istiʿlāʾ density; the corpus-level NULL of
  the heavy↔ʿadhāb iconicity hypothesis means Q 103's emphasis is *lexical-spine* driven, not theme-driven.
- **H-NEW-2210** (qasam→jawāb inventory) — Q 103 is cluster #44's neighbour: a single wāw-oath, temporal
  object, minimal jawāb distance 1.
- **H-NEW-750 / H-NEW-840** — perfect monorhyme + top-decile local cohesion, but bottom-band UAS (106/114).
- **H-NEW-590** — Q 103 is a cohesion member (NULL outlier) of the FR-dense short-Meccan window {100-106}.
- **Q 108 al-Kawthar** — the minimal-surah rā'-twin (Arm A); rank-1 FR neighbour.
- **Q 113 al-Falaq** — the only surah denser in istiʿlāʾ letters than Q 103.

## 7. Classical-tradition status

- al-Ṭabarī (*Jāmiʿ al-bayān*, on Q 103): the *ʿaṣr* = *dahr* (time/age) debate — Ibn ʿAbbās ("ساعة من
  ساعات النهار"), al-Ḥasan ("العشيّ"), with the preferred reading that the oath is on time-in-general; the
  ʿAlī b. Abī Ṭālib variant recitation *wa-l-ʿaṣr wa-nawāʾib al-dahr…* (reported as *tafsīr*, not Qurʾān).
- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*, on Q 103): Meccan (Qatāda dissenting); the five readings of *ʿaṣr*
  (dahr / layl-nahār / ʿashī / ṣalāt al-ʿaṣr per Muqātil / "the age of the Prophet"); the legal *masʾala*
  (Mālik: an oath "not to speak for an ʿaṣr" = a year; al-Shāfiʿī: an hour).
- Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 103): **al-Shāfiʿī's** «لو تدبر الناس هذه السورة لوسعتهم»;
  the two-Companions-recite-al-ʿAṣr-before-parting tradition (via al-Ṭabarānī, ← ʿAbdullāh b. Ḥiṣn); the
  Musaylima / ʿAmr b. al-ʿĀṣ failed-imitation anecdote.
- al-Rāzī (*Mafātīḥ al-ghayb*, on Q 103): uses Q 103 + Q 109 as his worked example in the *taḥaddī*
  (inimitability-challenge) discussion of Q 2:23; the ʿaṣr/ḍuḥā oath-pair (loss-oath vs profit-oath); the
  merchant-of-loss metaphor (the ice-seller anecdote, *irḥamū man yadhūbu raʾs mālihi*).
- al-Baghawī (*Maʿālim al-tanzīl*, on Q 103) and al-Jalālayn: concise versions of the *ʿaṣr* glosses and
  the "loss = squandering one's capital (life/time) in sin" reading.

## 8. Open questions / queued tests

- Q103-F-02 (queued): is the *tawāṣaw bi-… wa-tawāṣaw bi-…* doubled-reciprocal-enjoining frame of v 3
  corpus-rare? (w-ṣ-y form-VI reciprocal appears twice in one verse — test corpus frequency of the
  doubled *tawāṣaw bi-X wa-tawāṣaw bi-Y* template.)
- Q103-F-03 (queued): formalize the Q 103 ↔ Q 108 minimal-surah rā'-twin at the *root-Jaccard* and
  *rhyme-foot* levels — do the two share a phonological foot beyond the bare rā' final?
- Q103-F-04 (queued): re-run Arm B's emphatic-iconicity null at the *content-root-shuffle* level (permute
  which roots fill the surah's slots) to separate lexical-spine emphasis from positional emphasis.

---

*Investigation: Wave-N (2026-05-30) Q 103 al-ʿAṣr full deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified (and honestly-flagged) faḍāʾil chain.*
