---
id: H-NEW-82
title: Yā-Sīn (Q 36) as the "heart of the Quran" — multi-axis quantitative test
phase: B
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running any centrality / median computation involving Q 36)
parent: classical hadith (Tirmidhī #2887): "Everything has a heart, and the heart of the Quran is Yā-Sīn"
bonferroni_family: 2026-04-15-Wave-Yasin-Heart
bonferroni_k: 6   (6 pre-locked "heart axes"; full grid pre-declared)
alpha_bon: 0.00833   (= 0.05 / 6)
seed: 20260417
rules_tuple: (no-tashkeel JSON; QAC morphology v0.4 STEM-tokens for roots/lemmas; basmala-only-in-Q1; mushaf-order canonical positions 1..114; divine-names = `divine-names-by-verse.csv`)
---

# [[h-new-82-yasin-heart|H-NEW-82]] — Yā-Sīn (Q 36) as the "heart of the Quran" (Pre-registration)

## The classical claim

Tirmidhī ḥadīth #2887: "Everything has a heart, and the heart of the
Quran is Yā-Sīn (إن لكل شيء قلباً، وقلب القرآن يس)." A widely-circulated
saying, but the property "heart" has never been quantitatively defined
or tested. The classical commentary tradition (al-Rāzī, al-Qurṭubī, Ibn
Kathīr) glosses "heart" along several incompatible axes:

(a) **Positional / structural midpoint** — Q 36 sits at index 36/114 ≈
0.316 (just past the first third, not at the median 57/58).
(b) **Gateway to eschatology** — Q 36 contains the longest sustained
description of the resurrection scene of any Meccan surah of its size.
(c) **Lexical / theological centroid** — Q 36 distills the dominant
themes of the Quran (tawḥīd, prophet-rejection, resurrection) in compact
form.
(d) **Recitational pre-eminence** — taught for memorisation early, recited
over the dying.

Of these, (a)–(c) are statistically testable on the corpus. We test all
three, with multiple operationalisations, and pre-commit a Bonferroni
correction.

The hadith itself is **disputed in classical ḥadīth criticism** (al-
Albānī rates it ḍaʿīf jiddan / mawḍūʿ via the chain of Hārūn Abū
Muḥammad, an unknown narrator). We are testing the *content* of the
claim, not endorsing the chain.

## Question

Does Q 36 Yā-Sīn occupy a quantitatively-distinguished "heart" position
in the corpus on multiple structural axes, beyond what a randomly-chosen
surah at its mushaf position / length-class would occupy?

## Locked test axes — 6 axes (full grid pre-declared)

For each axis below, we compute a per-surah scalar score, identify which
surah ranks #1 ("most heart-like" on that axis), and test whether Q 36
specifically holds the #1 rank or the top-K rank.

**Axes are locked BEFORE inspecting any per-surah scores or similarity
matrices.** The test statistic for each axis is its observed Q 36 rank
out of 114 (for axes A1–A4) or its observed Q 36 score against a
position/length-matched null (for axes A5–A6).

### Axis A1 — Positional median (mushaf index)

Score(s) = − |position(s) − 57.5| where position(s) is the 1-indexed
mushaf number. The "most central" surah is the one whose index is closest
to 57.5 (= 114/2 + 0.5). Pre-locked test: Q 36's rank on this axis.

### Axis A2 — Verse-count median

Score(s) = − |verse_count(s) − median(verse_counts)|. Median verse count
across 114 surahs. Pre-locked test: Q 36's rank on this axis.

### Axis A3 — Letter-count median

Score(s) = − |letter_count(s) − median(letter_counts)| where letter
counts are no-tashkeel grapheme counts per surah. Pre-locked test: Q 36's
rank on this axis.

### Axis A4 — Centroid by lexical similarity (root-Jaccard, all-pairs)

Build the 114×114 root-Jaccard similarity matrix S where
S[i,j] = |R_i ∩ R_j| / |R_i ∪ R_j| with R_i = set of distinct QAC STEM
roots in surah i. Score(s) = mean_{j≠s} S[s, j] = the surah's mean
similarity to all other surahs. The **centroid surah** is argmax. Pre-
locked test: Q 36's rank on this axis.

### Axis A5 — Network eigenvector centrality (root-Jaccard graph)

On the same 114×114 similarity matrix S (zero diagonal), compute the
eigenvector centrality (principal eigenvector of S, normalized). Score(s)
= eigenvector_centrality(s). Pre-locked test: Q 36's rank on this axis,
AND the empirical p-value of Q 36's centrality against a position-matched
null (10,000 random surah indices, each scored against the same matrix).

### Axis A6 — Theme-centroid by Quranic-keyword profile

Build a per-surah vector over a pre-locked 8-dimensional theme palette,
where each component is the rate (per-100-words) of distinct STEM-roots
in that theme. Themes locked from the existing `findings/phase-b-
hypotheses/` taxonomy; no theme tuned to Q 36's content:

  T1 tawḥīd / divine names         (الله, رب, إله, رحمن, رحيم)
  T2 prophet / messenger           (رسل, نبي, ا ر س ل)
  T3 resurrection / hereafter      (ق ي م, ب ع ث, ج ز ي, ج ن ن, ن و ر, ج ح م)
  T4 belief / disbelief            (ا م ن, ك ف ر, ش ر ك, ن ف ق)
  T5 creation / cosmos             (خ ل ق, س م و, ا ر ض, ش م س, ق م ر)
  T6 narrative / past peoples      (ق و م, ق ر ي, ا ه ل, م ل ك)
  T7 commandment / law             (ا م ر, ن ه ي, ح ل ل, ح ر م, ك ت ب)
  T8 reflection / understanding    (ع ق ل, ف ك ر, ع ل م, ذ ك ر, ا ي ة)

Each surah's vector is L2-normalised. The corpus centroid is the L2-
normalised mean of all 114 vectors. Score(s) = cosine(v_s, v_centroid).
Pre-locked test: Q 36's rank on this axis.

(Theme keyword roots locked here BEFORE inspecting Q 36's morphology.
They were chosen to be a plausible "themes of the Quran" palette per
the project's topical files, not selected to favour Q 36.)

## Null distributions (pre-locked)

For axes A1, A2, A3, A4, A6: the test is **rank out of 114 surahs**. Q
36's score is significant at one-sided α iff it ranks in the top
⌊α·114⌋ + 1 surahs (rank ≤ ⌊α·114⌋ + 1; rank 1 = best). The exact rank
gives a discrete one-sided p ≤ rank / 114.

For axis A5 (eigenvector centrality), in addition to the rank, we draw
N=10,000 position-matched bootstrap nulls: for each draw, pick a random
surah index uniformly from {1, …, 114} and report its centrality.
p_one_sided = (1 + |{null ≥ observed Q 36 centrality}|) / (1 + N).

This null is conservative for A5 because the eigenvector centrality of
each surah is fixed by the matrix; the null is just permuting the
"target-surah-index" identity.

Bonferroni: α_bon = 0.05 / 6 = 0.00833.

## PASS criterion (declared before any computation)

[[h-new-82-yasin-heart|H-NEW-82]] declared **PASS** iff Q 36 attains rank ≤ ⌊α_bon · 114⌋ + 1 = 1
(i.e. Q 36 is **the #1 surah on at least 3 of the 6 axes**, OR Q 36
appears in the top-5 on at least 5 of the 6 axes).

Otherwise:
- **PARTIAL** if Q 36 is top-5 on 3-4 of the 6 axes.
- **NULL** if Q 36 is outside top-5 on > 3 axes.

The full per-axis rank table is published regardless.

## Method-witness — MW-5 negative control

Two pre-locked control surahs, each known **NOT** to be a candidate
"heart" by classical tradition:

  C1 = Q 1 (al-Fātiḥa) — opens corpus; classical "key" / "mother of the
       book" but not "heart".
  C2 = Q 114 (al-Nās) — closes corpus; refuge prayer.

MW-5 condition: **At least one of {C1, C2} must rank in the BOTTOM half
on at least 4 of the 6 axes** (rank > 57). The instrument must not
spuriously promote the corpus endpoints to "heart" status.

If MW-5 fails, log INSTRUMENT_FAIL_NO_DECLARATION (per project policy)
and report ranks honestly without declaring PASS / NULL on [[h-new-82-yasin-heart|H-NEW-82]].

We additionally report Q 1 and Q 114 ranks on every axis as a sanity
table.

## Garden-of-forking-paths disclosure (locked before run)

Choices made BEFORE any per-surah score is computed:

1. **6 axes, not more or fewer.** Considered and explicitly excluded:
   gematria-total centroid (already studied in `gematria-landscape`,
   would inflate family), unique-root density (already [[h-new-54-extended-root-enrichment|H-NEW-54]]), char-
   per-verse rhythm (axis A6 indirectly captures), iltifāt rate (no
   surah-level scalar yet), peak-verse density (would require external
   scoring). The 6 chosen are computable from existing primary tools
   (loader + QAC + divine-names CSV).
2. **Mushaf order, not chronological.** Classical claim is about the
   mushaf "heart"; chronology variant could be added as a secondary
   diagnostic but does NOT enter the PASS/NULL declaration.
3. **Bonferroni k = 6** (full axis grid). Loosening to k = 3 would
   require ratification per the bonferroni_tightening_vs_loosening rule.
4. **Theme palette T1–T8 locked** before checking Q 36's STEM-root
   distribution; chosen from the project's topical taxonomy.
5. **MW-5 = Q1 + Q114** chosen as canonical "non-heart" surahs because
   both are widely treated as having distinguished but distinct
   functions (key, refuge) and neither is a candidate for "heart" in
   any classical source we know of.
6. **Eigenvector centrality** chosen for the network axis because it is
   the standard centrality measure for weighted graphs and mathematically
   well-defined on the symmetric Jaccard matrix.
7. **Root-Jaccard** for the lexical similarity matrix because it is the
   identical operational definition used in [[h-new-58-surah-pair-twinning|H-NEW-58]] (consistency).

We commit to publishing **all 6 per-axis ranks for Q 36** (and the
parallel ranks for Q 1, Q 36, Q 57 the literal-median surah, Q 58 the
literal-median+1 surah, and Q 114) regardless of outcome.

## Secondary diagnostic axes (post-hoc; NOT in PASS/NULL declaration)

Reported for transparency but excluded from the Bonferroni family:

- **D1**: Distance-from-classical-heart-candidates ensemble. Compare Q
  36's centrality to other plausible candidates (Q 1 al-Fātiḥa, Q 2 al-
  Baqara, Q 18 al-Kahf, Q 50 Qāf, Q 55 al-Raḥmān, Q 67 al-Mulk).
- **D2**: Rank stability under chronological order (Nöldeke/Schwally).
- **D3**: Rank stability when divine-names density per axis A6 weight is
  doubled.

## Data + outputs

- Input corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`
- Input morphology: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`
- Input divine-names: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-by-verse.csv`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_82_yasin_heart.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-82.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-82-yasin-heart.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-82-run-1.md`

## Status

PRE-REGISTERED 2026-04-15. Spec locked before running any per-surah
score, similarity matrix, or rank computation involving Q 36.
