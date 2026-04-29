---
id: H-NEW-126
title: "True-isolate-core characterization — what unites {Q 16, 21, 22, 23, 25}"
status: PRE-REGISTERED 2026-04-17
spec_locked_at: 2026-04-17 (all 4 cells locked BEFORE any null draws)
bonferroni_family: h-new-126-isolate-core
bonferroni_k: 4
alpha_bon: 0.0125  # 0.05 / 4
direction_A: "within-core pairwise mean root-Jaccard > null (5 random non-cluster surahs, 10K perms); ONE-SIDED upper"
direction_B: "5/5 surahs are concept-named (descriptive, >95% pre-commit per concept-name classification)"
direction_C: "rhetorical-mode clustering: within-core pairwise Euclidean distance (in imperative/declarative/interrogative ratio space) < null; ONE-SIDED lower; 10K perms; p < 0.0125"
direction_D: "descriptive — identify single most-distinctive feature per surah vs corpus (max or min on a single quantitative axis from the 9-axis descriptive profile)"
rules_tuple: "(no-tashkeel, hafs-kufan, canonical-114, Tanzil-JSON, morphology-0.4-roots for root-sets, 20-cluster cross-finding-010 lock)"
primary_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
morphology: /Users/grey/Downloads/quran/data/morphology/surah-root-graph.json
chronology: /Users/grey/Downloads/quran/data/revelation-order.csv
seed: 20260417
n_perm: 10000
author: h-new-126-specialist
prior_work_consulted:
  - findings/phase-b-hypotheses/cross-finding-010-extended-network.md (identified the 5-surah true-isolate core)
  - findings/phase-b-hypotheses/h-new-89-meta-cluster-network.md (parent 11-cluster scheme)
  - findings/phase-b-hypotheses/h-new-94-q16-q25-zone.md (zone shadow-cluster hunt, Cell B NULL-BROKEN)
  - findings/phase-b-hypotheses/h-new-125-chronology-content-prereg.md (content-axis operationalisations)
---

# [[h-new-126-isolate-core|H-NEW-126]] — True-isolate-core characterization

## Question

**[[cross-finding-010-extended-network|cross-finding-010]] identified 5 surahs — {Q 16 al-Naḥl, Q 21 al-Anbiyāʾ,
Q 22 al-Ḥajj, Q 23 al-Muʾminūn, Q 25 al-Furqān} — that are ISOLATES under
ALL 20 cluster systems** (no muqaṭṭāʿat, no oath-opener, no qul-opener,
no refrain cluster, no divine-attribute-named, no prophet-named, no
classical pair, no Friday liturgy, no musabbiḥāt, no mufaṣṣal
participation, etc.).

What unites this core? What separates them from every other surah?

## Provenance disclosure (garden-of-forking-paths)

**CRITICAL**: The 5 surahs were NOT identified by this specialist. They
emerge from [[cross-finding-010-extended-network|cross-finding-010]]'s 20-cluster extension as the survivors
of the Q 16-25 cluster-empty zone (dropped from 8/10 to 5/10). This is
a **POST-HOC-NOTICED SUBSET** under PRE-REG-STANDARD post-hoc protocol.

Consequences under the post-hoc protocol (HANDOFF/04-DISCIPLINE.md):
- **Single-test α = 0.05 cap** is applied at the per-cell level.
- **Bonferroni-4 within this family** tightens further to α_bon = 0.0125.
- **Verdict ceiling = PASS-DIRECTED** (NOT CONFIRMED) per cell, until
  INDEPENDENT REPLICATION on a distinct data dimension.
- Extreme p (< 10⁻¹⁰) would survive any conceivable Bonferroni.

## Cells (LOCKED BEFORE ANY NULL DRAW)

### Cell A — Shared content (primary inferential)

- Compute pairwise root-Jaccard between each pair of the 5 core surahs (10 pairs).
- Observed T_A = mean root-Jaccard over these 10 pairs.
- **Null**: randomly sample 5 non-cluster-core surahs from the 109-surah
  complement-set 10,000 times; compute same statistic. Direction: ONE-SIDED
  UPPER (core more similar than random non-core sets).
- **PASS** if p < 0.0125.

#### Positive control (MW-5)

- Sample 5 adjacent muqaṭṭāʿat-opened surahs {Q 17 is not muq-opened; use
  instead {Q 40, 41, 42, 43, 44} — the contiguous ḥawāmīm core, which
  share opener and are classically a cluster}. If pairwise root-Jaccard
  for {Q 40, 41, 42, 43, 44} does NOT significantly exceed null at
  α = 0.05 (one-sided upper), MW-5 FAILS → NULL-BROKEN.

### Cell B — Genre coherence (descriptive)

- Classify each surah's NAME by category:
  - **concept-name**: abstract concept, not a proper noun
    (e.g., al-Furqān = "the criterion", al-Muʾminūn = "the believers")
  - **prophet-name**: named after a prophet (Yūsuf, Nūḥ, etc.)
  - **event-name**: named after an event (al-Isrāʾ, al-Fatḥ, etc.)
  - **object-name**: named after a concrete object (al-Naḥl = "the bee",
    al-Mulk = "the dominion") — note al-Naḥl is an object/creature-name
  - **attribute-name**: divine-attribute name (al-Raḥmān, al-Malik, etc.)
  - **letter-name**: named after a muqaṭṭāʿat (Ṭā-Hā, Yā-Sīn, etc.)
- Pre-commitment: Expected 5/5 are "concept-or-object" (not prophet,
  event, attribute, or letter).
- Report mapping with justification. No null — this is descriptive.

### Cell C — Rhetorical mode (primary inferential)

For each of the 114 surahs, compute the per-verse ratio of three modes:
- **Imperative**: verse contains at least one known imperative opener
  token from the locked list: `{قل, قلنا, اقرأ, اعبدوا, اتقوا, آمنوا,
  ادعوا, اذكروا, انظروا, اسجدوا, اركعوا}` or verse starts with
  imperative-form (ifʿal/uktub/etc. — approximated by matching first
  token against the locked list).
- **Interrogative**: verse contains any of `{أ, هل, متى, أين, كيف, من,
  ما}` at the START of a token (whole-word or prefix of a token).
  Locked check: token equals one of `{أ, هل, متى, أين, كيف, من, ما}`
  OR token starts with `أَ` or `أ` with length ≥ 2 (likely interrogative hamza).
- **Declarative**: residual — every verse not matching imperative or
  interrogative.

For each surah, compute (imp%, int%, dec%) — a 3-vector (they sum to 100%).

- **Statistic T_C = mean pairwise Euclidean distance** within the 5-core
  in this 3-vector space.
- **Null**: 10,000 random 5-sets drawn from the 109 non-core surahs;
  compute same statistic. Direction: ONE-SIDED LOWER (core cluster-tight).
- **PASS** if p < 0.0125.
- **Positive control (MW-5)**: the musabbiḥāt inner-5 {Q 57, 59, 61,
  62, 64} — known tight cluster. If THAT does NOT fire at α = 0.05
  one-sided lower, NULL-BROKEN.

### Cell D — Per-surah unique feature (descriptive)

Compute for each of the 114 surahs a 9-axis descriptive profile:
1. `surah_length` (number of verses)
2. `mean_verse_length` (tokens per verse)
3. `allah_density` (Allah-tokens per 100 verses; locked token set
   `{الله, لله, اللهم}` + proclitic-stripped match)
4. `noldeke_rank` (continuous 1..114 from data/revelation-order.csv)
5. `unique_root_count` (size of root-set from surah-root-graph.json)
6. `root_density` (unique_root_count / total_word_tokens)
7. `prophet_narrative_density` (per-100-verse count of tokens matching
   locked prophet list `{موسى, عيسى, ابراهيم, نوح, يوسف, يونس, لوط,
   هود, صالح, شعيب, داود, سليمان, زكريا, يحيى, اسماعيل, اسحاق, يعقوب,
   ادم, ايوب, ادريس, الياس, اليسع, ذا, الكفل, فرعون, النبي, نبي,
   رسول, مرسل}`; prefix-tolerant whole-word match)
8. `first_word_token` (orthographic-token at verse 1, position 1 —
   descriptive, not quantitative)
9. `imperative_ratio` (from Cell C, % verses classified imperative)

For each of the 5 core surahs, identify the axis on which it scores
highest or lowest on a percentile basis vs corpus. Report the most
distinctive single feature per surah. Descriptive only; no null.

## MW-5 positive control bank

- Cell A: **ḥawāmīm core** {Q 40-44} — expect pairwise root-Jaccard
  significantly above null (p < 0.05 one-sided upper).
- Cell C: **musabbiḥāt inner-5** {Q 57, 59, 61, 62, 64} — expect
  within-cluster rhetorical distance significantly below null.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| All MW-5 pass; ≥2 of Cells A, C pass at α_bon | PASS-DIRECTED (CORE COHERENT); queue independent replication |
| MW-5 passes for at least one cell; 1 cell passes α_bon | MINIMAL SIGNAL — single axis of coherence |
| MW-5 fails for a cell | that cell → NULL-BROKEN (report honestly) |
| All MW-5 pass; 0 inferential cells pass | NULL (the 5-core is NOT a hidden cluster — it is truly heterogeneous) |
| Cell B (descriptive): ≥4/5 concept-or-object | GENRE-COHERENT (descriptive) |

## Expected a-priori results (honest guesses)

- Cell A: UNCERTAIN. These 5 surahs are cluster-empty by all 20 axes;
  there is **no a-priori reason** to expect shared roots beyond corpus
  baseline. A NULL result would be the MOST HONEST finding (they are
  isolates because they have no shared structure).
- Cell B: 5/5 concept-named is PRE-COMMITTED (al-Naḥl = the Bee is
  object/creature; al-Anbiyāʾ = the Prophets is plural-concept; al-Ḥajj
  = Pilgrimage is concept; al-Muʾminūn = the Believers is plural-concept;
  al-Furqān = the Criterion is concept). All 5 are concept/object, NONE
  are prophet/event/attribute/letter-named.
- Cell C: UNCERTAIN. If these surahs share a rhetorical mode (e.g., all
  heavy on interrogatives), that would be SURPRISING and revealing.
- Cell D: Expected per-surah distinctive axes vary: al-Ḥajj is likely
  Medinan outlier in the zone; al-Naḥl is likely max unique_root_count
  for its length; etc.

## Garden-of-forking-paths log (BEFORE RUNNING)

### Choices made (locked)
1. The 5-surah target is POST-HOC per [[cross-finding-010-extended-network|cross-finding-010]]; single-test α=0.05 cap applies.
2. Bonferroni-4 within this family. Tightens to α_bon = 0.0125.
3. Direction LOCKED per cell (see YAML).
4. Null = random 5-sets from the 109 non-core surahs (NOT from the full 114).
5. Cell B descriptive only; Cell D descriptive only.
6. MW-5 cells selected BEFORE running (ḥawāmīm for A, musabbiḥāt for C).

### Choices NOT made (to avoid forking)
- We are NOT adding a 5th inferential cell. If we notice a striking
  pattern in Cell D, we file it as new H-NEW-126.1.
- We are NOT using char-ngram similarity (as in [[h-new-94-q16-q25-zone|H-NEW-94]] Cell B);
  root-Jaccard is the single locked similarity for Cell A.
- We do NOT residualize by length. Length is captured separately in
  Cell D as axis 1.

### Alternative rule tuples considered and rejected
- Using ALL pairs of non-core surahs as the null (C(109,2)=5886 pairs).
  Rejected because the core is 5 surahs, so null of 5-tuples is direct
  and exchangeability-correct.
- Extending the core to {Q 16, 21, 22, 23, 25, 33, 34, 39, 48} (the
  broader 20-cluster isolate list). Rejected because [[cross-finding-010-extended-network|cross-finding-010]]
  specifically identifies the 5 as the Q 16-25 CORE; the other 4 are
  Q 33-48 zone isolates (different zone). Keeping the scope pre-reg-tight.

## MW-7 internal error gate

Before promoting, verify:
1. Core list {16, 21, 22, 23, 25} matches [[cross-finding-010-extended-network|cross-finding-010]] exactly.
2. Null sampling excludes all 5 core surahs.
3. Bonferroni k=4 matches cells (A inferential, B descriptive, C inferential, D descriptive). Actually only 2 inferential → we set k=4 as the family ALPHA lock, even though descriptive cells do not need a p-value. This is the CONSERVATIVE choice (tightening, not loosening). Documented here.
4. MW-5 runs BEFORE the target cells.

## Integrity

- Seed: 20260417
- N_perm: 10,000
- Bonferroni k = 4; α_bon = 0.0125
- Direction LOCKED per cell (one-sided upper for A, one-sided lower for C)
- Post-hoc-subset disclosed; single-test cap at α = 0.05
- Author: [[h-new-126-isolate-core|h-new-126]]-specialist
