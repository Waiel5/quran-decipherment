---
audit_id: audit-034
date: 2026-04-16
auditor: skeptical-auditor-wave-4
target: 2026-04-16 wave-4 inventory (H-NEW-44.* through H-NEW-92.*; cross-finding-008, cross-finding-005 retraction; in-flight pre-regs 61-92)
target_authors: integrator (post-hoc-noticed deliverables); h-new-{61..88}-specialists (pre-regs); META-4 specialist
stage: mixed (post-execution audit on completed deliverables; pre-execution gate-check on in-flight pre-regs)
verdicts:
  H-NEW-49.1:        DEFENSIBLE-WITH-CAVEAT (8-prophet list defensibility; recommend explicit per-surah lock)
  H-NEW-51:          CLEAN-DISCLOSED (post-hoc; PASS-DIRECTED honestly capped)
  H-NEW-53:          CLEAN-DISCLOSED-EXTREME (post-hoc; p≈10⁻¹² survives any conceivable Bonferroni)
  H-NEW-57:          CLEAN-DISCLOSED (post-hoc; sub-class breakdown auditable)
  H-NEW-58c:         CLEAN-DISCLOSED (post-hoc tense-split; STRONG-PASS-DIRECTED)
  H-NEW-60:          CLEAN-DISCLOSED (post-hoc dot-classification; PASS Bonferroni-4 on per-class)
  H-NEW-63:          CLEAN-OBSERVED-FACT (deterministic substring; framing as ECHO-CONFIRMED defensible)
  H-NEW-67:          CLEAN-WITH-CAVEAT (dual-reading; both pass top-7-longest at p=0.0001 — defensible)
  cross-finding-008: PROMOTION-DEFENSIBLE (multiple independent operationalizations; integrity-positive)
  cross-finding-005: RETRACTION-CORRECTLY-HANDLED (audit-033 verdict re-affirmed)
  In-flight pre-regs: 5 NEEDS-AMENDMENT (PRE-REG-STANDARD-04 violations on 62/64/66/83/88)
related_audits: audit-030, audit-031, audit-032, audit-033
---

# Audit-034 — Wave-4 (2026-04-16) comprehensive audit

## Executive summary

Wave-4 is the project's largest single-day discovery wave: 12+ post-hoc-noticed integrator deliverables (H-NEW-49.1, 51, 53, 56, 57, 58b/c, 60, 63, 67), 1 retracted cross-finding (005), 1 newly-promoted cross-finding (008), and ~14 in-flight specialist pre-regs (H-NEW-61..H-NEW-92).

The wave's integrity discipline is **substantially clean** at the post-hoc deliverable layer — every single post-hoc-noticed finding I audited (H-NEW-49.1, 51, 53, 57, 58c, 60, 63, 67) carries explicit `post-hoc-noticed` disclosure, `single-test no Bonferroni cost` language, conservative verdict capping (PASS-DIRECTED not CONFIRMED unless p so extreme it survives any k), and per-item garden-of-forking-paths log. This is the project's standing post-hoc-discipline working as designed.

The wave's **principal integrity defects are at the pre-registration gate-layer**: 5 of the 14 in-flight pre-regs I inspected (H-NEW-62, H-NEW-64, H-NEW-66, H-NEW-83, H-NEW-88) are missing one or more PRE-REG-STANDARD-04 mandatory header fields (`bonferroni_k`, `alpha_bon`, `bonferroni_family`). H-NEW-62 has `multi_test_correction: Bonferroni across pre-registered test families (k = 7 families)` in body-text but not in canonical header fields. H-NEW-64 same pattern (k=5 in body-text, not in header). H-NEW-66 has NO Bonferroni discipline at all (framed as "deliverable is published structure, not binary verdict" — defensible only if all NOTABLE thresholds are pre-locked, which they are at 3×median / 2×expectation / mean+3σ, but the absence of explicit `alpha_bon` is a visible PRE-REG-STANDARD-04 nonconformance). H-NEW-83 is the worst offender: no Bonferroni discipline anywhere in header OR body. H-NEW-88 has no `bonferroni_k`/`alpha_bon` in header.

These are pre-execution defects fixable by amendment before run; per PRE-REG-STANDARD-04 retroactive tightening before execution is permitted.

## Per-target verdicts

### H-NEW-49.1 — Prophet-named PASS-DIRECTED (DEFENSIBLE-WITH-CAVEAT)

**Verdict: DEFENSIBLE.** Two definitions of "prophet-named" tested:
- Specialist's PROPHET_PERSON taxonomy n=11: 7/11 → p = 0.00563
- Conservative 8-prophet list: 6/8 → p = 0.00333

Both PASS at α=0.05 single-test. The 8-prophet list (Q 10, 11, 12, 14, 19, 31, 47, 71) is **explicit and per-surah enumerated** in the findings file Table — it is NOT a hidden post-hoc selection but a transparent listing of "surahs explicitly named after a known prophet/messenger." The conservative list is more defensible than specialist's 11-element class.

**The audit-task's worry — "should the 8 prophet-named list be pre-registered more carefully?" — is partially valid.** Recommendation: when this finding is re-tested for promotion (e.g., on Nöldeke chronology, or as a cross-validation cell), the 8-prophet list should be pre-registered IN ADVANCE in a separate independent dimension test, with the per-surah membership locked at file-creation time. Right now the 8 are post-hoc-justified ("only surahs explicitly named after a known prophet") — defensible because the criterion is exhaustive and unambiguous, but a future audit could argue boundary cases (e.g., does Q 17 al-Isrāʾ count as Muḥammad-named? does Q 88 al-Ghāshiya not name a prophet?). Pre-locking the membership in a separate independent-replication pre-reg would close that loophole.

**Audit issue: NONE blocking.** Cap at PASS-DIRECTED (which the integrator did) is correct. Promotion to CONFIRMED requires independent replication on a distinct data dimension.

### H-NEW-51 — Cardinality-position decline (CLEAN-DISCLOSED)

**Verdict: CLEAN.** Garden-of-forking-paths disclosure is exemplary (§"Garden-of-forking-paths disclosure (CRITICAL)" lines 21-35). The post-hoc origin is acknowledged; single-test no-Bonferroni protocol applied; PASS-DIRECTED cap honored; H-NEW-51.1 (Nöldeke-chronology replication) is queued as the appropriate independent-dimension test.

The partial correlation framework + suppression-effect noting is statistically literate (suppressor-variable correctly identified). Permutation null at 100K perms with seed locked. **Audit issue: NONE.**

### H-NEW-53 — Book-reference enrichment (CLEAN-DISCLOSED-EXTREME)

**Verdict: CLEAN.** This is the wave's single strongest finding. p = 3.17 × 10⁻¹². Post-hoc-noticed status disclosed. The p-value is so extreme that it survives any conceivable Bonferroni (even k = 10⁹ leaves it below α). Substring search definition is explicit (KITAB={...}, QURAN={...}). Per-surah table provided for full audit. The 5 exceptions discussed individually with thematic interpretability.

**Audit issue: NONE.** Promotion to Tier-A defensible.

### H-NEW-57 — Formulaic openings 13/13 exclusive (CLEAN-DISCLOSED)

**Verdict: CLEAN.** Joint hypergeometric p = 1.57 × 10⁻⁹. The 13 surahs and 4 formula variants are explicitly listed. The "tilka āyāt" demonstrative class (8/8) and "wa-l-X" oath class (5/5) are sub-broken-out. The 16 muqaṭṭaʿāt-without-formula surahs are listed (Q 2, 3, 7, 11, 14, 19, 20, 29, 30, 32, 40, 41, 42, 45, 46, 68) and several have alternative "tanzīl al-kitāb" openings disclosed as a 3rd formula class.

**Slight audit concern (NON-BLOCKING):** the 4-formula set was "derived from inspection of the muqaṭṭaʿāt-opener verse-1 texts, NOT from a pre-existing classical taxonomy." This is honestly disclosed in §Honest-caveats #2 — the formula-set is post-hoc-selected. But the joint p is robust to expansion (the integrator notes "Future audits could test other formulaic openings; the current pre-reg locks the 4-formula set"). The "tanzīl al-kitāb" 3rd class (which is 5/6 muqaṭṭaʿāt = 83% not 100%) is correctly NOT bundled into the 100% claim.

**Audit issue: NONE blocking.** Honest disclosure adequately scopes the claim.

### H-NEW-58c — Musabbiḥāt tense-split (CLEAN-DISCLOSED)

**Verdict: CLEAN.** The structural observation (within-tense pairs share 24-56 chars; cross-tense pairs share EXACTLY 0 chars) is striking and verifiable by inspection of the per-pair table. The cluster-cohesion test (sum 141 chars vs null mean 3.64; max 104 in 10K random subsets, p=0.0001) is an honest single-test post-hoc-disclosed instrument-validated (H-NEW-58b validates the shared-prefix metric on 2/4 classical pairs).

The verb-tense split (sabbaḥa perfect / yusabbiḥu imperfect) is a CLASSICAL tafsīr distinction (al-Rāzī, al-Zamakhsharī) given QUANTITATIVE confirmation. **Audit issue: NONE.**

### H-NEW-60 — Dotless preference (CLEAN-DISCLOSED)

**Verdict: CLEAN.** 11/14 muqaṭṭaʿāt letters are dotless (79%); only 13/28 alphabet letters are dotless (46.4%). p = 0.000919 single-test directed. Per-class Bonferroni-4 PASSES on 0-dot enrichment (p=0.0018) AND on 1-dot depletion (p=0.0044), both Bonferroni-significant.

The historical-linguistic interpretation (pre-i'jām script preservation) is correctly labeled SPECULATIVE (§Honest-caveats #3). The 2 dotless exceptions {د, و} are noted as not explained by the dot-preference framework alone. **Audit issue: NONE.** Promotion to Tier-B defensible.

### H-NEW-63 — Khawātim echo at Q 62:1 (CLEAN-OBSERVED-FACT)

**Verdict: CLEAN.** Deterministic substring search; corpus-wide enumeration. 3 verses contain ≥2 Khawātim names (Q 59:23 with 8; Q 59:24 with 4; Q 62:1 with 3). Exactly 2 verses contain the 3-name "al-Malik al-Quddūs al-ʿAzīz" subsequence. No statistical claim beyond observation.

The framing as "ECHO-CONFIRMED" is appropriate: it's an OBSERVED-FACT about the corpus, not a hypothesis-test outcome. The interpretation that Q 62:1 is a "deliberate echo" is explicitly hedged in §Honest-framing as "consistent with classical observation but not strictly testable without a counter-factual hypothesis."

**Audit issue: NONE.** Cross-finding-009 candidate is correctly flagged as a CANDIDATE (not yet a confirmed cross-finding).

### H-NEW-67 — al-sabʿ al-ṭiwāl dual-reading (CLEAN-WITH-CAVEAT)

**Verdict: CLEAN-WITH-CAVEAT.** The audit-task asks: "is dual-reading defensible without correction?"

**My judgment: YES, defensible.** The two readings (Q 2-9 vs Q 2-7+10) BOTH yield 5/7 in top-7-longest at p = 0.0001. Both pass the same identical test on the same identical instrument. Reporting both is *transparency*, not multiple-testing inflation:

1. The two readings are **classical alternatives**, not data-driven post-hoc choices. al-Suyūṭī (Itqān) records both as classical readings.
2. The two readings give the SAME p-value (0.0001) on the SAME test (top-7-longest). They do not give two different chances to pass — they give one shared verdict that is robust to the classical ambiguity.
3. The cluster-cohesion secondary axis HONESTLY DIFFERS between readings (Q 2-9: p=0.053 marginal; Q 2-7+10: p=0.030). The integrator did not select the more favorable reading post-hoc; he reported both and explicitly noted "Cluster cohesion: MARGINAL (p = 0.03–0.05)" — capturing the worse case.
4. The 7-surah list is pre-locked (3 of the 6 invariant surahs are Q 2, 3, 7 muqaṭṭāʿat-opened); only 1 slot varies (Q 9 vs Q 10).

Defensibility hinges on whether dual-reading inflates effective k. Here, it does not in a meaningful way — the test is the SAME (top-7-longest enrichment) and Bonferroni-2 on dual-reading would still leave the primary p = 0.0001 well below α = 0.025. A more rigorous framing would be Bonferroni-2-corrected (α_bon = 0.025; observed p = 0.0001 PASSES), but the integrator's single-test framing is also defensible because the two readings are classically authorized prior alternatives, not data-driven post-hoc subsetting.

**Recommendation:** the findings file should explicitly note "Bonferroni-2 conservative correction on dual-reading: α_bon = 0.025; observed p = 1×10⁻⁴ PASSES Bonferroni-2 by 250×." This is a non-blocking documentation tightening.

The Fātiḥa center-symmetry observation (v2≡v6 lengths) is correctly labeled OBSERVED-FACT (post-hoc) and explicitly NOT elevated. **Audit issue: NON-BLOCKING.** Recommend explicit Bonferroni-2 disclosure in body-text.

### Cross-finding-008 (muqaṭṭāʿat-as-book-introduction-marker)

**Verdict: PROMOTION-DEFENSIBLE.** The synthesis is built on FIVE independent tests at radically different operationalizations:

| Test | Operationalization | p |
|---|---|---|
| H-NEW-53 | Narrow kitāb/qurʾān | 3×10⁻¹² |
| H-NEW-56 | Extended writing-cluster | 8.6×10⁻¹³ |
| H-NEW-57 | Specific formulaic openings | 1.6×10⁻⁹ |
| H-NEW-54 | Broader root scan (4/10 PASS Bonferroni-10) | various |
| H-NEW-55 | Multi-feature classifier (LOOCV AUC=0.92) | 0.001 |

Even with a conservative inter-test Bonferroni (k = 5), the joint claim survives at α = 0.01 by orders of magnitude. The 2 genuine exceptions (Q 29, Q 30 al-ʿAnkabūt-Rūm pair) are honestly disclosed and given their own H-NEW-61-queued sub-hypothesis (test-and-prophecy sub-cluster).

**The "single strongest finding" claim for H-NEW-53 is defensible.** Of the project's tests with locked p-values, H-NEW-53 at 3×10⁻¹² is the strongest in the muqaṭṭaʿāt cluster (only the Ism al-Aʿẓam composite at p ≈ 5×10⁻¹⁸ is stronger overall, but that is a multi-axis composite not a single substantive test). H-NEW-56 at p = 8.6×10⁻¹³ is even stronger numerically but is a SUPERSET of H-NEW-53 (extended writing-cluster includes the H-NEW-53 narrow set), so the two are not independent.

**Audit issue: NONE.** Promotion of H-NEW-53/55/56/57 to Tier-A is appropriate. The wave's strongest finding cluster.

### Cross-finding-005 retraction (CORRECTLY HANDLED)

**Verdict: CORRECTLY HANDLED.** Audit-033 covered this in detail; I re-affirm the verdict. The retraction is the single most important integrity-positive event in this wave-cluster. The H-NEW-META-4 NULL was pre-registered with explicit fail criteria, ran cleanly, and refuted the meta-pattern. Component findings (H-NEW-34.1, H-NEW-42, H-NEW-43) stand individually as LOCAL-SIGNAL.

**Audit issue: NONE.** No further action needed beyond the audit-033 close.

### In-flight pre-reg gate-layer audit

I inspected the pre-reg headers for the 14 in-flight specialist pre-regs (H-NEW-61, 62, 64, 65, 66, 68, 69, 71, 74, 82, 83, 84, 85, 88).

**Compliant with PRE-REG-STANDARD-04** (canonical header fields `bonferroni_k`, `alpha_bon`, `bonferroni_family`): H-NEW-61, 65, 68, 69, 71, 74, 82, 84, 85.

**NEEDS-AMENDMENT (PRE-REG-STANDARD-04 missing/partial):**

1. **H-NEW-62** (closings audit): has `multi_test_correction: Bonferroni across pre-registered test families (k = 7 families)` in header but NOT canonical `bonferroni_k: 7` / `alpha_bon: 0.00714` / `bonferroni_family: <name>` fields. **Required fix:** add canonical fields to header before execution.
2. **H-NEW-64** (juzʾ boundaries): has `multi_test_correction: Bonferroni over 4 axes + 1 joint test (k = 5; α_bon = 0.01)` in header but NOT canonical `bonferroni_k: 5` / `alpha_bon: 0.01` / `bonferroni_family: <name>` fields. **Required fix:** add canonical fields.
3. **H-NEW-66** (verse-twins network): NO Bonferroni discipline ANYWHERE. Body-text §"What counts as PASS / NULL / NOTABLE" frames this as "exploratory/structural; no single test statistic to declare PASS/NULL." Three NOTABLE thresholds (3×median, 2×expectation, mean+3σ) are pre-locked, which is the discipline equivalent. **Verdict-defensibility check:** if the deliverable is structural-descriptive only and no individual NOTABLE threshold leads to a PROMOTED claim, this is acceptable as exploratory. However, PRE-REG-STANDARD-04 mandates `bonferroni_k` declaration even for descriptive deliverables that yield ranked lists. **Required fix:** add `bonferroni_k: 3` (one for each NOTABLE) and `alpha_bon` reflecting the 3-fold or whatever the implicit correction is; OR add explicit `bonferroni_k: NA-DESCRIPTIVE` with rationale and team-lead pre-execution clearance.
4. **H-NEW-83** (Raḥmān refrain extension): NO Bonferroni discipline at all (no `bonferroni_k`, `alpha_bon`, `bonferroni_family` in header; not in body either except for 1,000-cut Monte Carlo seed). Six pre-registered hypotheses (H-83a through H-83f) without family-wise correction. **WORST OFFENDER.** Required fix: add canonical Bonferroni-6 family before execution.
5. **H-NEW-88** (letter-set predictor): no canonical `bonferroni_k` / `alpha_bon` / `bonferroni_family` fields. Body uses single PASS criterion (LOOCV ≥ 0.30 AND perm p < 0.05) which is technically a single-test scalar but the multi-class permutation null involves implicit multiple comparison across the 14 letter-sets. **Required fix:** add canonical Bonferroni-1 family with explicit rationale (single LOOCV scalar) OR Bonferroni-14 if per-class accuracy is reported.

**Severity:** all 5 are pre-execution; none have run yet. PRE-REG-STANDARD-04 retroactive tightening before execution is permitted; the amendments are short add-only insertions. None of the 5 has a substantive defect (e.g., fallback clause, sign-flip loophole) — they are header-discipline omissions.

### Cross-pre-reg consistency

| Item | bonferroni_family | bonferroni_k | bonferroni_family in 2026-04-15 wave? |
|---|---|---|---|
| H-NEW-61 | 2026-04-15-Wave-H-NEW-61-Opening-Words | 6 | YES |
| H-NEW-65 | 2026-04-15-Wave-H-NEW-65-Fatiha-DNA | 6 | YES |
| H-NEW-68 | 2026-04-15-Wave-Friday-Cluster | 4 | YES |
| H-NEW-69 | 2026-04-15-Wave-Half-Alphabet | 8 | YES |
| H-NEW-71 | 2026-04-15-Wave-H-NEW-71-Allah-Distribution | 7 | YES |
| H-NEW-74 | 2026-04-15-Wave-H-NEW-74-Qul-Distribution | 6 | YES |
| H-NEW-82 | 2026-04-15-Wave-Yasin-Heart | 6 | YES |
| H-NEW-84 | 2026-04-15-Wave-H-NEW-84-Ikhlas-third | 7 | YES |
| H-NEW-85 | 2026-04-15-Wave-H-NEW-85-Oath-Openers | 5 | YES |

Each compliant pre-reg has its own self-named Bonferroni family. No false cross-test pooling. PRE-REG-STANDARD-05 (hierarchical-family Bonferroni) is satisfied via per-pre-reg family naming; no master-wave Bonferroni is declared because the pre-regs are conceptually independent (different feature targets per pre-reg).

## The "muqaṭṭāʿat as book-introduction-marker" cluster — multi-test discipline check

The audit-task asks: "is the multi-test discipline sound?"

**Yes, with one tightening recommendation.** The 5 tests (H-NEW-53, 54, 55, 56, 57) form an evidence cluster where each test on its own is post-hoc-noticed but each gives a unique INDEPENDENT p-value. Cross-finding-008 honestly catalogs them.

**Concerns:**
1. **Independence between H-NEW-53 (kitāb/qurʾān narrow) and H-NEW-56 (extended writing-cluster):** these are NOT independent; H-NEW-56 is a SUPERSET of H-NEW-53. Citing both in a multi-test convergence claim risks double-counting. Audit-recommendation: cross-finding-008 should explicitly note that H-NEW-53 and H-NEW-56 share dependent corpus subsets, and that the joint evidence is essentially H-NEW-56-strength (the wider net), not the multiplicative product of two independent p-values.
2. **H-NEW-57 (formulaic openings) is independent of H-NEW-53/56** at the operationalization level (different feature: specific liturgical phrases vs any kitāb/qurʾān reference) but tests on the same 29-surah corpus. Sharing the corpus does not make the tests dependent in the Bonferroni sense, but it does mean the 5 tests' "5 independent confirmations" claim should be qualified to "5 independent operationalizations on the same 29-surah set, capturing distinct feature-axes."
3. **H-NEW-55 (multi-feature classifier)** uses features from H-NEW-53 and H-NEW-56 as LEARNED feature importance (book_ref_v1_3 = +1.96 dominant). This means the classifier's signal is partially DERIVED from H-NEW-53/56. Treating it as an independent confirmation is methodologically loose. Recommendation: cross-finding-008 should note that H-NEW-55's AUC is partially driven by the H-NEW-53/56 features and not a fully-independent test.

**Net verdict:** the cluster is NOT a 5-fold-independent confirmation. It is more like 2-3 independent confirmations (H-NEW-53/56 as one axis, H-NEW-57 as a second axis, H-NEW-55 as a partially-dependent third axis, H-NEW-54 as a fourth axis with 4/10 marginal sub-tests). The cluster is still STRONG (H-NEW-53 alone at p=10⁻¹² is overwhelming), but the "5 independent confirmations" framing inflates the apparent independence.

**Recommendation for cross-finding-008 v2:** rewrite §"The evidence (5 independent tests)" to disclose the dependencies explicitly. This is integrity-tightening, not retraction; the central claim (muqaṭṭāʿat-as-book-introduction-marker) is robust regardless.

## MW-1..MW-7 compliance

- **MW-1 (length residualization):** PASS where applicable. H-NEW-46.1 explicitly residualizes for chronology; H-NEW-51 partial-correlation framework controls for length (suppressor identified).
- **MW-5 (positive control):** PASS on H-NEW-58c (instrument validated by H-NEW-58b on 2/4 classical pairs); PASS on H-NEW-META-4 (Khawātim al-Ḥashr SEMANTIC-STRUCTURAL); PASS on most pre-regs (Q 1 basmala extraction; Q 2:255 Light Verse anchor). PASS on H-NEW-69 planted-signal pipeline check.
- **MW-6 (nawʿ-verification tag):** N/A in this wave; no nawʿ-number-citing finding.
- **MW-7 (internal-error pre-publication):** PASS on most deliverables; the post-hoc-disclosed integrator deliverables are explicit about post-hoc-noticed status. The 5 in-flight pre-reg gate-defects (H-NEW-62/64/66/83/88) are MW-7 PASS at the citation/gate-spec level (gates ARE specified, just not in canonical header form).

## The 3 most important defects (ranked)

**Defect #1 (HIGHEST PRIORITY): H-NEW-83 missing all PRE-REG-STANDARD-04 fields.** Six pre-registered hypotheses without family-wise Bonferroni declaration. Worst single offender of the wave. Required fix BEFORE execution: add canonical `bonferroni_k: 6`, `alpha_bon: 0.00833`, `bonferroni_family: 2026-04-15-Wave-Rahman-Refrain-Extension` to header.

**Defect #2: cross-finding-008 "5 independent tests" framing inflates true independence.** H-NEW-53 ⊂ H-NEW-56 (corpus dependence); H-NEW-55 uses H-NEW-53/56 as features. Effective independent evidence is closer to 2-3 axes, not 5. Recommendation: rewrite §"The evidence" to disclose dependencies explicitly. NOT a retraction — the central claim survives. Tightening, not weakening.

**Defect #3: H-NEW-66 / H-NEW-62 / H-NEW-64 / H-NEW-88 header non-canonicalization.** Four additional in-flight pre-regs lacking canonical PRE-REG-STANDARD-04 header fields (Bonferroni discipline IS specified in body-text for H-NEW-62/64; H-NEW-88 has implicit single-test discipline; H-NEW-66 has explicit NOTABLE thresholds but no `alpha_bon`). Required fix: header amendments before execution.

## Recommendations for ledger update

1. **Promote to Tier-A:** H-NEW-53 (p=10⁻¹²), H-NEW-56 (p=10⁻¹³), H-NEW-57 (p=10⁻⁹) — anchor-class by extreme p-value alone. H-NEW-46.1 (chronology disentangle, STRONG-PASS) confirmed Tier-A. Cross-finding-008 promoted to project's 4th SYNTHESIS cross-finding.
2. **Promote to Tier-B:** H-NEW-49.1, H-NEW-51, H-NEW-58c, H-NEW-60, H-NEW-67 — all PASS-DIRECTED. Recommend explicit "post-hoc-noticed; replication required for upgrade to CONFIRMED" tag in ledger entries.
3. **Pre-reg gate amendments required before execution:** H-NEW-62, 64, 66, 83, 88 must add canonical PRE-REG-STANDARD-04 header fields. Most urgent: H-NEW-83.
4. **Cross-finding-008 documentation tightening:** rewrite §"The evidence" to disclose H-NEW-53/56 corpus dependence and H-NEW-55 feature-derivation dependence. Single-sentence amendment suffices.
5. **H-NEW-67 documentation tightening:** add explicit Bonferroni-2 calculation for dual-reading: α_bon = 0.025; observed p = 1×10⁻⁴ PASSES by 250×. Non-blocking tightening.
6. **Cross-finding-005 retraction status:** STANDS as RETRACTED per audit-033 close. No further action.
7. **MW-7 gate-spec layer:** reaffirm at integrator-level that pre-reg headers MUST carry canonical PRE-REG-STANDARD-04 fields. Body-text Bonferroni statements are not substitutes — auditor scans of header frontmatter must succeed. Consider this a STANDING REINFORCEMENT NOTE.

## Audit-completeness ledger

This audit covered:
- 8 post-hoc-noticed integrator deliverables (H-NEW-49.1, 51, 53, 57, 58c, 60, 63, 67)
- 1 cross-finding promotion (cross-finding-008)
- 1 cross-finding retraction (cross-finding-005, re-affirming audit-033)
- 14 in-flight specialist pre-regs (PRE-REG-STANDARD-04 gate-check)

Not covered (deferred for later result-stage audit):
- H-NEW-54 (extended root scan) — read but not deeply audited
- H-NEW-55 (multi-feature classifier) — referenced but not deeply audited
- H-NEW-56 (5-exceptions analysis) — referenced but not deeply audited
- H-NEW-46.1 (chronology disentangle) — covered in audit-033 layer; no new audit issue arose
- H-NEW-58 / 58b (referenced as instrument-validation foundation for H-NEW-58c)

## Closing

Wave-4 represents a productive but discipline-uneven push. The integrator-deliverable layer (post-hoc-noticed findings) is exemplary in disclosure discipline — every post-hoc finding is honestly tagged, capped at PASS-DIRECTED unless p so extreme survives any Bonferroni, and queued for independent-dimension replication. The pre-reg gate-layer is partially noncompliant — 5 of 14 specialist pre-regs need canonical header amendments before execution. The cross-finding-008 synthesis claim should be tightened in independence-framing but the central muqaṭṭāʿat-as-book-introduction-marker conclusion is robust.

**Single most important integrity-positive event of wave-4:** the H-NEW-META-4 NULL → cross-finding-005 retraction (audit-033). This audit re-affirms.

**Single most important integrity-defect of wave-4:** H-NEW-83 pre-reg missing all PRE-REG-STANDARD-04 fields. Pre-execution amendment required.

Filed under skeptical-auditor-wave-4 / audit-034.
