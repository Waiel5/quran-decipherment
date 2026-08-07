---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
surah_name_english: "The Morning Brightness / The Forenoon"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 1 pre-registered 2-arm test landed — Arm A CONFIRMED (Q93↔Q94 scale-dissociation) + Arm B CONFIRMED (favor→command orphan-recall)
---

# Q 93 al-Ḍuḥā — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 93 | canonical |
| Arabic name | الضحى | canonical (*al-ḍuḥā*, the morning-brightness / forenoon; from v 1 oath *wa-l-ḍuḥā*) |
| Transliteration | al-Ḍuḥā | canonical |
| English meaning | "The Morning Brightness / The Forenoon" | classical |
| Verse count | 11 | Hafs-Kūfan (`data/hafs-verse-counts.tsv` line 93); al-Qurṭubī "إحدى عشرة آية" |
| Position in mushaf | 93 | canonical |
| Revelation order | #11 (Tanzil Egyptian Standard); Nöldeke #13 | `data/revelation-order.csv` (mushaf_order 93) |
| Type | Meccan ("مكية باتفاق" — Meccan by agreement) | al-Qurṭubī on v 1; al-Baghawī "مكية" |
| Word count (no-tashkeel, marks stripped) | 40 | computed (`scripts/Q093_F_01_duha_sharh_seam.py` pipeline) |
| Letter count (no-tashkeel) | 165 | computed |
| Distinct QAC roots | 23 (28 root-tokens) | `data/morphology/root-index.json` |
| Opening | والضحى — oath ("By the morning brightness") | oath-opening (qasam family) |
| Predominant rhyme (rāwī) | ي (yāʾ), 8/11 verses (72.7%) | `h-new-700.json` rhyme_letter_diagnostics; `h-new-750.json` |
| Length class | mufaṣṣal-qiṣār (short Meccan; al-mufaṣṣal lowest tier) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 93 matters for the project

1. **The classically-paired surah, dissociated by scale.** Q 93 al-Ḍuḥā and Q 94 al-Sharḥ are reported
   by **Ṭāwūs and ʿUmar b. ʿAbd al-ʿAzīz** (via al-Rāzī, *Mafātīḥ al-ghayb*, opening of Sūrat al-Sharḥ)
   to be "one surah" (*sūra wāḥida*) recited together in one rakʿa without an intervening basmala —
   because Q 94:1 (*alam nashraḥ laka*) reads like a continuation of Q 93:6 (*alam yajidka yatīman*).
   Q093-F-01 Arm A tests this at two scales and finds a **clean dissociation**: at the WHOLE-SURAH scale
   the pairing is real (Q 94 is Q 93's **4th-nearest** Fisher-Rao neighbor of 113; the Q 93 → Q 94 TSP
   seam is the **10th-smoothest** of 113 — a seamless joint), but at the BOUNDARY-PERICOPE scale the
   H-NEW-2280 seam root-Jaccard is **exactly 0.0** at both k=3 and k=5 (the close of al-Ḍuḥā and the
   opening of al-Sharḥ share ZERO QAC roots). The famous pairing is a whole-surah-distribution bond, NOT
   a boundary-lexical bond — a textbook scale-of-aggregation case (cross-finding-025).

2. **A favor→command surah with a single lexical bridge.** Q 93's body is a triadic past-favor block
   (vv 6-8, each *wajadaka X fa-Y*: orphan→sheltered, wandering→guided, poor→enriched) answered by a
   triadic future-command block (vv 9-11: orphan→do-not-oppress, asker→do-not-repel, blessing→proclaim).
   Q093-F-01 Arm B confirms (deterministically) that **`ytm` (yatīm, orphan) is the ONLY root bridging
   the two blocks** (v 6 → v 9), and that the anaphoric **`wjd` (wajadaka) unifies the favor block** (vv
   6,7,8 — and no other Q 93 verse). The other two favor/command pairs (wandering/asker, poor/blessing)
   are positional-thematic but share NO root — the orphan-recall is the surah's lone lexical hinge.

3. **The delayed-revelation asbāb.** Q 93's *sabab al-nuzūl* — Jibrīl's delay, the Prophet's distress,
   and a woman's taunt ("your devil has abandoned you") answered by *mā waddaʿaka rabbuka wa-mā qalā* —
   is among the most securely attested occasions of revelation, in al-Bukhārī (#4744, #4745 in the
   Tafsīr of Sūrat al-Ḍuḥā; #1092; #4776), Muslim (#4525, #4526, Jundub b. Sufyān), and al-Tirmidhī
   (#3429, *ḥasan ṣaḥīḥ*). All verified on disk.

4. **The al-Layl opening-echo.** Q 93:2 *wa-l-layl idhā sajā* echoes the opening of the chronologically-
   prior Q 92 al-Layl (#9) *wa-l-layl idhā yaghshā* — the same *wa-l-layl idhā [verb]* oath-frame. Ibn
   Kathīr explicitly cross-references Q 93:1-2 ↔ Q 92:1-2 (on disk). Yet Q 92 is only Q 93's **18th**-FR
   neighbor — the oath-frame echo is a surface-anaphora, not a whole-surah-distribution bond.

5. **Deep cohesion member of the short-Meccan tail.** Q 93's mean FR to all 113 surahs is **0.8152**
   (far below corpus mean 0.9235), and its H-NEW-590 outlier delta_pct is **−0.06** (p = 0.9997, NULL) —
   it sits inside an extraordinarily tight {Q 90-96} window (d̄_W ≈ 0.47). Q 93 is architecturally
   *in-block*, not dispersion-extreme.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.8152 | `h-new-111.json` (Q93 row) |
| Top-3 FR neighbors | Q 108, Q 106, Q 100 | `h-new-111.json` |
| Q 94 (next surah) rank in Q 93's FR list | **4/113** (FR 0.3641) | `h-new-111.json` |
| Q 92 (prev surah) rank in Q 93's FR list | 18/113 (FR 0.4338) | `h-new-111.json` |
| Q 92 → Q 93 seam | delta_raw = +0.06063, rank 55/113 (mid) | `h-new-720.json` |
| Q 93 → Q 94 seam | delta_raw = **−0.01520, rank 10/113 (seamless)** | `h-new-720.json` |
| H-NEW-590 outlier | delta_pct = −0.06, p = 0.9997, **NULL** (cohesion member of Q 90-96) | `h-new-590.json` |
| H-NEW-700 monorhyme | ي (yāʾ), 72.7%; entropy 0.760 nats | `h-new-700.json` / `h-new-750.json` |
| H-NEW-750 sig_A | +1.0503 (rank 32/114) | `h-new-750.json` |
| H-NEW-750 sig_B | +1.1581 (rank 23/114) | `h-new-750.json` |
| H-NEW-840 UAS | −1.4521 (rank 87/114) | `h-new-840.json` |
| Q93→Q94 seam root-Jaccard (H-NEW-2280) | **0.0** at k=3 and k=5 | computed (`csv/Q093-F-01.json`) |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| **Oath** | 1-2 | *wa-l-ḍuḥā · wa-l-layl idhā sajā* — by the forenoon and the settling night |
| **Consolation (jawāb al-qasam)** | 3-5 | *mā waddaʿaka rabbuka wa-mā qalā* (not forsaken/hated) · the Hereafter is better · *wa-la-sawfa yuʿṭīka rabbuka fa-tarḍā* (future reward) |
| **Past-favor triad** | 6-8 | *alam yajidka yatīman fa-āwā* (orphan→sheltered) · *wa-wajadaka ḍāllan fa-hadā* (wandering→guided) · *wa-wajadaka ʿāʾilan fa-aghnā* (poor→enriched) |
| **Future-command triad** | 9-11 | *fa-ammā al-yatīma fa-lā taqhar* (orphan→do not oppress) · *wa-ammā al-sāʾila fa-lā tanhar* (asker→do not repel) · *wa-ammā bi-niʿmati rabbika fa-ḥaddith* (blessing→proclaim) |

The macro-structure is a **temporal arc**: oath (1-2) → present/future consolation (3-5) → recollection
of past divine favors (6-8) → forward-looking ethical commands keyed to those favors (9-11). The
favor→command join is the surah's hinge (al-Rāzī ties Q 94:1 to exactly this junction).

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q093-F-01 Arm A | **CONFIRMED (scale-dissociation)** | Q 93↔Q 94 pairing is whole-surah-cohesive (FR rank 4; TSP seam rank 10/113 seamless) but boundary-lexically ZERO (seam root-Jaccard 0.0 at k=3 & k=5) — cohesion lives at the surah-distribution scale, not the seam-lexis scale |
| Q093-F-01 Arm B | **CONFIRMED** | `ytm` (orphan) is the UNIQUE root bridging the favor-block (vv 6-8) and command-block (vv 9-11), v 6→v 9; `wjd` (wajadaka) anaphora unifies vv 6-8; only Q 2, Q 4, Q 93 carry `ytm` in ≥2 verses, and Q 93 is the only one realizing a favor→command recall |

## 6. Cross-references

- **H-NEW-2280** (al-Biqāʿī munāsabah-seam) — Q 93 → Q 94 is one of the corpus's zero-Jaccard seams
  despite being a smooth whole-surah joint; a sharp instance of the seam-lexical/whole-surah dissociation
- **H-NEW-720** — Q 93 → Q 94 seamless seam (rank 10/113); Q 92 → Q 93 mid-spectrum
- **H-NEW-111** — Q 94 is Q 93's 4th-nearest FR neighbor; the short-Meccan tail {Q 100-114} dominates Q 93's neighborhood
- **H-NEW-590** — Q 93 is a deep COHESION member of the {Q 90-96} window (delta_pct = −0.06, NULL)
- **cross-finding-025** (scale-of-aggregation) — Arm A is a new supporting instance: a classically-paired
  unit cohesive at whole-surah scale but lexically null at the boundary
- **Q 94 al-Sharḥ** — the paired/single-unit successor (Ṭāwūs, ʿUmar b. ʿAbd al-ʿAzīz; al-Rāzī)
- **Q 92 al-Layl** — chronologically-prior; shares the *wa-l-layl idhā [verb]* oath-frame (Q 93:2)

## 7. Classical-tradition status

- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*): Meccan by agreement; 11 verses; the oath-of-the-forenoon and the
  *ḍuḥā* glosses; v 5 *wa-la-sawfa yuʿṭīka rabbuka fa-tarḍā* as the future-reward/intercession promise;
  v 11 *fa-ḥaddith* as proclaiming the blessing (the Qurʾān / prophethood — Mujāhid).
- al-Ṭabarī (*Jāmiʿ al-bayān*): *mā waddaʿaka rabbuka wa-mā qalā* = "your Lord has not abandoned you nor
  hated you"; the asbāb (Jundub al-Bajalī — Jibrīl's delay, the woman's/idolaters' taunt).
- al-Baghawī (*Maʿālim al-tanzīl*): Meccan; the Jundub b. Sufyān isnād for the asbāb; the variant that
  the woman was Umm Jamīl (wife of Abū Lahab); the Zayd b. Aslam cause-of-delay report.
- Ibn Kathīr (*Tafsīr al-ʿaẓīm*): the asbāb from Aḥmad/Bukhārī/Muslim/Tirmidhī/Nasāʾī; the orphan→
  shelter biography (father, mother, grandfather, Abū Ṭālib); the cross-reference Q 93:1-2 ↔ Q 92:1-2.
- al-Rāzī (*Mafātīḥ al-ghayb*): reports Ṭāwūs/ʿUmar b. ʿAbd al-ʿAzīz "one surah" pairing with al-Sharḥ
  (Q 94:1 ≈ continuation of Q 93:6) but REJECTS the identification (different revelation-states).

## 8. Open questions / queued tests

- Q093-F-02 (queued): the *wa-la-sawfa yuʿṭīka rabbuka fa-tarḍā* (v 5) — is the *sawfa*+future-divine-gift
  construction a Meccan-consolation distinctive?
- Q093-F-03 (queued): formalize the al-Layl (Q 92) → al-Ḍuḥā oath-frame echo (*wa-l-layl idhā [verb]*) as
  a corpus census of the oath-frame, testing whether the surface-anaphora vs FR-distance gap is general.
- Q093-F-04 (queued): re-run Arm A's seam dissociation across all 13 seamless seams — is the
  whole-surah-smooth-but-lexically-zero pattern systematic in the short-surah tail?

---

*Investigation: Wave-N (2026-05-30) Q 93 al-Ḍuḥā full deep-dive (single-specialist landing). See JOURNAL.md
for the method log; 06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified asbāb chain.*
