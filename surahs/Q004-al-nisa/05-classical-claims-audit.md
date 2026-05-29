---
surah: 4
surah_name_ar: النساء
surah_name_translit: al-Nisāʾ
file_type: classical-claims-audit
date_last_updated: 2026-05-29
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 SPLIT (alif-monorhyme: unique-in-ṭiwāl ✓ / length-extreme ✗), 1 NOT-TESTABLE
---

# Q 4 al-Nisāʾ — Classical Claims Audit

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`; rhyme uses min-tashkeel final-letter. Verse text from `quran-text/quran-no-tashkeel.json`.

## Claim 1 — "al-Nisāʾ is Medinan; 176 verses" (al-Zamakhsharī, al-Qurṭubī)

**Claim:** al-Zamakhsharī, *al-Kashshāf*, surah-header: *"madaniyya, wa-hiya miʾatun wa-sittun wa-sabʿūna āya"*
(Medinan, 176 verses). al-Qurṭubī: "Medinan, the sound view," citing ʿĀʾisha (Bukhārī) that al-Nisāʾ was
revealed in her time with the Prophet (Medina).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 4); cross-check `data/hafs-verse-counts.tsv`
and `data/revelation-order.csv`.

**Result:** 176 verses in the JSON; `hafs-verse-counts.tsv` line 4 = 176; `revelation-order.csv`: Q 4 =
revelation #92, period "Medinan", Nöldeke #100 "Medinan."

**Verdict: VINDICATED.** Q 4 is Medinan and exactly 176 verses (al-Zamakhsharī's count matches the disk
exactly). al-Qurṭubī's refutation of the "every *yā-ayyuhā al-nās* is Meccan" heuristic by the Q 2
counterexample is also correct (Q 2 is Medinan with two such vocatives).

## Claim 2 — al-Bukhārī: Q 4:176 (the kalāla) is the LAST verse of the Qurʾān revealed

**Claim:** al-Bukhārī, *Ṣaḥīḥ*, #6499 (al-Barāʾ): "the last Qurʾānic verse revealed was the final verse of
Sūrat al-Nisāʾ — *yastaftūnaka …* about al-kalāla (Q 4:176)."

**Test:** Cross-check `data/revelation-order.csv` for Q 4's surah-level chronology and the on-disk ḥadīth.

**Result:** ḥadīth VERIFIED on disk (Bukhārī #4174, #4448, #6499; al-Barāʾ). The surah-level revelation order
(`revelation-order.csv`) places Q 4 at #92 and Q 9 at #113 — consistent with the ḥadīth's statement that the
last *complete surah* was Q 9 (Barāʾa) while the last *individual verse* was Q 4:176 (a late insertion into an
earlier-ordered surah).

**Verdict: VINDICATED (riwāya-attested + chronology-consistent).** The last-revealed-verse claim is a
historical-isnād datum, here on-disk attested across three Bukhārī placements and consistent with the
surah-level chronology (Q 9 is the last complete surah; the kalāla verse is a final addition to Q 4). The
verse-level chronology itself is not independently testable from the project's structural instruments, but the
ḥadīth and the surah-order do not conflict.

## Claim 3 — al-Bāqillānī (iʿjāz al-fawāṣil) + close-reading: al-Nisāʾ is the lone alif-rhyme long surah

**Claim (project-internal, motivated by the al-Bāqillānī fawāṣil axis):** the seven long surahs are
overwhelmingly nūn-rhymed; al-Nisāʾ is the conspicuous alif-rhyme exception, holding a near-monorhyme.

**Test (PRE-REGISTERED as Q004-F-06 Arm A + Arm B + Arm C):** (A) among al-sabʿ al-ṭiwāl {2,3,4,5,6,7,9}, is
Q 4 the unique alif-dominant surah? (B) is Q 4 a structural-iʿjāz (fawāṣil-variety) minimum? (C) is Q 4's
rhyme concentration a length-stratified extreme?

**Result:**
- **Arm A VINDICATED:** dominant final-letters of al-ṭiwāl = Q2:ن, Q3:ن, **Q4:ا**, Q5:ن, Q6:ن, Q7:ن, Q9:ن.
  **Q 4 is the ONLY alif-dominant surah** (96.0%); the other six are all nūn. (Robustness: under the alternative
  ṭiwāl roster {2,3,4,5,6,7,8} taking Q 8 al-Anfāl as the seventh, Q 8 is also nūn — Q 4 remains the lone alif.)
- **Arm B VINDICATED:** Q 4 sig_A = **−3.1463, rank 113/114** (second-lowest in the corpus); rhyme_entropy =
  0.1989 nats, z = **−1.0339** (far below average). Q 4 is a fawāṣil-variety MINIMUM.
- **Arm C NULL (honest, pre-committed):** against a length-stratified null (n_verses ≥ 100), Q 4's 96.0% is
  NOT in the top 5% (p_perm = 0.17838); **Q 17 (99.1%), Q 18 (99.1%), Q 23 (96.6%) exceed it.** The Q17/Q18/Q23
  exceedance was named in the pre-reg in advance as the pre-committed honest-limit.

**Verdict: SPLIT.** The close-reading observation is VINDICATED in its precise form: al-Nisāʾ is the UNIQUE
alif-rhyme surah among al-sabʿ al-ṭiwāl (Arm A) and a corpus structural-iʿjāz minimum (Arm B). But the
over-claim that it is the corpus's MOST-concentrated long-surah rhyme is FALSIFIED (Arm C): three longer or
comparable surahs (Q 17, Q 18, Q 23) hold tighter monorhymes. The alif-monorhyme is real and unique-in-context,
but not a length-stratified extreme. Published with equal NULL prominence; full detail in `06-novel-findings.md`.

## Claim 4 — al-Rāzī/al-Biqāʿī: the Q 3 → Q 4 munāsaba (the family of ʿImrān → the law of the family)

**Claim:** al-Rāzī (*Mafātīḥ al-ghayb*) and al-Biqāʿī (*Naẓm al-Durar*): Āl ʿImrān closes on the believing
community and the family of ʿImrān; al-Nisāʾ opens on humankind from one soul and the rights of kinship — a
continuous family/community pair.

**Test:** Does the Q 3 → Q 4 seam (and Q 4 → Q 5) have an empirical smoothness correlate? Read `h-new-720.json`.

**Result:** Q 3 → Q 4 delta_raw = **−0.04662, rank 4/113** (seamless); Q 4 → Q 5 delta_raw = **−0.06571,
rank 2/113** (the 2nd-smoothest seam in the corpus). Q 4 is entered AND exited via seamless seams.

**Verdict: VINDICATED.** al-Rāzī/al-Biqāʿī's qualitative Q 3 → Q 4 munāsaba has a direct quantitative correlate:
the transition is the rank-4 smoothest seam, and Q 4 → Q 5 is the rank-2 smoothest — Q 4 is a doubly-seamless
interior member of the al-ṭiwāl head. The shared Medinan family/legal/social vocabulary makes the run
adjacency-cheap.

## Claim 5 — al-Qurṭubī: v 3 RESTRICTS (does not license) polygamy — the orphan-girl occasion

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām*, on Q 4:3, citing ʿĀʾisha (Muslim): the verse responds to guardians
marrying their orphan wards for their wealth without a fair dowry; it CAPS marriages at four and conditions
them on justice — a restriction, not a licence.

**Test:** This is a fiqh/asbāb-al-nuzūl claim (the legal function and occasion of the verse), not a
structural-numerical claim about the text.

**Verdict: NOT-TESTABLE (empirically) / riwāya-attested.** The occasion (orphan-girl guardianship) is on-disk
attested (Bukhārī #2398, #4368, #4860, #4888, #4894; ʿĀʾisha). The legal reading (restriction vs licence) is a
fiqh question outside the project's empirical-architectural instruments. Documented, not adjudicated.

## Claim 6 — Is al-Nisāʾ a content-cohesion outlier of the long-surah head?

**Claim (project-internal):** as the corpus's densest family-law surah, al-Nisāʾ might be a content-outlier of
its {Q1-7} window.

**Test:** Read Q 4's H-NEW-590 delta_pct and classification.

**Result:** delta_pct(X=4) = **+1.08**, classification **WEAK_OUTLIER**. Removing Q 4 barely changes the
window's dispersion — Q 4 is a near-neutral interior member, neither a cohesion-binder (like Q 3 at −15.28)
nor a strong outlier (like Q 1 at +27.09).

**Verdict: FALSIFIED (the outlier hypothesis).** Despite its distinctive legal content, al-Nisāʾ is NOT a
content-outlier of the long-surah head — it sits comfortably inside the al-ṭiwāl cluster (WEAK_OUTLIER,
delta_pct +1.08). Its distinctiveness is phonological (the alif-monorhyme), not content-dispersive: its
root-distribution is well within the long-Medinan-legal neighbourhood (FR-nearest Q 2, Q 5, Q 3, Q 33, Q 24).

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Medinan; 176 verses | al-Zamakhsharī / al-Qurṭubī | **VINDICATED** |
| 2 | Q 4:176 = last-revealed verse | al-Bukhārī #6499 | **VINDICATED** (riwāya + chronology-consistent) |
| 3 | lone alif-rhyme long surah / monorhyme | al-Bāqillānī axis + close-reading | **SPLIT** (unique-in-ṭiwāl ✓ Arm A; sig_A min ✓ Arm B; length-extreme ✗ Arm C) |
| 4 | Q 3 → Q 4 munāsaba | al-Rāzī / al-Biqāʿī | **VINDICATED** (seams rank 4 & 2 /113) |
| 5 | v 3 restricts polygamy (orphan occasion) | al-Qurṭubī | NOT-TESTABLE / riwāya-attested |
| 6 | content-outlier of long-surah head | project-internal | **FALSIFIED** (WEAK_OUTLIER, +1.08) |

## Honest limits

- Claim 3's SPLIT turns on the length-stratification threshold (n_verses ≥ 100). A different threshold (e.g.
  ≥ 150) would shrink the pool; under ≥ 150 verses only Q 2, Q 6, Q 7, Q 9, Q 26, Q 37 + Q 4 remain, and Q 4
  would rank higher — but the pre-committed threshold is ≥ 100, and the Q17/Q18/Q23 exceedance is reported as
  pre-committed. The over-claim is honestly capped.
- Claim 2's verse-level chronology cannot be independently derived from the project's structural instruments;
  it is reported as ḥadīth-attested and surah-order-consistent, not independently confirmed.
- The alif-rhyme `frac` is computed from the min-tashkeel final-letter; a different rhyme-extraction rule (e.g.
  including the rhyme vowel, or the full *rawī*+*waṣl*) could shift the exact percentage, though the
  alif-dominance is robust.

---

*All testable claims pre-registered before computation (Q004-F-06) or deterministic. 2026-05-29.*
