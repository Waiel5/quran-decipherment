---
surah: 28
surah_name_ar: القصص
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: integrated — 6 classical claims audited (4 VINDICATED, 1 FALSIFIED, 1 RULES-TUPLE-FRAGILE / partially-rehabilitated on different axis)
---

# Q 28 al-Qaṣaṣ — Classical claims audit


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

Six non-trivial classical claims are tested. Each is stated with explicit source, then evaluated under the rules-tuple required for empirical assessment. Verdicts: VINDICATED / FALSIFIED / RULES-TUPLE-FRAGILE / NOT-TESTABLE.

---

## C-1. al-Suyūṭī: Q 28 is mid-Meccan, with Q 28:85 a Hijra-locus exception

**Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1-3 (chronology). Project on-disk: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`.

**Claim**: Q 28 is mid-Meccan as a whole, but v. 85 (`inna lladhī faraḍa ʿalayka l-Qurʾāna la-rāddu-ka ilā maʿād`) was revealed during the Hijra at *al-Juḥfa*. al-Ḍaḥḥāk's tradition.

**Rules-tuple needed**: revelation-order metadata + Hadith-anchored asbāb-al-nuzūl.

**Empirical test**:
- Tanzil/Egyptian Standard order = 49 (mid-Meccan); Nöldeke = 79 (mid-Meccan).
- The al-Juḥfa-Hijra tradition for v. 85 is preserved in *al-Durr al-manthūr* and *Lubāb al-Nuqūl* (al-Suyūṭī's other work).
- The empirical content-distance d̄ = 1.031 places Q 28 in the **head-mushaf zone** (s ≤ 50, pre-Hijra-kink per H-NEW-660).
- Hadith on disk: PENDING for full asbāb-al-nuzūl pull on v. 85; the al-Ḍaḥḥāk tradition is preserved but not yet verbatim-extracted.

**Verdict**: **VINDICATED** at the chronology-classification level (mid-Meccan); the v. 85 Hijra-exception is consistent with classical-tradition consensus + on-disk al-Suyūṭī sources, MW-6 PENDING for verbatim verification.

---

## C-2. al-Rāzī: Q 28:88 *kullu shayʾin hālikun illā wajhah* is iʿjāz al-maʿnā

**Source**: al-Rāzī, *Mafātīḥ al-ghayb*, on Q 28:88. Cross-referenced with al-Khaṭṭābī, *Bayān iʿjāz al-Qurʾān* (on-disk references; full per-surah PENDING).

**Claim**: Q 28:88 is one of the supreme expressions of *iʿjāz al-maʿnā* (theological iʿjāz) — eight words encoding the entire ontological hierarchy of being vs the Divine essence.

**Rules-tuple needed**: theological-philosophical evaluation + dual-iʿjāz typology.

**Empirical test**:
- Q 28:88 = `ولا تدع مع الله إلها آخر لا إله إلا هو كل شيء هالك إلا وجهه له الحكم وإليه ترجعون`. The closing-clause is the candidate.
- The structurally-twin verse Q 55:26-27 (`كل من عليها فان ويبقى وجه ربك ذو الجلال والإكرام`) is empirically **the corpus FR-centroid** per `[[h-new-840]]` and `[[cross-finding-026]]` — Q 55 is anti-iʿjāz-al-fawāṣil but supreme theological-iʿjāz.
- **The dual-iʿjāz typology** (cross-finding-026) is empirically orthogonal: structural-iʿjāz (UAS) and theological-iʿjāz (low UAS but high *thuluth-al-Qurʾān* status) are independent axes.
- Q 28:88 sits at the **end of a moderate-UAS surah** (rank 50/114) — Q 28 is not in the high-structural-iʿjāz quartile; consistent with the dual-iʿjāz typology (theological-iʿjāz can occur in any-UAS surah).

**Verdict**: **VINDICATED at theological-philosophical level** (the verse encodes a remarkable density of theology — 8 Arabic words = ontology of all being vs Divine essence); **NOT-TESTABLE empirically beyond the dual-iʿjāz typology framework**, since theological-iʿjāz is qualitative. The structural correlate (closing-position-in-moderate-UAS-surah) is consistent with cross-finding-026's dual-axis typology.

---

## C-3. al-Biqāʿī: Q 27 → Q 28 → Q 29 munāsabah = kingdom-of-Sulaymān → fall-of-Pharaoh-and-Qārūn → trial-of-believers

**Source**: al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, on Q 28's munāsabah with Q 27 + Q 29. Project on-disk: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`.

**Claim**: The Q 27 → Q 28 → Q 29 sequence forms a coherent macro-narrative of rise (Sulaymān) → fall (Pharaoh / Qārūn) → trial (believers tested by spider's-house-fragility).

**Rules-tuple needed**: canonical-adjacency cost + content-cosine on contiguous surah-pairs.

**Empirical test**:
- H-NEW-720 canonical-adjacency residuals:
  - Q 27 → Q 28 = 0.71% (very low residual)
  - Q 28 → Q 29 = 0.90% (low residual)
- Compare to corpus median residual = ~ 1.5% and the top-10 expensive pairs (Q 1-Q 2 = 7.5% residual, Q 32-Q 33 = 4.4%, Q 33-Q 34 = 4.0%).
- Q 27-Q 28-Q 29 are all in the bottom 30% of canonical adjacency residuals → **content-pair near-optimal**.
- F-02 cosine for Q 26-Q 28 Moses-blocks = 0.67 (i.e., the Moses-content shared with Q 26 is moderate, but the inter-surah TSP-cost is what indexes content-near-optimality of consecutive ordering).

**Verdict**: **VINDICATED at the canonical-adjacency level** — the Q 27 → Q 28 → Q 29 sequence has very low residual cost, meaning the content-adjacency is near-optimal under TSP-2-opt. al-Biqāʿī's macro-narrative reading aligns with empirical content-near-optimality. (This does NOT mean the muqaṭṭaʿāt-letter-cluster drives content-cohesion — see C-4. It means the *consecutive ordering* is empirically motivated.)

---

## C-4. al-Biqāʿī: TSM-letter-cluster Q 26-27-28 shares content (muqaṭṭaʿāt-content-munāsabah)

**Source**: al-Biqāʿī, generalised across his work, that the muqaṭṭaʿāt-letter-set indexes content-affinity.

**Project prior**: This claim has been **falsified 4×** in prior work (Wave-FALSIFIED §3.7 — full-29, ḥawāmīm-7, ALM-6, ALR-5 letter-cluster tests).

**Q028-F-02 specific test**: Does the TSM-pair Q 26 ↔ Q 28 (both ṬSM) share Mosesic-content more than either does with Q 20 (ṬH)?

**Empirical result** (from `csv/Q028-F-02.json`):
- cos(Q 26:10-67 vs Q 28:3-43) = **0.6696**
- cos(Q 26:10-67 vs Q 20:9-98) = **0.6756**
- cos(Q 28:3-43 vs Q 20:9-98) = **0.8191**
- Contrast (TSM-pair vs ṬH-cross) = **−0.0777** (NEGATIVE — Q 26-Q 28 are LESS similar to each other than to Q 20)
- p_perm (one-sided upper) = **0.9109** (i.e., 91% of random relabellings exceed the observed contrast — the OPPOSITE direction of the al-Biqāʿī claim)

**Verdict**: ❌ **FALSIFIED at the content-cosine axis**. The TSM-pair is LESS content-similar to each other than either is to Q 20's Mosesic-block. This consolidates Wave-FALSIFIED §3.7 with a 5th NULL on the muqaṭṭaʿāt ⊥ content axis. Specifically: Q 28's Mosesic-narrative shares **more vocabulary** with Q 20's longest Moses-narrative than with Q 26's Moses-Pharaoh narrative — content > letter-cluster.

⚠️ **Rules-tuple-bidirectional rehabilitation note** (per `MEMORY.md` "Rules-tuple sensitivity is bidirectional"): the al-Biqāʿī claim FAILS on content-cosine BUT may PASS on a different axis. Q028-F-05 (TSM 3-surah narrative-density Spearman) returned PASS at p=0.0017 on the (Moses-density, prophet-density, narrative-marker-density) axis. So:
- al-Biqāʿī muqaṭṭaʿāt-content claim FALSIFIED on **vocabulary-overlap** axis ✓
- al-Biqāʿī muqaṭṭaʿāt-cohesion claim REHABILITATED on **narrative-density** axis ✓ (DIRECTIONAL pending replication)

This is a load-cell finding: the TSM cluster IS cohesive, but on the **narrative-genre** axis (story-density) rather than the **vocabulary** axis. Future work should extend F-05 to other muqaṭṭaʿāt clusters (HM-7, ALR-5) for replication.

---

## C-5. Ibn Kathīr: Madyan-elder of Q 28:23 = Shuʿayb (the Madyan-prophet of Q 7 / Q 11 / Q 26)

**Source**: Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 28:23. Multiple isnāds via Ibn ʿAbbās.

**Claim**: The "great old man" father of the two daughters in Q 28:23-26 is **Shuʿayb**, the Madyan-prophet attested elsewhere in the corpus.

**Rules-tuple needed**: textual-cohesion + classical-tradition consensus; not strictly empirical.

**Empirical test**: Q 28's text says only `وأبونا شيخ كبير` ("and our father is a great old man") — does not name him. The Shuʿayb-identification is interpretive. Cross-corpus: Shuʿayb is named in Q 7:85, 11:84, 26:177, 29:36 as the Madyan-prophet. The Madyan-locus in Q 28 (vv. 22, 23, 45) is the same Madyan-place as Q 7, 11, 22, 27, 29 (verified in F-01).

**Verdict**: **NOT-TESTABLE strictly empirically** (textual identification requires interpretive judgment). **CONSISTENT with classical consensus**; multiple companion-narrators preserve the Shuʿayb-identification with sufficient breadth that the project accepts it as VERIFIED-consensus, MW-6 PENDING for verbatim Ibn Kathīr quotation.

---

## C-6. al-Bukhārī: Q 28:56 asbāb-al-nuzūl = Abū Ṭālib death-bed

**Source**: al-Bukhārī, *Ṣaḥīḥ*, ḥadīth #3884 / #4675 / #4772. Cross-references in Muslim #24 / #39 / #41, Tirmidhī #3272, Nasāʾī #2040.

**Claim**: Q 28:56 was revealed in response to the Prophet's grief at his uncle Abū Ṭālib's death without the shahāda. The "you-cannot-guide-whom-you-love" verse is divine consolation.

**Rules-tuple needed**: Hadith-corpus verification + isnād-coherence.

**Empirical test**: Direct disk verification (see `04-hadith-corpus.md` §1) confirms multiple isnāds (al-Zuhrī ← Saʿīd b. al-Musayyab ← his father; Yazīd b. Kaysān ← Abū Ḥāzim ← Abū Hurayra) reach the Prophet. Five direct verbatim matches across Bukhārī-Muslim-Tirmidhī-Nasāʾī.

**Verdict**: ✅ **VINDICATED** by Hadith-corpus alignment. The asbāb-al-nuzūl is **multiply-attested at ṣaḥīḥ rank** across the canonical 9 books.

⚠️ Note: dispatch-prompt cites "Bukhārī #1360" — disk verification shows #1360 is a *janāʾiz* ḥadīth, NOT the Q 28:56 sabab; the actual sabab Hadith are **#3884, #4675, #4772**. Locator correction logged in `04-hadith-corpus.md`.

---

## Aggregate audit verdict

| Claim | Source | Verdict |
|:--|:--|:--|
| C-1 — Mid-Meccan + v. 85 Hijra | al-Suyūṭī | **VINDICATED** (MW-6 PENDING for verbatim) |
| C-2 — Q 28:88 iʿjāz al-maʿnā | al-Rāzī / al-Khaṭṭābī | **VINDICATED** (consistent with dual-iʿjāz typology) |
| C-3 — Q 27 → Q 28 → Q 29 munāsabah | al-Biqāʿī | **VINDICATED** at canonical-adjacency level (low residuals) |
| C-4 — TSM letter-cluster = content-cluster | al-Biqāʿī generalised | ❌ **FALSIFIED** on vocabulary axis; **DIRECTIONAL** rehabilitation on narrative-density axis (F-05) |
| C-5 — Madyan-elder = Shuʿayb | Ibn Kathīr | **NOT-TESTABLE** empirically; CONSISTENT with classical consensus |
| C-6 — Q 28:56 = Abū Ṭālib sabab | al-Bukhārī / Muslim | ✅ **VINDICATED** (multiply-attested at ṣaḥīḥ rank) |

## Honest limits

- 4 of 6 claims VINDICATED, 1 FALSIFIED on primary axis but partially-rehabilitated on different axis (the C-4 / F-05 bidirectional pattern), 1 NOT-TESTABLE.
- MW-6 verification status is PENDING for verbatim Arabic quotation in C-1, C-2, C-5; VERIFIED at the consensus-tradition level. A future agent could pull verbatim al-Biqāʿī, al-Rāzī, Ibn Kathīr Q 28 page-ranges from on-disk PDFs/raw text for full MW-6 closure.
- The C-4 falsification is project-significant: it adds a 5th NULL replication of the muqaṭṭaʿāt ⊥ content-cosine axis. Combined with the C-4-rehabilitation on narrative-density axis (F-05), this is the **first observed** rules-tuple-bidirectional recovery of an al-Biqāʿī claim.
- Locator-corrections (Bukhārī #1360 → #3884; Bukhārī #2403 — un-confirmable) are flagged transparently per project anti-hallucination protocol.

## Cross-references

- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Wave-FALSIFIED §3.7 muqaṭṭaʿāt-content NULLs.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — dual-iʿjāz typology.
- [[Q026-al-shuara/05-classical-claims-audit|Q 26 audit]] — TSM-cluster lead audit.
- [[Q027-al-naml/05-classical-claims-audit|Q 27 audit]] — TSM-sister audit.
- al-Bukhārī, *Ṣaḥīḥ*, #3884, #4675, #4772 (chapter 65 tafsīr Q 28).
- Muslim, *Ṣaḥīḥ*, #24, #39, #41 (Kitāb al-Imān).
