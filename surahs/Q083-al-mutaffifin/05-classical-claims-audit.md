---
surah: 83
surah_name_ar: المطففين
surah_name_translit: al-Muṭaffifīn
file_type: classical-claims-audit
date_last_updated: 2026-05-29
phase: B+
verdict: 5 claims audited. Boundary claim = VINDICATED-AS-CHRONOLOGICAL (not architectural). Rebuke-kallā max = VINDICATED. ruʾya proof-text = NOT-EMPIRICALLY-TESTABLE.
---

# Q 83 al-Muṭaffifīn — Classical Claims Audit

Every claim is stated with a disk-citation, given the rules-tuple needed to test it, tested where
testable, and assigned an honest verdict.

---

## Claim 1 — Q 83 is the Meccan/Medinan BOUNDARY surah ("last Meccan" / revealed in transit)

**Statement + citation.** al-Qurṭubī (*al-Jāmiʿ* ad Q 83:1,
`ar-tafseer-al-qurtubi/83.json`): Meccan (Ibn Masʿūd, al-Ḍaḥḥāk, Muqātil) / Medinan (al-Ḥasan, ʿIkrima;
Muqātil even: "the first surah revealed in Medina") / "between Mecca and Medina" (al-Kalbī, Jābir b.
Zayd). al-Suyūṭī (*al-Itqān*, raw `suyuti-itqan.openiti.raw.txt`): al-Nasafī and others — *"Sūrat
al-Muṭaffifīn, or part of it, was revealed during the journey of the Hijra, before the Prophet entered
Medina."* The project chronology (`data/revelation-order.csv`) records Q 83 as **revelation #86 — the
LAST Meccan surah before Q 2 al-Baqara (#87, the first Medinan)** in the Tanzil Egyptian Standard;
Nöldeke #37 ("Early Meccan").

**Rules-tuple to test.** This is a chronology-attribution claim, not a text-internal numerical one. The
testable empirical sub-claim is: *does Q 83 sit at an architectural seam corresponding to the
Meccan→Medinan transition?* Tuple: `(no-tashkeel, QAC-STEM roots, FR distance from h-new-111.json,
mushaf order)`.

**Test (FR chronology-architecture dissociation).** From `h-new-111.json`:
- FR(Q 83, Q 2) = **1.1670** — Q 2 (the surah revealed IMMEDIATELY AFTER Q 83 in the Egyptian
  chronology) ranks **109/113** in Q 83's distance list (the 5th-FARTHEST surah from Q 83).
- FR(Q 83, mean of short-Meccan-tail Q 84–114) = **0.6286**; FR(Q 83, Q 82) = **0.5770** (2nd-nearest).

**Verdict: VINDICATED AS A CHRONOLOGICAL FACT — but the boundary is NOT architectural.** Q 83 genuinely
sits at the chronological Meccan→Medinan hinge (Egyptian-order #86, last Meccan), and the classical
"revealed in transit during the Hijra" tradition (al-Suyūṭī ← al-Nasafī) is a coherent harmonization of
the Meccan and Medinan camps. BUT the FR-architecture shows ZERO trace of this boundary: Q 83 is
architecturally a short-Meccan-tail surah (FR-central, all 15 nearest neighbours in Q 91–114), and the
surah revealed right after it (Q 2) is one of its FARTHEST. This is the standard
**chronology-architecture dissociation** the project has documented across the corpus: the mushaf is
position/architecture-clustered, NOT chronology-clustered. The "boundary" is in the revelation TIMELINE,
invisible in the root-distribution ARCHITECTURE. (The Makkī/Madanī attribution itself is a transmission
question, not empirically decidable from the text alone — NOT-TEXT-DECIDABLE on that sub-point.)

---

## Claim 2 — Q 83 contains the maximum rebuke-*kallā* (the *radʿ* particle) and is in the latter half

**Statement + citation.** al-Zamakhsharī (*Kashshāf*, ad vv. 7–9: *"kallā radʿuhum …"*) and al-Baghawī
(*"kallā radʿ"*) classify Q 83's *kallā* as the rebuke-particle. al-Suyūṭī (*al-Itqān*, raw) cites
al-Dānī that rebuke-*kallā* occurs **33 times, all in the latter half of the Qurʾān** (§10.80 H-NEW-2160
in MASTER-FINDINGS-LEDGER). Q 83 has *kallā* at vv. 7, 14, 15, 18.

**Rules-tuple to test.** `(no-tashkeel, QAC v0.4 morphology, POS:AVR + LEM kal~aA, per-surah count)`.
Critically requires MORPHOLOGICAL disambiguation: raw substring كلا conflates rebuke-*kallā* with
*kullā/kilā* ("both/all").

**Test (QAC).** Computed from `data/morphology/quranic-corpus-morphology-0.4.txt`:
- Q 83 genuine rebuke-*kallā* (POS:AVR) = **4** (vv. 7, 14, 15, 18) — **TIED with Q 74 al-Muddaththir for
  the corpus MAXIMUM** (no surah exceeds 4).
- Total genuine AVR-*kallā* corpus-wide = **33** — exactly matching al-Dānī's classical count.
- **27 of 33** are in surahs s>57 (mushaf second half); Q 83's 4 are all second-half, all clause-initial.
- Q 4 al-Nisāʾ shows "4 كلا" by raw substring but **0** are genuine rebuke-*kallā* (all homograph
  *kullā/kilā*) — the §10.80 homograph trap.

**Verdict: VINDICATED.** Q 83 IS one of the two corpus-maximal rebuke-*kallā* surahs (4, tied with
Q 74), all in the latter half, vindicating both the al-Zamakhsharī/al-Baghawī *radʿ* classification and
al-Dānī's "latter-half-only / count = 33" observation — but ONLY after morphological disambiguation
(the raw substring count would mislead, exactly as §10.80 warns). This extends §10.80: Q 83 is a
co-holder of the rebuke-*kallā* maximum and a clean case where the disambiguated count rescues the
classical claim.

---

## Claim 3 — *sijjīn* and *ʿilliyyīn* are an antithetical *muqābala* pair (frame-shared, content-opposite)

**Statement + citation.** al-Rāzī (*Mafātīḥ*, raw) and al-Zamakhsharī (*Kashshāf*, ad vv. 29–36, raw)
read sijjīn↔ʿilliyyīn as a deliberate *muqābala* of two records — same announcement frame (*kallā inna
kitāba …, wa-mā adrāka mā …, kitābun marqūm*), opposite destiny (earth/heaven, prison/loftiness).

**Rules-tuple to test.** `(no-tashkeel, QAC-STEM roots, root-SET overlap, 11-verse blocks vv.7-17 vs
18-28, 10000-perm block-pair null, seed 20260509)`. Pre-registered as **Q083-F-01**.

**Test (Q083-F-01, 06-novel-findings).**
- The two blocks share **3 roots** (`ktb`, `rqm`, `dry` — the bare frame) vs a random-block-pair null
  mean of **12.7** (the blocks are FAR MORE disjoint than chance; the pre-committed "elevated-mirror"
  direction was REVERSED → published as a pre-commit violation).
- Destiny-vocabularies **perfectly disjoint** (H3 CONFIRMED, zero leakage).

**Verdict: VINDICATED (in a sharper form than claimed).** The muqābala is real, but it is achieved by a
**minimal 3-root shared scaffold + total destiny-disjunction** — NOT by lexical mirroring. The classical
*muqābala* reading is empirically correct; the naive empirical expectation (that "mirror" ⇒ high shared
vocabulary) is FALSE. The antithesis is rhetorically austere: the only shared lexis is the announcement
formula that signals "another record." (Verdict for the test as a whole: DIRECTIONAL — H1 pre-commit
violation + H3 confirmed.)

---

## Claim 4 — Q 83:15 (*maḥjūbūn*) proves the believers will SEE God (ruʾyat Allāh)

**Statement + citation.** al-Shāfiʿī, via Ibn Kathīr (*Tafsīr* ad Q 83:15,
`ar-tafsir-ibn-kathir/83.json`): *"In this verse is a proof that the believers will see their Lord on
that Day"* — by *mafhūm al-mukhālafa* (if the wicked are *veiled* as punishment, the believers are
*unveiled* as reward). Ibn Kathīr corroborates with Q 75:22–23 and the mutawātir vision-hadiths.

**Rules-tuple to test.** None applicable — this is a theological-juristic inference (*istidlāl
bi-l-mafhūm*) on a doctrinal matter (the beatific vision, contested between Ashʿarīs/Shāfiʿīs and the
Muʿtazila).

**Verdict: NOT EMPIRICALLY TESTABLE (theological).** This is a valid object of classical *uṣūl*
argument, not of root-distribution or distance analysis. Recorded for completeness as a major reception-
historical fact: Q 83:15 is a primary anti-Muʿtazilī proof-text for ruʾyat Allāh. Out of project scope
(§10 of the Protocol: theological miracle/doctrine claims are not empirical).

---

## Claim 5 — Ibn ʿAbbās: Q 83 was "the first surah revealed when [the Prophet] reached Medina"

**Statement + citation.** al-Qurṭubī (ad Q 83:1, `ar-tafseer-al-qurtubi/83.json`) reports from Ibn
ʿAbbās: *"it is the first surah revealed upon the Messenger of God the moment he arrived in Medina."*
Muqātil concurs ("the first surah revealed in Medina"). This is a STRONGER version of Claim 1.

**Rules-tuple to test.** Chronological-transmission claim; not text-decidable. Note it CONTRADICTS the
Egyptian-standard ordering (which makes Q 2 al-Baqara the first Medinan and Q 83 the last Meccan).

**Verdict: TRANSMISSION-CONTESTED, NOT TEXT-DECIDABLE.** The classical sources themselves disagree
(Ibn ʿAbbās/Muqātil "first Medinan" vs the dominant "last Meccan / Hijra-transit" placement adopted by
the Egyptian standard). The text carries no internal marker that adjudicates this; the two positions
are alternative transmission-traditions. What IS empirically clear (Claim 1): wherever in the timeline
Q 83 falls, its ARCHITECTURE is short-Meccan-tail, not Medinan-ṭiwāl (FR(Q83,Q2)=1.167, rank 109/113).
The "first/last at the Mecca-Medina seam" debate is precisely a debate about a single hinge point — and
that the surah sits AT the hinge is the one thing all camps agree on, vindicating the **boundary**
characterization regardless of which side of the hinge one assigns it to.

---

## Audit summary

| # | Claim | Verdict |
|:-:|:--|:--|
| 1 | Q 83 = Meccan/Medinan boundary surah | **VINDICATED as chronological** (Egyptian #86, last-Meccan; Hijra-transit tradition) — but NOT architectural (FR shows no boundary) |
| 2 | Q 83 = max rebuke-*kallā*, latter-half | **VINDICATED** (4, tied Q 74; corpus total 33; after QAC disambiguation) |
| 3 | sijjīn↔ʿilliyyīn muqābala | **VINDICATED in sharper form** (3-root frame + total destiny-disjunction; Q083-F-01) |
| 4 | Q 83:15 proves ruʾyat Allāh | **NOT EMPIRICALLY TESTABLE** (theological *istidlāl*) |
| 5 | Ibn ʿAbbās "first Medinan surah" | **TRANSMISSION-CONTESTED, NOT TEXT-DECIDABLE** (contradicts Egyptian last-Meccan order) |

## Cross-references
- 06-novel-findings (Q083-F-01 detail for Claim 3).
- 01-empirical-profile §8 (rebuke-*kallā* for Claim 2); §2 (FR for Claim 1).
- 03-tafsir-survey (al-Shāfiʿī ruʾya argument for Claim 4).
- §10.80 H-NEW-2160 (MASTER-FINDINGS-LEDGER) for Claim 2's homograph methodology.
