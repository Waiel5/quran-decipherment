---
audit_id: audit-008
finding_id: H-NEW-8
finding_title: Twin-opener character-length profile N(k) — Quran has localized excess of 25-40-char shared prefixes
audited_by: skeptical-auditor
date: 2026-04-13
parent: known twin-opener finding at k=30 (pre-existing, pre-team)
status: NEEDS REVISION
---

# Audit memo — H-NEW-8 (Twin-opener N(k) profile)

## Verdict: NEEDS REVISION

This is the team's second-strongest candidate. Strong pre-registration, a priori k-grid, dual-null protocol (intra-shuffle + cross-baseline), bimodal profile is interpretively coherent (k=5 formulaic, k=15–20 anti-repetition, k=25–40 parallelism), and the existence of known individual pairs at Q2:149-150, Q4:131-132, Q2:231-232 gives the effect a concrete target. Intra-shuffle z = +4.44 at k=28 is a real signal and is independent of the cross-baseline z = +7.11.

Three issues prevent PASSED. The most important — and computational-tester flagged it himself — is that z = +7.11 is computed against a 9-point sample standard deviation, which is a fragile statistic. The other two are the poetry-vs-prose symmetry in the baseline and a subtler concern about the k=15–20 "anti-repetition" interpretation.

## Critique items

### 1. n=9 baseline σ inflates cross-corpus z-scores (BLOCKING)
At k=20, Quran rate = 2.94×10⁻³, baseline mean = 3.15×10⁻⁴, baseline sd = 3.7×10⁻⁴. The z = +7.11 is computed as (Q − μ)/σ with σ estimated from **9 data points**. Under a small-sample t-distribution with df=8, the effective threshold for α=0.01 two-sided is t ≈ 3.36 — not the 2.58 gaussian equivalent. More critically, if baseline sd is itself uncertain (95% CI on σ with n=9 is roughly [0.68·σ̂, 1.83·σ̂]), the z can range from +3.9 to +10.5 depending on which σ we use. The headline +7.11 is the *point* estimate; it is not robust to σ uncertainty.

**Required**:
(a) Report **studentized p-values** under t_8, not gaussian z, for all cross-baseline claims.
(b) Report the **rank statistic**: is the Quran's rate at k=20 above ALL 9 baselines? (From the table, Quran = 2.94×10⁻³ vs baseline mean + 3σ = 1.42×10⁻³ — so yes, Quran is far above max-baseline.) The rank-based claim "Quran rate > max baseline rate" is robust to σ estimation and is the stronger non-parametric statement.
(c) **Expand the baseline pool** if feasible. Classical-scholar or existing project data may have access to: additional dīwāns (al-Farazdaq, Jarīr, Dhū al-Rumma), additional prose (al-Ṭabarī *Tārīkh* paragraphs, Ibn Isḥāq *Sīra* already in, al-Aṣmaʿī). Target n ≥ 15 for σ stability. Computational-tester flagged this; I'm seconding it as blocking, not optional.

### 2. Poetry-vs-prose baseline symmetry (BLOCKING)
Treating jāhilī dīwān *lines* symmetrically with Bukhari/Jāḥiẓ sentence-split is defensible only if the unit "adjacent line pair" in poetry is comparable to "adjacent sentence pair" in prose. Poetry lines are **metrically forced** to have the same length (per baḥr), which artificially constrains how many characters a "shared opening" can cover — a jāhilī qaṣīda's ṭawīl lines run ~60 characters each, so a 20-char shared opening is 1/3 of a line, whereas in Quranic verses (mean ~40 chars) a 20-char shared opening is half a verse. This asymmetry could systematically lower baseline rates at mid-k without any genuine difference in compositional density.

**Required**: recompute baseline rates **normalized by line/sentence length** — i.e. rate of shared-opening-length-≥-k/L where L is pair-mean length. Alternatively, restrict to line/sentence pairs where both elements exceed 2k characters. If the +7.11 at k=20 survives this normalization, the cross-corpus claim holds. If it attenuates below z = +2.58, the cross-corpus leg weakens and the finding reduces to the intra-Quran signal only.

Also: **separate poetry and prose baselines**. Report Quran vs 3-prose and Quran vs 6-poetry distributions separately. If the outlier is driven by prose baselines being very low (because their sentence boundaries are noisy), the result may be a prose-splitting artifact.

### 3. The k=15–20 "anti-repetition" interpretation is intriguing but under-powered (non-blocking, interpretive refinement)
At k=20 intra-shuffle, z = −1.02. This is *not statistically significant* — it's a 1-σ-below-null point. The author correctly reports it but then interprets it substantively as "active anti-repetition at the mid-length scale." A 1-σ fluctuation is exactly what a null model produces by chance; calling it "anti-repetition" over-reads the data.

But here is the genuine puzzle the author flagged: intra-shuffle at k=20 shows no excess (z=−1.02), yet cross-baseline at k=20 shows the *largest* excess (+7.11). How can the Quran be "normal vs its own shuffle" but "extreme vs classical Arabic" at the same k?

**The resolution** (and the author should make this explicit): the intra-Quran shuffle *preserves the rate at which the Quran produces 20-char shared prefixes* (since it shuffles which pairs occur adjacent, but any Quranic verse pair can produce the same prefix distribution). The cross-baseline comparison reveals that **the pool of Quranic verses** has a much higher rate of 20-char shared prefixes than classical Arabic, whether adjacent or not. This reframes: the finding is NOT "the Quran places 20-char twins at adjacent positions" (intra-null would show +z) — it is "the Quran has many more 20-char near-identical verse openings than classical Arabic at the whole-corpus level, and when you arrange them, many happen to land adjacent."

**Required (interpretive)**: rewrite the interpretation of the k=15–20 regime. It is not "anti-repetition" — it is "baseline Quran density of 20-char matches is high, and the shuffle preserves this density while destroying adjacency; intra-null z≈0 is correct and expected." The "anti-repetition" reading should be dropped unless supported by a different test (e.g. a k=20 pair-distance distribution, where anti-repetition would show pair-distances *longer* than null). Drop this sub-claim or test it separately.

### 4. Basmala exclusion convention — disclosed, fine
The basmala is excluded from the first-pair position. Standard. No issue.

## Alternative-explanation audit

1. **Poetry metrical constraint on baseline** (item 2) — most likely alternative for the cross-baseline signal. Highest priority.
2. **Small-n σ fragility** (item 1) — procedural.
3. **Quran-internal vocabulary recycling** — the Quran's lexical inventory is smaller than Jāḥiẓ's or Mutanabbī's (a known fact). Smaller vocabulary → higher baseline rate of identical short-k openings. Does this secondary fact account for the k=5 excess (z=+19 intra, +3.66 cross)? Possibly. Does it account for k=20–30 excess? Less clear, because shared 25-char openings aren't a vocabulary-size effect, they're a formulaic-phrase-reuse effect. Worth a check: compute Quran vs baseline mean-first-word-of-pair entropy as a vocabulary-size proxy; if Quran shows dramatically lower opening-word entropy, much of the k=5 and possibly k=10 excess may be vocabulary-size driven.
4. **Adjacent-pair ritual structure** — the k=25–30 excess is genuinely interesting and maps onto known classical *tashābuh al-maṭāliʿ* examples. This is the most compelling leg of the finding and the sub-claim most likely to pass. Items 1–2 affect the cross-baseline magnitude but not the existence of the localized excess bump.

## Classical cross-reference

Author cites al-Zarkashī *al-Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 52" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; nawʿ number retagged per MW-6 mechanical scan; substantive classical doctrine (al-mutashābih al-lafẓī) unchanged; statistical finding unaffected; candidate correct locus: nawʿ 37-47 range pending Phase-2 secondary-triangulation]** (al-mutashābih al-lafẓī) correctly. Al-Kirmānī's *al-Burhān fī mutashābih al-Qurʾān* is the canonical source for identifying and discussing these pairs verse-by-verse — the Q2:149-150 and Q2:231-232 pairs in the top-6 are each treated in al-Kirmānī's tradition. Al-Suyūṭī *Itqān* nawʿ 63 (al-mutashābih) gives the theoretical framing.

Worth noting classical scholars pre-identified many of these pairs qualitatively. The contribution here is **the curve** — the discovery that N(k) is bimodal and the mid-range dip, not the existence of individual twin-openers. If items 1–3 clear, the N(k) curve as an artifact of composition rather than chance is a legitimately novel operational statement of a classical qualitative observation.

## Robustness requests (blocking)

1. **Studentized p-values + rank statistic** for cross-baseline claims (replace gaussian z with t_8 and report max-of-baseline comparison).
2. **Length-normalized baseline rates** — rate-per-pair-per-mean-line-length, to control for metrical-line-length asymmetry in poetry baselines.
3. **Separate poetry/prose baselines** — report Quran vs 3-prose and vs 6-poetry distributions individually.
4. **Expanded baseline corpus** — target n ≥ 15 if available from existing project data.
5. **Drop the "anti-repetition" interpretation** at k=15–20 OR run a separate test (pair-distance distribution at k=20).

## Family-size note

Pre-registered k-grid has 12 points in {5…60}. Acceptance criterion is "at least one k in {25..40} passes both nulls at z>2.58." This is already Bonferroni-controlled because the acceptance was committed to a specific window; treating it as "any k" would require correction across 12 points. The author's stated window of {25..40} has 6 points (25, 28, 29, 30, 31, 32, 35, 40) — actually 8, not 4 — so Bonferroni-within-window is α=0.01/8 = 0.00125 per point. The intra-shuffle p=0.001 at k=28 *just* clears this. The cross-baseline p at k=28 is p=0.004 under gaussian — doesn't clear k=8 Bonferroni at 0.00125. Under t_8, the studentized p will be larger. This needs recomputation.

If H-NEW-8 is also measured against the across-finding family (8 findings total so far), per-finding α ≈ 0.006. Intra-shuffle p=0.001 clears; cross-baseline p needs item 1 redone.

## What would change the verdict

- **PASSED if**: (a) rank statistic "Quran rate ≥ max(baseline rates)" holds at k ∈ {25, 28, 29, 30} AND (b) length-normalized baseline test holds at z ≥ 3 in studentized-t form at same k AND (c) expanded baseline n ≥ 15 preserves cross-baseline signal.
- **REFUTED if**: length-normalized baseline comparison collapses the cross-baseline z to < 2 (meaning the original effect was poetry-metric-length artifact) AND rank statistic does not place Quran above all baselines.
- **REFINED if**: cross-baseline effect attenuates but intra-shuffle z = +4.44 at k=28 survives — finding becomes "within-Quran parallelism excess, baseline comparison inconclusive at current n."

## Cross-finding overlap flag for integrator

This finding operationalizes *tashābuh al-maṭāliʿ* (al-Kirmānī's explicit subject), which is a specific rhetorical doctrine distinct from al-Bāqillānī differentiation, al-Biqāʿī munāsaba, or al-Jurjānī naẓm. **This is a candidate 4th classical-doctrine leg** for the triangulation framework integrator is building (T-2 candidate). The doctrine: "the Quran systematically uses 25–30-char parallel openings as a rhetorical device (*mutashābih lafẓī*)."

If H-NEW-8 passes after revision, it would be an independent leg from al-Jurjānī naẓm (parallelism structure is pre-compositional templating, not naẓm's multi-axis composition theory), and importantly **not** from an axis already counted in T-2. Flagging this as a potential T-2 companion.

**M-pattern connections**: weakly touches M-3 (verse-as-composite-marker) — if verse openings are constrained to join a shared-prefix pool, the verse boundary is doing additional structural work. But this is indirect; H-NEW-5 mood-switch is a more direct M-3 instance. Not flagging as primary M-3 evidence.

## Lineage

Parent: known twin-opener finding at k=30 (the two-pair observation, pre-team). H-NEW-8 deepens this into a full N(k) curve. Integrator should tag parent = "pre-existing twin-opener observation (Q2:149-150, Q59:22-23) at fixed k=30."
