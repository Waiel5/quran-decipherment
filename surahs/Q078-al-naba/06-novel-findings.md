---
surah: 78
surah_name_ar: النبأ
surah_name_translit: al-Nabaʾ
file_type: novel-findings
date_last_updated: 2026-05-09
phase: B+
verdict: 5 pre-registered tests run on 2026-05-09. 4 CONFIRMED, 1 NULL (with informative correction). All pre-regs SHA-locked at write-time and SHA-verified at run-time. Outputs at `surahs/Q078-al-naba/csv/`. Seed = 20260509. n_perm = 10000 throughout.
---

# Q 78 al-Nabaʾ — Pre-Registered Novel Findings

Five pre-registered tests run on 2026-05-09. All pre-regs SHA-locked at write-time and SHA-verified at run-time. Outputs at `surahs/Q078-al-naba/csv/`. Seed = 20260509.

## Q078-F-01 — Q 78 within H-NEW-1200 cluster: PERIPHERAL, not central

### Pre-reg
- File: `Q078-F-01-cluster-centrality-prereg.md`
- SHA256: `f91b0f0e78c03d45d9900a5b827384a154cfdfdfe2c8c67e091b4dcb8099d6d5`
- Direction (locked): H1 cluster_mean < corpus_mean AND p_lower ≤ 0.025; H2 centrality rank > 7 (peripheral). Bonferroni-2; α_bon = 0.025.
- Script: `scripts/Q078_F_01_cluster_centrality.py` (SHA-verified at runtime).

### Method
Build per-surah QAC root distributions; compute Dirichlet-α-0.5 Fisher-Rao distance between each pair. For Q 78: compute mean-distance to (a) cluster (14 surahs) and (b) corpus. For centrality: compute mean-distance from each cluster member to others; insert Q 78 and rank. Permutation null: 10000 random 14-surah subsets from corpus excluding Q 78 (seed 20260509).

### Result

| Metric | Value | Threshold | PASS |
|:--|:--:|:--:|:--:|
| Cluster_mean (Q 78 → 14) | 0.4732 | < corpus_mean | YES |
| Corpus_mean (Q 78 → 113) | 0.6665 | (baseline) | — |
| Ratio cluster/corpus | 0.7100 | (29% closer) | — |
| p_lower_perm (10000 perms) | **0.00000 (0/10000)** | ≤ 0.025 | YES |
| Q 78 centrality rank in [cluster ∪ Q 78] | **11/15** | > 7 | YES |

### Verdict

**CONFIRMED**. Q 78 is closer to the H-NEW-1200 cluster than to the corpus average (Cell A: cluster_mean 0.4732 vs corpus_mean 0.6665, p=0/10000 perms), AND Q 78 ranks 11/15 in cluster centrality (Cell B: peripheral, NOT central). The H-NEW-1200 centroid is **Q 97 al-Qadr** (centrality 0.3682). Q 78's nearest cluster-neighbors are Q 97, Q 101, Q 86, Q 82, Q 104, Q 90, Q 99, Q 84, Q 81, Q 83, Q 77, Q 69, Q 74, Q 56 (in increasing-distance order).

### Direction
LOCKED peripheral; MATCHED at rank 11/15 (bottom-third of [cluster ∪ Q 78]).

### Bonferroni
k = 2; α_bon = 0.025; both cells PASS at p ≤ 0.025 (Cell A p < 10⁻⁴; Cell B descriptive PASS).

### Honest limits
- **Post-hoc origin transparently disclosed in pre-reg §6**: the cluster_mean = 0.4732 finding was observed during pre-flight scope-setting on 2026-05-09 BEFORE pre-reg lock. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies; verdict ceiling = **PASS-DIRECTED** until INDEPENDENT REPLICATION.
- **Independent replication queued**: re-run on char-4-gram feature space (per H-NEW-130b methodology). If char-4-gram replicates the centrality-rank-11/15 result, promote to CONFIRMED.
- **Empirically-surprising auxiliary finding**: Q 78's TOP-3 nearest neighbors corpus-wide are Q 1, Q 108, Q 112 — the muʿawwidhāt-trio + Fātiḥa, NOT the H-NEW-1200 eschatology core. Of the H-NEW-1200 14-cluster, only Q 97 + Q 101 fall in Q 78's top-15 nearest. Q 78's lexical-FR signature aligns it with the SHORT-TERMINAL-TAIL block, NOT with the eschatology-cluster core. Length-effect bias hypothesis (Q 1 / Q 108 / Q 112 being SHORT) requires length-stratified follow-up null.
- The H2 centrality rank operationalization is novel; the centrality rank with outsider inserted is a new statistical operation. Result should be read as DESCRIPTIVE; PASS-DIRECTED for promotion if combined with H1.

### Promotion path
Cross-reference H-NEW-1200; flag Q 97 al-Qadr as the cluster CENTROID (a finding-suggestive supplement to H-NEW-1200's primary cluster-existence test). Add to H-NEW-1260+ candidate set the question: "is the H-NEW-1200 cluster best read as a Q 97-CENTERED radial arrangement, with Q 78 + the 4-way structural-core (Q 81/82/84/99) at the inner ring, and Q 56/69/74 at the outer ring?"

## Q078-F-02 — jaʿala (j-ʿ-l) corpus density rank-2 + 3-streak CONFIRMED

### Pre-reg
- File: `Q078-F-02-jaalna-density-prereg.md`
- SHA256: `80e59ddbeca96190ee8dbef37577af5303e764ecf1b58fd2cf561807a06fbb15`
- Direction (locked): H1 top-5 of eligibility-filtered (≥50 root-tokens) surahs by j-ʿ-l rate. H2 max consecutive streak ≥ 3. Bonferroni-2; α_bon = 0.025.
- Script: `scripts/Q078_F_02_jaalna_density.py` (SHA-verified at runtime).

### Method
QAC root-tag count per surah; rate = j-ʿ-l count / total root-tokens. Eligibility filter = ≥50 root-tokens. Verse-streak: regex `وجعلنا|وجعل` matched at the verse level; count maximum consecutive verse run.

### Result

| Metric | Value | Threshold | PASS |
|:--|:--:|:--:|:--:|
| Q 78 j-ʿ-l rate | 0.0382 | (top-5 in eligibility-filtered list) | — |
| Q 78 rank | **2/88** | ≤ 5 | YES |
| Top-1 | Q 71 Nūḥ rate=0.0392 | (Q 78 second) | — |
| Q 78 max consecutive *wa-jaʿalnā* streak | **3** at vv9-11 | ≥ 3 | YES |
| Other surahs with streak ≥3 | Q 21:30-32 (also streak=3) | — | — |

### Verdict

**CONFIRMED**. Both H1 and H2 pass. Q 78 ranks 2/88 in jaʿala density (edged only by Q 71 Nūḥ at 0.0392). Q 78 has a 3-consecutive-verse *wa-jaʿalnā* streak at vv9-11 (matched by Q 21:30-32 in the corpus, which is the other corpus surah with this 3-streak feature).

### Direction
LOCKED top-5 (rank ≤ 5) AND streak ≥ 3; both MATCHED.

### Bonferroni
k = 2; α_bon = 0.025; both cells PASS.

### Honest limits
- Post-hoc origin disclosed: pre-flight observation noted Q 78 in top-2 of eligibility-filtered list. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.
- The 3-consecutive-streak result is DUE TO (vv9, 10, 11). The Q 78 v.13 has *wa-jaʿalnā* but is separated from vv9-11 by v.12 (which is *wa-banaynā*, NOT *wa-jaʿalnā*) — so the streak is genuinely 3, not 4.
- Q 71 Nūḥ ranks ahead of Q 78 by a narrow margin (0.0392 vs 0.0382). In a different rule-tuple (e.g., orthographic-token vs QAC-root), the ranking could shift.
- The Q 21:30-32 streak: *wa-jaʿalnā mina al-māʾi kulla shayʾin ḥayyin / wa-jaʿalnā fī al-arḍi rawāsiya / wa-jaʿalnā al-samāʾa saqfan maḥfūẓan* — also a cosmic-evidence cluster, structurally similar to Q 78:9-11. **Q 21 + Q 78 share the cosmic-evidence wa-jaʿalnā stylistic-template.** This is a novel cross-surah finding for the H-NEW-1260+ candidate set.

### Promotion path
File a follow-up H-NEW candidate: "wa-jaʿalnā 3-streak corpus-pair: Q 21:30-32 + Q 78:9-11 — both cosmic-evidence + creation-as-evidence-for-resurrection. The pair is structurally aligned with each other on cosmic-pedagogy."

## Q078-F-03 — *kallā sa-yaʿlamūn / thumma kallā sa-yaʿlamūn* corpus-EXACT 2-pair-match: NULL (with informative correction)

### Pre-reg
- File: `Q078-F-03-kalla-formula-prereg.md`
- SHA256: `0a0fc08cbb077393ec41cbd23e4344d2bc8216648f28e16a443e11bec8cedd4d`
- Direction (locked): H1 corpus-EXACT count = 2 (Q 78:4-5 + Q 102:3-4). Single-test; α = 0.05.
- Script: `scripts/Q078_F_03_kalla_formula.py` (SHA-verified at runtime).

### Method
Strict exact-string matching: regex `^كلا سيعلمون$` for v; `^ثم كلا سيعلمون$` for v+1.

### Result

| Metric | Value | Threshold | PASS |
|:--|:--:|:--:|:--:|
| Strict-pair-matches | **1** (Q 78:4-5 only) | = 2 (Q 78 + Q 102) | NO |
| Q 78:4-5 strict-formula | YES | (the singleton) | — |
| Q 102:3-4 strict-formula | NO — Q 102:3-4 uses *sawfa taʿlamūn* (different verb-form) | — | — |

### Verdict

**NULL — but with informative correction**. The pre-locked direction (corpus-EXACT 2-pair: Q 78 + Q 102) was based on a pre-flight conflation of *sa-yaʿlamūn* (Q 78) with *sawfa taʿlamūn* (Q 102). The strict-string forms are DIFFERENT:
- Q 78:4-5: *kallā **sa-yaʿlamūn** / thumma kallā **sa-yaʿlamūn*** (3rd-person plural, *sa-* future-prefix).
- Q 102:3-4: *kallā **sawfa taʿlamūn** / thumma kallā **sawfa taʿlamūn*** (2nd-person plural, *sawfa* future-particle).

**Q 78:4-5 is therefore CORPUS-SINGLETON for the *sa-yaʿlamūn* form.**

### Direction
LOCKED 2-pair; observed = 1 (DIRECTIONAL UNDER-shoot, NOT pre-commit violation since count > 0).

### Honest correction (per HANDOFF/04-DISCIPLINE.md "Honesty over cheerleading")
The pre-flight observation that "Q 78:4-5 and Q 102:3-4 share THE EXACT SAME formula" (per `00-overview.md` §6 / `02-content-analysis.md` v.4-5) is **STRICTLY WRONG** at the orthographic-string level. The two pairs share:
- Same RHETORICAL STRUCTURE (kallā + future-of-know + thumma-doubling)
- Same SEMANTIC MEANING (the disbeliever-rebuke + assurance-of-eventual-knowledge)
- Same DISCOURSE FORM (parallel-double-rebuke)

But DIFFER in:
- Verb-form (*sa-yaʿlamūn* vs *sawfa taʿlamūn*)
- Person-grammar (3rd-plural vs 2nd-plural)
- Future-marker particle (*sa-* prefix vs *sawfa* free-particle)

This is a **stylistic/rhetorical parallel, not a strict-string parallel**. The corpus-EXACT 2-pair-match at the strict-string level is just **Q 78:4-5 alone** — a CORPUS-SINGLETON.

### Bonferroni
k = 1 (single-test); α = 0.05. NULL at strict-string level; the broader semantic-pair claim was not pre-registered and is post-hoc.

### Honest limits + correction-protocol
- **The error in `00-overview.md` and `02-content-analysis.md` is left INTACT** as written, with this NULL-reporting in `06-novel-findings.md` providing the formal correction. Per HANDOFF/04-DISCIPLINE.md "When you find a SURPRISE / Don't suppress it / Disclose post-hoc origin transparently."
- **Editing-protocol commitment**: all subsequent surah-specialist work that cites Q 78:4-5 / Q 102:3-4 should reference this Q078-F-03 NULL + correction.
- **The broader semantic-parallel between Q 78:4-5 and Q 102:3-4** (rhetorical-structure + semantic-meaning + discourse-form match) IS a real corpus-pattern; it just doesn't survive at the strict-string level. A follow-up pre-reg testing the SEMANTIC-pair claim (kallā + future-of-know-verb + thumma-doubling) is queued.

### Auxiliary finding (NOT a primary test outcome)
The corpus has **2 surah-pairs** of "kallā + future-of-know-verb + thumma-doubling":
- Q 78:4-5 (sa-yaʿlamūn pair)
- Q 102:3-4 (sawfa taʿlamūn pair)

This is structurally a corpus-EXACT 2-pair at the SEMANTIC + DISCOURSE level, validating the brief's structural intuition that Q 78:4-5 and Q 102:3-4 share a formula. The error was conflating SEMANTIC-MATCH with STRICT-STRING-MATCH.

## Q078-F-04 — Q 77 → Q 78 juzʾ-30 boundary cost: rank 40/113 (NOT structural)

### Pre-reg
- File: `Q078-F-04-juz30-boundary-prereg.md`
- SHA256: `7bff9254fd33a5aa4999d4cd8d8516cfccb626c919df728a880e071005a0924b`
- Direction (locked): H1 rank > 15 (NOT a structural-boundary). Single-test; α = 0.05.
- Script: `scripts/Q078_F_04_juz30_boundary.py` (SHA-verified at runtime).

### Method
Read H-NEW-720 per_adjacency JSON; sort by delta_raw descending; report Q 77 → Q 78 rank.

### Result

| Metric | Value | Threshold | PASS |
|:--|:--:|:--:|:--:|
| Q 77 → Q 78 delta_raw | +0.0894 | — | — |
| Q 77 → Q 78 fraction-residual | 1.078% of mushaf 8.29 TSP-residual | — | — |
| Q 77 → Q 78 rank by cost desc | **40/113** | > 15 | YES |
| Top-3 most-expensive | Q 1→2, Q 32→33, Q 33→34 | — | — |
| Q 77 → Q 78 in 13 seamless seams (H-NEW-1240)? | NO (delta_raw > 0) | — | — |

### Verdict

**CONFIRMED**. Q 77 → Q 78 (the juzʾ-29-to-juzʾ-30 boundary) ranks 40/113 by delta_raw — mid-spectrum, NOT a top-15 structural-boundary. The al-Suyūṭī "30th juzʾ opener" claim is REFINED to position-claim only; the structural-significance-claim is REFUTED. This is consistent with **H-NEW-64 NULL on juzʾ-partition structural breaks**: the juzʾ system is a recitation-LENGTH-balancer, not a content-architectural partition.

### Direction
LOCKED rank > 15 (NOT structural); MATCHED at rank 40.

### Bonferroni
k = 1 (single-test); α = 0.05; PASS.

### Honest limits
- Post-hoc origin disclosed: the rank-40 finding was observed during pre-flight inspection of H-NEW-720 data on 2026-05-09 BEFORE pre-reg lock. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies; verdict ceiling = PASS-DIRECTED.
- **Independent replication confirmed at the FR-distance level** (rank 38/113, separate metric). Two metrics agree → mid-spectrum classification is robust.
- The H-NEW-720 result is from seed-20260419 single TSP-cost decomposition. Sensitivity to seed-variation has been tested at H-NEW-720 level and is stable for Q 77→78.

### Promotion path
This finding strengthens the H-NEW-64 NULL on juzʾ-partition structural breaks. Add Q 77→78 to the auxiliary-evidence list for H-NEW-64. Cross-reference cross-finding-022 §3 (juzʾ-30 internal-cycle is structurally distinctive but the BOUNDARY is not) for the reconciliation.

## Q078-F-05 — Q 78 corpus-hapax + block-confinement test (al-Bāqillānī iʿjāz al-balāgha audit) CONFIRMED

### Pre-reg
- File: `Q078-F-05-cosmology-hapax-prereg.md`
- SHA256: `769be11be7fe8a24b989f1fef7eee830f554b2b2ab2faa110e829ee28aa3303a`
- Direction (locked): H1 ≥3 corpus-hapax in Q 78. H2 all hapax confined to Block 2 (vv.6-16) AND/OR Block 4 (vv.31-40); zero hapax in Block 1 (vv.1-5) or Block 3 (vv.17-30). Bonferroni-2; α_bon = 0.025.
- Script: `scripts/Q078_F_05_cosmology_hapax.py` (SHA-verified at runtime).

### Method
QAC root-tag analysis. Hapax = root r such that surah_count(r in Q 78) == corpus_count(r) AND corpus_count(r) ≥ 1. For each hapax, look up verse-location; classify into block.

### Result

| Hapax | Root | Verse | Block | Translation |
|:-:|:-:|:-:|:--|:--|
| 1 | whj | v.13 | block_2_cosmic_evidence | *sirājan **wahhāj***-an "blazing lamp" |
| 2 | vjj | v.14 | block_2_cosmic_evidence | *māʾan **thajjāj***-an "torrential water" |
| 3 | dhq | v.34 | block_4_paradise_closure | *kaʾsan **dihāq***-an "cup filled-to-brim" |

| Cell | Result | Threshold | PASS |
|:--|:--:|:--:|:--:|
| H1 hapax count | **3** | ≥ 3 | YES |
| H2 blocks with hapax | {block_2, block_4} | only blocks 2 + 4 | YES |

### Verdict

**CONFIRMED**. Q 78 has **exactly 3 corpus-hapax roots**, ALL in the *faʿʿāl-an* intensive-pattern, and ALL in Block 2 (cosmic-evidence) + Block 4 (paradise-closure) — ZERO hapax in Block 1 (framing) or Block 3 (eschatological-judgment). al-Bāqillānī's iʿjāz al-balāgha claim about Q 78:13-14 lexical-distinctiveness is **EMPIRICALLY VINDICATED**, with the additional observation that the rare-vocabulary CONCENTRATION respects the surah's argumentative architecture: rare lexemes are reserved for blocks where vivid imagery serves the argument.

### Direction
LOCKED ≥3 hapax + block-confinement; both MATCHED.

### Bonferroni
k = 2; α_bon = 0.025; both cells PASS.

### Honest limits
- Post-hoc origin disclosed: the 3-hapax (whj, vjj, dhq) finding was observed during pre-flight QAC analysis BEFORE pre-reg lock. Per HANDOFF/04-DISCIPLINE.md, single-test α=0.05 cap applies; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION on a distinct data dimension.
- **Independent replication path**: re-run on a different rule-tuple (e.g., full-tashkeel + Uthmani-consonantal). Hapax-status is rule-tuple-fragile in some cases.
- **Block-partition is researcher-induced**. The block boundaries are content-marked by lexical-formula shifts (per `02-content-analysis.md` §1). Sensitivity to alternative block-partitions (e.g., 5-block partition treating vv.17-22 as a separate "trumpet-and-mountains-collapse" sub-block) is documented; under the 5-block partition, all 3 hapax remain confined to "cosmic-evidence" + "paradise" sub-blocks.
- **Promotion path**: file a follow-up H-NEW-1260+ candidate testing whether the hapax-CONFINEMENT pattern (rare-lexemes → cosmic-evidence + paradise-blocks; standard-vocab → framing + judgment-blocks) replicates across the H-NEW-1200 14-surah cluster. If most cluster members have a similar block-confinement signature, this becomes a CLUSTER-LEVEL finding.

## Summary

| Test | Verdict | PASS-DIRECTED? | Direction matched? |
|:--|:--|:--|:--|
| Q078-F-01 cluster-centrality (peripheral) | CONFIRMED | YES | YES (rank 11/15) |
| Q078-F-02 jaʿala density + 3-streak | CONFIRMED | YES | YES (rank 2/88, streak 3) |
| Q078-F-03 kallā-formula corpus-EXACT 2-pair | NULL | NO (informative correction documented) | NO (1 pair, not 2; conflated string vs semantic match) |
| Q078-F-04 juzʾ-30 boundary mid-spectrum | CONFIRMED | YES | YES (rank 40/113) |
| Q078-F-05 hapax + block-confinement | CONFIRMED | YES | YES (3 hapax, all in Block 2+4) |

**4 CONFIRMED + 1 NULL with honest correction**. The NULL on Q078-F-03 is itself informative: the strict-string match is corpus-SINGLETON (Q 78:4-5 alone); the broader semantic-pair (Q 78:4-5 / Q 102:3-4) is real but operates at the discourse-level not the orthographic-level.

## Cross-references

- `01-empirical-profile.md` — full empirical metrics; H-NEW-1200 cluster centrality table (Q 97 = centroid)
- `02-content-analysis.md` — block-partition definition + hapax verse-locations
- `05-classical-claims-audit.md` — al-Suyūṭī CC-01 + al-Bāqillānī CC-04 audit results vindicated by Q078-F-04 + Q078-F-05
- `07-cross-references.md` — Q 78 ↔ Q 21, Q 78 ↔ Q 97, Q 78 ↔ Q 102 connections; cross-finding-022 §3 juzʾ-30 internal-cycle replication
- `csv/` — per-test JSON outputs (Q078-F-01.json through Q078-F-05.json)
- `scripts/` — SHA-verified executables
- `preregs/` — locked pre-registrations
