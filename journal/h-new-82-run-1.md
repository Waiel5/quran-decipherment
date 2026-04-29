# H-NEW-82 — Run 1 journal

Date: 2026-04-15
Specialist: h-new-82-specialist (Opus 4.6 1M)
Pre-reg locked: 2026-04-15 (BEFORE any per-surah scoring against Q 36)

## Inputs

- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (114 surahs, 6236 verses)
- Morphology: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4 STEM tokens)
- Divine names: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/divine-names-by-verse.csv`

## What was done

1. Pre-registered 6 axes operationalising "heart of the Quran" (positional median, verse-count median, letter-count median, lexical-centroid by mean root-Jaccard, eigenvector centrality on root-Jaccard graph, cosine to corpus theme centroid). Bonferroni k=6, α_bon = 0.00833. Locked PASS criterion (Q36 rank=1 on ≥3 axes OR top-5 on ≥5 axes), MW-5 negative-control test (Q1 + Q114 must rank > 57 on ≥4 axes), and theme palette T1-T8 BEFORE inspecting Q 36's STEM-root distribution.
2. Wrote `scripts/h_new_82_yasin_heart.py` implementing the spec verbatim.
3. Built 114×114 root-Jaccard similarity matrix, mean-similarity per surah, eigenvector centrality (power iteration, converged), theme-vector cosine to L2-normalised corpus-mean theme centroid.
4. Computed Q 36 ranks across 6 axes; computed control-surah ranks (Q1, Q114); computed diagnostic ensemble ranks (Q2, Q18, Q50, Q55, Q57, Q58, Q67).
5. Drew n=10,000 position-matched bootstrap null for axis A5 (eigenvector centrality).
6. Wrote findings, JSON, and this journal.

## Top-line numerical results

- Median verse count = 40; median letter count = 1477.
- Q 36 ranks (1=best, lower=more "heart-like"):
  - A1 mushaf-position-median: rank 43 (Q 57 al-Ḥadīd is rank 1; Q 36 is 21.5 surahs from positional median)
  - A2 verse-count-median: rank 88 (Q 36 has 83 verses; median is 40; 43 verses off)
  - A3 letter-count-median: rank 76 (Q 36 has ~3092 letters, median ~1477; >1600 letters off)
  - A4 lexical-centroid: rank 18 (Q 10 Yūnus is the lexical centroid)
  - A5 eigenvector-centrality: rank 27 (Q 10 Yūnus is most central; A5 null p = 0.2383)
  - A6 theme-centroid: rank 16 (Q 46 al-Aḥqāf is the theme centroid)
- Q 36 is rank-1 on **0 axes** and top-5 on **0 axes**.
- MW-5 instrument check: PASS for both Q 1 (6/6 axes in bottom half) and Q 114 (6/6 axes in bottom half). The instrument correctly demotes corpus endpoints.

## Verdict

- Pre-registered PASS criterion (Q 36 rank=1 on ≥3 axes OR top-5 on ≥5 axes): NOT MET on any axis.
- PARTIAL band (top-5 on 3-4 axes): NOT MET.
- Verdict: **NULL** — Q 36 is not the structural heart of the corpus on any of the 6 pre-locked axes.
- MW-5 instrument check: PASS — the instrument is honest (it correctly demotes Q 1 and Q 114 to the bottom half on all 6 axes).

## Honest interpretation

The classical hadith claim "Yā-Sīn is the heart of the Quran" is a content / liturgical / theological claim, not a quantitative claim about position, length, similarity, or theme-centrality. Q 36 ranks closer to the lexical and theme centroid (positions 16-18) than to the positional / size median (positions 43-88), but is never #1 and never even top-5.

Notable surface findings (all post-hoc, NOT in the pre-registered family):
- The **positional-median** surah is Q 57 al-Ḥadīd (literally rank 1: |57 - 57.5| = 0.5; Q 58 al-Mujādilah is rank 2 at 0.5 also). Al-Ḥadīd is famously the surah whose name (الحديد = "iron", abjad = 26) and verse on iron (Q 57:25) generates the celebrated "code-19 / iron / al-Ḥadīd" claim cluster. We do NOT here endorse or test those claims, but note that the positional median surah is *al-Ḥadīd*, not Yā-Sīn.
- The **lexical centroid** (mean similarity to all surahs, AND eigenvector centrality #1) is Q 10 Yūnus, with Q 40 Ghāfir close behind. Both are mid-mushaf Meccan surahs in the "Ḥawāmīm" / 7th–8th decile region. The lexical centroid finding is consistent with a known classical observation that al-Ḥawāmīm (Q 40-46) form a thematically dense cluster.
- The **theme centroid** is Q 46 al-Aḥqāf, a Ḥawāmīm surah, with Q 23 al-Muʾminūn second.
- Q 50 Qāf and Q 55 al-Raḥmān (each itself sometimes nominated as a "heart" candidate in popular literature) rank 4 and 11 on letter-count median — much closer than Q 36.

Substantive reading: classical "heart of the Quran" is a *liturgical* designation, paralleling Christian "lectio divina" choices of pericopes for memorisation and recitation over the dying. The hadith chain itself is rated weak / fabricated by al-Albānī, and the *content* of the claim is not borne out by any of 6 distinct quantitative operationalisations of "heart".

## Run-time

~12 seconds (114×114 Jaccard + 2,000-iteration power iteration + 10,000-draw null on commodity hardware).

## Outputs

- Pre-reg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-82-yasin-heart-prereg.md`
- Script: `/Users/grey/Downloads/quran/scripts/h_new_82_yasin_heart.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-82.json`
- Findings: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-82-yasin-heart.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-82-run-1.md`
