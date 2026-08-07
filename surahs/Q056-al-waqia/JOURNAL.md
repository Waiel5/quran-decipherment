---
surah: 56
file_type: journal
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 8-file template + 5 pre-registered tests executed
---

# Q 56 al-Wāqiʿa — Investigation Journal


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

## Session 2026-05-07 — Q056-al-waqia-specialist

### 0. Pre-flight reading completed

- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` ✓
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` ✓
- `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` ✓
- `/Users/grey/Downloads/quran/surahs/Q055-al-rahman/00-overview.md` ✓ (neighbor reference)
- `/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` ✓ (full incl. amendment §13)

### 1. Empirical anchors loaded (all from `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/`)

- h-new-111: Q 56 mean FR-distance = 1.0202 (rank 92/114)
- h-new-590: Q 56 Δ%ile = +1.33 pp (WEAK_OUTLIER, window 53-59)
- h-new-700: Q 56 within compression-tail at s=56
- h-new-720: Q 56 → Q 57 = 0.2274 (rank 17/113, 2.74% of TSP residual)
- h-new-750: sig_A = -0.057, sig_B = +0.061
- h-new-840: UAS rank 75/114

### 2. Pre-registrations (all SHA-locked)

| Test | SHA |
|:--|:--|
| Q056-F-01 (3-class ring) | f5583581e6b14d2fa19a87fc278463ae2f4f47ab36cbb1fd7dd4cfb51cd6882c |
| Q056-F-02 (Sābiqūn vocab) | 2a21f274e459cd1244d7f7d72d4df7fac144830a164ec98a6b63bda9db6b018b |
| Q056-F-03 (META-OATH rate) | 93625801acf90a9667638b8163e6f1d6203538734cd25fa5ca70931259dfbb80 |
| Q056-F-04 (cosmic density) | 662f6b175d98c43c73495ecedd5a0ce6c6942810e49bde2d0d67506d9a6f7d27 |
| Q056-F-05 (deathbed concentration) | 9bae02fa413bb6b3ef9060ea5857dc0ce070a2ac659e6530df62b3d9bee1361a |

### 3. Test execution log

#### Q056-F-01 — 3-class RING ARCHITECTURE
- Pre-reg SHA verified at runtime ✓
- Seed 20260507, n_perm 10000, Bonferroni-3 α_bon=0.0167
- **Result: NULL (0/3 cells pass)**
- Direction reversal in F-01.a (A.1 ↔ B.1 J=0.0164 < null mean 0.0223). Pre-commit honored — published with prominence.
- LABEL-level ring (al-muqarrabūn, aṣḥāb al-yamīn) is real; FULL-VOCABULARY ring is not.

#### Q056-F-02 — Sābiqūn vocab uniqueness
- Pre-reg SHA verified ✓
- **Result: STRONGLY VINDICATED**
- 26 rare tokens (corpus_count ≤ 5), **10 corpus-hapax** in vv 10-26.
- Pre-commit threshold: 3 rare tokens. Effect: 8.7× threshold.

#### Q056-F-03 — META-OATH device rate
- Pre-reg SHA verified ✓
- **GARDEN-OF-FORKING-PATHS DISCLOSURE**: Initial regex anchored to `^فلا أقسم` failed to match Q 56:75 because the verse text starts with the ornamental rukūʿ-marker `۞`. The 199-verse-corpus contains these markers as PRESENTATION DETAILS (not content graphemes per the rules-tuple). Script amended to strip ornament markers before regex anchoring; this is a mechanical fix, NOT a direction-change or operational-definition shift. Pre-disclosed in script comment block; the test direction (META-OATH count ≤ 3) was unchanged.
- **Result: VINDICATED** — META-OATH found in Q 56, Q 75, Q 89 (count = 3, at upper boundary of pre-committed 1-3 range).

#### Q056-F-04 — Cosmic-time-marker density
- Pre-reg SHA verified ✓
- **Result: NULL**
- Q 56 rank = 8/114. Pre-commit threshold: rank ≤ 5.
- Honest limit: pre-committed token set excluded WAW-prefixed forms; under stricter stem-matching rules-tuple, Q 53 al-Najm (currently scored 0) would move up. The pre-committed rule-tuple is the published verdict.

#### Q056-F-05 — Deathbed-hadith verse-citation concentration
- Pre-reg SHA verified ✓
- **Result: NULL**
- 31.6% of citations in vv 83-96 (above uniform-random 14.6% but below 50% threshold).
- Honest interpretation: deathbed/Ibn Masʿūd association is REAL but NOT narrowly localized to vv 88-94; concentration spreads vv 75-91 with peaks at 79, 83, 87.

### 4. Hadith corpus audit

- 9 canonical books searched for الواقعة (Arabic, n=4 unique hits) and `Waqi`-variants (English, n=8 incl. false positives)
- Excluded false positives (Tirmidhī #1775 is "Wāqid" name, Bukhārī #4224 is Tabūk story).
- Verified 4 Q56-explicit canonical hadiths: Tirmidhī #3381, Dārimī #627, Dārimī #2101, Mālik #478.

### 5. Critical hadith corrections to user-prompt seed

The user-supplied seed contained TWO HADITH-NUMBER ERRORS that the project's anti-hallucination protocol caught:

1. **Tirmidhī #2987 — "the Prophet had Q 56 read at his deathbed"** — INCORRECT. Tirmidhī #2987 is verified on disk (`tirmidhi.json`, idInBook=2987) and is a *general* hadith on Quranic recitation (the proficient reciter is with the noble angels; the struggling one earns two rewards). Topic NOT Q 56-specific, NOT deathbed-specific. The actual Tirmidhī Q 56 hadith is **#3381** (gray-hair hadith including Q 56).

2. **"a Sahih hadith reports the Prophet had Q 56 read at his deathbed"** — UNVERIFIED. There is no canonical 9-book hadith for the Prophet's-OWN-deathbed-Q 56 tradition. The classical attestation is the IBN MASʿŪD-deathbed story (Ibn Masʿūd recited Q 56 on his OWN deathbed; chain ḍaʿīf), distinct from "the Prophet's deathbed."

These corrections are documented in `04-hadith-corpus.md` §3.

### 6. Tafsir survey

- 6 mufassirūn surveyed (al-Ṭabarī, al-Qurṭubī, Ibn Kathīr, al-Rāzī via Maarif-ul-Qurʾān, al-Suyūṭī al-Itqān, al-Biqāʿī, al-Zamakhsharī, en-Jalālayn) — disk-verified citations only.
- Key disagreement on Q 56:76: al-Rāzī / Ibn Kathīr / Jalālayn read it as META-OATH (self-reference); al-Zamakhsharī reads it as cosmic-magnification of the sworn-by-objects.

### 7. 8-file template completion

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md (this file)

### 8. Garden-of-forking-paths log

| Decision point | Choice | Rationale |
|:--|:--|:--|
| F-01 null distribution | Token-shuffle within block-A (preserving block sizes) | Most principled given tiny B-block sizes; alternative (label-permutation of B) gives only 6 perms |
| F-03 ornament-marker stripping | Strip ۞ ۚ ۖ ۗ ۘ ۙ ۛ before regex | Presentation-detail per rules-tuple; pre-disclosed; does NOT alter direction |
| F-03 broader vs narrower scan | Both reported; verdict on broader (3 surahs vs 2) | Pre-reg specified META-OATH structure; broader scan captures the canonical 3-surah cluster identified by al-Rāzī |
| F-04 token set | Use pre-committed token set (no WAW-prefix forms) | Pre-commit discipline; stricter rules-tuple recovery noted as honest limit |
| F-05 deathbed-context filter | Tafsir text containing "Ibn Masʿūd" / "deathbed" / "ḥulqūm" | Best-available proxy for deathbed-context; small N caveat documented |

### 9. Discipline checks (pre-publication)

- [x] All pre-reg SHAs locked and verified at runtime
- [x] Direction-of-effect pre-committed for all 5 tests
- [x] Bonferroni applied (F-01 k=3); single-test α=0.05 for F-02, F-03, F-04, F-05
- [x] Equal NULL prominence in 06-novel-findings.md
- [x] Honest limits sections in every file
- [x] Classical citations are scholar+work+passage+disk-path
- [x] No invented hadith numbers; user-prompt errors corrected (Tirmidhī #2987 ≠ Q 56)
- [x] Rules-tuple sensitivity documented (F-04, Q 53 case)

### 10. Verdict per quality gates

- Q056-F-01: NULL — direction reversed in F-01.a; published with prominence
- Q056-F-02: VINDICATED-CONFIRMED (single-test, but effect 8.7× threshold)
- Q056-F-03: VINDICATED at upper boundary; pass-directed (single-test α=0.05)
- Q056-F-04: NULL with honest rules-tuple sensitivity note
- Q056-F-05: NULL with directional information (citations enriched but below threshold)

No findings promoted to corpus-wide H-NEW-NNNN status from this investigation. Per-surah Q056-F-NN local IDs apply.

### 11. Output artifacts

- `surahs/Q056-al-waqia/` — 8 files (this directory)
- `surahs/Q056-al-waqia/preregs/` — 5 SHA-locked pre-regs
- `surahs/Q056-al-waqia/scripts/` — 5 Python test scripts
- `surahs/Q056-al-waqia/csv/` — 5 JSON results

### 12. Recommendations for future Q 56 work

1. Run F-01 secondary on QAC root-tokens (lemma-level) — may recover the ring at root-level (q-r-b root for muqarrab/qarīb across A.1 / B.1).
2. Pre-register a corpus-wide test for "double-surah-end-marker" rarity (Q 56:96 / Q 69:52 *fa-sabbiḥ bi-smi rabbika ʾl-ʿaẓīm*).
3. Cross-surah Q 56 ↔ Q 75 ↔ Q 89 META-OATH cluster cohesion test (FR-content distance among the 3 surahs).
4. Verify Aḥmad b. Ḥanbal *Musnad* Jābir b. Samura *fajr*-Q 56 hadith primary chain — requires obtaining full Musnad corpus.
5. Investigate the 6th-cell candidate ("boundary surah / Hijra-kink keystone"); seek a comparable surah for replication.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
