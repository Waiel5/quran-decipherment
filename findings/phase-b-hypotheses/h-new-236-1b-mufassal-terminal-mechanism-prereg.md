# [[h-new-236-1b-mufassal-terminal-mechanism|H-NEW-236.1b]] — Mufaṣṣal-short terminal-block mechanism test: pre-registration


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

```yaml
finding_id: h-new-236-1b
title: "Mufaṣṣal-short terminal-block mechanism test — does one of {M_H hinge-100, M_R rhyme-class, M_L liturgical-pairs, M_B sub-block-partition} close the last residual L_mufaṣṣal-short z=+10.66 above top-50 hinge baseline?"
parent: h-new-236-1a (NEAR-GENERATIVE-CLOSURE at top-30 and top-50; L_path closes; ḥawāmīm closes; mufaṣṣal-short z=+10.66 remains OUTSIDE HIGH)
grandparent: h-new-236-1 (M1.3 hinge closure 73%)
great-grandparent: h-new-236 (primary 4-principle simulator) → cross-finding-020 (the complete equation)
siblings:
  - H-NEW-130 (Fisher-Rao residuals; top-15 hinges)
  - H-NEW-202 (Juzʾ 30 internal structure)
  - H-NEW-185 (spectral ring-Laplacian; Juzʾ 30 boundary at Q 97/98)
  - H-NEW-188 (PC3 refrain-stylistic within-M5)
  - H-NEW-234 (Q 55 Mode-B refrain PARTIAL)
date: 2026-04-18
specialist: autonomous (H-NEW-236.1b)
seed: 20260420    # new day per project convention; fresh stream
rules_tuple: "(no-tashkeel, 114 surahs Hafs-Kūfan, basmala-counted-only-in-surah-1, QAC-STEM root tokens, Fisher-Rao arccos-Bhattacharyya per H-NEW-111, stochastic 2-opt with classical-block + Q1-lock + length-stratification + M2-muq + TOP-50-HINGE-BASELINE + per-cell mechanism-constraint, seed 20260420)"
bonferroni_k: 4
alpha_family: 0.05
alpha_bon: 0.0125   # one test per mechanism cell
cells:
  - M_H: hinge-truncation extension to ranks 1-100 (adds ≥1 mufaṣṣal-short-internal edge beyond top-50 baseline)
  - M_R: rhyme-class preservation within mufaṣṣal-short (pre-committed rhyme-bins from classical fāṣila-catalogue)
  - M_L: liturgical recitation-pair adjacency constraints for 4 pre-committed classical pairs
  - M_B: within-block 2-opt restricted to 3 sub-block brackets {Q 78-88, Q 89-107, Q 108-114}
n_simulations: 1000
n_random_null: 1000     # shared MW-5 baseline (plus a dedicated MW-5 for the top-50-baseline MW-5-positive-control)
```

## 1. Hypothesis

**H0 (null across all 4 cells — no terminal-block mechanism closes mufaṣṣal-short)**: Under the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 hinge-preserved simulator, augmenting the constraint set with any one of M_H / M_R / M_L / M_B does NOT bring empirical L_mufaṣṣal-short inside the simulated 95% CI. The z-score stays ≥ +2.0 one-tailed (observed > 97.5-th percentile of the per-cell simulator distribution). R12a remains OPEN and the causal-generative layer stays NEAR-COMPLETE but NOT CONFIRMED.

**H1 (alternative — at least one mechanism closes mufaṣṣal-short)**: Under at least one mechanism, empirical L_mufaṣṣal-short enters the simulated distribution at pct ≤ 97.5 (equivalently z ≤ +2.0). That mechanism becomes the identified **terminal-block organizing principle**; OQ-15 causal-generative layer is CONFIRMED at that mechanism.

**Direction-locked pass criterion (per cell)**:
- PASS_strict = empirical L_mufaṣṣal-short ≤ sim 97.5-th percentile AND empirical L_path remains INSIDE sim 95% CI (parsimony: mechanisms must not break what top-50 already solved).
- PASS_loose = empirical L_mufaṣṣal-short z ≤ +2.0 regardless of L_path status (flags mechanisms that trade one observable for another).

The primary pre-registered decision uses PASS_strict.

## 2. Motivation and parent context

[[h-new-236-1a-extended-hinges|H-NEW-236.1a]] (landed 2026-04-18) established:
- top-30 hinges close L_path exactly (pct 48.1) and close ḥawāmīm (z = -0.04)
- top-50 hinges close L_path to pct 59.1 and close ḥawāmīm EXACTLY (sim_std = 0)
- mufaṣṣal-short remains OUTSIDE HIGH in both cells (z = +10.90 at top-30; z = +10.66 at top-50)
- first mufaṣṣal-short internal edge is rank 73 in the canonical FR ranking

The residual R12a = **mufaṣṣal-short within-block cost-excess** is the final unsolved residual at the causal-generative layer. The empirical block-sum L_mufaṣṣal-short = 16.5149 sits ~0.90 FR units above the within-block FR-minimum (sim mean ≈ 15.62 under top-50).

Four plausible terminal-block organizing mechanisms compete:
- M_H: the gap is an enumeration gap in M1.3 (top-K is just too short a cut).
- M_R: classical rhyme/fāṣila continuity (al-Suyūṭī *Itqān* fann 59 on *al-fawāṣil wa-l-qawāfī*; al-Zarkashī *Burhān* on prosodic patterns) is the missing organizing pressure.
- M_L: liturgical recitational pairs (sabbiḥ-openers Q 87+88; al-Ḍuḥā/al-Sharḥ Q 93+94 consolation pair; al-ʿAṣr/al-Humaza Q 103+104; al-Kāfirūn/al-Naṣr Q 109+110; al-Muʿawwidhatān Q 113+114) pin specific adjacencies.
- M_B: Farāhī-Iṣlāḥī *naẓm*-group thematic brackets within mufaṣṣal-short {eschatological panorama Q 78-88; ethical-theological Q 89-107; closing refrains Q 108-114}.

## 3. Pre-computed mechanism specifications (LOCKED pre-run)

### 3.1 M_H hinge-100

- Baseline: inherit **top-50 canonical Fisher-Rao consecutive edges** from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] (verified by re-ranking the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix at run start).
- Extension: add canonical consecutive edges **rank 51..100** as additional hard constraints.
- Classification (within/cross) of each new hinge is determined automatically by the same `classify_hinges` routine as [[h-new-236-1a-extended-hinges|H-NEW-236.1a]].
- No hand-picked hinges; all 100 hinges are the top-100 FR consecutive-edge ranks on the canonical mushaf D-matrix.
- Rationale: tests Reading A of [[h-new-236-1-hinges-constrained-simulator|H-NEW-236.1]] extended: "if we simply cut deeper, we eventually capture Q 78→79 at rank 73 and the first internal mufaṣṣal-short edges at ranks 73+." The enumeration-gap hypothesis.

### 3.2 M_R rhyme-class preservation within mufaṣṣal-short

- Rhyme-class assignment is pre-committed by classical fāṣila-catalogue. Classes for Q 78-114 (using predominant verse-ending pattern, single-letter or vowel class):
  - **R-ā**: Q 79 ("-ā" pattern — al-Nāziʿāt), Q 87 al-Aʿlā, Q 88 al-Ghāshiya, Q 89 al-Fajr, Q 91 al-Shams, Q 92 al-Layl, Q 93 al-Ḍuḥā, Q 94 al-Sharḥ, Q 95 al-Tīn, Q 96 al-ʿAlaq, Q 98 al-Bayyina, Q 100 al-ʿĀdiyāt
  - **R-ūn/-īn**: Q 83 al-Muṭaffifīn, Q 95 al-Tīn (secondary), Q 102 al-Takāthur, Q 104 al-Humaza, Q 105 al-Fīl, Q 106 Quraysh, Q 107 al-Māʿūn, Q 109 al-Kāfirūn
  - **R-r/-r-saj'**: Q 97 al-Qadr, Q 103 al-ʿAṣr, Q 108 al-Kawthar, Q 110 al-Naṣr
  - **R-saj'-mixed**: Q 78 al-Nabaʾ, Q 80 ʿAbasa, Q 81 al-Takwīr, Q 82 al-Infiṭār, Q 84 al-Inshiqāq, Q 85 al-Burūj, Q 86 al-Ṭāriq, Q 90 al-Balad, Q 99 al-Zalzalah, Q 101 al-Qāriʿa
  - **R-d-tawḥīd**: Q 112 al-Ikhlāṣ (aḥad / ṣamad / ulid / aḥad — unique)
  - **R-s**: Q 111 al-Masad, Q 114 al-Nās
  - **R-q**: Q 113 al-Falaq

  (Assignment derived from classical *Itqān* fann 59 + working mushaf rhyme-catalogue; LOCKED pre-run as listed above — no post-hoc reassignment.)

- Mechanism enforcement (soft+hard hybrid):
  - **Hard**: surahs of the same rhyme-class that are ADJACENT in the canonical ordering must remain adjacent in the sampled ordering (i.e. swaps that separate them are rejected). Within mufaṣṣal-short under this rule the maximal same-class adjacency runs are: R-ā Q 87-89, Q 91-96, Q 98 (with Q 97 as internal break), Q 93-94 consolation pair (subset); R-ūn Q 105-107.
  - **Hard**: Q 112 tawḥīd class is a 1-element class with no same-class neighbour; acts as no-op.

- Scope: only within mufaṣṣal-short (Q 78-114). All other blocks unchanged from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 baseline.

### 3.3 M_L liturgical recitation-pair adjacencies

Pre-committed pairs (LOCKED pre-run; classical sources cited):

- Q 87 + Q 88 adjacency (both sabbiḥ-openers; Ibn Kathīr *Tafsīr* on linked recitation).
- Q 93 + Q 94 adjacency (al-Ḍuḥā + al-Sharḥ; classical consolation-pair per al-Zarkashī *Burhān*; some schools recite together with one takbīr).
- Q 109 + Q 110 adjacency (al-Kāfirūn + al-Naṣr; classical *qul*-opener + closing completion pair).
- Q 113 + Q 114 adjacency (al-muʿawwidhatān; Bukhārī 5016, Abū Dāʾūd 1523 — protective pair recited after obligatory prayers).

(Not pre-committed: Q 103 + Q 104 — treated as descriptive-only, not added as a hard constraint because the "both al-*short*" observation is lexical, not a recitation-pair hadith.)

- Mechanism enforcement: each of 4 pairs is a hard within-block adjacency constraint on top of the top-50 hinge baseline. (Some may already be included in top-50: verify at run start and dedupe.)

### 3.4 M_B sub-block partition

Pre-committed sub-block boundaries LOCKED from Farāhī-Iṣlāḥī *naẓm*-groups reading:
- Sub-block B1 = Q 78-88 (eschatological panorama: al-Nabaʾ through al-Ghāshiya)
- Sub-block B2 = Q 89-107 (ethical-theological: al-Fajr through al-Māʿūn)
- Sub-block B3 = Q 108-114 (closing refrains: al-Kawthar through al-Nās)

- Mechanism enforcement: the within-block 2-opt SA is **further restricted** so that swaps are rejected if they move a surah across a sub-block boundary. Within each sub-block, 2-opt runs freely (subject to top-50 hinge preservation).
- This REDUCES within-block flexibility: the canonical ordering is no longer competing against all permutations of Q 78-114 but against permutations within each sub-block.

## 4. Generative procedure (DELTA from [[h-new-236-1a-extended-hinges|H-NEW-236.1a]])

Start from `scripts/h_new_236_1a_extended_hinges.py`. Changes:

1. **Baseline for all cells**: top-50 canonical FR consecutive edges, identical to [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] cell B.
2. **Per-cell augmentation**: add the mechanism-specific constraint on top of the baseline.
3. **Seed**: 20260420 (new day per project convention). MW-5 baseline uses same seed stream.
4. **SA schedule unchanged**: T_HOT=0.05, T_COLD=0.001, 200 iters.
5. **MW-5 positive control**: re-run the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] top-50 baseline without any new mechanism under seed 20260420. It MUST reproduce L_mufaṣṣal-short z ≈ +10.66 (± simulator noise). If that control fails, the instrument is broken and the whole run is discarded.
6. **MW-HINGE**: verify all sampled orderings respect the top-50 hinges + the per-cell mechanism constraint.
7. **N_sim=1000 per cell** (4 cells × 1000 = 4000 constrained samples). N_random_null=1000 (shared).

## 5. Observables (same 4 as [[h-new-236-generative-simulator|H-NEW-236]] / 236.1 / 236.1a)

- **O1 L_path**
- **O2 W_wrap**
- **O3 Block-χ²** (decomposed into L_ṭiwāl + L_ḥawāmīm + L_mufaṣṣal-short)
- **O4 L_tail_91_114**

**Primary target per cell**: L_mufaṣṣal-short z-score and its sim percentile.

## 6. Interpretation rules (LOCKED pre-run)

For each cell ∈ {M_H, M_R, M_L, M_B}:

| Outcome | Verdict |
|---|:---|
| Empirical L_mufaṣṣal-short pct ≤ 97.5 AND L_path INSIDE sim 95% CI | **MECHANISM CLOSES** → OQ-15 CAUSAL-GENERATIVE-LAYER CONFIRMED (at that mechanism, Bonferroni α_bon = 0.0125) |
| Empirical L_mufaṣṣal-short pct ≤ 97.5 but L_path leaves 95% CI | **PARSIMONY-CONFLICT**: mechanism trades path-length closure for block closure — report but do NOT declare confirmation |
| Empirical L_mufaṣṣal-short pct > 97.5 and L_path INSIDE | **MECHANISM NULL**: mechanism does not address R12a |
| Both fail | **MECHANISM BROKEN**: mechanism over-constrains the baseline |

**Overall OQ-15 causal-generative-layer verdict**:
- ≥1 cell passes strict → CONFIRMED (Bonferroni k=4 protected).
- 0 cells pass strict, ≥1 pass loose → PARSIMONY-CONFLICT REPORTED; verdict remains NEAR-COMPLETE.
- 0 cells pass either → NULL with equal prominence; OQ-15 causal-generative-layer remains OPEN.

## 7. Bonferroni discipline

k=4 (one test per mechanism, independent direction). α_bon = 0.0125. Self-tightens vs [[h-new-236-1a-extended-hinges|H-NEW-236.1a]]'s k=2 (per the project rule that Bonferroni tightening self-verifies; loosening would require ratification).

## 8. Honest limits (disclosed pre-run)

1. **Parsimony ceiling**: top-50 baseline already hard-locks 50 of 113 consecutive edges (44%). Adding M_H to 100 edges means 88% of the path is hinge-constrained — the generator becomes weakly distinguishable from the canonical mushaf trivially. We disclose this: if M_H closes under top-100, it is informative but qualified.
2. **Rhyme-class assignment (M_R)** uses a single-letter reduction of classical fāṣila-catalogues; finer prosodic distinctions are not captured. Misassignment is a known risk; the coarse classification is the **deliberate** low-parameter choice.
3. **Liturgical pairs (M_L)** uses 4 well-attested classical hadith/tafsīr pairs only. Pairs like Q 103+104 (lexical-structural but NOT hadith-attested) are EXCLUDED pre-registration.
4. **Sub-block partition (M_B)** uses Farāhī-Iṣlāḥī *naẓm*-group boundaries. Alternative partitions (e.g. 2-sub-block Q 78-99 + Q 100-114; 4-sub-block) are NOT swept.
5. **Compute budget**: 4000 constrained simulations + 1000 MW-5 random null + 1000 MW-5-positive-control (top-50 reproducibility). Vectorised where possible; SA re-uses the [[h-new-236-1a-extended-hinges|H-NEW-236.1a]] 2-opt routine.
6. **Bonferroni k=4 does not control for cross-mechanism multiplicity** if mechanisms overlap (e.g. Q 93-94 appears in both M_R and M_L). This is disclosed; we report per-cell results independently and flag the overlap.
7. **Garden-of-forking-paths log (ALL locked BEFORE execution)**:
   - Rhyme-class assignment dictionary above (§3.2)
   - Liturgical-pair list above (§3.3)
   - Sub-block boundaries above (§3.4)
   - top-100 rank cutoff (§3.1)
   - Per-cell pass criterion (§6)
   - Seed 20260420

## 9. Deliverables

- `scripts/h_new_236_1b_mufassal_terminal.py`
- `findings/phase-b-hypotheses/h-new-236-1b-mufassal-terminal-mechanism.md`
- `findings/phase-b-hypotheses/csv/h-new-236-1b.json`
- `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md` §12.8 amendment
- MASTER-LEDGER Wave-5 entry appended
- `journal/h-new-236-1b-run-1.md`
- **If any cell PASSES strict**: MASTER-LEDGER flag that [[cross-finding-023-causal-generative-closure|cross-finding-023]] synthesis is warranted (not written by this specialist).

Pre-reg locked 2026-04-18. Execution follows.
