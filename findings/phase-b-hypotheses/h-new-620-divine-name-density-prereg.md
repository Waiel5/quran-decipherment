---
id: H-NEW-620
title: "Divine-name density as candidate 6th cohesion factor — extension of cross-finding-024 5-factor model"
phase: B
status: PRE-REGISTERED 2026-04-28
date: 2026-04-28
agent: h-new-620-specialist (inline)
parent_1: cross-finding-024 (5-factor cohesion model, §9 follow-up #5)
parent_2: H-NEW-59 (99-name distribution; Madanī Q 57-66 divine-name dense)
parent_3: H-NEW-95 (Khawātim 99-name density anchor)
parent_4: al-Tirmidhī asmāʾ-al-ḥusnā tradition (Bukhārī 7392, Tirmidhī 3507)
seed: 20260501
bonferroni_k: 3
bonferroni_family: h-new-620-divine-name-density
alpha_bon: 0.01667
rules_tuple: "(no-tashkeel; whitespace-tokenized words; CORE-DN list = {الله, الرحمن, الرحيم, رب, ربك, ربكم, ربنا, ربه, ربها, ربهم, ربي, الإله→الله} matched by exact-word equality after stripping a SINGLE optional proclitic ∈ {و, ف, ب, ل, ك, س, فب, وب, فل, ول, وس, فس}; FULL-DN list = the 99 al-Tirmidhī names from data/asma-al-husna.txt under the SAME proclitic-strip rule, with multi-word names matched as whitespace-bounded substring; per-surah density = total-DN-occurrences / total-words; mushaf 114-surah corpus quran-no-tashkeel.json; 12 training subsets locked from cross-finding-024 §3 table)"
direction: |
  PRIMARY (ΔR² test): Adding dn_density_variance + dn_density_mean to the 5-factor regression (block, register, chrono, formula, no_outlier) raises R² by ΔR² > 0.05 in the 12-subset training data, and the permutation null (10000 perms shuffling DN-density labels among 12 subsets, seed 20260501) gives empirical p ≤ 0.01667.
  DIRECTIONAL (dn_variance β-sign): coefficient on dn_density_variance is POSITIVE (higher within-subset DN-density-variance → higher %ile = LESS cohesion). Pre-committed sign.
  EXPLORATORY (dn_density_mean): no pre-committed sign — included only as covariate; sign reported descriptively.
  Aggregate H1 6th-FACTOR PASS: ΔR² > 0.05 AND ΔR² perm-p ≤ 0.01667 AND dn_variance β > 0.
  Aggregate NULL: 5-factor model is TERMINAL; divine-name density is NOT an independent 6th factor of subset-level content cohesion.
verdict: PENDING
---

# [[h-new-620-divine-name-density|H-NEW-620]] — Divine-name density as candidate 6th cohesion factor

## 1. Question

[[cross-finding-024-five-factor-cohesion-model|Cross-finding-024]] (2026-04-21) closed at a 5-factor cohesion model: `content-cohesion ≈ f(block × register × chrono × formula × no_outlier)`. §9 queued: "Incorporate divine-name density as potential 6th factor." [[h-new-95-khawatim-extension|H-NEW-95]] anchored the Khawātim al-Ḥashr (Q 59:22-24) as a 99-name density peak; H-NEW-59 confirmed the Madanī Q 57-66 liturgical block as the corpus DN-density region. If DN-density-homogeneity within a subset is itself a cohesion driver — independent of the 5 existing factors — the model expands to 6.

[[h-new-620-divine-name-density|H-NEW-620]] tests this directly: do per-subset divine-name density statistics (mean and within-subset coefficient-of-variation) PREDICT residual %ile beyond the 5 existing factors?

## 2. Locked divine-name lists

### 2.1 CORE-DN list (primary regex-style match)

Singular-divine and frequent-pronominal-rabb forms:

| Form | Notes |
|:--|:--|
| الله | the supreme name; canonical |
| الرحمن | al-Raḥmān |
| الرحيم | al-Raḥīm |
| رب | rabb (bare) |
| ربك | rabbu-ka |
| ربكم | rabbu-kum |
| ربنا | rabbu-nā |
| ربه | rabbu-hu |
| ربها | rabbu-hā |
| ربهم | rabbu-hum |
| ربي | rabb-ī |
| الإله | mapped → الله (counted as الله occurrence, exclusion of generic "ilāh") |

Match rule: each whitespace-token in the verse is normalized for proclitic-prefixes by trying each prefix in {و, ف, ب, ل, ك, س, فب, وب, فل, ول, وس, فس} and checking if `prefix + DN-form == token`. Exact-equal also matches. No partial-substring within larger tokens (i.e., "ربيع" does NOT match "ربي"). The `الإله` mapping is to `الله` (counted under the same key).

Excluded for transparency: bare "إله" (without article) is NOT counted. "ربي/ربك" + suffix variants beyond those listed (e.g., "ربيهما") are NOT counted. The list is INTENTIONALLY conservative — chosen to maximize precision over recall, and locked here.

### 2.2 FULL-DN list (secondary)

The 99 al-Tirmidhī asmāʾ al-ḥusnā from `data/asma-al-husna.txt` (105 lines minus 6 comment-lines = 99 names). Match rule: same proclitic-prefix-strip rule for single-word names; multi-word names ("مالك الملك", "ذو الجلال والإكرام") matched as whitespace-bounded substring of the full verse text.

This is the EXACT match-rule used in H-NEW-59 (already-published, locked).

### 2.3 Density definition

For surah s with W_s total whitespace-tokens:
- `core_density(s) = core_DN_occurrences(s) / W_s`
- `full_density(s) = full_DN_occurrences(s) / W_s`

CORE-DN is the PRIMARY metric (high-precision, semantically-monolithic). FULL-DN is a secondary descriptive layer.

## 3. Locked 12 training subsets (from [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] §3 table)

| Rank | Subset name | Surahs | %ile (cross-024) |
|:-:|:--|:--|:-:|
| 1 | Q 107-114 terminal-tail | 107,108,109,110,111,112,113,114 | 0.0 |
| 2 | Q 98-114 terminal-17 | 98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114 | 0.0 |
| 3 | Medinan half Q 57-66 | 57,58,59,60,61,62,63,64,65,66 | 4.8 |
| 4 | Mufaṣṣal-awsāṭ Q 67-77 | 67,68,69,70,71,72,73,74,75,76,77 | 7.1 |
| 5 | Musabbiḥāt block-subset | 57,59,61,62,64 | 8.1 |
| 6 | Ṭiwāl Q 2-9 | 2,3,4,5,6,7,8,9 | 17.3 |
| 7 | Ḥawāmīm 5-6 | 40,41,42,43,44,45 | 21.5 |
| 8 | Musabbiḥāt Q 50-56 MINUS Q 55 | 50,51,52,53,54,56 | 37.5 |
| 9 | Mufaṣṣal-ṭiwāl Q 50-66 | 50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66 | 50.1 |
| 10 | Meccan half Q 50-56 | 50,51,52,53,54,55,56 | 70.1 |
| 11 | al-Ḥāmidāt | 1,6,18,34,35 | 75.0 |
| 12 | Q 1 + Q 27 Basmala-pair | 1,27 | 81.0 |

Notes on resolution: rank-7 ḥawāmīm-5-6 is recorded in [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] §3 as a range "19-24%"; I lock 21.5% (the midpoint) as the canonical %ile for this subset to enable scalar regression. This locking is documented BEFORE running. (If a strict reviewer prefers 24% or 19%, sensitivity-check is reported descriptively.)

## 4. Statistical protocol

### 4.1 5-factor encoding (Model A baseline)

From [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] §3, encode per-subset:
- `block` ∈ {0, 1}: 1 if all surahs are mushaf-contiguous; 0 otherwise.
- `register` ∈ {0, 1}: 1 if UNIFORM content-register; 0 if MIXED.
- `chrono` ∈ {0, 1}: 1 if YES homogeneous chronology (all-Meccan or all-Medinan); 0 if MIXED or HIJRA-SPANS.
- `formula` ∈ {0, 1}: 1 if subset shares a fawātiḥ formula (al-ḥamd, sabbaḥa, ḥā-mīm, qul); 0 otherwise.
- `no_outlier` ∈ {0, 1}: 1 if Q 55 is NOT in subset (and no other recognized outlier); 0 if Q 55 is in subset.

These are LOCKED from [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] §3 columns directly. Locked values:

| Rank | block | register | chrono | formula | no_outlier |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 1 | 1 | 1 | 0 | 1 |
| 2 | 1 | 1 | 1 | 0 | 1 |
| 3 | 1 | 1 | 1 | 0 | 1 |
| 4 | 1 | 1 | 1 | 0 | 1 |
| 5 | 1 | 1 | 1 | 1 | 1 |
| 6 | 1 | 0 | 0 | 0 | 1 |
| 7 | 1 | 0 | 1 | 1 | 1 |
| 8 | 1 | 0 | 1 | 0 | 1 |
| 9 | 1 | 0 | 0 | 0 | 0 |
| 10 | 1 | 0 | 1 | 0 | 0 |
| 11 | 0 | 0 | 0 | 1 | 1 |
| 12 | 0 | 0 | 0 | 1 | 1 |

(rank-12 "formula" = 1 because both Q 1 and Q 27 begin with bismillāhi al-raḥmāni al-raḥīm in the canonical reading, per cross-024 H-321 framing).

### 4.2 DN-density features

For each of the 12 subsets:
- `dn_mean = mean(core_density(s) for s in subset)`
- `dn_variance = stddev(core_density(s) for s in subset) / dn_mean` (coefficient of variation; if dn_mean=0 set to 0)

These ARE THE 6th-factor candidates.

### 4.3 Regressions

- **Model A**: OLS `pct ~ 1 + block + register + chrono + formula + no_outlier` (5 predictors + intercept; 6 params on N=12).
- **Model B**: OLS `pct ~ 1 + block + register + chrono + formula + no_outlier + dn_variance + dn_mean` (7 predictors + intercept; 8 params on N=12).

Compute `R²_A`, `R²_B`, `ΔR² = R²_B − R²_A`.

### 4.4 Permutation test on ΔR²

Null: shuffle the (dn_variance, dn_mean) pair-tuples among the 12 subsets (jointly — keep the pairing intact, permute the assignment to subsets). Recompute Model B and ΔR² for each shuffle. 10000 perms, seed 20260501. Empirical p = (#{ΔR²_perm ≥ ΔR²_obs}) / 10000.

### 4.5 Direction test on dn_variance β

If permutation passes Bonferroni gate AND `β_dn_variance > 0`, directional pre-commit is confirmed.

### 4.6 Spearman descriptive

Compute corpus-wide Spearman ρ between (per-surah core_density) and (per-surah inherited cohesion-rank). Each surah inherits the %ile of the FIRST subset in the 12-list that contains it (rank-1 surahs get 0%, etc.); surahs not in any of the 12 subsets are excluded. Reported descriptively only — does NOT enter the Bonferroni family.

## 5. Bonferroni reconciliation

3 inferential gates (PRE-LOCKED):
1. ΔR² > 0.05.
2. ΔR² perm p ≤ 0.01667.
3. dn_variance β > 0.

α_bon = 0.05 / 3 = 0.01667 (per-test).

PASS = all 3 gates.
NULL = ANY of the 3 gates fails.

Spearman ρ is descriptive (k=0). Mean-coefficient sign is exploratory (k=0).

## 6. Pre-commit predictions

| Quantity | Predicted | Confidence |
|:--|:--|:-:|
| ΔR² | 0.03 - 0.20 (modest 6th-factor) | LOW |
| ΔR² perm p | 0.05 - 0.30 (likely NULL given small N) | MODERATE |
| dn_variance β | POSITIVE if anything | HIGH (sign), LOW (magnitude) |
| dn_mean β | UNDETERMINED | EXPLORATORY |
| Aggregate verdict | NULL most likely (5-factor TERMINAL); 6th-factor confirmation would be a positive surprise | MODERATE-NULL |

## 7. Honest limits (pre-locked)

1. **Regex matching imperfect**: substring "ربي" matches "ربي" but a future "rabbi-hi" form is missed. The CORE list locks specific suffixes — alternate suffix-coverage would change density values.
2. **Tashkeel ambiguities**: removed-tashkeel corpus may merge "rabbi" (vocative-genitive) with "rab" (jussive-undefined); my list doesn't disambiguate and that is a known limitation.
3. **Pronominal contractions**: "lillāhi" (ل + الله) is captured; "billāhi", "fillāhi" similarly. But "li-rabbi-ka" → "لربك" is captured by my proclitic rule; OK.
4. **Multi-word divine names** (mālik al-mulk, dhū al-jalāl wa-l-ikrām) for FULL-DN use whitespace-bounded substring; this matches the H-NEW-59 rule but may overcatch.
5. **N = 12 is small**; 8-parameter Model B is borderline-overfitting (df = 4). Permutation test is the appropriate inferential tool, not parametric F-test.
6. **The %ile values are themselves estimates** from [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] with their own permutation-noise (typically ±1-3pp per subset).
7. **Multicollinearity**: the 5 factors are highly correlated; adding 2 more colinear features may not increase R² even if they carry independent signal at higher N.
8. **Single-rule training**: a single rule-tuple is locked. Rule-variants (e.g., adding "ربكما", "ربهما", or restricting to bare "rabb"-only) are NOT in the Bonferroni family — they would require separate pre-reg.

## 8. Deliverables

- This pre-reg, locked at 2026-04-28.
- SHA256 hash embedded in `scripts/h_new_620_divine_name_density.py`.
- Output `findings/phase-b-hypotheses/csv/h-new-620.json` with all per-surah and per-subset measurements + regression outputs + permutation null distribution summary.
- Findings markdown `findings/phase-b-hypotheses/h-new-620-divine-name-density.md`.
- Journal `journal/h-new-620-run-1.md`.

## 9. If NULL

Publish with equal prominence: "5-factor model is TERMINAL; divine-name density is NOT an independent 6th factor of subset-level content cohesion. The Madanī Q 57-66 DN-density peak (H-NEW-59) is captured BY the 5-factor model — it does NOT carry independent variance."

If PASS: [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] upgrades to 6-factor; classical Tirmidhī asmāʾ-al-ḥusnā tradition gains a NEW empirical anchor as a structural factor.

Pre-reg locked 2026-04-28.
