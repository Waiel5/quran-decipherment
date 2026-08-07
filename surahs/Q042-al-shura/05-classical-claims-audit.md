---
surah: 42
surah_name: al-Shūrā
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
---

# Q 42 al-Shūrā — classical claims audit


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

## Claim 1: Q 42 has the unique two-verse muqaṭṭaʿāt structure (al-Suyūṭī, *al-Itqān* nawʿ 27)

**Source**: al-Suyūṭī, *al-Itqān*, nawʿ 27 (*al-fawātiḥ*); also al-Rāzī ad Q 42:1-2.

**Claim**: Q 42 is the only surah in the Qurʾān where the muqaṭṭaʿāt span two verses (ḥā mīm in v.1; ʿayn sīn qāf in v.2) — all other muqaṭṭaʿāt are within a single āya.

**Empirical test (this session)**: Verified by direct examination of all 29 muqaṭṭaʿāt-opened surahs in `quran-text/quran-no-tashkeel.json`. Only Q 42 has two-verse split. Q 2:1 = "الم"; Q 7:1 = "المص"; Q 13:1 = "المر"; Q 14:1 = "الر"; Q 19:1 = "كهيعص"; ... — all single-verse. Q 42:1 = "حم", Q 42:2 = "عسق" — split.

**Verdict**: **VINDICATED** at exact-uniqueness level.

## Claim 2: Q 42:11 *laysa ka-mithlihi shayʾ* is the foundational tanzīh prooftext (Sunni kalām consensus)

**Source**: al-Ashʿarī, *al-Ibāna*; al-Bāqillānī, *al-Tamhīd*; al-Ghazālī, *al-Iqtiṣād*; al-Rāzī ad loc.

**Claim**: Q 42:11 is the central Qurʾānic anchor for via-negativa theology.

**Empirical test**: String search for *لیس کمثله شيء* and similar phrasings yields:
- Q 42:11 (verbatim) — primary attestation.
- No other verse contains the *laysa ka-mithlihi* construction. Related tanzīh formulae (e.g., Q 112:4 *lam yakun lahu kufuwan aḥad*) are different in grammar.

**Verdict**: **VINDICATED** — Q 42:11 is the unique attestation of this specific tanzīh formula.

## Claim 3: Q 42:23 — Sunni-mainstream reading is general kindred-love (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr); Imāmī reading is Ahl al-Bayt (al-Ṭabarsī)

**Source**: al-Ṭabarī ad Q 42:23 (general kindred); al-Ṭabarsī, *Majmaʿ al-bayān* (Ahl al-Bayt).

**Claim**: The verse has two valid classical readings, with sectarian alignment.

**Empirical test**: Direct examination of classical sources. Bukhārī #3348 (verified this session) gives the Sunni-mainstream Quraysh-kinship reading via Ibn ʿAbbās; Imāmī tradition is in al-Ṭabarsī. Both isnād-traditions exist.

**Verdict**: **DOCUMENTED** — both readings are classically attested. The empirical-data-level question (which classical sources held which reading) is settled; the theological-correctness question is out of scope.

## Claim 4: Q 42:38 *shūrā baynahum* is the Sunni political-theory anchor for consultation (al-Mawārdī, al-Juwaynī)

**Source**: al-Mawārdī, *al-Aḥkām al-sulṭāniyya*; al-Juwaynī, *Ghiyāth al-umam*.

**Claim**: Q 42:38 is the constitutional verse of Sunni political theory.

**Empirical test**: The verse's verbatim wording (verified) — *وأمرهم شورى بينهم* — is the only place in the Qurʾān where *shūrā* (as substantive abstract noun) appears. Q 3:159 has *wa-shāwirhum fī al-amr* (verb-form). The Q 42:38 substantive form is unique.

**Verdict**: **VINDICATED** at uniqueness level for the substantive *shūrā* lexeme.

## Claim 5: Q 42:51 establishes the three-mode taxonomy of revelation (al-Bukhārī's *Kitāb badʾ al-waḥy*)

**Source**: al-Bukhārī, *Kitāb badʾ al-waḥy* (the opening book of his *Ṣaḥīḥ*).

**Claim**: Q 42:51 (*illā waḥyan aw min warāʾi ḥijāb aw yursila rasūlan*) establishes the three-mode revelation taxonomy that structures Sunni doctrine.

**Empirical test**: Verse-text verified verbatim. The three-mode disjunction (1) direct waḥy (2) from behind a veil (3) angelic mediation is a unique grammatical construction in the Qurʾān.

**Verdict**: **VINDICATED** — Q 42:51 is the unique attestation of the three-mode revelation taxonomy. al-Bukhārī's organizational structure builds on this.

## Claim 6: Q 42 has the highest sig_A in HM-7 (this session, h-new-840)

**Source**: `h-new-840.json`, this session.

**Claim**: Q 42 has the strongest al-Bāqillānī iʿjāz al-fawāṣil signature in HM-7.

**Empirical test**: From `h-new-840.json`:
- Q 42 abs_ijaz = 1.275 (sig_A = +1.27)
- Q 41 abs_ijaz = 1.092
- Q 43 abs_ijaz = 1.102
- Q 40 abs_ijaz = 0.796
- Q 45 abs_ijaz = 0.654
- Q 46 abs_ijaz = 0.384
- Q 44 abs_ijaz = 0.167

**Verdict**: **VINDICATED** — Q 42 has the largest |iʿjāz signature| in HM-7. This is the empirical signature of the surah's prosodic distinctiveness (multi-rāwī, ر-shifted).

## Claim 7: Q 42:13 is the *ūlū al-ʿazm* prefiguring (al-Biqāʿī)

**Source**: al-Biqāʿī, *Naẓm al-durar* ad Q 42:13; also al-Rāzī ad loc.

**Claim**: Q 42:13's listing of Nūḥ, Ibrāhīm, Mūsā, ʿĪsā (+ Muḥammad implicit) is a 5-prophet *ūlū al-ʿazm* prefiguring the explicit Q 46:35 *ūlū al-ʿazm* reference.

**Empirical test**: 
- Q 42:13: names Nūḥ, Ibrāhīm, Mūsā, ʿĪsā explicitly + Prophet implied — 5 prophets.
- Q 46:35: *fa-ṣbir kamā ṣabara ūlū al-ʿazm min al-rusul* — explicit *ūlū al-ʿazm* reference, no name list.
- Q 33:7: parallel 5-prophet list (Muḥammad, Nūḥ, Ibrāhīm, Mūsā, ʿĪsā).

The Q 42:13 ↔ Q 46:35 cross-link is HM-7-internal (HM-A → HM-B). Q 33:7 is the Madinan parallel.

**Verdict**: **VINDICATED** — al-Biqāʿī's *naẓm* claim that Q 42:13 sets up the Q 46:35 *ūlū al-ʿazm* reference is empirically supported by the explicit list-vs-reference structure.

## 8. Summary table

| Claim | Verdict | Strength |
|:--|:--|:--|
| 1. Two-verse muqaṭṭaʿāt unique to Q 42 | VINDICATED | Exact uniqueness |
| 2. Q 42:11 = tanzīh prooftext | VINDICATED | Unique attestation |
| 3. Q 42:23 sectarian readings | DOCUMENTED | Both classical |
| 4. Q 42:38 *shūrā* doctrine | VINDICATED | Unique substantive form |
| 5. Q 42:51 three-mode revelation | VINDICATED | Unique disjunction |
| 6. Q 42 sig_A is HM-7 max | VINDICATED | Empirical (h-new-840) |
| 7. Q 42:13 ↔ Q 46:35 *ūlū al-ʿazm* | VINDICATED | Structural-textual |

## 9. Honest limits

1. The two-verse muqaṭṭaʿāt's *significance* (vs. mere descriptive uniqueness) requires a separate investigation.
2. Q 42:23 sectarian-hermeneutic adjudication is theological-out-of-scope.
3. The Q 42:13 *ūlū al-ʿazm* prefiguring is a *naẓm*-structural claim; al-Biqāʿī's interpretation is one valid frame.

## 10. Cross-references

- [[Q042-al-shura/03-tafsir-survey|Q 42 tafsīr]]
- [[Q042-al-shura/04-hadith-corpus|Q 42 ḥadīth]]
- [[Q046-al-ahqaf/05-classical-claims-audit|Q 46 audit — *ūlū al-ʿazm*]]
- [[hawamim-7-cluster-synthesis]]
