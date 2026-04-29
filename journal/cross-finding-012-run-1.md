---
id: cross-finding-012
run: 1
date: 2026-04-17
author: synthesizer
pre_reg: findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement-prereg.md
script: scripts/cross_finding_012_joint_peak.py
output_json: findings/phase-b-hypotheses/csv/cross-finding-012.json
---

# cross-finding-012 run 1 journal

## Setup

- Axes (5, Pattern B): qul_density, book_reference_density, eschatological_density, muq_cardinality, loanword_density
- Sub-bins: octile over Nöldeke rank 1..114 (N_BINS=8)
- Sub-bin counts (B1..B8): [15, 14, 14, 14, 14, 14, 14, 15] — near-equal
- Nöldeke Late-Meccan band (ranks 70–90) spans bins B5, B6, B7 (0-indexed 4,5,6)
- Target bins for Cell B: {B5, B6, B7}
- Null: 10,000 Nöldeke-rank shuffle permutations, seed 20260417
- Bonferroni k=3, α_bon=0.01667

## Audit-036 tightening amendments applied BEFORE run

1. YAML frontmatter acceptance_window, verdict_ceiling, post_hoc_origin, effective_independent_axes
2. Post-hoc-noticed-origin disclosure section added
3. Inflated-independence disclosure restructured into 3 tiers (definitional-axis / latent-factor / interpretation-discipline)
4. Cell A-sensitivity (4-axis drop-muq W) added as mandatory companion statistic; not a new Bonferroni cell
5. PASS-DIRECTED verdict ceiling explicit throughout

All amendments are TIGHTENINGS (no α loosened); self-verifying per
HANDOFF/04-DISCIPLINE.md §Bonferroni-asymmetry-rule. No results
viewed before amendments applied.

## Observed statistics

### Cell A (PRIMARY) — 5-axis Kendall's W

- **W_obs = 0.7924**; perm p = **0.00990**; **PASS @ α_bon=0.01667** ✓
- Per-axis peak bins:
  - qul_density → B7
  - book_reference_density → B7
  - eschatological_density → B6
  - muq_cardinality → B6
  - loanword_density → B7
- 3 of 5 axes peak at B7, 2 of 5 at B6; all 5 in target {B5,B6,B7}

### Cell A-sensitivity (audit-036) — 4-axis drop-muq Kendall's W

- **W_obs = 0.8929**; perm p = **0.00300**; **PASS @ α_bon=0.01667** ✓
- Removal of the definitional axis STRENGTHENS the concordance
  (W rises from 0.79 to 0.89; p drops from 0.0099 to 0.0030)
- Evidentiary-floor claim HOLDS on truly-independent axes alone
- Per-axis peak bins: qul→B7, book→B7, eschat→B6, loanwords→B7

### Cell B (SECONDARY) — Joint peak-bin argmax

- Observed: 5/5 axes in target {B5,B6,B7}; modal peak bin = B7
- Criterion met in observed data (pre-committed PASS)
- Perm null: criterion (4/5 in target AND mode in target) met by
  15.79% of perms — **FAIL @ α_bon=0.01667** ✗
- **Interpretation**: Cell B's perm null is LIBERAL because target
  spans 3 of 8 bins (37.5% of bin-space), so random alignment hits
  the criterion often. The positive control also fails Cell B's
  α_bon gate (p=0.128) despite passing the descriptive criterion
  — confirming this is a test-design issue, not evidence failure.
  See §Design-weakness disclosure below.

### MW-5 positive control (5 Pattern-A monotone-up axes)

- W_obs = 0.9467; perm p = 0.00090; **PASS @ α_bon=0.01667** ✓
- All 5 axes peak at B8 (Medinan core); 5/5 in target {B7,B8}
- Kendall's W pipeline recovers expected Medinan joint-peak → pipeline VALID
- Cell B positive-control p = 0.128 (same liberal-null problem)

## Design-weakness disclosure (Cell B)

Cell B's "modal-peak + 4/5 in target" criterion is satisfied by
~16% of random perms because the target bin set {B5,B6,B7}
occupies 3/8 = 37.5% of the bin-space. Random-alignment p-values
are therefore never going to be <1.67% under this exact test
design.

This is a PRE-REG DESIGN FLAW, not a data failure. The positive
control confirms: when the 5 Pattern-A axes genuinely jointly peak
at Medinan core (B8, with 5/5 at B8), Cell B's perm null still
gives p=0.128. If 100%-at-one-bin concordance can't beat α_bon
under this null, the test was mis-calibrated.

**Correct interpretation**: Cell B's OBSERVED criterion met (5/5
in target, modal B7) is consistent with the Pattern B axes
jointly living in the {B5,B6,B7} zone. The perm null's p=0.158
indicates this level of clustering isn't formally significant
against a "3 of 8 bins occupies target" chance expectation, but
Cell B was never the primary test — Cell A (Kendall's W) is.

**Cell A is what passes; Cell A-sensitivity (4-axis) passes more
strongly. That is the result.**

## Headline verdict

- **Cell A (primary): PASS** — Kendall's W=0.79, p=0.0099, 5-axis
- **Cell A-sensitivity (4-axis drop-muq): PASS** — W=0.89, p=0.0030
  (the stronger, evidentiary-floor statistic)
- **Cell B (liberal-null design flaw): PASS on observed criterion,
  FAIL on perm-null α_bon** — disclosed as design weakness
- **MW-5 positive control: PASS** — pipeline valid
- **Modal peak bin: B7 (Nöldeke ranks 86–99)** — slightly shifted
  from hypothesized B6 (ranks 72–85); B7 straddles the Late-Meccan/
  Medinan boundary (Nöldeke Late Meccan is ranks 70–90)
- **Verdict: PASS-DIRECTED** (post-hoc-noticed; replication
  required for CONFIRMED)

## What the peak shift (B6 → B7) means

The pre-committed HYPOTHESIZED peak was B6 (Nöldeke ranks 72–85,
"Late Meccan core"). The OBSERVED modal peak is B7 (ranks 86–99,
"Late Meccan / early Medinan boundary"). B7 still falls within the
1-bin-tolerance acceptance window {B5,B6,B7}, so Cell B's
descriptive criterion is met. But the empirical scripture-
announcement apparatus appears to be most-concentrated at the
LATE END of Late-Meccan / transition into Medinan, not at Late-
Meccan's chronological center.

Narratively: the apparatus peaks JUST BEFORE or JUST AT the Hijra,
then drops off sharply in the Medinan-core B8. This refines the
H-NEW-125 Pattern-B story: the Late-Meccan peak is not diffuse
over the 21-surah Late-Meccan band but concentrated at its late
edge. This is consistent with traditional historical-critical
readings placing the most-self-consciously-scriptural surahs
(Q 39-45, Q 17-18, Q 25) at the very end of the Meccan period.

## Surahs in modal peak bin B7 (Nöldeke ranks ~86–99)

See JSON `surahs_by_bin.B7` for the 14-surah list. By construction
these are Nöldeke rank 86–99 surahs.

## Discipline check

- MW-1 (length residualization): not applied per pre-reg (axes
  are /100v densities by construction); logged in garden-of-forking-
  paths
- MW-5 positive control: PASS
- MW-6 (classical-citation tags): not applicable (no verbatim
  quotation of tafsir/classical sources)
- MW-7 (pre-publication 3-check): synthesis identifiers match
  scratch (scratch/connection-muqattaat-as-late-meccan-scripture-
  announcement.md), citations match H-NEW-125 JSON (no re-extraction),
  gate-specs carry MW-5
- Post-hoc discipline (HANDOFF/04 §"Post-hoc-noticed protocol"):
  origin disclosed; test family locked; α_bon < 0.05 single-test cap;
  verdict ceiling = PASS-DIRECTED; replication queue enumerated

## Files

- Pre-reg: findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement-prereg.md
- Script: scripts/cross_finding_012_joint_peak.py
- JSON: findings/phase-b-hypotheses/csv/cross-finding-012.json
- Findings: findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement.md (next)
- Journal: this file
