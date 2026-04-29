---
finding_id: h-new-196-oath-cluster
phase: B
status: PASS — 3 of 3 cells fired (Cells V, H1, H2 PASS)
date: 2026-04-17
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, H-NEW-85-locked-oath-set, K_TOP=500, DIRICHLET_ALPHA=0.5, Fisher-Rao metric)
null_models: 10,000-perm random 21-surah samples (Cell H1); 10,000-perm random-assignment null (Cell H2)
bonferroni_k: 2
alpha_bon: 0.025
seed: 20260419
prereg_sha256: 17667fbbcb5ed1a696bfdc58f05b6a28e33e13373625f71db45cde9421db296d
author: h-new-196-autonomous
parent: h-new-85-oath-openers
---

# [[h-new-196-oath-cluster|H-NEW-196]] — Oath-opening surahs form a mechanically distinct cluster in Fisher-Rao compositional space

## Headline

The 21 classical waw-qasam-opening surahs ([[h-new-85-oath-openers|H-NEW-85]] locked set) form a
**significantly tighter cluster in Fisher-Rao information space** than
random 21-surah samples (mean pairwise D = 0.794 vs null mean 0.923;
z = −3.12; **p = 0.0073**, passes α_bon = 0.025), AND disproportionately
concentrate in a specific compositional mode under 5-means clustering
(**χ² = 17.86, p = 0.0005**, passes α_bon = 0.025). **The waw-oath
rhetorical gear has a measurable compositional footprint.**

This refines [[h-new-85-oath-openers|H-NEW-85]]'s dual NULL (length + jawāb-theme): while oath-openers
are NOT distinct on *those* two axes, they ARE distinct on the broader
**top-500-root probability profile** captured by Fisher-Rao. The intuition
that oath-opening surahs "feel similar" is mechanically real — it is
encoded in lexical-root distribution, not in surface length or macro-theme.

## Verdict table

| Cell | Test | Result | Verdict |
|---|---|---|---|
| V | v1/v2 wa-prefix scan of all 114 | 21/21 OATH_21 in candidates | **PASS** |
| H1 | M(oath-21) < M(rand-21), perm | p = 0.0073 (z = −3.12) | **PASS** |
| H1-sens | Task-stated 22-surah list | M = 0.734, p = 0.0005 | even tighter |
| H2 | χ² mode-assignment (k=5) | χ² = 17.86, p = 0.0005 | **PASS** |

**3 of 3 cells fire at α_bon = 0.025 (k=2 outer; Cell V is verification,
not a statistical test).**

## Cell V — mechanical verification of the 21-oath list

Scanning v1 (first 2 tokens, separators stripped) + v2 for muqaṭṭaʿāt-
prefixed surahs, the wa-prefix scan recovers **21/21** of the [[h-new-85-oath-openers|H-NEW-85]]
locked oath list plus **4 extras** (Q 56, Q 80, Q 83, Q 104) that open
with a waw-particle but whose waw is NOT the classical qasam-particle:

- **Q 56 al-Wāqiʿa** v1 "*idhā waqaʿat al-wāqiʿa*" — no waw-qasam; my scan
  hit "*wa-l-ʿaṣr*"-pattern false positive on a different word.
- **Q 80 ʿAbasa** v1 "*ʿabasa wa-tawallā*" — waw is coordinating, not qasam.
- **Q 83 al-Muṭaffifīn** v1 "*waylun li-l-muṭaffifīn*" — *way-l*, not *wa-l*.
- **Q 104 al-Humaza** v1 "*waylun li-kulli humazatin lumaza*" — same *way-l*.

None of the 4 extras open with a true *wa-qasam*. The [[h-new-85-oath-openers|H-NEW-85]] list
(established via QAC STEM-walker on the OATH_PARTICLE class) is
**mechanically correct** and the task-stated list (Q 37, 51, 52, 53, 56,
68, 75–79, 81, 84, 85, 86, 89, 90, 91, 92, 95, 100, 103 = 22 surahs)
**incorrectly includes** 7 non-waw-qasam openers (Q 56, 75, 76, 78, 81,
84, 90) while **excluding** 6 true waw-qasam openers (Q 36, 38, 43, 44,
50, 93). **Cell V PASS: [[h-new-85-oath-openers|H-NEW-85]] locked list is the correct 21-set.**

## Cell H1 — Fisher-Rao cluster cohesion (PRIMARY, PASS)

Setup: K_TOP=500 stem roots from QAC, Dirichlet α=0.5 smoothing,
L1-normalized per-surah probability vectors, Fisher-Rao
distance D_ij = 2·arccos(Σ √(p_i · p_j)). 114×114 matrix.

Test statistic: M(S) = mean of all (|S| choose 2) pairwise distances.

| quantity | value |
|---|---|
| M(OATH_21) | **0.7937** |
| null mean (10,000 perms, |S|=21) | 0.9232 |
| null sd | 0.0415 |
| null min | ~0.74 (comparable to OATH) |
| null 1% quantile | 0.824 |
| null 5% quantile | 0.855 |
| null 50% quantile | 0.925 |
| null 95% quantile | 0.988 |
| z(M_oath) | **−3.118** |
| **p_H1 (one-sided lower)** | **0.0073** |

The oath-21 cluster is **3.1 σ tighter** than random draws. **PASS
α_bon = 0.025.**

### Sensitivity — task-stated 22-surah list

Running the identical test on the task-stated alternate 22-surah list
(which mis-includes Q 56, 75, 76, 78, 81, 84, 90 and mis-excludes Q 36,
38, 43, 44, 50, 93):

| quantity | value |
|---|---|
| M(task-list-22) | **0.7336** |
| null mean (10,000 perms, |S|=22) | ~0.923 |
| p_sens | **0.0005** |

**The task-stated list is EVEN TIGHTER.** Why? Because it over-weights
the Mufaṣṣal short-Meccan block (Q 75–92) where successive surahs share
massive root vocabulary. Replacing the muqaṭṭaʿāt-prefixed long
INSTRUMENTAL_SCRIPTURAL oath-openers (Q 36, 38, 43, 44, 50) — which
inject the ḥawāmīm/alif-lam-mim lexical profile — with more short
Mufaṣṣal surahs further tightens the cluster. **Both lists yield
highly significant cluster cohesion; the [[h-new-85-oath-openers|H-NEW-85]] locked list is the
more conservative (correctly-specified) test.**

## Cell H2 — k-means mode assignment (SECONDARY, PASS)

k-means (k=5) on the Hellinger-embedded (√-prob) surah vectors, seed
20260419. Resulting modes:

| Mode | n_total | n_oath | rate | character (inferred from members) |
|---|---|---|---|---|
| 0 | 19 | 0 | 0.000 | Madinan legislative block (Q 2, 3, 4, 5 vicinity) |
| 1 | 26 | 0 | 0.000 | Long Meccan narrative (Q 6, 7, 10–18) |
| 2 | 7 | 2 | 0.286 | Mid-Meccan prophetic cycle (incl. Q 37, 43) |
| 3 | 51 | **13** | **0.255** | **Late-Meccan Mufaṣṣal** (Q 53, 55–114) |
| 4 | 11 | **6** | **0.545** | **ḥawāmīm / muq-cluster** (Q 15, 20, 32, 36, 38, 44, 50, 51, 52, 54, 67) |

**χ² = 17.86, df = 4, p_perm = 0.0005. PASS α_bon = 0.025.**

### Per-oath-surah mode assignment

| Oath surah | Mode | Category |
|---|---|---|
| Q 36 Yā-Sīn | 4 | INSTR_SCRIPT (muq-cluster) |
| Q 37 aṣ-Ṣāffāt | 2 | KIN_AG (mid-Meccan narrative) |
| Q 38 Ṣād | 4 | INSTR_SCRIPT (muq-cluster) |
| Q 43 az-Zukhruf | 2 | INSTR_SCRIPT (mid-Meccan narrative) |
| Q 44 ad-Dukhān | 4 | INSTR_SCRIPT (muq-cluster) |
| Q 50 Qāf | 4 | INSTR_SCRIPT (muq-cluster) |
| Q 51 adh-Dhāriyāt | 4 | KIN_NAT (muq-cluster) |
| Q 52 aṭ-Ṭūr | 4 | TERR (muq-cluster) |
| **Q 53 an-Najm** | **3** | **CELEST (Mufaṣṣal)** |
| Q 68 al-Qalam | 3 | INSTR_SCRIPT (Mufaṣṣal) |
| Q 77 al-Mursalāt | 3 | KIN_AG (Mufaṣṣal) |
| Q 79 an-Nāziʿāt | 3 | KIN_AG (Mufaṣṣal) |
| Q 85 al-Burūj | 3 | CELEST (Mufaṣṣal) |
| Q 86 aṭ-Ṭāriq | 3 | CELEST (Mufaṣṣal) |
| Q 89 al-Fajr | 3 | TEMP (Mufaṣṣal) |
| **Q 91 ash-Shams** | **3** | **MIXED (Mufaṣṣal) — structural max** |
| Q 92 al-Layl | 3 | TEMP (Mufaṣṣal) |
| Q 93 aḍ-Ḍuḥā | 3 | TEMP (Mufaṣṣal) |
| Q 95 at-Tīn | 3 | TERR (Mufaṣṣal) |
| Q 100 al-ʿĀdiyāt | 3 | KIN_AG (Mufaṣṣal) |
| Q 103 al-ʿAṣr | 3 | TEMP (Mufaṣṣal) |

**The 21 oath-openers split 13/6/2/0/0 across the 5 modes**, concentrating
overwhelmingly in the Mufaṣṣal mode (Mode 3: 13 surahs) and the
muq-cluster mode (Mode 4: 6 surahs). Modes 0 (Madinan legislative) and
Mode 1 (long Meccan narrative) contain ZERO oath-openers — a striking
absence. **The waw-qasam rhetorical gear is a Late-Meccan / muq-cluster
phenomenon in compositional space.**

Mode 4 is particularly striking: **6 of its 11 members (55%) are
oath-openers**. Mode 4 contains exactly the "muqaṭṭaʿāt-prefixed
oath-cluster" subset of classical taxonomy — Q 15 (*alr*), Q 20
(*ṭh*), Q 32 (*alm*), Q 36 (*ys*), Q 38 (*ṣ*), Q 44 (*ḥm*), Q 50
(*q*), Q 51 (no muq but same block), Q 52 (no muq but same block),
Q 54 (no muq but same block), Q 67 (no muq but same block) — almost
every member either has muqaṭṭaʿāt OR opens with a waw-qasam, and
most have both. **Mode 4 is the "opening-marker cluster" in lexical
space.**

## Q 91 al-Shams and the Mufaṣṣal mode

[[h-new-85-oath-openers|H-NEW-85]] established Q 91 as the UNIQUE structural maximum on three
oath-axes (7-verse cluster, 8 head-NPs, 4 category-diversity). Here we
confirm Q 91 sits inside Mode 3 — the late-Mufaṣṣal block — alongside
12 other short-Meccan oath-openers. Q 91 is NOT a compositional outlier
within the oath-opener family; it is the **structural maximum of a
coherent compositional cluster**. Its uniqueness is in its oath-verse
count (7, vs next 5 in Q 77, Q 79), not in its root-vocabulary profile.

## Novel findings

1. **Oath-openers form a Fisher-Rao-tight cluster** at z = −3.1 (p =
   0.0073), refining [[h-new-85-oath-openers|H-NEW-85]]'s NULL cells 4+5. Length and macro-theme
   don't separate oath-openers from other Meccan surahs — but the
   deeper top-500-root compositional profile DOES. Ways-of-speaking-
   about-the-world (lexical profile) cohere more strongly than surface
   dimensions.

2. **Two-mode partition of oath-openers**: Mode 3 (Mufaṣṣal, n=13) +
   Mode 4 (muq-cluster, n=6) = 19/21 = 90% of the oath-opener family.
   The INSTRUMENTAL_SCRIPTURAL sworn-by profile (Q 36, 38, 43, 44, 50)
   is precisely what places those surahs in the muq-cluster Mode 4 —
   the "book-oath" surahs are compositionally a ḥawāmīm-adjacent block.

3. **Mode 4's 55% oath-density**: the muqaṭṭaʿāt-cluster mode is the
   **single most oath-dense mode in the corpus**. Combined with prior
   findings on muqaṭṭaʿāt-oath correlation ([[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]), this
   positions the *muq → wa-l-kitāb* sequence as a structural formula:
   isolated-letter + book-oath = signature opening of a specific
   compositional block.

4. **Modes 0+1 contain ZERO oath-openers** (0/45 surahs). The long
   Meccan narrative and Madinan legislative blocks do NOT use
   waw-qasam as an opening gear. This is a **hard empirical bound**
   on the classical claim: the waw-oath is a Meccan-only, genre-
   specific opening device.

5. **Task-stated list more significant than [[h-new-85-oath-openers|H-NEW-85]] locked list**
   (p = 0.0005 vs p = 0.0073) — but this is an artifact of over-
   weighting the short-Mufaṣṣal block. The correctly-specified
   [[h-new-85-oath-openers|H-NEW-85]] list gives the conservative, generalizable result. The
   sensitivity confirms cluster cohesion is robust to list-definition
   changes within the reasonable range.

## Limitations

- Cell V's wa-prefix scan is lexical, not morphological; it can
  produce extras (*waylun* false-positives). The task's list itself
  includes 7 non-waw-qasam openers by this metric. We adopt the
  [[h-new-85-oath-openers|H-NEW-85]] QAC-morphological list as authoritative.
- k-means k=5 is not a pre-existing H-NEW-191 finding; H-NEW-191
  does not exist in this project yet. The k=5 choice was pre-
  registered based on the task prompt; it operationalizes "5 modes"
  as k-means with k=5 on the same root-probability space.
- The Fisher-Rao cohesion test is one-sided (oath-cluster tighter,
  not looser). This is the theoretically motivated direction given
  [[h-new-85-oath-openers|H-NEW-85]]'s discovery that oath-openers share sworn-by categories.
- Cross-reference to [[h-new-111-fisher-rao-mushaf|H-NEW-111]] Fisher-Rao-mushaf: oath-openers are
  NOT clustered in mushaf position (scattered Q 36 → Q 103). They
  are clustered in compositional space but distributed across the
  mushaf — which is itself a finding: the mushaf DOES NOT put the
  oath-openers adjacent, even though they are compositionally
  similar. M1 chose a different placement principle.

## Cross-reference

- **[[h-new-85-oath-openers|H-NEW-85]]** (4/5 PASS) — locked the 21 oath list, confirmed Q 91
  triple-maximum. Refined here: Cells 4+5 NULLs on length/theme are
  consistent with oath-openers being distinct on **vocabulary**, not
  on surface features.
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]** ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) — same Fisher-Rao parameterization;
  mushaf is geodesic-optimal overall, but oath-openers are NOT
  adjacently placed — mushaf uses a different rule.
- **[[h-new-192-mushaf-position-decomposition|H-NEW-192]]** — mushaf position is 80% compositional + 20% liturgical;
  the 20% residual includes the choice to NOT cluster oath-openers.
- **[[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]** — classical scholarship validation pattern;
  classical "21 oath surahs" anchor confirmed mechanically AND shown
  to be a cluster, not just a list.
- **Farahi *Niẓām al-Qurʾān*** — argumentative-oath thesis further
  supported: not only do sworn-by categories correlate with
  sworn-about themes ([[h-new-85-oath-openers|H-NEW-85]]), but the **oath-openers cohere as a
  compositional family** — there is a "register" of waw-qasam, not
  21 isolated uses.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-196-oath-cluster-prereg.md`
  (SHA-256: 17667fbbcb5ed1a696bfdc58f05b6a28e33e13373625f71db45cde9421db296d)
- Script: `scripts/h_new_196_oath_cluster.py`
- JSON results: `findings/phase-b-hypotheses/data/h-new-196.json`
