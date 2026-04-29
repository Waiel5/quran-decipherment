# [[h-new-272-mixed-hard-soft-completion|H-NEW-272]] - Mixed hard-soft completion on the OQ-15 parsimony frontier: pre-registration

```yaml
finding_id: h-new-272
title: "Mixed hard-soft completion at the OQ-15 frontier - can the real lambda 0.07 soft sweet spot be completed by the exact 95->100 tranche or the smallest overlap complement?"
parent: h-new-236-1h / h-new-236-1g
grandparent: h-new-236-1e / h-new-236-1d -> h-new-236-1a -> h-new-236-1 -> h-new-236 -> cross-finding-020
date: 2026-04-18
specialist: autonomous (H-NEW-272)
seed: 20260421
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kufan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-50-HINGE-BASELINE + SOFT-TERMINAL-PREFERENCE-PENALTY lambda=0.07 + LOCKED-HARD-COMPLEMENT, seed 20260421)"
bonferroni_k: 2
alpha_family: 0.05
alpha_bon: 0.025
cells:
  - cell_a_lambda0p07_plus_exact_tranche
  - cell_b_lambda0p07_plus_overlap_pair
n_simulations: 1000
n_random_null: 1000
positive_control:
  cell: mw5_positive_control_lambda0p07_soft_only
  seed_offset: 70000
```

## 1. Motivation

[[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] established a real but incomplete soft result:

- on the locked fine grid, `lambda = 0.07` was the only cell that reached the
  pre-registered primary target
- that cell still failed strict closure because empirical `L_tail_91_114`
  remained just outside low

[[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] established a complementary hard result:

- the exact decisive `95->100` five-edge tranche has real local causal bite
- but in hard-only direct form it does not repair the global residual

That leaves one narrow next question worth testing without reopening search:

> if the real `lambda = 0.07` soft sweet spot is already almost complete, can a
> tiny locked hard complement finish the job?

This finding attacks exactly that question and nothing broader.

## 2. Hypothesis

**H0:** fixing the [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] soft sweet spot at `lambda = 0.07`, neither the
exact decisive five-edge tranche nor the smallest direct overlap complement
converts the parent primary-only pass into strict closure.

**H1:** at least one of the two locked mixed cells preserves the parent primary
pass and also brings empirical `L_tail_91_114` inside, yielding strict closure.

Primary preservation criterion per cell:

- empirical `L_path` inside sim 95% CI
- empirical `L_mufassal_short` inside sim 95% CI

Strict completion criterion per cell:

- primary preservation criterion satisfied
- plus empirical `W_wrap` inside sim 95% CI
- plus empirical `Block-chi2` inside sim 95% CI
- plus empirical `L_tail_91_114` inside sim 95% CI

## 3. Locked parent state

The parent soft baseline is fixed and not re-searched:

- base hard scaffold = [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 canonical consecutive-edge set
- soft family = exact [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] / [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] rhyme + liturgical preference
  family
- lambda fixed at `0.07`

Parent target cell to be reproduced by the positive control:

- [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] `cell_b_lambda_0p07`
- verdict `SOFT-CLOSES-PRIMARY`
- strict closure absent because `L_tail_91_114` remains just outside low

No lambda sweep is allowed here.

## 4. Locked hard complements

Only two inferential cells are permitted.

### 4.1 Cell A - exact decisive tranche

Add the exact [[h-new-236-1d-minimal-k-bracket|H-NEW-236.1d]] / [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] decisive hard tranche:

- `92-93`
- `99-100`
- `100-101`
- `101-102`
- `109-110`

Cell name:

- `cell_a_lambda0p07_plus_exact_tranche`

### 4.2 Cell B - smallest overlap complement

Add only the [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]] overlap subset:

- `92-93`
- `109-110`

Cell name:

- `cell_b_lambda0p07_plus_overlap_pair`

Why this is the only alternative tiny complement allowed:

- it is already pre-separated inside [[h-new-236-1g-direct-tranche-test|H-NEW-236.1g]]
- it is the smallest direct component extracted from the decisive tranche
- both edges overlap the existing soft preference family (`92-93` rhyme;
  `109-110` liturgical), making it the cleanest mixed hard-soft completion test

## 5. Forbidden expansions

The following are explicitly forbidden in this finding:

- no new lambda values
- no core-triple cell `(99,100)/(100,101)/(101,102)`
- no cumulative prefix additions
- no new hard edges outside the two locked complements above
- no expansion of the rhyme or liturgical soft families
- no adaptive follow-up cells after seeing outcomes

## 6. Positive control

The positive control re-runs the exact [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] parent sweet-spot cell
through the new mixed-code path with **no added hard complement**:

- cell `mw5_positive_control_lambda0p07_soft_only`
- seed offset `70000`
- same top-50 scaffold
- same `lambda = 0.07`
- same shared random null

It must reproduce the parent [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] `cell_b_lambda_0p07` verdict and the
sim means for:

- `L_path`
- `W_wrap`
- `L_mufassal_short`
- `L_tail_91_114`

within absolute drift `<= 1e-9`.

If this fails, the run is instrument-broken and no inferential read is allowed.

## 7. Generative procedure

Everything is inherited from [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] / [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]] except the two added
hard complements.

Locked details:

1. Base hard scaffold: [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 canonical consecutive edges.
2. Fixed soft penalty: `lambda = 0.07`.
3. Soft family unchanged:
   - [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] rhyme pairs
   - [[h-new-236-1e-soft-terminal-penalties|H-NEW-236.1e]] liturgical pairs
   - overlap weights additive as before
4. SA schedule unchanged:
   - `T_HOT = 0.05`
   - `T_COLD = 0.001`
   - `SA_ITERS = 200`
5. `N_sim = 1000` per cell.
6. Shared `N_random = 1000` null.
7. Seed base inherited from [[h-new-236-1h-fine-soft-band|H-NEW-236.1h]]: `20260421`.
8. Inferential seed offsets are fixed before execution:
   - Cell A exact tranche: `170000`
   - Cell B overlap pair: `270000`

## 8. Observables

Primary target observables:

- `L_path`
- `L_mufassal_short`

Strict completion observables:

- `W_wrap`
- `Block-chi2`
- `L_tail_91_114`

Additional diagnostics:

- weighted preference satisfaction
- rhyme-pair satisfaction count
- liturgical-pair satisfaction count
- sim-mean drift versus the parent `lambda = 0.07` cell

## 9. Interpretation rules

Per inferential cell:

| Outcome | Verdict |
|---|---|
| primary preserved and strict completion achieved | `MIXED-COMPLETES-STRICT` |
| primary preserved but strict completion still fails | `MIXED-PRESERVES-PRIMARY-ONLY` |
| `L_mufassal_short` inside but `L_path` outside | `MIXED-PARSIMONY-CONFLICT` |
| `L_path` inside but `L_mufassal_short` outside | `MIXED-LOCAL-FAIL` |
| both primary observables fail | `MIXED-BROKEN` |

Overall decision:

- if any inferential cell reaches `MIXED-COMPLETES-STRICT`, the mixed
  hard-soft completion story is confirmed for the tested complements
- else if any inferential cell reaches `MIXED-PRESERVES-PRIMARY-ONLY`, the hard
  add-on does not complete the frontier but also does not destroy the soft sweet
  spot
- else the tested tiny mixed completion route fails

## 10. Bonferroni discipline

Only the two inferential cells count toward the family:

- `k = 2`
- `alpha_bon = 0.05 / 2 = 0.025`

The positive control is excluded from the inferential family.

## 11. Honest limits

1. This is not a general mixed-model search.
2. A negative result only rules out these two locked tiny complements at fixed
   `lambda = 0.07`.
3. A positive result would still not imply that hard-only repair was sufficient;
   it would imply specifically that the soft sweet spot needed a small hard
   completion.
