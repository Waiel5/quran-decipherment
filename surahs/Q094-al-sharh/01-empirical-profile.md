---
surah: 94
surah_name_ar: الشرح
surah_name_translit: al-Sharḥ
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 (every value cited to path)
---

# Q 94 al-Sharḥ — Empirical Profile

All values below are read directly from the on-disk artifacts. No value is asserted from memory.
Q 94 is surah-id 94; in the 1-indexed Fisher-Rao matrix it is index 94; in the 0-indexed phoneme
vector list (`h-new-700.json` → phoneme.phoneme_vectors) it is index 93.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`, 6441 pairs),
1-indexed surah IDs. Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235.

| Quantity | Value |
|:--|:--|
| Q 94 mean FR to all 113 surahs | **0.7936** (far below corpus mean 0.9235) |
| Nearest neighbor | **Q 108 al-Kawthar** at FR 0.2305 |
| Top-15 FR neighbors | Q 108 (0.231), Q 106 (0.271), Q 111 (0.287), Q 113 (0.290), Q 103 (0.293), Q 100 (0.295), Q 112 (0.298), Q 105 (0.305), Q 107 (0.305), Q 110 (0.317), Q 104 (0.318), Q 114 (0.319), Q 101 (0.340), Q 102 (0.351), Q 95 (0.361) |
| 5 farthest | Q 5 (1.255), Q 2 (1.261), Q 4 (1.299), Q 3 (1.303), Q 9 (1.304) |

**Reading.** Q 94's FR neighborhood is almost the entire short-Meccan / muʿawwidhāt tail (Q 108, 106,
111, 113, 103, 100, 112, 105, 107, 110, 104, 114, 101, 102, 95) — the densest, lexically-narrowest
short surahs. Q 94's mean FR of 0.7936 is one of the lowest in the corpus: it is deep *inside* a tight
cluster, not a dispersion-extreme. The 5 farthest are the long-Medinan legal/narrative surahs (Q 5
al-Māʾida, Q 2 al-Baqara, Q 4 al-Nisāʾ, Q 3 Āl-ʿImrān, Q 9 al-Tawba) — the maximal-vocabulary
end of the corpus. The content-axis cleanly separates Q 94 (8-verse consolation) from the legal corpus.

**Neighbor surahs in Q 94's FR list:**

| Surah | Rank in Q 94's FR list | FR to Q 94 |
|:--|:--|:--|
| Q 95 al-Tīn (next) | 15 / 113 | 0.3614 |
| Q 93 al-Ḍuḥā (prev, paired) | 16 / 113 | 0.3641 |

Both neighbors are top-16 FR neighbors — Q 94 sits among its mushaf neighbors content-wise, consistent
with the seamless Q 93 → Q 94 seam (§5) and the consolation-pair reading.

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 94) | {Q 91, 92, 93, 94, 95, 96, 97} |
| d̄_W (window with Q 94) | 0.4530 |
| d̄_W−X (window without Q 94) | 0.4742 |
| pct_W | 0.01 |
| pct_W−X | 0.08 |
| **delta_pct** | **−0.07** |
| p_greater_W | 0.9999 |
| **classification** | **NULL** |

**Reading.** The {Q 91-97} window has pct_W = 0.01 — an extraordinarily low content-dispersion
percentile, i.e. this run of short late-mushaf surahs is one of the most internally-homogeneous
neighborhoods in the corpus. Removing Q 94 *lowers* the dispersion percentile by only 0.07pp, so Q 94
is a textbook **cohesion member**, not an outlier (contrast the project's outliers: Q 33 +31.46,
Q 1 +27.09). Q 94's architectural interest is therefore micro-structural (the near-verbatim reprise),
not whole-surah-dispersion-extreme.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 94): top final-letter **ك (kāf)**, fraction **0.5** (4/8 verses).
The close-read final-letter scan shows the surah is actually **three-zone**, not a monorhyme:

| Zone | Verses | Final | Rhyme syllable |
|:--|:--|:--|:--|
| A (addressee) | 1-4 | ك | -aka: ṣadra-**ka**, wizra-**ka**, ẓahra-**ka**, dhikra-**ka** |
| B (reprise) | 5-6 | ا | -rā: yus-**rā** (the identical couplet) |
| C (charge) | 7-8 | ب | -ab: fa-nṣa-**b**, fa-rgha-**b** |

The kāf-zone (vv 1-4) is the 2nd-person possessive suffix on four favors (breast, burden, back, fame);
it gives the 50% top-letter fraction. Q 94 (s=94 > 50) sits in the dispersing tail of the project rhyme
dispersion-tail law (two-piece kink-50, primary_r2 = 0.7886).

**Phoneme** (phoneme_vectors index 93, 4-dim density vector):
`[0.04902, 0.07843, 0.07843, 0.06863]`. Project phoneme dispersion-tail law two-piece kink-75
(primary_r2 = 0.9457). Q 94 (s=94 > 75) sits in the high-dispersion tail; its four channels are
relatively balanced (2nd and 3rd channels tied at 0.0784 are the largest).

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 94:

| Field | Value |
|:--|:--|
| n_verses | 8 |
| rhyme_entropy_nats | **1.0397** |
| top_final_letter | ك |
| top_final_letter_frac | 0.5 |
| mean_content_distance | 0.7936 |
| local_cohesion | **2.4524** |
| z_rhyme_entropy | +0.4887 |
| z_mean_content_distance | **−1.2817** |
| z_local_cohesion | **+1.2716** |
| **sig_A** | **+1.7705** (rank **11 / 114**) |
| **sig_B** | **+1.7603** (rank **13 / 114**) |

**Reading.** Q 94 is a high-iʿjāz-signature short surah: sig_A rank 11/114 and sig_B rank 13/114 place
it in the top ~10% of the al-Bāqillānī *iʿjāz al-fawāṣil* structural-significance axis — remarkable for
an 8-verse surah. The drivers are (a) the **very low mean content distance** (z = −1.28: Q 94 is much
more lexically-typical-of-its-cluster than average) and (b) the **high local cohesion** (2.45, z = +1.27:
the surah's roots are concentrated and internally repeated — the *-ka* suffix run and the ʿ-s-r/y-s-r
reprise drive this). Rhyme entropy 1.04 nats (z = +0.49) is slightly above average, reflecting the
three-zone fawāṣil rather than a single rāwī.

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | ascending-rank | class |
|:--|:--|:--|:--|
| **Q 93 → Q 94** | **−0.01520** | **10 / 113** | **seamless** (negative-delta joint) |
| Q 94 → Q 95 | +0.04700 | 43 / 113 | mid-spectrum |

The Q 93 al-Ḍuḥā → Q 94 al-Sharḥ entry is one of the smoothest joints in the mushaf (negative delta,
asc-rank 10/113), and the immediately-preceding Q 91 → Q 92 is the corpus's single cheapest seam
(delta_raw = −0.0868) — so the late-Meccan short run Q 91 → Q 92 → Q 93 → Q 94 is an unusually smooth
stretch. The exit Q 94 → Q 95 al-Tīn is a normal mid-cost transition (+0.047, rank 43/113).

**Classical correlate.** The smoothness of the Q 93 → Q 94 seam is the empirical correlate of the
classical *consolation-pair* reading: al-Ḍuḥā (*mā waddaʿaka rabbuka wa-mā qalā* — "your Lord has not
forsaken you") and al-Sharḥ (*a-lam nashraḥ laka ṣadrak* — "did We not expand your breast?") are both
direct second-person reassurances to the Prophet, sharing the *rabbuka* address (Q 93:3,5,11; Q 94:8)
and the dhikr/elevation theme. Top-3 most-expensive corpus seams for contrast: Q 1→Q 2 (0.622),
Q 32→Q 33 (0.363), Q 33→Q 34 (0.331).

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **−0.6415** (rank **65 / 114**) |
| abs_outlier | 0.07 (from H-NEW-590 delta_pct) |
| max_cost | 0.04700 (the Q 94 → Q 95 seam) |
| abs_ijaz | 1.7705 (= sig_A) |

**Reading.** Q 94's UAS rank 65/114 places it in the middle band. The iʿjāz component is high (sig_A
1.77, top ~10%) but the other two components are near-zero — the outlier strength is essentially nil
(deep cohesion member) and the max neighbor TSP cost is low (both seams are cheap, the seamless backward
seam pulls the max down to the forward 0.047). So Q 94 is **not** a top-UAS whole-surah architectural hub
(top-10 are Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17); its distinctiveness is **local and micro-structural**
(the corpus-singleton near-verbatim reprise, Q094-F-01), exactly the profile of a short, dense, cohesive
consolation surah.

## 7. Lexical counts (computed; `scripts/Q094_F_01_usr_yusr_reprise.py` pipeline + close-read scan)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 8 | `data/hafs-verse-counts.tsv` "94	8" |
| Words (marks stripped) | 27 | computed |
| Letters | 102 | computed |
| Distinct QAC roots | 14 | `data/morphology/root-index.json`, 16 root-tokens |
| Per-verse roots | v1 {š-r-ḥ, ṣ-d-r}, v2 {w-ḍ-ʿ, w-z-r}, v3 {n-q-ḍ, ẓ-h-r}, v4 {r-f-ʿ, dh-k-r}, v5 {ʿ-s-r, y-s-r}, v6 {ʿ-s-r, y-s-r}, v7 {f-r-gh, n-ṣ-b}, v8 {r-b-b, r-gh-b} | QAC v0.4 |
| Near-verbatim reprise | v5 ≈ v6 (edit distance 1, the leading fāʾ) | Q094-F-01 (global corpus minimum) |
| v5/v6 root-Jaccard | 1.0 (identical root-set {ʿ-s-r, y-s-r}) | Q094-F-01 Arm C |

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** deep in-block COHESION member (delta_pct −0.07, NULL); window pct 0.01.
- **iʿjāz axis (H-NEW-750):** high structural-iʿjāz (sig_A rank 11/114, sig_B rank 13/114) driven by
  very-low content distance + high local cohesion.
- **UAS (H-NEW-840):** middle (rank 65/114) — iʿjāz-high but outlier-flat, hence not a whole-surah hub.
- **Net:** Q 94 is a **short, lexically-concentrated, internally-cohesive Meccan consolation surah**
  whose single most distinctive empirical signature is *micro-structural*: the corpus-tightest
  near-verbatim adjacent couplet (Q 94:5-6). This matches its content profile — a four-favor address
  (vv 1-4), a doubled hardship-ease assurance (vv 5-6), and a two-clause discharge charge (vv 7-8).

## 9. Honest limits

- The phoneme 4-vector channel labels are not annotated in `h-new-700.json`; only the raw 4-density
  values are reported, so the per-channel interpretation (emphatic/pharyngeal/sibilant/glottal) is left
  un-assigned to avoid asserting an un-verified mapping.
- H-NEW-590's window for Q 94 is the symmetric ±3 neighborhood {91-97}; the NULL classification is
  window-definition-dependent.
- FR distances are on QAC-STEM root distributions; for an 8-verse / 14-root surah the per-surah root
  distribution is sparse, so the FR neighbor list is more sensitive to individual root weights than for
  long surahs — the very-low mean FR (0.79) partly reflects the small root vocabulary shared across the
  whole short-surah cluster.
- The H-NEW-700 "top letter ك 0.5" is a single-letter diagnostic; the surah is genuinely three-zone, so
  the monorhyme framing would be misleading and is corrected here.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 94 row; mean 0.7936, nearest Q 108)
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 94 NULL, cohesion member of {91-97})
- [[h-new-700|H-NEW-700]] — rhyme (three-zone) + phoneme dispersion-tails
- [[h-new-720|H-NEW-720]] — Q 93 → Q 94 seamless seam (asc-rank 10/113)
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank 11/114, sig_B rank 13/114)
- [[h-new-840|H-NEW-840]] — UAS rank 65/114
- [[h-new-2310-refrain-structure|H-NEW-2310]] — Q 94:5-6 is the near-verbatim complement of the verbatim census

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30.*
