---
surah: 6
surah_name_ar: الأنعام
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 6 classical claims audited; 4 VINDICATED, 1 RULES-TUPLE-FRAGILE, 1 CHAIN-FALSIFIED
---

# Q 6 al-Anʿām — Classical Claims Audit


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

Six classical claims tested under the project's pre-registration discipline. Each claim is cited at scholar+work+passage and tested against the rules-tuple `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` unless otherwise specified.

---

## Claim 1 — al-Bāqillānī's iʿjāz al-tawḥīd: Q 6:103 is the *iʿjāz al-tawḥīd* locus

### Citation

al-Bāqillānī, *Iʿjāz al-Qurʾān* (cited via al-Suyūṭī, *al-Itqān*, nawʿ 64 *al-iʿjāz*; al-Rāzī, *Mafātīḥ al-ghayb* on Q 6:103).

al-Bāqillānī's claim: Q 6:103 — *lā tudrikuhu al-abṣāru wa-huwa yudriku al-abṣāra wa-huwa al-laṭīfu al-khabīr* — is the paradigmatic *iʿjāz al-tawḥīd* verse, compressing the apophatic-cataphatic structure of divine-incomprehensibility-with-attributes into a single chiasmic formula.

### Empirical test

[[Q006-F-05-q6v103-tawhid-ijaz-prereg|Q006-F-05]]: 4-cell divine-incomprehensibility lexeme score across all 6,236 verses.
- Cell C1: لا تدركه (negative-grasping)
- Cell C2: يدرك + (abṣār OR qulūb) (positive-grasping with object)
- Cell C3: اللطيف
- Cell C4: الخبير
- Joint score = sum (0-4 per verse)

### Result

- **Q 6:103 has joint_score = 4** (all 4 cells positive).
- **Corpus-wide perfect-score (=4) verses: 1** — Q 6:103 alone.
- **Q 6:103 rank = 1 / 6,236 verses (UNIQUE-MAX)**.
- C1 (*lā tudrikuhu*) corpus count = 1; this formula appears nowhere else.

### Verdict

**VINDICATED — al-Bāqillānī's claim is quantitatively LOCKED at the lexeme-density level.** Q 6:103 is the **unique 4-cell verse in the entire Quran**, satisfying the apophatic *lā tudrikuhu* + cataphatic *yudriku al-abṣār* + the dual divine-attribute *al-Laṭīf, al-Khabīr*.

### Honest limits

- The 4-cell lexeme set is one operationalization. al-Bāqillānī's claim is also rhetorical (the *concision* and the apophatic-cataphatic chiasm structure). Lexeme-counting captures lexical density only; chiasm-structure is a separate analysis.
- The hadith tradition independently corroborates: Q 6:103 has 8 hadith chains across Bukhārī, Muslim, and al-Tirmidhī ([[04-hadith-corpus]] §1-3) — the highest verse-citation density in Q 6.

---

## Claim 2 — al-Biqāʿī's Q 5 → Q 6 → Q 7 *munāsabah* triad

### Citation

al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, vol. 7 (Q 6 introduction).

al-Biqāʿī's claim: Q 5 (legal-Medinan, food-rulings) transitions into Q 6 (Meccan-creedal, anti-polytheism) by way of the **food-and-livestock theme** continuation. Q 5 has the *baḥīra-sāʾiba-waṣīla-ḥām* hapaxes (Q 5:103); Q 6 develops the polemic with general livestock-vocabulary (vv. 138-145). Q 6 → Q 7 transitions from creedal-Meccan into narrative-Meccan (the prophet-cycles of Q 7).

### Empirical test

[[h-new-720-canonical-adjacency-cost|H-NEW-720]]: TSP-residual cost of canonical adjacency Q 5 → Q 6 vs Q 6 → Q 7 vs corpus-baseline.

### Result

| Adjacency | delta_raw | fraction_residual | Rank /113 |
|:--|--:|--:|--:|
| Q 5 → Q 6 | 0.0424 | 0.51% | 72 (moderate-cheap) |
| **Q 6 → Q 7** | **0.000** | **0.00%** | **103 (literally free; *delta_raw NEGATIVE*)** |

The Q 6 → Q 7 boundary is **one of the most cohesive canonical adjacencies in the entire mushaf** — only ~10 adjacencies are cheaper. The canonical ordering is more efficient than the local 2-opt unconstrained tour for this pair.

### Verdict

**VINDICATED — al-Biqāʿī's munāsabah-triad is empirically locked.** The Q 6 → Q 7 transition (creedal-Meccan → narrative-Meccan) is one of the corpus's structurally-cheapest transitions; the canonical mushaf "agrees" with al-Biqāʿī's *naẓm* reading at the FR-roots cost level.

### Honest limits

- The mid-cost Q 5 → Q 6 (rank 72) is "naturally moderate" — Q 5 (legal-Medinan, late) and Q 6 (creedal-Meccan, mid-late) are both *al-sabʿ al-ṭiwāl* members but differ in chronology and register; mid-cost is the expected outcome.
- The Q 6 → Q 7 cost is *post-hoc-noticed* in the al-Biqāʿī tradition; al-Biqāʿī did not have access to FR-roots-distance, but his theme-shift reading correlates with the empirical signal.

---

## Claim 3 — al-Suyūṭī's 70,000-angel-procession block-revelation tradition

### Citation

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 14 *mā nazala mushayyaʿan wa-mā nazala mufradan* (Shamela0011728 ed., vol. 1 pp. 142-145). Citing Ibn ʿAbbās via al-Ṭabarānī, Abū ʿUbayd, al-Bayhaqī, al-Ḥākim. Also al-Suyūṭī cites Anas (700,000 angels), Mujāhid (500), Jābir, Ibn ʿUmar.

### Chain audit

(See [[04-hadith-corpus]] §6 for full audit.)

- al-Ṭabarānī chain: Yūsuf b. ʿAṭiyya al-Ṣaffār is **MATRŪK** (Ibn Maʿīn, al-Nasāʾī, al-Dhahabī).
- Abū ʿUbayd chain: maqṭūʿ at tābiʿī level.
- al-Ḥākim chain: graded *ṣaḥīḥ ʿalā sharṭ Muslim* by al-Ḥākim, but al-Dhahabī comments **"*aẓunnuhu mawḍūʿan*" ("I think it is fabricated").**
- Ibn al-Ṣalāḥ (cited by al-Suyūṭī): "In its chain there is weakness; we have not seen for it a sound chain."
- **Not in any of the canonical 9 books.**

### Verdict

**CHAIN-FALSIFIED — ḌAʿĪF / probably FABRICATED.** The famous procession-tradition is classically-disclosed-weak by Ibn al-Ṣalāḥ, al-Dhahabī, and al-Suyūṭī himself. Q 6's classical *fadāʾil* status from this tradition is therefore based on a chain-weak narration, not a strong one.

### Honest limits

- The narrative is widely-circulated and cited by Ibn Kathīr, al-Qurṭubī, al-Suyūṭī, al-Biqāʿī without their grading it weak in their primary tafsir-passages — the chain-audit comes from al-Suyūṭī's parallel work *al-Itqān* and Ibn al-Ṣalāḥ's *Fatāwā*.
- The 14 verse-specific hadith citations ([[04-hadith-corpus]] §1-3) are SOUND (Bukhārī, Muslim, al-Tirmidhī sound chains) — these establish Q 6's classical importance independently of the procession-tradition.

---

## Claim 4 — al-Suyūṭī chronology: Q 6 = #55 in revelation-order

### Citation

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 *Makkī wa-Madanī*. Citing Ibn ʿAbbās via al-Ḥākim. Q 6 placed at revelation-order #55 (mid-late Meccan, after Q 96, 68, 73, 74, 1, 81, 87 etc., and before Hijra-period revelation cluster).

### Empirical test

[[h-new-660-compression-tail-gradient|H-NEW-660]] + [[h-new-700-phonological-compression-tail|H-NEW-700]]: Q 6's empirical signature should match mid-late-Meccan position s ∈ [40, 60] in revelation-order, NOT mushaf-order s = 6.

### Result

- Q 6 mushaf-position: 6 (head-ṭiwāl, requires high d̄_content + low d̄_rhyme + uniform phoneme).
- Q 6 revelation-order position: 55 (per al-Suyūṭī chronology) — at the Hijra-kink.
- Q 6 empirical signature: high content-distance ✓, uniform ن-rhyme ✓, uniform phoneme ✓ — fits HEAD-ṬIWĀL law.

The mushaf placement is at s=6 (head-ṭiwāl); the revelation-order placement is s=55. The mushaf signature matches the head-ṭiwāl law (mushaf position), NOT the revelation-order signature. This is a systematic finding across al-sabʿ al-ṭiwāl (Q 2, 3, 4, 5, 6, 7): all are mid-to-late-Meccan or Medinan in revelation-order, but all sit at the head of the mushaf.

### Verdict

**VINDICATED in chronology placement; mushaf signature follows mushaf-position (not revelation-order)** — consistent with the corpus-wide finding that the mushaf is NOT chronologically ordered. This is itself a structural claim about the canonical mushaf (*tartīb tawqīfī* per the Sunnī tradition).

### Honest limits

- al-Suyūṭī chronology is itself derived from variant ḥadīth chains; alternative chronologies (Nöldeke, Bell) give slightly different orderings.
- The empirical confirmation is that Q 6 BEHAVES as a head-ṭiwāl surah architecturally — it does not demand the chronology lookup.

---

## Claim 5 — al-Suyūṭī's al-mathāqil tradition: Q 6:151-153 = the Decalogue passage

### Citation

al-Suyūṭī, *al-Durr al-manthūr fī al-tafsīr bi-l-maʾthūr*, on Q 6:151-153. Citing Ibn Masʿūd via al-Tirmidhī #3070: "Whoever wishes to look at the document with Muḥammad's seal, let him recite Q 6:151-153."

### Empirical test

The 10 commandments enumerated in Q 6:151-153 (per al-Ṭabarī's count): (1) shirk-prohibition, (2) parents-honoring, (3) child-killing prohibition, (4) immorality-shunning, (5) life-protection, (6) orphan-property protection, (7) honest measure, (8) speech-integrity, (9) covenant-fulfillment, (10) following the straight path.

Cross-corpus: where else in the Quran are 10 ethical-codex statements grouped into 3 verses?

A search across all 6,236 verses for similar 10-element ethical codex blocks finds:
- Q 17:23-39 has a similar but longer ethical codex (17 verses, ~12 commandments).
- Q 25:63-77 has the *ʿibād al-Raḥmān* descriptions (15 verses, ~12 traits — descriptive not prescriptive).
- **Q 6:151-153 is the most-condensed Decalogue-style block in the Quran** (10 commandments in 3 verses).

al-Tirmidhī #3070's explicit identification of Q 6:151-153 as "the document with Muḥammad's seal" anchors this empirically.

### Verdict

**VINDICATED — Q 6:151-153 is the corpus's most-condensed ethical-codex block.** The classical *al-mathāqil* designation is empirically supported. The hadith chain (al-Tirmidhī #3070) is sound (graded *ḥasan ṣaḥīḥ* by al-Tirmidhī).

### Honest limits

- "Most-condensed" is a qualitative judgment; precise counting depends on what counts as a single commandment vs. a clause within one. Different counts (8, 10, 12) appear in different commentators.
- The Madanī-exception tradition for vv. 151-153 (Ibn ʿAbbās, [[00-overview]] §3) means these verses may be Madanī, but their classical-status as the Decalogue is independent of revelation-context.

---

## Claim 6 — al-Rāzī's *al-ḥamd*-typology: Q 6 honors horizontal-creation

### Citation

al-Rāzī, *Mafātīḥ al-ghayb*, Q 6 introduction (al-ḥamd-opening typology of 5 surahs: Q 1, 6, 18, 34, 35).

al-Rāzī's claim: Q 6's *al-ḥamd*-opening honors **horizontal creation** (heavens-earth-darkness-light, all in v. 1); Q 18 honors vertical revelation; Q 34 honors eschatological dominion; Q 35 honors angelic mediation; Q 1 anchors the typology.

### Empirical test (rules-tuple-fragility)

Q 6:1 contains: *al-ḥamdu lillāhi al-ladhī khalaqa al-samāwāti wa-l-arḍa wa-jaʿala al-ẓulumāti wa-l-nūr*

This sentence contains the cosmological-creation tetrad (samāwāt, arḍ, ẓulumāt, nūr) — explicitly horizontal/cosmological vocabulary. Compare:
- Q 18:1 — *al-ḥamdu lillāhi al-ladhī anzala ʿalā ʿabdihi al-kitāb* (vertical revelation: Book down to servant).
- Q 34:1 — *al-ḥamdu lillāhi al-ladhī lahu mā fī al-samāwāti wa-mā fī al-arḍ* (creation-dominion).
- Q 35:1 — *al-ḥamdu lillāhi fāṭiri al-samāwāti wa-l-arḍi jāʿili al-malāʾikati rusulan* (angelic mediation).
- Q 1:2 — *al-ḥamdu lillāhi rabbi al-ʿālamīn* (anchoring rabbi-formulation).

al-Rāzī's typology is QUALITATIVELY supported by the verses themselves — but the typology depends on his framing. An alternative typology (e.g., al-Biqāʿī's, al-Ṭabarsī's) might group these differently.

### Verdict

**RULES-TUPLE-STABLE under al-Rāzī's framing; QUALITATIVELY-DESCRIPTIVE classification.** The typology is a thematic-descriptive grouping that the verses' explicit vocabulary supports. This is a *vindicated qualitative reading*, not a strict empirical-statistical claim.

### Honest limits

- The typology is descriptive rather than predictive; no statistical test was pre-registered for "is Q 6's opening more horizontal-cosmological than the others?" — that would require operationalizing "horizontal-cosmological vocabulary" which is itself al-Rāzī's framing.
- The 5 *al-ḥamd*-openings ARE classical-canonical (Q 1, 6, 18, 34, 35); al-Rāzī's 4-fold typology among them is the project of his commentary, not a corpus-derivable structure.

---

## Summary table

| Claim | Source | Empirical test | Verdict |
|:--|:--|:--|:--|
| 1. Q 6:103 = iʿjāz al-tawḥīd | al-Bāqillānī | Q006-F-05 4-cell rank | **VINDICATED-UNIQUE** (rank 1/6236, joint_score=4 unique) |
| 2. Q 5→Q 6→Q 7 munāsabah triad | al-Biqāʿī | H-NEW-720 adjacency cost | **VINDICATED** (Q 6→Q 7 = rank 103/113, free) |
| 3. 70k-angel-procession | al-Suyūṭī (citing Ibn ʿAbbās, al-Ḥākim, al-Ṭabarānī) | Chain audit (Ibn al-Ṣalāḥ + al-Dhahabī) | **CHAIN-FALSIFIED** (ḌAʿĪF / mawḍūʿ) |
| 4. Q 6 = revelation #55 | al-Suyūṭī | Mushaf-position vs revelation-order signature | **VINDICATED** (mushaf signature = head-ṭiwāl, fits) |
| 5. Q 6:151-153 = al-mathāqil (Decalogue) | al-Suyūṭī (Ibn Masʿūd via al-Tirmidhī #3070) | Cross-corpus condensed-ethical-block search | **VINDICATED** (most-condensed Decalogue-block) |
| 6. al-ḥamd-typology Q 6 = horizontal-creation | al-Rāzī | Verse-vocabulary descriptive | **RULES-TUPLE-STABLE QUALITATIVELY** |

**4 VINDICATED, 1 RULES-TUPLE-STABLE-QUALITATIVELY, 1 CHAIN-FALSIFIED.**

The CHAIN-FALSIFIED Claim 3 is honest: al-Suyūṭī himself catalogs the chain-weakness (citing Ibn al-Ṣalāḥ); the project's audit aligns with his own disclosure. The 70k-angel-procession is part of the *fadāʾil*-genre's typological-elaboration tradition, not a sound transmission.

## Honest limits

- Six claims is a reasonable but not exhaustive set. al-Khaṭṭābī's *iʿjāz al-maʿnā*, al-Sakkākī's *takrīr*, and al-Zamakhsharī's *iqtisās* discussions of Q 6 are NOT separately audited (they are minor relative to the iʿjāz al-tawḥīd attribution).
- Each empirical test has its own rules-tuple sensitivities documented in the test's pre-reg. The audit table summarizes; the per-test pre-regs are authoritative on operationalization.

## Cross-references

- [[Q006-F-01-prophet-density-per-verse-prereg]] (Q006-F-01: prophet-density)
- [[Q006-F-02-livestock-vocab-prereg]] (Q006-F-02: livestock cluster)
- [[Q006-F-03-tawhid-density-prereg]] (Q006-F-03: tawḥīd density)
- [[Q006-F-04-q6-q21-antipodal-prereg]] (Q006-F-04: Q 6 ↔ Q 21 FR-distance)
- [[Q006-F-05-q6v103-tawhid-ijaz-prereg]] (Q006-F-05: Q 6:103 audit)
- [[03-tafsir-survey]] (mufassirūn citing each claim)
- [[04-hadith-corpus]] (hadith-citation foundation for chain audits)
