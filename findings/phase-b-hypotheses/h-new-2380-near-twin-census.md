---
finding: H-NEW-2380
title: Cross-surah NEAR-twin verse census (≤2 token edits) + revelation-order proximity
date: 2026-05-29
phase: B+
seed: 20260509
nperm: 10000
prereg_sha256: 42828931e11e5d432a1b570adb98071c1a58f053ccfcfeefdfc4b219a24ae8b9
verdict: CONFIRMED (direction locked "closer than random")
extends: H-NEW-2350 (exact twins), H-NEW-2310 (refrain census)
---

# H-NEW-2380 — The "almost the same verse": near-twin verse census and its chronology

**Verdict: CONFIRMED.** Direction was locked to "near-twin surah-pairs are revealed CLOSER in revelation order than random," matching the exact-twin result H-NEW-2350. Pre-reg SHA-256 `42828931e11e5d432a1b570adb98071c1a58f053ccfcfeefdfc4b219a24ae8b9`, seed 20260509, 10000 permutations, runtime-verified (fail-fast assert passed).

This is **compositional repetition with variation in one canonical text** — the slight variants of recurring formulae across surahs. It is NOT the variant-readings (qirāʾāt) debate and NOT abrogation (naskh); we measure where, in the single Hafs-Kūfan corpus, near-identical verse formulae recur across surah boundaries, and when those surahs were revealed.

## Instrument

- **Text:** `quran-text/quran-no-tashkeel.json`.
- **Tokenization (critical honesty point):** the no-tashkeel file still carries Quranic **waqf / pause marks** (U+06D6–U+06DC, U+06DE rub-el-ḥizb, U+06E9 sajda, etc.) as standalone whitespace-separated glyphs. These are codex/recitation annotations, **not lexical words**, and were stripped before tokenizing. Disclosed consequence: 2:162 and 3:88 — which the raw H-NEW-2350 tokenization saw as distinct (a lone ۖ between them) — are **EXACT lexical twins** once the pause-mark is removed; the exact-after-strip ≥8-token cross-surah twin count is **17 surah-pairs**, a small refinement of the instrument over 2350's raw figure.
- **Edit distance:** true token-level **Levenshtein** (unit-cost substitution / insertion / deletion), capped with early-exit. Cross-surah only; same-surah repetition is the domain of H-NEW-2310/2330.
- **Near-twin (locked):** a cross-surah verse-pair with **1 ≤ edit ≤ k = 2** and both verses **≥ L = 8 lexical tokens**. Distance 0 (exact after strip) is excluded — it is the exact-twin domain (H-NEW-2350).
- **k, L calibration:** k=2 and L=8 were fixed transparently BEFORE locking direction (instrument design, MW-1), to capture "almost the same verse" without admitting recognizably-different verses sharing a stock phrase. The k∈{1,2,3} × L∈{6,8,10} ladder is reported as robustness.

## The census — 32 near-twin verse-pairs

**17 at edit-distance 1, 15 at edit-distance 2 → 32 verse-pairs spanning 31 distinct surah-pairs.** (For reference, the exact-after-strip set is 17 surah-pairs at L≥8.) Full table with aligned differing tokens is in `csv/h-new-2380.json`. Selected exemplars:

| d | pair | Δrev | edit (A→B) |
|:-:|:--|:-:|:--|
| 1 | 39:72 ≡̃ 40:76 | **1** | del `قيل` — "[it is said] enter the gates of Hell…" |
| 1 | 16:43 ≡̃ 21:7 | **3** | del `من` — *wa-mā arsalnā [min] qablika illā rijālan* (ask the people of remembrance) |
| 1 | 15:11 ≡̃ 43:7 | 9 | sub `رسول → نبي` — "no **messenger/prophet** came to them but they mocked" |
| 1 | 3:182 ≡̃ 22:10 (also 8:51) | 14/15 | sub `أيديكم → يداك` — "that for what **your hands / your two hands** sent ahead" |
| 1 | 30:37 ≡̃ 39:52 | 25 | sub `يروا → يعلموا` — "do they not **see / know** that God extends provision" |
| 1 | 39:48 ≡̃ 45:33 | 6 | sub `كسبوا → عملوا` — "the evils of what they **earned / did**" |
| 2 | 21:92 ≡̃ 23:52 | **1** | sub `إن→وإن`, `فاعبدون → فاتقون` — "this is your one community… so **worship Me / fear Me**" |
| 2 | 2:49 ≡̃ 7:141 | 48 | sub `نجيناكم→أنجيناكم`, `يذبحون → يقتلون` — Pharaoh "**slaughtering / killing** your sons" |
| 2 | 7:81 ≡̃ 27:55 | 9 | sub `إنكم→أئنكم`, `مسرفون → تجهلون` — Lot's people "transgressors / ignorant" (rhyme) |
| 2 | 6:21 ≡̃ 10:17 | 4 | sub `ومن→فمن`, `الظالمون → المجرمون` — "the **wrongdoers / criminals** do not prosper" (rhyme) |
| 2 | 15:19 ≡̃ 50:7 | 20 | sub `شيء→زوج`, `موزون → بهيج` — "We grew in it of every **measured thing / delightful pair**" (rhyme) |

## The differing-token patterns (the prize)

Across the 32 pairs, the edits fall into a small, highly structured set — and they are NOT random word noise. Four mechanisms dominate:

1. **Connective/particle alternation (و / ف / ∅, إن / وإن / إلا).** The single most common one-edit type. *fa-* ↔ *wa-* ↔ ∅ openers (6:21 `ومن`↔`فمن`; 84:25 `لهم`↔`فلهم`; 16:29 `فادخلوا`↔`ادخلوا`), and the *inna / wa-inna / illā* particle swap (3:51↔19:36 `إن`↔`وإن`; 41:8↔84:25 `إن`↔`إلا`). These are *seam-fitting* edits: the same clause is re-anchored to its new syntactic context.

2. **Rhyme-driven final-word substitution (fāṣila swap).** When a recurring formula lands in a surah with a different rhyme, the **last word** is swapped to fit: `الظالمون`↔`المجرمون` (6:21↔10:17), `مسرفون`↔`تجهلون` (7:81↔27:55), `موزون`↔`بهيج` (15:19↔50:7), `فاعبدون`↔`فاتقون` (21:92↔23:52). This is iʿjāz al-fawāṣil operating *across* surahs — the body of the verse is conserved, the cadence-word is re-tuned. This is the cross-surah analogue of the within-surah anti-twin lock (content conserved, rhyme adapted).

3. **Near-synonym lexical substitution.** Theologically equivalent verbs/nouns swapped: `رسول`↔`نبي` (messenger/prophet, 15:11↔43:7), `يروا`↔`يعلموا` (see/know, 30:37↔39:52), `كسبوا`↔`عملوا` (earn/do, 39:48↔45:33), `يذبحون`↔`يقتلون` (slaughter/kill, 2:49↔7:141). The Pharaoh-deliverance pair 2:49↔7:141 is the longest near-twin (19/20 tokens, 2 edits) and a textbook case: *najjaynākum* ↔ *anjaynākum* (same root, II vs IV form) + *yudhabbiḥūna* ↔ *yuqattilūna*.

4. **Single-content-word insertion/deletion and pronoun/inflection shift.** A verse gains or loses one word in a new context: `قيل` "it is said" prepended (39:72↔40:76), `واستوى` "and matured" added to the prophet-coming-of-age formula (12:22 Yūsuf ↔ 28:14 Mūsā), `قال` dropped (26:24↔44:7). Pronoun/clitic shifts: `أيديكم`↔`يداك` (your-pl-hands / your-sg-two-hands, addressing a crowd vs an individual), `يتمنوه`↔`يتمنونه`.

Raw taxonomy tally (heuristic classifier, descriptive only — some "lexical substitution" labels above are connective or rhyme edits the heuristic under-split): lexical/epithet substitution 22, single-word ins-del 11, connective ins-del 4, rhyme/final-word swap 4, connective swap 3, pronoun/inflection 3.

**Interpretation:** near-twins are *the same composed clause re-deployed in a new sūra*, adjusted by (a) a connective to fit the new syntactic seam, (b) the final word to fit the new rhyme, or (c) a near-synonym/pronoun to fit the new addressee. The conserved core is the proposition; the edits are *contextual fitting*. This directly extends the H-NEW-2350 / H-NEW-2310 picture of formulaic cross-surah repetition.

## Primary result — near-twins are a same-period phenomenon

- **D_obs = 21.10** revelation-order units (mean over 31 distinct near-twin surah-pairs) vs **size-matched random-pair null 38.29**, one-sided **p = 0.0001**. → **CONFIRMED** on the locked direction.
- **Nöldeke robustness:** D_obs = **13.29** (same direction, even tighter under the Nöldeke chronology).
- **Period concordance:** **27 / 31** near-twin surah-pairs are same-period (both Meccan or both Medinan) vs random null, **p = 0.0028**.
- **k/L ladder (all 9 cells same direction, all D_obs ≈ 17–24 ≪ null ≈ 38):** the effect is stable from L6 to L10 and k1 to k3; it is not an artefact of the chosen cutoff.

## Near vs exact — exact twins are directionally tighter, same regime

| set | n surah-pairs | mean rev-distance | p (closer) |
|:--|:-:|:-:|:-:|
| exact (after strip, L≥8) | 17 | **15.18** | 0.0001 |
| near (k≤2, L≥8) | 31 | **21.10** | 0.0001 |
| random null | — | 38.29 | — |

**Exact twins are numerically MORE revelation-clustered than near-twins (15.18 < 21.10), but the gap is NOT statistically significant** (label-permutation contrast on the two distance distributions: p = 0.15). Both sit in the same **same-period regime**, decisively below the random expectation of ~38. The honest reading: relaxing identity to ≤2 edits **does not break** the same-period signal; it only slightly loosens it, consistent with a monotone "more conserved ⇒ tighter chronology" gradient that is suggestive but not significant at this n.

The widest-spaced near-twins are mostly the **Pharaoh/Lot/cosmic-sign Meccan narrative formulae** redeployed across distant Meccan sūras (2:49↔7:141 Δ48; 7:80↔29:28 Δ46; 6:117↔68:7 Δ53; 84:25↔95:6 Δ55) — the stock-narrative and stock-doxology phrases that recur throughout the Meccan period regardless of exact sūra date. The tightest (Δ1–6) are adjacent-revelation formula pairs: 39:72↔40:76 (Hell-gates, Δ1), 21:92↔23:52 (one-community creed, Δ1), 16:43↔21:7 (ask-the-people-of-remembrance, Δ3).

## Integration

- **Extends H-NEW-2350** (§10.100): the same-period clustering of repeated verses survives relaxation from exact to ≤2-edit near-identity. Repeated *and near-repeated* verses track the chronological timeline, not the positional mushaf FR-architecture (pillar law #2 — chronology ⊥ codex-position).
- **Extends H-NEW-2310** (§10.93): adds the *variation* layer to the refrain census — not just verbatim repeats but their fitted variants.
- **Cross-surah iʿjāz al-fawāṣil:** the rhyme-driven final-word swaps (mechanism 2) are the cross-surah face of the within-surah content⊥rhyme anti-twin lock (r = −0.86, [[h-new-730-content-rhyme-anticorrelation]]): the proposition is conserved while the fāṣila is re-tuned to the host sūra's cadence.
- **Classical anchor:** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 60 (*tikrār al-āyāt wa-l-qiṣaṣ*) names verse-repetition as a deliberate device; the near-twin census makes its *adaptive* form quantitative.

## Honest limits

- **n is small** (31 near-twin surah-pairs); the near-vs-exact tightness gap is not significant. The same-period *direction* is robust (p=0.0001, stable across k/L ladder and both chronologies); the *exact-tighter-than-near* claim is directional only.
- Revelation order itself is a scholarly reconstruction (Tanzil Egyptian Standard primary, Nöldeke robustness); both give the same direction, but neither is observational ground truth.
- The edit-type taxonomy is a descriptive heuristic; the *alignments* (which tokens differ) are exact and machine-verified, but the *labels* are coarse (the table in this document hand-corrects several heuristic mislabels). The JSON carries the raw alignments for independent re-classification.
- k=2 is a deliberate "near" cutoff; at k=3 the census doubles and begins admitting verses that share a formula but read as distinct — the L8/k2 cell is the honest "almost the same verse" set.

## Files
- `prereg-h-new-2380-near-twin-census.md` (SHA-256 self-locked, embedded, runtime-verified)
- `scripts/h-new-2380.py`
- `csv/h-new-2380.json` (full 32-pair census with token-level edit alignments + ladder + taxonomy)
- `h-new-2380-near-twin-census.md` (this file)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
