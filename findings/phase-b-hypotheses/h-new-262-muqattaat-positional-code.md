# [[h-new-262-muqattaat-positional-code|H-NEW-262]] — Muqatta'at positional code

**Finding ID**: [[h-new-262-muqattaat-positional-code|H-NEW-262]]  
**Date**: 2026-04-18  
**Pre-reg**: `findings/phase-b-hypotheses/h-new-262-muqattaat-positional-code-prereg.md`  
**Script**: `scripts/h_new_262_muqattaat_positional_code.py`  
**JSON**: `findings/phase-b-hypotheses/csv/h-new-262.json`  
**Bonferroni**: `k = 14`, `alpha_bon = 0.0035714286`  
**Verdict**: **MIXED-LETTER-SPECIFIC.** The broad 14-letter positional-code claim is not supported, but **two letters do survive Bonferroni-14 in the pre-registered later-position direction: `ن` and `ي`**. Positive control passes.

## Headline

The formal same-letter contrast does **not** produce a coherent
14-letter late-position code across muq-opened surahs. Exactly **2 of
14** letters survive the pre-registered one-sided family:

- `ن`: strong later-position shift in muq-opened surahs
- `ي`: narrow Bonferroni survivor with a small effect

Everything else is either null or direction-reversed. The sign balance
is perfectly split (`7` positive deltas, `7` negative/non-positive), and
the descriptive Stouffer aggregation of the 14 pre-registered p-values
is not supportive (`Z = -0.97`, `p = 0.834`).

So the honest read is:

> **there are letter-specific positional differences, but not a broad
> all-14 later-position code.**

## Positive control — PASS

The [[h-new-113-letter-position|H-NEW-113]]-style position-binning instrument behaves as expected on
known rhyme-heavy versus prefix-heavy letters:

| Letter | Overall bin-10 density | Threshold | Result |
|---|---:|---:|---|
| `ن` | 0.1556 | `> 0.13` | PASS |
| `ر` | 0.1598 | `> 0.13` | PASS |
| `ي` | 0.1551 | `> 0.13` | PASS |
| `ا` | 0.0680 | `< 0.10` | PASS |
| `ل` | 0.0783 | `< 0.10` | PASS |

This matters because the main result is mostly null/mixed. The null is
interpretable only because the instrument clearly detects the expected
terminal bias for canonical rhyme letters.

## Primary family results

Primary test per letter: one-sided Mann-Whitney U (`muq-opened > non-muq-opened`)
on normalized within-verse positions. Table reports the signed mean shift
and the verse-final bin-10 relative risk for interpretation.

| Letter | `n_muq` | `n_non` | `Δ mean pos` | `RR_bin10` | `p_one_sided` | Bonf-14 | Note |
|---|---:|---:|---:|---:|---:|---|---|
| `ا` | 28063 | 31217 | -0.00458 | 0.755 | 9.518e-01 | NO | reverse-leaning |
| `ل` | 17933 | 20258 | +0.00468 | 1.079 | 5.344e-02 | NO | null |
| `م` | 12812 | 13923 | +0.00912 | 1.047 | 4.133e-03 | NO | near miss |
| `ص` | 988 | 1084 | +0.00013 | 1.077 | 4.820e-01 | NO | null |
| `ر` | 5703 | 6700 | -0.02377 | 0.785 | 1.000e+00 | NO | exploratory reverse hit |
| `ك` | 4937 | 5560 | -0.00555 | 0.890 | 8.448e-01 | NO | null |
| `ه` | 7826 | 9368 | -0.01702 | 0.591 | 1.000e+00 | NO | exploratory reverse hit |
| `ي` | 12243 | 13504 | +0.00973 | 1.028 | 3.465e-03 | **YES** | small positive survivor |
| `ع` | 4563 | 4842 | +0.00627 | 1.075 | 1.374e-01 | NO | null |
| `ط` | 560 | 713 | -0.02065 | 0.955 | 9.145e-01 | NO | null |
| `س` | 2832 | 3180 | -0.00962 | 1.139 | 9.205e-01 | NO | shape mismatch without mean shift |
| `ح` | 1934 | 2206 | +0.00448 | 0.908 | 3.376e-01 | NO | null |
| `ق` | 3579 | 3455 | -0.03152 | 0.839 | 1.000e+00 | NO | exploratory reverse hit |
| `ن` | 13255 | 14015 | +0.02446 | 1.245 | 4.084e-12 | **YES** | clear positive survivor |

### Survivors in the pre-registered direction

`ن` is the cleanest positive result:

- mean position: `0.5376` in muq-opened vs `0.5131` in non-muq-opened
- `Δ = +0.02446`
- verse-final `RR_bin10 = 1.245`
- `p = 4.08e-12`

`ي` survives too, but only narrowly and with a much smaller effect:

- mean position: `0.5296` vs `0.5199`
- `Δ = +0.00973`
- verse-final `RR_bin10 = 1.028`
- `p = 3.47e-03`, just under `alpha_bon = 3.57e-03`

`م` is the main near miss:

- `Δ = +0.00912`
- `RR_bin10 = 1.047`
- `p = 4.13e-03`, slightly above Bonferroni-14

## Reverse-direction signals

The pre-registered family looked only for **later** positions in
muq-opened surahs. Three letters survive Bonferroni-14 in the opposite
direction on the exploratory reverse check:

- `ر`: `Δ = -0.02377`, reverse `p = 1.53e-06`
- `ه`: `Δ = -0.01702`, reverse `p = 6.94e-06`
- `ق`: `Δ = -0.03152`, reverse `p = 3.31e-06`

These reverse hits reinforce the main interpretation: the family is not
moving in one common signed direction. It is a mixed per-letter pattern.

## Distributional note

Because the task is about position **distributions**, the script also
reported two-sided KS tests descriptively. Those KS results do show that
several letters differ between partitions, but the signs are mixed:

- positive-directionally interesting: `ن`, `م`
- reverse-directional: `ا`, `ر`, `ه`, `ق`

That is exactly why the directional family verdict should stay
conservative. There is structure here, but not a clean all-14 code.

## Verdict

**Broad verdict**: **MIXED-LETTER-SPECIFIC**, not a general 14-letter
positional code.

**Direct Bonferroni-14 answer**:

- **Yes**, letter-level effects survive Bonferroni-14.
- In the **pre-registered later-position direction**, the survivors are
  **`ن` and `ي`**.
- In the **exploratory reverse direction**, the strongest survivors are
  **`ر`, `ه`, and `ق`**.

That pattern is too mixed to promote a broad "the muq-opened surahs push
the muq letters later in verse" claim. The honest promotion ceiling is:

> **isolated letter-specific positional shifts, especially `ن`, rather
> than a family-wide positional code.**
