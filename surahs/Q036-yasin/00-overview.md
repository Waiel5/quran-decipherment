---
surah: 36
surah_name_ar: يس
surah_name_translit: Yāsīn
surah_name_english: Yā Sīn (the muqaṭṭaʿāt opening)
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all 9 template files + JOURNAL produced 2026-04-28 (Wave D)
---

# Q 36 Yāsīn — Overview


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
| Surah ID | 36 | canonical |
| Arabic name | يس | canonical |
| Transliteration | Yāsīn (Yā-Sīn) | conventional |
| English meaning | "Y-S" (the two letters of the muqaṭṭaʿāt opening; not translated) | n/a |
| Verse count | 83 | Hafs-Kufan; verified `quran-text/quran-no-tashkeel.json` Q36 |
| Position in mushaf | 36 | canonical |
| Type | Meccan | classical (al-Suyūṭī, *al-Itqān*, nawʿ 1) |
| Position in revelation order (al-Suyūṭī) | 41 of 114 | al-Suyūṭī, *al-Itqān*, nawʿ 1 (mid-Meccan, immediately after Q 72 al-Jinn at #40 and before Q 25 al-Furqān at #42) |
| Word count (no-tashkeel orthographic) | 754 | computed `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, no spaces) | 3,092 | computed |
| Root-tokens (QAC v0.4) | 438 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Distinct roots | 211 | same |
| Opening | يس (Yā Sīn) — 2-letter muqaṭṭaʿāt | textual |
| Bismala | counted-only-in-Q1 (rules-tuple default); Q 36 carries the standard prefixed bismala in Hafs-Kufan but it is not counted in word/letter totals here | rules-tuple |

## 2. Classical names and epithets

- **Yāsīn** (يس) — the muqaṭṭaʿāt opening, taken as the surah name.
- **Qalb al-Qurʾān** (قلب القرآن, "the heart of the Qurʾān") — popular epithet, sourced to the ḥadīth at al-Tirmidhī (the *Sunan* collection, in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json` at idInBook=2970, global id=28750) — graded *gharīb* by al-Tirmidhī himself and graded ḍaʿīf jiddan / mawḍūʿ by modern critic al-Albānī (Hārūn Abū Muḥammad in the chain). See `04-hadith-corpus.md` and `05-classical-claims-audit.md` Audit 1.
- **al-Muʿimma** / **al-Dāfiʿa** / **al-Qāḍiya** — minor honorifics found in some classical *fadāʾil*-collections (e.g., al-Suyūṭī, *al-Durr al-manthūr*, opening of Q 36); not corpus-standard.

## 3. Opening formula

**Muqaṭṭaʿāt opening — 2-letter (يس)**. Q 36 is one of **3 distinct 2-letter muqaṭṭaʿāt openings** in the corpus:
- Q 20 طه (Ṭāhā)
- Q 27 طس (Ṭā Sīn) [actually Q 27's muqaṭṭaʿāt is طس spanning 2 letters; Q 26 + Q 28 use 3-letter طسم]
- Q 36 يس (Yā Sīn)

If we ALSO count the 7 ḥawāmīm (Q 40-46, opening حم), the 2-letter muqaṭṭaʿāt set has cardinality **10** (= 3 + 7) — far from the singleton claim sometimes asserted. See [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] and `05-classical-claims-audit.md` Audit 3.

After the 2-letter opening, Q 36 v.2-3 contains the *qul*-less oath-form **"wa-l-Qurʾāni l-ḥakīm | innaka la-min al-mursalīn"** — the surah opens with an oath on the Quran itself paired with the assertion of Muḥammad's apostleship. This pattern is shared with Q 38 ص (which opens "ص ۚ والقرآن ذي الذكر") and Q 50 ق ("ق ۚ والقرآن المجيد") — the **3-surah cluster of muqaṭṭaʿāt + Quran-oath openings** = {Q 36, 38, 50}, all short-cardinality muqaṭṭaʿāt (2/1/1 letters). See [[MASTER-FINDINGS-LEDGER#Wave-D Q 36 entry|MASTER-FINDINGS-LEDGER §9.14]].

## 4. Length classification

83 verses, 754 words — **mufaṣṣal-ṭiwāl** (long-mufaṣṣal). Position s=36 places Q 36 just past the al-sabʿ al-ṭiwāl head-block (Q 1-9, ṭiwāl by classical reckoning: Q 2-9; Fātiḥa stands separately) and inside the **mid-Meccan zone** (Q 10-46) of the mushaf. Pre-Hijra-kink at s=50 (per [[h-new-660-compression-tail-gradient|H-NEW-660]] / [[h-new-700-phonological-compression-tail|H-NEW-700]]).

## 5. Rhyme structure

Final-letter distribution across 83 verses (computed `quran-text/quran-no-tashkeel.json`, last consonantal letter after stripping mushaf marks):

| Final letter | Count | % |
|:--|:-:|:-:|
| ن (nūn) | 70 | 84.34% |
| م (mīm) | 12 | 14.46% |
| س (sīn) | 1 | 1.20% |

**Rhyme entropy (Shannon, nats): 0.4765** — `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah[surah=36]`. This is BELOW the corpus mean (z = −0.531) — Q 36 is **near-monorhyme on -ūn/-īn** (the nūn-final pattern).

The single sīn-final verse is **Q 36:1 (يس)** itself — the muqaṭṭaʿāt verse, ending in the second of the two-letter pair. Apart from this opening fingerprint, Q 36 is functionally a nūn/mīm bi-rhyme surah dominated by -ūn/-īn fawāṣil over the eschatological resurrection scene (vv. 51-83).

## 6. Empirical architectural profile (headline)

See `01-empirical-profile.md` for the full integration of all H-NEW metrics. Headline:

- **UAS rank: 35/114** — `findings/phase-b-hypotheses/csv/h-new-840.json` `all_uas[surah=36]`; UAS = 0.5040, well below the structural-iʿjāz top-9 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23). **Q 36 is empirically a mid-pack architectural surah, NOT a top-tier outlier.**
- **Outlier-strength Δ%ile: −6.17 pp WEAK_ANCHOR** — `h-new-590.json` `all_surahs_results[X=36]`; Q 36 is the *opposite* of an outlier in its 7-window [33-39]: removing Q 36 *raises* the window's percentile, meaning Q 36 INCREASES window similarity. Q 36 is integrated in its mid-Meccan neighborhood, not architecturally distinct.
- **iʿjāz signature**: sig_A = **−0.7238** (rank 80/114, anti-structural-iʿjāz), sig_B = **−1.0711** (rank 85/114, anti-rhyme-purity) — `h-new-750.json`. Q 36 is **anti-iʿjāz al-fawāṣil** at the al-Bāqillānī axis.
- **Q 35 → Q 36 canonical-adjacency cost: rank 13/113** (delta = 0.1993, fraction-of-residual 2.40%) — `h-new-720.json`. The transition INTO Q 36 is moderately expensive (top-15 of 113).
- **Q 36 → Q 37 cost: rank 54/113** (cheap-to-mid; delta = 0.0662, fraction 0.80%). The transition OUT of Q 36 is unremarkable.
- **Mean Fisher-Rao distance to corpus**: 0.9430 — `h-new-111.json` D-matrix (computed); rank **64/114** (median band).
- **Nearest FR neighbors** (computed): Q 25 al-Furqān (0.778), Q 43 al-Zukhruf (0.787), Q 67 al-Mulk (0.794), Q 23 al-Muʾminūn (0.805), Q 15 al-Ḥijr (0.805) — all Meccan, prophetological-and-scripture-announcement.
- **Farthest FR neighbors**: Q 8 al-Anfāl (1.108), Q 33 al-Aḥzāb (1.117), Q 4 al-Nisāʾ (1.138), Q 9 al-Tawba (1.186), Q 55 al-Raḥmān (1.195) — all Medinan-legal or monorhyme-fawāṣil. Q 55 is corpus-farthest from Q 36.

## 7. Quick content structure

(Verse-by-verse in `02-content-analysis.md`.)

- **vv. 1-12 — Opening + Mission frame**. Muqaṭṭaʿāt (v.1) → oath-on-Quran + Muḥammad's apostleship (vv. 2-4) → revelation-from-the-Mighty-Merciful (v.5) → Meccan addressee-mission (vv. 6-12) → divine reckoning of all things in *imām mubīn* (v.12).
- **vv. 13-32 — Aṣḥāb al-Qarya (Companions of the City) narrative**. Three messengers (vv. 13-19) → the believing man from the far side of the city (vv. 20-27, climax: *yā layta qawmī yaʿlamūn*) → divine retribution (vv. 28-32). The longest sustained pericope in Q 36.
- **vv. 33-44 — Cosmic signs / āyāt**. Dead earth → fruit-and-water (33-35) → **Q 36:36 *subḥāna alladhī khalaqa al-azwāja kullahā*** (the pairs-creation hymn) → night-sun-moon (37-40) → ships and beasts of burden (41-44).
- **vv. 45-50 — Meccan rejecter sub-cycle**. Charge of *ghafla*; Resurrection-Day surprise scene (the Trumpet → graves opened, v.51 onward).
- **vv. 51-65 — Eschatological resurrection arc**. The Trumpet (*al-ṣūr*, v.51) → "from where they were sleeping" (v.52) → al-jannah-eligible greeting "salām qawlan min Rabbin Raḥīm" (v.58) → segregation of *al-mujrimūn* (vv. 59-64) → mouths-sealed-hands-and-feet-testify (v.65).
- **vv. 66-68 — Theodicy and aging**. Vision-blinding warning + creation-reversal sign-of-aging (Q 36:68 *wa man nuʿammirhu nunakkishu fī al-khalq*).
- **vv. 69-76 — "We did not teach him poetry" + creator-creation reflexivity**. Q 36:69 (*wa-mā ʿallamnāhu al-shiʿra*) → ownership-of-cattle (71-73) → polemic against false gods (74-76).
- **vv. 77-83 — Sealing argument: *kun fa-yakūn* + bone-revival**. The man-from-a-drop-doubts-resurrection scene (77-79) → Allāh as creator-of-bone-from-dust → **Q 36:82 *innamā amruhu idhā arāda shayʾan an yaqūla lahu kun fa-yakūn*** (the *kun fa-yakūn* climax) → Q 36:83 sealing tasbīḥ.

## 8. The "heart of the Qurʾān" status — empirical context

This investigation is launched into the literature's most-discussed Yāsīn claim: that Q 36 is the *qalb al-Qurʾān*. The project has **already empirically tested and rejected** the multi-axis quantitative form of this claim:

> [[h-new-82-yasin-heart|H-NEW-82]] (`findings/phase-b-hypotheses/h-new-82-yasin-heart.md`): across 6 pre-registered "heart" axes (mushaf-position median, verse-count median, letter-count median, lexical centroid, eigenvector centrality, theme centroid), **Q 36 ranks #1 on 0/6 axes and top-5 on 0/6 axes**. NULL verdict; classical hadith claim **not corroborated** by quantitative analysis.

The empirical positional median is **Q 57 al-Ḥadīd**; the empirical lexical centroid is **Q 10 Yūnus** with the al-Ḥawāmīm cluster (Q 40-46) close behind; the empirical FR-distance corpus centroid is **Q 112 al-Ikhlāṣ** (`h-new-111.json` D-matrix, rank 1/114 by minimum mean FR distance to all other surahs). On none of these axes is Q 36 even in the top-quintile.

In `06-novel-findings.md` we re-test this on a 7th axis (Q036-F-01 — the **liturgical-recitation-frequency-weighted-centrality** axis, the operationalisation H-NEW-82 explicitly excluded), with explicit pre-registration and equal-NULL-prominence discipline. The H-NEW-82 result is the binding prior and is not over-written by Q036-F-01.

## 9. Cross-references

- [[h-new-82-yasin-heart|H-NEW-82]] — the binding prior NULL on Q 36 "heart of the Qurʾān" claim (6 axes, 0 PASS).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 36 −6.17 pp WEAK_ANCHOR (window-integrated).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 35→Q 36 rank 13/113.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 36 sig_A = −0.7238 (rank 80), sig_B = −1.0711 (rank 85), nūn-final 84.34%.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 35/114.
- [[h-new-860-hadith-architectural-alignment|H-NEW-860]] — Q 36 hadith-fadāʾil score 10/10 (high) vs UAS rank 35/114 (mid). Most-striking divergence in the Q 36 row: classical fadāʾil pipeline elevates Q 36, the structural pipeline does not. Concretizes the **dual-iʿjāz orthogonality**: Q 36 is on the al-Khaṭṭābī meaning-iʿjāz axis without high al-Bāqillānī fawāṣil-iʿjāz.
- [[h-new-127-verse-fisher-rao-fractal|H-NEW-127]] — Q 36 verse-level FR optimality CONFIRMED (z = −2.82, p ≤ 0.0046 at Bonferroni-5 threshold 0.01) — Q 36's verse-order is information-geodesically optimal at the verse scale.
- [[h-new-134-mst-analysis|H-NEW-134]] — Q 36 partial metric-specific rehabilitation as MST-centroid (does NOT override H-NEW-82 NULL verdict).
- [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — YS-letter-centroid maps to ḤM-cluster centroid (unexpected; classically-plausible).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 36's **fourth-cell** (high-fadāʾil-meaning-iʿjāz, mid-UAS-structural-iʿjāz) profile.
- [[Q020-taha/00-overview|Q 20 Ṭāhā]] — only other 2-letter muqaṭṭaʿāt + Meccan + similar mid-narrative position (reciprocal).
- [[Q112-al-ikhlas/00-overview|Q 112 al-Ikhlāṣ]] — empirical FR-centroid + thuluth-al-Qurʾān / *qalb al-Qurʾān* contrast (reciprocal).
- [[Q067-al-mulk/00-overview|Q 67 al-Mulk]] — other recitation-saturated short-Meccan with al-Munjiya tradition (reciprocal); FR-near-neighbor of Q 36 (rank 3 closest at 0.794).
- [[Q001-al-fatiha/00-overview|Q 1 al-Fātiḥa]] — *umm al-Kitāb* (al-Bukhārī #4474 / al-Tirmidhī #2875) opening counterpart to Q 36's *qalb al-Qurʾān* (reciprocal).

## 10. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md (7 audits)
- [x] 06-novel-findings.md (4 pre-registered tests)
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 4 pre-regs in `preregs/`
- [x] 4 scripts in `scripts/`
- [x] 4 JSON outputs in `csv/`
