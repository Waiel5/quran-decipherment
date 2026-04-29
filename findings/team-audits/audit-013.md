---
audit_id: audit-013
target_finding: team-discovery-012 (H-NEW-2 pronoun-chain entropy)
auditor: skeptical-auditor
date: 2026-04-12
verdict: NEEDS REVISION
parent_finding: H-NEW-2 pre-reg + MASTER:iltifat classical framing
cc: integrator
---

# Audit-013 — H-NEW-2 pronoun-chain entropy signature of iltifāt

## Verdict: NEEDS REVISION

The double-result framing (H_A pre-reg REFUTED in opposite direction, H_B pre-reg CONFIRMED three channels) is methodologically clean and a model of falsifiable design. I commend the simultaneous pre-registration and the 300-perm null. However, the interpretive claim — "classical iltifāt theory vindicated" — is not established by the current null model, and the Z≈60–80 magnitude warrants the same "too good to be true" scrutiny I applied to H-NEW-20 (Z=+30.76). Four issues gate promotion.

## Blockers

**B1. Pericope/narrative-block confound (primary).** The within-surah marginal-preserving shuffle destroys *all* chain correlation, including trivial referent-tracking within a single narrative pericope. A sustained Yūsuf pericope (Q12) tracks a 3MS referent for dozens of verses; a sustained direct-address homiletic block tracks 2MP for dozens of verses. Low pronoun-entropy is the expected signature of *any* text with pericope-scale topical segmentation, not specifically of *iltifāt architecture*. The stricter null — within-pericope/narrative-block shuffle preserving block boundaries — is required to isolate the iltifāt-specific signal from the mundane pericope-structure signal. Parallel to audit-011's demand on H-NEW-20.

**B2. No iltifāt ground-truth correlation.** The author flags this (Limit 3). Without per-surah correlation between pronoun-chain z-score and a hand-annotated iltifāt-density catalog (at minimum the surahs al-Zarkashī nawʿ 47 and al-Suyūṭī nawʿ 56 cite as iltifāt-rich), the claim reduces to "pronoun chains are block-structured," which is weaker than and different from "iltifāt architecture detected." Classical-scholar can produce this catalog.

**B3. Markov-k surrogate null (author-flagged, run it).** Limit 1 acknowledges that Markov-2 is the stronger null. At Z≈-77 the effect will likely survive, but the reduction factor matters for interpretation — if Markov-2 collapses Z from -77 to e.g. -8, that tells us most of the signal is first-order chain stickiness (a person-tag copies its predecessor), which is the pericope-structure confound reconceived. Run k=2 and k=3.

**B4. Referent-aware re-analysis.** 3MS→3FS within a single referent-chain (e.g., a dialogue between two characters) is functionally continuation, not shift. The 14-tag coarse scheme records it as a shift. This doesn't threaten the direction of the result (shift-density LOWER than null) but it means the reported effect size is itself biased — true referent-aware shift density is even lower than measured, making the H_B result qualitatively robust but quantitatively imprecise.

## Framing edit (non-blocking)

Text lines 52–65 claim "classical theory empirically vindicated at the channel level" and that "modern 'surprise' framing of iltifāt needs revision." This overclaims on the current evidence. What is established:

- Quranic pronoun chains are block-structured (confirmed under marginal-shuffle null).
- This is **consistent with** classical iltifāt framing (al-Zarkashī's *al-intiqāl min ṣīgha ilā ṣīgha* presumes stable sides).
- It does **not yet** demonstrate that the measured block-structure is specifically the iltifāt signal as opposed to pericope structure.

Suggested revision: "Pronoun chains are substantially more block-structured than their marginal-matched shuffle. This is consistent with — but under the current null does not uniquely identify — iltifāt architecture."

## What would change the verdict to PASSED

1. Within-pericope shuffle null holds the effect at |Z| > 2.81 Bonferroni-corrected, OR Markov-2 surrogate null does.
2. Per-surah z-score correlates positively with iltifāt-density from a hand-annotated catalog of al-Zarkashī nawʿ 47 / al-Suyūṭī nawʿ 56 example surahs (Spearman ρ > 0 at p < 0.01).
3. Framing revised to separate "block-structured pronoun chain" (confirmed) from "iltifāt-specific architecture" (requires B2).

Either of (1) — stricter null — OR (2) — ground-truth correlation — alone suffices for PASSED, if paired with framing revision (3). Both together would be a clean promotion to §2 with potential §3 candidate status.

## Strengths (logged for the record)

- Simultaneous H_A/H_B pre-registration with genuine falsifiability on both sides is the cleanest experimental design in the Phase-B slate.
- 100% / 98.6% / 98.6% of 73 qualifying surahs on predicted side under the reported null is a real effect direction, even if the effect size is inflated by B1.
- Full garden-of-forking-paths disclosure, a priori feature set, no post-hoc selection.

## Meta-pattern notes

This finding — if revised per B1/B2 — would be a candidate data point for M-5 CANDIDATE (classical doctrines as rhetorical affordances operationalizable but not literally recovered). The current "classical theory vindicated" framing, if held literally, fights the M-5 pattern; the revised framing ("consistent with, operationalized as") fits it cleanly. Flagging for integrator.

Cross-ref: audit-011 (H-NEW-20) for the parallel pericope-null issue. If both H-NEW-2 and H-NEW-20 survive stricter nulls, the pericope-block structure of the Quran becomes a findable phenomenon in its own right, distinct from the classical doctrines built on top of it.
