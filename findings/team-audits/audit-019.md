---
audit_id: audit-019
audits: H-NEW-24 letter-multiset surah-boundary detectability (findings/phase-b-hypotheses/letter-multiset-boundary-detection.md)
auditor: skeptical-auditor
date: 2026-04-13
verdict: PARTIAL → NEEDS REVISION (2 blockers, 2 framing edits)
finding_status_after_audit: essential-claim positive direction preserved but NOT yet publishable until B1-B2 resolved
blockers: 2 (B1 length-confound orthogonalization; B2 precision/K-sensitivity)
framing_edits: 2 (F1 sub-b "bad pre-reg" label; F2 mechanism-attribution language)
strengthening_followups: 4
parent_meta_patterns: MASTER:scale-stratified-signature §1 (adds 8th data point, character-level positive); connects to M-6 (pericope substrate) via register/length mediation
classical_alignment: none (novel-lane; no classical anchor, per tester)
---

# Audit-019 — H-NEW-24 letter-multiset surah-boundary detectability

## Verdict

**NEEDS REVISION.** The essential finding — JS-divergence scan detects 41/113 true surah boundaries at z=+4.39 — is real and the shuffle control (sub-c) is the critical safeguard that rules out the most common failure mode. But there are **2 blockers** before this can be elevated past PARTIAL, and **2 framing edits** on how sub-(b) and mechanism are described. The essential positive direction is preserved, not downgraded.

The tester's own PARTIAL verdict is well-calibrated. I am upgrading from PARTIAL → NEEDS REVISION (stricter) because the mechanism-layer disclosure in AMEND-15 Addition 2 implies the finding isn't yet interpretively closed: the scan works, but we don't know *on what signal*. Until that's tested, it's not a standalone finding; it's an input to a longer investigation.

## The tester's ad-hoc question — direct answer

The tester asks: *"Sub-(b) failure is 'bad pre-reg' framing; please flag if this crosses into ad-hoc rationalization."*

**Ruling: partial yes, partial no. Flagged as F1 below.**

- The *direction* of the sub-(b) failure (peaked at moderate w rather than monotonic) is mechanistically explicable from prior knowledge of Quranic surah-length distribution (median interior surah is ~200-2000 letters; w=5000 blurs the short ones). The tester's explanation is correct.
- The *framing* "this sub-test fails because it was the wrong prediction" crosses a line. It retroactively reframes a failed pre-registration as a design defect rather than a test failure. That's the structural move HARKing uses.
- **Honest alternative framing**: "Sub-(b) fails as pre-registered (ρ=-0.20). The observed peak at moderate w is consistent with surah-length distribution (median surah ≤ w=5000), but since we did not pre-register a peaked prediction, we cannot count this as support. It stands as a pre-registration error for H-NEW-24-v2."
- The tester did disclose honestly. The failure IS reported. The issue is the interpretive label. This is framing edit F1, not a blocker.

Contrast with audit-018 (H-NEW-22 anti-signal): there the tester refused to count the anti-signal. Here the tester's "bad pre-reg" label is closer to claiming the prediction-that-would-have-succeeded is the real one. **F1 asks for label precision, not for removal of the discussion.**

## Blockers

### B1 — Length-confound orthogonalization (load-bearing)

The tester's own AMEND-15 Addition 2 concedes that register drift, length drift, and topical coherence may all mediate the signal. Sub-(c) rules out *uniform random* artifacts (letter-permutation destroys all structure). It does NOT rule out length-driven artifacts.

**The problem:** the mushaf is ordered roughly by decreasing length. Surah boundaries coincide with length transitions. JS-divergence between a 10,000-letter window and a 200-letter window is mechanically large if the short-surah sampling rate is lower (fewer characters → higher variance → inflated JS even under identical true distributions). The current sub-c control destroys the ordering entirely, which removes both (i) letter-ordering signal and (ii) length-induced sampling-rate structure. We cannot tell which one is producing the 41 hits.

**Required test (non-optional for upgrade past PARTIAL):**
- **Sub-(e) length-matched surrogate null.** Preserve surah order and surah lengths; within each surah, uniform-permute letters. Re-run JS scan. If hits drop to chance (~24.6), the signal is purely in within-surah letter ordering. If hits stay near 41, the signal is in the per-surah unigram multiset — which is the H-NEW-24 claim. **This is the test that distinguishes "letter-multiset discontinuity is real" from "length discontinuity fakes a multiset signal."**
- **Sub-(f) length-matched negative control.** Generate a synthetic corpus of 114 blocks with lengths matching Quranic surahs, each block drawn i.i.d. from the *global* Quranic letter unigram distribution. Run JS scan. If this also gives ~41 hits, the signal is *pure length/sampling-rate* with no per-surah multiset heterogeneity. If it gives chance (~24.6), per-surah multiset heterogeneity is real and H-NEW-24's essential claim is robust.

Both are cheap (stride-100 JS scans at N=330,709). Together they decompose the signal into (letter-order, per-surah-unigram, length-driven) contributions. **Without (e) or (f), the claim that "letter-multiset discontinuity is detectable" can't be separated from "length-induced sampling noise is detectable," which is trivial.**

### B2 — K=113 precision-recall collapse; tighter K untested

K=113 gives the scanner exactly as many guesses as there are true boundaries. With ε=500 tolerance and stride=100, the valid prediction space per true boundary is ~10 positions. Under random placement the null mean is 24.6 — that's the baseline for "K=113 random guesses at ε=500 tolerance." The scanner's 41 hits is +16 above this.

But **precision is unreported.** We know recall = 41/113 = 36%. We don't know what fraction of the 113 predictions hit a boundary. (It's also 41/113 = 36% since matching is 1-1, so *precision = recall by construction at K=113*.) This is a degenerate regime: the scanner is not being asked to discriminate good predictions from bad ones, only to cover as much as possible.

**Required test:**
- **Sub-(g) K-sensitivity curve.** Run with K ∈ {30, 60, 113, 200, 300}. Plot precision and recall vs K. The *interesting* finding would be: at K=30, the scanner hits >15 true boundaries (high precision, ~50%+ above chance per prediction). If so, the top-30 JS peaks are substantively real boundaries and the signal localizes to a small number of genuinely detectable transitions. If at K=30 the scanner hits ~5 (chance = ~3), then the signal is spread diffusely across many weak peaks and the claim is much weaker.

This is a 5-minute addition and dramatically changes how the finding should be reported. Without it, the z=+4.39 headline is potentially inflated by the choice of K=113 being maximally permissive.

## Framing edits

### F1 — Sub-(b) "bad pre-reg" label → "pre-registration error, H-NEW-24-v2 peaked prediction for future test"

Current language: *"This sub-test fails because it was the wrong prediction."* Change to: *"Sub-(b) fails as pre-registered (ρ=-0.20, p=0.635). Post-hoc, the observed peak at moderate w is consistent with the distribution of surah lengths. A future H-NEW-24-v2 should pre-register a peaked prediction with a specified location; we do not count the post-hoc peak as support here."* This is load-bearing for HARKing hygiene. Not a blocker because the structural disclosure is already present; the label is what needs tightening.

### F2 — Mechanism-attribution language in Addition 2

AMEND-15 Addition 2 is mostly well-disclosed, but the phrasing *"None of these is a miracle"* is editorial. Replace with neutral: *"These mediating mechanisms are not adjudicated by the current test. Orthogonalization (sub-e/f above) is required to attribute the signal to any specific layer."* The audit does not need the tester to editorialize about miracles in either direction; the test result should stand as a methodological observation.

## Technical notes (non-blocking)

### N1 — Jonckheere-Terpstra reduction

The tester correctly flagged: J-T on 4 scalar observations reduces to Spearman-vs-identity, which is a weak test with n=4 (critical values are nearly at the ceiling). This is a **pre-registration error** independent of whether sub-(b)'s direction was wrong. The test as specified had low power to detect any ordering. A better pre-registration would have been either (a) test individual w's for above-chance, pool via Fisher, require all-positive; or (b) fit a parametric peak model w* and test w* vs null. Not blocker-level because the essential claim doesn't rest on sub-(b).

### N2 — MIN_SEP=500 not tuned

MIN_SEP=500 is explicitly an untuned parameter choice. I checked: at stride=100, MIN_SEP=500 means adjacent peaks must be ≥5 stride-steps apart. This is not aggressive. The greedy top-K with MIN_SEP=500 will behave similarly to greedy top-K with MIN_SEP=100 in practice because the JS-score landscape at stride=100 is already smoothed by the window. **Minor**: re-run with MIN_SEP=100 to confirm robustness; I expect ≤2 hit difference.

### N3 — Greedy 1-to-1 matching in `detect()`

The matching in `detect()` is greedy from the truth side: for each true boundary, assign the first prediction within ε that isn't already used. This can underestimate hits when multiple predictions are near one true boundary but better predictions are elsewhere. Hungarian/bipartite matching would be the right test. In practice with K=113 and MIN_SEP=500 the effect is small. **Minor.**

### N4 — AMEND-15 Addition 1 tercile result is not meaningful

The tercile analysis reports hit rates of 37.5% / 55.0% / 41.2%. With 8, 20, 85 true boundaries respectively, the early-tercile hit rate is based on 3/8 = 37.5% which has ±17% standard error. This cannot support any claim of position-uniformity. **Remove or flag as noise.** Tightening this would require bootstrap CIs on the tercile rates.

## Meta-pattern placement

### MASTER:scale-stratified-signature §1 — 8th data point if B1/B2 resolved

Current layers:

| Layer | Finding | Status | Scale |
|---|---|---|---|
| Local pairwise | H-BIQAI-LOCAL seam | POSITIVE z=+10.06 | adjacent pair |
| Verse-composite | H-NEW-20 | POSITIVE-pending-block-null | verse-internal |
| Bigram transition | H-NEW-13 | NULL clean | letter-bigram |
| Intra-surah bracketing | H-SUYUTI-BRACKETING | NULL (not refuted) | within-surah |
| Verse-boundary acrostic | H-NEW-22 | NULL + rhyme-suppression | verse-boundary |
| Corpus register | H-NEW-13 Bukhari | POSITIVE λ_2=0.265 | corpus-register |
| Long-range ring | H-BIQAI ring | REFUTED | whole-surah |
| **Surah-boundary letter multiset** | **H-NEW-24** | **PENDING (pending B1)** | **surah-level letter** |

If B1 resolves positive (length-matched null centers near chance), H-NEW-24 registers as a novel positive at the **surah-level letter-statistics** scale — an orthogonal layer to the 7 existing. If B1 resolves as length-confound (length-matched null also gives ~41), H-NEW-24 collapses into a trivial-by-sampling-rate phenomenon and adds no new layer.

**Critical for §1 registration:** this is precisely the test that determines whether the signal is new or trivial. Without B1, I can't place it in the stratification.

### M-6 (pericope substrate candidate) — indirect connection

Tester's Addition 2 lists "topical coherence: divine-name clustering, prophet-pericope blocks" as one mediating mechanism. If B1 attributes the signal to per-surah letter-unigram heterogeneity, that's close to M-6's "pericope block substrate produces local coherence" hypothesis — but at the *surah* level not *pericope* level. A partial cross-reference for integrator.

## What would change this verdict

- **To PASSED (positive):** B1 sub-(e) length-matched within-surah shuffle gives hits ≈ chance (~24.6) and sub-(f) length-matched i.i.d. control also gives chance. The scanner's 41 hits then localize to per-surah multiset heterogeneity, a real and novel finding.
- **To REFUTED:** B1 sub-(f) length-matched i.i.d. control gives hits ≈ 41. The signal is pure length-induced sampling-rate artifact.
- **To NEEDS REVISION indefinitely:** B2 K-sensitivity curve shows 41 is inflated by K=113 permissiveness — e.g., K=30 gives only 5-6 hits. Then the essential claim is weaker than the headline implies.
- **To stay at PARTIAL:** framing edit F1 applied but B1/B2 not run. Finding sits at "real phenomenon, mechanism unresolved."

## Strengthening follow-ups (beyond blockers)

1. **H-NEW-24-v2 peaked prediction pre-registration**: fit w*, test w* ∈ [1000, 3000] for peak location, single pre-registered hypothesis.
2. **Meccan/Madani split**: detect Meccan-Meccan transitions vs Meccan-Madani transitions separately. If the latter are easier to detect, the signal is register-mediated.
3. **Letter-bigram instead of unigram**: JS on bigram distributions. Should give cleaner signal if per-surah style differences go beyond letter frequency.
4. **Cross-corpus: Tanakh, NT, Mahabharata**: do other religious texts show surah-like multiset boundaries at their canonical book divisions? This tests whether this is a Quran-specific phenomenon or a compiled-text universal.

## Closing

The essential positive (a ∧ c ∧ d) is real at z=+4.39 but the mechanism is ambiguous between "per-surah letter-multiset heterogeneity" (novel and interesting) and "length-induced sampling-rate artifact" (trivial). Sub-(c)'s uniform shuffle is not enough to distinguish these. Sub-(e) length-matched surrogate and sub-(f) length-matched i.i.d. control are the load-bearing tests. **Run B1 + B2 and this upgrades to PASSED. Without them, finding sits at PARTIAL indefinitely.**

Tester's HARKing self-check on sub-(b) was well-disciplined in the structural sense (failure IS reported) but the interpretive label needs tightening (F1). Not at the honest-disclosure level of audit-018; sits between audit-018 (clean) and a full HARKing instance.

---

**Handoff items:**
- B1 length-matched null (sub-e within-surah shuffle + sub-f length-matched i.i.d.) required before upgrade past PARTIAL
- B2 K-sensitivity curve (K ∈ {30, 60, 113, 200, 300}) required for precision claim
- F1 sub-(b) label tightening (pre-reg error, not "bad prediction")
- F2 mechanism-attribution neutralization ("None of these is a miracle" → neutral)
- N1-N4 technical notes non-blocking
- MASTER:scale-stratified-signature §1 registration pending B1 outcome
