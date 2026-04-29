# H-NEW-286.2 run journal

Date: 2026-04-19
Operator: codex

## Scope

Run the preregistered conditioned exact-null follow-up to H-NEW-286.1 on
the OQ-18 `Q17` leak branch.

Question:

> under the same pairwise `Delta_pair` statistic used in H-NEW-286.1,
> does the locked nucleus `{16,21,22,23,25}` become the exact optimum
> once `Q17` is excluded from the positive side?

## Locked design

- zone fixed to `Q16..Q25`
- target nucleus fixed to `{16,21,22,23,25}`
- conditioned exclusion fixed to `Q17`
- representation fixed to surah-level QAC root sets
- pair score fixed to set Jaccard
- primary statistic fixed to
  `Delta_pair(S) = mean_jaccard(++) - mean_jaccard(other pairs)`
- primary null fixed to all `C(9,5) = 126` admissible five-surah subsets
  excluding `Q17`
- direction fixed to one-sided upper-tail

## Exact outputs

Observed assignment:

- target positive set = `{16, 21, 22, 23, 25}`
- mean Jaccard across `++` pairs = `0.34138556942690185`
- mean Jaccard across `+-` pairs = `0.3154574405982288`
- mean Jaccard across `--` pairs = `0.30516838491368325`
- mean Jaccard across `other` pairs = `0.31251771040264437`
- observed `Delta_pair(S*) = 0.02886785902425748`

Conditioned exact-null result:

- conditioned exact space size = `126`
- exact rank = `1 / 126`
- assignments `>=` observed = `1`
- exact upper-tail `p = 0.007936507936507936`
- conditioned null mean = `-0.004939076660072468`
- conditioned null median = `-0.006061755410743996`
- conditioned null min = `-0.03169181948860378`
- conditioned null max = `0.02886785902425748`
- verdict = `PASS-DIRECTED`

Reference to the parent full-space result from H-NEW-286.1:

- full-space exact rank = `8 / 252`
- full-space exact upper-tail `p = 0.031746031746031744`
- strictly better full-space assignments = `7`
- strictly better `Q17`-excluded assignments = `0`
- strictly better `Q17`-included assignments = `7`

## Descriptive bridge note

Outsider best single-swap comparisons versus the locked nucleus:

- `Q17` best swap: replace `Q21` ->
  `{16,17,22,23,25}`, `Delta_pair = 0.0346190439274357`,
  gain `+0.005751184903178219`
- `Q20` best swap: replace `Q22` ->
  `{16,20,21,23,25}`, `Delta_pair = 0.023534808510252636`,
  gain `-0.0053330505140048445`
- `Q18` best swap: replace `Q21` ->
  `{16,18,22,23,25}`, `Delta_pair = 0.02283488740258932`,
  gain `-0.0060329716216681595`
- `Q24` best swap: replace `Q25` ->
  `{16,21,22,23,24}`, `Delta_pair = 0.018458974618540347`,
  gain `-0.010408884405717134`
- `Q19` best swap: replace `Q21` ->
  `{16,19,22,23,25}`, `Delta_pair = 0.007298358714302788`,
  gain `-0.021569500309954692`

Only `Q17` improves the target statistic.

## Continuity note

This resolves the H-NEW-286.1 leak observation in the strongest bounded
way available without changing the instrument.

The honest read is:

- the OQ-18 pairwise nucleus is stable
- the residual mismatch is not distributed across the whole complement
- `Q17` is the unique bridge/leak surah inside `Q16..Q25`

Because the `Q17` branch was opened from the H-NEW-286.1 result, the
verdict ceiling stays at `PASS-DIRECTED`.

## Files written

- `findings/phase-b-hypotheses/h-new-286-2-q17-conditional-bridge-test-prereg.md`
- `scripts/h_new_286_2_oq18_q17_conditional_bridge_test.py`
- `findings/phase-b-hypotheses/csv/h-new-286-2.json`
- `findings/phase-b-hypotheses/h-new-286-2-q17-conditional-bridge-test.md`
- `journal/h-new-286-2-run-1.md`
