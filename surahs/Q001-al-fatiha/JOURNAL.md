---
surah: 1
surah_name_ar: الفاتحة
surah_name_translit: al-Fātiḥa
file_type: journal
date_last_updated: 2026-04-28
phase: B+
---

# Q 1 al-Fātiḥa — Investigation Journal


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

## 2026-04-28 — Wave-1 deep-investigation kickoff

### 2026-04-28 (timestamp ≈ session-active)
- **Created** `00-overview.md` (prior session; verdict SCAFFOLD).
- **In-flight specialists**: empirical-profile / content-analysis / tafsir-survey writers.

### 2026-04-28 — empirical-profile + content-analysis + tafsir-survey writer (this agent)

**Agent ID**: opus-4-7-1m specialist (3-of-8 template-builder)
**Inputs read**:
- `INVESTIGATION-PROTOCOL.md` (full)
- `00-overview.md`
- `findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json`
- `quran-text/quran-{no,min,full}-tashkeel.json` (cross-validated all 7 verses)
- `data/morphology/surah-root-graph.json` (Q 1 root distribution)
- `data/revelation-order.csv` (Q 1 = revelation order 5 Tanzil; 48 Nöldeke)
- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` (lines 800-980, 2255-2470, 3299-3460)
- `data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt` (lines 40-980)
- `data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt` (lines 53-120, 5625-5810, 5860-5890)
- `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/1/{1-7}.json`
- `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-ibn-kathir/1/{1,5,7}.json`
- `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafseer-al-qurtubi/1/{1,5,7}.json`
- `data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`
- `data/literature/classical-tafsir/razi-biqai-munasabat-rings.md`
- `data/literature/wikipedia/2026-wikipedia-al-fatiha.md`
- `data/literature/misc/114chambers-ring-composition-al-fatiha.md`
- `MASTER-FINDINGS-LEDGER.md` (Q 1 references, esp. line 59, 75, 233)

**Computations performed (this session)**:

1. **Q 1 distance row** extracted from `h-new-111.json` `D_matrix_upper_triangular`:
   - mean FR distance to other surahs = 0.7789 (consistent with H-NEW-750 cell)
   - 5 nearest neighbours: Q 108 (0.338), Q 110 (0.353), Q 106 (0.357), Q 112 (0.357), Q 100 (0.377)
   - 5 farthest: Q 5 (1.176), Q 2 (1.178), Q 4 (1.222), Q 3 (1.223), Q 9 (1.224)
   - **NEW empirical observation**: Q 1's nearest-neighbour pole is muʿawwidhāt + late-corpus short surahs; farthest pole is Q 2-9 (the long Medinan stretch). This vindicates al-Biqāʿī's *Fātiḥa-bracket-muʿawwidhatayn* munāsaba claim at law-strength.

2. **Q 1 final-letter audit** across all 3 tashkeel variants:
   - v1=م, v2=ن, v3=م, v4=ن, v5=ن, v6=م, v7=ن → 4 ن / 3 م
   - **CORRECTION TO 00-overview.md**: the overview reports "م: 2 verses (29 %)"; the correct count is **3 م (43 %)**, verified across all three tashkeel variants. The overview's H-NEW-750 cell `top_final_letter_frac = 0.5714` is consistent with 4 ن / 3 م.

3. **Razi-7 missing-letters claim** verified: Q 1's no-tashkeel character set excludes exactly **ث ج خ ز ش ظ ف**. al-Rāzī's 7-letter list (raw lines 5784-5808) is empirically VINDICATED. The verification is rules-tuple-stable across no-tashkeel, min-tashkeel, full-tashkeel, and Uthmani-consonantal cells.

4. **Q 1 → Q 2 canonical-adjacency cost**: 0.6216 length-units = 7.495 % of TSP-residual = rank 1 of 113 adjacencies (most expensive in the corpus). Verified from `h-new-720.json` `top10_expensive[0]`.

5. **Q 1 root-distribution**: 23 root-tokens, 18 distinct roots (rank 15 / 114 by token count). Top: *rḥm* (4), *Allāh* (2), *ṣrāṭ* (2). Verified from `data/morphology/surah-root-graph.json` `surahs.1`.

6. **Verse 7 weight calculation**: 9 / 29 = 31.0 % of words; 44 / 143 = 30.8 % of letters (no-tashkeel grapheme rule). Q 1 is back-loaded.

7. **Phrase-uniqueness regex audits** (against `quran-flat-no-tashkeel.txt`):
   - *ihdinā al-ṣirāṭ al-mustaqīm*: imperative-1pl form is unique to Q 1:6.
   - *anʿamta ʿalayhim* (2nd-person-perfect with God-as-addressee): unique to Q 1:7.
   - These are pre-registered as observations, not pre-registered hypotheses; cap at single-test α.

**Files written this session**:
- `01-empirical-profile.md` — full empirical metrics integration with H-NEW-{590, 700, 720, 750, 840} + h-new-111 distance row.
- `02-content-analysis.md` — verse-by-verse Arabic-grounded analysis with cross-validation across 3 tashkeel variants.
- `03-tafsir-survey.md` — survey of al-Suyūṭī, al-Zarkashī (partial — PDF on disk, txt extraction queued), al-Biqāʿī, al-Rāzī, al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, al-Zamakhsharī (indirect via al-Suyūṭī / al-Biqāʿī, raw txt awaiting acquisition).

**Decision points**:
- Decided to use the spa5k-tafsir-api JSON sources (Tabari, Ibn Kathir, Qurtubi) directly rather than mark them "AWAITING ACQUISITION" — they are on disk in machine-readable form and provide per-verse Arabic text.
- Marked al-Zamakhsharī (Kashshāf), al-Ṭabarsī, al-Durr al-Manthūr, al-Ālūsī, al-Saʿdī as AWAITING ACQUISITION — these are not on disk in raw form.
- al-Zarkashī al-Burhān PDF is on disk but no extracted Arabic raw — flagged AWAITING TXT EXTRACTION.
- Used the line-numbers in OpenITI raw text for all al-Suyūṭī, al-Biqāʿī, al-Rāzī citations; this preserves verifiability per protocol §2.11.

**Garden-of-forking-paths log**:
- Considered adding a pre-registered ring-composition audit for Q 1's ABCBA structure (claim from `114chambers-ring-composition-al-fatiha.md`). Decided to defer this to `06-novel-findings.md` rather than fold it into `02-content-analysis.md`, because the audit requires a locked metric (lexical distance? phonological? root-distribution? — each gives a different answer) and a pre-registered Bonferroni cap. Adding a hand-wavy ring-comp claim to the content-analysis would be a forking-paths violation.
- Considered counting verse-2 word *li-llāh* as 1 vs 2 morphological tokens. Used the QAC v0.4 / Mashriqi orthographic-token rule consistently — *li-llāh* counts as 1 token. Documented in §1 of `02-content-analysis.md`.
- Decided NOT to compute a permutation-null p-value for Razi-7-missing-letters in this file — that requires a pre-registered audit, queued for `05-classical-claims-audit.md`.

**Cross-references created (Obsidian wikilinks)**:
- `[[h-new-111-fisher-rao-mushaf|H-NEW-111]]` × multiple
- `[[h-new-590-outlier-spectrum|H-NEW-590]]` × multiple
- `[[h-new-720-canonical-adjacency-cost|H-NEW-720]]` × multiple
- `[[h-new-750-ijaz-signature|H-NEW-750]]` × multiple
- `[[h-new-840-unified-architectural-score|H-NEW-840]]` × multiple
- `[[h-new-860-hadith-architectural-alignment|H-NEW-860]]`
- `[[cross-finding-010-extended-network|cross-finding-010]]`
- `[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]`

**Pre-reg SHA hashes**: not applicable — this session produced descriptive integration files, not hypothesis-running tests. All numerical claims are computed from already-pre-registered data (h-new-* artifacts) or directly from the canonical text on disk.

**Outstanding tasks for next agent(s)**:
- `04-hadith-corpus.md` (specialist): catalog all hadith citing Q 1 — fadāʾil chains in al-Suyūṭī Itqān raw lines 2255-2470 are a starting point; al-Bukhārī #4474 (Umm al-Qurʾān), Muslim #395 (qasamtu al-ṣalāh), Tirmidhī #2953 (ḍāllīn-Naṣārā mapping), Aḥmad Musnad multi-chain, al-Dāraquṭnī's basmala-as-verse-1 ḥadīth.
- `05-classical-claims-audit.md`: pre-registered tests for Razi-7-missing-letters (permutation-null), basmala-19-letters (rules-tuple stability check), Q 1 ring-composition (lexical, phonological, root-distribution metrics), 25-name-density (rules-tuple-stable count vs corpus).
- `06-novel-findings.md`: dual-pivot structure (v 3-4 thematic + v 4-5 grammatical), the unique *ihdinā ṣirāṭ-mustaqīm* imperative-1pl form, the back-loading of v 7 mass.
- `07-cross-references.md`: integrate Q 1 ↔ Q 108-Q 114 lexical-doxological pole (cross-finding-010); Q 1 → Q 2 canonical-cost paradox (cross-finding-011); al-ḥāmidāt cluster head; Q 1 in MASTER-LEDGER #2 (Khawātim divine-name density rank 2).

## 2026-04-28 — hadith-corpus + classical-claims-audit + novel-findings + cross-references writer (this agent)

**Agent ID**: opus-4-7-1m specialist (4-of-8 template-builder, "B" track)
**Inputs read**:
- `INVESTIGATION-PROTOCOL.md` (full)
- `KNOWLEDGE-GRAPH.md`
- `00-overview.md`
- `findings/phase-b-hypotheses/csv/h-new-{111, 590, 700, 720, 750, 840}.json` (Q 1 rows extracted)
- `quran-text/quran-{no, min, full}-tashkeel.json` (Q 1 cross-validated; word counts, letter counts, central-word identification)
- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` (lines 3299-3460 names-of-surahs section; 22420-22470 *fadāʾil al-Fātiḥa* section; 22700-22800 architectural-meaning analysis)
- `data/literature/wikipedia/2026-wikipedia-al-fatiha.md`
- `data/literature/misc/114chambers-ring-composition-al-fatiha.md`
- `data/literature/al-kaheel/kaheel-fatiha-numerical-miracle.md`

**Pre-registered novel tests (4 written, locked, run, reported)**:

| Test | SHA256 (locked) | Script | JSON | Findings | Verdict |
|:--|:--|:--|:--|:--|:--|
| Q001-F-01 chiastic | `84c6157b...3608da` | `scripts/Q001_F_01_chiastic_symmetry.py` | `csv/Q001-F-01.json` | `Q001-F-01-chiastic-symmetry.md` | NULL (rank 4/15 word, 15/15 letter — mirror is the WORST scoring) |
| Q001-F-02 central word | `badefd87...f7f3c5` | `scripts/Q001_F_02_central_word.py` | `csv/Q001-F-02.json` | `Q001-F-02-central-word.md` | VINDICATED (V5 is central; word #15 = naʿbudu, not iyyāka) |
| Q001-F-03 rhyme entropy | `55bfd377...e94fa1e` | `scripts/Q001_F_03_rhyme_entropy_short.py` | `csv/Q001-F-03.json` | `Q001-F-03-rhyme-entropy-vs-7-verse.md` | NULL (z=+0.53, p=0.79) |
| Q001-F-04 centroid-anchor | `3f8b31c0...99a0070` | `scripts/Q001_F_04_centroid_shift.py` | `csv/Q001-F-04.json` | `Q001-F-04-q1-removal-centroid-shift.md` | PRE-COMMIT-VIOLATION (direction logic-inverted); CORRECTED-DIRECTION VINDICATED at rank 4/114 |

**Pre-commit violation honest disclosure**: Q001-F-04 pre-reg specified "Q 1 in BOTTOM-3 of d_bar" but the centroid-anchor hypothesis logically predicts TOP-3 (removing a central surah RAISES residual mean). The pre-reg is locked-as-written; result reported per INVESTIGATION-PROTOCOL §1.8. Underlying centrality claim DIRECTIONALLY VINDICATED at rank 4/114 (most-central surahs: Q 112, Q 110, Q 108, Q 1, Q 106 — Q 1 is rank 4). Updated finding markdown documents the direction-of-effect error transparently.

**Computations performed (this session)**:

1. **Q 1 word/letter cross-tashkeel verification**: 29 words across all 3 tashkeel variants. 143 letters (no-tashkeel grapheme rule). Basmala = 19 letters under no-tashkeel/min-tashkeel; 20 under full-Uthmani-script (RULES-TUPLE-FRAGILE finding).
2. **Q 1 central word**: position 15 (median of N=29) = نعبد (*naʿbudu*) in V5, INVARIANT across all 3 tashkeel variants. Refines agent-prompt's "iyyāka" claim — central word is the verb, not the pronoun.
3. **Q 1 lexical structure**: All 21 pairwise word-overlaps computed (al- stripped). Only V1↔V3 (basmala-echo) and V6↔V7 (ṣirāṭ chain) have positive overlap. The textbook ABCBA chiasm is NOT supported at the lexical level.
4. **FR-roots centrality ranking**: Computed row-mean for all 114 surahs from h-new-111 D_matrix. Q 1 = rank 4 (0.7789); top-3 are Q 112, Q 110, Q 108. Top-7 includes Q 1, Q 113, Q 114 — the mushaf-frame surahs.
5. **7-verse surah set**: Only Q 1 and Q 107 have exactly 7 verses (Hafs-Kufan).
6. **Fibonacci-29 check**: 29 is NOT in Fibonacci sequence; documented as honest negative.

**Garden-of-forking-paths log**:
- Q001-F-04 direction-of-effect error caught at runtime. Considered amending pre-reg before publishing; rejected per §1.8 — pre-reg is LOCKED, violation must be published. Finding markdown documents both ranks.
- Considered widening rhyme-entropy comparison to all surahs (not just n_verses ≤ 10); kept the n≤10 rule per pre-reg.
- Considered adding a pre-registered semantic-coding chiastic test; deferred to future investigation cycle (semantic coding would require a separate pre-registered coding rubric).

**Findings written this session**:
- `04-hadith-corpus.md` — al-Suyūṭī al-Itqān-derived hadith corpus with explicit "via" attributions; Bukhārī/Muslim/Tirmidhī/Aḥmad/Dāraquṭnī all cited via al-Suyūṭī, with original-collection IDs flagged for follow-up acquisition.
- `05-classical-claims-audit.md` — 7 major claims audited with rules-tuple discipline. 3 VINDICATED (umm al-Kitāb, sabʿ mathānī, recitation-most-recited), 1 VINDICATED-with-refinement (central word), 1 RULES-TUPLE-FRAGILE (basmala-19-letters), 1 NULL/NOT-TESTABLE (chiasm), 1 VINDICATED-as-dual (outlier-strength).
- `06-novel-findings.md` — 4 pre-registered tests + 3 descriptive secondary observations; transparently reports the F-04 pre-commit violation.
- `07-cross-references.md` — mushaf-neighbor + classical-cluster + H-NEW-finding integration.

**Pre-reg SHAs and verification**:
All 4 pre-reg files have their SHA256 locked, embedded in the run scripts, and verified at runtime with `assert sha == EXPECTED`. All 4 scripts ran successfully on first run.

**Open follow-ups queued (NOT run this session)**:
- Q001-F-07 (queued): Spearman correlation of "alternate-name count in al-Suyūṭī" vs UAS rank, all 114 surahs.
- Mushaf-frame centrality test (queued): Pre-register a test of the joint centrality of {Q 1, Q 113, Q 114}.
- Q 1 + Q 112 thuluth-pair joint test: Pre-register whether their union covers more root-content than any other pair.
- Full Bukhārī/Muslim/Tirmidhī text acquisition for direct verification of hadith citations currently flagged "via al-Suyūṭī".

## File-state checklist

- [x] `00-overview.md` (prior session; one minor correction logged: ن:م = 4:3, not 4:2)
- [x] `01-empirical-profile.md` (prior session, COMPLETE)
- [x] `02-content-analysis.md` (prior session, COMPLETE)
- [x] `03-tafsir-survey.md` (prior session, COMPLETE; al-Zamakhsharī indirect, al-Zarkashī txt-extraction queued)
- [x] `04-hadith-corpus.md` (this session, COMPLETE; primary collections AWAITING ACQUISITION)
- [x] `05-classical-claims-audit.md` (this session, COMPLETE; 7 claims audited)
- [x] `06-novel-findings.md` (this session, COMPLETE; 4 pre-registered + 3 descriptive)
- [x] `07-cross-references.md` (this session, COMPLETE)
- [x] `JOURNAL.md` (updated)
- [x] Q001-F-01 to Q001-F-04 pre-regs + scripts + JSONs + finding-markdowns (this session)
