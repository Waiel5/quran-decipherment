---
surah: 18
surah_name_ar: الكهف
surah_name_translit: al-Kahf
surah_name_english: The Cave
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — full 9-file template + 4 pre-regs + JOURNAL produced 2026-04-28 (Wave D launch)
---

# Q 18 al-Kahf — Overview


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
| Surah ID | 18 | canonical |
| Arabic name | الكهف | canonical (`quran-text/quran-no-tashkeel.json` Q18) |
| Transliteration | al-Kahf | canonical |
| English meaning | "The Cave" | from *aṣḥāb al-kahf* narrative vv. 9-26 |
| Verse count | **110** | Hafs-Kufan; cross-validated `quran-text/quran-no-tashkeel.json` |
| Position in mushaf | 18 | canonical |
| Type | Meccan (consensus, per al-Qurṭubī Q18 opening) | classical |
| Position in revelation order (al-Suyūṭī) | 69 of 114 | `data/revelation-order.csv` |
| Word count (no-tashkeel orthographic, mushaf-marks-stripped) | **1,583** | computed `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, no spaces, mushaf-marks-stripped) | **6,552** | computed |
| Total root-tokens (QAC v0.4) | **1,057** | rank 12/114 by total root-tokens; `data/morphology/quranic-corpus-morphology-0.4.txt` |
| Distinct roots | 369 | computed |
| Opening | الحمد لله الذي أنزل على عبده الكتاب ولم يجعل له عوجا — *al-ḥamdu lillāhi alladhī anzala ʿalā ʿabdihi al-kitāba wa-lam yajʿal lahu ʿiwajan* | one of 5 *al-ḥamdu lillāh*-opening surahs (Q 1, 6, 18, 34, 35) |
| Muqaṭṭaʿāt | **NONE** | unlike most ḥawāmīm and ALR-cluster prophet-narratives |
| Bismala status | counted only in Q1 (project rules-tuple) | per protocol |

## 2. Classical names

- **al-Kahf** (الكهف) — "The Cave" (after the *aṣḥāb al-kahf* narrative at vv. 9-26).
- The surah is classically referenced as one of the *al-musabbiḥāt* in some lists due to *al-ḥamdu lillāh* opening, though strictly the *musabbiḥāt* are surahs opening with the root *sbḥ*; al-ḥamd-openers (Q 1, 6, 18, 34, 35) form their own classical group (al-Suyūṭī, *al-Itqān*, nawʿ 17).

## 3. Opening formula — *al-ḥamdu lillāh* + meta-textual reference to revelation

Q 18:1-2:
> الحمد لله الذي أنزل على عبده الكتاب ولم يجعل له عوجا • قيما لينذر بأسا شديدا من لدنه ويبشر المؤمنين الذين يعملون الصالحات أن لهم أجرا حسنا

"Praise be to God who sent down the Book upon His servant and made it not crooked, [making it] straight, to warn of severe punishment from Him and to give good tidings to the believers who do righteous deeds — that for them is a goodly reward."

This is the **third of five** *al-ḥamdu lillāh*-opening surahs (after Q 1 al-Fātiḥa and Q 6 al-Anʿām, before Q 34 Sabaʾ and Q 35 Fāṭir). Q 18 is the only one of the five that is Meccan-mid-length without muqaṭṭaʿāt; Q 6 is much longer (Meccan-large), and Q 34, 35 sit in the ALM/ḥā-mīm/ALR-prophet-narrative zones.

The verse-1 *ʿabdihi* ("His servant") + *al-kitāb* ("the Book") pair is the surah's first signature — Q 18 announces itself as a revelation about the *kitāb-receiving servant* (Muḥammad).

## 4. Length classification

110 verses, 1,583 words, 1,057 root-tokens. **Meccan-mid (mufaṣṣal-ṭiwāl-adjacent zone)**: longer than the al-mufaṣṣal block but shorter than the al-sabʿ al-ṭiwāl. By verse-count Q 18 is closest to Q 19 Maryam (98 vv.), Q 21 al-Anbiyāʾ (112 vv.), Q 23 al-Muʾminūn (118 vv.) — the late-Meccan-large prophet-narrative block.

## 5. Rhyme structure — the alif-monorhyme cluster

Final-letter distribution across 110 verses (computed from `quran-text/quran-min-tashkeel.json`, last-word-stripped of remaining tashkeel):
- **ا (alif): 109 verses (99.09%)** — extreme monorhyme
- ى (alif maqṣūra): 1 verse (v. 13, *hudan* — هدى)

**Rhyme entropy (Shannon, nats): 0.0518** — *the SECOND-LOWEST in the corpus* among the 100%-or-near-100% monorhyme cluster. By H-NEW-750 ranking, Q 18 sits in the {Q 18, 48, 65, 72, 76, 91} alif-monorhyme cluster (Q 87, 92 end in *yāʾ*, NOT alif — see §11 of `05-classical-claims-audit.md`). Source: `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah[surah=18]`.

Q 18's 99.09% alif-monorhyme is the project's **largest near-monorhyme surah by verse-count** (110 verses; the next largest in the cluster is Q 76 at 31 verses). The alif-monorhyme phenomenon is therefore *unparalleled at this scale* — Q 18 sustains a single end-letter for 109 of 110 verses across 1,583 words.

## 6. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **46/114** — middle-ranked. Q 18 is NOT a top-decile UAS surah; it is *architecturally distinct in a different way*.
- **Outlier-strength** Δ%ile: **+0.39 pp** (rank 31/114) — WEAK_OUTLIER. Q 18's window {15-21} is the late-Meccan-prophet-narrative block; Q 18 fits this window's content register (Mūsā/Khaḍir is a prophet-narrative, like Q 19 Maryam, Q 21 al-Anbiyāʾ, etc.).
- **iʿjāz sig_A**: **−2.395 (rank 110/114)** — extreme anti-structural-iʿjāz (5th-from-bottom). Q 18 wins on *register-monolithic* alif-monorhyme + content-distance; the al-Bāqillānī fawāṣil-virtuosity is empirically inverted here.
- **Mean Fisher-Rao distance to corpus**: 1.0344 (rank 19/114, far above corpus mean 0.9235; high content-distance).
- **Q 17→Q 18 canonical-adjacency cost**: 0.0279 (rank 86/113 — CHEAP).
- **Q 18→Q 19 canonical-adjacency cost**: 0.0193 (rank 92/113 — CHEAP).

**Q 18 sits cheaply between its canonical neighbors.** Q 17 al-Isrāʾ and Q 19 Maryam are both Meccan-prophetic; Q 18 fits this zone naturally. This is the *opposite* of Q 24 al-Nūr's bracketing-cost geometry. Q 18 belongs structurally to its position; Q 24 disrupts its position.

## 7. Quick content structure — FOUR DISTINCT NARRATIVES

Q 18 is the corpus's **canonical four-narrative surah**:

| # | Narrative | Verses | Length (verses) | Subject |
|:-:|:--|:-:|:-:|:--|
| Frame opening | Praise + warning + *ʿiwaj* clause | 1-8 | 8 | book-as-revelation; warning-and-glad-tidings |
| **1** | **Aṣḥāb al-Kahf** (Companions of the Cave) | **9-26** | **18** | youth taking refuge in cave; sleep across-time miracle |
| Bridge A | Servant of God + Book + Patience | 27-31 | 5 | discipline of recitation; reward in heaven |
| **2** | **The two gardens** (parable of two men) | **32-44** | **13** | rich man's two gardens; blasphemy and destruction |
| Bridge B | Worldly-life parable + Day of Judgment | 45-59 | 15 | mirage; deeds-record; Iblīs; false reliance |
| **3** | **Mūsā and al-Khaḍir** (wisdom-test) | **60-82** | **23** | journey to *majmaʿ al-baḥrayn*; three trials |
| **4** | **Dhū al-Qarnayn** (geographic-eschatological) | **83-101** | **19** | east, west, Yājūj-Mājūj barrier |
| Frame closing | Believers' destiny + Q-as-revelation closing | 102-110 | 9 | Hell/Paradise; *qul innamā anā basharun mithlukum* |

The 4-narrative-block structure is locked at `findings/phase-b-hypotheses/h-new-268-kahf-four-narratives-prereg.md` with starts (9, 32, 60, 83). The empirical spacing-geometry test ([[h-new-268-kahf-four-narratives|H-NEW-268]]) found a **DIMENSION-SPECIFIC verdict** — the joint palindromic-expansion cell `d_outer_left = d_outer_right < d_middle` (gaps 23, 28, 23) survives Bonferroni-3 at p = 1089/135751 = 0.00802, against α_bon = 0.0167.

## 8. Friday-recitation tradition + 10-verses-Dajjāl-protection

Two of the corpus's most-cited Q 18 fadāʾil:

1. **Friday recitation**: al-Bayhaqī, al-Ḥākim, al-Suyūṭī *al-Itqān* — recommend reciting Sūrat al-Kahf on Fridays. Earliest canonical attestation is **al-Dārimī** (`data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/darimi.json`). al-Qurṭubī (`data/literature/classical-tafsir/raw/qurtubi-jami-ahkam.openiti.raw.txt`, Q18 opening): cites the al-Dārimī tradition that whoever reads Q 18 on Friday-night has light shining "between him and the Ancient House" (i.e., reaching the Kaʿba).

2. **10-verses-Dajjāl-protection**: **Muslim #1775** transmits via Abū al-Dardāʾ ← Maʿdān ← Sālim ← Qatāda: *"Whoever memorizes ten verses from the **first** of Sūrat al-Kahf will be protected from the Dajjāl"*. Variant in **Abū Dāwūd #4325**: same chain, but transmitted with two recensions — *"first ten"* (Hishām al-Dastawāʾī from Qatāda) and *"closing ten"* (Shuʿba from Qatāda). The textual variant is preserved in the canonical isnād. See `04-hadith-corpus.md` §3.

## 9. Cross-references

- [[h-new-268-kahf-four-narratives|H-NEW-268]] — Q 18 four-narrative spacing test, DIMENSION-SPECIFIC verdict (joint palindromic-expansion p = 0.00802, Bonferroni-3 pass).
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 18 WEAK_OUTLIER, Δ = +0.39 pp.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 17-18 cheap (rank 86/113); Q 18-19 cheap (rank 92/113).
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 18 sig_A = -2.395, rank 110/114 (extreme anti-iʿjāz); rhyme entropy 0.052 nats (extreme low).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 18 UAS = 0.046, rank 46/114 (mid).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 18 mean FR distance 1.0344 (rank 19/114 — high content-distance); FR-nearest = Q 7 al-Aʿrāf (0.871), Q 25 al-Furqān (0.879), Q 28 al-Qaṣaṣ (0.879); FR-farthest = Q 55 al-Raḥmān (1.271).
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 18 occupies the *anti-iʿjāz al-fawāṣil + monolithic-rhyme-register* cell (rank 110 sig_A combined with mid UAS).
- [[Q012-yusuf/00-overview|Q 12 Yūsuf]] — single-narrative comparator.
- [[Q017-al-isra/00-overview|Q 17 al-Isrāʾ]] — left canonical neighbour, alif-monorhyme cluster sibling.
- [[Q019-maryam/00-overview|Q 19 Maryam]] — right canonical neighbour, prophet-narrative sibling.

## 10. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md (≥6 mufassirūn, with rules-tuple discipline)
- [x] 04-hadith-corpus.md (all 9 books computed)
- [x] 05-classical-claims-audit.md (≥6 audits)
- [x] 06-novel-findings.md (4 pre-registered tests)
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 4 pre-regs in `preregs/`
- [x] 4 scripts in `scripts/`
- [x] 4 JSON outputs in `csv/`

## 11. Synthesis (one-paragraph)

Q 18 al-Kahf is the corpus's **canonical four-narrative surah** (aṣḥāb al-kahf, two gardens, Mūsā-Khaḍir, Dhū al-Qarnayn) rendered in a **register-monolithic** alif-monorhyme covering 109 of 110 verses (99.09%). It is empirically **anti-structural-iʿjāz** (sig_A rank 110/114, 5th-from-bottom on al-Bāqillānī's fawāṣil-virtuosity axis) yet sits cheaply between Q 17 and Q 19 (both adjacency costs in the bottom-third), giving it a moderate UAS (rank 46/114) with high mean content-distance (rank 19/114). Q 18 is structurally the inverse of Q 24 al-Nūr: where Q 24 disrupts its position with multi-rāwī rhyme and high adjacency cost, Q 18 fits its position with extreme single-rāwī rhyme and low adjacency cost. The four-narrative-spacing test ([[h-new-268-kahf-four-narratives|H-NEW-268]]) found the verse-index geometry to carry a real palindromic-expansion signature (p = 0.008, Bonferroni-3 pass). The Friday-recitation tradition and the 10-verses-Dajjāl-protection tradition are both attested in the canonical hadith corpus (Muslim #1775; Abū Dāwūd #4325; al-Dārimī), with the **first-vs-last-ten** textual variant preserved in the isnād. Pre-registered novel tests in this investigation address: (i) the actual 4-narrative word-count balance, (ii) Q 18's narrative-purity rank vs Q 12 Yūsuf, (iii) the 99.09% alif-monorhyme final-letter test, (iv) the Khaḍir-Mūsā passage's lexical-hapax signature within Q 18.
