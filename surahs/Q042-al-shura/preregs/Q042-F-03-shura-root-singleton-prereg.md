---
prereg_id: Q042-F-03
title: Root š-w-r corpus-EXACT attestation count
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T00:15:00-05:00
status: PRE-REG-LOCKED
---

# Pre-registration: Q042-F-03 — root š-w-r corpus-EXACT count

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The QAC root `$wr` (Buckwalter for š-w-r,
"consult / point") is attested **≤ 3 times** across the full 6,236-verse
corpus. The named-attestations in the brief: Q 3:159 (*shāwirhum*),
Q 42:38 (*shūrā*); any third is to be reported.

## 2. Null

**H0**: The root š-w-r is attested ≥ 4 times in the QAC v0.4 root-index.

## 3. Operationalization

- Source: `data/morphology/root-index.json` (QAC v0.4).
- Root key: `$wr` (Buckwalter); cross-checked against direct grep of
  `data/morphology/quranic-corpus-morphology-0.4.txt` for `ROOT:\$wr` lines.
- Counting unit: distinct (surah:verse:word) attestations.
- The "consult" semantic field is the *intended* target; *ashārat* (Q 19:29,
  "she pointed") shares the root but is semantically distinct ("indicate /
  point", not "consult").
- Direction: ≤ 3 stems (vindication if any of {1, 2, 3}).

## 4. Direction lock

Pre-committed: count ≤ 3 → VINDICATED ("corpus-singleton/twin/triple lexical
field"). Count ≥ 4 → NULL.

## 5. Bonferroni / k

Single test (k=1).

## 6. Success / failure criteria

- **VINDICATION**: root-count ≤ 3.
- **NULL (pre-commit violation)**: root-count ≥ 4.

If NULL, the script reports the breakdown by semantic sense (consultation
vs. pointing/indicating) so the post-hoc question "is the *consultation*
sub-field corpus-EXACT?" can be examined in a separate, post-hoc-capped
finding (Protocol §1.7, MW-7).

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q042-F-03.json` with all root-attestations + per-attestation
(surah:verse:word) + lemma + verdict.

## 9. Rationale

Sūrat al-Shūrā (Q 42) is named after a single Qurʾānic noun
(*shūrā*, Q 42:38). If the š-w-r root is corpus-sparse (≤ 3 stems), then the
surah's title is anchored on a lexeme of corpus-EXTREME rarity. Direction is
locked here before the count is read.
