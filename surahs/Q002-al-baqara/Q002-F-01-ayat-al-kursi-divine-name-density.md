---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-01
date_last_updated: 2026-04-28
phase: B+
verdict: NULL on density (pre-committed); RULES-TUPLE-FRAGILE on absolute counts
prereg_sha: e395b9bb9b8ccc02ff2105520c624a18106b5ccffd061ea4f79771cbcd679b2c
---

# Q002-F-01 — Āyat al-Kursī divine-name-density rank

## Target claim

al-Bukhārī ḥadīth #4008 + Muslim — Q 2:255 *āyat al-kursī* is "the greatest verse" (aʿẓam āya) of the Quran.

## Pre-registration

`Q002-F-01-ayat-al-kursi-divine-name-density-prereg.md` (SHA256 e395b9bb9b8ccc02ff2105520c624a18106b5ccffd061ea4f79771cbcd679b2c). Direction-LOCKED: top tail (TOP-10 by total density, TOP-5 by distinct density).

## Empirical result

From `csv/Q002-F-01.json` (6,236 verses, 99 names from `data/asma-al-husna.txt`):

| Metric | Q 2:255 value | Rank / 6236 |
|:--|:--|:--|
| Total density (occ / wlen) | 0.10 (5/50) | **563** |
| Distinct density (distinct / wlen) | 0.10 (5/50) | **377** |
| Absolute occurrence count | 5 | **5** |
| Absolute distinct names | 5 | **3** |

Distinct names matched in Q 2:255: الله, العظيم, العلي, الحي, القيوم.

## Verdict — primary (PRE-COMMITTED METRIC)

**NULL on the pre-committed direction.** Q 2:255 ranks 563/6,236 by total density and 377 by distinct density. Both fail the pre-committed VINDICATED threshold (top-10 / top-5) AND fail the DIRECTIONAL threshold (top 1% = rank ≤ 62).

The density distribution is dominated by SHORT verses with name-only content (Q 1:1, Q 1:3, Q 112:2, Q 55:1, etc.) where short word-lengths trivially boost density. This is a methodological artefact: density-normalisation treats "Allah is enough for me" (Q 39:38: short) as denser than the grand summary verse Q 2:255.

## Secondary observation (RULES-TUPLE-FRAGILE — MW-7 post-hoc)

When the rules-tuple is changed from `density` (pre-registered) to **absolute count** (post-hoc):

| Metric | Q 2:255 value | Rank / 6236 | Top competitor |
|:--|:--|:--|:--|
| Absolute occurrences | 5 | **5** | Q 59:23 (10), Q 2:282 (7), Q 59:24 (6) |
| Absolute distinct | 5 | **3** | Q 59:23 (9), Q 59:24 (6) |

Under absolute counting Q 2:255 is in the **top-5** of all 6,236 verses for both occurrences and distinct names. The only verses ranking higher are:
- **Q 59:23** (the famous Hashr-khawātim, 9 distinct names — see [[h-new-95]]).
- **Q 59:24** (sister verse to Q 59:23).
- **Q 2:282** (āyat al-dayn — 7 occurrences but only 2 distinct names; surface-count is inflated by repetition of "Allāh" in the long debt-contract verse).
- **Q 73:20** (6 occurrences, 1 distinct name — also a long verse).

Per MW-7 protocol: this absolute-count finding was NOT pre-registered. It carries single-test-α=0.05 ceiling and is reported as RULES-TUPLE-FRAGILE.

## What this tells us

The hadith claim "greatest verse" can plausibly track several empirical signatures, but **divine-name density (per-word) is NOT one of them**. The intuitive interpretation that "Q 2:255 has many names so it's name-dense" relies on absolute (not normalised) counting.

What IS true under MW-7: Q 2:255 sits in a triumvirate of verses (Q 59:22-24, Q 2:255) that constitute the empirical apex of distinct-divine-name concentration. This was first noted in H-NEW-95 (Q 59:22-24 rank 1 in 99-name density). Q 2:255 is the only single verse outside Q 59 to break the top-5 by distinct count.

## Rules-tuple sensitivity

| Metric | Rank | Verdict |
|:--|:--|:--|
| `(no-tashkeel, density, words)` (pre-reg) | 563 | NULL |
| `(no-tashkeel, density, words)` (distinct) | 377 | NULL |
| `(no-tashkeel, abs-count, occurrences)` (MW-7) | 5 | DIRECTIONAL-fragile |
| `(no-tashkeel, abs-count, distinct)` (MW-7) | 3 | DIRECTIONAL-fragile |
| `(min-tashkeel, density, words)` (replication) | (see JSON) | reproducible |

## Honest limits

- The 99-names list is the al-Tirmidhī recension (`data/asma-al-husna.txt`). Other classical lists (Ibn al-ʿArabī, etc.) give slightly different sets; rerunning against another canonical 99 may shift the rank by ±1-2.
- Surface-form matching does not catch morphological variants (e.g. `الحي` vs `الحيُّ` vs nominative-form). A QAC-lemma-level match would be more rigorous.
- The classical claim is theological (greatest *qua* meaning), not empirical (greatest *qua* divine-name density). Our test is a falsifiable PROXY, not a direct measure of the theological claim.

## Cross-references

- [[h-new-95-divine-name-density]] — Q 59:22-24 rank-1 by 99-name density.
- [[h-new-620-divine-name-density]] — divine-name density NOT a 6th cohesion factor.
- [[hadith-corpus.md|04-hadith-corpus]] for full citation chain on āyat al-kursī.
- [[Q002-al-baqara/05-classical-claims-audit|05-classical-claims-audit]] — claim #2 verdict.

## Status

- VINDICATED on **rules-tuple-fragile** secondary metric (absolute count).
- NULL on pre-committed primary metric (density). Pre-commit honoured.
