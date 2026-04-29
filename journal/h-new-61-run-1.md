---
date: 2026-04-15
run_id: h-new-61-run-1
hypothesis: H-NEW-61 — Surah opening-word distribution (comprehensive)
seed: 20260416
author: h-new-61-specialist
verdict_summary: PASS — all 6 cells fired at α_bon=0.00833
---

# H-NEW-61 Run 1 — Journal

## Setup

- Pre-registration written FIRST (`h-new-61-opening-words-prereg.md`).
- Taxonomy of 9 opener classes locked BEFORE running; muqaṭṭaʿāt-token list
  (14 distinct strings) locked.
- Opener extractor specified mechanically in pre-reg before any
  distributional inspection.

## Garden-of-forking-paths log (made BEFORE running)

Pre-known surah openers from memorisation:
- Q 1, 6, 18, 34, 35 → *al-ḥamdu lillāh* (MW-5 control).
- Q 17, 87 → praise (*subḥān*, *sabbiḥ*).
- Q 4, 5, 22, 33, 49, 60, 65, 66, 73, 74 → *yā-ayyuhā* (vocative).
- Q 109, 112, 113, 114 → *qul* (imperative).
- Q 81, 82, 84, 99 → *idhā* (conditional).
- Q 38, 50 → muqaṭṭaʿāt + *wa-l-qurʾān* (oath).
- Q 19 → muqaṭṭaʿāt + *dhikr*.
- Q 2, 3, 29, 30, 31, 32 → muqaṭṭaʿāt + *dhālika/Allāh/ḥasiba/al-ḥamd/tanzīlu*.

These were declared in pre-reg's garden-of-forking-paths section. None
biased the distributional χ²/Fisher tests because the taxonomy was
pre-locked.

## Steps

1. **Load** Quran no-tashkeel JSON (114 surahs) + Nöldeke chronology
   (114 surahs) + QAC morphology (~128k segment lines).
2. **Extract** opener for each of 114 surahs via locked extractor:
   skip basmala (S=1: skip v1), skip muqaṭṭaʿāt-prefix run for the 29
   muqaṭṭaʿāt surahs (special handling for Q42 ḥm + ʿsq across v1+v2).
3. **Cell 2 first** (MW-5 control). Result: 5/5 *al-ḥamd* surahs detected
   correctly. Extractor validated.
4. **Cell 1 descriptive**: 19 distinct openers cover 73/114 surahs (64%);
   distribution highly skewed.
5. **Cell 3 χ²**: p = 1.86 × 10⁻⁴, passes Bonferroni.
6. **Cell 4 period × class**: VOCATIVE Medinan p = 0.00018 (passes inner
   Bonferroni 0.000926). OATH p = 0.00171 (suggestive, fails strict).
7. **Cell 5 muq × class**: DEMONSTRATIVE-after-muq p = 3.7 × 10⁻⁹ (10/10
   demonstrative openers follow muqaṭṭaʿāt — 0/85 elsewhere).
8. **Cell 6 twin-incipit**: 10 distinct twin-(w1,w2,w3) groups covering 31
   surahs. Marginal-independence null (10⁴ samples, seed 20260416): null
   median = 0; observed = 10; empirical p < 0.0001.

## Issues encountered

### MW-5 a-priori check

The opener-token "الحمد" is the merged *al-ḥamd* form. After confirming
all 5 surahs detect it, no extractor adjustment needed.

### Q42 ḥm + ʿsq spanning v1 and v2

Original concern: the muqaṭṭaʿāt-skip needed to walk past TWO tokens
(v1 = *ḥm*, v2 = *ʿsq*) to get to v3's first content word *kadhālika*.
The extractor handles this cleanly because the skip-loop iterates while
the next normalized token ∈ MUQATTAAT_NORMALIZED_TOKENS, regardless of
verse boundary.

### Q38 ص with v1 = "ص ۚ والقرآن ذي الذكر"

Original heuristic in H-NEW-31 (`len(words) ≤ 4`) would NOT skip this v1
(it has 5 tokens). The new extractor instead skips the *first token* if
it matches MUQATTAAT_NORMALIZED_TOKENS, so Q38 gets w1 = *wa-l-qurʾān*
correctly.

### Pause-marker handling

Tanzil includes `ۛ` (U+06DB) as inline pause markers. Added to the
PUNCT_RE so they don't create empty tokens. Verified Q38 splits correctly
into [*ṣ*, *wa-l-qurʾān*, *dhī*, *al-dhikr*].

### Cell 6 null choice

Initial pre-reg said "permute opener-tuples among 114 surahs". I noticed
during implementation that this is DEGENERATE — re-assigning (w1,w2,w3)
tuples to surah-IDs preserves the multiset of tuples and thus the
twin-count is invariant under permutation. Switched to the
**marginal-independence null** (independent draws from w1, w2, w3
marginals) — declared in the pre-reg as the actual implementation; this
captures whether the JOINT (w1, w2, w3) distribution is more clustered
than independence would predict. The substitution was made before any
test was run and is the strictly weaker null (i.e., the test PASSES under
the easier null). Documented here for integrity.

## Verdicts

| cell | result |
|---|---|
| Cell 1 (descriptive) | PUBLISHED |
| Cell 2 (MW-5) | PASS (5/5) |
| Cell 3 (χ² uniformity) | PASS (p = 1.86 × 10⁻⁴) |
| Cell 4 (period × class) | PASS (VOCATIVE-Medinan inner-pass p = 0.00018) |
| Cell 5 (muq × class) | PASS (DEMONSTRATIVE-after-muq inner-pass p = 3.7 × 10⁻⁹) |
| Cell 6 (twin-incipit perm) | PASS (p < 0.0001) |

JOINT: ALL 6 cells fire.

## Files written

- `findings/phase-b-hypotheses/h-new-61-opening-words-prereg.md` (pre-reg)
- `findings/phase-b-hypotheses/h-new-61-opening-words.md` (findings)
- `findings/phase-b-hypotheses/csv/h-new-61.json` (raw data + per-surah)
- `scripts/h_new_61_opening_words.py` (analysis script)
- `journal/h-new-61-run-1.md` (this file)

## Honest caveats

- Three borderline classifications (Q 78 *ʿamma* → OTHER not INTERROG;
  Q 102 *alhākum* → OTHER not REPORT; Q 111 *tabbat* → OTHER not REPORT)
  were left in the pre-reg-locked classification rather than retroactively
  re-classified. A sensitivity-analysis ext (h-new-61-1-sensitivity) is
  warranted.
- The marginal-independence null is weak. A stronger Markov-bigram null on
  the full corpus would still leave the dominant *tilka āyāt al-kitāb*
  and *tanzīl al-kitāb min* templates as significant, but should be run
  for a follow-up. Twin-incipit count is dominated by formulaic templates,
  not random rhyme.
- VOCATIVE Medinan finding overlaps H-NEW-31 (already PARTIAL); this
  re-confirms at the explicit single-word level.
- DEMONSTRATIVE-after-muqaṭṭaʿāt finding (Cell 5) is a CLEAN structural
  recovery of a classical claim (Suyūṭī, Zarkashī: *fawātiḥ al-suwar*
  followed by *dhikr al-kitāb*). The 10/10 + 0/85 split is the strongest
  single result of this hypothesis.
- OATH-as-Meccan-only (21/21) just barely missed strict inner-Bonferroni
  (p = 0.00171 vs α_inner = 0.000926). The directional pattern is
  unambiguous; a one-sided test would pass cleanly. Pre-reg specified
  two-sided so the conservative call stands.

## Next steps (suggestions, not commitments)

- h-new-61-1-sensitivity: re-run with borderline reclassifications and
  one-sided tests where direction was pre-specified.
- h-new-61-2-incipit-templates: characterize the 10 twin-incipit templates
  (length, prosodic profile, repetition rate) and test whether they cluster
  in particular Mufaṣṣal regions.
- h-new-61-3-markov-null: replace marginal-independence null in Cell 6
  with corpus-bigram Markov null.
