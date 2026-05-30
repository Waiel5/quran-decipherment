# Q 71 Nūḥ — Novel Findings (pre-registered)

All tests pre-registered with SHA-256-locked pre-regs (embedded in the run scripts, verified at runtime), seed 20260509, equal NULL prominence. Pre-regs in `surahs/Q071-nuh/preregs/`; scripts in `surahs/Q071-nuh/scripts/`; results in `surahs/Q071-nuh/csv/`.

## Q071-F-01 — Is the dedicated Nūḥ surah the lexical CENTROID of the Nūḥ-pericope cycle? — **NULL**

**Pre-reg SHA-256 `e19913e96977f32ea95405ab399f69f992e774b68f33d331214e59d7b5cf996f` (runtime-verified). Bonferroni-2 α=0.025.**

Building on [[h-new-2260-prophet-cycle-pericope|H-NEW-2260]] (the Nūḥ-cycle of 6 pericopes cohered at z=+2.51, driven by ark/flood roots `flk`/`grq`/`njw`), this test asks whether Q 71 — the *only* whole surah named for and dedicated to Nūḥ — is the lexical hub (centroid) of that cycle.

- **Arm A (centrality rank) — NULL.** Mean pairwise root-Jaccard of each pericope to the other five (the MW-7 reproduction of the stored H-NEW-2260 Jaccards reproduces all 15 pairwise values to 1e-9):

  | rank | pericope | mean J |
  |:-:|:--|:--|
  | 1 | Q 7:59-64 | 0.21685 ← centroid |
  | 2 | Q 23:23-30 | 0.19685 |
  | 3 | Q 11:25-49 | 0.19035 |
  | 4 | Q 26:105-122 | 0.18128 |
  | **5** | **Q 71:1-28** | **0.14933** |
  | 6 | Q 54:9-17 | 0.14833 |

  Q 71 ranks **5 of 6** — the *briefest* retelling (Q 7:59-64) is the centroid, not the dedicated surah.
- **Arm B (length-matched random-anchor swap null, L=28) — NULL.** Q 71 centrality 0.14933 vs null mean 0.13650 (sd 0.03022, p95 0.17584); z=+0.424, p_perm=0.278.

**Verdict: NULL.** Q 71 is **FR-peripheral to the very narrative cycle it names** — a meaningful negative. The standalone Nūḥ surah develops *distinct* material (the night-and-day daʿwa appeal vv 5-9, the wealth/children rebuke, the five named idols v 23, the cosmological signs vv 13-20) rather than recapitulating the cycle's shared ark/flood core. This is a clean instance of the **scale-of-aggregation / title-density-independence family**: eponymy (the surah named *Nūḥ*) does NOT entail lexical centrality in the eponymous theme — the same dissociation H-NEW-1820 found for title-roots, here extended to *narrative-cycle* centrality.

## Q071-F-02 — Are the five named idols corpus-singletons clustered at Q 71:23? — **PASS-DIRECTED-STRONG**

**Pre-reg SHA-256 `f818bc8db586a1d708c873183bec5bfdd775f5a266aece4fddabd3bf28ed2947` (runtime-verified).** Rules-tuple: (Hafs-Kūfan, no-tashkeel, orthographic-token match, basmala-counted-only-in-Q1).

The five pre-Islamic deities named in Q 71:23 — *Wadd, Suwāʿ, Yaghūth, Yaʿūq, Nasr* — are tested for corpus-exclusivity.

- **4 of 5 are corpus-STRICT singletons, all co-located at Q 71:23**: Suwāʿ (سواعا), Yaghūth (يغوث), Yaʿūq (ويعوق), Nasr (ونسرا) occur **nowhere else** in the corpus. Joint-uniform-singleton H₀ probability = **4.12×10⁻¹²**.
- **Honest disclosure:** *Wadd* (ودا) is NOT a strict orthographic singleton — it recurs at Q 19:96 in the *lexical* sense "love/affection" (*sa-yajʿalu lahum al-Raḥmānu wuddā*). Wadd is therefore a CONTEXTUAL-singleton-deity, not a strict one.

**Verdict: PASS-DIRECTED-STRONG.** Q 71:23 is a corpus-EXACT lexical island: a single verse holding four hapax-legomenon proper nouns. This directly instantiates **[[h-new-2320-hapax-census|H-NEW-2320]]** (hapax concentration is a Meccan signature — these four are Meccan hapaxes) and **[[h-new-2330-lexical-burstiness|H-NEW-2330]]** (surah-defining vocabulary clumps within one surah/verse; the idol-names are Q 71's burst, analogous to *qamīṣ*→Yūsuf and *kahf*→al-Kahf). It also resolves the F-01 NULL: Q 71's lexical mass is in its *unique* daʿwa/idol vocabulary, not the shared cycle-core — which is exactly why it is peripheral to the Nūḥ-cycle centroid.

## Queued (pre-registered, not yet finalized)

- **Q071-F-03** — prophet-named-surah cluster cohesion (Nūḥ / Hūd / Ibrāhīm / Yūsuf / Muḥammad eponymous surahs).
- **Q071-F-04** — Q 70→71→72 transition geometry (the expensive Q70→71 seam vs the smooth Q71→72).
- **Q071-F-05** — prayer/petition-density (the surah's daʿwa-imperative texture).

These are pre-reg-only (SHA-locked) pending run; deferred to a follow-up to avoid post-hoc selection.

---

*Q071-F-01/F-02 finalized 2026-05-30 by Waiel Al-Shujaa. Eponymy is not centrality; the idols are an island. Bismillāhi al-Raḥmāni al-Raḥīm.*
