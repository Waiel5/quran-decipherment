---
date: 2026-04-13
status: pre-registered BEFORE execution
spec_locked_at: 2026-04-13
rules_tuple_default: (no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
---

# The Tomorrow Tests — Pre-Registered Novel Audits

Five tests that have never (to my knowledge) been applied to the Quran or any other sacred text. Each is locked in **before execution**, with null model + acceptance criterion committed up front. Bonferroni k = 5 across this suite; family-wise α = 0.05 → per-test α = 0.01.

The purpose: the Quran has previously been subjected to every test that 20th-century computational linguistics and classical scholarship could devise. These are tests from fields (TDA, counterfactual robustness, reverse-engineering, LLM judgeship, constraint satisfaction) that didn't exist in usable form until the past 5-10 years. A text composed in the 7th century would have no way to anticipate them.

Honest protocol: if a test fails, it's reported with equal prominence. Null results are publishable.

---

## Test 1 — LLM-as-judge inauthenticity detection at short-span granularity

**Question:** Can state-of-the-art LLMs distinguish genuine Quranic text from plausible LLM-generated classical Arabic forgeries at 10-word granularity?

**Procedure:** Sample 500 random 10-word Quranic subsequences. For each, generate 10 "plausible fake" 10-word classical Arabic sequences via a second-line LLM prompted to mimic classical Arabic with no Quranic-specific training signal. Have a third LLM blind-judge which is genuine.

**Null:** If the Quran has no distinguishable signature at the 10-word scale, judge accuracy ≈ 9.1% (1-in-11 random).

**Acceptance (pass):** Accuracy significantly above 9.1% at Bonferroni-corrected α=0.01.

**Acceptance (strong pass):** Accuracy > 50% (judge picks the true Quran over majority of forgery attempts).

---

## Test 2 — Counterfactual fragility vs matched Arabic

**Question:** For every word in the Quran, how structurally fragile is the surrounding surah to that word being replaced with a plausible synonym? Compare to matched classical Arabic.

**Procedure:** For each of ~77,797 real-word tokens, compute the structural fingerprint (rhyme, hapax-at-end pattern, divine-name density, n-gram gzip ratio, palindrome score, ring-symmetry score) of the surah before and after single-word substitution. Define fragility = mean fingerprint Δ across the 6 axes. Compute same for matched-Arabic baseline texts.

**Null:** Fragility distribution matches baseline.

**Pre-registered prediction:** If the Quran is dense-multi-constraint-optimized, its fragility will be HIGHER than baseline (single-word changes break more simultaneous structures). If it's loose prose, fragility ≈ baseline.

**Acceptance:** Fragility mean is z > +2.58 vs matched-baseline at α=0.01.

---

## Test 3 — Canonical-order reverse-engineering

**Question:** Can the canonical 114-surah order be recovered from the text alone, with no chronology or historical information?

**Procedure:** Given only the 114 surah texts (scrambled), define a pairwise "structural adjacency" score from gzip compression, shared vocabulary, phonetic continuity, and topical embedding. Build a graph; solve for the Hamiltonian path that minimizes cumulative adjacency distance. Compare recovered order to the actual canonical mushaf order using Kendall-tau and Spearman correlation.

**Null:** A random Hamiltonian path has expected τ = 0.

**Pre-registered prediction:** If canonical order is structurally encoded, τ > 0 at significance; the stronger the τ, the more the mushaf order reflects structural coherence beyond chronology.

**Acceptance:** τ > 0 at p < 0.01 under random-permutation null (10,000 samples).

---

## Test 4 — Simultaneous N-constraint density

**Question:** For each verse, how many independent structural constraints does it satisfy simultaneously, and is the Quran's distribution above matched-Arabic baseline?

**Procedure:** Define 12 independent structural/linguistic constraints per verse:
1. Rhymes with preceding verse in same surah
2. Last word is hapax or dispreferred word-class
3. Contains a divine name
4. Has a chiastic root-palindrome ≥3
5. Has classical jinās score ≥ threshold
6. Abjad sum is digit-root-3-or-9 (classical saba7ic property)
7. Has assonance density above median
8. Length is within Fibonacci-adjacent range
9. Opens with one of the 12 canonical Quranic incipits
10. Contains an iltifāt shift
11. Contains at least one rare-root
12. Has information-theoretic surprisal > baseline

Count per verse; compute distribution. Compare to matched-Arabic.

**Null:** Quranic constraint-count distribution ≈ baseline Poisson.

**Pre-registered prediction:** Quran's verses satisfy MORE simultaneous constraints than matched Arabic, AND the tail (verses satisfying 8+ constraints) is over-represented at Bonferroni-significant rate.

**Acceptance:** Kolmogorov-Smirnov vs baseline p < 0.01, AND tail ≥8 at z > +2.58.

---

## Test 5 — Topological Data Analysis of verse-embedding manifold

**Question:** Does the Quran's semantic embedding manifold have topological features (Betti numbers, persistent homology) that distinguish it from matched-Arabic baselines?

**Procedure:** Embed all 6,236 verses using an Arabic-fluent sentence encoder. Compute persistent homology via Vietoris-Rips filtration. Report Betti-0, Betti-1, Betti-2 persistence diagrams. Compute same for matched-length classical Arabic corpora (Bukhari, Jahiliyya poetry, Muʿallaqāt, Jāḥiẓ).

**Null:** Quranic persistence barcodes are statistically indistinguishable from matched-Arabic.

**Pre-registered prediction:** Quran has more persistent 1-dimensional topological features (loops in semantic space) than baseline — indicating self-referential / recurrent semantic structure.

**Acceptance:** Bottleneck distance between Quranic barcode and baseline barcodes exceeds the 99th percentile of within-baseline bottleneck distances.

---

## Reporting commitments

- All five test results published regardless of outcome
- Bonferroni-corrected verdicts: Test-level α=0.01, family-wise α=0.05
- Any mid-run methodology change disclosed in "garden of forking paths" section
- Scripts + random seeds + raw output JSON preserved
- If a test produces an unexpected signal: investigate but do NOT claim as the pre-registered finding unless it survives sensitivity analysis

---

## Completion tracking

| Test | Status | Output |
|---|---|---|
| T1 LLM-judge inauthenticity | DISPATCHED | findings/phase-b-hypotheses/llm-judge-inauthenticity.md |
| T2 Counterfactual fragility | DISPATCHED | findings/phase-b-hypotheses/counterfactual-fragility.md |
| T3 Canonical-order reverse-engineering | DISPATCHED | findings/phase-b-hypotheses/canonical-order-recovery.md |
| T4 Simultaneous N-constraint density | DISPATCHED | findings/phase-b-hypotheses/simultaneous-constraint-density.md |
| T5 TDA verse-embedding manifold | DISPATCHED | findings/phase-b-hypotheses/tda-manifold.md |

---

## H-NEW-34.1 — Muʿallaqāt rhymed-baseline pre-registration for the H-NEW-34 reverse-signal upgrade

**Registered:** 2026-04-14 (skeptical-auditor gate ruling, post-audit-025; supersedes 2026-04-13 integrator amendment on Bonferroni k)
**Status:** HELD — no execution until skeptical-auditor confirms pre-reg text clean.
**Parent:** H-NEW-34 primary verdict stands at PASSED-AS-NULL (unchanged). This pre-reg gates only the reverse-signal upgrade from exploratory to confirmed.
**Seed:** 20260413 (universal).
**Pre-reg file canonical:** `findings/phase-b-hypotheses/h-new-34-1-prereg.md` (content pre-reg); this entry is the TOMORROW-TESTS gate row.

### Question

The H-NEW-34 parent produced a post-hoc reverse signal: Quran verse-final abjad residues are MORE UNIFORM than Bukhari and Jāḥiẓ baselines (z = −4.28 to −11.36 across 6 tests). This reverse-signal is currently filed as "hypothesis-generating exploratory." The upgrade to "confirmed reverse finding" requires an independent pre-registration with Muʿallaqāt rhymed-baseline as the decisive rhyme-mechanism control — otherwise the same pattern would match "rhyme-register artefact." This is H-NEW-34.1.

### Three pre-reg conditions (team-lead / skeptical-auditor specification)

**(i) Direction pre-registration.** The Quran-under-dispersion direction (z_Quran ≤ 0 relative to null mean χ²) is the pre-registered hypothesized direction. The current observation from H-NEW-34 is post-hoc; H-NEW-34.1 must be independently pre-registered even though direction is the same. Sign-flip post-hoc is prohibited.

**(ii) Length-mediation / fāṣila-mechanism diagnostic.** Pre-register a decomposition that distinguishes "fāṣila high-frequency lexeme repetition drives the variance" from "some other Quran-specific structure drives the variance." Operationalization: per-rhyme-class variance decomposition — compute within-rhyme-class χ² vs between-rhyme-class χ² at each modulus m ∈ {7, 11, 19}.
   - **If within-class variance < 20 % of total:** rhyme-repetition dominates → MECHANISM-CONFIRMED, route to M-6 fāṣila-substrate candidate.
   - **If within-class variance > 80 % of total:** effect survives conditioning on rhyme → Quran-specific residual → NOVEL-FINDING, file as H-NEW-34.1-REVERSE.
   - **If 20 %–80 %:** PARTIAL.
   Note: supplements (not replaces) the length-deciled stratification from the 2026-04-14 integrator amendment to h-new-34-1-prereg.md.

**(iii) Three-corpus joint threshold.** The under-dispersion must hold across **Bukhari AND Jāḥiẓ AND Muʿallaqāt** at a jointly-binding threshold. Not majority-of-three — all-three. Bonferroni k = 9 (3 baselines × 3 moduli), **α_bon = 0.05 / 9 = 0.0056**. (This supersedes the 2026-04-14 amendment's α = 0.0033 across baselines; the auditor's k=9 jointly binds across the full (baseline × modulus) grid.) Any single (baseline, m) cell failing the one-sided under-dispersion threshold at α_bon = 0.0056 forces NULL verdict for H-NEW-34.1.

### Baselines and N

- Bukhari-noquran (prose)
- Jāḥiẓ *Kitāb al-Ḥayawān* (prose)
- Muʿallaqāt 7-ode pool (rhymed poetry) — verse-final-word extraction per bayt

N_comparison = min(Quran N=6219, Muʿallaqāt pool size). If Muʿallaqāt < 6219, use full Muʿallaqāt and report power-adjusted z. No upscale by repeat-sampling, no downscale of Quran.

### Pre-committed verdict table

| Joint outcome (one-sided z_Quran < null 5th-pct equivalent, α_bon = 0.0056 per cell, k = 9) | Verdict |
|---|---|
| All 9 cells under-disperse | **PASS — reverse signal confirmed; upgrade H-NEW-34 reverse-signal from exploratory to confirmed** |
| 1+ cells fail (any baseline × m) | **NULL** — no H-NEW-34.1 upgrade; primary H-NEW-34 NULL stands; reverse signal remains exploratory footnote |
| Any baseline OVER-disperses at α_bon | **MECHANISM-INCONSISTENT** — escalate; possibly reopen parent H-NEW-34 |

**Mechanism routing** (conditional on PASS above):
- Within-rhyme-class variance < 20 % of total → MECHANISM-CONFIRMED (fāṣila-substrate; M-6 candidate)
- Within-rhyme-class variance > 80 % of total → NOVEL-FINDING (file as H-NEW-34.1-REVERSE; route to H-NEW-SURVEY-EXT task #84)
- 20–80 % → PARTIAL; report both

### Scripts and outputs

- Script edit: `scripts/h_new_34_abjad_modular.py` — add Muʿallaqāt baseline loader + three-corpus joint-threshold verdict logic + per-rhyme-class variance decomposition.
- Shared loader (efficiency, not blocking): if `data/baseline-corpora/muallaqat_pool.py` is built first, also serves H-NEW-22-BASELINE (#63) and T-004 (#72 already complete).
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-34.json` — add sections `muallaqat_nulls_per_m`, `within_rhyme_class_variance`, `three_corpus_joint_verdict`.
- Findings file: `findings/phase-b-hypotheses/h-new-34-1-under-dispersion.md` — separate from parent `abjad-residue-null.md`.

### Gate protocol (standing from audit-023)

1. TOMORROW-TESTS entry filed (this entry) — **done**.
2. Skeptical-auditor confirms pre-reg text clean — **pending**.
3. Execute the Muʿallaqāt baseline extension.
4. Re-file as `h-new-34-1-under-dispersion.md` separate from the parent `abjad-residue-null.md`.
5. Skeptical-auditor audits both pre-reg clarity and execution result.

**No "per pre-registered fallback clause" language** in the result write-up without an actual clause in this pre-reg file.

### Reporting commitment

Both directions publishable:
- PASS → reverse signal upgraded, routed per mechanism diagnostic.
- NULL → reverse signal stays as exploratory footnote on parent H-NEW-34.
- MECHANISM-INCONSISTENT → escalation to classical-scholar.

### Reconciliation with 2026-04-14 integrator amendment

The 2026-04-14 amendment to `h-new-34-1-prereg.md` specified α_bon = 0.0033 (k=3 across baselines, "worst-m wins within each baseline"). The skeptical-auditor gate ruling (this entry) specifies α_bon = 0.0056 (k=9 cartesian across baselines × moduli, no "worst-m wins" internal step). **The auditor's k=9 supersedes** because it binds the full grid rather than collapsing across moduli. The content of the 2026-04-14 amendment (direction pre-reg, length-mediation via deciles, three-corpus) remains intact; only the threshold arithmetic tightens from 0.0033-per-baseline to 0.0056-per-(baseline × m)-cell.
