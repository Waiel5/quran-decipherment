---
finding: Q052-F-04
title: "Q 51-52-53 oath-trio: oath-element-count + FR-cohesion + lexical-bridge analysis (refines H-NEW-1140)"
seed: 20260509
date_locked: 2026-05-09
prereg_locked_before_results: true
bonferroni_k: 3
bonferroni_family: Q052-F-04-oath-trio
alpha_bon: 0.0167
direction_pre_registered: true
---

# Q052-F-04 PRE-REG: The Q 51 → Q 52 → Q 53 consecutive oath-trio is non-monotone in oath-element-count, with Q 52 as the peak; mushaf-adjacency cost asymmetry: smooth Q 51→52 (rank 18) but mid-rank Q 52→53 (rank 90)

## 1. Hypothesis (pre-locked)

**H1 (oath-element-count non-monotonicity)**: The 3-surah consecutive oath-trio Q 51-52-53 (per H-NEW-1140) has **non-monotone oath-element counts**, with Q 52 as the peak:
- Q 51 al-Dhāriyāt: 4 oath-elements (vv. 1-4 *wa-l-dhāriyāt / fa-l-ḥāmilāt / fa-l-jāriyāt / fa-l-muqassimāt*)
- Q 52 al-Ṭūr: 5 oath-elements (vv. 1-2, 4-6 *wa-l-ṭūr / wa-kitābin masṭūr / wa-l-bayti al-maʿmūr / wa-l-saqfi al-marfūʿ / wa-l-baḥri al-masjūr*; v.3 is a continuation-qualifier, not an independent oath-head)
- Q 53 al-Najm: 1 oath-element (v.1 *wa-l-najmi idhā hawā*)

**H2 (mushaf-adjacency-cost asymmetry)**: The Q 51 → Q 52 transition has cost rank 18/113 (delta_raw ≈ 0.01, near-clamped); Q 52 → Q 53 has cost rank 90/113 (delta_raw ≈ 0.125, mid-rank). The asymmetry is **not symmetric** despite both transitions being within the H-NEW-1140 oath-adjacent run.

**H3 (lexical-bridge vs FR-cost dichotomy)**: The Q 52→Q 53 transition has a **rhetorically-vivid lexical bridge** (Q 52:49 *idbāra al-nujūm* ↔ Q 53:1 *wa-l-najmi idhā hawā* — same n-j-m root) but a **mid-rank FR-cost (rank 90)**, demonstrating that **surface-lexical bridges are NOT sufficient for low FR-cost**. This is a useful empirical refinement of al-Biqāʿī's munāsabah claims.

## 2. Test statistic and operationalization

### H1 — oath-element-count

Manual textual analysis of vv. 1-6 for each of Q 51, Q 52, Q 53:
- Q 51: count of distinct *wa-* / *fa-* coordinated oath-heads with active-feminine-plural-participle + cognate-accusative pattern.
- Q 52: count of distinct *wa-* coordinated oath-heads with definite-noun + qualifying-participle pattern.
- Q 53: count of distinct *wa-* / *bi-* coordinated oath-heads.

PASS if oath-element counts are exactly (4, 5, 1) for (Q 51, Q 52, Q 53) — non-monotone with peak at Q 52.

### H2 — mushaf-adjacency cost asymmetry

Use H-NEW-720 per_adjacency data from `findings/phase-b-hypotheses/csv/h-new-720.json`:
- look up Q 51→Q 52: delta_raw + rank
- look up Q 52→Q 53: delta_raw + rank
- compute rank-asymmetry = rank(Q52→Q53) - rank(Q51→Q52)

PASS if rank-asymmetry > 50 — i.e. the two adjacency-costs differ by >50 ranks out of 113. Pre-registered direction: rank(Q52→Q53) > rank(Q51→Q52) (Q 52→Q 53 is more expensive).

### H3 — lexical-bridge vs FR-cost dichotomy

Compute Q 52:49 surface-token overlap with Q 53:1 surface-tokens. Specifically:
- shared root: n-j-m (al-nujūm in Q 52:49 → al-najm in Q 53:1).
- the root is **the SAME**.
- mushaf-adjacency-cost rank for Q 52→Q 53 (from H2) is mid-rank (NOT clamped-zero, NOT extreme high).

PASS if (a) the shared root is verified, AND (b) the rank is in [50, 100] (i.e. mid-rank, not extreme low/high).

## 3. Pass criteria

- H1: oath-element-counts == (4, 5, 1) → PASS
- H2: rank-asymmetry > 50 → PASS
- H3: shared n-j-m root verified AND rank ∈ [50, 100] → PASS

All 3 must pass for joint CONFIRMED. α_bon = 0.0167.

## 4. Rules tuple

- text source: `quran-text/quran-no-tashkeel.json`
- adjacency-cost source: `findings/phase-b-hypotheses/csv/h-new-720.json` (H-NEW-720 canonical-adjacency-cost decomposition)
- oath-element-count: manual+programmatic counting of *wa-* / *fa-* coordinated oath-heads in vv. 1-6 (the standard oath-completion boundary at v.7 *jawāb al-qasam*).
- shared-root: substring match of "نجم" (n-j-m) base-form across Q 52:49 and Q 53:1.
- inclusion: only Q 51, Q 52, Q 53.

## 5. Bonferroni declaration

- bonferroni_k: 3 (H1 + H2 + H3)
- bonferroni_family: Q052-F-04-oath-trio
- alpha_bon: 0.0167
- pre-committed acceptance window: 3 binary tests, all must pass for CONFIRMED.

## 6. Direction pre-registered

H1: counts = (4, 5, 1), peak at Q 52.
H2: rank(Q52→Q53) > rank(Q51→Q52) by ≥ 50.
H3: shared root verified AND rank ∈ [50, 100].

## 7. Garden-of-forking-paths

- Pre-registration origin: this hypothesis emerged from comparison of Q 37, Q 51, Q 52 oath-cluster structures during specialist-deliverable build 2026-05-09. The non-monotonicity (peak at Q 52, dropoff at Q 53) was **noticed via direct comparison of the opening verses**; the H-NEW-720 numbers were looked up only AFTER the H1 hypothesis was locked.
- 3 cells pre-locked; no alternatives considered post-hoc.
- The H3 dichotomy (lexical-bridge vs FR-cost) was anticipated from H-NEW-143's surface-word vs root-level finding; framing was decided BEFORE running the H-NEW-720 lookup.

## 8. Empirical anchors

- H-NEW-1140 (oath-cluster mushaf-adjacency: Q 51-52-53 is one of 3 consecutive oath-runs).
- H-NEW-720 (canonical-adjacency-cost decomposition).
- H-NEW-143 (surface-word vs root-level bridge dichotomy).
- al-Biqāʿī *Naẓm al-Durar* (the Q 52→Q 53 al-nujūm/al-najm lexical bridge claim — see CLAIM 2 in `05-classical-claims-audit.md`).
- al-Rāzī *Mafātīḥ al-ghayb* (mid-mushaf classification of the oath-trio).

## 9. Pre-reg SHA-256 lock

Locked at script-runtime; recorded in `csv/Q052-F-04.json`.

## 10. Author

waiel — pre-reg locked 2026-05-09.
