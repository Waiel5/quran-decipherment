---
audit_id: audit-004
finding_id: H-NEW-4
finding_title: Muqaṭṭaʿāt surahs — first-lemma-introduction rate signature
audited_by: skeptical-auditor
date: 2026-04-12
parent: null
status: PASSED (as a refutation)
---

# Audit memo — H-NEW-4 (muqaṭṭaʿāt lexical-header hypothesis)

## Verdict: PASSED (as a refutation)

Clean null result. Pre-registered k=6 checkpoint family, length-stratified permutation null (appropriate for the claim), no retrofitting, direction actually reverses at later checkpoints — which is strong evidence against the claim rather than "failed to find". Reporting discipline is textbook.

## Critique items (minor, non-blocking)

1. **Sample size decay at long checkpoints.** At cp=2000, n_muq = 3, n_non_muq = 4, and the z reads NaN. Fine — author correctly excluded this cell. But the k=6 family in Bonferroni should be k=5 (since cp=2000 is uninformative). Mechanical impact is negligible (threshold 0.05/5 = 0.01 vs 0.05/6 = 0.00833, same verdict), but the family counting should be accurate.

2. **Length-stratified permutation is the right null.** Deciles are reasonable. A quantile-matched null might be cleaner but decile-stratification is standard and was pre-registered. No concern.

3. **QAC STEM vs token-orthographic.** Using lemmas is the right semantic unit for "lexical introduction rate" — testing with orthographic tokens instead would conflate inflection with lexical novelty. Justified.

4. **Why not also test root-introduction?** Author flags this as a sibling that was NOT tested — correctly. Roots would be a distinct hypothesis (and probably less null-sensitive since the root count is much smaller). Leaving it out is the right move; listing as sibling is correct disclosure.

## Alternative-explanation audit for a refutation

- **Did we test the right claim?** Yes — the hypothesis is lemma-introduction rate; the test is lemma-TTR at checkpoints. Direct operationalization.
- **Could a signal hide at a checkpoint not tested?** The set {50, 100, 200, 500, 1000, 2000} spans the informative range for 29 muqaṭṭaʿāt surahs with n ≥ 1 at each cp. Finer-grained scanning would be valid but would inflate k proportionally; the current choice is sensible.
- **Could signal hide at a different lexical granularity (root, morphological family)?** Possibly — but that's a *different hypothesis*, properly scoped out.

## Classical cross-reference

al-Suyūṭī, *Itqān* nawʿ 43 (on al-ḥurūf al-muqaṭṭaʿa) catalogs ~20 classical theories for the purpose of the isolated letters. **None** of them predicts accelerated lexical introduction. The classical tradition variously reads muqaṭṭaʿāt as (a) divine oath-letters, (b) abbreviations of divine names, (c) challenges to the Arabs to compose like (*iʿjāz* framing), (d) letters whose sum equals a specific numerical value, or (e) an unfathomable divine mystery (*al-Shāfiʿī's position*). **None** predicts downstream-surah lexical effects. So the refutation here aligns with tradition: the muqaṭṭaʿāt are formal/phonetic openers, and the hypothesis under test was a modern conjecture, not a classical claim. This should be stated in the write-up's interpretation section — currently implicit, would be strengthened by naming al-Suyūṭī nawʿ 43 explicitly.

## Robustness requests

None blocking. Optional:
1. Correct k from 6 to 5 in the Bonferroni family statement.
2. Add explicit citation of al-Suyūṭī *Itqān* nawʿ 43 framing in the interpretation paragraph.

## What would change the verdict

- A rerun using orthographic tokens that reveals a hidden lexical signal → reframe as "lexical-but-only-for-inflectional-richness" effect, not a full reversal.
- A rerun using root-level TTR that shows a significant effect → different hypothesis (H-NEW-4R), not a revision to this one.

Neither is likely given the direction reversal already observed at longer checkpoints.

## Cross-finding overlap flag for integrator

This refutation **reinforces** the existing confirmed finding that muqaṭṭaʿāt distinctiveness lives at the letter/phonetic level (already established in prior project work). The combination is coherent: muqaṭṭaʿāt are phonetically-distinctive openers *without* downstream lexical signature — exactly what al-Suyūṭī's **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; internal contradiction with `classical-quantitative-claims-audit.md:155` CC-050 which cites "nawʿ 41"; classical-scholar best-guess is nawʿ 41 *fī asmāʾ al-ḥurūf*]** would predict. This is a useful triangulation, not a new finding, but worth noting in synthesis § mapping muqaṭṭaʿāt properties.

## Lineage

Parent: null.
Sibling-not-child: the prior "muqaṭṭaʿāt letter-density" findings are topically adjacent but independently established. This refutation constrains the interpretation of those prior findings by ruling out one modern extension of them.
