---
surah: 39
test_id: Q039-F-03
title: Q 39 — Zumar-throng motif (vv. 71-75) corpus-EXACT structural-twin search
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q039-novel-tests
alpha_bon: 0.0125
direction: zumar_motif_corpus_unique
---

# Q039-F-03 — Pre-registration: Zumar-throng motif structural-twin search

## 1. Hypothesis (locked before observation)

Q 39's terminal cycle vv. 71-75 contains the surah's eponymous motif: the wicked are driven *zumaran* (in throngs) to Jahannam (v. 71-72) ↔ the pious are driven *zumaran* to the Garden (v. 73-74), with the angelic *salām ʿalaykum ṭibtum* greeting and the closing *al-ḥamdu li-llāhi rabb al-ʿālamīn* (v. 75) providing closure.

The *zumar* root (*z-m-r*) appears EXACTLY 2 times corpus-wide — both in this surah, both in vv. 71 and 73 (verified from QAC v0.4). The eponymous motif is corpus-EXACT to Q 39.

The wider motif — paired escort scenes to Hell+Garden with verbatim parallel construction *wa-sīqa alladhīna [kafarū / ittaqaw]... ilā [Jahannam / al-jannah] ZUMARAN ḥattā idhā jāʾūhā [futiḥat / wa-futiḥat] abwābuhā wa-qāla lahum khazanatuhā [...]* — is a paired-twin construction. Test: is there a structural-twin elsewhere in the corpus where two consecutive verses share equal-length verbatim wa-sīqa parallel mirroring?

**H1 (direction-locked):** Among all consecutive-verse-pair structural twinnings in the corpus (operationalized as verse pairs with ≥ 60% surface-string Jaccard overlap AND opposite eschatological polarity = one mentions Jahannam-class word, one mentions Janna-class word, both within same surah), Q 39:71-72 ↔ Q 39:73-74 is RANK-1 by Jaccard overlap.

**H2 (direction-locked, secondary):** No other surah has 2 consecutive eschatological-polarity-paired verse-pairs with shared verbatim opening word ≥ 4 (i.e., the *wa-sīqa alladhīna* 3-word + ḥattā idhā jāʾūhā parallel structure is corpus-EXACT to Q 39).

**Pre-commit violation conditions:**
- H1 reverse: Q 39's twin-block ranks below 50th percentile of the consecutive-twin-pair Jaccard distribution → publish as NULL with `EXPLORATORY-REVERSE`.
- H2 reverse: Multiple other surahs replicate the *wa-sīqa alladhīna* construction → motif is shared, not Q 39-EXACT.

**H0:** Q 39:71-75 is one of many similar paired-eschatological constructions in the corpus.

## 2. Operational definitions

- Source: `quran-text/quran-no-tashkeel.json`.
- Strip waqf marks ۚۖۗۘۙۛۜ۞.
- For each surah, enumerate all 4-tuple-windows (v_a, v_a+1, v_b, v_b+1) where v_b > v_a+1, both pairs in same surah.
- Eschatological-polarity test: pair_1 contains a Jahannam-class lemma {jhnm, nAr, bs, sEr, jHm, lZy, htm, hwy} OR pair_2 contains a Janna-class lemma {jnn (paradise), Erš, frdws}. Use QAC root.
- Surface Jaccard: bag-of-orthographic-words. j(pair_1, pair_2) = |w(pair_1) ∩ w(pair_2)| / |w(pair_1) ∪ w(pair_2)|.

### Test 1 (H1) — Rank-1 paired-twin
- For all qualifying 4-tuples, compute Jaccard. Q 39's (71-72, 73-74) gets a Jaccard score; check whether it is RANK-1 over the corpus.
- Permutation: 10,000 shuffles of within-surah verse positions (re-numbering only); recompute the Q 39:71-72/73-74 Jaccard at each shuffle.

### Test 2 (H2) — wa-sīqa pattern corpus-EXACT
- Search no-tashkeel corpus for any verse beginning *wa-sīqa* (وسيق) at first orthographic word position; count surahs with ≥ 2 such verses.
- Required: corpus-wide ≥ 2 *wa-sīqa* incipits exist in EXACTLY 1 surah (Q 39).

## 3. Empirical anchors (verified pre-reg)

From `quran-text/quran-no-tashkeel.json`:
- Q 39:71 begins: وسيق الذين كفروا إلى جهنم زمرا...
- Q 39:73 begins: وسيق الذين اتقوا ربهم إلى الجنة زمرا...
- Q 39:72 begins: قيل ادخلوا أبواب جهنم...
- Q 39:74 begins: وقالوا الحمد لله الذي صدقنا وعده...

The verbatim parallel *wa-sīqa alladhīna* + *ḥattā idhā jāʾūhā futiḥat abwābuhā wa-qāla lahum khazanatuhā* is the load-bearing parallel.

The H2 *wa-sīqa* corpus-incipit count is NOT inspected pre-reg; the corpus-EXACT direction is locked because (a) the root *zmr* IS corpus-EXACT to Q 39 (2 tokens), (b) the parallel construction in adjacent verses is rare (al-Suyūṭī notes it in *Itqān* nawʿ on *al-mutashābih*).

## 4. Success / Failure

- **CONFIRMED-DIRECTED**: H1 rank-1 with perm-p ≤ 0.0125 AND H2 corpus-EXACT (only Q 39 has the construction repeated).
- **PASS-DIRECTED**: H1 or H2 passes; not both.
- **NULL**: Both fail.

## 5. Honest limits

- The Q 39:71-72/73-74 parallel is OBVIOUSLY visible to any reader of the surah; the test is whether it is *corpus-EXACT* in the formal sense (no equivalent paired construction elsewhere). The Jaccard rank-1 prediction is a strong empirical claim, and the *wa-sīqa* incipit count is the simpler binary check.
- A near-twin elsewhere (e.g., Q 7 al-Aʿrāf paired Jahannam/Janna entrances at vv. 36-43 vs vv. 42-43) is plausible; if found, H1/H2 may both fail.
- Surface Jaccard is fragile to function-word inclusion. Robustness sub-test: also compute root-Jaccard via QAC. Disclosed: this is a sensitivity check, not Bonferroni-counted.

## 6. Bonferroni & rules-tuple

- Family `Q039-novel-tests`, k=4, α_bon = 0.0125.
- Rules-tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan).
- Seed 20260509.
