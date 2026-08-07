---
surah: 65
surah_name_ar: الطلاق
surah_name_translit: al-Ṭalāq
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 65 al-Ṭalāq — Investigation Journal


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 2026-05-09 — full 8-file deep-dive (specialist: Waiel Al-Shujaa)

The seven content files (00-overview through 07-cross-references) and the 4 pre-registered tests
(Q065-F-01..04) were authored on 2026-05-09 — the ledger's first specialist landing INSIDE the
H-NEW-1080 short-Medinan-block (Q 57-66). This JOURNAL is the run-log summary, written consistent
with the on-disk files; every value below is traceable to the cited artifact, not restated from
memory.

**Pre-flight (per INVESTIGATION-PROTOCOL.md §6.1):** quran-investigation SKILL.md →
INVESTIGATION-PROTOCOL.md (full) → KNOWLEDGE-GRAPH.md → MASTER-FINDINGS-LEDGER.md (H-NEW-1080
short-Medinan-block + H-NEW-1240 seamless-seams + H-NEW-119 sabʿ-samāwāt sections) → built the
template.

**Surah profile (from disk, every value path-traced):**
- 12 verses, **Medinan** (uncontested Sunnī + Nöldeke; mid-Medinan, post-Aḥzāb / pre-Tawba); Tanzil
  rev-order 99/114 (`data/revelation-order.csv`); `data/hafs-verse-counts.tsv` line 65 = 12.
- 289 word-tokens / 1,203 letter-graphemes (no-tashkeel), mean 24.08 words/verse — computed from
  `quran-text/quran-no-tashkeel.json`. Length-skew = few-verse + dense-verse (v.1 = 42 words), the
  classical legislative-Medinan signature.
- Opening: يا أيها النبي إذا طلقتم النساء… — Q 65 is one of only **three** surahs opening at v.1 with
  the prophetic vocative *yā ayyuhā al-nabī* (the corpus-exact trio {Q 33, Q 65, Q 66}); Q 65 + Q 66
  are a mushaf-adjacent 12-verse legal-domestic dyad.
- 3 blocks: A (1-7 ṭalāq + ʿiddah + nafaqah procedure), B (8-10 historical warning to past
  communities + believers' affirmation), C (11-12 messenger affirmation + cosmology codification).
- Rhyme: functionally alif-monorhyme 91.7% (11/12; sole departure v.6 *ukhrā* / alif-maqṣūra ى under
  strict-grapheme convention — MASTER-FINDINGS-LEDGER line ~1985). Grammatically driven by the
  feminine-plural ṭalāq legislation (*-hunna* suffixes).

**H-NEW metrics integrated (01-empirical-profile, all cited to path):**
- **h-new-111**: mean FR 0.9534 (rank 69/114, modest above-mean content-distinctness); intra-block
  mean to its 9 short-Medinan siblings 0.8479 vs corpus pairwise 0.9235.
- **h-new-590**: WEAK_OUTLIER, Δ%ile +0.94, window {Q 62-68}.
- **h-new-750**: rhyme entropy 0.2868 nats (z −0.871, near-monorhyme/low); sig_A −1.170 (rank 89),
  sig_B −1.360 (rank 98) — structurally iʿjāz-NEGATIVE on both al-Bāqillānī axes (legislative-prose
  register).
- **h-new-720 / h-new-1240**: Q 64→Q 65 δ_raw −0.0087 → clamped 0.0000; Q 65→Q 66 δ_raw −0.0340 →
  clamped 0.0000. Q 65 is the central surah of a clamped-zero seam-pair (one of only two surahs with
  this property — the other is Q 73 in the muqaddimāt cluster).
- **h-new-840**: UAS rank 94/114 (structurally non-distinctive on the unified axis but
  cluster-positive).

**Tafsīr (≥5, scholar + work + passage, in 03-tafsir-survey):** al-Ṭabarī, al-Zamakhsharī
(*al-Kashshāf*), Ibn Kathīr, al-Qurṭubī, al-Rāzī, al-Biqāʿī (*Naẓm al-Durar*, Q 64→65→66 munāsaba).

**Ḥadīth (04-hadith-corpus, verified on disk):** al-Bukhārī *Kitāb al-Ṭalāq* (95 ḥadīth) +
Muslim *Kitāb al-Ṭalāq* (87 ḥadīth); the Ibn ʿUmar ṭalāq-during-ḥayḍ ḥadīth at al-Bukhārī global
#5042 / Muslim ʿAbd al-Bāqī #1471a; the 7-earths cosmology ḥadīth (Bukhārī #2452 / Muslim #1610) as
Sunna-side validator of the Q 65:12 7+7 codification.

**Pre-registered tests (06-novel-findings; Bonferroni-k=4, α_bon 0.0125; seed 20260509). NOTE:
unlike Q 31, these 4 tests are deterministic FR-distance reads from `h-new-111.json` + exhaustive
no-tashkeel corpus scans (no permutation null is required for an exact-distance or 1/6,236 count),
so they were computed and documented INLINE (00-overview §10 + 06-novel-findings). The per-test
`preregs/`, `scripts/`, `csv/` directories were created but the individual files were NOT persisted
to disk — flagged here honestly. A future pass should serialise the prereg-SHA + script + JSON for
each test to bring the artifact trail to Q031-level completeness.**
- **Q065-F-01** *yā ayyuhā al-nabī* trio {Q 33, Q 65, Q 66} FR-cohesion — predicted NOT cohesive.
  Trio mean 0.9619 > corpus 0.9235; Q 65↔Q 66 alone is a tight 0.8705 pair. **CONFIRMED-DIRECTIONAL**
  (Q 33 dilutes; literary-form opener ≠ whole-surah content unity).
- **Q065-F-02** Q 65:12 corpus-EXACT 7+7 cosmology — strict phrase *sabʿ samāwāt wa-min al-arḍ
  mithlahunn* = 1/6,236 (Q 65:12 only); token *mithlahunn* HAPAX; *khalaqa sabʿ* = 2 (Q 65:12,
  Q 67:3); *sabʿ samāwāt* = 5 (Q 2:29, 41:12, 65:12, 67:3, 71:15). **CONFIRMED-EXACT** — refines the
  FALSIFIED H-NEW-119 "7 occurrences" claim: the count is 5, but the 7+7-symmetric architecture is
  uniquely localised at Q 65:12.
- **Q065-F-03** Q 65 intra-block position in H-NEW-1080 — predicted peripheral. Mean FR-to-siblings
  0.8479 = **rank 10/10 (most peripheral)**; block centroid Q 64 al-Taghābun (0.7409).
  **CONFIRMED-DIRECTIONAL** — and the Q 64(centroid)→Q 65(edge) clamped-zero seam is a
  core-to-periphery link.
- **Q065-F-04** classical 3-surah ṭalāq cluster {Q 2, Q 33, Q 65} whole-surah FR — predicted NULL.
  Cluster mean 0.9652 > corpus 0.9235. **CONFIRMED-NULL-DIRECTIONAL** — second formal NULL-confirm
  of *classical-thematic-cluster ≠ whole-surah FR-cluster* (after Q033-F-05 wives-cluster);
  published with equal prominence per §1.3 / §8.

**Decision points / discipline (garden-of-forking-paths, 00-overview §14):** all 4 directions
pre-committed before computing; 4/4 matched; no sign-flips, no post-hoc feature-space expansion.
Net: 3 CONFIRMED + 1 NULL (CONFIRMED at the NULL direction), reported with equal prominence.

**Architectural verdict:** Q 65 is the corpus's **only dedicated ṭalāq-legislation surah** — a
4-cluster over-determined node (short-Medinan-block / qiṣār al-Madanī / ṭalāq-legislation /
*yā ayyuhā al-nabī* opener trio), structurally iʿjāz-NEGATIVE (legislative prose), geometrically
peripheral within its block, yet seamlessly seated via a clamped-zero seam-pair; closes on the
corpus-EXACT 7+7 cosmology-omniscience codification grounding the ḥudūd in divine encompassment.

**Files on disk:** 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey,
04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this).
Empty `preregs/` `scripts/` `csv/` dirs present (per-test artifacts not yet serialised — see note
above).

## 2026-05-30 — JOURNAL added (→ 9/9)

This JOURNAL was added in the surah-completeness pass to bring Q 65 from 8/9 to the full 9/9
template; it summarises the 2026-05-09 deep-dive already on disk and introduced no new computation.
The honest flag on the unpersisted per-test artifacts (above) is the one substantive gap noted for
future work.
