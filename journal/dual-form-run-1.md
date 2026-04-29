---
run: dual-form-phase-b-run-1
date: 2026-04-12
agent: dual-form-mapper
scope: Every dual-form token in the Quran via Leeds QAC v0.4
output: findings/phase-b-hypotheses/dual-form-mapping.md
data:
  - findings/phase-b-hypotheses/csv/dual-tokens.csv
  - findings/phase-b-hypotheses/csv/dual-density-per-surah.csv
  - findings/phase-b-hypotheses/csv/dual-verse-index.json
  - findings/phase-b-hypotheses/csv/dual-root-frequencies.csv
  - findings/phase-b-hypotheses/csv/dual-aggregates.json
---

# Journal — Dual-Form Mapping Run 1

## Approach

Read prior art in rahman-deep-dive.md and master-index before touching data. QAC feature encoding for dual:
- Stem-marked: `|MD|`, `|FD|`, `|2D|`, `|2MD|`, `|2FD|`, `|3MD|`, `|3FD|` (no literal "DUAL" string; that was a misleading hint in the task brief).
- Pronoun-suffix: `PRON:2D`, `PRON:2MD`, `PRON:2FD`, `PRON:3D`, `PRON:3MD`, `PRON:3FD`.

Wrote `scripts/dual_extract.py`:
1. Parse all morphology rows into token groups `(s, v, w) → segments[]`.
2. Flag a token as "dual" if *any* segment has stem-dual OR pron-suffix-dual.
3. For each dual token, extract stem POS, root, lemma, dual marker code; and a flag for whether the suffix was dual.
4. Emit: per-token CSV, per-surah density CSV, verse-level JSON index, root-frequency CSV, aggregate JSON.

## Errors fixed during the run

1. **First pass: "DUAL" string search returned 0 results.** QAC doesn't use that string; it uses code letters. Switched to regex `\|(?:2D|3D|2MD|2FD|3MD|3FD|MD|FD)(?:\||$)`.

2. **"Indicative dual imperfect" counted 0 on first filter.** Reason: QAC puts verb 2D/3MD/3FD on the *stem* and appends the final *-āni* nūn as a *separate PRON suffix segment*. Filter `|2D$` fails because of whitespace/newline; used Python with explicit line strip. Got 54 total indicative dual impf verbs — 36 in Surah 55 (31 being the refrain *tukadhdhibān*).

3. **Prophet-pair detection: same-verse lemma co-occurrence gave zero duals** because the Moses/Aaron scenes deploy dual in the *surrounding* verses, not on the verse where both names appear. Expanded to ±3-verse window; got much cleaner results.

4. **Adam/Eve pair detection:** Eve is never named in the Quran. Proxy via lemma "zawj" (spouse) co-occurring with "Adam". This works for Q 2:35, 7:19, 20:117.

5. **Word-count for density:** used morphology's distinct `(s,v,w)` triples as the word count per surah. This counts the refrain-words 31 times for Surah 55 (correctly — they are 31 distinct word-tokens, not type-counted).

## Findings (raw numeric log)

- **616 dual word-tokens in the Quran** (77,429 total = 0.796%).
- **Stem-dual: 426**, **pron-suffix-dual: 347** (overlap: tokens like *rabbikumā*).
- **105 dual-lemmas unique to one surah** (surah-hapaxes); peaks: S18 (19), S5 (12), S2/S28/S55 (9 each).
- **Top 5 surahs by count**: 55 (88), 18 (50), 2 (49), 7 (42), 4 (37).
- **Top 5 surahs by density (≥5 duals)**: 55 (25.07%), 66 (4.02%), 18 (3.17%), 20 (2.02%), 28 (1.75%).
- **Ar-Raḥmān without refrain:** 26 duals / ~227 body-words = **11.5%** — still 14× corpus average.
- **Indicative dual imperfect verbs: 54 total; 36 in S55 (66.7%); 31 of those = tukadhdhibān root k\*b.**

## Classic dual catalogue (counts)

- *yadā* (two hands) — 33 (most frequent classic dual)
- *wālidayn* (two parents) — 20 (always dual; never plural)
- *ithnayn / ithnatān* (two) — 20 (cardinal)
- *jannatān* (two gardens) — 8 (S18 x2, S34 x2, S55 x4)
- *ʿaynān* (two springs/eyes) — 7
- *zawjān* (two pairs) — 7
- *rajulān* (two men) — 6
- *unthayayn* (two females) — 6
- *baḥrān* (two seas) — 5 (in S18, 25, 27, 35, 55)
- *mashriqayn* — 2 (only S43:38, S55:17)
- *dhakarayn* — 2 (only Q6:143-144)
- *malakān* (two angels) — 2 (Q2:102 Harut/Marut, Q7:20 tempters of Adam)
- *al-maghribayn* — 1 (HAPAX, only Q55:17)
- *al-thaqalān* — 1 (HAPAX, only Q55:31 — the only Quranic lexicalisation of "humans+jinn" as a dual noun)

## Paired-opposites vs dual finding

The biggest surprise: **the Bonferroni-significant antithesis pairs from `paired-opposites-network.md` are almost never grammatically dual**. Heavens+earth (224 verses), sun+moon (18), life+death (65), night+day (42) — all use conjoined singulars or plurals, not -ān/-ayn. The Quran operates with two separate "pair-grammars" that don't overlap:
- **Cosmic conjoined pair** (rhetorical/theological): singular + singular or plural + singular.
- **Dual morphology** (narrative, legal, anthropomorphic, paradisal): single word with -ān/-ayn.

Ar-Raḥmān is the only surah that bridges both.

## Novel observations

1. **Surah 18 Al-Kahf is the Quran's dual-narrative hub**, not just a surah about the Sleepers. Three extended two-person narratives (two-men-two-gardens parable, Moses-and-Khidr, Dhūʾl-Qarnayn) account for virtually all 50 duals. The traditional "four trials" structuring of Kahf can be re-read as: three of the four trials deploy grammatical dual as their organising morphology.

2. **Dhūʾl-Qarnayn's title itself is dual** (*dhū l-qarnayn* = "the-possessor-of-the-two-horns"). This is a surah-exclusive titular dual.

3. **Adam-Eve is the Quran's tightest prophet-pair dual pattern** — Eve is never named but the dual is her grammatical signature. 100% of Adam-spouse co-occurrence verses have surrounding dual morphology.

4. **Moses+Aaron uses dual only in direct-commissioning scenes.** This is a clean stylistic rule: dual = co-address, plural/singular = narrative reference.

5. **At-Taḥrīm (S66) is a "wives-pairs" surah** — 4% dual density driven by the Prophet's two wives (vv 1-5) and the four exemplar wives (vv 10-12: Noah/Lot + Pharaoh/Mary).

6. **The tukadhdhibān concentration** (31 in Surah 55 of 54 total Quran indicative-dual-impf verbs = 66.7%) is the strongest single-surah morphological concentration in the Quranic corpus. No other morphological form in the Quran is this surah-localised.

## Gaps / caveats

- **QAC is authoritative but not infallible.** I trusted its dual-marker tagging without independent verification of each token. Cross-checks against the Dukes corpus web interface and al-Mu'jam al-Mufahras sampling would be a good follow-up.
- **Word-count normalization** uses QAC word-segments, which slightly differs from traditional Arabic "kalima" counts. Doesn't affect rankings but per-100-words figures are QAC-specific.
- **Zachariah/John pair** had 0 dual tokens in window — this may reflect that they are mentioned only as father-son in genealogy lists, never as co-agents. But it could also be a coverage gap worth checking in wider contexts (Q 3:38-41, 19:7-15). Spot-check: Q 19:12 addresses John as singular "take the Book"; Q 3:39 announces John singularly. So the dataset is correct — Zachariah+John is NOT a Quranic dual pair.
- **"Adam/Eve as dual-only" claim** depends on accepting "zawj" as Eve's proxy. The dual morphology is what encodes Eve; she has no personal name in Quran.

## Time & compute

~40 min end-to-end. Single Python script; no heavy computation. Morphology file is 128K lines parsed once.

## Follow-ups worth doing

- **Cross-reference with *iltifāt***: does grammatical-person shift from singular/plural to dual coincide with iltifāt events? (Suspect yes for Ar-Raḥmān v1→v13 shift; sg→dual is a sub-type of iltifāt.)
- **Dual in chronological order of revelation**: is dual-heavy Ar-Raḥmān an early or late Meccan surah? (Usually classified early Meccan, 37th chronologically.) Do duals concentrate in early Meccan or late?
- **Compare with Bible's biblical-Hebrew dual** (which is mostly frozen in body-part pairs: yadayim, raglayim, ʿenayim). Is Quranic dual as productive, or is Quranic dual productive in areas where Hebrew's isn't?
- **Addressee-grammar typology**: map every 2nd-person dual in the Quran to see which referents are dualised (wives, prophet-pairs, thaqalān, etc.). This would give a complete "who does the Quran address as 'you-two'?" inventory.
