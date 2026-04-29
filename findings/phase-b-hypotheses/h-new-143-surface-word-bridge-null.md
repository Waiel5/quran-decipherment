# [[h-new-143-surface-word-bridge-null|H-NEW-143]] — Surface-word rhetorical-bridge NULL across mushaf boundaries

**Finding ID**: [[h-new-143-surface-word-bridge-null|h-new-143]]
**Date**: 2026-04-17
**Specialist**: specialist-a
**Parent**: [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] (post-hoc rhetorical-bridge observations)
**Type**: directly-inferential test (published NULL with equal prominence to PASS)
**Verdict**: **NULL** (surface-word shared-tokens do not discriminate top-15 FR jumps)

## Headline

**Surface-word token-identity overlap between surah boundaries does NOT discriminate mushaf's 15 largest Fisher-Rao jumps from the other 98 boundaries on any feature space or any of 4 bridge metrics.** All 12 Mann-Whitney tests return p > 0.6; effect signs are mildly NEGATIVE (top-15 boundaries have slightly FEWER shared tokens — consistent with "large FR jump = discontinuity at surface").

**Interpretation**: classical al-Biqāʿī munāsabāt theory operates at ROOT / SEMANTIC / THEMATIC level, not at surface-word level. [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]'s post-hoc rhetorical-bridge observations (tasbīḥ echo at Q 56→57; message-about-message at Q 14→15; omniscience-Quran-oath at Q 49→50) are real thematic bridges — BUT they do not manifest as shared surface tokens. The proper inferential test is at root / semantic level.

**[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] status update**: its rhetorical-bridge claim is downgraded from "surface-level evidence" to "thematic-level reading under classical munāsabāt framework". EXPLORATORY-POST-HOC ceiling unchanged. [[h-new-143-1-root-bridge|H-NEW-143.1]] root-level test queued.

## Method

For each of 113 consecutive mushaf boundaries (surah i → surah i+1):
1. Extract whitespace-split tokens from the LAST verse of surah i (set A).
2. Extract whitespace-split tokens from the FIRST verse of surah i+1 (set B).
3. Compute bridge strength under 4 metrics:
   - `overlap_count` = |A ∩ B|
   - `cos` = |A ∩ B| / √(|A| · |B|)
   - `jaccard` = |A ∩ B| / |A ∪ B|
   - `dice` = 2|A ∩ B| / (|A| + |B|)

For each of 3 Fisher-Rao feature spaces (root, char-4-gram, verse-length), identify the top-15 jump set. Mann-Whitney U test: do top-15 boundaries have HIGHER bridge strength than the other 98?

One-sided positive direction would confirm [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]. Two-sided test reported for symmetry.

## Results

### Zero-overlap frequency

- Under 1-verse window: **92 of 113 boundaries** have ZERO shared tokens.
- Under 2-verse window (last 2 of surah i, first 2 of surah i+1): **66 of 113** still zero.

(Task description reported 99 zero under unspecified metric; my reproduction gets 92. Small numerical discrepancy; qualitative NULL pattern robust across metric choice.)

### 12 Mann-Whitney tests

| feature | metric | mean top-15 | mean other | z | p_two_sided |
|---|---|---:|---:|---:|---:|
| root | cos | 0.0295 | 0.0266 | −0.135 | 0.892 |
| root | jaccard | 0.0151 | 0.0137 | −0.135 | 0.892 |
| root | dice | 0.0281 | 0.0251 | −0.135 | 0.892 |
| root | overlap_count | 0.40 | 0.45 | −0.085 | 0.933 |
| char_4gram | cos | 0.0202 | 0.0280 | −0.334 | 0.738 |
| char_4gram | jaccard | 0.0102 | 0.0145 | −0.351 | 0.725 |
| char_4gram | dice | 0.0189 | 0.0265 | −0.351 | 0.725 |
| char_4gram | overlap_count | 0.27 | 0.47 | −0.393 | 0.694 |
| vlen | cos | 0.0176 | 0.0284 | −0.385 | 0.700 |
| vlen | jaccard | 0.0087 | 0.0147 | −0.402 | 0.688 |
| vlen | dice | 0.0163 | 0.0269 | −0.402 | 0.688 |
| vlen | overlap_count | 0.13 | 0.49 | −0.487 | 0.627 |

**ALL 12 TESTS NULL.** Effect signs are MILDLY NEGATIVE across the board: top-15 FR-jumps have slightly fewer shared tokens, not more. Consistent with "large FR distance = surface-level discontinuity".

### Top-10 strongest surface-word bridges across entire corpus

| pair | cos | shared tokens |
|:---:|---:|:---|
| Q 17→18 | 0.331 | الحمد, الذي, لله, له, ولم |
| Q 3→4 | 0.228 | أيها, الله, واتقوا, يا |
| Q 5→6 | 0.224 | السماوات, لله, والأرض |
| Q 106→107 | 0.204 | الذي |
| Q 48→49 | 0.177 | آمنوا, الذين, الله, ۖ, ۚ |
| Q 4→5 | 0.173 | إن, الله, لكم, ما, ۗ, ۚ |
| Q 57→58 | 0.159 | الله, والله, ۚ |
| Q 12→13 | 0.152 | ولكن, يؤمنون, ۗ |
| Q 49→50 | 0.151 | ۚ |
| Q 34→35 | 0.150 | في, ما, ۚ |

**None of these top-10 surface-word bridges are in any FR top-15.**

Q 17→18 is the strongest surface bridge (الحمد لله الذي — both open/end with "praise to Allah who"). This is a classical al-Biqāʿī transition, but NOT a Fisher-Rao top-15 jump. Q 17→18 is rank 47 on root FR consecutive-pair distance (middling).

Q 49→50 appears in my surface top-10 but the "shared token" is only the waqf-mark ۚ — not substantive. Surface-word analysis picks up PUNCTUATION noise that Fisher-Rao abstracts away.

## Interpretation

### What the NULL means

[[h-new-143-surface-word-bridge-null|H-NEW-143]] does NOT refute [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]'s rhetorical-bridge claim. It refutes a specific operationalization of that claim (surface-word shared-tokens). Classical munāsabāt theory (al-Biqāʿī, al-Suyūṭī, al-Ghazālī) has always operated at the level of:
- Thematic / topical continuity (e.g., divine omniscience → Quran as vehicle)
- Conceptual echo (tasbīḥ imperative → tasbīḥ execution)
- Root-level morphological echo (سبح root at Q 56:96 and Q 57:1)
- Syntactic parallels (pronoun-shifts, aspect-shifts)

Surface-word identity is a NOISY approximation of these deeper bridges. The NULL is expected if we take classical munāsabāt literature seriously.

### Why top-15 is slightly NEGATIVE

Large Fisher-Rao distance between two distributions implies they differ AT THE FEATURE LEVEL (roots, char-4-grams, verse-length). Since whitespace-token identity is closely related to all three feature spaces, high-FR-distance pairs naturally also tend to have low surface-word overlap. This is MECHANICAL, not informative about munāsabāt.

The small negative effect (−0.1 to −0.5 z) would become strongly negative if surface-word-overlap were a DIFFERENT operationalization of FR-distance — but it's not strong enough to be significant. The 12 p-values are all in the "noise" range (0.6-0.93), consistent with near-orthogonality between surface-token overlap and FR top-15 membership.

### What this means for [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]

[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] had identified 3 specific hinge bridges by close-reading the Quranic text. Those readings were at SEMANTIC / THEMATIC / CROSS-ROOT level, not surface-token level. The NULL here doesn't invalidate those readings — it clarifies the LEVEL at which they operate.

[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]'s verdict is UPDATED:
- From: "rhetorical bridges confirmed at all 3 universal hinges"
- To: "thematic/semantic bridges observable under close-reading classical munāsabāt framework at all 3 universal hinges; surface-word-level test is NULL ([[h-new-143-surface-word-bridge-null|H-NEW-143]])"

The EXPLORATORY-POST-HOC ceiling remains. [[h-new-143-1-root-bridge|H-NEW-143.1]] (root-level replication) is the promotion path.

### Instrument consideration (for auditor)

This test was specified as a FALSIFICATION of [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]'s rhetorical-bridge claim. It returned NULL because the instrument (surface-word token identity) was poorly-matched to what was being claimed (classical munāsabāt, which is thematic/root-level). This is a methodological issue, not a claim-refutation.

Queue [[h-new-143-1-root-bridge|H-NEW-143.1]]: redo with QAC-STEM roots instead of surface tokens. Use same method (last-verse-of-i ∩ first-verse-of-i+1 at root-set intersection), same Mann-Whitney U structure. This is the proper root-level test. Pre-reg filed below.

## Honest limits

1. **This test is the WRONG instrument for [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]'s claim**. I'm filing it NULL transparently, not as a refutation.
2. **Minor numerical discrepancy with task-description's reported numbers** (99 vs my 92 zero-overlap; different mean values). Metric choice differs; qualitative NULL robust.
3. **Token-split uses whitespace only** (no morphological analysis). Arabic morphology means "kitāb" and "kitābuka" are different surface tokens but share a root. The root-level test ([[h-new-143-1-root-bridge|H-NEW-143.1]]) addresses this.
4. **Close-reading of 3 hinges is POST-HOC**. [[h-new-143-surface-word-bridge-null|H-NEW-143]] cannot falsify close-reading observations; only a pre-registered root-level analysis can.

## Connections

- **[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] parent**: its rhetorical-bridge claim is refined (thematic not surface).
- **[[h-new-143-1-root-bridge|H-NEW-143.1]]** (next, pre-reg below): root-level replication.
- **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]**: 4th classical-scholarship validation (al-Biqāʿī) — DOWNGRADED to "awaiting [[h-new-143-1-root-bridge|H-NEW-143.1]] confirmation at root level".
- **H-NEW-17→18 bridge observation**: al-Isrāʾ→al-Kahf share الحمد لله الذي opening — this is a KNOWN al-Biqāʿī exemplar of surface-word bridge, and it's the #1 surface-bridge in our data. But it's NOT a FR top-15 jump, so it's a different category.

## Verdict

**NULL** (12/12 tests, all p > 0.6).

**Interpretation**: instrument-method-level NULL, NOT refutation of classical munāsabāt theory. Queue [[h-new-143-1-root-bridge|H-NEW-143.1]] root-level replication with proper inferential pre-reg.

## Files

- Script: `scripts/h_new_143_surface_word_bridge.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-143.json`
- This findings file.
- [[h-new-143-1-root-bridge|H-NEW-143.1]] pre-reg: `findings/phase-b-hypotheses/h-new-143-1-prereg.md` (next)
