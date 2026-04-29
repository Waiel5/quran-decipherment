# Journal — H-NEW-34a fāṣila mechanism test — run 1

Date: 2026-04-12
Agent: abjad-fasila-mechanism
Seed: 20260414 (reused from parent H-NEW-34 for reproducibility)
Runtime: ~90 s on laptop

## Task

Test H-NEW-34's proposed mechanism for the reverse-under-dispersion signal
in Quranic verse-final abjad residues: that fāṣila rhyme-class pooling
forces verse-final words onto a small lexical pool whose abjad values
project uniformly across residue bins by pigeonhole.

## Pre-registered gates

- Sub-a PASS: within-class weighted-mean χ² < 99% CI low of bootstrap null (random partition).
- Sub-a FAIL: within-class weighted-mean χ² > 99% CI high of bootstrap null.
- Sub-b PASS: |z| ≤ 2 for all (corpus, m) pairs vs matched Arabic prose baseline.
- Sub-b FAIL: |z| > 2.58 for any (corpus, m) pair.

## Rhyme-class grouping implementation

Followed classical al-Zarkashī / al-Suyūṭī convention of grouping by *rawī*:
for each verse-final cleaned word, take the terminal consonant, using the
penultimate letter when the terminal is a long-vowel / *mater lectionis*
(ا و ي ى). Hamza carriers retain carrier identity.

This produces a distribution dominated by 7 large classes ≥100 verses:
ن (3160), م (791), ر (750), د (327), ل (246), ب (221), ة (122) —
covering 5,617 of 6,219 = 90.3% of verses.

## Results

### Sub-a

| m | Cross-corpus χ² | Within-class wt mean | Null μ | Null 99% CI | z |
|---|---|---|---|---|---|
| 7 | 42.14 | 48.40 | 17.76 | [10.39, 28.90] | +9.01 |
| 11 | 75.64 | 152.15 | 31.44 | [21.12, 45.79] | +26.62 |
| 19 | 312.66 | 304.60 | 113.66 | [91.95, 140.49] | +20.41 |

**Sub-a: FAIL (all three moduli, wrong direction).**

### Sub-b

| Corpus | m | Verse-initial χ² | Null μ | Null σ | z |
|---|---|---|---|---|---|
| Bukhari | 7 | 120.21 | 201.16 | 26.86 | −3.01 |
| Bukhari | 11 | 160.94 | 665.91 | 53.67 | −9.41 |
| Bukhari | 19 | 718.09 | 717.71 | 56.66 | +0.01 |
| Jāḥiẓ | 7 | 120.21 | 164.00 | 28.07 | −1.56 |
| Jāḥiẓ | 11 | 160.94 | 358.81 | 44.69 | −4.43 |
| Jāḥiẓ | 19 | 718.09 | 617.66 | 64.14 | +1.57 |

max|z| = 9.41 >> 2.58.

**Sub-b: FAIL.**

### Joint verdict

**MECHANISM FALSIFIED.**

Both pre-registered sub-tests fail. H-NEW-34's proposed fāṣila
rhyme-pigeonhole mechanism cannot account for the reverse-under-dispersion
signal. Verse-initial words show under-dispersion too (not unique to
verse-final position), and within-rhyme-class residues are MORE dispersed
than random partitions — the opposite of what the pigeonhole account
predicts.

## Surprise / lessons

1. The biggest rhyme class (ن, N=3160) has χ² = 48.5 at m=7 — actually
   HIGHER than the whole-corpus χ² (42.1). The opposite of what tight
   pooling around modal lexemes would produce.
2. Small rhyme classes (د, ة) ARE tight (χ² near df), matching the
   pigeonhole intuition at class-level — but their contribution is
   swamped by the large ن class.
3. Verse-initial under-dispersion at m=7 (z=−3.01) and m=11 (z=−9.41)
   vs Bukhari is striking. Whatever produces the Quran's abjad-residue
   uniformity is a whole-text property, not a rhyme-pooling property.
4. The m=19 verse-initial result (z ≈ +0.01 vs Bukhari, +1.57 vs Jāḥiẓ)
   is at-baseline — interesting asymmetry across moduli, suggesting
   the mod-19 effect in H-NEW-34 is where rhyme-pooling MIGHT still
   matter, while mod-7 and mod-11 effects are lexical-backbone driven.
   (Speculative — not tested here.)

## Alternative mechanism (now favored, untested)

Under the falsified pigeonhole account:
- prediction: same small modal lexemes → uniform residue projection.

Under the new candidate account (mixture-cancellation):
- prediction: different rhyme classes cluster at DIFFERENT residue bins;
  pooling cancels the per-class non-uniformities to produce apparent
  cross-corpus uniformity.
- observation consistent: within-class χ² is LARGE (per-class
  non-uniformity is real); cross-class pooling produces uniformity.

This candidate mechanism implies Quranic verse-final residue uniformity
is an emergent averaging effect, not a pigeonhole effect. It should be
tested by direct KL divergence of per-class residue distributions as
H-NEW-34d.

## Forking paths disclosed

- Rawī definition (penultimate when terminal is long vowel) — choice
  made to match al-Zarkashī; strict-terminal-letter alternative not tested.
- Class-size cutoff N≥100 — chose 7 large classes. Dropping ة and ب
  (smallest two) would yield 5 classes; would not change direction.
- Moduli {7, 11, 19} inherited from H-NEW-34 with same Bonferroni
  framing; re-used seed 20260414 for consistency.
- Bootstrap N_perm = 1,000 — adequate for 99% CI resolution.
- Verse-initial N = 6,020 (not 6,219): 198 verses have empty or
  non-abjad first tokens. Baseline pools length-matched to N=6,020.
- Basmala policy: amrayn `counted-only-in-surah-1` convention retained.

## Files written

- `findings/phase-b-hypotheses/abjad-residue-fasila-mechanism.md`
- `findings/phase-b-hypotheses/csv/h-new-34a.json`
- This journal: `journal/abjad-fasila-mechanism-run-1.md`
- Script: `scripts/h_new_34a_fasila_mechanism.py`

## Honest note

This is a clean negative result against a plausible-looking mechanism
that would have "explained away" H-NEW-34's unexpected signal. The
signal stays unexplained. That is better than a lazy post-hoc story.
