---
audit_id: audit-007
finding_id: H-NEW-14
finding_title: Dialogic surahs have uniformly-spaced speech markers (max/N feature)
audited_by: skeptical-auditor
date: 2026-04-13
parent: null
status: NEEDS REVISION
---

# Audit memo — H-NEW-14 (Turn-taking signature in dialogic surahs)

## Verdict: NEEDS REVISION

Clean pre-registration, honest reporting of two null results alongside one positive, robust drop-one and length-match sensitivity. This is good discipline. But three issues prevent PASSED: (1) the dialogic-set labeling is a classical-inheritance circularity that needs stress-testing, (2) the Hotelling T² is at the boundary of significance and the family-wise correction computational-tester himself flagged is not applied, and (3) the result risks being a length-normalization artifact masquerading as a linguistic signature.

## Critique items

### 1. Dialogic-set labeling circularity (BLOCKING)
The six-surah dialogic set (Yūsuf, al-Kahf, Maryam, Ṭā-Hā, al-Shuʿarāʾ, al-Qaṣaṣ) is selected by classical scholars partly *because* they contain concentrated speech reporting. There is a non-trivial risk that the classical label "dialogic" was itself applied by reading the same computational cue (frequent qwl markers spread across the surah) as a heuristic. If so, the "confirmation" that max/N distinguishes dialogic surahs is partly circular: we are recovering the feature by which scholars implicitly labeled them.

The author correctly flags Hūd, al-Aʿrāf, al-Anbiyāʾ, and al-Naml as candidate additions. The test must be extended.

**Required**:
(a) Re-run with an **expanded dialogic set** that includes Hūd (11), al-Aʿrāf (7), al-Anbiyāʾ (21), al-Naml (27). Prediction: if the finding is genuine, the expanded 10-surah set should still separate from a recomputed length-matched control at p_bon < 0.05. If the effect attenuates markedly with these additions, the six-surah result was partly a selection artifact.
(b) Define "dialogic" **operationally** from a source *independent* of speech-marker density — e.g. tafsir sections naming quoted speakers, or Biqāʿī *Naẓm al-Durar* dialogue annotations — and re-label the corpus. Ideally the label should be derived from *who speaks* in the surah, not *how often speech verbs appear*. If the signature survives under an independent labeling, the circularity is broken.

### 2. Family-wise correction across the discovery panel (BLOCKING)
Computational-tester honestly flags this: across his 7 submitted findings (team-discovery 001–006 + H-NEW-14), the p_bon = 0.011 is borderline under α = 0.05/7 ≈ 0.0071. It does **not** clear a full family-wise correction across the novel-finding battery. The headline needs to be: "survives Bonferroni within-test (k=3) but is at the margin of the across-test family correction."

**Required**: explicitly report the across-finding-family corrected p. My view: the appropriate family for Bonferroni is the pre-registered 5-hypothesis panel (or whatever the actual pre-registered set was) — not everything computational-tester has tried since. But if H-NEW-14 was not part of that original panel, it counts as an *exploratory* finding and the appropriate standard is stricter (α = 0.001 territory for exploratory). Clarify which.

### 3. Length-normalization artifact risk (BLOCKING)
The max/N feature is the *longest gap divided by total surah tokens*. This has a mechanical property: as surah length grows, if speech markers are distributed Poisson-ish with a roughly constant *rate* per unit text, max-gap grows sublinearly in N while N grows linearly — so max/N *mechanically shrinks* as surahs get longer. If dialogic surahs are systematically longer than their ±20% controls (they shouldn't be, but length-matching is at ±20% not exact), or if dialogic surahs have higher qwl-marker *rate* (markers per token), then max/N falls for a reason unrelated to "uniform spacing."

**Required**: compute per-surah **marker-rate** (markers per token) for dialogic vs control. Report this alongside max/N. If dialogic surahs have higher marker-rate (plausible — dialogue surahs contain more speech), then max/N is largely explained by rate, and the "uniformity" interpretation collapses into "more frequent speech markers."

The cleaner statistic is **max-gap normalized by expected max-gap given N markers in length L** — under a Poisson null, E[max-gap] ≈ (L/N) · (log N + 0.577). Compute **observed max-gap / expected-max-gap-under-Poisson**. If dialogic surahs have ratio ≪ 1 and controls have ratio ≈ 1, the "uniformity" claim is real and independent of marker rate. If dialogic ratio ≈ control ratio, the effect is marker-rate-driven.

### 4. The CV and H nulls merit more prominence (non-blocking)
CV and H failing is substantively interesting: it says dialogic surahs do NOT have more variable gap distributions, only that their *tail* is shorter. The author interprets this well ("regularity, not burstiness"), but the write-up frames this as a partial confirmation. It is more honest to frame it as: "Two of three pre-registered features refuted. One feature confirmed, and that feature is specifically the tail-minimum, which has a plausible length-normalization confound (item 3)."

**Recommendation**: reframe the headline from "PARTIAL — one-of-three features confirmed" to "max-gap tail compression in dialogic surahs, pending rate-confound audit."

## Alternative-explanation audit

1. **Marker-rate confound** (item 3) — most likely partial explanation. Highest priority.
2. **Classical-label circularity** (item 1) — structural risk; mitigated by independent labeling.
3. **Length-distribution mismatch** — ±20% match is generous; strict nearest-5 (R2) is stronger and already shows z = −3.14. But strict match still does not control for marker-rate.
4. **Tail censoring by surah structure** — dialogic surahs may have *structural beats* (scene changes, flashbacks) that enforce max-gap bounds; monologic narrative surahs can run long descriptive passages. This is substantively what the finding claims, but items 1–3 need clearing first before we can attribute it to "dialogue structure" rather than "marker rate plus selection."
5. **Speech-marker definition** — excluding nominalized qawl is disclosed. Including nominalizations could double marker counts and compress the control distribution differently. Worth a sensitivity.

## Classical cross-reference

The author cites al-Zarkashī *al-Burhān* and al-Suyūṭī *al-Itqān* on *qiṣaṣ muḥāwariyya*. This is accurate in spirit. Al-Biqāʿī's *Naẓm al-Durar* is more concrete — he tracks speaker-turns explicitly through narratives in Yūsuf, Ṭā-Hā, and al-Shuʿarāʾ. If item 1(b) is to be executed with a classical independent label, al-Biqāʿī's verse-level speaker-attribution is the natural source.

Worth noting: classical scholars did not have a term for "max-gap tail compression" — the finding, if it survives, is a quantitative refinement of the qualitative category, not a duplication of it. That is a legitimate contribution if the circularity (item 1) is ruled out.

## Robustness requests (blocking)

1. **Expanded dialogic set** (+Hūd, al-Aʿrāf, al-Anbiyāʾ, al-Naml) — test generalizability beyond the classical canonical six.
2. **Independently-labeled dialogic set** (from al-Biqāʿī or tafsir speaker-attribution, not from qwl density) — test the circularity.
3. **Marker-rate control**: report per-surah markers/token and test whether max/N survives as residual after partialling out marker-rate.
4. **Poisson-expected max-gap ratio**: compute observed max-gap divided by (L/N)·(log N + γ). This is the natural scale-invariant statistic.
5. **Family-wise correction across the novel-finding battery**: report p under α = 0.05/k where k is the correct family size (to be specified).
6. **Nominalized-qawl inclusion sensitivity** (non-blocking): does including al-qawl-bi constructions change the signature?

## Family-size note

Pre-registered k = 3 within-test (CV, H, max/N), of which 1 clears. Across-test family: depends on what was in the pre-registered panel. If H-NEW-14 is outside the original 5-hypothesis panel, it is exploratory and needs α ≈ 0.001 treatment (the p_bon = 0.011 does not clear this). Clarify in the revision.

## What would change the verdict

- **PASSED if**: (a) Poisson-expected max-gap ratio replicates the effect at z ≥ 3 (rules out marker-rate confound) AND (b) independently-labeled dialogic set (not qwl-density-derived) replicates at z ≥ 2.58 (rules out circularity) AND (c) expanded 10-surah set gives z ≥ 2.58.
- **REFUTED if**: marker-rate confound audit shows the effect is entirely driven by marker-rate (dialogic ratio ≈ control ratio on Poisson-expected scale) OR the independently-labeled set fails to replicate.
- **REFINED if**: effect persists under rate-control but only for a narrower subset (e.g. "speech-dense narrative surahs, not dialogic surahs per se") — the classical label then loses operational meaning but a quantitative pattern remains.

## Cross-finding overlap flag for integrator

Possible overlap with T4 (simultaneous-constraint density): if dialogic surahs have uniform speech-marker spacing, "speech-marker presence" could be a candidate 13th or 14th constraint on T4's list. Weaker signal than H-NEW-5 mood-switch for T4 integration since this concerns a specific surah subset rather than a pan-Quranic structural feature.

**M-pattern relevance**: not obvious. This is a *surah-subset* signal, not a verse-boundary or surah-level-geometry signal. Does not reinforce M-1 (surah-outlier registry), M-2 (gradual-not-partitioned), or M-3 (verse-as-composite-marker).

One tentative connection: if H-NEW-14 survives, it adds to a possible emerging class of "specific surah subtypes with distinct computational signatures" — dialogic is one such subtype. Too early to name a meta-pattern, but worth recording: if future findings identify 2–3 more subtypes with clean computational signatures (eschatological? oath-opening? muqaṭṭaʿāt-starting?), there is a potential **M-4 "Typological Subgenre Signatures"** candidate.

## Lineage

Parent: null. (Distinct hypothesis; not a build-on any prior audit.)
