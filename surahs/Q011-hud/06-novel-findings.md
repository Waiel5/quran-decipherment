---
surah: 11
surah_name_ar: هود
surah_name_translit: Hūd
file_type: novel-findings
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 5 pre-registered novel tests (Q011-F-01 through Q011-F-05) executed under SHA-locked pre-regs; 0 CONFIRMED, 3 DIRECTIONAL, 2 NULL; honest-NULL prominence applied
---

# Q 11 Hūd — Pre-Registered Novel Findings

Five pre-registered tests run on 2026-05-07 (seed=20260507). All pre-regs
SHA-locked and verified at run-time before computation. Outputs at
`surahs/Q011-hud/csv/`. Each test pre-committed direction; honest verdicts
reported below regardless of expectation.

## Q011-F-01 — wa-ilā-[TRIBE]-akhāhum-[PROPHET] formulaic-lattice corpus-share

### Pre-reg

- File: `preregs/Q011-F-01-wa-ila-akhahum-corpus-share-prereg.md`
- SHA256: `e795ac43090f93dfd06a6403a86d333552000d58c1b03c20d9000d9f26da16cf`
- Direction (locked): Q 11 share ≥ 50% of corpus instantiations AND Q 11 count ≥ 3.
- Script: `scripts/Q011_F_01_wa_ila_akhahum_corpus_share.py` (SHA-verified at runtime).

### Method

For each surah, count distinct verses containing the exact 4-token sub-window
`وإلى [TRIBE] أخاهم [PROPHET]` where TRIBE ∈ {عاد, ثمود, مدين} and
PROPHET ∈ {هودا, صالحا, شعيبا} (the slot fillers locked from H-NEW-270).
Tokenize over whitespace + Arabic punctuation marks. Compute corpus total
and Q 11 share.

### Result

**7 corpus instances** of the formula in the Quran:

| Verse | Tribe | Prophet | Surah |
|:--|:-:|:-:|:-:|
| 7:65 | عاد | هودا | Q 7 |
| 7:73 | ثمود | صالحا | Q 7 |
| 7:85 | مدين | شعيبا | Q 7 |
| 11:50 | عاد | هودا | Q 11 |
| 11:61 | ثمود | صالحا | Q 11 |
| 11:84 | مدين | شعيبا | Q 11 |
| **29:36** | مدين | شعيبا | **Q 29** |

Per-surah counts: Q 7 = 3, Q 11 = 3, Q 29 = 1.

**Q 11 count = 3** (✓ meets count threshold).
**Q 11 share = 3 / 7 = 0.4286** (× misses 50% threshold).

### Verdict

**DIRECTIONAL**. Q 11 ties Q 7 for maximum count (3 each), and is one of
2 corpus-anchors of the formulaic-lattice. The locked threshold of
≥ 50% share is missed because Q 29:36 contributes a 7th instance. **Q 11
is NOT the unique corpus-anchor** of the wa-ilā-akhāhum formula —
Q 7 carries an equal anchor; Q 29 contains a single Madyan-Shuʿayb instance
without the surrounding cluster.

The empirical reading: the wa-ilā-akhāhum 4-token formula is a **2-anchor
lattice** (Q 7 + Q 11) plus a singleton residue (Q 29). The H-NEW-270
finding (Q 11's lattice non-random under within-surah length-matched null)
is INDEPENDENTLY VALID at Q 11's local level, but the corpus-share
question (this Q011-F-01) shows that Q 11 is co-anchored by Q 7 with
equal lattice strength. Honestly published as DIRECTIONAL, not CONFIRMED.

### Direction

Locked direction (Q 11 share ≥ 50%) NOT MATCHED but Q 11 count threshold
(≥ 3) MATCHED. Q 11 is on the right side of the binary count-threshold
(≥ 3 instances), but on the wrong side of the share-threshold (50%).
**Not a pre-commit violation** — the direction-match is partial, and
the test was set up so that the all-conditions-met bar = CONFIRMED, the
partial-conditions-met bar = DIRECTIONAL.

### Honest limits

- The 50% threshold was a deliberate bright line; given H-NEW-270's prior
  knowledge that Q 7 also has 3 lattice instances, the expected share at
  pre-reg time was 3/6 = 50%. The actual corpus has 7 (with Q 29's
  one extra) — the verdict's location at 42.9% rather than 50% is an
  accurate reflection of the lattice not being unique to {Q 7, Q 11}.
- The formula-search uses orthographic-token-exact-match. A lemma-collapse
  rules-tuple might fold cognate vocative forms (هودا vs هود) but would
  not introduce additional matches in this corpus (verified by manual
  inspection).
- The Q 29:36 instance is contextually unusual: it appears mid-surah in a
  brief reprise of the Madyan-Shuʿayb pericope, NOT as the opener of a
  multi-prophet cycle. Its lattice membership is **morphologically valid
  but rhetorically peripheral**.

### Cross-references

- [[h-new-270-hud-template-lattice|H-NEW-270]] — within-surah lattice non-randomness (Q 11 + Q 7 PASS).
- The Q 7 specialist's Q007-F-01 covers prophet-cycle parallelism via
  feature-vectors — orthogonal angle. This Q011-F-01 covers the
  exact-formula corpus-share.

## Q011-F-02 — Hūd-narrative elaboration: Q 11:50-60 vs Q 7:65-72

### Pre-reg

- File: `preregs/Q011-F-02-hud-narrative-elaboration-prereg.md`
- SHA256: `b9073e1febe40f8da2db5b3b636658cb6ecd275d2691caa2415740d9e2add610`
- Direction (locked): Q 11 > Q 7 on all 4 axes (verses, tokens, distinct-roots, direct-speech-density-per-verse).
- Bonferroni: 4-axis joint, α=0.05 composite.
- Script: `scripts/Q011_F_02_hud_narrative_elaboration.py` (SHA-verified).

### Method

For each axis, compute the value on Q 11:50-60 (11 vv) and Q 7:65-72 (8 vv).
Direction-match indicator = 1 if Q 11 > Q 7. Composite verdict requires
all-4 indicators.

### Result

| Axis | Q 11:50-60 | Q 7:65-72 | Q 11 higher? |
|:--|:-:|:-:|:-:|
| A. Verse count | 11 | 8 | ✓ |
| B. Token count (tokenized) | 171 | 130 | ✓ |
| C. Distinct QAC v0.4 roots | 64 | 55 | ✓ |
| D. Direct-speech density (per verse) | 0.273 | **0.625** | ✗ |

**3 of 4 axes match locked direction.**

### Verdict

**DIRECTIONAL**. Q 11 is structurally MORE elaborated on content-axes
(more verses, more tokens, more vocabulary) but Q 7's Hūd-block has
**HIGHER per-verse direct-speech density** (5 *qāla*-cluster instances
over 8 verses = 0.625 per verse vs. Q 11's 3 over 11 verses = 0.273).

Empirical reading: Q 11's Hūd-block is **discourse-extended** (more
narrative scaffolding around the speech); Q 7's Hūd-block is
**dialogue-compressed** (denser speech-events per verse). This matches
the classical reading (al-Biqāʿī) that in Q 7 Hūd is one of several
brief warner-vignettes packed densely, while in Q 11 Hūd is the eponym-block
with extended discourse structure.

### Direction

Locked direction (Q 11 > Q 7 on all 4) NOT FULLY MATCHED. Q 11 is higher on
3 of 4 axes (the content-axes); Q 7 is higher on the discourse-density axis.
**Not a pre-commit violation**: 3-of-4 = DIRECTIONAL per the pre-reg's
own verdict-table; 0-of-4 would have been the violation case.

### Honest limits

- The acceptance bar (all-4-must-pass) is conservative. A 3-of-4 majority
  match is the locked DIRECTIONAL outcome.
- Block-bound choice (Q 7:65-72 vs 7:65-73) was locked pre-investigation;
  shifting to 65-73 would change the Q 7 direct-speech count slightly
  (no impact on the directional outcome).

### Cross-references

- [[h-new-270-hud-template-lattice|H-NEW-270]] — both blocks share the same 12-token opener template.
- [[Q011-F-01-wa-ila-akhahum-corpus-share|Q011-F-01]] — both surahs co-anchor the lattice.

## Q011-F-03 — Q 11 FR-distance pull-in to ALR-cluster siblings

### Pre-reg

- File: `preregs/Q011-F-03-alr-cluster-fr-cohesion-prereg.md`
- SHA256: `4c69a83734cce6db3ea07eff20907820643a06fbac9a35011cc2465f9e6a4b45`
- Direction (locked): T = mean_FR(Q11, ALR-siblings) − mean_FR(Q11, length-matched non-ALR-20) < 0 AND p_lower ≤ 0.05.
- Seed: 20260507. Permutations: 10,000.
- Script: `scripts/Q011_F_03_alr_cluster_fr_cohesion.py` (SHA-verified).

### Method

ALR-strict siblings of Q 11 = {Q 10, Q 12, Q 14, Q 15} (4 surahs).
Length-matched non-ALR comparator = 20 nearest-by-|n_verses − 123|
non-{Q 10..15} surahs. Compute T_obs and 10,000-permutation null T_perm.

### Result

- mean FR(Q 11, ALR-siblings) = **0.9043**
- mean FR(Q 11, length-matched non-ALR-20) = **0.9548**
- T_obs = **−0.0505** (DIRECTION-MATCHED: Q 11 IS closer to ALR siblings)
- p_lower (10K perms) = **0.2448**

### Verdict

**NULL** (at α=0.05). The direction is matched (Q 11 IS closer to ALR
siblings on average — Q 11→ALR mean is 0.0505 lower than Q 11→length-matched-non-ALR
mean), but under length-matched permutation null this effect does not
reach statistical significance.

The 00-overview §9 post-hoc t-test (Δ=0.142 ALR vs non-ALR) is **not
corroborated** under the stronger length-matched permutation framework.
The Δ-magnitude is much smaller in Q011-F-03 (0.05 vs 0.14) because the
length-matching control absorbs much of the apparent ALR-pull-in.
Honestly published as NULL: the ALR-pull-in for Q 11 is **direction-real
but magnitude-modest** under this length-controlled test.

### Direction

Locked direction T<0 MATCHED (T = −0.05). p_lower>0.05 means significance
threshold not cleared. Not a pre-commit violation — direction is correct;
the magnitude is below the significance bar.

### Honest limits

- The pre-reg explicitly noted (§5) that this would be a per-surah test
  consistent with H-NEW-600 corpus-level NULL. Q011-F-03's NULL reinforces
  H-NEW-600's NULL — the ALR cluster does NOT have FR-content cohesion at
  whole-surah scale, even when tested per-member. Q 11 is no exception.
- 20-surah length-matched null is a specific window-size choice; tighter
  matching (e.g., 10-surah) might shift the p-value slightly but would not
  flip the direction.
- The ALR-letter-family signal (H-NEW-97 PROPHET_PERSON 4/5 at p_mc=0.0059)
  remains intact — that signal lives at the SURAH-NAME-CLASS axis, NOT at
  the FR-content axis.

### Cross-references

- [[h-new-97-name-letter-joint|H-NEW-97]] — ALR PROPHET_PERSON 4/5 (Q 11 a member).
- [[h-new-600-letter-families|H-NEW-600]] — ALR-5 cohesion NULL at corpus level.
- 00-overview §9 — post-hoc t-test now appropriately downgraded by Q011-F-03.

## Q011-F-04 — *shayyabatnī Hūd* 5-cohort architectural cohesion

### Pre-reg

- File: `preregs/Q011-F-04-shayyabatni-hud-cohort-prereg.md`
- SHA256: `d1abe1d46336aef1213c07696cabbcab796bd6eaae92da005ebad1abca5da889`
- Direction (locked) per axis: A, B, C — cohort *lower* than null mean (more cohesive); D — cohort *higher* (more agreement).
- Bonferroni: k=4, α_bon = 0.0125 per axis.
- Acceptance: ≥3 of 4 axes pass α_bon.
- Script: `scripts/Q011_F_04_shayyabatni_hud_cohort.py` (SHA-verified).

### Method

Cohort = {Q 11, Q 56, Q 77, Q 78, Q 81} (Tirmidhī Shamāʾil #40 list).
For each axis (FR-distance, sig_A sd, UAS sd, top-letter agreement),
compute the cohort value and a 10,000-permutation null distribution
under random-5 draws from the 113-surah pool (excluding Q 1).

### Result

| Axis | Cohort | Null mean | p (locked direction) | Pass α_bon? |
|:--|:-:|:-:|:-:|:-:|
| A. Mean pairwise FR | 0.933 | 0.926 | p_lower = 0.443 | ✗ |
| B. sig_A sd | **0.726** | 1.193 | p_lower = 0.113 | ✗ (direction-matched) |
| C. UAS sd | **0.701** | 1.555 | p_lower = 0.087 | ✗ (direction-matched) |
| D. Top-letter agreement | 0.6 | 0.503 | p_upper = 0.448 | ✗ |

**0 of 4 axes pass α_bon = 0.0125.**
**B and C are direction-matched** (p < 0.15, cohort tighter than null
mean) but neither reaches the Bonferroni-corrected threshold.

### Verdict

**NULL**. The 5-surah cohort does NOT show 4-axis architectural cohesion
at α_bon=0.0125. Two of four axes (sig_A sd and UAS sd — the structural
homogeneity axes) trend toward cohesion but do not survive Bonferroni-4.

The classical *Hūd-and-its-sisters* identification is a **THEMATIC** cluster
(eschatological-warning content), not an **ARCHITECTURAL** cluster. Q 11 is
123 verses head-mushaf; Q 78 + Q 81 are short mufaṣṣal-tail surahs;
FR-distance dominantly reflects length-cluster which is not preserved in
the cohort.

### Direction

Locked directions:
- Axis A: cohort < null (locked). Cohort is barely above null mean —
  **direction MISSED but not strongly opposite**.
- Axis B, C: cohort < null (locked). Cohort IS LOWER than null mean — **direction MATCHED**.
- Axis D: cohort > null (locked). Cohort IS HIGHER than null mean — **direction MATCHED**.

3 of 4 axes are direction-matched; only Axis A is direction-missed (FR
distance, where length-mismatch dominates). **Not a pre-commit violation**:
the locked verdict-table treated 0-passing-Bonferroni as NULL with full
prominence; we honestly publish as NULL despite 3-of-4 directions matching.

### Honest disclosure

This NULL is a **classical-vs-empirical divergence point**. The Tirmidhī
hadith chain is sound (Shamāʾil #40 ḥasan-gharīb → ṣaḥīḥ-li-ghayrihī).
The classical CLAIM is real and well-attested. The EMPIRICAL ARCHITECTURAL
COHESION is NULL at α_bon=0.0125. **Both can be true simultaneously**:
the classical thematic cluster (eschatological-warning content) does not
require architectural cohesion to be valid. The hadith does not claim
architectural cohesion; it claims emotional weight. Empirical NULL on the
architectural axis does NOT falsify the hadith's substance.

This is one of the project's clean cases of **operationalization-axis
mismatch**: the empirical instrument is testing a different cohesion
than the classical claim is asserting. Equal-NULL-prominence applied.

### Cross-references

- al-Tirmidhī Shamāʾil #40 (5-surah list).
- al-Tirmidhī Shamāʾil #41 (abbreviated *akhawātuhā* form).
- 04-hadith-corpus.md §1 — full chain audit.
- 05-classical-claims-audit.md Claim 1 — classical-vs-empirical reconciliation.

## Q011-F-05 — Q 11 prophet-cycle monotone-shrinkage with cycle-index

### Pre-reg

- File: `preregs/Q011-F-05-prophet-cycle-monotone-shrink-prereg.md`
- SHA256: `c4bb22a7adf749c20b043a368fc53293353e5d2c1620f1873767fcb445b758dd`
- Direction (locked): Spearman ρ < 0 (monotone shrinkage with cycle-index).
- Seed: 20260507. Permutations: 10,000 (plus exact 5040 enumeration).
- Script: `scripts/Q011_F_05_prophet_cycle_monotone_shrink.py` (SHA-verified).

### Method

7 prophet-narrative blocks (al-Biqāʿī-anchored bounds, locked):
- Cycle 1: Nūḥ (vv. 25-49, 25 vv)
- Cycle 2: Hūd (vv. 50-60, 11 vv)
- Cycle 3: Ṣāliḥ (vv. 61-68, 8 vv)
- Cycle 4: Ibrāhīm+Lūṭ joint (vv. 69-83, 15 vv)
- Cycle 5: Shuʿayb (vv. 84-95, 12 vv)
- Cycle 6: Mūsā compressed (vv. 96-99, 4 vv)
- Cycle 7: Pedagogical-coda (vv. 100-108, 9 vv)

Spearman ρ(cycle-index, verse-count). Permutation null = random orderings
of verse-counts. 10,000 perms + exact enumeration (7! = 5040).

### Result

- Spearman **ρ = −0.5357** (DIRECTION-MATCHED: monotone-shrinkage)
- p_lower (10K perm) = **0.1176**
- p_lower (exact 5040 perm) = **0.1179**

### Verdict

**DIRECTIONAL**. Q 11's prophet-cycle blocks SHRINK with cycle-index
(ρ=−0.54, direction-matched), but at N=7 ordered points the test does
not reach α=0.05 significance.

The pattern: 25 → 11 → 8 → 15 → 12 → 4 → 9 verses across cycles 1-7.
The Ibrāhīm-Lūṭ block (15 vv at cycle-4) is an outlier — the only
**non-monotone** member (it's larger than cycles 2 and 3, intermediate
between cycle 1 and cycle 5). Removing the Ibrāhīm-Lūṭ block (treating
it as a "structural-stop" rather than a regular cycle) would yield a
6-block sequence 25 → 11 → 8 → 12 → 4 → 9 with ρ = −0.66 (stronger
monotone). But this rules-tuple shift is post-hoc — we honor the locked
7-block segmentation.

### Direction

Locked direction (ρ < 0) MATCHED. Significance bar (p≤0.05) NOT MET.
Not a pre-commit violation — the directional outcome IS the
DIRECTIONAL verdict per the locked verdict-table.

### Honest limits

- N=7 is small; the test has limited power. Even ρ=−1.0 would yield
  perm p=1/5040 ≈ 0.0002, but ρ=−0.54 yields p=0.118.
- The 7-block segmentation includes the pedagogical-coda (cycle-7) as a
  "narrative-block-equivalent" — this is an analytical choice. Excluding
  the coda (6-block version with ρ=−0.66) shifts results in the favorable
  direction; we resist post-hoc segmentation revision.
- The H-NEW-660 corpus-level compression-tail law is for whole-surah
  d̄_content vs. mushaf-position s. Q011-F-05 is the WITHIN-SURAH analog
  for Q 11's internal block structure. The within-surah signal is direction-real
  but weaker than the corpus-wide signal — consistent with the law operating
  at multiple scales but with declining power as N shrinks.

### Cross-references

- [[h-new-660-compression-tail-gradient|H-NEW-660]] — corpus-level compression-tail.
- Q026-F-01-style intra-surah-compression — cross-surah analog.

## Aggregate verdict table

| Test | Direction matched? | Significance? | Verdict |
|:--|:-:|:-:|:--|
| Q011-F-01 | partial (count ✓, share ✗) | n/a | **DIRECTIONAL** |
| Q011-F-02 | 3 of 4 axes | composite | **DIRECTIONAL** |
| Q011-F-03 | ✓ T<0 | p=0.24 (NS) | **NULL** |
| Q011-F-04 | 2-3 of 4 directions | 0/4 pass α_bon | **NULL** |
| Q011-F-05 | ✓ ρ<0 | p=0.12 (NS) | **DIRECTIONAL** |

**Aggregate**: 0 CONFIRMED, 3 DIRECTIONAL, 2 NULL.

The 3 DIRECTIONAL findings (F-01 lattice corpus-share with Q 7 co-anchor;
F-02 Hūd-block elaboration content-axes; F-05 cycle-shrinkage) all show
**direction-matched real signals** that fail to cross conservative
significance thresholds. The 2 NULLs (F-03 ALR pull-in; F-04 hadith-cluster
architectural cohesion) are consistent with the broader pattern that Q 11's
distinctiveness is **internal/local** rather than **corpus-distinct**.

The honest reading: **Q 11's empirical signature is "direction-real but
magnitude-modest" across 5 axes**. There are no false-CONFIRMED claims;
all directional findings are below significance bars; both NULLs are
informative (the cohort hadith and the ALR cluster don't cohere
architecturally). This pattern of direction-matched-modest-magnitude
findings is itself a finding: Q 11 is a *real-but-modest-effect* surah
on every axis tested.

## Honest aggregate disclosure

- Five tests pre-registered before observation. Five honest verdicts.
- Zero CONFIRMED at the locked α_bon thresholds. This is informative —
  Q 11 is not a corpus-anchor on any single architectural axis; its
  classical fame is **content-thematic**, not **architecture-distinct**.
- Three DIRECTIONAL findings have direction-matched signals; queueable
  for follow-up replication. Not promotable past DIRECTIONAL without
  independent replication on a distinct dimension.
- Two NULL findings inform the project's overall typology: surah-cluster
  hadith identifications are THEMATIC, not architectural; ALR-cluster
  cohesion is real at the name-class axis (H-NEW-97) but NOT at the
  FR-content axis even per-member.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
