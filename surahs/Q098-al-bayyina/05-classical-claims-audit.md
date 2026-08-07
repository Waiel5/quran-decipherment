---
surah: 98
surah_name_ar: البينة
surah_name_translit: al-Bayyina
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 7 claims audited — 3 VINDICATED, 1 VINDICATED-as-singleton, 1 title-density FALSIFIED (corrects H-NEW-1820 summary), 1 RULES-TUPLE/DATA documented, 1 NOT-TESTABLE
---

# Q 98 al-Bayyina — Classical Claims Audit

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, QAC v0.4 roots,
basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`.
The four pre-registered tests (Q098-F-01 Arms A-D) underpin Claims 1, 4, 5 and are detailed in
`06-novel-findings.md`.

## Claim 1 — "Q 98 al-Bayyina is rank-1 in its title-root" (H-NEW-1820 SUMMARY-LIST entry)

**Claim:** the project's H-NEW-1820 (title-density independence) summary-list asserted Q 98 al-Bayyina is
in the "title-density-EXACT (rank-1)" set for its title-root byn. (Project-internal summary; never verified
per-surah on disk.)

**Test (PRE-REGISTERED, Q098-F-01 Arm A, direction-locked FALSIFICATION):** is Q 98 corpus-rank-1 in byn,
(i) by raw root-attestation count, and (ii) by the exact eponymous surface form البينة/بينة? Source:
`data/morphology/root-index.json` (byn root) + `quran-text/quran-no-tashkeel.json` (surface scan).

**Result** (`csv/Q098-F-01.json`):
- **Raw byn count:** Q 98 = **2** attestations, raw-count rank **59/71**. The byn top-5 surahs are
  Q 2 (46), Q 4 (37), Q 5 (24), Q 3 (22), Q 6 (16). Q 98 is nowhere near rank-1.
- **Exact البينة surface form:** Q 98 = **2**; **4 other surahs tie or beat it** — Q 11 leads with **4**
  (على بينة), then Q 6 (2), Q 7 (2), Q 8 (2), Q 98 (2). Q 98 is NOT the surface-form peak either.
- Normalized-density rank = **6/71** (its 2-in-8-verses density is high but still not rank-1).

**Verdict: title-density-EXACT FALSIFIED.** Q 98 al-Bayyina — the surah whose very NAME means "the clear
proof" — is NOT the byn density-peak by any operationalization. The H-NEW-1820 summary-list entry is
**corrected**: Q 98 moves into the non-rank-1 majority (the H-NEW-1820 law is that eponymy and density-rank-1
are INDEPENDENT; 47/89 eponymous surahs are not rank-1). This is a clean new title-density-independence data
point. (See `06-novel-findings.md` Arm A; the ledger-ready §10.NN entry is in the JOURNAL hand-off.)

## Claim 2 — "It is nine verses (*tisʿ āyāt*)" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, Q 98:1: *"wa-hiya tisʿ āyāt"* — **nine verses**.

**Test:** count verses in `quran-text/quran-no-tashkeel.json` (Q 98); cross-check `data/hafs-verse-counts.tsv`.

**Result:** **8 verses** in the JSON; `hafs-verse-counts.tsv` line 98 = **8**. al-Qurṭubī's *tisʿ āyāt* is
a **non-Kūfan counting tradition** (likely Madanī/Baṣran), which partitions the same consonantal text into 9
fawāṣil — most plausibly by splitting one of the longer verses (the v 1 / v 2 region, or treating
*ṣuḥufan muṭahhara* as a separate fāṣila). The text is identical; only the āya-boundary count differs.

**Verdict: RULES-TUPLE / COUNTING-TRADITION documented.** Under the project-default Hafs-Kūfan tuple the
surah is **8 verses** (canonical here). al-Qurṭubī's 9-āya count is a legitimate alternative
counting-school reading of the *same* text, not an error — the Quran is one text with variant fāṣila
partitions. The exact split-point is queued (Q098-F-04). No word/letter count is affected.

## Claim 3 — "Meccan per Yaḥyā b. Sallām; Medinan per Ibn ʿAbbās and the majority" (al-Qurṭubī)

**Claim:** al-Qurṭubī, Q 98:1: *"makkiyya fī qawl Yaḥyā b. Sallām, wa-madaniyya fī qawl Ibn ʿAbbās
wa-l-jumhūr."* Ibn Kathīr concurs ("revealed in Madina").

**Test:** cross-check `data/revelation-order.csv` (Tanzil Egyptian Standard + Nöldeke).

**Result:** Q 98 → period **"Medinan"** (mushaf_order 98); revelation-order #100 (Tanzil Egyptian Std),
Nöldeke #92. No Meccan classification on disk; the Meccan qawl is the minority (Yaḥyā b. Sallām) opinion.

**Verdict: VINDICATED (majority position).** The on-disk chronologies both classify Q 98 as **Medinan**,
matching Ibn ʿAbbās + the jumhūr (and Ibn Kathīr). al-Qurṭubī's record of the Meccan minority qawl is
faithfully preserved as a documented dissent, not adopted by the on-disk data.

## Claim 4 — al-bariyya (البرية) is a corpus-rare lexical item (qurrāʾ/mufassirūn attention)

**Claim:** the rhyme-word *al-bariyya* in vv 6-7 receives concentrated qiraʾāt attention (al-Ṭabarī,
al-Zamakhsharī, al-Baghawī all discuss its hamza/non-hamza reading), implying it is a distinctive word.

**Test (PRE-REGISTERED, Q098-F-01 Arm B, deterministic):** how many corpus positions carry the surface
form البرية/برية, and are they all in Q 98? Source: `quran-text/quran-no-tashkeel.json` full scan.

**Result** (`csv/Q098-F-01.json`): البرية occurs in **exactly 2** corpus positions — **(98,6) and (98,7)**
— and nowhere else. It is a **Q 98-exclusive corpus hapax-pair**.

**Verdict: VINDICATED — corpus-SINGLETON.** The mufassirūn's philological attention is empirically
grounded: *al-bariyya* is a word the Quran uses only here, twice, in immediate antithetical adjacency. The
qiraʾāt fuss (Nāfiʿ + Ibn ʿĀmir hamza-ing both occurrences vs the majority non-hamza reading) is about a
word that appears nowhere else to anchor the reading — explaining the disagreement. (Arm B,
`06-novel-findings.md`.)

## Claim 5 — the vv 6-7 *sharr*/*khayr al-bariyya* contrast is a deliberate antithesis (muqābala)

**Claim:** the mufassirūn (al-Baghawī setting v 7 directly against v 6; al-Zamakhsharī's two-pole framing;
al-Suyūṭī's *ṭibāq/muqābala* figure, *Itqān* nawʿ 59) read vv 6-7 as a deliberate verbal antithesis: the
held-constant frame *ulāʾika hum [X] al-bariyya* with the antonym pivot *sharr → khayr*.

**Test (PRE-REGISTERED, Q098-F-01 Arm C, deterministic census):** among all corpus *adjacent*
faith-antithetical verse-pairs (one verse carrying the faith-pole root {Amn}, the other a disbelief-pole
root {kfr, nfq, Srk} — the SHA-locked H-NEW-2290/2360 F1 lexicon), is Q 98:6-7 the corpus-UNIQUE pair whose
verse-tails align with **exactly one substituted word** over **≥3 matched trailing words** AND whose single
pivot is the *khayr↔sharr* antonym? Source: `quran-text/quran-no-tashkeel.json` + `root-index.json`.

**Result** (`csv/Q098-F-01.json`): of **219** adjacent faith-antithetical verse-pairs in the corpus,
**exactly 1** satisfies all three criteria — **Q 98:6-7** (matched-tail = 3, pivot {شر, خير}). The nearest
contenders match a single-substitution tail but pivot on a **non-antonym** word: Q 2:102-103 (خير/أنفسهم),
Q 34:52-53 (التناوش/بالغيب), Q 63:7-8 (يعلمون/يفقهون), Q 3:176-177 (أليم/عظيم). None is a true antonym
muqābala.

**Verdict: VINDICATED — corpus-SINGLETON.** Q 98:6-7 is the corpus's **tightest *muqābala lafẓiyya***: a
single-word-substitution aligned tail-frame pivoting on a genuine lexical antonym. al-Suyūṭī's muqābala
figure (*Itqān* nawʿ 59) has here a corpus-unique exemplar. (Arm C, `06-novel-findings.md`.)

## Claim 6 — the antithesis sets two lexically DISJOINT contents against a shared frame (classical muqābala intuition)

**Claim:** classical muqābala theory (and the Q083-F-01 "destiny-catalogue" precedent) suggests an
antithesis opposes two lexically *disjoint* contents within a parallel frame.

**Test (PRE-REGISTERED, Q098-F-01 Arm D, permutation; seed 20260509, 10000 perms; direction-locked
DISJOINT):** is the QAC-root Jaccard J(v6, v7) BELOW a length-matched random-verse-pair null (more disjoint
than chance)?

**Result** (`csv/Q098-F-01.json`): J(v6,v7) = **0.0833** (they share the root **brA** = *al-bariyya*).
null_mean = **0.0261**, null_std = 0.0492, **z = +1.163**, p_lower = 0.878. The observed Jaccard is
**ABOVE** the null mean — the pre-committed DISJOINT direction is **REVERSED**.

**Verdict: NULL (pre-commit violation, full prominence).** Even the corpus's tightest *surface*-muqābala is
content-OVERLAPPING at the root level (it shares the very rhyme-root brA on which the antithesis pivots).
This **replicates the H-NEW-2360 jadal-overlap law at verse-pair scale**: antithetical pairs OVERLAP in
content rather than being disjoint — the parallel frame is built *from* shared roots, not against disjoint
ones. The classical "disjoint contents" intuition fails; the empirical signature is overlap. (Arm D,
`06-novel-findings.md`, published as NULL.)

## Claim 7 — the recitation faḍīla and the *qirāʾat al-ʿālim ʿalā al-mutaʿallim* fiqh point (al-Qurṭubī)

**Claim:** al-Qurṭubī (Q 98:1): the ṣaḥīḥ basis of the surah's virtue is the Ubayy recitation report
(Bukhārī + Muslim); the weak Abū al-Dardāʾ thawāb report is *bāṭil* (Ibn al-ʿArabī); and the report yields
the fiqh of *qirāʾat al-ʿālim ʿalā al-mutaʿallim* (a teacher reciting to a student).

**Test:** verify the ṣaḥīḥ and weak attestations on disk (`04-hadith-corpus.md`). The fiqh inference is a
juristic reading, not an empirical-structural claim.

**Result:** the Ubayy report is VERIFIED in Bukhārī #4753/#4754, Muslim #1757/#6185, Tirmidhī
#3888/#3889/#3995 (gradings ḥasan ṣaḥīḥ / ḥasan / ḥasan ṣaḥīḥ); the Abū al-Dardāʾ report is recorded and
graded *lā yaṣiḥḥ / bāṭil* by al-Qurṭubī citing Ibn al-ʿArabī.

**Verdict: VINDICATED (attestations) + NOT-TESTABLE (fiqh inference).** The ḥadīth basis is exactly as
al-Qurṭubī represents it; the *qirāʾat al-ʿālim ʿalā al-mutaʿallim* legal inference is a juristic-uṣūl
point outside the project's empirical-architectural instruments and is recorded, not adjudicated.

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Q 98 rank-1 in title-root byn | H-NEW-1820 summary | **title-density-EXACT FALSIFIED** (corrected) |
| 2 | nine verses (*tisʿ āyāt*) | al-Qurṭubī | RULES-TUPLE / counting-tradition (Hafs = 8) |
| 3 | Meccan (minority) / Medinan (majority) | al-Qurṭubī, Ibn Kathīr | **VINDICATED** (Medinan, majority) |
| 4 | al-bariyya is corpus-rare | qurrāʾ / mufassirūn | **VINDICATED — corpus-SINGLETON** (hapax-pair) |
| 5 | vv 6-7 deliberate antonym muqābala | al-Baghawī / al-Zamakhsharī / al-Suyūṭī | **VINDICATED — corpus-SINGLETON** (1 of 219) |
| 6 | antithesis = disjoint contents | classical muqābala / Q083 | **NULL (pre-commit violation)** — overlap, replicates H-NEW-2360 |
| 7 | ṣaḥīḥ Ubayy faḍīla + weak Abū al-Dardāʾ + fiqh | al-Qurṭubī | VINDICATED (attestations) + NOT-TESTABLE (fiqh) |

## Honest limits

- Claim 1's FALSIFIED verdict is a correction of a project-internal *summary* claim, not a classical
  scholar's claim; the underlying H-NEW-1820 *law* (title-density independence) is reinforced, not refuted.
- Claim 5's "corpus-SINGLETON" depends on the locked operationalization (faith-field F1 lexicon,
  single-substitution-aligned-tail with matched-tail ≥ 3, the {خير, شر} antonym set). A looser antonym set
  or a different antithesis lexicon could admit more pairs; the strict locked definition yields exactly 1.
- Claim 6's NULL turns on the QAC-root Jaccard instrument; a surface-bigram or lemma-level overlap measure
  would shift the magnitude but cannot flip the sign (the shared brA root is on the rhyme-word itself).
- Claim 2's 9-āya split-point is inferred, not located on disk; the variant fāṣila partition is queued
  (Q098-F-04).

---

*Testable claims pre-registered before computation (Q098-F-01, seed 20260509, SHA-locked) or deterministic.
2026-05-30.*
