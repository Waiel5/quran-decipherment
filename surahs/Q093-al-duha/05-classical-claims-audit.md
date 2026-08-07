---
surah: 93
surah_name_ar: الضحى
surah_name_translit: al-Ḍuḥā
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 SPLIT (whole-surah ✓ / boundary-lexis ✗), 1 NOT-TESTABLE
---

# Q 93 al-Ḍuḥā — Classical Claims Audit


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

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, QAC v0.4 ROOT,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`.

## Claim 1 — "Sūrat al-Ḍuḥā is Meccan, by agreement" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 93:1
(`spa5k-tafsir-api/ar-tafseer-al-qurtubi/93/1.json`): *"makkiyya bi-ttifāq"* (Meccan by agreement).
al-Baghawī (`ar-tafsir-al-baghawi/93/1.json`) concurs: *"makkiyya."*

**Test:** Cross-check `data/revelation-order.csv` (Tanzil Egyptian Standard + Nöldeke).

**Result:** mushaf_order 93 → revelation_order **#11**, period **"Meccan"**, Nöldeke **#13**, phase
"Early Meccan." No Medinan-classification variant on disk. (Chronological neighbors: Q 92 al-Layl =
revelation #9 / Nöldeke #10; Q 94 al-Sharḥ = revelation #12 / Nöldeke #12.)

**Verdict: VINDICATED.** Q 93 is Meccan in both the Egyptian-standard and Nöldeke chronologies on disk,
matching al-Qurṭubī's *bi-ttifāq*. It is an early-Meccan surah (revelation #11 of 114).

## Claim 2 — "It is eleven verses" (al-Qurṭubī)

**Claim:** al-Qurṭubī, on Q 93:1: *"iḥdā ʿashrata āya"* (eleven verses).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 93) and cross-check
`data/hafs-verse-counts.tsv` line 93.

**Result:** 11 verses in the JSON; `hafs-verse-counts.tsv` line 93 = **11**.

**Verdict: VINDICATED.** 11 verses, Hafs-Kūfan, matching al-Qurṭubī. (No divergent verse-count tradition
for Q 93 is on disk — the surah is below the threshold where the Kūfan/Baṣran/Madanī counting schools
split. The oath-pair vv 1-2 and the favor/command triads vv 6-8 / 9-11 are not contested as fawāṣil.)

## Claim 3 — the asbāb al-nuzūl (the fatra: delayed revelation + the taunt → Q 93:1-3)

**Claim:** the mufassirūn (al-Ṭabarī, al-Baghawī, al-Qurṭubī, Ibn Kathīr) are unanimous that vv 1-3 were
revealed after the *fatrat al-waḥy* (withholding of Jibrīl) and a taunt that the Prophet had been
forsaken — via the **al-Aswad b. Qays ← Jundub** chain.

**Test:** Verify the chain in the on-disk 9-book ḥadīth corpus (`scripts/verify_fatra_hadith.py`).

**Result:** the fatra ḥadīth is confirmed on disk in **Bukhārī #1092, #4744, #4745, #4776; Muslim #4525,
#4526; Tirmidhī #3429** (*ḥasan ṣaḥīḥ*) — all al-Aswad b. Qays ← Jundub (b. ʿAbdallāh al-Bajalī /
b. Sufyān). See `04-hadith-corpus.md` §1 for the verified `idInBook` numbers and the per-narration wording
(woman's taunt vs idolaters' *qad waddaʿa Muḥammad*).

**Verdict: VINDICATED.** The asbāb of vv 1-3 is among the most securely attested occasions of revelation —
Ṣaḥīḥayn + Tirmidhī *ḥasan ṣaḥīḥ*, all via the single al-Aswad-b.-Qays ← Jundub chain, verified on disk.
(The peripheral details — Umm Jamīl as the taunter; the puppy-under-the-bed cause of delay — are
*qīla*/tafsīr material in al-Baghawī, NOT in the 9-book chains; flagged in `04-hadith-corpus.md` §2.)

## Claim 4 — al-Ḍuḥā + al-Sharḥ are "one surah" (Ṭāwūs, ʿUmar b. ʿAbd al-ʿAzīz; al-Rāzī's report)

**Claim:** al-Rāzī, *Mafātīḥ al-ghayb*, opening Sūrat al-Sharḥ
(`raw/razi-mafatih-al-ghayb.openiti.raw.txt`, ~L260761): it is related from **Ṭāwūs and ʿUmar b. ʿAbd
al-ʿAzīz** that al-Sharḥ and al-Ḍuḥā are *sūra wāḥida* — recited together in one rakʿa without an
intervening basmala — because Q 94:1 (*alam nashraḥ laka*) is *ka-l-ʿaṭf* (like a continuation) of Q 93:6
(*alam yajidka yatīman*). al-Rāzī himself **REJECTS** the identification (the two surahs were revealed in
different states — grief vs expanded-breast). al-Suyūṭī (*al-Itqān*, nawʿ on *al-munāsaba bayna al-suwar*)
carries the same Ṭāwūs / ʿUmar report.

**Test (PRE-REGISTERED as Q093-F-01 Arm A):** does the claimed pairing manifest (i) at the whole-surah
root-distribution scale (FR proximity + TSP-seam smoothness) and (ii) at the boundary-pericope lexical
scale (H-NEW-2280 seam root-Jaccard)? Direction-locked DISSOCIATION prediction.

**Result (from `csv/Q093-F-01.json`, SHA-verified at runtime):**
- **Whole-surah scale — VINDICATED.** Q 94 is Q 93's **4th-nearest** Fisher-Rao neighbor of 113
  (FR 0.3641, top-5; A-H1 ✓), and the Q 93 → Q 94 canonical-adjacency seam is the **10th-smoothest** of
  113 (delta_raw −0.01520, a clamped/seamless joint; A-H2 ✓). The pair's FR distance ranks **128 / 6441**
  (1.99th percentile) corpus-wide (`csv/Q093F01-pair-cohesion.json`).
- **Boundary-pericope scale — the pairing does NOT hold (dissociation).** The seam root-Jaccard between
  the last-k verses of Q 93 and the first-k verses of Q 94 is **exactly 0.0 at both k=3 and k=5** (≤ the
  corpus seam means 0.0416 / 0.0632; A-H3 ✓; percentile 43.4 / 24.8, A-H4 ✓). The two surahs share ZERO
  QAC roots across their boundary pericopes; the only root they share anywhere is `rbb` (Lord), which does
  not fall in the seam.

**Verdict: SPLIT (scale-dissociation; the dissociation itself is CONFIRMED).** The classical "one surah"
intuition is **vindicated at the whole-surah root-distribution scale** (Q 94 is a top-5 FR neighbor and the
exit-seam is among the 13 smoothest in the mushaf) but **falsified at the boundary-lexical scale** (the
junction al-Rāzī names — Q 93:6 ↔ Q 94:1 — shares no root). This is exactly the pre-registered
dissociation: the famous pairing is a **whole-surah-distribution bond, not a seam-lexical bond.** Crucially,
the claim is **NOT ḥadīth-attested** (no 9-book narration cites both surahs; `04-hadith-corpus.md` §4) — it
is a juristic/exegetical position with whole-surah empirical support but no isnād. Full detail in
`06-novel-findings.md` (Q093-F-01 Arm A, CONFIRMED scale-dissociation).

## Claim 5 — Ibn Kathīr's favor→command parallel (v 6↔9 orphan, v 7↔10 lost/asker, v 8↔11 poor/proclaim)

**Claim:** Ibn Kathīr, *Tafsīr al-ʿaẓīm*, on Q 93:9-11
(`spa5k-tafsir-api/en-tafisr-ibn-kathir/93/9.json`): each future-command is the moral counterpart of the
corresponding past-favor — *"just as you were an orphan and Allāh sheltered you, do not oppress the
orphan"* (v 6→9); *"just as you were astray and Allāh guided you, do not scorn the one who asks"* (v 7→10);
*"just as you were poor and Allāh enriched you, tell of Allāh's favor"* (v 8→11). A triad-answers-triad
chiasm.

**Test (PRE-REGISTERED as Q093-F-01 Arm B):** does the favor→command structure leave a lexical fingerprint?
B-H1: does `wjd` (*wajadaka*) unify the favor block (vv 6,7,8 only)? B-H2: among the favor-block roots,
exactly how many also appear in the command block, and is the bridge `ytm` (orphan)?

**Result (from `csv/Q093-F-01.json`):**
- **B-H1 ✓:** `wjd` appears in exactly vv 6, 7, 8 and no other Q 93 verse — the three-fold *wajadaka*
  anaphora opens the favor triad.
- **B-H2 ✓:** the favor block {vv 6-8} roots = {Awy, Dll, Eyl, gny, hdy, wjd, **ytm**}; the command block
  {vv 9-11} roots = {Hdv, nEm, nhr, qhr, rbb, sAl, **ytm**}; the intersection is **exactly one root —
  `ytm`** (orphan), bridging v 6 → v 9.

**Verdict: VINDICATED — with an empirical refinement.** Ibn Kathīr's favor→command *thematic* mapping is
real, AND the surah lexically realizes it — but **only at the first pair (orphan, v 6↔9)**. The other two
pairings he names (lost/asker v 7↔10; poor/proclaim v 8↔11) are positional-thematic with **zero shared
root**. The orphan is the surah's single lexical hinge: the only word that is both the name of a divine
favor and the head of an ethical command in the same surah. Corpus census (B-H3): `ytm` appears in ≥2
verses in only **3 surahs** — Q 2, Q 4, Q 93 — and Q 93 is the only one realizing a favor→command recall.
Full detail in `06-novel-findings.md` (Arm B, CONFIRMED).

## Claim 6 (NOT-TESTABLE empirically) — the *al-ḍuḥā* gloss and the *fa-tarḍā* (v 5) referent

**Claim:** the mufassirūn dispute (a) what *al-ḍuḥā* (v 1) denotes — al-Ṭabarī: *al-nahār kulluh* (the whole
day); al-Qurṭubī/Qatāda: an hour of the daytime; a minority (Jaʿfar al-Ṣādiq): the forenoon Allāh spoke to
Mūsā — and (b) what *wa-la-sawfa yuʿṭīka rabbuka fa-tarḍā* (v 5) promises — worldly victory + the
Hereafter (Ibn Isḥāq); the *ḥawḍ* and *shafāʿa*; "a thousand palaces of pearl" (Ibn ʿAbbās).

**Test:** these are lexical-semantic and theological referent questions, not structural-numerical claims
about the text.

**Verdict: NOT-TESTABLE (empirically).** The *al-ḍuḥā* gloss and the *fa-tarḍā* referent are matters of
lexicography and tafsīr, outside the project's empirical-architectural instruments. Documented in
`03-tafsir-survey.md` §1, §4, not adjudicated here. (The *fa-tarḍā*=intercession reading IS attached to a
Ṣaḥīḥ Muslim narration cited by al-Qurṭubī — see `04-hadith-corpus.md` §3 — but the *choice* among the
readings is exegetical, not empirical.)

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Meccan by agreement | al-Qurṭubī | **VINDICATED** (revelation #11, Nöldeke #13) |
| 2 | 11 verses | al-Qurṭubī | **VINDICATED** (Hafs line 93 = 11) |
| 3 | fatra asbāb (vv 1-3) via Jundub | al-Ṭabarī / Ibn Kathīr | **VINDICATED** (Bukhārī/Muslim/Tirmidhī, verified) |
| 4 | al-Ḍuḥā + al-Sharḥ "one surah" | Ṭāwūs, ʿUmar b. ʿAbd al-ʿAzīz (al-Rāzī) | **SPLIT** (whole-surah ✓ FR rank 4 / seam rank 10; boundary-lexis ✗ J=0.0; NOT ḥadīth-attested) |
| 5 | favor→command parallel (v6↔9, 7↔10, 8↔11) | Ibn Kathīr | **VINDICATED** (refined: only v6↔9 orphan is lexically realized) |
| 6 | *al-ḍuḥā* gloss / *fa-tarḍā* referent | tafsīr dispute | NOT-TESTABLE |

## Honest limits

- Claim 4's split verdict is on the QAC v0.4 ROOT level. A surface-token or lemma seam metric WOULD
  register the shared *rabbi* (Q 93:11 *bi-niʿmati rabbika* / Q 94:8 *wa-ilā rabbika*) — but at the ROOT
  level the boundary pericopes are disjoint, matching the H-NEW-2280 instrument. The dissociation claim is
  ROOT-level. (Cf. MEMORY: rules-tuple sensitivity is bidirectional — a lemma-level instrument could
  *rehabilitate* a weak boundary bond; this is flagged, not run, here.)
- Claim 5's "only the orphan pair is lexically realized" is on the ROOT level; the other two pairs share
  *thematic* but not *root* material — a semantic-field instrument would score them as related.
- Verse-count and Meccan-classification variant traditions for Q 93 are not on disk; the 11-verse Hafs
  count and Meccan classification are treated as canonical.
- The Ṭāwūs / ʿUmar "one surah" report's isnād was not separately traced (al-Rāzī carries it on disk;
  al-Zamakhsharī's al-Kashshāf on the same pairing was not separately transcribed — flagged in
  `03-tafsir-survey.md` §7).

---

*All testable claims pre-registered before computation (Q093-F-01) or deterministic. 2026-05-30.*
