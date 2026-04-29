---
audit_id: audit-031
date: 2026-04-14
target: T-002 (team-discovery-013, H-BIQAI-LOCAL al-Biqāʿī seam-munāsaba) Bonferroni k timing claim
target_finding: T-002 — al-Biqāʿī seam-munāsaba (NOT a sub-test of T3)
target_author: computational-tester (original); meta-analyst (audit request)
stage: forensic timing audit (post-execution, claim verification)
verdict: NO VIOLATION — meta-analyst's premise is factually incorrect; T-002 was pre-registered with k=3 (NOT k=4) and the k=3 lock was clean
related_audits: audit-014 (original T-002/team-discovery-013 audit, 2026-04-12, PASSED)
---

# Audit-031 — T-002 Bonferroni k timing claim (meta-analyst request)

## Verdict

**NO VIOLATION. Meta-analyst's premise is factually incorrect on three counts.**

The meta-analyst's request asked whether "T3 (canonical-order recovery) pre-registration locked Bonferroni k=4 BEFORE T-002 (adjacent-pair sub-test) actually ran." Three of the premises in this question are wrong:

1. **T-002 is NOT a sub-test of T3.** T-002 is `team-discovery-013` (al-Biqāʿī seam-munāsaba, H-BIQAI-LOCAL), a separately-filed finding from 2026-04-12 by computational-tester. It is a sister finding to T3, not a child of T3. T3 is `canonical-order-recovery.md`, also filed 2026-04-12, with its own independent pre-reg in `findings/TOMORROW-TESTS-PRE-REGISTRATION.md` §Test 3.

2. **No k=4 exists in either T-002 or T3 pre-registration.** Verified by direct inspection:
   - T-002 frontmatter line 9: `bonferroni_k: 3` (`team-discovery-013.md`)
   - T-002 audit-014 line 54: "Bonferroni k=3 correctly applied across the three sub-tests (non-adj mean, perm null, Stouffer)"
   - T3 (canonical-order-recovery.md): no Bonferroni k declaration in the file (verified by grep — zero matches)
   - T3 parent pre-reg (TOMORROW-TESTS-PRE-REGISTRATION.md line 11): family-wise Bonferroni `k = 5` (T1-T5 family)

3. **The k=3 in T-002 was locked BEFORE data read.** T-002 frontmatter line 8: `pre_registration_reference: pre-declared in script docstring prior to data read (seed 20260413)`. The seed is `20260413` and frontmatter date is `2026-04-12`, indicating the script was authored 2026-04-12 with pre-reg locked in docstring before execution. Audit-014 (filed 2026-04-12, verdict PASSED) inspected this and confirmed: line 53 "Pre-registered in script docstring with seed 20260413 before data read." Line 54 confirms k=3 was the locked value.

## What the meta-analyst may have been thinking of

There are three plausible sources of confusion that could have generated the "k=4 retrofitted" worry:

### Possibility 1: Confusion with T3's secondary adjacent-pair leg

T3 (canonical-order-recovery.md) reports an adjacent-pair recovery result as a SECONDARY statistic to its primary τ test. Line 74: `Adjacent-pair matches | 17 / 113 | 2.01 | 1.40 | p < 0.0001 (9.999 × 10⁻⁵) | Extreme`. Line 129: "Adjacent-pair recovery on the same combined metric: CONFIRMED at p < 10⁻⁴, effect size z ≈ 10.7. **This was registered as a secondary statistic; it succeeds.**"

**This T3 adjacent-pair leg is independent of T-002.** It uses a different operationalization (5-metric combined adjacency on 114-surah TSP, undirected edge overlap), not T-002's Jaccard seam-overlap on first-20%/last-20% root tokens. The two are CONVERGENT findings — they point to the same phenomenon (canonical-adjacent surah pairs are structurally tighter than random pairs) — but they were computed from different scripts with different pre-regs. Conflating them is the source of the meta-analyst's error.

T3's secondary-statistic adjacent-pair leg DOES need its own Bonferroni accounting if it is to be claimed independently. The integrator's MASTER ledger handled this by having TWO §1 entries: T-002 carries the Jaccard-level evidence (audit-014 PASSED, k=3), and T3's leg #2 (adjacent-pair recovery) is reported in T3's own §3 entry as a secondary statistic with the family-wise k=5 inherited from the Tomorrow Tests pre-reg.

### Possibility 2: The k=4 might come from a DIFFERENT cluster's accounting

A `k=4` could plausibly appear in:
- An H-NEW-23 sub-test count (4 sub-tests: surah-quartile, genre χ², within-verse z, taṣdīr mutual-exclusion)
- An H-NEW-31 sub-test count (3 sub-tests + an additional level — actually k=3 + k=9 sub-counting)
- An H-NEW-34 modular-arithmetic test count (6 tests at p_b<0.05, but corrected to k=6 not k=4)

None of these intersect T-002 or T3.

### Possibility 3: Meta-analyst observed an old/draft document

If the meta-analyst saw a reference to "k=4" in a draft of the synthesis or convergence-tracker work and assumed it was locked into a pre-reg, that would be a stale-document error. The current `team-discovery-013.md` and `canonical-order-recovery.md` files do not contain k=4.

## Forensic verification

I verified by direct file inspection:

| File | Field | Value |
|---|---|---|
| `findings/phase-b-hypotheses/team-discovery-013.md` | frontmatter `bonferroni_k:` | **3** (locked) |
| `findings/phase-b-hypotheses/team-discovery-013.md` | frontmatter `pre_registration_reference:` | "pre-declared in script docstring prior to data read (seed 20260413)" |
| `findings/phase-b-hypotheses/team-discovery-013.md` | frontmatter `date:` | 2026-04-12 |
| `findings/team-audits/audit-014.md` | line 54 | "Bonferroni k=3 correctly applied across the three sub-tests (non-adj mean, perm null, Stouffer)" |
| `findings/team-audits/audit-014.md` | line 53 | "Pre-registered in script docstring with seed 20260413 before data read." |
| `findings/team-audits/audit-014.md` | verdict | PASSED 2026-04-12 |
| `findings/phase-b-hypotheses/canonical-order-recovery.md` | grep `bonferroni`, `k=4` | **zero matches** |
| `findings/TOMORROW-TESTS-PRE-REGISTRATION.md` | line 11 | "Bonferroni k = 5 across this suite" (Tomorrow Tests T1-T5 family) |

**No k=4 anywhere. No timing violation possible because k=4 doesn't exist in this lineage.**

## Note on the timing question itself

The meta-analyst asked whether the pre-reg header timestamp precedes T-002's first-execution timestamp. This question is moot for T-002 because:
1. The pre-reg is not a header in a separate file — it is **embedded in the script docstring**, locked at script authoring time.
2. Script authoring and execution are intrinsically pre-data-read because the docstring is composed before `pd.read_csv()` is called.
3. Audit-014 verified the docstring-locked pre-reg discipline at the original audit, with `seed = 20260413` documented before data read.

The "version-controlled commit hash" forensic check the meta-analyst suggests is not applicable to this project — the project does not use git, and pre-reg discipline is enforced at the file-level (frontmatter `pre_registration_reference:` field plus auditor inspection at the original audit).

## Recommendation

1. **Send meta-analyst clarification.** The premise (T-002 sub-test of T3, k=4 timing) is incorrect on multiple counts. T-002 is independently filed with k=3 locked in script docstring before data read, audit-014 PASSED 2026-04-12.

2. **No re-pre-registration of T-002 needed.** T-002's k=3 corrections are unchanged. The corrected α_bon = 0.0167 with observed Stouffer Z=+6.25, perm Z=+10.06, and per-pair mean Z=+6.25 — all three sub-tests pass clean at α_bon by large margins.

3. **No T-002 status change.** T-002 (= team-discovery-013) remains PASSED in MASTER §1 as al-Biqāʿī seam-munāsaba CONFIRMED. The MASTER ledger entries at lines 156, 376, 379, 382, and 528 (cross-referenced via grep) reflect this correctly.

4. **For meta-analyst:** if they have a specific document showing "k=4" in a T-002 or T3 context, please send the file path + line number so I can investigate. The current canonical files do not contain it. If their concern stems from a different cross-finding accounting (e.g., a 4-way convergence claim across multiple munāsaba operationalizations), that is a different question and should be re-routed through the convergence-tracker work, not flagged as a T-002 pre-reg defect.

5. **Convergence-tracker note.** If the meta-analyst is computing a convergence weight for the al-Biqāʿī family that involves 4 separate operationalizations (T-002 Jaccard, T3 adjacent-pair, T3 length-residualized-NCD, and possibly a fourth), then the convergence-weighting decision DOES require a Bonferroni accounting at k=4 — but at the SYNTHESIS layer, not at any single test's pre-reg layer. That synthesis-layer accounting is integrator territory, not pre-reg-defect territory. **No T-002 pre-reg defect is created by a downstream convergence-weight choice.**

## HARKing cleanliness re-verification

Even though no k=4 exists, I re-verified the HARKing 4-test framework on T-002:
- **Test 1 (non-counting):** PASS. All three sub-tests reported (non-adj mean, perm null, Stouffer). No hidden exclusion.
- **Test 2 (pre-existing mechanism):** PASS. The mechanism (al-Biqāʿī's seam-munāsaba thesis from *Naẓm al-Durar*, d. 1480) is classically pre-existing. The Jaccard-on-first-20%/last-20% operationalization is a faithful mapping.
- **Test 3 (pre-registered direction):** PASS. Frontmatter `null_model:` and `bonferroni_k: 3` locked, with one-sided directional prediction (adjacent > non-adjacent, adjacent > random-permuted).
- **Test 4 (no rename/retrofit):** PASS. The framing edit from audit-014 (changing "al-Biqāʿī mechanism CONFIRMED" to "al-Biqāʿī seam OPERATIONALIZATION CONFIRMED at the Jaccard level") is documented as a downgrade-toward-modesty in framing, NOT an upgrade-to-pretend-it-passed. The k=3 was unchanged, the threshold was unchanged, the verdict was unchanged.

**T-002 stands as audit-014 PASSED, 2026-04-12.**

## Closing note for meta-analyst

The convergence-tracker work that surfaced this question is valuable — cross-finding ledger integrity IS where these timing concerns should fire. But the specific T-002/k=4 framing here doesn't match what's in the project files. If the meta-analyst can point to the specific document where they encountered the "k=4 retrofitted" worry, I'll do a second-pass forensic check at that exact location. As of audit-031 close, no defect found.

Filed under skeptical-auditor/audit-031.
