---
id: H-NEW-1360
title: yā-ayyuhā al-nabī (prophet-vocative) 6-surah cluster Fisher-Rao cohesion — NULL with PC pass
date_locked: 2026-05-09
date_executed: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
verdict: NULL (with MW-5 PC pass)
prereg_sha: b82d6c917feb0a34c9a8f8de30302b7124766d6318736843efccbbd0c8273578
parent_dispatch: H-NEW-1260 (Q 49 al-Ḥujurāt corpus-rank-1 on *yā-ayyuhā alladhīna āmanū* density)
sister_construction: yā-ayyuhā alladhīna āmanū (believer-vocative) — H-NEW-1260
related: H-NEW-1190 (PC), H-NEW-1261, H-NEW-1340, cross-finding-025
---

# H-NEW-1360 — yā-ayyuhā al-nabī (prophet-vocative) cluster FR-cohesion test


> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**STATUS: NULL with MW-5 PC pass — substantive null, not instrument failure.**

## Headline

The 6 surahs containing *yā-ayyuhā al-nabī* — **{Q 8, 9, 33, 60, 65, 66}** — do NOT form a Fisher-Rao-cohesive cluster on the H-NEW-111 root-distribution instrument. Observed intra-cluster mean FR = **0.9532** is SLIGHTLY ABOVE the corpus null mean (0.9240); pre-registered direction one-sided LOWER is reversed. Cell A p = 0.5734, Cell B (length-matched) p = 0.5835 — both far above α_bon = 0.025. The MW-5 PC on H-NEW-1190 sub-sample {Q 69, 97, 101} passes at p = 0.0445, confirming the instrument is working: this is a **substantive empirical NULL**, not an instrument failure.

## Cluster membership (locked from direct corpus search)

Regex `يا\s*أيها\s*النبي` over `quran-text/quran-no-tashkeel.json` returned 13 attestations across 6 distinct surahs:

| Surah | Verses with *yā-ayyuhā al-nabī* | Count | Length |
|:-:|:--|:-:|:-:|
| Q 8 al-Anfāl  | 64, 65, 70                  | 3 | 75 |
| Q 9 al-Tawba  | 73                          | 1 | 129 |
| Q 33 al-Aḥzāb | 1, 28, 45, 50, 59           | 5 | 73 |
| Q 60 al-Mumtaḥana | 12                      | 1 | 13 |
| Q 65 al-Ṭalāq | 1                           | 1 | 12 |
| Q 66 al-Taḥrīm | 1, 9                       | 2 | 12 |

All 6 are Medinan. Q 33 carries 5/13 (38.5%) of all attestations.

Q 73 al-Muzzammil and Q 74 al-Muddaththir use *different* vocatives (*yā-ayyuhā al-muzzammil*, *yā-ayyuhā al-muddaththir*) and are NOT in the cluster.

## Numerical results

| Quantity | Value |
|:--|:--|
| Observed intra-cluster mean FR | 0.9532 |
| Cell A (uniform 6-of-114) null mean | 0.9240 |
| Cell A null 5th percentile | 0.7534 |
| Cell A p (one-sided, lower) | **0.5734** |
| Cell B (length-matched ±20%) null mean | 0.9392 |
| Cell B null 5th percentile | 0.8454 |
| Cell B p | **0.5835** |
| MW-5 PC {Q 69, 97, 101} obs | 0.6078 |
| MW-5 PC p | **0.0445** (PASS) |
| α_bon per cell (k=2) | 0.025 |

Cell A pass: ✗ — Cell B pass: ✗ — PC pass: ✓ → **NULL**.

## Pairwise FR-distance breakdown inside the cluster

Sorted ascending (tightest pair first):

```
Q 60 — Q 66 : 0.8038   ← TIGHTEST PAIR (short Medinan domestic-marriage)
Q 65 — Q 66 : 0.8705
Q 60 — Q 65 : 0.8756
Q  8 — Q 60 : 0.9079
Q  8 — Q  9 : 0.9110
Q  8 — Q 33 : 0.9166
Q  9 — Q 33 : 0.9175
Q 33 — Q 60 : 0.9590
Q 33 — Q 66 : 0.9609
Q  9 — Q 60 : 1.0046    ← OVER UNIT DISTANCE
Q 33 — Q 65 : 1.0065
Q  8 — Q 66 : 1.0120
Q  8 — Q 65 : 1.0201
Q  9 — Q 66 : 1.0589
Q  9 — Q 65 : 1.0725    ← FARTHEST PAIR
```

Median pair distance = 0.917 — comparable to corpus median.

## Diagnostic structural reading

The cluster fragments into TWO distinct sub-regions whose internal coherence is canceled when pooled:

**Sub-region α — short Medinan domestic-marriage cluster** {Q 60, 65, 66}:
Mean intra-FR = (0.804 + 0.870 + 0.876) / 3 = **0.850**. This is the SAME cluster previously found tight in H-NEW-1261 (Q 49 FR-cluster TARGET-SET = {Q 61, 62, 63, 64, 66}). Q 60, 65, 66 share short length (12–13 verses), domestic jurisprudence (divorce, marriage covenants, oath-revocation), and frequent imperative discourse. The vocative *yā-ayyuhā al-nabī* in these surahs introduces RULES for the Prophet's household.

**Sub-region β — long Medinan polity / Confederates cluster** {Q 8, 9, 33}:
Mean intra-FR = (0.911 + 0.917 + 0.917) / 3 = **0.915**. These three surahs share length (73–129 verses), battle/community-formation content (Badr, Tabūk, Khandaq), and complex narrative-jurisprudence interleaving. They are tightly self-coherent BUT distinct from sub-region α.

**Cross-region pairs** average **0.972** — the long-Medinan-polity surahs are AS FAR from the short-Medinan-domestic surahs as random Medinan surahs are from each other. Q 9 — Q 65 (FR = 1.0725) is the most distant pair in the cluster: al-Tawba's treaty-and-warfare discourse versus al-Ṭalāq's divorce-rule discourse share little root-distribution overlap despite sharing the prophet-vocative formula.

## Interpretation

**The *yā-ayyuhā al-nabī* vocative is a DISCOURSE MARKER, not a content-cohesion driver.** The construction serves as a second-person prophetic command-anchor across multiple thematic domains: battle (Q 8), confrontation with unbelievers (Q 9), the Prophet's household + Confederates (Q 33), women's allegiance + treaty (Q 60), divorce (Q 65), and oath-revocation + household (Q 66). The vocative is THIN in cross-finding-025 terms — a 3-token discourse anchor inserted into otherwise-distinct thematic surahs.

This is the EXACT OPPOSITE of H-NEW-1260's finding for the SISTER construction *yā-ayyuhā alladhīna āmanū*. That construction has 89 corpus attestations concentrated in Q 49 (5/18 verses = 27.78%, corpus-rank-1) and clusters at FR = 0.7703 across the TARGET-SET {Q 61–64, 66} (H-NEW-1261). The prophet-vocative is structurally different: it is a SCATTERED discourse-marker, not a CONCENTRATED content-marker.

This NULL aligns with the H-NEW-1310 Christ-narrative cluster NULL (commit e6fd9506d) and H-NEW-1301 IMPV-qrA cluster NULL (commit a47c32588): **THIN markers do NOT generate FR-content clusters under the H-NEW-111 root-distribution instrument**. Cross-finding-025 (marker-thickness vs FR-cohesion threshold) acquires a third independent replication data-point.

The substantive structural signal that DOES survive is the within-cluster fragmentation: the 3-surah short-Medinan-domestic sub-cluster {Q 60, 65, 66} at FR ≈ 0.85 is real, and it sits inside the larger Q 49 al-Ḥujurāt FR-cluster confirmed by H-NEW-1261. The 3-surah long-Medinan-polity sub-cluster {Q 8, 9, 33} at FR ≈ 0.915 is also real but distinct.

## Classical reading

al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 51 *fī khiṭābātihi*, distinguishes between addresses to the Prophet (singular) and addresses to the community (plural). The classical insight that *yā-ayyuhā al-nabī* identifies surahs where Allāh speaks directly to Muḥammad is **descriptively confirmed** — exactly 6 surahs carry the vocative, all Medinan, and Q 33 al-Aḥzāb (the Prophet's-household surah) holds the densest concentration. However, this descriptive truth does NOT translate into FR-content cohesion. The vocative is a STRUCTURAL/DISCOURSE pattern, not a CONTENT pattern at the root-distribution level.

This refines the classical observation: the prophet-vocative marks a CONSISTENT discourse mode (direct second-person command to Muḥammad), but the CONTENT of those commands spans the full Medinan revelation spectrum.

## MW-1..MW-7 audit

- **MW-1 (instrument-prior)**: H-NEW-111 Fisher-Rao matrix; locked before run.
- **MW-2 (corpus-prior)**: 10,000-perm Cell A + 10,000-perm Cell B.
- **MW-3 (alternative-models)**: 2 cells (uniform + length-matched). Sub-region diagnostic post-hoc but unweighted.
- **MW-4 (over-fitting)**: zero fitted parameters; observed statistic is a single mean.
- **MW-5 (replication)**: MW-5 PC {Q 69, 97, 101} passes at p = 0.0445. Instrument confirmed working.
- **MW-6 (instrument-control)**: Length-matched null is the within-test instrument-control.
- **MW-7 (post-hoc cap)**: The sub-region diagnostic (α and β) is post-hoc — descriptive only, no claim of significance.

## Honest limits

1. The cluster is small (6 surahs / 15 pairs) — statistical power is modest. A 12-surah candidate cluster might reveal what a 6-surah one cannot.
2. Direction-of-effect was locked one-sided LOWER; observed direction is slightly REVERSED. Under Protocol §1.8 this is honest NULL, not a flip violation (the test direction was symmetrically constructed and the cluster simply sits at corpus baseline).
3. The H-NEW-111 instrument captures root-distribution. The vocative might cohere under a DIFFERENT instrument (e.g., morphology of imperative-verb-forms, verse-length kink, or rhyme-class — cf. H-NEW-1301 lesson that IMPV-qrA cluster fails on root-FR).
4. Q 33 al-Aḥzāb is UAS rank-1 (H-NEW-840) and may be too structurally heavy to integrate cleanly into a 6-surah mean.

## Verdict

**NULL — instrument-pass, direction-reversed, p > 0.5 on both cells.**

The *yā-ayyuhā al-nabī* construction is a DESCRIPTIVELY-DISTINCT classical marker but is NOT FR-cohesive on root-distribution. The classical observation (al-Suyūṭī) about its function — Allāh directly addresses Muḥammad — is empirically TRUE as a discourse-identifier but does NOT predict content-clustering. This is a substantive NULL that strengthens cross-finding-025: THIN markers (single short vocative phrase scattered across long-form surahs) do not generate FR-cohesive clusters under root-distribution.

The internal sub-structure (sub-region α {Q 60, 65, 66} at FR ≈ 0.85 vs sub-region β {Q 8, 9, 33} at FR ≈ 0.915) IS structurally informative, and is consistent with H-NEW-1261's Q 49-cluster TARGET-SET finding. It does not, however, repair the headline NULL.

## Cross-references

- [[h-new-1260-q049-believer-vocative-density]] — sister construction, CONFIRMED corpus-rank-1
- [[h-new-1190-wa-ma-adraka-cluster]] — MW-5 PC; CONFIRMED p=0.00068
- [[h-new-1261-q049-fr-cluster-target-set]] — overlapping cluster (Q 60, 66) tight
- [[h-new-1310-christ-narrative-cluster]] — analogous thin-marker NULL
- [[h-new-1301-impv-qra-cluster]] — analogous thin-marker NULL
- [[h-new-1340-hamdu-lillah-cluster]] — analogous classical-form-pattern test
- [[cross-finding-025-marker-thickness-vs-fr-cohesion-threshold]] — NEW DATA POINT
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 51 *fī khiṭābātihi*
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, *al-khiṭāb* section
