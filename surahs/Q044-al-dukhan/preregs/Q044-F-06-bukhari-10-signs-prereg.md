---
prereg_id: Q044-F-06
title: Muslim 10-signs hadith citation verification (dukhān as eschatological sign)
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q044-F-06 — Muslim "10 signs of Hour" hadith verification

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The famous "10 signs of the Hour" hadith — which lists *dukhān* (smoke) as one of the eschatological signs and is classically referenced to *Sahih Muslim* — exists at hadith number **#2901** (or #2902 in some editions) in the Muslim corpus on disk, and explicitly mentions the word **دخان** (dukhān).

## 2. Null / negation

**H0**: The hadith at Muslim #2901 OR #2902 does NOT contain دخان, OR the hadith is not found at either number.

## 3. Operationalization

- Source: `data/literature/hadith/muslim*` (whatever Muslim files exist on disk).
- Search target #1: hadith #2901 — read text, check for دخان.
- Search target #2: hadith #2902 — read text, check for دخان.
- Search target #3 (corpus-wide cross-check): all 10-signs-of-hour hadiths containing both عشر and آية and دخان.

## 4. Direction lock

Pre-committed: **at least one of #2901 or #2902 contains دخان in the 10-signs context**.

## 5. Bonferroni

Single citation-verification test; α = 0.05.

## 6. Success / failure criteria

- **VERIFIED**: at least one of #2901, #2902 contains دخان and the 10-signs list.
- **VERIFIED-PARTIAL**: hadith contains دخان but is at a different number.
- **NULL**: no Muslim hadith on disk matches.

## 7. Seed

`20260509` (not used; this is a search test).

## 8. Output

JSON to `csv/Q044-F-06.json`: muslim_files_found, hadith_2901_text (preview), hadith_2902_text (preview), dukhan_attestations_in_muslim, verdict.

## 9. Rationale

Classical and modern eschatology routinely cites the Muslim "10 signs" hadith. Per the project's anti-hallucination rule (Protocol §2.11), any hadith number cited in a deliverable must be verified against disk. This pre-reg formalizes that verification for the dukhān-eschatology linkage.

## 10. Honest limits

- Hadith numbering varies across editions (Abdul-Baqi numbering vs in-book numbering); the test allows for both #2901 and #2902.
- The hadith corpus on disk may use Arabic or English; the test reads both.
- If the hadith is absent on disk, the verdict is NULL-DATA-GAP, not falsification of the classical claim.
