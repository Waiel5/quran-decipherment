# Pre-registration — H-NEW-2350: Cross-surah exact-verse twins and their revelation-order proximity

**Pre-registered by:** Waiel Al-Shujaa
**Date:** 2026-05-29 (locked BEFORE computation)
**Seed:** 20260509 · **Permutations:** 10000
**Rules-tuple:** (no-tashkeel orthographic verse-string, NFC + whitespace-normalized, Hafs-Kūfan; revelation order = Tanzil Egyptian Standard, primary; Nöldeke = robustness)

## Background

H-NEW-2310 censused all repeated verse-strings (≥2×). The Q066-F-01 deep-dive noted **11 verbatim full-verse (≥10-token) twin groups**. This pre-reg isolates the **substantive cross-surah** twins and asks a new, directional question: when the *same verse* appears in two different surahs, are those surahs revealed **close together in time** (a same-period compositional phenomenon) or scattered across the revelation timeline?

## Definitions

- **Verse-string:** the full no-tashkeel text of a verse, NFC-normalized, single-spaced, trimmed (basmala handled as it appears in the JSON).
- **Token length:** word count by whitespace.
- **Cross-surah twin group:** a verse-string that occurs in **≥2 distinct surahs**, with token length **≥ 8** (primary; report also ≥6 and ≥10 for robustness — ≥10 should reproduce the "11 groups" figure).
- **Revelation order:** `revelation_order` (1-114) from `data/revelation-order.csv`, keyed by `mushaf_order` = surah id.
- **Within-group pairwise distance:** for a group spanning surahs S = {s1..sg}, the mean over all pairs of |revelation_order(si) − revelation_order(sj)|.

## Primary hypothesis (direction LOCKED)

> **H1:** Cross-surah exact-verse twins link surahs revealed **CLOSE together** in revelation order — the observed aggregate within-group pairwise revelation-distance is **SMALLER** than a size-matched random-surah null.
> Statistic: D_obs = mean over twin groups of (group mean pairwise revelation-distance).
> Null: for each group of size g, draw g distinct random surahs, compute mean pairwise distance; aggregate identically; 10000×, seed 20260509. One-sided p = fraction of null aggregates ≤ D_obs.

If D_obs ≥ null mean (twins are NOT closer, or are farther), publish as NULL/reversed with full prominence.

## Secondary (descriptive / robustness)

- S1: full enumeration of all ≥8-token cross-surah twin groups with verse refs, token length, period, and revelation-order span.
- S2: period-concordance — fraction of groups whose surahs are all the same period (Meccan/Medinan) vs a size-matched random-surah null.
- S3: repeat H1 under Nöldeke order.
- S4: report the count at the ≥10-token cut (cross-check the "11 groups" claim).

## Quality gates

- Direction locked; reversal → NULL with prominence.
- All strings/counts from quran-text/quran-no-tashkeel.json; orders from data/revelation-order.csv; no values from memory.
- Verdict ∈ {CONFIRMED, NULL, CONFIRMED-BUT-MEANINGLESS}.

## Files

- This pre-reg (SHA-256 self-locked; embedded in scripts/h-new-2350.py, runtime-verified)
- scripts/h-new-2350.py · csv/h-new-2350.json · h-new-2350-verse-twin-chronology.md
