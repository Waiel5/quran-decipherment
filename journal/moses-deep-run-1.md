# Moses Deep-Dive — Run 1 Journal

**Agent:** moses-deep-reader
**Date:** 2026-04-12
**Output:** `findings/phase-c-structures/moses-deep-dive.md`

## Goal

Comprehensive computational analysis of Moses (مُوسَى, Mūsā) across the Quran:
- Locate every Moses mention in QAC morphology
- Investigate the Mūsā/ittabaʿa = 136 each word-pair coincidence (test thematic
  reality vs accident)
- Build a comparative-vocabulary matrix across the top-5 Moses pericopes
- Compute Moses signature roots (which roots are most uniquely Moses-coded?)
- Pharaoh distribution; Moses-Khidr structure; staff miracle cross-comparison
- Ta-Ha vs Qasas structural comparison
- Chronological trace: Moses-as-revealed across Meccan→Medinan
- Prior-art search on Reynolds/Neuwirth/Firestone

## Method

1. Scan `quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4) for `LEM:muwsaY``
   with `POS:PN` to lock the 136 token / 131 verse list. Cross-check with
   word-pair-symmetry.md anchor.
2. Scan for `LEM:{t~abaEa` (the canonical "to follow" verb) — also 136 tokens.
   Compute spatial overlap with Moses verses (same verse, ±5, ±10, same surah).
3. Build per-surah Moses spans (min..max Moses verse, padded ±2). Compute root
   sets for the top-5 surahs by token count. Pairwise Jaccard.
4. Moses signature root extraction: for every root with ≥5 occurrences in the
   Quran, compute the fraction of occurrences within the union of all Moses
   spans. Rank.
5. Ring scores (paired-Jaccard chiasmus metric) for ~22 candidate Moses
   pericopes, vs 500-trial within-window verse-shuffle null. Same null model
   used by `chiastic-detector` agent for consistency with §3 of chiastic-audit.md.
6. Five staff-miracle passages (7:107-108, 20:17-22, 26:32-33, 27:10-12,
   28:31-32) — root-set Jaccard matrix; common-to-all and unique-to-each.
7. Surah 20 vs Surah 28 whole-surah ring score and jinas density.
8. Chronological trace by Egyptian-edition revelation order, joined to Moses
   spans, computing tokens-per-verse density per Moses pericope.
9. WebSearch: Reynolds (Biblical Subtext), Neuwirth (Ta-Ha narrative),
   Firestone (Khidr).

## Key intermediate files

- `scratch/moses/moses_deep.py` — main analysis
- `scratch/moses/moses_structures.py` — ring scores per pericope
- `scratch/moses/moses_summary.json` — raw output
- `scratch/moses/run1.log`, `run2.log` — full console captures

## Verified anchors

- **Moses (lemma muwsaY`, PN): 136 tokens, 131 distinct verses, 34 surahs.** ✓
  Matches word-pair-symmetry.md anchor exactly.
- **ittabaʿa (lemma {t~abaEa): 136 tokens, 123 distinct verses.** ✓ Matches
  word-pair-symmetry.md anchor.
- Top Moses surahs (token count): 7 (21), 28 (18), 20 (17), 2 (13), 10 (8),
  26 (8), 40 (5), the rest single-digit.
- Pharaoh (firoEawon, PN): 74 tokens, 67 distinct verses, 27 surahs.

## Headline findings (this run)

1. **The Moses=ittabaʿa=136 pair is thematically a coincidence at the verse
   level.** Only 2/136 ittabaʿa tokens land in a Moses verse (7:142, 18:66).
   At ±5 verses: 27/136 (20%). At ±10: 39/136 (29%). Even using "any surah
   that has Moses" generously gives 98/136 (72%) — but that's 25 of 114 surahs,
   so 72% includes most of the long Medinan surahs that talk about
   "following" in many other contexts. **The semantic match
   ("Moses → followers") is real qualitatively but the count match isn't
   driven by Moses contexts.** 18:66 is the ONE verse where Moses literally
   says "may I follow you" — to Khidr, not by his followers.

2. **`ESw` (ʿaṣā, "staff") is 100% Moses-coded.** All 12 occurrences are in
   verses about Moses's staff. No other Quranic figure has a staff. Sister
   roots: `sHr` (sorcery/magic) is 39/63 = 62% in Moses sections (the
   magicians-of-Pharaoh contests dominate); `sbT` (tribes / Israelite tribes)
   is 5/5 = 100%; `Twr` (mount Sinai) is 7/11 = 64%; `bqr` (cow / Baqarah's
   cow narrative) is 7/9 = 78%.

3. **The brief staff miracle 7:107 = 26:32 is word-for-word identical** — the
   exact same 6 words: *fa-alqā ʿaṣāhu fa-idhā hiya thuʿbānun mubīn* ("So he
   threw his staff, and behold, it was a manifest serpent"). The fuller
   versions in 20, 27, 28 share only the core lqy/ʿaṣā/yad/byḍ tetrad and
   then diverge dramatically.

4. **The Moses-Khidr pericope (18:60-82) has a real, statistically meaningful
   ring score: z = +2.28** under the chiastic-audit.md null model. The
   structure has obvious literary form (three episodes — boat, boy, wall —
   bookended by the fish/junction opening and the interpretation closing),
   and the metric agrees.

5. **Surah 28 (Al-Qaṣaṣ) has a mild whole-narrative ring (z = +1.71 for vv
   3-46)** while Surah 20 (Ṭā-Hā) does not (z = -1.57 for the equivalent vv
   9-98). Ta-Ha is more episodic; Qasas is more cyclic. Both have very high
   jinas density (Ta-Ha 0.733, Qasas 0.717 over the full Moses span).

6. **The Jaccard matrix across top-5 Moses surahs shows S26 (Shuʿarā) as the
   outlier**: lowest mean Jaccard to others (0.245). S26's Moses material is
   compressed into a refrain-driven recitation embedded in a 7-prophet sequence
   — vocabulary is constrained by formula. Most-similar pair: **S2 ↔ S7
   (J=0.365)**, the two longest Moses-rich corridors.

7. **Chronological trace shows clear ramp.** Earliest Meccan Moses mentions
   are 1-verse "scriptures of Moses" allusions (87:19, 53:36, 79:15, 51:38)
   averaging 2-3 root-tokens per verse. Mid-late Meccan period gets the long
   biographies (S20, S26, S28, S7) at 4-10 tokens/verse. Medinan S2 expands
   to 13.7 tokens/verse but pivots away from biography toward
   covenant-and-Israelite-disobedience material.

## Honest caveats

- The "Moses signature root" analysis is reference-bias-aware: I did not
  cherry-pick the 0.5 threshold; I report the full ranked list down to that
  cut-off (~33 roots). The top entries (`ESw`, `sbT`, `jwz`, `$Tr`) are
  unambiguously Moses-coded by content.
- Ring scores for sub-surah windows are uncorrected for multiple comparisons.
  The Khidr +2.28 z is consistent with chiastic-audit.md's listing of that
  pericope as a known literary unit but is not itself Bonferroni-surviving
  in this scan; it should be cross-checked against the chiastic-audit's
  full sub-surah scan.
- Jinas density is biased upward in long-verse-rich pericopes; reported
  numbers are raw, not normalised for verse length.

## What I did NOT do

- No full chronological concatenation as a single text block (the chrono-
  revelation finding's general thesis is already established; I only show
  it at the per-surah Moses-section level).
- No tafsir cross-reference (deferred to `tafsir-xref` agent).
- No fresh null model on the 136/136 word pair (already covered by
  word-pair-symmetry.md §5: matching-count buckets are at-or-below null
  expectation given Quranic count distribution, so the 136 pair is not
  "miraculous" in the McKay sense; the question of whether the pair is
  *thematically* meaningful is answered above as "weakly").

## Cross-references

- `findings/phase-b-hypotheses/word-pair-symmetry.md` — anchor for the 136/136
  finding
- `findings/phase-c-structures/chiastic-audit.md` — null-model standard
- `findings/phase-b-hypotheses/jinas-wordplay.md` — methodology for jinas
- `findings/phase-b-hypotheses/chronological-revelation.md` — verse-length
  ramp framework
