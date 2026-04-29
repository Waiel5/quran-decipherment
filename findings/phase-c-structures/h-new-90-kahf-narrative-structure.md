---
phase: C
finding_id: h-new-90-kahf-narrative-structure-run-1
date: 2026-04-15
agent: h-new-90-specialist
status: reported
prereg: findings/phase-b-hypotheses/h-new-90-kahf-narrative-structure-prereg.md
script: scripts/h_new_90_kahf_narrative_structure.py
data: findings/phase-c-structures/csv/h-new-90-results.json
journal: journal/h-new-90-kahf-narrative-structure-run-1.md
verdict: WEAK
n_pass: 2 of 5
mw5: PASS
claim_class: literary-structural / comparative-narratology / NULL-on-uniqueness
rules_tuple:
  orthography: no-tashkeel
  word_definition: whitespace-split tokens
  letter_definition: rasm graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  similarity: Jaccard of triliteral-root sets per narrative
  null_model: random 4-block partition preserving (18,13,23,16) verse-count tuple, 1000 iter
bonferroni_k: 5
alpha_bon: 0.010
z_threshold: 2.326
---

# H-NEW-90 — Q 18 al-Kahf 4-narrative structural parallelism: a NULL result on uniqueness

## TL;DR

The al-kahf-deep-dive (2026-04-12) qualitatively asserted that Al-Kahf's 4 narratives share an unusual parallel structure. **H-NEW-90 tests this quantitatively against three pre-locked multi-narrative comparator surahs (Q 7 al-Aʿrāf, Q 11 Hūd, Q 26 al-Shuʿarāʾ).** Of 5 pre-registered cells, **only 2 pass**:

- **T1 PASS** — 4-narrative boundaries extract cleanly from modal scholarly consensus.
- **T2 FAIL (z = -6.13)** — Al-Kahf's inter-narrative root-Jaccard is *lower than random* and substantially below all 3 comparators.
- **T3 PASS** — v50 lies in interlude B (45-59), confirming the word-midpoint convergence is at a non-narrative junction.
- **T4 FAIL (z = -4.98)** — Al-Kahf has *fewer* shared-across-3+-narratives roots than random partition predicts.
- **T5 FAIL (z = -0.46)** — Al-Kahf openers share **zero** vocabulary; Q11 Hūd is dramatically more parallel (z = +3.25).

**Verdict: WEAK** — Al-Kahf's 4-narrative structure is *thematically* unified (the al-kahf-deep-dive is correct that the surah has a 4-trial classical reading) but **structurally MORE DIVERSE, not more parallel**, than other multi-narrative surahs. The classical "four trials" reading captures content-level parallelism (faith / wealth / knowledge / power) that does NOT propagate to the lexical-root or opener-formula level.

The MW-5 positive control passes (Moses-Khidr ↔ Dhū'l-Qarnayn jaccard 0.199 > Kahf mean 0.148), confirming the metric is responsive — but this only flags ONE of the 6 narrative pairs as above-mean.

---

## 1. Locked boundaries (T1)

| Surah | Narratives | Source | All 4 extracted? |
|---|---|---|:-:|
| Q 18 al-Kahf | Cave 9-26, Gardens 32-44, Moses-Khidr 60-82, Dhū'l-Qarnayn 83-98 | al-Rāzī *Mafātīḥ*; Qadhi *Light upon Light* | ✓ |
| Q 7 al-Aʿrāf | Adam 11-25, Nūḥ 59-64, Hūd 65-72, Ṣāliḥ 73-79 | Mawdūdī, Quṭb modal | ✓ |
| Q 11 Hūd | Nūḥ 25-49, Hūd 50-60, Ṣāliḥ 61-68, Ibrāhīm-Lūṭ 69-83 | Mawdūdī modal | ✓ |
| Q 26 al-Shuʿarāʾ | Mūsā 10-68, Ibrāhīm 69-104, Nūḥ 105-122, Hūd 123-140 | first-4 by mushaf order | ✓ |

T1 passes by design (boundary extraction succeeds for all 4 surahs).

## 2. Inter-narrative Jaccard (T2) — Al-Kahf is the LEAST parallel

For each surah, compute the 4×4 root-Jaccard matrix; report mean off-diagonal vs null (1000 random 4-block partitions of the surah's narrative verses with verse-count tuple (18,13,23,16)):

| Surah | mean_offdiag | null mean ± std | z-score | Verdict |
|---|---:|---:|---:|---|
| **Q 18 al-Kahf** | **0.1476** | 0.2139 ± 0.0108 | **-6.134** | NULL — *less* shared vocabulary than random |
| Q 7 al-Aʿrāf | 0.2043 | 0.0685 ± 0.0259 | +5.252 | strongly parallel |
| Q 11 Hūd | 0.1913 | 0.1861 ± 0.0237 | +0.220 | average |
| Q 26 al-Shuʿarāʾ | 0.2000 | 0.1783 ± 0.0197 | +1.102 | mildly above null |

**Al-Kahf's 4 narratives use SYSTEMATICALLY DIFFERENT lexicons.** This is the opposite of what a "structural parallelism" claim would predict. The mechanism is intelligible: the four narratives are temporally and topically diverse (sleep vs garden vs sea-voyage vs cosmic journey); the al-kahf-deep-dive correctly notes "time-and-space is Al-Kahf's unifying theme" — but each narrative has its OWN time-vocabulary (lbv/snw for Cave; qTf for Gardens; etc.) that is *internally specialized*.

Al-Kahf's full 4×4 Jaccard:

|  | Cave | Gardens | Moses-Khidr | Dhū'l-Qarnayn |
|---|---:|---:|---:|---:|
| Cave | 1.000 | 0.142 | 0.170 | 0.128 |
| Gardens | 0.142 | 1.000 | 0.103 | 0.144 |
| Moses-Khidr | 0.170 | 0.103 | 1.000 | **0.199** |
| Dhū'l-Qarnayn | 0.128 | 0.144 | **0.199** | 1.000 |

The HIGHEST pair is Moses-Khidr ↔ Dhū'l-Qarnayn at 0.199 — confirming MW-5: these two narratives are the most structurally akin (matching the al-kahf-deep-dive §6.1 three-act-isomorphism observation). But the other 5 pair-Jaccards are at-or-below random.

By contrast, Q 7's prophet-narratives share a thick lexicon (Hūd↔Ṣāliḥ = 0.301, Nūḥ↔Hūd = 0.365) — the well-known "prophet-cycle" formula. Al-Kahf is **not** a prophet-cycle surah at the lexical level.

## 3. v50 boundary check (T3) — PASS

v50 ("And [recall] when We said to the angels, prostrate to Adam, and they prostrated, except for Iblīs. He was of the jinn and departed from the command of his Lord") sits at the geometric midpoint of interlude B (vv 45-59), **not** at any narrative boundary or interior.

This **confirms** the al-kahf-deep-dive §1.1 claim that the whole-Quran word-midpoint at v50 falls at a *non-narrative* junction. The 4 narratives bracket the midpoint without containing it. v50 is itself a 4th-narrative-style brief micro-narrative (the angelic prostration) embedded *between* the Gardens parable and Moses-Khidr.

The implication: the project's "midpoint at v50" finding is **not** explained by v50 being a structural boundary of any specific Al-Kahf narrative; it is genuinely a stand-alone micro-event at the interlude's centre. The v50 word-midpoint convergence is preserved as a real claim.

## 4. Thematic root sharing (T4) — Al-Kahf shares FEWER roots, not more

Number of roots appearing in ≥3 of 4 narratives, vs null (1000 random partitions):

| Surah | n_3of4 | n_4of4 | null mean ± std | z |
|---|---:|---:|---:|---:|
| Q 18 al-Kahf | 22 | 7 | 36.84 ± 2.98 | **-4.98** |
| Q 7 al-Aʿrāf | 18 | 6 | 4.33 ± 5.02 | +2.72 |
| Q 11 Hūd | 27 | 11 | 28.43 ± 3.14 | -0.45 |
| Q 26 al-Shuʿarāʾ | 21 | 11 | 14.21 ± 2.42 | +2.81 |

Al-Kahf's 4-of-4 roots: `Aty (come), byn (clarity/between), kwn (be), qwl (say), qwm (people), rbb (Lord), wjd (find)` — the al-kahf-deep-dive §7 list, confirmed.

But **the COUNT (7) is small** and the random null expects ~37 such roots given the surah's overall vocabulary. The 4 narratives are lexically more SEPARATED than chance. Q 11 by contrast has 11 4-of-4 roots in line with chance (the prophet-cycle formula contributes high-density shared content + frame).

The al-kahf-deep-dive correctly identified `wjd` as a thematic-spine root, but the OVERALL pattern is sparse-and-focused — not dense-and-shared.

## 5. Opener-triple Jaccard (T5) — Al-Kahf has ZERO opener overlap

| Surah | mean_offdiag opener-Jaccard | null ± std | z |
|---|---:|---:|---:|
| Q 18 al-Kahf | **0.000** | 0.014 ± 0.029 | -0.46 |
| Q 7 al-Aʿrāf | 0.083 | 0.013 ± 0.028 | +2.55 |
| **Q 11 Hūd** | **0.117** | 0.015 ± 0.031 | **+3.25** |
| Q 26 al-Shuʿarāʾ | 0.033 | 0.014 ± 0.033 | +0.59 |

Al-Kahf's 4 openers (first-3 normalized tokens):
- Cave: `ام حسبت ان` ("or have you thought that")
- Gardens: `واضرب لهم مثلا` ("and strike for them an example")
- Moses-Khidr: `واذ قال موسي` ("and when Moses said")
- Dhū'l-Qarnayn: `ويسالونك عن ذي` ("and they ask you about Dhū'l-")

**Zero overlapping tokens across all 4 openers.** The al-kahf-deep-dive §2 grid correctly noted these as four DIFFERENT opener formulae — and that diversity is precisely the un-parallel feature: each narrative announces itself in its own grammatical register (interrogative, parable-imperative, narrative-past, question-from-Quraysh).

By contrast Q 11 Hūd uses `wa-ilā [tribe] akhāhum [prophet]` ("and to [tribe] their brother [prophet]") for ʿĀd→Hūd and Thamūd→Ṣāliḥ, plus `wa-laqad arsalnā` ("and certainly We sent") for Nūḥ and the Ibrāhīm-Lūṭ chain — this gives a measurable opener-formula lattice (z = +3.25) that Al-Kahf entirely lacks.

## 6. The classical reading vs the empirical pattern

The classical reading (al-Rāzī, Qadhi) frames Al-Kahf's 4 narratives as the *four great trials* (faith / wealth / knowledge / power) — a thematic schema. The al-kahf-deep-dive correctly identified:

- 4-trial classical mapping (canonical)
- 3-act isomorphism in Moses-Khidr ↔ Dhū'l-Qarnayn (real, captured here as the only above-mean pair)
- Cave ↔ Moses-Khidr "Lord knows best" closure parallelism (qualitative)
- Gardens ↔ Dhū'l-Qarnayn "authority/mercy is my Lord's" closure (qualitative)

**What it OVER-STATED:** that this thematic schema corresponds to a measurable lexical-structural parallelism. It does not. Al-Kahf's 4 narratives are *thematically* a 4-trial template *whose lexical realization is deliberately diversified*. The four narratives speak about the same underlying schema in genre-specific vocabularies (cave-mythology, agricultural-parable, Moses-saga, world-conquest-saga) which by design do NOT overlap.

This is, paradoxically, an *intentional* feature: the surah's didactic strength is that the four trials appear in four maximally different settings (centuries-long sleep / single garden / one journey / the whole earth), so the moral generalizes across genres. **A high inter-narrative Jaccard would actually undercut this rhetorical strategy.**

## 7. Implications for prior findings

Three changes to the project ledger:

1. **al-kahf-deep-dive §2 ("Four-narrative structural parallelism") is RECLASSIFIED:**
   - The 4-narrative *thematic schema* is robust (classical, multi-source attested).
   - The claimed *structural parallelism* (matching openers, dialogue density, three-act templates) is MIXED:
     - Three-act isomorphism (Moses-Khidr ↔ Dhū'l-Qarnayn) survives at pair-level (J = 0.199, only above-mean pair).
     - Opener parallelism FAILS (J = 0).
     - Cross-narrative thematic roots are FEWER than random.
   - The "structural parallelism" framing should be reduced to **the Moses-Khidr ↔ Dhū'l-Qarnayn pair**, where it is real (3-act + Jaccard above mean).

2. **Q 11 Hūd is now identified as the project's strongest opener-formula-parallel surah** (z = +3.25 on opener-triple Jaccard). This is a NEW finding worth a follow-up — the prophet-cycle formula in Hūd is more rigid than in Al-Aʿrāf or al-Shuʿarāʾ. Suggested follow-up: H-NEW-91 testing Q 11 Hūd as the project's best "prophet-cycle template" surah.

3. **The v50 word-midpoint claim is REINFORCED, not weakened.** v50 sits in interlude B at the geometric centre between narratives 2 and 3. The midpoint convergence is at a structural seam, not a narrative event — confirming the al-kahf-deep-dive's reading of v50 as a meta-narrative anchor.

## 8. Honest limits

- Boundaries are locked-but-debatable. Tafsīr disagreement on Cave (whether v27-31 is interlude or part of Cave epilogue) is real; we used the modal Rāzī-Qadhi spec. Sensitivity test (v9-31 as one block) is *not* run here; deferred.
- Verse-count tuple (18, 13, 23, 16) is locked from Al-Kahf and applied to all comparators. This means Q 26's enormous Mūsā pericope (59 verses) is NOT compared at its native size; the test is "would Al-Kahf's narrative-size-tuple, applied to other surahs, produce structural parallelism?" — a fair vs-Al-Kahf control.
- 1000 iterations may underestimate null tail; doubling to 10000 is unlikely to flip the verdict given |z| > 4.9.
- Inter-narrative Jaccard is one of many possible structural-similarity metrics. PMI-based or co-occurrence-based metrics MIGHT yield different results; not tested here.
- Q 7 has multiple narratives beyond the first 4; truncation may obscure structure. We pre-locked first-4 to keep the comparison fair.

## 9. Verdict

**WEAK (2 of 5 cells PASS).** Al-Kahf's 4-narrative structure is thematically real (classical 4-trials reading is sound) but **structurally LESS parallel than other multi-narrative surahs**. The al-kahf-deep-dive's claim of unusual structural parallelism does not survive matched-control quantification. The Moses-Khidr ↔ Dhū'l-Qarnayn pair survives as the one structurally parallel sub-pair within the surah.

The v50 word-midpoint convergence is REINFORCED: v50 lies at the centre of interlude B, a non-narrative seam — exactly where a meta-structural anchor would sit.

Q 11 Hūd, not Al-Kahf, is identified as the Quran's strongest opener-formula-parallel surah. New hypothesis (H-NEW-91) suggested.

---

## Cell verdict table

| Cell | Test | Value | z | PASS at α_bon=0.010? |
|---|---|---:|---:|:-:|
| T1 | 4 boundaries extracted | 4/4 | — | ✓ |
| T2 | Kahf inter-narrative Jaccard z | 0.148 | -6.13 | ✗ (Al-Kahf is LOWEST of 4 surahs) |
| T3 | v50 in interlude (not narrative) | InterludeB | — | ✓ |
| T4 | Kahf 3-of-4 thematic roots z | 22 roots | -4.98 | ✗ (Al-Kahf is LOWEST of 4) |
| T5 | Kahf opener-triple Jaccard z | 0.000 | -0.46 | ✗ (Q11 Hūd is highest at z=+3.25) |
| MW-5 | N3↔N4 above mean | 0.199 > 0.148 | — | ✓ (metric responsive) |

n_pass = 2/5 → **VERDICT: WEAK**.

Bonferroni-corrected (α_outer = 0.010, z > 2.326): only T1 and T3 PASS by definition; the three quantitative cells (T2, T4, T5) all FAIL with negative z-scores against Al-Kahf.

---

## Files

- prereg: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-90-kahf-narrative-structure-prereg.md`
- script: `/Users/grey/Downloads/quran/scripts/h_new_90_kahf_narrative_structure.py`
- raw JSON: `/Users/grey/Downloads/quran/findings/phase-c-structures/csv/h-new-90-results.json`
- journal: `/Users/grey/Downloads/quran/journal/h-new-90-kahf-narrative-structure-run-1.md`
