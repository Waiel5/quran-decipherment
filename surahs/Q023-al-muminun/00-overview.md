---
surah: 23
surah_name_ar: المؤمنون
surah_name_translit: al-Muʾminūn
surah_name_english: The Believers
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — all 8 template files + JOURNAL produced 2026-04-28
---

# Q 23 al-Muʾminūn — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 23 | canonical |
| Arabic name | المؤمنون | canonical |
| Transliteration | al-Muʾminūn | canonical |
| English meaning | "The Believers" | from the opening *qad aflaḥa al-muʾminūn* (v. 1) |
| Verse count | 118 | Hafs-Kufan; verified `quran-text/quran-no-tashkeel.json` |
| Position in mushaf | 23 | canonical |
| Type | Meccan | classical (no Medinan exception in al-Suyūṭī *Itqān*) |
| Position in revelation order | **74 / 114** | `data/revelation-order.csv` (Egyptian Standard + Nöldeke 64 / Middle Meccan) |
| Word count (no-tashkeel orthographic) | **1,089** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, no spaces) | **4,520** | computed |
| Opening | **قد أفلح المؤمنون** — "Indeed the believers have prospered" | meta-textual / performative-declarative |
| Bismala status | counted-only-in-Q1 (default rules-tuple) | per `INVESTIGATION-PROTOCOL.md` §1.4 |
| Length classification | mid-Meccan (al-mathānī, post-mufaṣṣal-ṭiwāl) | al-Suyūṭī *Itqān* nawʿ 18 |

## 2. Classical names

- **Sūrat al-Muʾminūn** (سورة المؤمنون) — "The Believers" (canonical, from v. 1).
- **Sūrat *qad aflaḥa* / Sūrat *qad aflaḥa al-muʾminūn*** (سورة قد أفلح / سورة قد أفلح المؤمنون) — by opening incipit; this is the form used in the Tirmidhī ʿUmar-narrated ḥadīth (`tirmidhi.json` entry idInBook=3257; common index #3173 in printed editions): «قد أفلح المؤمنون حتى ختم عشر آيات» (see `04-hadith-corpus.md`).
- **Sūrat al-Muʾminīn** (المؤمنين, genitive form) — used in al-Nasāʾī (`nasai.json` idInBook=1009) on the Conquest-day prayer where the Prophet recited this surah at the Kaʿba.

## 3. Opening formula

**Performative-declarative opening** — Q 23 opens with a ḳad-particle + perfect-tense verb (*qad aflaḥa*, "indeed they have prospered"), an extraordinarily rare pattern in Quranic openings.

Cross-corpus opening typology:
- **al-ḥamd-li-llāh** openings: Q 1, 6, 18, 34, 35.
- **sabbaḥa / yusabbiḥu** openings (musabbiḥāt): Q 57, 59, 61, 62, 64, 87.
- **muqaṭṭaʿāt** openings: 29 surahs.
- **qul** openings: Q 109, 112, 113, 114.
- **yā ayyuhā** openings: Q 33, 49, 65, 66, 73, 74.
- **direct narrative** openings: Q 12, 21, 24, 26, 27, 28, ... (most narrative-Meccan).
- **performative-declarative qad-perf** openings: **Q 23 alone** (*qad aflaḥa al-muʾminūn*).

Q 23's opening is unique: it is a **performative completion-statement** ("they have prospered" — an act already-realized for those who fulfill what follows). Classical scholars (al-Ṭabarī ad loc.) report a tradition that the Garden of ʿAdn was made to speak this verse upon its creation (al-Ṭabarī from Kaʿb b. al-Aḥbār via Maʿmar–Qatāda; from Mujāhid; from Abū al-ʿĀliya — three independent isnāds, see `03-tafsir-survey.md` §2.1).

## 4. Length classification

118 verses, 1,089 words. Position s = 23 places Q 23 in the **post-Q22-Ḥajj, pre-Q24-Nūr Meccan-narrative zone**. Length-class is mid-Meccan-narrative (mathānī tier, between mufaṣṣal-ṭiwāl and short Meccan). Compression-tail laws (kink at s = 50; [[h-new-660-compression-tail-gradient|H-NEW-660]]) are silent here by construction; Q 23 belongs to the pre-kink head zone.

## 5. Rhyme structure — corpus's extreme monorhyme

Final-letter distribution across 118 verses (no-tashkeel; see `01-empirical-profile.md` §5):

| Final letter | Count | Fraction |
|:--|:-:|:-:|
| ن (nūn) | 114 | **96.6%** |
| م (mīm) | 4 | 3.4% |

**Rhyme entropy (Shannon, nats): 0.148** — rank 109 / 114 (= 6th-purest monorhyme in the corpus). Q 23 is **the corpus's near-extreme monorhyme surah** by entropy: almost-monorhyme on **-ūn / -īn**.

The rhyme falls almost exclusively on the form-IV active-participle plural `mu-CCi-ūn / mu-CCi-īn` plus other plural-noun and plural-verb -ūn/-īn endings. This produces the **one-rhyme cantata** quality that Q 23 is famous for in classical recitation traditions.

**Cross-validation (full-tashkeel)**: 101 verses end in fatḥa (-a-) preceding nūn; 9 in kasra; 7 in tanwīn-kasra; 1 in tanwīn-ḍamma. The vowel before nūn is overwhelmingly fatḥa = **-ūna / -īna** rhyme.

## 6. Empirical architectural profile

See `01-empirical-profile.md`. Headline:
- **UAS rank**: **9 / 114** (top decile).
- **Outlier-strength Δ%ile**: **−10.91 pp** — `COHESION_ANCHOR` (i.e., removing Q 23 makes the [Q 20 – Q 26] window LESS cohesive, not more). Q 23 is mildly cohesion-positive.
- **iʿjāz signature sig_A**: **−1.55** (rank 93 / 114) — anti-structural-iʿjāz on the al-Bāqillānī axis (anti-correlation breaks because the rhyme is too pure: monorhyme reduces sig_A score).
- **iʿjāz sig_B (rhyme-purity / monorhyme)**: **−1.71** (rank 106 / 114) — extreme. Note: the project's sig_B convention treats z-positive rhyme-entropy as positive sig_B; Q 23's z = −1.13 of rhyme-entropy contributes negatively.
- **Q 22 → Q 23 canonical-adjacency cost**: **0.2595 length-units (rank 6 / 113 most expensive)** — see `h-new-720.json`.
- **Q 23 → Q 24 cost**: **0.2116 (rank 11 / 113)**. **Q 23 is one of only two surahs in the corpus with both adjacencies in the top-15 expensive** — the other being Q 24 itself. Q 23 acts as the *Meccan side* of the Q 24 (al-Nūr) Medinan-legal pivot.

## 7. Quick content structure (the "five movements" of Q 23)

I read Q 23 as a five-movement architecture, each marked by a rhetorical hinge:

- **Movement I — vv. 1-11 — The believer-typology block.** *qad aflaḥa al-muʾminūn* (v. 1) opens; ten character-traits (khushūʿ, iʿrāḍ-ʿan-laghw, zakāh, ḥifẓ-al-furūj, riʿāyat al-amāna, ḥifẓ al-ṣalawāt) close at v. 11 *humu al-wārithūn alladhīna yarithūna l-firdaws*. **The famous "ten verses" of the ʿUmar-Tirmidhī ḥadīth** (see `04-hadith-corpus.md` §1).
- **Movement II — vv. 12-22 — The creation/embryology + sustenance block.** *wa-laqad khalaqnā l-insāna min sulālatin min ṭīn* (v. 12) → *fa-tabāraka llāhu aḥsanu l-khāliqīn* (v. 14) → *anshaʾnā lakum bihi jannātin min nakhīlin wa-aʿnāb* (v. 19) → cattle-as-sign (v. 21) → ships (v. 22).
- **Movement III — vv. 23-54 — Prophet-cycle.** Three named messengers + one collective: Nūḥ (vv. 23-30) → "another generation" (vv. 31-41, traditionally Hūd or Ṣāliḥ) → "another generations" (vv. 42-44) → Mūsā/Hārūn before Pharaoh (vv. 45-49) → ʿĪsā / Maryam (v. 50) → universal address to the messengers (vv. 51-54).
- **Movement IV — vv. 55-77 — The wealth-test, the ḥisāb, and the sealing of unbelief.** *a-yaḥsabūna annamā numiddu-hum bihi min mālin wa-banīna nusāriʿu lahum fī l-khayrāt* (v. 55) → *a-fa-lā yatadabbarūna l-qawl* (v. 68) → *fa-dharhum fī ghamratihim ḥattā ḥīn* (v. 54 echo at v. 75).
- **Movement V — vv. 78-118 — Closing argument.** Sense-organs as evidence (v. 78), creation as proof (vv. 79-83), three rhetorical *qul* questions on lordship (vv. 84-89), eschatology + judgment (vv. 99-115), and the ring-closing inversion: *innahu lā yufliḥu l-kāfirūn* (v. 117) inverts the opening *qad aflaḥa l-muʾminūn* (v. 1). The surah closes (v. 118) with *wa-qul rabbi ighfir wa-irḥam wa-anta khayru l-rāḥimīn*.

The structural "spine" is therefore: **opening *aflaḥa* (v. 1) → middle *aflaḥa* (v. 102, *al-mufliḥūn*) → closing inverted *lā yufliḥu* (v. 117)**. This is a triple-anchor inclusio on the root *flḥ* — verified at v. 1, v. 102, v. 117 only (three flḥ-tokens, no others), see `06-novel-findings.md` Q023-F-03.

## 8. The opening *qad aflaḥa al-muʾminūn* — uniqueness

In the canonical mushaf, no other surah opens with this *qad + perfect-tense* construction declaring an already-completed state on behalf of a class of human agents. The closest cognates are:

- Q 87:14 *qad aflaḥa man tazakkā* — but this is a mid-surah verse, not an opening.
- Q 91:9 *qad aflaḥa man zakkāhā* — likewise a verse-internal locution.

Thus *qad aflaḥa al-muʾminūn* is **uniquely positioned as a surah-opener**, not as a recurring formulaic motif. al-Ṭabarsī (*Majmaʿ al-bayān*) and al-Rāzī (*Mafātīḥ al-ghayb*) both note this uniqueness.

## 9. The 10-believer-traits (Q 23:1-11) — cross-validated text

Per the protocol's anti-hallucination § 2.11, the canonical text of vv. 1-11 was extracted from `quran-text/quran-no-tashkeel.json` (and cross-validated against `quran-text/quran-min-tashkeel.json` and `quran-text/quran-full-tashkeel.json`). The 10 traits:

| Verse | Arabic (no-tashkeel) | Trait |
|:-:|:--|:--|
| 1 | قد أفلح المؤمنون | **performative declaration** — they have prospered |
| 2 | الذين هم في صلاتهم خاشعون | **trait 1**: khushūʿ in prayer |
| 3 | والذين هم عن اللغو معرضون | **trait 2**: turning away from idle-speech |
| 4 | والذين هم للزكاة فاعلون | **trait 3**: doing/giving zakāh |
| 5 | والذين هم لفروجهم حافظون | **trait 4**: guarding their private parts |
| 6 | إلا على أزواجهم أو ما ملكت أيمانهم فإنهم غير ملومين | **trait 4 (clause)**: exception — spouses / what their right hands possess |
| 7 | فمن ابتغى وراء ذلك فأولئك هم العادون | **trait 4 (closer)**: anyone seeking beyond this is a transgressor |
| 8 | والذين هم لأماناتهم وعهدهم راعون | **trait 5**: keeping trusts and covenants |
| 9 | والذين هم على صلواتهم يحافظون | **trait 6**: guarding their prayers |
| 10 | أولئك هم الوارثون | **closing**: those are the inheritors |
| 11 | الذين يرثون الفردوس هم فيها خالدون | **closing 2**: who inherit Firdaws, abiding therein eternally |

(Cross-validated against `quran-text/quran-min-tashkeel.json` index 22 verses 1-11 and `quran-text/quran-full-tashkeel.json` index 22 verses 1-11. All three variants yield identical orthographic-token boundaries; the only differences are tashkeel marks, sukūn, and shadda — none of which alter the trait-count or trait-content.)

**Note on counting**: Most classical mufassirūn count exactly 6 distinct trait-clauses (khushūʿ, iʿrāḍ-laghw, zakāh, ḥifẓ-furūj, riʿāyat-amāna, ḥifẓ-ṣalawāt). The Tirmidhī ʿUmar-narrated ḥadīth simply says *ʿashr āyāt* ("ten verses"), referring to the verse-count not the trait-count: vv. 1-10 inclusive of the framing v. 1 *qad aflaḥa* and the closing v. 10 *ulāʾika humu l-wārithūn*. Some recensions (al-Tha'labī *al-Kashf*) extend the unit to v. 11 *firdaws* for the trait-content closure. The empirical reading is that the believer-typology block is **vv. 1-11 inclusive** (the *firdaws*-closure verse v. 11 belongs to the typology semantically), but the ḥadīth-named scriptural unit is **vv. 1-10**.

## 10. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 23 Δ_outlier = −10.91 pp (`COHESION_ANCHOR`); 7-window [20,21,22,24,25,26].
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 22 → Q 23 cost rank 6/113 (3.13% TSP-residual); Q 23 → Q 24 cost rank 11/113 (2.55%); combined 5.68% of TSP residual on Q 23's two adjacencies.
- [[h-new-750-ijaz-signature|H-NEW-750]] — Q 23 sig_A = −1.55 (rank 93); sig_B = −1.71 (rank 106); rhyme entropy 0.148 nats.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 23 UAS = 2.977; rank 9 / 114; component breakdown: |outlier|=10.91, max_cost=0.260, |sig_A|=1.55.
- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 23 mean FR distance = 0.9665 (rank 74); nearest = Q 43 (0.789), farthest = Q 55 (1.183).
- [[Q024-al-nur/01-empirical-profile|Q 24 al-Nūr]] — Q 23-Q 24 boundary is the Meccan-Medinan register-class hinge (Q 24 is the only Medinan-legal surah inserted into the Meccan-narrative zone Q 21-27).
- [[Q002-al-baqara/00-overview|Q 2 al-Baqara]] — Q 23's *flḥ* inclusio (v. 1 / v. 117) parallels Q 2:5 *ulāʾika humu l-mufliḥūn* (the corpus's other major *flḥ*-success-formulation).

## 11. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md (5 audits)
- [x] 06-novel-findings.md (4 pre-registered tests)
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 4 pre-regs in `preregs/`
- [x] 4 scripts in `scripts/`
- [x] 4 JSON outputs in `csv/`
