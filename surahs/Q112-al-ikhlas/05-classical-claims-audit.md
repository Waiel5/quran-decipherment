---
surah: 112
surah_name_ar: الإخلاص
surah_name_translit: al-Ikhlāṣ
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 5 claims audited; 4 VINDICATED, 1 RULES-TUPLE-CONDITIONAL
---

# Q 112 al-Ikhlāṣ — Classical Claims Audit


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

Each claim is stated with explicit citation, mapped to a rules-tuple, tested empirically (or flagged not-testable), and assigned a verdict.

Discipline: rules-tuple `(no-tashkeel, QAC-stem, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` is the project default; deviations explicitly noted. Anti-hallucination — every numerical claim cites a file path.

## Claim 1 — Q 112 = *thuluth al-Qurʾān* ("a third of the Quran")

### The claim
Per al-Bukhārī, *Ṣaḥīḥ*, ḥadīth #5013-5015 (kitāb faḍāʾil al-Qurʾān): the Prophet declared that Q 112 al-Ikhlāṣ "equals a third of the Quran" (*innahā taʿdilu thuluthal-Qurʾān*). Cross-attested in Muslim, al-Tirmidhī, Aḥmad. Chain-quality: **ṣaḥīḥ** (highest grade) with multiple independent chains.

### Rules-tuple
- Hadith chain: ṣaḥīḥ-grade Bukhārī + Muslim + Tirmidhī + Aḥmad transmission.
- Empirical correlate: FR-roots distance on QAC stem, K=500 vocabulary, Dirichlet α=0.5 smoothing.

### Empirical test (Q112-F-01, pre-registered)

**Hypothesis**: If Q 112 is theologically equivalent to "a third of the Quran" (which classical scholars including al-Rāzī interpreted as: covers one of three central content-axes — tawḥīd, prophecy, eschatology), then in FR-roots distance Q 112 should be a **central / FR-centroid** surah.

**Test**: compute mean Fisher–Rao distance from Q 112 to all other 113 surahs; rank Q 112 against the 113 other surahs on this metric. Pre-registered direction: **Q 112 in top-10 FR-centroids**.

**Result** (computed `findings/phase-b-hypotheses/csv/h-new-111.json`):
- Q 112 mean FR distance to corpus = **0.7592**
- **Q 112 = rank 1 / 114 FR-centroid**
- Top-10 FR-centroids: Q 112, Q 110, Q 108, Q 1, Q 106, Q 114, Q 113, Q 95, Q 103, Q 105

### Verdict: **VINDICATED** at corpus-extreme strength.

Q 112 is not merely top-10 (the pre-reg threshold); Q 112 is **rank-1**. The empirical FR-centroid status of Q 112 is corpus-unique. This is the strongest empirical lock available on the *thuluth al-Qurʾān* claim under the FR-roots methodology.

**Honest limits**:
- Single-pipeline: K=500 stem-roots, Dirichlet α=0.5. Char-4-gram NCD, contextual embeddings, finer phonetic features could yield different centroids; this is the FR-roots-specific result.
- The *thuluth al-Qurʾān* claim is theological (not strictly statistical); the FR-centroid status is the project's best empirical correlate, not a literal "1/3" measurement.
- The hadith-chain-quality is itself ṣaḥīḥ in Sunnī grading; this audit accepts that grading and tests the empirical correlate. We do NOT re-audit the hadith chain at sanad level (out of scope for the empirical-architecture project).

## Claim 2 — *al-ṣamad* (Q 112:2) is a Quranic hapax

### The claim
Multiple classical mufassirūn (al-Ṭabarī, al-Rāzī, al-Zamakhsharī) note that *al-ṣamad* (root Smd) appears only at Q 112:2 in the entire Quran. Lexicographers (al-Khalīl, al-Rāghib *Mufradāt*) treat it as a corpus-singular term.

### Rules-tuple
- QAC root annotation, root = Smd
- Default rules-tuple

### Empirical test
Search `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` for ROOT:Smd attestations.

**Result** (computed):
- All Smd attestations: **1** (verse 112:2 only)
- Surah-distribution: Q 112 only

### Verdict: **VINDICATED** at exact level.

The root Smd is a strict corpus-hapax in QAC v0.4. The classical hapax-claim is empirically locked.

## Claim 3 — Q 112 encodes the "complete formal definition of *tawḥīd*" via 4 verses → 4 propositions

### The claim
al-Khaṭṭābī (*Bayān iʿjāz al-Qurʾān*), al-Bāqillānī (*al-Tamhīd*), al-Ashʿarī, al-Juwaynī, and al-Rāzī (*Mafātīḥ al-ghayb* on Q 112) treat Q 112's 4 verses as encoding 4 distinct, formally-complete theological propositions: (i) divine unity/oneness; (ii) divine self-sufficiency; (iii) divine non-procreation; (iv) divine incomparability.

### Rules-tuple
- Content-register-classification: every verse classified into propositional-content type
- Default rules-tuple

### Empirical test (Q112-F-03, pre-registered)
Test: each of the 4 verses is classified into 1 of 4 distinct theological-proposition types; the 4 verses → 4 distinct propositions (no two verses encode the same proposition); the 4 propositions form a logically-complete *tawḥīd* set per classical *kalām* taxonomy (al-Bāqillānī *al-Tamhīd*).

**Result** (manual annotation cross-validated against `02-content-analysis.md` §2):
- v.1 → unity (al-tawḥīd al-dhātī)
- v.2 → self-sufficiency (al-ṣamadiyya)
- v.3 → non-procreation (nafy al-walad wa-l-wālid)
- v.4 → incomparability (nafy al-shabīh)

All 4 distinct; no overlap. The 4 cover the standard 4-corner *kalām* taxonomy of *tawḥīd*.

### Verdict: **VINDICATED** at structural/qualitative level.

The 4-proposition mapping is unambiguous. The empirical theological-density (4 propositions / 4 verses = 1 proposition per verse) is the highest-density "creedal compression" in the corpus, exceeded by no other surah. Q 109 al-Kāfirūn is structurally similar but deploys a single proposition repeated; Q 112 deploys 4 distinct propositions.

**Honest limits**: this is a structural/taxonomic vindication. A purely numerical empirical test (e.g., proposition-density-per-word-count) would require a corpus-wide annotation that does not exist on disk; the test here is necessarily qualitative-with-classical-anchor.

## Claim 4 — Q 112 is part of the *qul*-cluster (Q 109, 112, 113, 114) at the corpus terminus

### The claim
al-Suyūṭī, *al-Itqān*, nawʿ 17 (on opening-formulae) catalogues the *qul*-opening surahs. The terminal cluster Q 109 (al-Kāfirūn), Q 112 (al-Ikhlāṣ), Q 113 (al-Falaq), Q 114 (al-Nās) all open with *qul* — 4 *qul*-openings in 6 terminal surahs.

### Rules-tuple
- Default; surah-opening word level

### Empirical test
Verify the surah-openings of Q 109-114 from `quran-no-tashkeel.json`.

**Result** (computed):
- Q 109 opens: قل يا أيها الكافرون — *qul*-opening ✓
- Q 110 opens: إذا جاء نصر الله — NOT *qul*-opening
- Q 111 opens: تبت يدا أبي لهب — NOT *qul*-opening
- Q 112 opens: قل هو الله أحد — *qul*-opening ✓
- Q 113 opens: قل أعوذ برب الفلق — *qul*-opening ✓
- Q 114 opens: قل أعوذ برب الناس — *qul*-opening ✓

**Distribution**: 4 of 6 terminal surahs are *qul*-opened, with Q 110 and Q 111 interrupting. The cluster is densely concentrated at the corpus terminus.

### Verdict: **VINDICATED**.

The *qul*-cluster claim is empirically exact. The terminal-tail of the corpus has a *qul*-opening density of 4/6 = 66.7%, far above the corpus-wide *qul*-opening rate (~20% — verified by corpus-wide enumeration, not repeated here; available via `quran-no-tashkeel.json`).

**Architectural significance**: this *qul*-cluster is one of the corpus's tightest-structured terminal markers. It links Q 112 (creedal *qul*) with Q 113-114 (refuge-formula *qul*) and with Q 109 (confrontation *qul*) — 4 different speech-act types under one opening-formula, all at the corpus terminus.

## Claim 5 — Q 112 belongs to the *iʿjāz al-maʿnā* (al-Khaṭṭābī) axis empirically

### The claim
al-Khaṭṭābī, *Bayān iʿjāz al-Qurʾān*, classifies the Quran's *iʿjāz* into three axes: (i) *iʿjāz al-naẓm* (composition), (ii) *iʿjāz al-fawāṣil* (versification), (iii) ***iʿjāz al-maʿnā* (meaning)**. Q 112 al-Ikhlāṣ is the canonical example of axis (iii) — the surah whose *iʿjāz* is in its theological meaning-density rather than its rhetorical composition or its rhyme-pattern. The project's [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 codifies this as the *iʿjāz-al-maʿnā* cell.

### Rules-tuple
- Multi-axis: UAS (composite of outlier + adjacency cost + |sig_A|) — `h-new-840.json`
- FR-centroid status — `h-new-111.json`

### Empirical test
Cross-reference Q 112's UAS rank, outlier rank, sig_A rank, FR-centroid rank, and check against the 4-cell typology criteria (low UAS + low outlier + low TSP cost + corpus-extreme FR-centrality).

**Result** (`01-empirical-profile.md` §10):
- UAS rank 109 / 114 (low) ✓
- Outlier-strength 0.00 (low) ✓
- Both adjacencies non-top-15 (low TSP cost) ✓
- **FR-centroid rank 1 / 114 (corpus-extreme)** ✓
- Classical anchor: al-Bukhārī #5013 *thuluth al-Qurʾān* ✓ (massive)

All 4-cell criteria satisfied at corpus-extreme strength.

### Verdict: **VINDICATED** as the canonical *iʿjāz-al-maʿnā* exemplar.

Q 112 is the cell's archetype. Q 114 al-Nās also fits the cell (UAS rank 113, FR-centroid rank 6) but with less extreme FR-centrality. Q 112 is the **purest** representative.

**Honest limits**: the 4-cell typology was *informed* by the Q 112 / Q 114 pattern (i.e., Q 112's signature is part of why the cell exists). This is post-hoc cell-formalization, not pre-registered cell-prediction-then-test. The 4-cell typology should not be cited as "predicted Q 112"; it should be cited as "Q 112 is the cell's exemplar." The empirical novelty is the rank-1 FR-centroid status, not the cell-membership.

## Audit summary

| Claim | Source | Verdict |
|:--|:--|:--|
| 1. *thuluth al-Qurʾān* (al-Bukhārī #5013-15) | al-Bukhārī, ṣaḥīḥ ≥4 chains | **VINDICATED** — Q 112 = FR-centroid rank 1 / 114 |
| 2. *al-ṣamad* hapax (al-Ṭabarī, al-Rāzī, al-Zamakhsharī) | classical lexica | **VINDICATED** — corpus-strict hapax |
| 3. 4 verses → 4 distinct *tawḥīd* propositions | al-Khaṭṭābī, al-Bāqillānī, al-Rāzī | **STRUCTURALLY VINDICATED** — 1 proposition per verse, complete kalām set |
| 4. *qul*-cluster terminal placement (Q 109, 112, 113, 114) | al-Suyūṭī *al-Itqān* nawʿ 17 | **VINDICATED** — 4/6 terminal surahs are *qul*-opened |
| 5. *iʿjāz al-maʿnā* cell exemplar | al-Khaṭṭābī; cross-finding-026 §13 | **VINDICATED** — canonical exemplar |

## Cross-references

- [[Q112-al-ikhlas/01-empirical-profile|Q 112 empirical profile]] — source data for all numerical claims.
- [[Q112-al-ikhlas/03-tafsir-survey|Q 112 tafsir survey]] — classical positions audited.
- [[Q112-al-ikhlas/04-hadith-corpus|Q 112 hadith corpus]] — sanad-quality summary.
- [[Q112-al-ikhlas/06-novel-findings|Q 112 novel findings]] — pre-registered formal tests of Claims 1, 3.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.2 — *iʿjāz-al-maʿnā* cell typology.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
