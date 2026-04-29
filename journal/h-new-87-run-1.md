# Journal — H-NEW-87, Run 1

**Specialist:** `h-new-87-specialist`
**Date:** 2026-04-15
**Pre-reg:** `findings/phase-b-hypotheses/h-new-87-786-substrings-prereg.md`
**Output:** `findings/phase-b-hypotheses/h-new-87-786-substrings.md`
**Catalog:** `findings/phase-b-hypotheses/h-new-87-786-catalog.tsv`
**Script:** `scripts/h_new_87_786_substrings.py`
**Family/Wave:** 2026-04-15-Wave-Bismillah-Numerology

## Goal

Audit the classical claim that the Bismillah's mashriqī abjad value of **786** is in any way distinctive: is 786 a *unique* signature of `بسم الله الرحمن الرحيم` in the Quran's running text, or do many other multi-word substrings sum to 786 too?

## Procedure

1. Loaded `quran-text/quran-no-tashkeel.json` via direct JSON (matches `analysis/tools/loader.load_quran('no-tashkeel')` semantics — basmala only at Q 1:1, and per H-NEW-50 also at Q 27:30 inside the verse).
2. Built the canonical-order word stream — 82,375 whitespace-tokens.
3. Computed mashriqī `word_value` for every token via `analysis/tools/gematria.word_value` (verified anchor: `text_value('بسم الله الرحمن الرحيم') = 786` at startup).
4. Sliding-window sums for w ∈ {3, 4, 5, 6} via O(n) rolling-sum over the per-word values (no recomputation per window).
5. Catalogued every position whose sum = 786, plus distribution stats (rank of 786, neighbour-density ratio at radii 10/20/50, top-5 most-common values, max count of any value).
6. Meaningfulness pass: for every 786-substring, flagged those that are **single-verse** (no cross-verse boundary) and **contain a divine-name token** (الله, الرحمن, الرحيم, ربك/رب-family, etc.) or are literally the Bismillah.

## Key results

- **Bismillah verified at exactly 786** under mashriqī.
- **w=4 (the Bismillah's own word count): 52 substrings sum to 786**, including the actual Bismillah at Q 1:1[0–3] and the internal Bismillah at Q 27:30[4–7].
- **Neighbour-density ratio at w=4 = 0.943** (≈ 1.0 = typical density). Sensitivity at r=10 → 0.913, r=50 → 0.924.
- **Rank of 786 at w=4 = 345** out of 3,418 distinct values — top decile of frequency, *not* a sparse value. The most common w=4 sum is **915** (128 occurrences); 786 is roughly half as common, but that places it among hundreds of similarly-common totals, not as an outlier.
- w=3: 56 hits, ratio 0.867 (also typical-to-dense).
- w=5: 29 hits, ratio 1.435 (somewhat rarer).
- w=6: 23 hits, ratio 1.296 (somewhat rarer).
- **Verdict per locked decision rule: CONTRADICTED H1.** 786 is *not* numerically distinctive at the Bismillah's own window size. It is approximately as common as nearby abjad totals.

## Most striking matches (qualitative, single-verse)

- **`ألم تر أن الله`** ("Hast thou not seen that God…") = 786 at w=4. Ten occurrences: Q 14:19, 22:18, 22:63, 22:65, 24:41, 24:43, 31:29, 35:27, 39:21, 58:7. A canonical iltifāt-tinged phrase that opens many divine-witness passages. This is the most contextually meaningful 786-substring after the Bismillah itself.
- **`التي حرم الله إلا`** ("which God has made forbidden, except…") = 786 at w=4. Three occurrences: Q 6:151, 17:33, 25:68 — all in the famous "do not kill the soul which God has forbidden except by right" prohibition. This is a verbatim repeated formula.
- **`كفروا بآيات الله`** ("they disbelieved in God's signs") at w=3 = 786, four occurrences (Q 3:4, 8:52, 29:23, 39:63).
- **`ومما رزقناهم ينفقون`** ("and from what We have provided them, they spend") at w=3 = 786, six occurrences across the Quran (Q 2:3, 8:3, 22:35, 28:54, 32:16, 42:38).
- **`بسم الله الرحمن الرحيم`** at Q 27:30 (Sulaymān's letter to Bilqīs) — the second canonical 786 of the Bismillah.

## Interpretation

- The 786-of-Bismillah is **not** a cryptographic signature; it is one of hundreds of ordinary values reachable by 4-word stretches of Arabic Quranic text.
- However, two of the recurring 786-phrases (`ألم تر أن الله` 10×, `التي حرم الله إلا` 3×) are **genuine theological-formula repetitions**, not random word-bag matches. This is a *content* phenomenon (formulaic repetition) showing through the abjad metric, not an esoteric numerological signal.
- Classical audit ledger entry: this lays an empirical foundation for the standard scholarly position that the **786 = bism allāh ar-raḥmān ar-raḥīm** equation is real arithmetic but bears no statistical uniqueness inside the Quran. Its talismanic significance in the post-classical tradition (use as protective seal, etc.) cannot draw warrant from Quran-internal numerical sparsity.
- The fact that the *most-common* w=4 sum is 915 (128 occurrences) — much more than 786's 52 — is a useful counter-anchor; if 786 were truly sparse, we would expect rank ≤ 100 and ratio ≥ 5. Neither holds.

## Followups queued

- Same scan under maghribī table (Bismillah maghribī = 1026; H-NEW-87b candidate).
- Classical-source pass: trace whether any pre-modern source already noticed the `ألم تر أن الله` = 786 coincidence (likely not).
- Cross-reference with H-NEW-50: does the 27:30 internal Bismillah contribute disproportionately to any sub-pattern here?

## Files touched (created)

- `findings/phase-b-hypotheses/h-new-87-786-substrings-prereg.md`
- `scripts/h_new_87_786_substrings.py`
- `findings/phase-b-hypotheses/h-new-87-786-substrings.md`
- `findings/phase-b-hypotheses/h-new-87-786-catalog.tsv`
- this journal

## Confirmed not touched

- monograph (THE-QURAN-DECIPHERMENT-MONOGRAPH.md)
- man-at-the-center (THE-MAN-AT-THE-CENTER.md)
- master-findings-ledger (left to integration agent)
