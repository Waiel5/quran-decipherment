# Gematria landscape — run 1 journal

**Date:** 2026-04-12
**Agent:** phase-b-novelty (gematria sub-line)
**Inputs read:** docs/design.md, docs/methodology.md (§6 abjad table,
§8 anchors), docs/statistical-rigor-protocol.md, docs/claims-catalog.md
(family A only — Khalifa Code-19), analysis/tools/gematria.py,
analysis/tools/loader.py
**Code:** analysis/notebooks/gematria_landscape.py

## Sequence of decisions

1. **Read methodology and confirmed the rules tuple** before touching
   any data. Decided to use no-tashkeel JSON (the locked primary corpus
   per §8 of methodology). Letter set = ABJAD_MASHRIQI keys (i.e.
   tashkeel-naked graphemes that the table assigns a value to;
   hamza carriers, ta marbuta, alif maqsura skipped).
2. **Reproduced the basmala = 786 anchor.** First line of every run.
   Maghribi reported as 1026 — the Maghribi value of the basmala does
   not appear to be locked in our anchors yet, recommend adding to
   methodology.md §8.
3. **Computed per-surah and per-verse abjad totals.** Wrote both CSVs.
   Verse count assertion (6236) passed.
4. **Ran a battery of anomaly scans.** Surah level: prime, mod 19,
   small-multiple of sid, famous-word equality, near-19 misses.
   Verse level: ab=letters (impossible), ab=sid×vid, palindromes,
   arithmetic and geometric word-value runs, max/min/mode.
5. **Word-value histogram.** Counted every whitespace token's mashriqi
   value across all 6236 verses. 78,231 non-zero tokens + 4,578
   recitation-mark-only tokens (the locked count).
6. **Prime-mod hunt.** 8 primes × analytic binomial null + Bonferroni.
   Clean negative result.
7. **Surah-name coincidence hunt.** 114 names × {==sid, ==sid×k,
   ==n_verses, ==triangular(sid), %19==0}. Permutation null.
8. **Three null models actually run:**
   (a) Quran-letter-bag draw of N letters, sample size 20 000, for
       Al-Ikhlas total = 1000 question.
   (b) Surah-index permutation, 20 000 trials, for surah-name hits.
   (c) Verse-level abjad shuffle, 5 000 trials, for the
       ab=sid×vid scan.
   Plus analytic binomial for the prime-mod hunt.
9. **WebSearch for prior art** on the most striking individual
   findings: Al-Hadid 57, Al-Ikhlas 1000, Yusuf 156, Surah Qaf.

## What surprised me

- **Al-Ikhlas as a stylistic outlier.** I knew Surah 112 was short
  and Allah-dense; I did not expect its abjad-per-letter to be
  *half* of every other surah. The next-lowest is Al-Kafirun at
  41.6, then a long tail. Al-Ikhlas at 22.2 is not just the minimum,
  it is the minimum *by a large margin*. That is a real, robust,
  table-independent fact about the surah.
- **The exact 1000 is mashriqi-only.** I had hoped this was robust
  but maghribi gives 970. Demoted from "novel finding" to
  "exploratory observation requiring confirmatory pre-registration."
- **No prime beats 19.** I went in expecting the open-prime hunt to
  surface at least one borderline result (8 primes, 1/19 hit rate
  each, raw α=0.05 should produce ~0.4 expected hits at random).
  Instead, all 8 are non-significant and most are *below* their
  expected counts. That itself is mildly anomalous (8 non-anomalies
  in a row), but consistent with Poisson variance.
- **Length-3 arithmetic word runs exist (44 of them) but length-4
  does not.** Reading those length-3 cases by hand is suggestive of
  pure chance (the diffs are arbitrary integers like 53, 10, 50, 16,
  -24).
- **Khalifa's 19 below expectation in this counting tuple.** 5 of 114
  vs expected 6. This isn't a refutation of the Code-19 claims (which
  use a different counting tuple — Uthmani rasm + their own
  basmala policy + per-letter counts within muqatta'at, not surah
  totals). It does mean: nobody should claim "surah mashriqi totals
  are 19-divisible at unusual rates."

## What I would do differently in run 2

- Run all surah-level scans under **both** orthography variants
  (no-tashkeel and full-tashkeel) and report the rule-brittleness as
  a column. Some "novel" findings will collapse; the survivors are
  worth pre-registering.
- Add the **Maghribi basmala = 1026** to methodology.md §8 anchors
  so it locks for downstream tools.
- Add `khalifa-mod19-mashriqi-totals` as a Phase A negative-result
  replication (the "we couldn't find a magic prime" cell deserves to
  go in the catalog as a documented null).
- Compute **lemma-level word-value histograms** once Quranic Arabic
  Corpus morphology is wired in. The current histogram conflates
  inflected forms.
- Properly compute the **expected number of arithmetic length-3 runs**
  under a real Quranic word-value distribution (not uniform), to
  confirm the "44 is unremarkable" claim.

## Files written

- `findings/phase-b-hypotheses/gematria-surah-totals.csv` (114 rows)
- `findings/phase-b-hypotheses/gematria-verse-totals.csv` (6236 rows)
- `findings/phase-b-hypotheses/gematria-landscape.md` (this run's
  full landscape report)
- `analysis/notebooks/gematria_landscape.py` (the analysis script;
  rerunnable from scratch in <30 s)

## Open items handed back to the orchestrator

1. Promote **Al-Ikhlas abjad/letter minimum** to the test register
   with a pre-registration before the next sweep.
2. Add **Maghribi basmala anchor** to methodology.md §8.
3. Spawn a Phase A worker to take the **Quran 50:38** verse and
   the broader Code-19 sub-claims this run did not touch — they
   live in the catalog, not in this gematria sweep.
4. Once QAC morphology is wired, redo the word-value histogram at
   lemma level and recompare to Khalifa's Allah=2698 / Rahim=114
   counts as a clean replication of `khalifa-basmala-word-counts`.
