---
id: cross-finding-012
title: "Late-Meccan Scripture-Announcement Apparatus — joint-peak concordance test for 5 Pattern-B axes"
phase: B (synthesis)
status: PRE-REGISTERED 2026-04-17
spec_locked_at: 2026-04-17 (BEFORE any Kendall-W / joint-peak computation on the 5 Pattern-B axes)
agent: synthesizer
parent_findings:
  - cross-finding-008 (muqaṭṭāʿat as book-introduction markers; audit-034-tightened)
  - H-NEW-125  (Pattern-B = 5 Late-Meccan-peak content/structural axes)
  - H-NEW-74   (qul density Late-Meccan peak)
  - H-NEW-53   (book-reference density, post-hoc)
  - H-NEW-51.1 (muq cardinality × Nöldeke rank)
bonferroni_family: cross-finding-012-joint-peak
bonferroni_k: 3
alpha_bon: 0.0167   # 0.05 / 3
direction: Late-Meccan-peak (1-sided per axis; joint-peak test is inherently directional)
acceptance_window: "Cell A Kendall's W perm p < 0.0167 (1-sided) AND Cell B (modal peak ∈ {B5,B6,B7} AND ≥4/5 axes peak in {B5,B6,B7}) perm p < 0.0167 AND MW-5 positive control passes (Pattern-A monotone-up axes joint-peak in {B7,B8} with p<0.0167)"
verdict_ceiling: PASS-DIRECTED (post-hoc-noticed connection per audit-036 pitfall; independent replication on a distinct data dimension — e.g., Egyptian revelation order, Mingana/Horovitz loanword list — required before any upgrade to CONFIRMED)
post_hoc_origin: "Connection was EYEBALLED from cross-finding-008 (muqaṭṭāʿat-as-book-introduction-markers) + H-NEW-125 Pattern B (5-axis Late-Meccan peak); see scratch/connection-muqattaat-as-late-meccan-scripture-announcement.md. Test family locked BEFORE any Kendall-W / joint-peak computation; no prior run consumed; but the 5-axis bundle itself is a post-hoc selection from H-NEW-125's 15-axis result."
effective_independent_axes: "≤ 4 (muq_cardinality is Pattern-B by definition per scratch connection note §Supporting-data; evidentiary-floor is ≤ 3 after scripture-self-reference latent-factor discount)"
seed: 20260417
n_perm: 10000
rules_tuple: (no-tashkeel; Tanzil-JSON verse text; Leeds-QAC-v0.4 morphology; Nöldeke rank from data/revelation-order.csv column noldeke_order; phase boundaries from that same file; densities and axis values inherited VERBATIM from H-NEW-125 per-surah axis_values JSON; no re-extraction)
primary_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
chronology:   /Users/grey/Downloads/quran/data/revelation-order.csv
upstream_json: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-125.json
prior_runs_consumed: 0   # THIS PRE-REG LOCKED BEFORE THE JOINT-PEAK RUN
---

# [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] — The Late-Meccan Scripture-Announcement Apparatus

## Claim to test

Pattern B in [[h-new-125-chronology-content|H-NEW-125]] is NOT five independent Late-Meccan peaks but one
latent scripture-announcement signature surfacing on five axes. If that
is true, the five axes' **Nöldeke-sub-bin rankings should be concordant**
(i.e., they should all peak at the same fine-grained bin, within a one-
bin tolerance), at a level far beyond what random Nöldeke-bin assignments
would produce.

**Pre-committed directional claim** (1-sided by construction): the joint
peak of the 5 Pattern-B axes falls in a LATE-MECCAN sub-bin (strictly
interior to the Nöldeke ranks 70–90 band in `revelation-order.csv`).
Neither Early-Meccan, Middle-Meccan, nor Medinan peaks satisfy the
claim. A null peak in any non-Late-Meccan bin = DIRECTIONAL FAIL
(no sign-flip).

## Inflated-independence disclosure (MANDATORY, audit-034/035/036 lineage)

The 5 Pattern-B axes are **NOT independent**. The effective count of
truly-independent axes is **≤ 4**, and arguably **≤ 3**. Critical
disclosure per audit-036 pre-review pitfall:

### (A) muq_cardinality is Pattern-B BY DEFINITION, not by independent evidence

`muq_cardinality` is [[h-new-125-chronology-content|H-NEW-125]] axis 3. Its Pattern-B classification
is a **direct observation** from [[h-new-125-chronology-content|H-NEW-125]] phase-means, and the
connection seed itself (scratch/connection-muqattaat-as-late-
meccan-scripture-announcement.md §"Supporting data") explicitly
flags: "muq-cardinality is Pattern B BY DEFINITION ([[h-new-125-chronology-content|H-NEW-125]] axis
13)." Counting muq_cardinality as a 5th evidentially-independent
axis in the joint-peak test INFLATES the effective independence
to 5 when the true count is at most 4.

**Therefore**: Cell A's 5-axis Kendall's W is reported **alongside**
a "drop-muq-cardinality" 4-axis W as a mandatory sensitivity check.
The 4-axis W is the evidentiary-floor statistic:

- If 4-axis W remains significant at α_bon=0.0167 → joint apparatus
  claim holds on truly-independent axes; Cell A PASS robust to the
  definitional-axis removal.
- If 4-axis W drops below α_bon while 5-axis W passes →
  muq_cardinality is carrying a material share of the concordance
  signal; the "joint apparatus" claim weakens and is interpreted
  as "4 content axes + 1 definitional axis aligning at Late Meccan."
- Both W values reported in the findings file with equal prominence.

### (B) Remaining 4-axis latent-factor dependency structure

Even after the muq-cardinality adjustment, the 4 remaining axes
(qul, book-ref, eschat, loanwords) share a "scripture-self-reference
mode" latent factor:

1. `qul_density` and `book_reference_density` are both Meccan-
   dialogic register features; Medinan surahs drop both ([[h-new-74-qul-distribution|H-NEW-74]],
   [[h-new-53-muqattaat-book-reference|H-NEW-53]]).
2. `eschatological_density` and `book_reference_density` are
   lexical-content densities measured on overlapping verse sets
   (e.g., "yawm al-qiyāma" verses often also reference the "kitāb"
   of deeds; lexical-verse overlap is non-zero).
3. `loanword_density` (Jeffery 218) is the least dependent — the
   lemma list is lexically orthogonal to the other three — but
   co-varies via verse length and surah register.

Effective independent-axis count is thus **≤ 3 for strong-
independence-evidence purposes**. We treat 4 as the reporting-
floor and 3 as the evidentiary-floor. The findings file will
explicitly avoid "4 independent axes" and "5 independent axes"
language; the correct framing is "4 axes with shared latent
register factor + 1 definitional axis."

### (C) Interpretation discipline

The joint-peak test therefore **over-estimates effective independence**.
We report the Kendall's W result as a concordance statistic and do
NOT multiply per-axis p-values. The inflated-independence discount
means: even a highly-concordant peak is consistent with ONE latent
factor expressing through 3–4 correlated operationalisations, not 4
or 5 independent confirmations. The test's value lies in:
- Confirming that concordance is > null (so the Pattern-B axes DO
  move together at the fine-grained sub-bin level, not accidentally)
- Locating the **specific Nöldeke-sub-bin** where they peak (the
  empirical coordinate of the scripture-announcement mode)
- NOT in constructing an independent-evidence argument.

Per audit-034 on cross-finding-008 "5 independent tests" framing and
audit-036 pre-review pitfall: we disclose at two tiers (axis 1 is
definitional; axes 2-5 share latent factor), we do not double-count,
and we do not promote on independent-evidence grounds.

## Post-hoc-noticed origin (MANDATORY disclosure per audit-036 pitfall)

**This is a POST-HOC-NOTICED connection.** The specific claim tested
("5 Pattern-B axes jointly peak at the same Nöldeke-sub-bin in Late-
Meccan") was NOT pre-registered before [[h-new-125-chronology-content|H-NEW-125]] ran. It was
**eyeballed after** [[h-new-125-chronology-content|H-NEW-125]] classified 5 of its 15 axes as
INVERTED-U peak-Late-Meccan (see
scratch/connection-muqattaat-as-late-meccan-scripture-announcement.md).
The 5-axis bundle IS a post-hoc selection from [[h-new-125-chronology-content|H-NEW-125]]'s 15-axis
result; it is not a de-novo hypothesis.

Per `HANDOFF/04-DISCIPLINE.md §"Post-hoc-noticed findings — the
protocol"`:

1. **Origin disclosed** here (this section) and in garden-of-
   forking-paths entry "post-hoc origin" below and in the YAML
   frontmatter field `post_hoc_origin`.
2. **Test family LOCKED in this pre-reg BEFORE running Cell A/B
   null**. Single test family (k=3 cells); no post-registration
   expansion. No perm numbers viewed.
3. **Single-test α=0.05 cap applies** — but we've chosen the
   tighter α_bon = 0.0167 (Bonferroni-3 over the 3 cells) which
   strictly exceeds the required discipline. Tightening self-
   verifies per project convention.
4. **Verdict ceiling = PASS-DIRECTED**, not CONFIRMED. Upgrade to
   CONFIRMED requires **independent replication on a distinct
   data dimension**, explicitly:
   - Swap Nöldeke rank for Egyptian Standard revelation order
     (already partially done by Sadeghi 2011; rerun cross-finding-
     012 on that chronology)
   - Swap Jeffery-1938 loanword list for Mingana 1927 or Horovitz
     1926 alternative; test whether `loanword_density` axis peak
     bin persists
   - Swap eschat-lemma list for alternative Quranic-studies
     operationalisation (e.g., Neuwirth 1981 Day-of-Judgement
     concordance)
   - Swap to a different binning granularity (e.g., 10 equal-count
     bins) as ROBUSTNESS check; not itself a replication
5. Cross-reference against existing findings (cross-finding-008,
   [[cross-finding-010-extended-network|cross-finding-010]], [[h-new-93-q29-q30-subpattern|H-NEW-93]]): already present in parent-findings
   YAML frontmatter and body.

This PASS-DIRECTED ceiling is logged in YAML frontmatter
`verdict_ceiling` field and reiterated in the findings-file
verdict section regardless of Cell A/B outcomes.

## The 5 Pattern-B axes (LOCKED; verbatim from [[h-new-125-chronology-content|H-NEW-125]])

All 5 axes are directly pulled from `[[h-new-125-chronology-content|h-new-125]].json.per_surah_axis_values[sid].axis_values[axis_name]`:

| # | Axis | [[h-new-125-chronology-content|H-NEW-125]] operational def | Pattern-B classification source |
|---|---|---|---|
| 1 | `qul_density` | qul-imperatives / 100 verses (QAC POS:V IMPV LEM:qaAla 2MS) | [[h-new-125-chronology-content|H-NEW-125]] axis 5, ρ=+0.542 INVERTED-U peak Late |
| 2 | `book_reference_density` | kitāb/qurʾān/āyāt/nazala root tokens / 100 verses | [[h-new-125-chronology-content|H-NEW-125]] axis 9, ρ=+0.574 INVERTED-U peak Late |
| 3 | `eschatological_density` | yawm/ākhira/qiyāma/jahannam/firdaws/nār/janna / 100 verses | [[h-new-125-chronology-content|H-NEW-125]] axis 8, ρ=+0.710 INVERTED-U peak Late |
| 4 | `muq_cardinality` | 0 for non-muq; unique letters for muq surah | [[h-new-125-chronology-content|H-NEW-125]] axis 3, ρ=+0.255 INVERTED-U peak Late |
| 5 | `loanword_density` | Jeffery-1938 218-entry matches / 100 verses | [[h-new-125-chronology-content|H-NEW-125]] axis 15, ρ=+0.833 INVERTED-U peak Late |

These are the EXACT 5 axes called out in [[h-new-125-chronology-content|H-NEW-125]] §Pattern B and in
the `scratch/connection-muqattaat-as-late-meccan-scripture-announcement.md`
seed document. No swaps, no substitutions, no additions.

## Nöldeke sub-binning (LOCKED)

We use **equal-count octile bins** over the continuous Nöldeke rank
(1..114). This gives 8 sub-bins of ~14 surahs each. The binning is
rank-based (not phase-label-based) to gain sub-phase resolution:

| Sub-bin | Nöldeke-rank range | ~n surahs | Classical phase mapping |
|--------:|:------------------:|----------:|:------------------------|
| B1 | 1–14   | 14 | Early Meccan, early stratum |
| B2 | 15–29  | 15 | Early Meccan, mid stratum |
| B3 | 30–43  | 14 | Early Meccan, late stratum |
| B4 | 44–57  | 14 | Early/Middle Meccan boundary (Early: 48 surahs → B1–3 and part of B4) |
| B5 | 58–71  | 14 | Middle Meccan / Late Meccan boundary |
| B6 | 72–85  | 14 | **Late Meccan core** (Nöldeke rank 70–90) |
| B7 | 86–100 | 15 | Late Meccan / Medinan boundary |
| B8 | 101–114 | 14 | Medinan core |

(Exact per-surah bin assignments determined by a STABLE numpy
 percentile split on the 114 Nöldeke ranks; LOCKED seed 20260417.
 If the percentile split produces off-by-one edge cases, bin
 membership is computed once at script start and printed to journal
 for transparency; actual n per bin may vary by ±1.)

**Why octile**: (a) it gives ≥3 bins overlapping the Nöldeke
Late-Meccan 21-surah band, enough to distinguish a peak at B6 (core)
from peaks at B5 (pre-Late) or B7 (post-Late/early-Medinan); (b) it
keeps ≥14 surahs per bin so within-bin axis-value means are stable
(CV < 0.3 expected from [[h-new-125-chronology-content|H-NEW-125]] phase-means); (c) it does NOT use
the 4 coarse Nöldeke phases directly (which would make the test
trivial — all 5 Pattern-B axes obviously peak at "Late Meccan" phase
3 out of 4 by [[h-new-125-chronology-content|H-NEW-125]] design).

**Pre-committed**: the HYPOTHESIZED joint peak is B6 (ranks 72–85).
B5 and B7 are within 1-bin tolerance. B1–B4 and B8 are OUTSIDE
tolerance (FAIL if the joint peak lands there).

## Pre-committed analytical cells (three, per Bonferroni k=3)

### Cell A (PRIMARY, inferential) — Kendall's W concordance

**Statistic**: Kendall's coefficient of concordance W over the 5
axes' sub-bin rankings. For each axis, rank the 8 sub-bins by their
mean axis value (highest = rank 1, lowest = rank 8). Kendall's W
measures agreement among the 5 ranking-of-8 profiles.

W ∈ [0, 1]; W = 1 = perfect agreement; W = 1/5 = chance under
5 independent rankings of 8 items.

**Null distribution**: 10,000 permutations. For each perm, shuffle
the per-surah Nöldeke rank (i.e., randomly re-assign surahs to
sub-bins while keeping bin cardinalities fixed). For each perm,
recompute per-axis sub-bin means, re-rank, and compute W. This is
the standard "Nöldeke-agnostic" null.

**P-value**: p = (1 + #{W_perm ≥ W_obs}) / (1 + 10000). **1-sided**
(higher W = more concordance = supports claim).

**Acceptance**: PASS Cell A at p < α_bon = 0.0167.

### Cell A-sensitivity (audit-036 tightening) — 4-axis drop-muq Kendall's W

Mandatory companion statistic: Kendall's W over the 4 axes with
muq_cardinality DROPPED (qul, book-ref, eschat, loanwords). Same
perm null, same α_bon. Reported alongside Cell A regardless of
either's pass/fail state. Per audit-036 inflated-independence
pitfall, this is the **evidentiary-floor** statistic:

- If 4-axis W p < 0.0167 → concordance holds on truly-evidentiary
  axes; Cell A claim robust to definitional-axis removal.
- If 4-axis W p > 0.0167 while 5-axis W passes → muq_cardinality
  is carrying material share of concordance; "joint apparatus"
  claim weakens; interpret as "4 content axes + 1 definitional
  axis co-peaking at Late Meccan," not "5 independent axes
  co-peaking."

This is a TIGHTENING amendment (adds a more-stringent secondary
test; does NOT loosen α); self-verifies per project discipline
(HANDOFF/04-DISCIPLINE.md §"Bonferroni asymmetry rule"). It is
NOT added as a 4th cell with a Bonferroni inflation; it is an
observability-enhancement on Cell A reporting. The Cell A PASS
GATE remains the 5-axis W for compatibility with the scratch-note
hypothesis framing, but the 4-axis W is mandatorily disclosed.

### Cell B (SECONDARY, inferential) — Joint peak-bin argmax

For each of the 5 axes, identify the argmax sub-bin (the sub-bin
with the highest mean axis value). Call this axis's "peak bin".
Let `mode_peak` = the modal peak bin across the 5 axes.

**Pre-committed**: the joint peak passes iff `mode_peak ∈ {B5, B6, B7}`
(Late-Meccan core ± 1 bin tolerance) AND **at least 4 of 5** axes
peak within `{B5, B6, B7}` (1-bin-tolerance-to-the-core).

**Null distribution**: 10,000 permutations of Nöldeke rank (same
shuffling scheme as Cell A). For each perm, count the fraction
of perms where ≥4 axes peak inside `{B5, B6, B7}` AND `mode_peak ∈ {B5, B6, B7}`.

**P-value**: the fraction of perms meeting the above criterion.
**1-sided**. Acceptance at p < 0.0167.

### Cell C (TERTIARY, descriptive) — Peak-bin coordinate disclosure

No p-value gate. Pre-committed descriptive products:
- Per-axis peak bin (5 values)
- Per-axis sub-bin mean table (5 × 8 matrix)
- Joint modal peak bin (one value)
- For the modal peak bin: list the surahs in it, and the mean of
  each of the 5 Pattern-B axes at that bin vs the 7 other bins
- Cross-reference: which classical Nöldeke Late-Meccan sub-period
  does the modal peak bin correspond to (check period names in
  the `revelation-order.csv` `source` column and the per-bin
  Nöldeke rank range)

## MW-5 positive control (locked)

Pick 5 axes known to jointly peak in MEDINAN from [[h-new-125-chronology-content|H-NEW-125]] Pattern A:
`allah_density`, `legal_term_density`, `personal_pronoun_density`,
`mean_verse_length`, `divine_name_density`. These are all 5 MONOTONE-UP
axes whose means in Medinan exceed all 3 Meccan-phase means (per
[[h-new-125-chronology-content|H-NEW-125]] phase-means table). If the pipeline is valid, these 5 axes'
joint peak bin should be B8 (Medinan core, ranks 101–114).

**Acceptance**: positive-control Kendall's W p < 0.0167 AND modal peak
bin = B8. If the positive control FAILS, the pipeline is BROKEN and
Cell A results are invalidated → STOP and report NULL-BROKEN.

## MW-1 length residualization (locked decision)

**NOT APPLIED.** The 5 Pattern-B axes are densities (count / 100
verses), not raw counts. Length is normalised out by construction.
`muq_cardinality` is per-surah structural (0 or letter-count,
length-independent). `loanword_density` and `qul_density` are both
/100 verses. This is the pre-committed choice logged in garden-of-
forking-paths.

## Null distribution (Nöldeke-rank-shuffle, 10K draws)

- For each permutation, randomly permute the 114 Nöldeke ranks
  across the 114 surahs.
- Recompute sub-bin membership using the locked octile breakpoints
  (which are functions of the rank distribution; since the rank
  distribution is 1..114 by construction, breakpoints are constant
  across perms — only surah-to-rank mappings change).
- Recompute per-axis sub-bin means → per-axis rankings → Kendall's W
  and Cell-B joint-peak statistic.
- Seed 20260417; 10,000 perms.

## Bonferroni declaration (locked in frontmatter)

- `bonferroni_k: 3` (Cells A, B, C — but C is descriptive so
  effectively k=2 inferential; we keep k=3 conservatively per
  audit-034 "tightening self-verifies" rule)
- `bonferroni_family: [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]-joint-peak`
- `alpha_bon: 0.0167` (= 0.05 / 3)
- Directional: Late-Meccan-peak specifically (B5/B6/B7 modal); FAIL
  if modal peak lands at B1–B4 or B8
- PASS rule: Cell A p < 0.0167 AND Cell B criterion met
  (mode_peak ∈ {B5, B6, B7} AND ≥4 of 5 axes peak in {B5, B6, B7}).
  BOTH cells must pass for CROSS-FINDING-012 PASS verdict.

## Garden-of-forking-paths (locked BEFORE run)

1. **Octile (8-bin) sub-binning**, not quintile (5-bin) or decile
   (10-bin). Rationale: 8 gives enough resolution across a 114-unit
   rank while keeping ≥14 surahs per bin. 10 would give <12 per bin;
   5 would collapse Late-Meccan (21 surahs) into 1 bin, making the
   test trivial. Locked.
2. **Mean-based (not median-based) sub-bin ranking**. Rationale:
   axis densities are already normalised; means are more sensitive
   to the Late-Meccan peak shape. Medians would de-weight the 2-
   outlier-surah phenomenon for `muq_cardinality` and
   `loanword_density`. Locked.
3. **Kendall's W** over Spearman-pairwise-mean or Friedman χ² as
   the concordance statistic. Rationale: W is the classical choice
   for concordance of m rankings of n items; Friedman χ² is
   equivalent for this n.m configuration (χ² = m(n-1)W) and would
   give the same p. Locked on W for interpretability.
4. **1-sided direction** (higher W = more concordance). Kendall's
   W is naturally non-negative; "lower concordance than chance"
   is not a meaningful direction. Locked.
5. **Peak-bin argmax, not half-max or Gaussian fit**. Rationale:
   the hypothesis is "peaks at the SAME sub-bin"; argmax is the
   direct operationalisation. Half-max or Gaussian would smooth
   and lose the joint-peak localisation. Locked.
6. **1-bin tolerance** (B5, B6, B7), not 0-bin (B6 only) or 2-bin
   (B4–B8). Rationale: 0-bin is too strict given the noisy axis
   estimates; 2-bin is too lax (admits Early-Meccan-adjacent B4 or
   Medinan B8). 1-bin is the middle-ground choice. Locked.
7. **Permutation scheme: surah-to-Nöldeke-rank shuffle**, not
   within-bin resampling or Nöldeke-phase-preserving shuffle.
   Rationale: the null is "no chronological signal"; rank shuffle
   is the exchangeability hypothesis. Phase-preserving would
   under-count null concordance and inflate p-values toward PASS.
8. **Positive-control axes are Pattern-A monotone-up 5**, not
   Pattern-A length 5 or a mixed set. These 5 are the cleanest
   monotone-up set with independent per-H-NEW-125 confirmations.
9. **Axis 3 (`muq_cardinality`) is 0-padded at [[h-new-125-chronology-content|H-NEW-125]] level.**
   This is inherited; we do NOT switch to within-muq-only axis 3
   (which would use n=29 not 114). The 0-padded version is what
   was declared Pattern-B in [[h-new-125-chronology-content|H-NEW-125]]. Locked.
10. **No secondary-null residualization.** Per MW-2, secondary
    nulls require adversarial-flag origin. None has been raised on
    this pre-reg (see auditor-review step below). If auditor
    requests one before run, we add it with the flag origin logged.

## Anti-HARK pre-commitments

- All 5 axes' per-bin means and peak bins reported regardless of
  Cell A/B pass or fail.
- Full Kendall's W distribution summary (mean, SD, 95%CI, 99%CI)
  under the null reported.
- Per-axis peak bin reported (even if it lands at B1 or B8).
- Modal peak bin AND the 2nd/3rd-mode peak bins reported.
- NULL results (if Cell A/B fail) reported with SAME PROMINENCE as
  PASS results, and the interpretation is "Pattern B is not a joint
  apparatus — the 5 axes share the inverted-U shape but not a
  common sub-peak" (i.e., they're correlated on the 4-phase level
  but not the 8-bin level).
- Inflated-independence disclosure section MANDATORY in findings
  file regardless of verdict.

## Expected outcomes (priors, disclosed before run)

Based on [[h-new-125-chronology-content|H-NEW-125]] phase-means:

- All 5 Pattern-B axes have their max-of-4-phases at "Late Meccan"
  ([[h-new-125-chronology-content|H-NEW-125]] Pattern B classification by definition)
- Under an 8-bin refinement, the Late Meccan phase (ranks 70–90)
  spans B5 (58–71) late tail, B6 (72–85) fully, B7 (86–100) early
  portion. Expected modal joint peak bin: B6.
- Expected Kendall's W ≈ 0.6–0.9 (if all 5 axes peak within B5–B7
  and are concordant on rank-order)
- Null W mean ≈ 1/5 = 0.20; 95%ile ≈ 0.40 (rough expectation).
- Expected Cell A p: 10⁻³ to 10⁻⁴ (i.e., below α_bon = 0.0167).
- Expected Cell B: 5 of 5 axes peak in {B5, B6, B7}; mode_peak = B6.
- Expected Cell B p: 10⁻³ to 10⁻⁴.

These priors are disclosed; the actual run is blind to perm numbers.

**Honest expected-fail scenarios**:
- If `muq_cardinality` peaks at B5 (Middle/Late boundary) and the
  other 4 peak at B6, Cell B still passes (4 of 5 in {B5,B6,B7},
  mode B6) but W slightly lower.
- If `loanword_density` peaks at B7 (loanword-Medinan-creep
  hypothesis), Cell B still passes.
- If `qul_density` AND `book_reference_density` peak at B5 while
  the others peak at B6, W may be lower but Cell B still passes.
- If ANY axis peaks at B4 or B8, Cell B may still pass (mode is
  B6 with 4-of-5) but we report the outlier axis honestly.
- Real FAIL scenario: if `loanword_density` peaks at Medinan-core
  B8, `muq_cardinality` at B5, and only 3 axes peak in {B5,B6,B7}
  — NULL Cell B.

## Data + outputs (locked)

- Script: `/Users/grey/Downloads/quran/scripts/cross_finding_012_joint_peak.py`
- JSON:   `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/cross-finding-012.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement.md`
- Journal: `/Users/grey/Downloads/quran/journal/cross-finding-012-run-1.md`

## Auditor review gate

This pre-reg was authored by the SYNTHESIZER and is submitted to the
AUDITOR for review BEFORE script execution. The specialist will DM
the auditor and wait for review; any tightening amendments will be
applied BEFORE run (Bonferroni tightening self-verifies per project
discipline; Bonferroni loosening would require explicit attestation).

## Status

PRE-REGISTERED 2026-04-17, awaiting auditor review before execution.
