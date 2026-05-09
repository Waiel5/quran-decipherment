---
surah: 89
test_id: Q089-F-03
title: 4-element wa-coordinated oath-architecture taxonomy — Q 89 vs other oath-cluster members
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q089-F-03-oath-architecture-taxonomy
alpha_bon: 0.025
---

# Q089-F-03 — Pre-registration: 4-element wa-coordinated oath-architecture taxonomy and Q 89's place

## 1. Hypothesis (locked before observation)

Q 89 opens with **four wa-coordinated oath-elements**:
- v.1 *wa-l-fajr* — by the dawn
- v.2 *wa-layālin ʿashr* — by ten nights
- v.3 *wa-l-shafʿ wa-l-witr* — by the even and the odd (compound oath)
- v.4 *wa-l-layl idhā yasr* — by the night when it passes

Then v.5 *hal fī dhālika qasamun li-dhī ḥijr* asks rhetorically whether this oath suffices for one of understanding — a META-OATH closing.

Other oath-cluster surahs (per H-NEW-1070) open with:
- Q 51 al-Dhāriyāt: 4 *wa-l-/fa-l-* oath elements (4-fa pattern: *wa-l-dhāriyāt / fa-l-ḥāmilāt / fa-l-jāriyāt / fa-l-muqassimāt*)
- Q 52 al-Ṭūr: 6 *wa-* oath elements (*wa-l-ṭūr / wa-kitābin masṭūr / fī raqqin manshūr / wa-l-bayti al-maʿmūr / wa-l-saqfi al-marfūʿ / wa-l-baḥri al-masjūr*)
- Q 53 al-Najm: 1 *wa-* oath element (*wa-l-najmi idhā hawā*)
- Q 77 al-Mursalāt: 5 *fa-l-/wa-l-* oath elements (*wa-l-mursalāti ʿurfā / fa-l-ʿāṣifāti ʿaṣfā / wa-l-nāshirāti nashrā / fa-l-fāriqāti farqā / fa-l-mulqiyāti dhikrā*)
- Q 79 al-Nāziʿāt: 5 oath elements
- Q 100 al-ʿĀdiyāt: 5 *wa-/fa-* oath elements
- Q 91 al-Shams: 7 *wa-* oath elements (corpus-MAX per H-NEW-85)
- Q 92 al-Layl: 3 *wa-* oath elements
- Q 93 al-Ḍuḥā: 2 *wa-* oath elements
- Q 95 al-Tīn: 4 *wa-* oath elements
- Q 103 al-ʿAṣr: 1 *wa-* oath element

**H1 (locked direction, primary)**: counting only **wa-coordinated oath elements** at v.1 (excluding *fa-* particles), Q 89 carries exactly **4 wa-coordinated oath-elements** (vv. 1-4). This is a corpus-class-exact diagnostic; the 4-wa pattern places Q 89 alongside Q 95 al-Tīn (also 4-wa) and distinguishes it from the *fa-* dominated Q 51, Q 77, Q 100 patterns.

**H2 (locked direction, secondary)**: Q 89 v.5 contains a META-OATH closing of the form *hal fī dhālika qasamun li-X*. This rhetorical question-form closing is corpus-EXACT to Q 89:5; no other oath-opener surah closes its initial oath-block with this rhetorical-meta-question form.

**H0**: Q 89's oath-architecture is generic among oath-cluster members; no taxonomic distinctiveness.

## 2. Operational definitions

- **Source**: `data/alt-text/quran-uthmani-consonantal.json` (no-tashkeel, hamza-normalized, final-yā-normalized).
- **Oath-element identification (locked rules)**:
  - At v.1 of each oath-cluster surah, parse the verse into wa-/fa-coordinated noun-phrases.
  - Count `wa-` particles (`و` followed by definite article `ال` OR by indefinite noun-with-tanwin) as wa-elements.
  - Count `fa-` particles (`ف` in same positions) as fa-elements.
  - Continue counting through subsequent verses until either: (a) a non-particle-starting verse, OR (b) a `inna`/`hal`/imperative-verb signaling the oath's purpose-clause.
- **Oath-cluster surahs scanned (H-NEW-1070 strict-15)**: {Q 37, 51, 52, 53, 77, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103}.
- **H2 META-OATH closing pattern (locked)**: regex `هل\s+في\s+ذلك\s+قسم` (with hamza-tolerance) or its semantic-equivalent (rhetorical-question-meta-oath-closing).

## 3. Test statistic

- **H1**: integer count `n_wa` of wa-coordinated oath-elements at Q 89 vv.1-4. PASS if = 4.
- **H1 cohort partition**: produce a taxonomy table of all 15 H-NEW-1070 cluster members partitioned by (n_wa, n_fa, total) at v.1 onward.
- **H2**: integer count of corpus-occurrences of the META-OATH closing pattern. PASS if = 1.

## 4. Success / Failure

- **CONFIRMED**: H1 PASS AND H2 PASS.
- **DIRECTIONAL**: only one of H1/H2.
- **NULL**: neither.
- **Pre-commit violation**: count differs from prediction (e.g., Q 89 actually has 3 wa + 1 fa at v.1-4, not 4 pure wa); META-OATH closing form has > 1 corpus occurrence.

## 5. Honest limits known a priori

- al-Suyūṭī *al-Itqān* nawʿ 67 (al-aqsām) classifies oath-openers but does not provide a quantitative architecture-taxonomy by particle-count. al-Bāqillānī *Iʿjāz al-Qurʾān* discusses the rhetorical-coherence of oath-clusters but at the qualitative level.
- The H-NEW-1070 finding established the 15 oath-cluster surahs as FR-cohesive at p=0.0004; this test EXTENDS H-NEW-1070 by adding a particle-architecture taxonomy axis ORTHOGONAL to FR-content cohesion.
- Q037-F-04 found Q 37 is the LEAST-central oath-cluster member by FR distance; this test asks whether the same 2-tier structure (short-tail core vs mid-mushaf periphery) is reflected at the oath-particle-architecture level.
- Confound-acknowledgement: the wa/fa distinction may be a stylistic-rhythmic (*saj'*) consideration rather than a semantic-architectural one. The taxonomic claim is INSTRUMENT-DEFINED, not classical-doctrine-grounded.

## 6. Rules-tuple

`(no-tashkeel, hamza-normalized, final-yā-normalized, orthographic-token, particle-coordination-rule, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (H1, H2). α_bon = 0.025.

## 8. SHA256 lock

Embedded in `scripts/Q089_F_03_oath_architecture.py`; verified at runtime.
