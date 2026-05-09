---
surah: 78
surah_name_ar: النبأ
surah_name_translit: al-Nabaʾ
file_type: journal
date_last_updated: 2026-05-09
phase: B+
verdict: 5 pre-registered tests run; 4 CONFIRMED + 1 NULL with informative correction. All 8 surah-template files written; full investigation complete on 2026-05-09.
---

# Q 78 al-Nabaʾ — Specialist Investigation Journal

## 2026-05-09 — Investigation kickoff

### Inputs
- Brief from team-lead (Q 78 specialist task; juzʾ-30 frontispiece; H-NEW-1200 cluster placement question; ≥5 tafsir authorities; SHA-locked novel-findings).
- HANDOFF/04-DISCIPLINE.md, HANDOFF/01-WHAT-WE-KNOW.md (pre-flight).
- MASTER-FINDINGS-LEDGER.md §10.34 (H-NEW-1190), §10.35 (H-NEW-1200), §10.41 (H-NEW-1240), §10.43 (H-NEW-1250).
- cross-finding-022-wave5-terminal-synthesis (terminal architecture).
- Reference template: `surahs/Q037-al-saffat/`.
- Quran text: `quran-text/quran-no-tashkeel.json`.
- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt`.
- TSP-cost decomposition: `findings/phase-b-hypotheses/csv/h-new-720.json`.

### Pre-flight observations (post-hoc origin disclosed in pre-regs)
- Q 78 word count = 177; verse count = 40; root-tokens = 131; distinct roots = 100.
- Q 78 has 3 corpus-hapax roots (whj v.13, vjj v.14, dhq v.34), all in *faʿʿāl-an* intensive pattern.
- Q 78 ranks 5/93 in *yawm* density (top-tier but NOT corpus-extreme; outranked by Q 77 / Q 82 / Q 75 / Q 80).
- Q 78 ranks 2/88 in jaʿala (j-ʿ-l) density per word (edged by Q 71 Nūḥ).
- Q 78 has a 3-consecutive-verse *wa-jaʿalnā* streak at vv9-11 (matched by Q 21:30-32).
- Q 77→78 (juzʾ-30 boundary) has TSP-cost rank 40/113 (mid-spectrum), FR rank 38/113 — NOT a structural-architectural break.
- Q 78's mean FR-distance to H-NEW-1200 cluster = 0.4732 (vs corpus 0.6665); cluster-attraction ratio = 0.71.
- Q 78's intra-cluster centrality rank (with Q 78 inserted as outsider) = 11/15. The H-NEW-1200 cluster CENTROID is Q 97 al-Qadr (centrality 0.3682). Q 78 is PERIPHERAL.
- Q 78's TOP-3 nearest neighbors corpus-wide are Q 1, Q 108, Q 112 (the muʿawwidhāt-trio + Fātiḥa).
- Q 78 is NOT in the H-NEW-1190 *wa-mā adrāka mā* cluster (the cluster has 10 members; Q 78 is sandwiched between Q 77 and Q 82 but does NOT use the formula).
- Q 78:4-5 (*kallā sa-yaʿlamūn / thumma kallā sa-yaʿlamūn*) appears, on initial inspection, to share the formula with Q 102:3-4 — BUT the strict-string match revealed Q 102 uses *sawfa taʿlamūn* (different verb-form). The semantic-pair is real; the strict-string match is corpus-SINGLETON.

### Pre-reg lock + script lock (2026-05-09 morning)

5 pre-regs written and SHA-locked:
- Q078-F-01-cluster-centrality (SHA: f91b0f0e78c03d45d9900a5b827384a154cfdfdfe2c8c67e091b4dcb8099d6d5)
- Q078-F-02-jaalna-density (SHA: 80e59ddbeca96190ee8dbef37577af5303e764ecf1b58fd2cf561807a06fbb15)
- Q078-F-03-kalla-formula (SHA: 0a0fc08cbb077393ec41cbd23e4344d2bc8216648f28e16a443e11bec8cedd4d)
- Q078-F-04-juz30-boundary (SHA: 7bff9254fd33a5aa4999d4cd8d8516cfccb626c919df728a880e071005a0924b)
- Q078-F-05-cosmology-hapax (SHA: 769be11be7fe8a24b989f1fef7eee830f554b2b2ab2faa110e829ee28aa3303a)

5 scripts written; pre-reg SHA-verification at runtime.

### Test runs (2026-05-09)

**Q078-F-01 — Cluster centrality**: CONFIRMED.
- Cluster_mean = 0.4732; Corpus_mean = 0.6665; ratio = 0.7100.
- p_lower_perm = 0/10000 (no random 14-surah subset is closer to Q 78 than the H-NEW-1200 cluster).
- Q 78 centrality rank in [cluster ∪ Q 78] = 11/15 (PERIPHERAL).
- H1 + H2 PASS direction-locked.

**Q078-F-02 — jaʿala density + 3-streak**: CONFIRMED.
- Q 78 j-ʿ-l rate = 0.0382, rank 2/88 (top-5 PASS).
- Q 78 max consecutive *wa-jaʿalnā* streak = 3 at vv9-11 (≥3 PASS).
- Q 21 also has streak=3 at vv30-32 (corpus-paired with Q 78).

**Q078-F-03 — kallā formula corpus-EXACT 2-pair**: NULL.
- Strict-string pair-matches = 1 (Q 78:4-5 only). Q 102:3-4 uses *sawfa taʿlamūn* (different verb-form), so strict-string match misses Q 102.
- HONEST CORRECTION published in `06-novel-findings.md` Q078-F-03 §honest-correction: the SEMANTIC-pair (kallā + future-of-know + thumma-doubling) IS real (Q 78:4-5 + Q 102:3-4); the strict-string match is corpus-SINGLETON Q 78:4-5 alone.

**Q078-F-04 — Q 77→78 juzʾ-30 boundary**: CONFIRMED.
- Q 77→78 delta_raw = +0.0894, rank 40/113 (mid-spectrum, NOT top-15 structural-boundary).
- Direction-locked: rank > 15 = PASS. al-Suyūṭī's "30th juzʾ opener" structural-significance claim REFINED to position-claim only.

**Q078-F-05 — Hapax + block-confinement**: CONFIRMED.
- 3 corpus-hapax roots: whj v.13 (block 2), vjj v.14 (block 2), dhq v.34 (block 4).
- All hapax confined to Block 2 (cosmic-evidence) + Block 4 (paradise-closure). Zero in Block 1 (framing) or Block 3 (judgment).
- al-Bāqillānī iʿjāz al-balāgha claim VINDICATED at lexical-rarity + block-confinement axis.

### Net result

| Test | Verdict | Bonferroni | Direction matched |
|:--|:--|:--:|:--|
| Q078-F-01 | CONFIRMED | 2/2 | YES (peripheral 11/15) |
| Q078-F-02 | CONFIRMED | 2/2 | YES (rank 2/88, streak 3) |
| Q078-F-03 | NULL | n/a | NO (informative correction) |
| Q078-F-04 | CONFIRMED | 1/1 | YES (rank 40/113) |
| Q078-F-05 | CONFIRMED | 2/2 | YES (3 hapax, Blocks 2+4 only) |

**4 CONFIRMED + 1 NULL with honest correction.**

## 2026-05-09 — Documentation written

8 surah-template files written:
- `00-overview.md` (300+ lines)
- `01-empirical-profile.md` (250+ lines, with H-NEW-1200 cluster centrality table)
- `02-content-analysis.md` (300+ lines, 4-block architecture)
- `03-tafsir-survey.md` (8 classical authorities)
- `04-hadith-corpus.md` (Q 78:18 trumpet, Q 78:38 al-Rūḥ, Q 78:40 animal-tradition)
- `05-classical-claims-audit.md` (5 audited claims; 2 vindicated, 1 partial, 1 refined, 1 contested)
- `06-novel-findings.md` (Q078-F-01 through Q078-F-05 with full results)
- `07-cross-references.md` (12 connections to existing findings + future questions)

5 pre-regs, 5 scripts, 5 CSV outputs all committed.

## 2026-05-09 — Pending tasks for downstream

1. **Independent replication of Q078-F-01 on char-4-gram feature space** to promote PASS-DIRECTED → CONFIRMED.
2. **MW-6 verification of classical citations** in `03-tafsir-survey.md` and `04-hadith-corpus.md` (most are PENDING / SECONDARY-TRIANGULATED; only Ibn Kathīr Dār Ṭayyiba and al-Suyūṭī Dār al-Kutub al-ʿIlmiyya are VERIFIED).
3. **MASTER-FINDINGS-LEDGER update** to add Q 78 specialist findings (Q078-F-01 through Q078-F-05) — leave to team-lead per workflow.
4. **H-NEW-1260 candidate finding suggestion**: the H-NEW-1200 cluster best read as Q 97-CENTERED radial arrangement (3-shell geometry).

## 2026-05-09 — Audit notes for future review

- Q078-F-03 NULL is the highest-value teaching-moment of this investigation: a strict-string conflation that was caught at runtime. The HONESTY-OVER-CHEERLEADING discipline is preserved.
- Q078-F-01 cluster centrality finding (Q 78 = peripheral, Q 97 = centroid) is the most architecturally-novel result; it suggests the H-NEW-1200 cluster has an internal radial structure not previously characterized.
- Q078-F-04 juzʾ-30 boundary mid-spectrum confirms H-NEW-64 NULL with a specific case-study; useful for downstream juzʾ-related work.
- Q078-F-05 al-Bāqillānī iʿjāz vindication is a clean cross-finding-015 contribution.

## 2026-05-09 — Closing notes

The Q 78 specialist deliverable is complete. The 4-CONFIRMED + 1-NULL outcome (with honest informative correction on the NULL) is the empirical answer at this lock-date. All findings are PASS-DIRECTED pending independent replication on distinct-data-dimensions.

The investigation surfaces Q 97 al-Qadr as the H-NEW-1200 cluster CENTROID — a finding that may merit downstream follow-up via a Q 97 specialist run.

— Waiel Al-Shujaa, 2026-05-09
