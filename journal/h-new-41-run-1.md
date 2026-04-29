# H-NEW-41 run 1 — process journal (post-audit-032 amendments)

**Date:** 2026-04-15
**Agent:** h-new-41-specialist
**Pre-reg:** findings/phase-b-hypotheses/h-new-41-root-combinatorial-saturation-prereg.md
**Amendments:** 41-A (LOO posctrl) + 41-B (SHA-256 lock, fallback C = QAC ∪ Mutanabbī-only)
**Script:** scripts/h_new_41_root_combinatorial.py
**Seed:** 20260415

## Timeline

### Phase 1 — initial run (pre-amendments)
1. Read pre-reg. Built a broader fallback C (QAC + prose-extracted roots
   from mutanabbi + jahiz + sira + bukhari + six Mu'allaqāt/Dīwāns,
   |C|=8,130) per the pre-reg's "union" fallback clause.
2. Ran pipeline. Results (viewed):
   - |Q|=1,602, coverage Q/C = 0.197
   - 5 / 12 Q cells crossed α_per_cell at 1.39e-3
   - Original MW-5: max |z_M| = 4.72 (Mutanabbī in C, no LOO)
   - Under original MW-5 rule: NULL-BROKEN
3. Wrote findings + journal reflecting NULL-BROKEN.

### Phase 2 — audit-032 amendments filed
Coordinator delivered amendments 41-A (LOO posctrl) and 41-B (SHA-256 lock
+ fallback C = QAC ∪ Mutanabbī-only-roots). Both are tightening-only.

### Phase 3 — amendment-compliant re-run
4. Disclosed that prior-run results had been viewed (garden-of-forking-
   paths honesty). This is unavoidable because amendments were filed mid-
   execution; I apply them exactly as written and do NOT use prior
   numerics to adjudicate the new verdict.
5. Pinned SHA-256s per 41-B:
   - QAC: `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` ✓
   - Mutanabbī: `d1bbed14b25111436af4149bacb5ff7cf3f400979a16e13cc45bf0d9a7ca89b9` ✓
   Lane, Wehr: not available.
6. Rebuilt script with:
   - C = QAC ∪ Mutanabbī-only (|C|=2,213)
   - Primary null for Q: 10k size-1,602 uniform subsets of C
   - Posctrl null for M: 10k size-|M| uniform subsets of C\M_candidate
     (LOO per 41-A). |C\M| = 1,115, |M| = 1,098.
7. Pre-declared coherent reading of amendment 41-A verdict text (n=0
   PASS / 1≤n≤11 PARTIAL / n=12 NULL-BROKEN), because the amendment text
   is literally inconsistent as written. Documented in the script's
   garden-of-forking-paths log BEFORE viewing re-run numeric output.
8. Ran amended pipeline. Console:

```
[SHA] QAC: ... -> True
[SHA] Mut: ... -> True
[step1] QAC Q roots: 1602
[step2] Mutanabbī candidate roots minfreq>=2: 1098
[step2] Mutanabbī-only roots (not in Q): 611
[step2] |Q|=1602, |M_only|=611, |C|=2213
[subA] Q / C coverage = 0.7239
[null Q]   10k size-1602 uniform subsets from |C|=2213
[null M-LOO] 10k size-1098 uniform subsets from |C\M|=1115
[MW-5 41-A] posctrl cells failing (|z|>=2): 11/12, worst |z_M|=71.69
[verdict raw] Q significant cells = 1/12
[verdict] >>> EXPLORATORY (partial-posctrl downgrade) <<<
```

9. Encountered and fixed a dtype overflow in the token-weighted accumulation
   (int8 overflow when summing Quran token frequencies × feature indicator).
   Rerun confirmed same verdict structure.

10. MW-7 internal-error checks:
    - SHA-256 verification returns True for both source files.
    - |Q|=1,602 matches prior run.
    - C_feats shape (2,213, 12); C\M shape (1,115, 12).
    - LOO null σ extremely small (e.g. 0.0006 for guttural_coronal_1-2)
      — this is numerically correct: draws of 1,098 from a pool of 1,115
      leave only 17 elements' worth of variance.
    - Output JSON parses, all 12 cells present, all fields populated.

11. Updated findings file with amendment-compliant results and mechanism
    interpretation of the degenerate-LOO-null artifact.

## Final verdict

**EXPLORATORY (partial-positive-control downgrade)** per amendment 41-A's
intermediate-cells branch.

- 1 / 12 Q cells crosses α_per_cell = 1.39×10⁻³: `guttural_coronal_1-2`
  at z_Q = −6.94, p ≈ 1×10⁻⁴.
- 11 / 12 posctrl cells fail LOO |z_M| < 2.0, but the failure is a
  degenerate-null artifact (|C\M| ≈ |M|).
- Not promoted; reported as exploratory only.

## Data-availability constraints

- **Primary:** No Lane's / Wehr root index on disk. Amendment 41-B's
  explicit fallback (QAC ∪ Mutanabbī-only) was used.
- **Secondary:** The narrowness of the fallback C (|C|=2,213) combined
  with the LOO rule makes the positive-control null near-deterministic,
  inflating |z_M|. A Lane-curated C (|C| ≈ 6,500–7,500) would give
  |C\M| ≈ 5,400–6,400, restoring normal null variance.
- **Tertiary:** Heuristic stemmer (diacritic-strip → longest-prefix-strip
  → longest-suffix-strip → drop weak letters → take strong trigram) has
  QAC-overlap precision ≈ 0.43 on Mutanabbī. Minfreq=2 mitigates noise.

## Recommendations

1. Before any further H-NEW-41-family test, acquire a Lane or Wehr root
   index and pin its SHA-256. This is the single highest-value data
   acquisition for this hypothesis.
2. If a Lane-based re-run is mounted, it must be pre-registered anew; do
   not reuse this hypothesis's alpha budget.
3. The guttural_coronal_1-2 exploratory hit (z_Q = −6.94, token-weighted
   z = −4.87) is worth a follow-up pre-registration that uses a
   phonotactic-structure-preserving null (Frisch/Pierrehumbert style)
   rather than uniform-subsample-of-C.

## Files produced / updated

- /Users/grey/Downloads/quran/scripts/h_new_41_root_combinatorial.py (amended)
- /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-41.json (amended)
- /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-41-rootlists.json
- /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-41-root-combinatorial-saturation.md (amended)
- /Users/grey/Downloads/quran/journal/h-new-41-run-1.md (this file, amended)
- /Users/grey/Downloads/quran/journal/h-new-41-run-1.log (stderr log, amended run)
- /Users/grey/Downloads/quran/journal/h-new-41-run-1-prior-to-amendments.log (preserved for audit)
