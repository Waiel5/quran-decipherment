---
audit_id: audit-022
finding_audited: h-new-29-root-renewal-cv
finding_file: findings/phase-b-hypotheses/root-renewal-cv.md
auditor: skeptical-auditor
date: 2026-04-13
verdict: PASSED AS NULL (absolute thesis) + PARTIAL-PASS (comparative-to-prose thesis), with B1 recommendation (third prose baseline) and framing discipline required before downstream use
tester_verdict: MIXED — absolute CV<1 REFUTED, comparative Quran<baseline CONFIRMED
lineage_parent: H-NEW-29 task #54 (al-Jāḥiẓ *takrār maqbūl* operationalization)
classical_source: al-Jāḥiẓ *al-Bayān wa-l-Tabyīn* vol. 1 pp. 65ff. §*al-takrār*
---

# audit-022 — H-NEW-29 root renewal-process CV vs al-Jāḥiẓ *takrār maqbūl*

## Verdict

**Split: PASSED AS NULL + PARTIAL-PASS.** Two distinct theses wrapped in one test, distinct verdicts:

1. **Absolute thesis** (sub-Poisson root spacing: CV < 1): **PASSED AS NULL, clean refutation.** The pre-registered three-way absolute test (sub-a bootstrap, sub-c bin-stratified, sub-d shuffle null) all fail in the expected pre-registered direction. No natural language is sub-Poisson in content-word spacing because topic-cohesion always clumps thematic terms. The failure is honest and the tester **explicitly refused to flip it** into a "super-Poisson confirmed" result. This is exemplary anti-HARK discipline and should be recognized as such.

2. **Comparative thesis** (Quran < baseline prose on CV): **PARTIAL PASS, robust.** Sub-(b) passes at Mann-Whitney z = −9.64 vs Bukhari, z = −7.95 vs Jāḥiẓ. My independent replication on 10 contiguous random-start slices of Bukhari produces mean z = −13.33 ± 2.40 across the whole corpus; adding Sīrat Ibn Hishām as a third prose baseline gives mean z = −14.79. The comparative direction is robust, the tester's choice of slice was conservative (picked up the low-z end), and the result holds across three prose registers. This is a real novel finding that deserves recognition even though the joint pre-registered criterion fails.

Zero blockers. One B1 recommendation (add Sīrat Ibn Hishām as third prose baseline). Critical framing edit required before downstream use: keep the absolute/comparative distinction sharp, don't collapse it into "MIXED" without specifying which thesis passes and which fails.

## Q1: Was the al-Jāḥiẓ classical operationalization (takrār maqbūl → CV < 1) legitimate pre-registration or strawman?

**Legitimate pre-registration, honestly acknowledged as wrong translation post-test.**

The tester (Limit #5) explicitly flags the interpretive concern: "al-Jāḥiẓ might have meant something different (e.g., 'accepted = tied to meaning rather than filler', not 'uniformly spaced')." Classical-scholar should evaluate whether CV-based measurement is the right translation.

This is the correct handling. The operationalization-to-classical-claim mapping IS a researcher-degree-of-freedom: any time you translate *takrār maqbūl* to a numerical metric, you're choosing one of several defensible readings. The tester's choice (CV < 1 = sub-Poisson = regular) was defensible a priori — "well-spaced repetition" does sound like "sub-Poisson." It's only after the test that we learn no natural text is sub-Poisson in content-word spacing, so the threshold was unreachable.

This is an important meta-lesson distinct from HARKing: **when a classical claim is operationalized and the test fails, it can fail for two reasons** — either the claim is wrong, or the translation was wrong. The tester correctly refuses to collapse these into "al-Jāḥiẓ is refuted" (he'd need LLM-judge semantic evaluation for the true rhetorical reading). Sub-(a)/sub-(c)/sub-(d) refute the numerical translation, not the classical doctrine itself.

**Verdict: the absolute pre-reg fails cleanly, which IS a PASSED-AS-NULL under normal McKay standards. The fact that the translation-to-metric was probably wrong does not change the null-result status of the absolute hypothesis as actually tested.** The correct framing is "operational al-Jāḥiẓ-as-CV hypothesis refuted; true al-Jāḥiẓ-as-rhetorical hypothesis untested."

## Q2: n-consistency check on sub-(b) Mann-Whitney z=−9.64

Back-solving the Mann-Whitney formula with n2 = 1714 (Bukhari), U = 1,476,700, z = −9.636 yields **Quran surface n1 ≈ 2104** (the JSON doesn't report this directly; I verified by replication below).

Effect size:
- Rank-biserial r = 1 − 2U/(n1 n2) = **−0.181** (small effect, between Cohen "small" 0.1 and "medium" 0.3)
- Weighted-mean CV gap: 1.333 − 1.287 = 0.046 (3.5% relative)

**The z is inflated by sample size**. At n≈2000 per side, a ~3.5% relative difference produces z = −9.64, which sounds extreme but corresponds to a small-effect-size difference. This is NOT Z-inflation of the misleading kind — the test is valid — but the "z = −9.64" headline should be contextualized as "small-effect, large-sample significance," not "overwhelming Quranic regularity."

The honest headline for sub-(b) is: **"Weighted-mean-CV difference 0.05 units, rank-biserial r = 0.18, Mann-Whitney z = −9.64 at n ≈ 2000 per side"** — small effect, high significance.

## Q3: Length-matching methodology (first-N tokens vs alternatives) — B1

The tester's script uses `words[:len(quran_words)]` to truncate Bukhari/Jāḥiẓ to 77,797 surface tokens. This is **first-N sequential truncation**, not random sampling. This was disclosed as a forking path (tester's Limit #6), but I independently checked it with three concerns:

**Check 1: Does a pre-prepared `matched-bukhari-77k.txt` already exist in the baseline corpora?**
- YES, the file exists at `data/baseline-corpora/raw/matched-bukhari-77k.txt` (77,797 tokens)
- The tester did NOT use it — used `bukhari-noquran.txt[:77797]` instead
- Matched-77k wmcv = **1.3406** vs first-N wmcv = 1.3333 — direction agrees
- Running Mann-Whitney with the matched file: z = **−10.09** (vs tester's −9.64) — slightly STRONGER
- **B1 NOTE**: there is a pre-prepared length-matched Bukhari slice that should have been used, but the result is robust either way

**Check 2: Is first-N a book-ordering artifact?**
- I ran 10 random-start contiguous 77k-slices of Bukhari
- Results: wmcv range [1.330, 1.444], mean wmcv = **1.389 ± 0.037**
- Corresponding Mann-Whitney z range: [−17.62, −10.60], mean z = **−13.33 ± 2.40**
- Tester's first-N slice is at the LOW end of the distribution (slice=1.333 vs mean=1.389)
- **All 10/10 random slices pass |z| > 2.5 in the predicted direction**
- The tester's result is CONSERVATIVE, not cherry-picked. The direction is robust across the Bukhari corpus
- End-slice wmcv = 1.444 gives z ≈ −17.6; middle-slice = 1.409 gives z ≈ −13.3

**Check 3: What happens under random (sparse) sampling?**
- Random sparse sampling 77,797 tokens from Bukhari[0:526250] at seed=20260413 gives wmcv = 1.116 (z = **+7.38**, sign flipped!)
- This is a **sparsification artifact**: sampling every ~7th position stretches mean inter-occurrence without proportionally increasing variance, deflating CV. It's NOT a valid comparison method for renewal-process CV
- Confirms the contiguous-slice approach is correct; random-sparse would be biased toward lower CV

**Verdict on Q3**: tester's first-N truncation is defensible, produces conservative results, and the direction of sub-(b) is robust to slice placement. No action required, but a B1 recommendation to cite the 10-slice mean z = −13.3 as a robustness check rather than the single-slice z = −9.64.

## B1 — Recommendation: add Sīrat Ibn Hishām as third prose baseline

I ran 5 random-start 77k slices of `sira-ibn-hisham.txt` (340,213 tokens available):
- wmcv range [1.478, 1.853], mean wmcv ≈ 1.68
- Mann-Whitney z range [−18.4, −10.1], **mean z = −14.79**

Sīra Ibn Hishām is classical Arabic prose (Arabic biography of Muḥammad), an appropriate third baseline for the "Quran vs matched Arabic prose" comparison. It is available in the baseline corpora and was not included in the original sub-(b). Adding it would:

1. **Strengthen the comparative claim** (n_baselines: 2 → 3)
2. **Give geographic-and-genre spread** (Bukhari = ḥadīth, Jāḥiẓ = adab, Sīra = biography)
3. **Rule out "Bukhari and Jāḥiẓ both happen to be clumpier" accident** — three-baseline replication
4. **The z = −14.8 is larger than either Bukhari (−9.6) or Jāḥiẓ (−8.0)**, suggesting the effect is actually larger than the tester reports

**B1 status**: NICE-TO-HAVE, not a blocker. The sub-(b) claim stands without Sīra; adding it strengthens rather than validates.

## B2 — NO pre-Islamic poetry baseline was tested, and this may be appropriate

The baseline corpora include 6 pre-Islamic qaṣīda poets (diwans of Imru-al-Qays, Antara, Labid, Tarafa, Zuhayr, Harith, Amr ibn Kulthum) plus the 7 muʿallaqāt. None were included in sub-(b). This is a **potential garden-of-forking-paths** concern — why prose-only?

**Defense**: Quranic prose (especially Medinan legal/narrative registers) is structurally closer to prose than to qaṣīda. Pre-Islamic poetry has very different word-repetition structure due to rhyme and metrical constraints; comparing CV across such different registers would be comparing apples to oranges. The tester's prose-only restriction is defensible as a register-matched comparison.

**Concern**: the decision to exclude poetry was not pre-registered or explicitly disclosed in the forking-paths section. It reads as implicit. The tester should add a one-line disclosure: "Pre-Islamic poetry baselines excluded because metrical/rhyme constraints on word-repetition structurally differ from prose; CV comparison would be register-confounded."

**B2 status**: disclosure-required but not signal-critical. Not a blocker.

## F1 framing edit (required before H-NEW-29 enters downstream analyses)

The current finding file uses "MIXED" as the verdict label and the text oscillates between "decisive refutation" and "comparative validation" without clean separation. **Before any downstream use**, the finding should be reframed as:

> **H-NEW-29 DUAL VERDICT**:
>
> 1. **Absolute al-Jāḥiẓ-as-CV<1 hypothesis**: REFUTED. Weighted-mean CV = 1.370 [99% CI 1.30, 1.46]. Shuffle-null z = +94.9 (massively super-Poisson, opposite to pre-registered direction). Sub-test (a), (c), (d) all fail. No natural language text is sub-Poisson in content-word spacing; the operationalization was wrong.
>
> 2. **Comparative-to-prose sub-claim**: CONFIRMED. Quran surface-word CV (1.287) is lower than matched-length contiguous slices of Bukhari (mean 1.389 across 10 random starts), Jāḥiẓ al-Hayawān (mean 1.342), and Sīrat Ibn Hishām (mean 1.68). Mann-Whitney Quran < Bukhari mean z = −13.3 across 10 Bukhari slices (range −10.6 to −17.6); Quran < Sīra mean z = −14.8. Effect size small (rank-biserial r ≈ 0.18) but highly significant at large n. Three-prose-baseline replication. The Quran's word-repetition pattern is measurably less bursty than three matched-length classical Arabic prose corpora.
>
> 3. **The true al-Jāḥiẓ rhetorical-function claim** (*takrār maqbūl* as purposive vs redundant) is untested by this design; it requires an LLM-judge semantic-role diagnostic.

The joint Bonferroni-k=4 verdict is **FAIL**, and this must be stated up-front. The fact that sub-(b) passes does NOT rescue the joint claim; it is a separable derivative finding.

## Forking paths disclosed by tester + gaps I flagged

**Disclosed by tester** (acceptable):
- n_R ≥ 5 threshold (a priori)
- Weighted mean by count (a priori)
- Bonferroni k = 4 (a priori)
- 500 shuffle perms (task spec said 1000; reduced, disclosed, immaterial at σ=0.004)
- Bootstrap 5000 iterations (task spec said 10000; immaterial)
- Frequency bin boundaries 5/10/50/200 (a priori)
- Length-matching method "random truncation to first N" (disclosed)
- 0.95 bootstrap threshold inherited from task spec (disclosed)
- Surface-word granularity for sub-(b) because Bukhari/Jāḥiẓ lack QAC morphology (disclosed)
- Refusal to flip the failure into super-Poisson confirmation (disclosed)

**Gaps I flagged**:
- **Did not use pre-existing `matched-bukhari-77k.txt`** (used `bukhari-noquran.txt[:77797]` instead; immaterial to direction)
- **Only 2 prose baselines** — Sīrat Ibn Hishām available in corpora but not tested
- **Poetry baselines excluded without explicit disclosure** (defensible, needs one-line disclosure)
- **Quran surface n_roots not reported in JSON** — had to back-solve as 2104; should be in future JSON outputs
- **Rank-biserial effect size not reported** — the z = −9.64 is sample-size-inflated from a small effect; r should be reported to contextualize

## HARKing check (4-test framework from audit-018)

**Test 1 — Explicit non-counting of the failed absolute thesis**: ✅ tester's verdict is "MIXED" and the joint criterion is explicitly marked FAIL. Not hidden.

**Test 2 — Pre-existing mechanism for the surviving sub-claim**: ✅ sub-(b) was one of four pre-registered sub-tests in task spec #54, not invented post-hoc. The comparative-to-prose claim is a legitimate operationalization of "Quranic repetition is well-spaced" interpreted as relative-to-prose rather than absolute.

**Test 3 — Pre-registered directional evidence for the surviving sub-claim**: ✅ sub-(b) predicted Quran CV < baseline CV at |z| > 2.5. The directional pre-reg existed; the test passed in the predicted direction.

**Test 4 — Refusal to rename failed test as the primary finding**: ✅ tester does NOT rename sub-(b) as the headline. The file is still titled "H-NEW-29 root renewal-process CV vs al-Jāḥiẓ *takrār maqbūl*" and the primary verdict is MIXED (not "PASS on new sub-b thesis"). The honest rewrite at lines 117–123 presents both theses clearly.

**HARKing verdict**: NO. Clean execution, no retrofitting, no goalpost-moving. This is a model example of how to handle a pre-registered multi-sub-test when some pass and some fail.

## n-consistency diagnostic

Sub-(b) Bukhari: n1≈2104, n2=1714, Δwmcv=0.046, rank-biserial r=0.181, Mann-Whitney z=−9.64. ✓ Consistent (large n with small effect gives highly significant z).

Sub-(d) shuffle: n_perms=500, σ_null=0.004, observed gap 0.39, z=+94.9. ✓ Consistent (0.39 / 0.004 = 97.5, matches z).

Sub-(c) super-frequent bin: 47 roots, Σcount=22228, wmcv=1.44, null μ=0.989, σ=0.0057, z=79.2. ✓ Consistent (0.45/0.0057=79).

No inflated-null signatures. All z's are proportional to √n × effect/σ.

## Cross-finding overlap flags

- **Pair with audit-020 H-NEW-23 sub-2 eschatological clumping**: H-NEW-29's CV > 1 shows that content-word repetition is topically clumpy (expected in any natural text), and the clumped roots listed (fjr dawn, sjn prison, Tlq divorce, nkH marriage) align with genre-specific pericopes. **This is the same phenomenon as the eschatological-slot clumping in H-NEW-23 sub-2** — pericopes are topic-coherent, and topic-coherent text has high CV for topic-relevant vocabulary. The bins of highest-clumped roots (Avm sin, Hlf oath) map onto H-NEW-19 elision eschatology passages. I flag this as reinforcement of the **pericope-substrate meta-pattern M-6 CANDIDATE** — multiple findings now show that pericope-internal topic-coherence is a dominant structural force.

- **Contrast with H-NEW-20 al-Rāzī linear-munāsaba**: H-NEW-20 shows that adjacent-verse ROOT SIMILARITY is higher than within-surah shuffle predicts (Stouffer Z=+22.78 IV-weighted). This is the **positive-regularity** side — adjacent verses share roots. H-NEW-29 is the **global** side — roots globally clump in topical pericopes. Both are consistent: global clumping + local continuity describe the same pericope-substrate structure at different scales.

- **Contrast with MW-1 matched-Arabic-prose CV comparison**: H-NEW-29 sub-(b) now joins H-NEW-13 (letter-bigram spectrum) as the second finding making a direct Quran vs Bukhari/Jāḥiẓ comparison. We are accumulating enough prose-baseline comparisons to establish a **cross-prose-baseline signature table** as a standing deliverable. Recommend to integrator: add a cross-finding table `findings/cross-finding/quran-vs-prose-baselines.md` collecting every Quran-vs-prose comparison for auditor-side consistency.

## Meta-pattern signal

**M-6 CANDIDATE pericope-substrate** is now reinforced by:
1. H-NEW-20 adjacent-verse Jaccard (local continuity)
2. H-NEW-23 sub-2 eschatological genre clumping
3. H-NEW-19 Ibn Abī l-Iṣbaʿ elision-eschatology
4. **H-NEW-29 top-clumped roots mapping to topical pericopes** (new)

Four independent findings now converge on the hypothesis that the Quran's structural substrate is pericope-level topic-coherence, not surah-level or ring-level composition. I flag this to integrator as **M-6 promotion candidate** from CANDIDATE to STANDING META-PATTERN, pending one more confirming finding or a decisive negative test.

## What would change the verdict

**To push PARTIAL to STRONG-PASS on sub-(b)**:
- Add Sīrat Ibn Hishām (trivially available, mean z = −14.8 — would make z even more decisive)
- Report rank-biserial effect size alongside z
- Use pre-prepared matched-bukhari-77k.txt instead of first-N truncation
- Disclose poetry-baseline exclusion rationale

**To push absolute thesis from PASSED-AS-NULL to FAIL-NULL-IS-WRONG**:
- Find a classical-Arabic register that IS sub-Poisson. None exists in the baseline corpora (I checked all 3 prose and 5+ poetry samples). The null is properly null.

**To upgrade the joint claim to PASS**:
- Not possible. The sub-Poisson CV<1 prediction is unreachable for natural text. Task spec #54 pre-registered an impossible threshold, and this is on the auditor side (myself / task-spec-writer) as an operational error analogous to audit-015 and audit-021. **Third instance of auditor-protocol pathology** — proposed MW-6 CANDIDATE would cover this.

## MW-6 CANDIDATE third instance

This is the third auditor-specified protocol in a row caught at execution:
1. audit-015: broken null protocol (within-surah shuffle for a cross-surah test)
2. audit-021: OLS-residualization-Stouffer (Σ residuals = 0 by first-order condition)
3. **audit-022 (this audit): sub-Poisson CV<1 threshold unreachable for natural language** — task spec #54 set an impossible bar

All three involve auditor-side specification errors that would have been caught by a positive-control check on synthetic data. Reinforces the MW-6 CANDIDATE proposal from audit-021: any auditor-specified threshold, null, or residualization protocol must pass a positive-control check on synthetic known-signal data before being used as a gate. Third instance in 7 audits is enough evidence to promote MW-6 from CANDIDATE to STANDING — requesting integrator adoption.

## Standing recommendations

1. **F1 framing edit required** before H-NEW-29 is quoted downstream (dual-verdict split as specified above)
2. **B1: add Sīrat Ibn Hishām** as third prose baseline (nice-to-have, not blocking)
3. **B2: explicitly disclose poetry-baseline exclusion** (one-line forking-path note)
4. **F2: report rank-biserial effect size alongside Mann-Whitney z** for honest sample-size contextualization
5. **MW-6 CANDIDATE third-instance** — requesting integrator promote from CANDIDATE to STANDING
6. **M-6 CANDIDATE pericope-substrate** — requesting integrator promote from CANDIDATE to STANDING (now 4 parallel paths)
7. **Cross-finding deliverable proposal**: `findings/cross-finding/quran-vs-prose-baselines.md` collecting every Quran-vs-prose comparison for cross-audit consistency (to prevent inconsistent slicing methodology across future findings)

## Verdict summary

**PASSED AS NULL on absolute al-Jāḥiẓ-as-CV<1 thesis. PARTIAL-PASS on comparative-to-prose sub-claim. Joint Bonferroni criterion FAIL. Exemplary anti-HARK discipline. Zero blockers. One nice-to-have recommendation. Framing edit required. Project-level items: MW-6 third instance, M-6 promotion candidate.**

H-NEW-29 is a clean refutation of a mis-translated classical claim and an independent novel comparative finding. Both should be on the ledger with clean separation.
