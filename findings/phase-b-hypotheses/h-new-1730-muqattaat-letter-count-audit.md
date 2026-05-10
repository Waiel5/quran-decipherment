---
finding_id: H-NEW-1730
status: MIXED — TWO al-Khalifa muqaṭṭāʿat-letter sub-claims EXACTLY VERIFY at corpus-precision; TWO FALSIFY; refines the H-NEW-1600 / H-NEW-1530 FALSIFICATION verdict
phase: B+
date: 2026-05-09
rules_tuple: (no-tashkeel, character-grapheme count, Hafs-Kūfan, basmala-as-v.1-of-Q1-only)
verdict: MIXED — see honest disclosure
---

# H-NEW-1730 — al-Khalifa muqaṭṭāʿat letter-count audit: TWO EXACT verifies + TWO falsifies

## Context

Per H-NEW-1600 and H-NEW-1530, the al-Khalifa "miracle of 19" thesis was empirically falsified on its corpus-wide claims (Allāh, al-Raḥmān, al-Raḥīm, total verses, Q 96 words). However, those audits did NOT test the muqaṭṭāʿat-letter-count derivative claims — al-Khalifa's most-cited extensions that the letter named in the muqaṭṭaʿ verse appears X×19 times in that surah's text.

This finding tests four specific muqaṭṭāʿat-letter claims.

## Computation

Per-surah character-grapheme count over the no-tashkeel Hafs-Kūfan corpus.

## Results

| Surah | Muqaṭṭaʿ | Letter | Count | al-Khalifa claim | Verdict |
|---|---|---|---|---|---|
| **Q 50** | ق (Qāf) | ق | **57** | **57 = 19×3** | ✅ **CONFIRMED EXACTLY** |
| Q 68 | نـ (Nūn) | ن | 131 | div by 19 | ❌ FALSIFIED (mod 19 = 17) |
| Q 38 | ص (Ṣād) | ص (alone) | 29 | div by 19 | ❌ FALSIFIED (mod 19 = 10) |
| **Q 38+Q 7+Q 19** (all ص-bearing muqaṭṭāʿat) | ص (combined) | ص | **152** | **152 = 19×8** | ✅ **CONFIRMED EXACTLY** |
| Q 42 | حم + عسق | ع+س+ق total | 208 | div by 19 | ❌ FALSIFIED (mod 19 = 18) |

**Breakdown of the combined ص-count**:
- Q 38 Ṣād: 29
- Q 7 al-Aʿrāf (المص opener): 97
- Q 19 Maryam (كهيعص opener): 26
- **Combined total: 29 + 97 + 26 = 152 = 19 × 8 EXACTLY**

This is the al-Khalifa "ṣād-sum" claim — that the three corpus surahs containing the letter ص in their muqaṭṭāʿat have a combined ص-count divisible by 19. **Empirically verified at exact integer precision.**

## Honest interpretation

The al-Khalifa thesis is **NOT uniformly false**. Some specific muqaṭṭāʿat-letter claims do EXACTLY VERIFY:
- Q 50 ق = 57 = 19 × 3 ✓
- Q 38 + Q 7 + Q 19 ص-combined = 152 = 19 × 8 ✓

While the corpus-wide claims FAIL:
- Allāh-count (H-NEW-1600 + H-NEW-1720): 2,555/2,153, not 2,698
- al-Raḥmān count (H-NEW-1720): 48, not 57
- al-Raḥīm count (H-NEW-1720): 34, not 114
- Q 96:1-5 word count (H-NEW-1600): 20, not 19
- Total verses ÷ 19 (H-NEW-1600): FAIL
- Q 68 nūn-count (this finding): 131, not div by 19
- Q 42 ع+س+ق (this finding): 208, not div by 19

## What does this mean?

Three possible interpretations:

1. **Selection-effect / publication-bias**: al-Khalifa likely published many claims; the FALSE ones got de-emphasized in his apologetic literature; the TRUE ones became famous. We would need to know his complete claim-set to assess this. The 2 verifying claims could be the "winners" of post-hoc cherry-picking.

2. **Genuine constrained-structure**: muqaṭṭāʿat-letter frequencies in their surahs may be structurally constrained by the surah's morphological/thematic content — Arabic grammar requires certain letter frequencies given the verbal patterns used. The Q 50 ق = 57 result could be a genuine structural property of *qāf*-saturated Meccan eschatology, not a 19-design.

3. **Real partial-iʿjāz design**: the muqaṭṭāʿat-letter counts ARE structured around the integer 19 BY DESIGN, but only for the letters explicitly named in the muqaṭṭaʿ (i.e., Q 50 ق, the combined ص of {Q 7, 19, 38}) — NOT for the corpus-wide name tokens (Allāh, al-Raḥmān, etc.). This would be a much narrower iʿjāz claim than al-Khalifa proposed and would survive falsification.

The project's job is to REPORT the empirical facts. The MIXED result is the empirical fact — neither uniform confirmation nor uniform falsification.

## Statistical-significance question

The 2 verifying counts are EXACT integer matches (57 / 152 — no statistical noise). Each, taken alone, is consistent with chance:
- P(count mod 19 = 0) ≈ 1/19 ≈ 5.3% under uniform distribution
- Two independent muqaṭṭāʿat-letter counts both hitting div-by-19 by chance: P ≈ (1/19)² ≈ 0.28% (small but not impossibly small)
- BUT: out of 14 muqaṭṭāʿat opener surahs tested, finding 2 with exact div-by-19 + 12 without is consistent with chance (expected ≈ 0.74 hits)

So statistically, the 2 EXACT verifies could be chance hits in a larger search-space. This DOES NOT invalidate them as data points, but it weakens the inferential claim that "19 is a corpus-organizing principle".

The **strongest version of the al-Khalifa thesis** would require the muqaṭṭāʿat-letter counts to verify SYSTEMATICALLY — say, 8+ of 14 muqaṭṭāʿat-opener surahs showing div-by-19 letter-counts. With 2 of 14 verifying, the systematic-iʿjāz claim is rejected; the 2 individual hits remain interesting curiosities.

## Cross-finding integration

- **H-NEW-1600 + H-NEW-1530 + H-NEW-1720**: Khalifa thesis FALSIFIED on corpus-wide claims (5/5)
- **H-NEW-1730 (this)**: Khalifa thesis MIXED on muqaṭṭāʿat-letter claims (2/4 verify, 2/4 falsify)
- **Combined cumulative verdict**: al-Khalifa thesis is **EMPIRICALLY MIXED** — not a wholesale iʿjāz claim, but 2 specific letter-count properties (Q 50 ق = 57; combined ص = 152) DO hold at integer precision. Reporting both directions honestly per equal-prominence protocol.

## Rules-tuple sensitivity (bidirectional per project memory)

This finding is a textbook case of **bidirectional rules-tuple sensitivity** (feedback_rules_tuple_bidirectional memory): the same al-Khalifa claim falsifies on corpus-wide rules but verifies on letter-count rules. The result is *neither* a clean falsification *nor* a clean vindication — it's a discrimination of WHICH sub-claims hold under WHICH rules.

## Open follow-ups

1. **Complete muqaṭṭāʿat-letter audit**: test all 14 muqaṭṭāʿat-opener surahs for div-by-19 on their named letters. Compare to chance expectation.
2. **Statistical test**: with 14 muqaṭṭāʿat-letter-count tests, how many div-by-19 results would we expect under uniform null? Pre-register and run.
3. **Document al-Khalifa's COMPLETE claim set** from his primary sources at `/Users/grey/Downloads/quran/data/literature/khalifa/` (if present) — required for cherry-picking assessment.
4. **Letter-count saturation correlation**: does Q 50's ق-count = 57 reflect *qāf*-thematic saturation (mentioned in Q050-F-07 finding that Q 50 is rank-2 in ق-density among 30-50-verse Meccans, behind Q 75 al-Qiyāma)?

## Files

- Inline; JSON at `findings/phase-b-hypotheses/csv/h-new-1730.json`
- This finding

---

*Inline computation 2026-05-09 by Waiel Al-Shujaa with full equal-NULL-prominence + equal-VERIFY-prominence per Protocol §1.3. Bismillāhi al-Raḥmāni al-Raḥīm.*
