---
title: Surah-Completeness Audit — all 114 surah dirs vs the 8-file template
file_type: audit
date: 2026-05-29
phase: B+
author: Waiel Al-Shujaa
method: per-dir presence + substantiveness check (≥1200 bytes) of the 9 template files (8 content files + JOURNAL)
---

# Surah-Completeness Audit (2026-05-29)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Purpose

All 114 surahs have directories under `surahs/`. This audit checks, for each surah, which of the canonical
template files exist AND are **substantive** (not stubs), producing a completeness matrix to guide all future
per-surah work. The template (per `INVESTIGATION-PROTOCOL.md` §4) is 8 content files + a JOURNAL:

`00-overview · 01-empirical-profile · 02-content-analysis · 03-tafsir-survey · 04-hadith-corpus ·
05-classical-claims-audit · 06-novel-findings · 07-cross-references · JOURNAL`

## Method

- A file counts as **present + substantive** (✓) if it exists at the exact template path and is **≥ 1200 bytes**.
  Files below 1200 bytes, or absent, count as not-substantive (·). The 1200-byte threshold separates a genuine
  section from a stub/frontmatter-only placeholder; spot-checks confirmed every ✓ is real prose and every ·
  is absent (no borderline near-1200-byte stubs exist in the current tree — files are either full or absent).
- `#/9` = count of substantive files (max 9). Audit script logic in `scripts/` (deterministic, re-runnable).
- **State:** this matrix reflects the tree AFTER the two deep-dives completed in this same session (Q 3 Āl
  ʿImrān and Q 4 al-Nisāʾ, now 9/9). Q 66 al-Taḥrīm and Q 83 al-Muṭaffifīn (completed immediately prior) are
  also 9/9.

## Headline numbers

| Tier | #surahs | meaning |
|:--|:-:|:--|
| **Complete (9/9)** | **60** | full 8-file deep-dive done |
| Near-complete (7-8/9) | 5 | one or two files missing (Q002, Q031, Q065 @8; Q032, Q099 @7) |
| Partial (3-6/9) | 19 | overview + profile + some analysis, no tafsir/hadith/novel |
| Skeletal (1-2/9) | 20 | overview only (often + profile or JOURNAL) |
| **Empty (0/9)** | **10** | directory exists, no substantive content |

**10 fully-empty (0/9) surahs — the highest-priority stubs:**
Q 20 Ṭā-Hā · Q 71 Nūḥ · Q 84 al-Inshiqāq · Q 90 al-Balad · Q 92 al-Layl · Q 93 al-Ḍuḥā · Q 94 al-Sharḥ ·
Q 98 al-Bayyina · Q 102 al-Takāthur · Q 103 al-ʿAṣr.
(Before this session there were 12; Q 3 and Q 4 were two of them and are now complete.)

## The completeness matrix (114 × 9)

| Q | slug | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | JNL | #/9 |
|:--|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 001 | al-fatiha | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 002 | al-baqara | ✓ | ✓ | · | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **8** |
| 003 | al-imran | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 004 | al-nisa | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 005 | al-maida | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 006 | al-anam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 007 | al-araf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 008 | al-anfal | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 009 | al-tawba | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 010 | yunus | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 011 | hud | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 012 | yusuf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 013 | al-rad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 014 | ibrahim | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 015 | al-hijr | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 016 | al-nahl | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 017 | al-isra | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 018 | al-kahf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 019 | maryam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 020 | ta-ha | · | · | · | · | · | · | · | · | · | **0** |
| 021 | al-anbiya | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 022 | al-hajj | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 023 | al-muminun | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 024 | al-nur | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 025 | al-furqan | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 026 | al-shuara | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 027 | al-naml | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 028 | al-qasas | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 029 | al-ankabut | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 030 | al-rum | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 031 | luqman | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | **8** |
| 032 | al-sajda | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | **7** |
| 033 | al-ahzab | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 034 | saba | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 035 | fatir | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 036 | yasin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 037 | al-saffat | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 038 | sad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 039 | al-zumar | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 040 | ghafir | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 041 | fussilat | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 042 | al-shura | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 043 | al-zukhruf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 044 | al-dukhan | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 045 | al-jathiyah | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 046 | al-ahqaf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 047 | muhammad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 048 | al-fath | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 049 | al-hujurat | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 050 | qaf | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 051 | al-dhariyat | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 052 | al-tur | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · | **6** |
| 053 | al-najm | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 054 | al-qamar | ✓ | · | · | · | · | · | · | · | ✓ | **2** |
| 055 | al-rahman | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 056 | al-waqia | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 057 | al-hadid | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · | **6** |
| 058 | al-mujadala | ✓ | · | · | · | · | · | ✓ | · | ✓ | **3** |
| 059 | al-hashr | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 060 | al-mumtahana | ✓ | · | · | · | · | · | · | · | · | **1** |
| 061 | al-saff | ✓ | ✓ | ✓ | · | · | · | · | · | · | **3** |
| 062 | al-jumuah | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 063 | al-munafiqun | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | · | · | **5** |
| 064 | al-taghabun | ✓ | ✓ | ✓ | · | · | · | · | · | · | **3** |
| 065 | al-talaq | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | **8** |
| 066 | al-tahrim | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 067 | al-mulk | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 068 | al-qalam | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 069 | al-haqqa | ✓ | ✓ | ✓ | · | · | · | · | · | · | **3** |
| 070 | al-maarij | ✓ | ✓ | · | · | · | · | · | · | · | **2** |
| 071 | nuh | · | · | · | · | · | · | · | · | · | **0** |
| 072 | al-jinn | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 073 | al-muzzammil | ✓ | · | · | · | · | · | ✓ | · | ✓ | **3** |
| 074 | al-muddaththir | ✓ | · | · | · | · | · | · | · | ✓ | **2** |
| 075 | al-qiyama | ✓ | · | · | · | · | · | · | · | · | **1** |
| 076 | al-insan | ✓ | ✓ | · | · | · | · | · | · | · | **2** |
| 077 | al-mursalat | ✓ | · | · | · | · | · | · | · | · | **1** |
| 078 | al-naba | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 079 | al-naziat | ✓ | · | · | · | · | · | · | · | · | **1** |
| 080 | abasa | ✓ | · | · | · | · | · | · | · | · | **1** |
| 081 | al-takwir | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 082 | al-infitar | ✓ | · | · | · | · | · | · | · | · | **1** |
| 083 | al-mutaffifin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 084 | al-inshiqaq | · | · | · | · | · | · | · | · | · | **0** |
| 085 | al-buruj | ✓ | · | · | · | · | · | · | · | · | **1** |
| 086 | al-tariq | ✓ | · | · | · | · | · | · | · | · | **1** |
| 087 | al-ala | ✓ | ✓ | ✓ | · | · | · | · | · | · | **3** |
| 088 | al-ghashiya | ✓ | ✓ | · | · | · | · | · | · | · | **2** |
| 089 | al-fajr | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 090 | al-balad | · | · | · | · | · | · | · | · | · | **0** |
| 091 | al-shams | ✓ | · | · | · | · | · | · | · | · | **1** |
| 092 | al-layl | · | · | · | · | · | · | · | · | · | **0** |
| 093 | al-duha | · | · | · | · | · | · | · | · | · | **0** |
| 094 | al-sharh | · | · | · | · | · | · | · | · | · | **0** |
| 095 | al-tin | ✓ | ✓ | ✓ | · | · | · | · | · | · | **3** |
| 096 | al-alaq | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 097 | al-qadr | ✓ | · | · | · | · | · | · | · | · | **1** |
| 098 | al-bayyina | · | · | · | · | · | · | · | · | · | **0** |
| 099 | al-zalzala | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | · | · | **7** |
| 100 | al-adiyat | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 101 | al-qaria | ✓ | ✓ | · | · | · | · | · | · | · | **2** |
| 102 | al-takathur | · | · | · | · | · | · | · | · | · | **0** |
| 103 | al-asr | · | · | · | · | · | · | · | · | · | **0** |
| 104 | al-humaza | ✓ | ✓ | · | · | · | · | · | · | · | **2** |
| 105 | al-fil | ✓ | · | · | · | · | · | · | · | · | **1** |
| 106 | quraysh | ✓ | · | · | · | · | · | · | · | · | **1** |
| 107 | al-maun | ✓ | · | · | · | · | · | · | · | · | **1** |
| 108 | al-kawthar | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 109 | al-kafirun | ✓ | ✓ | ✓ | · | · | · | · | · | · | **3** |
| 110 | al-nasr | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 111 | al-masad | ✓ | ✓ | ✓ | ✓ | · | · | · | · | · | **4** |
| 112 | al-ikhlas | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 113 | al-falaq | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
| 114 | al-nas | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **9** |
### Distribution

| #substantive /9 | count | surahs |
|:-:|:-:|:--|
| 0 | 10 | Q020 ta-ha, Q071 nuh, Q084 al-inshiqaq, Q090 al-balad, Q092 al-layl, Q093 al-duha, Q094 al-sharh, Q098 al-bayyina, Q102 al-takathur, Q103 al-asr |
| 1 | 13 | Q060 al-mumtahana, Q075 al-qiyama, Q077 al-mursalat, Q079 al-naziat, Q080 abasa, Q082 al-infitar, Q085 al-buruj, Q086 al-tariq, Q091 al-shams, Q097 al-qadr, Q105 al-fil, Q106 quraysh, Q107 al-maun |
| 2 | 7 | Q054 al-qamar, Q070 al-maarij, Q074 al-muddaththir, Q076 al-insan, Q088 al-ghashiya, Q101 al-qaria, Q104 al-humaza |
| 3 | 8 | Q058 al-mujadala, Q061 al-saff, Q064 al-taghabun, Q069 al-haqqa, Q073 al-muzzammil, Q087 al-ala, Q095 al-tin, Q109 al-kafirun |
| 4 | 8 | Q059 al-hashr, Q062 al-jumuah, Q081 al-takwir, Q089 al-fajr, Q100 al-adiyat, Q108 al-kawthar, Q110 al-nasr, Q111 al-masad |
| 5 | 1 | Q063 al-munafiqun |
| 6 | 2 | Q052 al-tur, Q057 al-hadid |
| 7 | 2 | Q032 al-sajda, Q099 al-zalzala |
| 8 | 3 | Q002 al-baqara, Q031 luqman, Q065 al-talaq |
| 9 | 60 | Q001 al-fatiha, Q003 al-imran, Q004 al-nisa, Q005 al-maida, Q006 al-anam, Q007 al-araf, Q008 al-anfal, Q009 al-tawba, Q010 yunus, Q011 hud, Q012 yusuf, Q013 al-rad, Q014 ibrahim, Q015 al-hijr, Q016 al-nahl, Q017 al-isra, Q018 al-kahf, Q019 maryam, Q021 al-anbiya, Q022 al-hajj, Q023 al-muminun, Q024 al-nur, Q025 al-furqan, Q026 al-shuara, Q027 al-naml, Q028 al-qasas, Q029 al-ankabut, Q030 al-rum, Q033 al-ahzab, Q034 saba, Q035 fatir, Q036 yasin, Q037 al-saffat, Q038 sad, Q039 al-zumar, Q040 ghafir, Q041 fussilat, Q042 al-shura, Q043 al-zukhruf, Q044 al-dukhan, Q045 al-jathiyah, Q046 al-ahqaf, Q047 muhammad, Q048 al-fath, Q049 al-hujurat, Q050 qaf, Q051 al-dhariyat, Q053 al-najm, Q055 al-rahman, Q056 al-waqia, Q066 al-tahrim, Q067 al-mulk, Q068 al-qalam, Q072 al-jinn, Q078 al-naba, Q083 al-mutaffifin, Q096 al-alaq, Q112 al-ikhlas, Q113 al-falaq, Q114 al-nas |

## Ranked incompleteness (work-priority order)

Future surah work should proceed in roughly this order (most-incomplete first; within a tier, prioritise by
architectural significance / UAS rank and by length-of-material available):

1. **0/9 — fully empty (10):** Q 20 Ṭā-Hā (UAS rank 43; a major ṬH muqaṭṭaʿāt narrative — highest-priority of
   the empty set), Q 71 Nūḥ, Q 84 al-Inshiqāq, Q 90 al-Balad, Q 92 al-Layl, Q 93 al-Ḍuḥā, Q 94 al-Sharḥ,
   Q 98 al-Bayyina, Q 102 al-Takāthur, Q 103 al-ʿAṣr (short Meccan oath/wisdom surahs).
2. **1/9 — overview only (13):** Q 60, 75, 77, 79, 80, 82, 85, 86, 91, 97, 105, 106, 107.
3. **2/9 (7):** Q 54 al-Qamar, Q 70, 74, 76, 88, 101, 104.
4. **3/9 (8):** Q 58, 61, 64, 69, 73 al-Muzzammil, 87, 95, 109.
5. **4/9 (8):** Q 59, 62, 81, 89, 100, 108, 110, 111.
6. **5-8/9 (8):** Q 63 (5), Q 52 + Q 57 (6), Q 32 + Q 99 (7), Q 2 + Q 31 + Q 65 (8) — finish the missing files.

### Notable near-complete gaps worth closing first (low effort, high completeness gain)
- **Q 2 al-Baqara (8/9)** — missing only `02-content-analysis`. The corpus's longest surah; highest priority
  among the 8/9 tier.
- **Q 31 Luqmān (8/9)** — missing only JOURNAL.
- **Q 65 al-Ṭalāq (8/9)** — missing only JOURNAL.
- **Q 32 al-Sajda (7/9)** — missing 07-cross-references + JOURNAL.
- **Q 99 al-Zalzala (7/9)** — missing 07-cross-references + JOURNAL.

## This session's two completions (0/9 → 9/9)

Selected from the (then 12) empty 0/9 set by architectural significance + material richness; Q 66 / Q 83
excluded per instruction (just done):

| Surah | Why chosen | Landed finding (verdict) |
|:--|:--|:--|
| **Q 3 Āl ʿImrān** | al-sabʿ al-ṭiwāl; ALM; UAS rank 37; FR-nearest to Q 2; H-NEW-590 COHESION_ANCHOR (15.28); the longest empty surah | **Q003-F-01** — Arm A CONFIRMED ({2-5} rank-1/111 smoothest 4-block) + Arm B CONFIRMED (cohesion anchor) + **Arm C NULL** (block smoothness not beyond chance once 111-block multiplicity controlled, p=0.123) |
| **Q 4 al-Nisāʾ** | al-sabʿ al-ṭiwāl; UAS rank 26; |sig_A| 3.15 (corpus 2nd-largest); the lone alif-rhyme long surah; doubly-seamless | **Q004-F-06** — Arm A CONFIRMED (unique alif-rhyme among al-ṭiwāl) + Arm B CONFIRMED (sig_A rank 113/114, fawāṣil-variety minimum) + **Arm C NULL** (96.0% not a length-stratified extreme; Q17/Q18/Q23 exceed, pre-committed) |

Both deep-dives integrate real on-disk H-NEW metrics (h-new-111 FR, h-new-590 outlier, h-new-700 rhyme/phoneme,
h-new-720 TSP, h-new-750 iʿjāz, h-new-840 UAS — all cited to path), ≥5 mufassirūn (scholar+work+passage), and
9-book ḥadīth with `idInBook` verified on disk. Each landed test is SHA-locked (seed 20260509, 10,000 perms,
runtime-verified) with honest SPLIT verdicts (2 deterministic CONFIRMED + 1 permutation NULL each), reported
with equal NULL prominence per PRE-REG-STANDARD-04.

## Honest limits of this audit

- The 1200-byte threshold is a proxy for "substantive." It was validated against the current tree (no
  borderline stubs exist — files are either full prose or absent), but a future tree with near-threshold files
  would need manual review.
- "Substantive" measures presence + length, NOT depth-of-rigour. A 9/9 surah is structurally complete but not
  necessarily exhaustively investigated (per `INVESTIGATION-PROTOCOL.md` §11, true investigation-completeness
  additionally requires ≥5 claims audited, ≥3 novel tests, all metrics integrated — many 9/9 surahs meet this,
  but the audit does not verify it cell-by-cell).
- A few surah dirs carry extra pre-reg / script / csv files not counted in the 9-file matrix; those are
  supporting artifacts, not template files.

---

*Audit and the two completions by Waiel Al-Shujaa, 2026-05-29. Matrix re-runnable from the deterministic
presence+size check over `surahs/Q*/`.*

---

## Update 2026-05-30 — the 10 empty (0/9) stubs are now COMPLETE (Wave-O)

All ten formerly-empty surahs were brought to the full 8-file template (ledger §10.111-121): **Q20 Ṭā-Hā, Q71 Nūḥ, Q84 al-Inshiqāq, Q90 al-Balad, Q92 al-Layl, Q93 al-Ḍuḥā, Q94 al-Sharḥ, Q98 al-Bayyina, Q102 al-Takāthur, Q103 al-ʿAṣr.** Every surah in the corpus now has a substantive directory; the complete-count rises from 60 to ~70 (the 10 stubs + the earlier Q3/Q4 completions). Each carries ≥1 pre-registered, SHA-locked, runtime-verified novel test with an honest verdict.

**Remaining work for a future completeness pass** (from the matrix above, unchanged by Wave-O): the 5 near-complete (Q2 missing 02-content; Q31/Q65 missing JOURNAL; Q32/Q99 7/9), the 19 partial (3-6/9), and the 20 skeletal (1-2/9) surahs — these have *some* substantive files but are not yet at full 8-file depth. Priority order for the next surah-completion wave: skeletal → partial → near-complete quick-wins. Recommended concurrency cap: **≤4-5 heavy deep-dive agents** (the Wave-O 10-way launch hit a 600s stream-watchdog stall on 9/10; batches of 3-4 completed cleanly).
