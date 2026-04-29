---
surah: 12
test_id: Q012-F-04
title: Q 12:3 aḥsan al-qaṣaṣ self-reference position test
file_type: pre-registration
date_locked: 2026-04-28
seed: 12040
---

# Q012-F-04 — Pre-registration: aḥsan al-qaṣaṣ position

## 1. Hypothesis (locked before observation)

**H1.a (uniqueness):** The phrase أحسن القصص occurs in **exactly one verse** in the Quran, and that verse is Q 12:3.

**H1.b (head-tail framing):** The root q-s-s in Q 12 is positioned in a **head-tail bookend frame**: at least one attestation is in the first 5% of verses (≤ Q 12:6) AND at least one attestation is in the last 5% of verses (≥ Q 12:106).

**H0.a:** The phrase appears in ≥ 2 verses corpus-wide.
**H0.b:** Root q-s-s in Q 12 has no head-tail framing (no early or no late attestation).

**Direction**: H1.a strict uniqueness; H1.b head AND tail (LOCKED).

## 2. Operational definition

**Phrase test (H1.a)**: orthographic exact match `أحسن القصص` (with the space).
**Root test (H1.b)**: regex `(نقص|قصص|قصصت|قصصنا|تقصص|قصة|اقصص)` over Q 12 verse-texts; verse-position recorded as `verse_id / 111`.

**Head zone**: positions 1–6 (5.4% threshold).
**Tail zone**: positions 106–111 (95.5% threshold).

## 3. Success / Failure

- **CONFIRMED H1.a**: phrase occurs in exactly 1 verse, and that verse is Q 12:3.
- **CONFIRMED H1.b**: at least one attestation in head zone AND at least one in tail zone.
- **NULL H1.a**: phrase occurs in ≥ 2 verses.
- **NULL H1.b**: no head OR no tail attestation.

## 4. Rules-tuple

`(no-tashkeel, orthographic-token, whitespace-tokenized, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 5. Honest limits

- H1.a is a near-trivial empirical check (the *aḥsan al-qaṣaṣ* phrase is well-known to be unique to Q 12:3). Logged for completeness and rules-tuple-stability cross-check.
- H1.b is the substantive test: does Q 12 *frame* itself with q-s-s at both ends, supporting a deliberate-architecture reading of the surah?
- Cross-validation across 3 tashkeel variants (no/min/full) is required for the verse-text quotation in the findings file.

## 6. SHA256 lock

Embedded at run-time in `scripts/Q012_F_04_self_reference.py`.
