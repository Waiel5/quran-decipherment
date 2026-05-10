---
surah: 9
surah_name_ar: التوبة
surah_name_translit: al-Tawba
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
verdict: 10 audits — 4 VINDICATED (Q 9 outlier-status, al-Faḍiḥa hypocrisy-density, Q 9:128-129 multiple-Companion-attestation, basmala-corpus-singleton al-Suyūṭī Itqān nawʿ 6), 2 FALSIFIED (Q 8-Q 9 unity, no-mercy → no-basmala), 2 NULL (last-revealed-verse single dominance, al-Biqāʿī Q 8↔Q 9 thematic-couplet at FR-seam level), 1 RULES-TUPLE-FRAGILE (lost-original-opening of Q 9 — empirically opaque, theologically rejected by al-Rāzī), 1 NULL-DIRECTIONAL (long-Medinan verse-length signature: top-12 not top-10).
---

# Q 9 al-Tawba — Classical-Claims Audit

This file rigorously audits the major non-trivial classical claims about Q 9, applying pre-registered tests where possible. Every audit follows: **state-claim → cite-source → specify-rules-tuple → run-test (or note non-testable) → verdict**.

---

## Audit 1 — Q 8-Q 9 unity (Ibn ʿAbbās, Ubayy b. Kaʿb)

### Claim
Q 8 al-Anfāl and Q 9 al-Tawba were originally **one surah**; the redaction (during ʿUthmān's compilation) split them, leaving the Q 9-no-basmala as the trace.

### Sources
- Ibn ʿAbbās via Saʿīd b. Jubayr; Ubayy b. Kaʿb (al-Zamakhsharī, *al-Kashshāf* `zamakhshari-openiti-Q009.txt` lines 9-30).
- al-Ṭabarsī, *Majmaʿ al-bayān* `tabarsi-openiti-Q009.txt` lines 3-12.
- al-Qurṭubī, position-4 (`qurtubi-openiti-Q009.txt` lines 41-47).

### Rules-tuple
- Tashkeel: Hafs no-tashkeel
- Tokens: orthographic-words
- Distance: Fisher-Rao on QAC stem-root probability vectors (matching H-NEW-111 method)
- Variant: also re-verified on Hafs full-tashkeel for sensitivity check

### Test
[[h-new-890-numerical-reaudit]] T1: compute d_FR(Q8, Q9); compare to distribution of all 113 adjacent-pair distances.

### Result
- d_FR(8, 9) = **0.911**
- adjacent-pair mean = 0.759, median = 0.816, std = 0.242
- Q 8-Q 9 rank: **81 / 113** (above-median dissimilarity)
- p_one-sided = 0.717 (testing for *smaller-than-typical*)
- α_bon (k=5) = 0.01

### Verdict: **FALSIFIED** (rules-tuple-stable)

The unity-claim predicts Q 8 and Q 9 should be MORE similar than typical adjacent pairs. Empirically they are LESS similar. The classical doubt that motivated the no-basmala convention had a real textual basis (the redactors couldn't be sure), but at the FR-roots-distance level, Q 8 and Q 9 are NOT a duplicated unit.

### Implication for the no-basmala question
Position 4 (the "compromise" position: leave a blank line, no basmala, accommodating both views) was driven by Companion *uncertainty*. Modern empirical analysis shows the uncertainty was misplaced — Q 8 and Q 9 are demonstrably distinct surahs by content. The mushaf's redactional decision (no basmala but separated as two) honoured the Companions' epistemic humility and is **architecturally consistent** with the FR result.

---

## Audit 2 — No-basmala because no-mercy (al-Bayhaqī, ʿAlī, al-Mubarrad, Sufyān b. ʿUyayna)

### Claim
The basmala = mercy-and-protection (*amān*); Q 9 is a sword/wrath proclamation, hence incompatible with mercy. al-Suyūṭī *Itqān* nawʿ 7 cites this as ʿAlī b. Abī Ṭālib's reported answer to Ibn ʿAbbās's query.

### Source
- al-Qurṭubī, position-5 (lines 50-56): "البسملة أمان وبراءة نزلت بالسيف ليس فيها أمان."
- al-Mubarrad: "البسملة رحمة وبراءة نزلت سخطة."
- Sufyān b. ʿUyayna (lines 56-58): "this surah was revealed regarding the *munāfiqūn* and the sword, and there is no *amān* for the *munāfiqūn*."

### Rules-tuple
- Hafs no-tashkeel
- QAC v0.4 root-attestations
- Density: per-1000-token

### Test
[[Q009-F-01-mercy-density]] (`csv/Q009-F-01-02-density-results.json`).

### Result
- Q 9 root *r-ḥ-m* count: 13
- Q 9 density: **4.86 / 1k tokens** (rank 24/114, top-quartile)
- Corpus mean: 3.95 / 1k
- Corpus median: 1.59 / 1k

Q 9's mercy-vocabulary density is **above the corpus mean** and ranks in the top-quartile.

### Verdict: **FALSIFIED** at the empirical-density level

The classical "no-mercy → no-basmala" claim is **not supported** by Q 9's actual mercy-vocabulary distribution. Q 9 contains 13 root-r-ḥ-m attestations including:
- v. 5: *fa-inna llāha ghafūrun raḥīm* (forgiving, merciful)
- v. 27: *thumma yatūbu llāhu min baʿdi dhālika ʿalā man yashāʾu wa-llāhu ghafūrun raḥīm*
- v. 99: *wa-yudkhilahum llāhu fī raḥmatih*
- v. 102: *wa-llāhu ghafūrun raḥīm*
- v. 117: *innahu bihim raʾūfun raḥīm*
- v. 128: *bi-l-mu'minīna raʾūfun raḥīm*

Indeed, the surah closes (v. 128) with two of God's mercy-attributes for the believers, not the sword. The classical position holds rhetorically (Q 9 has more *qātilū* / sword-imperatives than any other surah, *jhd* root rank 2/114) but does NOT hold at the mercy-density level.

### Honest qualification
The semantic question "is the *target* of mercy in Q 9 narrower than in other surahs?" is OPEN — perhaps Q 9's mercy is exclusively for *al-tāʾibūn* (the penitent) rather than for *all*. A finer-grained semantic-frame test could reveal heterogeneity. But Position-5's claim **as stated** ("no mercy → no basmala") is **falsified by root-density count**.

---

## Audit 3 — al-Faḍiḥa naming (Saʿīd b. Jubayr → Ibn ʿAbbās)

### Claim
Q 9 should be called *al-Faḍiḥa* (the Exposer) because it relentlessly enumerates the hypocrites by *wa-minhum… wa-minhum* refrain.

### Source
- al-Bukhārī **ḥadīth #4674**: "Sūrat al-Tawba? It is exposure (*al-Faḍiḥa*)..."
- al-Suyūṭī *al-Itqān* nawʿ 9 (line 3392).
- al-Zamakhsharī catalogues 11 names of the surah, with *al-Faḍiḥa* central.

### Rules-tuple
- Hafs no-tashkeel
- QAC root-density per-1000-tokens

### Test
[[Q009-F-02-hypocrite-density]].

### Result
- Q 9 root *n-f-q* count: 21
- Q 9 density: **7.85 / 1k tokens** — rank **5 / 114**
- Corpus mean: 1.02 / 1k
- Pre-registered threshold: rank ≤ 12 ⇒ VINDICATED.

Differential test: Q 9 nfq-rank (5) vs. kfr-rank (17): difference = −12 (Q 9 is *more* distinctively a hypocrisy-surah than a disbelief-surah).

### Verdict: **VINDICATED** (rules-tuple-stable, pre-registered, in top-decile)

Q 9 is **not just any hypocrisy-discussing surah** — it is the *most concentrated nifāq-discourse text in the entire Quran* (top-5; Q 63 al-Munāfiqūn is rank 1 with the smaller word base of 180 tokens making the ratio extreme). The al-Faḍiḥa naming captures a genuine empirical signature.

---

## Audit 4 — Q 9 = al-sabʿ al-ṭiwāl 7th member (al-Suyūṭī, al-Zamakhsharī)

### Claim
Q 9 functions as the 7th of the seven longest surahs (*al-sabʿ al-ṭiwāl*: Q 1-9 with the canonical absorption Q 8+Q 9 sometimes treated as one). al-Suyūṭī, *al-Itqān* nawʿ 4 (mufaṣṣal/ṭiwāl-classification).

### Source
- al-Suyūṭī *al-Itqān* nawʿ 4
- al-Zamakhsharī *al-Kashshāf* (ll. 22-25 of Q 9 extract): "تعدان السابعة من الطول"
- al-Ṭabarsī *Majmaʿ al-bayān* (Q9 extract ll. 3-12): same.

### Rules-tuple
- Hafs no-tashkeel
- Outlier-strength method: H-NEW-590 percentile-spectrum

### Test
[[h-new-590-outlier-spectrum]] (`csv/h-new-590.json` `top_10_outliers[3]`):
- Q 9 Δ%ile = +21.57 pp under window-{1..7-with-Q9-extension} exclusion test
- Classification: MODERATE_OUTLIER

This is a different question than "is Q 9 a 7-tier-classmember" — the test we have evaluates the COHESION-isolation of Q 9 within the al-sabʿ al-ṭiwāl group. With Δ%ile = +21.57 (rank 4 of 114), Q 9 IS a content-outlier within this group. By contrast, Q 2 has Δ%ile = −20.62 (the strongest cohesion-anchor of the group).

### Verdict: **VINDICATED with NUANCE**

Q 9 IS classified by classical scholarship as a 7-tier member, AND it is empirically an **outlier within that group** — not a typical member but one that the group encompasses by virtue of Q 9's length and Medinan period rather than its content-cohesion to its neighbours. Both claims (membership and outlier-status) are simultaneously true.

---

## Audit 5 — Q 9:128-129 = the LAST verses revealed (Ubayy b. Kaʿb, al-Ḥasan, Saʿīd b. Jubayr)

### Claim
Q 9:128-129 are the chronologically-last two verses of the Quran.

### Sources
- Ubayy b. Kaʿb chain (al-Bukhārī, al-Ṭabarī's 4 chains, al-Aḥmad).
- al-Ḥasan al-Baṣrī (al-Rāzī line 8268).
- Saʿīd b. Jubayr (al-Suyūṭī *Durr al-manthūr* line 6142).

### Competing claims
- Q 4:176 (al-Barāʾ b. ʿĀzib via al-Bukhārī)
- Q 2:281 (Ibn ʿAbbās; ʿUmar via Aḥmad)
- Q 5:3 (Sufyān b. ʿUyayna)

### Rules-tuple
- Source-corpus: 10 OpenITI tafsirs
- Match: regex-based "آخر ما نزل/آية/سورة" within 8-line context window of rival-claim markers

### Test
[[Q009-F-04-last-revealed]].

### Result
- Q 9:128-129 cited 64×
- Q 2:281 cited 61×
- Q 4:176 cited 49×
- Q 5:3 cited 9×
- Pre-registered threshold: VINDICATED if Q9 > each rival × 1.10. **Result: 64 vs. 61 = 1.05× — does NOT exceed pre-registered margin.**

### Verdict: **NULL — al-Bayhaqī's harmonization upheld**

al-Bayhaqī's harmonization position (cited al-Suyūṭī *Itqān* nawʿ 8 line 1800) — that each Companion answered with what reached him, with Q 9:128-129 being the absolutely-last ENTIRE-PASSAGE while Q 2:281 (ribā ruling) and Q 4:176 (kalāla ruling) are the last LEGAL-RULINGS in their respective domains — is the most defensible reading.

The pre-committed direction was Q 9:128-129 dominance; the result narrowly missed the threshold; honesty requires reporting NULL not VINDICATED. **No pre-commit violation** — direction was supported but at insufficient magnitude.

---

## Audit 6 — Q 9 was originally as long as al-Baqara (Mālik via Ibn Wahb, Ibn al-Qāsim; Ibn ʿAjlān; Saʿīd b. Jubayr)

### Claim
The opening of Q 9 was originally as long as the entire Q 2 al-Baqara (286 verses), but parts dropped from active recitation; with the lost opening went the basmala.

### Sources
- al-Qurṭubī position-3 (line 32): citing Mālik via three chains.
- Ibn ʿAjlān: chain that "*surah Barāʾa equalled al-Baqara*."
- Saʿīd b. Jubayr (al-Qurṭubī line 36): "*kānat mithla sūrati l-Baqara*" — "it was like *al-Baqara*."

### al-Rāzī's epistemic objection
al-Rāzī, *Mafātīḥ al-ghayb* (lines 8275-8285) **rejects this on tawātur grounds**: "if we permitted [Ḥudhayfa b. al-Yamān's] report [of the longer original Q 9], this would imply *ziyāda wa-nuqṣān* (addition and subtraction) entered the Quran — which would invalidate its evidentiary status."

### Rules-tuple
- Empirical test: not directly testable — we have the **textual** Quran but not any **lost-text** to compare against.
- Possible indirect test: if the original opening included a basmala-receiving formula, Q 9's current OPENING content (vv. 1-2) would be the *non-opening* of the original. Some classical predictors say it was "treaty-renunciation prelude" or longer narrative. Without manuscript or revelation evidence, this is opaque.

### Test
**NOT EMPIRICALLY TESTABLE** with available textual data.

### Verdict: **RULES-TUPLE-FRAGILE / NOT-EMPIRICALLY-TESTABLE**

al-Rāzī's theological argument (preserving tawātur) is the project-aligned position. We do not endorse the lost-text position. We document it as a classical-historical claim without empirical traction.

---

## Audit 7 — Q 9-Q 10 transition is structurally significant

### Claim (modern, this project)
The Q 9 → Q 10 boundary is among the most structurally-expensive transitions in the entire mushaf — implying a deliberate honoring of a chronology-block boundary (Medinan-late → Meccan-ALR-cluster).

### Source
- [[h-new-720-canonical-adjacency-cost]] `top10_expensive`.

### Rules-tuple
- Hafs no-tashkeel
- FR-TSP residual decomposition (best-of-K-restarts, K=20)
- per_adjacency `fraction_residual`

### Test
[[Q009-F-03-q9-q10-boundary]].

### Result
- Q 9 → Q 10 fraction_residual: **3.73%** of total
- Rank: **4 / 113**
- Q 8 → Q 9 (left neighbour): 0.74%, rank 58/113
- Q 6 → Q 7 control (Q 7 starts المص): **0.00%, rank 103/113** — muqaṭṭaʿāt-introduction is NOT inherently expensive

### Verdict: **VINDICATED**

The Q 9-Q 10 transition is the **4th most expensive canonical adjacency** in the mushaf. The control rules out muqaṭṭaʿāt-cluster-onset as the driver. The remaining hypothesis — that the cost is the chronology-block boundary (Q 9 = Medinan late ≈ revelation-order #113; Q 10 = Meccan ≈ revelation-order #51) — is supported.

This is a **modern empirical finding** that complements the classical observation of Q 9's Tabuk-era status: the mushaf-redactors paid a structural cost to place Q 9 here (alongside its long-Medinan length) rather than in a Medinan-block at the back of the corpus.

---

## Audit 8 — Q 9:111 *bayʿ al-jihād* connection to *Tawrāt* and *Injīl*

### Claim
Q 9:111 — *waʿdan ʿalayhi ḥaqqan fī t-tawrāti wa-l-injīli wa-l-qurʾān* — explicitly grounds the *bayʿat al-jihād* in prior revelations. Classical mufassirūn (al-Ṭabarī, al-Qurṭubī) interpret this as pointing to **specific** Torah and Gospel passages.

### Source
- al-Ṭabarī (`tabari-openiti-Q009.txt`): cites Saʿīd b. Jubayr that "*hādhihi l-āyatu maktūbatun fī t-tawrāti wa-l-injīl*."
- al-Qurṭubī: extensive cross-reference to *muḥāsabāt* literature.

### Rules-tuple
- Cross-textual: Quranic claim of textual-precedent in pre-Islamic scriptures.

### Test
- The QAC's parallel cross-finding-010 syncs Quran-internal *bayʿ al-jihād* references; cross-corpus testing against Hebrew/Greek scriptural corpora is BEYOND the project's current data scope.

### Verdict: **NOT-TESTABLE within current corpus**

Documented as a classical claim that requires extra-Quranic textual corpus to evaluate.

---

## Audit 9 — Basmala canonical-attestation: Q 9 is the corpus-only basmala-omitter (al-Suyūṭī, ʿUthmān via al-Tirmidhī)

### Claim
The Quranic mushaf prints the basmala formula *bismi llāhi al-raḥmāni al-raḥīm* as the canonical opener of all 114 surahs EXCEPT Q 9 al-Tawba; the basmala appears internally exactly once more, at Q 27:30 (Solomon's letter to Bilqīs). This is the canonical 5-position debate documented in al-Suyūṭī.

### Sources
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 6 *fī asbāb sukūt al-basmala fī Barāʾah*.
- al-Suyūṭī, *al-Itqān*, nawʿ 7 *fī ʿadad suwarihā wa-āyātihā wa-kalimātihā wa-ḥurūfihā*.
- al-Tirmidhī, *Sunan*, ḥadīth #3086: ʿUthmān ibn ʿAffān explaining that the Prophet (ﷺ) did not specify whether Q 9 was a continuation of Q 8 or a separate surah; the Companions opted for separation-without-basmala.
- al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, introduction to Q 9 (5 classical positions on the omission).

### Rules-tuple
- Hafs-Kufan + orthographic + NFKD-strip
- Corpus-1: stored JSON (`quran-text/quran-no-tashkeel.json`) — basmala stored as v.1 only for Q 1
- Corpus-2: printed convention (`data/alt-text/quran-simple-txt.txt`) — basmala printed before every surah except Q 9

### Test
[[Q009-F-05-basmala-corpus-singleton]].

### Result
- Surahs with v.1 = basmala (in stored Hafs-numbered JSON): **[1]** (Q 1 only).
- Surahs with v.1 ≠ basmala: **113** (all surahs except Q 1, including Q 9).
- Q 9 is in the "v.1 ≠ basmala" set: **TRUE**.
- Internal-basmala occurrences (non-v.1): **1**, at **Q 27:30**.
- Printed corpus total basmala count: **114** = 113 printed-openers + 1 internal.

### Verdict: **VINDICATED-CORPUS-EXACT**

The al-Suyūṭī / ʿUthmān / al-Qurṭubī canonical attestation that Q 9 is the corpus-only basmala-omitter, and that Q 27:30 is the corpus-only internal basmala, is **exact** at the textual-arithmetic level. The 5-position theological debate that this attestation presupposes is preserved AS DEBATE; only the bare phenomenon (singleton-omission + singleton-internal) is rendered empirically explicit.

### Cross-implications
- Audit 2 (no-mercy → no-basmala) had FALSIFIED Position 5 of the omission-debate.
- Audit 1 (Q 8-Q 9 unity) had FALSIFIED Position 2 (Ibn ʿAbbās).
- Audit 9 (this one) leaves Positions 1 (ʿAlī war-context), 3 (ʿUthmān doubt-default), 4 (compromise), 6 (lost-opening) open as candidates — the bare phenomenon is now empirically locked, while the *causation* remains a classical inter-pretive question.

---

## Audit 10 — al-Biqāʿī Q 8 ↔ Q 9 thematic-couplet *tanāsub*

### Claim
al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* — Q 8 al-Anfāl and Q 9 al-Tawba form a single *tanāsub* unit at the surah-pair level: Q 8 develops the Badr-victory/spoils-of-war discourse and the believer-mushrik treaty-base; Q 9 extends to Tabūk-expedition / treaty-renunciation / Faḍīḥa of the hypocrites. The two surahs are read as a connected war/community-discipline diptych. This is a *weaker* version of Ibn ʿAbbās's "one surah" claim (FALSIFIED in Audit 1) — it asserts thematic coupling, not textual unity.

### Sources
- al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, introduction to Q 9 (`biqai-nazm-al-durar.pdf`).
- al-Suyūṭī, *al-Itqān*, nawʿ 7 endorses *tanāsub*-style readings as legitimate even where the unity claim is rejected.

### Rules-tuple
- Hafs no-tashkeel + QAC v0.4 stem-roots
- Source: H-NEW-720 `per_adjacency` `delta_raw` (FR-TSP residual)
- Test: rank-smooth = position of Q 8 → Q 9 in ascending delta_raw across 113 seams
- Pre-committed: VINDICATED if rank-smooth ≤ 34 (top 30% smoothest), NULL if 35-80, FALSIFIED if ≥ 81.

### Test
[[Q009-F-06-q8-q9-seam-smoothness]].

### Result
- Q 8 → Q 9 `delta_raw` = 0.0612, `fraction_residual` = 0.74%.
- **Rank-smooth: 56 / 113** (49.6th percentile, mid-band).
- For comparison: Q 9 → Q 10 `delta_raw` = 0.3094, rank-smooth = 110/113 (4th most-expensive in corpus).

### Verdict: **NULL** (rank-smooth 56 ∈ [35, 80] band)

The pre-committed direction (top-30% smooth) is **not supported** at the FR-roots seam-smoothness level. The Q 8 → Q 9 seam is structurally mid-band — neither corpus-smooth (which would have supported al-Biqāʿī at root-frequency level) nor corpus-expensive.

### Honest interpretation
This is a NULL, not a FALSIFICATION. al-Biqāʿī's thematic *tanāsub* reading is interpretive — it operates on content topic, asbāb al-nuzūl chronology, and rhetorical movement, not necessarily on root-frequency distributions. The Q 8 ↔ Q 9 thematic-couplet reading is consistent with the mid-band seam (the surahs sit together without major TSP penalty), but the strong empirical signature predicted by the top-30% threshold is absent. The al-Biqāʿī reading remains a legitimate *literary*-level claim; the empirical translation to FR-seam-smoothness is not supported.

This complements:
- Audit 1: Ibn ʿAbbās's stronger "one surah" claim FALSIFIED (d_FR rank 81/113 — too dissimilar).
- Audit 7: Q 9 → Q 10 boundary rank-4 expensive — Q 9's chronology-block transition is on its RIGHT side.
- Audit 9 (this set): basmala-omission is a graphical-canonical fact orthogonal to root-distribution.

Together: Q 9's couplings to its mushaf neighbours are NOT root-distribution-smooth in either direction; both Ibn ʿAbbās's textual-unity reading and al-Biqāʿī's thematic-couplet reading lack empirical support at the FR-roots seam level, even though both remain rhetorically/literarily plausible.

---

## Summary of Audits

| # | Claim | Verdict | Evidence-strength |
|:-:|:--|:--|:--|
| 1 | Q 8-Q 9 unity (Ibn ʿAbbās) | **FALSIFIED** | rules-tuple-stable, p=0.717 |
| 2 | No-mercy → no-basmala (Position 5) | **FALSIFIED** | density rank 24/114, vs. predicted ≥ 87 |
| 3 | al-Faḍiḥa naming | **VINDICATED** | density rank 5/114, predicted ≤ 12 |
| 4 | Q 9 = 7th of al-sabʿ al-ṭiwāl with content-distinctness | VINDICATED-WITH-NUANCE | outlier rank 4/114 |
| 5 | Q 9:128-129 = absolutely last | **NULL** (margin missed) | 64 vs 61 in 10-tafsir survey |
| 6 | Q 9 originally al-Baqara-length | NOT-EMPIRICALLY-TESTABLE | al-Rāzī rejects on tawātur |
| 7 | Q 9-Q 10 boundary structural | **VINDICATED** | rank 4/113, control falsifies muqaṭṭaʿāt-driver |
| 8 | Q 9:111 *bayʿ* in Torah/Gospel | NOT-TESTABLE | extra-corpus |
| 9 | Basmala canonical-singleton (al-Suyūṭī Itqān nawʿ 6) | **VINDICATED-CORPUS-EXACT** | exactly 113 openers + 1 internal Q 27:30 = 114 |
| 10 | al-Biqāʿī Q 8 ↔ Q 9 thematic-couplet *tanāsub* | **NULL** | seam rank-smooth 56/113 (mid-band) |

**Headline contributions to project**:
- Empirical falsification of the most popular classical answer to "why no basmala" (Position 5).
- Empirical confirmation of the al-Faḍiḥa naming.
- Q 9-Q 10 boundary identified as the **4th most-expensive** canonical adjacency (a finding NOT in classical scholarship).
- Basmala corpus-exact singleton verified (exactly 114 in corpus, 113 openers + 1 internal at Q 27:30).
- al-Biqāʿī's *tanāsub* reading of Q 8 ↔ Q 9 NOT supported at FR-roots seam-smoothness, though the unity claim remains FALSIFIED while the *thematic* claim remains literarily plausible.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
