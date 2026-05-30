---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 7 claims audited — 4 VINDICATED, 1 VINDICATED-as-orthographic-fact (Q094-F-01 Arm C), 2 NOT-TESTABLE
---

# Q 94 al-Sharḥ — Classical Claims Audit

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`; empirical values cited to the
on-disk artifacts via `01-empirical-profile.md`.

## Claim 1 — "Sūrat A-lam Nashraḥ is Meccan, by consensus" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 94:1: *"makkiyya fī qawl al-jamīʿ"* (Meccan by
all accounts).

**Test:** cross-check `data/revelation-order.csv` (Tanzil Egyptian Standard + Nöldeke).

**Result:** Q 94 (mushaf_order 94) → revelation-order **#12**, period **Meccan**, Nöldeke **#12**, phase
**Early Meccan**. No Medinan-classification variant on disk.

**Verdict: VINDICATED.** Q 94 is Early-Meccan in both the Egyptian-standard and Nöldeke chronologies on
disk; al-Qurṭubī's "by consensus" holds against the on-disk record.

## Claim 2 — "It is eight verses" (al-Qurṭubī)

**Claim:** al-Qurṭubī: *"wa-hiya thamānī āyāt"* (it is eight verses).

**Test:** count verses in `quran-text/quran-no-tashkeel.json` (Q 94); cross-check `data/hafs-verse-counts.tsv`.

**Result:** 8 verses in the JSON; `hafs-verse-counts.tsv` line 94 = `94<TAB>8`.

**Verdict: VINDICATED.** 8 verses, Hafs-Kūfan. (No variant verse-count tradition for Q 94 is on disk — the
surah is below the threshold where the Kūfan/Baṣran/Madanī counting schools diverge.)

## Claim 3 — al-Qurṭubī: *a-lam nashraḥ* = *qad sharaḥnā* (the rhetorical-negative reads as affirmation)

**Claim:** al-Qurṭubī, on Q 94:1: the *lam* of *a-lam nashraḥ* is a *jaḥd*, and a *jaḥd* inside an
*istifhām* "returns to affirmation" (*rajaʿa ilā al-taḥqīq*); his syntactic proof is that the coordinated
v 2 verb is the **perfect** *wa-waḍaʿnā* ("and We removed"), not the jussive *wa-naḍaʿ* — *"law kāna ʿalā
al-tanzīl la-qāla wa-naḍaʿ"* — so the surface negative-interrogative is read as a completed affirmation.
al-Zamakhsharī agrees (the *istifhām inkārī* affirms the sharḥ).

**Test:** does the text bear out the perfect-tense coordination al-Qurṭubī's argument rests on?

**Result:** Q 94:1-4 in `quran-no-tashkeel.json`: v 1 *ألم نشرح* (jussive *nashraḥ* under *lam*); v 2
*ووضعنا* (perfect *waḍaʿnā*); v 4 *ورفعنا* (perfect *rafaʿnā*). The coordinated verbs **are** perfect, not
jussive — exactly the morphological fact al-Qurṭubī adduces.

**Verdict: VINDICATED (orthographic/morphological fact).** The affirmative-reading of *a-lam nashraḥ* has
an exact textual basis: the coordinated favors (vv 2, 4) are in the **perfect** tense, so the opening
rhetorical-negative is grammatically completed as a past affirmation, as al-Qurṭubī states. (The
*semantic* "this is affirmation" inference is the standard *istifhām taqrīrī* reading; what is verified
here is the morphological substrate.)

## Claim 4 — al-Qurṭubī: v 6's dropped fāʾ marks an independent *ibtidāʾ* (a "second, distinct ease")

**Claim:** al-Qurṭubī, on Q 94:5: the second assurance (v 6, *inna maʿa al-ʿusri yusrā*) is a fresh
*ibtidāʾ* (independent restart), not a coordinated continuation, and the **syntactic proof of the fresh
start is its being stripped of a connective**: *"al-dalīl ʿalā ibtidāʾihi taʿarrīhi min fāʾ aw wāw aw
ghayrihā min ḥurūf al-nasaq"* ("the proof of its being a new beginning is its bareness of fāʾ, wāw, or any
other coordinating particle"). v 5, by contrast, opens with a connective fāʾ (*fa-inna*).

**Test (PRE-REGISTERED as Q094-F-01, Arms A & B):** is the single-leading-connective delta between v 5 and
v 6 a real, corpus-distinctive textual fact?

**Result (from `csv/Q094-F-01.json`, pre-reg SHA `2dd9380…f71d2a`, runtime-verified):**
- v 5 = `فإن مع العسر يسرا` (opens *fa-inna*); v 6 = `إن مع العسر يسرا` (opens *inna*, no connective) —
  character edit distance **= 1** (the leading fāʾ).
- **Arm A CONFIRMED:** Q 94:5-6 is the **UNIQUE** adjacent same-surah verse pair in the entire corpus
  that is token-identical except for a single leading fāʾ/wāw on one token (count = 1, = Q 94:5-6),
  under both the token-level and whole-string operationalizations.
- **Arm B CONFIRMED:** Q 94:5-6 achieves the **global minimum** character edit distance (1) over all 5,821
  substantive (≥3-word) adjacent same-surah pairs (rank 1 of 5,821); the corpus contains **0**
  exact-verbatim adjacent pairs; the observed edit-1 is extreme vs a length-matched permutation null
  (null mean edit 12.83; p_perm 0.0003 seed 20260509, replicated 0.0001 seed 20260530).

**Verdict: VINDICATED — corpus-SINGLETON.** al-Qurṭubī's grammatical observation — that the **absence of
the connective** in v 6 is the structural marker distinguishing it from v 5 — corresponds to an exact,
**corpus-unique** orthographic fact: Q 94:5-6 is the single tightest near-verbatim adjacency in the Quran,
and the *one and only* feature distinguishing the two verses is precisely the leading fāʾ al-Qurṭubī
points to. The classical *ibtidāʾ*-vs-*nasaq* reading rests on a textual datum that is not merely present
but corpus-singular. (The *theological* "second, distinct ease" inference al-Qurṭubī draws from this is
out of scope; only the syntactic delta is verified — full detail in `06-novel-findings.md`.)

## Claim 5 — the definite-ʿusr / indefinite-yusr "two-eases" grammar (Thaʿlab; Ibn ʿAbbās; Ibn Kathīr)

**Claim:** Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, on Q 94:5-6: *"al-ʿusru muʿarraf fī al-ḥālayn fa-huwa
mufrad, wa-l-yusru munakkar fa-taʿaddad … fa-l-ʿusru al-awwalu ʿaynu al-thānī wa-l-yusru taʿaddad"* (the
hardship is definite in both states, hence one; the ease is indefinite, hence multiplied). Thaʿlab (via
al-Qurṭubī): a repeated definite is the same referent, a repeated indefinite is a different one. The
underlying *athar*: *"lan yaghliba ʿusrun yusrayn."*

**Test (PRE-REGISTERED as Q094-F-01, Arm C):** is the definite/indefinite asymmetry an exact orthographic
fact in the no-tashkeel text?

**Result (from `csv/Q094-F-01.json`):** *العسر* (definite, الـ) appears in **both** v 5 and v 6; *يسرا*
(indefinite accusative, no article, alif-tanwīn spelling) appears in **both** v 5 and v 6; the v5/v6
root-Jaccard is **exactly 1.0** (identical root-set {ʿ-s-r = `Esr`, y-s-r = `ysr`}), i.e. the same
proposition is reprised. Arm C **CONFIRMED**.

**Verdict: VINDICATED — orthographic asymmetry present.** The grammatical substrate of the two-eases
reading (definite *al-ʿusr* repeated identically; indefinite *yusran* repeated) is a genuine textual fact,
not an interpretive imposition. **Important scope note:** this VINDICATES the *grammatical observation*
(the asymmetry exists), **not** the *theological* "two eases" claim itself, which is out of empirical scope
(Protocol §10), and **not** any single reading over the rival *taʾkīd* (al-Farrāʾ) reading. Indeed
al-Jurjānī's preserved objection (al-Qurṭubī: the two-eases logic would force *inna maʿa al-fārisi sayfan,
inna maʿa al-fārisi sayfan* = one rider, two swords) shows the inference is contested **within** the
tradition; the audit verifies only the asymmetry on which both Thaʿlab's reading and al-Jurjānī's
counter-argument operate.

## Claim 6 — al-Rāzī/classical: al-Ḍuḥā (Q 93) → al-Sharḥ (Q 94) is a consolation *pair*

**Claim:** the classical *munāsaba* tradition treats Q 93 al-Ḍuḥā and Q 94 al-Sharḥ as a paired
consolation-diptych addressed to the Prophet (the *waddaʿaka* / *a-lam* solace pair), sharing the
second-person *rabbuka* address; some authorities recited them as a single unit (and the Meccan
recitation tradition begins the takbīr from the end of al-Ḍuḥā). (Reflected in al-Qurṭubī's framing and
the standard munāsabah literature; the single-unit recitation point is a *qirāʾāt* tradition.)

**Test:** does the Q 93 → Q 94 mushaf seam have an empirical smoothness correlate, and are the two surahs
content-near in FR space? Read `h-new-720.json` (per-adjacency) and `h-new-111.json` (FR matrix).

**Result (from `01-empirical-profile.md`, traced to JSON):**
- Q 93 → Q 94 seam: delta_raw **−0.0152**, ascending-rank **10/113** — a negative-delta **seamless** joint
  (one of the smoothest in the mushaf; the immediately preceding Q 91 → Q 92 is the corpus's single
  cheapest seam, −0.0868, so Q 91→92→93→94 is an unusually smooth stretch).
- Q 93 is the **rank-16 / 113** FR-nearest surah to Q 94 (FR 0.3641) — a top-16 neighbor.
- Chronology: Q 93 al-Ḍuḥā = revelation **#11**, Q 94 al-Sharḥ = revelation **#12** — the two are
  *immediately consecutive in revelation order* AND *immediately consecutive in the mushaf* (a rare
  double-adjacency among Early-Meccan surahs).

**Verdict: VINDICATED.** The classical consolation-pair reading has a direct quantitative correlate: the
Q 93 → Q 94 transition is the rank-10 smoothest seam in the corpus on the TSP-residual instrument, Q 93 is
a top-16 FR neighbor of Q 94, and the two surahs are consecutive in both mushaf and revelation order. The
paired-unit intuition is empirically grounded at the seam/FR level. (Corroborates H-NEW-2280
munāsabah-seam.)

## Claim 7 — the *lan yaghliba ʿusrun yusrayn* report is a sound prophetic ḥadīth

**Claim:** the report is widely cited as a prophetic ḥadīth (al-Ṭabarī, Ibn Kathīr present it as marfūʿ:
"the Prophet came out laughing and said *lan yaghliba ʿusrun yusrayn*").

**Test:** isnād status — a 9-book on-disk search.

**Result:** a diacritics-stripped search across all 9 books returns **no marfūʿ ḥadīth** of the phrase
connected to the Prophet through a Companion isnād. The only 9-book attestation is **Mālik Muwaṭṭaʾ #1007**
(Book of Jihād), where it is **ʿUmar b. al-Khaṭṭāb's mawqūf statement** in his letter to Abū ʿUbayda b.
al-Jarrāḥ. In the tafsīr literature the marfūʿ form is preserved as a **mursal** from al-Ḥasan al-Baṣrī
(al-Ṭabarī, Ibn Kathīr explicitly: *"mursalan"*).

**Verdict: NOT-TESTABLE empirically (and FLAGGED for accuracy).** Isnād-soundness is a *riwāya*/hadith-
criticism question, outside the project's empirical-architectural instruments. What the on-disk record
*does* establish is a correction of common usage: in the 9-book corpus the phrase is an **athar of ʿUmar**
(mawqūf, via Mālik ← Zayd b. Aslam), and the prophetic attribution survives only as a **mursal** in the
tafsīr chains, not as a connected ḥadīth. Documented, not adjudicated (see `04-hadith-corpus.md`).

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Meccan by consensus | al-Qurṭubī | **VINDICATED** |
| 2 | 8 verses | al-Qurṭubī | **VINDICATED** |
| 3 | *a-lam nashraḥ* = affirmation (perfect coordination) | al-Qurṭubī / al-Zamakhsharī | **VINDICATED** (morphological) |
| 4 | v 6 dropped-fāʾ = *ibtidāʾ* | al-Qurṭubī | **VINDICATED — corpus-SINGLETON** (Q094-F-01 A+B) |
| 5 | definite-ʿusr / indefinite-yusr "two-eases" grammar | Thaʿlab / Ibn ʿAbbās / Ibn Kathīr | **VINDICATED — orthographic asymmetry** (Q094-F-01 C); theology out-of-scope |
| 6 | Q 93→Q 94 consolation-pair | al-Rāzī / munāsabah tradition | **VINDICATED** (seam rank 10/113; FR rank 16; consecutive revelation) |
| 7 | *lan yaghliba ʿusrun yusrayn* is a sound prophetic ḥadīth | al-Ṭabarī / Ibn Kathīr | **NOT-TESTABLE** (mawqūf in 9 books; mursal in tafsīr) |

## Honest limits

- Claims 4-5's verdicts rest on the no-tashkeel orthographic text and the QAC root-index; they are
  deterministic and fully replicable, but they verify the *grammatical substrate*, not the theological
  inferences the tradition draws from it (those are out of scope per Protocol §10).
- Claim 6's seam-smoothness is on the TSP-residual instrument (`h-new-720.json`); the consolation-pair is
  *also* supported by content (FR rank 16) and chronology (consecutive revelation), so the correlate is
  multi-instrument, but the "single-unit recitation" point itself is a *qirāʾāt* tradition not directly
  testable here.
- Claim 7's "not-testable" applies only to isnād-soundness; the *distributional* fact (phrase present as
  ʿUmar's mawqūf, marfūʿ only as mursal) IS established from disk.
- Verse-count variant traditions for Q 94 are not on disk; the 8-verse Hafs count is treated as canonical.

---

*All testable claims pre-registered before computation (Q094-F-01) or deterministic. 2026-05-30.*
