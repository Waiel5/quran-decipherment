---
finding_id: Q024-F-06
title: "Q 24:35 'Allāh nūr al-samāwāti wa-l-arḍ' — the only cop-less identity nominal equating Allāh with nūr"
date_pre_registered: 2026-05-09
status: PRE-REGISTERED
seed: 20260509
n_perm: not-applicable (string search)
bonferroni_k: 4
alpha_raw: 0.05
alpha_bonferroni: 0.0125
direction: Q 24:35 is the unique cop-less identity-nominal equating Allāh = nūr in the corpus
---

# Q024-F-06 — Q 24:35 is the unique *Allāh = nūr* cop-less identity nominal in the corpus

## Hypothesis (LOCKED before observation)

Classical Arabic nominal sentences (*jumla ismiyya*) of the form *mubtadāʾ + khabar* (subject + predicate) without an overt copula identify the subject with the predicate. The construct *Allāhu nūru al-samāwāti wa-l-arḍ* — "Allāh is the light of the heavens and the earth" — at Q 24:35 is such a cop-less identity nominal predicating *nūr* directly of Allāh.

The pre-registered claim is that this construction — `Allāh + nūr` as identity-nominal (NOT as preposition-object or partitive) — appears **exactly once** in the entire 6,236-verse Quranic corpus, at Q 24:35.

This is a uniqueness claim, not a frequency claim. It is the kind of claim that classical mufassirūn (al-Ghazālī in *Mishkāt al-Anwār*, al-Rāzī in *Mafātīḥ*) treat as theologically distinctive but rarely state empirically.

## Method (LOCKED)

Stage 1 — surface search.
- Search the no-tashkeel corpus (`quran-text/quran-no-tashkeel.json`) for the bigram `الله نور` (Allāh nūr, adjacent tokens) and variant `نور الله` (nūr Allāh, reversed).
- Record all hits with surah, verse, and surrounding context.

Stage 2 — syntactic classification (PRE-LOCKED CATEGORIES).
- Each hit is assigned one of four categories:
  - **I-NOM (identity nominal)**: subject-predicate construction equating Allāh with *nūr* without copula. Pre-registered count: 1, at Q 24:35.
  - **PARTITIVE (min + Allāh + nūr)**: *min-Allāhi nūr* = "from Allāh, a light" — the *nūr* is a thing originating from Allāh, not Allāh himself.
  - **GENITIVE (nūr Allāh)**: *nūr Allāh* = "Allāh's light" — light belongs to Allāh as a possessed attribute.
  - **PREDICATE-CHAIN**: *Allāh* and *nūr* appear adjacent but as part of a longer noun-phrase chain that does not constitute identity.

Each category assignment is made by the syntactic structure visible in the verse — adjacency-of-tokens is necessary but not sufficient for I-NOM classification.

Stage 3 — cross-validation.
- Verify the I-NOM categorization in min-tashkeel and full-tashkeel variants. The diacritics in min/full-tashkeel (nominative-case markers on *Allāhu* and *nūru*) confirm or falsify the nominal-sentence reading.

## Rules-tuple (LOCKED)

`(no-tashkeel for surface search, min-tashkeel + full-tashkeel for case-marking verification, orthographic-token adjacency, Hafs-Kufan, mushaf-order)`

## Direction (LOCKED)

The direction is uniqueness: Q 24:35 is the ONLY I-NOM. If any other verse in the corpus is also classified I-NOM after applying the locked syntactic criteria, the uniqueness claim is FALSIFIED.

## Success criteria

- Exactly one I-NOM hit, at Q 24:35: **CONFIRMED**.
- Two or more I-NOM hits: **FALSIFIED** with the contradicting verses reported.
- Zero I-NOM hits (i.e., Q 24:35 itself fails the syntactic test): **NULL with paradox flag** (would require re-reading Q 24:35).

## Honest limits (pre-registered)

- The corpus may contain *Allāh + nūr* constructions broken by intervening particles (e.g., conjunction, demonstrative). These will be tagged "DISCONTIGUOUS" and reported descriptively but are not counted in the contiguous-bigram search of Stage 1.
- The Sahih International English translation may use the gloss "Allāh is the Light" for verses that do not have the Arabic identity-nominal structure (e.g., Q 5:15 reads "there has come to you from Allāh a light" — partitive, not identity). The test is on the Arabic syntactic structure, not the translation.
- The QAC v0.4 morphological tagging marks *Allāh* as PN (proper noun) and *nūr* as N (noun) but does not explicitly label nominal-sentence structure. The classification is therefore syntactic-by-inspection of the Arabic text, not parser-output. This is documented and is acceptable for a single-verse-vs-corpus uniqueness test where the corpus has at most a handful of candidates.

## Seed

20260509 (not used for permutation; logged for reproducibility)

## Pre-registration SHA256

Computed at write-time; embedded in `Q024_F_06_allah_nur_unique.py` and verified at runtime.
