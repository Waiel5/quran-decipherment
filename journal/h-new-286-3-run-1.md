# H-NEW-286.3 run journal

Date: 2026-04-19
Operator: codex

## Scope

Run the preregistered outsider-family follow-up to H-NEW-286.2 on the
OQ-18 `Q17` branch.

Question:

> with the nucleus fixed at `{16,21,22,23,25}`, is `Q17` the unique
> best outsider bridge among `{17,18,19,20,24}` under a fixed
> core-plus-bridge Jaccard mask?

## Locked design

- zone fixed to `Q16..Q25`
- core fixed to `{16,21,22,23,25}`
- outsider family fixed to `{17,18,19,20,24}`
- observed bridge of interest fixed to `Q17`
- representation fixed to surah-level QAC root sets
- pair score fixed to set Jaccard
- predicted-high mask fixed to:
  core-core pairs union bridge-core pairs
- primary score fixed to:
  `Delta_bridge(b) = mean_jaccard(predicted_high) - mean_jaccard(other)`
- exact comparison space fixed to the 5 outsider candidates only
- direction fixed to one-sided upper-tail

## Important inferential limit

The outsider family has only 5 admissible candidates, so the minimum
possible one-sided exact upper fraction is:

- `1 / 5 = 0.20`

Therefore this follow-up can establish only:

- exact outsider-family rank
- descriptive unique-best status

It cannot yield an inferential pass at `alpha = 0.05`. This was stated
in the prereg before execution.

## Command run

```bash
python3 scripts/h_new_286_3_oq18_bridge_identity_test.py
```

## Exact outputs

Pre-reg SHA-256:

- `9d7cdcde1c94a4e6b6e01ab2e89a39b60836c6384edaaafa876c338b293f4fbe`

Observed bridge candidate `Q17`:

- mean Jaccard across predicted-high edges = `0.3415968263411155`
- mean Jaccard across other zone pairs = `0.3076007721081613`
- observed `Delta_bridge(Q17) = 0.03399605423295421`

Exact outsider-family result:

- candidate family size = `5`
- exact descending rank = `1 / 5`
- candidates `>=` observed = `1`
- exact upper fraction = `0.2`
- minimum attainable exact upper fraction = `0.2`
- inferential verdict = `NULL`

Family summary:

- family mean = `0.020715104447297218`
- family median = `0.021176192972585384`
- family min = `0.007457427166184971`
- family max = `0.03399605423295421`

Full ranking by `Delta_bridge`:

- `Q17`: `0.03399605423295421`
- `Q20`: `0.02382721893190054`
- `Q18`: `0.021176192972585384`
- `Q24`: `0.01711862893286098`
- `Q19`: `0.007457427166184971`

## Descriptive continuity with H-NEW-286.2

Mean outsider-to-core Jaccard:

- `Q17`: `0.3420193401695428`
- `Q20`: `0.32168166956743544`
- `Q18`: `0.3163796176488051`
- `Q24`: `0.30826448956935626`
- `Q19`: `0.2889420860360043`

Best one-swap replacement of the H-NEW-286.2 core:

- `Q17` replacing `Q21` -> `{16,17,22,23,25}`,
  `Delta_pair = 0.0346190439274357`,
  gain `+0.005751184903178219`
- `Q20` replacing `Q22` -> gain `-0.0053330505140048445`
- `Q18` replacing `Q21` -> gain `-0.0060329716216681595`
- `Q24` replacing `Q25` -> gain `-0.010408884405717134`
- `Q19` replacing `Q21` -> gain `-0.021569500309954692`

Only `Q17` improves the parent H-NEW-286.2 core statistic.

## Continuity note

This follow-up does exactly what it should do and no more.

- It sharpens the H-NEW-286.2 leak story into a direct bridge-identity
  comparison.
- It confirms that `Q17` is the unique best outsider bridge around the
  locked nucleus.
- It does not over-claim significance where the exact family size makes
  significance impossible.

So the honest read is:

- descriptive identity claim: `Q17` is the unique best outsider bridge
- inferential claim: `NULL`

## Files written

- `findings/phase-b-hypotheses/h-new-286-3-q17-bridge-identity-test-prereg.md`
- `scripts/h_new_286_3_oq18_bridge_identity_test.py`
- `findings/phase-b-hypotheses/csv/h-new-286-3.json`
- `findings/phase-b-hypotheses/h-new-286-3-q17-bridge-identity-test.md`
- `journal/h-new-286-3-run-1.md`
