---
surah: 27
surah_name_ar: النمل
surah_name_translit: al-Naml
surah_name_english: The Ant
file_type: overview
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — all 8 template files + JOURNAL; 9 pre-registered novel tests (F-01..F-09). Wave-1 (2026-04-28): 3 CONFIRMED (F-01 naml 100%, F-02 lexical-match, F-03 Sulaymān rank 1 41%) + 1 MIXED (F-04 numerology). Wave-2 (2026-05-07): 4 DIRECTIONAL (F-05 second-basmala class=3 verses incl. NEW Q 11:41; F-06 hud-hud 8 hapaxes; F-08 Q 27↔Q 34 FR-closer than Q 27↔Q 38; F-09 Q 27:18 3-hapax floor met) + 1 WEAK_DIRECTIONAL (F-07 2-letter family).
---

# Q 27 al-Naml — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 27 | canonical |
| Arabic name | النمل | canonical |
| Transliteration | al-Naml | canonical |
| English meaning | "The Ant" — from the *namla*-warning narrative at vv. 18-19 | classical |
| Verse count | 93 | `/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv` (Hafs-Kufan) |
| Position in mushaf | 27 | canonical |
| Type | Meccan (Middle Meccan, per al-Suyūṭī chronology) | classical |
| Position in revelation order | 48 of 114 (Tanzil/Egyptian Standard); Nöldeke 68 (Middle Meccan) | `/Users/grey/Downloads/quran/data/revelation-order.csv` |
| Word count (no-tashkeel, orthographic) | 1,163 (computed) | `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel) | (not computed in this pass) | — |
| Opening | طس ۚ تلك آيات القرآن وكتاب مبين | muqaṭṭaʿāt + book-reference |

Note: prompt's pre-supplied "1,215 words" likely reflects a different tashkeel/tokenization rule. Under (no-tashkeel, orthographic, pause-marker stripped) the recomputed Q 27 word count is **1,163**. This rule-tuple sensitivity is documented (see §10).

## 2. Classical names

- **al-Naml** (النمل) — "The Ant" (canonical name; from v. 18 — the *namla*-warning).
- **Sūrat Sulaymān** (سورة سليمان) — sometimes used because of the dominant Sulaymān-Bilqīs narrative (vv. 15-44).

## 3. Opening formula — muqaṭṭaʿāt + book-reference (al-ṬS family)

Q 27 opens with **ṬS** muqaṭṭaʿāt (ṭāʾ-sīn) followed by *tilka āyātu al-Qurʾāni wa-kitābin mubīn* — "These are the verses of the Qurʾān and a Clear Book." This places Q 27 in the **ṭ-s/ṭ-s-m letter cluster**:

- Q 26 al-Shuʿarāʾ — opens ṬSM (ṭāʾ-sīn-mīm).
- Q 27 al-Naml — opens ṬS (ṭāʾ-sīn).
- Q 28 al-Qaṣaṣ — opens ṬSM (ṭāʾ-sīn-mīm).

The triplet Q 26-27-28 are the four prophets-narrative ṭ-s family. (See `[[h-new-600-letter-families]]` and §7 of this overview.)

## 4. ⭐ Unique structural feature — THE SECOND BASMALA

Q 27:30 is the **only verse in the entire Quran (outside surah-openings)** containing the full phrase *bismi llāhi al-raḥmāni al-raḥīm*. Cross-validated across all three tashkeel variants:

**Q 27:30 (no-tashkeel)**:
> إنه من سليمان وإنه بسم الله الرحمن الرحيم

**Q 27:30 (min-tashkeel)**:
> إِنَّهُ مِن سُلَيمٰنَ وَإِنَّهُ بِسمِ اللَّهِ الرَّحمٰنِ الرَّحيمِ

**Q 27:30 (full-tashkeel)**:
> إِنَّهُۥ مِن سُلَيۡمَٰنَ وَإِنَّهُۥ بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ

**Translation**: "It [the letter] is from Sulaymān, and it is: 'In the Name of God, the Most Gracious, the Most Merciful.'"

**Q027-F-02** confirmed (deterministic): the basmala-phrase slice from Q 27:30 (`بسم الله الرحمن الرحيم`) is **token-for-token identical to Q 1:1** under all three tashkeel variants. This is structurally non-trivial — see `06-novel-findings.md` and `Q027-F-02.json`.

## 5. ⭐ Other unique features

- Q 27 contains the **only Quranic mention of al-Hudhud (the hoopoe)** — Q 27:20 (one occurrence corpus-wide; Q027-F-01 sister test).
- Q 27 contains the **only narrative scene of an ant warning her colony** (vv. 18-19); *naml* (ant) tokens are 100% concentrated in Q 27 (3/3 — Q027-F-01 CONFIRMED).
- Q 27 names **Sulaymān** more than any other surah (7 of 17 corpus attestations = 41.2%; Q027-F-03 CONFIRMED rank 1, p_perm < 0.0001).
- Q 27 contains the only Quranic mention of **al-Dābba** (the eschatological Beast emerging from the earth) under the specific construction of v. 82.

## 6. Length classification

93 verses, 1,163 words (no-tashkeel) — **mufaṣṣal-ṭiwāl-adjacent / mid-Meccan medium length**. Position s=27 places Q 27 in the head-mushaf zone (well before the s=50 Hijra-kink of `[[h-new-660-compression-tail-gradient]]`).

## 7. Rhyme structure

Final-letter distribution across 93 verses (computed from no-tashkeel JSON, pause markers stripped):

| Letter | Count | % |
|:--|:-:|:-:|
| **ن (nūn)** | **84** | **90.3%** |
| م (mīm) | 8 | 8.6% |
| ۩ (sajda marker) | 1 | 1.1% |

**Rhyme entropy (Shannon, nats)**: **0.318** — quite low; near-monorhyme on -ūn/-īn endings.

This matches the iʿjāz signature pre-computed in `[[h-new-750-per-surah-iʿjāz-signature]]`: top_final_letter_frac = 0.9032, rhyme_entropy_nats = 0.3179. Q 27 is rhyme-uniform, like Q 12 Yūsuf — both heavily Sulaymān/Yūsuf prophet-narrative surahs.

## 8. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **23/114** (UAS = 1.023; abs_outlier = 8.76, max_cost = 0.081, abs_iʿjāz = 1.649).
- **Outlier-strength** Δ%ile = **−8.76pp** (WEAK_ANCHOR — Q 27 is mildly *more* cohesive with its window-7 neighbors than they are without it).
- **iʿjāz sig_A** = **−1.649** (rank 96/114) — LOW iʿjāz al-fawāṣil; the narrative-uniform rhyme structure penalizes the *i-jāz al-fawāṣil* metric (rhyme variety).
- **Mean content distance** (Q 27 vs other 113): **1.0077** (slightly above corpus mean — the Sulaymān-Bilqīs material is content-distinct).
- **Q 26 → Q 27 canonical-adjacency cost** (per `[[h-new-720-canonical-adjacency-cost]]`): **0.081** (low; both surahs in ṭ-s family).
- **Q 27 → Q 28 canonical-adjacency cost**: **0.059** (low; ṬSM continuation).

**Q 27 is content-anchor-mild within a tight ṭ-s prophet-narrative cluster, with sustained nūn-rhyme.**

## 9. Quick content structure

- vv. 1-6: opening — muqaṭṭaʿāt + book-reference + theological framing (guidance/warning).
- vv. 7-14: brief Mūsā narrative — fire-encounter, staff/hand signs, Pharaoh.
- vv. 15-44: **Sulaymān-Bilqīs cycle** (the surah's narrative center).
  - vv. 15-16: Sulaymān + Dāwūd's gifts; understanding the speech of birds (*manṭiq al-ṭayr*).
  - vv. 17-19: Sulaymān's host; the ant-warning (naml verses).
  - vv. 20-26: the missing Hudhud; report on Sheba's queen and her solar idolatry.
  - vv. 27-31: Sulaymān's letter sent via Hudhud; **Q 27:30 — the second basmala**.
  - vv. 32-37: Bilqīs's deliberation; sending gifts; Sulaymān refuses.
  - vv. 38-44: throne-bringing; pavilion-of-glass conversion.
- vv. 45-53: Ṣāliḥ + Thamūd narrative (the nine wicked clansmen).
- vv. 54-58: Lūṭ narrative (brief).
- vv. 59-66: theological refutation series (*amman khalaqa…* / *amman jaʿala…* refrain — the **al-Naml refrain**).
- vv. 67-75: resurrection-denial polemic.
- vv. 76-93: **eschatological closing** — Day of Resurrection signs.
  - v. 82: **al-Dābba** (the Beast) emerges from earth.
  - vv. 87-90: Trumpet, terror, mountains pass like clouds, judgment.
  - vv. 91-93: closing — Prophet's commission to recite this Qurʾān.

## 10. Rules-tuple notes & data discrepancies

- The pre-supplied "Q 27: 1,215 words" reflects a different tokenization (perhaps including Quranic-pause-markers as separators, or counting under min-tashkeel). Under default tuple (no-tashkeel, orthographic, pause-stripped), Q 27 is 1,163 words. Both are valid; tuple discipline is documented.
- The rhyme entropy 0.318 nats matches `h-new-750.json` to within rounding.

## 11. Cross-references

- [[h-new-590-outlier-spectrum]] — Q 27 −8.76pp WEAK_ANCHOR.
- [[h-new-840-unified-architectural-score]] — UAS rank 23/114.
- [[h-new-750-per-surah-iʿjāz-signature]] — Q 27 sig_A = −1.649, rank 96.
- [[h-new-720-canonical-adjacency-cost]] — Q 26-27 cost 0.081, Q 27-28 cost 0.059.
- [[h-new-700-phonological-compression-tail]] — Q 27 nūn-rhyme 90.3%.
- [[h-new-NEW-321]] — Q 1 ↔ Q 27 Basmala-echo NULL at 81%ile (FR cohesion); see `07-cross-references.md`.
- [[Q012-yusuf]] — sister late-Meccan prophet-narrative surah, similar rhyme uniformity.
- [[Q026-al-shuara]] / [[Q028-al-qasas]] — ṭ-s letter-family neighbors.

## 12. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md (Wave-1 F-01..F-04: see file; Wave-2 F-05..F-09: see file)
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] Wave-2 pre-regs: Q027-F-05..F-09 (5 new pre-regs, all SHA-locked, all run, all reported)
