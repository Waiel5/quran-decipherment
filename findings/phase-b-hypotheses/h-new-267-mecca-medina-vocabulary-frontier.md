# [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]] - Mecca-Medina vocabulary frontier test

**Finding ID**: `[[h-new-267-mecca-medina-vocabulary-frontier|h-new-267]]`  
**Date**: `2026-04-18`  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-267-mecca-medina-vocabulary-frontier-prereg.md`  
**Pre-reg SHA-256**: `554bfb1f4ee27f6d4febf3ad4f62ca8d660892a6a1d5ad8d21c8e7f203eb265a`  
**Seed**: `20260418`  
**Rules tuple**: `(QAC v0.4 STEM roots via surah-root-graph.json; Late Meccan vs Medinan pool from revelation-order.csv Noldeke phases; alternating split-halves by Noldeke rank within phase; Dirichlet-0.5 pooled log-odds scorer; held-out AUC cells; root-localizer support rule >=10 pooled tokens and >=2 surahs per side; Hafs-Kufan)`  
**Bonferroni**: `k=3`, `alpha_bon=0.0166667`, `N_perms=5000`  
**Verdict**: **PASS-DIRECTED**

## Headline

On the locked split-half root-log-odds instrument, the
**Late-Meccan -> Medinan transition is a reproducible lexical frontier**.

All 3 preregistered cells pass:

- train on one half, test on the other: **AUC = 1.000**
- swap halves: **AUC = 1.000**
- split-half root-weight replication: **Spearman rho = 0.458**

The MW-5 easier-control boundary, broad **Meccan vs Medinan**, also passes all
3 cells. So this is not a null-breaking artifact of the scorer.

This is still a **bounded** positive result. It shows a reproducible root-level
partition at the Hijra boundary under this instrument. It does **not** prove
that the Hijra is the only chronological frontier or that roots alone capture
the full historical transition.

## Primary numbers

### Bonferroni family (3 cells, alpha_bon = 0.0166667)

| Cell | Observed | Null mean | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---:|---|
| Train A -> test B AUC | **1.000000** | 0.509480 | 0.700000 | **0.0002** | **PASS** |
| Train B -> test A AUC | **1.000000** | 0.509376 | 0.689394 | **0.0002** | **PASS** |
| Split-weight Spearman rho | **0.457673** | -0.037535 | 0.104450 | **0.0002** | **PASS** |

Interpretation:

- The held-out scorer does not merely beat chance. It **perfectly separates**
  the two sides of the transition in both split directions.
- The learned root-weight vectors are not arbitrary. Across the locked support
  set of **434 roots**, the two split-half weight vectors correlate at
  `rho = 0.458`, far above the null.
- The held-out score ranges do not overlap:
  `gap_A->B = 0.105421`, `gap_B->A = 0.090290`.

Those score gaps matter because they show the result is not being carried by
one or two borderline surahs. Under this locked split, the frontier is clean.

## MW-5 positive control

MW-5 used the same scorer on the broader **Meccan vs Medinan** split. All 3
control cells pass at the same Bonferroni threshold.

| Cell | Observed | Null q95 | p_perm | Verdict |
|---|---:|---:|---:|---|
| Train A -> test B AUC | **0.901993** | 0.659468 | **0.0010** | **PASS** |
| Train B -> test A AUC | **0.853821** | 0.666113 | **0.0010** | **PASS** |
| Split-weight Spearman rho | **0.513728** | 0.096997 | **0.0010** | **PASS** |

So the instrument behaves normally on an easier, broader period boundary. The
primary positive result is therefore interpretable.

## Descriptive boundary ranking

These numbers are **descriptive only**. They do not consume extra Bonferroni
slots.

| Adjacent boundary | Mean held-out AUC | Split-weight rho |
|---|---:|---:|
| Early Meccan -> Middle Meccan | 0.906250 | 0.331475 |
| Middle Meccan -> Late Meccan | 0.965868 | 0.262604 |
| **Late Meccan -> Medinan** | **1.000000** | **0.457673** |

The Hijra boundary is descriptively the strongest of the three adjacent
phase-boundary separations on this metric. I do **not** promote that ranking as
an extra inferential claim inside [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]], because it was not in the locked
three-cell family.

## Which roots shift most sharply

Two descriptive lenses are useful here:

1. **Stable log-odds roots** identify the roots whose directional shift is
   sharp and reproducible across both split-halves.
2. **Absolute mean-density shifts** identify broad high-mass roots whose usage
   moves a lot even if their log-odds are less extreme.

### Sharp stable roots toward Medinan

| Root | Stable score | Full log-odds | Late tok | Med tok | Delta mean density |
|---|---:|---:|---:|---:|---:|
| `Avm` | **1.779882** | 1.737684 | 5 | 34 | +0.000704 |
| `nfq` | **1.776165** | 2.129950 | 10 | 97 | +0.006122 |
| `nsw` | **1.664369** | 1.683380 | 8 | 50 | +0.001762 |
| `mwl` | **1.640769** | 1.759607 | 8 | 54 | +0.002189 |
| `jnH` | **1.547906** | 1.962896 | 3 | 27 | +0.000687 |
| `qtl` | **1.547906** | 1.775150 | 20 | 133 | +0.004259 |

These are the clearer later-shift markers on this instrument: hypocrisy,
combat, and community-regulatory vocabulary surface strongly.

### Sharp stable roots toward Late Meccan

| Root | Stable score | Full log-odds | Late tok | Med tok | Delta mean density |
|---|---:|---:|---:|---:|---:|
| `flk` | **1.841789** | -1.784926 | 13 | 2 | -0.000858 |
| `jrm` | **1.702468** | -2.163982 | 35 | 4 | -0.002029 |
| `$ms` | **1.573525** | -1.856385 | 14 | 2 | -0.000863 |
| `wHy` | **1.558174** | -1.833128 | 42 | 7 | -0.002099 |
| `fry` | **1.386917** | -1.901336 | 45 | 7 | -0.001681 |
| `swE` | **1.348901** | -1.360769 | 26 | 7 | -0.001642 |

These lean more toward proclamation, accusation, and eschatological-rhetorical
material characteristic of the late Meccan side.

### Broad high-mass density shifts

The biggest full-pool mean-density moves are not always the sharpest
log-odds roots, because very common roots can move a lot in density while still
remaining common on both sides. The clearest examples are:

- `Alh`: `+0.047716` toward Medinan
- `Amn`: `+0.015118` toward Medinan
- `qwl`: `-0.014822` toward Late Meccan
- `rbb`: `-0.010194` toward Late Meccan
- `Ayy`: `-0.009053` toward Late Meccan

So the frontier has **two layers**:

- a broad common-root drift (`Alh`, `Amn`, `qwl`, `rbb`)
- and a sharper, more specific root frontier (`nfq`, `qtl`, `wHy`, `fry`, `jrm`)

## Interpretation

The conservative reading is:

- there is a real, reproducible lexical partition at the
  **Late-Meccan -> Medinan** boundary in root space;
- the partition survives **held-out testing in both directions**;
- the underlying root-weight ranking is itself reproducible;
- and the roots that move are historically interpretable in the expected
  direction: broader community and legal-conflict vocabulary on the Medinan
  side, stronger proclamation/argumentation and eschatological rhetoric on the
  Late-Meccan side.

What I would **not** claim from [[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]:

- that the Hijra frontier is the only or universally strongest frontier under
  every metric,
- that chronology can be reduced to a single lexical axis,
- or that the root tables by themselves establish semantic causality.

## Honest limits

- The scorer family was chosen **after feasibility prototyping** and then
  locked before the production run. This is why the verdict ceiling is
  `PASS-DIRECTED`, not `CONFIRMED`.
- Phase labels come from the **Noldeke chronology**, which is a scholarly
  reconstruction rather than directly observed metadata.
- Surah is the unit. Verse-level and passage-level transition structure may be
  more graded than the surah-level frontier suggests.
- Root IDs are Buckwalter-style QAC root labels. They collapse multiple surface
  forms and do not capture phraseology or syntax.
- The sharp-root tables use a locked support rule
  (`>=10` pooled tokens, `>=2` surahs per side). They are localization aids,
  not extra inferential tests.

## Bottom line

`[[h-new-267-mecca-medina-vocabulary-frontier|H-NEW-267]]` lands as **PASS-DIRECTED**.

The Hijra transition is recoverable as a **clean held-out lexical frontier** in
QAC STEM-root space:

- `AUC_A->B = 1.000`
- `AUC_B->A = 1.000`
- `rho_split_weights = 0.458`
- MW-5 broad Meccan/Medinan control = **PASS**

The roots shifting most sharply are not only the broad common ones like
`Alh` and `Amn`, but also a sharper stable band including
`nfq`, `qtl`, `nsw`, `mwl` on the Medinan side and
`wHy`, `fry`, `jrm`, `$ms` on the Late-Meccan side.
