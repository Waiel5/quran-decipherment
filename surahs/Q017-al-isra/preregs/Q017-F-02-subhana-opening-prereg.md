---
id: Q017-F-02
title: Q 17 *Subḥāna* opening — uniqueness among musabbiḥāt verb-forms
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (no-tashkeel, orthographic-token, surah-opening-first-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q017-F-02 — *Subḥāna alladhī asrā* opening uniqueness (PRE-REG)

## Hypothesis (locked direction)

Among the seven musabbiḥāt (Q 17, 57, 59, 61, 62, 64, 87), Q 17 is the unique surah opening with the **maṣdar/proper-noun-form** *Subḥāna* (سبحان) — a verbal-noun construction with accusative-marker and *alladhī* relative-clause. The other six musabbiḥāt open with either:
- *sabbaḥa* (perfect verb): Q 57, 59, 61, 62
- *yusabbiḥu* (imperfect verb): Q 64
- *sabbiḥi* (imperative verb): Q 87

Direction: Q 17's opening *Subḥāna alladhī asrā* uses a verb-form attested in NO other surah's opening word. The maṣdar *subḥāna* opening is unique.

## Method

1. Load `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
2. For each surah, take verse 1's first orthographic token. (Skip basmala — it is verse 1 only in Q 1.)
3. Tabulate which surahs open with which form of root س-ب-ح: `سبحان` (maṣdar), `سبح` (perfect), `يسبح` (imperfect), `سبح`/`سبحي` (imperative).
4. Count each form's frequency among the 114 surahs.
5. NULL: another surah also opens with *Subḥāna* (or with the same maṣdar form).

## Success criteria

- DIRECTIONAL VINDICATION: only Q 17 opens with the *Subḥāna* maṣdar; the seven musabbiḥāt fall into 4 distinct verb-form buckets, with Q 17 alone in the maṣdar bucket.
- DIRECTIONAL FALSIFICATION: another surah also opens with *Subḥāna*.

## Bonferroni

Single uniqueness test (k=1) — α=0.05.

## NULL

If any other surah opens with the *Subḥāna*-maṣdar form, publish as NULL with full prominence.

## Classical anchor

Al-Suyūṭī, *al-Itqān*, file `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, refers to "ʿarāʾis al-Qurʾān" (the brides of the Qurʾān) as the **musabbiḥāt** — Q 17 is associated with this group via its tasbīḥ-opening. Verifying that Q 17 stands grammatically distinct within the group is a direct empirical test of classical taxonomy.
