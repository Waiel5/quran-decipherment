# H-NEW-127 — Run 1 journal

**Date**: 2026-04-17
**Specialist**: h-new-127-specialist
**Pre-reg SHA-256**: `bc42449238e4eb67c3b54e234d2f392d093c9993622261d510d8ab7a5fe29e95`
**Seed**: 20260417

## Timeline

1. **Orientation**. Read HANDOFF/04-DISCIPLINE.md, parent finding H-NEW-111 (surah-level Fisher-Rao PASS-DIRECTED, p < 10⁻⁴, ratio 1.107), and the parent's pre-reg + script.
2. **Pre-reg written and locked**. Five surahs (Q 2, 7, 12, 36, 55), K=300, α=0.5, PERMS=10,000, α_bon=0.01 (Bonferroni-5), MW-5 = length-sort on Q 55. File SHA hashed into script for tamper-evidence.
3. **Script written and run**. Mirrors H-NEW-111's algorithmic structure (QAC STEM parsing → top-K roots → Dirichlet smoothing → L1 normalize → Fisher-Rao distances → random-permutation null → greedy-NN + 2-opt).
4. **Results captured in `findings/phase-b-hypotheses/csv/h-new-127.json`**.

## Raw per-surah results

| Sura | n_v | L_canon | null μ  | null σ | z      | p      | ratio | pass |
|------|-----|---------|---------|--------|--------|--------|-------|------|
| 2    | 286 | 104.30  | 108.49  | 0.408  | −10.26 | 0.0001 | 1.22  | PASS |
| 7    | 206 | 65.80   | 68.27   | 0.304  | −8.11  | 0.0001 | 1.21  | PASS |
| 12   | 111 | 32.79   | 34.26   | 0.218  | −6.72  | 0.0001 | 1.19  | PASS |
| 36   | 83  | 19.13   | 19.52   | 0.137  | −2.82  | 0.0046 | 1.21  | PASS |
| 55   | 78  | 13.64   | 11.25   | 0.442  | +5.39  | 1.0000 | 2.49  | FAIL (reversed) |

## MW-5 (pre-committed) on Q 55

- L_canon(55) = 13.64
- L_length_sorted_token = 8.58  → MW-5 FAIL (8.58 < 13.64)
- L_length_sorted_char = 7.94  → MW-5 FAIL

## Mechanism of Q 55 reversal

Q 55 contains the refrain "fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān" 31 times (31 of 78 verses), interleaved with content verses. Refrain verses are near-identical in Fisher-Rao distance (D ≈ 0 among them). The canonical alternating structure maximizes consecutive-verse distance; any order that clusters the refrains (including length-sort, since all refrain verses are similar in length) dramatically shortens the path.

Confirmation: 72 of 78 verses have text length ≤ 40 chars; 31 are the exact refrain.

## Pre-reg compliance audit (self)

- [x] Direction pre-registered: "canonical < random, one-sided lower-tail" — pre-committed before run.
- [x] K = 300 locked before run.
- [x] Bonferroni-5 declared in YAML frontmatter.
- [x] MW-5 pre-committed to length-sort on Q 55.
- [x] Failure modes explicitly listed: NULL-STRONG (n_pass=0), NULL-WEAK (n_pass∈{1,2}), STRONG-REPL (n_pass≥3), INSTRUMENT-BROKEN (MW-5 fail).
- [x] Seed 20260417 same as parent.
- [x] Script hashes pre-reg to stderr on every run.
- [x] JSON artifact written to `findings/phase-b-hypotheses/csv/h-new-127.json`.
- [x] No post-hoc feature-space expansion (did not add K-robustness, did not change α).

## Specialist-judgment-override check

I did NOT override the team-lead's method spec. The pre-reg surah list (5), K=300, α=0.5, MW-5 choice (length-sort on Q 55) were all as specified in the task. On encountering the Q 55 result (z=+5.39, p=1.0 reversal; MW-5 also fails), I did NOT adjust the Bonferroni correction, replace the MW-5 control, or re-select surahs. I honored the pre-committed INSTRUMENT-BROKEN verdict.

## Bonferroni-asymmetry note

No tightening and no loosening occurred. k=5 stays at k=5. Despite 4 strong passes + 1 extreme reversal, I did not propose dropping Q 55 from the family post-hoc — that would be loosening (smaller k → smaller α_raw-equivalent = more power). Ratification not needed since no change made.

## Substantive finding (reported honestly)

Even with INSTRUMENT-BROKEN headline, the data is clear:
- 4 of 5 surahs independently replicate the H-NEW-111 fractal hypothesis with extreme significance.
- Q 55 exhibits the OPPOSITE behavior, interpretable as deliberate anti-geodesic design for hymnic/refrain surahs.

Per DISCIPLINE §honesty-over-cheerleading: both findings published with equal prominence in `h-new-127-verse-fisher-rao-fractal.md`. PASS-DIRECTED promotion does NOT apply (INSTRUMENT-BROKEN vetoes). Follow-up pre-regs queued: H-NEW-127.1 (sound MW-5), H-NEW-127.2 (different 5-surah set), H-NEW-128 (anti-geodesic hypothesis test on other refrain surahs).

## Runtime notes

- QAC parse: ~2s
- Per-surah D-matrix build: ~0.1s–5s (quadratic in n_verses)
- Null (10,000 perms): <5s per surah on medium sizes; ~25s on Q 2 (n=286)
- Greedy-NN + 2-opt: dominant cost on Q 2 (n=286, 2-opt is O(n^2) per pass × 50 passes × 286 starts)
- Total runtime: ~3–5 minutes

## Artifacts

- Pre-reg: `findings/phase-b-hypotheses/h-new-127-prereg.md`
- Script: `scripts/h_new_127_verse_fisher_rao.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-127.json`
- Findings: `findings/phase-b-hypotheses/h-new-127-verse-fisher-rao-fractal.md`
- Journal: this file.
