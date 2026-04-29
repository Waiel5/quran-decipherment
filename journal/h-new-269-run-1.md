# H-NEW-269 Run 1 — qul imperative addressee-pattern test

**Date**: 2026-04-18  
**Agent**: h-new-269-specialist  
**Seed**: 20260418  
**N_PERM**: 5,000  
**Bonferroni**: `k = 4`, `alpha_bon = 0.0125`  
**Verdict**: `PARTIAL-CLASS-ONLY`  
**Pre-reg SHA-256**: `f00d81df4b7808d35f8f06a8fcd4e41af9994341cc849758697ce1e71efef322`

## Task

Land H-NEW-269 as a conservative formal test of whether the 332
canonical `qul` imperatives contain distinct addressee or
rhetorical-context classes **beyond raw opener frequency**.

The brief explicitly asked to keep it bounded and empirical. I therefore
avoided full discourse parsing and locked a small opener-family test.

## Locked design

### Corpus and unit

- unit = individual canonical `qul` tokens
- total = **332** tokens across **306** verses
- filter = `POS:V`, `IMPV`, `LEM:qaAla`, `2MS`

### Four inferential classes

1. `VOCATIVE_ADDRESS`
   first token after `qul` = `يا`; strip `يا`, and strip `ايها` too if
   immediately following
2. `INTERROGATIVE_OR_CHALLENGE`
   first token after `qul` in `{من, ما, هل, ارايتم, ارايتكم, هاتوا,
   فاتوا, اغير, افلا}`; strip first token
3. `SELF_OR_DEVOTIONAL`
   first token after `qul` in `{اني, انني, انا, رب, ربي, اعوذ, اللهم,
   حسبي}`; strip first token
4. `RESTRICTIVE_DECLARATION`
   first token after `qul` = `انما`; strip first token

Residual representation:

- next up to **6 words** after stripping
- convert those words to a **set of QAC STEM roots**
- statistic = mean pairwise Jaccard within class

Null:

- same-size matched sets drawn from non-class `qul` tokens
- match on residual 6-word STEM-token mass
- candidate neighborhood = nearest `max(40, 2 * n_class)`
- sampling without replacement

### MW-5

Feasible positive control:

- `qul a-ra'aytum / a-ra'aytakum ...`

Same residual-root Jaccard statistic, same mass-matched null.

## Implementation notes

Created:

- `scripts/h_new_269_qul_addressee_pattern.py`
- `findings/phase-b-hypotheses/h-new-269-qul-addressee-pattern-prereg.md`
- `findings/phase-b-hypotheses/csv/h-new-269.json`
- findings markdown
- this journal

No non-owned files touched.

One honest implementation note:

- an early exploratory sampler with too-small candidate neighborhoods
  was not viable for the 55-token interrogative class under
  no-replacement matching
- before the locked run, the prereg fixed the final rule
  `candidate_pool_k = max(40, 2 * n_class)`
- the locked script and the reported JSON both use that rule

## Results

### Corpus frame

- inferential-class coverage = **117 / 332** tokens (**35.2%**)
- `OTHER` residue = **215 / 332** tokens (**64.8%**)

### Bonferroni family

| Cell | n | Observed | Null mean | z | p_perm | Verdict |
|---|---:|---:|---:|---:|---:|---|
| `VOCATIVE_ADDRESS` | 16 | 0.0442 | 0.0387 | +0.317 | 0.3221 | NULL |
| `INTERROGATIVE_OR_CHALLENGE` | 55 | 0.0372 | 0.0394 | -0.288 | 0.5767 | NULL |
| `SELF_OR_DEVOTIONAL` | 27 | 0.0249 | 0.0410 | -1.286 | 0.9256 | NULL |
| `RESTRICTIVE_DECLARATION` | 19 | **0.1142** | 0.0406 | **+4.879** | **0.0008** | **PASS** |

Pass count = **1 / 4**.

### MW-5

| Control | n | Observed | Null mean | z | p_perm | Verdict |
|---|---:|---:|---:|---:|---:|---|
| `ARAYTUM` family | 13 | **0.1596** | 0.0409 | **+6.622** | **0.0002** | PASS |

MW-5 passed, so the family verdict is interpretable.

## Readout

The run gives a narrow positive and a broad negative:

- **Positive**: `qul innama ...` is a real residual class beyond opener
  frequency.
- **Negative**: the more visible `ya ...`, interrogative/challenge, and
  self/devotional families do not survive the same stricter test.

The key surviving pair inside the restrictive class is:

- **Q 18:110 ↔ Q 41:6**, residual Jaccard = **1.00**

after stripping `innama`.

So this does not support a strong claim that the `qul` corpus has a
stable many-class addressee taxonomy. It supports one narrower claim:

- the restrictive / exclusivizing `innama` register is a coherent
  sub-family

## Interpretation

This is the right conservative landing:

- opener families are easy to see descriptively
- but "I can count repeated openers" is weaker than
  "the opener family stays coherent after I remove the opener"
- under that stricter standard, only one of the four locked families
  survives

Hence the verdict:

- `PARTIAL-CLASS-ONLY`

## Files produced

1. `scripts/h_new_269_qul_addressee_pattern.py`
2. `findings/phase-b-hypotheses/h-new-269-qul-addressee-pattern-prereg.md`
3. `findings/phase-b-hypotheses/h-new-269-qul-addressee-pattern.md`
4. `findings/phase-b-hypotheses/csv/h-new-269.json`
5. `journal/h-new-269-run-1.md`
