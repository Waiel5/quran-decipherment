---
id: H-NEW-2310
title: "Refrain / exact-repeated-verse structure — full census + spacing-regularity test"
type: pre-registration
date_locked: 2026-05-29
phase: B+
author: Waiel Al-Shujaa
status: LOCKED-BEFORE-COMPUTATION
seed: 20260509
n_perm: 10000
rules_tuple: "(no-tashkeel, orthographic-token verse-string, NFC + whitespace-collapsed, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# Pre-registration — H-NEW-2310: Refrain / exact-repeated-verse structure

## 0. Relationship to prior work (NOT a re-run)

The refrain **inventory** is already established at corpus-EXACT precision by three
inter-verifying findings: H-NEW-1230 (combined-count axis), H-NEW-1320 (max-count
axis), H-NEW-1790 (saturation + strict-≥3 enumeration). Those findings answer
*which surahs and which verses* carry refrains, and *how many times*.

H-NEW-2310 asks a **new, orthogonal question**: among a refrain-bearing surah's
verses, are the refrain occurrences **placed more regularly** (lower variance of
inter-refrain gaps) than a random placement of the same number of dividers among
the surah's verses? This is a test of the "refrain = structural section-marker"
intuition (al-Zarkashī *al-Burhān* nawʿ on *al-tikrār*; al-Suyūṭī *al-Itqān*
nawʿ 60 on repetition's structural role). The spacing-regularity test has **not**
been run by any prior finding. H-NEW-2310 additionally produces the **complete
machine-generated census** of every verse-string appearing ≥2× anywhere in the
corpus (intra- and cross-surah), with counts and (surah:ayah) positions, as a
single reproducible artifact.

## 1. Census (descriptive, no inferential claim)

**Refrain-detection rule (LOCKED):**
1. Load `quran-text/quran-no-tashkeel.json`.
2. For every verse, normalize: `unicodedata.normalize("NFC", text)` then
   collapse all runs of whitespace to a single space and strip
   (`" ".join(text.split())`). No further stripping (recitation marks such as
   the small ۖ remain part of the string, as they are in the no-tashkeel file).
3. A **repeated verse** is any normalized verse-string with global count ≥2.
4. Report for each repeated string: global count, intra-surah maximum count,
   and the full list of (surah, ayah) attestations.
5. Separately report **near-exact** repeats: pairs of distinct normalized strings
   whose edit (Levenshtein) ratio ≥0.90 AND that are not already exact-equal,
   to surface refrains that differ by a single particle. Near-exact is a
   descriptive supplement (MW-7 capped, no inferential claim).

The census carries **no p-value**; it is a factual enumeration filed for the record.

## 2. Inferential hypothesis — spacing regularity (DIRECTION-LOCKED)

### 2.1 Test family
The inferential family is every **(surah, refrain-string)** pair in which that
exact normalized string occurs **≥4 times within the surah**. (Refrain repeats
≥4 is the threshold given in the task: "Q 55 … Q 77 … and any other surah with
≥4 refrain repeats.") The family is enumerated FROM DISK at runtime; the count k
is whatever the data yields and is used as the Bonferroni divisor.

### 2.2 Statistic
For a (surah, refrain) pair with occurrences at 1-indexed verse positions
`p_1 < p_2 < … < p_m` in a surah of `N` verses, define the inter-refrain gaps
`g_i = p_{i+1} − p_i` (m−1 gaps) and the statistic

    V_obs = population variance of {g_1, …, g_{m-1}}.

Lower V = more regular spacing.

### 2.3 Null model (random divider placement)
Under H0 the m refrain-verses are placed at m positions chosen **uniformly at
random without replacement** from the N verse-positions of the surah (i.e. a
random m-subset of {1,…,N}). For each of `N_PERM = 10000` draws (seed=20260509,
one `random.Random` per pair, re-seeded deterministically as
`SEED + surah*1000 + family_index`), compute the gap-variance V_perm. This is the
"random placement of the same number of dividers among the surah's verses" null
the task specifies.

### 2.4 Direction (LOCKED — must not change after observation)
**Refrain occurrences are STRUCTURAL DIVIDERS placed MORE REGULARLY than chance:
V_obs is LOWER than the null.** One-sided left-tail p-value:

    p = (1 + #{V_perm ≤ V_obs}) / (N_PERM + 1).

A result in the OPPOSITE direction (V_obs at or above the null median, i.e. spacing
no more regular — or LESS regular — than random) is a **pre-commit-direction
NULL** and will be published with equal prominence. Irregular spacing would itself
refine the "refrain = section marker" intuition (refrains as *rhythmic-emphatic*
rather than *evenly-partitioning* devices), and that interpretation is stated in
advance so it cannot be presented as a confirmation.

### 2.5 Bonferroni
k = number of (surah, refrain) pairs in the ≥4 family (computed at runtime).
α_bon = 0.05 / k. A pair is "regular" only if p_pair ≤ α_bon. Both raw and
Bonferroni-corrected verdicts are reported.

### 2.6 Success / failure criteria
- **PASS (confirm locked direction)** for a pair iff V_obs < null median AND
  p_pair ≤ α_bon.
- **DIRECTIONAL** iff V_obs < null median AND raw p_pair ≤ 0.05 but p_pair > α_bon.
- **NULL** iff V_obs ≥ null median (wrong/zero direction) OR p_pair > 0.05.
- Headline verdict is per-pair; an aggregate sentence reports how many of k pairs
  PASS / are DIRECTIONAL / are NULL.
- The famous anchors Q 55 (31×) and Q 77 (10×) are reported individually
  regardless of family verdict.

## 3. Robustness / MW protections
- **MW-1 (instrument-prior):** statistic = gap-variance; null = uniform random
  m-subset; both fixed here, before computation.
- **MW-2 (corpus-prior):** 10000 permutations.
- **MW-3 (alternative model):** secondary statistic = coefficient of variation of
  gaps (CV = std/mean), same null, reported alongside variance. A pair counts as
  robust only if BOTH variance and CV point the same direction. (CV is reported;
  the variance test is primary.)
- **MW-5 (replication):** re-run the Q 55 and Q 77 pairs at a second seed
  (20260530); the direction and PASS/NULL verdict must be stable.
- **MW-6 (instrument-control):** a "phantom-refrain" control — pick a NON-refrain
  surah of comparable length (Q 56 al-Wāqiʿa, 96 verses, no ≥4 refrain) and a
  random m-subset of its verses; the control's gap-variance must NOT pass (it
  should sit at the null median by construction), confirming the test is not
  trivially significant.
- **MW-7 (post-hoc cap):** near-exact census and any non-pre-registered observation
  carries single-test α=0.05 ceiling.

## 4. Counting caveat (verified at runtime, not assumed)
The 31 (Q 55) and 10 (Q 77) counts cited in the task are to be **re-derived from
disk** inside the script and asserted via `assert`; the script fails fast if the
data does not produce them. No count is taken on faith.

## 5. Rules-tuple sensitivity
Primary lens is no-tashkeel. As a sensitivity check the census max-count for the
two anchors is re-derived on `quran-text/quran-min-tashkeel.json`; if the
refrain count differs across the two lenses it is flagged.

## 6. Output files
- This pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2310-refrain-structure.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2310.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2310.json`
- Findings: `findings/phase-b-hypotheses/h-new-2310-refrain-structure.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
