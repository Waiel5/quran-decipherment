---
id: H-NEW-286-4
title: Q17-conditioned eschatological bridge-bundle exact test
phase: B
status: PRE-REGISTERED (locked before run)
date: 2026-04-19
agent: codex
parent_1: H-NEW-286-3
parent_2: H-NEW-287
parent_3: H-NEW-125
open_question: OQ-18 mechanism inside the true-isolate core plus Q17 bridge
bonferroni_family: h-new-286-4-q17-conditioned-eschatological-bridge-bundle
bonferroni_k: 1
alpha: 0.05
alpha_bon: 0.05
rules_tuple: "(H-NEW-125 per-surah eschatological_density reused from findings/phase-b-hypotheses/csv/h-new-125.json; z-score computed across all 114 surahs using population mean and population standard deviation; exact within-zone enumeration over all C(10,6)=210 six-surah subsets of Q16..Q25; target bundle fixed to B*={Q16,Q17,Q21,Q22,Q23,Q25}; primary statistic Delta_E(S)=mean_{q in S} z_eschat(q)-mean_{q in Z\\S} z_eschat(q); one-sided upper-tail exact null)"
direction_primary: "determine whether the fixed core-plus-Q17 bridge bundle is unusually eschatology-loaded relative to all other 6-of-10 bundles inside Q16..Q25"
---

# [[h-new-286-4-q17-conditioned-eschatological-bridge-bundle|H-NEW-286.4]] - Q17-conditioned eschatological bridge-bundle exact test

## Question

`[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]]` and `[[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]]` localized the residual OQ-18 leak to `Q17`.

- `[[h-new-286-2-q17-conditional-bridge-test|H-NEW-286.2]]` showed that the best one-swap bridge out of the locked core
  `{Q16,Q21,Q22,Q23,Q25}` is specifically `Q17`
- `[[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]]` then showed that under the fixed bridge model, `Q17` is the
  unique rank-1 outsider bridge, though the 5-candidate family is too small
  for an inferential pass
- `[[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]]` showed that one obvious compact three-axis semantic blend points
  the wrong way and does not explain the nucleus

This finding asks a narrower mechanistic question:

> If the fixed bridge bundle is taken seriously as
> `B* = {Q16,Q17,Q21,Q22,Q23,Q25}`, is that exact 6-surah bundle unusually
> elevated on the already-locked `[[h-new-125-chronology-content|H-NEW-125]]` `eschatological_density` axis
> relative to all other `6-of-10` bundles inside `Q16..Q25`?

This is a bridge-bundle mechanism test, not a new composite search.

## Locked zone and target

Define the fixed zone:

`Z = {Q16,Q17,Q18,Q19,Q20,Q21,Q22,Q23,Q24,Q25}`

Define the fixed target bridge bundle:

`B* = {Q16,Q17,Q21,Q22,Q23,Q25}`

Define the complement:

`Z \\ B* = {Q18,Q19,Q20,Q24}`

## Locked axis

Reuse only the landed `[[h-new-125-chronology-content|H-NEW-125]]` per-surah axis:

- `eschatological_density`

No new ontology, no new content composite, and no retuning are permitted.

## Standardization

For each surah `q`, define:

`E_q = z(eschatological_density_q)`

where the z-score is computed over all 114 surahs using:

- population mean
- population standard deviation

This keeps the scale identical to the already-landed `[[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]]` style of
within-zone exact comparison.

## Primary statistic

For any six-surah subset `S ⊂ Z`, define:

`Delta_E(S) = mean_{q in S} E_q - mean_{q in Z \\ S} E_q`

Interpretation:

- larger `Delta_E(S)` means the six-surah subset is more
  eschatology-loaded than its four-surah within-zone complement

Observed statistic:

`Delta_E(B*)`

## Null

Exact within-zone enumeration:

- enumerate all `C(10,6) = 210` six-surah subsets of `Z`
- compute `Delta_E(S)` for every subset

Primary one-sided upper-tail:

`p_exact = #{S : Delta_E(S) >= Delta_E(B*)} / 210`

Report also:

- `rank_desc = 1 + #{S : Delta_E(S) > Delta_E(B*)}`
- exact-space mean, median, minimum, maximum
- top ranked six-surah subsets for context

## Decision rule

Because the target bundle is inherited from prior OQ-18 work rather than
discovered in this test, the strictest honest ceiling is:

- `PASS-DIRECTED` iff `p_exact < 0.05`
- `NULL` otherwise

## Why this test

This is the cleanest next mechanism probe after `[[h-new-286-3-q17-bridge-identity-test|H-NEW-286.3]]` because:

1. it directly tests the bridge bundle rather than the old 5-surah core alone
2. it uses a single already-landed interpretable axis
3. it preserves exact within-zone boundedness
4. it avoids inventing a new weighted content blend after `[[h-new-287-oq18-within-zone-three-axis-content-composite|H-NEW-287]]` failed

## Honest limits

1. This is a single-axis mechanism test, not a full explanation of OQ-18.
2. The bridge bundle is inherited from earlier findings, so even a pass is
   directional rather than discovery-clean.
3. The exact null is within-zone only; it does not speak to corpus-wide
   rarity.
4. A non-maximal but significant rank would still matter: the claim is
   unusual elevation, not necessarily exact top-1 status.

## Deliverables

- Script: `scripts/h_new_286_4_q17_conditioned_eschatological_bridge_bundle.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-286-4.json`
- Findings: `findings/phase-b-hypotheses/h-new-286-4-q17-conditioned-eschatological-bridge-bundle.md`
- Journal: `journal/h-new-286-4-run-1.md`
