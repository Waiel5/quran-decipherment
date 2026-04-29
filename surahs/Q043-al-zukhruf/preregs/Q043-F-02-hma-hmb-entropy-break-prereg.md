---
prereg_id: Q043-F-02
title: HM-A → HM-B rhyme-entropy structural break — Q 43 entropy < HM-A min
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T19:10:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q043-F-02 — HM-A → HM-B rhyme-entropy structural break

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: Q 43's per-surah Shannon rhyme entropy (last-grapheme of each verse, no-tashkeel) is **strictly less than** the minimum entropy of HM-A {Q 40, Q 41, Q 42}. The HM-A → HM-B transition (Q 42 → Q 43) is therefore a structural break (Q 43 outside HM-A entropy support).

## 2. Null

**H0**: Q 43 entropy is within the HM-A entropy range (≥ min(HM-A entropies)).

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (per project default; matches existing 00-overview-recorded values).
- Source: `quran-text/quran-no-tashkeel.json`.
- For each verse v in surah s: take the last Arabic grapheme of `v["text"].strip()`.
- For each surah s: compute Shannon entropy H(s) = − Σ p_i log₂ p_i over the distribution of last-graphemes across that surah's verses.
- Compute H(40), H(41), H(42), H(43).
- Test: H(43) < min(H(40), H(41), H(42)).

## 4. Direction lock

Pre-committed direction: **H(43) < min(H(40..42))**.

If observed direction reversed: **NULL with pre-commit violation flag**.

## 5. Bonferroni

This pre-reg is part of the Q 43 novel-findings family (4 tests: F-02, F-03, F-04, F-05). Bonferroni-corrected α = 0.05 / 4 = **0.0125**. Per-test thresholds below use the corrected α implicitly via gap-magnitude rather than parametric p (counting tests are exact, not parametric).

## 6. Success / failure criteria

- **VINDICATED**: H(43) < min(H(40..42)) AND H(43) is also below the lowest entropy among any other HM-7 surah (i.e., Q 43 = HM-7 entropy minimum).
- **DIRECTIONAL**: H(43) < min(H(40..42)) but not the global HM-7 minimum.
- **NULL**: H(43) ≥ min(H(40..42)).
- **PRE-COMMIT VIOLATION**: H(43) ≥ max(H(40..42)).

Permutation extension: as a corpus-prior null (MW-2), draw 10000 permutations of the verse-final-letter labels across the corpus, recompute per-surah entropies, and check Q 43's empirical rank against the permuted-null distribution. Report empirical p_perm.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q043-F-02.json` with: H(40..46), HM-7 entropy ranking, Q 43 empirical rank under permutation null, p_perm.

## 9. Rationale

The existing 00-overview claims Q 42 → Q 43 is the "sharpest one-step bifurcation" in HM-7 with ΔH ≈ −1.97 bits. The pre-reg formalizes the bifurcation claim by demanding Q 43 lie *outside* the HM-A entropy support — not just lower, but strictly below the HM-A range. This is a stronger structural claim than mere magnitude.

## 10. Honest limits

- Last-grapheme is a proxy for *qāfiya* (classical rhyme), not a full *qāfiya* analysis. Classical qāfiya-rules incorporate vowel-sound and pre-final letters; this is a coarse approximation.
- The rules-tuple is no-tashkeel; min-tashkeel and full-tashkeel give different absolute entropies. The relative HM-7 ranking under min/full-tashkeel is not pre-committed and would require a separate test.
