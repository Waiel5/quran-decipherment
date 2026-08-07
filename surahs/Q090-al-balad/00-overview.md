---
surah: 90
surah_name_ar: البلد
surah_name_translit: al-Balad
surah_name_english: "The City"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 1 pre-registered test landed — Q090-F-01 CONFIRMED (corpus-hapax-root enrichment, p_perm=0.0012) with an honest register-level caveat (MW-6 control Q 91 equally enriched)
---

# Q 90 al-Balad — Overview


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
| Surah ID | 90 | canonical |
| Arabic name | البلد | canonical (from v 1 *hādhā al-balad*, "this city" = Makka) |
| Transliteration | al-Balad | canonical |
| English meaning | "The City" | classical (al-balad al-ḥarām = Makka) |
| Verse count | 20 | Hafs-Kufan (`data/hafs-verse-counts.tsv` line 90); al-Qurṭubī "وهي عشرون آية" |
| Position in mushaf | 90 | canonical |
| Revelation order | #35 (Tanzil Egyptian Standard) — Early Meccan | `data/revelation-order.csv` line `35,90,البلد,Al-Balad,Meccan,...` |
| Type | Meccan ("مكية باتفاق" — Meccan by agreement) | al-Qurṭubī on v 1 |
| Word count (no-tashkeel, marks stripped) | 82 | computed (`quran-text/quran-no-tashkeel.json`) |
| Letter count (no-tashkeel) | 342 | computed |
| Distinct QAC roots | 45 (52 root-tokens) | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Opening | لا أقسم بهذا البلد — negated-oath (*lā uqsimu*) | qasam family (H-NEW-2210); one of only 2 surah-initial *lā uqsimu* openers |
| Predominant rhyme | tāʾ-marbūṭa (-ah) block vv 11–20 (10/20 = 50%); -d block vv 1–7; dual -ayn vv 8–10 | `h-new-700.json` (top_letter ه, frac 0.50); computed from `quran-min-tashkeel.json` |
| Length class | mufaṣṣal-qiṣār (short Meccan; al-mufaṣṣal short-tier) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 90 matters for the project

1. **Corpus-hapax-root carrier (Q090-F-01 CONFIRMED).** Q 90 carries **4 roots that occur
   nowhere else in the entire Quran**: `kbd` (kabad "toil", 90:4), `njd` (najdayn "the two
   highways", 90:10), `$fh` (shafatayn "two lips", 90:9), `sgb` (masghaba "hunger", 90:14).
   Against a length-preserving permutation null (10,000 perms, seed 20260509) the expected
   number of corpus-exclusive roots for a Q 90-sized surah is **0.42**; observing **4** gives
   **p_perm = 0.0012** (count arm) / **0.0008** (density arm) — both pass Bonferroni α_bon = 0.025
   in the locked enrichment direction, and the direction replicates at a second seed. **Honest
   caveat:** the MW-6 control Q 91 al-Shams is *equally* enriched (4 exclusive roots, p = 0.0004),
   so this is a **short-Meccan-register** property, not a Q 90 singleton (see §5, `06-novel-findings.md`).

2. **One of only TWO surah-initial *lā uqsimu* openers.** In the morphology-grounded H-NEW-2210
   qasam inventory, exactly two surahs OPEN at verse 1 with the *(lā) uqsimu* form: **Q 75
   al-Qiyāma** (`lā uqsimu bi-yawmi-l-qiyāma`) and **Q 90 al-Balad** (`lā uqsimu bi-hādhā al-balad`).
   Their jawāb structures differ: Q 75's apodosis is classically **elided** (`bare`), Q 90's is the
   explicit lām-al-tawkīd `la-qad khalaqnā al-insān fī kabad` (90:4) — identified as the *jawāb
   al-qasam* by al-Ṭabarī ("هذا هو جواب القسم") and al-Zamakhsharī. (Descriptive / MW-7-capped:
   the pair is NOT close in FR space — FR(Q75,Q90)=0.6695, rank 37/113 — the oath-form is an
   opener-grammar axis orthogonal to content, consistent with the project's letter-axis ⊥
   content-axis law.)

3. **The classical *lā* crux.** Whether the opening *lā* negates the oath or is the *zāʾida*
   emphatic-particle (`lā` = "Nay! I do swear…") is a genuine exegetical fault-line
   (al-Akhfash, al-Qushayrī, Ibn al-ʿArabī, Mujāhid). This is a testable balāgha claim, audited
   in `05-classical-claims-audit.md`.

4. **The steep-path (*ʿaqaba*) social-ethics core.** vv 11–16 define *al-ʿaqaba* — the
   freeing-of-a-slave (*fakk raqaba*), feeding the orphan and the destitute on a day of hunger —
   the surah's distinctive social-justice register. The *fakk raqaba* gloss has a verified
   direct hadith correlate (the Abū Dharr "most-precious slave" hadith, see below).

5. **Extreme-cohesion member of the {Q 87–93} window (H-NEW-590 NULL).** Q 90 sits in one of the
   tightest content-dispersion neighbourhoods in the corpus (window pct = 0.1); removing it
   barely moves the dispersion (delta_pct = −0.17, p = 0.999). It is architecturally "in-block",
   NOT a dispersion outlier.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.8372 (well below corpus mean 0.9235) | `h-new-111.json` (Q90 row) |
| Top-3 FR neighbors | Q 112 (0.395), Q 103 (0.411), Q 107 (0.431) | `h-new-111.json` |
| Q 89 (prev surah) rank in Q 90's FR list | 33/113 (FR 0.6326) | `h-new-111.json` |
| Q 91 (next surah) rank in Q 90's FR list | 23/113 (FR 0.5300) | `h-new-111.json` |
| Q 89 → Q 90 seam | delta_raw = +0.05033, asc-rank 47/113 | `h-new-720.json` |
| Q 90 → Q 91 seam | delta_raw = +0.09936, asc-rank 81/113 | `h-new-720.json` |
| H-NEW-590 outlier | delta_pct = −0.17, **NULL** (extreme-cohesion member of {Q 87–93}) | `h-new-590.json` |
| H-NEW-700 rhyme | ه (tāʾ-marbūṭa), 50%; rhyme entropy 1.1421 nats | `h-new-700.json` / `h-new-750.json` |
| H-NEW-750 sig_A | +1.5261 (rank **16/114**) | `h-new-750.json` |
| H-NEW-750 sig_B | +0.9706 (rank 30/114) | `h-new-750.json` |
| H-NEW-840 UAS | −0.4422 (rank 60/114) | `h-new-840.json` |
| Corpus-hapax roots | 4 (`kbd, njd, $fh, sgb`); hapax-density rank 10/114 | `data/morphology/...`; Q090-F-01 |

## 4. Surface structure (the surah's tripartite rhyme + theme architecture)

| Block | Verses | Function | Rhyme |
|---|---|---|---|
| **A. The oath** | 1–4 | *lā uqsimu* by the City (Makka), by *wālid wa-mā walad*; jawāb: man created *fī kabad* (in toil) | -d |
| **B. The self-deluded man** | 5–7 | "Does he think none has power over him? … none has seen him?" — the boaster of "wealth heaped up" | -d / -ad |
| **C. God's bestowed faculties** | 8–10 | two eyes, a tongue, two lips; *wa-hadaynāhu al-najdayn* (the two highways) | dual -ayn |
| **D. The steep path (*al-ʿaqaba*)** | 11–16 | *fa-lā iqtaḥama al-ʿaqaba* … freeing a slave / feeding the orphan + destitute in a day of hunger | -aba / -ah |
| **E. The two companies** | 17–20 | the believers (*aṣḥāb al-maymana*, "those who counsel patience and mercy") vs. the deniers (*aṣḥāb al-mashʾama*) with a sealed Fire over them | -ah |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q090-F-01 | **CONFIRMED** (register-level) | Q 90 carries 4 corpus-exclusive roots vs null-expected 0.42 (H1 p=0.0012, H2 p=0.0008, both < α_bon=0.025, replicated). **Honest limit:** the MW-6 control Q 91 al-Shams is equally enriched (p=0.0004) — the hapax-enrichment is a short-Meccan-register feature, not a Q 90 singleton. |

## 6. Cross-references

- **H-NEW-2210** — qasam/jawāb inventory; Q 90 is one of 8 *(lā) uqsimu* openers and one of only 2
  *surah-initial* ones (with Q 75 al-Qiyāma).
- **H-NEW-590** — Q 90 is an EXTREME-COHESION member of {Q 87–93} (delta_pct = −0.17, NULL).
- **H-NEW-111** — Q 90's FR neighborhood is the muʿawwidhāt/short-mufaṣṣal tail (Q 112, 103, 107…).
- **H-NEW-720** — Q 89 → Q 90 mid-low seam; Q 90 → Q 91 upper-mid seam.
- **Q 89 al-Fajr** — backward neighbour; also a stacked-oath surah (5 sworn objects, *bare* jawāb).
- **Q 91 al-Shams** — forward neighbour; oath-surah (8 sworn objects); the MW-6 hapax control.
- **Cross-finding (letter ⊥ content)** — the *lā uqsimu* set's FR non-clustering reinforces the
  opener-grammar-axis-⊥-content-axis pattern.

## 7. Classical-tradition status (full survey in `03-tafsir-survey.md`)

- **al-Ṭabarī** (*Jāmiʿ al-bayān*): the oath is on Makka (al-balad al-ḥarām); v 4 *la-qad khalaqnā
  al-insān fī kabad* is explicitly "هذا هو جواب القسم"; najdayn = "the two ways" of good and evil
  (ʿAbdallāh b. Masʿūd via Zirr); *fakk raqaba* anchored to the "most-expensive slave" prophetic report.
- **al-Zamakhsharī** (*al-Kashshāf*): the balāgha of the qasam→jawāb pairing; *wa-anta ḥill* is
  parenthetical (*iʿtirāḍ*); *kabad* = labour/hardship from *kabid* (the liver/inner-pain etymon).
- **al-Rāzī** (*Mafātīḥ al-ghayb*): five faces of *wa-anta ḥill bi-hādhā al-balad*; the future-sense
  reading (the conquest of Makka) vs. the Meccan revelation date; the najdayn = the two ways.
- **al-Qurṭubī** (*al-Jāmiʿ li-aḥkām*): Meccan by agreement, 20 verses; the *lā* crux (zāʾida vs.
  genuine negation, six positions); najdayn = the two breasts (ʿIkrima, al-Ḍaḥḥāk) vs. the two ways.
- **Ibn Kathīr** (*Tafsīr al-Qurʾān al-ʿaẓīm*): Makka's sanctity hadith ("Allah made it sacred the
  day He created the heavens and the earth"); man created in repeated hardship; the *ʿaqaba* deeds.

## 8. Open questions / queued tests

- Q090-F-02 (queued): is the Q 75 / Q 90 surah-initial *lā uqsimu* doublet matched by a shared
  *register* signature (both early-Meccan, both resurrection/accountability theme) even though
  they are FR-distant? — a content-vs-opener decomposition.
- Q090-F-03 (queued): the *najdayn / ʿaynayn / shafatayn* dual-noun triple (vv 8–10) — is Q 90
  the corpus's densest run of anatomical/path duals?
- Q090-F-04 (queued): formalise the tripartite-rhyme architecture (-d / -ayn / -ah) against a
  within-surah rhyme-segmentation null.

---

*Investigation: Wave-N (2026-05-30) Q 90 al-Balad full deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified Makka-sanctity + fakk-raqaba chains.*
