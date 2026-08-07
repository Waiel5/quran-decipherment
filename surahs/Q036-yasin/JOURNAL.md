---
surah: 36
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-05-09
phase: B+
verdict: EXTENDED (Wave-H 2026-05-09 added F-05 + F-06 + F-07)
---

# Q 36 Yāsīn — Investigation Journal


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

## 2026-04-28 — Wave-D specialist run

### Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- `/Users/grey/Downloads/quran/surahs/Q024-al-nur/00-07*.md` + JOURNAL.md (polished template reference)
- `/Users/grey/Downloads/quran/surahs/Q055-al-rahman/` (refrain-rich Meccan comparator)
- `findings/phase-b-hypotheses/csv/h-new-{111,590,700,720,750,840,860}.json`
- `findings/phase-b-hypotheses/h-new-82-yasin-heart.md` (binding prior — NULL on multi-axis "heart of Quran" claim)
- `findings/phase-b-hypotheses/h-new-127-verse-fisher-rao-fractal.md` (Q 36 PASS at verse-level FR optimality)
- `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` (dual-iʿjāz typology framework)

### H-NEW data integration

Pulled and integrated:
- H-NEW-840 UAS rank **35 / 114** (UAS = 0.5040; abs_outlier = 6.17, max_cost = 0.1993, abs_ijaz = 0.7238).
- H-NEW-590 outlier-strength rank 22 / 114 by abs delta = **−6.17 pp WEAK_ANCHOR (NEGATIVE)**. Q 36 is window-binder (its removal *raises* d̄ of [33-39]), not window-disrupter.
- H-NEW-720 canonical-adjacency-cost: Q 35 → Q 36 rank **13/113** (delta = 0.1993, fraction 2.40%); Q 36 → Q 37 rank 54 (cheap-to-mid). **Asymmetric: expensive-to-enter, cheap-to-leave.**
- H-NEW-750 iʿjāz signature: sig_A = **−0.7238 (rank 80/114)**, sig_B = **−1.0711 (rank 85/114)**; rhyme entropy 0.477 nats (z = −0.531, near-monorhyme); top-final letter ن at 70/83 = **84.34%**.
- H-NEW-111 Fisher-Rao distance: mean to corpus **0.9430 (rank 64/114, mid-pack)**; nearest = Q 25 al-Furqān (0.778), Q 43 al-Zukhruf (0.787), Q 67 al-Mulk (0.794), Q 23 al-Muʾminūn (0.805), Q 15 al-Ḥijr (0.805); farthest = Q 55 al-Raḥmān (1.195).
- H-NEW-860 Q 36 fadāʾil rubric **10/10** (corpus-max tier, tied with Q 1, Q 2, Q 67, Q 112).
- H-NEW-127 verse-level FR optimality **CONFIRMED** at z = −2.82, p = 0.0046 (Bonferroni-5 PASS).
- H-NEW-134 partial MST-centroid rehabilitation — does NOT override H-NEW-82 NULL.
- H-NEW-232 YS-letter-centroid maps to ḤM-cluster centroid (classically-plausible miss).

### Pre-registered novel tests run

| Pre-reg | Test | Pre-reg SHA-head | Verdict |
|:--|:--|:--|:--|
| Q036-F-01 | Recitation-frequency-weighted centrality (7th axis, H-NEW-82-excluded) | 5af602872a5a | **NULL** (rank 46/114; binding H-NEW-82 prior preserved; discriminating control on Q 112 also failed — metric is length-biased) |
| Q036-F-02 | UAS-vs-fadāʾil divergence cell membership | 6d2a50a502bf | **CONFIRMED 3/3** (Q 36 in mild-divergence sub-cell; nearest fadāʾil-10 peer = Q 67 at FR d=0.794) |
| Q036-F-03 | Q 36:82 *kun-fa-yakūn* climax-position uniqueness | 1575bf3f4bd1 | **CONFIRMED 3/3** (Q 36:82 at 98.8%; next-closest Q 40:68 at 80.0%; gap 18.8 pp) |
| Q036-F-04 | Eschatological-formula density audit | 515ce2dea2c6 | **NULL** (Q 36 rank 47/114; density 14.59/1000 above corpus mean 10.93/1000 but not significant; p_perm = 0.27) |

**Tally: 2 CONFIRMED + 2 NULL** — equal-NULL-prominence discipline followed.

### 7 classical claims audited (per `05-classical-claims-audit.md`)

| Audit | Verdict |
|:--|:--|
| 1. al-Tirmidhī *qalb al-Qurʾān* (1a chain + 1b multi-axis) | 1a DIRECTIONAL ḌAʿĪF (chain corpus-internally graded *gharīb* + *shaykh majhūl* + *isnāduhu ḍaʿīf* by al-Tirmidhī himself); 1b FALSIFIED (H-NEW-82 multi-axis NULL) |
| 2. "Recite Yāsīn over the dying" (Abū Dāwūd #3122 / Ibn Mājah #1182) | DIRECTIONAL ḌAʿĪF (chain-grade-disputed; Maʿqil-chain has unnamed-father + Abū-ʿUthmān-not-Nahdī defects) |
| 3. Q 36 = singleton 2-letter muqaṭṭaʿāt | **FALSIFIED** (cardinality 10 with Ḥm-cluster, 3-4 distinct combinations; Q 36 is one of THREE distinct 2-letter openings) |
| 4. Aṣḥāb al-Qarya = Antioch | NOT-EMPIRICALLY-TESTABLE (extra-textual identification) |
| 5. Q 36:82 *kun-fa-yakūn* climax position | VINDICATED at descriptive-position level (98.8% vs next 80.0%; 18.8 pp gap) |
| 6. Q 36 word-count corpus-positional-uniqueness | FALSIFIED (Q 36 at none of the natural midpoints) |
| 7. Q 36:69 anti-poetry assertion | VINDICATED at law-strength via H-NEW-730 / H-NEW-740 / cross-finding-007 (Bonferroni-19 distinction p < 10⁻⁴) |

### Tafsir survey: 9 mufassirūn

al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Zamakhsharī, al-Biqāʿī, al-Suyūṭī (al-Durr), al-Ṭabarsī, al-Thaʿlabī. Verbatim Arabic citations with raw-file offsets to OpenITI extracts. Cross-tafsir consensus table at §8 of `03-tafsir-survey.md`.

Major findings:
- 8 of 9 mufassirūn cite the *qalb al-Qurʾān* tradition; al-Thaʿlabī is the source naming Hārūn Abū Muḥammad as the chain-key (the named weakness).
- al-Ṭabarsī (Imāmī tafsir) confirms cross-sectarian reception of the tradition via independent Imāmī chains (Abū Baṣīr ← Imām Jaʿfar al-Ṣādiq).
- al-Rāzī cites al-Ghazālī's *Iḥyāʾ* grounding for the tradition: Q 36's resurrection-presentation justifies the *qalb*-status (this grounding is what Q036-F-04 tests; NULL).
- Aṣḥāb al-Qarya = Antioch is the dominant identification (8/9 mufassirūn).

### Hadith corpus: all 9 books surveyed

`bukhari.json`, `muslim.json`, `tirmidhi.json`, `abu-dawud.json` (= `abudawud.json`), `nasai.json`, `ibnmajah.json`, `malik.json`, `ahmed.json`, `darimi.json` from the ahmedbaset-json bundle.

**3 substantive Yāsīn-fadāʾil hadiths in our corpus**:
- Tirmidhī global #28750 (idInBook 2970) — *qalb al-Qurʾān* via Anas chain (Hārūn Abū Muḥammad ← Muqātil ← Qatāda ← Anas); **al-Tirmidhī's own grading: *gharīb* + *shaykh majhūl* + *isnāduhu ḍaʿīf*** (corpus-internal grading, no external referee needed).
- Abū Dāwūd global #23626 (idInBook 3122) — "iqraʾū yāsīn ʿalā mawtākum" via Maʿqil b. Yasār chain (Ibn al-Mubārak ← Sulaymān al-Taymī ← Abū ʿUthmān-not-al-Nahdī ← his father ← Maʿqil).
- Ibn Mājah global #31015 (idInBook 1182) — same Maʿqil-chain.

**0 substantive matches in al-Bukhārī, Muslim, al-Nasāʾī, Mālik, al-Dārimī**. Aḥmad's *Musnad* in our partial JSON has 0 matches; the canonical Aḥmad #20302 (Maʿqil-chain) is cited by Ibn Kathīr but not in our partial corpus (DATA-GAP).

H-NEW-860 fadāʾil rubric **10/10** for Q 36 — corpus-max tier driven by *qalb al-Qurʾān* + recite-on-the-dying + Friday-night-recitation traditions.

### Files produced

- `/Users/grey/Downloads/quran/surahs/Q036-yasin/00-overview.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/01-empirical-profile.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/02-content-analysis.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/03-tafsir-survey.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/04-hadith-corpus.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/05-classical-claims-audit.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/06-novel-findings.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/07-cross-references.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/JOURNAL.md` (this file)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/preregs/Q036-F-01-recitation-frequency-weighted-centrality-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/preregs/Q036-F-02-uas-vs-fadail-corpus-divergence-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/preregs/Q036-F-03-kun-fa-yakun-climax-position-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/preregs/Q036-F-04-eschatological-formula-density-prereg.md` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/scripts/Q036_F_01_recitation_frequency_weighted_centrality.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/scripts/Q036_F_02_uas_vs_fadail_corpus_divergence.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/scripts/Q036_F_03_kun_fa_yakun_climax.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/scripts/Q036_F_04_eschatological_formula_density.py` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/csv/Q036-F-01.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/csv/Q036-F-02.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/csv/Q036-F-03.json` (NEW)
- `/Users/grey/Downloads/quran/surahs/Q036-yasin/csv/Q036-F-04.json` (NEW)

### Cross-validation: Q 36:82 across tashkeel variants

Q 36:82 verified across all three on-disk variants. All 14 words, *kun fa-yakūn* (كن فيكون) phrase rules-tuple-stable.

**no-tashkeel** (`quran-text/quran-no-tashkeel.json` Q36 v82): "إنما أمره إذا أراد شيئا أن يقول له كن فيكون"

The 8 corpus *kun fa-yakūn* verse identification is rules-tuple-stable across no-tashkeel, min-tashkeel, and full-tashkeel variants (verified by Q036_F_03 script's cross-validation step).

### Honest pre-commit notes

- All 4 Q036-F-* novel tests had locked pre-regs WRITTEN BEFORE the run. SHA-256 checksums computed at runtime and embedded in JSON outputs. No post-hoc adjustments to direction-of-effect.
- Q036-F-01 NULL: published with full prominence per [[INVESTIGATION-PROTOCOL]] §1.3. The discriminating-control failure (Q 112 ranks 105/114 under length-biased root-Jaccard) is itself an honest finding — the metric is length-biased and does not coherently capture FR-centrality.
- Q036-F-04 NULL: published with full prominence; documents the **pericope-vs-density distinction** (Q 36 has the corpus's signature eschatological pericope at vv. 51-65 but does NOT score on per-1000-words density relative to the short-Meccan eschatological cluster).
- The H-NEW-82 binding-prior NULL on multi-axis "heart of Quran" claim has been respected throughout. Q036-F-01 was the H-NEW-82-excluded 7th-axis salvage attempt; it returned NULL, confirming the binding prior across an additional axis.
- Audit 3 (singleton 2-letter muqaṭṭaʿāt) FALSIFIED the launch-task assertion that "YS = 2-letter muqaṭṭaʿāt singleton". The actual 2-letter muqaṭṭaʿāt set has cardinality 10 (or 3-4 distinct combinations); Q 36 is one of THREE distinct openings, NOT a singleton. Reported with full prominence per the discipline.

### Verdict-of-the-investigation

Q 36 Yāsīn is the **canonical exemplar of meaning-iʿjāz / theological-iʿjāz without high structural-iʿjāz** — the cell's MILD-DIVERGENCE anchor (UAS rank 35) bridging the structural-iʿjāz tier (Q 1, Q 2 at UAS rank 2-3) and the extreme-meaning-iʿjāz tier (Q 67, Q 112 at UAS rank 102-109). Its FR-nearest fadāʾil-10 peer is Q 67 al-Mulk (d = 0.794), confirming the meaning-iʿjāz cluster's FR-cohesion. The classical *qalb al-Qurʾān* claim is **FALSIFIED at multi-axis quantitative form** (H-NEW-82 binding prior + Q036-F-01 7th-axis salvage NULL + Q036-F-04 vocabulary-density NULL) but **VINDICATED at liturgical-theological-classical-tradition reception level** (10/10 fadāʾil rubric; 8/9 mufassirūn cite the tradition; cross-sectarian Imāmī confirmation). The tradition's chain is corpus-internally graded *gharīb* + *shaykh majhūl* + *isnāduhu ḍaʿīf* by al-Tirmidhī himself. **One novel structural fact emerges**: Q 36:82 is the corpus's only *kun fa-yakūn* verse positioned at the rhetorical climax of its surah (98.8% through; next-closest Q 40:68 at 80%; gap 18.8 pp).

### Headline empirical signature (descriptive)

UAS rank **35/114** (mid-pack); outlier-strength **−6.17 pp WEAK_ANCHOR (NEGATIVE)** = window-binder; iʿjāz signature sig_A = **−0.7238 rank 80/114** (anti-fawāṣil); FR mean = **0.9430 rank 64/114** (mid); Q 35→Q 36 cost rank **13/113** (top-15 expensive entry); fadāʾil rubric **10/10** (corpus-max tier); H-NEW-127 verse-level FR-optimal **CONFIRMED**.

### Wave-D residual data-gaps (flagged for future work)

- Aḥmad #20302 Maʿqil-b-Yasār Yāsīn-on-the-dying chain not directly verifiable in our partial Aḥmad JSON (1,374/30,000+ hadith); Ibn Kathīr's "*infarada bihī Aḥmad*" citation is the trace.
- Per-Q-36 OpenITI extracts not pre-extracted into surah-specific files (the Wave-A/B Q 1, Q 2, Q 9, Q 10, Q 17, Q 19 have these; Q 36 does not). Tafsir citations resolved by raw-file character offsets.
- al-Suyūṭī's *al-Itqān* nawʿ-references for Q 36 deferred (the al-Itqān raw extract's smaller index would benefit from per-Q-36 nawʿ identification).
- Length-normalised liturgy-weighted centrality follow-up (Q036-F-01b) post-hoc-flagged but not pre-registered in this run.
- Eschatology-pericope-coherence test (Q036-F-04b candidate) for Block E (vv. 51-65) post-hoc-flagged but not pre-registered.

None of these data-gaps affect the four pre-registered verdicts.

### Cross-finding-026 §13 amendment hook

Q036-F-02's CONFIRMED 3/3 result on the dual-iʿjāz typology refines [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13 with **mild-vs-extreme-divergence sub-cells** within the meaning-iʿjāz cell. This refinement is descriptive-amendment level (does not flip any prior verdict) but adds resolution to the typology. Recommended amendment-hook for cross-finding-026 §13.

### Wave-D launch task verification

Per the Wave-D launch task's "REPORT BACK" specification:
- ✓ Verdict + headline produced
- ✓ Files produced (9 template files + 4 preregs + 4 scripts + 4 JSONs = 21 NEW files)
- ✓ Heart-of-Quran tradition empirical verdict: **chain-grade DIRECTIONAL ḌAʿĪF; multi-axis quantitative form FALSIFIED at 7-axis level (H-NEW-82 6 axes + Q036-F-01 7th axis); liturgical-theological-fadāʾil reception VINDICATED**
- ✓ DATA-GAPs flagged (Aḥmad partial; per-Q-36 tafsir extracts; *al-Itqān* Q-36 nawʿ index)


## 2026-05-09 — Wave-H specialist follow-up

### Scope

Three additional pre-registered tests on Q 36 Yāsīn, following the brief's T1/T2/T3 specification:
- T1 → Q036-F-05: YS muqaṭṭāʿat corpus-EXACT singleton verification.
- T2 → Q036-F-06: "heart of Qurʾān" → empirical FR-centroid audit (Q 112 vs Q 36).
- T3 → Q036-F-07: aṣḥāb al-qarya (Q 36:13-32) lexical cohesion with parallel town-pericopes vs ambient Q 36.

### Pre-reg SHAs (locked-before-run)

| ID | SHA-256 |
|:--|:--|
| Q036-F-05 | `9cc710c5a340e52a98a9030c27edfe92031bad37b43b4a106dfdd33d62d6053f` |
| Q036-F-06 | `69c0782025c1ae13c951fd5ab019f5ce1ca34591042c987c881c39b5c301a4b1` |
| Q036-F-07 | `6f71e1877fff6e799a5a2b2c494452fb117198396468cc3284737fe68802e82d` |

All three SHAs verified at runtime by the scripts' hash-check.

### Garden-of-forking-paths log

- **Q036-F-06 FR-centroid metric choice**: my initial implementation (raw L1-normalised root vectors, no smoothing) gave Q 3 as rank-1 centroid and Q 112 as rank 96. This is the natural-Fisher-Rao result. To match the project's canonical lens (which Q112-F-01 used to lock Q 112's rank-1 status at p < 0.0125), I switched to **the canonical H-NEW-111 D-matrix** (K=500 root-truncation, Dirichlet α=0.5 smoothing). Under that canonical lens: Q 112 rank 1 (mean_FR = 0.7592), Q 36 rank 64. The pre-committed direction is reaffirmed.
  - **The switch is documented honestly**: under the unsmoothed natural lens the centroid is Q 3, not Q 112. The project's canonical "FR-centroid = Q 112" claim is rules-tuple-dependent (specifically dependent on K=500 + α=0.5 smoothing). This is itself worth recording — but it does not retract Q112-F-01's pre-registered verdict, which was locked against the canonical H-NEW-111 metric.
  - The pre-reg uses the canonical H-NEW-111 metric as the binding test; this is the correct lens for re-testing within the project's standing framework.

### Verdicts

| ID | Verdict | Headline |
|:--|:--|:--|
| Q036-F-05 | **PASS-DIRECTED-CORPUS-EXACT** | "يس" is the v1 of exactly one surah (Q 36) across all three orthographic variants |
| Q036-F-06 | **PASS-DIRECTED-REAFFIRMED** | Q 112 rank 1, Q 36 rank 64 on canonical H-NEW-111 FR-centroid metric; 8th-axis NULL on quantitative *qalb al-Qurʾān* |
| Q036-F-07 | **NULL** (Δ=−0.022, p_perm=0.19) | aṣḥāb al-qarya pericope is NOT more aligned with parallel town-pericopes than with ambient Q 36 |

### Files produced

- `preregs/Q036-F-05-ys-singleton-prereg.md`
- `preregs/Q036-F-06-heart-of-quran-empirical-centroid-prereg.md`
- `preregs/Q036-F-07-town-of-prophets-cohesion-prereg.md`
- `scripts/Q036_F_05_ys_singleton.py` (in root `scripts/` dir per repo convention)
- `scripts/Q036_F_06_fr_centroid_audit.py`
- `scripts/Q036_F_07_town_of_prophets_cohesion.py`
- `csv/Q036-F-05.json` / `csv/Q036-F-06.json` / `csv/Q036-F-07.json`
- `Q036-F-05-ys-singleton.md`
- `Q036-F-06-fr-centroid-audit.md`
- `Q036-F-07-town-of-prophets-cohesion.md`
- `06-novel-findings.md` — appended §6 Wave-H addendum + §7 aggregate table

### Heart-of-Qurʾān hadith verification (per brief)

Brief asserted "al-Tirmidhī #2887". On disk in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`:
- The hadith *"إن لكل شيء قلبا وقلب القرآن يس..."* is at **idInBook=2970** (global id=28750).
- al-Tirmidhī himself grades it ***gharīb*** + ***shaykh majhūl*** (Hārūn Abū Muḥammad) in the entry text itself.
- The "#2887" reference reflects al-Tirmidhī's *Kitāb fadāʾil al-Qurʾān* internal numbering; in the ahmedbaset-json bundle the same hadith sits at idInBook=2970. This off-by-N is a known edition-numbering shift documented in `04-hadith-corpus.md` §1.1.
- The hadith is **NOT in al-Bukhārī or Muslim** (verified by 0-match Arabic-substring search in `bukhari.json` and `muslim.json` for the *qalb al-Qurʾān* phrase).

The brief's reminder to be honest about the weak-chain status is fully respected: the hadith is *ḍaʿīf / mawḍūʿ* by al-Albānī, and al-Tirmidhī's own in-text grading is *gharīb* — the popular "heart of Qurʾān" tradition rests on a chain al-Tirmidhī himself flagged as weak.

### What's now decisively NULL on Q 36

The classical *qalb al-Qurʾān* claim, in its quantitative-centrality forms, is now NULL on **8 independent operationalisations**:
1. H-NEW-82 axis 1: positional median (Q 57 wins).
2. H-NEW-82 axis 2: verse-count median.
3. H-NEW-82 axis 3: letter-count median.
4. H-NEW-82 axis 4: lexical centroid (Q 10 wins).
5. H-NEW-82 axis 5: eigenvector centrality.
6. H-NEW-82 axis 6: theme centroid.
7. Q036-F-01 (liturgy-weighted Jaccard).
8. Q036-F-06 (canonical FR-centroid; Q 112 wins).

What survives (with full prominence):
- **Liturgical-theological** content of the *qalb al-Qurʾān* claim — VINDICATED via Q036-F-02's UAS-vs-fadāʾil divergence cell membership.
- **Structural-position** content (the *kun-fa-yakūn* climax at v.82, 98.8%) — VINDICATED via Q036-F-03.
- **Singleton-marker** identity (the YS-only opening) — VINDICATED via Q036-F-05.
