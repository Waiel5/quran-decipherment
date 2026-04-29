# palindrome-full-sweep — run 1 journal

**Agent:** palindrome-full-sweep
**Start:** 2026-04-13 00:48 +08
**Task:** Pre-registered unified palindrome sweep across three scales (letter / root / word) with null-model validation, testing H11, H12, H13 from the deep-hypotheses queue.

## Pre-registration (copied from task spec)

- **H11 letter-level.** Scan all 6,236 verses for odd-length letter palindromes
  ≥ 7 chars within the letter-stream of each verse (whitespace-stripped).
  Primary null: character-shuffle within-verse (1000 permutations). Secondary
  null: 3-gram Markov surrogate (1000 draws). Accept if observed count exceeds
  the 95th percentile of the null under Bonferroni-adjusted α = 0.017.
- **H12 root-level.** Derive the root sequence for each verse from QAC v0.4
  (first ROOT feature per segment aggregated by orthographic token). Scan for
  root-palindromes of length ≥ 3. Null: bag-of-roots shuffle within verse,
  1000 permutations, preserving stem count.
- **H13 word-level.** Scan across verse boundaries at the surah level for
  3-word palindromic sequences (orthographic-token identity). Null: word-shuffle
  within surah, 1000 permutations preserving verse length.

## Rules tuple

```yaml
orthography: no-tashkeel
word_definition: orthographic-token (real_words filter) + lemma/root via QAC v0.4
letter_definition: graphemes (U+0621..064A ∪ U+0671..06D3)
basmala_policy: counted-only-in-surah-1
verse_numbering: hafs-kufan
abjad_table: mashriqi
null_model: within-verse char-shuffle (H11 primary), 3-gram Markov (H11 secondary),
            bag-of-roots shuffle (H12), word-shuffle within surah (H13)
```

## Log

- 00:48 Read docs/methodology §8 anchors, statistical-rigor-protocol, deep-hypotheses-queue, existing palindromes.md, master-index.
- 00:50 Built `scratch/palindrome_full_sweep.py`. Initial run was buffered because of `| tail -80` pipe — killed and rewrote with `python3 -u` and per-hypothesis JSON checkpoints.
- 01:03 Second run launched.
  - H12 bag-of-roots null (1000 perms over 5,386 verses): 38s. Observed = 1170, null mean = 882.7, SD = 27.3, p95 = 929, **z = +10.51, p_exceed = 0.0000**. Confirmed.
  - H11 char-shuffle null (1000 perms over 6,236 verses): 36s. Observed = 19, null mean = 79.9, SD = 8.9, p95 = 94, **z = −6.75, p_exceed = 1.00**. Refuted in the enrichment direction.
  - H11 3-gram Markov null (1000 perms, numpy-cumsum-weighted sampling): ~600s. Observed = 19, null mean = 50.8, SD = 7.3, p95 = 63, **z = −4.37, p_exceed = 1.00**. Refuted under the stronger null as well.
  - H13 word-shuffle null (1000 perms): 22s. Observed A-B-A = 420, null mean = 387.2, p95 = 420, **z = +1.67, p_exceed = 0.053** (fails Bonferroni). Observed A-B-C-B-A = 13, null mean = 2.4, p95 = 5, **z = +6.84, p_exceed = 0.0000** (confirmed).
  - Total runtime: **703 s**.
- 01:15 Run complete. JSON outputs saved to `scratch/palindrome_full_sweep_out/{h11,h12,h13}.json`.
- 01:17 Wrote finding `findings/phase-b-hypotheses/palindrome-full-sweep.md`.
- 01:23 Updated `docs/master-index.md`.

## Findings summary (for master-index)

- **Confirmed (H12):** root-palindromic windows ≥ 3 are enriched at z = +10.5 (p < 0.001 after Bonferroni). 1,170 nontrivial windows in 880 verses vs null p95 = 929. Top qualitative cases: Q 24:3 (7-root palindrome `zny·nkH·zny·$rk·zny·nkH·zny` encoding adultery-marriage restriction rule), Q 6:136 (7-root palindrome `$rk·wSl·Alh·kwn·Alh·wSl·$rk` on partners-vs-Allah polemic), Q 5:116 (Jesus's apophatic self-abdication `Elm·nfs·Elm·nfs·Elm`), Q 2:231 (divorce ethics `msk·Erf·srH·Erf·msk`). Kinship-list verses in Q 4, Q 24, Q 33 contribute a large baseline.
- **Confirmed (H13 five-word):** 13 A-B-C-B-A five-word palindromes vs null p95 = 5 (z = +6.84). **11 of 13 are instances of the cosmic-inversion formula** (night/day `yūliju` template ×7; living/dead `yukhriju` template ×4; belief-cycle `āmanū / kafarū` ×2). Q 59:2 is the sole non-cosmic singleton. The formula is a classical Quranic *leitmotiv* noted in al-Rāzī's *Mafātīḥ al-Ghayb* on Q 3:27; its *palindromic-template-at-nine-surahs* characterization is novel.
- **Refuted (H11):** 19 observed odd-length letter palindromes ≥ 7 vs null means 79.9 (char-shuffle) and 50.8 (3-gram Markov). Both nulls overshoot observed by z = −6.75 and z = −4.37 respectively. The Quran **suppresses** letter palindromes; popular apologetics around `kullun fī falak` / `rabbaka fa-kabbir` gets the direction wrong.
- **Refuted (H13 three-word):** 420 observed vs null p95 = 420 exactly. Not significant (p_exceed = 0.053, above Bonferroni 0.017). Particle-flanked function-word palindromes dominate.

## Errors and notes

- First run piped through `| tail -80`, which buffered all output to the end — killed it (PID 33928) before results surfaced. The failure mode was a harness-level pipeline issue, not a bug.
- Second run used `python3 -u` with `tee` to a log file, plus per-hypothesis JSON writes so partial results were durable.
- The 3-gram Markov sampler became the runtime bottleneck (10+ min). Implemented with numpy cumsum + binary search for context-to-successor sampling. Could be faster with vectorized generation, but 1000 perms in 10 min is adequate for a one-time sweep.
