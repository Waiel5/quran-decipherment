---
surah: 32
surah_name_ar: السجدة
file_type: classical-claims-audit
date_last_updated: 2026-05-10
phase: B+
---

# Q 32 al-Sajda — Classical Claims Audit

Rigorous verify/falsify of non-trivial classical claims about Q 32, with rules-tuple, instrument, and verdict.

## Claim 1 — al-Suyūṭī: muqaṭṭaʿāt are Meccan markers; Q 32 is Meccan and ALM-opener (al-Itqān nawʿ 1 + nawʿ 6)

- **Source**: al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (Meccan/Medinan classification) + nawʿ 6 (muqaṭṭaʿāt as Meccan markers).
- **Rules-tuple**: `(orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan)`; chronology source = al-Suyūṭī-aligned Tanzil Egyptian Standard.
- **Operationalization**: Q 32 should be (a) in the Meccan band of `data/revelation-order.csv` and (b) open with a recognized muqaṭṭaʿāt-token.
- **Test**: Direct corpus-enumeration. Q 32 is Meccan (rev order 75/114) per `data/revelation-order.csv`. Q 32:1 is the ALM 3-letter token (verified against QAC `morphology/quranic-corpus-morphology-0.4.txt` location `(32:1:1:1)`).
- **Verdict**: **VINDICATED** at corpus-enumeration level. The al-Suyūṭī classification matches the standard chronology source on disk.
- **Cross-classical**: Nöldeke also places Q 32 in the Late Meccan band (chronological position ~70 per the convention used in the project's revelation-order.csv `noldeke_phase` field).

## Claim 2 — al-Suyūṭī (al-Itqān nawʿ 30): Q 32:15 is canonical sajda-verse #10

- **Source**: al-Suyūṭī, *al-Itqān*, nawʿ 30 (sujūd al-tilāwah catalog).
- **Rules-tuple**: standard Mashriqi sajda-canon.
- **Test**: Q 32:15 should be one of the 14 (or 15 with Shāfiʿī Q 22:77) canonical sajda-verses.
- **Verdict**: **VINDICATED**. Q 32:15 is corpus-attested with the sajda-marker ۩ in `quran-text/quran-no-tashkeel.json[31].verses[14].text`.
- **Refinement (Q032-F-01)**: Q 32:15 is in the BEHAVIORAL sajda-sub-class, not the cosmic-roll-call sub-class. al-Ṭabarī's *under-reminder* clause structurally distinguishes Q 32:15 from cosmic-roll-call sajdas; the classical reading is vindicated at the typological level.

## Claim 3 — al-Bukhārī (#870, #1037): the Prophet recited Q 32 + Q 76 in Friday-Fajr prayer

- **Source**: al-Bukhārī, *Ṣaḥīḥ*, idInBook 870 + 1037 (variant chain).
- **Rules-tuple**: hadith source = `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json`.
- **Test 1 (hadith-on-disk verification)**: Bukhārī #870 should contain the Arabic substrings "الم تنزيل" + "هل أتى" + "الجمعة" + "الفجر".
- **Test 2 (FR-distance)**: FR(Q 32, Q 76) below corpus pairwise mean (cross-finding-028 P2 claim).
- **Verdict (Test 1)**: **VINDICATED**. All four substrings present in #870 and #1037.
- **Verdict (Test 2)**: **VINDICATED at aggregate level** (cross-finding-028 PASS p=0.0009); **PASS-DIRECTED on strict per-pair 1σ threshold** (Q032-F-05 Cell A: FR=0.8395, z=−0.40 — directional but below 1σ strictness). The classical claim is empirically anchored at moderate strength.

## Claim 4 — al-Tirmidhī (#2975): the Prophet recited Q 32 + Q 67 before sleeping (al-Munjiya)

- **Source**: al-Tirmidhī, *Sunan*, idInBook 2975.
- **Test 1 (hadith-on-disk verification)**: Tirmidhī #2975 should contain "الم تنزيل" + "تبارك" + a non-sleep verb.
- **Test 2 (FR-distance)**: FR(Q 32, Q 67) below corpus pairwise mean.
- **Verdict (Test 1)**: **VINDICATED**. All substrings present.
- **Verdict (Test 2)**: **VINDICATED at aggregate level + strong on per-pair (z=−0.81)**. FR(Q 32, Q 67) = 0.7534 is Q 32's FR-#1 neighbor corpus-wide. The al-Munjiya nightly pair is empirically the tightest FR pairing for Q 32.
- **Note on brief's hadith-number error**: The agent brief incorrectly cited "Tirmidhī #2891/#2892" for this pairing. On-disk verification finds those IDs are clothing-hadith. The actual al-Munjiya hadith is **Tirmidhī #2975** (per the project's idInBook convention). This MW-6 control was applied and the on-disk attestation was used.

## Claim 5 — al-Biqāʿī: the Q 32 → Q 33 seam is a deliberate thematic-pivot (*Naẓm al-Durar*)

- **Source**: al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, on Q 32 → Q 33 transition.
- **Rules-tuple**: instrument = h-new-720 TSP-residual-cost on QAC stem-root distributions.
- **Test**: The Q 32 → Q 33 canonical-adjacency cost should be in the top-decile of the 113-adjacency corpus.
- **Result**: δ(Q 32, Q 33) = **0.3631**, rank-3 of 113 corpus adjacencies (4.4% of L_mushaf, behind only Q 1 → Q 2 at 7.4% and one other).
- **Verdict**: **VINDICATED at law-strength**. al-Biqāʿī's *thematic-pivot* reading is empirically among the project's most-vindicated *munāsabāt* observations: the structural break is rank-3 corpus-wide.

## Claim 6 — al-Biqāʿī: the Q 31 → Q 32 seam is thematic-continuity (from the limits of human knowledge to the revealed Book that addresses those limits)

- **Source**: al-Biqāʿī, *Naẓm al-Durar*, on Q 31 → Q 32 transition.
- **Rules-tuple**: same instrument.
- **Test**: The Q 31 → Q 32 canonical-adjacency cost should be moderate (NOT extreme).
- **Result**: δ(Q 31, Q 32) = **0.1005**, mid-pack of corpus adjacencies.
- **Verdict**: **CONSISTENT** — al-Biqāʿī's continuity reading is empirically supported by the moderate (non-extreme) adjacency cost; the seam is structurally "easy" relative to the Q 32 → Q 33 break.

## Claim 7 — al-Rāzī: the *yudabbiru al-amra* construction (Q 32:5) is a cosmic-management cross-reference to Q 10:3 + Q 13:2

- **Source**: al-Rāzī, *Mafātīḥ al-ghayb*, on Q 32:5.
- **Rules-tuple**: lexical search for "يدبر" substring corpus-wide.
- **Test**: Lexical *yudabbir* occurrences should be corpus-rare and concentrated in cosmic-management contexts.
- **Result (preliminary, descriptive)**: The verb *yudabbiru* occurs in Q 10:3, Q 10:31, Q 13:2, Q 32:5 — a corpus-rare verb concentrated in cosmic-management theological contexts.
- **Verdict**: **VINDICATED at descriptive level**. al-Rāzī's cross-referencing of Q 32:5 to Q 10:3 + Q 13:2 is empirically anchored: the *yudabbiru* construction is corpus-rare and concentrated in the cosmic-management theological cluster.

## Claim 8 — Ibn Kathīr: Q 32:16-17 (Tahajjud + qurrati aʿyun) is anchored by al-Tirmidhī #2975 (al-Munjiya pre-sleep)

- **Source**: Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 32:16-17.
- **Test**: The hadith should explicitly mention pre-sleep recitation of Q 32 (Sajda) + Q 67 (Mulk).
- **Result**: Tirmidhī #2975 = "أن النبي صلى الله عليه وسلم كان لا ينام حتى يقرأ {الم * تنزيل} و{تبارك الذي بيده الملك}". Explicit pre-sleep + Q 32 + Q 67.
- **Verdict**: **VINDICATED**. Ibn Kathīr's anchor-citation is on-disk-confirmed.

## Claim 9 — al-Suyūṭī (al-Itqān nawʿ 6): muqaṭṭaʿāt are Meccan markers — Q 13 is the exception (classical recognition of structural anomaly)

- **Source**: al-Suyūṭī, *al-Itqān*, nawʿ 1 + nawʿ 6.
- **Test (Q013-F-06 cross-reference)**: Intersect {29 muqaṭṭaʿāt-openers} ∩ {Medinan in al-Suyūṭī/Tanzil chronology}.
- **Result (per Q013-F-06)**: Intersection = **{Q 2, Q 3, Q 13}** — three Medinan muqaṭṭaʿāt-openers, NOT just Q 13.
- **Verdict on the al-Suyūṭī generalization**: **PARTIALLY VINDICATED** — 26/29 muqaṭṭaʿāt-openers are Meccan; the generalization holds at ~90% but is NOT a corpus-exact rule.
- **Verdict on Q 13's "exception" status**: **PARTIALLY FALSIFIED** at the corpus-enumeration level. Q 2 and Q 3 are ALSO Medinan ALM-openers per the standard chronology. Q 13 is the only MUQAṬṬAʿ-OPENER with ALMR (4-letter), but not the only Medinan one. The brief's claim that Q 13 is "the ONLY surah classified as Medinan that opens with a muqaṭṭaʿ" is FALSIFIED on the on-disk chronology. (See Q013-F-06 finding for full disclosure.)

## Claim 10 — Q032-F-04 a-priori-vindicates Q030-F-08 NULL (ALM-cluster NOT FR-cohesive)

- **Source**: Q030-F-08 PARTIAL (Cell A uniform NULL p=0.418; Cell B length-matched PASS p=0.0225). Cross-finding-025 marker-thickness rule.
- **Test (Q032-F-04 ALM-4 sub-cluster)**: ALM-4 mid-Meccan {Q 29, 30, 31, 32} — chronologically tighter, length-class uniform — should be FR-cohesive if Q030-F-08's PARTIAL was driven by Q 2 + Q 3 length-mismatch.
- **Result (per Q032-F-04)**: ALM-4 T_obs = **0.916**; Cell A p=0.366 (NULL); Cell B p=0.126 (NULL). Both NULL.
- **Verdict**: **REPLICATES** cross-finding-025 marker-thickness rule. Removing Q 2 + Q 3 does NOT tighten the ALM cluster — the ALM-axis alone is not enough for FR-cohesion. This is the 5th empirical replication of the muqaṭṭaʿāt-axis-content-orthogonality finding (after ALR-5, ALM-6, ḤM-7, full-29 all NULL).

## 9. Summary table

| Claim | Source | Verdict |
|:--|:--|:--|
| 1. Q 32 = Meccan ALM-opener | al-Suyūṭī | **VINDICATED** |
| 2. Q 32:15 = canonical sajda #10 | al-Suyūṭī | **VINDICATED**; refined behavioral-sajda (Q032-F-01) |
| 3. Q 32 + Q 76 = Friday-Fajr pair | al-Bukhārī #870/#1037 | **VINDICATED** at aggregate; PASS-DIRECTED at strict 1σ (Q032-F-05A) |
| 4. Q 32 + Q 67 = al-Munjiya pair | al-Tirmidhī #2975 | **VINDICATED** at aggregate; strong directional but not 1σ (Q032-F-05B) |
| 5. Q 32 → Q 33 = thematic-pivot | al-Biqāʿī | **VINDICATED at law-strength** (rank-3 corpus adjacency) |
| 6. Q 31 → Q 32 = thematic-continuity | al-Biqāʿī | **CONSISTENT** (moderate adjacency cost) |
| 7. *yudabbir* cross-reference Q 10:3 + Q 13:2 | al-Rāzī | **VINDICATED descriptively** (lexical concentration) |
| 8. Q 32:16-17 anchored by Tirmidhī #2975 | Ibn Kathīr | **VINDICATED** on-disk |
| 9. al-Suyūṭī muqaṭṭaʿāt-as-Meccan rule | al-Suyūṭī | **PARTIALLY VINDICATED** (26/29); brief's "Q 13 ONLY Medinan" FALSIFIED (intersection = {Q 2, 3, 13}) |
| 10. ALM-cluster FR-cohesion (Q032-F-04) | cross-finding-025 | **REPLICATED-NULL** — marker-thickness rule holds |

## 10. Honest limits

- Verdict "VINDICATED" means the classical claim's empirical predictions match the data within the project's rules-tuple and instruments; it does NOT certify the theological-philosophical correctness of the classical reading.
- Verdict "PASS-DIRECTED" means direction-locked AND p-value below α_bon BUT awaiting independent replication for promotion to CONFIRMED.
- Claim 9's partial falsification depends on the chronology source (Tanzil/al-Suyūṭī puts Q 2, 3, 13 all in Medinan; Nöldeke puts Q 13 in Late Meccan and Q 2, 3 in Medinan, giving an intersection of 2). The "Q 13 ONLY Medinan muqaṭṭaʿāt-opener" claim is incorrect under either source; the brief's framing was therefore in error.
