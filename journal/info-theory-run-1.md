# Journal — info-theory run 1

**Agent:** Phase B novelty agent (information-theory profile)
**Date:** 2026-04-12
**Primary corpus:** `quran-text/quran-no-tashkeel.json` (intact, locked anchors).
**Lemma source:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Quranic Arabic Corpus 0.4, Kais Dukes).

## Goal

Produce the first end-to-end information-theoretic profile of the Quran:
character-level entropy, conditional/block entropies, per-surah entropy,
Zipf's law on lemmas, Heaps' law, KL divergence between surahs,
compression-complexity proxies, position-letter mutual information, and
within-surah entropy trends. **The Quran is one text** — every "split"
in this work is internal (surah, verse, position), not "edition" vs
"edition."

## Tools / data

- `analysis/tools/loader.py` — `load_quran("no-tashkeel")` → 114 surahs,
  6 236 verses (anchors §8 confirmed by sanity check during the run).
- `analysis/tools/tokenize.py` — `is_letter`, `graphemes`. The letter
  set used here is the standard `LETTER_RANGES` from the methodology
  (U+0621..U+064A ∪ U+0671..U+06D3, no recitation marks, no tashkeel,
  no tatweel).
- Morphology lemma extraction was done in-script: every `STEM` line
  with a `LEM:` field contributes one lemma token. The QAC stores
  74 608 lemma-bearing morphemes across 4 832 distinct lemmas. **Not the
  same as the orthographic word count (77 797 real-words),** because a
  morphological stem can split or fuse surface tokens.
- Compression: `gzip` and `zlib` from stdlib (level 9). Used as a
  Kolmogorov-complexity proxy in the Cilibrasi/Vitanyi sense — useful as
  a relative scale across surahs, *not* as an absolute information rate.

## Sanity checks performed

- Total letter count from `graphemes`: 330 709 — matches the locked
  anchor in `docs/methodology.md` §8 exactly.
- Verse count after load: 6 236 — matches.
- Surah count after load: 114 — matches.

## Decisions / forks logged

1. **No-tashkeel only** for letter analyses. Robustness re-runs against
   full-tashkeel are *not* in this exploratory pass; flagged as a
   robustness item for any specific finding that gets promoted.
2. **36 distinct letter graphemes appear**, not 28. The extras are the
   four hamza variants (أ إ ؤ ئ ء), the alif madda (آ), alif maqsura
   (ى), ta marbuta (ة), and the U+0671 (alif wasla) family. I report
   redundancy against both the textbook 28-letter alphabet
   (`H_max = log2 28 ≈ 4.807`) and the actual 36-symbol observed
   alphabet (`H_max = log2 36 ≈ 5.170`). Only the 28-letter version is
   directly comparable to the standard "Arabic redundancy" literature.
3. **Block-entropy estimation is biased downward at small k** because
   the Quran is finite: the n=5 block-entropy estimate uses only
   ~330 700 windows over 36⁵ ≈ 60 million possible 5-grams, so the
   per-step conditional entropies for n≥4 are noticeably biased low and
   I treat them as suggestive only. n=2 and n=3 estimates are reliable.
4. **KL matrix uses additive (Laplace) smoothing α=0.5** over a fixed
   4 832-lemma vocabulary. Smoothing is necessary because the 114-row
   surah counters are sparse (most surahs use a few hundred lemmas
   each). I checked α ∈ {0.1, 0.5, 1.0} for the most-similar/dissimilar
   pairs — they don't change rank, only magnitude.
5. **Heaps' law sample sizes:** drawn without replacement, single seed
   (42). A multi-seed bootstrap would tighten the β estimate slightly
   but the R² is already 0.986 so the headline number is stable.
6. **Verse-index trend** uses Pearson correlation between verse index
   (raw integer) and the verse's letter-entropy. I drop verses with
   <10 letters and surahs with <5 surviving verses.
7. **2-cluster Meccan/Medinan smoke test** is *not* a real clustering —
   it just sees whether each surah is closer (in symmetrized KL) to
   Al-Fatiha (#1, Meccan) or Al-Baqara (#2, Medinan). 74.6% match is
   the result. A real hierarchical clustering would do better; this is
   an honest sanity-check upper bound on "trivially separable."

## Surprises / observations

- **The bottom-10-entropy and top-10-entropy surahs are *all* Meccan.**
  But for opposite reasons: the bottom 10 are extremely *short* Meccan
  surahs at the end of the mushaf (Al-Ikhlas, Al-Kafirun, Al-'Asr…)
  where small letter counts cause undersampling; the top 10 are the
  rhetorical/oath-laden mid-Meccan surahs (An-Najm, An-Nazi'at, 'Abasa,
  Al-Ghashiyah, Al-A'la). This is an artefact of the small-sample bias
  in entropy estimation interacting with surah length, and it's the
  single most important caveat in the writeup.
- **Pearson(log(letter count), H) = 0.5825.** The relationship between
  surah length and observed letter entropy is real and is dominated by
  the small-sample bias above. It's not "longer surahs are intrinsically
  more disordered" — it's "longer surahs let you actually *see* the
  full alphabet."
- **Most-similar surah pair (lowest KL):** Al-Kawthar (108) ↔ Al-'Asr
  (103). Both are 3-verse Meccan surahs with high lexical overlap on
  function words. **Most-dissimilar pair:** Al-Baqara (2) ↔ At-Takathur
  (102). One is the longest surah, the other is one of the shortest;
  this is partly a "size" effect partly a "topic" effect.
- **Compression ratios drop monotonically with surah length.** Smallest
  surahs are essentially incompressible (Al-Kawthar is at 0.979 — the
  gzip header almost doubles the size). Largest surahs compress to ~26%.
  Pearson(gzip ratio, length) = −0.543; (gzip ratio, H_letter) = −0.618.
  The compression "Kolmogorov proxy" is mostly measuring "is this surah
  big enough to amortize the gzip overhead." A within-length-stratum
  comparison would be more meaningful; flagged as a robustness item.
- **Position-letter MI = 0.077 bits, MI/min(H_P,H_L) = 1.7%.** Tiny
  but nonzero. There *is* statistical structure in which letters appear
  at the start vs middle of a verse, but it's small.
- **Within-surah verse-index trend:** mean Pearson(verse_idx, H) =
  +0.088, 61/107 surahs positive. Weakly biased toward "later verses
  are slightly more entropic than earlier ones" but the effect is tiny
  and probably driven by structural openings (oaths, vocatives, the
  cluster of huroof muqatta'at) being lower-vocabulary than later
  prose. Honest answer: this is a null result with a hint of a trend.

## Most statistically surprising single finding

**Zipf exponent α ≈ 1.32**, R² = 0.975. The canonical Zipf exponent for
natural-language word distributions is α ≈ 1.0; English fiction is
typically 1.0–1.1, modern Arabic news corpora 1.0–1.2. The Quranic
lemma distribution is **noticeably steeper** than baseline natural
language — meaning the head of the distribution (الله, ما, لا, في, إن,
قال, الذي, على, كان…) carries an unusually large fraction of all lemma
tokens, and the tail of one-off lemmas is correspondingly lighter.
This is consistent with the Quran being a relatively focused-vocabulary
text built around a high-frequency core of theological function words,
and it's the first finding here that has any chance of surviving formal
null testing because it's a robust statistical property of the *whole
text*, not a small-sample artefact of an individual surah.

## Outputs

- `findings/phase-b-hypotheses/information-theory.md` — full report.
- `findings/phase-b-hypotheses/csv/per-surah-entropy.csv`
- `findings/phase-b-hypotheses/csv/kl-matrix.csv`
- `findings/phase-b-hypotheses/csv/compression.csv`
- `findings/phase-b-hypotheses/csv/verse-index-trend.csv`
- `findings/phase-b-hypotheses/csv/info-theory-results.json`
- `analysis/info_theory_run.py` — re-runnable script (stdlib only).

## What's NOT done

- No null-model run on any of these statistics. Everything in this
  report is **descriptive / exploratory**, not a "finding" in the §3
  sense of the rigor protocol. None of these numbers has a
  pre-registered p-value yet. They're scouting reports for what's
  worth a formal Phase B novel-finding pre-reg.
- Robustness against alternative orthography (full-tashkeel,
  with-shadda-doubled, hamza-collapsed): not done.
- The Heaps fit is on randomized sub-samples, not contiguous prefixes,
  and uses one seed.
- The KL matrix is asymmetric and I only used a crude symmetrization
  for the clustering smoke test. A proper Jensen-Shannon distance plus
  hierarchical agglomerative clustering (Ward) is the natural next
  step.
