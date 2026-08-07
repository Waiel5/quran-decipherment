---
finding_id: Q026-F-01
title: 7-prophet-refrain-cycle structure of Q 26 al-Shuʿarāʾ
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q026-F-01..F-05
alpha_bon: 0.01
acceptance_window: see §6
---

# Q026-F-01 — Prophet-refrain cycle structure


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

## 1. Hypothesis (locked before observation)

**H1.a (corpus-uniqueness)**: The full paired refrain
- R1 = "إن في ذلك لآية وما كان أكثرهم مؤمنين"  ("Indeed in that is a sign, and most of them were not believers")
- R2 = "وإن ربك لهو العزيز الرحيم"  ("And indeed your Lord — He is the Mighty, the Merciful")

(detected as `أكثرهم مؤمنين`-bearing verse for R1 and `العزيز الرحيم` rhyme tail for R2 — substring match; pause-marker ۖ tolerated)
occurs ≥ 6 paired refrain-cycles within Q 26, and the R2 phrase exact-match (`وإن ربك لهو العزيز الرحيم`) occurs **exclusively** in Q 26 across the corpus (≤ 1 occurrence outside Q 26 is acceptable for sensitivity).

**H1.b (cycle-progression)**: Inter-refrain cycle-lengths (in verses) are **monotone non-increasing** after the first prophet-cycle, OR show a structured progression captured by Spearman correlation `rho` between cycle-index and cycle-length with `|rho| ≥ 0.50`. Direction LOCKED: **negative rho** (later cycles are shorter — "compression-by-cycle" hypothesis, parallel to compression-tail). One-sided test, lower-tail.

**H0**: R2 is not corpus-unique to Q 26; cycles are not monotone; |rho| < 0.50 with neutral sign.

## 2. Operational definition

- Refrain R1 surface = any verse containing the substring `أكثرهم مؤمنين` (no-tashkeel).
- Refrain R2 surface = any verse containing the substring `وإن ربك لهو العزيز الرحيم` (no-tashkeel).
- A "cycle" = the verse-range from `(end_of_previous_R2 + 1)` through the next `R2`. Cycle 0 = the prologue (vv 1 through first R2). The 7 prophet-cycles = cycles 1..7. The post-R2 coda (after last R2 through v 227) = cycle 8.
- Cycle-length = (number of verses in the cycle) including the closing R1+R2 pair.

## 3. Test statistic

- `R2_count_in_Q26` (expected ≥ 6).
- `R2_count_outside_Q26` (expected ≤ 1).
- `R1_count_in_Q26` (expected to match R2 count within ±1).
- `rho` = Spearman(cycle_index, cycle_length) over the 7 prophet-cycles only (cycle 0 = prologue and cycle 8 = coda EXCLUDED — they are not prophet-cycles).
- `p_perm` = permutation null over rho: 10000 random permutations of cycle_lengths.

## 4. Direction (LOCKED)

- R2 corpus-uniqueness to Q 26: PRE-COMMIT direction = **YES** (≥ 99% of corpus R2-attestations in Q 26).
- rho < 0 (cycles get shorter as we go); pre-committed one-sided lower-tail.

## 5. Permutation null

Seed 20260507. 10000 perms.
For rho: shuffle the 7 cycle-lengths against fixed cycle-indices [1..7]; count rho_perm ≤ rho_obs (one-sided lower-tail); p = (1 + count) / (1 + 10000).

## 6. Bonferroni / acceptance

k=5 family (Q026-F-01..F-05). α_bon = 0.01.
- **CONFIRMED** = R2 corpus-unique-to-Q26 ≥ 6 hits AND |rho_obs| ≥ 0.50 in committed direction AND p_perm < 0.01.
- **DIRECTIONAL** = corpus-unique YES but rho fails (NULL on length progression).
- **NULL/PRE-COMMIT-VIOLATION** = R2 NOT corpus-unique OR rho positive (lengths increase).

## 7. Rules-tuple

`(no-tashkeel, orthographic-substring-match, pause-markers-tolerated, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

Corpus file: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`. All hits computed deterministically; no values cited until after run.

## 9. Honest a-priori limits

- The "7 prophet-narratives" claim is classical (al-Suyūṭī al-Itqān, al-Rāzī Mafātīḥ, al-Biqāʿī Naẓm al-Durar) — but the boundary verses depend on which scholar one follows. Our cycle-boundary definition is the R2-refrain-end rule (objective).
- Spearman with n=7 has limited power; a |rho| of 0.5 corresponds roughly to p ≈ 0.13 unpermuted; the 10000-perm test gives the exact distribution.
- Cycle 1 (Moses-Pharaoh) is the longest by raw narrative-tradition; cycles 3-7 (Abraham, Noah, Hud, Salih, Lot, Shuʿayb) are progressively shorter. The compression-by-cycle hypothesis is empirically motivated by the prologue-vs-coda structure of the surah.
