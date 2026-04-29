---
id: H-NEW-290
title: Q 42 HMASQ — mushaf-block vs phonological-cluster tension
phase: B
status: PRE-REGISTERED 2026-04-18
date: 2026-04-18
agent: team-lead (inline)
parent: H-NEW-232 (5-way convergent finding Q 42 HMASQ → TSM phonologically)
related: H-NEW-165.2, H-NEW-252 (independent feature-space replications)
seed: 20260422
bonferroni_k: 3
bonferroni_family: h-new-290-q42-tension
alpha_bon: 0.01667
n_perm: 1000
rules_tuple: "(Fisher-Rao root distance matrix from H-NEW-236.1a simulator JSON; Q 42 as pivot; mushaf-block neighbors (Q 41, Q 43) vs TSM-phonological-cluster members (Q 26, Q 28) vs random-non-muq control; permutation null preserving cardinalities; seed 20260422; n_perm=1000)"
direction: "Cell A: Q 42's FR distance to ḥawāmīm-block neighbors (Q 41, Q 43) COMPARED TO its FR distance to TSM-phonological cluster members (Q 26, Q 28). Direction pre-committed: if block-mean-distance < phonological-mean-distance, BLOCK-DOMINANCE; if reverse, PHONOLOGY-DOMINANCE"
verdict: PENDING
---

# [[h-new-282-q108-top500-coverage-normalized-mst|H-NEW-282]] — Q 42 HMASQ: mushaf-block vs phonological-cluster tension

## 1. Question

Wave-4/5 delivered a 5-way convergent finding: Q 42 HMASQ's phonological signature, measured across V0/V1/V2/V3 codebooks ([[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]) plus joint phon+(α,β) ([[h-new-252-combined-phon-alphabeta-singleton|H-NEW-252]]), places it nearest to the TSM (ṭā-sīn-mīm) cluster — not to the HM (ḥā-mīm) cluster where classical a-priori assignment places it.

Yet Q 42 sits at mushaf position 42 — **INSIDE the ḥawāmīm block** (Q 40-46). al-Biqāʿī's *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* and al-Zarkashī's *al-Burhān* treat this block as a cohesive architectural unit defined by the ḥā-mīm opener. The HMASQ 5-letter opening (ح م ع س ق) is the only variant within the block.

**The structural question**: which principle wins at Q 42?

- **Mushaf-block-adjacency** (al-Biqāʿī munāsabāt): Q 42's nearest neighbors by CONTENT should be Q 41 Fuṣṣilat and Q 43 al-Zukhruf — both HM openers.
- **Phonological-cluster-similarity** (al-Khalīl tajwīd): Q 42's nearest neighbors by LETTER-SET should be Q 26 al-Shuʿarāʾ and Q 28 al-Qaṣaṣ — both TSM openers.

The two principles predict DIFFERENT nearest-neighbor sets. Which prediction is empirically correct under the Fisher-Rao content-distance metric already used across the project?

## 2. Hypothesis

**H_BLOCK**: d̄(Q 42, {Q 41, Q 43}) < d̄(Q 42, {Q 26, Q 28}). If true, mushaf-block adjacency dominates phonological-cluster similarity at Q 42. al-Biqāʿī's block-level munāsabāt principle empirically wins.

**H_PHON**: d̄(Q 42, {Q 41, Q 43}) > d̄(Q 42, {Q 26, Q 28}). If true, phonological-cluster similarity dominates mushaf-block adjacency at Q 42. al-Khalīl's tajwīd-classification principle empirically wins — and Q 42 sits in the ḥawāmīm block DESPITE being content-closer to TSM surahs.

**Null H_0**: the two distances are statistically indistinguishable after permutation-null calibration.

## 3. Data

- Fisher-Rao root distance matrix: from `findings/phase-b-hypotheses/csv/h-new-236-1a.json` field encoding the 114×114 FR distance matrix (same one used in [[h-new-111-fisher-rao-mushaf|H-NEW-111]], [[h-new-236-generative-simulator|H-NEW-236]], [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]).

## 4. Protocol

### Cell A — Head-to-head comparison (primary)

For the 4 target pairs:
- `d_block_41 = d_FR(Q 42, Q 41)` — mushaf-block left neighbor
- `d_block_43 = d_FR(Q 42, Q 43)` — mushaf-block right neighbor
- `d_phon_26 = d_FR(Q 42, Q 26)` — TSM cluster member
- `d_phon_28 = d_FR(Q 42, Q 28)` — TSM cluster member

Statistics:
- `d̄_block = (d_block_41 + d_block_43) / 2` — mean block-neighbor distance
- `d̄_phon = (d_phon_26 + d_phon_28) / 2` — mean phonological-cluster distance
- `Δ = d̄_block − d̄_phon` — signed difference (negative means block wins)

Direction: under H_BLOCK, Δ < 0 (block distances smaller). Under H_PHON, Δ > 0. Under H_0, |Δ| ≈ permutation null expectation.

Null (permutation): for 1000 iterations, randomly select 2 surahs from the non-Q-42 HM-block set (Q 40, 41, 43, 44, 45, 46 minus itself) and 2 from the non-Q-26/28 TSM set (TSM has only 2 members, so null here is matched to the entire FR distance distribution: sample 2 random surahs). Compute Δ_null. PASS if |Δ_obs| in top or bottom 2.5% of null distribution (two-sided test under H_0, becomes one-sided under pre-committed direction).

### Cell B — Ranked-neighbor test

Rank all 113 non-Q-42 surahs by FR distance to Q 42. Report:
- Position of Q 41 (mushaf-left-neighbor) in this ranking
- Position of Q 43 (mushaf-right-neighbor)
- Position of Q 26, Q 28 (TSM cluster)
- Position of Q 40, Q 44, Q 45, Q 46 (other HM-block members)

Decision: if median rank of {Q 41, Q 43} < median rank of {Q 26, Q 28}, block wins at Q 42. Test via Mann-Whitney U null over random pair rankings.

### Cell C — HMASQ-to-centroid distance (confirmatory)

Compute d_FR(Q 42, centroid(HM block)) and d_FR(Q 42, centroid(TSM block)). These are the same centroids used in [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]. Report ratio.

Direction: if d(HM centroid) < d(TSM centroid), block wins at CONTENT level, phonology-cluster-classification is a classical-interpretation refinement. If d(TSM centroid) < d(HM centroid), CONTENT and PHONOLOGY AGREE — both point to TSM as empirically closer, which would strongly ratify the 5-way convergent finding.

## 5. MW-5 positive control

Run the same protocol on a ḥā-mīm surah that is NOT HMASQ — e.g. Q 43 al-Zukhruf. For Q 43, expected result is d̄_block < d̄_phon_to_TSM (block should win definitively because Q 43 IS canonically HM). If MW-5 for Q 43 fails to show block-dominance, the instrument is broken.

## 6. Bonferroni

k = 3 cells (A head-to-head; B ranked-neighbor; C centroid-distance). α_bon = 0.05/3 = 0.01667.

## 7. Decision rules

| Cell A | Cell B | Cell C | Verdict |
|---|---|---|---|
| H_PHON | H_PHON | TSM closer | **PHON-DOMINANCE** (al-Khalīl wins; Q 42 is in HM-block DESPITE content-similarity to TSM — "surprising empirical placement") |
| H_BLOCK | H_BLOCK | HM closer | **BLOCK-DOMINANCE** (al-Biqāʿī wins; Q 42 is empirically HM — 5-way convergent "miss" was a phonological-vs-content axis mismatch, not a classical apriori error) |
| Mixed | — | — | **MIXED** (block and phonology each capture different axes at Q 42) |

## 8. Interpretation rules (pre-committed)

- **PHON-DOMINANCE**: strengthens [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]]'s 5-way convergent finding — Q 42 is a genuine outlier in the ḥawāmīm block. Classical al-Biqāʿī block-coherence does NOT hold at Q 42; Q 42's placement in the HM block reflects a STRUCTURAL decision (MUSHAF POSITION as P3-liturgical-like override of content-similarity).
- **BLOCK-DOMINANCE**: refutes the 5-way convergent phonological finding as a CLUSTERING artifact. Q 42 IS empirically HM by content; the phonological apparatus just mis-categorizes it due to the 5 extra letters overwhelming the ḥ-m stem.
- **MIXED**: the Q 42 placement is multi-principled — block-adjacency at content level + phonological-distance at letter-set level, jointly producing the observed "wrong-cluster" nearest-neighbor in [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]].

## 9. Garden-of-forking-paths constraints

1. Only the pre-specified target pairs are tested (Q 41, Q 43, Q 26, Q 28).
2. Only the Fisher-Rao root distance metric (from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]) is used.
3. The 3 cells are adjudicated with Bonferroni k=3.
4. MW-5 positive control is LOCKED at Q 43 before execution.
5. Centroid definitions inherited verbatim from [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] (no re-annotation).
6. No post-hoc threshold edits.

## 10. Honest limits

1. **Single-surah analysis**. Conclusions are specific to Q 42; generalization to Q 36 or to other singletons requires separate pre-reg.
2. **Fisher-Rao is one content metric**; char-4-gram ([[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]) or NCD ([[h-new-169-ncd-mushaf|H-NEW-169]]) could shift the result. Report sensitivity as a secondary note, not a primary inferential change.
3. **MW-5 at Q 43**: Q 43 is one HM-block control surah; alternative controls (Q 40, 41, 44, 45, 46) could give different baselines.
4. **Small-sample Mann-Whitney U on 2-element phon set (Q 26, Q 28)**: statistical power is limited. Report the test + a more informative descriptive version.

## 11. Classical-scholarship anchors

- **al-Biqāʿī *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*** — treats ḥawāmīm as a cohesive block based on the ḥ-m opener; implicit prediction is block-adjacency dominance.
- **al-Khalīl al-Farāhīdī *Kitāb al-ʿAyn*** — 8-tier makhraj for the 5-letter HMASQ set; implicit prediction is phonological-cluster dominance (HMASQ's {ʿ, s, q} extra letters shift it phonologically toward TSM).
- **al-Suyūṭī *al-Itqān*** — catalogs HMASQ as a *separate* 5-letter variant of ḥawāmīm; explicitly acknowledges the letter-set difference from HM.
- **al-Zarkashī *al-Burhān fī ʿUlūm al-Qurʾān*** — discusses mushaf-block structure; ḥawāmīm is one of the named blocks.

## 12. Deliverables

- Pre-reg: this file (SHA-256 computed post-lock)
- Script: `scripts/h_new_290_q42_block_vs_phonology.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-290.json`
- Findings: `findings/phase-b-hypotheses/h-new-290-q42-block-vs-phonology-tension.md`
- Journal: `journal/h-new-282-run-1.md`

Pre-reg locked 2026-04-18. Execution follows immediately.
