---
surah: 67
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 9 template files + 7 pre-regs + 7 scripts + 7 JSON outputs (Wave-D launch + Wave-H additions)
---

# Q 67 al-Mulk — Investigation Journal

## 2026-04-28 — Wave-D specialist agent run

### Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/` (all 9 template files — polished template)
- `/Users/grey/Downloads/quran/surahs/Q055-al-rahman/` (Meccan comparator — directory listing)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840}.json` (relevant entries inspected for Q 67)

### H-NEW data integration

Pulled and integrated:

| H-NEW finding | Q 67 value | Rank/Class |
|:--|:--|:--|
| H-NEW-840 UAS | −2.0526 | **102 / 114** (bottom decile) |
| H-NEW-590 outlier | Δ = −0.20 pp | **NULL** classification, window {64-70} |
| H-NEW-720 Q66-Q67 cost | 0.0780 | rank 47/113 (mid-pack) |
| H-NEW-720 Q67-Q68 cost | 0.0962 | rank 36/113 (mid-pack) |
| H-NEW-750 sig_A | +0.3108 | rank 52/114 (mid-pack) |
| H-NEW-750 sig_B | −0.5663 | rank 67/114 |
| H-NEW-750 rhyme entropy | 0.7698 nats | dominant ر at 70% |
| H-NEW-111 mean FR distance | 0.892 (computed) | rank 67/114 (mid-pack) |
| H-NEW-111 nearest neighbour | Q 81 al-Takwīr (0.7531) | followed by Q 32 al-Sajda (0.7534) |

### Pre-registered novel tests run

| Pre-reg | SHA-head | Title | Verdict |
|:--|:--|:--|:--|
| Q067-F-01 | `591775e3a068` | Architectural rank cross-comparison (Q67 vs Q36/Q112/Q18) | **VINDICATED** (median rank 74; orthogonality confirmed) |
| Q067-F-02 | `f9f2d651034d` | Post-Hijra-kink distinctness (s=67) | **DIRECTIONAL_ENHANCED** — pre-commit-violation, honest report |
| Q067-F-03 | `6722a3a4f9af` | Corpus-singleton phrases (Q67:1, Q67:3-4) | **CONFIRMED 3/3** (all matches predicted) |
| Q067-F-04 | `2611e9cc5ed1` | mlk-stem (m-l-k) lexical concentration | **NULL** (p=0.58, name-tracks-vocabulary FALSIFIED) |

### 8 classical claims audited (per `05-classical-claims-audit.md`)

| Audit | Verdict |
|:--|:--|
| 1. Q 67 has thirty verses (matching faḍāʾil hadith) | **VINDICATED** at exact-match precision |
| 2. Q 67 = al-Mānīʿa / al-Munjiya (Ibn ʿAbbās narrative chain) | **DA'IF-CHAIN** (Yaḥyā b. ʿAmr al-Nukrī, Tirmidhī's own *gharīb* grade) |
| 3. Q 67 thirty-verses-shafāʿa tradition (general claim) | **VINDICATED at *ḥasan* level** (independent isnads: ʿAbbās al-Jushamī ← Abū Hurayra; al-Zuhrī ← Ḥumayd ← ʿAbd al-Raḥmān b. ʿAwf) |
| 4. Q 67:1 *bi-yadihi al-mulk* corpus-singleton | **VINDICATED** at corpus-singleton level |
| 5. Q 67:3 *fa-rjiʿi al-baṣar* corpus-singleton | **VINDICATED** at corpus-singleton level |
| 6. Q 67:3 *sabʿa samāwātin ṭibāqan* cosmological signature | **VINDICATED** at corpus-pair level (Q67:3 + Q71:15) |
| 7. Q 67 has no specific event-asbāb | **VINDICATED with DATA-GAP** (al-Wāḥidī primary not on disk) |
| 8. Q 67 named *al-Mulk* by opening-word convention | **VINDICATED** (mlk-stem density NULL → falsifies name-tracks-vocabulary at Q67) |

### Tafsir survey: 9 mufassirūn (DATA-GAP noted)

al-Ṭabarī, al-Thaʿlabī, al-Ṭabarsī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Biqāʿī, al-Suyūṭī.

**DATA-GAP**: per-Q67 surah-extract files (`*-Q067.txt`) are NOT in `data/literature/classical-tafsir/raw/` directory. Citations are made via the consolidated `*.openiti.raw.txt` files; a second-pass extract-on-demand is recommended for any hard-empirical claim that depends on exact passage text.

### Hadith corpus: all 9 books

Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī.

**Striking finding**: Q 67-specific *faḍāʾil* hadith are **absent from al-Bukhārī and al-Muslim** (the *ṣaḥīḥayn*) but concentrated in al-Tirmidhī (3 hits), Abū Dāwūd (1), Ibn Mājah (1), Mālik (1), Dārimī (1). The Tirmidhī idInBook 2974 (the famous "thirty-verses-pleads" hadith, cited as #2890 in print conventions) and Mālik *Muwaṭṭaʾ* idInBook 497 (independent isnad via al-Zuhrī) form the two-isnad *ḥasan*-grade core. The Tirmidhī idInBook 2973 (the *al-Mānīʿa / al-Munjiya* narrative) is *gharīb-ḍaʿīf* via Yaḥyā b. ʿAmr al-Nukrī.

**Empirical Q 32 + Q 67 alignment**: the classical Prophetic-nightly-recitation pair-tradition (Tirmidhī idInBook 2975, Dārimī idInBook 2667) corresponds to Q 32 being Q 67's empirical FR-distance rank-2 nearest neighbour (FR=0.7534). This is one of the project's clearest *recitation-tradition / empirical-architecture alignments* — recorded post-hoc descriptively.

### Files produced

- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/00-overview.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/01-empirical-profile.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/02-content-analysis.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/03-tafsir-survey.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/04-hadith-corpus.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/05-classical-claims-audit.md` (NEW; 8 audits)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/06-novel-findings.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/07-cross-references.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/JOURNAL.md` (this file)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/preregs/Q067-F-01-architectural-rank-cross-comparison-prereg.md` (NEW; SHA `591775e3a068...`)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/preregs/Q067-F-02-postkink-distinctness-prereg.md` (NEW; SHA `f9f2d651034d...`)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/preregs/Q067-F-03-corpus-singleton-phrases-prereg.md` (NEW; SHA `6722a3a4f9af...`)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/preregs/Q067-F-04-mulk-stem-density-prereg.md` (NEW; SHA `2611e9cc5ed1...`)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/scripts/Q067_F_01_architectural_rank_cross_comparison.py` (NEW; SHA-verified)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/scripts/Q067_F_02_postkink_distinctness.py` (NEW; SHA-verified)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/scripts/Q067_F_03_corpus_singleton_phrases.py` (NEW; SHA-verified)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/scripts/Q067_F_04_mulk_stem_density.py` (NEW; SHA-verified)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-01.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-02.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-03.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/csv/Q067-F-04.json` (NEW)

### Cross-validation: Q 67:1 across tashkeel variants

Q 67:1 Arabic text verified across all three on-disk variants. All 9-word.

**no-tashkeel** (`quran-text/quran-no-tashkeel.json` Q67 v1):
> تبارك الذي بيده الملك وهو على كل شيء قدير

**min-tashkeel** (`quran-text/quran-min-tashkeel.json` Q67 v1):
> تَبارَكَ الَّذى بِيَدِهِ المُلكُ وَهُوَ عَلىٰ كُلِّ شَىءٍ قَديرٌ

**full-tashkeel** (`quran-text/quran-full-tashkeel.json` Q67 v1):
> تَبَارَكَ ٱلَّذِى بِيَدِهِ ٱلۡمُلۡكُ وَهُوَ عَلَىٰ كُلِّ شَىۡءٍ قَدِيرٌ

Word count (after stripping mushaf marks): **9 words** in all three variants. Letter count varies by 4% between variants due to tashkeel-marker presence; the consonantal-skeleton count is rules-tuple stable.

### Honest pre-commit notes

- All four Q067-F-* novel tests had locked pre-regs WRITTEN BEFORE the run. SHA-checksums computed and embedded in run scripts. SHA verification at runtime in every script. No post-hoc adjustments to direction-of-effect.
- **Q067-F-02 was a pre-commit-direction violation**: pre-registered direction was NULL (Q 67 expected to track law within ±2 SE); empirical residual was +2.7 SE. Reported with full prominence as DIRECTIONAL_ENHANCED with honest interpretation that the most-likely explanation is sampling-noise at the single-surah level (not architectural distinctness).
- **Q067-F-04 is a substantive corpus-wide NULL**: pre-registered direction was POSITIVE (Q 67 expected to over-concentrate mlk-stem); empirical p=0.58. The NULL falsifies the corpus-wide name-tracks-vocabulary generalization, refining it to a rules-tuple-fragile sub-hypothesis.
- The "Light-verse Tahajjud-dhikr" finding cited in cross-corpus literature (Q 24 parallel) is NOT applicable to Q 67 — Q 67's classical-recitation embedding is in the *grave-protection* and *nightly-recitation* traditions, not in Prophetic dhikr-prayer-formula.
- The Q 32 + Q 67 FR-distance alignment finding (FR=0.7534, rank 2) is **post-hoc descriptive** — recorded with the explicit "post-hoc" flag.

### Verdict-of-the-investigation

**Q 67 al-Mulk is the corpus's clearest case of theological-iʿjāz / recitation-tradition prominence WITHOUT structural-architectural distinctness.** UAS rank 102/114 (bottom decile) sits Q 67 in the same architectural cell as Q 112, Q 87, Q 73, Q 83 — yet its classical recitation-tradition prominence (al-Mānīʿa / al-Munjiya / nightly-recitation pair with Q 32) is among the corpus's richest. The Wave-D investigation produced four pre-registered novel findings (Q067-F-01 through F-04) with verdicts: VINDICATED, DIRECTIONAL_ENHANCED (pre-commit violation, honest), CONFIRMED 3/3, and substantive NULL. The eight classical-claims audit catches multiple verdict types: VINDICATED (×6), DA'IF-CHAIN (×1), VINDICATED-with-DATA-GAP (×1). The empirical signature precisely matches the qualitative classical reading: a Meccan-mufaṣṣal-awsāṭ surah whose distinctness lives at the *recitation-tradition* level (high faḍāʾil) and at the *token-level lexical-uniqueness* level (corpus-singleton phrases at Q 67:1, 67:3-4), but NOT at the *fawāṣila / outlier / adjacency-cost* level (UAS rank 102, NULL outlier, mid-pack adjacency, mid-pack sig_A).

**Headline empirical verdict on the recitation-tradition / architectural-rank alignment hypothesis**: ORTHOGONAL — high *faḍāʾil* recitation-tradition status does NOT predict elevated UAS. This vindicates the [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] dual-iʿjāz typology at one of its most dramatic instances.

## 2026-05-09 — Wave-H additions (3 follow-up pre-registered tests)

### Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md`
- `/Users/grey/Downloads/quran/surahs/Q067-al-mulk/` (Wave-D landing, full 8-file template)
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` (TSP adjacency-cost map)

### 3 additional pre-registered tests run

| Pre-reg | SHA-head | Title | Verdict |
|:--|:--|:--|:--|
| Q067-F-05 | `826c4a8e7934` | Q 66 → Q 67 mushaf-seam adjacency cost (juzʾ-29 boundary) | **NULL** (rank 47/113, outside top-decile) |
| Q067-F-06 | `d39272d33613` | tabāraka alladhī opener verse-pair tightness {Q 25:1, Q 64:1, Q 67:1} | **NULL** (p_perm=0.084, near-miss directional) |
| Q067-F-07 | `61ded14703d7` | mulk-stem density rank across 114 corpus | **NULL** (rank 37/114, outside top-5) |

### Data-verification correction

The brief's pre-registration for Q067-F-06 asserts that Q 25:1, Q 64:1, and Q 67:1 *all* open with *tabāraka alladhī*. **This is empirically false** (verified against `quran-text/quran-no-tashkeel.json`):
- Q 25:1 ✓ opens with *tabāraka alladhī*
- Q 64:1 ✗ opens with *yusabbiḥu li-llāhi* (musabbiḥāt-class opener); contains *lahu al-mulk* phrase mid-verse
- Q 67:1 ✓ opens with *tabāraka alladhī*

The 5 corpus-wide *tabāraka alladhī* occurrences are: Q 25:1, Q 25:10, Q 25:61, Q 43:85, Q 67:1 (per Q067-F-03 corpus-singleton audit, vindicated).

The locked triplet is honored per §1.6 pre-registration discipline (interpreted as a "mulk-doxology opener" test rather than a *tabāraka alladhī* opener test); the script's secondary test computes FR over the actual 5 *tabāraka alladhī* verse-occurrences. This correction is documented in `06-novel-findings.md` Q067-F-06 § Data-verification note.

### Headline Wave-H verdict

All three Wave-H tests resolve NULL. The pattern reinforces the Wave-D portrait of Q 67: its empirical-architectural signature does NOT live at standard structural axes (UAS, outlier, adjacency-cost, density, opener-cohesion). It lives at:
- **token-singularity** (Q067-F-03 *bi-yadihi al-mulk*, *fa-rjiʿi al-baṣar* corpus-singletons)
- **recitation-tradition prominence** (`04-hadith-corpus.md`; al-Mānīʿa / nightly-recitation pair with Q 32)
- **al-mulk-doxology motif** (descriptive, not statistically tight at verse-level)

The Wave-H NULLs anchor Q 67 firmly in the **theological-iʿjāz** cell of cross-finding-026 and add a third data point to **cross-finding-025** (marker-thickness rule): the juzʾ-29 boundary, the *tabāraka alladhī* opener formula, and the *mlk*-root-name each fail to drive empirical cohesion when isolated as single thin markers.

### Files added 2026-05-09

- `preregs/Q067-F-05-q66-q67-mushaf-seam-prereg.md` (SHA `826c4a8e7934…`)
- `preregs/Q067-F-06-tabaraka-alladhi-pair-prereg.md` (SHA `d39272d33613…`)
- `preregs/Q067-F-07-mulk-root-density-rank-prereg.md` (SHA `61ded14703d7…`)
- `scripts/Q067_F_05_q66_q67_mushaf_seam.py` (SHA-verified)
- `scripts/Q067_F_06_tabaraka_alladhi_pair.py` (SHA-verified)
- `scripts/Q067_F_07_mulk_root_density_rank.py` (SHA-verified)
- `csv/Q067-F-05.json`
- `csv/Q067-F-06.json`
- `csv/Q067-F-07.json`

### Honest pre-commit notes (Wave-H)

- All three Wave-H pre-regs locked BEFORE running. SHAs embedded in scripts. Runtime SHA verification in every script. No post-hoc adjustments.
- Q067-F-06 contains a pre-reg factual error (Q 64:1 mis-attributed to *tabāraka alladhī* openers). Per §1.6, the locked triplet is honored AS-LOCKED and the verdict is reported on what was actually computed; the factual correction is documented prominently in both the JOURNAL and 06-novel-findings § Data-verification note.
- All three verdicts are NULL. Per §1.3 equal-NULL-prominence, they carry the same publication weight as positive findings.
