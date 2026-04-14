# Quranic Arabic Corpus — Morphological Features

**Source:** https://corpus.quran.com/documentation/morphologicalfeatures.jsp
**Project:** Quranic Arabic Corpus, Language Research Group, University of Leeds
**Maintainer:** Kais Dukes (originally), now quran.com team
**License:** GNU public license
**Fetched:** 2026-04-12

## Overview

Arabic's intricate morphology allows single words to function as complete English sentences. The example "fajaʿalnāhum" (فَجَعَلْنَٰهُمُ) from verse 23:41 demonstrates this: "and We made them" comprises four morphological segments—a prefix, stem, and two suffixes—each receiving its own part-of-speech tag.

## Morphological Segmentation

Words consist of optional prefixes, a required stem, and optional suffixes. For instance, "fajaʿalnāhum" breaks down as:
- _fa_ (conjunction prefix)
- _jaʿal_ (verb stem)
- _nā_ (subject pronoun suffix)
- _hum_ (object pronoun suffix)

Rarely, words contain two stems functioning as contractions, such as عَن + مَا = عَمَّ in verse 78:1.

## Prefix Features

The corpus identifies multiple prefix types:

| Feature | Name | POS/Description |
|---------|------|-----------------|
| Al+ | Determiner | "the" prefix |
| bi+ | Preposition | "by," "with," "in" |
| ka+ | Preposition | "like" or "thus" |
| ta+ | Preposition | Oath particle ("by Allah") |
| sa+ | Future particle | Indicates future action |
| ya+, ha+ | Vocative particles | "O" and "Lo!" |
| A:INTG+, A:EQ+ | Alif particles | Interrogative and equalization |
| w:CONJ+, w:REM+, w:CIRC+, w:SUP+, w:P+, w:COM+ | Wāw particles | Six distinct functions |
| f:REM+, f:CONJ+, f:RSLT+, f:SUP+, f:CAUS+ | Fā particles | Five distinct functions |
| l:P+, l:EMPH+, l:PRP+, l:IMPV+ | Lām particles | Four distinct functions |

## Roots and Lemmas

"Triliteral or quadriliteral" roots consist of consonants creating related word families. For example, the root ك ت ب generates "write," "book," "author," and "library."

Lemmas group inflectionally-related words without derivational changes. The corpus employs:
- **ROOT:** (triliteral root, e.g., ROOT:ktb)
- **LEM:** (lemma form, e.g., LEM:kitaAb)
- **SP:** (special grammatical rules)

Verbs reference only roots; nouns, adjectives, and proper nouns include both roots and lemmas; particles use only lemmas.

## Person, Gender, and Number

| Feature | Values | Description |
|---------|--------|-------------|
| Person | 1, 2, 3 | First, second, third |
| Gender | M, F | Masculine, feminine |
| Number | S, D, P | Singular, dual, plural |

Notation concatenates these features (e.g., 3MS = third person masculine singular; 2D = second person dual).

## Verb Features

**Aspect features:**
- PERF (Perfect/completed action)
- IMPF (Imperfect/ongoing action)
- IMPV (Imperative)

**Mood features:**
- IND (Indicative, default)
- SUBJ (Subjunctive)
- JUS (Jussive)

**Voice features:**
- ACT (Active, default)
- PASS (Passive)

**Form features:** Roman numerals I–XII indicating derivational patterns

## Derived Nouns

| Feature | Arabic Name | Description |
|---------|------------|-------------|
| ACT PCPL | اسم فاعل | Active participle |
| PASS PCPL | اسم مفعول | Passive participle |
| VN | مصدر | Verbal noun |

## Nominal Features

**State features:**
- DEF (Definite state)
- INDEF (Indefinite state, marked by _tanwīn_)

**Case features:**
- NOM (Nominative)
- ACC (Accusative)
- GEN (Genitive)

The Al+ prefix marks the determiner "the."

## Suffix Features

The corpus identifies:
- **PRON:** compound tags for attached pronouns (e.g., PRON:3MS for third person masculine singular possessive/subject/object pronouns)
- **+VOC** for vocative suffix (with _allāh_)
- **+n:EMPH** for emphatic _nūn_
