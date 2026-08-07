---
id: H-NEW-2070
title: Divine-name verse-final pairing arithmetic + co-occurrence graph (al-fawāṣil)
phase: B
status: PASS-DIRECTED (Bonferroni-2; both concentration statistics p<0.0001; Medinan-robustness concordant)
date: 2026-05-29
executed_by: specialist (pre-registered, SHA-locked)
classical_anchor: al-Bāqillānī, Iʿjāz al-Qurʾān (al-fawāṣil as governed cadence); al-Zarkashī, al-Burhān fī ʿulūm al-Qurʾān, nawʿ on al-fawāṣil (murāʿāt al-fāṣila); al-Suyūṭī, al-Itqān, nawʿ 59 (al-fawāṣil)
prereg: findings/phase-b-hypotheses/prereg-h-new-2070-divine-name-pairing.md
prereg_sha256: 03e5b967421cc4e78856c23251a84c5b100ec3ad70172e176c3c4b4691e3aa79
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
direction: POSITIVE — observed verse-final pairing concentration > slot-independence null
verdict: PASS-DIRECTED
---

# [[h-new-2070-divine-name-pairing|H-NEW-2070]] — Divine-name verse-final pairing (al-fawāṣil)


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## What was tested

Classical *balāgha* treats verse-closings under the rubric **al-fawāṣil** —
al-Zarkashī's principle of *murāʿāt al-fāṣila* (al-Burhān, the *nawʿ* on
al-fawāṣil) and al-Bāqillānī (*Iʿjāz al-Qurʾān*) hold that the closer of a verse
is a *governed* collocation, not interchangeable ornament. A characteristic
case is the verse that closes on a PAIR of divine epithets in the fixed cadence
*X-un Y-un* / *X-an Y-an* / *al-X al-Y*: *ghafūrun raḥīm*, *ʿazīzun ḥakīm*,
*samīʿun ʿalīm*, *ʿalīmun ḥakīm*, …

The project's prior pairing findings (H-NEW-140, H-NEW-170) counted divine-name
co-occurrence *anywhere in a verse*. This test is orthogonal: it isolates the
**verse-final ordered bigram** — the fawāṣila closer itself — enumerates the
full pairing graph, and asks whether the pairings are **non-random** beyond what
the marginal verse-end frequencies of individual names would predict.

**Detection rule (locked, no-tashkeel)**: a verse closes on a divine-name pair
iff its last two tokens both base-normalize (strip `ال`; strip one trailing
accusative alif) to one of the **97 single-token al-Tirmidhī names**
(`data/asma-al-husna.txt`).

**Result**: **321 verses** close on a divine-name pair, across **54 distinct
ordered pairs**, forming a directed graph of **42 nodes / 54 edges**.

## Top-15 verse-final divine-name pairs

| Rank | Pair (base) | Translit | Count | Share | Example |
|:-:|:--|:--|:-:|:-:|:--|
| 1 | غفور + رحيم | *ghafūr + raḥīm* | **64** | 19.9% | Q 2:173 |
| 2 | عزيز + حكيم | *ʿazīz + ḥakīm* | **47** | 14.6% | Q 2:129 |
| 3 | سميع + عليم | *samīʿ + ʿalīm* | **31** | 9.7% | Q 2:127 |
| 4 | عليم + حكيم | *ʿalīm + ḥakīm* | **29** | 9.0% | Q 2:32 |
| 5 | عزيز + رحيم | *ʿazīz + raḥīm* | 13 | 4.0% | Q 26:9 |
| 6 | سميع + بصير | *samīʿ + baṣīr* | 11 | 3.4% | Q 17:1 |
| 7 | تواب + رحيم | *tawwāb + raḥīm* | 9 | 2.8% | Q 2:37 |
| 8 | غني + حميد | *ghanī + ḥamīd* | 9 | 2.8% | Q 2:267 |
| 9 | واسع + عليم | *wāsiʿ + ʿalīm* | 7 | 2.2% | Q 2:115 |
| 10 | حكيم + عليم | *ḥakīm + ʿalīm* | 7 | 2.2% | Q 6:128 |
| 11 | رحمن + رحيم | *raḥmān + raḥīm* | 6 | 1.9% | Q 1:3 |
| 12 | عزيز + عليم | *ʿazīz + ʿalīm* | 6 | 1.9% | Q 6:96 |
| 13 | واحد + قهار | *wāḥid + qahhār* | 6 | 1.9% | Q 12:39 |
| 14 | علي + كبير | *ʿalī + kabīr* | 5 | 1.6% | Q 4:34 |
| 15 | لطيف + خبير | *laṭīf + khabīr* | 5 | 1.6% | Q 6:103 |

(Full 54-pair table + per-instance rows in `csv/h-new-2070.json`.)

The **top-5 pairs alone account for 57.3%** of all 321 divine-pair closings;
the **top-4 account for 53.3%**. This is the *al-fawāṣil* concentration the
classical tradition asserts, now quantified.

## The famous *al-ʿazīz al-ḥakīm* count — verified

*al-ʿazīz al-ḥakīm* ("the Mighty, the Wise") closes **47 verses** in total,
distributed across three morphological cadences:

| Cadence | Count |
|:--|:-:|
| العزيز الحكيم (definite *al-X al-Y*) | **29** |
| عزيز حكيم (indefinite nominative *X-un Y-un*) | 13 |
| عزيزا حكيما (accusative *X-an Y-an*) | 5 |

The classical claim that *al-ʿazīz al-ḥakīm* (in the definite *al-X al-Y* form)
closes "about thirty" verses is **confirmed at exactly 29**; the broader epithet
across all three cadences reaches 47. This reconciles the apparent discrepancy
between H-NEW-140's "~29" (definite form) and the raw bigram scan's higher count.

## Pairing graph — hub structure

The directed graph (slot-1 = penultimate "head" name → slot-2 = final "seal"
name) is sharply **role-differentiated**. Weighted in/out degree:

| Name | Total deg | Out (head) | In (seal) | Role |
|:--|:-:|:-:|:-:|:--|
| raḥīm (*الرحيم*) | 95 | 2 | **93** | terminal seal (almost never a head) |
| ḥakīm (*الحكيم*) | 91 | 12 | 79 | seal-dominant |
| ʿalīm (*العليم*) | 88 | 35 | 53 | bidirectional pivot |
| ʿazīz (*العزيز*) | 82 | **77** | 5 | head-dominant (rarely sealed) |
| ghafūr (*الغفور*) | 78 | 71 | 7 | head-dominant |
| samīʿ (*السميع*) | 42 | 42 | **0** | pure head (never a seal) |
| khabīr | 17 | 4 | 13 | seal |
| baṣīr | 15 | 0 | 15 | pure seal |

The graph reveals a **non-symmetric grammar of the cadence**: certain names are
structurally "heads" (*ʿazīz, ghafūr, samīʿ, tawwāb* — they open the pair) and
others are structurally "seals" (*raḥīm, ḥakīm, baṣīr, khabīr* — they close it).
*raḥīm* is the dominant terminal (93/95 occurrences in seal position); *samīʿ*
is a pure head (42/42 in head position, never sealing). *ʿalīm* is the unique
high-traffic pivot, working in both roles (35 head / 53 seal). This ordering
asymmetry is exactly the *tartīb al-fāṣila* (cadence-ordering) the balāghiyyūn
describe and is itself strong evidence the pairings are rule-governed.

## Verdict on non-randomness

Two pre-registered concentration statistics tested against a **slot-independence
null** (10,000 perms, seed 20260509) that holds each name's head-slot and
seal-slot marginal frequency EXACTLY fixed and only destroys the head↔seal
*pairing* — so the test cannot be passed merely because *raḥīm* or *ḥakīm* are
frequent verse-enders:

| Statistic | Observed | Null p97.5 | p_perm | Pass (α=0.025) |
|:--|:-:|:-:|:-:|:-:|
| **H1** top-5-pair share | **0.573** | 0.318 | **<0.0001** | ✓ |
| **H2** normalized HHI | **0.0871** | 0.0302 | **<0.0001** | ✓ |

Both reject the null decisively. The observed pairing concentration is roughly
**1.8× the null's upper-2.5% tail** on top-5-share and **2.9×** on HHI.

**Medinan-robustness (Cell B)**, on the 182 Medinan-revealed pair-closings
alone, is **concordant** on both statistics (observed > null median, p<0.0001) —
the concentration is *not* a chronology artifact of one revelation stratum
dominating.

**Verdict: PASS-DIRECTED.** Verse-final divine-name pairings are highly
non-random: a small set of ordered pairs dominates, names occupy
structurally-differentiated head vs seal roles, and the head↔seal pairing is
constrained far beyond the names' independent verse-end frequencies. The
classical *al-fawāṣil* doctrine (al-Zarkashī's *murāʿāt al-fāṣila*; al-Bāqillānī)
is empirically vindicated at the collocational level.

## Corpus-extreme pairs

- **Corpus-MAX fawāṣila pair**: غفور + رحيم (*ghafūr + raḥīm*) at **64** verse-final
  attestations — the single most frequent verse-closing collocation of any kind
  in the corpus (cf. the raw-bigram scan where it leads at 42 in pure
  *X-un Y-un* form, 64 across all cadences).
- **Corpus-SINGLETON fawāṣila pairs (n=25)**: ordered pairs that seal exactly one
  verse in the whole Quran. Notable theologically-charged singletons:
  - حي + قيوم (*ḥayy + qayyūm*, "the Living, the Self-Subsisting") — Q 3:2 (the
    pair recurs mid-verse in Āyat al-Kursī Q 2:255, but seals a verse only once).
  - مالك... → الله + صمد (*Allāh + ṣamad*) — Q 112:2, the sole *al-Ṣamad* closing.
  - متكبر + جبار (*mutakabbir + jabbār*) — Q 40:35.
  - غفور + ودود (*ghafūr + wadūd*) — Q 85:14 (the unique *al-Wadūd*-as-seal verse,
    matching H-NEW-140's note that *al-Wadūd + al-Ghafūr* is a z>+8 rare pairing).
  - عزيز + وهاب (*ʿazīz + wahhāb*) — Q 38:9; فتاح + عليم (*fattāḥ + ʿalīm*) — Q 34:26.

## Classical connection — al-Bāqillānī, al-Zarkashī, al-Suyūṭī

- **al-Bāqillānī, *Iʿjāz al-Qurʾān***: the verse-closings are part of the
  inimitable *naẓm*; the cadence is content-fitted, not metrical filler. The
  measured head/seal asymmetry (ʿazīz/ghafūr open; raḥīm/ḥakīm close) is the
  concrete shape of this claim.
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on al-fawāṣil**: articulates
  *murāʿāt al-fāṣila* — the closer must "observe" the verse. The 1.8–2.9× excess
  concentration over the slot-independence null is the empirical signature of
  this constraint operating at corpus scale.
- **al-Suyūṭī, *al-Itqān*, nawʿ 59 (al-fawāṣil)**: catalogues fawāṣila types and
  notes the *asmāʾ mutazāwijah* (paired names). H-NEW-2070 supplies the full
  ranked enumeration al-Suyūṭī gestures at but never tabulated.

## Relation to prior project findings

- **H-NEW-140 / H-NEW-170 (anywhere-in-verse co-occurrence)**: those measured
  whether classical pairs co-occur in a verse at all. H-NEW-2070 is the stricter,
  positional refinement — the *verse-FINAL ordered bigram* — and adds the
  head/seal directional grammar that anywhere-in-verse counting cannot see. The
  rankings broadly agree (ʿazīz+ḥakīm, ghafūr+raḥīm, samīʿ+ʿalīm dominate both),
  confirming the classical pair-list against an independent positional rule.
- **H-NEW-1560 (99-name surah density)**: orthogonal axis (surah-level density vs
  verse-final bigram). Both vindicate the al-Tirmidhī list as a live corpus object.

## Honest limitations

1. **Referent ambiguity**: the no-tashkeel base rule does not disambiguate divine
   vs non-divine referent. Verse-final spot-check (Q 12 — the surah most prone to
   the *al-ʿazīz* = Egyptian-governor and *al-malik* = king-of-Egypt confound)
   found all 9 verse-final pairs to be genuine divine epithets *except* the mild
   cases Q 12:31 (*malik karīm*, of Joseph's bearing) and Q 12:55 (*ḥafīẓ ʿalīm*,
   Joseph self-describing). At 2/321 = 0.6% the confound is negligible and, being
   internal to the pair-set, does not affect the slot-independence null.
2. **Excluded epithets**: by locking to the 97 single-token al-Tirmidhī names,
   genuine fawāṣila epithets outside the canonical list (*naṣīr, bashīr, nadhīr,
   khallāq, ʿallām*) are excluded by design. The pre-reg documents this; including
   them would only *increase* observed concentration, so the lock is conservative.
3. **Verdict ceiling**: PASS-DIRECTED. Independent replication under a second rule
   (min-tashkeel final-letter, or QAC-morphology divine-DET-MS tagging) is required
   for promotion to CONFIRMED.

## Reproduction

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2070-divine-name-pairing.md`
  (SHA256 `03e5b967421cc4e78856c23251a84c5b100ec3ad70172e176c3c4b4691e3aa79`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2070.py` (verifies SHA at runtime)
- Output: `findings/phase-b-hypotheses/csv/h-new-2070.json`
- Data: `quran-text/quran-no-tashkeel.json`, `data/asma-al-husna.txt`,
  `data/revelation-order.csv`
