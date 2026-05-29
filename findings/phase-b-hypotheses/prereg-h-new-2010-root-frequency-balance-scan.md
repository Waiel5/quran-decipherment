---
id: H-NEW-2010
title: Exhaustive root-frequency exact-equality balance scan — candidate-pattern generator + permutation null on semantic over-representation
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-2010 (single pre-registered over-representation test; the ranked-list deliverable is descriptive, not a hypothesis test)
alpha: 0.05
direction_of_effect:
  T1: The number of exact-equal-count UNORDERED ROOT PAIRS that fall WITHIN a pre-registered semantic group (antonym / synonym / co-thematic) EXCEEDS the chance baseline obtained by shuffling the (root → semantic-group) labels across the fixed frequency distribution. Direction LOCKED HIGH (more meaningful balances than chance).
origin: >
  The Quran word-count-miracle literature (Nawfal 1983 *al-Iʿjāz al-ʿadadī li-l-Qurʾān al-karīm*; Taslaman 2006; al-Kaheel kaheel7.com) cites ~15 hand-picked "balanced-word" pairs — al-dunyā/al-ākhira (claimed 115/115), al-malāʾika/al-shayāṭīn (88/88), al-ḥayāt/al-mawt (claimed 145/145), etc. The project's earlier exploratory file `findings/phase-b-hypotheses/word-pair-symmetry.md` (2026-04-12, agent word-pair-hunter-run-1, NO pre-registration) replicated these mechanically at the QAC lemma/root level (2 verify cleanly, 6 fail outright) and enumerated novel same-count pairs, but its "null model" (§5) was an EYEBALLED estimate ("roughly 15-20%... higher than ~5%") — never a real permutation test. It concluded informally that "finding 20-50 semantically-coherent equal-count pairs is expected by chance" without running the shuffle. H-NEW-2010 closes that gap: an EXHAUSTIVE, mechanical scan of the full 1,642-root corpus frequency distribution + a rigorous 10,000-permutation label-shuffle null testing whether semantically-meaningful exact balances are OVER-represented relative to chance. This is a candidate-pattern GENERATOR (it surfaces every exact balance), not a test of one prior pair.
verdict_ceiling: PASS-DIRECTED (single pre-registered test; the ranked top-30 list is a descriptive generator output, NOT a hypothesis test; INDEPENDENT REPLICATION with a second seed + a second semantic-gazetteer variant required for CONFIRMED promotion).
rules_tuple:
  orthography: no-tashkeel
  token_definition: QAC root (Buckwalter-keyed; the morphological root, not lemma or orthographic-token)
  counting_unit: total corpus attestations of the root (= len of the root's attestation list in root-index.json = total_occurrences in root-stats.csv; the two agree EXACTLY for all 1,642 roots, verified at lock time)
  basmala_policy: as-encoded-in-QAC (basmala of Q 1:1 contributes; the other 112 basmalas are NOT separate QAC verses — standard QAC convention)
  verse_numbering: hafs-kufan
  reading_tradition: Hafs ʿan ʿĀṣim (Kūfan)
  script: Mashriqi (irrelevant at root level)
  source_files:
    - /Users/grey/Downloads/quran/data/morphology/root-index.json (1,642 roots → attestation lists; count = list length)
    - /Users/grey/Downloads/quran/data/morphology/root-stats.csv (cross-validation of total_occurrences; ZERO mismatches at lock time)
---

# H-NEW-2010 pre-registration — exhaustive root-frequency exact-equality balance scan

## What this is

A **candidate-pattern generator**, not a prior-test. The famous balanced-word claims (dunyā=ākhira, etc.) are a tiny hand-picked subset. This scan finds ALL exact-frequency balances in the corpus mechanically, ranks them by semantic surprisingness, and then asks the one rigorous question the prior exploratory file never answered with a real null:

> **Do semantically-meaningful exact-balance root-pairs occur MORE often than chance, given the corpus's (heavy-tailed) root-frequency distribution?**

## The mechanical scan (deterministic — no hypothesis test)

```
1. Load root-index.json. For each of the 1,642 roots, count = len(attestation list).
2. Cross-validate every count against root-stats.csv total_occurrences (fail-fast on any mismatch).
3. Build the inverted map  freq_value -> [roots with that exact count].
4. For each freq_value whose bucket has >= 2 roots, every unordered pair of roots in that bucket
   is an EXACT-BALANCE PAIR. Enumerate all of them.
5. This is exhaustive and deterministic. Save the full inverted map + all buckets to JSON.
```

This step is pure enumeration. It is the GENERATOR. No statistics, no cherry-picking.

## The ranked deliverable (descriptive)

For every exact-balance pair, attach Buckwalter, Arabic, and an English gloss (QAC glosses / standard lexicon: Lane, Hans Wehr, the QAC dictionary). Score each pair for **semantic surprisingness** with a pre-committed priority order (locked here, BEFORE seeing which roots share counts):

- **Tier A (highest surprise)** — antonym / polar-opposite pair (e.g. life/death, guidance/misguidance, this-world/hereafter, belief/disbelief, heaven/earth, day/night, reward/punishment, near/far, first/last, good/evil). The Tier-A antonym list is the union of the 27 paired-opposite families already locked in `findings/phase-b-hypotheses/paired-opposites.csv` (so the antonym membership is NOT chosen after seeing counts — it is inherited from a pre-existing, independently-built file).
- **Tier B** — synonym / near-synonym or morphological-semantic complement (e.g. two roots both meaning "to know", "command/matter", "path/way").
- **Tier C** — co-thematic / collocational (roots that habitually co-occur theologically: e.g. "remember"/"night", "garden"/"god", "command"/"Hell").
- **Tier D (no surprise)** — semantically unrelated. The default.

The top-30 ranked list = highest-tier, then (within tier) rarest-bucket (smaller bucket = less coincidence-prone), then highest-count (high-frequency coincidences are rarer in a heavy tail).

## The ONE pre-registered hypothesis test (T1)

**Test statistic** `M_obs` = number of exact-balance unordered root-pairs that fall within the SAME pre-registered semantic group, where the semantic groups are the 27 paired-opposite families of `paired-opposites.csv` (Tier-A antonyms) PLUS a fixed Tier-BC gazetteer of co-thematic/synonym groups locked below. Each root is assigned to AT MOST one semantic group (a fixed, pre-committed assignment; roots in no group are "unlabelled").

**Why this is not circular**: the semantic-group MEMBERSHIP (which roots are "life", which are "death", which are "guidance", etc.) is fixed BEFORE the frequency counts are consulted. We then ask how many same-count pairs happen to land inside a group. The frequency counts are never used to define the groups.

**Null model (label-shuffle permutation, 10,000 perms, seed 20260509)**:
```
The set of root-frequencies is FIXED (the heavy-tailed distribution is held constant).
The set of semantic-group labels is FIXED (same multiset of labels).
NULL: randomly REASSIGN the semantic-group labels to roots (permute which roots carry which
      group-membership), preserving the number of roots per group, then recount how many
      same-count pairs fall within a group.
Repeat 10,000 times -> null distribution of M_null.
p = (#{M_null >= M_obs} + 1) / (10000 + 1).   [one-tailed, direction LOCKED HIGH]
```
This shuffle holds the corpus frequency distribution and the group-size structure constant, and asks ONLY whether the OBSERVED root→meaning assignment puts more semantically-related roots at equal counts than a random meaning-assignment would. This is exactly the "shuffle root-meanings randomly across the frequency distribution" null specified in the task brief.

### Pre-committed semantic gazetteer (LOCKED — Buckwalter roots)

Tier-A antonym families (inherited verbatim from `paired-opposites.csv`, both sides are group-members of their family):
```
heaven/earth:        smw | ArD
life/death:          Hyy | mwt
dunya/akhira:        dnw | Axr
sun/moon:            $ms | qmr
guidance/misguidance:hdy | Dll
day/night:           ywm,nhr | lyl
secret/open:         srr | Eln
east/west:           $rq | grb
faith/disbelief:     Amn | kfr
male/female:         *kr | Anv
good/evil:           Hsn | swA
truth/falsehood:     Hqq | bTl
ease/difficulty:     ysr | Esr
light/darkness:      nwr | Zlm
wealthy/poor:        gny | fqr
seen/unseen:         $hd | gyb
remember/forget:     *kr | nsy
first/last:          Awl | Axr
heaven/hell:         jnn | nar(=nwr? NO -> use root 'nwr' is light; hell-root is 'nar' but QAC root for fire is n-w-r? see note) 
give/withhold:       Aty | mnE,bxl
near/far:            qrb | bEd
pure/impure:         Thr | njs,rjs
obedience/disobed:   TwE | ESy
grateful/ungrateful: $kr | kfr
mercy/wrath:         rHm | gDb
reward/punishment:   Ajr | E*b
speak/silent:        qwl | Smt,nSt
```
NOTE on hell: the Quranic "fire/hell" is the root n-w-r in some indices but jhnm/nar; `paired-opposites.csv` used `nar_lemma` (a lemma, not a root) for heaven/hell. Because H-NEW-2010 operates strictly at the ROOT level, the heaven/hell family is mapped to roots `jnn` (garden/paradise) | `Hrq`/`nwr`-ambiguous; to avoid a lemma/root-level confound this family is INCLUDED only via its unambiguous root side `jnn` paired against the hell-root `jhnm` if present in root-index, else the family is DROPPED and logged. Same-count pairing only fires if BOTH sides are present as roots. This decision is locked here, before computation.

Tier-BC co-thematic / synonym groups (LOCKED — each group's members are mutually "meaningful" if they share a count):
```
know/sign:           Elm | Ayy        (knowledge & sign/verse — revelation pair)
path/deny:           sbl | k*b        (the path vs denying it)
command/matter:      Amr | wqy        (divine command & God-consciousness)
no-other-god:        gyr | Alh        (la ilaha ghayruhu)
garden/god:          jnn | Alh        (the two ultimate theological terms)
guide/besides:       hdy | dwn        (guidance vs "besides God")
prophet-follow:      Aty | tbE         (giving/sending & following)  [Aty already in give/withhold -> see overlap rule]
disbeliever/wrongdoer: kfr | Zlm       (the two rejected-community nouns) [kfr already in faith/disbelief & grateful/ungrateful]
remember/night:      *kr | lyl         (remember God in the night)
religion/word:       dyn | qwl         (religion & the Word) [qwl already in speak/silent]
glorify/prostrate:   sbH | sjd         (the two worship verbs)
```

### Overlap rule (LOCKED)
A root may appear in multiple families (e.g. `*kr` is in remember/forget, male/female, remember/night; `kfr` is in faith/disbelief, grateful/ungrateful, disbeliever/wrongdoer). For T1, a same-count pair (rootX, rootY) counts as a "meaningful balance" if there EXISTS at least one pre-registered family containing BOTH rootX and rootY. Each unordered pair is counted AT MOST ONCE regardless of how many families it satisfies. The permutation null shuffles a root's FULL family-membership-set as a unit (a root carries its set of group-tags; the assignment of tag-sets to roots is permuted), preserving the multiset of tag-sets. This is locked to avoid double-counting and to keep the null structurally faithful.

## Pre-committed predictions (the bets)

- **Mechanical scan**: ~118,000 total exact-balance pairs exist (dominated by the count=1 bucket of ~395 roots and count=2 of ~197 roots). The overwhelming majority are low-count combinatorial coincidences. HONEST FRAMING locked: most exact-balances are coincidental.
- **T1 prediction**: `M_obs` will be SMALL in absolute terms (the pre-registered families cover only ~60 roots out of 1,642, so few same-count pairs can land inside a family). The BET is that `M_obs` nonetheless EXCEEDS the shuffled chance baseline (p < 0.05, direction HIGH). I expect this to be a WEAK effect at best — quite possibly NULL. Prior exploratory eyeballing suggested only a mild enrichment.
- **Most-surprising single pairs predicted at top**: malak/shayṭān-type (already lemma-level; at root level $Tn shares count 88 with qrA); and the famous antonym balances IF any land exactly. Given `paired-opposites.csv`, NONE of the 27 antonym families have exactly-equal raw root counts except possibly small ones — this scan will reveal which, if any, are EXACT at the root level.

## Decision rule

- **T1 PASS-DIRECTED** if `M_obs > median(M_null)` AND one-tailed p < 0.05 AND direction matches lock (HIGH).
- **T1 NULL** if p >= 0.05.
- **T1 PRE-COMMIT VIOLATION** if `M_obs < median(M_null)` (meaningful balances UNDER-represented) — published as NULL with explicit reversal flag per Protocol §1.8.
- The ranked top-30 list is published REGARDLESS of T1 outcome, clearly labelled as a descriptive generator output, NOT evidence of design.

## What would make this finding interesting vs not

- **Interesting (rare)**: T1 PASS with low p — the corpus puts antonym/synonym roots at equal counts more than chance. Even then, the effect is modest and the honest reading is "suggestive, not miraculous."
- **Expected (likely)**: T1 NULL — same-count balances are pigeonhole coincidences; semantically-meaningful ones are NOT over-represented. This would empirically retire the "balanced-word miracle" claim at the mechanical root level, which is itself a valuable, publishable NULL.

## MW protections

- **MW-1 (instrument-prior)**: metric (exact-count equality) + test statistic (M_obs) + null (label-shuffle) all specified here, before running.
- **MW-2 (corpus-prior)**: 10,000-perm permutation null.
- **MW-3 (alternative-models)**: report M_obs under (a) Tier-A-only (antonyms), (b) Tier-A+BC (full gazetteer) — two model variants.
- **MW-5 (replication)**: a second seed (20260530) reported as a replication check; flagged for an independent second-gazetteer replication before CONFIRMED.
- **MW-6 (instrument-control)**: also report the same M_obs/null using a DECOY gazetteer of the same size built from arbitrary (semantically-unrelated) root groupings — expect NO enrichment, confirming the instrument isn't trivially inflating.
- **MW-7 (post-hoc cap)**: any pair noticed only after seeing counts carries single-test α and is flagged descriptive.

## Honest limits

1. **Pigeonhole dominates.** With 1,642 roots and counts clustering on small integers, ~118,000 exact-balance pairs exist by construction. Exact equality is cheap. The famous pairs are a hand-picked ~15 out of an enormous pool.
2. **Semantic-group membership is a judgement call.** The gazetteer is locked here to prevent circularity, but a different (equally defensible) gazetteer could shift M_obs. This is why MW-3 (two variants) and a second-gazetteer replication are required for CONFIRMED.
3. **Root ≠ lemma ≠ semantic-sense.** The QAC root conflates senses (e.g. mlk = king/angel/possess). Root-level counts differ from the lemma-level counts used in the famous claims; many famous pairs (which rely on lemma- or custom-filtered counts) will NOT be exact at the root level. This is expected and honest.
4. **No causal claim.** Even a PASS cannot distinguish authorial design from a happy property of Arabic theological vocabulary frequency. Frequency alone is mute on intention.
5. **Direction is the only thing being tested.** The ranked list is a generator, not evidence; only T1 is a hypothesis test.

## Cross-references

- `findings/phase-b-hypotheses/word-pair-symmetry.md` — prior EXPLORATORY scan (no pre-reg; eyeballed null). H-NEW-2010 supersedes its §5 with a real permutation test.
- `findings/phase-b-hypotheses/paired-opposites.csv` — the 27 locked antonym families (source of Tier-A membership).
- `findings/phase-b-hypotheses/paired-opposites-network.md` — opposite-pair co-occurrence network.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 (al-muqaddam wa-l-muʾakhkhar) — classical attention to lexical pairing/balance, NOT numerical-count balance (the count-miracle is a 20th-c. claim).
- Nawfal 1983, *al-Iʿjāz al-ʿadadī li-l-Qurʾān al-karīm* — primary numerical-balance source (FALSIFIABLE TARGET).
- H-NEW-1810 (letter-frequency), H-NEW-1560/1800 (divine-names) — sibling enumeration generators.

## Seed and reproducibility

- Seed: `20260509` (primary null); `20260530` (replication null).
- All numerical outputs to `findings/phase-b-hypotheses/csv/h-new-2010.json`.
- Run script: `findings/phase-b-hypotheses/scripts/h-new-2010.py`.
- Pre-reg SHA256: locked at first commit; embedded in run script; verified at runtime (fail-fast on mismatch).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
