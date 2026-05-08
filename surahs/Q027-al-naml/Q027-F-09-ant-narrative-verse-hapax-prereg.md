---
finding_id: Q027-F-09
title: Ant-of-Solomon (Q 27:18) verse-level hapax inventory and lexical distinctiveness
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q027-F-05..F-09
alpha_bon: 0.01
acceptance_window: see §6
---

# Q027-F-09 — Ant-of-Solomon Verse Hapax (Q 27:18)

## 0. Origin

Q 27:18 is the surah's eponymous verse:

> *qālat namlatun yā ayyuhā al-namlu udkhulū masākinakum lā yaḥṭimannakum sulaymānu wa-junūduhu wa-hum lā yashʿurūn*

> "An ant said: 'O ants! Enter your dwellings lest Solomon and his hosts crush you, while they perceive not.'"

This single verse contains the **canonical ant-narrative** that gives the surah its name. F-09 audits the verse-level lexical distinctiveness: how many tokens in this single verse are corpus-wide hapaxes or near-hapaxes? Is Q 27:18 verse-level **lexically distinctive** vs corpus-baseline single verses?

This complements Q027-F-01 (corpus-wide *naml*-token concentration: 100% in Q 27); F-09 narrows the lens to a single VERSE and audits its distinctive-token DENSITY.

## 1. Hypothesis (locked before observation)

**H1.a — verse hapax count**: Among the locked candidate tokens in Q 27:18 — `نملة`, `النمل` (×2 = 2 occurrences in v.18), `مساكنكم`, `يحطمنكم`, `وجنوده` — at least **3 are corpus-wide hapaxes** (count == 1).

**H1.b — verse lexical-distinctiveness percentile**: Q 27:18's "verse-distinctiveness score" — defined as (# unique tokens in verse) / (# tokens in verse), with each unique-token weighted by inverse corpus-document-frequency (IDF on token-orthographic level) — is in the **top 10%** of verses corpus-wide (high distinctiveness). Direction one-sided upper-tail.

**H1.c — sentence-internal vocative-verb construction**: The verb `يحطمنكم` (yaḥṭimannakum, "let-them-not-crush-you") is corpus-wide hapax in this energetic-emphatic-nūn (nūn al-tawkīd) form. Pre-committed prediction: corpus-wide count of `يحطمنكم` == 1.

**H0.a**: < 3 hapaxes in the locked candidate set.
**H0.b**: Q 27:18 is at-or-below 90%ile of verse-distinctiveness.
**H0.c**: `يحطمنكم` count > 1 corpus-wide.

## 2. Operational definitions

- **Locked candidate token list** for H1.a (5 unique tokens, 6 occurrences, locked-before-observation):
  - `نملة` (one ant — feminine singular indefinite)
  - `النمل` (the ants — definite plural; appears 2x in Q 27:18)
  - `مساكنكم` (your dwellings — masāqin + plural-2nd-person possessive)
  - `يحطمنكم` (let-them-not-crush-you — emphatic verb form)
  - `وجنوده` (and his hosts — wāw + junūd + 3rd-singular possessive)
- **Verse distinctiveness score** for H1.b:
  - Tokenize each corpus verse (no-tashkeel, ws-split).
  - Compute corpus token-IDF: IDF(t) = log(N_verses / df(t)), where df(t) = #verses containing token t.
  - Verse score = mean IDF(t) over t in unique(verse_tokens). Higher = more distinctive.
  - Compute the percentile rank of Q 27:18's score among all 6236 corpus verses.
- **`يحطمنكم` corpus-wide count**: orthographic-exact-match search across `quran-text/quran-no-tashkeel.json`.

## 3. Test statistics

- **stat_a** = #(locked tokens with corpus-wide-count == 1).
- **stat_b** = percentile rank of Q 27:18's verse-distinctiveness score among 6236 verses.
- **stat_c** = corpus-wide count of `يحطمنكم`.

## 4. Direction (LOCKED before observation)

- H1.a: stat_a ≥ 3.
- H1.b: stat_b ≥ 90.
- H1.c: stat_c == 1.

## 5. Permutation null (deterministic-where-possible)

H1.a, H1.c: deterministic counts.

H1.b: rank-percentile within 6236 corpus verses; deterministic.

For sanity-check power, an OPTIONAL null for H1.b — random 9-token verses constructed by sampling without replacement from the corpus token distribution; 10000 perms; seed 20260507 — to confirm the rank-percentile is not artifact of verse length.

## 6. Bonferroni and acceptance

- bonferroni_k = 5; α_bon = 0.01.
- **Acceptance windows** (LOCKED before observation):
  - **CONFIRMED** = H1.a AND H1.b AND H1.c all PASS.
  - **DIRECTIONAL** = 2 of 3 PASS.
  - **MIXED** = 1 of 3 PASS.
  - **NULL** = 0 of 3 PASS.

## 7. Rules-tuple

`(no-tashkeel, orthographic-exact-match for tokens; orthographic-tokens for IDF, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Token list locked from Q 27:18 verse text (verified by reading verse `id=18` from the JSON).
- IDF computed on the fly; no external pre-computed IDF used.

## 9. Honest a-priori limits

- The locked token list is small (5 unique forms); a longer list might surface more hapaxes. The 5-token list is a-priori-locked to avoid garden-of-forking-paths.
- IDF on orthographic tokens is sensitive to inflection (every inflectional variant is a separate token). This is exactly the rules-tuple convention; alternative QAC-root-IDF would yield a different (and likely lower) distinctiveness rank, since the root *n-m-l* is less rare than the inflected forms.
- The `يحطمنكم` verb form combines (a) energetic-nūn al-tawkīd + (b) 2nd-plural object suffix; the combined form is rare across the corpus. The pre-commit is for the surface form, not the root.
- Q 27:18 has 19 tokens (ws-split, no-tashkeel); IDF mean is sensitive to outliers. We report median-IDF as a sensitivity metric.
- 6236-verse population is the full corpus; the percentile estimate is exact.

## 10. Cross-references

- Q027-F-01 (corpus-wide *naml* concentration, CONFIRMED) — F-09 narrows to verse level.
- Q027-F-06 (hud-hud narrative-block hapax inventory) — companion verse-level test.
- al-Rāzī *Mafātīḥ al-ghayb* on Q 27:18 (the ant-narrative theological discussion).

## 11. Garden-of-forking-paths log

- 5-token list locked pre-observation. No post-hoc additions allowed.
- 90%ile cutoff for H1.b is pre-committed.
- The IDF metric uses orthographic tokens (the project's default rules-tuple), not roots. This is locked.
- The reverse direction for H1.b (Q 27:18 in BOTTOM 10%, i.e., lexically generic) would be a pre-commit violation.
