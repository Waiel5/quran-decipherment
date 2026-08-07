---
surah: 74
file_type: journal
date_started: 2026-05-09
specialist_owner: Waiel Al-Shujaa
prereg_seed: 20260509
status: complete (8-file template + 4 SHA-locked tests)
---

# Q 74 al-Muddaththir — Specialist Journal


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

## 2026-05-09 — Run 1 (specialist landing)

### Pre-flight
Read `HANDOFF/04-DISCIPLINE.md`, `HANDOFF/01-WHAT-WE-KNOW.md`, `MASTER-FINDINGS-LEDGER.md` §1-3 and §10.34 (H-NEW-1190 *wa-mā adrāka mā* cluster). Confirmed Code-19 REFUTED across all 13+ axes per `MASTER-LEDGER` and `findings/phase-a-replications/code19-khalifa-full-audit.md`. Confirmed Q 74 is one of 10 surahs in the H-NEW-1190 cluster (formula at v.27: *wa-mā adrāka mā saqar*). Confirmed Q 73→Q 74 is one of the 13 empirically-seamless mushaf-transitions (H-NEW-1240, ranked 7/13 most-seamless).

### Tests run
4 SHA-locked pre-registered tests:

1. **Q074-F-01 — Code-19 / Khalifa Q 74:30 RECAP audit** (RECAP-CONFIRMED-NULL)
   - 13 claim-axes adversarially audited; 8 FAILED, 1 RULES-TUPLE-FRAGILE, 1 VERIFIED-TEXTUAL, 3 VERIFIED-TRIVIAL
   - 11 reasonable NEW operationalizations of Q 74:30 → none yields 19-residue at chance-improbable rate
   - The single Q 73+Q 74 verse total = 76 = 4×19 coincidence is small-integer (Bonferroni-NULL per H-NEW-237)
   - Output: `csv/Q074-F-01.json`

2. **Q074-F-02 — Q 74 within H-NEW-1190 cluster FR centrality rank** (CONFIRMED, replicates H-NEW-1190 result)
   - Cluster {69, 74, 77, 82, 83, 86, 90, 97, 101, 104} replicates at p=0.00030 (vs original 0.00068)
   - Q 74 ranks **9/10** in cluster centrality — peripheral member (with Q 69 = 10/10)
   - Reveals cluster has 2-tier structure: CORE {Q 82, 83, 86, 90, 97, 101, 104} + PERIPHERY {Q 69, 74, 77}
   - Q 74's nearest cluster-member: Q 104 al-Humaza (FR=0.6919)
   - Output: `csv/Q074-F-02.json`

3. **Q074-F-03 — Q 73-Q 74 vocative-pair cohesion** (PARTIAL-CONFIRMED)
   - 10 yā-ayyuhā opener surahs: {4, 5, 22, 33, 49, 60, 65, 66, 73, 74}
   - Q 73-Q 74 = SINGLE-TIGHTEST pair within 10-vocative cluster (rank 1/45, FR=0.7614, -17.6% below corpus mean)
   - Corpus level: percentile 17.76 (moderately tight, not extreme)
   - NOT mutual-nearest in corpus (both nearest = Q 112 al-Ikhlāṣ, the corpus FR-centroid)
   - Rhyme axis NOT cohesive (Q 73 ا-monorhyme 90%; Q 74 ر-monorhyme 55%)
   - Honest limitation: 97.96% of random 10-subsets contain a tighter min-pair → signal is intra-cluster ranking, not corpus-rare
   - Output: `csv/Q074-F-03.json`

4. **Q074-F-04 — Saqar root corpus-wide hapax check** (CONFIRMED)
   - Saqar (سقر, Hellfire-name) corpus-EXACT count: 4 instances total
   - Q 74:26 + 74:27 + 74:42 + Q 54:48 → Q 74 owns 3/4 = 75%
   - Length-weighted permutation null p<0.0001 (10K perms)
   - Uniform null p=0.0001
   - Output: `csv/Q074-F-04.json`

### Honest disclosures
- Q074-F-03 partial-confirmed: 1/45 intra-cluster rank is real, but corpus-level percentile is only 17.76% — pair tightness is not corpus-rare.
- Q074-F-01 recap is descriptive: catalogues prior REFUTATIONS rather than running a fresh independent test on the Q 74:30 anchor.
- Q074-F-04: orthographic-token-only test. The QAC `LEM:saqar` confirms exactly the same 4 instances at the lemma level (independently verified).

### Cross-references generated
- H-NEW-1190 cluster: confirmed cluster cohesive at p=0.00030 (replicates H-NEW-1190 p=0.00068)
- H-NEW-1240 13-seamless-seams: Q 73→Q 74 = rank 7/13 most-seamless (delta_raw = -0.0289)
- H-NEW-1220 FR-centroid ranking: Q 74 = rank 42/114 (mid-pack, mean_d=0.8743); Q 74's nearest in corpus = Q 112 al-Ikhlāṣ (d=0.6675)
- H-NEW-840 UAS: Q 74 = rank 54/114 (UAS=-0.194)
- H-NEW-590 outlier-strength: Q 74 = NULL (delta_pct=-3.43, p_greater=0.8942)
- H-NEW-750 iʿjāz-signature: Q 74 sig_A=+1.31 rank 21/114 (HIGH-CONTENT-DIVERSITY); sig_B=+0.46 rank 44/114
- Bukhari #4714, #4716 + al-Suyūṭī Itqān القول الثاني → Q 74 al-Muddaththir as alternative-first-revealed-surah view
- al-Ṭabarī ad loc. (Q 74:30): the 19 = خزنة النار (angels guarding Hell); classical interpretation unanimous

### Files produced
- `00-overview.md` — name, verses, opening, structure
- `01-empirical-profile.md` — full H-NEW metrics integrated
- `02-content-analysis.md` — verse-by-verse + thematic blocks
- `03-tafsir-survey.md` — al-Ṭabarī, al-Rāzī, al-Qurṭubī, Ibn Kathīr, al-Zamakhsharī, al-Suyūṭī, al-Bāqillānī
- `04-hadith-corpus.md` — 9-book citations including Bukhari first-revealed pair, asbāb al-nuzūl al-Walīd
- `05-classical-claims-audit.md` — Code-19 RECAP, classical first-revealed dispute, 19-angels exegesis
- `06-novel-findings.md` — 4 SHA-locked tests + their detailed methodology
- `07-cross-references.md` — H-NEW links + Q 73 sister + cluster-network
- `JOURNAL.md` — this file
- 4 pre-regs in `preregs/`
- 4 scripts in `scripts/`
- 4 JSON outputs in `csv/`

### Commit-protocol note
Per `feedback_github_commit_protocol.md`, deliverable will be committed as Waiel without third-party-agent references; all paths under `surahs/Q074-al-muddaththir/`; any large auto-generated artifacts to be reviewed before stage.
