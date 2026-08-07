---
surah: 73
surah_name_ar: المزمل
surah_name_translit: al-Muzzammil
surah_name_english: "The Enshrouded One"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: 5 pre-registered tests landed — 1 CONFIRMED + 1 VERIFIED + 2 DIRECTIONAL + 1 NULL
---

# Q 73 al-Muzzammil — Overview


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
| Surah ID | 73 | canonical |
| Arabic name | المزمل | canonical (active participle of the Form-V verb *tazammala* "to wrap oneself in a garment"; the title refers to the Prophet at v 1) |
| Transliteration | al-Muzzammil | canonical |
| English meaning | "The Enshrouded / Wrapped One" | classical |
| Verse count | 20 | Hafs-Kufan |
| Position in mushaf | 73 | canonical |
| Revelation order | #3 (Tanzil); Nöldeke #23, Early Meccan | data/revelation-order.csv |
| Type | Meccan (with possibly-Medinan v 20) | classical consensus |
| Pair-twin | Q 74 al-Muddaththir (next surah, also Form-V opening vocative) | structural |
| Word count (no-tashkeel) | ~287 | computed |
| Letter count (no-tashkeel) | ~1,300+ | computed |
| Opening | يا أيها المزمل — "O you who are enshrouded" | UNIQUE Form-V passive-participle vocative |

## 2. Why Q 73 matters for the project

1. **Earliest revelation cohort** — Q 73 is revelation #3 in classical chronology (Q 96 al-ʿAlaq → Q 68 al-Qalam → Q 73 al-Muzzammil), placing it in the foundational pre-Medinan period.

2. **Q 73:20 = corpus rank-3 longest verse** (CONFIRMED Q073-F-05) — 90 words, far longer than any other Early-Meccan verse. The verse alone contains 31% of the surah's word-count and embeds the entire post-abrogation legal-ritual framework (night-prayer relaxation + recitation feasibility + zakat + Q 73's anchor injunction).

3. **Classical abrogation locus** — Q 73:1-3 (mandate of night-prayer "stand half the night") was abrogated by Q 73:20 ("ʿalima an lan tuḥṣūhu… fa-iqraʾū mā tayassara"). Q073-F-03 VERIFIED this on-disk via Abū Dāwūd #1305 (Ibn ʿAbbās chain).

4. **Vocative-twin pair with Q 74** — Q 73 opens with *yā ayyuhā al-muzzammil*, Q 74 with *yā ayyuhā al-muddaththir*. Both 3-word + Form-V passive participle + ال definite. Q073-F-02 DIRECTIONAL: 2/3 axes pass (clamped-zero seam + morph-iso) but FR mutual-top-15 FAILS — pair is structurally-twin yet content-divergent.

5. **IMPV-qrA carrier** — Q 73 contains 2 of the corpus's 6 *iqraʾ* imperatives (Q 73:20 × 2, both 2MP plural). The 2MS/2MP grammatical split refines the H-NEW-1300 inventory (see Q073-F-01).

6. **Dual seamless-seams** — Q 72 → Q 73 (delta_raw = -0.00118) AND Q 73 → Q 74 (delta_raw = -0.02888) are BOTH in the 13-clamped-zero seamless set (H-NEW-1240). Q 73 is bracketed by seamless seams on both sides — one of very few mushaf positions with dual-seamless bracket.

## 3. Empirical anchor summary

| Instrument | Value | Notes |
|---|---|---|
| FR mean to all 113 surahs | 0.8555 | well below corpus mean 0.9234 |
| Top-3 FR neighbors | Q 112, Q 91, Q 110 | short-mufaṣṣal Early-Meccan tail neighborhood |
| Rank of Q 74 in Q 73's FR list | 37/113 | NOT in top-15 — pair NOT content-cohesive |
| Q 73 → Q 74 TSP-cost rank | clamped-zero | in 13-seamless set (H-NEW-1240) |
| H-NEW-590 outlier | delta_pct = -4.08, NULL | Q 73 = COHESION_ANCHOR with Q 70-76 window |
| H-NEW-700 monorhyme | ا (alif), 90% verses | low entropy (0.394 nats) |
| H-NEW-750 sig_A | -0.009 (rank 59) | mid-range iʿjāz al-fawāṣil |
| H-NEW-840 UAS | -2.696 | low (consistent with short Meccan) |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| Vocative opening | 1 | yā ayyuhā al-muzzammil |
| Night-prayer mandate | 2-4 | "stand half the night, or less, or more" |
| Recitation instruction | 4 | "wa-rattil al-qurʾāna tartīlan" |
| Cosmic-judgment block | 5-14 | hardness of message + day-of-shaking |
| Pharaoh single-pericope | 15-16 | one mention; sole Mosaic narrative |
| Eschatological warning | 17-19 | day of separation |
| Abrogation verse | 20 | the 90-word abrogator + zakat + ritual |

## 5. Pre-registered novel findings (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q073-F-01 | DIRECTIONAL | Q 73:20 ↔ Q 96 IMPV-qrA pair — co-occurrence p<10⁻⁴, but verse-twin sim FAIL (length asymmetry) |
| Q073-F-02 | DIRECTIONAL | Q 73 ↔ Q 74 vocative-twin pair — morph-iso + seamless-seam PASS, FR mutual-top-15 FAIL |
| Q073-F-03 | VERIFIED | Q 73:20 abrogation on disk at Abū Dāwūd #1305 (brief-correction: NOT Mālik/Bukhārī) |
| Q073-F-04 | NULL (PC VALID) | IMPV-qrA 4-cluster genuinely NOT FR-cohesive; promotes H-NEW-1301 with valid instrument |
| Q073-F-05 | CONFIRMED | Q 73:20 corpus rank-3 by length; Early-Meccan rank-1; 43% longer than 2nd-place |

## 6. Cross-references

- Cross-finding-025 (marker-thickness rule) — Q073-F-04 adds to NULL-side
- H-NEW-1190 (*wa-mā adrāka mā* cluster) — gold-standard MW-5 PC going forward
- H-NEW-1240 (13 seamless seams) — Q 72 → Q 73 → Q 74 dual-bracket
- H-NEW-1300 / 1301 (IMPV-qrA) — refined by 2MS/2MP grammatical split
- Q 96 al-ʿAlaq — paired chronology (revelation #1 ↔ #3) + paired IMPV-qrA carrier

## 7. Classical-tradition status

- al-Suyūṭī (Itqān): Q 73 revelation #3, between Q 68 and Q 74; chronology consensus
- Ibn Kathīr: night-prayer obligation v 2 abrogated by v 20; chain via Ibn ʿAbbās verified
- al-Biqāʿī (Naẓm al-durar): Q 73 → Q 74 munāsabah is opening-formula-driven (the muzzammil/muddaththir twin) + sequential-prophetic-discipline (preparation → public-warning)
- al-Bāqillānī (iʿjāz al-fawāṣil): Q 73 alif-monorhyme; mid-range significance

## 8. Open questions / queued tests

- H-NEW-1400: corpus-wide search for other OPENING-LINKED CONTENT-DIVERGENT pairs analogous to Q 73 ↔ Q 74
- H-NEW-1401: Q 73:20 imperative-density per word — distinguishable from other long verses?
- H-NEW-1402: codify H-NEW-1190 as canonical MW-5 PC for FR-cohesion tests

---

*Investigation: Wave-H specialist landing, 2026-05-09. See JOURNAL.md for full method log; 06-novel-findings.md for test detail.*
