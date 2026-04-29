---
finding_id: h-new-34.1
parent_finding: h-new-34
phase: B
status: PRE-REGISTERED — awaiting execution
pre_registered_by: computational-tester (2026-04-13); amended by hypothesis-generator (2026-04-14) per integrator three-point checklist
registration_date: 2026-04-13
amendment_date: 2026-04-14
promoted_from: audit-025 B1 blocker
rules_tuple: (hafs-kufan, mashriqi-abjad, hamza-carrier-policy, last-word-of-verse, verse-final-word definition identical to H-NEW-34 parent)
moduli: [7, 11, 19]
seed: 20260413
sided_test: one-sided under-dispersion (Quran z < baseline z; pre-committed sign)
direction_prereg_source: parent H-NEW-34 audit-025 Table 1 observed reverse signal (z ≈ −11 vs Bukhari/Jāḥiẓ at m=19); ≥2 empirical baselines already agree on sign → PRE-REG-STANDARD-02 one-sided permitted
baselines: [Bukhari-noquran, Jāḥiẓ Ḥayawān, Muʿallaqāt pooled-7-odes]
bonferroni_k: 3   # family = 3 baselines per integrator checklist point (3); worst-baseline wins verdict
alpha_bon: 0.0033  # = 0.01 / 3 per integrator α = 0.01 locking
null_publishable: true
positive_publishable: true
---

# [[h-new-34-1-under-dispersion|H-NEW-34.1]] — Muʿallaqāt rhymed-Arabic baseline for the reverse-signal under-dispersion of H-NEW-34

## Why this pre-registration exists

The parent finding H-NEW-34 (audit-025) closed as **PASSED-AS-NULL on its
primary pre-reg** (ḥisāb al-jummal modular clustering on verse-final-word
abjad residues does NOT distinguish the Quran from Bukhari/Jāḥiẓ baselines
at m∈{7, 11, 19}). A surprising **reverse signal** emerged in the raw χ²
contrasts: the Quran is *more uniform* than the prose baselines (z ≈ −11 vs
Bukhari/Jāḥiẓ at m=19).

The classically-grounded candidate mechanism is that the Quran's
rhyme-scheme forces verse-final-words onto a small recurring pool (fāṣila
repetition), which makes the abjad residue distribution more uniform than
sampling from un-rhymed prose.

Skeptical-auditor audit-025 §4 ruled this mechanism ASSERTED-NOT-TESTED and
recommended a Muʿallaqāt rhymed-baseline (B1) as the decisive adjudication.
Without running B1, the reverse signal cannot be promoted (either to M-6
fāṣila-substrate candidate OR to standalone novel finding).

## Pre-registered hypothesis

**[[h-new-34-1-under-dispersion|H-NEW-34.1]]-A (mechanism-confirmation):** If rhyme-driven fāṣila repetition
fully explains the under-dispersion, the Muʿallaqāt (a rhymed classical
Arabic corpus with enforced rāwī monorhyme) will show comparable χ²
under-dispersion vs the Bukhari/Jāḥiẓ prose baselines. Specifically, at
each modulus m ∈ {7, 11, 19}, the expected result is Quran z vs Muʿallaqāt
(same χ² framework) **close to zero** — Quran and Muʿallaqāt both
under-disperse relative to prose.

**[[h-new-34-1-under-dispersion|H-NEW-34.1]]-B (novel-finding alternative):** If the Quran under-disperses
even vs the Muʿallaqāt, the reverse signal has a residual beyond what
monorhyme-driven repetition explains, and H-NEW-34 becomes a standalone
hypothesis-generating finding about Quran-specific verse-final structure
(plausibly tied to M-6 pericope-substrate at a finer grain than rhyme).

## Pre-registered acceptance criteria (Bonferroni k=3, α_bon = 0.0167)

| Outcome                                                             | Verdict                                   | Downstream promotion                       |
|---------------------------------------------------------------------|-------------------------------------------|--------------------------------------------|
| |z_Quran − z_Muʿallaqāt| < 1.0 for all three m                      | **MECHANISM-CONFIRMED**                   | Reverse signal → M-6 fāṣila-substrate candidate |
| z_Quran < z_Muʿallaqāt − 3.0 for ≥ 1 m (after Bonferroni)           | **NOVEL-FINDING** (surplus under-disp.)    | Reverse signal → standalone hypothesis-generating finding; file as [[h-new-34-1-under-dispersion|H-NEW-34.1]]-REVERSE |
| 1.0 ≤ |gap| ≤ 3.0 at ≥ 1 m                                          | **PARTIAL** (rhyme-dominated but residual) | Report both; no M-5/M-6 promotion          |
| Muʿallaqāt χ² > prose baselines at any m                             | **MECHANISM-REJECTED** (unexpected: poetry over-disperses) | Escalate — mechanism hypothesis revised    |

"Gap" = z_Quran_vs_that_baseline − z_Muʿallaqāt_vs_that_baseline. The sign
convention matches audit-025 Table 1: more-negative z = more under-dispersion
vs prose.

## Pre-registered operationalization

1. **Corpus selection (locked BEFORE script modification):** the 7
   Muʿallaqāt dīwān texts already present in
   `data/baseline-corpora/raw/` (imru-al-qais, tarafa, zuhayr, labid,
   antara, amr-bin-kulthum, harith).

2. **Verse-final extraction:** tokenize each bayt (line) into whitespace-
   delimited tokens after DIAC stripping; take last token as the verse-final
   word. Apply the identical abjad-sum computation as the H-NEW-34 parent
   (mashriqi table, hamza-carrier rule).

3. **Sampling N=6219** (matching Quran's N in parent) **OR full Muʿallaqāt
   if smaller, no subsampling after seeing result**. Pooled across 7 odes.

4. **Null identical to parent H-NEW-34:** per-m χ² vs uniform expectation,
   with per-baseline resamples from the corpus (B=1000) to establish
   z_Muʿallaqāt_vs_prose (using Bukhari/Jāḥiẓ as in parent). Recompute
   Quran z vs Muʿallaqāt using the Muʿallaqāt as the NEW baseline.

5. **Add section `muallaqat_nulls_per_m` to the existing JSON output**
   `findings/phase-b-hypotheses/csv/h-new-34.json` (per audit-025 B1 spec).
   Do NOT overwrite parent-finding cells.

## Pre-committed no-fork protections

- **Sign of effect IS pre-registered:** parent H-NEW-34 already showed
  Quran under-disperses (z < 0 vs prose). The mechanism hypothesis predicts
  Muʿallaqāt *also* under-disperses vs prose (z < 0). If Muʿallaqāt χ² > 
  prose (over-disperses), mechanism is REJECTED — not a forking path.

- **No post-hoc modulus selection:** all three moduli {7, 11, 19} are tested
  with Bonferroni k=3. The worst-supported m wins the verdict.

- **No post-hoc baseline swap:** the three baselines (Bukhari, Jāḥiẓ,
  Muʿallaqāt) are fixed ex ante. If different baselines produce different
  verdicts, report all of them side-by-side and let the integrator adjudicate.

- **N-matching:** if Muʿallaqāt total verse-final-words < 6219, use full
  corpus and report the actual N. Do NOT upscale by repeat-sampling or
  downscale Quran to match; instead, compute power-adjusted z.

## Rationale for task #94 vs immediate execution

The immediate-execution version would run the code now. Task #94 is
**registration only** — formal pre-reg entry in team-discovery-synthesis §4a
and this file, such that when the Muʿallaqāt B1 run is subsequently
dispatched (expected to complete in ~30 min once queued), its result is
unambiguously adjudicated against this pre-commitment rather than
post-hoc interpreted.

## Link to H-NEW-SURVEY / H-NEW-SURVEY-EXT

If [[h-new-34-1-under-dispersion|H-NEW-34.1]]-A confirms (mechanism), this becomes part of M-6 substrate
evidence and should not double-count into H-NEW-SURVEY (cross-scale
mirror-string suppression).

If [[h-new-34-1-under-dispersion|H-NEW-34.1]]-B confirms (novel finding), it becomes eligible for
H-NEW-SURVEY-EXT (task #84) — abjad-residue flatness as a third
mirror-string-suppression scale beyond letter-level palindromes and
phonetic palindromes.

The H-NEW-SURVEY meta-hypothesis (AMEND-24) already anticipates this
conditional routing in its pre-reg.

## Status and dispatch

- **This file:** registers the pre-reg per task #94.
- **Actual B1 run:** a separate task that will edit
  `scripts/h_new_34_abjad_modular.py` to add the Muʿallaqāt baseline and
  re-emit `csv/h-new-34.json` with `muallaqat_nulls_per_m`. Expected ≤ 30 min.
- **Team-discovery-synthesis §4a:** will reference this file under the
  H-NEW-34 row (pending task #94 closure; this is part of this registration).

## Seed

`20260413` — identical to parent H-NEW-34 for deterministic reproducibility.
Muʿallaqāt subsampling (if needed) uses `random.Random(20260413)`.

## Registration closure

This file registers [[h-new-34-1-under-dispersion|H-NEW-34.1]] as a formal pre-registered follow-up. Task
#94 closes on this registration. Dispatch of the B1 execution run is a
separate task per team-lead queue management.

---

## AMENDMENT 2026-04-14 — integrator three-point checklist lock-in

Team-lead approved [[h-new-34-1-under-dispersion|H-NEW-34.1]] pre-reg subject to skeptical-auditor's
three-point checklist (relayed via integrator 2026-04-14). This amendment
locks those three points into the pre-registration. No changes to the
2026-04-13 operationalization above; these are additive pre-commitments.

### Point (1) — Independent pre-registration of under-dispersion direction (ONE-SIDED)

Parent H-NEW-34 was two-tailed and closed NULL on its own two-tailed test.
[[h-new-34-1-under-dispersion|H-NEW-34.1]] is pre-registered as **one-tailed under-dispersion** (Quran z <
baseline z). This is permitted under PRE-REG-STANDARD-02 because:

- Parent H-NEW-34 Table 1 empirical baselines (Bukhari and Jāḥiẓ) already
  agree on direction: z_Quran vs Bukhari ≈ −11 at m=19; z_Quran vs Jāḥiẓ
  also negative. Two independent prose baselines agree on sign.
- The under-dispersion mechanism (rhyme-driven fāṣila repetition) classically
  predicts Quran-uniformity as lower-tail departure from uniform sampling.

**Sign of effect IS pre-registered as Quran z < baseline z**, committed
BEFORE any [[h-new-34-1-under-dispersion|H-NEW-34.1]] execution. Post-hoc sign flip is prohibited.

### Point (2) — Length-mediation check (length-stratified dispersion statistic)

Confound: short verses have fewer letters → lower abjad variance
mechanically. Without stratification, an apparent under-dispersion signal
could be an artifact of the Quran's average verse-length being shorter (or
longer) than baselines.

**Pre-registered stratification protocol:**

1. Compute per-verse verse-final-word **letter-count** (not abjad sum — the
   raw letter count of the final word) across Quran + all three baselines.
2. Bin into **deciles** (10 equal-frequency bins of letter-count), using the
   **pooled Quran+baselines distribution** to define decile cut-points (so
   the bins are comparable across corpora).
3. Compute the χ² under-dispersion statistic **within each decile bin
   separately** for each corpus. This yields 10 z-scores per (corpus, m)
   combination.
4. The primary length-stratified statistic is
   `z_stratified_corpus_m = mean_over_deciles(z_corpus_decile_m)` with
   per-decile inverse-variance weighting.
5. Report raw (unstratified) and stratified z side-by-side. If the
   stratified z shrinks toward zero by > 50 % vs raw, report as
   **LENGTH-CONFOUND EXPLAINS MOST OF EFFECT** (verdict: not a rhyme-driven
   mechanism but a length-mediated artifact).
6. If stratified z retains ≥ 50 % of magnitude and still meets one-sided
   α_bon < 0.0033, verdict follows the matrix in §"Pre-registered acceptance
   criteria" above, restricted to the stratified statistic.

**Pre-committed tie-breaker:** if raw and stratified disagree (one meets
α_bon, the other does not), the **stratified** statistic is authoritative
for PASS/FAIL — the length confound is the central skeptical concern and
the stratified statistic is purpose-built to neutralize it.

### Point (3) — Three-baseline consistency (Bukhari + Jāḥiẓ + Muʿallaqāt)

The pre-reg's acceptance matrix from §"Pre-registered acceptance criteria"
is **extended to require Quran-specific under-dispersion across all three
baselines**, not just vs Muʿallaqāt alone.

**Extended pre-committed verdict table (supersedes 2026-04-13 matrix for
primary verdict purposes; 2026-04-13 matrix preserved for mechanism-vs-novel
routing):**

| Joint outcome across 3 baselines                                              | Primary verdict                    |
|-------------------------------------------------------------------------------|------------------------------------|
| Stratified Quran-z < baseline-z at α_bon < 0.0033 for **all 3** baselines     | **PASS — Quran-specific under-dispersion** |
| Stratified Quran-z < baseline-z at α_bon < 0.0033 for **2 of 3** baselines     | **PARTIAL** (report all; no PASS) |
| Stratified Quran-z < baseline-z at α_bon < 0.0033 for **≤1 of 3** baselines    | **NULL**                           |
| Any baseline shows Quran **over-disperses** at α_bon                           | **MECHANISM-INCONSISTENT** — escalate |

**Mechanism-vs-novel-finding routing** (2026-04-13 matrix) now runs on the
**Muʿallaqāt-specific comparison only** to adjudicate whether
rhyme-mechanism fully explains the effect, conditional on the primary
verdict above being PASS.

### Integrator α = 0.01 Bonferroni lock

Per integrator instruction: **α = 0.01, Bonferroni k = 3 across baselines →
α_per_baseline = 0.0033**. This supersedes the 2026-04-13 header's
`alpha_bon = 0.0167` (which reflected k=3 across moduli, not across
baselines). Both corrections are now required jointly:

- Across 3 baselines: α = 0.0033.
- Across 3 moduli: worst-m wins within each baseline (no additional
  Bonferroni — the "worst-supported m wins" rule inherited from 2026-04-13
  pre-reg is maintained).

The effective per-(baseline, worst-m) threshold is 0.0033.

### Dispatch chain locked

1. hypothesis-generator → files formal pre-reg (this document, this
   amendment) — **done by this commit**.
2. computational-tester → executes [[h-new-34-1-under-dispersion|H-NEW-34.1]] per rules above (edits
   `scripts/h_new_34_abjad_modular.py` to add length-deciled +
   three-baseline protocol).
3. skeptical-auditor → audits per three-point checklist compliance.
4. integrator → integrates verdict into MASTER-FINDINGS-LEDGER.

### Reporting commitment (both directions publishable)

- If **PASS** (all-3 baselines one-sided under-dispersion at α_bon =
  0.0033 after length-stratification): report as positive finding; route per
  2026-04-13 §"Link to H-NEW-SURVEY" (mechanism vs novel conditional).
- If **NULL** (≤1 baseline meets): report as honest NULL; M-6
  fāṣila-substrate downgrades; reverse signal from parent H-NEW-34 becomes
  length-confound-explained and does not promote.
- If **MECHANISM-INCONSISTENT**: escalate to classical-scholar for
  explanation; possibly reopen parent H-NEW-34 mechanism hypothesis.

### Provenance of this amendment

Authored by hypothesis-generator 2026-04-14 in response to integrator
request relaying team-lead approval + skeptical-auditor three-point
checklist. No changes to 2026-04-13 operationalization; all additions are
pre-commitments BEFORE any execution. The 2026-04-13 author
(computational-tester) retains primary authorship of the base pre-reg; this
amendment is an integrator-requested pre-execution tightening.
