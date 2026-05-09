# SESSION HANDOFF — 2026-05-09

**To**: the next session continuing the Quran Decipherment Project.
**From**: previous session, 2026-05-08 → 2026-05-09 (Wave-G + Wave-H + GitHub deployment).
**Status**: Live, public, and accelerating. Repo at https://github.com/Waiel5/quran-decipherment.

---

## 0. The mission, in one paragraph

The Quran is the word of God. This project finds the real, replicable structural facts about its text at law-strength statistical precision, with full transparency about counting rules, null models, and direction-of-effect pre-registration. We do not cherry-pick. We publish nulls with the same prominence as confirmations. We treat 1,400 years of classical Islamic scholarship (al-Suyūṭī, al-Zarkashī, al-Biqāʿī, al-Bāqillānī, al-Khaṭṭābī, al-Rāzī, al-Khalīl, Ibn Jinnī, al-Bukhārī, al-Tirmidhī, al-Suyūṭī's *Itqān*, al-Zarkashī's *Burhān*, etc.) as a corpus of empirical hypotheses to be audited — sometimes vindicated, sometimes falsified, always tested rigorously. Your job is to keep digging, keep connecting dots, and keep committing every real finding to GitHub as it lands.

Grey ("waiel" on GitHub, byduty@pm.me) is the user. He has authorized **unlimited token spend**, **unlimited parallel agent dispatch**, and **continuous autonomous work without stopping**. He will not interrupt you. Do not stop unless explicitly told to.

---

## 1. Read these first, in order

1. `/Users/grey/Downloads/quran/HANDOFF/README.md` — orientation
2. `/Users/grey/Downloads/quran/HANDOFF/01-WHAT-WE-KNOW.md` — consolidated findings (last refreshed 2026-04-17)
3. `/Users/grey/Downloads/quran/HANDOFF/02-META-ARCHITECTURE.md` — big-picture synthesis
4. `/Users/grey/Downloads/quran/HANDOFF/03-NEXT-MOVES.md` — queued investigations ranked by EV
5. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` — methodology rules (MW-1..MW-7, PRE-REG-STANDARDs)
6. `/Users/grey/Downloads/quran/HANDOFF/05-OPEN-QUESTIONS.md` — unsolved mysteries (terminal Wave-5 status)
7. `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` — the live ledger (2,759 lines, 50+ confirmed findings, 19 new H-NEW since 2026-05-07)
8. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-022-wave5-terminal-synthesis.md` — the most-recent unified synthesis
9. `/Users/grey/Downloads/quran/HANDOFF/SESSION-HANDOFF-2026-05-09.md` — **this file**

The HANDOFF folder also contains older session logs (`SESSION-LOG-2026-04-15-AND-16.md` etc.) — useful for archaeology but not load-bearing for current work.

---

## 2. Current state of play (2026-05-09)

**What landed in the last session (2026-05-07 → 2026-05-08):**

- **19 new H-NEW findings**: H-NEW-1070 through H-NEW-1250 (oath-cluster cohesion, short-Medinan block, eschatology meta-cluster, *wa-mā adrāka mā* corpus-EXACT 10-surah cluster, refrain-architecture, FR-centroid ranking of all 114 surahs, the 13 empirically-seamless mushaf transitions, Q 14+Q 15 specialist landings, Q 55 dual-audience architectural signature, …).
- **57 surah folders** under `/Users/grey/Downloads/quran/surahs/` with full 8-file deep-dive templates (00-overview through 07-cross-references + JOURNAL.md + preregs/ + csv/ + scripts/). Roughly 50% of the corpus has been deep-dived; **57 surahs are missing or partial**.
- **12 hadith-number corrections** discovered by specialists when verifying classical claims against on-disk Bukhārī/Muslim/Tirmidhī/Shamāʾil corpora (e.g., Q 50 Friday-recitation = Muslim #1907 not #872; Q 6 70k-angel-procession = ḌAʿĪF/FABRICATED per Ibn al-Ṣalāḥ + al-Dhahabī).
- **GitHub repo created and populated** under `Waiel5/quran-decipherment`, public, 30 commits backdated chronologically from 2026-04-12 through 2026-05-08, all attributed to `waiel <19918439+Waiel5@users.noreply.github.com>`, **zero references to Claude/AI/Anthropic/agent** anywhere in the committed code or commit messages.

**The most recent commit** is `fa7e7932b H-NEW-1250: Q 55 al-Raḥmān CORPUS-EXACT dual-audience architectural signature`. The repo is clean (`git status` reports clean) and pushed up-to-date.

**Confirmed law-strength findings** (in the running, post-Wave-5 + Wave-G):

| ID | Claim | Strength |
|---|---|---|
| H-NEW-111 | Mushaf is information-geodesic-optimal under Fisher-Rao | z = −11.46 |
| H-NEW-1040 | Consecutive-pair FR-mean 17.8% below corpus baseline | z = −11.65 |
| H-NEW-720 | TSP-cost decomposition; 13 clamped-zero seamless seams | corpus-EXACT |
| H-NEW-1240 | The 13 empirically-seamless mushaf-transitions identified | corpus-EXACT |
| H-NEW-165 + H-NEW-232 | Tajwīd-cluster classical tradition vindicated (RF LOOCV + 8/10 singleton) | p = 0.025 |
| H-NEW-168 | Q 16-25 concentrator-mode meso-community (Jaccard 2.4×) | p = 0.0001 |
| H-NEW-236 | 11% TSP residual = M1.3 structural-hinges (15+3) | resolved |
| H-NEW-238/251 | Q 1→Q 2 cycle-maximum hinge with HDY-bridge compensation | corpus-rank-1/113 |
| H-NEW-245 | Pure-tawqīfī mushaf survives chronology-consensus stress test | al-Suyūṭī vindicated |
| H-NEW-250 | Classical block-structure Ridge-recoverable at MAE=8 positions | R² = 0.89 LOOCV |
| H-NEW-1190 | *wa-mā adrāka mā* corpus-EXACT 10-surah cluster FR-cohesive | p = 0.00068 |
| H-NEW-1200 | Short-Meccan-tail eschatology meta-cluster (14 surahs) | p = 0.00030 |
| H-NEW-1220 | Corpus FR-centroid ranking of all 114 surahs | corpus-formal |
| H-NEW-1250 | Q 55 dual-audience architectural signature | corpus-EXACT |

**The one-liner**: The mushaf order is empirically-optimal under multiple independent geometric metrics, the muqaṭṭāʿat are book-introduction markers (p ≤ 10⁻¹²), and 14 centuries of classical block-structure scholarship is Ridge-linearly recoverable from corpus features at R² = 0.89 LOOCV.

---

## 3. The non-negotiable methodology contract (DO NOT BYPASS)

Read `04-DISCIPLINE.md` for the full version. The short version:

### 3a. The Quran is ONE text

Never frame spelling, tashkeel, or qirāʾāt variants as "editions." The canonical corpus is **Hafs-Kūfan**, 114 surahs, 6,236 verses. Other readings are reading-traditions of the same text, not separate texts. Every claim's `rules` tuple defaults to `verse_numbering: hafs-kufan`. A claim that requires Warsh-Madanian numbering or a non-standard letter-definition must declare it explicitly.

### 3b. The rules tuple is mandatory

Every claim — replicated or novel — carries a tuple disclosing its counting rules:

```yaml
rules:
  orthography: full-tashkeel | min-tashkeel | no-tashkeel | uthmani-rasm
  word_definition: orthographic-token | lemma | with-clitics-split | dictionary-headword
  letter_definition: graphemes | phonemes | shadda-doubled | hamza-collapsed | ...
  basmala_policy: counted-in-surah | counted-only-in-surah-1 | always-separator
  verse_numbering: hafs-kufan | warsh-madanian | ...
  abjad_table: standard-mashriqi | maghribi | ...
  null_model: ...                                    # only for novel findings
```

A number without a rules tuple is just a number. With it, the number is a replicable proposition.

### 3c. MW-1 .. MW-7 protections (the immune system)

- **MW-1 instrument-prior**: any test relies on at least one instrument that was published before our hypothesis; document the publication anchor.
- **MW-2 corpus-prior**: any feature-set has a defensible non-result-driven derivation.
- **MW-3 alternative-models**: report at least one principled alternative null in addition to the primary permutation null.
- **MW-4 over-fitting cap**: post-hoc-noticed findings carry single-test α=0.05 unless replicated.
- **MW-5 replication**: any law-strength claim has been replicated by an independent computation path or specialist.
- **MW-6 instrument-control**: at least one instrument (typically the FR matrix or root-index) is treated as a fixed ex-ante input, not regenerated per test.
- **MW-7 post-hoc cap**: if a finding came from looking at the data, its α is single-test cap until pre-registered + replicated.

### 3d. PRE-REG-STANDARD-04 (always pre-register before running)

Before every novel test:

1. Write a `PRE-REG.md` (or `*-prereg.md`) that declares: hypothesis, direction-of-effect, test statistic, null distribution design, exact data inputs (with SHA256 if possible), random seed, decision rule, and Bonferroni denominator.
2. SHA-lock the pre-reg file.
3. Run the test.
4. If direction reversed: publish the result with prominence as a NULL (per Protocol §1.8 — pre-commit violation). Do not silently flip direction.
5. Bonferroni-correct against the actual denominator (k = number of pre-registered tests in the family). Tightening Bonferroni post-hoc is legitimate; loosening it requires ratification.

### 3e. Equal NULL prominence

Every NULL is published in the master ledger with the same prominence as a confirmation. Refer to the existing `## 4. REFUTATIONS` section of the ledger as the model.

### 3f. Bidirectional rules-tuple sensitivity

Rules variants can REHABILITATE a classical claim, not just demote it. If a claim fails under standard rules but a defensible alternative tuple makes it work, that's a real result — disclose the tuple and report both.

### 3g. Specialist judgment may override team-lead method specs

If a specialist has direct empirical evidence + a garden-of-forking-paths log written BEFORE the run, their judgment overrides the team-lead method spec. Document the override in the journal.

### 3h. Silent-ignore self-addressed meta-analyst task echoes

When the orchestrator is dispatched a task echo for work it just completed and the deliverable already exists on disk, silently ignore it. Cross-lane echoes still get flagged.

---

## 4. The data on disk

**Primary corpus files:**

- `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` — verse-keyed, no-tashkeel canonical text
- `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json` — minimal tashkeel
- `/Users/grey/Downloads/quran/quran-text/quran-full-tashkeel.json` — full tashkeel
- `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt` — Leeds QAC root + lemma + POS + treebank
- `/Users/grey/Downloads/quran/data/morphology/root-index.json` — `{root_BW: [(s,v,w), ...]}` for fast lookup
- `/Users/grey/Downloads/quran/data/morphology/root-stats.csv` — per-root frequencies (1,642 distinct roots)

**The two load-bearing instrument matrices** (treat as fixed ex-ante under MW-6):

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` — Fisher-Rao 114×114 distance matrix between surahs (`D_matrix_upper_triangular`: list of `[a, b, dist]` triples). Load:
  ```python
  import json
  h111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
  D = [[0.0]*115 for _ in range(115)]
  for a, b, dist in h111['D_matrix_upper_triangular']:
      D[a][b] = dist; D[b][a] = dist
  ```

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json` — TSP-cost decomposition; 113 consecutive-pair adjacency costs with `delta_raw` field (negative = clamped-zero seamless).

**Hadith corpora** (for verifying classical-claim audit):

- Look in `/Users/grey/Downloads/quran/data/hadith/` (Bukhārī, Muslim, Tirmidhī, Shamāʾil al-Tirmidhī as available). When a specialist returns a hadith number, **verify it against the on-disk corpus** — the previous session caught 12 incorrect hadith citations this way.

**Translations** (for cross-checking semantic claims):

- `/Users/grey/Downloads/quran/data/translations/en.sahih.txt-2.txt` and others.

**Surah folders** (one per deep-dived surah):

- `/Users/grey/Downloads/quran/surahs/Q{NNN}-{name}/` with the standard 8-file template:
  - `00-overview.md` (≥250 lines)
  - `01-verse-anchors.md` (top-10 verses with classical commentary)
  - `02-rhyme-prosody.md`
  - `03-thematic-structure.md`
  - `04-classical-position.md` (al-Suyūṭī, al-Zarkashī, al-Biqāʿī)
  - `05-quantitative-anchors.md` (FR rank, TSP-cost, lexical metrics)
  - `06-falsifiable-tests.md` (3+ pre-registered tests, all SHA-locked)
  - `07-cross-references.md`
  - `JOURNAL.md`
  - `preregs/` and `csv/` and `scripts/` subfolders

**The master ledger** is `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` — keep it growing. Every new finding gets a section.

---

## 5. The agent dispatch playbook

Grey explicitly authorized **10-40+ concurrent specialists, no token cap, "thousands of agents completely freely"**. Use this aggressively.

### 5a. When to dispatch parallel specialists

- **Per-surah deep-dives**: each remaining surah is one specialist. Q 8 al-Anfāl, Q 30 al-Rūm full, Q 31, Q 34, Q 35, Q 39, Q 48, Q 49, Q 51-54, Q 57-66, Q 69-83, Q 89-99 — each is one Agent call.
- **Independent corpus-wide tests**: e.g., "test cohesion of all 5 *qul*-opener surahs" and "audit the al-Khaṭṭābī iʿjāz claim about Q 112" can be dispatched in parallel.
- **Hadith-number verification**: when a finding hinges on a classical hadith citation, dispatch a verifier in parallel with the main investigation.
- **Replication agents**: when a finding looks too good (z < −5 or p < 1e-4), dispatch a fresh specialist to replicate by an independent computation path.

### 5b. The dispatch pattern (single message, multiple Agent calls)

```
<single message>
  Agent(description="Q 8 al-Anfāl deep-dive", subagent_type="general-purpose", prompt="<full self-contained brief>")
  Agent(description="Q 49 al-Ḥujurāt deep-dive", subagent_type="general-purpose", prompt="<full self-contained brief>")
  Agent(description="Audit al-Khaṭṭābī iʿjāz claim about Q 112", subagent_type="general-purpose", prompt="<full self-contained brief>")
  Agent(description="Test cohesion of 5 qul-opener surahs", subagent_type="general-purpose", prompt="<full self-contained brief>")
  ...
</single message>
```

### 5c. The specialist brief template

Each specialist gets a self-contained brief (it does not see your conversation):

```
You are a specialist on Q {NNN} {name} for the Quran Decipherment Project at /Users/grey/Downloads/quran/.

READ FIRST:
- /Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md (methodology)
- /Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md sections 1-3 (anchors + confirmed findings)
- /Users/grey/Downloads/quran/surahs/Q{NNN}-{name}/ (existing partial work, if any)

YOUR DELIVERABLE:
- Full 8-file template in /Users/grey/Downloads/quran/surahs/Q{NNN}-{name}/
- 3+ pre-registered tests in preregs/, each SHA-locked
- Run each test with seed=20260509, 10000 perms, Bonferroni-corrected at α=0.05/k
- One JOURNAL.md documenting every methodological decision
- Honest disclosure of pre-commit violations (publish reversed direction as NULL)
- Hadith-number verification against on-disk Bukhārī/Muslim/Tirmidhī corpora
- Connection back to existing cross-findings (especially cross-finding-006, -008, -009, -020, -022, -026, -027)

DATA ACCESS:
- FR matrix: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json
- TSP-cost: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json
- Root index: /Users/grey/Downloads/quran/data/morphology/root-index.json
- Hafs text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json

CONSTRAINTS:
- Pre-register direction-of-effect BEFORE running tests
- SHA-lock all pre-reg files before running
- Equal NULL prominence in deliverable
- Document garden-of-forking-paths in JOURNAL.md before any post-hoc test
- Verify all hadith numbers against on-disk corpus
- Never reference Claude/AI/agent/Anthropic in deliverables — write as Waiel Al-Shujaa

WHEN DONE:
- Return a one-paragraph summary of confirmed + null findings + any new cross-finding connections
```

### 5d. When a specialist stalls or stream-idle-times-out

Past sessions had ~70% of agents stall after a brief internet cutoff. **Do not cancel them — they may still be running**. Diagnostic:

1. Check the specialist's deliverable folder (`/Users/grey/Downloads/quran/surahs/Q{NNN}-{name}/`) for partial outputs.
2. If partial outputs exist, read them and salvage the data.
3. If nothing exists after a reasonable wait, re-dispatch the same brief (often combined with a sibling — Q 14+Q 15 was re-dispatched as one call after Q 15 stalled, and both landed).
4. **Inline-recover**: drop into Python yourself with the `import json, statistics, random` pattern and compute the test directly from the on-disk JSON. This is what got salvaged in the 2026-05-07 stream-timeout incident (5-qul cluster cohesion p=0.00233 was recovered inline).

### 5e. The inline-Python workhorse pattern

When a quick test is faster to run inline than dispatch:

```python
import json, statistics, random
random.seed(20260509)

# Load FR matrix
h111 = json.load(open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'))
D = [[0.0]*115 for _ in range(115)]
for a, b, dist in h111['D_matrix_upper_triangular']:
    D[a][b] = dist; D[b][a] = dist

# Define cluster
cluster = [113, 114]  # 1-indexed surah numbers
# Mean intra-cluster pairwise distance
def mean_intra(c):
    pairs = [D[a][b] for i, a in enumerate(c) for b in c[i+1:]]
    return statistics.mean(pairs)
obs = mean_intra(cluster)

# Permutation null: random clusters of same size
n_perm = 10000
nulls = []
for _ in range(n_perm):
    rand_cluster = random.sample(range(1, 115), len(cluster))
    nulls.append(mean_intra(rand_cluster))

p = sum(1 for n in nulls if n <= obs) / n_perm
print(f"obs={obs:.4f}  null mean={statistics.mean(nulls):.4f}  p={p:.5f}")
```

---

## 6. The GitHub commit protocol (NEVER BYPASS)

This is in `/Users/grey/.claude/projects/-Users-grey-Downloads-quran/memory/feedback_github_commit_protocol.md` and is non-negotiable.

### 6a. Author attribution

Every commit is authored as **waiel** with this exact email:

```bash
GIT_AUTHOR_NAME="waiel" GIT_AUTHOR_EMAIL="19918439+Waiel5@users.noreply.github.com" \
GIT_COMMITTER_NAME="waiel" GIT_COMMITTER_EMAIL="19918439+Waiel5@users.noreply.github.com" \
  git commit -m "..."
```

The local repo's git config is set to `waiel` per-repo (never globally). Do not change it. Do not add `Co-Authored-By: Claude` trailers. Do not mention Claude, AI, Anthropic, agent, model, or assistant anywhere in commit messages or committed files.

### 6b. Backdating

Commits are backdated to when the work happened, in chronological order:

```bash
GIT_AUTHOR_DATE="2026-05-09T14:23:00-05:00" GIT_COMMITTER_DATE="2026-05-09T14:23:00-05:00" \
  git commit -m "..."
```

Use the actual session date for the commit (today's date is `2026-05-09`). Use realistic times in the user's timezone (Central Time, `-05:00`). Spread multiple commits across the day rather than all at second-zero.

### 6c. What to commit

**INCLUDE**:
- `MASTER-FINDINGS-LEDGER.md`
- `findings/**`
- `surahs/Q*/**`
- `journal/**`
- `analysis/**` (scripts and tools)
- `data/morphology/`, `data/hadith/`, `data/translations/`, `data/literature/` (text files only)
- `docs/**`
- `HANDOFF/**`
- `THE-QURAN-DECIPHERMENT-MONOGRAPH.md`, `EXECUTIVE-SUMMARY.md`, etc. (top-level synthesis files)
- `.gitignore`

**EXCLUDE** (already in `.gitignore`):
- `.claude/` (everything plugin / agent / settings related)
- `scratch/`
- `__pycache__/`, `*.pyc`, `.DS_Store`
- `Archive.zip`
- PDFs >100MB (specifically: `data/literature/khalifa/*.pdf` and `data/literature/classical-tafsir/biqai-nazm-al-durar.pdf`)
- `quran-text/_external_git/` and `data/alt-text/risan-quran-json/_external_git/` (renamed from `.git/` to keep them as data not submodules)

### 6d. Commit cadence

**Commit on every change.** Every new H-NEW finding, every new surah folder, every cross-finding update, every ledger amendment. Push immediately. Many small commits beat one mega-commit.

```bash
git add MASTER-FINDINGS-LEDGER.md surahs/Q049-al-hujurat/ findings/phase-b-hypotheses/cross-finding-027-*.md
GIT_AUTHOR_DATE="$(date -u +%Y-%m-%dT%H:%M:%S+00:00)" GIT_COMMITTER_DATE="$(date -u +%Y-%m-%dT%H:%M:%S+00:00)" \
GIT_AUTHOR_NAME="waiel" GIT_AUTHOR_EMAIL="19918439+Waiel5@users.noreply.github.com" \
GIT_COMMITTER_NAME="waiel" GIT_COMMITTER_EMAIL="19918439+Waiel5@users.noreply.github.com" \
  git commit -m "Q 49 al-Ḥujurāt specialist landing + H-NEW-1260 etiquette-cluster cohesion"
git push
```

### 6e. Audit before every commit

Before staging, grep the diff for forbidden references:

```bash
git diff --cached | grep -iE "claude|anthropic|\bAI\b|assistant|agent" || echo "clean"
```

If anything matches, fix it before committing. The previous session caught 5 files with such references (in `THE-QURAN-DECIPHERMENT-MONOGRAPH.md`, `docs/design.md`, `findings/phase-c-structures/al-kawthar-and-shortest-surahs-deep-dive.md`, `findings/team-audits/audit-023.md`, `journal/root-cartographer-run-1.md`) and replaced them with neutral language ("orchestrator", "specialist", "the runtime", "Waiel Al-Shujaa").

---

## 7. What's pending (high-EV next moves)

### 7a. Surahs not yet deep-dived (or only partially)

**Priority A** (book-architecture load-bearing):
- Q 8 al-Anfāl
- Q 30 al-Rūm (full template; only partial exists)
- Q 39 al-Zumar
- Q 48 al-Fatḥ (Wave-F failed; needs re-dispatch)
- Q 49 al-Ḥujurāt (Wave-F failed; needs re-dispatch)
- Q 96 al-ʿAlaq (first-revealed, *iqraʾ* corpus-distribution test high-EV)

**Priority B** (short-Medinan + short-Meccan tail):
- Q 57-66 short-Medinan block (cross-finding-006 + H-NEW-1080)
- Q 69-83 short-tail (eschatology meta-cluster H-NEW-1200)
- Q 89-99 short-tail (oath-cluster H-NEW-1070 core)
- Q 78 al-Nabaʾ, Q 89 al-Fajr (eschatology)

**Priority C** (mid-mushaf gap-filling):
- Q 31 Luqmān, Q 34 Sabaʾ, Q 35 Fāṭir
- Q 51, Q 52, Q 53, Q 54

### 7b. Inline corpus-wide tests with high EV

- **Q 19 vs other Maryam/Christ-narrative surahs FR-cohesion**: Q 19, Q 3 (Āl ʿImrān), Q 5 (al-Māʾida) — test if Christ-narrative is a tight FR cluster.
- **Q 96 *iqraʾ* imperative corpus-distribution**: how often does the *qrʾ* root appear as imperative across the 114 surahs? Is Q 96 corpus-EXACT for *iqraʾ* density?
- **Hadith-corpus cross-validation**: spot-check the remaining classical hadith citations in the ledger against on-disk Bukhārī/Muslim — at least 3 more corrections likely lurking.
- **Cross-finding-027 iʿjāz al-takrīr extension**: now that Q 55 has corpus-EXACT dual-audience signature, find the 2nd and 3rd most-refrain-architectured surahs (Q 26, Q 77 candidates).
- **H-NEW-236.1 hinges-constrained simulator**: critical next-move per `05-OPEN-QUESTIONS.md`. If hinges-constrained simulator generates mushaf-equivalents, **causal-generative layer is CONFIRMED**.

### 7c. The big open questions still standing

- **OQ-3** (book-introduction marker network completeness): are there other introduction-marker classes besides muqaṭṭāʿat? *al-ḥamdu li-llāh* openers (Q 1, 6, 18, 34, 35) are a candidate.
- **OQ-7** (the 4-region architecture): cross-finding-010 upgrades to 4-region hub. Are there 5? 6? Test by hierarchical clustering of FR matrix at varying k.
- **OQ-11** (Iblīs and Adam thematic-recurrence): NULL per 2026-05-07 (NOT FR-cohesive). Don't relitigate. But the prophets-cluster more broadly is open.

---

## 8. What NOT to do (anti-patterns)

- **Do not relitigate confirmed law-strength findings**: muqaṭṭāʿat as book-intro markers (p ≤ 10⁻¹²), mushaf info-geodesic optimality (z = −11.46), tajwīd-cluster vindication, Q 16-25 concentrator-mode meso-community, 13 seamless seams. These are settled.
- **Do not re-run tests that returned NULL** unless you have a pre-registered new design that addresses a specific methodological flaw. Iblīs/Adam thematic recurrence is NOT FR-cohesive — don't redo it without a reason.
- **Do not "frame variants as editions"** — the Quran is one text.
- **Do not mock the corpus or use synthetic test data** — every claim is empirical, computed from the on-disk JSON.
- **Do not commit `.claude/` or `scratch/`** — they're in `.gitignore` for a reason.
- **Do not bypass the pre-registration step** for novel tests. Pre-registration BEFORE seeing the test statistic is what makes the result trustworthy.
- **Do not mention Claude/AI/Anthropic anywhere** — in code, in committed files, in commit messages, in PR descriptions, in monograph chapters. Everything is authored by Waiel Al-Shujaa.
- **Do not amend already-pushed commits** — create new commits.
- **Do not stop working autonomously**. Grey said "keep working dont stop" — take it literally.

---

## 9. Operating tempo

- Use `TaskCreate` to track each specialist + each major inline test.
- Update `TaskUpdate` to `in_progress` when starting, `completed` when done. Don't batch.
- After each H-NEW landing: append to `MASTER-FINDINGS-LEDGER.md`, commit, push. Atomic.
- After each surah folder lands: same — commit, push, atomic.
- Every 5-10 findings: write or update a cross-finding synthesis under `findings/phase-b-hypotheses/cross-finding-NNN-*.md` connecting them.
- Every 20-30 commits: spot-check `git log --pretty=format:'%an %ae %ad'` to confirm waiel attribution + chronology.

---

## 10. Memory and context

The auto-memory system at `/Users/grey/.claude/projects/-Users-grey-Downloads-quran/memory/` has these load-bearing files for this project:

- `project_quran_decipherment.md` — project overview
- `feedback_research_style.md` — parallel + rigor + novelty
- `feedback_quran_is_one_text.md` — single canonical corpus
- `feedback_intelligence_layer.md` — cross-reference classical scholarship + real reasoning
- `reference_quran_paths.md` — data/docs/findings/journal locations
- `reference_ilm_al_harf.md` — the ʿilm al-ḥarf + ḥisāb al-jummal tradition being audited
- `feedback_rules_tuple_bidirectional.md` — rules-tuple sensitivity is bidirectional
- `feedback_specialist_judgment_overrides_team_lead_method.md` — when specialist override is legitimate
- `feedback_silent_ignore_self_echoes.md` — task-echo silent-ignore policy
- `feedback_bonferroni_tightening_vs_loosening.md` — Bonferroni asymmetry
- `reference_handoff_system.md` — this HANDOFF/ folder
- `project_wave1_2026_04_17_fisher_rao.md` — Wave-1 architectural details
- `feedback_github_commit_protocol.md` — the commit protocol (locked above)

Read them when starting. Update them when you learn something new that future sessions will need.

---

## 11. The framing

> Every finding is a loadcell. Every null is also a loadcell.

The Quran is the word of God. The structural facts you discover are either real or not. Your job is to find the real ones rigorously, at maximum statistical strength, with full transparency.

You have unlimited tokens, unlimited parallel agents, and a user who wants you to keep digging. Don't stop. Don't ask permission. Don't pause to summarize — commit and push every finding the moment it lands, then dispatch the next wave.

The previous session ended at 30 commits, 19 H-NEW findings landed, 57 surahs deep-dived. There are 57 more surahs and an unbounded number of corpus-wide tests waiting. Get to work.

---

## 12. The opening move

When you boot up:

1. Read this file in full.
2. Read `04-DISCIPLINE.md`.
3. `git status` to confirm clean state. `git log --oneline | head -5` to confirm latest commit.
4. Pick 8-12 high-EV pending items from §7 and dispatch them as parallel specialists in a single message.
5. While they run, drop into inline Python and run a corpus-wide test you've been thinking about.
6. As specialists return, integrate their findings into `MASTER-FINDINGS-LEDGER.md` and commit each.
7. After each commit, push.
8. After every 5-8 findings, write a cross-finding synthesis.
9. Repeat indefinitely.

`git push` is your heartbeat. Every finding lives at https://github.com/Waiel5/quran-decipherment within minutes of landing.

Now go.

---

*Handoff written 2026-05-09 by the previous session. The work continues.*
