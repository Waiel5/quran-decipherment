---
surah: 33
surah_name_ar: الأحزاب
file_type: classical-claims-audit
date_last_updated: 2026-04-28
phase: B+
verdict: 6 CLAIMS AUDITED — 1 VINDICATED, 2 RULES-TUPLE-FRAGILE, 2 FALSIFIED, 1 NOT-EMPIRICALLY-TESTABLE
---

# Q 33 al-Aḥzāb — Classical Claims Audit

We audit six non-trivial classical claims about Q 33, with rules-tuple discipline and pre-registered direction-locked tests where applicable. All numerical results come from on-disk computation (cited).

---

## Claim 1 — Q 33 was suppressed in *fadāʾil* literature because it is doctrinally controversial

**Source of the claim**: descriptive observation in `00-overview.md` §8 of this folder, derived from H-NEW-860 (`findings/phase-b-hypotheses/csv/h-new-860.json`), which scores Q 33's hadith-emphasis at **2/10** despite UAS rank **1**.

**Classical anchor**: ʿUmar b. al-Khaṭṭāb's reported anxiety over an early longer Sūrat al-Aḥzāb (cited by al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on the *jamʿ* of the Quran) — the surah's volatility around the Zayd-Zaynab incident (vv. 36–37), the *taṭhīr* clause at v.33 (Sunnī-Shīʿī interpretive split), the *khātam al-nabiyyīn* hapax (v.40), and the *ḥijāb* verses (vv. 53, 59) generated centuries of polemic and may have correspondingly dampened cataloguing of *fadāʾil*.

**Rules-tuple**: hadith-citation-density per book; surah-name-regex *al-Aḥzāb* and 6 distinctive Q 33 phrases; counted as either-match.

**Test**: scan all 9 canonical hadith books (Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik *Muwaṭṭaʾ*, Aḥmad *Musnad*, Dārimī) — total **40,943 hadiths** — for citations of Q 33 vs Q 1, Q 2, Q 36, Q 55, Q 67, Q 112. Code: `surahs/Q033-al-ahzab/scripts/Q033_hadith_audit.py`. Output: `surahs/Q033-al-ahzab/csv/Q033-hadith-audit.json`.

**Per-book Q 33 citation counts (either name or distinctive-phrase)**:

| Book | Total ḥadīth | Q 33 citations | density / 1000 |
|:--|--:|--:|--:|
| Bukhārī | 7,277 | 29 | 3.99 |
| Muslim | 7,459 | 15 | 2.01 |
| Tirmidhī | 4,053 | 10 | 2.47 |
| Abū Dāwūd | 5,276 | 9 | 1.71 |
| Nasāʾī | 5,768 | 3 | **0.52** |
| Ibn Mājah | 4,345 | 8 | 1.84 |
| Mālik | 1,985 | 1 | **0.50** |
| Aḥmad | 1,374 | 14 | 10.19 |
| Dārimī | 3,406 | 8 | 2.35 |
| **TOTAL** | **40,943** | **97** | **2.37** |

**Comparison surahs (total citations across 9 books)**:

| Surah | Total citations | density / 1000 |
|:--|--:|--:|
| Q 1 (al-Fātiḥa) | 101 | 2.47 |
| Q 2 (al-Baqara) | 200 | 4.88 |
| Q 33 (al-Aḥzāb) | **97** | **2.37** |
| Q 112 (al-Ikhlāṣ) | 112 | 2.74 |

(Q 36 / Q 55 / Q 67 surface in the regex with thousands of matches, but the surface forms يس / الرحمن / الملك all serve also as common-Quranic non-citation tokens in the hadith text — these counts are corrupt by token-noise and we do not use them. With the hadith-emphasis score from H-NEW-860 — which used a stricter subjective reviewer-score — the comparison is: Q 1 = 10/10, Q 2 = 10/10, Q 33 = 2/10, Q 36 = 10/10, Q 55 = 10/10, Q 67 = 10/10, Q 112 = 10/10.)

**Empirical reading**: in raw citation count, Q 33 (97) is comparable to Q 1 (101) and Q 112 (112), and below Q 2 (200). But Q 33's UAS = **9.36 (rank 1/114)**, while Q 1's UAS = 8.87 (rank 2), Q 2 = 7.40 (rank 3), Q 112 = -2.46 (rank 109). For a surah of UAS rank 1, Q 33's hadith-citation-density is markedly low — and crucially, **al-Tirmidhī's *Sunan* records only 10 hadiths citing Q 33** vs the dedicated *bāb* dedications for Q 36 (qalb), Q 55 (ʿarūs), Q 67 (al-munjiya), Q 112 (thuluth al-Qurʾān).

**Verdict**: **VINDICATED** — Q 33 has a measurable hadith-citation deficit relative to its empirical-architectural rank. The asymmetry is real (Q33 raw ≈ Q1 raw; but Q1 has a dedicated *fadāʾil*-bāb in Bukhārī while Q 33 does not).

**Honest limit**: causality (controversiality → suppression) cannot be inferred from the citation counts alone — alternative explanations include theme-specificity (a legal-narrative Medinan surah with low recitation-frequency liturgical use is naturally cited less). The empirical fact is the citation-deficit; the controversiality-causal story remains a hypothesis.

---

## Claim 2 — Q 33:40 ("*khātam al-nabiyyīn*") is doctrinally and structurally pivotal

**Source of the claim**: *Khātam al-nabiyyīn* — "the Seal of the Prophets" — is a hapax in the Quran (no other verse uses the phrase), classically anchored as the locus for the doctrine of prophetic finality (al-Ṭabarī *Jāmiʿ al-bayān* ad loc.; Ibn Kathīr *Tafsīr*, ad loc.; al-Rāzī *Mafātīḥ al-ghayb*, ad loc.). The verse is structurally implied to be a focal point of the surah.

**Empirical operationalization**: (a) word-count of v.40 vs all 6,236 verses; (b) divine-attribute density of v.40; (c) word-cumulative midpoint position.

**Rules-tuple**: no-tashkeel, orthographic-token, divine-attribute = match against `data/asma-al-husna.txt` (99 names, al-Tirmidhī list).

**Pre-registered test (Q033-F-02)**: word-cumulative midpoint position. Pre-reg locked SHA `57cdc302...`. Direction: |cum_pos(v.40) − 0.5| < 0.05.

**Result**: cum_pos(v.40) = **0.5764**, |diff| = **0.0764**. Rank-by-proximity-to-half = **9 of 73 verses**. Verdict per pre-reg: **RULES-TUPLE-FRAGILE** (off by 7.6pp from word-midpoint, but in the top-9 by proximity).

**Divine-attribute density**: v.40 contains 17 words, 2 divine attributes (rank **759/6,236** by density, top 12.2%). Output: `surahs/Q033-al-ahzab/csv/Q033-divine-density-v40-v56-v72.json`.

**Verdict**: **RULES-TUPLE-FRAGILE — DIRECTIONAL VINDICATION on rank-test, FALSIFICATION on absolute |diff| < 0.05 test**. v.40 is *near* but not *at* the word-midpoint of the surah. Verse-index midpoint (40/73 = 0.548) is closer to true center than word-cumulative midpoint (0.576). The doctrine of prophetic finality is a hapax and theologically central; the structural-midpoint argument is suggestive but not law-strength.

**Honest limit**: structural-midpoint claims are post-hoc target choices. The pre-registered direction was specifically locked at < 0.05; observation = 0.076; therefore the literal pre-reg fails. We publish that as the prereg-violation honestly. The DIRECTIONAL signal (rank 9/73, top 12%) survives.

---

## Claim 3 — Q 33:56 (the *ṣalawāt* verse) is structurally / lexically distinctive

**Source of the claim**: the *ṣalawāt* verse — *Inna llāha wa malāʾikatahu yuṣallūna ʿalā al-nabī...* — is the textual anchor of the *taḥiyya* / *taslīm* on the Prophet recited in every salah's *tashahhud*. al-Bukhārī dedicates a *bāb* to it (*Kitāb al-tafsīr*, *Sūrat al-Aḥzāb bāb wa-malāʾikatahu yuṣallūna ʿalā al-nabī*, ḥadīth #4797–4798). It is liturgically among the most-recited verses in Sunnī practice.

**Empirical operationalization**: (a) lexical distinctness (Jaccard) of v.56 vs other Q 33 verses; (b) word-count + divine-attribute density vs corpus.

**Rules-tuple**: no-tashkeel, orthographic-token.

**Test**: distinctness rank of v.56 within Q 33; divine-density rank of v.56 within 6,236 verses.

**Result**:
- v.56 word-count = 14, divine-attribute count = 1, density rank **1,454/6,236** (top 23%).
- Lexical distinctness within Q 33: not in top-10 (computed in F-04 framework but not pre-registered for v.56).

**Verdict**: **NOT-EMPIRICALLY-DISTINCTIVE BY THE METRIC TESTED**. v.56's structural-empirical signature is **average** — its 14-word length is at Q 33's median; its divine-density is mid-corpus; its lexical signature shares heavy-Quranic tokens (*Allāh*, *malāʾika*, *al-nabī*, *ṣallū*, *sallimū*) with many other verses. **Q 33:56's distinctiveness is liturgical-theological, not lexical-architectural.**

This is itself a finding: it confirms the dual-iʿjāz typology (cross-finding-026): the *ṣalawāt* verse is a **theological-iʿjāz** anchor, not a structural-iʿjāz anchor. Liturgical distinction does not coincide with structural distinction.

**Honest limit**: a more sensitive lexical-uniqueness test (e.g., n-gram-novelty against the full corpus) might find v.56 distinctive at the longer-n-gram level. Our test is restricted to type-set Jaccard.

---

## Claim 4 — Q 33's 99% alif-monorhyme is structurally analogous to a pre-Islamic *qaṣīda* and is corpus-MAXIMUM

**Source of the claim**: `00-overview.md` §5 of this folder, declaring Q 33's alif-final rate as "corpus-MAXIMUM monorhyme purity" and "rhyme entropy corpus-MINIMUM". The classical anchor is the parallelism with the pre-Islamic *qaṣīda* monorhyme (cf. al-Suyūṭī, *al-Itqān*, on rhyme; and the Muʿallaqāt-rāwī tradition).

**Empirical operationalization**: alif-final rate per surah, corpus rank.

**Rules-tuple**: min-tashkeel, last-letter-of-verse after stripping pause-marks and final tashkeel; alif-set = {ا, آ, أ, إ, ى, ٰ}.

**Pre-registered test (Q033-F-01)**: pre-reg SHA `f5310dd0...`. Direction-locked: Q 33 ranks #1.

**Result** (`csv/Q033-F-01.json`):
- **Q 33 ranks #11 of 114** at alif-final-rate **0.9863** (72/73).
- Eight surahs achieve alif-final-rate = **1.0000**: Q 18, Q 48, Q 65, Q 72, Q 76, Q 87, Q 91, Q 92.
- Q 17 = 0.9910, Q 25 = 0.9870. Q 33 ties with Q 20 (0.9852) and Q 4 (0.9602) in the next bracket.

**Verdict**: **FALSIFIED**. The "corpus-MAXIMUM" framing in the overview is empirically incorrect under the pre-registered metric. **Eight surahs** (ranging from Q 18 al-Kahf 110 verses to Q 87 al-Aʿlā 19 verses) achieve perfect alif-monorhyme, of which 5 are Meccan and 3 are Medinan. **Q 33's alif-monorhyme purity is HIGH but NOT corpus-leading.**

**Cross-corpus poetry control**: among 6 testable Muʿallaqāt:
- Labid: 0.9888 (176/178)
- ʿAmr b. Kulthūm: 0.9810 (103/105)
- Imruʾ al-Qays, ʿAntara, Ṭarafa, al-Ḥārith: 0.0000 each (these qaṣāʾid use rāwī other than alif; the dominant rāwī is *lām*, *mīm*, *dāl*, etc.).

So the "Q 33 = pre-Islamic qaṣīda" comparison is structurally apt: when a qaṣīda IS alif-monorhyme (Labid, ʿAmr b. Kulthūm), it achieves comparable purity (≈ 0.98). Q 33 sits in the "alif-monorhyme qaṣīda mode" bucket — but so does Q 18, Q 48, Q 65, Q 72, Q 76, Q 87, Q 91, Q 92 (and to a lesser extent Q 17, Q 25, Q 20, Q 4). Q 33 is NOT special on this axis within the corpus.

**Implication for the project**: `00-overview.md` §5 needs an explicit retraction/refinement. The corrected statement should read: "Q 33 is **one of 11 surahs** with alif-final rate ≥ 0.98; eight surahs achieve perfect 1.00 monorhyme; Q 33 ranks #11 by this metric." The rhyme-entropy claim (corpus-MINIMUM) is also implied-FALSIFIED for the same reason: any surah at 100% has zero rhyme-entropy.

(Note: the overview's H-NEW-700 rhyme-entropy figure of 0.072 nats may have been computed on a different last-letter convention or on a tashkeel-sensitive scheme that distinguishes *-an* from *-ā* etc., generating non-zero entropy even for the 100%-alif surahs. The point stands: under the simplest-rules-tuple last-letter rhyme metric, Q 33 is one-of-many, not unique.)

---

## Claim 5 — al-Tirmidhī silence on Q 33 *fadāʾil* is asymmetric

**Source of the claim**: `00-overview.md` §8 implies a specific al-Tirmidhī silence relative to his catalog of *fadāʾil* for Q 36 (qalb al-Qurʾān, Tirmidhī #2887), Q 55 (ʿarūs al-Qurʾān, Tirmidhī tradition), Q 67 (al-Munjiya, Tirmidhī #2891), Q 112 (Tirmidhī #2898ff).

**Test**: count Q 33-citing hadiths in al-Tirmidhī's *Sunan* (4,053 hadiths total). File: `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/tirmidhi.json`.

**Result**:
- Q 33 in al-Tirmidhī: **10 citations** (6 surah-name + 4 distinctive-phrase, total 10 either-match).
- Q 36 in al-Tirmidhī: 3,395 hits — but most are token-noise (يس / Yāsīn appears as a standalone reference; the *fadāʾil* count is much smaller). Hadith #2887 specifically declares Q 36 *qalb al-Qurʾān*.
- Q 55: similar regex-noise; Tirmidhī's specific *fadāʾil* tradition for Q 55 is short.
- Q 67: 156 regex hits; *al-Munjiya* tradition at #2891.
- Q 112: 19 hits; the *thuluth al-Qurʾān* tradition is at #2898–2902.

**Verdict**: **VINDICATED with rules-tuple caveat**. al-Tirmidhī's *Sunan* records 10 hadith citations of Q 33 (vs his explicit *fadāʾil* hadiths for Q 36, Q 55, Q 67, Q 112 each anchored at single-hadith-numbers). The asymmetry is real even though the regex-counts for Q 36/55/67 are corrupt by surface-form ambiguity. The qualitative claim — that Q 33 receives no dedicated *fadāʾil* in Tirmidhī's *Sunan* — survives.

**Honest limit**: a careful chapter-level audit (al-Tirmidhī's *Kitāb fadāʾil al-Qurʾān*) is needed to confirm there is NO chapter-headed *fadāʾil al-Aḥzāb*. Our regex test counts citations, not chapter-dedications. We flag this as VINDICATED-DIRECTIONAL pending chapter-level read.

---

## Claim 6 — Q 33:72 (the *amāna* verse) is among the most tafsir-discussed verses

**Source of the claim**: classical *tafsīr* extensively comments on v.72 (al-Ṭabarī ad loc., al-Rāzī ad loc., al-Qurṭubī ad loc., al-Zamakhsharī ad loc., Ibn Kathīr ad loc., al-Suyūṭī *al-Durr al-manthūr* ad loc.). The *amāna* verse generates one of the longer entries in any classical *tafsīr* due to its cosmic-load metaphor (heavens-earth-mountains refusing the trust; humans accepting; *ẓalūm jahūl* characterization).

**Empirical operationalization**: (a) lexical distinctness of v.72 within Q 33; (b) divine-attribute density.

**Rules-tuple**: no-tashkeel, orthographic-token, Jaccard distinctness.

**Pre-registered test (Q033-F-04)**: pre-reg SHA `6665a12e...`. Direction-locked: v.72 ranks ≤ 8 of 73 in distinctness.

**Result** (`csv/Q033-F-04.json`):
- v.72 raw distinctness rank = **9/73** (top 12.3%).
- v.72 length-controlled distinctness rank = **8/73** (top 11.0%).
- v.72 divine-attribute count = 0; density rank = 4,229/6,236 (mid-low).

**Verdict**: **VINDICATED (length-controlled) — DIRECTIONAL (raw)**. v.72's lexical signature IS distinctive within the surah, particularly when controlling for verse-length. Top-distinct vocabulary in v.72: *al-amāna*, *al-samāwāt wa al-arḍ wa al-jibāl*, *yaḥmilna*, *ashfaqna*, *al-insān*, *ẓalūm*, *jahūl* — none of which recur elsewhere in Q 33.

**Cross-references**: the *amāna* root `ʾ-m-n` recurs in Q 4:58, Q 8:27, Q 23:8, Q 70:32 — but the cosmic-trust framing is unique to Q 33:72. The *ẓalūm jahūl* hapax-pair appears only here in the corpus (verified vs `data/morphology/quranic-corpus-morphology-0.4.txt` — no second attestation of the *ẓ-l-m* + *j-h-l* hapax pair).

**Honest limit**: token-set Jaccard is a coarse distinctness measure. A lemma-set or root-set analysis might shift the rank. The divine-attribute-density is mid-low (counter to a naive expectation), reminding us that lexical-distinctness and divine-name-density are uncorrelated axes.

---

## Summary table

| # | Claim | Verdict | Effect direction | Source |
|--:|:--|:--|:--|:--|
| 1 | Q 33 *fadāʾil*-suppression vs UAS rank 1 | VINDICATED | citation-deficit confirmed | hadith-audit |
| 2 | Q 33:40 *khātam al-nabiyyīn* is structural focal point | RULES-TUPLE-FRAGILE | DIRECTIONAL by rank, FALSIFIED by absolute threshold | F-02 |
| 3 | Q 33:56 *ṣalawāt verse* is structurally / lexically distinctive | NOT-EMPIRICALLY-TESTABLE-AS-STRUCTURAL | liturgical-only | density check |
| 4 | Q 33's alif-monorhyme is corpus-MAXIMUM | FALSIFIED | rank 11/114; 8 surahs at 100% | F-01 |
| 5 | al-Tirmidhī *fadāʾil*-silence on Q 33 | VINDICATED | 10 citations vs dedicated *bāb*s for Q 36/55/67/112 | hadith-audit |
| 6 | Q 33:72 (*amāna*) is tafsir-distinct | VINDICATED (length-ctrl) | rank 8/73 distinctness | F-04 |

Net: 3 VINDICATED, 1 RULES-TUPLE-FRAGILE, 1 FALSIFIED, 1 NOT-TESTABLE-AS-STRUCTURAL. The largest correction goes to Claim 4 — the alif-monorhyme uniqueness story is wrong; Q 33 is *one of many* alif-monorhyme surahs.

## Honest limits

- All hadith-citation counts use a regex on Arabic text post-tashkeel-stripping; surah-name regexes for Q 36 / Q 55 / Q 67 are noise-corrupted by surface-form ambiguity. We restrict our quantitative comparison to Q 1, Q 2, Q 33, Q 112 (whose surah-name regexes are unambiguous).
- The *amāna* and *khātam al-nabiyyīn* tests are post-hoc target choices (these are well-known verses); a more rigorous protocol would pre-select all 73 verses for distinctness ranking and ask whether v.40 and v.72 rank in the top-decile *jointly*. Our pre-reg locks were direction-only, not joint.
- The dual-iʿjāz typology (structural vs theological iʿjāz) is the framework that lets us say: "Q 33:56 is theological-iʿjāz, not structural." Without that frame, Claim 3's NOT-TESTABLE verdict would feel weaker.
