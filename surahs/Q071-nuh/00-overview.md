---
surah: 71
surah_name_ar: نوح
surah_name_translit: Nūḥ
surah_name_english: "Noah"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: "Q071-F-01 NULL (Q 71 is NOT the lexical centroid/anchor of the Nūḥ cycle — it is rank 5/6; the centroid is the short Q 7:59-64 retelling). Q071-F-02 PASS-DIRECTED-STRONG (4/5 named idols are corpus-strict orthographic singletons co-located at Q 71:23)."
---

# Q 71 Nūḥ — Overview


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
| Surah ID | 71 | canonical |
| Arabic name | نوح | canonical (the proper name *Nūḥ*; from v 1 *innā arsalnā Nūḥan*) |
| Transliteration | Nūḥ | canonical |
| English meaning | "Noah" | classical |
| Verse count | 28 | Hafs-Kūfan (`data/hafs-verse-counts.tsv` line 71); al-Qurṭubī "ثمان وعشرون آية" (`ar-tafseer-al-qurtubi/71/1.json`) |
| Position in mushaf | 71 | canonical |
| Revelation order | Tanzil Egyptian Standard #71; **Nöldeke #51, Middle Meccan** | `data/revelation-order.csv` row mushaf=71 |
| Type | Meccan ("مكية") | al-Qurṭubī on v 1 (`ar-tafseer-al-qurtubi/71/1.json`); Ibn Kathīr "revealed in Makkah" (`en-tafisr-ibn-kathir/71/1.json`) |
| Word count (no-tashkeel, waqf-marks stripped) | 227 | computed (`scripts/Q071_F_01_*.py` pipeline; verified) |
| Letter count (no-tashkeel, excl. spaces) | 965 | computed |
| Distinct QAC roots | 87 (380 morphological segments) | `data/morphology/quranic-corpus-morphology-0.4.txt` (s==71) |
| Opening | إنا أرسلنا نوحا — "Indeed We sent Noah" | direct narrative (NOT muqaṭṭaʿāt, NOT *qul*, NOT *ḥamd*) |
| Predominant rhyme (rāwī) | ا (alif), final-letter frac 0.857 (24/28) | `h-new-750.json` per_surah Q71 `top_final_letter='ا'`, `top_final_letter_frac=0.857` |
| Rhyme entropy | 0.4904 nats (z = −0.506) | `h-new-750.json` per_surah Q71 `rhyme_entropy_nats` |
| Length class | mufaṣṣal-ṭiwāl (long-mufaṣṣal Meccan; al-Zarkashī mufaṣṣal-3-tier) | classical |

## 2. Why Q 71 matters for the project

1. **The only whole-surah dedicated to a single prophet's flood-narrative.** Q 71
   tells the Nūḥ story end-to-end in one surah — call, complaint, the cosmological
   signs, the people's idolatry (the five named idols), the drowning, and the
   closing imprecatory prayer. It is the NARRATIVE anchor of the corpus's most
   frequently-retold prophet cycle.

2. **Q071-F-01 NULL — Q 71 is NOT the LEXICAL anchor of its own cycle (the headline
   finding).** Extending H-NEW-2260 (Nūḥ cycle PASS, z=+2.51), we pre-registered the
   intuitive hypothesis that the dedicated surah is the *lexical centroid* of the
   6-pericope Nūḥ cycle {Q 7:59-64, Q 11:25-49, Q 23:23-30, Q 26:105-122, Q 54:9-17,
   Q 71}. It is FALSIFIED. Q 71 ranks **5th of 6** in mean intra-cycle root-Jaccard
   (mean_J = 0.1493); the centroid is the short **Q 7:59-64** al-Aʿrāf retelling
   (mean_J = 0.2169). A length-matched random 28-verse window contributes about as
   much cohesion to the cycle as Q 71 (Arm B z = +0.42, p_perm = 0.278, NULL). The
   long dedicated surah is the narrative hub but a **lexical periphery member**,
   precisely because its private vocabulary (cosmological signs vv 15-20; the five
   idols v 23; "by night and day") is unshared by the lean cross-surah retellings.

3. **Q071-F-02 PASS-DIRECTED-STRONG — the five-idol corpus-singleton.** Of the five
   pre-Islamic deities named at Q 71:23 (Wadd, Suwāʿ, Yaghūth, Yaʿūq, Nasr), **four**
   (Suwāʿ سواعا, Yaghūth يغوث, Yaʿūq ويعوق, Nasr ونسرا) are corpus-strict orthographic
   singletons that occur EXACTLY ONCE in the 6,236-verse corpus and ALL co-locate at
   Q 71:23. The fifth (Wadd ودا) is a *contextual* deity-singleton only — the same
   token-form ودا also appears at Q 19:96 ("affection"). This is one of the densest
   proper-name singleton clusters in the corpus, corroborated by Ṣaḥīḥ al-Bukhārī
   Kitāb al-Tafsīr (Ibn ʿAbbās chain; idInBook 4712 in the on-disk collection).

4. **Whole-surah-scale corroboration of the centroid NULL.** At the H-NEW-111
   Fisher-Rao whole-surah scale, the five cross-surah Nūḥ host-surahs are among
   Q 71's MOST DISTANT surahs (Q 7 rank 93/113, Q 11 rank 94, Q 23 rank 79, Q 26
   rank 102, Q 54 rank 87). Q 71's nearest neighbours are short Meccan creedal
   surahs (Q 112, Q 110, Q 91, Q 105, Q 63), not the long mixed-content surahs that
   host the Nūḥ pericopes. The cycle does NOT cohere at whole-surah scale; it cohered
   at pericope scale (H-NEW-2260) — and even there Q 71 is the least-central member.

5. **Petition-narrative register.** The surah is framed as Noah's first-person
   report-and-prayer to his Lord: the night/day complaint (vv 5-9), the
   wealth/children rejection (vv 21-22), and the closing two-fold imprecation +
   forgiveness prayer (vv 26-28). This is the structural feature flagged by the
   queued Q071-F-05 petition-density test.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.8793 | `h-new-111.json` (Q71 row); matches `h-new-750.json` `mean_content_distance` 0.87925 |
| Top-3 FR neighbours | Q 112 (0.695), Q 110 (0.700), Q 91 (0.706) | `h-new-111.json` |
| 5 Nūḥ-host surahs in Q 71's FR list | Q 7 (93/113), Q 11 (94), Q 23 (79), Q 26 (102), Q 54 (87) | `h-new-111.json` |
| Q 70 → Q 71 seam | delta_raw = +0.17597, frac_resid 0.0212, ascending-rank 96/113 (expensive) | `h-new-720.json` per_adjacency pair [70,71] |
| Q 71 → Q 72 seam | delta_raw = +0.04082, frac_resid 0.0049, ascending-rank 40/113 | `h-new-720.json` per_adjacency pair [71,72] |
| H-NEW-750 sig_A | −0.0694 (rank 64/114) | `h-new-750.json` |
| H-NEW-750 sig_B | −0.9128 (rank 77/114) | `h-new-750.json` |
| H-NEW-750 local_cohesion | 1.2196 (z = −0.407) | `h-new-750.json` |
| H-NEW-840 UAS | −1.3242 (rank 84/114) | `h-new-840.json` all_uas Q71 |
| H-NEW-590 outlier | NOT a tested candidate (590 candidates = {1,9,18,55,62,112}) — DATA GAP | `h-new-590.json` |

## 4. Surface structure (4 movements)

| Block | Verses | Function |
|---|---|---|
| Commissioning + the warning | 1-4 | *innā arsalnā Nūḥan* … *anindhir qawmaka* — the call to worship, taqwā, obedience |
| The night/day complaint | 5-9 | *rabbi innī daʿawtu qawmī laylan wa-nahāran* — secret, public, and proclaimed calling, all rebuffed |
| The *istighfār* sermon + cosmological signs | 10-20 | seek forgiveness → rain, wealth, children, gardens, rivers; *alam taraw kayfa khalaqa Allāhu sabʿa samāwātin ṭibāqan* — heavens, moon, sun, earth, paths |
| The verdict, the five idols, the drowning, the closing prayer | 21-28 | *qāla Nūḥun rabbi innahum ʿaṣawnī* → the idol-list v 23 → *mimmā khaṭīʾātihim ughriqū* (drowned, cast into fire) → *rabbi lā tadhar* / *rabbi ighfir lī* |

## 5. Pre-registered novel findings (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q071-F-01 | **NULL** | Q 71 is NOT the lexical centroid of the Nūḥ cycle: rank 5/6 (mean_J 0.149); centroid = Q 7:59-64 (0.217); random-anchor swap z=+0.42, p=0.278. The dedicated surah is the NARRATIVE anchor but a LEXICAL outlier. Direction matched (z>0), no pre-commit violation. |
| Q071-F-02 | **PASS-DIRECTED-STRONG** | 4/5 named idols (Suwāʿ, Yaghūth, Yaʿūq, Nasr) are corpus-strict orthographic singletons, all at Q 71:23; Wadd is contextual-singleton-deity only (also Q 19:96). |

## 6. Cross-references

- **H-NEW-2260** — parent; Nūḥ cycle PASS (z=+2.51); Q 71 is one of the 6 pericopes but the **least central**.
- **cross-finding-025 / 026** — scale-of-aggregation: the Nūḥ cycle's cohesion lives at PERICOPE scale (and is carried by the SHORT retellings), not whole-surah scale, and not by the dedicated surah.
- **H-NEW-111** — whole-surah FR: the 5 Nūḥ-host surahs are among Q 71's most distant.
- **H-NEW-49.1 / H-NEW-86** — Q 71 in the prophet-named set; one of 2 NON-muqaṭṭaʿāt prophet-named surahs (with Q 47 Muḥammad) [queued Q071-F-03].
- **Q 70 al-Maʿārij / Q 72 al-Jinn** — neighbours; Q 70→71 is an Early→Middle-Meccan Nöldeke phase seam (queued Q071-F-04).

## 7. Classical-tradition status (full survey in `03-tafsir-survey.md`)

- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*): Meccan; 28 verses; Nūḥ as the **first messenger** sent (Qatāda ← Ibn ʿAbbās ← the Prophet); genealogy of Nūḥ.
- al-Ṭabarī (*Jāmiʿ al-bayān*): the five idols were righteous men of Nūḥ's people whose statues were later worshipped (Muḥammad b. Qays, ʿIkrima chains).
- Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm*): the idol-list with the full Ibn ʿAbbās/al-Bukhārī tribal-attribution chain; Noah's 950-year complaint.
- al-Jalālayn: terse glosses — *laylan wa-nahāran* = "continuously"; *dayyār* (v 26) = "not one dweller"; *baytī* (v 28) = house/place of worship.
- al-Wāḥidī (*Asbāb al-nuzūl*) + al-Wāsiṭī: the *aṭwāran* (v 14) creation-in-stages reflection.

## 8. Open questions / queued tests

- **Q071-F-03** (queued): H-NEW-49.1 prophet-named hypergeometric — verify Q 71 in the NON-muq + prophet-named cell (with Q 47).
- **Q071-F-04** (queued): H-NEW-130 boundary-set — Q 70→71 in B (Early→Middle Meccan phase seam), Q 71→72 NOT in B.
- **Q071-F-05** (queued): petition-density corpus-rank (rabb-vocatives + duʿāʾ/ighfir tokens).
- **Follow-up to F-01**: re-run the centroid test on the LEMMA or orthographic-token lens (rules-tuple sensitivity is bidirectional) — could the dedicated surah be the centroid on a finer-grained lens?

---

*Investigation: Wave-N (2026-05-30) Q 71 Nūḥ full deep-dive. See JOURNAL.md for the
method log; 06-novel-findings.md for the F-01 NULL detail; 04-hadith-corpus.md for the
verified five-idol Bukhārī chain (idInBook 4712, with the Fatḥ-al-Bārī #4920 cross-numbering flagged).*
