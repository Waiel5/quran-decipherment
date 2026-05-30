---
finding: H-NEW-2450
title: Adjacent near-verbatim reprise — corpus census + adjacency-excess / genre-concentration tests
type: pre-registration
date: 2026-05-30
author: Waiel Al-Shujaa
seed: 20260509
nperm: 10000
status: LOCKED-BEFORE-INFERENCE
---

# H-NEW-2450 — Pre-registration: the ADJACENT NEAR-VERBATIM REPRISE

## 0. Position in the repetition scale-ladder

The project's repetition findings climb a ladder of repeated-material rungs:

- **H-NEW-2100 / 2140** — mutashābihāt / verse-twin network (exact + near, any distance).
- **H-NEW-2310** — refrain / exact-repeated-verse census (byte-exact strings appearing ≥2×) + spacing-regularity.
- **H-NEW-2350** — cross-surah EXACT-verse twins → same-period (chronology) phenomenon.
- **H-NEW-2380** — cross-surah NEAR-twins (token edit 1–2, ≥8 tokens, **non-adjacent**) → same-period; edits are rhyme-driven fāṣila re-tuning.
- **Q094-F-01** (§10.118) — discovered Q94:5–6 (*fa-inna maʿa al-ʿusri yusrā / inna maʿa al-ʿusri yusrā*) is the corpus-tightest ADJACENT couplet: char-edit 1, the SOLE adjacent same-surah pair differing by a single leading fāʾ; 0 exact-verbatim adjacencies; edit-2 runners-up {Q74:19-20, Q75:34-35, Q82:17-18, Q102:3-4}.

**The rung this finding formalises:** the ADJACENT near-verbatim reprise — a verse immediately echoed (at position i+1) with minimal change. H-NEW-2310 (byte-exact) MISSES Q94:5-6 (the one-fāʾ delta); H-NEW-2350/2380 covered EXACT and NEAR but explicitly **excluded adjacency** (they are cross-surah). This finding builds the dedicated corpus census of the (i, i+1) rung — the full edit-distance distribution over every adjacent verse-pair, the low-edit roster with coordinates, the edit-2/3 differing-token taxonomy, and two locked inferential tests.

## 1. Definitions (LOCKED)

### 1.1 Rules-tuple
`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` — project default.

### 1.2 Adjacency
An **adjacent verse-pair** is (verse i, verse i+1) where BOTH verses belong to the SAME surah, in canonical order. Cross-surah boundary transitions (the 113 surah-to-surah junctions) are EXCLUDED from the adjacency census (the reprise is a within-surah device; the cross-surah rung is H-NEW-2350/2380). There are 6,122 within-surah adjacent pairs (= 6,236 verses − 114 surahs).

### 1.3 Tokenization (the H-NEW-2380 waqf lesson — LOCKED)
The `quran-no-tashkeel.json` text carries Quranic waqf / pause / codex glyphs (U+06D6–U+06DC, U+06DE rub-el-hizb, U+06E9 sajda place, and the U+06DF–U+06ED annotation block) as **standalone glyph-tokens** — recitation/codex annotations, NOT lexical words. These are STRIPPED before tokenizing (NFC-normalise, then drop every codepoint in the locked PAUSE set, then whitespace-split). This is the same instrument refinement that made 2:162≡3:88 exact in H-NEW-2380.

PAUSE set (locked): the 25 codepoints U+06D6, U+06D7, U+06D8, U+06D9, U+06DA, U+06DB, U+06DC, U+06DD, U+06DE, U+06DF, U+06E0, U+06E1, U+06E2, U+06E3, U+06E4, U+06E5, U+06E6, U+06E7, U+06E8, U+06E9, U+06EA, U+06EB, U+06EC, U+06ED.

### 1.4 Edit distance (TWO levels — both LOCKED)
For each adjacent pair (i, i+1) with lexical token-lists A, B:
- **Token-level edit distance** `t_ed`: Levenshtein over the token sequences (unit cost, sub/ins/del).
- **Char-level edit distance** `c_ed`: Levenshtein over the concatenated character strings (tokens joined with no separator — matches Q094-F-01 Arm B, the `.replace(' ','')` convention).

Both are reported for every pair. The **char-level** distance is the PRIMARY ranking metric (it is the one on which Q094-F-01 established the global minimum; it discriminates one-letter connective deltas, which token-edit collapses to 1 regardless of letter count).

### 1.5 Substantive filter
A pair is **substantive** if BOTH verses have ≥ 3 lexical tokens (matches Q094-F-01 Arm B `SUB=3`; excludes muqaṭṭaʿāt-only and 1–2-word verses whose tiny edit distances are not "reprise"). The census reports both the full 6,122-pair distribution AND the substantive subset; all inferential tests use the substantive subset.

### 1.6 "Low-edit reprise" roster threshold
Reported roster = every substantive adjacent pair with `c_ed ≤ 6` (descriptive; this band was chosen from the descriptive histogram shape to capture the visibly-isolated low tail before it merges into the bulk — it is a REPORTING bucket, not a test threshold). The locked TEST statistic (below) uses an a-priori band, not this roster cutoff.

## 2. Pre-registered hypotheses (DIRECTION-LOCKED, family of k=2, Bonferroni α = 0.05/2 = 0.025)

### H1 — ADJACENCY-EXCESS (PRIMARY)
**Locked claim:** the Quran's actual canonical verse-order places near-identical verses ADJACENT more than chance. Operationally: the COUNT of substantive adjacent pairs with `c_ed ≤ 3` in the true order EXCEEDS the count obtained when the within-surah verse sequence is randomly shuffled.

- **Test statistic** `N_low` = number of substantive within-surah adjacent pairs with `c_ed ≤ 3`. (Band `≤3` locked a priori: it is the closed low tail = edit-1 ∪ edit-2 ∪ edit-3; it is fixed before the null is run and is NOT the ≤6 reporting roster.)
- **Null (PRIMARY):** for each surah independently, randomly permute the order of its verses (a within-surah derangement), then recompute `N_low` over the shuffled adjacent pairs. This PRESERVES each surah's exact multiset of verses, its verse count, its length profile and its genre — it isolates "did the composer place the reprise members next to each other" from "this surah happens to be uniformly short." 10,000 permutations, seed 20260509.
- **Secondary null (robustness):** global verse-sequence shuffle (all 6,236 verses permuted, re-segmented into the original 114 surah-length blocks), 10,000 perms, seed 20260509+1. Reported but NOT the primary inferential basis (it does not control surah-internal length homogeneity).
- **Direction LOCKED:** `N_low(observed) > mean(N_low(null))`. One-sided p = (#{null ≥ obs} + 1)/(nperm + 1).
- **PASS:** observed strictly greater AND p < 0.025 (Bonferroni).
- **REVERSED → NULL with full prominence:** if `N_low(observed) ≤ mean(N_low(null))`, this is a pre-commit violation, published as NULL. (Plausible reversal: refrains/reprises may be DISPERSED rather than adjacent — cf. H-NEW-2310's Q55 *fa-bi-ayyi ālāʾ* which is anti-adjacent by design, and H-NEW-2420's Q55 z=−5.32 ordering-by-dispersion. If reprise-members are systematically spaced, adjacency would be DEPLETED.)

### H2 — GENRE-CONCENTRATION (SECONDARY)
**Locked claim:** the adjacent-reprise device concentrates in the short-mufaṣṣal / eschatological genre (the juzʾ-ʿamma register, Q78–114). Operationally: the per-surah RATE of low-edit adjacencies (`c_ed ≤ 3` substantive pairs ÷ that surah's substantive adjacent-pair count) is HIGHER for juzʾ-ʿamma surahs (mushaf id 78–114) than for the rest (id 1–77).

- **Test statistic:** Δ = mean per-surah low-edit RATE (juzʾ-ʿamma) − mean per-surah low-edit RATE (rest). Surahs with 0 substantive adjacent pairs are excluded from the rate computation.
- **Null:** 10,000 label-permutations — shuffle the juzʾ-ʿamma / rest label across surahs (preserving the count of juzʾ-ʿamma surahs), recompute Δ. Seed 20260509+2.
- **Direction LOCKED:** Δ(observed) > 0 (juzʾ-ʿamma higher). One-sided p = (#{null ≥ obs}+1)/(nperm+1).
- **PASS:** Δ > 0 AND p < 0.025 (Bonferroni).
- **REVERSED → NULL with full prominence** if Δ ≤ 0.

## 3. Census deliverables (descriptive — enumeration, not inference)
1. Full `c_ed` and `t_ed` histograms over all 6,122 adjacent pairs and over the substantive subset.
2. The complete `c_ed ≤ 6` low-edit roster with coordinates (surah:verse-verse), both texts, both distances, surah region (Meccan/Medinan), genre tag.
3. The edit-1 singleton, the edit-2 family, the edit-3 family — each with their aligned differing-token patterns.
4. Differing-token taxonomy linking the H-NEW-2380 mechanisms: (a) connective/particle prepend (ثم / و / ف / leading إن↔فإن); (b) rhyme-driven final-word swap (fāṣila re-tuning, conserving the proposition); (c) parallel-template noun/verb swap (the "wa-idhā X Y'at" cosmic-collapse cascades, the antithetical destiny pairs); (d) pronoun/inflection shift. Counts per mechanism.

## 4. MW protections
- **MW-1 (instrument-prior):** edit distances + adjacency + PAUSE-set + bands defined in §1 BEFORE running.
- **MW-2 (corpus-prior):** 10,000-perm permutation nulls.
- **MW-3 (alternative-models):** TWO nulls for H1 (within-surah shuffle PRIMARY + global shuffle robustness); TWO edit metrics (char PRIMARY + token).
- **MW-5 (replication):** H1 replicated at a second seed (20260509+10).
- **MW-6 (instrument-control):** the substantive ≥3-token filter is itself a control against muqaṭṭaʿāt / ultra-short-verse artefacts; H2 label-shuffle is the genre control.
- **MW-7 (post-hoc cap):** the ≤6 roster band is descriptive-only; all inference uses the a-priori ≤3 band.

## 5. Failure / honesty conditions
- Reversed direction on either H is a pre-commit violation → NULL with full prominence (no massaging, no silent re-lock).
- If the within-surah-shuffle PRIMARY null and the global-shuffle robustness null DISAGREE in sign, the within-surah (conservative) result governs the verdict and the disagreement is reported prominently.
- Genre is out-of-scope as a theological claim; H2 is a register/length-class observation only.

## 6. Anti-hallucination
Every count, coordinate, and Arabic string is computed from `quran-text/quran-no-tashkeel.json` at runtime. Revelation/region tags from `data/revelation-order.csv`. No value is asserted from memory.

Seed 20260509. 10,000 permutations. This file is SHA-256-locked; the run script embeds the hash and fails fast on mismatch.
