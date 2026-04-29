# H-NEW-237 journal — run 1

**Date**: 2026-04-17
**Seed**: 20260419
**Pre-reg SHA-256** (runtime-computed):
`ab6ee8d39f0fa53d431406030130b151637d8a6ae5c651986ed6738a16116a63`

## What ran

`scripts/h_new_237_numerical_residuals.py` — three pre-registered null cells
following H-NEW-175 Benford PASS:

- **Cell A**: prime density of 114 per-surah verse counts vs 1000 uniform-
  range integer draws in [3, 286].
- **Cell B**: cumulative letter-count prefix sums against 34
  distinguished-constant × 10ⁿ targets within range [143, 330,709]; null =
  2000 permutations of the 114 per-surah letter counts.
- **Cell C**: total abjad of 114 surah names (mashriqi + maghribi); Null-1
  = letter-bag shuffle (invariance check); Null-2 = 1000 fake-name draws
  from corpus-wide letter-frequency distribution with matched per-name
  lengths.

Rules tuple: (no-tashkeel, hafs-kufan graphemes, orthographic tokens,
basmala-counted-only-in-surah-1, mashriqi primary + maghribi secondary).
Bonferroni k = 3, α_bon = 0.0167.

## Results (summary)

| Cell | Statistic | Observed | Null mean | p_raw | p_bon | Pass @α=0.0167 |
|---|---|---:|---:|---:|---:|:-:|
| A prime-V | count of primes in V | 32 | 24.03 | 0.0810 | 0.243 | **NO → NULL** |
| B cum-const | hits @ε=0.001 (upper tail) | 2 | 1.14 | 0.3065 | 0.919 | **NO → NULL** |
| B cum-const | min-rel-distance (lower tail) | 4.73e-4 | 9.55e-4 | 0.400 | — | NULL |
| C name-abjad (mashriqi) | sum | 40,089 | 46,183.5 | 0.108 | 0.324 | **NO → NULL** |
| C name-abjad (maghribi) | sum | 47,529 | 49,000.3 | 0.734 | — | NULL |

MW-5 cheats:
- Cell A index-shuffle invariance: OK (32 primes unchanged).
- Cell B identity-permutation invariance: OK (prefix sums exactly recovered).
- Cell C Null-1 letter-bag invariance: OK (sums unchanged under shuffle).

## Pre-committed expected verdict

NULL for all 3 cells — matched.

## Descriptive notes (not significant)

- Cell A: 32 > 24 at z = +1.86; explained by the descending-tail-density
  prior at small integers (many V ∈ {3, 5, 7, 11, 13}).
- Cell B: the 2 hits at ε = 0.001 fall at k = 40 (prefix = 261,643 vs
  φ²×10⁵ = 261,803, rel = 6.1×10⁻⁴) and k = 70 (prefix = 314,308 vs
  π×10⁵ = 314,159, rel = 4.7×10⁻⁴). Neither surah (Q 40 Ghāfir,
  Q 70 al-Maʿārij) holds an independent structural flag at letter-count
  prefix axis. The hit rate matches the analytic density prediction.
- Cell C: S_mashriqi = 40,089 lands 0.045% away from 40,071 = 19 × 2,109.
  BUT: null mean is 46,184 — surah names are *below*-average-abjad
  (low-value letters {ا,ل,ن,م,ه,ر} dominate). Maghribi S = 47,529 is
  *above* its null mean (49,000), giving p_raw = 0.734. Arithmetic is
  close but not rare.

## Operational notes

- All permutation counts delivered (1000 A, 2000 B, 1000 C); total
  runtime well under 1 min.
- JSON output at `findings/phase-b-hypotheses/csv/h-new-237.json` contains
  every per-cell statistic and all Cell-B observed-hit details.
- No post-hoc retuning of the distinguished-integer set in Cell C or the
  constant set in Cell B; rules as locked in pre-reg at SHA above.
- The Cell A uniform-range null was the pre-committed primary; the
  alternative "V shuffle null" is degenerate (invariant to permutation)
  and was not used.

## Output artifacts

- `findings/phase-b-hypotheses/csv/h-new-237.json` — full per-cell numerics.
- `findings/phase-b-hypotheses/h-new-237-numerical-residuals.md` — writeup.
- `findings/phase-b-hypotheses/h-new-237-numerical-residuals-prereg.md` — pre-reg.
- `scripts/h_new_237_numerical_residuals.py` — implementation.

## Lineage

- Parent: H-NEW-175 Benford PASS.
- Sibling null-catalog additions: H-NEW-174 (cumulative-sum arithmetic),
  `mathematical-sequences-audit.md` (24 prior NULLs).
- Cumulative family: ~163 tests, zero Bonferroni survivors across the
  numerological-audit.
