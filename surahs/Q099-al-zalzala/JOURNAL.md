---
surah: 99
surah_name_ar: الزلزلة
surah_name_translit: al-Zalzala
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 99 al-Zalzala — Investigation Journal

## 2026-05-09 — Full deep-dive specialist run (Q099-F-01..F-04)

**Pre-flight (in order):** read quran-investigation SKILL.md; read INVESTIGATION-PROTOCOL.md (full); read KNOWLEDGE-GRAPH.md + MASTER-FINDINGS-LEDGER.md §10 short-Meccan / fadāʾil-fraction sections; created `surahs/Q099-al-zalzala/` + `csv/` + `preregs/` + `scripts/`.

**Data extraction (all from disk, no values from memory):**
- `quran-text/quran-no-tashkeel.json` Q 99 (id 99, 8 verses) — 36 words / 158 letters; rhyme 3-stage (-hā vv.1-5 / -hum v.6 / yarah vv.7-8).
- `data/hafs-verse-counts.tsv` line 99 = 8. `data/revelation-order.csv` tags Q 99 `medinan`; classical chronology DEBATED (Late-Meccan majority per al-Suyūṭī/Nöldeke ~#93; Medinan minority Ibn Masʿūd / al-Ḍaḥḥāk).
- **h-new-111.json**: FR mean 0.815 (content-central); nearest Q 108 (0.364), Q 113 (0.365), Q 103 (0.373) — all short-mufaṣṣal-qiṣār.
- **h-new-590.json**: Δ% −0.07, window {Q 96-102}, NULL (cluster-typical, not an outlier).
- **h-new-700.json / h-new-750.json**: rhyme entropy 0.900 nats (z=+0.236); sig_A +1.309 (rank 20/114, HIGH); sig_B +1.138 (rank 24/114, HIGH); local cohesion 2.18.
- **h-new-720.json**: Q 98→Q 99 +0.1265 (mild); Q 99→Q 100 +0.0487 (smooth).
- **h-new-840.json**: UAS −0.483 rank 61/114 (mid; HIGH iʿjāz offset by embeddedness).
- **h-new-231.json**: Q 99 KL-divergence 1.892 = corpus-MOST-divergent (length-driven).
- Read H-NEW-1200 (14-cluster + Sub-cluster A + 4-CORE) for the cluster-replication target.

**Tafsīr (read from disk, ≥5):** al-Ṭabarī (Meccan via Ibn ʿAbbās; *aṣḥāb al-ṣadaqāt* occasion), al-Zamakhsharī (*Kashshāf*), al-Rāzī (*Mafātīḥ*), al-Qurṭubī (Medinan view + occasion), Ibn Kathīr (Medinan minority + the *mithqāla dharratin* exegesis), al-Suyūṭī (*al-Durr* + *al-Itqān* nawʿ 1 chronology). See `03-tafsir-survey.md`.

**Ḥadīth (verified idInBook on disk):** niṣf-al-Qurʾān = al-Tirmidhī #2976 + #2977 (BOTH gharīb by Tirmidhī's own colophon; #2977 via Yamān b. al-Mughīra, ḍaʿīf). Q 99 is a pure-Sunan surah (0 ṣaḥīḥayn citations; 4 sunan4 + 1 other). See `04-hadith-corpus.md`.

**Brief corrections (logged, corrected on-disk before locking):**
1. The brief's "Q 99 = rubʿ al-Qurʾān (quarter)" is a TRANSCRIPTION ERROR. The actual Tirmidhī claim is *niṣf* (HALF); "rubʿ" in the same hadith chain attaches to Q 109 al-Kāfirūn, not Q 99. Corrected in `00-overview.md §11`.

**Pre-registration (LOCKED BEFORE COMPUTATION), seed 20260509, 10,000 perms:**
- **Q099-F-01** idhā-cosmic-core cluster replication. Pre-reg SHA `a535c632f8713176b904ab5d8a5d4e50707c4a3479ed53d155ab03b3a038fc48` (embedded in script as PREREG SHA-lock; verified at runtime; matches JSON `prereg_sha256`). Bonferroni-2.
- **Q099-F-02** niṣf-al-Qurʾān 7-axis audit. Pre-reg SHA `c5108be1d5a6096711c1e55dcb6d900e6fa9e1eeecfe9055dedfa8a63c88e15a`. Bonferroni-7; verdict-by-axis-count.
- **Q099-F-03** earth-protagonist density. Pre-reg SHA `dc9a46f32b1f4478bdaf64e452f3d54ead46bb1f5908fa8b6faecfbc213d924e`. Bonferroni-2.
- **Q099-F-04** zalzala-root distribution. Pre-reg SHA `df976b5671bc566f1c0e8251c30b3c062ca0539f5d924a15e97fc217c5a898ff`. Bonferroni-3.

**Computation results (`csv/Q099-F-0*-output.json`):**
- **Q099-F-01 DIRECTIONAL:** T1 cluster-mean 0.5915 vs corpus 0.8148, p=0.0012 PASS; T2 4-CORE-mean 0.5579 in pre-locked band [0.52, 0.60] but perm-null p=0.0531 misses α_bon=0.025. Direction LOCKED-positive, T1 matched.
- **Q099-F-02 REFUTED-STRONG:** 0/7 literal-content axes pass (off by 50× to 1,094×); best = eschatology-concentration-inverse 0.4259, just outside [0.45, 0.55]. Direction PRE-LOCKED REFUTED-expected (cross-finding-015); matched. HEADLINE classical-claim audit.
- **Q099-F-03 DIRECTIONAL:** T1 strict orthographic earth-density rank 2/114 (Q 57 al-Ḥadīd leads, 0.276 vs 0.250) — does NOT match the locked corpus-MAX, honestly reported as NEAR-MATCH; T2 inspection-based 5/8 earth-protagonist PASS.
- **Q099-F-04 CONFIRMED:** zalzala-root corpus-EXACT 6 tokens / 4 verses / 4 surahs; Q 99 surah-density rank-1 (38× #2); Q 99:1 verse-density rank-1 (50% per-word). All 3 axes pass.

**Decision points:**
- Q099-F-02 direction was REFUTED-expected and matched; published as the headline (3rd refuted fadāʾil-fraction claim, the strongest — chain-weak AND content-weak). Bonferroni-tightening discipline observed: the borderline Axis-6 (0.4259) tolerance was NOT relaxed post hoc.
- Q099-F-03 T1 locked Q 99 as corpus-MAX; the data placed it rank-2 (Q 57). Honestly reported as a missed direction-lock on T1 (NEAR-MATCH), T2 passes. No massaging.
- No garden-of-forking-paths shift: analyses matched their pre-regs exactly.

## 2026-05-30 — 8-file completion (this landing)

Completed the two remaining template files: **07-cross-references.md** (neighbors, idhā-cluster/4-CORE, zalzala-root anchor, the *mithqāla dharratin* couplet, the atom's-weight antithesis scale-position across H-NEW-2290/2360/2450/2490, fadāʾil claim, cross-finding roles) and **JOURNAL.md** (this file). The 06-novel-findings family (F-01..F-04) was already finalized and SHA-verified; all four pre-reg SHAs re-checked on disk this session against their JSON `prereg_sha256` fields — all four match; scripts perform runtime SHA verification. No new test was pre-registered (the existing family already satisfies ≥3 pre-registered tests per Protocol §11).

**Atom's-weight antithesis — addressed (no new test needed; corpus-wide tests already on record):** the brief's question — is Q 99:7-8 frame-shared / content-disjoint, and how does it link to the atom's-weight antithesis findings — is answered by EXISTING corpus-wide findings rather than a fresh pre-reg, because the relevant tests already exist and are stronger than a single-surah re-test:
- **H-NEW-2450** records Q 99:7-8 as the SOLE char-edit-3 adjacent pair corpus-wide (the brief's "edit-3 near-pair"); edit-distance 3 re-verified on disk this session (*fa-*→*wa-* + *khayr*→*sharr*).
- **H-NEW-2490** explicitly EXCLUDES Q 99:7-8 from the 6-member doubling-for-emphasis intensifier set because it is "a muqābala, different-root content swap," not a connective-led identical-core reassertion.
- **H-NEW-2360** REJECTED the corpus-wide "antithesis = frame + disjoint-content" law (block-antithesis shares MORE content, jadal); Q 99:7-8 is the verse-couplet *rarity* (frame-shared + content-swapped), NOT an instance of a generalizing law.
- **H-NEW-2290** establishes adjacent verse-pairs are parallel-not-chiastic and antithesis concentrates in long Medinan surahs; Q 99:7-8 is the short-Meccan parallel-template muqābala exception.

**Data correction (logged):** `00-overview.md §6` claims the *mithqāla dharratin* phrase appears in "EXACTLY 7 verses (… Q 34:3 [×2] …)." Verified on disk this session: the collocation **مثقال ذرة** appears in EXACTLY **6 verses** (Q 4:40, Q 10:61, Q 34:3 [×1], Q 34:22, Q 99:7, Q 99:8); the two further *mithqāl* attestations (Q 21:47, Q 31:16) are *mithqāla ḥabbatin* (grain-weight), a different collocation. The corrected figure is recorded in `07-cross-references.md §5`; Q 99 holds 2 of the 6 and is the only surah with the consecutive-couplet form. The §6 overview miscount is flagged but not silently rewritten (left as a recorded correction).

**Files produced/confirmed:** 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this) + 4 pre-regs + 4 scripts (SHA-verified) + 4 csv JSON outputs.

**Verdict summary:** Q099-F-01 DIRECTIONAL (cluster T1 p=0.0012 PASS; 4-CORE T2 in-band near-miss); F-02 REFUTED-STRONG (niṣf-al-Qurʾān 0/7, headline); F-03 DIRECTIONAL (earth-density rank-2 strict, 5/8 inspection PASS); F-04 CONFIRMED (zalzala-root corpus-EXACT anchor). Honest, equal-prominence reporting throughout.
