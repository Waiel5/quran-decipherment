---
surah: 48
test_id: Q048-F-01
H_NEW: H-NEW-1260
title: "Q 48 al-Fatḥ — corpus-EXACT *fatḥ* root-density signature (length-controlled hypergeometric test)"
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 1
bonferroni_family: Q048-F-01-fath-density
alpha_raw: 0.05
alpha_bon: 0.05
direction_locked: true
rules_tuple: "(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
prereg_sha_expected: TBD-AT-WRITE-TIME
parent_findings:
  - h-new-660 (compression-tail gradient — root-density structure)
  - h-new-840 (UAS architectural significance)
  - h-new-86 (Q 12 Yūsuf name-root concentration; analogous test for Q 12)
classical_anchors:
  - al-Suyūṭī, *al-Itqān*, nawʿ 1 (chronology — Medinan late) and nawʿ 17 (asbāb al-nuzūl)
  - al-Bukhārī, *Maghāzī* #214 (Anas: Q 48:1 *fatḥ* = Hudaybiyya)
  - al-Bukhārī, *Maghāzī* #194 (al-Barāʾ: Riḍwān-Pledge as the *fatḥ*)
---

# Q048-F-01 Pre-registration — *fatḥ* root density in Q 48


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

**H1 (one-tailed, locked direction)**: The QAC v0.4 root *ftH* (f-t-ḥ, "to open / grant victory") has a **statistically significant over-representation** in Q 48 al-Fatḥ relative to the corpus baseline rate, controlling for Q 48's total root-tagged-token count.

**H0**: Q 48's *ftH* count is consistent with random length-proportional sampling at the corpus rate.

**Direction**: Q 48 = corpus-MAX or near-MAX in *ftH* density (LOCKED).

## 2. Operational definition

- **Source corpus**: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4 root annotations).
- **Root code**: `ROOT:ftH` (Buckwalter; corresponds to Arabic فتح).
- **Q 48 set**: all tokens with location prefix `(48:`.
- **Token universe**: all root-tagged tokens (those with `ROOT:` in features) — NOT all words; particles and demonstratives without root-tag are excluded uniformly.
- **Baseline**: corpus-wide *ftH* tokens / corpus-wide root-tagged tokens.

## 3. Test statistic

Hypergeometric exact test:
- Population N = total corpus root-tagged tokens.
- Successes K = total *ftH* tokens in corpus.
- Sample n = root-tagged tokens in Q 48.
- Observed k = *ftH* tokens in Q 48.
- p_one-tailed = P(X ≥ k | hypergeometric(N, K, n)).

Secondary descriptive: per-surah *ftH*-density rank (Q 48 vs all 114 surahs), restricted to surahs with ≥ 100 root-tagged tokens (length-control).

## 4. Permutation null (sensitivity)

Under H0: distribute the K *ftH* tokens uniformly at random across the N root-tagged-token positions; count how many fall in Q 48's n positions; compute p_perm = (count of perms with k_perm ≥ k_observed) / (n_perm + 1). n_perm = 10,000, seed = 20260509.

The hypergeometric and the permutation null should agree (the hypergeometric is the exact analytical version of the permutation null for finite populations).

## 5. Success / Failure criteria

- **CONFIRMED**: hypergeometric p ≤ 0.05 AND Q 48 ranks in top-3 of length-controlled (≥ 100 root-tokens) per-surah *ftH*-density.
- **DIRECTIONAL**: p ≤ 0.05 OR Q 48 ranks in top-3 (one of the two).
- **NULL**: p > 0.05 AND rank > 3.
- **PRE-COMMIT VIOLATION**: Q 48 has ≤ 2 *ftH* tokens (the brief's "5 occurrences" was incorrect; the on-disk count is 4 — pre-flight verification confirmed before lock).

## 6. Honest limits known a priori

- The brief stated "5 occurrences of *fatḥ* root" but on-disk QAC v0.4 verification before pre-reg lock returned **4 root-tokens / 3 verses**. This pre-reg uses the verified count of 4. The discrepancy is documented in `00-overview.md` §4 and `05-classical-claims-audit.md` §8.
- The *ftH* root has 38 corpus-wide tokens — a moderate-rare root. This makes the test sensitive to small absolute differences.
- Q 48's name comes from this root, so the test is in some sense "tautological" — the surah is named *al-Fatḥ* precisely because of the dense *fatḥ* vocabulary. The empirical contribution is **quantifying the magnitude** of the name-density linkage relative to corpus baseline.
- The test is post-hoc-noticed (the brief flagged this as a "novel-test idea"); per HANDOFF/04-DISCIPLINE.md post-hoc protocol, **single-test α=0.05 cap** applies and **verdict ceiling = PASS-DIRECTED** (not CONFIRMED) until INDEPENDENT REPLICATION on a distinct data dimension.
- INDEPENDENT REPLICATION candidate: surface-form *فتح*-substring count (orthographic) — a different operationalization than QAC root.

## 7. Garden-of-forking-paths log (BEFORE running)

- Decision: use QAC v0.4 root-tag (`ROOT:ftH`) as the primary operationalization. RATIONALE: QAC root is the project's standard root-resolution mechanism; orthographic substring counts surface forms but misses root-related allomorphs (e.g., *futiḥa, mafātiḥ, fattāḥ*).
- Decision: length-control by total root-tagged tokens (not total verses or words). RATIONALE: a verse can have many or few root-tagged tokens; the relevant baseline is the rate at which a root appears among root-tagged tokens.
- Decision: filter ≥ 100 root-tagged tokens for the rank-comparison, to avoid trivial-density inflation in tiny surahs (Q 110 al-Naṣr, with 1 token in 31, has artificially-high density). RATIONALE: standard length-control practice in the project; precedent in H-NEW-86.
- Decision: report both hypergeometric (analytical) and permutation null (n_perm = 10000). RATIONALE: cross-validation; the two should agree; if they disagree, instrument-failure.
- ALTERNATIVE-HYPOTHESIS-DECLARED: if Q 48 *ftH* count is at corpus-rate, then the surah's name-root linkage is decorative-classical only, NOT a quantitative-empirical signature.
- BEFORE running: pre-flight verification (Bash + Python on QAC corpus) confirmed Q 48 has 4 *ftH* root-tokens; the corpus has 38; Q 48 has 916 total root-tagged tokens; expected under uniform = 0.27 → enrichment ~14.7×.

## 8. Rules-tuple

`(no-tashkeel, QAC-v0.4-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 9. Bonferroni accounting

k = 1 (single test). α_bon = 0.05.

This pre-reg is part of a 4-test family for Q 48 (Q048-F-01, F-02, F-03, F-04). Each test is in a SEPARATE family; family-level Bonferroni is applied within the test's own family (k=1 here), not across the surah specialist's tests, since the 4 tests target distinct hypotheses.

## 10. Coordination

- Q 47 specialist did NOT run an *ftH*-density test. No duplication.
- The Q 12 Yūsuf specialist (H-NEW-86) ran an analogous test for Yūsuf-name-root concentration and found 532× enrichment, p = 3 × 10⁻³⁹. This Q 48 test is the parallel for the Hudaybiyya/al-Fatḥ surah and the *fatḥ* root.
- The Q 110 al-Naṣr specialist (if dispatched) would run a parallel test for *naṣr*-root density.

## 11. Output

- Pre-reg: this file.
- Script: `scripts/Q048_F_01_fath_density.py` with embedded SHA verification.
- JSON: `csv/Q048-F-01.json`.
- Findings: `06-novel-findings.md` §Q048-F-01.

## 12. SHA256 lock

Computed at write-time, embedded into `scripts/Q048_F_01_fath_density.py`, verified at runtime.
