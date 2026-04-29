---
id: H-NEW-83
title: Pre-registration — Q 55 al-Raḥmān refrain extension beyond 8+7+8+8
phase: B
status: PRE-REGISTERED
date: 2026-04-15
agent: h-new-83-specialist
prior:
  - findings/phase-c-structures/rahman-deep-dive.md (existing 31-refrain audit; 8+7+8+8 partition; inclusio v27/v78)
  - findings/phase-b-hypotheses/compression-and-self-reference.md (gzip z = −17.77)
  - MASTER-FINDINGS-LEDGER.md §1 #10 (locked finding)
  - MASTER-FINDINGS-LEDGER.md §3b "Refrain counts: Ar-Raḥmān 31; Al-Mursalāt 10; Al-Ṣāffāt 5"
data: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
rules: (no-tashkeel, orthographic-token, normalized hamza/alif/yāʾ/tāʾ-marbūṭa, hafs-kufan)
---

# [[h-new-83-rahman-refrain-extension|H-NEW-83]] — Q 55 Refrain Extension: Pre-Registration

## Motivation

§1-#10 in the master ledger locks the 31-refrain count and the 8+7+8+8 partition that matches classical tafsīr (al-Rāzī, Ibn ʿĀshūr). The phase-c rahman-deep-dive (2026-04-12) extended this to: (i) inclusio at v27/v78 *dhū l-jalāli wa-l-ikrām*; (ii) plosive signal localized to refrain; (iii) hell:paradise = 2:16; (iv) 4 paradises in 2 hierarchical pairs.

What remains UNTESTED that the task brief explicitly asks:
1. Is the **per-classical-block content** (the 31 inter-refrain "blessing slots") thematically coherent or noise? Specifically: do part A (8 blocks of cosmic creation), part B (7 blocks of judgment), parts C+D (16 blocks of paradise) cluster by lexical content above chance?
2. Are non-refrain verses substantially different from refrain verses on quantifiable axes (length, lexical, morphological)?
3. Do **sub-refrains** exist within Q 55 — repeating phrases other than the canonical refrain?
4. Cross-corpus: at the operational level "all 31 occupy distinct verses of the surah", is "31 occurrences" = "31 refrain-verses" identically? Are there ANY Q-corpus verses outside Q 55 that contain the refrain phrase?

## Pre-registered operationalizations

**RP-1 Refrain identity.** A verse is a refrain-verse iff its normalized text exactly matches the normalized v13 text. Normalization rules: alif variants ٱ إ أ آ → ا; alif-maqṣūra ى → ي; tāʾ-marbūṭa ة → ه; bare hamza ء → empty; hamza-on-yāʾ ئ → ي; hamza-on-wāw ؤ → و; squash whitespace.

**RP-2 Refrain count operationalization.** A refrain "occurrence" = a verse-level exact match to the normalized refrain. We ALSO test the substring count under normalization to detect any partial-verse refrains (would distinguish "31 occurrences" from "31 refrain-verses").

**RP-3 Cross-corpus refrain check.** We sweep all 6,236 verses for normalized substring of the refrain. We also sweep for the most distinctive 3-gram of the refrain (`الا ربكما تكذبان`) — a substring that would catch any near-paraphrase using the same theological language.

**RP-4 Inter-refrain block segmentation.** A "block" = the maximal contiguous span of non-refrain verses between consecutive refrains, plus the trailing refrain. Block 0 = vv 1–13 (12 non-refrain + refrain). Block k (k=1..30) = (last_refrain_verse+1)..next_refrain_verse. Block 31 = v78 alone (the coda after the last refrain at v77). Total blocks: 32 (12-verse opener + 30 inter-refrain + 1 coda).

**RP-5 Block-content statistics.** For each block we compute: (a) verse-count, (b) raw-byte length, (c) word-count, (d) unique-word-count, (e) leading-content-verse word-set. We then check whether the classical 4-part partition (vv 1–30 / 31–45 / 46–61 / 62–77) shows lower within-part variance than 1,000 random 4-cuts of the 32-block sequence.

**RP-6 Sub-refrains.** We identify any 3+ word phrase that appears at least 2 times in Q 55 and is NOT a substring of the canonical refrain. We use a simple n-gram counter on normalized tokens. Pre-declared n-gram sizes: 3, 4, 5. Pre-declared minimum count: 2.

**RP-7 Refrain-vs-non-refrain comparison.** We compute mean and stddev of (a) verse char-length, (b) verse word-count for the two pools (31 refrain verses vs 47 non-refrain verses) and report KS-test p-value on the length distributions. Pre-declared α = 0.05 unprotected; this is a descriptive contrast, not a hypothesis test for promotion.

## Pre-registered hypotheses

- **H-83a.** Refrain occurrences = 31 (FORCED by ledger; verifying tightness).
- **H-83b.** No verse outside Q 55 contains the canonical refrain (substring level).
- **H-83c.** No verse outside Q 55 contains the distinctive 3-gram `الا ربكما تكذبان`.
- **H-83d.** First refrain is at v13 (FORCED by ledger; verifying classical "first refrain at v13").
- **H-83e.** At least one sub-refrain (3+ token phrase, count ≥ 2) exists in Q 55.
- **H-83f.** The 4-part classical partition (vv 1-30/31-45/46-61/62-77) shows block-length variance significantly lower than random 4-cuts.

## Garden-of-forking-paths log (BEFORE run)

- Normalization choices fixed BEFORE running. Alternative (do-not-collapse-tāʾ) would not affect the canonical refrain since it has no tāʾ-marbūṭa-bearing word, but is logged.
- N-gram size set fixed at {3, 4, 5}.
- Block-segmentation has 3 reasonable options: (a) refrain-leading (block ends WITH refrain), (b) refrain-trailing (block starts WITH refrain), (c) refrain-isolated (refrain is its own block). RP-4 above uses option (a). Sensitivity to (b) and (c) NOT pre-registered; if reported, will be marked exploratory.
- 1,000 random 4-cuts uses fixed seed 20260415.
- KS test is two-sided.

## Deliverables

- `/Users/grey/Downloads/quran/scripts/h_new_83_rahman_refrain_extension.py` (run)
- `/Users/grey/Downloads/quran/journal/h-new-83-run-1.md` (raw log)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension.md` (final report)

## Status

PRE-REGISTERED. Will execute immediately after this commit.
