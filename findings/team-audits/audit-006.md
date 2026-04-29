---
audit_id: audit-006
finding_id: H-NEW-5
finding_title: Verse boundaries concentrate syntactic mood-switches above within-verse rate
audited_by: skeptical-auditor
date: 2026-04-13
parent: null
status: NEEDS REVISION
---

# Audit memo — H-NEW-5 (Mood-switch concentration at verse boundaries)

## Verdict: NEEDS REVISION

This is the strongest candidate confirmation from the team to date. Effect size is large (Δ rate = +0.061, z = +10.68 vs the strict null), the null is appropriate (mood-sequence shuffle preserves verse-length structure — exactly the right control for the "same-verse mood coordination" confound), the effect is pan-Quranic (73% of surahs positive, binomial p = 3×10⁻⁶, not a few-surah artifact), and it survives dropping short surahs. The pre-registration and statistic design are clean.

That said, four issues prevent a direct PASSED verdict. None kills the finding; all are solvable with modest additional compute.

## Critique items

### 1. The "default IND" assignment is a non-trivial choice (BLOCKING)
QAC's convention: `IMPF` tokens *without* an explicit `MOOD:` feature get labeled `IND`. In practice this means a very large share of the corpus's imperfect verbs default into IND. If that assignment is wrong for even a few percent of tokens — e.g. if unmarked imperfects in syntactic positions demanding SUBJ/JUS are defaulted to IND — the internal mood-switch rate is artificially suppressed (because ambiguous imperfects get a single label), and the boundary rate will appear elevated by contrast.

**Required**: rerun the test with a **3-way collapse** (IMPV / PERF / IMPF-pooled — where IND, SUBJ, JUS all collapse to IMPF). My prediction: the effect attenuates but survives with z ≥ 5. If the effect is ≥ z 3 in the 3-way scheme, the finding is robust to the IND-default confound. If it collapses to z < 2, the finding depends on the exact QAC mood-annotation convention and requires further investigation into whether SUBJ/JUS defaults at boundary vs internal positions explain the apparent concentration.

### 2. Position bias — verse-initial verbs may be systematically different (BLOCKING)
Arabic verse-initial positions often carry imperatives, vocatives, or conjunction-preceded verbs (wa-, fa-, qul). If verse-initial verbs have a strongly distinct mood profile (e.g. verse-initial IMPV rate is elevated), the "boundary switch" is actually a "verse-initial position effect" — not a boundary *transition* effect. The test compares (verb_last_of_verse_k, verb_first_of_verse_{k+1}) against within-verse verb-pairs, which conflates "verbs at different positions in the verse" with "verbs crossing a verse boundary."

**Required**: compute the per-mood rate at (a) verse-initial position, (b) verse-final position, (c) verse-interior positions. If verse-initial verbs have a markedly different mood distribution (χ² vs overall imperfect-marginal), the boundary effect is partly positional, not purely transitional. Quantify: the bookended "positional" Δ-rate versus the "transitional" Δ-rate.

**Related**: does the effect survive restricting the boundary comparison to **same-speaker adjacent pairs** (excluding pairs where tafsir attribution changes)? Author correctly notes (interpretation reading #2) that speaker-switch is confounded with mood-switch. This needs testing, not just mentioning.

### 3. Classical-Arabic baseline comparison (BLOCKING)
The finding states that verse boundaries as mood-shift units are "to my knowledge — not a framework classical scholars developed." This is the novel angle, but: the statistical effect may not be Quran-specific. Classical Arabic saj' prose (rhymed prose) has its own punctuation-via-rhyme-clause convention; mood coordination within a saj' clause and mood shift across saj' clauses is a plausible linguistic universal for rhymed/punctuated Arabic.

**Required**: identical statistic on matched classical Arabic baseline:
- Bukhari (non-saj' prose) — should show near-zero effect.
- A saj' prose sample (Ibn ʿArabī, al-Jāḥiẓ's *Kitāb al-Bukhalāʾ*) — should show weaker but directionally-positive effect.
- The Muʿallaqāt (rhymed poetry) — effect sign uncertain; poetry mood patterns are constrained by meter.

If Bukhari shows near-zero and the Quran shows +0.061, the finding is Quran-specific (strong). If saj' prose shows +0.03–0.05, the Quran's effect is amplified saj'-style (real but not unique). If the effect is equal or exceeded in saj' prose, the finding reduces to a saj'-convention result.

### 4. The negative null mean raises a subtler concern
The null mean under N2 is −0.0213 — meaning the null places the internal rate *above* the boundary rate. This is the correct direction given same-verse mood coordination. But: the observed Δ = +0.0610 is 10.7σ above this negative null mean, which means the "absolute-Δ" between observed and null is 0.082. Interpret carefully: the headline number is not "boundaries flip 6% more often than internal" but "boundaries flip *at all* while random mood-sequence shuffling within verse-structure would predict internal-flip higher than boundary-flip by 2%."

**Recommendation** (non-blocking): rewrite the interpretation to emphasize that the **direction** of the result (boundary rate > internal rate) is contrary to the random-shuffle baseline. The 10.7σ z is real, but its substantive interpretation is "the Quran inverts the default mood-coordination expectation, placing shifts AT boundaries rather than distributing them as shuffle would." That framing is stronger and more honest than the raw Δ-rate comparison.

## Alternative-explanation audit

1. **Speaker-switch confound** (author's reading #2) — most likely partial explanation. Needs direct test (item 2 above).
2. **Sentence-closure convention** — Arabic sentences tend to end with perfective verbs or noun predicates; if a disproportionate share of verse-final verbs are PERF and verse-initial verbs are IMPV, the boundary effect is a sentence-closure convention, not a rhetorical device. Item 2 audit addresses this.
3. **QAC annotation artifact** (author's reading #3) — item 1 addresses this.
4. **Rhyme-constraint secondary effect** — verse-final verb choice is constrained by rhyme; certain roots gravitate to verse-final under particular rhyme schemes. This could secondarily constrain mood. Item 2's position-specific mood-rate analysis will partially reveal this.
5. **Classical saj' convention** — item 3 addresses this.

## Classical cross-reference

The author correctly notes classical iltifāt theory covers person-shift and tense-shift but not mood-shift. This is accurate: al-Zarkashī *Burhān* naw' 61 on iltifāt enumerates six categories (person, number, tense, addressee-framing, predicate-type, construction) — mood *could* be subsumed under "construction" but is not separately catalogued. Ibn al-Athīr's *al-Mathal al-Sāʾir* has an extensive iltifāt taxonomy, also without an explicit mood category.

**Important qualifier**: the fact that classical scholarship did not catalogue mood-shift as an iltifāt category does NOT mean classical scholars did not notice it. Classical grammatical analysis (Sībawayhi, al-Mubarrad) is very sensitive to mood morphology; what was missing was the specific *rhetorical* framing of mood-shift as a verse-boundary phenomenon. If this finding survives, the contribution is "operationalizing a classical grammatical observation as a rhetorical register feature", not "discovering an unnoticed structural property."

## Robustness requests (blocking)

1. **3-way mood collapse** (IMPV / PERF / IMPF-pooled) — most critical, tests the IND-default assignment.
2. **Position-specific mood-marginal rates** (verse-initial, verse-final, interior) with chi-square on distribution differences.
3. **Classical Arabic baselines** (Bukhari prose, saj' sample, Muʿallaqāt) with the identical statistic.
4. **Speaker-switch confound**: use the tafsir attribution (if available from existing project data) to restrict to same-speaker adjacent pairs and report the boundary-vs-internal Δ.

## Family-size note

Pre-registered k = 5 hypotheses (the team panel). Bonferroni per-test α = 0.002; empirical p < 10⁻⁴ clears this trivially. My requested sensitivity battery adds 4 more tests (3-way collapse, position rates, 3 baselines, speaker-split) = 8 new tests. If the effect survives ≥ 2/3 of those with z ≥ 3.0 on the critical 3-way-collapse, finding holds under expanded family.

## What would change the verdict

- **PASSED if**: 3-way mood collapse gives z ≥ 3.0 AND at least one of (position-specific check rules out pure position effect, baseline test rules out pure saj' convention) gives a ≥ 3σ differentiator from the alternative explanation.
- **REFUTED if**: 3-way collapse gives z < 2.0 (the finding is annotation-driven) OR saj' baseline shows equal-or-greater effect OR verse-initial/final position effect fully accounts for the Δ.
- **REFINED if**: baseline shows saj' prose has half the effect — finding retains as "Quran amplifies saj' mood-shift convention."

## Cross-finding overlap flag for integrator

This finding relates directly to **MASTER's T4 simultaneous-constraint result** (mean 4.18 constraints/verse; iltifāt +41.3pp in Quran). If mood-switch is added as a 13th constraint to that framework, verse-boundary becomes a higher-constraint-density locus. Potential T4 build-upon: the discovery here — boundaries as mood-shift sites — is precisely one of the constraint types T4 measures but does not atomize. An **integration opportunity**: mood-switch is a candidate new constraint on T4's list, not a standalone finding competitor. Flag to integrator: does T4's iltifāt category already encompass mood-shift, or is this additive signal?

**Second flag — possible M-3 candidate**: the Quran's verse is multiply marked — rhyme (known), mood-shift (this), iltifāt person-shift (known), constraint-density peak (T4). "The Quranic verse is a multi-constraint-marked unit beyond what comparable Arabic prose/poetry delivers" is an emerging meta-pattern. If more constraint types concentrate at verse boundaries in future findings, M-3 "Verse-as-Composite-Marker" graduates. Not ready to name yet; recording the prompt.

## Lineage

Parent: null. (Related: T4 simultaneous-constraint finding from the parallel track — recommend integrator link the two in synthesis.)
