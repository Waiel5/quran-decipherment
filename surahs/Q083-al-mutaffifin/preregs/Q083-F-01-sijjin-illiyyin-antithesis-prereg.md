---
surah: 83
test_id: Q083-F-01
title: Q 83 SIJJĪN (kitāb al-fujjār, vv. 7–17) ↔ ʿILLIYYĪN (kitāb al-abrār, vv. 18–28) antithetical-pair structure — frame-mirroring vs content-disjunction
file_type: pre-registration
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
bonferroni_k: 3
bonferroni_family: Q083-F-01-sijjin-illiyyin-antithesis
alpha_bon: 0.016667
rules_tuple: "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)"
---

# Q083-F-01 — Pre-registration: SIJJĪN ↔ ʿILLIYYĪN antithetical-pair structure

## 0. Motivation (classical anchor)

Classical *balāgha* names the Q 83 fujjār/abrār contrast as a paradigm of **muqābala** (antithetical
parallelism): two destiny-records described in a deliberately MIRRORED frame but with OPPOSITE
content. The empirically interesting question is whether the "mirror" is **lexical** (the two blocks
re-use the same scaffolding words) while the "opposition" is **referential** (the destiny-content
vocabulary is disjoint). This test pre-registers that decomposition. It is the surah's signature
structure (al-Rāzī *Mafātīḥ al-ghayb* on Q 83:7–21 explicitly pairs *sijjīn* / *ʿilliyyīn* as
*muqābala*; al-Zamakhsharī *al-Kashshāf* ad loc.).

The two blocks (locked before observation, by content boundaries in `quran-text/quran-no-tashkeel.json`):
- **FUJJĀR block (B_f)** = Q 83:7–17 (11 verses): *kallā inna kitāba l-fujjāri la-fī sijjīn … kitābun marqūm … wayl … al-mukadhdhibīn … sāṭlū l-jaḥīm*.
- **ABRĀR block (B_a)** = Q 83:18–28 (11 verses): *kallā inna kitāba l-abrāri la-fī ʿilliyyīn … kitābun marqūm … inna l-abrāra la-fī naʿīm … raḥīqin makhtūm*.

Both blocks are exactly 11 verses — a NATURAL equal-length pairing (not chosen to balance; it is the
content structure of the surah).

## 1. Hypotheses (locked direction BEFORE observation)

**H1 — FRAME-MIRRORING (one-tailed, ELEVATED):** The two blocks share an anomalously HIGH count of
"frame" roots — the structural scaffolding of the antithesis. Frame roots are locked as the QAC stem-
roots of the words that recur in BOTH the *sijjīn* and *ʿilliyyīn* announcement formulae:
`{ktb (kitāb), rqm (marqūm), dry (adrāka), kfr/kdhb-class is NOT frame}`. Operationally: H1 statistic =
the count of DISTINCT QAC roots that appear in BOTH B_f and B_a. Direction LOCKED: shared-root count is
**GREATER** than the null of random equal-length (11-verse) within-corpus block pairs.

**H2 — OVERALL ROOT-JACCARD (two-tailed, reported; primary descriptive):** Jaccard(roots(B_f),
roots(B_a)). No locked direction (this is the disputed quantity — a high Jaccard would favour "lexical
mirror", a low Jaccard would favour "lexical disjunction"); reported as a percentile against the
within-corpus 11-verse-block-pair null. NOT counted toward CONFIRMED/NULL by direction (it is the
descriptive pivot); its percentile is the headline number.

**H3 — DESTINY-CONTENT DISJUNCTION (one-tailed, LOCKED):** The destiny-CONTENT vocabulary is disjoint.
Content roots are the destiny-naming roots locked as:
`fujjār-side {sjn (sijjīn), jḥm (jaḥīm), ḥjb (maḥjūbīn)}` vs
`abrār-side {ʿlw (ʿilliyyīn), nʿm (naʿīm), rḥq (raḥīq), msk (misk), snm (tasnīm), ark (arāʾik)}`.
Statistic: the cross-block overlap of these two destiny-root sets. Direction LOCKED: overlap = **0**
(the two destiny-vocabularies are mutually exclusive). This is a deterministic check (no null needed),
but is reported with the exact root lists so the disjunction is auditable.

**H0 (joint):** Shared-frame-root count is NOT above the null 95th percentile (H1), AND the destiny-
vocabularies are NOT disjoint (H3).

## 2. Operational definitions

- **Source text:** `quran-text/quran-no-tashkeel.json` (default tuple); roots from
  `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4), `ROOT:` features, Buckwalter.
- **roots(block):** the SET of distinct QAC stem-roots over all words in the block's verses.
- **B_f = (83, 7..17); B_a = (83, 18..28).** Both 11 verses.
- **Frame-root shared count (H1):** `|roots(B_f) ∩ roots(B_a)|`.
- **Jaccard (H2):** `|roots(B_f) ∩ roots(B_a)| / |roots(B_f) ∪ roots(B_a)|`.
- **Destiny-root disjunction (H3):** the two locked destiny-root sets above; check that no fujjār-side
  destiny-root appears in B_a's roots and no abrār-side destiny-root appears in B_f's roots, AND that
  the two locked sets do not intersect each other. Pass = full disjunction.

## 3. Permutation null (H1 and the H2 percentile)

Enumerate ALL contiguous 11-verse blocks in the corpus (over all 114 surahs). Draw `n_perm = 10000`
RANDOM PAIRS of distinct 11-verse blocks (seed = 20260509, `random.Random(20260509)`), excluding any
pair where either block overlaps Q 83:7–28. For each null pair compute (a) shared-root count, (b)
Jaccard. 
- **p_H1** = fraction of null pairs with shared-root count ≥ observed B_f∩B_a count.
- **pct_H2** = fraction of null pairs with Jaccard ≤ observed Jaccard (low-side percentile) AND the
  symmetric high-side percentile; both reported.

## 4. Test statistics

- `n_shared` = `|roots(B_f) ∩ roots(B_a)|`; `p_H1`.
- `jaccard_obs`; `pct_low_H2`, `pct_high_H2`.
- `destiny_disjoint` (bool, H3); the explicit fujjār-only / abrār-only / shared destiny-root partitions.

## 5. Success / Failure (Bonferroni k = 3, α_bon = 0.016667)

- **CONFIRMED:** H1 passes (`p_H1 ≤ 0.016667`, shared-frame elevated) AND H3 passes (destiny disjoint).
- **DIRECTIONAL:** exactly one of {H1, H3} passes.
- **NULL:** neither passes.
- H2 is reported as the descriptive pivot (its percentile classifies the antithesis as
  "lexical-mirror" if high-side or "lexical-disjunction" if low-side) but is NOT a pass/fail gate.

## 6. Honest limits known a priori

- The frame roots `{ktb, rqm, dr/dry}` are GUARANTEED shared (both formulae contain *kitābun marqūm* and
  *wa-mā adrāka mā…*); the open empirical question H1 actually tests is whether the TOTAL shared-root
  count (including incidental function/particle roots and any further content overlap) exceeds the null.
  Because the two announcement-formulae are near-verbatim, H1 is EXPECTED to pass; the value of the test
  is to QUANTIFY how anomalous the frame-mirror is against random block pairs, and to confirm H3's
  disjunction holds DESPITE the frame-mirror (the surah's signature: same frame, opposite destiny).
- 11-verse blocks straddling surah boundaries are included in the null (a contiguous-window null is
  standard for this project, cf. Q089-F-02); blocks shorter than 11 verses at corpus tail are not
  generated. Sensitivity: also report the null restricted to WITHIN-SINGLE-SURAH 11-verse blocks.
- Root-SET (presence) is used, not root-bag (counts), because muqābala is a vocabulary-overlap claim,
  not a frequency claim. A root-bag cosine robustness value is reported as a secondary diagnostic only.
- QAC particle/pronoun tokens without `ROOT:` features are excluded (no root) — this is the standard
  project convention and does not bias the antithesis (function words are frame, not destiny-content).

## 7. Pre-commit attestation

Block boundaries, the *kitābun marqūm* / *wa-mā adrāka mā* shared formulae, and the destiny-vocabulary
content were observed during pre-flight close-reading of `quran-text/quran-no-tashkeel.json` (vv. 7–28).
The shared-root COUNT, the Jaccard VALUE, and the null percentiles have NOT been computed prior to this
SHA-lock. Directions for H1 (elevated) and H3 (disjoint = 0) are locked here.

## 8. Garden-of-forking-paths log

- The block boundary at v.17/v.18 is the natural *kallā inna kitāba l-abrāri* turn; the fujjār block
  ends at v.17 (*hādhā lladhī kuntum bihi tukadhdhibūn*). An alternative boundary placing v.17 with the
  abrār block was considered and REJECTED before lock (v.17 is the closing taunt of the fujjār scene).
- The destiny-root sets in H3 were fixed from the surah's own destiny nouns (sijjīn/jaḥīm/maḥjūb vs
  ʿilliyyīn/naʿīm/raḥīq/misk/tasnīm/arāʾik) BEFORE running; no post-hoc adjustment is permitted.
- H2's no-locked-direction status is deliberate: the project's honesty rule forbids locking a direction
  on the disputed pivot quantity. H2 is descriptive; only H1+H3 gate the verdict.

## 9. Decision rule

1. Build roots(B_f), roots(B_a).
2. Compute `n_shared`, `jaccard_obs`, the destiny partition.
3. Build the 11-verse-block-pair null (10000, seed 20260509); compute `p_H1`, H2 percentiles.
4. Apply §5 matrix.
5. If H1 direction reverses (n_shared < null mean) → PRE-REG-STANDARD-01 violation flag, publish NULL.

## 10. Connection to existing findings

- al-Rāzī / al-Zamakhsharī muqābala reading of sijjīn↔ʿilliyyīn (03-tafsir-survey).
- §10.80 H-NEW-2160 rebuke-*kallā* census: both blocks OPEN with *kallā* (vv. 7, 18) — Q 83 is one of the
  two corpus-maximal rebuke-*kallā* surahs (07-cross-references).
- H-NEW-111 FR-roots distance (Q 83 row); Q 82 al-Infiṭār is the 2nd-nearest FR-neighbour (01-empirical).
