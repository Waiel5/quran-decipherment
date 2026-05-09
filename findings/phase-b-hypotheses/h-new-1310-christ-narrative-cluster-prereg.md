---
id: H-NEW-1310
title: Christ-narrative 3-surah cluster Fisher-Rao cohesion {Q 3, Q 5, Q 19}
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-1310-christ-narrative-cluster
alpha_bon: 0.025
direction_of_effect: The 3 surahs containing the most explicit Christ-narrative content {Q 3 Āl ʿImrān, Q 5 al-Māʾida, Q 19 Maryam} have a mean intra-cluster Fisher-Rao distance lower than 95% of length-matched random 3-surah samples
origin: pre-reg from handoff §7b high-EV inline test list (the cluster-membership is locked from the handoff text, not from any FR-matrix observation; this is a planned-not-discovered test)
verdict_ceiling: PASS-DIRECTED (handoff origin = single planned test; no INDEPENDENT REPLICATION yet)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: standard-mashriqi
  null_model: random-3-surah-samples-no-Q1-uniform-and-length-matched
---

# H-NEW-1310 pre-registration

## Origin

Handoff §7b (`SESSION-HANDOFF-2026-05-09.md`) lists as a high-EV inline test:
> "Q 19 vs other Maryam/Christ-narrative surahs FR-cohesion: Q 19, Q 3 (Āl ʿImrān), Q 5 (al-Māʾida) — test if Christ-narrative is a tight FR cluster."

This pre-reg locks that test exactly as specified. The 3-surah cluster {3, 5, 19} is **not derived from any FR-matrix observation** — it is the canonical Christ-narrative content list.

## Hypothesis

The Christ-narrative content cluster {Q 3 Āl ʿImrān, Q 5 al-Māʾida, Q 19 Maryam} forms a tight Fisher-Rao cohesion group on the H-NEW-111 root-distribution instrument.

## Test design

### Cell A (primary, uniform null)

Mean pairwise FR among {3, 5, 19} = 3 pairs. Permutation null: 10000 random 3-of-113 samples (excluding Q 1) without replacement. Direction-locked: intra-cluster mean ≤ permutation null 5th percentile.

**Decision**: PASS if p_perm ≤ 0.025; NULL otherwise.

### Cell B (length-matched control)

Same test restricting null to 3-surah samples whose total verse-count is within ±20% of observed (Q 3 = 200; Q 5 = 120; Q 19 = 98; total = 418 verses). Addresses long-Medinan + long-Meccan length confound.

**Decision**: PASS if p_perm ≤ 0.025; NULL otherwise.

### Bonferroni

k = 2 (Cell A + Cell B). α_bon = 0.025 per cell.

### MW-5 positive control (corrected from H-NEW-1301 lesson)

Use the **H-NEW-1190 *wa-mā adrāka mā* 10-surah cluster** {69, 74, 77, 82, 83, 86, 90, 97, 101, 104} — CONFIRMED FR-cohesive at p=0.00068. Sub-sample 3-of-10 deterministically (seed 20260509, sorted picks). Test under uniform 3-of-113 null. PC must pass at p ≤ 0.05 for instrument to be trusted.

Lesson learned from H-NEW-1301: HM cluster's letter-set tightness does NOT transfer to root-distribution FR. The H-NEW-1190 cluster IS root-distribution-FR-tight by construction. Correct PC for the FR instrument.

### Acceptance windows

| Cell A pass | Cell B pass | PC pass | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✗ | ✓ | DESCRIPTIVE-ONLY (length confound) |
| ✗ | ✓ | ✓ | PARTIAL |
| ✗ | ✗ | ✓ | NULL |
| any | any | ✗ | NULL-BROKEN |

### Garden-of-forking-paths

Origin disclosed: handoff §7b. No FR-matrix value loaded. Direction locked. No alternative cells. Cluster identity {3, 5, 19} is locked from the handoff text and not modifiable post-observation. Q 4 (denial of crucifixion v 157-158) and Q 43 (Jesus discussion vv 57-65) are NOT in the cluster despite arguably also being Christ-narrative; this is the handoff-locked 3-surah cluster, not a maximal Christ-content cluster.

### Anti-flip

Reverse direction (cluster mean ≥ 95th percentile = anti-cohesion / heterogeneous) is NOT a reportable PASS. Publish as NULL with reverse-direction note.

### Honest pre-disclosure of length spread

Q 3 = 200v Medinan, Q 5 = 120v Medinan, Q 19 = 98v Meccan. The length disparity is moderate; chronology is split (2 Medinan + 1 Meccan). Both chronology and length are confounded with possible thematic clustering. Cell B controls length but not chronology. If Cell A passes but Cell B fails: chronology-or-length-confound; if both pass: structural cohesion robust to length.

## Connection to existing findings

- Cross-finding-008 muqaṭṭāʿat-as-book-introduction: Q 3 is الم-opened, Q 19 is كهيعص-opened, Q 5 is non-muq. The cluster contains 1 ALM + 1 KHYAS + 1 non-muq — heterogeneous on muqaṭṭāʿat-axis.
- Cross-finding-013 ring-topology / M3: tests whether Christ-narrative connects across the mushaf despite being 3 distant surahs (Q 3 / Q 5 / Q 19 are Mushaf positions 3, 5, 19 — early-mushaf bunched, but Nöldeke-rank widely separated).
- H-NEW-86 surah-name-as-key-root: Q 19 is Maryam-named; *mrym* root density is corpus-EXTREME there. Test interaction with Christ-narrative cluster.

## Pre-commit attestation

Locked by SHA256 hash. Run script verifies SHA before loading FR matrix.
