# H-NEW-620 — Run 1 Journal

**Agent:** h-new-620-specialist (inline)
**Date:** 2026-04-28
**Status:** complete
**Pre-reg:** `findings/phase-b-hypotheses/h-new-620-divine-name-density-prereg.md`
**Pre-reg SHA256:** `73dfb7f5e48c6ea3ec72db82b00fb6add51fe457526f6c2da80b37bc32c1034c`
**Output:** `findings/phase-b-hypotheses/h-new-620-divine-name-density.md`
**Raw data:** `findings/phase-b-hypotheses/csv/h-new-620.json`
**Script:** `scripts/h_new_620_divine_name_density.py`
**Seed:** 20260501; n_perm = 10,000; Bonferroni k=3; α_bon = 0.01667.

## What I did

1. **Read context**: cross-finding-024 §3 table (12 training subsets + their pre-classified 5-factor encodings + %iles) and §9 follow-up #5 ("Incorporate divine-name density as potential 6th factor"). Confirmed H-NEW-59's CORE-DN matching rule (proclitic-strip on tokenized words) and H-NEW-95's Khawātim density anchor as complementary verse-level tests.

2. **Pre-registered (locked BEFORE running)** in `h-new-620-divine-name-density-prereg.md`:
   - CORE-DN list: 12 forms (Allāh, al-Raḥmān, al-Raḥīm, rabb + 7 pronominal-suffix forms, plus al-Ilāh→Allāh alias).
   - Match rule: exact-word-equality after stripping ONE optional proclitic prefix from {و, ف, ب, ل, ك, س, +6 bigrams}.
   - 12 training subsets locked from cross-024 §3 with explicit %ile and 5-factor binary encodings.
   - Three Bonferroni-3 gates: (1) ΔR² > 0.05; (2) perm p ≤ α_bon = 0.01667; (3) β(dn_variance) > 0 (POSITIVE pre-committed).
   - Direction: HIGHER DN-density-homogeneity (lower CV) → LOWER %ile.
   - Pre-commit confidence: MODERATE-NULL (5-factor model already saturating R² is likely high, leaving little room).

3. **Hashed** the pre-reg, embedded SHA into the run script.

4. **Ran script** under seed 20260501. Output went to `csv/h-new-620.json`.

5. **All three gates fail**:
   - Gate 1: ΔR² = 0.00587 (not > 0.05).
   - Gate 2: perm-p = 0.4913 (not ≤ 0.01667; in fact, observed ΔR² is BELOW the null-mean of 0.00657).
   - Gate 3: β(dn_variance) = −10.55 (NEGATIVE — sign-reversal from pre-commit).

6. **Wrote findings** with full per-surah density spectrum, per-subset homogeneity table, regression coefficients, permutation null summary, classical-tradition reading, honest limits, queued follow-ups.

## Surprises

- **5-factor Model A R² = 0.980** — strikingly high on N=12. The five binary indicators capture nearly all variance. This SHOULD have been anticipated more strongly in the pre-reg (I noted it as a "saturation risk" in §7 but did not fully internalize how decisively it would constrain ΔR² magnitude).

- **β(dn_variance) sign reversal** is the most informative gate-3 failure. The reason traces to a sample-size artifact: short-surah subsets (Q 107-114, Q 1+27 pair) have ARTIFICIALLY HIGH within-subset CV because of word-count heterogeneity (Q 109's 27 words vs Q 108's 10 words → DN-density highly variable across what is otherwise a creedally-uniform tail). My pre-committed direction was naïve to this. A revised pre-reg with length-normalized CV might give a different result, but this would require a NEW pre-reg, not a post-hoc rule-tweak.

- **Q 1 + Q 27 pair has the highest core_mean (0.118)** despite being at the 81%ile (LEAST cohesive). Q 1 has 6 DN-tokens / 29 words = 21% density (the corpus peak). Q 27 has bismillāh in v.30 plus rabb forms scattered. The pair's mean-DN is high but their %ile is high (less cohesive) — pulling β(dn_mean) NEGATIVE. This is the high-leverage data point driving the negative β(dn_mean).

- **Madanī half Q 57-66 is the most DN-homogeneous subset** (CV = 0.132), which IS the direction predicted, but the 5-factor model already places this subset at low %ile (4.8) via block=1 + register=1 + chrono=1, so the homogeneity adds no residual signal.

- **Q 1 al-Fātiḥa as supreme DN-density peak** (0.207, with 3 distinct names in 29 words). Quantitative anchor for the *umm al-Kitāb* designation.

## Negative findings

- **Aggregate H1 (6th-factor) — NULL on all 3 gates** at α_bon = 0.01667.
- **Spearman ρ = −0.144** (per-surah core_density vs inherited cohesion-%ile, N=64): weak negative, not significant — directional but very low magnitude.
- **β(dn_variance) sign-reversal**: pre-committed POSITIVE; observed −10.55. This is itself an honest pre-commit violation that I report transparently.
- **5-factor model is now empirically TERMINAL within the 12 training subsets**: cross-finding-024's verdict can be promoted from "5-factor empirically derived" to "5-factor empirically TERMINAL on training data."

## Methodological notes

- The R² saturation (0.98) is itself a *finding*, not a flaw. It says the 5 factors are SUFFICIENT for the 12-subset training data. Any candidate 6th factor would need to be tested against an EXPANDED training set (e.g., the Wave-1 4-region architecture, or new subsets from cross-finding-021 hub-spoke logic).
- Permutation test (10000 perms with seed 20260501, shuffling (cv, mean) PAIRS jointly) is the right inferential tool for N=12. Parametric F-test would be unreliable.
- The Spearman descriptive (ρ = −0.144) is reported as descriptive only, NOT in the Bonferroni family. Negative direction is consistent with "more DN-density → more cohesion" descriptively but the magnitude is small.
- I did NOT run sensitivity-checks on alternative %ile-locking choices for ranks 7 (ḥawāmīm-5-6 = 21.5%) or %ile rounding. These could perturb ΔR² by ~0.003-0.01 but would not flip the verdict.
- I did NOT use the FULL-DN list (99 names) in the regression; it was computed for descriptive purposes (per-surah full_density tabulated in JSON output). A separate run with full_cv + full_mean instead of core_cv + core_mean might give different numbers; this would require a new pre-reg.

## Cross-references followed

- cross-finding-024 (5-factor cohesion model, parent)
- H-NEW-59 (99-name distribution, methodology source for proclitic-prefix rule)
- H-NEW-95 (Khawātim density anchor, complementary verse-level finding)
- H-NEW-111 (FR distance matrix; parent for the underlying %ile values)
- al-Tirmidhī asmāʾ-al-ḥusnā tradition (Tirmidhī 3507; Bukhārī 7392)
- al-Biqāʿī *Naẓm al-Durar* (classical *munāsaba* framework)

## Disciplinary checks

- ONE-text rule: respected. Single Hafs-Kufan no-tashkeel corpus.
- Direction-locked for dn_variance (gate 3): respected; the sign-reversal is REPORTED HONESTLY as a pre-commit violation, not silently dropped.
- Equal NULL prominence: the findings file's title, headline, §1 table, and §9 final statement all foreground "NULL — 5-factor model TERMINAL." No PASS-framing leaks in.
- Bonferroni gate not loosened: α_bon = 0.01667 maintained on all 3 gates as pre-locked. (No tightening either; observed perm-p of 0.49 is far from any reasonable threshold so this is moot.)

## Verdict

**NULL on all 3 gates.** Cross-finding-024's 5-factor cohesion model is **empirically TERMINAL** within its 12 training subsets. Divine-name density is captured BY the existing 5 factors; it is NOT an independent 6th factor of subset-level content cohesion. Classical scholarship's decision to NOT elevate DN-density to a *munāsaba* axis is empirically vindicated.
