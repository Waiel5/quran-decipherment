# Journal — h-new-91-run-1

**Date:** 2026-04-15
**Agent:** h-new-91-specialist
**Task:** Test H-NEW-91 — Per-surah rare-root density. Identify surahs with anomalously high rare-root concentration and the inverse (most common-vocabulary surahs). Verify the prompt's specific claim about Q26 al-Shuʿarāʾ.

## 1. Context ingested

Required reading before pre-reg:
- `journal/zipf-per-surah-run-1.md` — H14 cautionary tale: Zipf α was 96% length-determined. Length confound for rare-root metrics suspected upfront.
- `journal/hapax-catalog-run-1.md` — H-NEW-7 parent finding: hapax-final p = 7.35e-29; baseline 395 root hapaxes.
- `findings/phase-b-hypotheses/hapax-slot-mechanism.md` — H-NEW-23 mechanism within-verse slot control z = +10.61; eschatological cluster.
- `data/morphology/root-stats.csv` — 1,642 distinct global roots (matches prompt's "~1,636").
- `findings/phase-b-hypotheses/root-cartography.md` — exploratory headline candidates.
- `docs/methodology.md` §7 rules-tuple format.

## 2. Pre-registration design

5-test Bonferroni family with α_bon = 0.01:
- T1: heterogeneity vs uniform null (Σz²)
- T2: length confound (Spearman ρ)
- T3: Q26 al-Shuʿarāʾ rank claim (one-sided pre-committed bottom-15)
- T4: H-NEW-23 hapax-final cross-reference (Spearman ρ)
- T5: genre ANOVA

Locked PRIMARY metric is `geom_mean_freq` (geometric mean of global root frequencies). Rare = global count ≤ 5; Common = ≥ 100. Genre coding identical to H-NEW-23.

Pre-reg SHA-256: d3f1fcce6fd0c750b9b21525acd95034c911dfa50d7ece153df41e5db3bfb60a

## 3. Implementation

Pure Python stdlib, ~310 lines. Single script `h_new_91_rare_root_density.py` with seed 20260415, 10,000 perms per permutation test. Total runtime ~6 minutes (T1's 10k full-corpus shuffles are the bottleneck).

Pipeline:
1. Parse QAC for STEM tokens with ROOT field → 49,968 tokens, 1,642 roots, 114 surahs.
2. Cross-check QAC-rebuilt root counts against root-stats.csv: **0 mismatches** across all 1,642 roots.
3. Per-surah metrics: arithmetic mean, geom mean, median, rare_density_5, hapax_density, common_only_density.
4. Per-surah `null_z` via Monte Carlo sampling (1000 iters per surah from global token distribution at exact N_s).
5. Test 1: aggregate Σz² and permutation p (10k full-corpus root-label shuffles).
6. Test 2: Spearman ρ vs log N_s.
7. Test 3: Q26 ranking on geom_mean_freq.
8. Test 4: cross-reference H-NEW-23 hapax-final per-surah rates.
9. Test 5: permutation ANOVA across 5 genres for both `geom_mean_freq` and `rare_density_5`.

## 4. Sanity checks

- QAC root counts match root-stats.csv to the integer (0 mismatches across 1,642 roots → confirms parsing rule is identical to project standard).
- Total root-bearing STEM tokens: 49,968 (matches H-NEW-29's 49,968).
- 114/114 surahs have at least 1 root token (no surah excluded for insufficient data).
- Q26 has 821 root-bearing STEM tokens, 265 distinct roots.

## 5. Headline results

| Test | Result | Verdict |
|---|---|---|
| T1 heterogeneity | Σz²=862.3 vs null 112.8±17.0; p < 0.0001 | PASS |
| T2 length confound | ρ = +0.554 (length-confounded) | DIAGNOSTIC: use null_z |
| T3 Q26 ≤ rank-15 | Q26 rank = 97/114; resid 22/26 in q4 | **FAIL** (FALSIFIED) |
| T4 hapax-final XR | ρ = +0.668; p < 0.0001 | PASS (strong) |
| T5 genre ANOVA | F(geom_mean_freq) = 12.98; F(rare_density_5) = 11.22; p < 0.0001 | PASS |

**Composite: PARTIAL-PASS (3/4 substantive)**.

## 6. Surprises

### Q26 al-Shuʿarāʾ FAILURE — falsified the prompt's directional claim

Q26 was the prompt's specific named "narrative-vocabulary" surah. Pre-committed test: Q26 in bottom-15 by geom_mean_freq.

Result: Q26 ranks 97/114 (above median!). Length-residualized: 22/26 in its q4 quintile (bottom of the long-surah common-vocab list). null_z = +3.43 (POSITIVELY skewed toward common vocabulary).

The actual length-controlled rare-vocab leaders among long surahs are Q20 Taha (z = -4.39), Q18 al-Kahf (z = -4.93), Q12 Yūsuf (z = -3.56) — exactly the canonically narrative-heavy surahs.

Why was Q26 mis-targeted? Q26 al-Shuʿarāʾ is structured as **seven repeated prophet-stories** with the SAME closing refrain ("inna fī dhālika la-āyatan...") seven times. The repeated refrain recycles a fixed set of common roots, inflating common-vocabulary density. Q26 is "narrative" in literary form but "common-vocabulary" in lexical statistics — the opposite of the prompt's intuition.

This is a clean falsification of a specific named-surah claim. It is the kind of negative result that the pre-registration discipline is designed to surface.

### The eschatological-slot-engineering cluster grows

H-NEW-91 adds to the cluster:
- H-NEW-19 (elision-eschatology): iltifāt + ellipsis density peaks eschatological
- H-NEW-23 (hapax-slot mechanism): hapax-final rate eschatological 0.077 vs legal 0.002 (38× ratio)
- **H-NEW-91 (this finding)**: rare-root density eschatological 0.134 vs legal 0.027 (5× ratio)
- Cross-correlation T4: rare_density_5 ↔ hapax-final-rate ρ = +0.668 across 87 surahs

The cluster is now a quadruple-test convergence with explicit cross-correlation between two of its members.

### Q56 al-Wāqiʿah is the strongest length-controlled rare-vocab outlier

Among all 114 surahs, Q56 al-Wāqiʿah has the strongest length-controlled rare-vocab z-score: **z = -5.59** at N_s = 255. Classically, Q56 is recognized as a uniquely lexically dense eschatological surah; the statistical signal confirms classical perception. Worth a follow-up H-NEW-91d deep-dive on what specific roots drive Q56's rarity.

### Q3 Āl ʿImrān is the strongest length-controlled common-vocab outlier

z = +8.52 at N_s = 2274. Despite its size and topical breadth, Q3 al-ʿImrān recycles the most-frequent legal/theological roots more heavily than uniform null predicts. This is consistent with Q3's status as a Medinan didactic/legal-narrative surah where the doctrinal vocabulary is intentionally conservative.

## 7. Length confound — the lesson from zipf-per-surah holds

I expected length confound from Day 1 (per the H14 zipf-per-surah lesson) and pre-registered Test 2 specifically. ρ = +0.554 — substantial but lower than the +0.962 that hit Zipf α. The lower ρ is because `geom_mean_freq` is a per-token average (not a tail-shape statistic), so it has a less brutal small-N bias than OLS-Zipf.

Two complementary length controls were applied:
1. Per-surah `null_z`: Monte Carlo z-score under uniform null at exactly N_s tokens. Automatically length-controlled.
2. Length quintiles: 5 equal-N bins by log N_s; within-bin rank.

Both produce convergent rankings. The per-surah `null_z` is the cleaner effect-size and is reported in §7 of the findings.

## 8. Decisions made BEFORE running (pre-reg log)

All locked in `findings/phase-b-hypotheses/h-new-91-rare-root-density-prereg.md` §Garden-of-forking-paths-log:
- Geom mean (not arithmetic) as PRIMARY.
- Rare ≤ 5, Common ≥ 100 thresholds.
- Q26 one-sided downward direction.
- Genre coding from H-NEW-23.
- Bonferroni k=5, α_bon=0.01.
- Surah-1 al-Fātiḥah included (not filtered).
- Basmala-counted-only-in-surah-1.
- Permutation seed 20260415, 10,000 perms.

## 9. Decisions during analysis (post-hoc, transparently flagged)

- §3 of findings adds a per-quintile-top-3 breakdown — descriptive expansion, not a new test.
- The "Q26 explained by 7-fold refrain" reading in §3 is post-hoc literary interpretation; the statistical falsification of T3 is the pre-registered claim.
- §7 ranking by null_z is a descriptive use of T1's pre-computed numbers.

## 10. Outputs

- `findings/phase-b-hypotheses/h-new-91-rare-root-density-prereg.md` — pre-reg
- `findings/phase-b-hypotheses/h-new-91-rare-root-density.md` — full findings writeup
- `findings/phase-b-hypotheses/csv/h-new-91.json` — summary JSON
- `findings/phase-b-hypotheses/csv/h-new-91-per-surah.csv` — per-surah table
- `scripts/h_new_91_rare_root_density.py` — reproducible script
- `journal/h-new-91-run-1.md` — this file

## 11. Follow-up hypotheses queued (in findings §11)

- **H-NEW-91b**: proper-noun-inclusive variant (predict Q26 rises substantially when prophet PNs are counted).
- **H-NEW-91c**: baseline-corpus rarity comparison (Bukhari/Jāḥiẓ length-matched slices).
- **H-NEW-91d**: Q56 al-Wāqiʿah root-driver decomposition.
- **H-NEW-91e**: long-narrative rare-root concentration test for Q12/Q18/Q20.
- **H-NEW-91f**: Q26 refrain-deletion test — quantify common-vocab inflation contribution.

## 12. Reflection

The headline finding is **negative for the prompt's specific Q26 claim, positive for the broader pattern**. The eschatological slot-engineering cluster gains a fourth independent test (H-NEW-91 → ρ = +0.668 with H-NEW-23) and a 5× quantitative gap with legal surahs.

The prompt's intuition that "rare-root concentration is a real surah-level signal" is **vindicated**: heterogeneity Σz² of 862 vs null 113 is a >40σ effect. The intuition that Q26 al-Shuʿarāʾ is the exemplar is **mis-targeted**: Q26's seven-fold refrain structure makes it a common-vocab outlier, not a rare-vocab outlier. The actual exemplars are Q12 Yūsuf, Q18 al-Kahf, Q20 Taha (long-narrative quintile q4 leaders) and Q56 al-Wāqiʿah (length-controlled outlier z = -5.59).

The convergence of (i) hapax-FINAL placement engineering (H-NEW-23), (ii) per-surah rare-root density clustering (H-NEW-91), and (iii) eschatological-genre dominance in BOTH puts the eschatological "rhetorical-payload concentration" claim on a multi-axis empirical foundation.
