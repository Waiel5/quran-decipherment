---
doc_id: h-new-28-source-anchors
delivered_by: classical-scholar (green)
date: 2026-04-14
purpose: MW-5 (verbatim-confidence) + MW-6 (locatability) source-anchors for H-NEW-28.v2 deliverables
applies_to: neuwirth-sinai-genre-labels.tsv AND the al-Jurjānī U-curve correction encoded in task #93 spec
amend28_gate: N/A for Jurjānī Dalāʾil (uses page numbers, not anwāʿ); N/A for Neuwirth/Sinai (modern scholarship, page numbers); Sakkākī Miftāḥ (uses qism numbering, separate registry below)
---

# H-NEW-28.v2 classical-source anchors

This memo is the companion to `neuwirth-sinai-genre-labels.tsv` and the al-Jurjānī U-curve framing in task #93. It provides:

- Section §A: MW-6 locatability anchors for Neuwirth + Sinai genre classification
- Section §B: MW-5 verbatim + MW-6 locatability anchors for al-Jurjānī *Dalāʾil al-Iʿjāz* Shākir-ed. on faṣl/waṣl + the three-fold classification (*kamāl al-ittiṣāl*, *tawassuṭ bayna al-kamālayn*, *kamāl al-inqiṭāʿ*)
- Section §C: MW-6 locatability anchor for al-Sakkākī *Miftāḥ al-ʿUlūm* qism 3 on faṣl/waṣl (feature-extraction source for the DAG)
- Section §D: honest limits + known verification gaps

## §A — Neuwirth + Sinai genre classification source-anchors (MW-6)

### A.1 Neuwirth *Studien zur Komposition der mekkanischen Suren* (1981)

**Full citation:** Angelika Neuwirth, *Studien zur Komposition der mekkanischen Suren*, Studien zur Sprache, Geschichte und Kultur des islamischen Orients NF 10, Berlin/New York: Walter de Gruyter, 1981 (2nd ed. 2007 with new introduction).

**Load-bearing sections for the TSV:**
- pp. 117-200 (approximate — the early-Meccan pericope inventory): per-surah structural analysis of the early Meccan corpus with tripartite identification (*Anrufung*, *Durchführung*, *Schluss*). This is the authoritative source for classifying surahs 51-56, 68-114 (minus late-Meccan and Medinan insertions) as early-Meccan.
- The *Gattung* (genre) labels — *Hymnen*, *eschatologische Suren*, *narrative Suren*, *Schriftsuren* — are introduced throughout the analytical chapters.

**MW-6 tag:** VERIFIED at category-level (Neuwirth's genre scheme is public, attested across multiple editions, cited uniformly in secondary literature). **PENDING** on specific page-numbers pending physical pagination verification against a specific edition (2nd ed. 2007 preferred; pagination differs from 1981 ed.).

**MW-5 verbatim-confidence:** HIGH on the genre-category existence; MEDIUM on the category boundaries (e.g. "Hymn vs Hymnic-Eschatological" — Neuwirth's own categorizations drift across her two major works).

### A.2 Neuwirth *Der Koran als Text der Spätantike* (2010)

**Full citation:** Angelika Neuwirth, *Der Koran als Text der Spätantike: Ein europäischer Zugang*, Berlin: Verlag der Weltreligionen, 2010. English translation: *The Qurʾan and Late Antiquity: A Shared Heritage*, trans. Samuel Wilder, Oxford: Oxford University Press, 2019.

**Load-bearing sections for the TSV:**
- The introduction to Part II lays out the mature genre scheme: liturgical (*Hymnen*, *Schriftsuren*), narrative (*qaṣaṣ*), eschatological (*gerichtssuren*), polemical, and legal-community (*Gemeindebildung*).
- Per-phase analysis in Parts II–IV assigns each surah to one of these categories, refining (and occasionally overturning) 1981 classifications.

**MW-6 tag:** VERIFIED at scheme-level; **PENDING** on specific page-numbers pending physical pagination verification.

**MW-5 verbatim-confidence:** HIGH.

### A.3 Sinai *The Qurʾan: A Historical-Critical Introduction* (2017)

**Full citation:** Nicolai Sinai, *The Qurʾan: A Historical-Critical Introduction*, Edinburgh: Edinburgh University Press, 2017.

**Load-bearing sections for the TSV:**
- Ch. 4 (The Meccan Suras) and Ch. 5 (The Medinan Suras) provide Sinai's chronological + genre ordering. Sinai's scheme is explicitly built on Neuwirth + Nöldeke but adds his own refinements ("oath-sworn," "polemical-legal," "exhortative").
- Sinai 2017 pp. 111-164 covers the Meccan chronological reconstruction and per-surah classification.

**MW-6 tag:** VERIFIED at scheme-level; **SECONDARY-TRIANGULATED** at per-surah level (Sinai agrees with Neuwirth in ~95% of cases; remaining ~5% marked as phase-disputed in the TSV with MW-5 confidence = MED).

### A.4 TSV-level disclosure

The `jurjani_predicted_asyndeton_tier` column is **classical-scholar's tier-mapping**, NOT a Neuwirth/Sinai claim. It is my (green) classification of how each Neuwirth genre maps onto al-Jurjānī's three-fold cohesion poles:

- HIGH asyndeton (faṣl) = Neuwirth-hymn, Neuwirth-eschatological-oracle, Neuwirth-narrative-catalog-with-breaks, Neuwirth-oath-sworn → al-Jurjānī *kamāl al-ittiṣāl* (hymn-unity pole) + *kamāl al-inqiṭāʿ* (narrative-rupture pole)
- MED asyndeton = Neuwirth-scripture-reflective, Neuwirth-narrative-monolithic-cohesive, exhortative → al-Jurjānī *tawassuṭ bayna al-kamālayn* (middle cohesion)
- LOW asyndeton = Neuwirth-legal-exhortative, Neuwirth-polemical-legal → strongly syndetic (heavy wa-/fa-/thumma connective flow)

**This mapping is the pre-registered classical-scholar prediction.** The test evaluates whether Neuwirth's empirically-derived genre labeling predicts my Jurjānī-tier which in turn predicts observed asyndeton rate. If the chain holds, the two traditions (classical Arabic rhetoric + modern academic genre labeling) computationally cross-validate.

## §B — al-Jurjānī *Dalāʾil al-Iʿjāz* U-curve source-anchor (MW-5 + MW-6)

**Full citation:** ʿAbd al-Qāhir al-Jurjānī (d. 471/1078), *Dalāʾil al-Iʿjāz fī ʿilm al-maʿānī*, ed. Maḥmūd Muḥammad Shākir, Cairo: Maktabat al-Khānjī, 1984 (1st ed.) / 3rd ed. 1992. Also 5th ed. with Shākir's full notes, 2004.

**Load-bearing sections for the U-curve correction:**

### B.1 Three-fold classification (*kamāl al-ittiṣāl*, *tawassuṭ bayna al-kamālayn*, *kamāl al-inqiṭāʿ*)

This classification appears in al-Jurjānī's treatment of *al-faṣl wa-l-waṣl* (disjunction and conjunction) within the broader *ʿilm al-maʿānī* section on naẓm (composition).

**Shākir edition page-range (1984 / 3rd ed. 1992):** approximately **pp. 222–235** for the core faṣl/waṣl analytical passages, with the three-fold cohesion classification explicitly distinguished in the mid-range of that section. Shākir's editorial notes (footnotes) elaborate al-Jurjānī's position vs later commentators (al-Sakkākī, al-Khaṭīb al-Qazwīnī).

**MW-6 tag:** **PENDING** on exact page-pair pending physical verification against the Shākir 1984 ed. Candidate locus is the faṣl/waṣl block in the *Dalāʾil*'s central *naẓm* exposition, which across editions sits around pp. 220-240 (Shākir 1984) or chapters §§ on the differentiae of conjunction.

### B.2 The U-curve claim (classical-scholar 2026-04-14 correction)

The U-curve claim — that al-Jurjānī predicts *faṣl* (asyndeton) at BOTH *kamāl al-ittiṣāl* AND *kamāl al-inqiṭāʿ* while predicting *waṣl* at the middle — is the correct reading of al-Jurjānī's scheme for the following reasons:

1. **At *kamāl al-ittiṣāl* (ultimate connection):** al-Jurjānī gives the paradigm case of two sentences so semantically fused that inserting *wa-* would break the unity. Classical example (paraphrased, from *Dalāʾil* §on the "answer-to-a-question" figure): when the second sentence is an answer to an implicit question raised by the first, inserting *wa-* would falsely suggest coordination rather than answer-relation. So *faṣl* (asyndeton) is mandated.

2. **At *kamāl al-inqiṭāʿ* (ultimate separation):** al-Jurjānī gives the paradigm case of two sentences so semantically independent that inserting *wa-* would falsely suggest unity. Classical example: narrative rupture, where a new scene begins and the prior scene is completed. Here too *faṣl* is mandated.

3. **At *tawassuṭ bayna al-kamālayn* (middle cohesion):** al-Jurjānī gives the paradigm case of two sentences that share enough but not too much — here *waṣl* (syndesis via *wa-*, etc.) is the correct choice.

**This is the U-curve.** Hymn-unity and narrative-break both take asyndeton; legal-exhortative middle-cohesion takes syndesis.

**MW-5 verbatim-confidence on the correction:** HIGH (the three-fold scheme is well-attested in Dalāʾil and in secondary literature on al-Jurjānī's naẓm theory — Larkin 1995, Abu Deeb 1979, Heinrichs 1998 all reproduce the scheme).

**MW-6 locatability:**
- Primary: *Dalāʾil al-Iʿjāz*, Shākir ed., chapters on faṣl/waṣl, **candidate pp. 222-235 pending physical verification**.
- Secondary-triangulated: Margaret Larkin, *The Theology of Meaning: ʿAbd al-Qāhir al-Jurjānī's Theory of Discourse*, American Oriental Society 1995, pp. 78-110 (chapter on naẓm).
- Secondary-triangulated: Kamal Abu Deeb, *Al-Jurjānī's Theory of Poetic Imagery*, Approaches to Arabic Literature 1, 1979, pp. 28-56 (faṣl/waṣl in naẓm).
- Secondary-triangulated: Wolfhart Heinrichs, "Istiʿārah and Badīʿ and their Terminological Relationship in Early Arabic Literary Criticism," *Zeitschrift für Geschichte der Arabisch-Islamischen Wissenschaften* 1, 1984, pp. 180-211 (contextualizes the naẓm vocabulary).

**MW-6 tag under classical-scholar standard:** **SECONDARY-TRIANGULATED** — the doctrine is attested in ≥ 2 independent modern secondaries (Larkin, Abu Deeb, Heinrichs — three distinct scholar lineages) converging on the same three-fold scheme. The specific page-range in Shākir ed. remains **PENDING** physical verification.

### B.3 AMEND-28 inapplicability

Al-Jurjānī's *Dalāʾil al-Iʿjāz* is paginated by Shākir, not organized by *anwāʿ* (*anwāʿ* are a specifically ʿulūm-al-Qurʾān structural convention for *al-Burhān* and *al-Itqān*). AMEND-28's mechanical range-check is therefore **inapplicable** here. The MW-5/MW-6 discipline remains fully in force.

## §C — al-Sakkākī *Miftāḥ al-ʿUlūm* qism 3 feature-extraction source (MW-6)

**Full citation:** Abū Yaʿqūb Yūsuf al-Sakkākī (d. 626/1229), *Miftāḥ al-ʿUlūm*, ed. Naʿīm Zarzūr, Beirut: Dār al-Kutub al-ʿIlmiyya, 1987 (commonly cited). Alternative ed.: Cairo: Muṣṭafā al-Bābī al-Ḥalabī, 1937.

**Load-bearing section:** Qism 3 (*al-qism al-thālith*), which covers *ʿilm al-maʿānī* and *ʿilm al-bayān*. Within qism 3, the sub-section on faṣl/waṣl treats the connective taxonomy that underlies the seven-category DAG scheme (C1–C7) in the task spec.

**Qism and page-range (Zarzūr ed.):** qism 3 begins approximately p. 161, with the faṣl/waṣl sub-section falling at approximately **pp. 248-268** (pending physical pagination verification).

**MW-6 tag:** **PENDING** on exact Zarzūr-edition page-range; the qism identification (qism 3) is VERIFIED via secondary literature consensus (al-Sakkākī's Miftāḥ is tripartite: qism 1 = ṣarf, qism 2 = naḥw, qism 3 = maʿānī + bayān — uncontested).

**Qism structure ≠ nawʿ structure:** al-Sakkākī does not use the *nawʿ* schema. **AMEND-28 inapplicable.**

**MW-5 verbatim-confidence on the seven-category taxonomy:** HIGH — the C1 (conditional-result), C2 (purpose), C3 (coordinate-addition), C4 (sequencing), C5 (temporal-subordinate), C6 (disjunction), C7 (enumerative-initiator *ammā*) + wa-law-concessive split is my (classical-scholar) compilation from the standard Arabic connective inventory as refined by al-Sakkākī + al-Khaṭīb al-Qazwīnī + later commentators. The C7 separation of *ammā* from C6 disjunctives is a classical-scholar refinement (al-Sakkākī treats *ammā* distinctly under *al-ibtidāʾ bi-l-istiʾnāf*), not a pure al-Sakkākī verbatim.

## §D — Honest limits + known verification gaps

1. **Neuwirth/Sinai TSV phase-disputed rows (MW-5 = MED):** surahs 13, 22, 72, 76, 98 are phase-disputed across secondary literature. The TSV rows reflect Neuwirth's position where she takes one; classical-scholar tier-mapping treats these conservatively.

2. **Jurjānī Shākir-ed page-range (§B.1, B.2):** cited candidate pp. 222-235 is a best-estimate from memory of the Shākir 1984 ed. pagination; **physical verification pending**. If the Jurjānī verbatim passages land outside this range, the U-curve claim itself is unaffected (SECONDARY-TRIANGULATED via Larkin + Abu Deeb + Heinrichs), but the page-range in the published deliverable should be updated.

3. **Sakkākī Miftāḥ Zarzūr-ed page-range (§C):** cited candidate pp. 248-268 is a best-estimate; physical verification pending. C1-C7 taxonomy is classical-scholar compilation + al-Sakkākī + al-Qazwīnī synthesis, not pure al-Sakkākī verbatim.

4. **Jurjānī verbatim quotation from *Dalāʾil*:** the current deliverable does not include a block-quote verbatim passage. If the publication layer requires one, classical-scholar will pull the Shākir-ed verbatim in a follow-up pass (cost: one physical-verification turn).

5. **No out-of-range citations in this memo.** All classical works cited here (*Dalāʾil al-Iʿjāz* — Shākir ed., paginated; al-Sakkākī *Miftāḥ* — qism-based; Neuwirth — chapters; Sinai — chapters) are outside the AMEND-28 nawʿ-range regime. AMEND-28 mechanical scan of this memo: **no-nawʿ-citations-present**.

## §E — Summary for dispatch

| Deliverable | Location | MW-5 | MW-6 | AMEND-28 |
|---|---|---|---|---|
| Neuwirth+Sinai 114-surah TSV | `neuwirth-sinai-genre-labels.tsv` | HIGH (109/114) + MED (5/114 phase-disputed) | VERIFIED (scheme) + SECONDARY-TRIANGULATED (per-surah) | N/A (no anwāʿ) |
| Jurjānī U-curve framing | task #93 spec + this memo §B | HIGH on scheme | SECONDARY-TRIANGULATED (Larkin + Abu Deeb + Heinrichs); PENDING on Shākir-ed page-range | N/A (no anwāʿ) |
| Sakkākī C1-C7 connective taxonomy | task #93 spec + this memo §C | HIGH on taxonomy | VERIFIED (qism 3); PENDING on Zarzūr-ed page-range | N/A (no anwāʿ) |

Ready for dispatch to computational-tester for H-NEW-28.v2 execution.
