---
finding_id: Q036-F-04
title: "Eschatological-formula density of Q 36 vs corpus"
date_pre_registered: 2026-04-28
status: PRE-REGISTERED
seed: 20260428
n_perm: 10000
bonferroni_k: 114
alpha_raw: 0.05
alpha_bonferroni: 4.39e-4
direction: positive (Q 36 expected to have eschatology-density above corpus mean)
---

# Q036-F-04 — Eschatological-formula density audit

## Hypothesis

al-Ghazālī's grounding for the *qalb al-Qurʾān* tradition (cited by al-Rāzī Q 36 commentary, see `03-tafsir-survey.md` §2.1) attributes Q 36's centrality to its **dense resurrection-and-eschatology presentation**: "the validity of faith is in confessing the *ḥashr* (resurrection-gathering), and the *ḥashr* is established in this surah with the most-expressive form, so it was made the heart of the Qurʾān for that reason."

We test: does Q 36 over-concentrate the Quranic eschatological-formula lexicon at a rate distinguishable from corpus mean, after Bonferroni correction for testing all 114 surahs?

## Eschatology-cluster definition (LOCKED PRE-REG)

The eschatology-cluster is defined as the set of substring-patterns:

```
ESCHAT = {
  يوم   (yawm — day, including yawm-al-qiyāma, yawm-al-baʿth, yawm-al-fasl etc.; substring incl. forms with prefixed وَ، فَ، الـ، نـ),
  الساعة (al-sāʿa — the Hour),
  الصور  (al-ṣūr — the Trumpet),
  القيامة (al-qiyāma — the Resurrection),
  بعث/يبعث (b-ʿ-th — raising-from-the-dead conjugations: يبعث / بعثنا / نبعث / البعث),
  نار   (nār — fire / النار / نار),
  الجنة (al-janna — the Garden),
  موت/الموتى (m-w-t — death-related: الموتى / موت / موتاكم),
}
```

This is 8 sub-patterns, drawn from the standard Quranic eschatological-vocabulary register. All 8 are pre-locked before any computation; no patterns will be added or removed after observing the data.

We exclude *kullu* (collective) and *idhā* (when..) as too generic across non-eschatological contexts.

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-substring, basmala-counted-only-in-Q1, Hafs-Kufan, mushaf-order)`.

## Per-surah computation

For each surah s, compute:
- `count(s)` = total occurrences of any of the 8 ESCHAT substrings in s.
- `words(s)` = total orthographic words (no-tashkeel) of s.
- `density(s)` = count(s) / words(s) × 1000 (per 1000 words).

Rank surahs by density.

## Null distribution

Permutation null: shuffle the (surah → words, surah → ESCHAT-counts) pairing 10,000× (seeded random, seed = 20260428), preserving total ESCHAT count + total words but breaking the surah-wise association. Compute null density distribution per surah-position.

## Direction (LOCKED)

The direction is **POSITIVE**: Q 36 is expected to over-concentrate eschatology lexicon. A *negative* result (Q 36 below corpus mean density) is a NULL finding to be published with full prominence.

## Success criteria

- p_raw < 4.39 × 10⁻⁴ (Bonferroni for 114 surahs): **VINDICATED**.
- p_raw < 0.05 but > 4.39 × 10⁻⁴: **DIRECTIONAL**.
- Q 36 ranked top-quintile (rank ≤ 23/114) on density: **DIRECTIONAL** (additional check).
- p_raw > 0.05: **NULL**.

## Failure criteria

- Q 36 density < corpus mean: direction-violation, treat as NULL with full prominence.
- Bonferroni α not met: not VINDICATED (DIRECTIONAL at most).

## Discriminating control

Q 75 al-Qiyāma (the eschatologically-named short-Meccan): expected to be top-3 by density. If Q 75 fails to outrank Q 36, the discriminating control fails (the test is too coarse). If Q 75 outranks Q 36 by a wide margin (which is expected — Q 75 is purely eschatological in 40 short verses), the test is discriminating but Q 36's claim becomes weaker (it is moderate-eschatological, not extreme-eschatological).

The corpus-wide expected top-density set: Q 75 al-Qiyāma, Q 77 al-Mursalāt, Q 82 al-Infitār, Q 99 al-Zalzala, Q 101 al-Qāriʿa, Q 81 al-Takwīr — the short-Meccan eschatological cluster.

## Output files

- Pre-reg: `preregs/Q036-F-04-eschatological-formula-density-prereg.md`
- Script: `scripts/Q036_F_04_eschatological_formula_density.py`
- JSON: `csv/Q036-F-04.json`
- Findings: `06-novel-findings.md` Q036-F-04.
