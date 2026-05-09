---
finding_id: Q084-F-02
title: Q 84:6 *kādih ilā rabbika kadḥan* mortar-and-clay structural-verse audit
phase: B+
date_locked: 2026-05-09
seed: 20260509
n_perm: 0  # corpus root-uniqueness test
bonferroni_k: 2
alpha_bon: 0.025
script: surahs/Q084-al-inshiqaq/scripts/Q084_F_02_mortar_clay.py
parent_findings: 
---

# Q084-F-02 — Q 84:6 root k-d-ḥ rarity audit

## Hypothesis

H1: The root k-d-ḥ (كدح) — meaning to toil, exert intense effort, scratch — is corpus-RARE. The famous *yā ayyuhā al-insān innaka kādiḥun ilā rabbika kadḥan fa-mulāqīh* construction in Q 84:6 contains ALL the corpus tokens of this root.

H1a: The root k-d-ḥ appears in EXACTLY 1 verse corpus-wide (Q 84:6), with all tokens (kādiḥ, kadḥ) clustered in this one verse.

H1b: Q 84:6's bigram (*kādiḥun ... kadḥan*) — verbal-noun + active-participle of same root in maṣdar-mafʿūl-muṭlaq construction — is corpus-EXACT (only such kdḥ-bigram in the corpus).

## Direction (LOCKED before observation)

- Root k-d-ḥ corpus token count: ≤ 2 (Q 84:6 only)
- Verse count containing root: 1 (Q 84:6 alone)

Counter-direction (root appears in any other verse) = NULL on uniqueness; partial on rarity.

## Rules-tuple

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

## Operationalization

1. Strip diacritics; normalize alif variants.
2. For each verse v in the corpus, search for the substring `كدح` (k-d-ḥ as raw consonant sequence) — also accept `كادح`, `كادحا`, `كادحون`, `كدحا`.
3. Count corpus-wide tokens; report verses.

## Success criteria

- 1 verse, 2 tokens, both in Q 84:6 → CONFIRMED corpus-EXACT-RARE
- 2-3 verses, 2-4 tokens, all in Q 84 cluster → DIRECTIONAL-RARE
- > 3 verses or root appears in non-Q-84 surah → NULL on uniqueness

## Failure conditions

- Root appears in any non-Q 84 verse.

## Pre-commit honesty

Direct corpus search; no permutation needed.

## Connection to existing findings

This is a verse-level signature test for Q 84's rhetorical centerpiece. Classical balāgha (al-Zamakhsharī *al-Kashshāf*, al-Rāzī *Mafātīḥ al-Ghayb*) treat Q 84:6 as a *waḍʿ al-kalām* (placement-of-speech) iʿjāz exemplar — the *kādiḥun + kadḥan* mafʿūl-muṭlaq doubles intensity. If the root is corpus-EXACT to this verse, then Q 84:6 is a content-anchor for the root k-d-ḥ in the entire Quran.
