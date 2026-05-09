---
surah: 23
surah_name_ar: المؤمنون
surah_name_translit: al-Muʾminūn
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — five non-trivial classical claims audited
---

# Q 23 al-Muʾminūn — Classical Claims Audit

This file audits five non-trivial classical claims about Q 23 against on-disk data using the binding methodology of `INVESTIGATION-PROTOCOL.md` §1.2 (pre-registration) and §2.11 (anti-hallucination). For each claim: state the claim with explicit citation; identify the rules-tuple required to test it; run the test or note "not-empirically-testable"; verdict.

## Claim 1 — al-Zamakhsharī: opening / closing inclusio on the root *flḥ*

### 1.1 Statement

al-Zamakhsharī, *al-Kashshāf* (file `data/literature/classical-tafsir/zamakhshari-kashshaf/zamakhshari-kashshaf.djvu.txt` offset ~2956200):

> وأورد في خاتمتها أنه لا يفلح الكافرون فشتان ما بين الفاتحة والخاتمة

— "And He brings forth at the surah's close: *innahu lā yufliḥu l-kāfirūn*. How vast the difference between the opening and the closing!" (citing v. 1 ↔ v. 117 inversion).

### 1.2 Rules-tuple

`(no-tashkeel, QAC-stem-roots, all-flḥ-attestations-in-Q23, mushaf-order)`.

### 1.3 Test

Per QAC v0.4 (cross-validated against `quran-text/quran-no-tashkeel.json`):

| Verse | Form | Stem |
|:-:|:--|:--|
| 23:1 | أفلح (afla**ḥ**a) | flḥ-IV-3MS-perfective |
| 23:102 | المفلحون (al-mufli**ḥ**ūn) | flḥ-IV-MP-act-participle |
| 23:117 | يفلح (yufli**ḥ**u) | flḥ-IV-3MS-imperfective, negated by لا |

Exactly **3** *flḥ*-attestations in Q 23, at exactly the positions {1, 102, 117}. The opening (v. 1) is positive-perfective applied to *muʾminūn*; the closing (v. 117) is negative-imperfective applied to *kāfirūn*. The two flank the surah with strict polarity-inversion.

Middle anchor v. 102 is at the eschatological *mawāzīn* scene (the scales of deeds). This is an asymmetric ABA structure: positive perfective at v. 1, positive participle at v. 102 (close to surah-end at ~87% through), negative imperfective at v. 117.

### 1.4 Verdict: **VINDICATED** (with empirical refinement)

al-Zamakhsharī's claim is **empirically confirmed**: opening + closing *flḥ*-inversion is real. The empirical refinement is that v. 102 supplies a **mid-late positive anchor** between the two endpoints — making the structure not a strict-ABA arc but an opening + mid-late reinforcement + closing-inversion. This matches al-Zamakhsharī's "vast difference between opening and closing" qualitative observation.

(See 06-novel-findings.md §3 for an extension testing whether the *flḥ*-triplet positioning is unique to Q 23 in the corpus.)

## Claim 2 — al-Suyūṭī: Q 23 belongs to the corpus's "purest-monorhyme" class

### 2.1 Statement

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 38 *al-fawāṣil* (PDF at `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`) treats Q 23 as belonging to the surahs whose verse-endings (fawāṣil) form a near-monorhyme.

### 2.2 Rules-tuple

`(no-tashkeel, final-orthographic-letter-per-verse, Shannon-entropy-nats)`.

### 2.3 Test

Final-letter distribution across Q 23's 118 verses, computed from `quran-text/quran-no-tashkeel.json` (see also 01-empirical-profile.md §5):

| Final letter | Count | Fraction |
|:-:|:-:|:-:|
| ن | 114 | 96.6% |
| م | 4 | 3.4% |

Shannon entropy = **0.148 nats** → rank **109 / 114** = corpus's 6th-purest monorhyme (after Q 55 al-Raḥmān, Q 26 al-Shuʿarāʾ, Q 71 Nūḥ, Q 105 al-Fīl, Q 109 al-Kāfirūn).

### 2.4 Verdict: **VINDICATED**

al-Suyūṭī's qualitative classification places Q 23 in the corpus's purest-monorhyme tier. The empirical entropy rank (109 / 114) directly confirms this. The dominant rhyme is the form-IV active-participle plural *mu-CCi-ūn / mu-CCi-īn* on a fatḥa + nūn rāwī (-ūna / -īna).

## Claim 3 — al-Biqāʿī: Q 22 → Q 23 *munāsabah* via post-Ḥajj-to-the-believers transition

### 3.1 Statement

al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* (file `data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt`) opens his Q 23 commentary with a *munāsabah* connecting it to the preceding Q 22 al-Ḥajj: the pilgrimage-surah closes with the *jihād* + *ʿibādah* injunction (Q 22:77-78), and Q 23 opens with the description of those who **achieve the success** (*falāḥ*) promised at the close of Q 22 ("that you may prosper" *laʿallakum tufliḥūn*, Q 22:77).

Specifically: Q 22:77 ends with *... wa-fʿalū l-khayr laʿallakum tufliḥūn* — "do good that you may prosper", and Q 23:1 opens with *qad aflaḥa l-muʾminūn* — "indeed the believers have prospered". al-Biqāʿī presents this as a deliberate sequential *flḥ*-pickup.

### 3.2 Rules-tuple

`(no-tashkeel, full-text-verse-by-verse, surah-final-and-surah-initial-verses)`.

### 3.3 Test

From `quran-text/quran-no-tashkeel.json`:

- **Q 22:77** (the penultimate verse of al-Ḥajj): *يا أيها الذين آمنوا اركعوا واسجدوا واعبدوا ربكم وافعلوا الخير لعلكم تفلحون* — "O you who believe, bow and prostrate and serve your Lord and do good, that you may prosper"
- **Q 22:78** (last verse of al-Ḥajj): closes on jihād-fī-Allāh + *al-muslimīn* identity; the verse does not contain *flḥ*.
- **Q 23:1** opens: *قد أفلح المؤمنون* — "indeed the believers have prospered"

Q 22:77 has the **prospective imperfective** *tufliḥūn* (may prosper, conditional on action); Q 23:1 has the **performative perfective** *aflaḥa* (have prospered). This is a **completion-arc** from prospective at the end-block of Q 22 to perfective at the start of Q 23.

Empirical corpus-context: under the window-rule "last-2 verses of Sa contain *flḥ* AND first-2 verses of Sb contain *flḥ*", Q 22 → Q 23 is the **only** adjacent surah-pair in the mushaf with this *flḥ*-pickup. Verified by scanning all 113 adjacent surah-pairs.

### 3.4 Verdict: **VINDICATED**

al-Biqāʿī's *munāsabah* is empirically distinctive in the corpus. The Q 22→Q 23 transition is the **corpus-unique adjacent flḥ-pickup pair**.

Caveat: the underlying Q 22→Q 23 canonical-adjacency cost (per `h-new-720.json`) is high (rank 6 / 113, cost 0.2595) — meaning the root-distribution distance is large despite the *flḥ*-pickup. This is consistent with al-Biqāʿī's view that the *munāsabah* operates at the **theological-narrative** level (al-Khaṭṭābī meaning-iʿjāz lineage), not at the root-distribution level (al-Bāqillānī structural-iʿjāz lineage). The architecture-vs-meaning orthogonality of H-NEW-860 applies.

## Claim 4 — al-Ṭabarī: Q 23:1 was spoken by Jannat ʿAdn at its creation

### 4.1 Statement

al-Ṭabarī, *Jāmiʿ al-bayān* (file `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/23.json` ayah 1) cites three / four independent isnāds:

- Kaʿb b. al-Aḥbār via Maʿmar–Qatāda
- Mujāhid b. Jabr via Yaḥyā b. al-Ḍurays
- Abū al-ʿĀliya via Ḥafṣ b. ʿUmar → Abū Khaldah
- Maysara via Ibn Ḥumayd

All reporting that *qad aflaḥa al-muʾminūn* was spoken by the Garden of ʿAdn (or by Allāh upon planting ʿAdn) at the moment of its creation, before the surah was revealed.

### 4.2 Rules-tuple

This claim is **not empirically testable** at the present project's data-resolution: the proposition is about the metaphysical-cosmological priority of the verse, not about textual-corpus structure.

### 4.3 Test

Not-empirically-testable. We document the tradition as classical-attested via four independent isnāds in al-Ṭabarī.

The empirical adjacent fact that **the opening verse is verbatim spoken by an addressee** (a *performative-declarative* surah-opener, the only such case in the corpus — see 00-overview.md §3) is consistent with the qualitative-theological tradition al-Ṭabarī records: the verse is presented in the classical tradition as the **first** of God's utterances about His creation, prior to the rest of the surah.

### 4.4 Verdict: **NOT-EMPIRICALLY-TESTABLE — classical-attested, four-isnād**

Documented; not adjudicated. The tradition is classically widely-attested; isnād-criticism (e.g., Kaʿb b. al-Aḥbār is an *isrāʾīliyyāt* source) places mild reservations but the tradition is preserved by al-Ṭabarī, Ibn Kathīr, and al-Qurṭubī without retraction.

## Claim 5 — The Tirmidhī ʿUmar-narrated "ten verses to Paradise" — the believer-typology block extent

### 5.1 Statement

al-Tirmidhī, *Sunan*, idInBook 3257 (classical ḥadīth #3173; see 04-hadith-corpus.md §1):

> أُنْزِلَ عَلَىَّ عَشْرُ آيَاتٍ مَنْ أَقَامَهُنَّ دَخَلَ الْجَنَّةَ — ثُمَّ قَرَأَ: قَدْ أَفْلَحَ الْمُؤْمِنُونَ حَتَّى خَتَمَ عَشْرَ آيَاتٍ.

— "Ten Ayāt have been revealed to me; whoever upholds them will enter Paradise. Then he recited *qad aflaḥa l-muʾminūn* until he completed ten verses."

The ḥadīth fixes the scriptural unit at exactly **ten verses** (Q 23:1-10). Some classical mufassirūn extend the unit to v. 11 (*firdaws*-closure).

### 5.2 Rules-tuple

`(no-tashkeel, contiguous-verse-run, believer-attribute-marker = الذين هم / والذين هم, no-narrative-break, Hafs-Kufan)`.

### 5.3 Test (this is pre-registered as Q023-F-02; see `06-novel-findings.md` §2 and `csv/Q023-F-02.json`)

A corpus-wide scan for the **longest contiguous run of verses each containing the strict marker الذين هم / والذين هم** yields:

| Rank | Surah | Run length | Verses |
|:-:|:-:|:-:|:-:|
| 1 | **Q 23** | **4** | vv. 2-5 |
| 2 | Q 70 al-Maʿārij | 3 | vv. 32-34 |
| 3 | Q 107 al-Māʿūn | 2 | vv. 5-6 |

Q 23 has the **corpus-EXACT longest contiguous strict-marker run** (4 verses). Within the wider 10-verse Tirmidhī-defined block (Q 23:1-10), verses 1 and 10 are *qad aflaḥa l-muʾminūn* and *ulāʾika humu l-wārithūn* (the framing/closing); verses 2-5 are the consecutive *alladhīna hum [trait]* clauses (khushūʿ → laghw → zakāh → ḥifẓ-furūj); verses 6-7 are sub-clauses of trait 4 (ḥifẓ-furūj); verses 8-9 use the *alladhīna hum* + the *al-...* pattern for the final two traits (amāna and ṣalawāt).

The control-test (longest contiguous **disbeliever-attribute** block: *الذين كفروا* / *الذين كذبوا*) yields a corpus maximum of **2 verses** (Q 3:55-56, Q 4:101-102, Q 7:176-177). The believer-attribute block is therefore **2× longer than the corpus's longest disbeliever-attribute block**.

### 5.4 Verdict: **VINDICATED — corpus-EXACT**

The ʿUmar-narrated "ten verses" ḥadīth-defined unit is empirically distinctive: Q 23 contains the corpus's **longest** contiguous strict-believer-attribute relative-clause block (4 verses) within the broader 10-verse Tirmidhī-block. The block is structurally precise. Family-Bonferroni α = 0.05/3 = 0.0167; this corpus-EXACT finding is not p-test-based but rank-test-based.

## Honest limits

- The four claims audited above are all real classical claims with on-disk source attribution. The Q 23 classical literature is substantially richer than these four — al-Rāzī's full tafsir (e.g., on the deliberate ambiguity of the unnamed messenger of vv. 31-41), al-Qurṭubī's full discussion of the embryology verses, and al-Biqāʿī's full *Naẓm* survey of Q 23 — but those are richly covered in 03-tafsir-survey.md.
- Claim 4 (Jannat ʿAdn spoke v. 1) is intentionally flagged as not-empirically-testable; the project does not adjudicate theological-cosmological claims that lack textual-structural correlates.
- Claim 3 (the Q 22 → Q 23 flḥ-pickup) is corpus-unique in adjacent-pair terms; this is descriptive corpus-exact, not an inference about Q 22-Q 23 specifically being "designed" for this pickup.
- The Q023-F-02 marker definition is locked in the pre-reg (strict markers الذين هم / والذين هم). Under looser definitions (e.g., including bare الذين without the هم pronoun), Q 23 may not retain its rank-1 position; see Q023-F-02 looser-marker top-5 in the JSON output for full transparency.
