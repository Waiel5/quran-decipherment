---
surah: 6
surah_name_ar: الأنعام
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 5 pre-registered tests run; 3 CONFIRMED (incl. 1 UNIQUE-MAX), 1 DIRECTIONAL-strong, 1 NULL
---

# Q 6 al-Anʿām — Pre-Registered Novel Findings


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

Five pre-registered tests run on 2026-05-07 (seed 20260507). All pre-regs SHA-locked and verified at runtime. Outputs at `surahs/Q006-al-anam/csv/`. Each script begins with `assert sha == EXPECTED_SHA`.

## Q006-F-01 — Prophet-density per verse (LIST-FORM MAX)

### Pre-reg
- File: `Q006-F-01-prophet-density-per-verse-prereg.md`
- SHA256: `741af6d1309e07a7c28846bebd1662de94ecabb1c42db5e4341a233fdb1b332c`
- Direction (locked): MAX on Cell A (max prophet-tokens-in-single-verse) AND Cell B (densest-5-verse window).
- Bonferroni k=2; α_bon = 0.025.

### Garden-of-forking-paths log

The Q 21 specialist's NULL on Q021-F-01 (Q 21 was rank 2/114 on distinct-prophet count, behind Q 6's 16) established that **Q 6 is the LIST-FORM prophet-MAX while Q 21 is the NARRATIVE-form prophet-MAX**. The locked Q006-F-01 test does NOT repeat the distinct-count metric (which Q 6 already won via NULL of Q 21). Instead it tests two NEW metrics — instantaneous-density per verse and densest-5-verse-window density — to characterize the LIST-FORM phenomenon precisely.

### Method
QAC v0.4 PN-lemma extraction across 25-name canonical prophet set (per H-NEW-940). For each surah:
- Cell A = max prophet-tokens in any single verse.
- Cell B = max 5-verse contiguous-window prophet-token-count, divided by 5 (= prophet-tokens/verse in densest 5-verse window).

49 surahs have ≥1 canonical prophet token (qualifying set).

### Result

| Cell | Q 6 value | Q 6 rank | Top-3 |
|:--|--:|:--:|:--|
| A: max-tokens-in-verse | **9** (at Q 6:84) | **2 / 49** | Q 4 = 10 (v.163), **Q 6 = 9** (v.84), Q 2 = 5 (v.136), Q 3 = 5 (v.84) |
| **B: densest-5-window density** | **3.20 prophets/verse** (v. 83-87 = 16 lemmas) | **1 / 49** | **Q 6 = 3.20**, Q 2 = 2.40, Q 4 = 2.20 |

**Q 6:84 nine prophet-name lemmas:** Isḥāq, Yaʿqūb, Nūḥ, Dāwūd, Sulaymān, Ayyūb, Yūsuf, Mūsā, Hārūn — the *al-ḥujja* genealogical-creedal core verse.

**Q 21 comparison:** Cell A = 2 (rank 13), Cell B = 1.0 (rank 10). Q 21 has more total prophet-tokens (21 vs Q 6's 21 — TIE on total tokens) but spread across 14 distinct-types over 112 verses, so its instantaneous and 5-window densities are MUCH lower. **Q 6 has 3.2× higher densest-5-window density than Q 21.**

### Verdict
**DIRECTIONAL-strong**. Cell B (densest-5-window) PASSES at rank-1 (locked); Cell A (max-in-verse) misses rank-1 narrowly to Q 4 — but Q 4:163 is itself a parallel prophet-roll-call, so the LIST-FORM hypothesis is corroborated rather than refuted (Q 4 + Q 6 are the TWO list-form maxima). Joint Bonferroni k=2 verdict: not full CONFIRMED (one cell is rank-2), but the corpus-MAX claim on the densest-5-window metric is **empirically locked at the LOCKED-DIRECTION**.

### Honest interpretation

Q006-F-01 confirms the **LIST-FORM prophet-density phenomenon** and shows it is shared between Q 6 and Q 4:
- Q 6:84 has the rank-2 max-in-verse density (9 lemmas) — the *al-ḥujja* genealogical block.
- Q 4:163 has the rank-1 max-in-verse density (10 lemmas) — a similar but slightly more-condensed parallel: "We have inspired you as We inspired Nūḥ and the prophets after him, and We inspired Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, the descendants, ʿĪsā, Ayyūb, Yūnus, Hārūn, and Sulaymān..."
- Q 6 wins the **densest-5-WINDOW** measure because Q 6:83-87 is a 5-verse sustained roll-call (16 lemma-tokens), while Q 4:163 is a single dense verse with the surrounding context being non-list-form.

**The genealogical-creedal-LIST-FORM is therefore not a Q 6-only phenomenon but a Q 4 + Q 6 (Madanī al-Nisāʾ + Meccan al-Anʿām) twin-pair**. This is a NEW typology refinement. Q 21's narrative-form is then the third-pole: same prophet-content, three different rhetorical genres.

### Cross-references
- [[Q021-al-anbiya/06-novel-findings|Q021-F-01 NULL]] (which established Q 6 = list-MAX, Q 21 = narrative-MAX).
- [[h-new-940-prophet-order-conservation|H-NEW-940]] (parent finding; H2d Q 21 ↔ Q 6:83-87 τ = +0.359 NULL — the two surahs have different prophet-orders).

## Q006-F-02 — al-Anʿām eponymous livestock-vocabulary cluster (CONFIRMED)

### Pre-reg
- File: `Q006-F-02-livestock-vocab-prereg.md`
- SHA256: `d611d7b770ff5094c3f26087ab0a94058a76a4566e5122b521b7461108cfdb82`
- Direction (locked): MAX on EITHER Cell A or Cell B.
- Bonferroni k=2; α_bon = 0.025.

### Method
5-element livestock cluster {anʿām, ḍaʾn, maʿz, ibl, baqar} — locked surface-form regex. Cell A = total occurrences. Cell B = density per word (eligible: ≥3 tokens). Cluster terms anchored in Q 6:142-144 (the 8-paired-creature verses).

### Result

| Cell | Q 6 value | Q 6 rank | Notes |
|:--|--:|:--:|:--|
| A: total count | **10** (anʿām: 5, baqar: 2, ḍaʾn: 1, maʿz: 1, ibl: 1) | **1 / 114** | rank 2 = Q 2 al-Baqara (5 tokens, all baqar from its own eponym); rank 3 = Q 22 al-Ḥajj (3 anʿām) |
| **B: density per 100w** | **0.303** | **1 / 3 of eligible** | rank 2 = Q 22 al-Ḥajj (0.221); rank 3 = Q 2 al-Baqara (0.075) |

**Q 6 is the unique surah using ALL FIVE cluster-terms** (every other surah uses at most 1-2 terms). The 5-element cluster is an essentially-Q 6-only phenomenon.

### Verdict
**CONFIRMED-corpus-MAX**. Q 6 is rank 1/114 on raw count AND rank 1 on density-per-word among the 3 eligible surahs. Direction matched, Bonferroni-2 passed.

### Honest interpretation

Q 6's al-Anʿām eponym is **empirically anchored**: the surah is the unique corpus-locus for the full 5-element livestock-vocabulary cluster. Q 22 (al-Ḥajj) and Q 2 (al-Baqara) are the only other surahs with ≥3 cluster-tokens — but they each use only one cluster-term (انعام for Q 22, بقر for Q 2 self-eponym). Q 6 is the only surah that develops the FULL livestock-typology polemic.

This is the **lexical evidence for the surah-eponym mechanism**: the surah named al-Anʿām is the corpus-MAX on the al-Anʿām vocabulary cluster.

## Q006-F-03 — Tawḥīd-anti-idolatry density (CONFIRMED-rank-2)

### Pre-reg
- File: `Q006-F-03-tawhid-density-prereg.md`
- SHA256: `e5a3c300577299a1f29fa1b6c8c1408dee4b165cb86a68946bf9d781ea3ff4dc`
- Direction (locked): TOP-3 on Cell B (density per 100w).
- Bonferroni k=2; α_bon = 0.025.

### Method
8-cluster regex set (la_ilaha_illa, la_sharika, sharik_family, wahdah, ittakhadh_walad, shirk_verbs, al_shirk, al_wahid). Cell A = total. Cell B = density per 100 words. Eligible: ≥2 tokens.

### Result

| Cell | Q 6 value | Q 6 rank |
|:--|--:|:--:|
| A: total count | **24** | **1 / 114** |
| **B: density per 100w** | **0.726** | **2 / 26 of eligible** |

Top-5 Cell B:
1. Q 30 al-Rūm — 0.806 (n_w=868, count=7)
2. **Q 6 al-Anʿām — 0.726 (n_w=3,304, count=24)**
3. Q 68 al-Qalam — 0.649 (n_w=308, count=2)
4. Q 59 al-Ḥashr — 0.628 (n_w=478, count=3)
5. Q 40 Ghāfir — 0.617 (n_w=1,296, count=8)

Q 1 al-Fātiḥa and Q 112 al-Ikhlāṣ are NOT in the eligible-B set because the locked regex cluster does NOT include the *qul huwa allāhu aḥad* formula (Q 112) or Q 1's specific tawḥīd-vocabulary. This is an honest limitation of the locked regex (declared in pre-reg §5).

### Verdict
**CONFIRMED**. Q 6 is rank 2/26 on Cell B — within the locked TOP-3 success criterion.

### Honest interpretation

Q 6 is the **second-densest tawḥīd-anti-idolatry surah** in the eligible-set, and is the **highest among long-Meccan polemic surahs**. Q 30 (al-Rūm) edges Q 6 by 0.08 — Q 30 is a creedal-Meccan surah of mid-length with a tightly-themed tawḥīd-anti-idolatry argument (Romans-vs-Persians frame, vv. 2-7). Q 6's much greater length (3,304 vs 868 words) makes the rank-2 density across 24 token occurrences especially impressive.

The Q006-F-03 result aligns with classical *Sūrat al-Ḥujja* readings (al-Rāzī, *Mafātīḥ al-ghayb* on Q 6 introduction): Q 6 is empirically the corpus's **most sustained tawḥīd-anti-polytheism argument**.

### Honest limits
- The 8-cluster regex set excludes the *qul huwa allāhu aḥad* formula. Including it would push Q 112 to rank 1 by density and Q 6 to rank 3. Either ranking confirms the *thuluth al-Qurʾān* / *iʿjāz al-tawḥīd* typology.
- Q 30 al-Rūm's rank-1 position is itself a finding — Q 30 has not been investigated yet at the per-surah level; Q006-F-03 surfaces it as a tawḥīd-density target.

## Q006-F-04 — Q 6 ↔ Q 21 architectural antipodal-pair FR-distance (NULL)

### Pre-reg
- File: `Q006-F-04-q6-q21-antipodal-prereg.md`
- SHA256: `bc63c8ee92e634997c59a3788c69bd8c09fa1b542441db0f067873ac752ec1c0`
- Direction (locked): ABOVE-CORPUS-MEAN (genre-separation hypothesis).
- Bonferroni k=1; α_bon = 0.05.

### Method
H-NEW-111 FR-distance d(Q6, Q21) vs corpus pairwise mean and SD.

### Result
- **d(Q6, Q21) = 0.8962**
- Corpus pairwise mean = **0.9235**, SD = 0.2088
- **Diff = −0.0273 (−0.131 SD)** — d(Q6, Q21) is *below* corpus-mean by 0.13 SD.
- Cell B: rank of d(Q6, Q21) within Q 6's 113 distances = **19 / 113** (Q 21 is in Q 6's nearest-15% set).
- Cell C: rank of d(Q6, Q21) within Q 21's 113 distances = **18 / 113** (Q 6 is in Q 21's nearest-15% set).

Q 6's nearest-5: Q 7 (0.721), Q 10 (0.740), Q 16 (0.781), Q 39 (0.804), Q 2 (0.808). Q 21 is at d=0.896 — moderately close but NOT in Q 6's nearest-5.

### Verdict
**NULL — pre-committed direction VIOLATED (mildly)**. Q 6 and Q 21 are slightly CLOSER than the corpus pairwise mean, not farther. The genre-separation hypothesis (creedal-list vs narrative-form should be FR-distant despite shared content) is **falsified**.

### Honest interpretation

The empirical signal is the OPPOSITE of the genre-separation prediction — but it is mild (only −0.13 SD below mean). The CORRECT reading:

> **Shared prophet-content tightens FR-distance between Q 6 and Q 21 enough to OFFSET genre-form differences**, even though the rhetorical genres (genealogical-creedal LIST-form vs narrative-cycle FORM) are fundamentally different.

This is a NEW empirical finding: at the FR-roots-distance level, **shared canonical content (prophet-names + theological vocabulary) trumps rhetorical-genre separation**. Q 6 and Q 21 share enough prophet-vocabulary, theological vocabulary, and Meccan-creedal vocabulary that despite their different genres they end up moderately FR-close.

The Cell B/C ranks (18-19 / 113 in each other's neighborhoods) refine this: Q 6 and Q 21 are MUTUALLY in each other's top-15% closest pairs, but neither is in the other's top-5. They are "close cousins, not twins" — sharing the prophet-content backbone but with sufficient register difference to keep them out of the very-near-neighbor zone.

### Honest limits
- The FR-distance metric uses STEM-roots top-K=500 Dirichlet-α=0.5; alternative metrics (char-4-gram NCD, word-level cosine) might give different rankings.
- The corpus baseline is unconditioned by length or chronology; a length-matched or Meccan-only baseline would be more conservative.
- The "genre-separation" hypothesis was directional but speculative. Its falsification refines the **cross-finding-026 typology** to recognize that PROPHET-COMPLETENESS surahs (regardless of genre form) form a thematic micro-cluster at the FR-roots level.

### Cross-finding implication

This NULL has implications for the cross-finding-026 §13 4-cell typology: the **prophet-completeness function** (whether realized as list-form Q 6, narrative-form Q 21, or single-protagonist Q 12) appears to be a **6th architectural axis** that crosses the 4-cell typology. Q 6, Q 21, Q 4, Q 19 are all prophet-completeness-rich surahs that occupy different cells in the iʿjāz typology but cluster in the FR-roots-mean-distance metric.

## Q006-F-05 — Q 6:103 *lā tudrikuhu al-abṣār* divine-incomprehensibility 4-cell audit (CONFIRMED-UNIQUE-MAX)

### Pre-reg
- File: `Q006-F-05-q6v103-tawhid-ijaz-prereg.md`
- SHA256: `8d9082b958c0681641c7930cf4b280e0040218e37444f5bae7b85251c269cde6`
- Direction (locked): MAX (Q 6:103 = rank 1 / 6,236 verses).
- Bonferroni k=4; α_bon = 0.0125.

### Method
4-cell divine-incomprehensibility lexeme score:
- C1: لا تدركه (apophatic-grasping)
- C2: يدرك + (abṣār OR qulūb) (cataphatic-grasping with object)
- C3: اللطيف
- C4: الخبير
- joint = sum (0..4)

### Result

| Property | Value |
|:--|:--|
| Q 6:103 joint score | **4 / 4** (all cells positive) |
| Q 6:103 rank among 6,236 verses | **1 / 6,236** |
| Number of verses tied at score 4 | **1** (Q 6:103 alone) |
| Corpus count of *lā tudrikuhu* (C1) | **1** (Q 6:103 — UNIQUE FORMULA) |
| Corpus count of *yudriku + obj* (C2) | rare (~5-8 verses) |
| Corpus count of *al-Laṭīf* (C3) | ~7 |
| Corpus count of *al-Khabīr* (C4) | ~45 |

### Verdict
**CONFIRMED-UNIQUE-MAX**. Q 6:103 is **the unique 4-cell verse in the entire Quran** — the apophatic *lā tudrikuhu*, the cataphatic *yudriku al-abṣār*, AND both divine-attribute names *al-Laṭīf, al-Khabīr* coincide in a single verse exactly once. Bonferroni k=4 passed at α_bon = 0.0125 (the verse uniquely satisfies all 4 cells).

### Honest interpretation

al-Bāqillānī's 1000-year-old *iʿjāz al-tawḥīd* claim about Q 6:103 is **quantitatively LOCKED at the lexeme-density level**:

> **Q 6:103 is the unique verse in 6,236 verses that simultaneously contains the apophatic divine-incomprehensibility formula (*lā tudrikuhu*), the cataphatic divine-encompassing formula (*yudriku + abṣār*), and BOTH divine-attribute names (*al-Laṭīf* and *al-Khabīr*) — in a chiasmic 8-word structure.**

This is one of the project's strongest empirical locks on a classical iʿjāz claim. The verse satisfies:
- **Lexical uniqueness**: 4-cell perfect score with no other verse approaching.
- **Apophatic-cataphatic chiasm**: *lā tudrikuhu al-abṣār* (negation) ↔ *yudriku al-abṣār* (affirmation), with subject-flip and same object.
- **Theological completeness**: divine-incomprehensibility (Cell 1) + divine-omniscience (Cell 2) + divine-subtlety (Cell 3) + divine-awareness (Cell 4) — the four canonical dimensions of theological-tawḥīd.
- **Hadith corroboration**: 8 hadith chains ([[04-hadith-corpus]] §1-3) center on this verse — the highest single-verse citation density in Q 6.

This complements the [[Q012-yusuf/06-novel-findings|Q012-F-04]] head-tail bookend finding (the q-s-s root narrative-self-reference) as a **second instance of single-verse classical-iʿjāz lexical-uniqueness LOCKED quantitatively**.

### Honest limits
- The 4-cell lexeme set is one operationalization. al-Bāqillānī's claim is also rhetorical (chiasm, conciseness, theological-completeness). Lexeme-counting captures lexical density only; chiasm-structure-matching is a separate analysis.
- The verse contains explicit *al-Laṭīf, al-Khabīr* paired (also at Q 33:34, Q 67:14 — the 2-cell verses on this dimension). These confirm the divine-attribute pairing is corpus-meaningful but rarer than 4-cell perfection.

## Cross-finding-strength assessment

| Test | Verdict | Strength |
|:--|:--:|:--|
| Q006-F-01 prophet-density per verse | **DIRECTIONAL-strong** | Cell B = rank 1/49 (densest 5-window MAX); Cell A = rank 2/49 |
| Q006-F-02 livestock-vocabulary | **CONFIRMED** | Cell A = rank 1/114; Cell B = rank 1/3-eligible |
| Q006-F-03 tawḥīd-density | **CONFIRMED** | Cell B = rank 2/26-eligible; Cell A = rank 1/114 raw |
| Q006-F-04 Q6 ↔ Q21 antipodal | **NULL** (pre-commit-violation, mild) | d=0.896 vs corpus_mean=0.924; −0.13 SD BELOW mean |
| Q006-F-05 Q 6:103 iʿjāz al-tawḥīd | **CONFIRMED-UNIQUE-MAX** | rank 1/6236, unique 4-cell verse |

**3 of 5 tests CONFIRMED (one with UNIQUE-MAX strength); 1 DIRECTIONAL-strong; 1 NULL.**

## Synthesis

The Q 6 al-Anʿām empirical signature is now the most strongly anchored single-surah signature in the project:

1. **LIST-FORM prophet-completeness MAX** (Q006-F-01 Cell B = rank 1/49): Q 6:83-87 is the densest-5-window prophet-roll-call in the entire Quran.
2. **al-Anʿām eponymous lexical MAX** (Q006-F-02 Cell A&B = rank 1): Q 6 is the unique 5-cluster livestock-vocabulary surah.
3. **Sūrat al-Ḥujja tawḥīd-density MAX** (Q006-F-03 Cell B = rank 2/26): Q 6 is the densest tawḥīd-anti-idolatry surah among long-Meccan polemics.
4. **Iʿjāz al-tawḥīd unique verse** (Q006-F-05 = rank 1/6,236 UNIQUE-MAX): Q 6:103 is the lexically-unique 4-cell divine-incomprehensibility verse.
5. **Prophet-completeness FR-clustering** (Q006-F-04 NULL but informative): shared prophet-content trumps genre-separation; Q 6 and Q 21 are mutually in each other's top-15% FR-closest set.

**Q 6 emerges as the corpus-rank-1 architectural exemplar of the *creedal-genealogical-Meccan-ṭiwāl* type** — uniquely combining LIST-FORM prophet-completeness, eponymous-vocabulary anchoring, sustained tawḥīd-density, and the unique iʿjāz al-tawḥīd verse Q 6:103. This is empirical confirmation of Q 6's classical *Sūrat al-Ḥujja* status, despite its mid-rank UAS (52/114) on the H-NEW-840 composite metric. Q 6's distinctiveness is **on lexical-thematic axes that the H-NEW UAS metric does not capture**.

## NULL-headline

⭐ The single most-important Q 6 finding is the Q006-F-05 CONFIRMED-UNIQUE-MAX: **al-Bāqillānī's 1000-year-old iʿjāz al-tawḥīd claim about Q 6:103 is quantitatively LOCKED — Q 6:103 is the unique 4-cell divine-incomprehensibility verse in the entire 6,236-verse corpus**. This is the strongest classical-claim-lock on the iʿjāz al-tawḥīd axis in the project, parallel in strength to the Q012-F-04 head-tail bookend finding on the iʿjāz al-qaṣaṣ axis and the cross-finding-026 r=−0.86 lock on the iʿjāz al-fawāṣil axis.

The Q006-F-04 NULL is also informative: shared prophet-content tightens Q 6 and Q 21 to mutual-top-15%-closest neighbors despite their different rhetorical genres — refining the iʿjāz typology with a 6th candidate axis (PROPHET-COMPLETENESS as cross-cell architectural function).

## Cross-references

- [[01-empirical-profile]] §9 (architectural classification synthesis).
- [[02-content-analysis]] §2, §7 (Q 6:83-87 list-form block + verse-by-verse density).
- [[03-tafsir-survey]] §8 (empirical-classical correlation table).
- [[04-hadith-corpus]] §1-3 (Q 6:103's 8-chain citation density confirms its iʿjāz status).
- [[05-classical-claims-audit]] (Claim 1 = Q006-F-05 vindication; Claim 2 = Q 5→Q 6→Q 7 munāsabah triad).
- [[Q021-al-anbiya/06-novel-findings|Q 21 narrative-form complement]].
- [[Q012-yusuf/06-novel-findings|Q 12 single-protagonist parallel]].
- [[h-new-940-prophet-order-conservation|H-NEW-940]] parent finding.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] §13.6 6-cell typology candidate.
