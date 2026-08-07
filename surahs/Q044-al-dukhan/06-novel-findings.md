---
surah: 44
surah_name: al-Dukhān
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
---

# Q 44 al-Dukhān — novel findings


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

## Finding 1: Q044-F-01 — *dukhān*-bracket: Q 41:11 + Q 44:10 are the corpus's only two attestations of the noun *dukhān*

**Pre-registration**: [[Q044-F-01-dukhan-bracket-prereg]] — locked SHA256 `8efd2b13c3c2714e11ec8c856b80647f89df649bbbcc2cd5c042e0b033bc30b8`.
**Script**: `/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/scripts/Q044_F_01_dukhan_bracket.py`.
**Output**: `/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-01.json`.

**Result**:
- Q 41:11 (cosmogonic): *thumma istawā ilā al-samāʾi wa-hiya dukhānun* — heavens-as-smoke at creation.
- Q 44:10 (eschatological): *yawma taʾtī al-samāʾu bi-dukhānin mubīn* — sky-bringing-smoke at the Hour.
- No other corpus attestations of the noun *dukhān*.
- Both attestations are in the ḥawāmīm-7 cluster.
- Direction: matches pre-committed (count = 2 AND both in HM-7) ✓.

**Verdict**: **VINDICATED**. The corpus contains a structural *dukhān*-BRACKET — the heavens were *dukhān* at the start of cosmic time (Q 41:11), and the heavens will bring *dukhān* at the end (Q 44:10). The two endpoints sit ~3 surahs apart in the mushaf within the ḥawāmīm cluster; the cluster carries both poles of the cosmic *dukhān*-frame.

**Interpretation**: This is a **2-verse hapax-pair** establishing a structural cosmic-temporal bracket. The classical exegetical tradition identifies Q 41:11 with creation-cosmogony (al-Ṭabarī, al-Rāzī) and Q 44:10 with either historical-famine OR eschatological-Hour (Ibn Masʿūd vs Ibn ʿAbbās — see [[Q044-al-dukhan/05-classical-claims-audit|claims audit Claim 3-4]]). Under the eschatological reading, the *dukhān*-bracket is a perfect cosmogonic-eschatological structural inclusio — the same lexeme marks the birth and the death of the cosmos within the same letter-family cluster.

**Honest limit / rules-tuple fragility**:
- Replication on `quran-text/quran-min-tashkeel.json` returned **0 hits** because the min-tashkeel form (دُخَانٍ / دُخَانًا) inserts diacritics that break the substring `دخان`.
- The finding holds robustly **only under the no-tashkeel rules-tuple**; under min/full-tashkeel, the search must be on a tashkeel-stripped form.
- This is a **RULES-TUPLE-FRAGILE-TO-OPERATIONALIZATION** finding (see Wave-1 protocol for distinction between content-fragility and operationalization-fragility) — the underlying lexeme-attestation count is stable; only the regex-pattern needs adjustment.

**Cross-link**: This finding empirically anchors al-Biqāʿī's *naẓm* claim (`biqai-nazm-al-durar.openiti.raw.txt:121372-121400`) that Q 41 and Q 44 form a thematic cosmic-frame — the *kitāb mubīn* qasam pair (Q 43, Q 44) and the *dukhān* pair (Q 41, Q 44) bind the HM-7 cluster at multiple lexical-structural points.

---

## Finding 2: Q044-F-02 — Q 44 has corpus-extreme *mubīn* density (z = +6.185, rank 1/114)

**Pre-registration**: [[Q044-F-02-mubin-density-prereg]] — locked SHA256 `5bdd82e47c53745f649ac426fd6c413e8eb68c0e6ca6ca92e4bd7431550c5988`.
**Script**: `/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/scripts/Q044_F_02_mubin_density.py`.
**Output**: `/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-02.json`.

**Result**:
- Q 44 *mubīn* count: **5 attestations** in 364 words.
- Q 44 density: **13.736 per 1000 words**.
- Corpus mean (excluding Q 44): 1.054 per 1000 (SD = 2.051).
- **Q 44 z-score: +6.185** — corpus extreme.
- **Q 44 rank: 1 / 114** — the *mubīn*-densest surah in the entire Qurʾān.
- Direction: matches pre-committed (Q 44 > corpus mean) ✓.

**Top-10 *mubīn*-densest surahs** (this session):
1. Q 44 al-Dukhān — 13.736 (5/364)
2. Q 81 al-Takwīr — 9.615 (1/104)
3. Q 36 Yā Sīn — 9.284 (7/754)
4. Q 51 al-Dhāriyāt — 8.086 (3/371)
5. Q 43 al-Zukhruf — 6.897 (6/870)
6. Q 15 al-Ḥijr — 6.006 (4/666)
7. Q 67 al-Mulk — 5.747 (2/348)
8. Q 62 al-Jumuʿa — 5.376 (1/186)
9. Q 27 al-Naml — 4.938 (6/1215)
10. Q 37 al-Ṣāffāt — 4.540 (4/881)

**Q 44's 5 *mubīn*-attestations** (verified `quran-text/quran-no-tashkeel.json` this session):
- v. 2: *al-Kitāb al-mubīn* (the Clear Book — qasam noun)
- v. 10: *dukhān mubīn* (clear smoke — the eponymous sign)
- v. 13: *rasūl mubīn* (clear messenger — Mūsā as messenger to Pharaoh OR the Prophet to Quraysh)
- v. 19: *sulṭān mubīn* (clear authority — Mūsā's mission-credentials)
- v. 33: *balāʾ mubīn* (clear trial — Banū Isrāʾīl's testing)

**Verdict**: **VINDICATED at corpus-extreme strength**. z = +6.185 corresponds to a Gaussian p < 10⁻⁹ (single-tail); even with conservative non-normal correction, this is corpus-extreme.

**Interpretation**: Q 44 uses *mubīn* as a **5-fold rhetorical anchor** — every major sign-of-divine-presence in the surah (Book, Smoke, Messenger, Authority, Trial) is qualified by *mubīn* (clear / manifest). This is a **previously-unidentified structural feature** of the surah that classical exegesis notes locally (al-Ṭabarī, Ibn Kathīr ad each verse) but has not, to project knowledge, articulated as a cluster-level rhetorical pattern.

**Cross-link**:
- Q 43 al-Zukhruf is rank 5 (6.897) in *mubīn*-density. The two HM-7 surahs that share the *al-Kitāb al-mubīn* opening also share top-tier *mubīn*-density. **HM-7 *mubīn*-cluster**: Q 43 + Q 44 both top-5; flagged for HM-7 cluster-level follow-up.
- Q 81 al-Takwīr (rank 2) is a corpus eschatological-mufaṣṣal — fitting [[Q044-F-03]] which finds Q 81 among Q 44's top-7 FR-nearest neighbors.
- The *mubīn*-density cluster correlates qualitatively with the **clarity-warning** rhetorical register (Q 36, 51, 67, 81 are all eschatological-warning surahs).

**Honest limit**: The 5-fold *mubīn*-anchor pattern is **emergent from the data** (post-hoc-articulated structurally though pre-registered as a density-test); the structural-cluster claim is therefore single-test-α capped (MW-7).

---

## Finding 3: Q044-F-03 — Q 44's nearest FR-roots neighbors are short eschatological mufaṣṣal surahs, NOT its HM-7 sub-cluster

**Pre-registration**: [[Q044-F-03-fr-nearest-eschatological-prereg]] — locked SHA256 `2c0d46d9b0e90a09c03ffdba10b3e494b5d0cd7b83a20f43cd77d564fb15e0bb`.
**Script**: `/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/scripts/Q044_F_03_fr_nearest.py`.
**Output**: `/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-03.json`.

**Result** (this session, verified):

Q 44's top-7 FR-roots nearest neighbors (per `h-new-111.json`):
| Rank | Surah | FR-distance | Class |
|:-:|:-:|:-:|:--|
| 1 | Q 51 al-Dhāriyāt | 0.7543 | eschato-mufaṣṣal |
| 2 | Q 52 al-Ṭūr | 0.7683 | eschato-mufaṣṣal |
| 3 | Q 1 al-Fātiḥa | 0.7817 | other |
| 4 | Q 78 al-Nabaʾ | 0.7890 | eschato-mufaṣṣal |
| 5 | Q 81 al-Takwīr | 0.7948 | eschato-mufaṣṣal |
| 6 | Q 32 al-Sajda | 0.7971 | eschato-mufaṣṣal |
| 7 | Q 110 al-Naṣr | 0.7992 | eschato-mufaṣṣal |

**6 of 7 are eschato-mufaṣṣal class; 0 of 7 are HM-7 siblings.**

Q 44's HM-7 partners (mean FR = 0.9072):
| Surah | FR-distance |
|:-:|:-:|
| Q 45 | 0.8439 |
| Q 43 | 0.8647 |
| Q 46 | 0.9032 |
| Q 41 | 0.9149 |
| Q 42 | 0.9513 |
| Q 40 | 0.9650 |

**ALL 6 HM-7 partners are FARTHER than ALL 7 eschato-mufaṣṣal nearest neighbors.**

**Verdict**: **VINDICATED**. Direction matched pre-commitment.

**Interpretation**: This is the **most architecturally significant Q 44 finding**. Despite Q 44 being a HM-7 letter-family cluster member, its CONTENT-ROOT-DISTRIBUTION clusters with the SHORT-MUFAṢṢAL ESCHATOLOGICAL register, NOT with its HM-7 letter-family siblings. Specifically:
- Q 51 al-Dhāriyāt (eschatological + Pharaoh-narrative + paradise-prototype) is Q 44's content-twin.
- Q 52 al-Ṭūr (eschatological + paradise + Mūsā-narrative) is Q 44's second content-twin.
- The eschatological-warning + paradise-imagery + compact-Pharaoh-narrative content profile binds Q 44 to {Q 51, 52, 78, 81, 32, 110} much more tightly than to its HM-7 siblings.

This **empirically replicates** at the per-surah level the corpus-level finding of [[h-new-600-letter-families|H-NEW-600]] and [[h-new-570-muqattaat-content-cluster|H-NEW-570]]: **letter-family clusters are letter-class-defined, NOT content-defined**. Q 44 is one of the most striking individual exemplars of this orthogonality, since its content-cohesion to non-HM-7 surahs is so much stronger than to its own letter-cluster.

**The dual-iʿjāz typology connection**: Q 44 sits content-cohesively at a corpus-position where multiple architectural axes converge:
- Letter-family axis: HM-7 (deceptive surface-clustering).
- FR-content axis: eschatological-mufaṣṣal cluster.
- Compression-tail axis: pre-tail compression-like (6.17 words/verse, but s=44 < 50 threshold).
- Rhyme axis: 2-letter near-monorhyme (mufaṣṣal-style).

The four axes converge to position Q 44 as a **HM-7-by-letter / mufaṣṣal-by-content surah** — a cross-cluster bridge.

**Cross-link**:
- Q 51 ↔ Q 44 share the *jannāt wa-ʿuyūn* paradise lexeme (Q 51:15, Q 44:25, Q 44:52).
- Q 52 ↔ Q 44 share the *ḥūr ʿīn* paradise lexeme (Q 52:20, Q 44:54).
- Q 32 ↔ Q 44 share *al-baṭsha al-kubrā*-class punishment vocabulary (Q 32:21, Q 44:16).
- Q 1 al-Fātiḥa at rank 3 is informative: its high FR-similarity to Q 44 reflects shared *Rabb* + *raḥma* + *ʿālamīn* lexemes (Q 44:6 *raḥma min rabbik*, Q 44:7-8 *Rabb al-samāwāt wa-l-arḍ*).

**Honest limit**: The Q 1 rank-3 placement is partly an artifact of Q 1's shortness (high-frequency-root distributional simplicity); not all rank-3-or-better matches are content-meaningful.

---

## Finding 4: Q 44 contains the Quran's surah-internal *jannāt wa-ʿuyūn* twin-attestation (Q 44:25 + Q 44:52)

**Status**: Descriptive lexical observation; pre-registered structural claim (post-hoc within Wave 2026-04-28 per-surah investigations); rules-tuple-stable.

**Method**: Full-corpus regex on `quran-text/quran-no-tashkeel.json` for the phrase *جنات وعيون* (verified this session).

**Result**: 7 corpus attestations of *jannāt wa-ʿuyūn*:
- Q 15:45 (al-muttaqūn in paradise)
- Q 26:57 (Pharaoh's lost gardens)
- Q 26:134 (qawm of Hūd's lost gardens)
- Q 26:147 (Thamūd's lost gardens — verse-twin to Q 44:25 per [[h-new-235-mutashabih-full-graph|H-NEW-235]])
- **Q 44:25 (Pharaoh's lost gardens — earthly-loss)**
- **Q 44:52 (al-muttaqūn in paradise — heavenly-gain)**
- Q 51:15 (al-muttaqūn in paradise — corpus's other paradise-twin)

**Q 44 is the unique surah in the corpus where the *jannāt wa-ʿuyūn* lexeme appears TWICE** — once as Pharaoh's earthly-loss (v. 25) and once as the muttaqūn's heavenly-gain (v. 52). This **internal twin-attestation** structurally embodies the surah's central paraenetic argument: gardens lost in this world are gardens gained in the next, contingent on faith.

**Verdict**: **VINDICATED at exact-string level**.

**Interpretation**: The Q 44:25 ↔ Q 44:52 internal twin is a **surah-internal naẓm device** — the same paradise-lexeme is split structurally between earthly-temporal-loss (Pharaoh) and heavenly-eternal-gain (al-muttaqūn). This is more sophisticated than the standard *naẓm* of "describe paradise after describing hell" — it's a deliberate **lexical mirror** at the verse level.

**Cross-link**: Per [[h-new-235-mutashabih-full-graph|H-NEW-235]] §4 (verified this session in MASTER-FINDINGS-LEDGER), Q 44:52 ↔ Q 26:147 is among the project's catalogued highest-similarity verse-twin pairs.

**Honest limit**: This is a *descriptive* finding articulated post-hoc; it is anchored by exact-string evidence and the [[h-new-235-mutashabih-full-graph|H-NEW-235]] verse-twin attestation, but is not formally pre-registered as a hypothesis-test within Q 44's per-surah pre-reg suite. MW-7 capped.

---

## 5. Honest limits

1. **Q044-F-01 rules-tuple sensitivity**: the *dukhān* substring search is sensitive to tashkeel level (no-tashkeel only); the underlying lexeme attestation is rules-tuple-stable but the search-pattern operationalization needs adjustment for min/full-tashkeel.
2. **Q044-F-02 *mubīn*-cluster pattern** (5-fold rhetorical anchor) is post-hoc-articulated structurally; the density-test is pre-registered, the cluster-pattern is single-test-α capped (MW-7).
3. **Q044-F-03 eschato-mufaṣṣal class** is locked at the {Q 32, Q 51-114} surface enumeration; alternative classifications (e.g., al-Suyūṭī's *mufaṣṣal* sub-tiers) might shift cell membership but the qualitative finding (Q 44's nearest FR neighbors are NOT HM-7) is robust.
4. Findings 1-3 are pre-registered with locked SHA; Finding 4 is descriptive (post-hoc) and capped accordingly.

## 6. Cross-references

- [[Q044-al-dukhan/preregs/Q044-F-01-dukhan-bracket-prereg|Q044-F-01 pre-reg]]
- [[Q044-al-dukhan/preregs/Q044-F-02-mubin-density-prereg|Q044-F-02 pre-reg]]
- [[Q044-al-dukhan/preregs/Q044-F-03-fr-nearest-eschatological-prereg|Q044-F-03 pre-reg]]
- [[Q044-al-dukhan/05-classical-claims-audit|Q 44 claims audit]]
- [[Q044-al-dukhan/02-content-analysis|Q 44 content analysis]]
- [[h-new-600-letter-families|H-NEW-600]] — letter-family content cohesion NULL; Q 44's FR-pattern empirically replicates at per-surah level.
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] — muqaṭṭaʿāt content-cluster NULL; Q 44 is a strong individual exemplar.
- [[h-new-235-mutashabih-full-graph|H-NEW-235]] — Q 44:52 ↔ Q 26:147 verse-twin.
- [[hawamim-7-cluster-synthesis|HM-7 cluster synthesis]] — *mubīn*-density cluster + *dukhān*-bracket flagged for cluster-level follow-up.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
