---
id: H-NEW-45
title: Muqaṭṭaʿāt Surah-Index Number-Theoretic Structure — do the 29 muqaṭṭaʿāt-opened surah indices show non-random enrichment on pre-specified number-theoretic properties?
status: PRE-REGISTERED with garden-of-forking-paths post-hoc-observation disclosure
registered: 2026-04-16
spec_locked_at: 2026-04-16 (BEFORE running null model; AFTER observing raw twin-prime pattern — disclosed below)
bonferroni_family: 2026-04-16-H-NEW-45
bonferroni_k: 8
alpha_bon: 0.00625 (= 0.05 / 8)
rules_tuple: (hafs-kufan surah numbering; no orthography/tashkeel dependence since this is a surah-index integer test)
primary_data: the 29 surah indices {2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68}
---

# [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] — Muqaṭṭaʿāt Surah-Index Number-Theoretic Structure

## Garden-of-forking-paths disclosure (CRITICAL)

This pre-registration was authored **AFTER** the hypothesis-generator (main integrator session) computed a quick eyeball of several number-theoretic properties of the 29 muqaṭṭaʿāt-opened surah indices during 2026-04-16 session. The eyeball surfaced one pattern that LOOKED striking: **three twin-prime pairs (11,13), (29,31), (41,43) all have BOTH members in the muqaṭṭaʿāt set**.

This eyeball-first discovery means the twin-prime hypothesis is **post-hoc** and cannot be cleanly pre-registered as a single directed test. The honest protection is to:

(a) **Lock a complete 8-member test family** of number-theoretic properties BEFORE running the null model, with the twin-prime test demoted to being ONE of EIGHT cells in a Bonferroni family of 8.
(b) **Report ALL eight cells** with equal prominence regardless of outcome.
(c) **Require the "hit" to survive Bonferroni-8 correction** (α_per_cell = 0.05/8 = 0.00625) to be elevated above EXPLORATORY.
(d) **Independently pre-register any surviving cell for a second confirmatory test on a separate (e.g., disjoint-surah-subset or non-muqaṭṭaʿāt-classical-feature) data source** before any upgrade beyond EXPLORATORY-POST-HOC.

This is the audit-022 pattern: the observed twin-prime pattern is NOT a claim at this stage; it motivates a disciplined test family, which is now locked.

Additionally: I eyeballed several OTHER properties in the same scan (triangular, Fibonacci, squares, HCN, mod-7/mod-11/mod-19). NONE of those eyeballed signals was striking (z < 2 under naïve Poisson for all of them). Only twin-prime-BOTH was striking. This is a transparent "multiple-comparison-while-looking" situation, handled by the pre-reg locking k=8 below.

## The 8 pre-registered test cells

For each, the data is the 29 muqaṭṭaʿāt-opened surah indices, and the null is 10⁵ uniform random samples of 29 surahs drawn from {1, ..., 114}.

### Cell 1: Prime enrichment

**Target set:** primes in [2, 114] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113} = 30 primes.

**Test statistic:** count of the 29 muqaṭṭaʿāt surahs that are prime.

**Direction:** two-sided (enrichment OR suppression).

### Cell 2: Twin-prime-BOTH enrichment (the eyeball observation)

**Target:** twin-prime pairs (a, a+2) in [1, 114] = {(3,5), (5,7), (11,13), (17,19), (29,31), (41,43), (59,61), (71,73), (101,103), (107,109)} = 10 pairs.

**Test statistic:** count of twin-prime pairs with BOTH members in the 29-muqaṭṭaʿāt set.

**Direction:** one-sided upper (enrichment), per the eyeball observation.

### Cell 3: Fibonacci enrichment

**Target:** Fibonacci numbers ≤ 114 = {1, 2, 3, 5, 8, 13, 21, 34, 55, 89} = 10 values.

**Test statistic:** count of muqaṭṭaʿāt surahs that are Fibonacci.

**Direction:** two-sided.

### Cell 4: Perfect-square enrichment

**Target:** {1, 4, 9, 16, 25, 36, 49, 64, 81, 100} = 10 values.

**Test statistic:** count in muqaṭṭaʿāt set.

**Direction:** two-sided.

### Cell 5: Triangular-number enrichment

**Target:** {1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105} = 14 values.

**Test statistic:** count in muqaṭṭaʿāt set.

**Direction:** two-sided.

### Cell 6: Highly-composite-number enrichment

**Target:** {1, 2, 4, 6, 12, 24, 36, 48, 60, 84, 90, 96, 108} = 13 values (Ramanujan's first 13 HCNs ≤ 114).

**Test statistic:** count in muqaṭṭaʿāt set.

**Direction:** two-sided.

### Cell 7: Mod-19 uniformity test

**Test statistic:** Pearson χ² of mod-19 residue distribution of the 29 surah indices against uniform expectation over the 19 residue classes.

**Direction:** two-sided on χ² (both EXCESS clustering AND anti-clustering are candidate signals).

**Why mod-19:** Khalifa's Code-19 lineage; pre-registered to close the theological relevance of 19 and separate from the code-19 replication (already refuted). Two-sided framing is the audit-015 honest null.

### Cell 8: Gap-entropy / concentration

**Test statistic:** Shannon entropy of the gap sequence between consecutive muqaṭṭaʿāt surah indices (28 gaps for 29 indices). Lower entropy = more concentrated clusters (contiguous muqaṭṭaʿāt blocks); higher entropy = more uniform spacing.

**Direction:** two-sided; absolute deviation from random-29-of-114 expected entropy.

## Null model (locked)

For each permutation trial i ∈ {1, ..., 100000}:
1. Uniform random sample of 29 surahs from {1, ..., 114}. Seed = 20260416.
2. Compute all 8 statistics.
3. Record.

For each cell:
- Observed statistic computed once.
- Empirical p = (count of null_stat as-extreme-as-observed + 1) / (100000 + 1).
- Two-sided cells: test both tails; p_two_sided = 2 × min(p_upper, p_lower).
- One-sided cells (Cell 2): p_upper only.

## MW-5 positive control

**Positive control:** on the same 100,000 permutations, verify that a pre-registered known-signal perturbation is detected. Specifically: construct a "planted signal" dataset: take 29 surahs = {all 20 twin-prime endpoints ≤ 114 that fit plus 9 random fillers}. Run cell 2. Under this planted signal, cell 2 should give p < α_bon/10 = 0.000625 with near-certainty. If not, the null model is broken.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| 0 cells significant at α_bon = 0.00625 | NULL — no non-random number-theoretic structure in muqaṭṭaʿāt surah indices |
| 1 cell significant (including twin-prime) | **EXPLORATORY-POST-HOC** — flagged for independent pre-reg on a distinct data dimension before elevation |
| 2 cells significant at α_bon | **EXPLORATORY** — multiple signals; priority H-NEW-45.1 follow-up |
| 3+ cells significant at α_bon | **PARTIAL-PASS** — cohesive pattern; H-NEW-45.1 required |
| 3+ AND twin-prime AND another prime-related cell | **STRONG-POST-HOC** — exceptionally improbable even after Bonferroni-8; route to classical-scholar for number-theoretic anchor |
| Positive-control planted signal NOT detected | NULL-BROKEN |

## Integrity commitment

- All 8 cells reported with equal prominence regardless of outcome.
- Twin-prime cell (cell 2) transparently flagged as post-hoc-noticed; verdict cannot exceed EXPLORATORY-POST-HOC on this pre-reg alone.
- Seed 20260416 locked.
- Pre-reg is filed BEFORE running the 100K null; output JSON will timestamp its completion AFTER this pre-reg's filing time.
- Raw JSON + script + null-distribution histograms preserved.

## Prior art

- Khalifa 1982 — Code-19 muqaṭṭaʿāt arithmetic (REFUTED in Phase A; cell 7 re-tests at α_bon).
- al-Kirmani (*Mutashabihāt al-Qur'ān*) — qualitative muqaṭṭaʿāt-surah mnemonic structure; no number-theoretic test.
- Nöldeke-school — catalog of muqaṭṭaʿāt surahs by revelation chronology, not surah-index.
- **No published study operationalizes the 29 muqaṭṭaʿāt surah indices as a target set against number-theoretic enrichment with a 10⁵-permutation null.**

## Mechanism candidates (conditional on PASS at any cell)

- Prime/twin-prime enrichment could reflect deliberate compositional assignment of muqaṭṭaʿāt across surah positions along a number-theoretic axis — would be extraordinary evidence for a non-random selection mechanism.
- Mod-19 non-uniform signal would (if confirmed) partially rehabilitate Code-19 lineage, though with an honest tuple.
- Triangular/Fibonacci/square enrichment would suggest pre-Islamic Near-Eastern number-symbolism embedded in the assignment.
- Gap-entropy cluster signal would match the qualitative classical observation of the "ḥawāmīm" cluster + "alif-lām-rā" cluster + "alif-lām-mīm" cluster.

## Honest caveats

1. This is the project's first test on the 29 surah indices as number-theoretic targets. No prior Quran-project finding depends on this.
2. The twin-prime pattern was eyeballed FIRST. Bonferroni-8 is the honest protection but is NOT equivalent to an independent pre-reg.
3. Any PASS must be followed by H-NEW-45.1 (separate pre-reg on a disjoint classical-feature data dimension) before upgrade to CONFIRMED.
4. NULL outcome is publishable.
