---
surah: 20
surah_name_ar: طه
surah_name_translit: Ṭā-Hā
file_type: empirical-profile
date_last_updated: 2026-05-30
phase: B+
verdict: integrated from h-new-111 / -590 / -700 / -720 / -750 / -840 (all values cited to path)
---

# Q 20 Ṭā-Hā — Empirical Profile

All values below are read directly from the on-disk artifacts. No value is asserted from memory.
Q 20 is surah-id 20; in the 1-indexed Fisher-Rao matrix it is index 20; in the 0-indexed phoneme
vector list (`h-new-700.json` → phoneme.phoneme_vectors) it is index 19.

## 1. Fisher-Rao geometry (`findings/phase-b-hypotheses/csv/h-new-111.json`)

Matrix stored as upper-triangular `[i, j, dist]` triples (`D_matrix_upper_triangular`), 1-indexed surah IDs.
Corpus matrix stats: min 0.2127, max 1.5509, mean 0.9235, median 0.9567.

| Quantity | Value |
|:--|:--|
| Q 20 mean FR to all 113 surahs | **1.0403** (well above corpus mean 0.9235 — Q 20 is content-distant) |
| Nearest neighbor | **Q 23 al-Muʾminūn** at FR 0.8600 |
| Top-15 FR neighbors | Q 23 (0.860), **Q 7 (0.865)**, Q 51 (0.881), Q 41 (0.882), Q 43 (0.891), **Q 28 (0.895)**, Q 32 (0.899), Q 15 (0.925), **Q 27 (0.928)**, Q 79 (0.934), Q 10 (0.935), Q 36 (0.937), Q 17 (0.939), Q 18 (0.947), Q 46 (0.950) |
| 5 farthest | Q 33 (1.174), Q 56 (1.182), Q 9 (1.200), Q 4 (1.203), Q 55 (1.270) |

**Reading.** Q 20's FR neighborhood is the **long-Meccan narrative cluster** — Q 23 al-Muʾminūn (nearest),
Q 7 al-Aʿrāf (#2), Q 51 al-Dhāriyāt, the ḥawāmīm Q 41/Q 43, Q 28 al-Qaṣaṣ (#6), Q 27 al-Naml (#9), Q 79
al-Nāziʿāt (#10), Q 10 Yūnus, Q 36 Yā-Sīn, Q 18 al-Kahf — surahs dense in prophet-narrative and
eschatology. The 5 farthest are the long Medinan-legal surahs (Q 9, Q 4, Q 33) and the two FR-isolates
Q 56 al-Wāqiʿa and Q 55 al-Raḥmān (corpus-farthest). **Crucially for Q020-F-06**: all three of Q 20's
Mūsā-cycle co-members rank in its top-10 FR neighbors — Q 7 (#2), Q 28 (#6), Q 27 (#9) — and Q 79
(the fourth cycle member) is #10. The Mūsā cycle is geometrically near at whole-surah scale AND
lexically cohesive at pericope scale (F-06).

**Mūsā-cycle / muqaṭṭaʿāt-family ranks within Q 20's FR list:**

| Related surah | Rank in Q 20's FR list | FR to Q 20 |
|:--|:--|:--|
| Q 7 al-Aʿrāf (Mūsā cycle) | 2 / 113 | 0.8650 |
| Q 28 al-Qaṣaṣ (Mūsā cycle) | 6 / 113 | 0.8948 |
| Q 27 al-Naml (Mūsā cycle + 2-letter ṬS) | 9 / 113 | 0.9281 |
| Q 79 al-Nāziʿāt (Mūsā cycle) | 10 / 113 | 0.9340 |
| Q 36 Yā-Sīn (2-letter YS family) | 12 / 113 | 0.9366 |
| Q 26 al-Shuʿarāʾ (Mūsā cycle) | 17 / 113 | 0.9559 |
| Q 19 Maryam (prev surah) | 28 / 113 | 0.9806 |

## 2. Outlier-strength (`findings/phase-b-hypotheses/csv/h-new-590.json`; seed 20260429, 10000 perms, α_bon 0.0083)

| Quantity | Value |
|:--|:--|
| Window (centered on Q 20) | {Q 17, 18, 19, 20, 21, 22, 23} |
| d̄_W (window with Q 20) | 0.9416 |
| d̄_W−X (window without Q 20) | 0.9333 |
| pct_W | 52.01 |
| pct_W−X | 46.49 |
| **delta_pct** | **+5.52** |
| p_greater_W | 0.4799 |
| **classification** | **WEAK_OUTLIER** (NULL by significance — p = 0.48) |

**Reading.** Removing Q 20 from its 7-surah {Q 17-23} neighborhood *raises* the window's content-dispersion
percentile by only +5.52 points (p = 0.48). Q 20 is a **mild positive outlier** — it pushes its window
slightly more cohesive when present — but the effect is far from significance (α_bon 0.0083). Q 20 is
NOT a STRONG_OUTLIER like Q 1 (+27.09) or Q 9 (+21.57); it sits comfortably inside the long-Meccan-narrative
{Q 17-23} block (which includes its FR-nearest-neighbor Q 23 al-Muʾminūn). The mild positive direction is
consistent with Q 20's high mean content-distance (§4): it is content-divergent from the *corpus* centroid
but in-family with its immediate narrative neighbors.

## 3. Rhyme + phoneme (`findings/phase-b-hypotheses/csv/h-new-700.json`)

**Rhyme** (rhyme_letter_diagnostics, Q 20): top final-letter **ى/ي (yāʾ / alif-maqṣūra)**, fraction
**0.7926** (107/135 verses). Project rhyme dispersion-tail law fitted as two-piece-kink-50
(primary_r2 = 0.7886) — Q 20 (s = 20 < 50) sits in the pre-kink low-dispersion regime; its yāʾ-monorhyme
is **strong** (79.3% — one of the highest single-rāwī fractions among the long narrative surahs). The
sustained *-á* ending tracks the Arabic verbal/nominal *maqṣūr* register of the Mūsā narrative
(*mūsā, ṭuwā, istawā, al-hudā, taqḍī, al-tuqā, yashqā*, …).

**Phoneme** (phoneme_vectors index 19, 4-dim density vector):
`[0.01908, 0.04575, 0.04001, 0.10854]`. Project phoneme dispersion-tail law fitted as two-piece-kink-75
(primary_r2 = 0.9457). Q 20 (s = 20 < 75) sits well before the phoneme-kink, in the low-dispersion regime.
The 4th component (0.1085) is the largest of its four channels.

## 4. iʿjāz signature (`findings/phase-b-hypotheses/csv/h-new-750.json`)

Rules-tuple: `[no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-surah-1, mushaf
order, Hafs-Kufan, 28-letter Arabic rhyme basis]`. Per-surah record for Q 20:

| Field | Value |
|:--|:--|
| n_verses | 135 |
| rhyme_entropy_nats | **0.5741** |
| top_final_letter | ى/ي |
| top_final_letter_frac | 0.7926 |
| mean_content_distance | 1.0403 |
| local_cohesion | 1.0065 |
| z_rhyme_entropy | **−0.3544** |
| z_mean_content_distance | **+1.1524** |
| z_local_cohesion | −0.6971 |
| **sig_A** | **−1.5068** (rank **92 / 114**) |
| **sig_B** | **−1.0514** (rank **83 / 114**) |
| rank_A | 92 |
| rank_B | 83 |

**Reading — the monorhyme paradox.** Q 20's rhyme entropy (0.574 nats, z = −0.35) is *below* corpus
average precisely *because* its yāʾ-monorhyme is so dominant (79.3%): a tight single-rāwī surah has LOW
fawāṣil-entropy. On the al-Bāqillānī *iʿjāz al-fawāṣil* structural-significance axis (which rewards
*varied* rhyme as evidence of constraint-satisfaction-under-difficulty), Q 20 therefore scores LOW —
sig_A = −1.51, rank 92/114. This is the project's recurring lesson that **structural-iʿjāz ≠ monorhyme**:
a sustained monorhyme is a different (and arguably easier) phonological feat than the varied-but-coherent
fawāṣil that drive high sig_A. z_mean_content_distance = +1.15 confirms Q 20 is content-divergent (its
dense, episode-specific Mūsā/Ādam lexicon sits far from the corpus centroid — mean_content_distance rank
99/114 ascending).

## 5. Canonical-adjacency / TSP seams (`findings/phase-b-hypotheses/csv/h-new-720.json`)

| Seam | delta_raw | fraction_residual | ascending-rank | class |
|:--|:--|:--|:--|:--|
| Q 19 → Q 20 | +0.06816 | 0.00822 | 61 / 113 | mid-spectrum |
| Q 20 → Q 21 | +0.05441 | 0.00656 | 50 / 113 | mid-spectrum |

Both seams are mid-spectrum (neither seamless nor expensive). For contrast, the top-3 most-expensive
corpus seams are Q 1→Q 2 (0.622), Q 32→Q 33 (0.363), Q 33→Q 34 (0.331). The Q 19 (Maryam) → Q 20 (Ṭā-Hā)
→ Q 21 (al-Anbiyāʾ) run is a smooth Meccan-narrative stretch: three consecutive prophet-narrative surahs,
all opening on muqaṭṭaʿāt-or-near (Q 19 KHYʿṢ, Q 20 ṬH) or direct prophet-narrative (Q 21). The forward
seam (Q 20 → Q 21, rank 50) is slightly smoother than the backward (Q 19 → Q 20, rank 61) — Q 21
al-Anbiyāʾ continues the prophet-cycle (it carries the Ibrāhīm and Mūsā material), so the topic continuity
forward is marginally tighter.

## 6. Unified Architectural Score (`findings/phase-b-hypotheses/csv/h-new-840.json`)

Method: `UAS = z(|outlier|) + z(max_neighbor_TSP_cost) + z(|iʿjāz_signature|)`.

| Field | Value |
|:--|:--|
| **UAS** | **+0.1585** (rank **43 / 114**) |
| abs_outlier | 5.52 (from H-NEW-590 delta_pct) |
| max_cost | 0.06816 (the Q 19 → Q 20 seam) |
| abs_ijaz | 1.5068 (= |sig_A|) |

**Reading.** Q 20's UAS rank 43/114 places it in the **upper-middle** band. The score is carried almost
entirely by `abs_ijaz` (|sig_A| = 1.51, one of the larger magnitudes — note UAS uses the *absolute* iʿjaz
signature, so Q 20's strongly-*negative* sig_A contributes positively): Q 20 is architecturally distinctive
on the iʿjāz axis *by being far below average* (the monorhyme-paradox), not by being a structural hub. Its
outlier strength (+5.52) and max TSP cost (0.068) are both modest. Q 20 is NOT a top-UAS hub (top-10 are
Q 33, 1, 2, 9, 24, 12, 55, 10, 23, 17 — note Q 23, Q 20's FR-nearest-neighbor, is rank 9). Q 20's
architectural interest is **narrative-lexical** (the Mūsā-cycle hub role, F-06; the v 14 divine-self-reference
peak, F-05), not whole-surah-dispersion-extreme.

## 7. Lexical counts (computed; `scripts/Q020_F_06_musa_hub.py` tokenizer + close-read scan)

| Quantity | Value | Note |
|:--|:--|:--|
| Verses | 135 | `data/hafs-verse-counts.tsv` line 20 |
| Words (marks stripped) | 1,356 | computed |
| Letters (marks stripped) | 5,402 | computed |
| Distinct QAC roots | 324 | `data/morphology/root-index.json`, 837 root-tokens |
| Longest verse | v 40 (35 words) | the Mūsā-infancy-flashback verse |
| Verses containing الله (substring) | 6 / 135 | computed (Allāh is sparse — the surah leans on 1sg divine self-reference, not the name; cf. F-05) |
| Densest divine-self-reference verse | v 14 (density 0.5455, rank 1/135) | Q020-F-05 CONFIRMED |
| Mūsā-marker verse count | 31 / 135 (frac 0.2296, rank 2/114) | Q020-F-01 (NULL — Q 28 is rank 1 at 0.2614) |
| 2sg-address density | 0.04794 (65 tokens, rank 7/114, z = +0.75) | Q020-F-02 (NULL) |

## 8. Architectural-type classification

- **Outlier axis (H-NEW-590):** WEAK positive outlier (delta_pct +5.52, p = 0.48, NULL) — in-family with
  its {Q 17-23} long-Meccan-narrative neighborhood.
- **iʿjāz axis (H-NEW-750):** LOW structural-iʿjāz (sig_A rank 92/114) due to the monorhyme paradox
  (79.3% yāʾ → low fawāṣil entropy). Content-divergent (z_mean_content_distance +1.15).
- **UAS (H-NEW-840):** upper-middle (rank 43/114), carried by |sig_A| magnitude.
- **Net:** Q 20 is a **content-divergent, monorhyme-dominant long-Meccan narrative surah** whose
  distinctive empirical signatures are *narrative-lexical*: the Mūsā burning-bush cycle hub-role (F-06,
  z = +5.81) and the single densest divine-self-reference verse in the surah (F-05, v 14). It is NOT a
  whole-surah dispersion hub, NOT a structural-iʿjāz hub, and its muqaṭṭaʿ-family membership imposes no
  multi-axis cluster (F-03, 0/4).

## 9. Honest limits

- The phoneme 4-vector dimension labels are not annotated in `h-new-700.json`; only the raw 4-density
  values are reported, so the per-channel interpretation (emphatic/pharyngeal/sibilant/glottal) is left
  un-assigned here to avoid asserting an un-verified mapping.
- H-NEW-590's window for Q 20 is the symmetric ±3 neighborhood {Q 17-23}; the WEAK_OUTLIER classification
  is window-definition-dependent.
- FR distances are on QAC-STEM root distributions; a lemma or surface-token level would shift the neighbor
  list (rules-tuple sensitivity is bidirectional).
- "Allāh-substring = 6/135" counts the orthographic string الله only; the surah's divine reference is
  overwhelmingly carried by 1sg pronouns (انا, ـني) and *al-raḥmān* / *rabb*, which F-05 captures.

## 10. Cross-references

- [[h-new-111|H-NEW-111]] — FR matrix (Q 20 row); Mūsā-cycle co-members in top-10
- [[h-new-590|H-NEW-590]] — outlier-strength (Q 20 WEAK_OUTLIER, +5.52, NULL)
- [[h-new-700|H-NEW-700]] — rhyme (79.3% yāʾ) + phoneme dispersion-tails
- [[h-new-720|H-NEW-720]] — Q 19 → Q 20 → Q 21 mid-spectrum seams
- [[h-new-750|H-NEW-750]] — iʿjāz signature (sig_A rank 92/114, the monorhyme paradox)
- [[h-new-840|H-NEW-840]] — UAS rank 43/114
- [[h-new-2260-prophet-cycle-pericope|H-NEW-2260]] — Mūsā cycle PASS (z=+3.34); Q020-F-06 extends it

---

*All numerical values traced to on-disk JSON artifacts as cited. Computed 2026-05-30 (F-06 pipeline) +
2026-05-07 (F-01..F-05).*
