---
finding_id: Q071-F-05
title: Q 71 Noah-prayer density — petitionary-vocative concentration vs corpus baseline
parent_finding: NEW (no prior parent in MASTER-LEDGER); thematically related to H-NEW-86 framework for Q 14
date_pre_registered: 2026-05-09
seed: 20260509
agent: Q 71 Nūḥ specialist (Waiel Al-Shujaa)
test_type: per-verse-density rank vs corpus distribution
bonferroni_family: Q071-novel-tests-2026-05-09
bonferroni_k: 5
alpha_bon: 0.01
direction_locked: Q 71's petition-vocative density (rabb-prefixed tokens + duʿāʾ verbs) ranks in the corpus top-10
acceptance_window: rank ≤ 10 / 114 surahs by petition-density
mw5_positive_control: Q 14 Ibrāhīm (the corpus-MAX 7-verse window per Q014-F-01 already at 14.95 prayer-tokens/100 words)
mw7_internal_check: cross-verify token list against ʿAbd al-Bāqī Quranic concordance
---

# Q071-F-05 — Q 71 Noah-prayer density corpus-rank

## 1. Hypothesis

Q 71 Nūḥ contains a corpus-extreme density of petitionary-prayer markers
(rabb-prefixed vocatives, the verbal noun duʿāʾ, the imperative iġfir, etc.),
reflecting the surah's structural function as a sustained record of Noah's
prophetic complaint and intercession.

The surah is structured as TWO petition-blocks:
- vv. 5-9: Noah reports his ongoing call (يا ليلا ونهارا "by night and day")
- vv. 21-28: Noah's CLOSING two-fold prayer (rabb la tadhar... rabb ighfir li...)

## 2. Pre-committed direction

Q 71's petition-density (per token, normalized to 100 tokens) ranks in the
top-10 of the 114 surahs.

## 3. Method

- **Corpus**: Hafs-Kūfan no-tashkeel, basmala-counted-only-in-Q1.
- **Petition-marker token-set** (locked):
  - `رب` (rabb, exact-token vocative)
  - `ربكم` (rabbakum)
  - `ربي` (rabbī)
  - `ربك` (rabbaka)
  - `ربنا` (rabbanā)
  - any token starting with `دع` (call/invoke) — root د-ع-و
  - any token starting with `استغف` or `اغف` (forgive — root غ-ف-ر) in imperative/cohortative
- **Per-surah density** = (sum of petition-marker tokens) / (total tokens in surah) × 100.
- **Rank**: surahs sorted descending by density; Q 71's rank reported.

## 4. Acceptance window

- Q 71 rank ≤ 10 / 114 → **PASS-DIRECTED**.
- Q 71 rank ≤ 20 / 114 → **DIRECTIONAL**.
- Q 71 rank > 20 / 114 → **NULL**.

## 5. Garden-of-forking-paths

- The token-set is locked PRE-OBSERVATION at the level of root-skeleton matching;
  surface-form variability (e.g., ربك vs ربكم) is COVERED via a fixed enumeration.
- Density-normalization on TOKENS (not VERSES) is locked because verse-length
  differs systematically across surahs.
- The locked acceptance bar is rank ≤ 10 (top 9% of corpus). This reflects
  the qualitative observation that the surah is petition-saturated; the bar
  is conservative-relative-to-impression but not extremized.

## 6. Independent-replication notes

A natural replication would test this on Q 14:35-41 (the 7-verse Ibrāhīm Mecca-prayer
window, which Q014-F-01 already established as corpus-MAX 7-verse window).
Q 71 should rank similarly high under this token-set.

## 7. Honest disclosure

- The petition-marker token-set is BROAD (8+ surface forms) and may inflate counts
  in any surah where rabb is used in narrative-third-person. Q 71's first-person-Noah
  framing is the SEMANTIC anchor, but our test is at the TOKEN-SURFACE level only;
  we do NOT distinguish first-person petition from third-person mention.
- Surahs like Q 1 al-Fātiḥa (rabb-vocative density extreme in 7 verses) and Q 12
  Yūsuf (Joseph's prayer at Q 12:101) may also rank high; Q 71's claim is COMPARATIVE
  not ABSOLUTE.

## 8. Cross-references

- [[Q014-ibrahim/06-novel-findings|Q014-F-01]] — Mecca-prayer 7-verse-window MAX.
- [[Q010-yunus/00-overview|Q 10 Yūnus]] — comparison: prophet-named with prayer at v. 88.
- 02-content-analysis.md §3 — Q 71 dual-petition narrative architecture.
- 06-novel-findings.md Q071-F-05 — result.
