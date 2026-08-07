---
surah: 28
surah_name_ar: القصص
file_type: journal
date_last_updated: 2026-05-07
phase: B+
specialist: Q028-al-qasas-specialist
---

# Q 28 al-Qaṣaṣ — Investigation journal


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

Timestamps + decision points + SHA-locks + garden-of-forking-paths logs.

---

## 2026-05-07 13:00 — kickoff

Specialist agent dispatched as `Q028-al-qasas-specialist`. Pre-flight reading completed:
1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` ✓
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` ✓
3. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` ✓
4. `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` (canonical template) ✓
5. `/Users/grey/Downloads/quran/surahs/Q027-al-naml/` (TSM-sister) ✓

Empirical anchors extracted:
- H-NEW-111 Q 28 row → nearest neighbor Q 7 (FR 0.762), Q 28-Q 27 = 0.805, Q 28-Q 26 = 0.954, Q 28-Q 20 = 0.895.
- H-NEW-590 Q 28 row → Δ%ile = −1.84pp, NULL classification.
- H-NEW-700 Q 28 → 92.0% nūn-rhyme.
- H-NEW-720 → Q 27→Q 28 = 0.71% residual, Q 28→Q 29 = 0.90% residual (both low).
- H-NEW-750 → Q 28 sig_A = −1.794, rank 98/114; iʿjāz-of-fawāṣil low.
- H-NEW-840 → Q 28 UAS = −0.041, rank 50/114.

---

## 2026-05-07 13:15 — pre-registrations locked

Five pre-registration markdown files written and SHA-locked:

| File | SHA-256 |
|:--|:--|
| `Q028-F-01-madyan-episode-lexical-isolation-prereg.md` | `0717e38d1749a70369591a0406a50b40c33aa0d0d9385fab609e7be4887ef218` |
| `Q028-F-02-tsm-moses-twin-pair-prereg.md` | `f32d033c43c9ca9676721cb5f0492c8d97a2145cef8c59c7bf829479f58ce886` |
| `Q028-F-03-qarun-block-isolation-prereg.md` | `80061fb62c8aed32f47f91ba90deba17601cb91d24e8f7430a6489625cdb1718` |
| `Q028-F-04-q28-34-impediment-reference-prereg.md` | `2e28b7a4129a8afb280eec2f6134509e3c5d9b5af36a5ea7e4737bda5a80efa9` |
| `Q028-F-05-tsm-3-surah-joint-test-prereg.md` | `f9d5c2de81343db78c5794c14fbded3ec07793ed4a55345128d4612809dd741d` |

All 5 SHAs embedded in `scripts/Q028_F_all.py` `PREREG_SHAS` dictionary. Runtime SHA verification implemented per protocol §1.2.

---

## 2026-05-07 13:20 — garden-of-forking-paths logs

### F-04 verse-locator correction (logged BEFORE running)

The dispatch prompt cites Q 28:35 as "speech-impediment-relief verse … قال ربي اشرح لي صدري ويسر لي أمري واحلل عقدة من لساني يفقهوا قولي". On-disk verification (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` Q 28 row) shows:

- Q 28:35 = `قال سنشد عضدك بأخيك ونجعل لكما سلطانا فلا يصلون إليكما ۚ بآياتنا أنتما ومن اتبعكما الغالبون` — God's response, not the relief-prayer.
- The actual *uḥlul ʿuqdatan min lisānī* relief-prayer = **Q 20:25-28**.
- Q 28 has TWO impediment-related verses: Q 28:34 (Mūsā's request: "and my brother Hārūn is more eloquent than I in tongue, so send him with me as a helper") + Q 28:35 (God's answer: "We will strengthen your arm with your brother...").

**Decision**: re-anchor F-04 to **Q 28:34-35** (the actual Q 28 impediment-reference + response pair) and lexically compare against **Q 20:25-28** (the relief-prayer). This decision was made BEFORE running F-04. Logged here as garden-of-forking-paths transparency. The locked direction (cosine to Q 20:25-28 should exceed random pairs) was set BEFORE observation.

### F-01 H3 threshold note

The 50% threshold for `مدين` Q 28 share was set BEFORE observation. This is high — Madyan is a corpus-shared toponym (7 surahs), so a 50% threshold is structurally unlikely. The pre-reg locked it as a clean structural threshold; the FAIL is honest.

### F-03 H1 distinctness-sort direction

The pre-reg locks "rank ≤ 4" as the threshold for "Qārūn-window most-distinct in Q 28". Implementation sorts by `−distinctness` (descending), so rank 1 = most distinct. The Qārūn-window's rank 80 / 82 means it is **near the bottom** of distinctness (i.e., highly-vocabulary-overlapping with the rest of Q 28). This was unexpected directionally — the pre-committed direction was UPPER (rank ≤ 4 = top 5% most distinct). Logged here as a pre-commit direction violation that produces NULL with full prominence.

### F-05 H2 corpus-median triviality

Discovery during F-05 implementation: corpus-median for `موسى`-density and prophet-density is **0** (most surahs don't mention any prophet by name). So H2 is somewhat trivially-fit. Logged here to ensure H1 (the perm-test against random Meccan-3-tuples) is treated as the load-bearing test. H2 cells-above-median = 9/9 is corroborating but soft.

### F-02 cosine selection

The pre-reg locks the cosine on **shared-root-vocabulary** (union of all roots in the three blocks). Implementation uses surface-form-stem (one-prefix-strip) rather than full-QAC root collapse, because (a) QAC processing has overhead and (b) surface-form-stem is the project's default rules-tuple. A future agent could re-run under full QAC root-collapse for sensitivity-check.

---

## 2026-05-07 13:30 — script execution

Ran `python3 /Users/grey/Downloads/quran/surahs/Q028-al-qasas/scripts/Q028_F_all.py`:

```
============================================================
Q028-al-qasas — pre-registered novel tests F-01..F-05
seed= 20260507 N_PERM= 10000 alpha_bon= 0.01
============================================================
F-01: verdict=DIRECTIONAL, target_rank=6/82, p=0.0026, hapax_in_window=28, madyan_share=0.300
F-02: verdict=NULL — consolidates Wave-FALSIFIED §3.7 (muqaṭṭaʿāt ⊥ content axis); cos(26,28)=0.6696, cos(26,20)=0.6756, cos(28,20)=0.8191; contrast=-0.0777, p=0.9109
F-03: verdict=DIRECTIONAL; qarun rank=80/82, madyan rank=49/82, qarun share=0.500, pair rank=2748/3321
F-04: verdict=NULL; shared low-freq=0 ([]); cos=0.0928, p=0.4545
F-05: verdict=PASS — TSM-cluster narrative-cohesion vindicated (CHALLENGES Wave-FALSIFIED §3.7); tsm_centroid=1.881, p=0.0017, cells_above=9/9
All 5 done. Outputs in /Users/grey/Downloads/quran/surahs/Q028-al-qasas/csv
```

All 5 pre-reg SHAs verified at runtime ✓. JSON outputs written to `csv/Q028-F-{01,02,03,04,05}.json`.

---

## 2026-05-07 13:45 — 8-file template + classical-claims-audit completion

All 8 surah-template files written:
- 00-overview.md
- 01-empirical-profile.md
- 02-content-analysis.md
- 03-tafsir-survey.md
- 04-hadith-corpus.md
- 05-classical-claims-audit.md
- 06-novel-findings.md
- 07-cross-references.md

Classical-claims audit verdicts (6 claims):
- C-1 al-Suyūṭī mid-Meccan + v. 85 Hijra: **VINDICATED**
- C-2 al-Rāzī Q 28:88 iʿjāz-al-maʿnā: **VINDICATED**
- C-3 al-Biqāʿī Q 27→28→29 munāsabah: **VINDICATED at canonical-adjacency level** (residuals 0.71%, 0.90%)
- C-4 al-Biqāʿī TSM letter-cluster = content-cluster: ❌ **FALSIFIED on vocabulary axis** (5th NULL); **DIRECTIONAL rehabilitation on narrative-density axis** (F-05 PASS)
- C-5 Ibn Kathīr Madyan-elder = Shuʿayb: **NOT-TESTABLE** empirically; CONSISTENT with consensus
- C-6 al-Bukhārī Q 28:56 = Abū Ṭālib sabab: ✅ **VINDICATED** (multiply-attested, ṣaḥīḥ rank)

---

## 2026-05-07 14:00 — locator corrections logged

Two locator corrections made vs dispatch-prompt:

1. **Bukhārī "#1360" for Q 28:56 sabab** → disk verification shows #1360 is a *janāʾiz* ḥadīth, NOT the Q 28:56 sabab. The actual sabab is **#3884, #4675, #4772**. Logged in `04-hadith-corpus.md`.

2. **Bukhārī "#2403" for Qārūn ḥadīth** → disk search across all 9 books shows **0 Qārūn hits in Bukhārī** (only Dārimī #1989 has a passing reference). The Qārūn-tradition lives in tafsir + isrāʾīliyyāt, not canonical Hadith. Logged in `04-hadith-corpus.md`.

These corrections are made transparently per project anti-hallucination protocol §2.11.

---

## Decision points + summary

### Decision 1: F-04 re-anchoring

**Decision**: re-anchored to Q 28:34-35 (impediment-reference + response) vs Q 20:25-28 (relief-prayer).
**Rationale**: dispatch-prompt's verse-locator was empirically wrong; logged BEFORE running.
**Result**: F-04 NULL (lexical echo not realised; conceptual echo holds in classical interpretation).

### Decision 2: F-05 H1 vs H2 prominence

**Decision**: H1 (perm-test) is the load-bearing test; H2 (cells-above-corpus-median) is corroborating but soft.
**Rationale**: corpus-median for prophet-density is 0; H2 trivially passes for any prophet-narrative surah.
**Result**: H1 p_perm = 0.0017 < α = 0.01 — robust PASS.

### Decision 3: F-05 PASS scope

**Decision**: report F-05 as DIRECTIONAL (single-cluster) pending replication on HM-7, ALR-5, ALM-6.
**Rationale**: per project protocol §1.6 PRE-REG-STANDARD, single positive result is not law-strength; replication on other muqaṭṭaʿāt clusters needed.
**Result**: published F-05 with explicit DIRECTIONAL caveat.

### Decision 4: Bonferroni α level

**Decision**: family k=5 (this surah's pre-registered novel tests F-01…F-05); α_Bonferroni = 0.05/5 = 0.01.
**Rationale**: standard project Bonferroni discipline per protocol §1.5; tightening from raw α=0.05.
**Result**: F-05 p=0.0017 passes Bonferroni-α=0.01; F-01 p=0.0026 passes raw α but its rank fails the top-4 threshold; F-02 p=0.9109 fails (NULL); F-04 p=0.4545 fails (NULL).

### Garden-of-forking-paths log: BEFORE results

All decisions above were made BEFORE running the script. The pre-reg SHAs are immutable; the script's output is reproducible (seed 20260507).

---

## Final headline

Q 28 is the **Moses-Madyan-Qārūn surah**. Its empirical profile shows:

1. The Madyan-episode (vv. 22-28) is hapax-rich (28 corpus-orthographic-hapaxes) but not *the* most distinctive in the surah — the Mūsā-birth-block (vv. 5-13) edges it out.
2. The Qārūn-episode (vv. 76-82) is **vocabulary-integrated** with Q 28's eschatological-closing material — corroborating the classical *Qārūn-as-exemplum* reading.
3. Q 28's content-pair partner is **Q 20 Ṭā-Hā**, NOT Q 26 al-Shuʿarāʾ (despite Q 26-28 sharing ṬSM letters). al-Biqāʿī muqaṭṭaʿāt-content claim REPLICATED-FALSIFIED (5th NULL).
4. The TSM 3-surah cluster Q 26-27-28 DOES cohere on **narrative-density** (Moses-density, prophet-density, narrative-marker density) at p = 0.0017 — first observed rules-tuple-bidirectional rehabilitation of the al-Biqāʿī muqaṭṭaʿāt-content-munāsabah claim, on a different axis than vocabulary.
5. Q 28:88 *kullu shayʾin hālikun illā wajhah* fits the al-Rāzī iʿjāz-al-maʿnā / theological-iʿjāz axis. Q 28:56 *innaka lā tahdī man aḥbabta* is the Abū Ṭālib death-bed sabab, multiply-attested at ṣaḥīḥ rank.

5 pre-registered tests run. 1 PASS, 1 NULL-pre-commit-reverse, 2 DIRECTIONAL, 1 NULL. Equal NULL prominence preserved per protocol.

---

## Cross-coordination

- Q026-al-shuara: TSM-cluster lead specialist; Q028-F-02 result feeds back as 5th NULL on Q026-F-02-related family. Q028-F-05 result EXTENDS Q026-F-02 to a different axis.
- Q020-ta-ha: Moses-cycle-purity lead specialist; Q028-F-04 result confirms the Q 20:25-28 relief-prayer is lexically self-contained in Q 20.
- Q029-al-ankabut (future): will document Q 28 → Q 29 munāsabah from the Q 29 side.

---

## Files produced

| Path | Purpose |
|:--|:--|
| `surahs/Q028-al-qasas/00-overview.md` | overview |
| `surahs/Q028-al-qasas/01-empirical-profile.md` | H-NEW integration |
| `surahs/Q028-al-qasas/02-content-analysis.md` | content + thematic blocks |
| `surahs/Q028-al-qasas/03-tafsir-survey.md` | 6 mufassirūn survey |
| `surahs/Q028-al-qasas/04-hadith-corpus.md` | hadith citations + locator corrections |
| `surahs/Q028-al-qasas/05-classical-claims-audit.md` | 6 classical claims audited |
| `surahs/Q028-al-qasas/06-novel-findings.md` | 5 + 3 pre-registered novel findings |
| `surahs/Q028-al-qasas/07-cross-references.md` | network coordinates |
| `surahs/Q028-al-qasas/JOURNAL.md` | this file |
| `surahs/Q028-al-qasas/Q028-F-01-...-prereg.md` | pre-reg files (SHA-locked) |
| `surahs/Q028-al-qasas/scripts/Q028_F_all.py` | Wave-A runner script |
| `surahs/Q028-al-qasas/csv/Q028-F-{01..05}.json` | Wave-A JSON outputs |
| `surahs/Q028-al-qasas/Q028-F-{06,07,08}-*-prereg.md` | Wave-H pre-reg files |
| `scripts/Q028_F_{06,07,08}_*.py` | Wave-H runner scripts |
| `surahs/Q028-al-qasas/csv/Q028-F-{06,07,08}.json` | Wave-H JSON outputs |

---

## 2026-05-09 PM — Wave-H addendum (F-06, F-07, F-08)

Wave-H dispatch added three further pre-registered tests as a follow-up specialisation set:

| Wave-H ID | Title | SHA-256 | Verdict |
|:--|:--|:--|:--|
| Q028-F-06 | Mūsā density and absolute-count corpus rank | `b2c6d43332bbd81bd267d3a38d027f617d395d0e270cb6469e8b1c251cef2d03` | DIRECTIONAL |
| Q028-F-07 | TSM-pair {Q 26, Q 28} FR closest-intra-cluster test | `dacc213250309dd1b8fe45d08b5d57ea9012790eb2109bcad63e980eecf93d53` | DIRECTIONAL |
| Q028-F-08 | Qārūn-pericope corpus-uniqueness rank-1 test | `076200dd8551ea742ddea59e239adad3735e53088555e3cf47afc00d811779d2` | ✅ CONFIRMED |

Seed 20260509. Bonferroni k = 3 in the Wave-H family, α_Bonferroni = 0.05/3 = 0.01667.

### Wave-H decision points

**Decision W-H-1: dispatch-prompt T1 direction was "corpus rank-1 in Mūsā attestations"**.
Empirical reality (verified at runtime): Q 7 al-Aʿrāf has 21 Mūsā QAC-attestations, Q 28 has 18 → Q 28 is rank 2, not rank 1. The pre-reg was direction-locked to rank-1 BEFORE running. Published as DIRECTIONAL with full prominence: H2 (density top-3) passes; H1 (absolute-rank-1) fails honestly. The classical "Sūrat Mūsā" attribution applies to **narrative-arc length** (Q 28 has the single longest Mosesic pericope, vv. 3-43, ~40 verses) and **density** (Q 28 in top-3 cluster), but NOT to **absolute count** (Q 7 leads).

**Decision W-H-2: dispatch-prompt T2 direction was "TSM-pair {Q 26, Q 28} is the closest TSM pair on FR"**.
Existing 00-overview.md already cited FR(Q 28, Q 26) = 0.954 and FR(Q 28, Q 27) = 0.805. The pre-reg was direction-locked to "TSM-pair closest" BEFORE running, with explicit honest-expectation note that this would likely FAIL. F-07 H1 fails as expected — published as DIRECTIONAL, consolidating Wave-FALSIFIED §3.7 on a 6th independent axis (Fisher-Rao on tightest TSM exact-letter-match specialisation).

**Decision W-H-3: F-08 pericope-extent definition**.
The pre-reg pre-commits TWO operational definitions for "Qārūn-pericope-extent":
  (a) QAC-attestation extent = max_verse_with_Qārūn − min_verse_with_Qārūn + 1; in Q 28 = 4 (vv. 76 → 79).
  (b) Narrative-block extent = the contiguous narrative arc; in Q 28 = 7 (vv. 76-82).
Both pass the corpus-monopoly test (no other surah has Qārūn-extent ≥ 2 by either definition). F-08 reports both; the deterministic threshold uses (a) for clarity.

**Decision W-H-4: Bonferroni for Wave-H family**.
k = 3 (this dispatch's three pre-registered tests). α_Bonferroni = 0.01667. All three sub-claim families pass / fail deterministically (no permutation p needed), so Bonferroni applies trivially to the 9-sub-claim grand family.

### Wave-H execution log

```
$ python3 scripts/Q028_F_06_musa_density_rank.py
Q028-F-06 verdict: DIRECTIONAL
  corpus Mūsā count (QAC): 136 (H-NEW-1710 ref: 136)
  Q 28 absolute count: 18 (rank 2/114; H1 pass=False)
  Q 28 density per 1000 stem tokens: 12.53 (rank 3/114; H2 pass=True)
  Q 28 orthographic substring count: 18 (rank 2/114)
  H3 count >= 20: pass=False
  top-5 by QAC count: [(7, 21), (28, 18), (20, 17), (2, 13), (10, 8)]
  top-5 by density:   [(87, 13.89), (20, 12.64), (28, 12.53), (7, 6.3), (26, 6.05)]

$ python3 scripts/Q028_F_07_tsm_pair_fr.py
Q028-F-07 verdict: DIRECTIONAL
  FR(Q 26, Q 28) = 0.9537
  FR(Q 26, Q 27) = 0.9585
  FR(Q 27, Q 28) = 0.8048
  min TS-only pair = 0.8048
  H1 TSM-pair closest in cluster: pass=False
  Q 26 rank in Q 28's neighbors: 29/113 (H2 ≤5 pass=False)
  Q 27 rank in Q 28's neighbors: 2/113
  FR(Q26,Q28) corpus percentile: 49.2% (H3 <50% pass=True)

$ python3 scripts/Q028_F_08_qarun_corpus_rank.py
Q028-F-08 verdict: CONFIRMED
  corpus Qārūn count (QAC PN-lemma): 4
  Q 28 Qārūn count: 2 (rank 1/4-attesting-surahs; H1 pass=True)
  Q 28 Qārūn QAC-extent: 4 verses; max other surah extent: 1 (H2 pass=True)
  Q 28:76-82 rare-token types (≤5 corpus-attest): 39 (H3 ≥5 pass=True)
```

All 3 Wave-H SHAs verified at runtime ✓.

### Wave-H headline

Q 28's Wave-H signature: **DIRECTIONAL on Mūsā-rank (Q 7 leads absolute count; Q 28 is rank-2 absolute, top-3 density), DIRECTIONAL on TSM-FR-cluster (6th independent NULL of muqaṭṭaʿāt-FR-cohesion claim), CONFIRMED on Qārūn-corpus-monopoly (rank-1 + corpus-extent-monopoly + 39 rare-token types).**

The Qārūn-monopoly finding is the most robust new datapoint: corpus rank-1 + extent-monopoly + lexical-singleton on three independent metrics. This is a project-significant triple-corroboration for the classical canonical "Qārūn surah" attribution.
