---
surah: 102
surah_name_ar: التكاثر
surah_name_translit: al-Takāthur
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 VINDICATED-w/-variant, 1 NOT-TESTABLE
---

# Q 102 al-Takāthur — Classical Claims Audit

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`; for the *kallā* part-of-speech work, add `(QAC v0.4, POS:AVR, LEM kal~aA)`. Verse
text from `quran-text/quran-no-tashkeel.json`.

## Claim 1 — "al-Takāthur is Meccan, by the consensus of the mufassirūn" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 102:1: *"makkiyya fī qawl jamīʿ al-mufassirīn,
wa-rawā al-Bukhārī annahā madaniyya"* (Meccan by the statement of all the mufassirūn; al-Bukhārī reported
it Medinan). Source: `spa5k-tafsir-api/ar-tafseer-al-qurtubi/102/1.json`.

**Test:** Cross-check `data/revelation-order.csv`.

**Result:** Q 102 → revelation_order #16, period **"Meccan"**, noldeke_phase **"Early Meccan"** (row:
`16,102,التكاثر,At-Takathur,Meccan,8,Early Meccan,…`). No Medinan classification in the on-disk
chronology file. The lone Medinan report al-Qurṭubī attributes to al-Bukhārī is a minority transmission,
not the dominant tradition.

**Verdict: VINDICATED (with the documented Bukhārī-Medinan minority variant).** Q 102 is Meccan / Early
Meccan in the on-disk chronology, matching the mufassirūn-consensus al-Qurṭubī cites. The minority
Medinan report is noted but not on-disk-supported.

## Claim 2 — "It is eight verses" (al-Qurṭubī)

**Claim:** al-Qurṭubī: *"wa-hiya thamānī āyāt"* (it is eight verses).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 102) and cross-check
`data/hafs-verse-counts.tsv`.

**Result:** 8 verses in the JSON; `hafs-verse-counts.tsv` line 102 = 8.

**Verdict: VINDICATED.** 8 verses, Hafs-Kūfan. (No divergent verse-count tradition for Q 102 is on disk;
the surah is below the threshold where the Kūfan/Baṣran/Madanī counting schools diverge.)

## Claim 3 — the rebuke-*kallā* census = 33, mufaṣṣal-concentrated (al-Suyūṭī ← al-Dānī)

**Claim:** al-Suyūṭī, *al-Itqān*, nawʿ 40 (← al-Dānī, *al-Muktafā*): the rebuke-particle *kallā* occurs
**33 times**, concentrated in the latter (mufaṣṣal) half of the muṣḥaf; Q 102 carries **3** of them.

**Test (PRE-REGISTERED as Q102-F-01 Arm A — `06-novel-findings.md`):** QAC-lemma disambiguation
(POS:AVR LEM `kal~aA`) over the whole corpus; verify total = 33, homograph-clean (no *kullan/kilā*
contamination), and Q 102's 3 tokens at vv 3, 4, 5.

**Result (from `csv/Q102-F-01.json`, replicating `findings/phase-b-hypotheses/h-new-2230-qac-lemma-numerical-rerun.md`
claim 7):** total rebuke-*kallā* = **33 EXACTLY** (raw substring count 38 conflates 5 *kullan* homographs —
H-NEW-2230); **no rebuke-*kallā* in Q 1–18** (first-half clean); **Q 102 = vv 3, 4, 5 (3 tokens)**.

**Verdict: VINDICATED — corpus-EXACT.** al-Dānī's 33 is confirmed at QAC-lemma strictness; Q 102 carries
3 of the 33. (This corrects the task-brief working figure of "×2 *kallā*": the morphological ground-truth
is **3**, vv 3-4-5.)

## Claim 4 — the v3/v4 doubling is *takrīr li-l-taghlīẓ* (al-Ṭabarī's Arab threat-device)

**Claim:** al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 102:4: *"wa-karrara qawlahu (kallā sawfa taʿlamūn)
marratayn, li-anna al-ʿArab idhā arādat al-taghlīẓ fī al-takhwīf wa-l-tahdīd karrarū al-kalimata
marratayn"* — the Arabs double a word to intensify a threat. Source:
`spa5k-tafsir-api/ar-tafsir-al-tabari/102/4.json`.

**Test (PRE-REGISTERED as Q102-F-01 Arm B):** Is the near-verbatim adjacent threat-doubling
(*kallā sawfa taʿlamūn* → *thumma kallā sawfa taʿlamūn*, identical-except-one-prefixed-particle)
corpus-distinctive?

**Result (from `csv/Q102-F-01.json`):**
- **B-H1 (corpus-exclusivity) FAILED (pre-commit violation):** the single-particle adjacent near-twin
  pair is NOT exclusive to Q 102 — there are **three** {Q 75:34-35, Q 78:4-5, Q 102:3-4}, all *thumma*-led.
- **B-H2 (bare-threat singleton) PASSED:** the bare threat-verse (*kallā sawfa taʿlamūn* / *thumma kallā
  sawfa taʿlamūn* as the whole verse) occurs corpus-wide only at Q 102:3 and Q 102:4 (count = 2, both Q 102).
- **B-H3 (supporting context):** the observed 3 single-particle adjacent near-twins vs a null_mean of
  0.183 (p_perm ≈ 0.0002) — such doublings are far rarer than chance re-pairing would produce.

**Verdict: VINDICATED (qualitatively), DIRECTIONAL (empirically).** al-Ṭabarī's *takrīr li-l-taghlīẓ*
device is real and has a cross-corpus correlate, BUT the device is **not unique to Q 102** — it is a
3-member *thumma*-doubled adjacent threat-refrain family. The bare-threat form (B-H2) IS a Q 102
singleton. Published honestly as DIRECTIONAL with the pre-commit violation flagged (`06-novel-findings.md`).

## Claim 5 — title-density independence: Q 102 is NOT rank-1 in its own title-root *kvr* (H-NEW-1820)

**Claim (project pillar law):** the eponymous surah is generally NOT the densest carrier of its own
title-root (title-density independence). Source: `findings/phase-b-hypotheses/h-new-1820-title-density-independence-formal.md`.

**Test:** Read Q 102's record in `findings/phase-b-hypotheses/csv/h-new-1820.json`.

**Result:** Q 102 (title al-Takāthur, root *kvr*): `title_density_rank` = **2**, `is_rank_1` = **false**,
`rank_1_surah` = **108** (al-Kawthar). Q 108 IS rank-1 in *kvr* by per-word density.

**Verdict: VINDICATED.** Q 102 is rank-2 in its own title-root; rank-1 is Q 108 al-Kawthar — the title is
a label, not a frequency-peak. This is a clean instance of the title-density-independence pillar law. The
project-relevant coincidence: rank-1 Q 108 is also Q 102's **nearest FR neighbor** (0.2937; H-NEW-111),
so the *kvr* root binds Q 102 ↔ Q 108 in both lexical-density and content-geometry space
(`01-empirical-profile.md` §1, §7).

## Claim 6 — the *yaqīn*-grade chain (project-internal, motivated by al-Jalālayn/al-Qurṭubī)

**Claim:** Q 102 contains the first two of the three classical *yaqīn*-grades — *ʿilm al-yaqīn* (v 5),
*ʿayn al-yaqīn* (v 7) — while the third, *ḥaqq al-yaqīn*, is withheld to Q 56:95 and Q 69:51.

**Test:** Scan `quran-text/quran-no-tashkeel.json` for the three *…al-yaqīn* genitive constructions.

**Result:** *ʿilm al-yaqīn* appears at Q 102:5; *ʿayn al-yaqīn* at Q 102:7; *ḥaqq al-yaqīn* at Q 56:95
and Q 69:51 (NOT in Q 102). The two-grade intra-surah pair (*ʿilm → ʿayn*) is in Q 102; the third grade
is cross-surah.

**Verdict: VINDICATED (descriptive).** Q 102 holds the first two certainty-grades as a deliberate
intra-surah pair (al-Jalālayn reads *ʿayn al-yaqīn* as the direct-sight intensification of v 5's
*ʿilm al-yaqīn*); the third grade's distribution is queued as Q102-F-03 (`00-overview.md` §8). This is a
descriptive distribution claim, not a formal corpus-singleton test.

## Claim 7 (NOT-TESTABLE) — the "visiting the graves" referent (death vs. literal grave-counting)

**Claim:** the mufassirūn split on whether *ḥattā zurtum al-maqābir* (v 2) means "until you died and were
buried" (al-Ṭabarī, al-Baghawī, Ibn Kathīr) or "until you literally went to the graveyards to count your
dead in the boast" (al-Jalālayn's second reading; al-Baghawī ← Muqātil/al-Kalbī on the Banū Sahm vs.
Banū ʿAbd Manāf grave-counting).

**Test:** This is a historical-*sabab* / lexical-semantic question, not a structural-numerical claim.

**Verdict: NOT-TESTABLE (empirically).** The death-vs-grave-counting reading is a matter of riwāya and
semantics, outside the project's empirical-architectural instruments. Both readings are on-disk attested
(`03-tafsir-survey.md`). Documented, not adjudicated.

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Meccan by mufassirūn consensus | al-Qurṭubī | **VINDICATED** (+ Bukhārī-Medinan minority variant) |
| 2 | 8 verses | al-Qurṭubī | **VINDICATED** |
| 3 | rebuke-*kallā* census = 33; Q 102 = 3 | al-Suyūṭī ← al-Dānī | **VINDICATED — corpus-EXACT** |
| 4 | v3/v4 = *takrīr li-l-taghlīẓ* | al-Ṭabarī | **VINDICATED (qual.) / DIRECTIONAL (empir.)** — 3-member family, not Q 102 singleton |
| 5 | Q 102 not rank-1 in own *kvr* root | H-NEW-1820 pillar | **VINDICATED** (rank-2; rank-1 = Q 108) |
| 6 | *yaqīn*-grade chain (*ʿilm → ʿayn*; *ḥaqq* elsewhere) | project / al-Jalālayn | VINDICATED (descriptive) |
| 7 | "visit graves" = death vs. grave-counting | tafsīr split | NOT-TESTABLE |

## Honest limits

- Claim 1's chronology rests on the single on-disk `revelation-order.csv` (Tanzil Egyptian Standard +
  Wikipedia Nöldeke); the Bukhārī-Medinan report al-Qurṭubī cites is documented but not chronology-file-supported.
- Claim 3's census is at QAC v0.4 POS:AVR LEM strictness; a raw-substring count (38) over-counts by
  conflating the *kullan/kilā* homographs (H-NEW-2230) — the rules-tuple matters, and is specified.
- Claim 4's empirical correlate is DIRECTIONAL: the *thumma*-doubling is a corpus family of 3, not a
  Q 102 singleton; full pre-commit-violation accounting in `06-novel-findings.md`.
- Claim 6 is a descriptive distribution observation, not a formal null-tested corpus-singleton; queued for
  formal promotion as Q102-F-03.

---

*Testable claims pre-registered before computation (Q102-F-01 Arms A, B) or deterministic. 2026-05-30.*
