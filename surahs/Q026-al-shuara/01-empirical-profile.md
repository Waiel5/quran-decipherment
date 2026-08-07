---
surah: 26
surah_name_ar: الشعراء
file_type: empirical-profile
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — empirical anchors integrated from H-NEW-{111, 590, 700, 720, 750, 840}
---

# Q 26 al-Shuʿarāʾ — Empirical Architectural Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

All values cited from disk. Default rules-tuple: `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` unless noted.

## 1. UAS (Unified Architectural Score)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json`.

| Component | Q 26 value | Corpus interpretation |
|:--|:-:|:--|
| **UAS composite** | **1.822** | rank **14 of 114** (top 13%) |
| abs(outlier) | 8.83 | mild |
| max canonical-adjacency cost | 0.0806 (Q 26 → Q 27) | low |
| abs(iʿjāz_signature_A) | 2.253 | high *magnitude*, NEGATIVE direction |

Q 26's UAS is driven primarily by the **|sig_A| = 2.253** term (rank 108/114 on rank_A — bottom decile by signed value, top decile by magnitude). This is "anti-iʿjāz al-fawāṣil" — same phenotype as Q 12 Yūsuf and Q 27 al-Naml: long continuous narrative + nūn-rhyme uniform → low rhyme entropy + *higher-than-average content distance*.

Top-10 UAS surahs: Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17. Q 26 sits at #14, just outside the top-10 with the same anti-iʿjāz-fawāṣil profile as Q 12 (#6) and just above Q 27 (#23).

## 2. Outlier-strength Δ%ile

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json`.

```
{
  "X": 26,
  "window": [23, 24, 25, 26, 27, 28, 29],
  "window_minus_X": [23, 24, 25, 27, 28, 29],
  "d_W": 0.9501,
  "d_W_minus_X": 0.9371,
  "pct_W": 57.22,
  "pct_W_minus_X": 48.39,
  "delta_pct": +8.83,
  "p_greater_W": 0.4278,
  "classification": "WEAK_OUTLIER"
}
```

**Interpretation**: Q 26, when *included* in the 7-window {23..29}, makes the window *more diffuse* (d_W = 0.950 > d_W_minus_X = 0.937), placing the with-Q26 window at 57th %ile vs without at 48th %ile. **Q 26 is mildly outlying** in its window — opposite to its right-neighbor Q 27 (a WEAK_ANCHOR). Q 26 brings ROOT-content novelty into the Q 24–30 cluster.

## 3. iʿjāz signature

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json`.

```
{
  "surah": 26, "n_verses": 227,
  "rhyme_entropy_nats": 0.4766,
  "top_final_letter": "ن", "top_final_letter_frac": 0.8502,
  "mean_content_distance": 1.0979,
  "local_cohesion": 0.9916,
  "z_rhyme_entropy": -0.531, "z_mean_content_distance": +1.722,
  "z_local_cohesion": -0.717,
  "sig_A": -2.2527, "sig_B": -1.2483,
  "rank_A": 108, "rank_B": 92
}
```

**Interpretation**: sig_A = z_rhyme_entropy − z_mean_content_distance = (-0.53) − (+1.72) = -2.25. Q 26 has BOTH:
- **low rhyme entropy** (0.477 nats; nūn-rhyme dominant at 85%) → contributes negative magnitude
- **high mean content distance** (1.098 — rank 110 of 114) → contributes negative magnitude

So Q 26 is *anti-iʿjāz-al-fawāṣil*: where the iʿjāz hypothesis (al-Bāqillānī) predicts *rhyme variety where content is most coherent*, Q 26 has *rhyme uniformity where content is most distinct*. The same phenotype as Q 12 Yūsuf — and matches the deep structural fact that Q 26 is a continuous-narrative-driven surah where the refrain ENFORCES rhyme uniformity (since R1 ends *muʾminīn* and R2 ends *raḥīm*, both -īn/-īm).

## 4. Position in compression-tail

Source: `[[h-new-660-compression-tail-gradient|H-NEW-660]]`.

Law: d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) for K=15 windows.

For s=26 (head zone, no kink contribution): predicted d̄_content ≈ 0.96.

Q 26's mean content distance = **1.098**, which is **+14 pp above** the law's prediction. Q 26 is *significantly more content-distinct than its mushaf-position predicts under the corpus compression-tail law* — directionally consistent with WEAK_OUTLIER (+8.83 pp) and with rank 110/114 on mean-FR.

## 5. Canonical-adjacency costs (TSP-residual decomposition)

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json`.

| Pair | δ (delta) | fraction of TSP residual (8.29) |
|:--|:-:|:-:|
| Q 25 → Q 26 | **0.0553** | 0.67% |
| Q 26 → Q 27 | **0.0806** | 0.97% |

Both low — the Q 25 (al-Furqān) → Q 26 (al-Shuʿarāʾ) → Q 27 (al-Naml) → Q 28 (al-Qaṣaṣ) run is **structurally cheap**. Q 26 fits its mushaf-position smoothly, despite being a content-outlier in absolute terms (rank 110/114 mean-FR). The adjacency cost is *local* (against immediate neighbors), not absolute.

The most-expensive canonical pair (Q 1-Q 2 = 7.4% of residual) is 7.6× more expensive than Q 25-Q 26. Q 26 is a low-friction insertion into its position.

## 6. FR-distance neighbors

Source: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json` (D-matrix reconstructed).

**Q 26's 5 nearest in FR-roots distance**:
| Rank | Surah | Name | d |
|:-:|:-:|:--|:-:|
| 1 | Q 7 | al-Aʿrāf | 0.832 |
| 2 | Q 15 | al-Ḥijr | 0.879 |
| 3 | Q 36 | Yāsīn | 0.903 |
| 4 | Q 23 | al-Muʾminūn | 0.904 |
| 5 | Q 11 | Hūd | 0.906 |

**All 5 are prophet-cycle / qaṣaṣ-rich Meccan surahs.** Q 26 is a textbook member of the *qaṣaṣ-cluster*. Notice: **Q 28 al-Qaṣaṣ (its ṬSM sister) is NOT in the top-5** (d_Q26_Q28 = 0.954); Q 27 al-Naml is also not (d_Q26_Q27 = 0.959). The shared muqaṭṭaʿ-letter-set DOES NOT predict FR-content-proximity.

**Q 26's 5 farthest**:
| Rank | Surah | Name | d |
|:-:|:-:|:--|:-:|
| 1 | Q 111 | al-Masad | 1.234 |
| 2 | Q 97 | al-Qadr | 1.238 |
| 3 | Q 88 | al-Ghāshiya | 1.262 |
| 4 | Q 80 | ʿAbasa | 1.281 |
| 5 | Q 55 | al-Raḥmān | 1.294 |

The farthest are short-mufaṣṣal-qiṣār surahs and Q 55 — anti-iʿjāz dual to Q 26 (Q 55 is the corpus-FR-most-distinctive surah; Q 26 is rank 110/114).

**Q 26 mean FR distance** = 1.098 (rank 110 of 114; one of the most content-distinct surahs corpus-wide).

## 7. Top roots in Q 26 (QAC v0.4)

Source: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.

Q 26 has 1,353 words, with QAC root annotations on the verse-text. The dominant roots reflect the prophet-cycle architecture:
- *qwl* (q-w-l, "say") — dialogue-heavy;
- *Alh* (ʾ-l-h, God) and *rbb* (r-b-b, Lord) — refrain-anchored ("rabbaka la-huwa al-ʿazīzu al-raḥīm" 8x);
- *qwm* (q-w-m, people/tribe) — the prophets-and-their-peoples motif;
- *ATy/jyA* (come/bring) — narrative-eventive;
- *ðhb* (go/depart) — Mūsā/exodus;
- *Sdq* (truth) and *kdb* (lie/deny) — rejection-narratives.

The single root **shʿr** (root of *shuʿarāʾ* "poets", verb *shaʿara* "to perceive/sense") appears 6 times across the corpus, including v 224 of Q 26 (the surah-name).

## 8. Architectural type classification

Per the dual-iʿjāz typology ([[h-new-840-unified-architectural-score|H-NEW-840]]):
- **Structural-iʿjāz axis**: high (UAS rank 14).
- **iʿjāz al-fawāṣil**: STRONGLY NEGATIVE (anti-fawāṣil; sig_A = −2.253 → rank 108/114). The dominant nūn-rhyme refrain is the OPPOSITE of multi-rāwiyy variety.
- **Theological-iʿjāz**: Q 26's coda (vv 224–227) is the *al-Bāqillānī foundational anti-poetry-iʿjāz claim* — the Quran refuses poetic-imitation as a genre. So Q 26 carries theological-iʿjāz weight via its coda, even though the surah itself is anti-iʿjāz-al-fawāṣil structurally.

**Type**: anti-iʿjāz-al-fawāṣil structural-distinctness (cluster: **Q 12 Yūsuf** UAS 6, **Q 26 al-Shuʿarāʾ** UAS 14, **Q 27 al-Naml** UAS 23, **Q 28 al-Qaṣaṣ**, **Q 18 al-Kahf**) — narrative-driven, rhyme-uniform, content-distinct.

## 9. Cross-references to all H-NEW findings touching Q 26

- [[h-new-111-fisher-rao-distance-matrix|H-NEW-111]] — Q 26 mean-FR rank 110/114; nearest cluster = qaṣaṣ-Meccan.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 26 +8.83pp WEAK_OUTLIER.
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 26 nūn 85.0%, entropy 0.477 nats.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 25-26 = 0.055, Q 26-27 = 0.081 (both low).
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — Q 26 sig_A = −2.253, rank 108/114.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 26 UAS rank 14/114.
- [[h-new-600-letter-families|H-NEW-600]] — relevant negative result (TSM-3 cluster cohesion NULL via Q026-F-02).
- [[h-new-660-compression-tail-gradient|H-NEW-660]] — Q 26 has *intra-surah* refrain-cycle compression (Q026-F-01); structurally analogous to the corpus-wide content-compression law.

## 10. Honest limits

- The signed sig_A of −2.253 puts Q 26 deep in the anti-iʿjāz tail. This is *not* a deficit — it is a structurally-different mode (continuous narrative + refrain-enforced rhyme uniformity). The dual-iʿjāz typology recognizes this as the structural-iʿjāz axis (UAS rank 14) being orthogonal to fawāṣil-variety.
- Mean FR-distance rank 110/114 reflects content distinctness, but Q 26's nearest neighbors *are* a coherent qaṣaṣ-cluster (Q 7, Q 11, Q 15, Q 23, Q 36) — i.e., distinct from corpus-mean BUT cohesive within its own family.
- The Q 26 ↔ Q 28 FR-distance (0.954) is *higher* than typical letter-family-twin-pairs would suggest. The shared ṬSM letter set does NOT predict FR-content-proximity at the whole-surah level. This anchors the FALSIFIED-direction of Q026-F-02 and Q026-F-04.
- Q026-F-01's intra-surah compression (rho = −0.839 over 7 prophet-cycles) is a **novel structural feature** uncovered in this investigation. The classical mufassirūn (al-Rāzī, al-Biqāʿī, Ibn Kathīr) noted the cycle-architecture but did NOT quantify the length-progression. This is a project-original finding.
