---
finding_id: Q055-F-04
title: Dual-paradise structural similarity test
phase: B+
date_locked: 2026-04-28
seed: 20260428
n_perm: 10000
bonferroni_k: 2  # (direction, perm-p)
alpha_bon: 0.025
script: surahs/Q055-al-rahman/scripts/Q055_F_04_dual_paradise.py
---

# Q055-F-04 — Dual-paradise structural similarity pre-registration

## Hypothesis

The two paradise-blocks of Q 55 — vv. 46-61 (P1, "first pair") and vv. 62-77 (P2, "second pair") — form parallel descriptions of two heavens with different rank, with structurally near-identical bag-of-tokens. Their normalized cosine similarity should exceed both (a) the cosine of P1 to a length-matched control block (vv. 14-29, the jinn-creation block), and (b) the cosine of P2 to that same control.

## Direction (LOCKED)

- cos(P1, P2) > cos(P1, CTRL) AND cos(P1, P2) > cos(P2, CTRL).
- Permutation-null on random 16-verse-block pairs from Q 55: cos(P1, P2) significantly higher (p<0.025 Bonferroni-corrected).

Counter-direction (P1-P2 cosine ≤ either control, OR perm-p ≥ 0.025) = NULL.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, Hafs-Kufan)`. Diacritics stripped; alif normalized.

## Permutation null

10,000 random 16-verse partitions of the 78 Q-55 verses; recompute cos. The count of perms where cos ≥ observed gives the permutation p-value.

Seed: 20260428.

## Success criteria

- direction PASS + perm-p < 0.025 → CONFIRMED
- direction PASS only → DIRECTIONAL
- direction FAIL → NULL
