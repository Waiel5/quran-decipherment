# Journal — H-NEW-2680, pillar-law joint conjunction

**Date**: 2026-08-07
**Investigator**: Waiel Al-Shujaa
**Pre-reg**: `findings/phase-b-hypotheses/prereg-h-new-2680-pillar-conjunction.md`
**Pre-reg SHA-256**: `012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94` (verified at runtime by all three scripts)
**Seeds**: 20260509 primary / 20260519 replication

## Timeline

| UTC | Step |
|---|---|
| — | Pre-flight: skill, INVESTIGATION-PROTOCOL, HANDOFF/01, the four pillar-law files, CROSS-FINDING-INDEX (handles `cf-025-formal`, `cf-026-formal` used throughout). |
| — | Calibration probe (scratch, discarded): verified the four statistics reproduce their published canonical values through the code paths to be reused, and measured 0.48 s per synthetic corpus so N could be locked. No law-satisfaction criterion was evaluated on any synthetic corpus before the pre-reg was written. |
| — | Pre-registration written and SHA-locked. Two nulls declared, forced by the §1 invariance table. |
| 01:19:17Z | `h-new-2680.py` — NULL-A (N=10 000), NULL-B, NULL-B′ (N=2 000 each), both seeds, D4 diagnostic, baseline control. 1 332 s. → `runs/h-new-2680/20260807T011917Z/` |
| 01:24:04Z | `h-new-2680b.py` — repaired L1 transport + contiguity diagnostic. → `runs/h-new-2680b/20260807T012404Z/` |
| 01:43:27Z | `h-new-2680c.py` — NULL-C, both seeds. → `runs/h-new-2680c/20260807T014327Z/` |

Two smoke runs at reduced N are preserved under `runs/h-new-2680-SMOKE/`. **No run directory has been deleted.**

## Decision points and garden-of-forking-paths log

1. **Two nulls rather than one.** The invariance table (pre-reg §1) was written before any null was coded and shows that surah-order permutation — the null of Pillar 2 — leaves the other three laws exactly unchanged. One null could not cover four laws.
2. **LENIENT tier primary.** Setting each bar at the corpus's own observed extremity would guarantee near-zero synthetic survivors by construction. Declared in the pre-reg before the run.
3. **L2 optimality ratio excluded from the criteria.** Under a homogenising null every path length converges and the ratio → 1.0, spuriously certifying "near-optimal" on structureless corpora. A tightening, declared in advance. Borne out: NULL-B ratio 1.0755 ± 0.004 on corpora with no content structure at all.
4. **L3 operationalised on 5 classes, not the 6 the task named.** `cf-026-formal` (2026-05-29) already retired the 6th (ring-composition, Q002-F-07) on the evidence of H-NEW-2220/2290. Testing 6 would have tested a withdrawn member.
5. **Pre-registration defect found at runtime.** STRICT L2 was locked as `p_perm < 1/2001`, which the `(n_le+1)/(n_perm+1)` estimator can never satisfy. The canonical corpus fails its own STRICT L2 cell, so the STRICT 4-way joint is void. **Not repaired** — the repair (`≤`) is a loosening and requires ratification. LENIENT was pre-registered as primary and is unaffected.
6. **L1 baseline transport failed its own control-of-the-control.** The pre-registered single-word-type marker search returned `n_candidates: 0` on the Qurʾān itself. Repaired in a separate, labelled script (`h-new-2680b.py`) as a greedy marker-class search of up to 14 members; the pre-registered run's unrepaired output stands on disk unmodified. The repair recovers the muqaṭṭaʿāt on the Qurʾān at p_bonf = 4.7×10⁻¹³.
7. **NULL-C is post-hoc** and labelled so (MW-7 single-test ceiling). It was constructed only after the pre-registered arms showed why each fails, though it follows directly from the pre-registered invariance table. It imports `h-new-2680.py` as a module so the code paths are verbatim, not re-implemented.
8. **Two diagnostics added mid-study, both capable only of undermining the study's own result**: the L2 length-confound probe (added after the smoke run showed NULL-B's L2 marginal at 1.000) and the contiguity/offset-cut control. Both were added because they could falsify a conclusion, not support one.
9. **A bidi hazard, recorded because it silently corrupts Arabic regexes.** A literal Arabic diacritic character class written into `h-new-2680b.py` was reordered on write, turning `[ؐ-ؚ][ً-ٟ][ٰ]…` into ranges that swallow the entire alphabet — the normaliser returned zero words and failed loudly. Rewritten with explicit `\uXXXX` escapes. `h-new-2680.py` was unaffected (verified by codepoint dump). Any future script handling Arabic character classes should use escapes.

## Instrument reproduction (canonical corpus)

| Law | This run | Published |
|---|---|---|
| L1 | 24/29, K=35, p = 9.48×10⁻¹² | 24/29, K=34, p = 3.17×10⁻¹² |
| L2 | L = 85.7597, z = −11.70, ratio 1.1063 | L = 85.760, z = −11.46, ratio 1.107 |
| L3 | 5/5 (z = +4.77 / +2.65 / +6.49 / +3.90 / +6.25) | 5/5 (+4.76 / +2.685 / +6.41 / +3.86 / +6.008) |
| L4 | rank-1 43/89, binomial p = 0.832 | 42/89 (JSON) |

## Incidental finding requiring another file's correction

An independent rebuild of the H-NEW-111 pipeline (reproducing L_mushaf, L_Nöldeke and the null to four decimals) shows that `h-new-111-fisher-rao-mushaf.md` mis-transcribes its length-sorted sanity anchor as 107.27 for both directions. Its own `csv/h-new-111.json` records 91.027805 / 90.301441, which the rebuild reproduces exactly. The write-up's conclusion "confirms MW-1 length control is working" is false: length-sorted descending is z = −8.66, and the mushaf's margin over pure length-sorting is 2.80 σ. **Flagged, not edited — correcting another finding's file is the ledger keeper's call.** See `h-new-2680-pillar-conjunction.md` §8.1.

## Concurrent work that lands on the same material

Two adjacent lines of work landed while this test ran, and both are integrated into the finding rather than ignored:

- **`h-new-2710-title-density-retest.md`** withdrew and replaced Pillar 4 (H-NEW-1820), citing this study's D4 diagnostic as the prior art that triggered it. Its Null B matches candidate title-roots on **frequency *and* dispersion** where D4 matched on frequency alone, and it refines D4's rate ratio 1.68 down to **1.285**, with median rank indistinguishable (p = 0.76). **That is the tighter control and it supersedes D4's effect size**; the *direction* (dependence, not independence) agrees across both. Recorded in §9.1 of the finding. The conjunction now has three standing pillars, not four.
- **`h-new-2670-joint-conjunction.md`** reached ARTEFACT-OF-CONSTRAINT-STACKING on the muqaṭṭaʿāt subset-intersection question (W = 7 / 40 116 600, p = 1.745×10⁻⁷ under the locked rule; q′ = 0.248 under a stricter post-observation control). Convergent methodological conclusion from the opposite end; cross-referenced in §13.

Also noted: commit `30f05aeb1` (another line of work) swept this study's pre-registration and main script into the repository before the results landed. Not done by this line of work, and it does not affect the SHA-lock — the pre-reg hash `012ca709…` is embedded in all three scripts and verified at runtime by each.

## Outputs

- Finding: `findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`
- Scripts: `findings/phase-b-hypotheses/scripts/h-new-2680.py`, `h-new-2680b.py`, `h-new-2680c.py`
- Runs: `findings/phase-b-hypotheses/runs/h-new-2680{,b,c}/` — each with `result.json` and `manifest.json` (frozen-input SHA-256s)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
