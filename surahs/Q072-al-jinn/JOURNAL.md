---
surah: 72
surah_name_ar: الجن
surah_name_translit: al-Jinn
file_type: journal
date_last_updated: 2026-05-09
phase: B+
---

# Q 72 al-Jinn — Investigation Journal


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

## 2026-05-09 — Wave-H specialist landing

### Pre-flight reading
- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md`
- `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` §10.18 (5-qul cluster prior), §10.34 (H-NEW-1190 PC), §10.20 (H-NEW-1080)

### Status at start of session
Q072-al-jinn/ folder existed but was empty (csv/ and scripts/ subdirs empty, no markdown files).
The dispatch brief was the SESSION-HANDOFF §2.c pending: "5 *qul*-opener cluster {Q 72, 109, 112, 113, 114} replication" + Q 72 specialist deep-dive.

### Investigation arc

#### Step 1 — orient on data inventory
- Verified Q 72: 28 verses, Meccan, revelation #40 (al-Suyūṭī), Nöldeke #62 (middle-Meccan). Source: `data/revelation-order.csv` line for surah 72; `data/hafs-verse-counts.tsv` line for surah 72.
- Verified al-Biqāʿī §Q72 section in `data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt` lines 144712-onward. Recorded the *maqṣūd* statement, the Q 71→Q 72 munāsabah claim, and the *nafar* / *nakhla* / *al-masājid* close-reading notes.
- Verified 9-book hadith corpus on disk. Search for Q 72-related hadiths yielded: **Bukhārī #755** (Aḏān ch. 10), **Bukhārī #4713** (Tafsīr ch. 65), **Muslim idInBook #908 + #909** (Kitāb al-Ṣalāh ch. 4), **Tirmidhī #3342, #3375, #3407** (Tafsīr ch. 47), **Nasāʾī #5503**, **Ibn Mājah #3247**, **Aḥmad #1356**. The dispatch brief's "Bukhārī Aḏān 773" reference was NOT verified — the actual Bukhārī Q72-related numbers are 755 and 4713. Logged the correction in `04-hadith-corpus.md` §1.

#### Step 2 — empirical baseline
- Loaded `findings/phase-b-hypotheses/csv/h-new-111.json` and computed Q 72's FR-neighborhood.
- Q 72's top-15 FR-nearest computed; **rank-1 = Q 112 al-Ikhlāṣ at d = 0.6945**. 4 of top-5 are 5-qul cluster members (Q 112, 114, 110, 113); rank-5 = Q 96.
- Q 72 mean FR to corpus = 0.8985 (slightly below corpus mean 0.92).
- Computed h-new-590 / h-new-700 / h-new-750 / h-new-720 / h-new-840 lookups for Q 72. Recorded all values in `01-empirical-profile.md`.
- **Striking finding**: h-new-750 reports Q 72's rhyme_entropy = 0.0, top_final_letter = ا at 100%. Direct text inspection of `quran-text/quran-no-tashkeel.json` Q72 verses 1-28 confirms 28/28 verses end in alif. This is a corpus-extreme rhyme-cohesion signature.

#### Step 3 — pre-registration (PRE-REG-STANDARD-04)

Pre-committed 3 tests BEFORE running any code:

| Test | Pre-reg | SHA |
|:--|:--|:--|
| Q072-F-01 | `preregs/Q072-F-01-five-qul-cluster-fr-cohesion-prereg.md` | `b4faaeeea844cf372b8e101fa2d53994b11c8db25e789728c36bd7a719b4f540` |
| Q072-F-02 | `preregs/Q072-F-02-jinn-density-rank-prereg.md` | `0129c9a395bc084e4b6df785af3f97c3f0abd5054e8288ab1dc6357e72864e69` |
| Q072-F-03 | `preregs/Q072-F-03-jinn-pericope-pair-prereg.md` | `ff4ec27cb7e802f4a090ba3e419466a1d6594d7598a21b1d38ca009cd944f4bc` |

Seed: 20260509. Bonferroni-k = 3, α_bon = 0.0167. All directions pre-committed PASS.

Garden-of-forking-paths log:
- **Q072-F-02 lens choice**: pre-committed STRICT LEM:jin~ as primary, expanded LEM:jin~+LEM:jaA^n~ as secondary sensitivity. Rationale logged BEFORE running. The strict-vs-expanded split was identified at the data-orientation step where I noticed Q 55 has 4 *al-jaAn~* tokens that would dominate the expanded lens. Pre-committing the strict lens prevented post-hoc lens-shopping.
- **Q072-F-03 null-pool design**: pre-committed length-matched (word-count ±25% around Q 46:29-32's 73 words) over ALL contiguous verse-windows in the corpus excluding the two reference blocks. Null pool turned out to be 19,023 candidate windows — well-sampled.

#### Step 4 — run all 3 tests

All 3 scripts verified SHA-lock at runtime:

```
Q072-F-01 verdict: PASS-STRONG (predicted p<0.01 met; PC passes)
  obs within-mean = 0.4983; null mean = 0.9236; sd = 0.1009
  p (one-sided ≤) = 0.0026; z = -4.217
  PC obs = 0.6078; PC null = 0.9255; PC p = 0.0362
  Q72→{109,112,113,114} mean = 0.7466

Q072-F-02 primary: PASS (rank=1/114 strict LEM:jin~)
  Q 72 strict-LEM:jin~ density: 10.239/1k (3/293)
  Q 72 expanded-lens density:   10.239/1k -> rank 2/114
  Top-5 strict:
    Q 72:   3/  293 =  10.24/1k
    Q 34:   3/  940 =   3.19/1k
    Q 46:   2/  676 =   2.96/1k
    Q 55:   1/  355 =   2.82/1k
    Q 51:   1/  371 =   2.70/1k

Q072-F-03 verdict: PASS
  obs Jaccard = 0.0851; intersection size = 16
  null mean = 0.0469; sd = 0.0136; p (one-sided ≥) = 0.0068; z = 2.808
  n candidate windows = 19023
  diagnostic in both: ['الجن', 'سمعنا', 'يهدي']
```

**Family verdict: 3/3 PASS**. All directions match pre-commit. Q072-F-01 and Q072-F-03 survive Bonferroni-k=3. Q072-F-02 is a deterministic rank-test.

#### Step 5 — write 8-file template

Files written:
1. `00-overview.md` — surah identification + headline forward-references
2. `01-empirical-profile.md` — UAS, FR, iʿjāz, outlier, adjacency, compression-tail position
3. `02-content-analysis.md` — verse-by-verse, block-A/block-B, diagnostic lexicon, *wa-anna* enumeration, *raṣadan* inclusio
4. `03-tafsir-survey.md` — al-Biqāʿī (primary on-disk citations), al-Rāzī, Ibn Kathīr, al-Suyūṭī, al-Ṭabarī, al-Zamakhsharī, al-Qurṭubī
5. `04-hadith-corpus.md` — Bukhārī 755/4713; Muslim 908/909; Tirmidhī 3342/3375/3407; Nasāʾī 5503; Ibn Mājah 3247; Aḥmad 1356 (cross-pericope linkage to Q 46:29)
6. `05-classical-claims-audit.md` — 6 classical claims audited; 4 VINDICATED/CONFIRMED, 1 RULES-TUPLE-FRAGILE (al-Biqāʿī Q 71→72 thematic arc), 1 NOT-TESTABLE (Ibn ʿAbbās vs Ibn Masʿūd asbāb)
7. `06-novel-findings.md` — Q072-F-01/02/03 full write-ups with pre-reg SHAs + verdicts
8. `07-cross-references.md` — cluster-membership map, H-NEW network, cross-surah pairings (Q 72 ↔ Q 46, Q 55, Q 112, Q 96)

#### Step 6 — final SHA verification + sanity check

All 3 pre-reg SHAs match the embedded values in the corresponding run scripts:
- `scripts/Q072_F_01_five_qul_replication.py` → SHA verified
- `scripts/Q072_F_02_jinn_density_rank.py` → SHA verified
- `scripts/Q072_F_03_jinn_pericope_pair.py` → SHA verified

Quality gates audit:
- [x] Pre-reg SHA matches embedded
- [x] Direction-of-effect matches pre-committed (3/3 PASS, no direction-reversal)
- [x] Bonferroni applied (k=3, α_bon=0.0167; F-01 and F-03 survive)
- [x] Replication (Q072-F-01 replicates H-NEW-74 / §10.18 at independent seed)
- [x] Honest limits section in each major file
- [x] Cross-references include challenging priors (H-NEW-265 opener-stripped NULL is cited in `06-novel-findings.md` and `07-cross-references.md`)
- [x] Classical citations are scholar+work+passage (al-Biqāʿī §Q72 with line numbers; Bukhārī with hadith numbers)
- [x] Final statements are intellectually honest

### Open items at end of session

- Q072-F-03.1: lemma-level Jaccard for Q 72:1-19 ↔ Q 46:29-32 (queued)
- Q072-F-04: 17-fold *wa-anna* enumeration corpus-uniqueness (queued)
- Q072-F-05: 100% alif-monorhyme corpus-rank within Meccan-restricted comparison (queued)
- Q072-F-06: *raṣadan* inclusio test (v.9 ↔ v.27) against intra-surah permutation null (queued)
- Cross-finding-028 (al-muʿawwidhāt-extended pattern) should be updated to reflect Q072-F-01 replication

### Headline outcome

Q 72 al-Jinn specialist landing CONFIRMED at 3/3 PASS. The 5-qul opener cluster is now corpus-empirically CONFIRMED with two independent seed replications (seed 20260508 inline + seed 20260509 Q072-F-01). The surah-name → primary-lemma faithfulness is VINDICATED at corpus-EXACT for Q 72 (rank 1/114 strict LEM:jin~ density, 3.2× margin over rank-2). The Abū Ḥayyān same-event reading of Q 72:1 ↔ Q 46:29 is empirically SUPPORTED at p=0.0068.

Three new corpus-empirical signals added to the project.
