---
surah: 112
surah_name_ar: الإخلاص
surah_name_translit: al-Ikhlāṣ
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 4 pre-registered tests run; 2 VINDICATED, 1 SPLIT (PASS-LOOSE/NULL-STRICT), 1 VINDICATED-RULES-TUPLE-STABLE
---

# Q 112 al-Ikhlāṣ — Novel Findings

Each finding below is pre-registered with a SHA-locked markdown file; the run script is invoked at runtime, the SHA is verified, and the result is written to `csv/Q112-F-NN.json`.

## Finding inventory

| ID | Title | Pre-reg SHA-head | Verdict |
|:--|:--|:--|:--|
| Q112-F-01 | FR-centroid status — empirical lock on *thuluth al-Qurʾān* | 6e4cdfbec48e | **VINDICATED** (rank 1/114; H1-strong) |
| Q112-F-02 | Modal-root-density mechanism for FR-centroid | 4d553d5a684c | **SPLIT** (top-20 PASS-DIRECTIONAL / top-50 NULL) |
| Q112-F-03 | Theological-proposition density (*iʿjāz al-maʿnā*) | f28637a062ad | **VINDICATED** (1.0 prop/verse, rank 1 among 5 comparators) |
| Q112-F-04 | *aḥad*-bookend chiasm rules-tuple stability | 5eede724edc0 | **VINDICATED-RULES-TUPLE-STABLE** |

## Q112-F-01 — FR-centroid status (HEADLINE)

**Hypothesis**: Q 112 al-Ikhlāṣ has FR-centroid rank ≤10 of 114; (strong) rank == 1.

**Result**: **rank = 1 / 114; mean_d = 0.7592**. Both H1 and H1-strong PASSED.

This is the **strongest empirical lock available on the *thuluth al-Qurʾān* claim** (al-Bukhārī ḥadīth #5013-15). See `Q112-F-01-fr-centroid.md` for the full findings markdown and the top-10 FR-centroid table.

**Bonferroni**: family of 4 → α=0.0125; p_under_uniform=1/114=0.0088 < 0.0125. **Significant under Bonferroni.**

## Q112-F-02 — Modal-root-density mechanism (SPLIT)

**Hypothesis**: Q 112's root-tokens concentrate in corpus-modal roots (top-20, top-50).

**Result**:
- Q 112 fraction in top-20 most-frequent roots = 40.0% (corpus mean 26.65%); rank **4 / 114**. PASSES strict (rank ≤ 11).
- Q 112 fraction in top-50 = 40.0% (corpus mean 42.06%); rank **76 / 114**. NULL (BELOW corpus mean).

**Mechanism**: the FR-centrality of Q 112 is partly explained by its concentration in the very-most-modal roots (Alh, qwl, kwn, wld) but NOT by a broader top-50 distribution. The 6/10 non-top-20 roots (AHd, Smd, kfA) are theologically signature roots, not modal roots. The FR-centrality emerges from a mix of top-modal vocabulary AND theologically-central but lexically-rare roots.

**Honest limit**: Bonferroni-corrected (α=0.0125), the rank-4 result has p=0.035 — does not pass Bonferroni. **DIRECTIONAL** rather than CONFIRMED at law-strength. NULL on top-50 published with full prominence.

See `Q112-F-02-modal-root-density.md`.

## Q112-F-03 — Theological-proposition density

**Hypothesis**: Q 112 has the highest theological-proposition density per word among comparator surahs (Q 1, Q 109, Q 113, Q 114).

**Result**:
- Q 112: 4 propositions / 15 words = **0.267 propositions per word; rank 1/5**.
- Q 112: 4 propositions / 4 verses = **1.000 propositions per verse; rank 1/5**.

**Verdict**: VINDICATED among comparators. Q 112 has the highest per-word AND per-verse theological-proposition density of any comparator.

**Honest limit**: Annotation is manual using the 4-cell *kalām* taxonomy (al-Bāqillānī *al-Tamhīd*). Alternative taxonomies could change the count. Replication-with-different-annotator and corpus-wide annotation are required for law-strength claims.

This empirically vindicates al-Khaṭṭābī's *iʿjāz al-maʿnā* claim for Q 112 at the comparator-set level.

## Q112-F-04 — *aḥad*-bookend chiasm rules-tuple stability

**Hypothesis**: v.1 and v.4 of Q 112 end in the same word (*aḥad*) across all 3 tashkeel variants; v.2 ends *al-ṣamad*, v.3 ends *yūlad*; all 4 verses end in د.

**Result** (all 3 tashkeel variants):
- v.1 final token (no-tashkeel): أحد ; (min-tashkeel): أَحَدٌ ; (full-tashkeel): أَحَدٌ → diacritic-stripped: **اhد** ✓
- v.4 final token (no-tashkeel): أحد ; (min-tashkeel): أَحَدٌ ; (full-tashkeel): أَحَدُۢ → diacritic-stripped: **احد** ✓
- v.1 == v.4 ✓
- v.2 == *al-ṣamad* ✓
- v.3 == *yūlad* ✓
- All 4 verses end in د ✓
- **RULES-TUPLE STABLE across all 3 tashkeel variants** ✓

**Verdict**: VINDICATED-RULES-TUPLE-STABLE.

**Architectural significance**: Q 112's *aḥad*-bookend with -ad rhyme on all 4 verses is an exact micro-chiasm structurally analogous to Q 1's 7-verse chiasm ([[Q001-al-fatiha/Q001-F-01-chiastic-symmetry|Q001-F-01]]). The 4-verse chiasm at the *iʿjāz-al-maʿnā* exemplar pairs with Q 1's 7-verse chiasm at the corpus head.

## Synthesis

Together, the 4 findings establish:

1. **Q 112 is the corpus FR-centroid (rank 1/114).** [Q112-F-01]
2. **The mechanism is partial concentration in top-modal vocabulary + theological-signature roots** — not pure modal-root weighting. [Q112-F-02]
3. **Q 112 has the highest theological-proposition density** of comparator surahs. [Q112-F-03]
4. **The *aḥad*-bookend chiasm is rules-tuple-stable** across all 3 tashkeel variants. [Q112-F-04]

These findings collectively constitute the project's most rigorous empirical lock on al-Khaṭṭābī's *iʿjāz al-maʿnā* claim for Q 112, and on al-Bukhārī's *thuluth al-Qurʾān* hadith.

## Cross-references

- [[Q112-al-ikhlas/01-empirical-profile|Q 112 empirical profile]] — H-NEW source data.
- [[Q112-al-ikhlas/05-classical-claims-audit|Q 112 audit]] — classical-claim verifications referencing these findings.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — *iʿjāz-al-maʿnā* cell typology.
- [[muawwidhat-cluster-synthesis|muʿawwidhāt cluster synthesis]] — cluster-level pre-registered cohesion test.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
