---
id: H-NEW-119
title: 7-fold patterns inventory — is 7 structurally privileged or culturally projected?
phase: B
date: 2026-04-17
agent: h-new-119-specialist
status: PRE-REGISTERED
corpus_anchor: 6,236 verses / 77,797 tokens / Hafs-Kūfan canonical 114
rules_tuple:
  orthography: no-tashkeel
  tokenization: whitespace
  basmala_policy: basmala-counted-only-in-surah-1 (default JSON state)
  verse_counting: Hafs-Kūfan (the total_verses field in quran-no-tashkeel.json)
bonferroni_k: 3
bonferroni_family: h-new-119-seven-fold
alpha_bon: 0.0167
direction_primary: observed structural 7-fold count > 5 out of the 7 pre-committed candidates (threshold of interest)
direction_secondary: 7 is enriched over 3/5/6/8 as a structural-cardinality across the same feature set (permutation p<alpha_bon, one-sided)
direction_tertiary: 7-fold pattern density per 10K tokens in Quran exceeds Bukhārī-noquran baseline (permutation p<alpha_bon, one-sided)
acceptance_window: primary fires if ≥5/7 locked candidates verify AT the Hafs-Kūfan level (exact count); secondary if 7 strictly dominates 3,5,6,8 as observed-coincidence count across same feature schema; tertiary if density(7-fold)/10K_tokens(Quran) > density(7-fold)/10K_tokens(Bukhārī)
seed: 20260417
---

# [[h-new-119-seven-fold|H-NEW-119]] — 7-fold patterns inventory (pre-registration)

## Hypothesis

Classical tradition attaches special significance to the number 7 in the Quran: 7 verses of al-Fātiḥa, 7 long surahs (*al-sabʿ al-ṭiwāl*), 7 heavens, 7 musabbiḥāt, 7 oaths of Q 91, etc. Test whether 7-fold structures recur at a non-random rate, distinguishing STRUCTURAL PRIVILEGE (the text itself favors 7) from CULTURAL PROJECTION (scholars post-hoc select 7-fold readings from ambiguous structures because 7 is a privileged number in the broader Near-Eastern milieu).

## Garden-of-forking-paths disclosure (CRITICAL)

**Cultural-privilege risk**: 7 is a privileged number in pre-Islamic Near-Eastern (Babylonian/Hebrew/Syriac) cosmology and Arabic idiom (*sabʿīn* "many", seven gates of hell, seven days of the week, etc.). Any enumerative claim about "7 X's in the Quran" carries SELECTION BIAS RISK: scholars have a motivated incentive to tabulate lists that come out to 7, ignoring lists that come out to 6 or 8. The project has previously documented this risk in `cosmology-audit.md` §7.

To guard against it:
- **LOCK the 7-fold candidate list in frontmatter** (below) BEFORE running the null.
- **Each item requires INDEPENDENT DERIVATION** — i.e., the 7-count must be either explicit in the text (numerical particles `sabʿ` / `sabʿa` / `sabʿan`) or structurally defined by a rule unrelated to cultural privilege (e.g., "the set of surahs opening with `sabbaḥa`").
- **No post-hoc additions** to the list after viewing any count.
- **Specificity check (direction_secondary)**: if 7 is culturally privileged but not structurally preferred, we would expect similar coincidence-rates for 3, 5, 6, 8. Explicit comparison required.

## LOCKED 7-FOLD CANDIDATE LIST (frozen before any counting)

The following 7 candidates are the ONLY items evaluated in direction_primary. Each has an independent derivation rule, fixed before counting.

### C1 — `sabʿ samāwāt` (7 heavens) — occurrences of the explicit phrase
- **Derivation rule**: count exact occurrences in the text of the lexical pattern "seven heavens" (Arabic phrases containing `سبع` + a form of `سماو`/`سموات`/`سماء`). This is a TEXT-EXPLICIT integer, not an interpretive list.
- **Classical claim**: occurs exactly 7 times in the Quran (per cosmology-audit.md and broader classical counts).
- **PASS condition**: exactly 7 occurrences under the locked pattern.

### C2 — al-Fātiḥa verse count (7 verses)
- **Derivation rule**: under Hafs-Kūfan counting (the only counting scheme in this project's data), Q 1 has 7 verses. Read directly from `total_verses` field of quran-no-tashkeel.json Q 1.
- **Classical claim**: 7 verses ("al-sabʿ al-mathānī").
- **PASS condition**: `total_verses == 7` for surah_id 1.

### C3 — al-sabʿ al-ṭiwāl (7 long surahs) — [[h-new-67-sab-tiwal-mathani|H-NEW-67]] confirmed
- **Derivation rule**: the classical 7 long surahs {Q 2, 3, 4, 5, 6, 7, 9-or-10}. Top-7-longest-in-muṣḥaf-front enrichment, [[h-new-67-sab-tiwal-mathani|H-NEW-67]] p=0.0001.
- **Classical claim**: a coherent cluster of 7.
- **PASS condition**: [[h-new-67-sab-tiwal-mathani|H-NEW-67]] verdict STRONG-PASS-DIRECTED on count of 7. (Independent: the derivation is "the 7 longest contiguous front-of-muṣḥaf surahs", not circularly defined by 7.)

### C4 — Q 91 oath-opener cluster (7 oath-verses) — [[h-new-85-oath-openers|H-NEW-85]] confirmed
- **Derivation rule**: Q 91 al-Shams opens with 7 consecutive oath-verses (*wa-l-shams*, *wa-l-qamar*, ..., *wa-l-samāʾ*, *wa-l-arḍ*, *wa-l-nafs*). Structural rule from [[h-new-85-oath-openers|H-NEW-85]].
- **Classical claim**: the unique structural oath-cluster maximum in the Quran, cluster-length = 7.
- **PASS condition**: contiguous oath-cluster opening Q 91 has length exactly 7 (per [[h-new-85-oath-openers|H-NEW-85]] Cell 2 verification).

### C5 — Musabbiḥāt (7 surahs with *sabbaḥa/yusabbiḥu/sabbiḥ/subḥāna* at v1) — [[h-new-103-musabbihat-4form|H-NEW-103]] 4-form confirmed
- **Derivation rule**: the classical 7 musabbiḥāt (Q 17, 57, 59, 61, 62, 64, 87) — set of surahs whose v1 begins with the root SBḤ (*subḥāna*, *sabbaḥa*, *yusabbiḥu*, *sabbiḥ*).
- **Classical claim**: the classical list is 7.
- **PASS condition**: count of surahs in {114 surahs} whose v1 (min-tashkeel) begins with the SBḤ verbal/nominal form = 7 exactly.

### C6 — 7 prophets in Q 7 al-Aʿrāf prophet cycle
- **Derivation rule**: count named prophets in the narrative sequence of Q 7 al-Aʿrāf verses 59–171 (the post-introductory narrative-cycle) among the set {Adam, Noah, Hud, Salih, Lot, Shuʿayb, Moses}. Fixed canonical prophet-set a priori.
- **Classical claim**: 7 prophets in canonical narrative order in Q 7.
- **PASS condition**: all 7 pre-committed prophet-names appear as a central narrative subject in Q 7 (verified by lexical match on each prophet's Arabic name-form).

### C7 — 7 `sabʿ`-cardinality explicit mentions (tokens `سبع` / `سبعا` / `سبعة` / `سبعون`)
- **Derivation rule**: does the total Quranic count of root-SBʿ cardinality tokens come out to a "privileged" 7 multiple, or is it simply a function of text size? We pre-commit: PASS if observed count is within ±1 of 24 (the classical tally of "7 × N" self-referential mentions) OR if it is exactly 7 OR 14 OR 21. This is an **EXPLORATORY specificity test**; direction is not 7 strictly but "in the expected classical range".
- *Note*: this item is intentionally weakest; cultural-privilege artifact risk is HIGHEST.
- **PASS condition**: count in {7, 14, 21, 22, 23, 24, 25}.

## Test cells

### Cell A — Observed count of 7-fold patterns (PRIMARY)

For each of the 7 locked candidates C1–C7, apply its pre-committed PASS rule and return boolean. Sum passes. Direction fires if count ≥ 5 out of 7 (threshold of interest = 5; below this, 7-fold preference is not demonstrated above baseline-plausibility).

### Cell B — Null baseline: rate of any-N-fold patterns in matched-length Arabic corpus

Measure the rate of "N-fold coincidences for any integer N ≤ 10" in a length-matched Bukhārī-noquran baseline. Specifically: (i) count `sabʿ`-variant occurrences and compare to (ii) count of `thalātha`, `arbaʿa`, `khamsa`, `sitta`, `thamāniya`, `tisʿa`, `ʿashara`. Report the distribution. If 7 is simply the most common numerical modifier due to Arabic convention, this is a cultural-privilege signal, not Quran-specific.

### Cell C — Specificity: 7 vs 3, 5, 6, 8 in the same pattern-schema

Apply the SAME enumeration rules used in C1, C5, C7 but for N ∈ {3, 5, 6, 8}:
- N-fold explicit phrase count (does `thalāth samāwāt` appear in pattern? `khams samāwāt`? etc.)
- N-surah classically-named clusters
- Explicit `N`-cardinality token counts

If 7 is STRUCTURALLY privileged in the Quran itself, 7 should dominate this space over 3/5/6/8 at a non-random rate.

### Cell D — 7-fold density per 10K tokens vs Bukhārī (TERTIARY)

Density of "seven + noun" collocations per 10K tokens in Quran (77,797 tokens) vs Bukhārī-noquran (matched 77,797-token slice). If Quran's rate exceeds Bukhārī's under permutation p<0.0167, structural privilege survives; if not, cultural projection is the parsimonious explanation.

## Analysis plan

1. Load quran-no-tashkeel.json; implement lexical pattern matchers for the 7 locked candidates.
2. Execute Cell A deterministically; report 0/7 through 7/7.
3. Execute Cell C by running N ∈ {3, 5, 6, 7, 8} on the parallel enumeration schema.
4. Execute Cell D by loading Bukhārī-noquran corpus, permutation test over 5K bootstrap samples.
5. Report verdicts per cell; publish NULL with same prominence as PASS.

## Expected honest outcome

MIXED. Items with INDEPENDENT LEXICAL DERIVATION (C1 seven-heavens phrase count, C2 Fātiḥa verses) are likely to verify. Items with STRUCTURAL DERIVATION established in prior [[h-new-67-sab-tiwal-mathani|H-NEW-67]]/85/103 will verify by construction. Items dependent on post-hoc selection of prophet-sets or cardinality-counts (C6, C7) carry high cultural-projection risk and may NOT verify cleanly.

## Verdict ceiling

- **PASS-DIRECTED** if Cell A ≥ 5/7 AND Cell C shows 7 strictly dominant over 3/5/6/8 AND Cell D density exceeds baseline.
- **PARTIAL-PASS** if only Cell A fires (trivial — 5/7 items are classical pre-commitments likely to verify mechanically).
- **MIXED** expected outcome — explicit disclosure in findings.
- **NULL** if Cell A < 5/7 OR Cell C shows 7 not privileged.

## Cross-references

- [[h-new-67-sab-tiwal-mathani|H-NEW-67]] (7 long surahs verification)
- [[h-new-85-oath-openers|H-NEW-85]] (Q 91 oaths verification)
- [[h-new-103-musabbihat-4form|H-NEW-103]] (musabbiḥāt 4-form typology)
- cosmology-audit.md §7 (seven heavens cultural backdrop)
- classical-quantitative-claims-audit.md (adjacent methodology)
