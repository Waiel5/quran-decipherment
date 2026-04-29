---
audit_id: audit-032
date: 2026-04-15
auditor: skeptical-auditor-fresh-wave-3
target: three Fresh-Wave-3 pre-registrations (H-NEW-41, H-NEW-42, H-NEW-43)
target_author: hypothesis-generator
stage: pre-execution pre-registration cleanliness audit
verdicts:
  H-NEW-41: NEEDS-AMENDMENT (two required edits; none are BLOCK-class)
  H-NEW-42: NEEDS-AMENDMENT (one BLOCK-class fallback-clause defect; one required edit)
  H-NEW-43: NEEDS-AMENDMENT (one required edit; one documentation note)
bonferroni_family: 2026-04-15-Fresh-Wave-3
bonferroni_k_declared: 3 across all three pre-regs (α_bon = 0.0167)
related_audits: audit-025 (PRE-REG-STANDARD-04 origin), audit-023 (fallback-clause abuse precedent), audit-030 (template-clean pre-reg), audit-031 (precision-of-claim forensics)
---

# Audit-032 — Fresh-Wave-3 pre-registration trio (H-NEW-41 / H-NEW-42 / H-NEW-43)

## Executive summary

Three pre-regs were filed 2026-04-15 by hypothesis-generator under a shared Bonferroni family `2026-04-15-Fresh-Wave-3` with `k=3`, `α_bon = 0.0167`. The shared-family declaration is correctly consistent across all three headers (PRE-REG-STANDARD-04 outer-level check passes).

Individually:

- **H-NEW-41** (root combinatorial saturation): substantively clean in structure, but (i) the classical reference set construction is under-specified and (ii) the positive-control threshold language ("similar to classical Arabic average") lacks a numerical fail threshold. **NEEDS-AMENDMENT.**
- **H-NEW-42** (reverse-direction fragility): contains a **BLOCK-class fallback clause** at §Three-baseline joint-threshold line 45: *"If Muʿallaqāt unavailable, we fall back to two baselines at α_cell = 0.0083 (and note the limitation explicitly)."* Muʿallaqāt IS available on disk (verified this audit). The availability-fallback is therefore both unnecessary and prohibited — it is exactly the T1 LLM-judge fallback-clause abuse pattern audit-023 caught. **NEEDS-AMENDMENT** (mandatory delete).
- **H-NEW-43** (corpus-wide verse-length FFT): the inner Bonferroni denominator quietly shifts from `k=10` (line 31) to `k=13` (line 41) without explicit reconciliation. Not a HARKing violation but a drafting error that must be corrected to a single, pre-committed denominator BEFORE execution. **NEEDS-AMENDMENT.**

**Most important single defect across the three:** the H-NEW-42 Muʿallaqāt-unavailable fallback. It is the one substantive pre-reg defect (not a drafting error) and is a live-ammunition reincarnation of the audit-023 fallback-clause abuse pattern. Remove it verbatim before execution.

All three are in-flight (not yet executed); per PRE-REG-STANDARD-04 this retroactive-tightening-before-execution is permitted.

---

## Pre-reg 1 — H-NEW-41 Root Combinatorial Saturation

**File:** `findings/phase-b-hypotheses/h-new-41-root-combinatorial-saturation-prereg.md`

**Verdict: NEEDS-AMENDMENT.** Two required edits; none are BLOCK-class.

### PRE-REG-STANDARD compliance

| Standard | Status | Notes |
|---|---|---|
| PRE-REG-STANDARD-01 (direction, no sign-flip) | PASS | Two-sided test explicitly declared (§Procedure step 5); the "either direction is publishable" language in §Mechanism interpretation is consistent with a genuine two-sided pre-reg and is NOT a sign-flip loophole (because both directions are mapped to named, pre-committed verdicts). CLEAN. |
| PRE-REG-STANDARD-02 (secondary-null adversarial origin) | PASS | The token-weighted secondary is declared PRE-data and flagged as robustness check, with type-level as primary. This is a pre-primary dual-spec, not an adversarial-flag amendment. Compliant. |
| PRE-REG-STANDARD-03 (feature-space locked) | PASS | §Garden-of-forking-paths explicitly prohibits expansion from 12 to 24 or 36 cells. 12 cells (4 POA-pair types × 3 root-position pairs) are locked. |
| PRE-REG-STANDARD-04 (Bonferroni before null) | PASS | Outer `k=3` / `α_bon = 0.0167` and inner k=12 / α_cell = 1.39×10⁻³ both declared in header and §Procedure step 6 before null design. |
| MW-1 (length/size confound) | PARTIAL | Type-level primary + token-weighted secondary is the correct treatment for this axis. One open question: roots with short segment counts (quadriliteral suppression, rare biliterals) are dropped, which is a reasonable but pre-registered choice. CLEAN. |
| MW-5 (positive control + failure criterion) | **NEEDS-AMENDMENT** | The positive-control spec (§Procedure step 7, "z < +2 / z > –2 on all 12 cells") uses "similar to classical Arabic average" as the PASS condition but does not state how z is COMPUTED or what the classical-Arabic reference distribution is. If classical-Arabic average is the mean of set C (classical but non-Quran), then Mutanabbī-vs-C should yield near-zero z. But Mutanabbī IS (in large part) a subset of C by construction. Need to either (a) hold out Mutanabbī's roots from C when computing the reference, or (b) use leave-one-out z. |
| MW-7 (internal-error pre-publication) | PASS | Gate-spec carries MW-5 control; rules-tuple declared; corpus paths declared. |

### HARKing 4-test

1. **Non-counting failed sub-tests:** CLEAN. The verdict table routes the "positive-control anomalous" case to NULL-BROKEN rather than silently discarding.
2. **Pre-existing mechanism:** CLEAN. Frisch-Pierrehumbert-Broe (2004) OCP-Place grounding is real prior art; the combinatorial-saturation framing is the novel contribution but sits on a known phonotactic literature.
3. **Pre-registered direction:** Two-sided test is explicitly declared; both high-structure and low-structure outcomes mapped to named verdicts. CLEAN.
4. **No rename/retrofit:** Verdict levels are pre-committed (NULL / EXPLORATORY-hit / PARTIAL-PASS / STRONG-PASS / NULL-BROKEN). No drift room.

### Required amendments before execution

**Amendment 41-A (MW-5 positive-control threshold precision).** Replace §Procedure step 7 language with:

> "Apply the identical pipeline to the Mutanabbī-Dīwān corpus. Compute the 12 phonotactic-cell z-scores using the classical reference set C with Mutanabbī's attested roots held out (leave-one-corpus-out). PASS criterion: for all 12 cells, |z_Mutanabbī| < 2.0. FAIL criterion (NULL-BROKEN): any cell with |z_Mutanabbī| ≥ 2.0. Any intermediate cell count (1–11) is reported as PARTIAL-POSITIVE-CONTROL and the Quran claim is downgraded to EXPLORATORY."

**Amendment 41-B (classical reference set documentation).** §Procedure step 2 says "Lane's *Arabic-English Lexicon* root index (public domain) + Hans Wehr's modern root list as the union." Specify BEFORE execution: (a) which digital edition of Lane is used (there are multiple PDF/OCR variants with different root-index completeness), (b) which Wehr edition (4th English / 5th Arabic / other). Recommendation: log exact source file paths and SHA-256 hashes in the script header. This does not change any statistic but prevents a future audit from arguing that the classical reference set was expanded/contracted to reach a target coverage number.

### Garden-of-forking-paths log check

The §Garden-of-forking-paths log (lines 66-70) covers: type-vs-token decision, positive-control-corpus choice (Mutanabbī, not Jāhiliyya), 12-cell inner family locked, quadriliteral split. Complete on all four axes that could drift. CLEAN.

### Publishable in both directions?

Yes. §Mechanism interpretation names both high-structure and low-structure Quran outcomes as publishable with distinct theological/linguistic readings. §Integrity commitment explicitly states "Publish PASS and NULL with equal prominence." CLEAN.

---

## Pre-reg 2 — H-NEW-42 Reverse-Direction Structural Fragility

**File:** `findings/phase-b-hypotheses/h-new-42-reverse-direction-fragility-prereg.md`

**Verdict: NEEDS-AMENDMENT** — one BLOCK-class fallback-clause defect; one required edit on baseline path documentation.

### PRE-REG-STANDARD compliance

| Standard | Status | Notes |
|---|---|---|
| PRE-REG-STANDARD-01 (direction) | PASS | §Direction pre-registration explicitly declares one-sided Δ̄_Quran > Δ̄_baseline with the reverse result reported as EXPLORATORY-REVERSE not promotable. This is the textbook implementation of the sign-flip prohibition. CLEAN. |
| PRE-REG-STANDARD-02 | N/A | No secondary-null residualization in this design. |
| PRE-REG-STANDARD-03 (feature-space locked) | PASS | §Garden-of-forking-paths explicitly prohibits f₇ post-hoc and locks embedding model before run. 6 fingerprint axes are LOCKED. CLEAN. |
| PRE-REG-STANDARD-04 (Bonferroni before null) | PASS | Outer k=3 / α_bon = 0.0167 declared; inner α_cell = 0.0167/3 = 5.56×10⁻³ declared in §Three-baseline joint-threshold. |
| MW-1 (length confound) | PASS | §Procedure step 5 length-matches baseline pseudo-surahs by quantile-matched letter count BEFORE computing fingerprints. Length normalization in Δ(S) divides by n_verses^0.5. Both treatments are pre-registered. CLEAN. |
| MW-5 (positive control + failure criterion) | PASS-with-note | Muʿallaqāt is the positive-control AND simultaneously one of the three decisive baselines. The failure criterion "Muʿallaqāt ≤ Jāḥiẓ" in the verdict table implements NULL-BROKEN correctly. CLEAN. However, see the fallback-clause block below. |
| MW-7 (internal-error gate) | **FAIL** | Baseline paths `bukhari_noquran.txt`, `jahiz_hayawan.txt`, `muallaqat_pool.txt` do NOT exist on disk. Actual files use hyphen-convention paths under `data/baseline-corpora/raw/` (e.g., `bukhari-noquran.txt`, `jahiz-hayawan.txt`, and a pool of 7 individual `muallaqa-*.txt` files). Pre-reg header paths are incorrect as written. |

### HARKing 4-test

1. **Non-counting:** CLEAN. Verdict table covers four outcomes including NULL-BROKEN.
2. **Pre-existing mechanism:** Acceptable — "dense-optimization vs ordered-prose" is a coherent structural-compositional hypothesis grounded in existing chiasm/rhyme literature on Quranic structure. Not a retrofitted framing.
3. **Pre-registered direction:** ONE-SIDED, pre-committed; reverse-direction mapped to named EXPLORATORY-REVERSE verdict with no promotion. CLEAN.
4. **No rename/retrofit:** Four verdict levels locked. No drift room visible.

### THE BLOCK-CLASS DEFECT (critical)

**Location:** §Three-baseline joint-threshold, line 45 of the pre-reg:

> *"If Muʿallaqāt unavailable, we fall back to two baselines at α_cell = 0.0083 (and note the limitation explicitly)."*

**Why this is BLOCK-class:**

1. **Muʿallaqāt IS available on disk.** Verified this audit: `data/baseline-corpora/raw/` contains all 7 Muʿallaqāt (`muallaqa-amr-bin-kulthum.txt`, `muallaqa-antara.txt`, `muallaqa-harith.txt`, `muallaqa-imru-al-qais.txt`, `muallaqa-labid.txt`, `muallaqa-tarafa.txt`, `muallaqa-zuhayr.txt`). The construction of `muallaqat_pool.txt` is a 5-line concatenation, not a data-availability question.
2. **The fallback LOOSENS α.** Going from α_cell = 0.0056 (with three baselines) to α_cell = 0.0083 (with two baselines) is a post-hoc α loosening. Per the 2026-04-14 ratification standard ("Bonferroni tightening self-verifies; loosening requires ratification"), this α loosening needs explicit ratification, which it does not have.
3. **It is the audit-023 fallback-clause abuse pattern.** Audit-023 caught a pre-reg that specified "if timeout → rule-based fallback" language that permitted silent path-switching from the hard test to a weaker test on an adjudication criterion the tester controls. "If Muʿallaqāt unavailable" has the same structure: the tester could claim unavailability for any downstream reason (failed preprocessing, encoding issue, etc.) and silently switch to the weaker two-baseline test at looser α.
4. **MW-5 depends on Muʿallaqāt specifically.** The pre-reg names Muʿallaqāt as the poetry positive-control distinguishing "poetic-constraint" from "super-poetic dense-optimization." Dropping it dissolves the entire distinction the test is designed to make. A two-baseline-only version of this test cannot separate PASS-VS-PROSE from STRONG-PASS.

**Required amendment (mandatory, BLOCK until applied):**

**Amendment 42-A (delete fallback clause).** Replace §Three-baseline joint-threshold line 45 with:

> "All three baselines (Bukhārī-ḥadīth-no-Quran, Jāḥiẓ-Ḥayawān, Muʿallaqāt-pool of the 7 canonical Muʿallaqāt) are REQUIRED. Muʿallaqāt-pool is constructed by concatenating the 7 Muʿallaqāt files at `data/baseline-corpora/raw/muallaqa-*.txt` in the canonical order: Imruʾ al-Qais, Ṭarafa, Zuhayr, Labīd, ʿAmr b. Kulthūm, ʿAntara, al-Ḥārith. If for any downstream reason Muʿallaqāt cannot be processed, THE TEST IS ABORTED (not downgraded) and re-filed with corrected preprocessing. No two-baseline fallback at any α. No α adjustment."

### Secondary required edit

**Amendment 42-B (fix baseline path paths in header).** The header `baselines:` block lists:
- `data/baseline-corpora/bukhari_noquran.txt`
- `data/baseline-corpora/jahiz_hayawan.txt`
- `data/baseline-corpora/muallaqat_pool.txt`

None of these exact paths exist. Correct to:
- `data/baseline-corpora/raw/bukhari-noquran.txt`
- `data/baseline-corpora/raw/jahiz-hayawan.txt`
- Muʿallaqāt-pool: construct-at-execution from `data/baseline-corpora/raw/muallaqa-{amr-bin-kulthum,antara,harith,imru-al-qais,labid,tarafa,zuhayr}.txt`, with the concatenation script and SHA-256 of the resulting pool logged in the findings file JSON output.

### Garden-of-forking-paths log check

The §Garden-of-forking-paths disclosure (lines 66-72) is good on: fingerprint-axes count, embedding-model lock, pseudo-surah matching scheme, verse-reversal-only scope. Missing: disclosure of which specific embedding model was LOCKED — the pre-reg says `aubmindlab/bert-base-arabertv02` OR EQUIVALENT. The "or equivalent" language is a soft drift point. Require the tester to pin the exact HuggingFace model commit-hash in the script header before execution (Note 42-1, non-blocking).

### Publishable in both directions?

§Integrity commitment lines 74-76 explicitly commit to publishing PASS, PASS-VS-PROSE, NULL, and NULL-BROKEN with equal prominence. CLEAN.

---

## Pre-reg 3 — H-NEW-43 Corpus-Wide Verse-Length FFT

**File:** `findings/phase-b-hypotheses/h-new-43-verse-length-fft-prereg.md`

**Verdict: NEEDS-AMENDMENT** — one drafting-error correction on inner-k denominator; one documentation note on AR(1) fit.

### PRE-REG-STANDARD compliance

| Standard | Status | Notes |
|---|---|---|
| PRE-REG-STANDARD-01 (direction) | PASS | The primary test is one-sided: "Is Quran max peak z-score > baseline max peak z-score?" (§Procedure step 6). Directed frequencies of interest (Fibonacci, 1/57, 1/7) are one-sided "peak present" tests. CLEAN. |
| PRE-REG-STANDARD-02 | N/A | No adversarial-flag secondary null. |
| PRE-REG-STANDARD-03 | PASS | §Garden-of-forking-paths locks: per-surah mean subtraction, canonical mushaf order as primary (chronology deferred), AR(1) null locked vs AR(2), K=10 locked, directed-frequency set locked pre-spectral-plot. CLEAN. |
| PRE-REG-STANDARD-04 (Bonferroni before null) | **NEEDS-AMENDMENT** | Inner Bonferroni denominator is declared as k=10 at §Procedure step 6 (α_cell = 0.0167/10 = 1.67×10⁻³) but then SHIFTS to k=13 at §Specific frequency-of-interest pre-register (α_inner = 0.0167/13 = 1.28×10⁻³). These two denominators disagree. |
| MW-1 | PASS | The per-surah mean subtraction + discarding k < 55 is a pre-registered control for the surah-length step-function trend. Length normalization on baseline comparison uses length-matched 6,236-point truncation. Pre-registered. |
| MW-5 (positive control + failure criterion) | PASS | §Procedure step 7 specifies a synthetic positive-control sinusoid at f₀ = 0.01 cycles/verse, amplitude 0.2σ, embedded in red noise matched to Quran. PASS criterion: "MUST be detected at α_cell." FAIL criterion: "NULL-BROKEN." CLEAN and specific. |
| MW-7 | PASS-with-note | Baseline corpora (Bukhārī, Jāḥiẓ, Muʿallaqāt) are assumed to have verse/sentence-length sequences extractable; that extraction protocol is not pre-registered. Recommendation for script header (Note 43-1, non-blocking). |

### HARKing 4-test

1. **Non-counting:** CLEAN. Four verdicts cover all outcomes including "0 peaks" and "positive-control not detected."
2. **Pre-existing mechanism:** ACCEPTABLE — the three directed frequencies (Fibonacci, 1/57 bipartition, 1/7 manzil) each have prior justification in classical or numerological discussion. The test is honestly scoped as "do these specific priors find signal, OR does exploratory K=10 find something unpredicted, OR is the spectrum featureless?"
3. **Pre-registered direction:** One-sided "peak present vs. null spectrum" is directional. CLEAN.
4. **No rename/retrofit:** Four-verdict table covers the space. CLEAN.

### The Bonferroni denominator drafting error

**Location:** Compare §Procedure step 6 ("Bonferroni inner k = 10") with §Specific frequency-of-interest pre-register ("Bonferroni across 3 directed + 10 undirected = 13 tests → α_inner = 0.0167 / 13 = 1.28 × 10⁻³").

Two competing denominators are declared in the same pre-reg. Per PRE-REG-STANDARD-04, the inner-k must be locked BEFORE null design, at a single value. This is a drafting error, not a HARKing violation, but it must be resolved before execution (otherwise the tester has a pre-committed choice of two α values and can select after seeing results).

**Required amendment 43-A.** Lock inner-k at 13 throughout:

> "Inner-k: **k = 13** (3 pre-specified directed frequencies + top-10 undirected peaks), α_inner = 0.0167 / 13 = 1.28 × 10⁻³. This supersedes the k=10 language in §Procedure step 6, which is a drafting error. All peak-significance tests (directed or exploratory) use α_cell = 1.28 × 10⁻³."

The tightening from α=1.67×10⁻³ to α=1.28×10⁻³ is a Bonferroni *tightening*, which per the 2026-04-14 standing note self-verifies and does not require external ratification. CLEAN to apply.

### Secondary required edit (documentation)

**Amendment 43-B (AR(1) fit pre-commit).** §Procedure step 4 fits AR(1) to L, but does not pre-commit the fit method (OLS, Yule-Walker, MLE) or a goodness-of-fit threshold. Following audit-030 Note 2 pattern: pre-commit a threshold — e.g., "AR(1) residuals must pass Ljung-Box test at p > 0.05; if fit is rejected, AR(1) null is disqualified and NULL-BROKEN is declared" — in the script header before execution. This prevents a post-hoc "AR(1) was mis-fit, let's try AR(2)" escape.

### Garden-of-forking-paths log check

Lines 52-58 cover: mean-subtraction choice, mushaf vs chronology order, AR(1) vs AR(2), K=10, directed-frequency set lock pre-spectral-plot. Complete. CLEAN modulo the drafting error above.

### Publishable in both directions?

§Mechanism interpretation names each verdict (DIRECTED-PASS at each directed frequency, EXPLORATORY-PASS, NULL) with substantively different theological/structural readings. §Integrity commitment lines 74-76 commits to publishing PASS or NULL alongside raw periodogram + null quantiles + positive-control output. CLEAN.

---

## Cross-pre-reg consistency

| Axis | H-NEW-41 | H-NEW-42 | H-NEW-43 | Consistent? |
|---|---|---|---|---|
| `bonferroni_family` | 2026-04-15-Fresh-Wave-3 | same | same | YES |
| `bonferroni_k` (outer) | 3 | 3 | 3 | YES |
| `alpha_bon` | 0.0167 | 0.0167 | 0.0167 | YES |
| `rules_tuple` | no-tashkeel + orth-token & lemma + graphemes + basmala-counted-only-in-surah-1 + hafs-kufan + mashriqi | no-tashkeel + orth-token + graphemes + basmala-counted-only-in-surah-1 + hafs-kufan + mashriqi | same as 42 | 41 includes "& lemma where noted", 42/43 do not — this is appropriate since 42/43 do not use lemmas. CLEAN. |
| `primary_corpus` | quran-no-tashkeel.json | same | same | YES |
| Positive control | Mutanabbī (MW-5 linguistic control) | Muʿallaqāt (MW-5 compositional control) AND synthetic sinusoid | synthetic sinusoid (MW-5 signal-detection control) | Each appropriately chosen for its test. CLEAN. |
| MW-7 physical-file verification | passes (QAC file exists) | **FAILS** (three baseline paths as written do not exist) | passes-with-note (baseline extraction protocol not pre-registered) | 42 needs path fix. |

**Family-level k=3 is correct.** Three independent hypotheses = three Bonferroni corrections. Cross-family inflation is not at risk here because the tests measure distinct axes (phonotactic selectivity vs. directional-optimization vs. spectral structure) on distinct data (root set vs. surah fingerprints vs. verse-length signal). No shared-corpus-dependence path exists that would require a tighter inter-pre-reg correction.

**Fresh-Wave-3 label integrity.** I verified this is not a re-submission of a previously-filed family (no `2026-04-15` Bonferroni family exists elsewhere in the pre-reg corpus per my scan). CLEAN.

---

## Per-pre-reg verdicts (consolidated)

| Pre-reg | Verdict | Blocking defect count | Required amendments |
|---|---|---|---|
| H-NEW-41 | NEEDS-AMENDMENT | 0 | 41-A (MW-5 positive-control threshold precision); 41-B (classical reference set SHA-256) |
| H-NEW-42 | NEEDS-AMENDMENT | 1 (fallback clause) | 42-A (**MANDATORY: delete Muʿallaqāt-unavailable fallback clause**); 42-B (fix baseline paths) |
| H-NEW-43 | NEEDS-AMENDMENT | 0 | 43-A (lock inner-k = 13 throughout, supersede k=10 drafting error); 43-B (AR(1) goodness-of-fit threshold) |

**All three pre-regs are fixable with small, targeted amendments. None of the three is structurally BLOCK (i.e., none has a defect so deep that the test needs to be redesigned). The H-NEW-42 fallback clause is BLOCK-CLASS as-written but is cleanly rescinded by deletion.**

After amendments 42-A, 43-A (and ideally 41-A, 41-B, 42-B, 43-B), all three can dispatch to execution.

## Single most important defect

**The H-NEW-42 Muʿallaqāt-unavailable fallback clause (line 45).** It is the only pre-reg defect in this audit that is substantive (not drafting) and that reincarnates a previously-caught abuse pattern (audit-023 T1 fallback-clause abuse). It is also conjoined with incorrect baseline paths that could plausibly cause the tester to *falsely* believe Muʿallaqāt is unavailable and trigger the fallback. Delete the fallback verbatim; fix the paths; require hard abort on processing failure rather than α-loosened two-baseline substitute.

## MW-series compliance summary

- **MW-1 (length residualization):** PASS on all three (41 via type-vs-token dual; 42 via quantile-matched pseudo-surahs; 43 via per-surah mean subtraction + k<55 discard).
- **MW-5 (positive control):** PASS on 43 (synthetic sinusoid fully specified); PASS-with-edit on 41 (threshold language needs 41-A); PASS on 42 (Muʿallaqāt-Jāḥiẓ ordering criterion); positive-control presence across all three is CLEAN.
- **MW-7 (internal-error gate):** FAIL on 42 due to baseline path errors; PASS on 41 and 43. Fixed by 42-B.

## Forward watches (for result-stage audit after findings land)

When the three findings files appear, the audit will check:

1. **Positive-control JSON outputs alongside findings.** All three pre-regs promise a positive-control output JSON. If absent, result is non-auditable.
2. **Exact Bonferroni denominator used.** For 41, 12 inner cells; for 43, 13 (after amendment). Any deviation = post-hoc drift.
3. **For H-NEW-42:** Muʿallaqāt must actually be in the baseline comparison — not silently omitted. SHA-256 of `muallaqat_pool.txt` logged in the JSON output.
4. **Direction of effect matches pre-registered prediction.** Especially H-NEW-42 where reverse-direction would be EXPLORATORY-REVERSE not STRONG-PASS. Verbatim verdict-level language expected.
5. **No new "per pre-registered fallback clause" language appears in any findings writeup** — the audit-023 failure mode.
6. **`bonferroni_family: 2026-04-15-Fresh-Wave-3` in frontmatter of all three findings** — locks cross-family accounting.

## MW-6 nawʿ-verification

N/A — none of the three pre-regs cite physical-edition nawʿ numbers. (H-NEW-41 cites Lane and Wehr as reference lexicons, not as classical-Islamic-sciences chaptered sources. CLEAN.)

## Classical-framing layer

Not required for this methodology audit. Classical-scholar involvement may become relevant at result-stage for H-NEW-43 if the 1/7 manzil peak clears (classical manzil-partition lore) or if the 1/57 mushaf-bipartition peak clears (classical ḥizb-structure lore).

## Closing

All three pre-regs are **high-quality by the standards of this project** — they each declare outer and inner Bonferroni before null design, each carry an MW-5 positive control with a failure criterion, each disclose a substantive garden-of-forking-paths log, and each commit to dual-direction publication. The H-NEW-42 fallback clause is the single substantive defect; it is easily amended by deletion.

After 42-A and 43-A (the two most important amendments) land, all three can be green-lit for execution. The remaining four amendments (41-A, 41-B, 42-B, 43-B) are tightening and documentation that I recommend but none of which BLOCK dispatch.

Filed under skeptical-auditor-fresh-wave-3/audit-032.
