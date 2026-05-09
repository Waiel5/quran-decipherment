---
surah: 67
surah_name_ar: الملك
surah_name_translit: al-Mulk
surah_name_english: The Dominion / Sovereignty
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 9 template files + JOURNAL (Wave-D 2026-04-28; Wave-H 2026-05-09 added 3 pre-regs/scripts/JSONs)
---

# Q 67 al-Mulk — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 67 | canonical |
| Arabic name | الملك | canonical |
| Transliteration | al-Mulk | canonical |
| English meaning | "The Dominion" / "The Sovereignty" / "The Kingship" | from Q 67:1 *bi-yadihi al-mulk* |
| Verse count | 30 | Hafs-Kufan; cross-checked against `quran-text/quran-no-tashkeel.json` Q67 |
| Position in mushaf | 67 | canonical |
| Type | Meccan | classical consensus (al-Suyūṭī, al-Qurṭubī, Ibn Kathīr) |
| Position in revelation order (al-Suyūṭī chronology) | 77 of 114 | `data/revelation-order.csv` (Nöldeke-Suyūṭī standard ordering) |
| Word count (no-tashkeel, mushaf-marks-stripped) | 333 | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, no-spaces) | 1,347 | computed from `quran-text/quran-no-tashkeel.json` |
| QAC root-tokens | 208 | `data/morphology/quranic-corpus-morphology-0.4.txt` |
| QAC distinct roots | 127 | same |
| Opening | تبارك الذي بيده الملك — "Blessed is He in whose hand is the dominion" | direct doxology |
| Muqaṭṭaʿāt | none | direct verse |
| Bismala status | counted as v.1 of `quran-text` only in Q1; printed but not numbered for Q67 | per project convention |

## 2. Classical names

Q 67 carries multiple classical names, each grounded in specific transmitted traditions:

- **al-Mulk** (الملك) — "The Dominion" — taken from the surah's first verse: *tabāraka al-ladhī bi-yadihi al-mulk* ("Blessed is He in whose hand is the dominion"). This is the dominant classical name and the project's reference name.
- **Tabāraka** (تبارك) — opening-word naming convention. Used in Tirmidhī #2890 and parallels: *kāna lā yanāmu ḥattā yaqraʾa … tabāraka alladhī bi-yadihi al-mulk* (Tirmidhī #2890 ahmedbaset-json idInBook 2975; see `04-hadith-corpus.md` §3).
- **al-Mānīʿa** (المانعة) — "The Preventer" / "The Protector" — from grave-protection tradition: this surah "prevents" (*tamnaʿu*) the punishment of the grave from its reciter. Traced via Ibn ʿAbbās in Tirmidhī (idInBook 2973). Verified in `04-hadith-corpus.md` §2.
- **al-Munjiya** (المنجية) — "The Saving One" — semantic parallel to *al-Mānīʿa*, recorded in Tirmidhī (idInBook 2973) and Dārimī (idInBook 2664; latter applied to *Alif-Lām-Mīm-Tanzīl* = Q 32, NOT to Q 67 directly — see audit 3 in `05-classical-claims-audit.md`).
- **al-Wāqīʿa al-Mujādila** (المجادلة) — "The Disputant" — from Tirmidhī #2890's text *tujādilu ʿan ṣāḥibihā* / *shafaʿat li-ṣāḥibihā* ("she pleads / disputes for her companion until forgiven"); recorded explicitly in Mālik *Muwaṭṭaʾ* idInBook 497 as *tujādilu ʿan ṣāḥibihā*.

NB the *al-Wāqiʿa* name is also used independently for Q 56; the *Mujādila*-by-itself name is reserved for Q 58. The Q 67 multi-name pattern is unusually rich.

## 3. Opening formula

**Doxological opening with *tabāraka*** — Q 67 begins with the verb *tabāraka* (perfect passive of *brk*, "be blessed / abundant in blessing"). This places Q 67 in the small *tabāraka*-opening cluster alongside Q 25 al-Furqān (which has 3 *tabāraka alladhī* occurrences at vv. 1, 10, 61). Across the Hafs-Kufan corpus, *tabāraka alladhī* (with relative pronoun) appears 5 times: Q 25:1, 25:10, 25:61, 43:85, **67:1** (computed from `quran-text/quran-no-tashkeel.json`).

The phrase *bi-yadihi al-mulk* ("in whose hand is the dominion") is a **corpus-singleton** at Q 67:1 — the exact 2-word phrase appears nowhere else in the Quran (computed from full corpus search; see `06-novel-findings.md` Q067-F-03).

## 4. Length classification

30 verses, 333 words. Per al-Suyūṭī's *al-Itqān fī ʿulūm al-Qurʾān* (nawʿ 1) tier-system, Q 67 sits in **al-mufaṣṣal-awsāṭ** (the middle-mufaṣṣal) — the tier of surahs from approximately Q 50 (Qāf) through Q 77 (al-Mursalāt) before the muʿawwidhāt-zone short surahs begin. Word-count (333) and verse-count (30) both place it near the corpus mean for Meccan-mufaṣṣal surahs.

## 5. Rhyme structure

Final-letter distribution across 30 verses (computed from `quran-text/quran-min-tashkeel.json`):

| Final letter | Count | Fraction |
|:--|:-:|:-:|
| ر (rāʾ) | 21 | 70.0% |
| ن (nūn) | 7 | 23.3% |
| م (mīm) | 2 | 6.7% |

**Rhyme entropy (Shannon, nats): 0.7698** — moderately monorhyme, dominant rāwī ر (rāʾ).

This matches `findings/phase-b-hypotheses/csv/h-new-750.json` `per_surah[surah=67]`: `rhyme_entropy_nats: 0.7698, top_final_letter: ر (70.0%)`.

The dominant rāwī ر serves *fawāṣil* with -īr (*qadīr* v.1, *ghafūr* v.2, *fuṭūr* v.3, *ḥasīr* v.4, *saʿīr* vv.5/10/11, *maṣīr* v.6, *tafūr* v.7, *nadhīr* vv.8/9/17/26, *kabīr* vv.9/12, *khabīr* v.14, *nushūr* v.15, *nakīr* v.18, *baṣīr* v.19, *ghurūr* v.20, *nufūr* v.21, *mustaqīm* v.22 [pivot], *tashkurūn* v.23 [pivot], *muʿīn* v.30) — the *-īr / -ūr* fawāṣila family. The 30% non-ر fawāṣila concentrate at vv. 22-23, 24-26, 28-30 — the closing rhetorical-question-cluster.

## 6. Empirical architectural profile

See `01-empirical-profile.md` for full integration. Headline:

- **UAS rank**: **102 / 114** (`findings/phase-b-hypotheses/csv/h-new-840.json`, `all_uas[surah=67]`: UAS=−2.053, abs_outlier=0.20, max_cost=0.096, abs_ijaz=0.311) — **Q 67 is in the bottom-decile of architectural significance by the project's compound metric**, despite its high recitation-tradition status.
- **Outlier-strength Δ%ile**: **−0.20 pp** — `h-new-590.json` classifies Q 67 as **NULL** (no outlier signal in its 7-window {64-70}).
- **iʿjāz sig_A**: **+0.311 (rank 52/114)** — middling structural-iʿjāz score; *not* in the high-fawāṣil tier (which is dominated by Q 55, Q 84, Q 100).
- **Q 66 → Q 67 canonical-adjacency cost**: 0.0780 length-units (rank **47/113**) — mid-pack, *not* high-cost.
- **Q 67 → Q 68 canonical-adjacency cost**: 0.0962 length-units (rank **36/113**) — also mid-pack.
- **Mean FR distance to corpus**: 0.892 (rank 67/114) — middle-of-pack content register.
- **Nearest 5 FR neighbours**: Q 81, Q 32, Q 105, Q 1, Q 112 (computed from QAC stem-roots, K=500, Dirichlet α=0.5; see `01-empirical-profile.md` §4).

**Headline empirical verdict**: **the recitation-tradition prominence of Q 67 (al-Mānīʿa / al-Munjiya, Tirmidhī #2890, nightly Prophetic recitation) does NOT align with elevated empirical-architectural-significance scores.** Q 67's UAS rank of 102/114 is in the same bottom-decile cell as Q 112, Q 87, Q 73, Q 83 — the project's *theological-iʿjāz / faḍāʾil-rich-but-architecturally-modest* zone (see [[h-new-840-unified-architectural-score|H-NEW-840]] and [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]).

This is a substantive empirical NULL on the cross-validation hypothesis "high-faḍāʾil surahs should rank highly on UAS." It joins Q 112 al-Ikhlāṣ and Q 36 Yāsīn as confirming cases that **architectural-iʿjāz and theological-iʿjāz are empirically orthogonal axes** (cf. [[cross-finding-026-iʿjāz-architecture|cross-finding-026]]; al-Khaṭṭābī's *iʿjāz al-maʿnā* lineage).

## 7. Quick content structure

Q 67 unfolds as a coherent dominion-creation-eschatology arc, in three movements:

| Block | Verses | Theme | Key lexicon |
|:-:|:-:|:--|:--|
| A | 1-2 | Doxology of dominion | *al-mulk*, *qadīr*, *al-ʿazīz al-ghafūr* |
| B | 3-5 | Cosmological dominion: 7-heavens *ṭibāq* + visual return | *sabʿa samāwātin ṭibāqan*, *fa-rjiʿi al-baṣar*, *maṣābīḥ*, *rujūm li-l-shayāṭīn* |
| C | 6-11 | Hellfire: *Saʿīr*'s reception of disbelievers | *jahannam*, *al-saʿīr*, *shahīq*, *fawj*, *nadhīr* |
| D | 12-15 | Believers vs. disbelievers contrast + earth-as-tame | *fī al-ghayb*, *maghfira wa-ajr kabīr*, *al-arḍ dhalūl* |
| E | 16-19 | Cosmic terror + birds-with-outstretched-wings | *yakhsifu bi-kum al-arḍ*, *al-ṭayr fawqa-hum ṣāffāt* |
| F | 20-22 | Disbelievers' delusion: tropic interrogatives | *amman hādhā alladhī huwa jund*, *amman hādhā alladhī yarzuqu-kum* |
| G | 23-27 | Five *qul* commandments + the Day's terror | *qul huwa al-ladhī anshaʾakum*, *fa-lammā raʾaw-hu zulfatan* |
| H | 28-30 | Final three *qul*-rhetorical-prophetic-stance | *qul aʾraʾaytum in ahlakanī*, *qul huwa al-Raḥmān*, *qul aʾraʾaytum in aṣbaḥa māʾukum ghawran* |

Five *qul* imperatives at vv. 23, 24, 26, 28, 29, 30 (counting v. 30's opening) — a high-density of imperative-prophetic-instruction near the surah's close.

## 8. Q 67:1 — the *al-mulk*-naming verse

> تبارك الذي بيده الملك وهو على كل شيء قدير

"Blessed is He in whose hand is the dominion, and He is, over all things, ever-Powerful."

The 2-word phrase *bi-yadihi al-mulk* is a **corpus-singleton** (computed: 1 occurrence in 6,236 verses, only Q 67:1; see `06-novel-findings.md` Q067-F-03). The closest cognate is Q 3:26 *qul Allāhumma mālika al-mulk tuʾtī al-mulka man tashāʾu wa-tanziʿu al-mulka mim-man tashāʾ* (the divine-king-formula), where the *mulk*-stem is concentrated 3× in one verse but not in the *bi-yadihi* construction.

## 9. The *fa-rjiʿi al-baṣar* / 7-heavens-*ṭibāq* signature (Q 67:3-4)

> الذي خلق سبع سماوات طباقا ما ترى في خلق الرحمن من تفاوت فارجع البصر هل ترى من فطور . ثم ارجع البصر كرتين ينقلب إليك البصر خاسئا وهو حسير

(v. 3) "He who created seven heavens *ṭibāq* (in layers / matching). You see in the creation of al-Raḥmān no flaw. So return the gaze: do you see any fissure?
(v. 4) Then return the gaze a second time: the gaze will return to you humbled and exhausted."

Cross-corpus check (computed): the phrase *sabʿa samāwātin ṭibāqan* appears at exactly **2 verses**: Q 67:3 and Q 71:15 (al-Suyūṭī's "Nūḥ-surah" cosmology). The verb-imperative *fa-rjiʿi al-baṣar* (with fāʾ-prefix) is a **corpus-singleton** at Q 67:3; the bare *irjiʿi al-baṣar* repeats at Q 67:4 (only). The 4-word imperative-cluster *ṭibāq* / *fa-rjiʿi al-baṣar* / *karratayn* / *khāsiʾan* is unique to Q 67:3-4. See `06-novel-findings.md` Q067-F-03 for full cross-corpus uniqueness audit.

## 10. Position in the s=50 Hijra-kink architecture

Q 67 sits at **s = 67**, well past the project's pre-registered Hijra-kink at s = 50 ([[h-new-660-compression-tail-gradient|H-NEW-660]], R²=0.986). The compression-tail predicts d̄_content for surahs s>50 to be:

> d̄_content(s) ≈ 0.96 − 0.012 · max(0, s−50)

For s=67: predicted d̄_content ≈ 0.96 − 0.012·17 = **0.756**.

Q 67 sits within the **post-Hijra-kink mufaṣṣal zone**. See `01-empirical-profile.md` §10 for full position-cost breakdown. Direct test of "Q 67 is architecturally distinct from pre-kink surahs" (Q067-F-02): pre-registered, run, **NULL** for distinctness — Q 67's content-distance and rhyme-dispersion are *typical* for the post-kink zone, not enhanced.

## 11. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 67 outlier-strength Δ = −0.20 pp; classification NULL; window {64-70}.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 67 UAS = −2.053, rank 102/114 (bottom-decile).
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 66-Q 67 cost rank 47/113; Q 67-Q 68 rank 36/113. Both mid-pack.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 67 sig_A=+0.311 (rank 52/114), sig_B=−0.566 (rank 67), rhyme entropy 0.770 (rank ~38).
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 67 mean FR distance to corpus 0.892 (rank 67/114, middle-of-pack).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 67 sits at s=67 in the post-kink mufaṣṣal zone.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 67 confirms *theological-iʿjāz / architectural-iʿjāz orthogonality* cell (high-faḍāʾil + low-UAS), alongside Q 112 and Q 36.

## 12. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md (≥6 audits)
- [x] 06-novel-findings.md (**7 pre-registered tests** — Wave-D F-01..04 + Wave-H F-05..07)
- [x] 07-cross-references.md
- [x] JOURNAL.md (Wave-D + Wave-H entries)
- [x] 7 pre-regs in `preregs/`
- [x] 7 scripts in `scripts/`
- [x] 7 JSON outputs in `csv/`
