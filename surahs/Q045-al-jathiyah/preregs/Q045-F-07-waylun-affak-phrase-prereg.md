---
prereg_id: Q045-F-07
title: *waylun li-kulli affāk* phrase corpus-uniqueness check (Q 45:7-8)
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-07 — *waylun li-kulli affāk* corpus-uniqueness

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The phrase **ويل لكل أفاك** (*waylun li-kulli affāk*) appears in *exactly one* locus in the Quranic corpus, at Q 45:7. The closely-related root attestation pattern (*ʾ-f-k* = `Afk`) and the *waylun* opener pattern intersect at this single point.

Secondary direction-lock: the phrase **affāk athīm** (the standard Q 45:7 collocation) is also corpus-unique to Q 45:7.

## 2. Null / negation

**H0**: The phrase ويل لكل أفاك appears more than once, OR not at Q 45:7.

## 3. Operationalization

- Source: `quran-text/quran-no-tashkeel.json`.
- Primary search: `ويل لكل أفاك` (exact substring).
- Secondary search: `أفاك أثيم` (the collocation).
- Cross-reference: enumerate all *waylun li-kull* attestations (= ويل لكل) and all *affāk* attestations (= أفاك) separately.

## 4. Direction lock

Pre-committed: **ويل لكل أفاك unique at Q 45:7**, **أفاك أثيم unique at Q 45:7**.

## 5. Bonferroni

k=3 (Q 45 family). α_corrected = 0.0167. Test is exact-locus.

## 6. Success / failure criteria

- **VINDICATED**: both phrases corpus-singleton at Q 45:7.
- **PARTIAL**: one phrase corpus-singleton.
- **NULL_OR_DISCREPANCY**: neither phrase corpus-singleton at Q 45:7.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q045-F-07.json`: waylun_lakulli_affak_loci, affak_athim_loci, waylun_lakull_all_loci, affak_all_loci, verdict.

## 9. Rationale

Q 45:7 is one of two *waylun li-kull* opener-warnings in the corpus (the other being Q 83:1, *waylun lil-muṭaffifīn*). The collocation *affāk athīm* ("habitual liar, sinner") is a sound-paired rhyme classically cited as iʿjāz al-fāṣila (al-Bāqillānī tradition). Locking the corpus-uniqueness of the phrase tests whether this is a *Q 45 signature* or a corpus pattern.

## 10. Honest limits

- Surface-form match (no-tashkeel); under min-tashkeel the search would behave identically because the consonantal skeleton is stable.
- The semantic claim ("affāk" = "habitual liar") is from classical tafsir (al-Ṭabarī ad. loc.) and is not empirically tested here — only the orthographic-token uniqueness.
