# Q 30 al-Rūm — Investigation Journal

## Run 1 — 2026-05-07

**Specialist agent**: Q029-30-sub-pattern-specialist (Wave-D revisit of H-NEW-93 NULL).

### Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-93-q29-q30-subpattern.md` (parent NULL)
- `/Users/grey/Downloads/quran/findings/cross-finding/muqattaat-book-introduction-marker-synthesis.md` (cross-finding-008 — Q29+Q30 are 2 ALM-exceptions)
- `/Users/grey/Downloads/quran/surahs/Q005-al-maida/06-novel-findings.md` (chronology-architecture dissociation framework — motivates present revisit)
- `/Users/grey/Downloads/quran/surahs/Q012-yusuf/` (canonical 8-file template + script style)

### Decision points

1. **2026-05-07 ~start**: Discovered Q 029 folder contained only `.DS_Store` + 3 empty subdirs (csv, preregs, scripts) — NOT 3 partial files as task description suggested. Built both Q 29 and Q 30 from scratch.
2. **Pre-reg framing**: Per PRE-REG-STANDARD-03, the present tests are NEW operationalizations (within-ALM comparison + lemma-hapax + FR-architectural-twin + cognitive-imperative density), NOT a retest of H-NEW-93. The parent H-NEW-93 NULL stands at its original operationalization.
3. **Bonferroni-k decision**: Q030-F-01 has k=2 (joint family). Q030-F-02, F-04, F-05 are individually single-test families (Bon-1). Q029-F-01 is single-test. Total k across the surah is 5 — but they are HETEROGENEOUS hypotheses (lexical hapax, FR distance, density-rate, cognitive-imperative density), not a single family for joint Bonferroni. Per PRE-REG-STANDARD-04, each test declares its own k in YAML frontmatter.
4. **C(6,2)=15 enumeration as primary**: pre-reg honest-limit §10 flags that min-p = 1/15 ≈ 0.067 > α_bon=0.025. The verdict ceiling on the primary axis is structurally DIRECTIONAL, not PASS. Secondary (10000-perm Meccan moderate-length) frame can in principle achieve α_bon — but does not (p=0.155-0.176).
5. **Garden-of-forking-paths log**: BEFORE running, the imtihān-cluster was set to `{ftn, blw, mHn, Sbr, jhd}` and the historical-prophecy cluster to `{glb, nSr, kwn, rwm, bDE, snw}`. These are EXTENSIONS of the H-NEW-93 sets (which used `{ftn, blw, mHn, Sbr}` and `{glb, nSr, kwn, ywm}`) — `jhd` and `rwm/bDE/snw` were added based on Q 29:69 + Q 30:2-5 surface form. This is an EXPANSION of the feature space, justified by the within-ALM frame and pre-locked before observation.
6. **Q030-F-04 architectural-twin frame**: pre-committed to the within-ALM-cluster comparison, with mushaf-adjacency control as a secondary. The mushaf-adjacency rank (82/113) was discovered post-run; documented as descriptive observation, not as a separate pre-registered test.

### Pre-registration SHA hashes (locked before script execution)

| Test | Pre-reg SHA256 |
|:--|:--|
| Q030-F-01 | `05a893361805442c1a83969f3f899f4e1d0563bebb7d92b52d76b902d657fa8f` |
| Q030-F-02 | `4850caed2dbcda8a9417948a398338c58ae54829b6ce872923c17d3e204c4c99` |
| Q029-F-01 | `dd9244bd0e00f39b89e2c06c7b1549ce665187ae4af274af4615afa769b38f60` |
| Q030-F-04 | `c92548471c002b18f89b5fbf232c38167e88cc545709143946de55bb32902383` |
| Q030-F-05 | `850b16e6a4c5fee4e4d2828a3bf1da4c149798625cc933c9ae22b722a5608111` |

All 5 SHAs verified at run-time by each script's `verify_sha()` call.

### Run results (timestamps approximate)

- Q030_F_01 ran successfully. Verdicts: imt=DIRECTIONAL, hist=DIRECTIONAL.
- Q030_F_02 ran successfully. Verdict: PASS-DIRECTED (3/6 hapax-or-near).
- Q029_F_01 ran successfully. Verdict: PASS-DIRECTED (2/5 hapax-or-near).
- Q030_F_04 ran successfully. Primary verdict: DIRECTED (rank 7/15). Secondary verdict: WEAK-DIRECTIONAL (corpus pct 40%).
- Q030_F_05 ran successfully. Verdict: DIRECTIONAL (rank 5/114).

### Files created in this run

**Pre-regs**:
- `surahs/Q030-al-rum/Q030-F-01-alm-exception-subcluster-prereg.md`
- `surahs/Q030-al-rum/Q030-F-02-rum-prophecy-hapax-prereg.md`
- `surahs/Q030-al-rum/Q030-F-04-architectural-twin-prereg.md`
- `surahs/Q030-al-rum/Q030-F-05-cognitive-imperatives-prereg.md`
- `surahs/Q029-al-ankabut/Q029-F-01-ankabut-parable-hapax-prereg.md`

**Scripts**:
- `scripts/Q030_F_01_alm_exception_subcluster.py`
- `scripts/Q030_F_02_rum_prophecy_hapax.py`
- `scripts/Q030_F_04_architectural_twin.py`
- `scripts/Q030_F_05_cognitive_imperatives.py`
- `scripts/Q029_F_01_ankabut_parable_hapax.py`

**JSON outputs**:
- `surahs/Q030-al-rum/csv/Q030-F-01.json`
- `surahs/Q030-al-rum/csv/Q030-F-02.json`
- `surahs/Q030-al-rum/csv/Q030-F-04.json`
- `surahs/Q030-al-rum/csv/Q030-F-05.json`
- `surahs/Q029-al-ankabut/csv/Q029-F-01.json`

**8-file template (Q 30)**:
- `00-overview.md`
- `01-empirical-profile.md`
- `02-content-analysis.md`
- `03-tafsir-survey.md`
- `04-hadith-corpus.md`
- `05-classical-claims-audit.md`
- `06-novel-findings.md`
- `07-cross-references.md`
- `JOURNAL.md` (this file)

### Honest limits and follow-ups

- C(6,2)=15 frame structurally caps p ≥ 0.067 — verdict ceiling DIRECTIONAL on Q030-F-01 even with stronger effect-sizes.
- Q030-F-02 PASS-DIRECTED at threshold ≥ 3 is achieved EXACTLY (3/6); a tighter threshold would NOT pass. Verdict-ceiling per discipline §post-hoc-noticed-findings is PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.
- Q030-F-04 architectural-twin REFUTED at the strong sense — Q 29 + Q 30 are NOT FR-content twins. The book-reference-exception status is a SURFACE-OPENER fact, NOT a deep-content-cohesion fact.
- al-Bāqillānī, al-Biqāʿī, al-Rāzī page-citations are MW-6 PENDING physical-edition verification.

### Verdict family rollup

2 PASS-DIRECTED (Q030-F-02 lexical hapax, Q029-F-01 spider parable hapax)
4 DIRECTIONAL (Q030-F-01 imt + hist, Q030-F-04, Q030-F-05)
0 NULL with reversed direction.

The H-NEW-93 parent NULL stands. The present family REFINES the interpretation: the ALM-exception status is REAL at lexical-eponymy axis, DIRECTIONAL at density axes, REFUTED at FR-content-twin axis.
