---
id: H-NEW-810
run: 1
date: 2026-04-28
seed: 20260448
prereg_sha: 4f3970eb430bd44d33c89d5577feffd3361866e9f80db6d93000e4e555161bb1
---

# H-NEW-810 — Run 1 Journal

## Pre-run

- Wrote prereg `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz-prereg.md`.
- SHA-256: `4f3970eb430bd44d33c89d5577feffd3361866e9f80db6d93000e4e555161bb1`.
- Embedded SHA in script header and runtime check.
- Prior expectation (forking-paths log written before run): rhyme axis at least partially length-mediated (since H-NEW-770 found r(letters, d_content) ≈ 0.872, very close to the |r(content, rhyme)| = 0.864 of H-NEW-730); phoneme axis less obviously length-coupled, since the phoneme channel is consonantal-spectrum-driven, not boundary-driven.

## Inputs

- d_content[100], d_rhyme[100], d_phoneme[100] from `csv/h-new-730.json`.
- letters_per_verse[100], words_per_verse[100] from `csv/h-new-770.json` (`metric_*.window_obs`).
- Verified all five vectors length-100 and `starts` arrays equal.
- Re-derived r(d_content, d_rhyme) = -0.8643 (matches H-NEW-730 reported value to 4 dp).
- Re-derived r(d_content, d_phoneme) = -0.8933 (matches H-NEW-730 reported value).

## Compute

- Partial-r formula: classical (r_xy − r_xz·r_yz) / sqrt((1-r_xz²)(1-r_yz²)).
- Permutation null: shuffle Y only (rhyme or phoneme), keep X (content) and Z (length) aligned. 10000 perms, seed 20260448. Lower-tail p (one-sided) since direction was pre-committed.
- Bonferroni-3, α_bon = 0.01667.

## Results

| Test | Pair | Z | partial r | perm p | classification |
|------|------|---|-----------|--------|----------------|
| T1 | content × rhyme   | letters | -0.4054 | 0.00010 | PARTIAL-DEPENDENT |
| T2 | content × rhyme   | words   | -0.4017 | 0.00010 | PARTIAL-DEPENDENT |
| T3 | content × phoneme | letters | -0.8563 | 0.00010 | PASS-INDEPENDENT |

Pairwise marginal r values used in the partial formula (X=d_content, Y=d_rhyme or d_phoneme, Z=length):
- T1: r_xy = -0.8643, r_xz(content,letters) = +0.8719, r_yz(rhyme,letters) = -0.8855. (rhyme-distinctness drops sharply with letters/verse — long verses → flat rhyme; short verses → sharp rhyme. Length and rhyme are tightly negatively coupled.)
- T2: r_xy = -0.8643, r_xz(content,words) = +0.8730, r_yz(rhyme,words) = -0.8861.
- T3: r_xy = -0.8933, r_xz(content,letters) = +0.8719, r_yz(phoneme,letters) = -0.6656. (phoneme-distinctness is less tightly coupled to length than rhyme is; |r_yz| = 0.67 vs 0.89.)

The asymmetry between rhyme and phoneme is driven by |r_yz|: rhyme tracks length at -0.89, phoneme tracks length at -0.67. When you partial out length, rhyme loses much more of its anti-twinning than phoneme does, because length explains nearly all of the rhyme-window variance but only ~44% of the phoneme-window variance.

## Verdict

- iʿjāz axis (T1 + T2 jointly): **PARTIAL-DEPENDENT**.
- phoneme axis (T3): **LENGTH-INDEPENDENT**.
- cross-finding-026 should be amended: rhyme strand softens; phoneme strand strengthens.

## Honesty notes

- Per prereg §8 honesty rule, this softening result is reported cleanly. The headline H-NEW-730 r = -0.864 is a real signal, but **most of its squared explanatory power is verse-length co-variation**. Only ~22% of the rhyme-axis r² survives length-control.
- The phoneme axis is the more architecturally robust iʿjāz channel.
- Forking-paths note: prior expectation matched outcome direction (rhyme more length-mediated than phoneme), so I did not adjust thresholds post hoc.

## Files

- Prereg: `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz-prereg.md`
- Script: `scripts/h_new_810_length_controlled_ijaz.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-810.json`
- Findings: `findings/phase-b-hypotheses/h-new-810-length-controlled-ijaz.md`

## Reproduce

```
python3 /Users/grey/Downloads/quran/scripts/h_new_810_length_controlled_ijaz.py
```

Deterministic given seed=20260448 and frozen parent JSONs.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
