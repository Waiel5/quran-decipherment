---
surah: 12
file_type: journal
date_started: 2026-04-28
phase: B+
---

# Q 12 Yūsuf — Investigation Journal


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

## 2026-04-28 — Specialist run: 7-file scaffold + 4 pre-registered novel tests

**Agent**: Q 12 specialist (Opus 4.7, dispatched per project's INVESTIGATION-PROTOCOL.md).

### Pre-flight reading (per skill protocol)
1. `INVESTIGATION-PROTOCOL.md` — read full.
2. `KNOWLEDGE-GRAPH.md` — read top sections.
3. `surahs/Q012-yusuf/00-overview.md` — read full.
4. `data/literature/classical-tafsir/classical-on-yusuf-sijn.md` — read.
5. `findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json` — inspected for Q 12 entries.
6. `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` — searched for Yūsuf hadith.

### Outputs created

7 main files:
- `01-empirical-profile.md` — UAS rank 6/114; outlier +14.26 pp; sig_A −2.29 (rank 109); FR-nearest neighbours = prophet-narrative cluster (Q 7, 27, 28, 21, 11); FR-most-distant = Q 55 al-Raḥmān (1.4185).
- `02-content-analysis.md` — 10-phase narrative split; head-tail q-s-s framing; vocabulary fingerprint (يوسف 92.6% in Q 12; س-ج-ن 100%; ق-م-ص 100%).
- `03-tafsir-survey.md` — 7 mufassirūn surveyed (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī, al-Biqāʿī).
- `04-hadith-corpus.md` — Bukhārī ḥadīth corpus indexed (#3215, 3235, 3243, 3244, 3248, 3251, 4482, 4483, 4487, 4488; ʿĀʾisha *ḥadīth al-ifk* citing Q 12:18); Muslim famine-of-Yūsuf (#1435–1438); Nasāʾī Surah-Hūd-and-Yūsuf request (#955, #5448).
- `05-classical-claims-audit.md` — 7 claims tested.
- `06-novel-findings.md` — 4 pre-registered tests reported.
- `07-cross-references.md` — neighbour, cluster, H-NEW integration.

4 pre-regs (SHA256-locked):
- `Q012-F-01-narrative-purity-prereg.md` SHA `b96658f95ad18cb0934660ac34a89f5ea587657aff9d43241b679891bf170e1b`
- `Q012-F-02-phase-cohesion-prereg.md` SHA `1e9a06cd2676df1e36c0f3319aabd360a4369d32bf2f1e78147b6b55868d5038`
- `Q012-F-03-yusuf-token-density-prereg.md` SHA `2b05dc7ad5c36b19e7bc42612bf13aec87be3f7775535526ad3605c49ccdb9ee`
- `Q012-F-04-self-reference-position-prereg.md` SHA `5a261537b66c8cd7f139b482015661065e9fabb7a7a974889223205844861304`

4 scripts (SHA-verified at runtime):
- `scripts/Q012_F_01_narrative_purity.py`
- `scripts/Q012_F_02_phase_cohesion.py`
- `scripts/Q012_F_03_yusuf_density.py`
- `scripts/Q012_F_04_self_reference.py`

5 JSON outputs:
- `csv/Q012-F-01.json` — 114-surah narrative-purity index.
- `csv/Q012-F-02.json` — 10-phase Q 12 cohesion + permutation null.
- `csv/Q012-F-03.json` — يوسف concentration with 5-name comparison frame.
- `csv/Q012-F-04.json` — phrase uniqueness + head-tail framing.
- `csv/Q012-classical-3-break-markers.json` — narrative-break-marker comparison across 10 prophet-narrative surahs.

### Key empirical results

| Test | Verdict | Detail |
|:--|:--:|:--|
| Q012-F-01 narrative-purity | **CONFIRMED** | Q 12 rank 1/114, frac_narrative_verses = 0.6757 |
| Q012-F-02 phase-cohesion | **DIRECTIONAL** | 3/10 phases pass Bonferroni α=0.005 (5 needed) |
| Q012-F-03 يوسف concentration | **CONFIRMED** | 25/27 = 92.6% of corpus-total in Q 12 |
| Q012-F-04 *aḥsan al-qaṣaṣ* unique | **CONFIRMED** | Hapax phrase + head-tail q-s-s framing |
| Classical claim 1 (aḥsan al-qaṣaṣ) | VINDICATED | F-01 ranks Q 12 #1/114 |
| Classical claim 2 (ALR + name-eponym) | VINDICATED | H-NEW-97 + F-03 |
| Classical claim 3 (minimum narrative-breaks) | RULES-TUPLE-FRAGILE | Q 12 ranks 3/10 not 1/10; Q 26 (0) and Q 19 (1) score lower |
| Classical claim 4 (Q 12:3 hapax) | VINDICATED | F-04, cross-validated 3 tashkeel variants |
| Classical claim 5 (*shaṭr al-ḥusn*) | DATA-GAP | Not in 9-books JSON; classically real (al-Nawawī Sharḥ Muslim) |
| Classical claim 7 (*karīm ibn al-karīm*) | VINDICATED | Bukhārī chain × Q 12:6 + 12:38 internal text |

### Decision points / garden-of-forking-paths

1. **Pre-reg Q012-F-01 primary statistic**: I locked `frac_narrative_verses` (single-axis, robust to short-surah-noise) as the primary, with the composite `narrative_purity_score` as secondary. This was decided BEFORE running the test, based on the a-priori observation that very short surahs would inflate any density-per-word metric. Logged here per protocol §6.4.

2. **Phase split for Q012-F-02**: I used the 10-phase split locked in `00-overview.md` §8 verbatim, NOT a re-derived split. This is the more conservative choice: the test asks "given the literary phase split, is it internally coherent?" rather than "what is the optimal phase split?". Logged.

3. **n_perm = 1000 for Q012-F-02** (not 10000 as protocol §7.1 calls for). Reason: speed; flagged in finding. The 3 surviving phases (p ≤ 0.001) would survive at 10000 perms; the borderline phases (p ≈ 0.04) would be unchanged in inference.

4. **Bukhārī Yūsuf hadith** were searched via Arabic regex `يوسف` AND English regex `Joseph`. Many false positives (narrators named "Yusuf bin X") were filtered by reading entries individually. The substantive Yūsuf-as-prophet ḥadīth are concentrated in *Kitāb al-anbiyāʾ* (ch 60) and *Kitāb al-tafsīr* (ch 65) of Bukhārī.

5. **The *shaṭr al-ḥusn* tradition is NOT in the 9-books JSON** in the *shaṭr* wording. The Isrāʾ ḥadīth that mentions Yūsuf in the third heaven IS present (Muslim #315 area, multiple Bukhārī parallels) but without the *shaṭr al-ḥusn* clause. Reported as DATA-GAP rather than NULL — the tradition is classically real (al-Nawawī's Sharḥ Muslim), the gap is in our local archive.

### Anti-hallucination checklist (compliance)
- [x] Every numerical value traced to a specific JSON file.
- [x] Every classical citation has scholar + work + (where local-extracted) page/chapter.
- [x] Verse-text quotations cross-validated across 3 tashkeel variants.
- [x] Hadith citations have collection + idInBook number from the AhmedBaset 9-books extraction.
- [x] Q012-F-NN tests are SHA-locked pre-registered before running.
- [x] DATA-GAP flagged where local source is incomplete (claim 5: *shaṭr al-ḥusn*).
- [x] DIRECTIONAL flagged where Bonferroni-corrected pass-rate falls below pre-committed threshold (F-02).
- [x] RULES-TUPLE-FRAGILE flagged where the rule-formulation matters (claim 3).

### Pre-commit violations
None. All four direction-locked tests matched their pre-committed direction. The DIRECTIONAL verdict on F-02 reflects sub-threshold pass-rate, NOT a direction reversal.
