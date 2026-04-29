---
audit_id: audit-011
finding_id: H-NEW-20
finding_title: al-Rāzī linear-munāsaba CONFIRMED (Z=+30.76) + al-Biqāʿī corpus-wide ring REFUTED (Z=-2.51)
audited_by: skeptical-auditor
date: 2026-04-13
parent: null (classical-scholar claim #4, adjudication between two dominant 12–15c schools)
status: NEEDS REVISION
---

# Audit memo — H-NEW-20 (al-Rāzī vs al-Biqāʿī)

## Verdict: NEEDS REVISION

Stouffer Z = +30.76 is an enormous signal — p ≈ 10⁻²⁰⁰. That magnitude is itself a red flag and demands we verify it is measuring what the finding claims it measures, not a mechanical consequence of the corpus structure or the null's construction. The al-Biqāʿī refutation direction (Z = −2.51) is modest and its interpretation is separable.

Two concerns are blocking for the al-Rāzī confirmation; two are non-blocking. The al-Biqāʿī side I accept with minor framing edits. Overall this is close to PASSED on the al-Rāzī leg but requires explicit confounder rule-outs before I route to §1 — precisely because §1 entry is consequential.

## The "Z=30 demands extra scrutiny" principle

In this corpus, a statistic producing Z > 30 across 95 surahs against a within-surah null almost certainly reflects **at least one of three phenomena**:
1. A genuine, massive structural signal (the claim).
2. A trivial consequence of how the null was constructed versus what the observed data contains.
3. A feature of the text that is not specifically about "al-Rāzī linear coherence" but which the chosen operationalization happens to measure.

My job is to distinguish (1) from (2) and (3) before routing to §1. Here is the critical path.

## Critique items

### 1. The within-surah verse-order-shuffle null is weak against what the effect actually measures (BLOCKING)

**Claim in finding**: "verse_{k+1} is thematically closest to verse_k" (al-Rāzī). Operationalized as adjacent-verse Jaccard of QAC roots.

**The issue**: within-surah verse-order-shuffle destroys thematic contiguity but also destroys **every local grammatical/pragmatic contiguity the text has**. Adjacent Quranic verses share roots not only because of "linear coherence" (al-Rāzī's claim) but because of:

(a) **Pericope-block structure**: Many surahs contain narrative blocks where adjacent verses are literally continuations (e.g., the Joseph narrative in Q12 runs ~100 verses with the same cast and vocabulary; the Noah pericopes in Q11, Q26, Q54, Q71 each run 20-40 adjacent verses). Within such blocks, root sharing is mechanical — same story, same people, same objects. Shuffling destroys this block structure. The resulting Z measures "pericopes have thematically coherent adjacent verses," which is true but trivial — not al-Rāzī's specific insight.

(b) **Rhyme-cluster effects**: verses within a rhyme cluster tend to share grammatical suffixes and often roots (e.g., Q55's repeated *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain). This is an adjacency effect unrelated to linear-munāsaba.

(c) **Turn-taking and parallel-clause structures**: adjacent verses in dialogue surahs (H-NEW-14 population) have structurally parallel openings. Again an adjacency effect, not a linear-coherence effect.

**Required**:
(a) **Within-pericope shuffle null**. Partition each surah into coherent narrative/rhetorical blocks (using existing project pericope data or a simple rule: same rhyme-cluster, same prophet-pericope). Shuffle verses within blocks only, preserving block membership but destroying inter-block ordering. Rerun. Prediction: Z reduces substantially (possibly from +30 to +5 to +10 range). If the residual is still highly significant, the finding is robust.

(b) **Alternative null: Markov-surrogate null**. Use a word-level 2-Markov surrogate of the surah, rebuild verses of matched lengths, compute ρ_lin(1). This null preserves local word-adjacency statistics while destroying verse-level coherence. Prediction: if al-Rāzī is the right reading, ρ_lin(1) under Markov should be far below observed. If ρ_lin(1) under Markov is close to observed, the effect is a local-word-adjacency artifact, not a verse-level linear coherence signal.

These are the standard §1.3 and §1.4 nulls from statistical-rigor-protocol.md. The current verse-shuffle is §1.2 only.

### 2. Effect-size decomposition: what share is pericope-block, what share is genuine residual? (BLOCKING)

The 89.5% of surahs showing z > 0 is compelling but we need to know **how much of ρ_lin(1)'s elevation is block-structural vs residual**.

**Required**: for each surah, report:
- ρ_lin(1) — already reported.
- ρ_within-block(1) — Jaccard for adjacent verses *within the same pericope block*.
- ρ_cross-block(1) — Jaccard for adjacent verses *crossing a block boundary*.

If ρ_within >> ρ_cross, the signal is primarily block-internal (trivial). If ρ_within ≈ ρ_cross (both elevated), the signal survives block decomposition and genuinely supports al-Rāzī's "every transition motivated" at the block-crossing level — which is the actually striking claim.

This is the diagnostic that separates "pericopes have coherent internal verses" (mundane) from "al-Rāzī: even block-crossing transitions are motivated" (extraordinary).

### 3. Monotonic-decay gradient claim is weaker than it looks (non-blocking)

Gradient = ρ_lin(1) − ρ_lin(10), Z = +19.67 on 95 surahs. Note:
- For N ≤ 20 surahs, ρ_lin(10) is on only a handful of verse pairs. High variance.
- For surahs with strong pericope blocks of length 5–15 verses, ρ_lin(10) often crosses block boundaries while ρ_lin(1) stays within. So the gradient is again partly a block-structural consequence, not specifically a "monotonic decay" claim.

**Non-blocking recommendation**: report ρ_lin(k) at k=1,2,3,5,10,20,50 and show the full curve. If the curve is monotone-decreasing across the entire range, that is strong al-Rāzī support. If it is flat after k=3–5 (block-sized distance), the claim reduces to "within-block coherence" which is already covered by item 2.

### 4. Stouffer independence (the author flagged this; affirmed as non-blocking)

Shared-vocabulary via divine names, common particles, and Quran-wide high-frequency roots makes per-surah z-tests weakly dependent. Stouffer's Z inflates under positive dependence. True effective Z is smaller than +30.76. But even a 5× deflation to Z ≈ +6 would still be decisive if the block-null passes item 1 and the decomposition in item 2 shows survival. So this dependence concern is secondary — not a blocker — IF items 1 and 2 pass.

### 5. Al-Biqāʿī refutation — accepted with framing edit (non-blocking)

Stouffer Z = −2.51 for mirror-pair Jaccard, marginally failing Bonferroni k=4 (critical |Z| ≈ 2.81). Author's interpretation is correct: "no corpus-wide ring pattern" is the appropriate conclusion; individual surah ring-claims (al-Baqara is classically-cited) are not tested here and remain open.

**Recommended framing**: the al-Biqāʿī sub-result should be called "NOT SUPPORTED AS CORPUS-WIDE LEXICAL PATTERN," not "REFUTED." Two reasons: (a) Bonferroni non-clearing means we do not reject the null with confidence; (b) al-Biqāʿī's actual thesis is about *thematic* rather than *lexical* rings. A sentence-embedding version is a natural next test.

The framing edit matters for §3 routing: classify as "marginal negative result, lexical operationalization only" — not as R-006 refutation proper. This preserves the integrator's separation of clean refutations from marginal negatives.

## Alternative-explanation audit

1. **Pericope-block structure** (item 1–2) — highest priority alternative. If adjacent verses share roots primarily because of within-pericope continuation, the al-Rāzī "every transition motivated" reading overclaims. Must be ruled out.
2. **Rhyme-cluster sharing** — can inflate ρ_lin(1) via grammatical-ending roots (when rhyme is rooted rather than particle-based). Partial overlap with (1), handled together.
3. **Divine-name anchoring** — many surahs have divine-name refrains at verse-ends (e.g., *al-ʿazīz al-ḥakīm*, *al-ghafūr al-raḥīm*). These land as roots in adjacent-verse overlap. Non-central but worth a quick sensitivity: compute ρ_lin(1) with top-20 function roots (divine names, *qāla*, *kāna*, *allāh*, *rabb*) removed. Robustness check, probably non-blocking.
4. **Verse-length confound** — short verses share fewer root-tokens than long verses; if surahs have length-runs (3 short / 3 long patterns), adjacent pairs are length-matched and Jaccard is inflated by the size-matching. Minor.
5. **Genuine linear-munāsaba** (the claim) — likely explains at least part of the effect; need decomposition to estimate residual share.

## Classical cross-reference

Al-Rāzī's *Mafātīḥ al-Ghayb* doctrine of *irtibāṭ al-āyāt* is cited. Accurate. The exact al-Rāzī phrase is more often rendered as *irtibāṭ* (connection) than *munāsaba* (correspondence); he uses both but distinctively emphasizes causal/thematic *irtibāṭ* at each transition. Al-Suyūṭī *Itqān* nawʿ 62 on *munāsabāt* formalizes al-Rāzī's practice into eight sub-types (sababiyya, musabbabiyya, etc.).

Al-Biqāʿī *Naẓm al-Durar* argues for both linear and ring-composition layers — he does NOT deny al-Rāzī's linear claim, he *adds* a ring layer on top. So the right synthesis-framing is **not** "al-Rāzī vs al-Biqāʿī adjudicated" but "al-Rāzī linear is confirmed corpus-wide, al-Biqāʿī's additive ring claim is not supported at the lexical level." Classical-scholar should help refine the synthesis language; a strict adjudication between the two theses misreads al-Biqāʿī's position.

**Worth noting classically**: al-Sakhāwī's *Dalīl al-Fāliḥīn* and Ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* both endorse al-Rāzī's linear thesis. So the finding supports not one but a majority classical position. This is a strength for synthesis.

## Robustness requests (blocking for al-Rāzī §1 routing; non-blocking for al-Biqāʿī)

1. **Within-pericope shuffle null** — partition surahs into blocks (rhyme-cluster + prophet-pericope + thematic-section), shuffle within blocks, rerun. This is the §1.3 null.
2. **Word-Markov-2 surrogate null** — generate surrogate text preserving local word-adjacency, partition into matched-length verses, rerun. This is a §1.4 null.
3. **ρ_within-block vs ρ_cross-block decomposition** — separate block-internal from block-crossing adjacency.
4. **Full ρ_lin(k) curve** for k=1,2,3,5,10,20,50 — the monotonic decay claim requires the shape.
5. **Function-root sensitivity** — rerun with top-20 most common roots removed.

## Family-size note

Within-finding k=4 (r1, gradient, ring-anomaly, composite) — correctly applied. Al-Rāzī passes at critical |Z|=2.81 trivially. Al-Biqāʿī fails at −2.51.

Across-finding family: if we are now at ~10 findings in the novel-discovery panel, family α ≈ 0.005. Z=+30.76 clears trivially; Z=−2.51 does not. Consistent with my recommended framing edit (al-Biqāʿī as "not supported" rather than "refuted").

## What would change the verdict

**For al-Rāzī confirmation**:
- **PASSED and routed to §1 if**: (a) within-pericope shuffle still shows Stouffer Z ≥ 5, (b) ρ_cross-block(1) > null by z ≥ 3 per-surah, (c) full ρ_lin(k) curve is monotone-decreasing through k ≥ 10.
- **REFINED to "within-pericope linear coherence" if**: within-pericope null halves Z to ~+10 but cross-block residual is small (ρ_cross-block ≈ null). Finding reframes as "pericopes are internally coherent," which is true but not the extraordinary claim.
- **REFUTED if**: within-pericope null Z falls below +2.58, meaning the entire effect was block-structural. Extremely unlikely given the magnitude, but the test must be run.

**For al-Biqāʿī side**:
- **Framing edit to "not supported, lexical operationalization only"** — accepted without further work.
- **Future work**: semantic-embedding version of ring test is the natural next step. Not this audit's scope.

## Cross-finding overlap flag for integrator

1. **This is the team's strongest candidate for §1 entry.** But it requires the block-null rule-out. If that passes, route al-Rāzī side to §1 as first PASSED novel confirmation and first PASSED classical-doctrine recovery. Do NOT route before the block-null runs.

2. **Framing of al-Biqāʿī**: I recommend R-006 be labeled "marginal non-support, lexical operationalization" rather than a clean refutation. It joins the watchlist you mentioned (pattern: classical claims fail as universal-law operationalizations, may survive as rhetorical-affordance or non-lexical reformulations). Companions: R-001 al-Suyūṭī, R-005 al-Kirmānī directionality. **This is becoming M-5 territory** — the pattern of "classical doctrines don't transmit as universal statistical laws; they transmit as rhetorical-affordance claims or non-lexical correlations." I formally propose **M-5 CANDIDATE: "Classical doctrines as rhetorical affordances, not universal laws"** with three instances now (R-001, R-005, R-006 pending). Promotion gate: one more instance of a classical claim that is refuted literal-operationally but survives reformulation.

3. **Corroborator for master chiastic finding**: integrator's note that this joins the pre-existing chiastic-audit r = −0.018 as a second non-ring corroborator at a distinct axis — agreed. Two independent nulls (between-layer correlation + mirror-pair Jaccard) converge. Strong.

4. **M-2 relevance (gradual-continuum)**: the 89.5% of surahs showing individual z > 0 for al-Rāzī ρ_lin(1) is the opposite of a partitioned pattern — it's continuous, pan-corpus, gradual. **Adds an M-2 leg**: al-Rāzī linear coherence is a universal pan-surah property, not a partitioned one (e.g., Meccan-only or long-surah-only). Strong M-2 evidence if the finding survives the block-null.

5. **T4 integration**: al-Rāzī linear coherence is a plausible 13th constraint for T4's simultaneous-constraint framework (adjacent-verse root-sharing). If T4 survives its own audit, integration question: is ρ_lin(1) already partly captured by T4's rhyme/rime constraint, or is it additive? Flag for synthesis.

## Lineage

Parent: null. Adjudication between classical-scholar claim #4 (al-Rāzī vs al-Biqāʿī).
Corroborates: MASTER chiastic-audit finding (second leg of non-ring corroboration).
Closes watch-seam: W-1 al-Rāzī linear × chiastic audit (pending the block-null rule-out).
Candidate sibling: H-NEW-20-EXT for semantic-embedding al-Biqāʿī reformulation.
