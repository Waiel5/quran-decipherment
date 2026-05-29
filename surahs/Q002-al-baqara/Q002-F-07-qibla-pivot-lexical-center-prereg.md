---
surah: 2
surah_name: al-Baqara
file_type: pre-registration
test_id: Q002-F-07
date_registered: 2026-05-29
phase: B+
status: LOCKED-BEFORE-RUN
seed: 20260509
n_perms: 10000
rules_tuple: (no-tashkeel, QAC-triliteral-root, root-sets, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q002-F-07 — The qibla-change pericope as al-Baqara's lexical center

## Motivation

Q002-F-04 found NO whole-surah verse-token ring around v143 (NULL, resolution-limited).
But the project's corpus-wide chiastic audit (`findings/phase-c-structures/chiastic-audit.md`,
§4.2 + §5.1) reports that the **single strongest ring in the entire Quran** is the
**root-Jaccard sub-surah window Q 2:131–144** (the Abraham/qibla pericope), z = +9.69
over a 57,996-window Bonferroni family. The classical/Farrin claim places the qibla-
change pivot at v143 — "We have made you a middle nation (ummatan wasaṭan)" — which some
classical reckonings call the literal middle of al-Baqara, and which Farrin (2010) calls
the geometric and theological centre of his macro-ring.

This test does TWO close-reading things F-04 did not:

1. **Replicate** the chiastic-audit's Q 2:131–144 ring z-score with an INDEPENDENT
   pipeline (my own root-set Jaccard, project seed 20260509, 10,000 perms) — MW-5
   independent-replication of a corpus-wide finding inside the surah file.
2. **Test the literal-center claim**: is the qibla-change passage actually at the
   LEXICAL midpoint of al-Baqara? Compute the cumulative-word-mass midpoint and the
   cumulative-root-mass midpoint of al-Baqara's 286 verses and ask which verse the
   midpoint falls on. Pre-register the prediction.

## Hypotheses (DIRECTION LOCKED)

**H1 (ring replication):** The root-Jaccard paired-symmetry ring score of the
14-verse window Q 2:131–144 exceeds the 95th percentile of 10,000 within-window
verse-order shuffles (one-sided), replicating the chiastic-audit's positive z. Direction
LOCKED: HIGH (canonical order is more ring-shaped than shuffles).

**H2 (lexical center):** The cumulative-word-mass 50% point of al-Baqara (the verse at
which cumulative word count first reaches half the surah total) falls within the
qibla-block, pre-committed as verses **142–152** (Farrin's central pivot block). Same
test for cumulative-root-mass (cumulative count of root-tokens). Direction LOCKED:
the word-mass and root-mass midpoints land in 142–152.

## Metrics (MW-1 locked)

- Ring score for a window of N verses: (1/⌊N/2⌋) Σ_{i=1..⌊N/2⌋} Jaccard(R(v_i), R(v_{N+1−i})),
  R(v) = QAC-triliteral-root set of verse v. Identical to chiastic-audit §1.
- Word mass: per-verse whitespace word count (no-tashkeel, sajda-stripped). Cumulative
  midpoint = first verse index where running sum ≥ 0.5 × total words.
- Root mass: per-verse count of QAC root-tokens (with multiplicity). Cumulative midpoint
  defined identically.

## Null / significance

- H1: one-sided permutation p < 0.05 (10,000 within-window shuffles, seed 20260509).
- H2: midpoint verse ∈ {142..152} → VINDICATED; ∈ {131..160} (wider pericope) →
  DIRECTIONAL; outside → NULL.
- Bonferroni: k = 2 (H1 ring, H2 midpoint) → α_corrected = 0.025 for H1.

## Failure / NULL conditions

- If the canonical ring score does NOT exceed the 95th percentile → H1 NULL (would
  contradict the chiastic-audit; flag as replication failure).
- If both midpoints fall outside 131–160 → H2 NULL: the "literal center" is a
  numerological folk-belief, not a lexical fact. Published with full prominence.

## MW protections

- MW-1: ring metric + midpoint metric locked pre-run.
- MW-2: 10,000-perm within-window shuffle (vs the chiastic-audit's 50 — a 200× tighter
  null, strengthening the replication).
- MW-5: this IS a cross-pipeline replication of a prior corpus-wide finding.
- MW-6: control — run the same ring test on a NON-pericope window of the same width
  (Q 2:100–113, an arbitrary 14-verse window) to confirm the metric returns NULL where
  no ring is expected.

## Honesty note

The "v143 is the literal middle verse of the Quran/al-Baqara" claim is a classical folk-
reckoning with multiple variant counts. We test the lexical-mass version, which is the
only falsifiable form. A NULL on H2 does not falsify Farrin's THEMATIC-pivot claim.
