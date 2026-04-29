# h-new-267-run-1

**Date**: `2026-04-18`  
**Task**: land `H-NEW-267`, a formal Mecca-Medina vocabulary frontier test  
**Outcome**: **PASS-DIRECTED**  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier-prereg.md`  
**Pre-reg SHA-256**: `554bfb1f4ee27f6d4febf3ad4f62ca8d660892a6a1d5ad8d21c8e7f203eb265a`

## Scope kept tight

Per task steer, I only touched the five owned files:

- `scripts/h_new_267_mecca_medina_vocabulary_frontier.py`
- `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier-prereg.md`
- `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier.md`
- `findings/phase-b-hypotheses/csv/h-new-267.json`
- `journal/h-new-267-run-1.md`

No unrelated repo files were changed.

## Locked design

- Data: `surah-root-graph.json` QAC STEM-root counts + `revelation-order.csv`
- Primary pool: `Late Meccan (21)` vs `Medinan (24)`
- Split rule: alternating by `noldeke_order` within each side
- Cell A: train on split A, test on split B AUC
- Cell B: train on split B, test on split A AUC
- Cell C: split-half root-log-odds Spearman on the locked support rule
  `>=10` pooled tokens and `>=2` surahs per side
- Null: 5000 label shuffles on the fixed 45-surah pool preserving `21 / 24`
- Bonferroni family: `k=3`, `alpha_bon=0.0166667`
- MW-5: same instrument on the broader `Meccan (86)` vs `Medinan (28)` split
  with 1000 label shuffles

## Exploratory disclosure

Before writing the prereg, I prototyped several candidate frontier summaries on
the same source data to avoid locking a metric that was mechanically useless.
The final held-out log-odds scorer family was chosen after that feasibility
stage, then frozen in the prereg, then run in production.

That is why the findings file uses the verdict ceiling `PASS-DIRECTED` rather
than `CONFIRMED`.

## Execution

I wrote the prereg first, then implemented the production script, then ran:

```bash
python3 scripts/h_new_267_mecca_medina_vocabulary_frontier.py
```

The first production run completed cleanly. I then corrected a spelling typo in
the prereg metadata (`Noldake` -> `Noldeke`), reran the script once to refresh
the prereg SHA and final JSON, and did not change the analysis logic.

No code-level blockers or rerun-for-bug reasons occurred.

## Result

### Primary family

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Train A -> test B AUC | **1.000000** | 0.700000 | **0.0002** | **PASS** |
| Train B -> test A AUC | **1.000000** | 0.689394 | **0.0002** | **PASS** |
| Split-weight Spearman rho | **0.457673** | 0.104450 | **0.0002** | **PASS** |

Overall verdict: **PASS-DIRECTED**.

The held-out score gaps were also clean:

- `gap_A->B = 0.105421`
- `gap_B->A = 0.090290`

So the two sides did not overlap under the locked split.

### MW-5

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Train A -> test B AUC | **0.901993** | 0.659468 | **0.0010** | **PASS** |
| Train B -> test A AUC | **0.853821** | 0.666113 | **0.0010** | **PASS** |
| Split-weight Spearman rho | **0.513728** | 0.096997 | **0.0010** | **PASS** |

MW-5 passed all 3 cells, so the instrument is not broken.

## Descriptive notes worth carrying forward

- Adjacent-boundary mean held-out AUCs:
  - Early -> Middle: `0.906250`
  - Middle -> Late: `0.965868`
  - Late -> Medinan: `1.000000`
- I did **not** promote that three-boundary ranking to extra inference.
- Locked support set for root localization ended up at `434` roots.

Broad high-mass shifts:

- `Alh` `+0.047716`
- `Amn` `+0.015118`
- `qwl` `-0.014822`
- `rbb` `-0.010194`
- `Ayy` `-0.009053`

Sharper stable roots:

- toward Medinan: `Avm`, `nfq`, `nsw`, `mwl`, `qtl`
- toward Late Meccan: `flk`, `jrm`, `$ms`, `wHy`, `fry`

## Limits logged during run

- The scorer family is a formal lock-down after feasibility checking, not a
  blind discovery.
- The chronology target is the Noldeke phase assignment.
- Surah is the unit; no verse-level frontier claim should be imported.
- Root tables are descriptive localizers under a locked support rule, not extra
  significance tests.

## Files shipped

- `scripts/h_new_267_mecca_medina_vocabulary_frontier.py`
- `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier-prereg.md`
- `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier.md`
- `findings/phase-b-hypotheses/csv/h-new-267.json`
- `journal/h-new-267-run-1.md`
