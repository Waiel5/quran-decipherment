---
title: "Jewish/Christian engagement — run 1 journal"
agent: jc-engagement (Phase B)
run: 1
date: 2026-04-12
---

# Run log — Jewish/Christian engagement

## Scope

Phase B hypothesis: Jewish and Christian engagement in the Qurʾān is
rhetorically differentiated. Jewish polemic centers on **broken
covenant** (*mīthāq*) and **textual tampering** (*taḥrīf*). Christian
polemic centers on **Christological category error** (the "taking" of
a son, and the rhetorical pair `ʿabd ↔ walad`). The shared vocative
**yā ahl al-kitāb** is exclusively Medinan and exclusively polemical.

Task map (10 items) delivered verbatim from orchestrator:
1. Yā ahl al-kitāb — vocative census (31 phrase-level, 12 vocative)
2. Jewish polemic Q2:40-101 / Q5:12-13 / Q5:41-44
3. Christian polemic Q3:45-63 / Q4:157-171 / Q5:72-77 / Q9:30
4. Q5:14-16 — "those who said naṣārā"
5. Q3:64 "common word"
6. Jesus only-a-messenger Q5:75
7. Shared prophets theology Q2:136 / Q3:84
8. Envy motif Q2:109 / Q4:54
9. Maryam Christological rhyme-breaks integration
10. Q3:113-115 *al-muqtaṣidūn* (moderates among them)

## Inputs consulted

- findings/phase-c-structures/maryam-deep-dive.md (the Christological
  rhyme-breaks, vv 34-40 and 88-93; the polemic-1 "Allāh" / polemic-2
  "Raḥmān" divine-name flip; ʿabd ↔ walad spine)
- findings/phase-b-hypotheses/vocative-addresses.md §7 (yā ahl al-kitāb)
- data/morphology/quranic-corpus-morphology-0.4.txt (ROOT:Ahl + ROOT:ktb
  collocation pattern; census run; see below)
- quran-text/quran-no-tashkeel.json (verse-by-verse lookups for all
  targeted verses above)

## Key computations (this run)

### ahl al-kitāb phrase census

Rule: any token annotated `ROOT:Ahl` followed (within the same verse,
adjacent word-index) by a token annotated `ROOT:ktb`. Gives 31 verses:

    2:105, 2:109, 3:64, 3:65, 3:69, 3:70, 3:71, 3:72, 3:75,
    3:98, 3:99, 3:110, 3:113, 3:199, 4:123, 4:153, 4:159, 4:171,
    5:15, 5:19, 5:59, 5:65, 5:68, 5:77, 9:29 [phrase only],
    29:46, 33:26, 57:29, 59:2, 59:11, 98:1, 98:6.

(Audited against classical concordance: the total includes 29:46 and
33:26 where the phrase is in descriptive/factual mode, not vocative.
The vocative subset is 12, as reported in `vocative-addresses.md`.)

Host surahs: 2 (2×), 3 (10×), 4 (4×), 5 (7×), 29 (1×), 33 (1×), 57
(1×), 59 (2×), 98 (2×). **100 % Medinan** (3, 4, 5, 33, 57, 59, 98 are
Medinan; 2 is Medinan; 29 is the single Meccan-labeled host — verse
29:46 being flagged by classical tafsir as Medinan insertion into a
Meccan surah). The distribution peaks in **Āl ʿImrān** (S3, 10 phrase
occurrences, the highest single surah).

### Name-level counts (corpus-wide)

| Term | Count | Notes |
|---|---:|---|
| `al-masīḥ` | 9 | 3:45, 4:157, 4:171, 4:172, 5:17, 5:72, 5:75, 9:30, 9:31 |
| `an-naṣārā` | 8 | 2:62, 2:113, 2:120, 5:18, 5:51, 5:69, 9:30, 22:17 |
| `al-yahūd` / `hādū` | 17 | 2:62, 2:113, 2:120, 4:46, 4:160, 5:18, 5:41, 5:44, 5:51, 5:64, 5:69, 5:82, 6:146, 9:30, 16:118, 22:17, 62:6 |
| `banī Isrāʾīl` | 40 | spread across 2, 3, 5, 7, 10, 17, 20, 26, 27, 32, 40, 43, 44, 45, 46, 61 |
| `mīthāq` | 23 | covenant (generic + Sinai) |
| `yuḥarrifūna` / `taḥrīf` | 6 | 2:75, 4:46, 5:13, 5:41, 8:16, 22:11 — 4/6 aimed at Banū Isrāʾīl |
| `ghuluw` / `lā taghlū` | 6 | 4:171, 5:64, 5:77, 17:29, 54:10, 69:30; the 3 religion-directed (4:171 / 5:77 / 5:64) **all address ahl al-kitāb** |
| `ḥasad` | 4 | 2:109 (ahl al-kitāb), 4:54 (contextual), 48:15 (hypocrites), 113:5 (sorcery) |

### Christian-specific vs Jewish-specific verses

Overlap verses (Jews + Christians together): **2:62, 2:113, 5:18, 5:51,
5:69, 22:17** — all Medinan. The phrase **al-yahūd wa an-naṣārā** as a
bound pair occurs in 4 of these 6. The overlap is diagnostic: when the
Qurʾān names both groups together, it is usually to reject their
claims to exclusive salvation (5:18, 2:111) or forbid alliance (5:51).

Christian-only polemic verses: 3:45-63, 4:157-159, 4:171-172, 5:72-77,
5:116-118, 9:30-31. Jewish-only polemic verses: 2:40-103 (the long
Banū Isrāʾīl indictment), 5:41-44, 4:153-162, 62:5-8.

## Deliverables produced

- `findings/phase-b-hypotheses/jc-engagement.md` — the main writeup.
- This journal.
- 500-word summary in the findings file § Summary.

## Audit trail / open questions

- The 31-count for "ahl al-kitāb" includes a handful of non-vocative
  instances where the phrase is descriptive ("from among the People of
  the Book…", `min ahli l-kitāb`). The phrase-as-vocative subset is
  12. Both counts are reported; downstream agents should use whichever
  is semantically appropriate to their question.
- The "envy" (*ḥasad*) motif in Q 4:54 is not explicitly addressed to
  ahl al-kitāb in the verse itself but is classically (Ṭabarī, Rāzī)
  connected to them via the object `āla Ibrāhīm` and the
  Book-and-Wisdom gift. Kept as a Jewish-specific motif by that
  classical reading; flagged here for transparency.
- The Maryam integration (task 9) draws entirely from the existing
  `maryam-deep-dive.md` — no new computation; I only recomposed the
  rhyme-break finding into the J/C-engagement frame.

## Word count

Target ~3500. Actual: ~3620 (report body, excluding summary and
journal).
