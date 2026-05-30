---
surah: 84
surah_name_ar: الإنشقاق
surah_name_translit: al-Inshiqāq
surah_name_english: "The Splitting Open / The Rending Asunder"
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: 3 pre-registered tests landed — F-01 CONFIRMED (biplex idhā+sajda marker) + F-02 CONFIRMED (k-d-ḥ corpus-EXACT) + F-03 NULL (book-hand muqābala by lexical disjunction, pre-commit violation)
---

# Q 84 al-Inshiqāq — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 84 | canonical |
| Arabic name | الإنشقاق | from v 1 *inshaqqat* (root š-q-q, VII verbal noun *inshiqāq* "splitting/rending") |
| Transliteration | al-Inshiqāq | canonical |
| English meaning | "The Splitting Open / The Rending Asunder" | classical |
| Verse count | **25** (Hafs-Kufan) | `data/hafs-verse-counts.tsv` line 84 ("84\t25"); al-Qurṭubī "خمس وعشرون آية" |
| Verse-count variants | 23 / 24 / 25 | al-Suyūṭī, *al-Itqān*, nawʿ on ʿadad al-āy: "الانشقاق: عشرون وثلاث وقيل أربع وقيل خمس" (`suyuti-itqan.openiti.raw.txt` @238467) |
| Position in mushaf | 84 | canonical |
| Revelation order | **#83** (Tanzil Egyptian Standard); **Nöldeke #29, "Early Meccan"** | `data/revelation-order.csv` (row mushaf_order=84) |
| Type | **Meccan** ("مكية في قول الجميع" — Meccan by all accounts) | al-Qurṭubī on v 1; al-Ṭabarī, al-Zamakhsharī ("نزلت بعد الانفطار") |
| Word count (no-tashkeel, marks stripped) | 107 | computed (`quran-text/quran-no-tashkeel.json`) |
| Distinct QAC roots | **52** | `data/morphology/root-index.json` (Q84 attestations) |
| Opening | إذا السماء انشقت — *idhā al-samāʾu inshaqqat* | **idhā-cosmic-event opener** (H-NEW-1200 Sub-cluster A) |
| Predominant rhyme (rāwī) | ا (alif/-ā), top-letter frac 0.24; rhyme entropy 1.791 nats (highest-entropy band) | `h-new-750.json` (Q84) |
| Sajda | **Yes** — Q 84:21 carries the recitation-prostration glyph (۩) | classical-Sunnī sajda #13 (al-Suyūṭī *Itqān*; verified glyph on disk) |
| Length class | **mufaṣṣal-qiṣār** (short-mufaṣṣal; juzʾ-30 / al-ḥizb al-mufaṣṣal) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 84 matters for the project

1. **The corpus-unique biplex marker (Q084-F-01, CONFIRMED).** Q 84 is the *single* surah that is
   simultaneously (a) a member of the 5-surah idhā-cosmic-event-opener set {Q 56, 81, 82, 84, 99}
   (H-NEW-1200 Sub-cluster A) AND (b) a member of the 14-surah classical-Sunnī sajdat-al-tilāwa set
   {Q 7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96} (al-Suyūṭī *al-Itqān*, sajda mas'ala).
   The intersection of the two LOCKED classical sets is exactly {84}. Q 84 bridges the
   eschatological-content axis (idhā) and the liturgical-prostration axis (sajda).

2. **The k-d-ḥ corpus-anchor verse (Q084-F-02, CONFIRMED).** Q 84:6
   (*yā ayyuhā al-insānu innaka kādiḥun ilā rabbika kadḥan fa-mulāqīh*) contains BOTH attested
   surface-forms of the root **k-d-ḥ** (active participle *kādiḥ* + verbal-noun *kadḥ* in
   mafʿūl-muṭlaq construction) — and they are the ONLY two corpus tokens of the root. Q 84:6 is
   the corpus-EXACT anchor verse for k-d-ḥ. Classical balāgha (al-Zamakhsharī, al-Rāzī) treat the
   doubling as an intensity device; the empirical fact is that the root occurs nowhere else.

3. **The book-hand antithesis is built by lexical DISJUNCTION, not shared-anchor mirroring
   (Q084-F-03, NULL — pre-commit violation, full prominence).** The judgment diptych — right-hand
   party (vv 7-9) vs behind-back party (vv 10-15) — was pre-registered on the *muqābala* hypothesis
   that the two antithetical arms reuse shared anchor-roots with reversed valence. They share only
   4 roots (`Aty` give, `ktb` book, `Ahl` family, `srr` joy), which is FEWER than the
   length-matched null mean of 5.30 (z = −0.334, p = 0.613). Direction reversed → NULL.
   Mechanism: Q 84's mufaṣṣal-qiṣār verses are root-sparse (vv 7-15 union = 19 roots vs corpus
   9-verse-block mean 50.15), and the antithesis is realized by switching to *different* vocabulary
   for the two fates (burning/destruction/watching in arm B), not by repeating the same anchors.

4. **The suspended-apodosis idhā-cascade (links H-NEW-2250).** Q 84 opens with the eschatological
   *idhā…wa-idhā…* "when…" cascade whose jawāb al-sharṭ (apodosis) is deleted — the classical
   *iʿjāz* device al-Zamakhsharī describes as "ḥudhifa jawāb idhā li-yadhhaba al-muqaddar kull
   madhhab." H-NEW-2250 found this idhā-cascade head concentrates in juzʾ-30 (2.6×, p=0.00010),
   peaking in the s=78-93 band that explicitly names al-Inshiqāq. H-NEW-2250's Limit 2 flagged that
   its grammatical detector *fragments* Q 84's opening because 84:2/84:4 begin *wa*-VERB
   (*wa-adhinat*, *wa-alqat*), not *wa-idhā* — Q 84 is a semantically-merged but
   grammatically-broken cascade. Q 84 carries an internal verbatim refrain
   (v 2 ≡ v 5 = *wa-adhinat li-rabbihā wa-ḥuqqat*, corpus-unique) bracketing the two cosmic protases.

5. **A COHESION member of its window, not an outlier.** Under H-NEW-590, Q 84 (X=84, window Q 81-87)
   has Δ%ile = **−0.33, classification NULL** — Q 84 is *not* an outlier; it sits cohesively inside the
   short-mufaṣṣal eschatological block, consistent with H-NEW-1200's FR-cohesive idhā-opener finding.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | **0.8263** | `h-new-111.json` D_matrix (Q84 row) = `h-new-750.json` mean_content_distance |
| Top-3 FR neighbors | Q 103 (0.483), Q 108 (0.484), Q 106 (0.494) | `h-new-111.json` |
| Q 83 (prev) FR rank in Q 84's list | 33/113 (FR 0.6522) | `h-new-111.json` |
| Q 85 (next) FR rank | 25/113 (FR 0.5843) | `h-new-111.json` |
| Q 83 → Q 84 seam | delta_raw = +0.06459, rank 59/113 (mid) | `h-new-720.json` |
| Q 84 → Q 85 seam | delta_raw = +0.00691, rank 17/113 (seamless) | `h-new-720.json` |
| H-NEW-590 outlier | Δ%ile = **−0.33, NULL** (cohesion member of Q 81-87 window) | `h-new-590.json` (X=84) |
| H-NEW-750 sig_A | **+2.809 (rank 2/114)** — very high structural-iʿjāz | `h-new-750.json` |
| H-NEW-750 sig_B | +2.012 (rank 7/114) | `h-new-750.json` |
| H-NEW-840 UAS | +0.926 (rank **25/114**) | `h-new-840.json` |
| Rhyme entropy | 1.791 nats (z=+1.85; high-entropy multi-rāwī) | `h-new-750.json` |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| Cosmic-rending protasis 1 + comment | 1-2 | *idhā al-samāʾu inshaqqat* / *wa-adhinat li-rabbihā wa-ḥuqqat* |
| Cosmic-flattening protasis 2 + comment | 3-4 | *wa-idhā al-arḍu muddat* / *wa-alqat mā fīhā wa-takhallat* |
| Refrain (≡ v 2 verbatim) | 5 | *wa-adhinat li-rabbihā wa-ḥuqqat* — internal corpus-unique refrain |
| The toil-address (k-d-ḥ anchor) | 6 | *yā ayyuhā al-insānu innaka kādiḥun ilā rabbika kadḥan fa-mulāqīh* |
| Right-hand fate (arm A) | 7-9 | book in right hand → easy reckoning → returns joyful to family |
| Behind-back fate (arm B) | 10-15 | book behind back → calls ruin → burns → had-been-joyful / thought-no-return / Lord watching |
| Oath-triplet (lā uqsimu) | 16-18 | *fa-lā uqsimu bi-l-shafaq* / *wa-l-layli wa-mā wasaq* / *wa-l-qamari idhā ittasaq* |
| The graduated-stages declaration | 19 | *la-tarkabunna ṭabaqan ʿan ṭabaq* |
| Rebuke of the non-believers | 20-21 | *fa-mā lahum lā yuʾminūn* / *wa-idhā quriʾa ʿalayhim al-Qurʾānu lā yasjudūn ۩* (sajda) |
| The deniers concealing | 22-23 | *bal alladhīna kafarū yukadhdhibūn* / *wa-Allāhu aʿlamu bi-mā yūʿūn* |
| Painful-tiding + believer exception | 24-25 | *fa-bashshirhum bi-ʿadhābin alīm* / *illā alladhīna āmanū wa-ʿamilū al-ṣāliḥāt …* |

## 5. Pre-registered novel findings (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q084-F-01 | **CONFIRMED** | Q 84 = corpus-UNIQUE biplex idhā-opener ∩ sajda-surah marker (intersection = {84}, |I|=1) |
| Q084-F-02 | **CONFIRMED** | Root k-d-ḥ is corpus-EXACT to Q 84:6 (1 verse, 2 forms, mafʿūl-muṭlaq) |
| Q084-F-03 | **NULL (pre-commit violation)** | Book-hand muqābala (vv 7-9 ↔ vv 10-15) shares FEWER anchor-roots (4) than length-matched null mean (5.30); the antithesis is built by lexical disjunction, not shared-anchor reversal |

## 6. Cross-references

- **H-NEW-1200** — idhā-cosmic-opener set {Q 56, 81, 82, 84, 99} (FR-cohesive); Q 84's biplex membership.
- **H-NEW-1330 / H-NEW-1510** — sajda set (whole-surah NULL → pericope PASS); Q 84:21 is pericope #14 (thin, 10 roots).
- **H-NEW-2250** — idhā-cascade juzʾ-30 marker; Q 84 explicitly flagged in its Limit 2 (grammatical fragmentation).
- **H-NEW-590** — Q 84 is a COHESION member of the Q 81-87 window (Δ%ile = −0.33, NULL).
- **H-NEW-750** — Q 84 sig_A rank 2/114 (top structural-iʿjāz / *iʿjāz al-fawāṣil*).
- **Q 83 al-Muṭaffifīn** (prev) / **Q 85 al-Burūj** (next) — eschatological short-Meccan neighbors.
- **Q 81 al-Takwīr / Q 82 al-Infiṭār** — sibling idhā-openers; shared suspended-apodosis device (al-Zamakhsharī).
- **Q 69 al-Ḥāqqa** — the parallel book-hand scene (*bi-yamīnih* / *bi-shimālih*); al-Rāzī harmonizes Q 84:10's *warāʾa ẓahrih* with Q 69:25's *bi-shimālih*.

## 7. Classical-tradition status (detail in `03-tafsir-survey.md`)

- **al-Ṭabarī** (*Jāmiʿ al-bayān*): Meccan, 25 āyāt; *wa-adhinat* = "sami'at wa-aṭāʿat" (heard and obeyed) on the authority of Ibn ʿAbbās, Mujāhid, Qatāda, al-Ḍaḥḥāk.
- **al-Zamakhsharī** (*al-Kashshāf*): the deleted-apodosis *iʿjāz* — "ḥudhifa jawāb idhā li-yadhhaba al-muqaddar kull madhhab"; cross-references al-Takwīr + al-Infiṭār.
- **al-Rāzī** (*Mafātīḥ al-ghayb*): SIX positions on the suspended jawāb al-sharṭ; the kādiḥ embryo-analogy ("yā ayyuhā al-janīn innaka kādiḥun ilā an tanfaṣila"); six positions on *warāʾa ẓahrih*.
- **al-Qurṭubī** (*al-Jāmiʿ li-aḥkām*): Meccan by consensus, 25 āyāt; asbāb attributions (Abū Salama / al-Aswad b. ʿAbd al-Asad); the qirāʾāt of *yuṣallā/yaṣlā* v 12; the Bukhārī/Muslim/Tirmidhī ḥisāb-yasīr hadith.
- **Ibn Kathīr** (*Tafsīr al-Qurʾān al-ʿaẓīm*): the full sajda-isnād chain (Mālik→Abū Salama; Bukhārī→Abū Rāfiʿ; Muslim/Abū Dāwūd/Nasāʾī); the Jibrīl *fa-innaka mulāqīh* hadith.
- **al-Suyūṭī** (*al-Itqān*): al-Inshiqāq listed among the 14 ʿazāʾim al-sujūd; verse-count variants 23/24/25.

## 8. Open questions / queued tests

- **Q084-F-03b (queued):** re-test the book-hand antithesis under a *rate-normalized* statistic
  (shared-anchor count ÷ surah-internal root budget) rather than absolute count — the F-03 NULL is
  driven by mufaṣṣal-qiṣār root-sparsity, so a budget-normalized null may flip the verdict. This is a
  PRE-REGISTERED follow-up, NOT a post-hoc rescue of F-03 (the absolute-count direction lock stands as a NULL).
- **Q084-F-04 (queued):** the semantic-cascade-merge of vv 1-5 (resolving H-NEW-2250 Limit 2) —
  test whether the thematic idhā-cascade {v1, v3} (with wa-VERB comment verses interleaved) is a
  tighter eschatological-cosmic-event unit than the grammatical detector's fragments.
- **Q084-F-05 (queued):** is *wa-adhinat li-rabbihā wa-ḥuqqat* (v 2 ≡ v 5) the corpus's only
  intra-surah verbatim refrain among the mufaṣṣal-qiṣār idhā-openers? (Compare al-Raḥmān's
  *fa-biʾayyi ālāʾi rabbikumā* and al-Mursalāt's *waylun yawmaʾidhin li-l-mukadhdhibīn*.)

---

*Investigation: Wave-N (2026-05-30) Q 84 al-Inshiqāq full deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified sajda isnād chain.*
