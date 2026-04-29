---
id: H-NEW-930
title: "Modular-arithmetic patterns in verse-count distribution — Pearson χ² goodness-of-fit on V mod m for m∈{7,11,13,19}"
phase: B+
status: PRE-REGISTERED 2026-05-07
date: 2026-05-07
agent: modular-arithmetic-specialist
parent_finding_1: H-NEW-34 (verse-final abjad-mod-m clustering NULL-CONFIRMED for m∈{7,11,19}; reverse-direction underdispersion exploratory)
parent_finding_2: HONEST-LIMITS §1.3 (Khalifa ALM-29 mod-19 1/29 REFUTED)
parent_finding_3: HONEST-LIMITS §1.9 (prime-mod scan p∈{7,11,13,17,19,23,29,31} on letter-counts NULL)
parent_finding_4: HONEST-LIMITS §1.10 (letter-div-19 rate across 15 corpora NULL)
seed: 20260507
n_perms: 10000   # used only for the H4(a) within-multiset permutation diagnostic
bonferroni_k: 4
bonferroni_family: "H1-modular-uniformity-{7,11,13,19}"
alpha: 0.05
alpha_bon: 0.0125
rules_tuple: |
  (no-tashkeel, orthographic-token, graphemes,
   basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
  Source of verse-counts: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  Hafs-Kūfan numbering ONLY (114 surahs; total verses 6236; Q1=7, Q2=286, Q108=3).
  Pre-Hafs alternative numberings for Q 6, Q 26, Q 27 EXCLUDED.
direction: |
  H1 (PRIMARY, direction-locked): For each m ∈ {7,11,13,19}, Pearson χ² goodness-of-fit
       against uniform expected (114/m per residue class) is two-sided non-uniform.
       Test = χ² df = m-1, two-tailed by construction (χ² is one-tailed in the upper tail
       but the alternative is "non-uniform" without a sign on which residue is enriched).
       At α_bon = 0.05/4 = 0.0125 → CONFIRMED for that m if p < 0.0125.

  H2 (RESIDUE-0 SECONDARY, two-sided): For each m for which H1 rejects (and ONLY for those),
       a SECONDARY two-sided binomial test of count(V≡0 mod m) against null = 1/m,
       at uncorrected α=0.05.  H2 is descriptive; it is NOT in the Bonferroni-4 family.

  H3 (NULL FALSIFIER): If 0 of 4 H1-tests reject at α_bon, the family verdict is NULL —
       "Quran's verse-counts are modularly random under {7,11,13,19}" — published with
       equal prominence to a positive finding.

  H4 (POST-HOC SAFETY, conditional on any H1 reject):
       (a) Mushaf-permutation null: 10000 random permutations of the 114 verse-counts
           (preserves the multiset {V_1,...,V_114}). Since H1 is computed on the multiset
           (not on surah-position), this null is mathematically a no-op for the modular
           χ² statistic — the χ² value is identical under any permutation. Documented as
           a sanity check; will be reported as MULTISET-INVARIANT (the statistic depends
           only on the multiset).
       (b) Pre-Islamic poetry baseline: poem-line-counts from
           data/baseline-corpora/raw/diwan-*.txt — DATA-GAP if the line-per-poem
           tabulation is not pre-tabulated. This pre-reg DOES NOT REQUIRE new
           tabulation work; if no clean per-poem-line-count list is on disk in
           tabular form, H4(b) is reported as DATA-GAP and the H-NEW-930 verdict
           does not depend on it.
verdict: PENDING
---

# H-NEW-930 — Modular-arithmetic patterns in verse-count distribution

## 1. Question

The Quran has 114 surahs whose verse-counts (Hafs-Kūfan) range from 3 (Q 108) to 286 (Q 2), totalling 6236. The classical and modern numerological traditions — most prominently Rashad Khalifa's *Code 19* lineage (1974+; Khalifa 1989 *Quran the Final Testament* appendix 1; Edip Yüksel 2007 *Quran: A Reformist Translation*) and broader ʿilm al-ḥarf (al-Suyūṭī *al-Itqān* nawʿ 56 *fī ʿilm al-ḥurūf*; al-Buni *Shams al-maʿārif* — though al-Buni is on the project's flagged-fringe list) — assert non-trivial modular structure in Quranic counts at moduli 7, 11, 13, and especially 19.

Most such claims are post-hoc cherry-picked. The project has previously falsified several at the **letter-count** and **verse-final-abjad-residue** levels:
- [[h-new-34-abjad-residue-fasila-mechanism|H-NEW-34]]: verse-final abjad mod m for m∈{7,11,19} → NULL-CONFIRMED (6/6 sub-tests).
- HONEST-LIMITS §1.3: Khalifa's 29-muqaṭṭaʿāt-surahs ALM-sum mod 19 → 1/29 (vs binomial-expected 1.53; P(X≥1)=0.79) → REFUTED.
- HONEST-LIMITS §1.9: prime-mod scan over letter counts at m∈{7,11,13,17,19,23,29,31} → min raw p=0.056 vs Bonferroni 0.00156 → NULL.
- HONEST-LIMITS §1.10: letter-div-19 rate across 15 corpora → Quran 5.6% vs expected 5.3% (range 0–11.1%) → NULL.

**MISSING from the project ledger**: a direction-locked, Bonferroni-corrected χ² goodness-of-fit on the **verse-COUNT** of each surah (V_s) modulo small primes. H-NEW-930 closes that gap.

This is distinct from H-NEW-34 (which tested **verse-final abjad** residues, not surah verse-COUNTS) and from HONEST-LIMITS §1.9 (which tested **letter-counts**, not verse-counts).

## 2. Data (LOCKED)

### 2.1 Source and rules-tuple

- File: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Field: `total_verses` for each of the 114 surah objects (verified above to match `len(verses)` exactly for all 114).
- Hafs-Kūfan numbering. Pre-Hafs / non-Hafs alternative verse-counts for Q 6, Q 26, Q 27 (which exist in Baṣran, Madanī-I, Madanī-II, Shāmī, Makkī numerations; documented in al-Dānī *al-Bayān fī ʿadd āy al-Qurʾān* and al-Suyūṭī *al-Itqān* nawʿ 19) are EXCLUDED.
- Total: 6236 verses; min = 3 (Q 108 al-Kawthar), max = 286 (Q 2 al-Baqara).

### 2.2 SHA256 verification

The pre-reg SHA256 will be computed at runtime from this file and embedded in the run script as EXPECTED_SHA. The run script will fail-fast if SHA mismatch.

## 3. Protocol

### 3.1 PRIMARY tests (Bonferroni-4 family)

For each m ∈ {7, 11, 13, 19}:

1. Compute residues r_s = V_s mod m for s = 1..114.
2. Tabulate observed counts O_k = #{s : r_s = k} for k = 0..(m-1).
3. Expected E_k = 114 / m for all k.
4. Compute χ² = Σ_k (O_k − E_k)² / E_k, df = m − 1.
5. p-value from upper-tail χ²(m−1). (Standard goodness-of-fit; 114/m is the asymptotic expected — see §6 for small-cell concern under m=19.)

### 3.2 Acceptance gates (Bonferroni-4)

| p-value (per modulus) | Per-modulus verdict |
|:--|:--|
| p < 0.0125 (= 0.05/4) | REJECT-UNIFORM (CONFIRMED non-uniform) |
| 0.0125 ≤ p < 0.05 | DIRECTIONAL (uncorrected only; not promoted) |
| p ≥ 0.05 | NULL (uniform-consistent) |

### 3.3 Family verdict

| #-rejects-at-α_bon (out of 4) | Family verdict |
|:--|:--|
| 0 | NULL: "verse-counts are modularly random under {7,11,13,19}" — equal prominence |
| 1 | PASS-DIRECTED: single-modulus finding capped at α=0.05 single-test (NOT Bonferroni'd-up); HONEST-LIMITS section mandatory |
| 2 | DOUBLE-PASS: report jointly with χ² statistic per modulus and combined Stouffer Z; HONEST-LIMITS mandatory |
| 3–4 | STRONG NON-UNIFORMITY: report all per-modulus stats + combined; HONEST-LIMITS mandatory; DOES NOT extrapolate to Khalifa-19-coding theological claims |

### 3.4 SECONDARY (descriptive, NOT in Bonferroni-4 family)

H2 — for each m where H1 rejects: two-sided binomial(114, 1/m) test of O_0 (count of surahs whose V is divisible by m) against null = 114/m. Reported at uncorrected α=0.05.

This is NOT direction-pre-committed (residue-class 0 might be over- OR under-represented). H2 is purely descriptive, gated MW-7-cap.

## 4. Bonferroni accounting

- k = 4 (one χ² test per modulus).
- α_bon = 0.05 / 4 = 0.0125.
- The H2 SECONDARY binomial tests are NOT counted (they fire only contingent on H1 reject and are descriptive, not decisional).
- The H4 SAFETY checks are NOT counted (they are sanity checks, not primary hypotheses).

This Bonferroni-4 spec is locked BEFORE observation per PRE-REG-STANDARD-04.

## 5. Hypotheses by source

| Source | Predicted direction | Magnitude |
|:--|:--|:--|
| Khalifa 1989 *Quran the Final Testament* appendix 1 (Code-19) | non-uniform mod 19 (over-rep of residue 0) | strong |
| Edip Yüksel 2007 (lineage) | non-uniform mod 19 | strong |
| ʿIlm al-ḥarf classical (al-Suyūṭī *Itqān* nawʿ 56) | non-uniform at small primes (no specific m) | qualitative |
| H-NEW-34 prior (verse-final abjad mod 7,11,19 NULL) | NULL by analogy | strong |
| HONEST-LIMITS §1.9 prior (letter-count prime-mod scan NULL) | NULL by analogy | strong |
| HONEST-LIMITS §1.10 (letter-div-19 NULL across 15 corpora) | NULL by analogy | strong |

The project's empirical priors (H-NEW-34 + HONEST-LIMITS §1.9, §1.10, §3) are heavily NULL on numerological-modular claims. The Khalifa-Yüksel literature predicts strong non-uniformity at m=19. H-NEW-930 adjudicates between these for the verse-COUNT operationalization specifically (which is not yet tested).

## 6. Honest limits

1. **Verse-counts are NOT independent**: they are the empirical content of a single text. Treating them as independent draws from a discrete distribution (which the χ² goodness-of-fit assumes) is a modelling choice. The χ² test asks: "is the empirical distribution of V mod m, treated as 114 i.i.d. draws, consistent with uniform on Z/mZ?" This is the standard Rashad-Khalifa-style operationalization; we adopt it for pre-commitment and call it out here as a known modelling-prior limitation.

2. **Small expected cell counts under m=19**: E_k = 114/19 = 6.0 exactly. The χ²(18) approximation is reasonable at E≥5; here E=6 is just-above. We will additionally report Fisher-exact-via-multinomial-permutation p (10000 perms, seed 20260507) for m=19 as a sensitivity check. m=13 → E=8.77; m=11 → E=10.36; m=7 → E=16.29 — all comfortable.

3. **One-text limitation**: any modular-pattern result, even if H1 rejects, is consistent with arbitrary post-hoc moduli having been tested for that specific text by prior numerologists. The Bonferroni-4 specifically corrects for the project's pre-committed 4 moduli; it does NOT correct for the universe of moduli that prior generations of numerologists tested. We address this by selecting moduli {7,11,13,19} on the *prior literature's specification* (Khalifa-19, classical 7-11-13-19) rather than on inspection of the data.

4. **No extrapolation to Khalifa-19-coding**: even if m=19 H1 rejects, this would be evidence for "verse-count distribution is non-uniform mod 19" — NOT for Khalifa's broader claim of a divine signature. H-NEW-930's CONFIRMED-region prose will explicitly disavow that extrapolation.

5. **Multiset-invariance of H1**: χ²(V mod m) depends only on the multiset {V_1,...,V_114}, not on which V is assigned to which surah. So H4(a) (mushaf-permutation null) is mathematically a no-op for this statistic; we report it as MULTISET-INVARIANT and document why.

6. **Independent replication**: per Protocol §1.5, a CONFIRMED-region result requires INDEPENDENT REPLICATION on a distinct data dimension (e.g., Meccan-only and Medinan-only sub-corpora). H-NEW-930 will, conditional on rejection, queue that as H-NEW-930.1 (NOT executed in this pre-reg).

7. **DATA-GAP for pre-Islamic-poetry control (H4b)**: a clean per-poem line-count tabulation across the dīwān corpus is not yet on disk in tabular form. Reported as DATA-GAP; not a precondition for the H-NEW-930 verdict.

## 7. Deliverables

- This pre-reg locked 2026-05-07; SHA256 embedded in run script.
- Run script: `/Users/grey/Downloads/quran/scripts/h_new_930_modular_verse_counts.py`
- Output JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-930.json`
- Findings markdown: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-930-modular-verse-counts.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-930-run-1.md`
- Update MASTER-FINDINGS-LEDGER.md after H-NEW-920 (H-NEW-920 slot reserved; H-NEW-930 entry inserted in numerical order).

## 8. Garden-of-forking-paths log (BEFORE run)

- Moduli {7, 11, 13, 19} were chosen BEFORE inspection of any V mod m statistic on the locked file. Choice rationale: 19 is the Khalifa-claimed modulus; 7, 11, 13 are the small primes commonly cited in classical ʿilm al-ḥarf and modern numerology. NO substitution of moduli is permitted post-observation. 17 is excluded (was tested in HONEST-LIMITS §1.9 letter-prime-scan); 23, 29, 31 excluded as out-of-tradition.
- The χ² goodness-of-fit is the standard, non-discretionary test for this hypothesis; no alternative was considered.
- The Bonferroni-4 correction is non-discretionary given k=4.
- The H2 binomial residue-0 test is direction-FREE (two-sided); we do NOT pre-commit a sign on residue-0 over- vs under-representation.
- No verse-count value has been viewed mod m at the time of pre-reg locking. The full multiset has been viewed (114 entries, range 3–286, sum 6236) for sanity-check only.

## 9. Direction LOCKED. ONE text. Equal NULL prominence.

Pre-reg locked 2026-05-07. SHA256 to be computed and embedded in run script before execution.
