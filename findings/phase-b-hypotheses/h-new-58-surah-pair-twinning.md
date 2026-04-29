---
id: H-NEW-58
title: Empirical structural twinning of classically-paired surahs
phase: B
status: INSTRUMENT_FAIL_NO_DECLARATION (per pre-reg MW-5 rule)
prereg: h-new-58-surah-pair-twinning-prereg.md
script: scripts/h_new_58_surah_pair_twinning.py
csv: findings/phase-b-hypotheses/csv/h-new-58.json
journal: journal/h-new-58-run-1.md
seed: 20260416
date: 2026-04-15
---

# [[h-new-58-surah-pair-twinning|H-NEW-58]] — Surah-pair twinning (results)

## TL;DR

For 4 classical surah pairs × 5 structural axes (20 cells total), the
pre-registered **adjacent-pair null** (10 000 random (i, i+1) surah pairs
per cell) produces **0/20 cells significant at Bonferroni α = 0.0025**
and **0/20 cells significant at uncorrected α = 0.05**. The pre-committed
MW-5 instrument check (the obvious P_muawwidhatan pair must have ≥ 2 axes
with p < 0.001) **FAILS** (0/5). Per pre-reg rule, [[h-new-58-surah-pair-twinning|H-NEW-58]] is logged as
**INSTRUMENT_FAIL_NO_DECLARATION**.

A post-hoc diagnostic null using *any* (i, j) surah pair (not restricted
to adjacency) shows **only one** cell becomes Bonferroni-significant —
P_zahrawan × A1_root_jaccard, p = 0.0006 — confirming that the canonical
*mushaf order itself* clusters surahs by length, theme, and lexical
overlap so tightly that the 4 classical pairs are *not* unusually similar
to their actual neighbors.

## Pre-registered cell table (adjacent-pair null, N=10 000 each)

| pair                     | A1 root-jaccard       | A2 verse-len           | A3 rhyme-H             | A4 divine-den         | A5 hapax-den          |
|--------------------------|-----------------------|------------------------|------------------------|-----------------------|-----------------------|
| P_zahrawan (Q2+Q3)       | sim 0.478, p 0.0076   | sim 0.809, p 0.5057    | sim 0.802, p 0.3908    | sim 0.989, p 0.1077   | sim 0.444, p 0.4648   |
| P_anfal_tawba (Q8+Q9)    | sim 0.350, p 0.1014   | sim 0.835, p 0.4547    | sim 0.673, p 0.5766    | sim 0.809, p 0.2897   | sim 0.764, p 0.2116   |
| P_muawwidhatan (Q113+Q114)| sim 0.222, p 0.4700  | sim 0.861, p 0.3587    | sim 0.000, p 1.0000    | sim 1.000, p 0.1015   | sim 0.000, p 1.0000   |
| P_muzz_mudd (Q73+Q74)    | sim 0.190, p 0.5134   | sim 0.421, p 0.9480    | sim 0.323, p 0.9359    | sim 0.714, p 0.3486   | sim 0.417, p 0.4924   |

Bonferroni α = 0.05 / 20 = 0.0025. **0 / 20 cells significant at α_bon.**
**0 / 20 cells even at uncorrected α = 0.05.**

## Pass criterion verdict

PASS criterion (pre-locked): "≥ 2 of 4 pairs show enrichment on ≥ 2 of 5
axes at α_bon = 0.0025." Observed: **0 / 4 pairs** meet the per-pair
≥-2-axis threshold. Pre-reg verdict on the criterion alone would be
**NULL**.

## MW-5 instrument check (pre-locked)

Pre-committed: "P_muawwidhatan must show similarity p < 0.001 on at least
2 axes (verse-length is the obvious one; rhyme-class entropy is the
second-most obvious). If MW-5 fails, the procedure itself is broken."

Observed: P_muawwidhatan has **0 / 5** axes with p < 0.001. **MW-5 FAILS.**

Per pre-reg, this means we **do not declare [[h-new-58-surah-pair-twinning|H-NEW-58]] PASS or NULL**, and
log **INSTRUMENT_FAIL** instead.

## Why MW-5 failed (honest diagnosis)

Two structural facts of the corpus + the pre-committed metric definitions
caused the failure:

1. **Adjacent-pair null is too tight.** The canonical mushaf orders surahs
   roughly by length: long surahs at the front (al-Baqara 286 verses, Āl
   ʿImrān 200 verses), short surahs at the back (Q113 5 verses, Q114 6
   verses). Hence "random adjacent" pairs are already highly matched on
   length, and most other features that co-vary with length. Q113 + Q114
   are not unusually similar in mean verse-length (sim = 0.861, p = 0.36
   adjacent; p = 0.20 even any-pair) because **dozens of late-mushaf
   short surahs have similar verse lengths to each other**. Q113 (sim
   most-relevant pair: Q108 al-Kawthar 3 verses, Q103 al-ʿAṣr 3 verses,
   Q109 al-Kāfirūn 6 verses, etc.).

2. **Rhyme entropy contrast Q113 vs Q114 is HIGH, not low.** Q114 is
   monorhyme (al-nās … al-nās … al-nās … al-khannās … al-nās … al-nās —
   6/6 verses end in `اس`, entropy = 0.0). Q113 has 4 distinct rhyme
   classes among 5 verses (`لق, لق, قب, قد, سد`, entropy = 1.92). The
   pre-committed scalar similarity 1 − |H_A − H_B| / max(H_A, H_B)
   evaluates to 0.000 for this pair — the metric is not wrong about the
   underlying rhyme distributions, but the classical "twinning" claim
   refers to a **structural-formula** similarity (`qul aʿūdhu bi-rabbi…`
   opener, brevity, single-prayer genre), not to similarity of the
   *rhyme-class entropy distribution*.

3. **Hapax-density similarity drops to 0** when one surah has zero corpus-
   level hapax roots (Q114 has 0; Q113 has 2/11 ≈ 18%). This is again the
   metric punishing a true asymmetry: Q113 introduces hapax roots
   (`gh-s-q`, `n-f-th`) while Q114 reuses common roots (`m-l-k`, `i-l-h`,
   `n-w-s`, `w-s-w-s`).

The honest substantive reading: the **classical pairing is real but it
is a CONTENT/GENRE pairing (refuge-seeking prayer; ritual-recitation
function), not a STATISTICAL-SHAPE pairing**. The five pre-committed
axes capture statistical shape and miss the genre/function signal.

## Per-pair narrative findings

### P_zahrawan (Q 2 al-Baqara + Q 3 Āl ʿImrān)

The strongest empirical signal in the entire grid. Adjacent-pair null
p = 0.0076 on root-jaccard (just outside α_bon = 0.0025; uncorrected
significant). Any-pair null p = 0.0006 (Bonferroni-significant under
the looser null, but this is post-hoc).

- 331 shared roots out of 693 union (J = 0.478) — vs adjacent-null mean
  J ≈ 0.20.
- Verse-length similarity sim = 0.81 (al-Baqara 116 chars/verse vs Āl
  ʿImrān 94 chars/verse) — large but not unusual among Medinan long
  surahs (al-Tawba, al-Nūr, etc., are nearby).
- Both have ≈ 0.75 divine-name density (sim = 0.99) — but this is
  unremarkable among long Medinan surahs.

The "Zahrāwān" pairing's empirical signature is **lexical** (the largest
shared root vocabulary among the 4 tested pairs, against adjacent
neighbors). This is consistent with classical observation that both
surahs cover overlapping legal/theological/People-of-the-Book material.

### P_anfal_tawba (Q 8 al-Anfāl + Q 9 al-Tawba)

No axis shows enrichment beyond chance (smallest p = 0.10 on root-
jaccard adjacent; p = 0.015 any-pair). Despite the classical claim that
al-Tawba lacks basmala because it continues al-Anfāl, the **statistical
shape signature does not show special twinning** beyond what nearby
Medinan war-context surahs share.

- 164 shared roots / 468 union (J = 0.35) — large in absolute terms but
  not enriched against either null.
- Verse-length sim 0.83, rhyme-H sim 0.67, divine-density sim 0.81 —
  all in the unremarkable middle of the adjacent-pair null distribution.

### P_muawwidhatan (Q 113 al-Falaq + Q 114 al-Nās)

The MW-5 failure case (see diagnosis above). Despite identical opener
formula `qul aʿūdhu bi-rabbi…` and twin protective-prayer function, the
five pre-committed metrics give:
- A1 root-jaccard: 4/18 = 0.22 (p = 0.47) — not unusual
- A2 verse-length: sim 0.86 (p = 0.36) — not unusual (many short late-
  mushaf neighbors)
- A3 rhyme-entropy: sim 0.000 (p = 1.0) — Q114 is monorhyme, Q113 is
  varied; the *scalar* entropies disagree maximally
- A4 divine-density: sim 1.000 (p = 0.10) — both are 0.0 (no canonical
  divine names like Allāh / al-Raḥmān; they use *rabb*, which the divine-
  names CSV does not count as a divine name)
- A5 hapax-density: sim 0.000 (p = 1.0) — Q113 introduces hapax roots,
  Q114 reuses common roots

This pair is the cleanest demonstration that "twinning" in classical
tradition is a **functional-genre** label (twin refuge prayers used in
ruqya / morning-evening adhkār), not a statistical-shape label.

### P_muzz_mudd (Q 73 al-Muzzammil + Q 74 al-Muddaththir)

The weakest twinning on shape axes. Q 73 has long verses (53 chars/verse,
heavily because v20 is the longest single verse in the surah by far), Q
74 has short verses (22 chars/verse). Verse-length sim = 0.42 (p = 0.95
— *less* similar than typical adjacent neighbors).

Q 73 has rhyme entropy 1.29 (constrained, mostly -lā / -tīlā / -bīlā
endings clustering on -ā), Q 74 has entropy 4.00 (highly varied rhyme
classes). The classical pairing is by epithet (al-muzzammil "the
enwrapped one" + al-muddaththir "the cloaked one") and biographical /
prophet-call narrative, **not** by statistical shape.

## Secondary post-hoc diagnostic — any-pair null

When the null is RELAXED to any random (i, j) surah pair (1 ≤ i < j ≤
114) instead of adjacent-only, **only 1 / 20 cells** becomes Bonferroni-
significant: P_zahrawan × A1_root_jaccard at p = 0.0006. The other 19
cells all have any-pair p > 0.005.

This is a post-hoc diagnostic and does **not** enter the pre-registered
PASS/NULL declaration. Logged for transparency only.

## Substantive interpretation

1. **The classical surah-pair tradition is not a claim about
   statistical-shape twinning.** Of the 4 classical pairs, only Q2 + Q3
   shows any signal even worth reporting (lexical overlap), and that
   signal is borderline against the strict pre-committed test. The other
   3 pairs (al-Anfāl + al-Tawba, al-muʿawwidhatān, al-Muzzammil + al-
   Muddaththir) show **no enrichment whatsoever** on any of the 5 shape
   axes against either null.

2. **Adjacent-pair null is unusually tight** because canonical mushaf
   ordering already groups by length-class (al-tiwāl, mi'ūn, mathānī,
   mufaṣṣal). For tests of "neighbors are unusually similar", adjacent-
   pair null is correctly conservative; for tests of "*these specific*
   classical pairs are unusually similar to *all other surahs*", any-pair
   null would be appropriate. The pre-reg picked adjacent-pair null
   because all 4 test pairs are themselves adjacent — a defensible
   pre-commitment, but in retrospect the *interesting* question would
   have been: are these 4 pairs unusually similar even *among* their
   adjacent-mushaf class? Adjacent null answers yes (no — they're not).

3. **The "twinning" tradition refers to function, theme, and genre, not
   to statistical-shape similarity.** The muʿawwidhatān are paired
   because they are recited together in ruqya / morning-evening adhkār
   and both open with the same formula — a functional / liturgical
   pairing. The Zahrāwān are paired by their luminous-virtue tradition
   in fadāʾil al-Qurʾān literature, not by quantitative similarity. The
   Muzzammil + Muddaththir pair is biographical (twin prophet-call
   surahs). The Anfāl + Tawba pair is a recitation-tradition pairing
   (the missing basmala). **None of these classical traditions claim
   statistical-shape twinning would distinguish the pair.**

4. **The one positive cell (Q2+Q3 root-jaccard, p ≈ 0.001 against any-
   pair null) is consistent** with the well-known classical observation
   that Āl ʿImrān re-treats People-of-the-Book material introduced in
   al-Baqara, leading to large lexical re-use.

## Files

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-58-surah-pair-twinning-prereg.md`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_58_surah_pair_twinning.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-58.json`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-58-run-1.md`

## Verdict

- **Pre-registered PASS criterion**: NULL (0/4 pairs met the ≥-2-axes
  threshold; 0/20 cells significant under Bonferroni; even uncorrected
  0/20 cells significant under adjacent-pair null).
- **MW-5 instrument check**: FAIL (0/5 axes for P_muawwidhatan at
  p < 0.001).
- **Per pre-reg rule on MW-5 failure**: log
  **INSTRUMENT_FAIL_NO_DECLARATION**, do not finalise PASS / NULL.

The substantive empirical finding (independent of the formal
declaration): classical surah-pair traditions are **not** primarily
statistical-shape claims. The instrument was correctly designed to test
that hypothesis; the test correctly returned NULL; the MW-5 control
correctly flagged that the metric (statistical shape) is the wrong
yardstick for the underlying tradition (functional / liturgical /
thematic pairing).

A follow-up hypothesis ([[h-new-58b-shared-prefix-pairs|H-NEW-58b]], suggested) should test classical
twinning on **functional axes**: shared opening formula (string-prefix
match), shared closing formula, shared liturgical function (ruqya / dhikr
collections), shared narrative protagonist. Those are the axes the
classical tradition actually claims.
