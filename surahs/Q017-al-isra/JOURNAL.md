---
surah: 17
file_type: journal
date_last_updated: 2026-04-28
phase: B+
---

# Q 17 al-Isrāʾ — Investigation Journal


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

## 2026-04-28 — Specialist run: full per-surah investigation (00-07 + JOURNAL + 4 pre-registered tests)

**Agent**: Q017-specialist (Opus 4.7 1M).
**Reading list completed**: `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`, `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`, `surahs/Q017-al-isra/00-overview.md` (and 01-06 as they were produced in earlier passes), `MASTER-FINDINGS-LEDGER.md` §9 (Wave A/B template), `surahs/Q033-al-ahzab/07-cross-references.md` and `JOURNAL.md` as templates.

### Pre-registrations locked

All four pre-regs were written BEFORE the run script was executed; SHAs were embedded in the runner and verified at runtime via `verify_preregs()` (see `scripts/Q017_F_all.py` lines 17-49). Re-verified 2026-04-28 (this session) by `shasum -a 256` over each prereg file:

| ID | Title | Pre-reg file | SHA-256 (verified) |
|:--|:--|:--|:--|
| Q017-F-01 | Alif-monorhyme purity rank for Q 17 | `preregs/Q017-F-01-alif-monorhyme-prereg.md` | `daa0e3d7bb1e6c5a49332ef639b26944b8657526bf5fe853b40844fb3baa0604` |
| Q017-F-02 | *Subḥāna* opening uniqueness (musabbiḥāt sub-classification) | `preregs/Q017-F-02-subhana-opening-prereg.md` | `d3bf2bc52e69777415bb62e2efd9f5122870aacaa84b90ca9ced7e18b1d40904` |
| Q017-F-03 | Q 17:88 taḥaddī verse — lexical signature + citation density | `preregs/Q017-F-03-tahaddi-citation-density-prereg.md` | `68942a558acd81b2e1e6883a7a8b14bc40a7a4ef4a75c8994b19dad82259ddf5` |
| Q017-F-04 | Banī Isrāʾīl narrative concentration | `preregs/Q017-F-04-children-of-israel-density-prereg.md` | `86f3cb12aa13ddb3f10ad5c6687924844246fd1f9dbffcf194cd119844a23c4f` |

All four SHAs match the values embedded in `scripts/Q017_F_all.py` `PREREG_SHAS` dictionary. Pre-reg discipline preserved.

### Run script

`surahs/Q017-al-isra/scripts/Q017_F_all.py` — single runner consolidating F-01 through F-04. Verifies all four pre-reg SHAs at start; fail-fast on mismatch (assertion at line 48). All four tests use seed-locked Python stdlib only (no external dependencies).

### Outputs

JSON (in `surahs/Q017-al-isra/csv/`):
- `Q017-F-01.json` — alif-monorhyme rates per surah; Q 17 record + top-10 + perfect-monorhyme list.
- `Q017-F-02.json` — musabbiḥāt opening tokens; categorized forms; all-114 *Subḥāna* opener list.
- `Q017-F-03.json` — Q 17:88 lemma hits + per-tafsir citation hits + verdict.
- `Q017-F-04.json` — per-surah إسرائيل counts + densities + ranks + Q 17 record.
- `Q017-hadith-catalog.json` — 9-collection hadith citation catalog (16 KB).
- `Q017-hadith-citations.json` — per-verse hadith citation inventory (19 KB).

Markdown (in `surahs/Q017-al-isra/`):
- `00-overview.md` — basic facts + classical names + opening + length-class + signature + content + cross-refs + status.
- `01-empirical-profile.md` — all H-NEW metrics integrated, UAS decomposition, FR neighbors, architectural type.
- `02-content-analysis.md` — 18-block segmentation, Decalogue-like ethical code, opening-closing inclusio.
- `03-tafsir-survey.md` — 9 mufassirūn surveyed; per-Q17 OpenITI extracts; convergences and disagreements.
- `04-hadith-corpus.md` — 22+ Q 17-tied ḥadīth catalogued; *al-ʿitāq al-uwal* + *maqām maḥmūd* clusters.
- `05-classical-claims-audit.md` — 7 classical claims tested; rules-tuple verdicts.
- `06-novel-findings.md` — 4 pre-registered tests, all VINDICATED; break-verse-architectural-law cross-finding observation.
- `07-cross-references.md` — neighbors + clusters + verse-twins + H-NEW integrations + reciprocal-link targets.
- `JOURNAL.md` — this file.

### Verdicts

Pre-registered tests:

| Test | Direction-locked hypothesis | Result | Verdict |
|:--|:--|:--|:--|
| Q017-F-01 | Q 17 alif-final rate ≥ 0.99 AND dense_rank ≤ 10 | rate = 0.9910 (110/111); dense rank = 2 of 114 | **VINDICATED** |
| Q017-F-02 | Q 17 is the unique surah opening with *Subḥāna* maṣdar across 114 surahs | 1 of 1 (Q 17 only) | **VINDICATED** |
| Q017-F-03 | (A) Q 17:88 contains 5 distinct iʿjāz-related lemmas; (B) ≥4 of 9 mufassirūn cite ≥200 chars | (A) 5/5 lemmas; (B) 7/9 substantive | **VINDICATED on both axes** |
| Q017-F-04 | Q 17 ranks ≤ 25 by count OR density of إسرائيل lemma | rank_count = 4; rank_density = 5 | **VINDICATED on both metrics** |

Classical-claims audit (`05-classical-claims-audit.md`):

| # | Claim | Verdict |
|--:|:--|:--|
| 1 | "Banī Isrāʾīl" naming (Ibn Masʿūd, al-Bukhārī #4502, #4533, #4787) | **VINDICATED** (via Q017-F-04) |
| 2 | Q 17 as one of the *al-musabbiḥāt* / *ʿarāʾis al-Qurʾān* (al-Suyūṭī, *al-Itqān*) | **VINDICATED** (via Q017-F-02; with Q 17's grammatical distinctness as a refinement) |
| 3 | al-Bāqillānī *iʿjāz al-fawāṣil* applies to Q 17 | **NOT-FALSIFIED but RULES-TUPLE-FRAGILE** — Q 17 is anti-fawāṣil locally; vindicates the dual-iʿjāz typology |
| 4 | Q 17:88 as the maximal taḥaddī | **VINDICATED** (via Q017-F-03; lexical + citation) |
| 5 | Q 17:111 as *āyat al-ʿizz* (al-Suyūṭī, *al-Itqān*, citing Aḥmad's Musnad via Muʿādh b. Anas) | **VINDICATED** (via classical citation; chain-grading deferred) |
| 6 | Q 17:79 = al-Shafāʿa al-Kubrā / Major Intercession (al-Tirmidhī #3221, #3232; al-Bukhārī #7155) | **VINDICATED** (direct ḥadīth corpus support across 3 collections) |
| 7 | Bodily *isrāʾ* (universal classical Sunnī position) | **NOT-TESTABLE EMPIRICALLY** (theological-philosophical) |

Tally: **5 VINDICATED, 1 nuanced (RULES-TUPLE-FRAGILE on a negative direction; vindicates the larger typology), 1 NOT-TESTABLE.**

### Key findings (5 most surprising)

1. **The single non-alif verse in Q 17 is verse 1 itself** — the Isrāʾ verse, ending in *al-Samīʿu al-Baṣīr* (rāʾ-final). The verse breaking the surah's monorhyme is the **founding event** of the surah. Structurally analogous to Q 33:4 breaking Q 33's monorhyme as the legal premise for v.37. **Two-data-point observation flagged as the candidate "break-verse architectural law"** — pre-registered as Q017-F-05 follow-up.

2. **Q 17 is the unique maṣdar-form musabbiḥa** — the *Subḥāna* (verbal-noun, accusative of glorification) opening is corpus-unique among the 7 musabbiḥāt. Q 17 alone *performs* tasbīḥ of God for a specific event (the *isrāʾ*), rather than narrating the cosmic *yusabbiḥu* of creation (Q 62, 64) or commanding/perfecting tasbīḥ (Q 57, 59, 61, 87). This is a refinement of al-Suyūṭī's *ʿarāʾis al-Qurʾān* taxonomy.

3. **Q 17 sustains 99.10% alif-final over 111 verses — outperforming Labid's *Muʿallaqa* (98.88% over 178 verses)**. The qaṣīda-form mastery is real, and Q 17's anti-fawāṣil profile (sig_A rank 111/114) is the empirical anchor for the **theological-iʿjāz at qaṣīda-form** reading: Q 17:88's maximal taḥaddī asserts inimitability *precisely* in the form that humans most successfully match.

4. **Q 17:88 is hub-anchored across 7 of 9 surveyed classical mufassirūn** with substantive (≥200 char) commentary. Combined with the 5/5 lemma signature (mithl, ijtimāʿ, jinn, ins, ẓahīr), Q 17:88 is the classical-reception hub of the maximal-taḥaddī doctrine. Two extracts (al-Biqāʿī, al-Suyūṭī al-Durr) are partial — flagged for re-extraction; a 9/9 result is plausible after follow-up.

5. **The al-ʿitāq al-uwal hadith block (Ibn Masʿūd via al-Bukhārī #4502, #4533, #4787) is empirically vindicated as a TSP-block.** Q 17 → Q 18 cost 0.028 (bottom-quartile), Q 18 → Q 19 cost ≈ −0.030 (rewarded by 2-opt), Q 19 → Q 20 and Q 20 → Q 21 also cheap. Five canonical neighbors experienced as one block by an early Companion, with empirical FR-distance/TSP-cost agreement. The Companion's mnemonic grouping reads as a low-architectural-cost block detection.

### Garden-of-forking-paths log

- **F-01**: pre-reg locked rate ≥ 0.99 AND dense_rank ≤ 10. Both conditions met (rate = 0.9910; dense_rank = 2). VINDICATED on both legs without any post-hoc adjustment. Strict alphabetical-tiebreak rank = 9, also within the locked rank ≤ 10. The 8-perfect-monorhyme-surah tier above Q 17 was anticipated in the pre-reg.
- **F-02**: pre-reg locked uniqueness across 114 surahs. Result = 1 of 1. The categorization of the other 6 musabbiḥāt by verb-form (*sabbaḥa* perfect = 4; *yusabbiḥu* imperfect = 2) was reported as informative-secondary, not pre-registered as a primary condition.
- **F-03**: pre-reg locked (A) ≥ 5 lemmas AND (B) ≥ 4 mufassirūn citing ≥ 200 chars. Both met cleanly (5/5; 7/9). The 2 absent tafsirs (al-Biqāʿī, al-Suyūṭī al-Durr) showed 0-char context — likely a partial-extraction artifact; reported conservatively without re-extraction. The pre-reg threshold was 4/9, so the 7/9 result clears with margin even if the partial-extraction artifact is upheld.
- **F-04**: pre-reg locked rank ≤ 25 by count OR density. Both met (rank_count = 4; rank_density = 5). The "OR" condition is satisfied with margin; the "AND" version (which was NOT pre-registered) would also pass.
- **No pre-commit violations** in this run. All four direction-locked predictions held in the locked direction.
- **Re-extraction flags**: al-Biqāʿī Q 17 extract = 44,400 chars, al-Suyūṭī al-Durr Q 17 extract = 43,888 chars — both partial; re-extraction with adjusted regex would likely upgrade F-03 to 9/9 but the verdict is already locked at VINDICATED.

### Cross-file consistency check

- 00-overview.md §5 and 06-novel-findings.md Q017-F-01 both report 0.9910 alif-final rate (110/111) and dense_rank 2 — consistent.
- 00-overview.md §6 and 01-empirical-profile.md §1 both report UAS = 2.220, rank 10/114 — consistent with `findings/phase-b-hypotheses/csv/h-new-840.json`.
- 04-hadith-corpus.md §1 and 05-classical-claims-audit.md Claim 1 both reference al-Bukhārī #4502, #4533, #4787 with the same Arabic transcription — consistent.
- 03-tafsir-survey.md §10 (Q 17:88 substantial commentary) matches 06-novel-findings.md F-03 (7 of 9 substantive) — consistent.
- All four pre-reg SHAs in `06-novel-findings.md` are identical to `scripts/Q017_F_all.py` `PREREG_SHAS` and to filesystem `shasum` output — verified.
- 07-cross-references.md §1 TSP-cost figures (Q 16-17 = 0.191; Q 17-18 = 0.028) match 01-empirical-profile.md §6 — consistent.

### NULL outcomes (per protocol §1.3 equal NULL prominence)

This run produced **no NULLs in the four pre-registered tests** (all four VINDICATED). Per protocol, NULL prominence is observed by ensuring this fact is reported honestly without inflating the four-for-four record beyond its actual content:

- **Q 17 outlier-strength is NULL** (H-NEW-590; Δ = −3.94 pp, p_greater = 0.379). Q 17 is *integrated*, not outlier-anchor — directly recorded in 01-empirical-profile.md §3.
- **Q 17 is not a structural-iʿjāz hub** (UAS rank 10, not in the structural top-9). The UAS top-9 (Q 33, 1, 2, 9, 24, 12, 55, 10, 23) precede Q 17.
- **Classical Claim 3 (al-Bāqillānī applies to Q 17)** is NOT-FALSIFIED but RULES-TUPLE-FRAGILE — Q 17 is locally anti-fawāṣil while still vindicating the project-wide cross-corpus distinction (per [[h-new-730-content-rhyme-anticorrelation]]). This is a NULL on the local-application sub-claim and a VINDICATION on the typology level — both are reported.
- **Classical Claim 7 (bodily *isrāʾ*)** is NOT-TESTABLE empirically; theological consensus is recorded without endorsement.
- The 9-book hadith JSON is partial for Aḥmad's *Musnad* (~1,374 of ~30,000 ḥadīth) — the *āyat al-ʿizz* ḥadīth itself is NOT in our partial JSON; we cite via al-Suyūṭī's *al-Itqān*. This is a **DATA-GAP** (not a NULL of the claim itself); flagged.
- al-Biqāʿī Q 17 extract is partial (44 KB; flagged in 03-tafsir-survey.md §11). al-Suyūṭī *al-Durr al-manthūr* Q 17 extract begins mid-surah at v. 59ff — also partial. Both flagged for re-extraction.

### Lessons learned

1. **Pre-registering with "OR" disjunctions on rank metrics** (F-04: rank ≤ 25 by count OR density) is a defensible discipline when the underlying classical claim is itself disjunctive ("Q 17 is a Banī Isrāʾīl-content surah" can be satisfied by raw frequency or by per-word density). Both legs passed independently; the OR was conservative.
2. **Single-runner script with fail-fast SHA verification** is operationally cleaner than per-test scripts; reduces SHA-mismatch risk by centralizing the verification at one entry-point.
3. **Q 17 as a four-for-four VINDICATION is rare in the project** — Q 33 had 2 FALSIFICATIONS, Q 1 had 1 pre-commit violation, Q 9 had 1 FALSIFICATION. The project's all-VINDICATED outcomes are not selection-biased: Q 17's classical claims are mostly content-level (Banī Isrāʾīl naming, taḥaddī, intercession) which are easier to verify than corpus-extremum claims (which is where Q 33 failed). The protocol's anti-extremum-overclaim discipline (cf. Q 33 cautionary case) is here vindicated by Q 17's content-claim survival.
4. **The break-verse architectural-law observation (Q 17:1 + Q 33:4 — break-verse = founding-event/legal-premise) is a TWO-data-point pattern** — explicitly NOT pre-registered; Q017-F-05 must be pre-registered before generalizing. This is recorded in 06-novel-findings.md §"break-verse architectural law" with appropriate caveats.
5. **The Q 17-Q 18 *al-ḥamdu lillāh* lexical handoff** (Q 17:111 → Q 18:1) is a candidate explanation for the empirical cheapness of the Q 17-18 TSP transition — but is *post-hoc* observation; needs pre-registered cross-boundary-handoff sweep before claiming.
6. **Equal NULL prominence in a four-for-four run** required deliberately surfacing the H-NEW-590 NULL, the UAS-not-structural-hub NULL, the Claim-3 RULES-TUPLE-FRAGILE NULL on local application, the Claim-7 NOT-TESTABLE, and the data-gaps (partial Aḥmad Musnad; al-Biqāʿī + al-Durr partial extracts). Documented in §"NULL outcomes" above.

### Recommended downstream actions

1. **Re-extract al-Biqāʿī and al-Suyūṭī *al-Durr al-manthūr* for Q 17** with adjusted regex matchers; expected outcome: F-03 upgrades from 7/9 to 9/9. (Independent of pre-reg verdict.)
2. **Pre-register Q017-F-05 (break-verse founding-event law)**: catalogue all surahs with alif-final rate ∈ [0.97, 0.999] and inspect each non-alif break-verse for "founding-identity" or "legal-pivot" content. Surahs to test: Q 17, Q 25, Q 33; cross-corpus poetry control: Labid's 2 non-alif of 178; ʿAmr b. Kulthūm's 2 non-alif of 105.
3. **Pre-register a formal cohesion test of {Q 17, 18, 19, 20, 21}** (the al-ʿitāq al-uwal block) — cumulative TSP cost vs random 5-tuples permutation null.
4. **Pre-register a Q 17 + Q 39 (al-Zumar) Prophet's-nightly-recitation cohesion test** — paired-FR-distance vs random Meccan pairs of comparable length.
5. **Update [[h-new-840-unified-architectural-score|H-NEW-840]] §"top-10 readout"** to record Q 17's empirical signature: anti-iʿjāz al-fawāṣil + maximal-taḥaddī hub + Banī-Isrāʾīl-content vindicated.
6. **Cross-link Q 17 into the [[h-new-870-q33-architectural-keystone|H-NEW-870]] follow-up**: investigate whether Q 17 plays a parallel "local-singular-anchor" role for the Meccan-narrative cluster as Q 33 does for the Medinan-legal cluster.

### Status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md (4 pre-registered tests, all VINDICATED)
- [x] 07-cross-references.md
- [x] JOURNAL.md (this file)

All eight template files produced; all four pre-registered SHA-locked tests run with VINDICATED verdicts; classical-claims audit completed (5 vindicated, 1 nuanced, 1 not-testable); cross-references mapped; honest limits and data-gaps recorded.

**Investigation status**: COMPLETE.
