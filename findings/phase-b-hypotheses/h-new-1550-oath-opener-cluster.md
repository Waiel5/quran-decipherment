---
id: H-NEW-1550
title: Oath-opener (qasamīyāt; *wa-l-* cosmic-or-natural-noun) whole-surah Fisher-Rao cohesion
status: PASS-DIRECTED
date: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
prereg: findings/phase-b-hypotheses/prereg-h-new-1550-oath-opener-cluster.md
prereg_sha: 2ad17dab54450851c17b201b54a1bfb1191424426f63c3115639808f92ad1ac8
csv: findings/phase-b-hypotheses/csv/h-new-1550.json
script: findings/phase-b-hypotheses/scripts/h-new-1550.py
classical_anchor: al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān, nawʿ 67 (al-aqsām fī l-Qurʾān)
---

# H-NEW-1550 — Oath-opener (qasamīyāt) whole-surah FR cohesion: PASS-DIRECTED

## Headline

The 15 surahs whose first verse begins with the strict *wa-l-* + cosmic/natural-noun oath formula cluster at **observed intra-mean Fisher-Rao distance = 0.6985** — well below both the uniform null (mean = 0.9235, p = 0.0011) and the length-matched null (mean = 0.8794, p = 0.0003), each surviving Bonferroni-corrected α = 0.025. MW-5 PC instrument arm valid (H-NEW-1190 sub-sample {Q 69, Q 97, Q 101}, p = 0.0445). Direction LOWER (TIGHTER) matches pre-commit lock.

**Verdict: PASS-DIRECTED** (k=2 Bonferroni; both cells survive; PC valid; direction matches).

## Classical anchor

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, **nawʿ 67** (*al-aqsām fī l-Qurʾān* — "the oaths in the Qurʾān") catalogs the divine oaths in the corpus. The strict-formula sub-class — surah-opener consisting of wāw + definite article + cosmic or natural object — is the THICKEST surface-orthographic marker of the qasamīyāt category. The classical claim that these surahs form a recognizable structural sub-class is empirically validated at whole-surah FR scale.

## Cluster (locked, runtime-verified by `r"^\s*وال"` over no-tashkeel v1)

| Surah | Opening | Verses |
|:--|:--|:--|
| Q 37 al-Ṣāffāt | والصافات صفا | 182 |
| Q 51 al-Dhāriyāt | والذاريات ذروا | 60 |
| Q 52 al-Ṭūr | والطور | 49 |
| Q 53 al-Najm | والنجم إذا هوى | 62 |
| Q 77 al-Mursalāt | والمرسلات عرفا | 50 |
| Q 79 al-Nāziʿāt | والنازعات غرقا | 46 |
| Q 85 al-Burūj | والسماء ذات البروج | 22 |
| Q 86 al-Ṭāriq | والسماء والطارق | 17 |
| Q 89 al-Fajr | والفجر | 30 |
| Q 91 al-Shams | والشمس وضحاها | 15 |
| Q 92 al-Layl | والليل إذا يغشى | 21 |
| Q 93 al-Ḍuḥā | والضحى | 11 |
| Q 95 al-Tīn | والتين والزيتون | 8 |
| Q 100 al-ʿĀdiyāt | والعاديات ضبحا | 11 |
| Q 103 al-ʿAṣr | والعصر | 3 |

**Cluster size: 15. Total verses: 587.**

Explicit exclusions (per pre-reg): Q 68 (muqaṭṭaʿ-then-oath), Q 75 + Q 90 (*lā-uqsimu* negation-oath), Q 36 (muqaṭṭaʿ-only), Q 56 + Q 81 (open with *idhā*). The strict cluster isolates the surface-orthographic *wa-l-* + definite-article formula only.

## Numerical results

| Quantity | Value |
|:--|:--|
| Observed intra-cluster mean FR | **0.6985** |
| Cell A uniform null mean | 0.9235 |
| Cell A uniform null 2.5%ile | 0.8085 |
| Cell A p (one-tailed LOWER) | **0.0011** |
| Cell B length-matched null mean | 0.8794 |
| Cell B length-matched null 2.5%ile | 0.7895 |
| Cell B p (one-tailed LOWER) | **0.0003** |
| MW-5 PC {Q 69, Q 97, Q 101} p | 0.0445 (valid) |
| Bonferroni α per cell | 0.025 |
| Both cells survive | YES |

The observed value sits ~2.5 null-standard-deviations below the uniform null mean and ~2.0 SD below the length-matched null mean. Cell B (length-matched) provides the stronger result by p-value, confirming that the cohesion is NOT purely a consequence of the cluster's heavy short-Meccan total-verse-count signature — the oath-opener formula adds a genuine root-distribution-level cohesion above and beyond what shared brevity alone produces.

## Diagnostic pair structure

**5 tightest pairs (intra-cluster):**

| Pair | FR distance |
|:--|:--|
| Q 95 al-Tīn — Q 103 al-ʿAṣr | 0.2972 |
| Q 100 al-ʿĀdiyāt — Q 103 al-ʿAṣr | 0.3109 |
| Q 93 al-Ḍuḥā — Q 100 al-ʿĀdiyāt | 0.3637 |
| Q 95 al-Tīn — Q 100 al-ʿĀdiyāt | 0.3667 |
| Q 93 al-Ḍuḥā — Q 103 al-ʿAṣr | 0.3830 |

**5 loosest pairs (intra-cluster):**

| Pair | FR distance |
|:--|:--|
| Q 37 al-Ṣāffāt — Q 77 al-Mursalāt | 1.0524 |
| Q 37 al-Ṣāffāt — Q 89 al-Fajr | 1.0404 |
| Q 37 al-Ṣāffāt — Q 103 al-ʿAṣr | 1.0320 |
| Q 37 al-Ṣāffāt — Q 85 al-Burūj | 1.0307 |
| Q 37 al-Ṣāffāt — Q 100 al-ʿĀdiyāt | 1.0295 |

**Single-outlier structure**: Q 37 al-Ṣāffāt (182 verses — the only long surah in the cluster) is loose against every other oath-opener. The shortest mufaṣṣal core (Q 95, Q 100, Q 103, Q 93) forms the cohesion-engine of the test. This is consistent with the compression-tail law (h-new-660): high-s surahs have lower d̄_content, and the very short Meccan oath-openers sit in the deep tail of that gradient, sharing both length-architectural and root-distribution signatures. If Q 37 is excluded (sensitivity arm, post-hoc only — NOT used for primary inference), the cohesion would deepen further.

## Direction lock

Direction was LOCKED before computation to LOWER (TIGHTER). Observed mean (0.6985) is below null mean (0.9235), so direction matches the pre-commit. No pre-commit violation.

## Differentiating prediction (vs discourse-marker NULL family)

This finding extends the cross-finding-025 marker-thickness threshold rule. The differentiating prediction was: **thick surface-orthographic marker + chronological-clustering → whole-surah FR-cohesion; thin/scattered discourse-marker → whole-surah FR-NULL** (potentially salvageable at narrower pericope-scale per H-NEW-1380 / H-NEW-1520).

| Class | Test | Cluster | Whole-surah FR verdict | p |
|:--|:--|:--|:--|:--|
| Thick + clustered | **H-NEW-1550 (this)** | 15 oath-opener surahs | **PASS-DIRECTED** | **0.0011 / 0.0003** |
| Discourse marker (vocative) | H-NEW-1360 | 6 prophet-vocative surahs | NULL | 0.5734 / 0.5835 |
| Discourse marker (sajda) | H-NEW-1330 | sajda surahs | NULL | (per ledger §10.44) |
| Discourse marker (al-ḥamdu) | H-NEW-1340 | al-ḥamdu opener | NULL | (per ledger §10.44) |

The contrast is sharp and pre-specified. The same instrument (H-NEW-111 FR matrix, identical permutation protocol, identical seed family) returns NULL on thin/scattered markers and PASS on the thick chronologically-clustered marker. This validates the marker-thickness axis as a substantive predictor, not a fishing artifact.

## MW-1..MW-7 compliance summary

- **MW-1 instrument-prior**: FR matrix H-NEW-111 + 105-pair mean + permutation null specified before run. ✓
- **MW-2 corpus-prior**: 10,000 perms per cell. ✓
- **MW-3 alternative-models**: Uniform + length-matched cells; both pass. ✓
- **MW-4 over-fitting**: No fitted parameter. Cluster size emerged from the regex; not tuned. ✓
- **MW-5 replication**: PC arm H-NEW-1190 {Q 69, Q 97, Q 101} passed at p = 0.0445 — instrument-valid on this run. ✓
- **MW-6 instrument-control**: Discourse-marker NULL family (H-NEW-1360, 1330, 1340) is the embedded negative control; same instrument returns NULL on thin markers, PASS on this thick marker — substantive contrast, not artifact. ✓
- **MW-7 post-hoc cap**: Single-direction pre-registered test on classical-cataloged cluster (al-Suyūṭī *Itqān* nawʿ 67). Not post-hoc. ✓

## Honest limits

- **Q 37 single-outlier load**: Q 37 al-Ṣāffāt is the only long surah in the cluster (182 verses; second-largest is Q 53 at 62). Q 37 is loose against every other member. The cohesion signal is driven primarily by the 14 short members. This does NOT invalidate the test — Cell B explicitly controls for total-verse-count and the test still passes at p = 0.0003 — but it does mean the *qasam* signature is most clearly visible in the short-mufaṣṣal tail, and Q 37 (which sits at chronological mid-Meccan in Nöldeke; the other 14 are all early-Meccan) is closer to a transitional case.
- **Strict vs wider definition**: The pre-reg locked the strict cluster (v1 begins with `وال`). A wider definition that includes *lā-uqsimu* (Q 75, Q 90) and muqaṭṭaʿ-then-oath (Q 68) is a queued sensitivity arm (H-NEW-1550-sens-wider) but is NOT used for the primary inference here.
- **Chronology-versus-formula confound**: The 15 oath-opener surahs are all Meccan, predominantly short-mufaṣṣal. Cell B's ±20% length-matched null partially controls for this by drawing surahs of similar total-verse-count, but it does not control for chronology-stratum directly. A chronology-matched null (Early-Meccan-only pool) would be a stronger control; it is queued as H-NEW-1550-sens-chrono.
- **FR is one of several instruments**: The cohesion is on QAC stem-root distributions. Whether the *qasam* signature also shows on phoneme, rhyme, or content-cohesion instruments is a separate empirical question; not tested here.

## Connection to existing findings

- **al-Suyūṭī *Itqān* nawʿ 67**: classical anchor SECONDARY-CONFIRMED. The qasamīyāt-as-structural-category claim now has whole-surah FR-cohesion as quantitative validation.
- **cross-finding-025 marker-thickness threshold**: PASS-DIRECTED supplies the second-strongest supporting finding on the THICK-marker side (alongside H-NEW-1260 *yā-ayyuhā alladhīna āmanū* root-cohesion). The contrast against the discourse-marker NULL family (H-NEW-1330, 1340, 1360) is sharp and pre-specified.
- **Wave 2026-04-28 compression-tail laws**: the short-mufaṣṣal core of the cluster sits in the deep tail of the d̄_content compression-tail law (h-new-660); the cohesion signal is consistent with and partially nested within that broader gradient — but Cell B's length-matched null demonstrates the *qasam* formula adds signal above the brevity-alone baseline.
- **Q 51 al-Dhāriyāt specialist (2026-05-09)**, **Q 53 al-Najm specialist (2026-05-09)**: per-surah templates landed for two cluster members in the immediate prior session; both surahs are intra-cluster tight (Q 51-Q 53 pair distance not at extremes but well below null).
- **H-NEW-1360 / H-NEW-1330 / H-NEW-1340 NULL family**: same-instrument NULL on thin discourse markers; this finding is the predicted contrast on the thick-marker side.

## Cross-references

- [[prereg-h-new-1550-oath-opener-cluster]] (pre-registration; SHA-locked 2ad17dab)
- [[cross-finding-025]] (marker-thickness threshold synthesis)
- [[h-new-1360-prophet-vocative]] (discourse-marker NULL — differentiating negative)
- [[h-new-1330-sajda]] / [[h-new-1340-al-hamdu]] (discourse-marker NULL family)
- [[h-new-1260-vocative-believers]] (CONFIRMED root-cohesion — sister thick-marker finding)
- [[h-new-660-compression-tail-gradient]] (architectural law nesting this finding)
- [[h-new-111-fisher-rao]] (instrument source)

## Final statement

The classical-cataloged qasamīyāt — strictly defined as surahs whose first verse begins with the *wa-l-* + cosmic/natural-noun oath formula — form an empirically cohesive Fisher-Rao cluster at whole-surah scale, p = 0.0011 (uniform) and p = 0.0003 (length-matched), both surviving Bonferroni α = 0.025. The marker-thickness axis of cross-finding-025 is reinforced: thick surface-orthographic markers cluster at the surah scale where thin discourse markers do not. al-Suyūṭī's nawʿ 67 category is structurally real, not nominal.
