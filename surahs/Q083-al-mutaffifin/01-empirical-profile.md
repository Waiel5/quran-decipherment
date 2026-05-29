---
surah: 83
surah_name_ar: المطففين
surah_name_translit: al-Muṭaffifīn
file_type: empirical-profile
date_last_updated: 2026-05-29
phase: B+
verdict: Empirical anchors integrated from H-NEW-{111,590,700,720,750,840} + §10.80 kallā census. All values computed/cited from disk.
---

# Q 83 al-Muṭaffifīn — Empirical Architectural Profile

All numbers below are read from `findings/phase-b-hypotheses/csv/*.json`, `data/`, or computed directly
from `quran-text/quran-no-tashkeel.json` + `data/morphology/quranic-corpus-morphology-0.4.txt`.

## 1. Headline numbers

| Metric | Value | Source |
|:--|:--:|:--|
| Verse count | 36 | `data/hafs-verse-counts.tsv`; verified `quran-no-tashkeel.json` |
| Word count (no-tashkeel, marks stripped) | 169 | computed |
| Letter count (no spaces, marks stripped) | 750 | computed |
| Distinct words | 118 | computed (TTR 0.698) |
| Avg verse length | 4.69 words / 20.8 letters | computed |
| Top final-letter (rhyme) | ن (nūn) | 27/36 = **0.75** |
| Rhyme 2nd letter | م (mīm) | 9/36 = 0.25 |
| Rhyme entropy (Shannon, nats) | **0.562** | `h-new-750.json` per_surah (rhyme_entropy_nats) — LOW (near-monorhyme) |
| FR-mean to corpus | **0.8653** | `h-new-111.json` D-matrix (computed); = `h-new-750.json` mean_content_distance |
| FR-median to corpus | 0.8564 | `h-new-111.json` (computed) |
| Corpus FR-mean (reference) | 0.9235 | `h-new-111.json` distance_matrix_stats.mean = 0.923487 |
| Δ (Q83 − corpus mean) | **−0.0581** (more central than average) | computed |
| FR centrality rank | **38/114** | computed from `h-new-111.json` |
| Outlier-strength delta_pct (H-NEW-590) | **−0.26** | `h-new-590.json` X=83; classification **NULL** (interior) |
| iʿjāz sig_A (al-Bāqillānī fawāṣil) | **+0.198** (rank 55/114) | `h-new-750.json` per_surah |
| iʿjāz sig_B (al-Sakkākī iqāʿ) | **−0.339** (rank 64/114) | `h-new-750.json` per_surah |
| UAS (H-NEW-840) | **−2.491, rank 110/114** | `h-new-840.json` all_uas — among corpus LOWEST |
| z_mean_content_distance | −0.574 | `h-new-750.json` |
| z_rhyme_entropy | −0.376 | `h-new-750.json` |
| z_local_cohesion | +0.037 | `h-new-750.json` |
| Q 82→83 adjacency delta_raw | **+0.0355**, rank 38/113 (smooth) | `h-new-720.json` per_adjacency s=82 |
| Q 83→84 adjacency delta_raw | **+0.0646**, rank 59/113 (middle-pack) | `h-new-720.json` per_adjacency s=83 |
| Genuine rebuke-*kallā* (QAC AVR) | **4** (vv. 7,14,15,18) — corpus-MAX tie w/ Q 74 | QAC v0.4 (computed); §10.80 |

## 2. Fisher-Rao neighbourhood (H-NEW-111)

Computed from `h-new-111.json` `D_matrix_upper_triangular` (entries `[i, j, dist]`, 1-based). Q 83's
top-15 FR-nearest:

| Rank | Surah | Name | FR | Note |
|:-:|:-:|:--|:--:|:--|
| 1 | Q 101 | al-Qāriʿa | 0.5625 | short-tail eschatological (the Striking Calamity; balance/weighing motif) |
| 2 | **Q 82** | **al-Infiṭār** | **0.5770** | **mushaf-left-neighbour; judgment-record scene twin (kirāman kātibīn)** |
| 3 | Q 108 | al-Kawthar | 0.5839 | shortest-mufaṣṣal hub |
| 4 | Q 112 | al-Ikhlāṣ | 0.5882 | terminal-triad |
| 5 | Q 114 | al-Nās | 0.5894 | terminal-triad |
| 6 | Q 107 | al-Māʿūn | 0.5910 | ethical short-tail (defrauding-the-orphan parallel) |
| 7 | Q 110 | al-Naṣr | 0.5917 | short-tail |
| 8 | Q 106 | Quraysh | 0.5929 | short-tail (commerce/caravan theme) |
| 9 | Q 113 | al-Falaq | 0.5976 | muʿawwidhāt |
| 10 | Q 105 | al-Fīl | 0.5988 | short-tail |
| 11 | Q 102 | al-Takāthur | 0.6011 | short-tail (worldly accumulation rebuke) |
| 12 | Q 103 | al-ʿAṣr | 0.6013 | oath-cluster |
| 13 | Q 111 | al-Masad | 0.6029 | short-tail |
| 14 | Q 91 | al-Shams | 0.6051 | oath-cluster |
| 15 | Q 100 | al-ʿĀdiyāt | 0.6055 | oath-cluster |

**ALL 15 top neighbours are in the short-Meccan-tail (Q 91–114) block.** The structurally salient one is
**Q 82 al-Infiṭār at rank 2 (FR 0.577)** — its mushaf-left-neighbour. Q 82 shares the *kitāb*/recording
theme (Q 82:10–12, the honourable recording angels *kirāman kātibīn* who "know what you do"), which is
the thematic glue with Q 83's *kitāb al-fujjār / kitāb al-abrār* records. This FR-adjacency + thematic
adjacency makes Q 82↔Q 83 a genuine judgment-scene twin pair.

Far end (FR-farthest): Q 9 al-Tawba (1.248), Q 4 al-Nisāʾ (1.231), Q 3 Āl ʿImrān (1.196), Q 5
al-Māʾida (1.168), Q 2 al-Baqara (1.167) — the long Medinan legal-polemic block, diametrically opposite
in length and register. (Note the irony: in the CHRONOLOGY, Q 83 is the immediate predecessor of Q 2;
in the FR-architecture, Q 2 is one of Q 83's farthest surahs. This is the standard
chronology-architecture dissociation seen across the short-tail.)

## 3. Outlier-strength (H-NEW-590)

`h-new-590.json` entry X=83: window [80–86], window-minus-X d̄ comparison →
- d_W = 0.6134, d_W_minus_X = 0.5956
- pct_W = 0.41, pct_W_minus_X = 0.67
- **delta_pct = −0.26**, p_greater_W = 0.9959, **classification = NULL**.

Q 83 is **INTERIOR** to its FR-cluster (removing it barely changes the window's distance profile; it is
typical of its local neighbourhood, not an outlier). This is consistent with its FR-centrality
(rank 38/114) and short-tail-typical profile.

## 4. iʿjāz signature (H-NEW-750)

From `h-new-750.json` per_surah (surah 83):
- **sig_A (al-Bāqillānī iʿjāz al-fawāṣil) = +0.198, rank 55/114** — middling. The fawāṣil-rhyme
  signature is slightly above the median but unremarkable; Q 83's near-monorhyme nūn-ending is regular
  rather than strikingly varied.
- **sig_B (al-Sakkākī iqāʿ) = −0.339, rank 64/114** — slightly below median; the content↔rhyme
  anti-correlation iqāʿ-signature is mild for Q 83.
- rhyme_entropy_nats = 0.562 (LOW; near-monorhyme), z = −0.376.
- mean_content_distance = 0.865, z = −0.574 (more cohesive/central than average).
- local_cohesion = 1.545, z = +0.037 (typical).

## 5. Unified Architectural Significance (H-NEW-840)

`h-new-840.json` all_uas (surah 83): **UAS = −2.491, rank 110/114.** Components:
- abs_outlier = 0.26 (near-zero — interior, per H-NEW-590).
- max_cost = 0.0646 (its largest adjacency cost, Q 83→84 — low).
- abs_ijaz = 0.198 (the sig_A magnitude — middling-low).

Q 83 is among the corpus's **lowest** UAS surahs (bottom-5: Q 83, 73, 105, 114, 87). This places Q 83
firmly in the **anti-iʿjāz / low-structural-significance** category on the project's UAS axis. This is
NOT a theological verdict — it means Q 83 is a SMOOTH, INTERIOR, low-adjacency-cost short-tail surah
without the outlier-strength or rhyme-extremity that drives high UAS. (The Protocol §3.3 bottom-10 list
explicitly names Q 83, confirming this profile.)

## 6. Canonical-adjacency cost (H-NEW-720)

From `h-new-720.json` per_adjacency (delta_raw = constrained-TSP cost of forcing the canonical pair):

| Boundary | delta_raw | rank (ascending, /113) | Note |
|:--|:--:|:--:|:--|
| Q 81 → Q 82 | +0.0621 | 57/113 | middle-pack |
| **Q 82 → Q 83** | **+0.0355** | **38/113** | smooth — consistent with the Q82↔Q83 FR-adjacency (rank-2 neighbour) + shared *kitāb*-record theme |
| **Q 83 → Q 84** | **+0.0646** | **59/113** | middle-pack |

Q 82→Q 83 is among the smoother seams (rank 38/113, below median). This is the empirical correlate of
the strong Q 82↔Q 83 FR-proximity (§2) and the shared recording-angels / record-book motif. Neither
seam is in the H-NEW-1240 corpus-extreme clamped-zero seamless tier; both are smooth-but-not-extreme.

## 7. Rhyme / phoneme (H-NEW-700)

- Rhyme: `h-new-700.json` rhyme_letter_diagnostics surah 83 → top_letter **ن**, frac **0.75**, n_verses 36.
  Computed verification: 27/36 verses end ن, 9/36 end م. This is a **strong near-monorhyme on -īn / -ūn /
  -ūn-class** endings (sijjīn, ʿilliyyīn, mubʿathūn, yaksibūn, tukadhdhibūn, al-mutanāfisūn, yanẓurūn,
  yafʿalūn …) with a secondary -ʿīm / -mīm cadence (naʿīm, raḥīm-class, tasnīm). The -īn/-ūn nūn-rhyme
  is the dominant cadence of the whole eschatological short-tail.
- Phoneme vector (`h-new-700.json` phoneme_vectors[82]) = [0.016, 0.032, 0.0267, 0.092] (emphatic /
  pharyngeal / sibilant-or-glottal density bins, per H-NEW-700 normalization). The 4th component (0.092)
  is the highest — consistent with a sibilant/glottal-rich text (sijjīn, taṭfīf, asāṭīr, sijjīl-class
  consonants).

## 8. Rebuke-*kallā* maximum (§10.80 H-NEW-2160 integration)

Computed from QAC v0.4 (`POS:AVR, LEM:kal~aA`):
- **Q 83 = 4 genuine rebuke-*kallā* (vv. 7, 14, 15, 18)** — TIED with Q 74 al-Muddaththir for the
  corpus maximum. Only these two surahs reach 4.
- Corpus-wide genuine AVR-*kallā* total = **33** (matches al-Dānī's classical count cited by al-Suyūṭī).
- Q 83's 4 are all clause-initial rebuke particles, all in the mushaf second half. Q 4's "4 كلا" by raw
  substring are ALL the homograph *kullā/kilā* (0 genuine rebuke-*kallā*) — the §10.80 homograph trap.
- Distribution check: 27 of 33 genuine rebuke-*kallā* are in surahs s>57 (second half) — vindicating
  al-Dānī's "latter-half-only" claim after disambiguation.

## 9. Architectural type classification

| Axis | Q 83 placement |
|:--|:--|
| Length class | short-Meccan-tail; lower-awsāṭ / upper-qiṣār al-mufaṣṣal |
| Compression-tail position | s=83 ≫ kink-50 — deep inside the compression-tail regime |
| Chronology bucket | Egyptian-std **#86 (last Meccan, boundary)**; Nöldeke #37 (Early Meccan) — DISPUTED Makkī/Madanī |
| FR neighbourhood | short-Meccan-tail (all top-15 in Q 91–114); FR-CENTRAL (rank 38/114); Q 82 2nd-nearest |
| Outlier-strength | INTERIOR (NULL; delta_pct −0.26) |
| UAS axis | **LOW (rank 110/114) — anti-iʿjāz / low-structural-significance** |
| iʿjāz signature | middling fawāṣil (+0.198), mild iqāʿ (−0.339) |
| Rhyme | near-monorhyme nūn (0.75); LOW entropy (0.562) |
| Adjacency role | smooth left-seam (Q82→83 rank 38), middle right-seam (Q83→84 rank 59) |
| Special feature | corpus-MAX rebuke-*kallā* (4, tie Q 74); SIJJĪN↔ʿILLIYYĪN muqābala |

**Architectural verdict:** Q 83 is a **FR-central, interior, low-UAS short-Meccan-tail eschatological
surah** whose distinctiveness is NOT structural-significance (it is near the bottom on UAS) but
**content-architectural**: the rebuke-*kallā*-driven SIJJĪN↔ʿILLIYYĪN antithesis and the
taṭfīf→recompense chiastic-justice frame. Its empirical profile (low UAS, interior, smooth seams,
near-monorhyme) is the signature of a tightly-cohesive, formula-repeating short-tail surah — and its
strong FR-adjacency to its mushaf-neighbour Q 82 (rank-2, 0.577) is the standout architectural fact.

## 10. Cross-references

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 83 FR row; Q 82 rank-2 neighbour.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 83 INTERIOR (NULL).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — nūn-monorhyme 0.75.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q82→83 smooth (rank 38); Q83→84 middle (rank 59).
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A +0.198, sig_B −0.339.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 110/114 (low).
- §10.80 H-NEW-2160 — rebuke-*kallā* corpus-MAX (4, tie Q 74).
- Q083-F-01 (this surah) — SIJJĪN↔ʿILLIYYĪN antithesis test (06-novel-findings).
