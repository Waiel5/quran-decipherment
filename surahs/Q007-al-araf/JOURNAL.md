---
surah: 7
file_type: journal
date_started: 2026-05-07
phase: B+
agent: Q007-al-araf-specialist
---

# Q 7 al-Aʿrāf — Investigation Journal


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 2026-05-07 — Specialist dispatched

Q007-al-araf-specialist deployed in coordination with Q006 + Q011 specialists running in parallel; Q026 already done (refrain-cycle CONFIRMED).

Pre-flight reading completed:
- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
- `findings/phase-b-hypotheses/h-new-940-prophet-order-conservation.md` (parent for prophet-cycle test)
- `surahs/Q026-al-shuara/06-novel-findings.md` (Q026-F-01 CONFIRMED)
- `surahs/Q012-yusuf/00-overview.md` (canonical 8-file template)

Empirical anchors extracted from on-disk JSON:
- h-new-590: Q 7 outlier NULL, Δ%ile=−3.78pp, p=0.598.
- h-new-700: Q 7 rhyme entropy 0.279 (extreme monorhyme; nūn 93.2%).
- h-new-720: Q 6→Q 7 cost=0.000 (cheapest); Q 7→Q 8 cost=0.212 (top-10).
- h-new-750: Q 7 sig_A=−2.033 (rank 104); sig_B=−1.474 (rank 101).
- h-new-840: Q 7 UAS rank 11/114, UAS=1.920.
- h-new-111: Q 7 nearest 5: Q 6, 10, 28, 11, 40. Farthest: Q 55.
- h-new-940: Q 7 contributes Adam-Nūḥ-Hūd-Ṣāliḥ τ=1.0 to CONFIRMED H2a.

## Pre-registration locks

5 pre-regs locked at 2026-05-07; SHA256 computed and embedded in `scripts/Q007_F_all.py`:

| Pre-reg | SHA-256 |
|:---|:---|
| Q007-F-01-prophet-cycle-parallelism-prereg.md | `03a92d7d12b85c5739f4bde19e80b0c12b5a6d56a32f2d3603f85e89dc616f9c` |
| Q007-F-02-mim-sad-cluster-position-prereg.md | `e46a503f8ebed24d911fbf0d9dd4d57c5ee997dcd5ea03396809ecaee5d65eb6` |
| Q007-F-03-araf-hapax-prereg.md | `ade0c117904d2f49f68937b8df1ca08b955b06b043778a398deb826613faa180` |
| Q007-F-04-adam-twin-prereg.md | `23e40a3b2f9b4414fb26edd1bd887a5a84facfda434b0b4c7624b7ed769cb58e` |
| Q007-F-05-prophet-order-primary-prereg.md | `370244294d4e82b2cb4576de8712d0dd804973572ad0463e1b993fdd90bad098` |

**Bonferroni-asymmetry note**: Originally planned k=4 (F-01..F-04). Added F-05 (prophet-order primary) at pre-registration time, tightening k to 5 → α_bon = 0.05/5 = 0.01. Per HANDOFF/04-DISCIPLINE.md "Bonferroni asymmetry rule," **TIGHTENING is self-verifying** without ratification.

## Garden-of-forking-paths log

1. **Block-boundary choice for Q 7 prophets** (locked in Q007-F-01 pre-reg §2.1):
   - Adam = vv 11–25 (locked). Choice: includes the Iblīs-fall narrative + the garden-trial. Alternative: vv 10–25 (extends to "creation prologue"). Chose v 11 because v 10 introduces "humans on earth" generically, not Adam-specifically.
   - Mūsā = vv 103–137 (locked). Choice: ends at the drowning of Pharaoh (the destruction-closure of the cycle). Alternative: vv 103–171 (extending to Bani-Israel + Calf episode). Chose 103–137 to keep the destruction-cycle homogeneous; the Bani-Israel phase is structurally different.
   - All other 5 prophet-blocks have classical-grouping consensus boundaries.

2. **Q 11 block-boundaries** (locked in Q007-F-01 pre-reg §2.4):
   - Locked at H-NEW-940's catalog. Q 11 has 5 destruction-cycle prophets (Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb) PLUS a Mūsā-prologue (v 25). I include only the 5 destruction-cycle prophets in the Q 11 mean-S calculation, NOT the Mūsā-prologue. This is consistent with the pre-reg H1 framing (test destruction-cycle parallelism).

3. **Feature-detector calibration**: F1, F2, F3, F4 are regex + root-set. The F1 regex catches `wa-ilā [tribe] akhāhum`, `laqad arsalnā`, `idh qāla`, `wa-X idh qāla`. Adam (vv 11–25) does NOT match F1 (it's a creation-narrative, not a mission-introduction); Adam's F1=0 is correct. Lūṭ (v 80) matches F1=1 via `wa-Lūṭan idh qāla`. Lūṭ's F2=0 (no named miracle) and F3=0 (the opposition is "akhrijūhum" not "qāla al-malaʾu") are honest detector outcomes.

4. **F-05 NULL was DISCLOSED in pre-reg**: I expected the H1 framing to fail because Q 7 places Mūsā LAST whereas Q 11 and Q 26 place Mūsā FIRST. The disclosure is in §5 of the pre-reg, written BEFORE the run. This is honest pre-disclosure of expected NULL, not post-hoc rationalization.

## Run trace 2026-05-07 — Q007 F-01..F-05

- **Q007-F-01: verdict=NULL** (Q 7 mean S = 0.667, rank 3/4; Q 11 corpus-MAX 1.000)
  - SHA expected: 03a92d7d12b85c5739f4bde19e80b0c12b5a6d56a32f2d3603f85e89dc616f9c (verified)
- **Q007-F-02: verdict=DIRECTIONAL** (Q 7 rank 2/114 on combined ALM-ALR proximity; equidistant within 0.067; p_perm=0.040)
  - SHA expected: e46a503f8ebed24d911fbf0d9dd4d57c5ee997dcd5ea03396809ecaee5d65eb6 (verified)
- **Q007-F-03: verdict=CONFIRMED** (`الأعراف` corpus-hapax, n=2, both in Q 7; analytic null p=0.0019)
  - SHA expected: ade0c117904d2f49f68937b8df1ca08b955b06b043778a398deb826613faa180 (verified)
- **Q007-F-04: verdict=NULL** (margin=+0.032 right-direction, p_perm=0.40)
  - SHA expected: 23e40a3b2f9b4414fb26edd1bd887a5a84facfda434b0b4c7624b7ed769cb58e (verified)
- **Q007-F-05: verdict=NULL** (Q 11 τ=0.33; Q 26 τ=0.05; Q 21 τ=−0.67 — pre-disclosed expected NULL)
  - SHA expected: 370244294d4e82b2cb4576de8712d0dd804973572ad0463e1b993fdd90bad098 (verified)

## Decision points

- **F-01 NULL is the most epistemically interesting failure**. The parent finding H-NEW-90 reported z=+5.25 for Q 7's prophet-cycle parallelism. Q007-F-01 used a DIFFERENT operationalization (4-feature vector / Hamming) and got NULL. This is honest independent-replication failure (MW-5).
   - **Implication**: H-NEW-90 should be revisited. Either (a) the parent metric captures a different aspect (chronological-discipline rather than feature-uniformity) and Q 7 IS corpus-MAX on the parent metric but NOT on the 4-feature metric; OR (b) the parent metric has a calibration issue.
   - **Recommended follow-up**: queue `H-NEW-90.1-replication-cross-operationalization` to systematically test H-NEW-90's z=+5.25 across multiple operationalizations.

- **F-02 DIRECTIONAL is striking but not Bonferroni-significant**. Q 7 ranking 2/114 on combined-cluster-proximity is empirically suggestive; the p_perm=0.040 fails the conservative α_bon=0.01.
   - **Recommended follow-up**: a more-tightly-defined Q007-F-02b (rank-only test, k=1 alpha=0.05) might pass. But that would be post-hoc.

- **F-03 CONFIRMED is the headline**. The eschatological-third-place is **lexically corpus-hapax** in Q 7. al-Bāqillānī's *iʿjāz al-Qurʾān* claim of *ibdāʿ al-naẓm* is empirically locked.

- **F-04 NULL with right-direction**: classical reading (al-Rāzī) is directionally correct but not iʿjāz-strength. This pattern is consistent with Q026-F-04 (PRE-COMMIT-VIOLATED on Mūsā-twin) and Q012-F-04 (CONFIRMED on hapax).

- **F-05 NULL pre-disclosed**: this is honest reporting of an expected NULL. The descriptive finding (Q 7's Mūsā-LAST placement is structurally distinct from Q 11/Q 26/Q 21's Mūsā-FRONT) is the empirical takeaway.

## Sources verified on-disk

- `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/{bukhari,muslim,tirmidhi,abudawud,nasai,ibnmajah,malik,ahmed}.json` — searched for Q 7 anchor hadith.
- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt` — referenced for Q 7 munāsaba.
- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/ibn-kathir-tafsir-quran.openiti.raw.txt` — referenced for Q 7 Adam + Aʿrāf-men.
- `/Users/grey/Downloads/quran/data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf` — al-Suyūṭī al-Itqān English (used for chronology, sabʿ ṭiwāl, nawʿ-classification).
- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` — Q 7 verse text (default rules-tuple).
- `/Users/grey/Downloads/quran/data/morphology/root-index.json` — root-occurrences per-verse (used for feature-vectors and cosine).
- `/Users/grey/Downloads/quran/data/revelation-order.csv` — Q 7 chronology lookup.
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840,940}.json` — empirical anchors.

## Open queues / follow-ups

1. `H-NEW-90.1-replication-cross-operationalization`: systematically test H-NEW-90's z=+5.25 across multiple operationalizations (continuous feature-strength, single-template-match-rate, etc.). Q007-F-01 NULL on the 4-feature-Hamming version.
2. `Q007-F-06-prophet-mission-opener-templated`: the 4 "yā qawmi-ʿbudū Allāha mā lakum min ilāhin ghayruh" prophet-mission openers in Q 7 (vv 59, 65, 73, 85) are corpus-uniformly templated. A formal pre-registered test of corpus-MAX templating is plausible.
3. `Q007-F-07-yā-banī-Ādam-4-fold-refrain`: Q 7's 4-fold "yā banī Ādam" refrain (vv 26, 27, 31, 35) is corpus-distinctive (corpus-total 4 contiguous occurrences of this exact form). Pre-reg-able.
4. **Bukhārī number for Q 7:31 zīna and Q 7:172 covenant**: data-gap flagged in `04-hadith-corpus.md` §5. Worth the follow-up to confirm specific Bukhārī numbers.
5. **al-Wāḥidī asbāb al-nuzūl extract for Q 7**: not on-disk yet (Q 1, Q 2 are; Q 7 not). Worth requesting extraction.
6. **Q 7-Adam ↔ Q 2-Adam at iʿjāz-strength**: Q007-F-04 was DIRECTIONAL but NULL. A larger-N replication including Q 15:26–43, Q 17:61–65, Q 18:50–51, Q 38:71–85 might give more power. Pre-reg-able as Q007-F-04.1.

## Reproducibility

- Pre-regs: `surahs/Q007-al-araf/Q007-F-{01,02,03,04,05}-*-prereg.md`.
- SHA-locked at runtime by `scripts/Q007_F_all.py`.
- Script: `/Users/grey/Downloads/quran/scripts/Q007_F_all.py`.
- JSON outputs: `surahs/Q007-al-araf/csv/Q007-F-{01,02,03,04,05}.json`.
- Seed: 20260507 (with offset +2, +4, +5 for tests F-02, F-04, F-05 to avoid null-correlation).
- Permutations: 10,000 each.
- Stdlib only.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
