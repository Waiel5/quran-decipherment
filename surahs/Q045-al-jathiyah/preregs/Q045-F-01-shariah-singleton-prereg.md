---
prereg_id: Q045-F-01
title: Q 45:18 *sharīʿa* noun-singleton corpus uniqueness
date: 2026-04-28
seed: 20260428
locked_at: 2026-04-28T03:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q045-F-01 — *sharīʿa* singleton at Q 45:18

## 1. Hypothesis (direction-locked)

**H1 (deterministic singleton)**: The orthographic-noun-form *شريعة* (sharīʿa, "ordained-path / law") appears in **exactly one** verse of the Qurʾān: Q 45:18, in the construction *thumma jaʿalnāka ʿalā sharīʿatin min al-amr*.

Sub-claim **H1b (root-distribution)**: Of the corpus's verb-form attestations of root ش-ر-ع (Q 5:48 *sharaʿa lakum / shirʿa*; Q 7:163 *shurraʿan / shurʿan*; Q 42:13 *sharaʿa lakum mina al-dīni*; Q 42:21 *sharakāʾu sharaʿū lahum*), **none** uses the noun *sharīʿa* form. Q 45:18 is the noun-form singleton.

## 2. Null

**H0**: The string *شريعة* appears in 0 or in ≥2 verses.

## 3. Operationalization

- Tashkeel level: **no-tashkeel** (default rules-tuple).
- Source corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Search method: exact substring match `شريعة` against each verse's text field.
- Cross-validation: re-run with `min-tashkeel` and `full-tashkeel` variants — the orthographic-noun root-letters are unaffected by tashkeel; rules-tuple-stable check.
- Sub-claim H1b: enumerate all verses containing the substring `شرع` and classify by part-of-speech using QAC v0.4 morphology features (`/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`).

## 4. Direction lock

Pre-committed direction: **exactly one verse contains *شريعة* and that verse is Q 45:18**.

If observed count is 0: **NULL — claim falsified, the noun does not appear**.
If observed count is ≥ 2: **NULL — singleton claim falsified**.
If observed count is 1 but verse ≠ Q 45:18: **PRECOMMIT_VIOLATION — direction wrong**.

## 5. Bonferroni

Single deterministic test (k=1); no multiplicity correction.

## 6. Success / failure criteria

- **Success (VINDICATED)**: count == 1 ∧ verse == Q 45:18.
- **NULL**: count != 1.
- **Precommit violation**: count == 1 but verse != Q 45:18.

H1b is descriptive (no threshold); reported alongside.

## 7. Seed

`20260428`.

## 8. Output

JSON to `csv/Q045-F-01.json` with: total noun-form hits, verse-list, root-family verb-form inventory, rules-tuple-stability table.

## 9. Motivation

Classical sources note the *sharīʿa* noun-singleton (al-Rāzī, *Mafātīḥ al-ghayb*, ad Q 45:18; al-Qurṭubī, *al-Jāmiʿ li-aḥkām*, ad Q 45:18; al-Suyūṭī, *al-Itqān*, nawʿ 17 *asmāʾ al-suwar* — Q 45 is sometimes called *sūrat al-sharīʿa*). The noun form is foundational to post-Quranic *sharīʿa*-doctrinal vocabulary; if it really is a hapax-noun in the corpus, that is a structurally significant fact for the surah's classical "al-Sharīʿa" alternative-naming and for the trajectory of the term in Islamic legal theory. Empirically locking the singleton-fact is also a discipline-marker: the test is deterministic and direction-locked.
