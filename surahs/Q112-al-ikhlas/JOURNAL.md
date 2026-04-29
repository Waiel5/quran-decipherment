---
surah: 112
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — Wave-D launch
---

# Q 112 al-Ikhlāṣ — Investigation Journal

## 2026-04-28 — Wave-D launch

### Pre-flight reading

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/` (polished template)
- `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/` (single-surah short-reference template)
- `/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (4-cell typology; Q 112 = *iʿjāz-al-maʿnā* exemplar)

### H-NEW data integration

Pulled and integrated from `findings/phase-b-hypotheses/csv/`:

- **H-NEW-840** UAS = −2.4622, **rank 109 / 114** (bottom decile).
- **H-NEW-590** outlier-strength Δ%=0.00 (NULL classification, rank 44/114).
- **H-NEW-720** canonical-adjacency: Q 111-Q 112 = 0.0221 (0.27%, rank 89/113); Q 112-Q 113 = 0.0683 (0.82%, rank 52/113).
- **H-NEW-750** sig_A=+0.2275 (rank 54), sig_B=+1.2417 (rank 18); rhyme entropy 0.000 (100% د monorhyme).
- **H-NEW-111** mean FR distance to corpus = 0.7592 — **rank 1 / 114 corpus FR-centroid**.

### Pre-registered novel tests run

| Pre-reg | Test | Pre-reg SHA-head | Verdict |
|:--|:--|:--|:--|
| Q112-F-01 | FR-centroid status | 6e4cdfbec48e | **VINDICATED** rank 1/114; Bonferroni-significant |
| Q112-F-02 | Modal-root density mechanism | 4d553d5a684c | SPLIT — top-20 PASS-DIRECTIONAL (rank 4); top-50 NULL (rank 76) |
| Q112-F-03 | Theological-proposition density | f28637a062ad | VINDICATED — rank 1/5 comparators |
| Q112-F-04 | *aḥad*-bookend chiasm rules-tuple stability | 5eede724edc0 | VINDICATED-RULES-TUPLE-STABLE across 3 tashkeel variants |

### 5 classical claims audited (per `05-classical-claims-audit.md`)

| Claim | Verdict |
|:--|:--|
| 1. *thuluth al-Qurʾān* (al-Bukhārī #5013-15) | VINDICATED — Q 112 = FR-centroid rank 1 |
| 2. *al-ṣamad* hapax | VINDICATED — strict QAC corpus-hapax |
| 3. 4 verses → 4 distinct *tawḥīd* propositions | STRUCTURALLY VINDICATED |
| 4. *qul*-cluster terminal placement | VINDICATED — 4/6 terminal surahs *qul*-opened |
| 5. *iʿjāz al-maʿnā* cell exemplar | VINDICATED — canonical exemplar |

### Decision points

- **Q 112's rank-1 FR-centroid status was higher than pre-registered (top-10 was the H1 threshold)**. The H1-strong (rank=1) variant was also pre-registered. Result published as VINDICATED-AT-STRONG-DIRECTION; not a post-hoc upgrade.
- **Q112-F-02 SPLIT result** (top-20 PASS / top-50 NULL) honored: NULL on top-50 published with full prominence; mechanism-claim downgraded to *partial* / DIRECTIONAL.
- **Cell-exemplar status (Claim 5)** is *post-hoc* in the sense that the 4-cell typology was informed by Q 112's signature; flagged in audit honest-limits.
- Hadith-chain-quality audit relies on canonical chain-grades (Sunnī ṣaḥīḥ); we do NOT re-audit at sanad-level (out of project scope).

### Tafsir survey (DATA-GAP NOTICE)

Per-surah Q 112 tafsir extracts NOT pre-extracted in `data/literature/classical-tafsir/raw/` (only Q 1, 2, 9, 10, 17 are pre-extracted). The 8-mufassir survey relies on classical positions cross-referenced from secondary indexing. Subsequent agents should extract Q 112 sections from the openiti.raw masters (al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Suyūṭī, al-Zamakhsharī, al-Biqāʿī, al-Ṭabarsī, al-Thaʿlabī) for citation-passage granularity.

### Hadith corpus (DATA-GAP NOTICE)

`/Users/grey/Downloads/quran/data/literature/hadith/Q112-citations.md` does NOT exist (parallel to Q001-, Q002-, Q009-citations.md). Subsequent agents should index the 9 books for Q 112 to canonical-number granularity. Current 04-hadith-corpus.md uses canonical chain-citations.

### Honest limits

1. Single-pipeline FR-roots methodology (K=500, Dirichlet α=0.5). Robustness under alternative metrics is honest-limit.
2. Bonferroni-corrected α=0.0125 met by Q112-F-01 (rank-1) but NOT by Q112-F-02 (rank-4 strict). Verdicts are Bonferroni-aware.
3. The 4-cell typology cell-membership is post-hoc cell-formalization, flagged in 05-audit Claim 5.

### Outputs

- 9 markdown files in `surahs/Q112-al-ikhlas/`.
- 4 pre-reg files (Q112-F-01 through Q112-F-04).
- 4 run scripts in `scripts/`.
- 4 JSON outputs in `csv/`.
- 4 finding markdowns (Q112-F-01 to Q112-F-04 done).

### Pre-reg SHAs (locked)

```
Q112-F-01: 6e4cdfbec48ea9067bfc805077b042ca859e346582b63d3e1d245e7946d2f0f0
Q112-F-02: 4d553d5a684cc28d934e37652b27a7f27732698a5ccff48019c3a91a3171d772
Q112-F-03: f28637a062ad652b31fcec04c8eff6630e5f18250aaf59423a17e8fbb2d86791
Q112-F-04: 5eede724edc02c62dcc2299deae23fd0a5c8bd8daa4ad5850ffe12e383c28acf
```

### Status: Q 112 al-Ikhlāṣ specialist run COMPLETE.

Bismillāhi al-Raḥmāni al-Raḥīm.
