# Pre-registration — H-NEW-2380: Cross-surah NEAR-twin verse census (≤k token edits) and revelation-order proximity

**Pre-registered by:** Waiel Al-Shujaa
**Date:** 2026-05-29 (locked BEFORE the confirmatory computation; calibration of k/min-length disclosed below)
**Seed:** 20260509 · **Permutations:** 10000
**Rules-tuple:** (no-tashkeel orthographic verse-string, NFC + **waqf/pause-mark-stripped** + whitespace-normalized lexical word-tokens, Hafs-Kūfan; revelation order = Tanzil Egyptian Standard `revelation_order`, primary; Nöldeke = robustness)

## Background and relation to H-NEW-2350

H-NEW-2350 (§10.100) established that **EXACT cross-surah verse-twins are a same-period phenomenon**: when the identical verse appears in two surahs, those surahs are revealed close together in time (mean within-group revelation-distance 16.47 vs size-matched random null 38.17, p=0.0002). H-NEW-2310 (§10.93) censused exact repeated strings.

This pre-reg **extends EXACT twins to NEAR twins**: the "almost the same verse" pairs — slight variants of recurring formulae across surahs (pronoun shifts, connective swaps, name/epithet substitutions, single-word insertions). The question: does the same-period clustering survive when we relax exact identity to a small token-level edit distance? And **are near-twins MORE or LESS revelation-clustered than exact twins?**

**This is one canonical text.** Near-twins are *compositional repetition with variation* (a rhetorical/redactional feature), NOT variant readings (qirāʾāt) and NOT the abrogation (naskh) debate. We make no claim about textual transmission; we measure where, in the single Hafs-Kūfan corpus, near-identical verse formulae recur across surahs.

## Instrument: token-level edit distance (locked)

- **Tokenization (CRITICAL honesty point):** the `quran-no-tashkeel.json` text still carries Quranic **waqf/pause marks** (U+06D6–U+06DC ARABIC SMALL HIGH …, U+06DE RUB EL HIZB, U+06E9 PLACE OF SAJDAH, etc.) as standalone whitespace-separated glyphs. These are codex/recitation annotations, **not lexical words**. They are STRIPPED before tokenization. (Disclosed consequence: 2:162 and 3:88, which H-NEW-2350 saw as distinct, are EXACT lexical twins once the lone ۖ pause-mark is removed; the exact-after-strip ≥8-token cross-surah twin count is 17, vs 2350's raw 15. This is a refinement of the instrument, reported transparently.)
- **Edit distance:** classical token-level **Levenshtein** (unit cost for substitution / insertion / deletion), computed with a cap = k and early-exit. Symmetric. Cross-surah only (a verse is never compared to another verse in the same surah; same-surah repetition is H-NEW-2310/2330's domain).
- **NEAR-twin definition:** a cross-surah verse-pair (a,b) with **1 ≤ edit_distance(a,b) ≤ k** where **both verses have ≥ L lexical tokens**. Distance 0 (exact after pause-strip) is excluded — it belongs to the exact-twin set (H-NEW-2350), not the near-twin set.

## Pre-locked parameters (k, L)

Calibrated transparently BEFORE locking direction (instrument design, MW-1), using a no-direction exploratory pass:

- **k = 2** (≤2 token substitutions/insertions/deletions). Rationale: k=1 captures minimal variants (single pronoun/connective); k=2 captures the canonical "two-edit" formula variants; k=3 begins to admit pairs that are recognizably *different* verses sharing a stock phrase, diluting the "almost the same verse" intent. We lock k=2 as primary and report k=1 and k=3 as the robustness ladder.
- **L = 8 tokens** (verse length floor, both members). Rationale: matches H-NEW-2350's primary substantive-twin threshold (≥8); below 8 tokens a 2-edit distance is a large *fraction* of the verse and no longer "near-identical." Report L=6 and L=10 as robustness.

Exploratory pass (disclosed, no direction inspected): at L=8, k=2 the census is ~17 pairs at d=1 and ~15 at d=2. Confirmatory run recomputes from disk; these calibration figures are not the test.

## Unit of analysis

Near-twins are intrinsically **pairwise** (edit distance is a binary relation). The analysis unit is the **near-twin surah-pair**: each near-twin verse-pair (a∈S_i, b∈S_j, i≠j) contributes the unordered surah-pair {S_i, S_j}. Deduplicate surah-pairs (multiple verse-pairs linking the same two surahs count once for the distance test, but all verse-pairs are enumerated in the census). Revelation distance of a surah-pair = |revelation_order(S_i) − revelation_order(S_j)|.

## Primary hypothesis (direction LOCKED)

> **H1:** Cross-surah NEAR-twin surah-pairs link surahs revealed **CLOSE together** in revelation order — the observed mean revelation-distance over distinct near-twin surah-pairs is **SMALLER** than a size-matched random-surah-pair null (same direction as exact twins).
> Statistic: D_obs = mean over distinct near-twin surah-pairs of |revelation_order(S_i) − revelation_order(S_j)|.
> Null: draw the same number of distinct random surah-pairs (uniform over the 114·113/2 pairs), compute mean distance; 10000×, seed 20260509. One-sided p = fraction of null means ≤ D_obs.

**Direction is LOCKED to "closer than random."** If D_obs ≥ null mean (near-twins are NOT closer, or are farther), publish as **NULL / REVERSED with full prominence** → the finding becomes "near-twins, unlike exact twins, are NOT a same-period phenomenon," which is itself a prominent result.

## Secondary / descriptive (the prize: differing-token patterns)

- **S1 — full census** of all near-twin verse-pairs (k≤2, L≥8) with refs, token lengths, edit distance, the two verse texts, and the **differing-token alignment** (which tokens were substituted / inserted / deleted).
- **S2 — edit-type taxonomy:** classify each edit as one of {pronoun/clitic shift, connective/particle swap (و/ف/ثم, إن/وإن), name-or-epithet substitution, single-word insertion/deletion, morphological inflection (e.g., يقتلون↔يذبحون), rhyme-driven final-word swap, other}. Report the distribution. This is the core deliverable.
- **S3 — comparison to exact twins:** recompute D_obs on the exact-after-strip twin set (L≥8) with the IDENTICAL surah-pair null, and report whether near-twins are MORE or LESS revelation-clustered than exact twins (compare D_obs values and their nulls; descriptive, plus a permutation contrast).
- **S4 — period concordance:** fraction of near-twin surah-pairs that are same-period (Meccan/Medinan) vs a size-matched random-pair null.
- **S5 — Nöldeke robustness:** repeat H1 under `noldeke_order`.
- **S6 — k/L ladder:** report counts and D_obs at k∈{1,2,3} and L∈{6,8,10}.

## Quality gates

- Direction locked (H1 = closer); reversal → NULL with full prominence.
- Pre-reg SHA-256 self-locked, embedded in `scripts/h-new-2380.py`, runtime-verified (fail-fast).
- All strings/counts from `quran-text/quran-no-tashkeel.json`; orders from `data/revelation-order.csv`; nothing from memory.
- Edit distance computed honestly (true Levenshtein, pause-marks stripped, cross-surah only, d=0 excluded).
- Permutation null ≥10000, seed 20260509.
- NOT conflated with qirāʾāt / naskh; framed as compositional repetition in one text.
- Verdict ∈ {CONFIRMED, NULL, NULL-REVERSED, CONFIRMED-BUT-MEANINGLESS}.

## Files

- This pre-reg (SHA-256 self-locked; embedded + runtime-verified)
- `scripts/h-new-2380.py` · `csv/h-new-2380.json` · `h-new-2380-near-twin-census.md`
