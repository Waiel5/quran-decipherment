---
surah: 84
surah_name_ar: الإنشقاق
surah_name_translit: al-Inshiqāq
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 NOT-TESTABLE (legal sajda-ʿazāʾim split), 1 VINDICATED-as-singleton (corpus-EXACT k-d-ḥ)
---

# Q 84 al-Inshiqāq — Classical Claims Audit


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
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`; roots from QAC v0.4.

## Claim 1 — "al-Inshiqāq is Meccan, by consensus" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 84:1: *"makkiyya fī qawl al-jamīʿ"* (Meccan by
the statement of all). al-Zamakhsharī adds *"nazalat baʿd al-Infiṭār."*

**Test:** Cross-check `data/revelation-order.csv`.

**Result:** Q 84 → revelation-order **#83** (Tanzil Egyptian Standard), period **"Meccan"**, Nöldeke **#29,
"Early Meccan."** No Medinan-classification variant on disk.

**Verdict: VINDICATED.** Q 84 is Meccan in both the Egyptian-standard and Nöldeke chronologies; the
"by consensus" qualifier matches the absence of any dissenting classification on disk.

## Claim 2 — "It is twenty-five verses" (al-Qurṭubī); variant counts 23/24/25 (al-Suyūṭī)

**Claim:** al-Qurṭubī: *"wa-hiya khams wa-ʿishrūn āya"* (25 verses). al-Suyūṭī, *al-Itqān* (*ʿadad al-āy*):
*"al-Inshiqāq: ʿishrūn wa-thalāth, wa-qīla arbaʿ, wa-qīla khams"* (23 / 24 / 25 are all transmitted).

**Test:** Count verses in `quran-text/quran-no-tashkeel.json` (Q 84) and cross-check
`data/hafs-verse-counts.tsv`.

**Result:** **25** verses in the JSON; `hafs-verse-counts.tsv` line 84 = **25**.

**Verdict: VINDICATED.** The Hafs-Kūfan count is 25, the highest of the three transmitted counts. The
23/24/25 spread (al-Suyūṭī) reflects the Kūfan vs Baṣran/Madanī *fawāṣil* schools' different counting of
the short verses; the project adopts the Hafs-Kūfan 25 as canonical (00-overview).

## Claim 3 — al-Zamakhsharī's deleted-apodosis *iʿjāz* (the suspended *jawāb idhā*)

**Claim:** al-Zamakhsharī, *al-Kashshāf*, on Q 84:1-5: the apodosis of the *idhā…* cascade is deliberately
**deleted** — *"ḥudhifa jawābu idhā li-yadhhaba al-muqaddaru kulla madhhab — aw iktifāʾan bi-mā ʿulima fī
mithlihā min sūratay al-Takwīr wa-l-Infiṭār."* al-Rāzī catalogues multiple reconstructions of the missing
answer. The claim implies Q 84 belongs to a small cluster of surahs opening with a suspended *idhā*-cascade
(with al-Takwīr 81 and al-Infiṭār 82 the explicit siblings).

**Test (links H-NEW-1200 / H-NEW-2250):** (i) Is Q 84 a member of the *idhā*-cosmic-opener cluster
empirically? (ii) Does the *idhā*-cascade head concentrate in juzʾ-30, as H-NEW-2250 found?

**Result:**
- (i) H-NEW-1200 Sub-cluster A locks the *idhā*-cosmic-opener set {Q 56, 81, 82, 84, 99} as FR-cohesive;
  Q 84 is a member. (`01-empirical-profile.md` §1: Q 84's 5 nearest FR neighbors are all juzʾ-30 short
  surahs.)
- (ii) H-NEW-2250 found the *idhā*-cascade head concentrates in juzʾ-30 at **2.6×** (p=0.00010), peaking in
  the s=78-93 band that explicitly names al-Inshiqāq. Its **Limit 2** flags that the grammatical detector
  *fragments* Q 84's opening because vv 2/4 begin *wa*-VERB (*wa-adhinat*, *wa-alqat*) not *wa-idhā*.

**Verdict: VINDICATED (cluster-membership) with a documented grammatical caveat.** al-Zamakhsharī's
cross-reference of Q 84 to al-Takwīr + al-Infiṭār as suspended-*idhā* siblings is empirically grounded:
all three are in the FR-cohesive juzʾ-30 *idhā*-opener cluster and the cascade-head juzʾ-30 concentration
is significant (H-NEW-2250). The *iʿjāz*-of-deletion (the rhetorical force of the suppressed apodosis) is a
balāghī-aesthetic judgment, not a numerical claim; only the cluster-membership is empirically testable.

## Claim 4 (NOT-TESTABLE) — Is the Q 84:21 sajda among the *ʿazāʾim al-sujūd*? (Mālik vs Ibn al-ʿArabī)

**Claim:** al-Qurṭubī, on Q 84:21, records the legal split: **Mālik** held *"innahā laysat min ʿazāʾim
al-sujūd"* (al-Inshiqāq's prostration is NOT among the obligatory-prostration verses — reading *lā
yasjudūn* as "they do not yield/obey," not a literal prostration cue); **Ibn al-ʿArabī** held *"al-ṣaḥīḥ
annahā minhu"* (the sound view is that it IS among them), citing the Medinan transmission from Mālik and
the reinforcing Qurʾān + Sunna. al-Suyūṭī classes it with the *sujūd al-mufaṣṣal*.

**Test:** This is a *fiqh* question (whether a verse triggers an obligatory recitation-prostration), not a
structural-numerical claim about the text. The empirically-testable adjacent fact — that Q 84:21 carries
the sajda glyph (۩) in the canonical Hafs text and that the Abū Hurayra prostration tradition is
massively attested — is confirmed (Q084-F-01; 04-hadith-corpus §1, 20 verified reports).

**Verdict: NOT-TESTABLE (empirically) as a legal ruling; the underlying textual/ḥadīth facts are
VINDICATED.** The Mālik ↔ Ibn al-ʿArabī disagreement is a matter of *fiqh al-sujūd*, outside the project's
empirical-architectural instruments. What IS confirmed on disk: (a) the sajda glyph at 84:21, (b) the
Abū-Hurayra-traces-to-the-Prophet prostration tradition (Bukhārī #748 etc.), and (c) Q 84's corpus-UNIQUE
status as the only surah that is both an *idhā*-cosmic-opener AND a sajda-surah (Q084-F-01). Documented,
not adjudicated.

## Claim 5 — al-Ṭabarī's *wa-adhinat = samiʿat wa-aṭāʿat*, and the v 2 ≡ v 5 "non-repetition" (al-Zamakhsharī/al-Rāzī)

**Claim:** al-Ṭabarī (on v 2): *wa-adhinat li-rabbihā* = *"samiʿat … wa-aṭāʿat"* (the heaven heard and
obeyed). al-Zamakhsharī/al-Rāzī: the verbatim repetition of v 2 at v 5 is not *takrār* (mere repetition)
*"idhā ikhtalafa wajhu al-kalāmi lam yakun takrāran"* — v 2 attaches the obedience to the heaven, v 5 to
the earth.

**Test:** (i) Is *wa-adhinat li-rabbihā wa-ḥuqqat* literally identical at v 2 and v 5? (ii) Is the phrase
corpus-unique?

**Result:**
- (i) v 2 text = v 5 text = *وأذنت لربها وحقت* — **character-for-character identical** in the no-tashkeel
  JSON (verified on disk).
- (ii) The phrase occurs at **exactly Q 84:2 and Q 84:5 corpus-wide** — **NOWHERE else** (corpus scan of
  `quran-text/quran-no-tashkeel.json`).

**Verdict: VINDICATED (the verbatim identity + corpus-uniqueness of the phrase).** The *phrase* is a
Q 84-internal corpus-singleton. al-Zamakhsharī's "different aspect → not mere repetition" reading is a
balāghī interpretation of WHY it repeats (heaven vs earth), which the verse-context supports but which is
not itself a numerical claim. **Honest scope-correction:** the *phenomenon* of intra-surah verbatim refrains
is NOT rare (Q 55's *fa-biʾayyi ālāʾi rabbikumā* ×31, Q 77's *waylun yawmaʾidhin* ×10, Q 26 and Q 37 refrain
clusters, Q 56:13≡39 + 74≡96, Q 109:3≡5, etc.); Q 84's refrain is special as a *corpus-unique phrase*
deployed as a 2× bracket, not as the only intra-surah refrain (see 06, Q084-F-05 result).

## Claim 6 — Q 84:6's root k-d-ḥ is a corpus-anchor (al-Zamakhsharī/al-Rāzī *waḍʿ al-kalām iʿjāz*)

**Claim:** classical balāgha (al-Zamakhsharī *al-Kashshāf*, al-Rāzī *Mafātīḥ al-ghayb*) treat *innaka
kādiḥun ilā rabbika kadḥan* as an intensity-doubling *mafʿūl-muṭlaq* construction — the active participle
*kādiḥ* + verbal-noun *kadḥ* of the same root.

**Test (PRE-REGISTERED as Q084-F-02):** count corpus tokens of the root k-d-ḥ.

**Result:** Root k-d-ḥ appears in **exactly 1 verse corpus-wide (Q 84:6)**, with **2 surface forms**
(*kādiḥ*, *kadḥ*) — and NOWHERE else (`csv/Q084-F-02.json`). Both attested forms are in the single
*mafʿūl-muṭlaq* construction.

**Verdict: VINDICATED — corpus-SINGLETON.** Q 84:6 is the corpus-EXACT anchor verse for k-d-ḥ. The
classical *intensity-doubling* reading is descriptively grounded, and the empirical addition is stronger
than the classical claim: the root occurs in NO other verse, so Q 84:6 is not merely an intense use of a
common root — it is the *sole* corpus locus of the root. (Q084-F-02; see 06.)

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Meccan by consensus | al-Qurṭubī | **VINDICATED** |
| 2 | 25 verses (23/24/25 variants) | al-Qurṭubī / al-Suyūṭī | **VINDICATED** |
| 3 | deleted-apodosis *iʿjāz* / *idhā*-sibling cluster | al-Zamakhsharī / al-Rāzī | **VINDICATED** (cluster) + caveat |
| 4 | v 21 sajda ∈ *ʿazāʾim*? | al-Qurṭubī (Mālik vs Ibn al-ʿArabī) | NOT-TESTABLE (legal); textual facts VINDICATED |
| 5 | *adhinat*=heard+obeyed; v2≡v5 non-repetition | al-Ṭabarī / al-Zamakhsharī | **VINDICATED** (phrase corpus-singleton) + scope-correction |
| 6 | k-d-ḥ corpus-anchor (intensity-doubling) | al-Zamakhsharī / al-Rāzī | **VINDICATED — corpus-SINGLETON** (Q084-F-02) |

## Honest limits

- Claim 3's *iʿjāz*-of-deletion is a balāghī-aesthetic judgment; only the *idhā*-cluster-membership and the
  juzʾ-30 cascade concentration (H-NEW-1200/2250) are empirically testable, and H-NEW-2250 Limit 2 documents
  that the grammatical detector fragments Q 84's opening (vv 2/4 are *wa*-VERB, not *wa-idhā*).
- Claim 4 is deliberately left NOT-TESTABLE: the *fiqh* of *ʿazāʾim al-sujūd* is outside scope; only the
  glyph-presence and ḥadīth-attestation are confirmed.
- Claim 5's corpus-uniqueness is on the no-tashkeel orthographic-token level (under full-tashkeel the two
  verses are also identical, no internal-vowel divergence); the scope-correction (intra-surah refrains are
  common as a phenomenon) is the load-bearing honesty caveat against over-claiming.

---

*All testable claims pre-registered before computation (Q084-F-01, F-02, F-03) or deterministic. 2026-05-30.*
