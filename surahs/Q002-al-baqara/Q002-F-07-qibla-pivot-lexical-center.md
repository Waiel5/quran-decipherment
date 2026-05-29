---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-07
date_last_updated: 2026-05-29
phase: B+
verdict: H1 VINDICATED (qibla-pericope ring replicates, p=0.010, control NULL); H2 NULL (lexical center is NOT at the qibla block)
prereg_sha: be6f15fdf1842fb079c7fa96b9ebf9273390ec00fedb6cc812e9a9d443d8e661
---

# Q002-F-07 — The qibla-change pericope as al-Baqara's lexical center

## Target claim

Farrin 2010 (*Sūrat al-Baqara: A Structural Analysis*) + al-Biqāʿī (*Naẓm al-Durar*,
Q 2 munāsabāt): the qibla-change pivot at Q 2:143 ("*wa-kadhālika jaʿalnākum ummatan
wasaṭan*" — "We have made you a middle nation") is the geometric AND theological
centre of al-Baqara's macro-ring. The project's corpus-wide chiastic audit
(`findings/phase-c-structures/chiastic-audit.md`, §4.2 + §5.1) found that the
**single strongest ring in the whole Quran** is the root-Jaccard window **Q 2:131-144**
(the Abraham/qibla pericope), z = +9.69 over a 57,996-window Bonferroni family.

Q002-F-04 found NO whole-surah verse-token ring around v143 (NULL, resolution-limited).
This test does what F-04 did not: (H1) independently REPLICATES the localized 131-144
ring with the project seed and a 200× tighter null, and (H2) tests whether the qibla
block is the literal LEXICAL center of al-Baqara.

## Pre-registration

`Q002-F-07-qibla-pivot-lexical-center-prereg.md`
(SHA256 `be6f15fdf1842fb079c7fa96b9ebf9273390ec00fedb6cc812e9a9d443d8e661`).
Direction LOCKED: H1 — canonical 131-144 ring score > 95th pct of 10,000 within-window
shuffles. H2 — word-mass & root-mass cumulative midpoints land in verses 142-152.
Seed 20260509, n_perms 10,000, Bonferroni k = 2.

## Empirical result — H1 (ring replication): VINDICATED

From `csv/Q002-F-07.json`:

| Statistic | Q 2:131-144 (target) | Q 2:100-113 (MW-6 control) |
|:--|:--|:--|
| Root-Jaccard ring score (canonical) | **0.2551** | 0.0823 |
| Within-window-shuffle null mean | 0.1003 | — |
| Null SD | 0.0420 | — |
| **z** | **+3.69** | — |
| **p (one-sided)** | **0.0100** | 0.285 |
| Verdict (α = 0.025) | **VINDICATED** | NULL (as expected) |

The canonical order of the Abraham/qibla pericope is more ring-shaped than ~99% of
within-window verse-order shuffles, while the arbitrary 14-verse control window
(Q 2:100-113) returns NULL (p = 0.285). The metric is sound (NULL where no ring is
expected) and the qibla-pericope ring is real.

### Note on the z-discrepancy with the chiastic-audit's +9.69

My z (+3.69) is LOWER than the chiastic-audit's +9.69 because the **null is different,
not the signal**: the audit shuffled the *entire 286-verse surah* (50 trials), giving a
tight null SD around al-Baqara's low cross-verse background; my pre-registered null
shuffles only the *14 verses inside the window* (10,000 trials), giving a wider null SD
(0.042) because the window's own roots are highly self-similar. Both nulls agree on the
DIRECTION and SIGNIFICANCE (canonical ≫ shuffles, p ≈ 0.01). The ring score itself
(0.255) reproduces the audit's reported 0.255 to three decimals — an **exact
independent replication of the observed statistic**, with a more conservative null.

## Empirical result — H2 (lexical center): NULL

| Midpoint definition | Verse where cumulative mass first ≥ 50% | Pre-committed block 142-152 | Verdict |
|:--|:--|:--|:--|
| Word-mass (6,140 words total) | **v172** | NO | NULL |
| Root-token-mass (3,884 tokens total) | **v175** | NO | NULL |
| Naive verse-count midpoint (286/2) | v144 | (borderline) | — |

The LEXICAL center of al-Baqara — by both word-mass and root-mass — sits at **v172-175**
(deep inside the communal-legal block E), NOT at the qibla block (142-152). The qibla
pivot v143 is the center only by the **naive verse-count** reckoning (286 verses →
v144), which weights every verse equally regardless of length. Because al-Baqara's
*second half* is dominated by the very long legal verses (the debt-verse 2:282 alone is
129 words), the mass-weighted center is pulled ~30 verses past the verse-count center.

## Verdict — split (pre-commit honoured)

- **H1 VINDICATED**: the qibla/Abraham pericope is a genuine, replicable root-level ring
  (the strongest in the corpus per the chiastic-audit) — Farrin's CENTRAL-PERICOPE claim
  has a real lexical correlate at the localized window level.
- **H2 NULL**: the "v143 is the literal middle of al-Baqara" reckoning is a
  **verse-count artefact**, not a lexical-mass fact. By word- or root-mass the surah's
  center is v172-175. Published with full prominence.

## Interpretation

This cleanly separates two senses of "center" that the classical/Farrin claim conflates:

1. **Ring-pivot center** (real, lexical): the qibla pericope IS a tight chiastic unit
   and IS the structural hinge between the Banū-Isrāʾīl/Abrahamic first half and the
   communal-legal second half. VINDICATED.
2. **Mass center** (folk-numerological): "v143 is the middle verse" is true only by
   counting verses as equal units. Once you weight by length — the way a reader
   actually experiences the text's bulk — the center moves to the legal core. NULL.

Farrin's THEMATIC + STRUCTURAL pivot claim survives (H1). The popular "literal middle
verse" claim is a counting artefact (H2). Both verdicts are pre-committed and honest.

## Tokenisation note (load-bearing)

The "6,140 total words" here is the sajda/waqf-stripped count (the no-tashkeel JSON
stores standalone pause glyphs — ۖ ۗ ۚ ۛ ۙ ۘ and the rubʿ-mark ۞ — as separate
whitespace tokens; `_norm` removes them, identical to Q002-F-05's pipeline). The
JOURNAL's "6,630 words" counts those glyphs as tokens. The H2 verdict is **robust to
this choice**: the word-mass midpoint is **v172** stripped vs **v174** raw — both deep
in legal block E, both NULL against the pre-committed 142-152 block. The conclusion does
not depend on the tokenisation.

## Honest limits

- The 131-144 window is taken verbatim from the chiastic-audit / Farrin; small boundary
  shifts (e.g. 133-142, which the audit reports at z = +4.24) change the score but not
  the direction.
- "Lexical mass" is one of several center definitions; a syllable-mass or phoneme-mass
  center could differ. Word- and root-mass agree here (v172 vs v175), which is
  reassuring.
- This does NOT test Farrin's full nine-section macro-ring (Q002-F-04 already returned
  NULL on that at the verse-token level; resolution-limited).

## Cross-references

- [[Q002-F-04-ring-structure|Q002-F-04]] — whole-surah verse-token ring NULL.
- `findings/phase-c-structures/chiastic-audit.md` §4.2, §5.1 — Q 2:131-144 z=+9.69,
  strongest corpus ring (the finding this test replicates).
- Farrin 2010 PDF: `data/literature/farrin-cuypers/2010-farrin-surat-al-baqara-structural-analysis.pdf`.
- MASTER-FINDINGS-LEDGER Tier-B items #6, #7 (chiastic rings).

## Status

H1 VINDICATED (independent replication, control NULL); H2 NULL (verse-count artefact).
Pre-commit honoured on both legs.
