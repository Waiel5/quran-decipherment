---
id: H-NEW-150
title: Liturgical prominence ↔ cluster-network hub-degree
phase: B
status: WEAK-LINK (primary PASS; secondary FAIL under length-residualization)
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [cross-finding-010, h-new-146]
seed: 20260417
rules_tuple: "(114 surahs Hafs-Kūfan; cluster-network from cross-finding-010; liturgical-prominence score locked in pre-reg from classical hadith + daily-prayer-manual sources)"
bonferroni: k=2 α_bon=0.025 family=h-new-150-liturgical-hub
pre_reg: findings/phase-b-hypotheses/h-new-150-liturgical-hub-prereg.md
script: scripts/h_new_150_liturgical_hub.py
output_json: findings/phase-b-hypotheses/csv/h-new-150.json
verdict: WEAK-LINK — primary passes at ρ=0.312 (p=0.0002) but the correlation DISSOLVES under length-residualization (residual ρ=0.086, p=0.18). The apparent liturgical-hub link is largely explained by length: liturgically-prominent surahs are either very long (Q 2, 3) or very short (Q 112, 113, 114), and both extremes are over-represented in the cluster-network.
---

# [[h-new-150-liturgical-hub|H-NEW-150]] — Liturgical prominence ↔ cluster-network hub-degree

## Summary

Primary test PASSED (ρ = 0.312, p_perm = 0.0002). Secondary
length-residualized test FAILED (residual ρ = 0.086, p_perm = 0.185).

Per pre-committed acceptance matrix: **WEAK-LINK** — the raw
liturgical-hub correlation is real, but it dissolves under length
control. The mechanism of cluster-network hub-ness is NOT cleanly
attributable to liturgical prominence.

MW-5 positive control PASSED: liturgical score is 17× stronger correlate
than chronology-rank (|ρ_lit|=0.312 vs |ρ_chrono|=0.018).

**Theorist P3 ("liturgical-hub mechanism") gets a partial anchor** but
not a clean one. The link is PRESENT but CONFOUNDED.

## Pre-reg compliance

Liturgical-prominence scores were LOCKED in the pre-reg frontmatter
BEFORE any data-viewing or correlation computation. Direction pre-committed
(PRIMARY: ρ ≥ 0.3; SECONDARY: residual ρ ≥ 0.2). Bonferroni k=2,
α_bon=0.025. Seed 20260417. PRE-REG-STANDARD-04.

Auditor DM not available in time; proceeded per autonomous-no-idle
directive with garden-of-forking-paths locked.

## Results

### Primary — raw correlation

Spearman ρ(LITURGICAL_SCORE, cluster_degree) across 114 surahs:

- **ρ = 0.3121** (exactly at the pre-committed 0.3 threshold)
- SciPy nominal 2-sided p = 0.00072
- Permutation (10K) 1-sided p = 0.0002
- **PASS** at α_bon=0.025 by 3 orders of magnitude

### Secondary — length-residualized

Residualize LITURGICAL_SCORE and cluster_degree against log(nverses)
via OLS, then correlate residuals:

- Residual ρ = **0.0859** (far below the pre-committed 0.2 threshold)
- Permutation p_one_sided = 0.185
- **FAIL**

### MW-5 control — chronology

- |ρ(chronology, degree)| = 0.018
- |ρ(liturgical, degree)| = 0.312
- Liturgical score is 17× stronger correlate than chronology
- **PASS** (liturgical signal is specifically LITURGICAL, not a generic
  classical-marker effect)

## Descriptive: top-15 overlap

**10 of 15 top-liturgical-score surahs are ALSO in top-15 cluster-degree**:

| Q | Name | Lit score | Degree |
|---:|---|---:|---:|
| 2 | al-Baqara | 8 | 4 |
| 3 | Āl ʿImrān | 4 | 4 |
| 32 | al-Sajda | 3 | 3 |
| 36 | Yā-Sīn | 4 | 3 |
| 50 | al-Qāf | 3 | 4 |
| 59 | al-Ḥashr | 3 | 4 |
| 62 | al-Jumuʿa | 3 | 5 |
| 112 | al-Ikhlāṣ | 4 | 4 |
| 113 | al-Falaq | 3 | 4 |
| 114 | al-Nās | 3 | 4 |

**5 of 15 top-liturgical NOT in top-degree**:
- Q 1 al-Fātiḥa (score 17, degree 1) — the MOST liturgical surah is a cluster-leaf!
- Q 18 al-Kahf (score 4, degree 1)
- Q 24 al-Nūr (score 3, degree 1)
- Q 63 al-Munāfiqūn (score 3, degree 1)
- Q 67 al-Mulk (score 3, degree 1)

**5 of 15 top-degree NOT in top-liturgical**:
- Q 10 Yūnus (deg 3, lit 0)
- Q 11 Hūd (deg 3, lit 0)
- Q 12 Yūsuf (deg 3, lit 0)
- Q 14 Ibrāhīm (deg 3, lit 0)
- Q 38 Ṣād (deg 3, lit 0)

These are the Q 10-14 prophet-cluster + single-letter-muq — they're
hub-members for reasons ORTHOGONAL to liturgy.

## The Q 1 al-Fātiḥa counterexample

**Q 1 is the strongest counterexample to the liturgical-hub hypothesis.**
It has the MAXIMAL liturgical score (17; recited in every prayer cycle,
17×/day in standard daily practice) but the LOWEST cluster-network
degree (1). Q 1 is a cluster LEAF despite being the liturgically most
central surah in Islam.

This is consistent with [[h-new-89-meta-cluster-network|H-NEW-89]]'s "Q 1 is structurally isolated"
finding and the 2026-04-17 scratch refinement (Q 1 is content-close to
short-mufaṣṣal but cluster-membership-isolated).

**Mechanism**: Q 1's structural isolation IS ITS liturgical role.
Q 1 is the "opening" — it is by design a sui-generis surah that doesn't
belong to any taxonomic cluster (no muqaṭṭāʿat, no musabbiḥāt, not
sabʿ-ṭiwāl, etc.). Its liturgical primacy is expressed via being
UNIQUE, not via belonging to many clusters.

This is a real tension: liturgical-hub hypothesis predicts Q 1 should be
hub, reality is Q 1 is a leaf. Q 1 fails the hypothesis SO HARD that
its inclusion likely drags the Spearman ρ DOWN — the signal comes from
the 10/15 non-Q 1 top-liturgical surahs being hub-members.

## Why the length-residualization kills the signal

The top-liturgical surahs are bimodal in length:

- **Very long**: Q 2 (286 verses, score 8), Q 3 (200, 4), Q 18 (110, 4),
  Q 36 (83, 4), Q 67 (30, 3)
- **Very short**: Q 112 (4, 4), Q 113 (5, 3), Q 114 (6, 3), Q 97 (5, 1),
  Q 109 (6, 1), Q 110 (3, 1), Q 94 (8, 1)

Meanwhile, the top cluster-degree surahs are ALSO bimodal in length
(front Q 2, 3 very long + back-terminal Q 112, 113, 114 very short).
The CORRELATION is between surah-length-extremity and both variables,
not between liturgy and hub-status per se.

After regressing out log(nverses), the residuals show only ρ=0.086 —
essentially no remaining signal. The liturgical-hub link is, within the
resolution of this test, a length-confound.

## What this means

### For theorist's P3 (liturgical-hub mechanism)

**P3 gets a partial empirical anchor but not a clean one**. The raw
correlation is real (ρ=0.312) but the residual correlation is not
(0.086). This means:

- **Weak form of P3 (raw signal)**: YES, liturgical prominence predicts
  hub-status at ρ=0.31.
- **Strong form of P3 (residual signal)**: NO, the correlation is
  length-mediated and disappears after control.

The theorist should treat P3 as a CONSEQUENCE of P2 (length-extremes
produce hubs) rather than as an INDEPENDENT mechanism.

### For Q 50's hub status ([[h-new-146-q50-qaf-hub|H-NEW-146]] refinement)

Q 50 has liturgical score 3 (Friday/Eid) and cluster-degree 4. Q 50 IS
in the top-15 overlap. So [[h-new-146-q50-qaf-hub|H-NEW-146]]'s Q 50 hub status is PARTIALLY
explained by liturgical prominence — BUT only at the raw level; under
length-control the explanation weakens.

Q 50's 45 verses puts it at the mid-length tier (below Q 2-3 long; above
Q 112-114 short). Q 50's hub-ness is NOT length-driven (it's mid-length),
but its liturgical-prominence also doesn't survive length-residualization
across the corpus. So Q 50 remains UNEXPLAINED at the strict level;
liturgical contribution is suggestive but not definitive.

### For Q 1 al-Fātiḥa

Q 1 is a SUI GENERIS case: maximal liturgical prominence, minimal
cluster-network membership. Q 1's role is LITURGICAL-VIA-ISOLATION
(unique opening) rather than LITURGICAL-VIA-HUB (connecting many
clusters). This may be a NEW principle: sui-generis liturgical role is
one pattern; hub liturgical role is another.

## Honest limits

1. **Scoring is hand-coded and subjective**. I tried to lock it before
   viewing data, but the scoring scheme itself (1-point per Friday
   prescription, 17-point for Q 1) reflects my judgment about relative
   liturgical weight. A different rater's weights might give different
   raw ρ. The DIRECTION of the finding (positive correlation before
   length-residualization) would likely survive most reasonable
   re-weightings; the RESIDUAL NULL finding is robust because the
   residual ρ is near zero.
2. **n=114 with many zeros** (87 of 114 have score 0). The correlation
   is driven by ~27 non-zero surahs.
3. **Madhhab-sensitivity**: prescribed recitations vary slightly between
   4 Sunni madhāhib (Ḥanafī / Shāfiʿī / Mālikī / Ḥanbalī). My coding
   aimed for "common classical core" but strict-madhhab replication
   could yield different scores.
4. **[[cross-finding-010-extended-network|Cross-finding-010]]'s cluster-network is one of many possible
   network definitions**. A different cluster taxonomy might give
   different degrees.
5. **The length-residualization assumes log-linear length effect**.
   Alternative (e.g., verse-count-bracket) might preserve some
   liturgical signal.

## Honest null reporting

The SECONDARY FAIL is the more important finding. The theorist's clean
P3 ("liturgical-prominence as hub-mechanism") does not survive
length-residualization at my pre-committed threshold. Published with
equal prominence to the primary-PASS.

## Queued follow-ups

- **H-NEW-150.1**: re-code liturgical scores via inter-rater agreement
  (3+ raters) to confirm ρ robustness to scoring choices.
- **H-NEW-150.2**: per-madhhab scoring variants (4 replications).
- **H-NEW-150.3**: alternative length-residualization (non-log, bracket)
  to probe whether the residual-NULL is scheme-specific.
- **H-NEW-150.4**: sui-generis-vs-hub liturgical role — formal
  classification test (is Q 1's isolated-liturgy pattern distinguishable
  from Q 2's hub-liturgy pattern in other structural features?).

## Connections

- Parent: [[cross-finding-010-extended-network|cross-finding-010]] (cluster-network); [[h-new-146-q50-qaf-hub|H-NEW-146]] (Q 50 hub)
- Aligns with: [[h-new-89-meta-cluster-network|H-NEW-89]] (Q 1 sui-generis), scratch Q 1 nearest-neighbors
  (Q 1 content-close to short-mufaṣṣal)
- Tensions with: theorist P3 clean-form (now weakened to P3★ = P2-mediated)
- Contributes to: OQ-6 META-architecture (liturgy as one axis, not THE axis)
