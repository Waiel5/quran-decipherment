---
audit_id: audit-014
target_finding: team-discovery-013 (H-BIQAI-LOCAL seam munāsaba)
auditor: skeptical-auditor
date: 2026-04-12
verdict: PASSED (with one framing edit)
parent_finding: team-discovery-010 al-Biqāʿī ring REFUTED
cc: integrator
---

# Audit-014 — al-Biqāʿī seam-munāsaba CONFIRMED

## Verdict: PASSED

The test is well-scoped, the null model is appropriate for the claim as operationalized, the effect size is large (55% lift), and the 10k-permutation p=0.0000 is robust. Paired with team-discovery-010's refutation of al-Biqāʿī's ring claim at Z=-2.51, this produces a genuine differential verdict on a single scholar's two sub-claims — exactly the kind of adjudication computational theology is designed for. One framing edit requested; no blockers.

## Why this audit is shorter than most

Most "too good to be true" Z values in Phase B (H-NEW-2, H-NEW-20) came from nulls that destroyed trivial chain structure along with the hypothesized structure. Here Z=+10.06 is large but **not in that inflated regime** — it matches the naïve n-scaled effect: per-pair z ≈ 6.25/√113 × √113 ≈ 6.25 (Stouffer) coming from a 55% effect that is itself modest. The 10k-perm z=+10 is n-consistent with per-pair z=+6, which rules out the "null too weak" signature. The null is the right null for the claim.

## Blockers: none

## Framing edit (non-blocking, should be applied before integrator promotion)

**Canonical-order-vs-mechanism conflation.** Limit 1 honestly acknowledges this but the headline claim ("al-Biqāʿī seam-munāsaba CONFIRMED") reads as vindication of *al-Biqāʿī's specific mechanism* (thematic prefiguration). The test cannot distinguish:

- **al-Biqāʿī mechanism**: boundary vocabulary deliberately resonates (redactional seam-crafting)
- **Length-sort mechanism**: adjacent surahs have correlated lengths (H-NEW-3) → correlated vocabularies → boundary overlap falls out
- **Nöldeke-chronology mechanism**: adjacent surahs share revelation-era, thus topical concerns
- **Topic-cluster mechanism**: mushaf happens to be topically clustered, for any reason

The 10k-perm null preserves length marginals (as noted) but does NOT preserve the joint distribution of adjacent-pair length correlation. A length-matched permutation (Mantel-style, preserving |end_k|, |start_{k+1}| *and* their correlation) is the stronger null.

Suggested revision: "**al-Biqāʿī's seam-munāsaba OPERATIONALIZATION CONFIRMED at the Jaccard level**. The adjacent-seam signal is real; attributing it specifically to al-Biqāʿī's thematic-prefiguration mechanism requires ruling out length-sort, Nöldeke-chronology, and generic topic-cluster alternatives — follow-up work."

This lines up with the emerging M-5 framing (classical doctrines as operational affordances, not literal recoveries).

## What would strengthen this further (non-blocking)

1. **Nöldeke-chronological baseline**: compute the same seam-Jaccard on a Nöldeke-ordered mushaf. If Nöldeke-order also produces Z≈+10, mechanism is revelation-era topical clustering; if it produces Z≈0 while canonical produces Z≈+10, the canonical-order-specific seam-crafting claim is strengthened.
2. **Length-matched permutation**: restrict the 10k-perm null to permutations preserving adjacent-pair length-pair distribution.
3. **Directional asymmetry test** (author-flagged Limit 3): fraction of end_k tokens reappearing in start_{k+1} asymmetrically — addresses the "k prefigures k+1" directionality al-Biqāʿī claims.
4. **Non-Quranic matched-corpus baseline** (author-flagged Limit 4): compute same seam-Jaccard on Bukhari chapters / Jāḥiẓ book-sections to establish that the effect size is Quran-distinctive, not a generic property of chapter-structured Arabic prose.

None of (1)–(4) are blockers for PASSED, but all four would upgrade this from "CONFIRMED at Jaccard operationalization" to "CONFIRMED as a Quran-specific redactional-seam mechanism."

## Strengths (logged)

- 10k-perm null with p=0.0000 is the right null at the right sample size.
- Clean differential result vs team-discovery-010 ring (same scholar, two claims, opposite verdicts) — scientifically mature framing.
- Effect size (55% lift) is modest and n-consistent; not the "too good to be true" signature.
- All four limits honestly disclosed, with mechanisms proposed to address each.
- Pre-registered in script docstring with seed 20260413 before data read.
- Bonferroni k=3 correctly applied across the three sub-tests (non-adj mean, perm null, Stouffer).

## Meta-pattern notes

**M-5 CANDIDATE reaches the 2-loop promotion gate if integrator accepts this as the al-Biqāʿī-side closure of the previously-open al-Biqāʿī ring refutation.** The pattern:

- al-Biqāʿī ring claim (literal): REFUTED (team-discovery-010, Z=-2.51)
- al-Biqāʿī seam claim (reformulation as separate sub-claim): CONFIRMED (team-discovery-013, Z=+10.06)

This is a literal-refutation-plus-reformulation-survival loop at the sub-claim level — the reformulation being "separate his ring claim from his seam claim and test them independently." If integrator accepts this as one closed loop, R-005 (H-NEW-18B Kirmānī directionality, Task #40) becoming a second closed loop would satisfy the M-5 promotion gate.

**M-6 CANDIDATE (pericope-block substrate as chain-coherence explanandum) unaffected** — this is a surah-pair-scale claim, not a within-surah chain claim, so it's not in the same family as H-NEW-2 / H-NEW-20.

**§1 candidacy.** If integrator elects to route this to §1 under MASTER:munāsaba, I would support that subject to the framing edit above. The differential (ring REFUTED, seam CONFIRMED) is §1-worthy scientific content by itself — the first genuine adjudication of a single classical scholar's multiple sub-claims.
