---
id: H-NEW-163
title: All-surah dispersion ranking — refinement of H-NEW-155 Q 1 sui-generis claim
phase: B
status: REFINES (H-NEW-155 narrowed; genre-pattern discovered)
date: 2026-04-17
executed_by: team-lead (inline)
parent: H-NEW-155 (Q 1 sui-generis-liturgical CONFIRMED via specialist-b)
seed: 20260417
rules_tuple: (no-tashkeel; simple Arabic stemmer — rougher than QAC-STEM; dispersion = mean fraction of non-self surahs containing each surah's stems; all 114 surahs ranked)
bonferroni_k: 1
bonferroni_family: h-new-163-all-surah-dispersion
alpha_bon: 0.05
direction: descriptive ranking
verdict: REFINES
---

# [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] — All-surah dispersion ranking

## Motivation

[[h-new-155-q1-sui-generis|H-NEW-155]] claimed Q 1 al-Fātiḥa is SUI-GENERIS-LITURGICAL (dispersion 0.504 vs null 0.397, p=0.0013). This test rank-orders ALL 114 surahs under a (rougher-stemmer) dispersion metric to verify:
1. Does Q 1 sit uniquely at the top?
2. Do other classical "brief-creedal" surahs cluster with Q 1 in the high-dispersion regime?
3. What's at the opposite extreme?

## Method

For each stem in each surah, compute what fraction of the OTHER 113 surahs contain that stem. Average across all stems in the surah to get a dispersion score per surah.

**Stemmer caveat**: simple Arabic prefix/suffix stripping (not QAC-STEM). Numbers differ from [[h-new-155-q1-sui-generis|H-NEW-155]] quantitatively but ranking-order is expected to be similar.

## Top-10 highest-dispersion surahs

| Rank | Q | Name | Dispersion | N stems |
|:-:|:-:|---|---:|---:|
| 1 | 103 | al-ʿAṣr (Time) | 0.325 | 12 |
| 2 | 110 | al-Naṣr (Victory) | 0.325 | 17 |
| **3** | **1** | **al-Fātiḥa** | **0.304** | **23** |
| 4 | 109 | al-Kāfirūn (Disbelievers) | 0.284 | 12 |
| 5 | 62 | al-Jumuʿah (Friday) | 0.275 | 111 |
| 6 | 95 | al-Tīn (Fig) | 0.271 | 31 |
| 7 | 84 | al-Inshiqāq | 0.264 | 74 |
| 8 | 85 | al-Burūj | 0.264 | 73 |
| 9 | 98 | al-Bayyinah | 0.263 | 57 |
| 10 | 64 | al-Taghābun | 0.260 | 148 |

## Bottom-10 lowest-dispersion surahs

| Rank | Q | Name | Dispersion | N stems |
|:-:|:-:|---|---:|---:|
| 114 | 2 | al-Baqara | 0.094 | 1616 |
| 113 | 111 | al-Masad | 0.095 | 18 |
| 112 | 106 | Quraysh | 0.102 | 12 |
| 111 | 4 | al-Nisāʾ | 0.111 | 1101 |
| 110 | 7 | al-Aʿrāf | 0.113 | 1174 |
| 109 | 3 | Āl ʿImrān | 0.117 | 1065 |
| 108 | 9 | al-Tawbah | 0.119 | 854 |
| 107 | 6 | al-Anʿām | 0.125 | 1020 |
| 106 | 12 | Yūsuf | 0.126 | 703 |
| 105 | 5 | al-Māʾidah | 0.127 | 922 |

## Q 1 specifically

- Rank 3/114 (98th percentile) under this stemmer
- [[h-new-155-q1-sui-generis|H-NEW-155]] under QAC-STEM had Q 1 at higher rank with sui-generis claim
- **The Q 1 uniqueness is STEMMER-SENSITIVE**: under rougher stemmer, Q 103 al-ʿAṣr and Q 110 al-Naṣr narrowly exceed Q 1
- Q 1 IS still in top-3% of dispersion

## Q 114 al-Nās specifically

- Rank 19/114 (84th percentile)
- High-dispersion but not extreme
- Q 114 IS in upper-quintile but not near top
- Q 113 al-Falaq (rank 80) and Q 112 al-Ikhlāṣ (rank 79) are MIDDLE
- **No symmetric "Q 114 = closing-seed" pattern** parallel to Q 1

## The architectural pattern (genre × dispersion)

**Top-10 = SHORT CREEDAL/LITURGICAL surahs**:
- Q 1 (prayer-frame), Q 103 (time-oath), Q 110 (victory-oath), Q 109 (creed-confession), Q 62 (Friday), Q 95 (fig-oath), Q 98 (clear-evidence), Q 84-85 (apocalyptic-oath), Q 64 (musabbiḥāt)

These use WIDELY-DISPERSED theological vocabulary (God-names, eschatology, general religion-terms) because they're templates or oath-fragments that draw from the Quran's general lexicon.

**Bottom-10 = LONG NARRATIVE/LEGAL surahs**:
- Q 2 (longest, Medinan legal), Q 4 (Nisāʾ legal), Q 7 (Aʿrāf narrative), Q 3 (Āl ʿImrān), Q 9 (Tawbah legal), Q 6 (Anʿām narrative), Q 12 (Yūsuf pure narrative), Q 5 (Māʾidah legal), plus Q 111 al-Masad (unique narrative-curse, short but concentrated) and Q 106 Quraysh (unique tribal-narrative)

These use SURAH-SPECIFIC vocabulary — legal codes, personal names in narratives, prophet-specific terms.

## Interpretation

**The dispersion metric distinguishes TWO COMPOSITIONAL MODES**:

1. **TEMPLATE MODE**: short creedal/liturgical surahs use the Quran's general theological palette. Their stems appear across the corpus. Q 1 is the APEX of this mode but not alone.

2. **CONCENTRATOR MODE**: long narrative/legal surahs use surah-specific vocabulary. Their stems appear mostly within themselves. Q 2 is the APEX of this mode.

The two modes are architecturally opposite: templates DISTRIBUTE THEIR CONTENT ACROSS THE CORPUS; concentrators ABSORB UNIQUE CONTENT INTO THEMSELVES.

**Refines [[h-new-155-q1-sui-generis|H-NEW-155]]**: Q 1's dispersion is in the top-3% but NOT uniquely sui-generis under this rougher stemmer. The classical "umm al-kitāb" intuition (Q 1 as seed-of-the-whole) is preserved at the group-level (template mode) but tightened at the individual level (Q 1 is the most-famous, not the most-extreme, template).

**Opens**: does the theorist's Class A distinction need revision? Under [[h-new-155-q1-sui-generis|H-NEW-155]] strict test, Q 1 is Class A alone. Under [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]] rough-stemmer, Class A would include Q 1, 103, 110, 109, 62 (top-5).

## Honest limits

1. **Rougher stemmer** than specialist-b's QAC-STEM — ranking differs quantitatively
2. **Dispersion is one axis** — other metrics (within-surah uniqueness, network-centrality) might give different extremes
3. **Short surahs have few stems** — sample-size effect. Q 1 (23 stems) is better-sampled than Q 103 (12 stems). Correction would need stem-count-residualization; descriptive only here
4. **Template vs Concentrator** is a binary simplification — many surahs sit in the middle

## Queue

- H-NEW-163.1: re-run with QAC-STEM roots (proper morphology) to see if Q 1 uniquely tops
- H-NEW-163.2: length-residualized dispersion (remove size bias)
- H-NEW-163.3: test whether the TEMPLATE/CONCENTRATOR binary structurally correlates with muq-opened surahs

## Connection to unified model

- **Refines Class A (sui-generis-liturgical) in theorist's model**: Q 1 may be joined by Q 103, 110, 109 as template-mode surahs
- **Within M5 (length-stratification + vocabulary concentration)**: template/concentrator mode IS an expression of the length × vocabulary-concentration gradient
- **Independent of M1/M2/M3**: dispersion is a compositional not topological axis

## Files

- Script: inline (seed 20260417)
- Log: `/tmp/h163.log`
- Findings: this file
