---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-02
date_last_updated: 2026-04-28
phase: B+
verdict: NULL on density; H-NEW-95 comparator vindicated independently
prereg_sha: 3be0c7c69db7d18ab2938d462ba99c8c028afdcd7e5c8c75131f9e0d135fa8bd
---

# Q002-F-02 — Khawātim al-Baqara (Q 2:284-286) divine-name-density rank


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

## Target claim

al-Bukhārī ḥadīth tradition (multiple chains; ḥadīth ~#5009-5010) — the last three verses of al-Baqara *suffice* (kafatāhu) for nightly protection.

## Pre-registration

`Q002-F-02-khawatim-baqara-divine-name-density-prereg.md` (SHA256 3be0c7c69db7d18ab2938d462ba99c8c028afdcd7e5c8c75131f9e0d135fa8bd). Direction-LOCKED: TOP tail (top 5%, ideally top 1%).

## Empirical result

From `csv/Q002-F-02.json` (6,008 in-surah 3-verse sliding windows):

| Metric | Q 2:284-286 value | Rank / 6008 |
|:--|:--|:--|
| Window word-length | 119 | — |
| Name occurrences | 5 | — |
| Distinct names | 5 | — |
| Total density | 0.0420 | **2,839** |
| Distinct density | 0.0420 | **3,052** |

Comparator (the rank-1 triple from prior work):

| Metric | Q 59:22-24 value | Rank |
|:--|:--|:--|
| Total density | 0.45 | **2** |

## Verdict

**NULL on density-rank claim.** Q 2:284-286 sits near the median (rank 2839 / 6008 ≈ 47th percentile) — squarely in the middle of the corpus distribution by divine-name density. The hadith's "suffice" claim does NOT have a divine-name-density empirical correlate.

This contrasts sharply with the comparator Q 59:22-24, which IS rank 2 / 6008 — placing the asmāʾ al-ḥusnā concentration nearly at the empirical apex (the only stronger window contains Q 59:23 alone repeated, an artefact of the sliding-window). H-NEW-95's finding that Q 59:22-24 is the unique divine-name density peak is REINFORCED, not displaced, by this Q 2 audit.

## What this means

The "kafatāhu" / protection-virtue tradition of khawātim al-Baqara cannot be reduced to "many divine names." The hadith is grounded in:
- The themes (universal-mission of ʾāmana al-rasūlu, prayer for forgiveness, prayer for victory).
- The ritual function (recitation at night for protection).
- The summary-of-Quran character (faith-articles in 285).

NOT in raw asmāʾ density. This is a clean illustration of why classical fadāʾil traditions resist single-metric reduction: different surahs/verses are great for *different* reasons.

## Cross-corpus context

| Verse / window | Empirical signature | Source |
|:--|:--|:--|
| Q 2:255 | Top-5 by absolute name-count | [[Q002-F-01]] |
| Q 59:22-24 | Top-2 by 3-verse density | [[h-new-95]] + this study |
| Q 2:284-286 | Median by density (rank 2839) | this study (NULL) |
| Q 1 | Highest *outlier strength* in mufaṣṣal-1 | [[h-new-590]] |
| Q 112 | Highest *thuluth al-Qurʾān* (al-Bukhārī) | [[h-new-860]] |

Each of these is "great" by a *different* empirical metric — confirming the dual-iʿjāz typology (architectural-iʿjāz vs theological-iʿjāz) and the pluralism of fadāʾil signals.

## Honest limits

- Sliding-window in-surah-only excludes cross-surah windows; a more permissive comparator could shift Q 2:284-286 by hundreds of ranks but not break the median verdict.
- We did not compute thematic-content cohesion or syntactic-iltifāt density — both could plausibly correlate with the hadith claim. This test is one slice of a larger evaluation surface.

## Cross-references

- [[h-new-95-divine-name-density]] — sister test for Q 59 windows.
- [[h-new-860-hadith-architectural-alignment]] — UAS vs hadith fadāʾil orthogonality.
- [[Q002-al-baqara/04-hadith-corpus]] — full hadith chain on khawātim al-Baqara.

## Status

NULL on pre-committed direction. Pre-commit honoured.
