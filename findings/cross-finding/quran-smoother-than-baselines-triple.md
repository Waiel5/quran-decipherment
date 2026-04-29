---
id: CROSS-FINDING-005
title: Quranic Smoothness Triple — three orthogonal probes consistently showing Quran LESS structured than matched-Arabic baselines
date: 2026-04-15
status: cross-finding EXPLORATORY; flagged for pre-registered confirmation (H-NEW-META-4)
components:
  - H-NEW-34.1 (verse-final abjad residue under-dispersion vs Bukhārī/Jāḥiẓ/Muʿallaqāt)
  - H-NEW-42 (reverse-direction structural fragility: Quran LESS fragile than all 3 baselines)
  - H-NEW-43 (verse-length AR(1) fit: Quran Ljung-Box Q ≈ 60 vs Bukhārī 1150, Jāḥiẓ 694, Muʿallaqāt 937 — Quran is 15–20× closer to white noise)
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
bonferroni_family_parent: 2026-04-15-Fresh-Wave-3
---

# Quranic Smoothness Triple (cross-finding)

## Observation

Three Fresh-Wave-3 probes on distinct axes all converge on the same directional signal: **the Quran is SMOOTHER than matched-Arabic baselines (Bukhārī prose, Jāḥiẓ prose, Muʿallaqāt rhymed poetry) across three orthogonal measurements.**

| Probe | Axis | Quran statistic | Baseline statistic | Direction |
|---|---|---|---|---|
| [[h-new-34-1-under-dispersion|H-NEW-34.1]] | Verse-final abjad residue variance | under-dispersed (z = −4.28 to −11.36) | baseline dispersed | Quran LESS dispersed |
| [[h-new-42-reverse-direction-fragility|H-NEW-42]] | Forward-vs-reverse 6-axis fragility | Δ̄ = 2.78e-4 | Bukh 3.50e-4 / Jāḥ 3.28e-4 / Muʿ 3.39e-4 | Quran LESS fragile |
| [[h-new-43-verse-length-fft|H-NEW-43]] | Verse-length AR(1) Ljung-Box Q(10) | Q ≈ 60 (p=1.35e-9) | Bukh Q=1150 / Jāḥ Q=694 / Muʿ Q=937 | Quran closer to AR(1)-white noise (15–20× closer) |

Each probe is independently pre-registered. Each gives a NULL verdict in the primary test (direction of original hypothesis failed). But the FAILURE-DIRECTION is the same across all three — Quran smoother, not more structured.

## What the observation does NOT claim

- It is NOT a primary PASS; each probe fell short of its pre-registered threshold. Per PRE-REG-STANDARD-01, sign-flips cannot be upgraded without independent pre-registration.
- It is NOT conditional evidence for any specific mechanism (register, rhyme, positional constraint). A unifying mechanism is hypothesized below; it is SPECULATIVE until H-NEW-META-4 tests it.
- It is NOT evidence that the Quran is "less structured" overall. Other probes (H-NEW-20 al-Rāzī adjacent z = +30.76; H-NEW-13 spectrum λ₂ = 0.265; [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter ordering suppression; root and semantic axes across dozens of tests) show Quran MORE structured than baselines. The smoothness-direction is SPECIFIC to three probes on three axes that share a common property below.

## What the three probes share (the mechanism hypothesis)

Each of [[h-new-34-1-under-dispersion|H-NEW-34.1]], [[h-new-42-reverse-direction-fragility|H-NEW-42]], [[h-new-43-verse-length-fft|H-NEW-43]] measures a structural property that, in classical Arabic, is dominantly driven by **rhetorical and phonetic-rhythmic regularity rather than by semantic/theological content:**

- [[h-new-34-1-under-dispersion|H-NEW-34.1]] verse-final abjad → driven by word-class at verse-end (rhyme/fāṣila)
- [[h-new-42-reverse-direction-fragility|H-NEW-42]] reversal fragility → surface adjacency properties (verse-to-verse transitions)
- [[h-new-43-verse-length-fft|H-NEW-43]] AR(1) on verse-length → short-horizon autocorrelation in rhythm

The hypothesis: **the Quran's register is distinctively less constrained on these surface-rhythmic axes than matched prose or poetry.** Prose has narrative-flow autocorrelation (topic persists across sentences) which raises Q. Rhymed poetry has strict meter/bayt-structure which also raises Q. The Quran, according to the classical naẓm doctrine (al-Bāqillānī *Iʿjāz al-Qurʾān* — being "neither prose nor poetry"), may occupy a regime between them — with the distinctiveness reading on SEMANTIC/THEOLOGICAL axes (which the smoothness does NOT cover) rather than on rhythmic-surface axes.

This is a TESTABLE hypothesis. If true:
1. The Quran's semantic/theological-axis structure scores should be dramatically HIGHER than prose AND poetry (already confirmed: H-NEW-20, H-NEW-13, divine-name density, root-palindrome scores, etc.).
2. The Quran's rhythmic-surface structure scores should be statistically INDISTINGUISHABLE from OR SMOOTHER THAN matched-Arabic baselines (the triple).
3. A "axis-signature" correlation: across many probes, Quranic deviation from baseline should be a BIMODAL distribution — extreme-positive on semantic axes and extreme-neutral-or-negative on rhythmic-surface axes. A unimodal distribution would falsify the distinctive-register reading.

## Classical anchor

**Al-Bāqillānī** (*Iʿjāz al-Qurʾān*, ~1000 CE) — THE foundational argument for Quranic inimitability claims the Quran's uniqueness is precisely that **it does not conform to Arabic prose (nathr) rhythm or Arabic poetry (shiʿr) meter**, but occupies a distinctive register that resists classification. The smoothness triple is a modern quantitative anchor for this 1,000-year-old doctrine. MW-6 tag: SECONDARY-TRIANGULATED (al-Bāqillānī is widely cited in modern scholarship on Quranic literary theory — Kermani, Mir, Neuwirth, Abdul-Raof all build on this framing).

**Al-Khaṭṭābī** (*Bayān Iʿjāz al-Qurʾān*) — argues the Quran's linguistic register is distinctive because it resists the four traditional Arabic prosodic modes. Complementary to al-Bāqillānī.

**Modern academic convergence:** Navid Kermani (*Gott ist schön*, 1999), Angelika Neuwirth (*Der Koran als Text der Spätantike*, 2010), Abdul-Raof (*Qur'an Translation*, 2001) — all independently argue the Quran occupies a distinctive literary-compositional register between Arabic prose and poetry.

## H-NEW-META-4 RESULT (2026-04-16): RETRACTED as cross-finding

**The bimodality test FAILED.** META-4 results: Semantic probes 89% Q-HIGH (✓ ≥70%), but Rhythmic probes ALSO 83% Q-HIGH (✗ predicted ≤50%), χ² p = 0.59 (✗ predicted < 0.05). 2 of 3 criteria fail.

**This cross-finding is RETRACTED as a META-pattern.** The three smoothness observations ([[h-new-34-1-under-dispersion|H-NEW-34.1]], [[h-new-42-reverse-direction-fragility|H-NEW-42]], [[h-new-43-verse-length-fft|H-NEW-43]]) are LOCAL exceptions to a broader Quran-HIGH-on-rhythm pattern (10 of 12 RHYTHMIC-SURFACE probes show Quran > baseline). The 3-probe coincidence does NOT generalize to the project's 19 RHYTHMIC-SURFACE probes.

**What survives after retraction:**
- The 3 component findings stand individually as point observations
- The mechanism hypothesis (al-Bāqillānī "neither prose nor poetry") is NOT supported by the inventory-wide data
- Future H-NEW-META-4.1 (refined sub-classification) is queued but not active

The cross-finding's status is now LOCAL-SIGNAL, not META-pattern. Cross-references in other findings should remove the bimodality framing.

## Integrity

- Filed within ~1 hour of the third component probe ([[h-new-43-verse-length-fft|H-NEW-43]] amendment re-run) completing.
- NO SELECTION of which probes to include — [[h-new-34-1-under-dispersion|H-NEW-34.1]], [[h-new-42-reverse-direction-fragility|H-NEW-42]], [[h-new-43-verse-length-fft|H-NEW-43]] are all Fresh-Wave-3, all three completed 2026-04-15, all three turned out in the same direction. Had any gone the other way, this cross-finding would not have been filed (and would have been reported with equal prominence as a NON-cross-finding).
- This file is explicitly EXPLORATORY, not promoted to §1 or §3 of the MASTER-FINDINGS-LEDGER.
- All three parent findings have been published with honest verdicts (NULL / NULL-BROKEN / NULL-BROKEN). This cross-finding does not change those verdicts.

## Next steps

1. File H-NEW-META-4 pre-registration for the rhythmic/semantic bimodality test (new pre-reg, independent of Fresh-Wave-3).
2. Route to classical-scholar for extended classical-anchor cross-reference (al-Rummānī *al-Nukat*, al-Jurjānī *Dalāʾil*).
3. Route to meta-analyst for effect-size inventory across the ~60 prior probes to enumerate the RHYTHMIC-SURFACE vs SEMANTIC-STRUCTURAL classification.
4. If H-NEW-META-4 passes, this cross-finding is promoted to a MASTER-LEDGER §3 meta-pattern. If not, it remains an EXPLORATORY cross-finding footnote to the three parent NULL findings.
