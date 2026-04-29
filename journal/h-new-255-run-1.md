# H-NEW-255 — Run 1 journal

Date: 2026-04-17
Seed: 20260419
Script: `scripts/h_new_255_juz30_mini_cycle.py`
Pre-reg: `findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle-prereg.md`
Pre-reg SHA-256: `574dcfeb0b56288028bd63500234faf20a188552e1a1a85bd9a212c33b2d1c52`

## Setup

Parent findings consulted: cross-finding-013 (mushaf = structured Hamiltonian cycle CONFIRMED), H-NEW-111 (Fisher-Rao D matrix; R_mushaf=1.107, z=−11.46), H-NEW-185 (ring Laplacian; Fiedler cut at Q 77/Q 78), H-NEW-202 (Juzʾ 30 internal structure NULL 0/3 but rank-1 descriptive cohesion), H-NEW-203 (full-juzʾ Fisher-Rao analysis; Juzʾ 30 is *least* coherent at verse-centroid pooling).

Feature choice locked in pre-reg: QAC v0.4 STEM root tokens, K=500 (H-NEW-111 inheritance), Dirichlet α=0.5, Fisher-Rao angular distance. Sub-mushaf = Q 78..Q 114 (37 surahs, canonical whole-surah approximation).

Pre-reg declared 3-cell Bonferroni (T1 ratio band, T2 permutation z+p, T3 wrap-edge), α_bon = 0.01667, seed 20260419, 1000 perms.

## Run

One production run, 1000 permutations, deterministic. Total runtime ~35 seconds on the 114×114 D-matrix build + 37×37 sub-problem. No retries, no parameter tweaks post-pre-reg.

## Results

- T1 (ratio): R_juz30 = **1.072** (band [1.05, 1.20]) — **PASS** (tighter than full mushaf 1.107 by 3.2%)
- T2 (permutation null): z = **−5.32**, p = 0.001, 0/1000 permutations shorter — **PASS** (crushes −3.0 threshold)
- T3 (wrap-edge): d(Q 114, Q 78) = 0.645, z = **+1.37** (SIGN-REVERSED from CF-013's −4.17 wrap-edge), p = 0.918 — **NULL**
- MW-5 (greedy-NN from Q 78): L = 15.902, z = −8.27, p = 0.001 — **PASS**

Joint label (pre-registered matrix): **MINI-GEODESIC-OPEN-PATH**.

## Key observations

1. **Geodesic backbone self-similar; closure layer NOT self-similar.** The 114-surah ring topology has a fractal geodesic component but a non-fractal closure. This is the central new result.
2. Juzʾ 30 pair-distance mean (0.489) is 47% smaller than full-mushaf (0.924) — mechanically compressed vocabulary range, but Juzʾ 30 still achieves stronger per-edge z (−0.148/edge vs −0.101/edge at full-mushaf scale), so the coherence is not fully explained by compression.
3. Top-5 structural hinges within Juzʾ 30 concentrate in the opening stretch Q 78..Q 84 (4 of 5) — the front of Juzʾ 30 has the between-surah heterogeneity; the back tail Q 89..Q 114 is smoother.
4. Juzʾ 30's Q 97/Q 98 (H-NEW-202 sub-Fiedler boundary) ranks #17 of 36 by consecutive-pair jump — spectral instrument and path-jump instrument disagree on Juzʾ-30's principal boundary. Not a contradiction; different statistics.
5. Against 78 other contiguous 37-surah arcs in the mushaf, Juzʾ 30 ranks **2nd shortest** (z_contig = −2.36, p = 0.025). Descriptive not primary, but a strong effect.
6. d(Q 1, Q 114) = 0.388 [full-mushaf wrap] vs d(Q 78, Q 114) = 0.645 [juzʾ-30 wrap] — the closure is **specifically Q 1 ↔ Q 114**, not a generic short-mufaṣṣal terminus phenomenon. The liturgical pair {fātiḥa, khawātim} is doing the closure work at the 114-scale.

## Alignment with classical scholarship

al-Suyūṭī's mufaṣṣal threefold division treats Juzʾ 30 as an open-ended length-graded block, NOT as a closed/cyclic unit. al-Ghazālī's ādāb of tilāwa frames the Q 1 ↔ Q 112/113/114 closure pair as a **session-level** (= 114-scale) liturgical frame, not as a juzʾ-internal feature. al-Zarkashī's fawātiḥ/khawātim structural pairing is specifically the mushaf's fātiḥa + khawātim. H-NEW-255's empirical finding (juzʾ-scale NO closure; 114-scale closure) RATIFIES the classical reading: the closure is a mushaf-scale feature.

## Garden of forking paths

No deviations from pre-reg. All parameters locked; single production run. Post-hoc additions: (i) S4 contiguous-37-arc null was pre-declared as descriptive; included in JSON and findings. (ii) the comparison of per-edge z (−0.148 vs −0.101) was not in the pre-reg but is a natural descriptive summary — included in findings as honest framing.

## Outputs

- `findings/phase-b-hypotheses/csv/h-new-255.json` (full JSON summary including opt-path, all 666 pair distances, 36 consecutive pairs, permutation null stats, wrap-edge null stats, contiguous-arc null)
- `findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle.md` (findings)
- `findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle-prereg.md` (pre-reg)

## Verdict

**MIXED: T1 + T2 PASS, T3 NULL.** Joint label: **MINI-GEODESIC-OPEN-PATH**. The ring-topology of cross-finding-013 is PARTIALLY self-similar: the geodesic backbone replicates at Juzʾ 30 sub-scale, but the wrap-around closure does not. This refines CF-013 from "the mushaf is a ring" to "the mushaf is a ring whose geodesic backbone is scale-invariant but whose closure is a 114-specific architectural feature at the fātiḥa + khawātim positions."

Ceiling: **PASS-DIRECTED** pending H-NEW-255b (length-matched null) + H-NEW-255c (char-4-gram replication) + H-NEW-255d (other-juzʾ sub-cycle tests).
