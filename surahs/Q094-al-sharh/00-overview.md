---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
surah_name_english: "The Expansion / The Relief"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 1 pre-registered 3-arm test landed — ALL THREE ARMS CONFIRMED (corpus-singleton near-verbatim reprise + global min-edit adjacency + definite/indefinite orthographic asymmetry)
---

# Q 94 al-Sharḥ — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 94 | canonical |
| Arabic name | الشرح | canonical (verbal-noun *sharḥ*, "opening/expanding"; from v 1 *a-lam nashraḥ*) |
| Transliteration | al-Sharḥ | canonical |
| English meaning | "The Expansion / The Relief / The Solace" | classical |
| Alternative names | *Sūrat a-lam nashraḥ* / *al-Inshirāḥ* | al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, intro to Q 94 ("سورة ألم نشرح") |
| Verse count | 8 | Hafs-Kufan (`data/hafs-verse-counts.tsv` line 94 = "94	8"); al-Qurṭubī "وهي ثماني آيات" |
| Position in mushaf | 94 | canonical |
| Revelation order | #12 (Tanzil Egyptian Standard); Nöldeke #12 | `data/revelation-order.csv` (rev_order=12, mushaf=94) |
| Type | Meccan ("مكية في قول الجميع" — Meccan by all accounts) | al-Qurṭubī, intro to Q 94 |
| Word count (no-tashkeel, marks stripped) | 27 | computed (`scripts/Q094_F_01_usr_yusr_reprise.py` pipeline) |
| Letter count (no-tashkeel) | 102 | computed |
| Distinct QAC roots | 14 (16 root-tokens) | `data/morphology/root-index.json` |
| Opening | ألم نشرح لك صدرك — "Did We not expand for you your breast?" | rhetorical-interrogative (*a-lam* affirmation) |
| Predominant rhyme (rāwī) | three-zone: ـك (kāf, vv 1-4, 4/8 = 50%), ـا (alif, vv 5-6), ـب (bāʾ, vv 7-8) | `h-new-700.json` rhyme_letter_diagnostics (top letter ك, frac 0.5); close-read final-letter scan |
| Length class | mufaṣṣal-qiṣār (short mufaṣṣal; the muʿawwidhāt/early-Meccan short block) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 94 matters for the project

1. **The corpus's tightest near-verbatim adjacent couplet (Q094-F-01 Arm A + B, CONFIRMED).**
   Q 94:5-6 — *fa-inna maʿa al-ʿusri yusrā* (v 5) / *inna maʿa al-ʿusri yusrā* (v 6) — are
   character-identical **except** for the single leading connective fāʾ (فإن vs إن). Two corpus-wide
   results lock this:
   - It is the **UNIQUE** adjacent same-surah verse pair in the entire Quran differing by only a
     single leading connective particle (Arm A: count = 1, = Q 94:5-6).
   - It achieves the **GLOBAL minimum** character edit distance (=1) among all 5,821 substantive
     (≥3-word) adjacent same-surah pairs — rank 1 of 5,821 — and the corpus contains **zero**
     exact-verbatim adjacent pairs, so Q 94:5-6 is as close to verbatim adjacency as the Quran ever
     comes. Against a length-matched permutation null the observed edit-1 is extreme: null mean edit
     = 12.83, p_perm = 0.0003 (seed 20260509), replicated p = 0.0001 (seed 20260530).

2. **A near-verbatim reprise the strict verbatim refrain census MISSES.** H-NEW-2310 §1.1 catalogues
   24 *verbatim* intra-surah repeated strings; Q 94:5-6 is absent precisely because of the one-fāʾ
   delta. Q 94 therefore extends the project's repetition-architecture ladder with a new rung —
   **near-verbatim adjacent reprise** — that is invisible to byte-exact refrain counting (links
   H-NEW-2310 refrain / H-NEW-2100 reduplication / H-NEW-2140 anaphora).

3. **The definite/indefinite asymmetry is an exact orthographic fact (Q094-F-01 Arm C, CONFIRMED).**
   The classical "one hardship, two eases" reading rests on *al-ʿusr* being definite (الـ) in both
   verses and *yusr* indefinite (يسرا, tanwīn) in both. This is verified on disk: العسر in v 5 and v 6;
   يسرا in v 5 and v 6; v5/v6 root-Jaccard = exactly 1.0. The grammatical substrate of al-Ḥasan
   al-Baṣrī's *lan yaghliba ʿusrun yusrayn* is genuinely present in the text (the *theological*
   "two-eases" inference is out of scope per Protocol §10; only the orthographic asymmetry is verified).

4. **An FR / content-cohesion exemplar of the short-Meccan tail.** Q 94's mean Fisher-Rao distance to
   all 113 surahs is **0.7936** — far below the corpus mean 0.9235 — the surah sits deep inside the
   dense short-surah neighborhood (nearest neighbor Q 108 al-Kawthar at FR 0.2305). Its local_cohesion
   is 2.452 (z = +1.27, well above average) and its iʿjāz signature is high (sig_A rank 11/114, sig_B
   rank 13/114). Q 94 is a small, lexically-concentrated, internally-cohesive surah.

5. **The Q 93 → Q 94 seamless seam (paired-unit correlate).** Q 93 al-Ḍuḥā → Q 94 al-Sharḥ is a
   negative-delta seam (delta_raw = −0.0152, ascending-rank 10/113 — one of the smoothest joints in
   the mushaf). This gives a direct FR/TSP correlate to the classical observation that al-Ḍuḥā and
   al-Sharḥ form a *consolation pair* addressed to the Prophet (the *a-lam* / *waddaʿaka* solace
   diptych), and some early authorities recited them as a single unit. Corroborates H-NEW-2280
   (munāsabah-seam) at one of the project's smoothest adjacencies.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | **0.7936** (well below corpus mean 0.9235) | `h-new-111.json` (Q94 row) |
| Top-3 FR neighbors | Q 108 (0.231), Q 106 (0.271), Q 111 (0.287) | `h-new-111.json` |
| Q 93 (prev surah) rank in Q 94's FR list | 16/113 (FR 0.3641) | `h-new-111.json` |
| Q 95 (next surah) rank in Q 94's FR list | 15/113 (FR 0.3614) | `h-new-111.json` |
| Q 93 → Q 94 seam | delta_raw = −0.0152, asc-rank 10/113 (seamless) | `h-new-720.json` |
| Q 94 → Q 95 seam | delta_raw = +0.0470, asc-rank 43/113 | `h-new-720.json` |
| H-NEW-590 outlier | delta_pct = −0.07, **NULL** (cohesion member of Q 91-97 window) | `h-new-590.json` |
| H-NEW-700 rhyme | top letter ك, 50% (vv 1-4) — three-zone fawāṣil | `h-new-700.json` / `h-new-750.json` |
| H-NEW-750 sig_A | +1.7705 (rank **11/114**) | `h-new-750.json` |
| H-NEW-750 sig_B | +1.7603 (rank **13/114**) | `h-new-750.json` |
| H-NEW-750 local_cohesion | 2.4524 (z = +1.27, above average) | `h-new-750.json` |
| H-NEW-840 UAS | −0.6415 (rank 65/114) | `h-new-840.json` |
| Verses / words / letters / roots | 8 / 27 / 102 / 14 | computed |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| Breast-expansion (the *sharḥ al-ṣadr* favor) | 1 | *a-lam nashraḥ laka ṣadrak* — rhetorical-affirmative opener |
| Burden-removal | 2-3 | *wa-waḍaʿnā ʿanka wizrak* / *alladhī anqaḍa ẓahrak* — the lifted load that "weighed down the back" |
| Fame-raising | 4 | *wa-rafaʿnā laka dhikrak* — the elevated remembrance (closes the *-ka* address rhyme-zone) |
| The hardship-ease reprise | 5-6 | *fa-inna maʿa al-ʿusri yusrā* / *inna maʿa al-ʿusri yusrā* — the near-verbatim couplet (Q094-F-01) |
| The discharge-charge | 7-8 | *fa-idhā faraghta fa-nṣab* / *wa-ilā rabbika fa-rghab* — "when free, toil; to your Lord aspire" |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q094-F-01 Arm A | **CONFIRMED** | Q 94:5-6 is the UNIQUE corpus adjacent pair differing by only a single leading ف/و (فإن vs إن) |
| Q094-F-01 Arm B | **CONFIRMED** | Q 94:5-6 = global min char edit-distance (1) of 5,821 adjacent pairs; 0 exact-verbatim adjacencies; p_perm 0.0003 (rep 0.0001) |
| Q094-F-01 Arm C | **CONFIRMED** | definite al-ʿusr (both verses) + indefinite yusran (both) + root-Jaccard 1.0 — the *yusrayn* grammatical substrate is an exact orthographic fact |

## 6. Cross-references

- **H-NEW-2310** (refrain census) — Q 94:5-6 is the near-verbatim complement the *verbatim* census omits; new rung on the repetition ladder
- **H-NEW-2100 / H-NEW-2140** — within-verse reduplication / verse-initial anaphora; Q 94:5-6 is *inter*-verse near-verbatim reprise
- **H-NEW-720** — Q 93 → Q 94 seamless seam (asc-rank 10/113); Q 94 → Q 95 mid-spectrum
- **H-NEW-590** — Q 94 is a COHESION member of the {Q 91-97} window (delta_pct = −0.07, NULL)
- **H-NEW-2280** (munāsabah-seam) — the Q 93/94 consolation-pair seam is a smooth-adjacency correlate
- **Q 93 al-Ḍuḥā** — the paired consolation surah (FR rank 16; seamless seam); *a-lam* / *waddaʿaka* solace diptych
- **Q 108 al-Kawthar** — Q 94's nearest FR neighbor (0.231); short-Meccan gift/consolation register

## 7. Classical-tradition status

- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*): Meccan by consensus; 8 verses; named *Sūrat a-lam nashraḥ*; links
  94:1 to the *shaqq al-ṣadr* (chest-opening) ḥadīth (Anas ← Mālik b. Ṣaʿṣaʿa, "fī al-ṣaḥīḥ"); on 94:5
  gives the *taʾkīd* (al-Farrāʾ) vs *definite-repeated-is-same / indefinite-repeated-is-other* (Thaʿlab)
  vs the al-Jurjānī critique (*qawl madkhūl*, the sword-rider counterexample); reads the fāʾ-less v 6 as
  a fresh *ibtidāʾ*.
- al-Ṭabarī (*Jāmiʿ al-bayān*): on 94:5-6 transmits *lan yaghliba ʿusrun yusrayn* via al-Ḥasan al-Baṣrī
  (mursal, several chains: Yūnus, ʿAwf, Maʿmar) + Qatāda; reads the hardship as the Prophet's struggle
  against the mushrikūn.
- Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm*): the explicit grammar — *"al-ʿusr muʿarraf fī al-ḥālayn fa-huwa
  mufrad, wa-l-yusr munakkar fa-taʿaddad"* (one definite hardship, two indefinite eases); cites Ibn Abī
  Ḥātim ← Anas (ʿĀʾidh b. Shurayḥ, *fīhi ḍaʿf*) + al-Ḥasan mursal; on 94:7-8 the *farāgh*/worship charge.
- al-Zamakhsharī (*al-Kashshāf*, preserved in the al-Wāsiṭ/Ibn ʿĀshūr citation chain): the *fa-in qulta…
  qultu* dialectic — *maʿiyya* (accompaniment) of the near-future ease; the *yusrayn* as the Prophet's
  conquests / the Caliphs' conquests, or dunyā-ease + ākhira-ease; the indefinite *yusran* is *tafkhīm*
  (magnification).
- al-Bāqillānī (iʿjāz al-fawāṣil): the three-zone fawāṣil (-ka / -ā / -b); sig_A rank 11/114 — high
  structural-iʿjāz significance for so short a surah.

## 8. Open questions / queued tests

- Q094-F-02 (queued): the edit-2 runner-up family (Q 74:19-20, Q 75:34-35, Q 82:17-18, Q 102:3-4) — are
  these a coherent class of "graded-threat / oath reprises," and is Q 94:5-6 the only *consolation*
  member of the near-verbatim-adjacent set?
- Q094-F-03 (queued): test the Q 93 ↔ Q 94 paired-unit hypothesis at the pericope level (last-k of Q 93
  vs first-k of Q 94 vs a scrambled-adjacency null) — does the consolation diptych leave a shared-root
  seam trace beyond the raw TSP delta?
- Q094-F-04 (queued): is Q 94 the corpus's densest "second-person addressee" surah (the *-ka* suffix
  saturation across vv 1-4, 8) per word-token?

---

*Investigation: Wave-N (2026-05-30) Q 94 al-Sharḥ full deep-dive (the surah's first directory).
See JOURNAL.md for the method log; 06-novel-findings.md for test detail; 04-hadith-corpus.md for the
verified shaqq al-ṣadr chain.*
