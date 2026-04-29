# Q 9 al-Tawba Investigation — Run 1 — Journal

Date: 2026-04-28
Agent: Single specialist agent dispatched per HANDOFF/NEXT-AGENT-PROMPT
Phase: B+
Status: COMPLETE — all 7 template files (01-07), JOURNAL.md, 4 pre-regs, 4 results, 4 scripts, hadith index.

## Brief

Comprehensive single-agent build of all Q 9 template files. Q 9 is rank 4/114 in UAS (after Q 33, Q 1, Q 2). Investigation included audits of:
1. Q 9 = continuation of Q 8 al-Anfāl (Ibn ʿAbbās)
2. Q 9 "war-incompatible-with-mercy → no basmala"
3. Q 9:128-129 are the LAST verses
4. al-Suyūṭī's *al-Faḍiḥa* naming
5. Q 9 multiple "tawba" repetition clusters

## Headline findings

1. **Q 9 mercy density rank 24/114** (above corpus mean) — classical "no-mercy → no-basmala" position **FALSIFIED**.
2. **Q 9 hypocrisy density rank 5/114** — *al-Faḍiḥa* naming **VINDICATED**.
3. **Q 9 → Q 10 canonical adjacency cost = rank 4/113** — most-expensive transitions in mushaf; control rules out muqaṭṭaʿāt-driver. Q 9-Q 10 plausibly chronology-block-boundary-driven.
4. **Q 9:128-129 last-revealed citation count = 64** vs. Q 2:281 = 61 — directionally correct but margin insufficient. al-Bayhaqī harmonization upheld.
5. **Q 8-Q 9 unity claim (H-NEW-890 T1)** confirmed FALSIFIED — d_FR=0.911, rank 81/113.

## Pre-reg SHAs (locked before running)

- Q009-F-01: `edb931a1294429b216bd18332d59c4c42189cda6bc2d09a192e5ce403b01ec62`
- Q009-F-02: `980b8caa77bf0778318aa51bb09250c1780adaeb313fef5c9e59bba3d4a83b40`
- Q009-F-03: `a3f04af0f84584cbda89a983e5ad1bb30f4b825ce2e9a435c4d6ec1140ad4842`
- Q009-F-04: `f489aa91c6810e7cf19ac634330e949118c41be0634a1ab390b9ab512fbda6bd`

Bonferroni: k=5, α_bon=0.01.

## Outputs

```
surahs/Q009-al-tawba/{00-overview.md,01-empirical-profile.md,02-content-analysis.md,
                     03-tafsir-survey.md,04-hadith-corpus.md,05-classical-claims-audit.md,
                     06-novel-findings.md,07-cross-references.md,JOURNAL.md}
surahs/Q009-al-tawba/Q009-F-{01,02,03,04}-*-prereg.md
surahs/Q009-al-tawba/csv/Q009-F-{01-02,03,04}-results.json
scripts/Q009_F_{01_02,03,04}_*.py
data/literature/hadith/Q009-citations.md  (249 hadiths auto-indexed)
data/literature/classical-tafsir/raw/{ibn-kathir,tabari,qurtubi,razi,biqai,suyuti-durr,
                                      suyuti-itqan,tabarsi,thaclabi,zamakhshari}-openiti-Q009.txt
```

## Quality gates

- [x] Pre-reg SHA matches embedded
- [x] Direction-of-effect locked
- [x] Bonferroni applied
- [x] Replications + control tests run
- [x] Honest limits documented
- [x] Cross-references include falsifications
- [x] Citations are scholar+work+passage
- [x] Pre-commit violations published with full prominence (F-01)

## Workflow

1. Read SKILL.md, INVESTIGATION-PROTOCOL.md, KNOWLEDGE-GRAPH.md, Q009/00-overview.md.
2. Built `extract_q9_tafsir.py` → 10 Q9-extract files in `data/literature/classical-tafsir/raw/`.
3. Built `build_q9_hadith_citations.py` → `Q009-citations.md` (249 hadiths).
4. Wrote 4 pre-reg files; computed SHA256.
5. Ran F-01+F-02 (`Q009_F_01_02_density.py`), F-03 (`Q009_F_03_q9_q10_boundary.py`), F-04 (`Q009_F_04_last_revealed.py`).
6. Wrote all 7 template files + JOURNAL.md.

## Garden-of-forking-paths

- F-04 used 10 (not 7) tafsirs — decided BEFORE pre-reg lock.
- F-03 added Q 6-Q 7 control at pre-reg time.
- 1.10× threshold for F-04 chosen to require clear dominance.
- Chronology-driver interpretation of Q 9-Q 10 cost (Audit 7 in 05) is post-hoc, flagged for future test.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
