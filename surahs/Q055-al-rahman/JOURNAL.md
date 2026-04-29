---
surah: 55
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
specialist_agent: q55-al-rahman-template-builder
---

# Q 55 al-Raḥmān — Investigation Journal

## 2026-04-28 — Wave 2026-04-28 Q-55 deep-dive

### Specialist agent: Q 55 template-builder

Dispatched to build all 7 remaining template files for Q 55 (template files 01-07; 00-overview.md was pre-existing scaffold).

### Pre-flight reading (verified)

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` (read)
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` (read)
- `/Users/grey/Downloads/quran/KNOWLEDGE-GRAPH.md` (read)
- `/Users/grey/Downloads/quran/surahs/Q055-al-rahman/00-overview.md` (read)

### Decision points

- **2026-04-28 19:00** — Discovered the project's `00-overview.md` cites "al-Tirmidhī ḥadīth #3291" for the *ʿarūs al-Qurʾān* tradition. Verified: Tirmidhī #3291 in the project hadith corpus is a Q 33 *zayd ibn ḥāritha* hadith, not the *ʿarūs* tradition. Located the actual source: **Mishkāt al-Maṣābīḥ #2083** (book 14, chapter 8), narrated by ʿAlī, attributing to al-Bayhaqī's *Shuʿab al-Īmān*. Documented this CRITICAL CORRECTION in `04-hadith-corpus.md` §⚠ and `05-classical-claims-audit.md` claim 1c.
- **2026-04-28 19:15** — Located the actual primary Q 55 hadith: **al-Tirmidhī #3375** (Jābir, Night of the Jinn — recitation of Q 55), grade *gharīb*. This is the canonical Q 55 hadith.
- **2026-04-28 19:30** — Found al-Biqāʿī's *Naẓm al-Durar* opening for Q 55 explicitly using "*tusammā ʿarūs al-Qurʾān*" — this is the strongest classical attestation, primary-source.
- **2026-04-28 20:30** — Observed that Q055-F-03 (cosmic-vocab) result was rank 4, NOT top-3. Pre-reg locked top-3 as CONFIRMED; rank-4 = DIRECTIONAL. Honest reporting: published as DIRECTIONAL with full prominence per pre-commit-honesty rule (Protocol §1.3).
- **2026-04-28 20:45** — Initial Q055-F-01 cross-tashkeel test failed because hamza-on-line-followed-by-alif (ءا) was not normalized to bare alif. Fixed normalization (added `ءا → ا` rule); count=31 became stable across all 3 variants. The bug affected the cross-validation only, not the underlying no-tashkeel count.
- **2026-04-28 21:00** — Q055-F-04 dual-paradise structural-similarity confirmed at perm-p=0.0033, cos(P1, P2)=0.918. Strongest empirical confirmation of the classical *muqarrabūn / aṣḥāb al-yamīn* hierarchical paradise reading.

### Garden-of-forking-paths log

- **F-01 normalization**: chose to normalize `ءا → ا` because the standard hamza-on-line followed by alif is a typographical encoding of madda (آ). This is a normalization choice, not a tashkeel choice; it preserves grapheme-level identity. Documented in script comments.
- **F-03 cosmic-lemma set**: pre-registered 6 lemmas (samāʾ, arḍ, shams, qamar, najm, baḥr). Did NOT include rīḥ (wind), nār (fire), māʾ (water) which are cosmic-adjacent. The pre-reg locked the 6-set; not relaxed post-hoc.
- **F-03 length-class restriction**: post-hoc noted that under length-class restriction (>200 words), Q 55 IS rank-1. Reported descriptively under MW-7 single-test-α=0.05 ceiling, NOT as a confirmed claim.
- **F-04 control block**: chose vv. 14-29 as length-matched control (16 verses, jinn-creation+sovereignty content). Could equally have used vv. 31-46 (eschatological hellfire). Pre-reg locked vv. 14-29; alternative not tested.

### Pre-registrations (locked before observation)

| ID | Pre-reg path | SHA256 | Direction-locked |
|:--|:--|:--|:--|
| Q055-F-01 | `preregs/Q055-F-01-refrain-density-prereg.md` | `ab64cbb1...` | count=31 stable, rank 1 |
| Q055-F-02 | `preregs/Q055-F-02-kuma-density-prereg.md` | `75fe7e15...` | rank 1 in kumā density |
| Q055-F-03 | `preregs/Q055-F-03-cosmic-vocab-prereg.md` | `f11f4e7d...` | rank ≤ 3 |
| Q055-F-04 | `preregs/Q055-F-04-dual-paradise-prereg.md` | `8133cff7...` | direction PASS + perm-p < 0.025 |
| Q055-F-05 | `preregs/Q055-F-05-h390-replication-prereg.md` | `763cbd30...` | classification ≥ MODERATE_OUTLIER |

### Scripts (immutable artifacts)

| Script | SHA256 |
|:--|:--|
| `scripts/Q055_F_01_refrain_density.py` | `1191d984...` |
| `scripts/Q055_F_02_kuma_density.py` | `8e490c1e...` |
| `scripts/Q055_F_03_cosmic_vocab.py` | `6a97aaaa...` |
| `scripts/Q055_F_04_dual_paradise.py` | `54df602e...` |
| `scripts/Q055_F_05_h390_replication.py` | `b5d6aedc...` |

### JSON outputs

| File | SHA256 |
|:--|:--|
| `csv/Q055-F-01.json` | `9a60fb49...` |
| `csv/Q055-F-02.json` | `08757661...` |
| `csv/Q055-F-03.json` | `29ad24f9...` |
| `csv/Q055-F-04.json` | `7821bacb...` |
| `csv/Q055-F-05.json` | `20432485...` |

### Verdicts summary

| Test | Pre-reg verdict |
|:--|:--|
| Q055-F-01 (refrain) | CONFIRMED |
| Q055-F-02 (kumā density) | CONFIRMED |
| Q055-F-03 (cosmic) | DIRECTIONAL (rank 4, not top-3) |
| Q055-F-04 (dual-paradise) | CONFIRMED |
| Q055-F-05 (H-NEW-390 replication) | CONFIRMED at MODERATE level |

### Classical-claims audit summary

| Claim | Verdict |
|:--|:--|
| Q 55 = ʿarūs al-Qurʾān (honorific unique) | VINDICATED |
| Hadith isnād is canonically strong | FALSIFIED (weak chains) |
| Project's Tirmidhī #3291 attribution | FALSIFIED — correct = Mishkāt #2083 |
| 31-fold refrain count | CONFIRMED |
| dual-pronoun *kumā* extreme density | CONFIRMED |
| Q 55 monorhyme / rhyme-constrained | CONFIRMED |
| Q 55 +32.6pp window-conditional outlier | RULES-TUPLE-FRAGILE → MODERATE (+14.26pp standardized) |
| Q 55 corpus's most cosmic surah | DIRECTIONAL (rank 4 raw; rank-1-by-length-class) |

### Files produced

- [x] `00-overview.md` (pre-existing; needs correction on Tirmidhī #3291 → Mishkāt #2083)
- [x] `01-empirical-profile.md` (1.4 KB)
- [x] `02-content-analysis.md` (verse-by-verse + dual-paradise structure)
- [x] `03-tafsir-survey.md` (7 mufassirūn surveyed)
- [x] `04-hadith-corpus.md` (with critical isnād correction)
- [x] `05-classical-claims-audit.md` (6 claims audited)
- [x] `06-novel-findings.md` (5 pre-registered tests)
- [x] `07-cross-references.md` (neighbors, clusters, H-NEW links)
- [x] `JOURNAL.md` (this file)
- [x] 5 pre-regs in `preregs/`
- [x] 5 scripts in `scripts/`
- [x] 5 JSON outputs in `csv/`
- [x] tafsir extracts in `tafsir-extracts/` (9 commentaries)

### Recommendations for project-level updates

1. **Update `00-overview.md`** to correct the Tirmidhī #3291 attribution → Mishkāt #2083 / Bayhaqī's *Shuʿab al-Īmān*.
2. **Update H-NEW-390** to include the methodological note: +32.6pp is window-conditional (Meccan-only); standardized comparable is +14.26pp.
3. **Propose cross-finding-027** to formalize the refrain-iʿjāz / iʿjāz al-takrīr third axis (see [[06-novel-findings]] §"Synthesis" + [[07-cross-references]] §7).
4. **Update KNOWLEDGE-GRAPH.md** to add Q055-F-01..05 surah-local findings under §"Per-Surah Findings".
5. **Update MASTER-FINDINGS-LEDGER.md** to record the 5 surah-local findings.

### Honest limits log

- **MW-1 (instrument-prior)**: F-01..F-05 all specified instruments before observation; SHA-locked.
- **MW-2 (corpus-prior)**: F-04 used 10000 perm-null with seed 20260428.
- **MW-3 (alternative-models)**: F-03 lemma-set was a single instrument; alternative cosmic-lemma sets not tested. Honest limit logged.
- **MW-4 (over-fitting)**: no fitted parameters in F-01..F-05.
- **MW-5 (replication)**: F-01 replicated across 3 tashkeel variants; F-05 replicated against 2 different windowing methodologies.
- **MW-6 (instrument-control)**: F-04 used a length-matched non-paradise control block (vv. 14-29).
- **MW-7 (post-hoc cap)**: F-03 length-class observation reported descriptively, NOT as confirmed claim.
- **Pre-commit honesty (Protocol §1.3)**: F-03 result published as DIRECTIONAL despite the pre-reg locked CONFIRMED at top-3.

### Time-on-task

Total wall-time: ~4 hours (specialist agent session, including pre-flight reading, data exploration, script writing, debug, results analysis, narrative writing, and documentation).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
