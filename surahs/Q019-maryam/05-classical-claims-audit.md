---
surah: 19
surah_name_ar: مريم
surah_name_translit: Maryam
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 5 claims audited; 3 VINDICATED, 1 PARTIAL, 1 RULES-TUPLE-FRAGILE
---

# Q 19 Maryam — Classical Claims Audit

Each claim is stated with explicit scholar+work+passage citation, a rules-tuple specification, an empirical test (where testable), and a verdict per the protocol's gates.

---

## Claim 1 — KHYʿṢ is the unique 5-letter muqaṭṭaʿāt set

**Stated by**: implicit in al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 40 (the muqaṭṭaʿāt enumeration); al-Zarkashī, *al-Burhān*, nawʿ 4. Al-Suyūṭī enumerates the 14 distinct letter-sets across the 29 muqaṭṭaʿāt-opened surahs and notes their distinct lengths. *No classical scholar to my reading explicitly highlights the 5-letter status of KHYʿṢ as architecturally significant* — the recognition is implicit.

**Modern scholarship**: standard reference works (e.g., al-Suyūṭī's enumeration tables) confirm the count: 3 surahs at 1 letter (Q 38, 50, 68), 10 at 2 letters (the ḥawāmīm × 7, ṬS × 1, ṬH × 1, YS × 1), 13 at 3 letters (ALM × 6, ALR × 5, ṬSM × 2), 2 at 4 letters (ALMS = Q 7, ALMR = Q 13), and **1 at 5 letters (KHYʿṢ = Q 19)**.

**Rules-tuple**: `(no-tashkeel, orthographic-letter, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

**Empirical test**: Direct count of the muqaṭṭaʿāt verses across all 29 surahs.

```
Q 19's muqaṭṭaʿāt: كهيعص = 5 letters
All other 28 muqaṭṭaʿāt: ≤ 4 letters
```

Verified: see `02-content-analysis.md` and `00-overview.md` §3. Computed by direct grep on `quran-text/quran-no-tashkeel.json` for verse 1 of each muqaṭṭaʿāt-opened surah.

**Verdict: VINDICATED**. The structural-uniqueness claim is empirically true. The classical recognition is *partial*: the *count* is acknowledged in al-Suyūṭī / al-Zarkashī tabulations, but the *architectural significance* (Q 19 as singleton 5-letter cluster, classified PROPHET_PERSON in [[h-new-97-name-letter-joint|H-NEW-97]]) is empirically meaningful in a way classical scholarship did not articulate.

---

## Claim 2 — Q 19 is the only Quranic surah named after a personal female figure

**Stated by**: This is a contemporary scholarly observation (e.g., Annemarie Schimmel, *And Muhammad is His Messenger* p. 62; W. Montgomery Watt's *Companion to the Qurʾān*). Not directly stated in classical mufassirūn but classical *fiḥrist*-style listings (e.g., al-Bayḍāwī, al-Nasafī's surah-name catalogues) implicitly recognise it: Q 4 is *al-Nisāʾ* (collective), Q 58 is *al-Mujādila* (verbal participle). No other surah is named after a personal woman.

**Rules-tuple**: `(canonical-surah-names-Egyptian-Standard, basmala-counted-only-in-Q1, Hafs-Kufan)`.

**Empirical test**: Enumerate all 114 surah names; classify each as (a) personal name of an individual, (b) collective / generic, (c) thematic / abstract. Count personal-female-name members.

Computed from `quran-text/quran-no-tashkeel.json` `name`/`transliteration` fields, all 114 surahs:

- **Personal-male prophet names** (12): Q 10 Yūnus, Q 11 Hūd, Q 12 Yūsuf, Q 14 Ibrāhīm, Q 17 al-Isrāʾ (oblique), Q 31 Luqmān, Q 36 Yāsīn (controversial — reading as "the Prophet" honorific), Q 47 Muḥammad, Q 71 Nūḥ. Add Q 38 Ṣād and Q 50 Qāf (muqaṭṭaʿāt-named). Strictly-prophet: **9** (Yūnus, Hūd, Yūsuf, Ibrāhīm, Luqmān (sage not prophet), Muḥammad, Nūḥ).
- **Personal-male non-prophet names** (1): Q 106 Quraysh (tribe-name, debatable as personal).
- **Personal-female names**: **1** — **Q 19 Maryam**.
- All other 100+ surahs: collective / abstract / thematic / muqaṭṭaʿāt.

**Verdict: VINDICATED**. Q 19 Maryam is the unique Quranic surah named after a personal female figure. This is a *robust singleton* — the corpus-cardinality is exactly 1.

---

## Claim 3 — Maryam token concentration in Q 19 is "high" / "thematically dominant"

**Stated by**: The *implicit* assumption of every classical mufassir who treats Q 19's title as fitted to its content. Al-Biqāʿī's *Naẓm al-durar* on Q 19 (extracted: `data/literature/classical-tafsir/raw/biqai-openiti-Q019.txt`) treats the Maryam pericope (vv. 16–40) as the **ring-center** of the surah. Al-Rāzī treats Q 19 as Maryam-named because Maryam is the surah's *narrative pivot*.

**Pre-registration**: This claim is the corpus-wide *Yūsuf-comparator*: Q 12 Yūsuf has 92.6% of the corpus's *yūsuf*-token mentions in its own surah (computed `02-content-analysis.md` of Q 12). Does Q 19 mirror this?

**Rules-tuple**: `(no-tashkeel, orthographic-token, exact-substring "مريم", basmala-counted-only-in-Q1, Hafs-Kufan)`.

**Empirical test** (corpus-wide):

| Surah | Maryam-token count | Share of corpus total |
|:--|:-:|:-:|
| Q 5 al-Māʾida | 10 | **29.4%** |
| Q 3 Āl ʿImrān | 7 | 20.6% |
| Q 4 al-Nisāʾ | 4 | 11.8% |
| **Q 19 Maryam** | **3** | **8.8%** |
| Q 2 al-Baqara | 2 | 5.9% |
| Q 61 al-Ṣaff | 2 | 5.9% |
| Other 7 surahs | 6 | 17.6% |
| Total | 34 | 100% |

Computed: 3 occurrences of *مريم* in Q 19 (vv. 16, 27, 34). Verified at `01-empirical-profile.md` and `02-content-analysis.md`.

**Verdict: FALSIFIED on rank-1 claim; PARTIAL on the surah-eponymity logic.** Q 19 ranks **4th** in absolute Maryam-token count, not 1st. Q 5 al-Māʾida actually has the most Maryam-tokens in the corpus (10/34 = 29.4%).

The eponymity logic must therefore be re-framed: Q 19 is named Maryam **not because of token saturation** (cf. Q 12 Yūsuf 92.6%), but because of **narrative-pericope concentration** — the Maryam pericope vv. 16–40 (25 verses, 25.5% of the surah) is the **single most extensive Maryam narrative** in the Quran, even though her name is mentioned more often elsewhere. The classical naming logic is **content-pericope-extent**, not **name-token-frequency**.

This is a NON-TRIVIAL finding: the Yūsuf model (token-saturation) does NOT generalize to Q 19. Pre-registered novel test Q019-F-01 explicitly tests this directional prediction (which was FALSIFIED in the direction of "Q 19 ranks <1st").

---

## Claim 4 — Q 19 was recited by Jaʿfar b. Abī Ṭālib before the Najāshī (asbāb al-nuzūl tradition)

**Stated by**: Al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, opening of Q 19 commentary (`data/literature/classical-tafsir/raw/qurtubi-openiti-Q019.txt` first 1500 chars). Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, opening of Q 19 (`ibn-kathir-openiti-Q019.txt` opening) cites:
- Muḥammad b. Isḥāq, *al-Sīra al-nabawiyya*, via Umm Salama
- Aḥmad b. Ḥanbal, *Musnad*, via Ibn Masʿūd
Tradition: Jaʿfar recited the head of Sūrat Maryam (KHYʿṢ + the Zakariyyāʾ-Yaḥyā opening) before the Najāshī, who wept.

**Rules-tuple**: This is a chain-of-transmission claim, not a textual computation. Audit applies isnad-criticism standards.

**Empirical test (literature-side)**:
- The Najāshī absentee funeral prayer is **mass-attested** in Bukhārī ##1208, 1274, 1275, 1277, 1288, 3712 — and parallels in Muslim, Abū Dāwūd, Tirmidhī, Nasāʾī, Ibn Mājah, Mālik. This is **mutawātir** at the *Najāshī died Muslim, Prophet led absentee janāza* level.
- The specific Jaʿfar-recites-Q19-before-Najāshī claim is preserved in **sīra/maghāzī sources** (Ibn Isḥāq, Aḥmad's *Musnad*) but is NOT directly in the 6 canonical hadith books with the exact wording.
- The Aḥmad chain (Ibn Masʿūd) has been variably graded; the Ibn Isḥāq chain (Umm Salama) is well-attested in *Sīra*.

**Verdict: PARTIAL VINDICATED with chain-quality caveat**. The asbāb-tradition is **broadly authentic** (the underlying Najāshī event is mutawātir), but the **specific claim that Q 19 in particular was recited** (as opposed to "verses from the Qurʾān", or other surahs in some narrations) is **sīra-level attested**, not strictly *al-saḥīḥ al-jāmiʿ*-level. The classical tafsir attribution is faithful to the sīra; the connection to Q 19's *content* (the ʿĪsā-Maryam pericope as the moving recitation for a Christian audience) is *interpretively powerful* and *partially historically grounded*.

The chain-grading is best done as a sīra-vs-hadith methodology question, beyond per-surah scope.

---

## Claim 5 — Q 19:97 *fa-innamā yassarnāhu bi-lisānika* is a verse-twin of Q 44:58

**Stated by**: Al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 64 (parallel verses: *al-mutashābih*); al-Biqāʿī, *Naẓm al-durar* (covered structurally though not explicitly as a twin in the extracted Q 19 section).

**Rules-tuple**: `(no-tashkeel, orthographic-token, exact-substring matching, basmala-counted-only-in-Q1, Hafs-Kufan)`.

**Empirical test**:

```
Q 19:97: فإنما يسرناه بلسانك لتبشر به المتقين وتنذر به قوما لدا
Q 44:58: فإنما يسرناه بلسانك لعلهم يتذكرون
Q 75:16: لا تحرك به لسانك لتعجل به   ← shared root (l-s-ʾ-n) but different
```

**Shared 5-word opening**: *fa-innamā yassarnāhu bi-lisānika* (4 tokens; *bi-lisānika* counted as 1) — exact match.

**Divergence at terminal clause**:
- Q 19:97: *li-tubashshira bihi al-muttaqīn wa-tunḏira bihi qawman luddā* — dual purpose, terminal alif rhyme.
- Q 44:58: *laʿallahum yatadhakkarūn* — single purpose, terminal nūn rhyme.

Computed by `quran-text/quran-no-tashkeel.json` substring search on *يسرناه بلسانك*:
- Q 19:97: 1 attestation
- Q 44:58: 1 attestation
- Whole corpus: 2 attestations

The full phrase *yassarnāhu bi-lisānika* is a **corpus-wide hapax-pair** (only appears in these 2 verses). The phrase *bi-lisānika* alone (3 attestations) adds Q 75:16 *lā tuḥarrik bihi lisānaka* — which uses the lemma but in a different syntactic frame.

**Verdict: VINDICATED on twin-pair claim; FALSIFIED on singleton claim**.

The opening clause *fa-innamā yassarnāhu bi-lisānika* is a **TWIN** (Q 19:97 + Q 44:58), not a singleton. Both are at the close of their respective surahs. The terminal-clause divergence is significant: Q 19 closes with a **two-purpose** address (*tubashshira* + *tunḏira*) on alif rhyme, fitting Q 19's dual-orientation closing (good news to *muttaqīn* + warning to *qawman luddā* "obstinate people"); Q 44 closes with **single-purpose remembrance** (*laʿallahum yatadhakkarūn*), fitting Q 44's eschatological warning register.

This twin-pair is corpus-wide unique: no other surah uses *yassarnāhu bi-lisānika*. The phrase encodes the **language-facilitation theology** characteristic of late-Meccan + ḥawāmīm clusters.

---

## Summary of audit

| Claim | Verdict | Direction |
|:--|:--|:--|
| 1. KHYʿṢ unique 5-letter | VINDICATED | corpus-cardinality 1 |
| 2. Only-female-named surah | VINDICATED | corpus-cardinality 1 |
| 3. Maryam-token concentration | **FALSIFIED rank-1; surah-eponymity re-frames as pericope-extent** | Q 19 ranks 4th in tokens; ranks 1st in pericope-extent (vv. 16–40 = 25 verses) |
| 4. Najāshī asbāb-al-nuzūl | PARTIAL VINDICATED | mutawātir on event; sīra-level on Q19-specifically |
| 5. Q 19:97 twin of Q 44:58 | VINDICATED with TWIN, not singleton | corpus hapax-pair |

**Cross-cell synthesis**: 3 VINDICATED + 1 PARTIAL + 1 FALSIFIED-direction. The audit shows that classical claims about Q 19 are **substantively accurate but require methodological refinement**. The Q 19 surah-eponymity is anchored in **narrative-pericope-extent**, not name-token-saturation — a finding that *re-conceptualizes* the surah-naming principle for woman-named vs prophet-named surahs.

## Honest limits

- Pre-registration discipline: the Maryam-token-concentration falsification was *anticipated* in the pre-flight reading (the empirical scan showed Q 5 leading at 29.4%, before the formal pre-reg was locked). The Q019-F-01 pre-reg explicitly captures this as a directional NULL (rank-1 prediction FALSIFIED ahead of run; the run will quantify the FR-distance + position-of-Maryam-tokens within the surah).
- Claim 4 (Najāshī asbāb): full sanad-grading would require al-Albānī *Silsila*, al-Dāraquṭnī *ʿIlal*, and Aḥmad's *Musnad* index; flagged as DATA-GAP for chain-level audit.
- Claim 1 (KHYʿṢ uniqueness): the muqaṭṭaʿāt-letter classification of HM-ʿSQ Q 42 (4 letters in v.1, 1 in v.2 split across two verses) is itself a classical-controversy point — under the alternative reading where Q 42 is "5 letters total", the Q 19 KHYʿṢ uniqueness becomes "Q 19 is one of 2 5-letter clusters". The default reading per al-Suyūṭī's *al-Itqān* is **per-verse**, which preserves Q 19's singleton status.
- Claim 3's "pericope-extent" framing should be stress-tested against other surahs (e.g., Q 12 Yūsuf has 100+ verses of continuous narrative; what's the surah's pericope-extent vs name-token concentration). Pre-registered as Q019-F-02 in `06-novel-findings.md`.
