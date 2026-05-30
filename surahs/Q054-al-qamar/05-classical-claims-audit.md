---
surah: 54
surah_name_ar: القمر
surah_name_translit: al-Qamar
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 7 claims audited — 4 VINDICATED, 1 VINDICATED-as-singleton, 1 NOT-TESTABLE, 1 BRIEF-REFUTED (pre-commit violation, full prominence)
---

# Q 54 al-Qamar — Classical Claims Audit

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an honest
verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, verse-as-unit, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`; metrics from
`findings/phase-b-hypotheses/csv/`.

## Claim 1 — "Sūrat al-Qamar is Meccan in its entirety (per the majority)" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 54:1: *"Makkiyya kulluhā fī qawl al-jumhūr"* — with
Muqātil's minority view that vv 44-46 (*am yaqūlūna naḥnu jamīʿun muntaṣir* … *wa-l-sāʿatu adhā wa-amarr*) are
Medinan, *"but it is not sound."*

**Test:** Cross-check `data/revelation-order.csv` (Tanzil Egyptian Standard + Nöldeke).

**Result:** Q 54 (mushaf_order 54) → period **"Meccan"**, revelation_order **#37**, Nöldeke **#49**, phase
**"Middle Meccan"**. No Medinan-classification variant on disk.

**Verdict: VINDICATED.** Q 54 is Meccan in both on-disk chronologies; the Muqātil vv 44-46 minority is correctly
flagged by al-Qurṭubī himself as "not sound" and has no on-disk chronological support.

## Claim 2 — "It is fifty-five verses" (al-Qurṭubī)

**Claim:** al-Qurṭubī: *"wa-hiya khamsun wa-khamsūna āya"* (it is 55 verses).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 54); cross-check `data/hafs-verse-counts.tsv`.

**Result:** 55 verses in the JSON; `hafs-verse-counts.tsv` line 54 = **55**.

**Verdict: VINDICATED.** 55 verses, Hafs-Kūfan (also confirmed: 350 words, 1,477 letters, no-tashkeel, sans
spaces).

## Claim 3 — al-Suyūṭī revelation-order placement of Q 54 (mid-late Meccan, ~#37)

**Claim:** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (chronology), places Q 54 in the mid-late Meccan
phase (00-overview §1 reports "#37 of 114").

**Test:** Read `data/revelation-order.csv` (Tanzil Egyptian-Standard, which encodes the standard chronology
descending from al-Suyūṭī/Nöldeke).

**Result:** Q 54 revelation_order = **#37** (Tanzil Egyptian Standard); Nöldeke = **#49**; phase = "Middle
Meccan." The #37 figure is exactly reproduced.

**Verdict: VINDICATED.** The 00-overview's "#37 of 114" matches the on-disk Egyptian-Standard chronology. (The
Nöldeke order differs at #49 but stays in the Middle-Meccan band — consistent.)

## Claim 4 — The moon-splitting (v 1) is a literal pre-Hijra Meccan event (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, Ibn Kathīr)

**Claim:** the *jumhūr* of mufassirūn read *wa-anshaqqa al-qamar* as a literal, witnessed pre-Hijra event at
Mecca (al-Ṭabarī: *"ʿalā ʿahdi rasūli llāh ﷺ wa-huwa bi-Makka, qabla hijratihi"*; al-Zamakhsharī refutes the
eschatological-future reading via v 2; Ibn Kathīr rejects metaphor-only). Anchored on the Ṣaḥīḥayn chains via
Ibn Masʿūd, Ibn ʿAbbās, Anas, Jubayr b. Muṭʿim.

**Test:** This is an **isnād/historical** claim about the *referent* of v 1, not a structural-numerical claim
about the text. The empirically-checkable component is: are the cited ḥadīth chains actually on disk with the
stated narrators?

**Result:** The moon-splitting chains were verified on disk (`04-hadith-corpus.md` §1): Bukhārī #3481/3706/3708/
4657/4658 (Ibn Masʿūd), #4659/4660 (Ibn ʿAbbās), #4661 (Anas); Muslim #6897-6903 (#6902 = Anas); Tirmidhī
#3369-3373 (#3370 = Anas). The al-Wāḥidī sabab via Masrūq ← Ibn Masʿūd is on disk.

**Verdict: VINDICATED (as an isnād-attested reading), NOT-EMPIRICALLY-ADJUDICABLE (as to event-historicity).**
The literal-Meccan reading is the on-disk consensus and the cited chains exist with the stated narrators (with
the 00-overview's #3706=Anas attribution **corrected** to #3706=Ibn Masʿūd; the Anas chain is #4661). The
historicity of the event itself is outside the project's empirical-architectural instruments — documented, not
adjudicated.

## Claim 5 — The doubled al-Muqtadir closure (vv 42, 55) is a name-of-power closure-frame (al-Qurṭubī)

**Claim:** al-Qurṭubī glosses both Q 54:42 (*ʿAzīz Muqtadir*) and Q 54:55 (*Malīk Muqtadir*) as the
capability-name (*qādir / yaqdiru ʿalā mā yashāʾ*) — implying a deliberate name-of-power closure on both the
destruction-block and the surah.

**Test (PRE-REGISTERED as Q054-F-06):** (i) Is Q 54 the corpus-max for *muqtadir* tokens? (ii) Are both Q 54
instances in surah-closure-frame position? (iii) Does Q 54's count exceed a length-weighted multinomial null?

**Result** (`csv/Q054-F-06.json`, re-run 2026-05-30, SHA verified):
- **(i) H6a PASS** (PASS-DIRECTED ceiling): corpus *muqtadir* tokens = 4 {(18,45),(43,42),(54,42),(54,55)};
  Q 54 holds 2 (share 0.50); Q 54 is the corpus-max. `is_corpus_max = true`.
- **(ii) H6b PASS:** both Q 54 instances are in the committed closure-frame {(54,42) destruction-block seal,
  (54,55) surah-final}.
- **(iii) H6c PASS:** perm_p (length-weighted) = **0.0002** < α_bon 0.025 (uniform secondary = 0.0011).

**Verdict: VINDICATED — corpus-distinctive doubled closure-frame.** al-Qurṭubī's reading of both occurrences as
the capability-name is empirically corroborated as a corpus-distinctive concentration (Q 54 holds 50% of all
corpus *muqtadir* tokens, both in closure position). **Honest limit:** *muqtadir* is rare (N=4), so the
significance is easy to reach; the substantive content is the closure-POSITION (H6b), not the bare count. Full
detail in `06-novel-findings.md` (Q054-F-06, CONFIRMED).

## Claim 6 — Q 54's perfect ر-monorhyme is the high-discipline sajʿ al-muraṣṣaʿ (Ibn Abī al-Iṣbaʿ / balāgha tradition)

**Claim (00-overview §8, attributing the *sajʿ al-muraṣṣaʿ* category to Ibn Abī al-Iṣbaʿ, *Badīʿ al-Qurʾān*):**
Q 54's 55/55 ر-final verses, with the rhyme-vowel rotating -ar/-ir/-ūr within one consonant-class, is the
highest-discipline perfect-monorhyme sajʿ.

**Test (PRE-REGISTERED as Q054-F-04):** Is Q 54's perfect monorhyme corpus-extreme, and is Q 54 unique among
long surahs?

**Result** (`csv/Q054-F-04.json`):
- top_final_letter_frac = **1.0000** (perfect 100% ر); H-NEW-750 rhyme_entropy = **0.0**.
- al-Sakkākī iqāʿ axis rank_B = **114/114 (corpus MINIMUM)**; al-Bāqillānī sig_A rank 105/114.
- Q 54 is the **ONLY perfect-monorhyme surah with ≥ 50 verses** (15 surahs are perfect-monorhyme; all others <50
  verses). `Q54_unique_long_surah_perfect_monorhyme = true`.
- **MW-5 positive control:** under a shuffled-final null on a Q-54-length surah (10,000 perms),
  P(perfect monorhyme) = **0.00000** — corpus-extreme.

**Verdict: VINDICATED — corpus-SINGLETON (perfect monorhyme among long surahs).** The *empirical* claim (perfect
corpus-extreme ر-monorhyme, unique at ≥50 verses) is locked at law-strength. The *attribution* to Ibn Abī
al-Iṣbaʿ's *sajʿ al-muraṣṣaʿ* category is **NOT independently verified on disk** (no Ibn Abī al-Iṣbaʿ text is in
the corpus); the category-label is a balāgha-tradition gloss carried from the 00-overview and is flagged here as
**UNVERIFIED-ATTRIBUTION** — the empirical monorhyme fact stands regardless of the label's provenance.

## Claim 7 — The Q 53 → Q 54 seam is "clamped-zero seamless" (dispatch-brief hypothesis)

**Claim (dispatch-brief, 2026-05-09 origin):** Q 53 and Q 54 are both Meccan and warning-themed, so the
Q 53→Q 54 canonical adjacency should be a clamped-zero seamless seam (a member of the 13-pair set where
delta_raw ≤ 0).

**Test (PRE-REGISTERED as Q054-F-03, locked in the brief's predicted direction):** Read `h-new-720.json`
per_adjacency for the (53,54) pair.

**Result:** Q 53→Q 54 delta_raw = **+0.21006**, fraction_residual 0.0253, **descending-rank 12/113
(TOP-12 most-expensive)**. The seam is NOT clamped-zero; it is one of the corpus's 12 most-expensive joints. The
rhyme-letters differ (Q 53 ى 0.855 vs Q 54 ر 1.0 — H3b PASS); 4 destruction-narratives are shared (H3c PASS,
interpretive).

**Verdict: BRIEF-REFUTED (pre-commit violation), published with full prominence.** The brief's "clamped-zero
seamless" direction is empirically **REVERSED**. The empirically-correct reading is al-Biqāʿī's
**expansion-from-summary**: Q 53:50-54's compressed destruction-tetrad is the seed of Q 54's 5-pericope
expansion — a high-cost content-genre transition, not a smooth continuation. This is the most important NULL of
the Q 54 family (Q054-F-03, `06-novel-findings.md`).

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | All-Meccan (jumhūr) | al-Qurṭubī | **VINDICATED** |
| 2 | 55 verses | al-Qurṭubī | **VINDICATED** |
| 3 | Revelation-order ~#37 | al-Suyūṭī (Egyptian-Std) | **VINDICATED** |
| 4 | Literal Meccan moon-splitting | al-Ṭabarī / al-Zamakhsharī / al-Rāzī / Ibn Kathīr | **VINDICATED** (isnād-attested) / NOT-adjudicable (historicity) |
| 5 | Doubled al-Muqtadir power-closure | al-Qurṭubī | **VINDICATED** (Q054-F-06, corpus-distinctive) |
| 6 | Perfect ر-monorhyme = sajʿ al-muraṣṣaʿ | balāgha tradition | **VINDICATED** (corpus-singleton); attribution UNVERIFIED |
| 7 | Q 53→Q 54 clamped-zero seamless | dispatch-brief | **BRIEF-REFUTED** (pre-commit violation, full prominence) |

## Honest limits

- Claim 4's historicity is outside empirical scope; only the isnād-existence is checked. The 00-overview's
  Bukhārī #3706=Anas attribution is **corrected** to Ibn Masʿūd (`04-hadith-corpus.md` ⚠ Correction 1).
- Claim 6's *sajʿ al-muraṣṣaʿ* / Ibn Abī al-Iṣbaʿ attribution is not verifiable on disk; the empirical
  perfect-monorhyme corpus-singleton is independent of the label.
- Claim 5's significance (perm_p 0.0002) is easy to reach given N=4 *muqtadir* tokens; H6b (closure-position) is
  the substantive discriminator, not the count.
- All testable claims were pre-registered before computation (Q054-F-03, F-04, F-06) or are deterministic
  cross-checks against on-disk reference tables.

---

*All testable claims pre-registered before computation or deterministic. 2026-05-30.*
