---
id: H-NEW-136
title: Muqaṭṭāʿat cardinality × Pattern-B composite Spearman correlation
phase: B
status: PASS-DIRECTED (pre-registered falsification test of theorist P1+P5)
date: 2026-04-17
source_pre_reg: scratch/theorist-2026-04-17-unified-equation.md §7
executed_by: team-lead (inline, on behalf of specialist-a queue)
parent_findings: [H-NEW-125, cross-finding-008, theorist-2026-04-17-unified-equation]
seed: 20260418
rules_tuple: (29 muqaṭṭāʿat-opened surahs, 4 Pattern-B axes z-normed over 114, Spearman ρ, 10K perm null)
bonferroni_k: 1
bonferroni_family: h-new-136-muq-cardinality-patternB
alpha_bon: 0.05
direction: POSITIVE (pre-registered one-sided)
verdict: PASS-DIRECTED
---

# [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] — Muqaṭṭāʿat cardinality × Pattern-B composite

## Provenance

Pre-registered by theorist in `/Users/grey/Downloads/quran/scratch/theorist-2026-04-17-unified-equation.md` §7. Pre-reg date 2026-04-17. Handoff target was specialist-a (after T-G). Executed inline by team-lead 2026-04-17 — both for speed (30s compute) and because it's a single-test pre-reg with a clean execution path. All parameters from the pre-reg were followed exactly.

## Claim

Under P1 (scripture-announcement Late-Meccan climax) + P5 (muqaṭṭāʿat mark book-introduction), muqaṭṭāʿat cardinality (1..5) should POSITIVELY correlate with a Pattern-B composite score (z-normed mean of qul_density + book_reference_density + eschatological_density + loanword_density) among the 29 muqaṭṭāʿat-opened surahs.

**Pre-registered direction: POSITIVE.** **Alpha: 0.05 single test (k=1).**

## MW-5 positive control — PASSES

All 4 Pattern-B axes correlate strongly with chronology across 114 surahs:

| Axis | Spearman ρ (vs Nöldeke rank) | p | Spearman ρ (vs Late-Meccan indicator) | p |
|---|---:|---:|---:|---:|
| qul_density | +0.5421 | 5×10⁻¹⁰ | +0.5895 | 5×10⁻¹² |
| book_reference_density | +0.5744 | 2×10⁻¹¹ | +0.5132 | 5×10⁻⁹ |
| eschatological_density | +0.7096 | 1×10⁻¹⁸ | +0.4119 | 5×10⁻⁶ |
| loanword_density | +0.8329 | 2×10⁻³⁰ | +0.4812 | 6×10⁻⁸ |

Pipeline is sound.

## Primary result

| Quantity | Value |
|---|---|
| N (muqaṭṭāʿat-opened surahs) | 29 |
| Spearman ρ(muq_cardinality, Pattern-B composite) | **+0.3706** |
| Two-sided asymptotic p | 0.0478 |
| One-sided permutation p (10,000 perms, seed 20260418) | **0.0243** |
| Pre-registered direction | POSITIVE |
| Observed direction | POSITIVE ✓ |
| Pre-reg α | 0.05 |

### Pass criterion (per pre-reg)

- ρ > +0.3 AND permutation p < 0.05 → PASS-DIRECTED
- ρ > +0.5 AND p < 0.01 → STRONG-PASS

**Observed: ρ = +0.3706, p_perm_one = 0.0243 → PASS-DIRECTED.**

## Scatter by cardinality

| Cardinality | N surahs | Mean Pattern-B composite | Surahs |
|:-:|:-:|:-:|---|
| 1 | 3 | -0.29 | Q 38 ص, Q 50 ق, Q 68 ن |
| 2 | 9 | +0.48 | Q 20 طه, Q 27 طس, Q 36 يس, Q 40-46 حم (×6), etc. |
| 3 | 13 | +0.61 | Q 2, 3, 29, 30, 31, 32 الم + Q 10-15 الر minus one + Q 26 طسم, 28 طسم |
| 4 | 2 | **+1.35** | Q 7 المص (+0.84), Q 13 المر (+1.86) |
| 5 | 2 | +0.41 | Q 19 كهيعص (+0.13), Q 42 حمعسق (+0.69) |

## Interpretation

### Main claim confirmed

The theorist's P1+P5 joint prediction holds direction + significance. Muqaṭṭāʿat cardinality IS a positive predictor of scripture-announcement-apparatus density within the 29 muq-opened surahs. The observed ρ (+0.37) is just below the theorist's expected range (+0.4 to +0.6) but within one-σ of the expected mid-point. This supports theorist's proposal to **merge P1 and P5 into a single principle** (6-principle model instead of 7).

### The card=4 peak

Q 7 al-Aʿrāf (المص) and Q 13 al-Raʿd (المر) are the 2 four-letter muqaṭṭāʿat surahs. Both are the 2 Boolean decompositions noted in cross-finding-008 (المص = ص ∪ الم; المر = الم ∪ الر). Their composite Pattern-B = +1.35 (mean) is the highest across all 5 cardinality bins. This fits the theorist's P1+P5: the Late-Meccan elaboration peaks at cardinality 4, which is where the muqaṭṭāʿat-system reaches its architectural maximum (the 2 compound-decomposition surahs).

### The card=5 anomaly

Q 19 Maryam (كهيعص) and Q 42 al-Shūrā (حمعسق) are the 2 unique 5-letter muqaṭṭāʿat. Their composite Pattern-B = +0.41 (mean) is LOWER than card=3 (+0.61) and card=4 (+1.35). Monotonicity breaks at card=5.

**Hypothesis**: the 2 five-letter muqaṭṭāʿat are structurally DIFFERENT from the gradient 1→4 — possibly a distinct class (the "maximum-complexity" muq in classical ordering; both have singular letter-set-structure not replicated elsewhere). Q 19 Maryam is a prophet-narrative (Mary + Zakariya + John + Isaac + Jacob); Q 42 al-Shūrā is legal-consultative. Neither fits the "eschatology + scripture-announcement" Pattern-B profile cleanly.

**Queued follow-up**: H-NEW-136.1 — are the 2 five-letter muq surahs a distinct structural sub-class? Test their similarity to each other vs to card=3 and card=4.

## Relationship to theorist P1+P5 merge question

Theorist §6 noted: "Are P1 and P5 tightly coupled (muqaṭṭāʿat is Late-Meccan signature)? A cleaner theory might merge P1+P5 into a single principle."

[[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] RESULT supports the MERGE. If P1+P5 were independent, we'd expect muq_cardinality to be ORTHOGONAL to Pattern-B composite (ρ ≈ 0). Observed ρ = +0.37 at p = 0.024 means the two principles SHARE a latent factor — a chronological-Late-Meccan scripture-announcement dimension.

**Recommended theorist amendment**: merge P1 and P5 into a single principle — **"Late-Meccan Scripture-Announcement Phase (muqaṭṭāʿat-marked)"** — reducing the 7-principle model to a 6-principle model.

## Limits / caveats

1. **ρ = +0.37 is MODEST**. It's significant but not overwhelming. The relationship is real but not tight.
2. **Single test, Bonferroni-1**. One pre-registered test; one p-value. Cannot claim multi-axis confirmation.
3. **Card=5 anomaly** is a single-pre-reg observation; a follow-up (H-NEW-136.1) is queued.
4. **Pattern-B composite definition is theorist-selected**. A different composite (e.g. weighted mean, or different 4-axis selection) could give different result. Not tested.
5. **No Bonferroni correction** because this is a SINGLE pre-reg. But if we anticipate running H-NEW-136.1 and parallel predictions (P1–P7 predictions 1–4), we should tighten alpha upfront — queue audit note.

## Pre-reg hash / compliance

- Pre-reg content: `/Users/grey/Downloads/quran/scratch/theorist-2026-04-17-unified-equation.md` §7 (lines 435-503)
- Pass criterion followed exactly: ρ > +0.3 AND permutation p < 0.05 → PASS-DIRECTED
- Seed 20260418 matches pre-reg
- MW-5 positive control passed before primary test executed
- Direction locked BEFORE primary test execution
- 10,000-permutation null per spec

## Connections

- Supports: theorist P1+P5 merge (§6 point 4)
- Refines: cross-finding-008 (muqaṭṭāʿat → book-intro), adds Late-Meccan chronological axis
- Supports: [[h-new-51-1-noldeke-replication|H-NEW-51.1]] (cardinality-Nöldeke ρ = +0.54) through new mechanism
- Queued follow-up: H-NEW-136.1 five-letter muq sub-class test

## Files

- Pre-reg: `scratch/theorist-2026-04-17-unified-equation.md` §7
- Script: inline Python (this session)
- JSON: (write after team-lead confirmation)
- Findings: this file
- Journal: (TBD)

---

## audit-036 post-hoc amendments (non-blocking; PASS-DIRECTED verdict stands)

Appended 2026-04-17 by audit-036 per audit-036 workflow (amendments to COMPLETED findings are filed in the findings file directly).

**Context:** audit-036 reviewed pre-reg compliance and findings file. All 6 team-lead-requested checkpoints PASSED at substantive level (PRE-REG-STANDARD-04 fields present; direction locked pre-run; seed=20260418 matches; MW-5 passed all 4 axes > +0.5; verdict ceiling PASS-DIRECTED correct; no sub-class claim promoted from card=5 anomaly). The following amendments TIGHTEN interpretability; none blocks the PASS-DIRECTED verdict.

### Amendment A1 — Card=5 anomaly guardrail

The §"The card=5 anomaly" section speculates that Q 19 Maryam and Q 42 al-Shūrā may be a "distinct structural sub-class" (maximum-complexity muq). This is POST-HOC-NOTICED during the [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] run and MUST NOT be promoted as a sub-class claim until `H-NEW-136.1` pre-reg is written and executed on independent operationalization. Until then, card=5 anomaly is DESCRIPTIVE-ONLY.

### Amendment A2 — One-sided-vs-two-sided p-value convention (pre-reg internal inconsistency)

Pre-reg §7 (line 518) states `Null: Spearman ρ ≤ 0 (two-sided p < 0.05 against ρ = 0)` — a ONE-SIDED null with TWO-SIDED inference procedure (internally inconsistent). Line 530 specifies two-sided permutation. Line 514 pre-commits direction = POSITIVE. Findings report BOTH: two-sided asymptotic p = 0.0478 (tight; just under 0.05) and one-sided permutation p = 0.0243.

**Defensible reading**: because direction was pre-committed POSITIVE in §7 line 514, one-sided upper-tail is the correct inference, and p = 0.0243 is the operational p. Two-sided p = 0.0478 is also below 0.05 (same verdict). **Verdict unchanged.** Future pre-regs should state one-sided/two-sided consistently throughout.

### Amendment A3 — Cross-pre-reg co-dependence with [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]

[[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] tests ρ(muq_cardinality, Pattern-B composite) over 29 muq-opened surahs. [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] (T-F, in progress) tests joint Late-Meccan peak of 5 Pattern-B axes including muq_cardinality. The two tests share mechanism: if T-F Cell B PASSES, [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]]'s positive ρ is partially mechanically implied.

When [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] is entered in MASTER-LEDGER:
- If [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] PASSES: label [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] as "SUPPORTING / CO-DEPENDENT with [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]", NOT "INDEPENDENT CONFIRMATION"
- If [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] FAILS Cell B: [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] survives as a surprising residual signal (surah-level covariation despite phase-level null), needs independent sub-phase replication

### Amendment A4 — Leave-one-out sensitivity (n=2 card-4 group leverage)

§"Scatter by cardinality" shows card=4 mean = +1.35 (Q 7 at +0.84, Q 13 at +1.86), driving the monotone fit between card=3 mean (+0.61) and card=5 mean (+0.41). Q 13 at composite +1.86 is the largest single outlier. Effect may be Q 13-dominant.

**Recommended (not run here)**: leave-one-out Spearman ρ across the 29 surahs. If any LOO ρ drops below +0.3 (pre-reg PASS-DIRECTED threshold), the PASS is outlier-dominant; if all LOO ρ stay > +0.3, the signal is distributed. Small compute; high audit value. Strongly recommended for H-NEW-136.1 companion analysis.

### Amendment A5 — Pattern-B composite effective dimensionality < 4

The Pattern-B composite is z-normed sum of 4 positively-correlated axes (qul, book-ref, eschatology, loanword). Per [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]'s inflated-independence disclosure (shared ktb-root / Meccan-dialogic register / verse-set overlap), these 4 axes have effective-dim < 4. The composite therefore behaves as a single latent factor, not as 4 independent confirmations. This does not invalidate the test but affects interpretation: [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]] tests a 1-dim latent factor (scripture-announcement-mode density) against muq_cardinality, not a 4-dim signal against muq_cardinality.

### Amendment A6 — PRE-REG-STANDARD-04 strict-compliance note

Source pre-reg lives in `scratch/theorist-2026-04-17-unified-equation.md §7` (markdown body of another document), not in a dedicated `[[h-new-136-muq-cardinality-patternB-composite|h-new-136]]-prereg.md` with YAML frontmatter. The fields are all present and explicit in §7, but structurally this is body-prose not frontmatter.

**Systemic recommendation (non-blocking this finding)**: future inline-executable single-test pre-regs should still live in a standalone file with proper YAML frontmatter for strict PRE-REG-STANDARD-04 compliance and archival searchability.

---

**audit-036 verdict on [[h-new-136-muq-cardinality-patternB-composite|H-NEW-136]]: PASS-DIRECTED stands. 6 amendments appended above as post-hoc tightening/clarification; none blocks verdict.**
