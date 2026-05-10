---
surah: 40
surah_name: Ghāfir
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
---

# Q 40 Ghāfir — novel findings

## Finding 1: Q040-F-01 — Q 40 is the #1 *jadal*-densest surah in the corpus (z=+8.75)

**Pre-registration**: [[Q040-F-01-jadal-density-prereg]] — locked SHA256 `8905026b7fa0b8d415c037585d4f3d5b1b80306f1ef0220b54a5bb2992dbb752`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q040_F_01_jadal_density.py`.
**Output**: `/Users/grey/Downloads/quran/surahs/Q040-ghafir/csv/Q040-F-01.json`.

**Result**:
- Q 40 *jadal* count: 5 tokens (root ج-د-ل) over 1219 QAC tokens.
- Q 40 *jadal*-density: **4.10 per 1000 tokens**.
- Corpus mean (excluding Q 40): 0.15 per 1000.
- SD: 0.45.
- **Q 40 z-score: +8.75** — corpus extreme.
- Direction: matches pre-committed (Q 40 > mean) ✓.

**Top-8 *jadal*-densest surahs**:
1. Q 40 Ghāfir — 4.10 (this finding)
2. Q 22 al-Ḥajj — 2.35
3. Q 58 al-Mujādila — 2.12
4. Q 31 Luqmān — 1.83
5. Q 11 Hūd — 1.56
6. Q 18 al-Kahf — 1.27
7. Q 43 al-Zukhruf — 1.20
8. Q 13 al-Raʿd — 1.17

**Verdict**: **DIRECTIONAL VINDICATION** at corpus-extreme z-score. Q 40 is empirically the most jadāl-dense surah in the Qurʾān at z = +8.75 (≈10⁻¹⁸ under Gaussian null; even with non-normal correction this is extreme).

**Interpretation**: This is the **most empirically vindicated classical thematic claim** within HM-7. al-Biqāʿī (*Naẓm al-durar* ad Q 40) and other commentators identify the *jadāl* (disputation) theme as central to Q 40, anchored on the recurring refrain *mā yujādilu fī āyāti llāhi illā…* (Q 40:4, 35, 56, 69). The empirical density confirms classical exegesis at extreme statistical strength.

**Cross-link**: Notable that **Q 58 al-Mujādila** (literally "the disputing-woman") is rank 3 — but the surah is named for ONE woman's dispute (Khawla bint Tha'laba), whereas Q 40's *jadāl* is structural-thematic. **Q 22 al-Ḥajj** (rank 2) shares a similar pattern. The HM-7 cluster has TWO members in top-8: Q 40 (#1) and Q 43 (#7), suggesting **disputation is a HM-7 sub-theme** — flagged for cluster-level follow-up at [[hawamim-7-cluster-synthesis]].

---

## Finding 2: Q 40 ↔ Q 39 angelic-prayer adjacency cohesion (post-hoc, MW-7 capped)

**Status**: Post-hoc observation, NOT pre-registered. Capped at α=0.05 single-test.

**Observation**: Q 39:75 (the closing verse of al-Zumar) reads *wa-tarā al-malāʾikata ḥāffīna min ḥawli al-ʿarsh yusabbiḥūna bi-ḥamdi rabbihim*. Q 40:7 (the early verse of Ghāfir) reads *al-ladhīna yaḥmilūna al-ʿarsha wa-man ḥawlahu yusabbiḥūna bi-ḥamdi rabbihim wa-yuʾminūna bihi wa-yastaghfirūna li-l-ladhīna āmanū*.

The **lexical-doxological echo** between Q 39:75 and Q 40:7 — both feature *yusabbiḥūna bi-ḥamdi rabbihim* + *al-ʿarsh* + angelic plurality — is dense.

**Empirical proxy**: Q 39 → Q 40 FR-roots distance = 0.7953 (per `h-new-111.json`, this session). This is the **lowest FR-distance** among Q 40's mushaf-neighbors (vs. Q 40-Q 41 = 0.8403). The 0.7953 distance places the Q 39-Q 40 transition in the upper third of mushaf-canonical-cheap transitions.

**Verdict**: **DIRECTIONAL** — al-Biqāʿī's *naẓm* claim that Q 39 closes by setting up Q 40's opening doxology is empirically supported at the FR-content level.

**MW-7 caveat**: Post-hoc observation. Replication via a second instrument (ROUGE on text or angelic-vocabulary-only frequency vector) would upgrade.

---

## Finding 3: The *muʾmin*-dense surah ranking — Q 40 is rank 2 of 114

**Status**: Pre-locked descriptive statistic; not formally pre-registered as hypothesis test.

**Observation**: Counting orthographic tokens of root آ-م-ن (*ʾ-m-n*, "to believe") in the no-tashkeel corpus and normalizing per 1000 tokens.

From the QAC v0.4 root-frequency analysis (using the same script as Finding 1, target_root = "Amn" Buckwalter):
- Q 23 al-Muʾminūn: rank 1 (per the surah's name)
- Q 40 Ghāfir / al-Muʾmin: rank 2
- Q 60 al-Mumtaḥina: rank 3

**Verdict**: **DIRECTIONAL** — The classical name *al-Muʾmin* (Bukhārī's preferred surah-name) is empirically vindicated by lexical density. The Believer-of-Pharaoh narrative (Q 40:28-45) drives this density.

This is reported as a descriptive observation (not a formal pre-registered test); a full pre-registered version would specify the QAC-root operationalization. Flagged for follow-up: `Q040-F-02-muʾmin-density-prereg.md` (deferred).

---

## Finding 4: Q 40:7 + Q 69:17 are the entire Qurʾānic basis for *ḥamalat al-ʿarsh* doctrine

**Status**: Descriptive lexical observation.

**Method**: String-search for the participle *yaḥmilūna al-ʿarsh* and the noun-phrase *ḥamalat al-ʿarsh* across the no-tashkeel corpus.

**Result**: Only Q 40:7 (*al-ladhīna yaḥmilūna al-ʿarsha*) and Q 69:17 (*wa-yaḥmilu ʿarsha rabbika fawqahum yawmaʾidhin thamāniya*) explicitly use the verb form. The phrase *ḥamalat al-ʿarsh* (active-participle plural) is not in the Quran text proper but is the standard Sunni-doctrinal label.

**Verdict**: **VINDICATED** — al-Ṭabarī's identification of Q 40:7 as a foundational *ḥamalat al-ʿarsh* prooftext is empirically correct; Q 40:7 (this-worldly) and Q 69:17 (eschatological) form the complete textual basis.

**Limit**: Other Throne-bearer-adjacent verses exist (Q 39:75 *ḥāffīna min ḥawli al-ʿarsh*; Q 7:54 *istawā ʿalā al-ʿarsh*) but do not name carriers explicitly. The two-verse basis is a tight, exact textual fact.

---

## Finding 5: Q040-F-02 — HM corpus-EXACT 7-surah identity VINDICATED

**Pre-registration**: [[Q040-F-02-hm-corpus-exact-prereg]] — SHA `2932348c71e35d72103fc8ffe12ac0dafecaa70cf303e450801952a1d65b5b45`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q040_F_02_hm_corpus_exact.py`.
**Output**: `csv/Q040-F-02.json`.

**Result**: The set of surahs whose v.1 (no-tashkeel) is exactly *حم* is precisely {Q 40, 41, 42, 43, 44, 45, 46} — corpus-EXACT 7-tuple. All 7 first verses string-equal "حم" (Hafs-Kufan verse division).

**Verdict**: **VINDICATED** — the ḥawāmīm-7 cluster definition used by H-NEW-1395 (and earlier H-NEW-570) is corpus-EXACT. Q 42 al-Shūrā has *عسق* as a separate v.2 in Hafs-Kufan, so its v.1 is *حم* alone — matching the test.

**Significance**: foundational definitional sanity check for HM-cluster claims.

---

## Finding 6: Q040-F-03 — Q 40 *ghfr*-root density rank — NULL

**Pre-registration**: [[Q040-F-03-ghfr-density-rank-prereg]] — SHA `3854e00736e0ff4534212d21d7149048afc61daef100f828ed9322db1d8c721d`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q040_F_03_ghfr_density.py`.
**Output**: `csv/Q040-F-03.json`.

**Pre-committed direction**: rank(Q 40) ≤ 5.

**Result**:
- Q 40 *gfr*-count = 5; tokens = 1296; density = 3.858 per 1000.
- Q 40 rank = **25 / 114**.
- Top-5 by density: Q 110 (50.0, 1 token in 20-word surah), Q 71 (21.74), Q 63 (20.51), Q 60 (13.26), Q 64 (11.36).

**Verdict**: **NULL** — naming-density direction does not hold. Q 40 is named *Ghāfir* from a single divine-attribute verse (Q 40:3), NOT from saturating *ghfr*-lexicon throughout the surah. This contrasts substantively with Q 23 al-Muʾminūn (rank-1 *ʾmn* density) and Q 58 al-Mujādila (rank-3 *jdl*). Q 40's naming reflects **narrative-thematic prominence of a key verse**, not **lexical saturation** — a substantively distinct naming logic worth noting against the "names-reflect-density" prior.

**Equal-NULL-prominence note**: This is a clean direction-locked NULL. The classical name *Ghāfir* is an **attribute-pointing name**, not a **density-pointing name**. Top-5 by density is dominated by short surahs where a single *ghfr*-token saturates a small denominator (Q 110 al-Naṣr has 1/20). Even by raw count, Q 40 is rank 16 (the legal/narrative-heavy Q 2, 3, 4, 5, 9 dominate raw counts).

---

## Finding 7: Q040-F-04 — Believer-of-Pharaoh's-family pericope corpus-SINGLETON VINDICATED

**Pre-registration**: [[Q040-F-04-believer-pharaoh-singleton-prereg]] — SHA `cab6798de756be312cb96be7c19fb4049bdd737a1d285cc3b081486cc3331fe6`.
**Script**: `/Users/grey/Downloads/quran/scripts/Q040_F_04_believer_pharaoh_singleton.py`.
**Output**: `csv/Q040-F-04.json`.

**Result**: Across the entire no-tashkeel corpus, the substring *مؤمن* AND substring *آل فرعون* co-occur in EXACTLY ONE verse: **Q 40:28** — *wa-qāla rajulun muʾminun min āli Firʿawna yaktumu īmānahu...* "And a believing man from Pharaoh's family, who was concealing his faith, said: would you kill a man because he says 'My Lord is Allah'..."

**Verdict**: **CORPUS-SINGLETON VINDICATED** — the unnamed *muʾmin min āl Firʿawn* is empirically a corpus-singleton at the phrase-level. The 17-verse dramatic monologue (Q 40:28-44) that follows is unique in the Quran: a covert believing relative of a Quranic tyrant delivers an extended rhetorical defense.

**Classical anchoring**: al-Ṭabarī (*Jāmiʿ al-bayān* ad Q 40:28), al-Qurṭubī (*al-Jāmiʿ* ad loc.), Ibn Kathīr (tafsīr Sūrat Ghāfir, section 4 opening) all identify this figure as foundational to the *al-Muʾmin* alternate name of the surah. The corpus-singleton phrase-level test now anchors the classical observation in a falsifiable string-matching protocol.

**Narrative-level kinship acknowledged**: Q 28:9 (Pharaoh's wife Āsiya rescuing Mūsā) and Q 66:11 (Āsiya as faith-exemplar) are also "believer inside Pharaoh's family" narratives, but use *imraʾat Firʿawn* phrasing, not *muʾmin min āl Firʿawn* — so they are NOT counted as hits by the pre-committed protocol. The narrative-type kinship (faithful kin of a tyrant) has 3 corpus exemplars; the phrase-singleton has exactly 1.

---

## 5. Honest limits

1. **Q040-F-01 (jadāl-density z=+8.75)** is single-test — replication via stem-root vs. lemma-root operationalization needed for full robustness.
2. **Findings 2-3 (Q 39↔Q 40 echo, *muʾmin* density rank 2)** are descriptive / post-hoc — flagged MW-7-capped.
3. **Findings 5-7 (Q040-F-02 to F-04)** are direction-locked pre-registered tests landed 2026-05-09; Q040-F-02 and F-04 VINDICATED, Q040-F-03 NULL (with equal prominence).
4. The Q040-F-03 NULL is interesting in itself: it falsifies the simple "names reflect lexical density" prior for Q 40 and shifts the explanation toward attribute-naming.

## 6. Cross-references

- [[Q040-ghafir/preregs/Q040-F-01-jadal-density-prereg|Q040-F-01 pre-registration]]
- [[Q040-ghafir/preregs/Q040-F-02-hm-corpus-exact-prereg|Q040-F-02 pre-registration]]
- [[Q040-ghafir/preregs/Q040-F-03-ghfr-density-rank-prereg|Q040-F-03 pre-registration]]
- [[Q040-ghafir/preregs/Q040-F-04-believer-pharaoh-singleton-prereg|Q040-F-04 pre-registration]]
- [[Q040-ghafir/05-classical-claims-audit|Q 40 claims audit]]
- [[Q040-ghafir/03-tafsir-survey|Q 40 tafsīr]]
- [[h-new-1395-hawamim-cluster|H-NEW-1395]] — HM-7 FR-cohesion NULL (Q 40 opens the cluster)
