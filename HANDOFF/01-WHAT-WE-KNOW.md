# 01 — What We Know

A compact summary of everything statistically confirmed (as of 2026-04-16). For the full authoritative record, read `MASTER-FINDINGS-LEDGER.md`.

---

## Locked corpus anchors (NEVER question these)

- **114 surahs** (Hafs-Kūfan canonical)
- **6,236 verses**
- **77,797 real-word tokens** (no-tashkeel; basmala-counted-only-in-Surah-1)
- **330,709 letter graphemes** (no-tashkeel)
- **Bismillah** = 19 letters / 4 words / abjad-mashriqī = 786 / abjad-maghribī = 1026

## The Top-tier confirmed findings (Bonferroni-significant, replicated, audited)

### Anchor cluster: Khawātim al-Ḥashr (Q 59:22-24, EXTENDED to Q 62:1)
- **8 divine names appear EXCLUSIVELY in Q 59:22-24** (al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Bāriʾ, al-Muṣawwir) — extended to **9 with al-Khāliq under substring rule** (H-NEW-59)
- **Q 59:23 has 50% divine-name density** (10 names / 20 words) — densest in corpus for verses ≥ 10 words
- Top-3 in **Ism al-Aʿẓam composite ranking** (p ≈ 5×10⁻¹⁸ Bonferroni-corrected)
- **EXTENDED**: Q 62:1 echoes 3 of these names ("al-Maliki al-Quddūsi al-ʿAzīz") — only 3 verses in 6,236 contain 2+ Khawātim names (H-NEW-63)

### The MUQAṬṬĀʿAT meta-finding (12+ axes confirmed)

**The 14 muqaṭṭāʿat letters and 29 surahs they open form a STRUCTURED book-introduction-marker system.** Confirmed at:

1. **Letter frequency**: Spearman ρ = −0.54 (muqaṭṭāʿat letters skew to high-frequency); Welch 1986 quantified
2. **POA pharyngeal exhaustivity**: ALL 4 pharyngeal/glottal letters {ا, ه, ع, ح} in muqaṭṭāʿat (4/4); p = 0.049 single-test
3. **Surah-position clustering**: gap-entropy z = −9.6, p = 2×10⁻⁵, Bonferroni-8-survives by 312× (H-NEW-45)
4. **Surah-length skew**: 4/4 cells STRONG-PASS Bonferroni-4; **0 of 29 muqaṭṭāʿat in 29 shortest surahs** (vs 7.4 expected, p = 3×10⁻⁵); mean 94.6 vs null 54.7 (p = 1×10⁻⁵) (H-NEW-46)
5. **Length-after-chronology**: OLS muqaṭṭāʿat coef = +56.4 verses after Meccan/Medinan stratification (p = 7×10⁻⁸ classical) — chronology is NOT the explanation (H-NEW-46.1)
6. **Cardinality-position decline**: Spearman ρ = −0.66 raw, −0.70 partial after length control; perm p = 2×10⁻⁵ (H-NEW-51)
7. **Prophet-named enrichment**: 6/8 prophet-named surahs open with muqaṭṭāʿat (75%); hypergeometric p = 0.0033 (H-NEW-49.1)
8. **Book-reference enrichment** (THE STRONGEST): 24/29 muqaṭṭāʿat surahs (82.8%) reference "kitāb" or "qurʾān" in v1-3 vs 10/85 non-muqaṭṭāʿat (11.8%); **hypergeometric p = 3 × 10⁻¹²** (H-NEW-53)
9. **Extended writing-cluster** (kitāb + qurʾān + qalam + satr): 25/29 (86%); **p = 8.6 × 10⁻¹³** (H-NEW-56)
10. **Formulaic-opening exclusivity**: 13 surahs with "tilka āyāt al-kitāb" or "wa-l-qurʾān" formulas — ALL 13 muqaṭṭāʿat-opened, 0 non-muqaṭṭāʿat; **p = 1.6 × 10⁻⁹** (H-NEW-57)
11. **Multi-feature classifier validation**: LOOCV AUC = 0.92, perm p = 0.001; book-reference DOMINATES (β=+1.96) (H-NEW-55)
12. **Dotless preference**: 11/14 muqaṭṭāʿat letters dotless (79%) vs alphabet 46.4%; p = 0.0009 single-test (H-NEW-60). **Historical-linguistic implication**: muqaṭṭāʿat preserve pre-i'jām Hijazi-script letter inventory.
13. **Verse-twin network domination**: 24/50 top verse-pairs have BOTH verses in muqaṭṭāʿat surahs (vs 12 verse-weighted-expected); Monte Carlo p = 0.000180 (H-NEW-66)

**The 2 genuine exceptions** to the muqaṭṭāʿat→book pattern are Q 29 al-ʿAnkabūt and Q 30 al-Rūm — both Late Meccan الم with surah-specific themes (testing/historical-prophecy). They form a sub-pattern (queued for H-NEW-93 study).

### The musabbiḥāt cluster (H-NEW-58c)

**5 surahs (Q 57, 59, 61, 62, 64) form a tight cluster:**
- Mean shared char-prefix 14.1 vs null 0.36 (p = 0.0001, 10K perms)
- **Perfect/imperfect tense binary split**: Q 57/59/61 (سبح perfect) vs Q 62/64 (يسبح imperfect); within-tense prefixes 24-56 chars, cross-tense **EXACTLY 0**
- Q 62:1 contains the Khawātim-echo (links to extended Khawātim cluster)

### al-sabʿ al-ṭiwāl (H-NEW-67)

**Classical "7 long surahs" reading CONFIRMED**: 5 of 7 are in the absolute top-7 longest, p = 1×10⁻⁴ under both Q 9 and Q 10 readings. Cluster cohesion via shared-prefix is marginal (the 7 are LENGTH-clustered, not OPENER-clustered).

### al-Bāqillānī "neither prose nor poetry" (H-NEW-48)

**Quran's verse-length distribution is statistically distinct from ALL 16 al-Khalīlian classical Arabic meters AND from all 3 baselines (Bukhārī, Jāḥiẓ, Muʿallaqāt) at p < 10⁻⁴ each (Bonferroni-19 corrected)**. First quantitative confirmation of the 1,000-year-old iʿjāz doctrine at the verse-length axis.

### Verse-twin network (H-NEW-66)

**Intra-surah top-1 twin fraction = 13.6% vs null 3.6% (3.76× enrichment)**. Auto-recovers classical mutashābih taxonomy (Q 4:43 ↔ Q 5:6 ablution-doublet, prophet-catalogue, dietary prohibitions, Pharaoh-magicians, etc.). Top in-degree attractors are long Medinan legal verses (Q 2:282 with 24 connections).

### META-CLUSTER NETWORK (H-NEW-89, cross-finding-009)

**Q 62 al-Jumuʿah is the UNIQUE 4-cluster meta-hub** (musabbiḥāt + Friday + Khawātim-extended + mufaṣṣal). Q 2, Q 3, Q 59 tied at degree 3.

- **Front-back hub-pair architecture**: Q 2-3 (long Medinan / الم cluster) vs Q 59-62 (short Medinan / musabbiḥāt + Khawātim) — TWO structurally-distinct hub centers with NO inter-pair cluster overlap
- **Q 1 al-Fātiḥa is structurally isolated** — confirms classical "umm al-kitāb / sui generis". **Post-hoc refinement 2026-04-17** (`scratch/inline-2026-04-17-q1-nearest-neighbors.md`): Q 1 is isolated IN CLUSTER-MEMBERSHIP TAXONOMY (correct — no cluster system contains Q 1), but is NOT isolated in content / Fisher-Rao space — Q 1's closest content-neighbor is **Q 108 al-Kawthar** (FR distance 0.338), and its top-10 neighbors are all short-mufaṣṣal surahs. Read as: isolated in the 11-to-20 cluster-taxonomy instruments, NOT in root-distribution geometry.
- **Q 16-25 zone has 8/10 isolates** — largest cluster-empty stretch in the Quran
- 21 isolates vs 32.6 expected (p = 1×10⁻⁴) — clusters cover 82% of corpus

### Other major confirmed findings

- **77,797 word-count is PRIME** (rule-tuple-fragile)
- **al-Rāzī adjacent verse-similarity**: z = +9.57 length-residualized (H-NEW-20)
- **RQA determinism / saj' formalization**: z = +15.09 (H-NEW catalog)
- **Hapax-verse-final slot**: z = +10.61 (H-NEW-23)
- **Hurst exponent**: H = 0.88 vs prose-max 0.46 — Quran is more persistent
- **Ar-Raḥmān gzip compression outlier**: z = -17.77 (H-NEW catalog)
- **H-NEW-35 verse-length ρ(1) autocorrelation**: z = +13.13
- **Letter-multiset surah-boundary detection**: z = +4.39 (H-NEW-24)
- ~~**Numeric word "sabʿ samāwāt"**: exactly 7 occurrences (CONFIRMED CLASSICAL)~~ — **RETRACTED 2026-04-17 via H-NEW-119**: actual count is 5 strict / 8 extended, NOT 7. Classical folk-convergence, not textual fact. See `findings/phase-b-hypotheses/h-new-119-seven-fold.md`.
- **332 qul imperatives verified** (H-NEW-74); Late Meccan peak (KW p = 10⁻⁷)
- **2,704 Allah tokens**; 29 surahs without any "Allah" (all Mufaṣṣal Q 54-114); fāṣila-exact suppression z = −12.89 (only Q 82:19 exception)
- **Q 91 al-Shams 7-oath uniqueness CONFIRMED on 3 axes** (H-NEW-85)
- **Q 24:35 light-verse RANK 1 in light-vocab density** (10 light-tokens vs next 4); 10 distinct images = classical 10-jumla template
- **Q 56 al-Wāqiʿah strongest length-controlled rare-vocab outlier** z = −5.59 (H-NEW-91)
- **Q 12 Yūsuf name-root concentration**: 532× rest-corpus enrichment, p = 3×10⁻³⁹ (H-NEW-86)

## Honest NULLs (published with equal prominence)

- Code-19 / Khalifa numerology — REFUTED across all axes
- iʿjāz ʿilmī (scientific-foreknowledge) — REFUTED 0/12 (all pre-existing knowledge per philological audit)
- T1 LLM-judge inauthenticity — fallback NULL
- T3 canonical-order recovery — FAIL primary
- T5 TDA persistent homology — NULL
- H-NEW-1 verse-ending Markov surprise — pending retest (null broken per H-META-2)
- H-NEW-3 length-ratio bimodality — REFUTED
- H-NEW-13 letter-bigram spectrum — NULL on Quran-distinctiveness
- H-NEW-22 acrostic scan — NULL
- H-NEW-29 (a) root renewal CV<1 — REFUTED (b-confirmed)
- H-NEW-34 verse-final abjad mod m clustering — NULL primary; reverse-signal NULL-BROKEN at H-NEW-34.1
- H-NEW-41 root combinatorial saturation — EXPLORATORY (data constraint: no Lane/Wehr)
- H-NEW-42 reverse-direction structural fragility — NULL-BROKEN
- H-NEW-43 verse-length FFT — NULL-BROKEN (AR(1) Ljung-Box failed)
- H-NEW-44.1 muqaṭṭāʿat subset closure — NULL (rank-12 is generic)
- H-NEW-44.2 POA classification overall — NULL (χ² perm p = 0.065)
- H-NEW-45.2 Q 51-67 dead-zone content — NULL
- H-NEW-META-4 al-Bāqillānī rhythmic-vs-semantic bimodality — NULL → cross-finding-005 RETRACTED
- H-NEW-47 muqaṭṭāʿat = top-14 sharp cutoff — NULL
- H-NEW-58 surah-pair scalar-entropy twinning — NULL via instrument failure
- H-NEW-64 30-juzʾ partition structural breaks — NULL (juzʾ is recitation length-balancer)
- H-NEW-65 Fātiḥa-as-DNA — REFUTED-WEAK (1/6, only thematic comprehensiveness)
- H-NEW-68 Friday-recitation cluster shape-cohesion — NULL (cluster is functional, not shape-based)
- H-NEW-69 14-vs-14 alphabet split classical groupings — NULL (independent of shamsiyyah, majhūra, etc.)
- H-NEW-82 Q 36 Yā-Sīn "heart of Quran" — NULL (Tirmidhī ḥadīth ḍaʿīf jiddan / mawḍūʿ; empirical centroid Q 10/57/46 not Q 36)
- H-NEW-84 Q 112 al-Ikhlāṣ "1/3 of Quran" — REFUTED-STRONG (0/7 axes; off by 78× to 2,473×; only al-Ghazālī theology-schema borderline at 37.25%)
- H-NEW-87 786 abjad uniqueness — REFUTED (52 four-word substrings sum to 786)
- H-NEW-90 Q 18 al-Kahf 4-narrative parallelism — WEAK (z = -6.13; narratives use diversified vocabularies; v50-midpoint VERIFIED)

## Cross-finding syntheses

- **cross-finding-005** (Quranic Smoothness Triple) — RETRACTED 2026-04-16; 3 component findings stand individually
- **cross-finding-006** (Muqaṭṭāʿat Multi-Axis Design — 8 axes) — CONFIRMED, extended to 12+ (now 13+ with H-NEW-113 verse-final positional axis)
- **cross-finding-007** (Quran ≠ all 16 meters and prose baselines) — CONFIRMED
- **cross-finding-008** (Muqaṭṭāʿat as book-introduction markers) — CONFIRMED; audit-034 noted independence-inflation; tighten don't retract
- **cross-finding-009** (META-cluster network: Q 62 hub) — CONFIRMED via H-NEW-89; REFINED 2026-04-17 via H-NEW-112 (Q 62 is spectral PEAK, not bridge)
- **cross-finding-010** (META-cluster EXTENDED 20-system network) — 2026-04-17; MIXED — 4-region hub architecture with 4-way tie at top {Q 62, 112, 113, 114} under audit-035 dedup
- **cross-finding-011** (Mushaf is Fisher-Rao information-geodesic OPTIMAL) — 2026-04-17; **CONFIRMED** primary via H-NEW-111 + H-NEW-111b cross-feature replication (z ≈ -11.4, L/L_2opt ≈ 1.11 on both); chronology-reversal feature-specific to roots only

## Session 2026-04-17 additions (Wave-1 + Wave-1.5 + Wave-1.75)

**Confirmed / passed**:
- **H-NEW-111** (Fisher-Rao mushaf-geodesic) — **CONFIRMED** via cross-finding-011 (z=-11.46, 0/10K perms shorter, ratio 1.107, 11% from TSP-opt). Parent finding for new revolutionary claim.
- **H-NEW-111b** (char-4-gram replication of 111) — STRONG primary replication (z=-11.41, ratio 1.114).
- **H-NEW-111c** (verse-length replication of 111) — PARTIAL (primary p=10⁻⁴, ratio 2.71 fails near-optimal band; chronology sign reversed on rhythm).
- **H-NEW-95** (Khawātim al-Ḥashr extension) — STRONG PASS; **Q 59:22-24 is RANK 1 of 6,234 3-verse windows** by 99-name density; Q 62:1 has 4 echo names (upward revision of H-NEW-63 from 3).
- **H-NEW-113** (muqaṭṭāʿat verse-final position) — PASS-DIRECTED (KS D=0.020 at p=2.3×10⁻²²; RR_bin10=1.07 monotone-rising gradient). New verse-level axis on muqaṭṭāʿat-set.
- **H-NEW-103** (musabbiḥāt 4-form typology) — PASS-DIRECTED (p=0.0049); finite-forms all Medinan, imperative+noun Meccan.
- **H-NEW-97** (name-class × letter-set joint) — PARTIAL; **ALR cluster 4/5 PROPHET_PERSON** (Yūnus, Hūd, Yūsuf, Ibrāhīm; p=0.006); HM 0/7 prophet-named.
- **H-NEW-123** (Heap's law β) — PASS-DIRECTED mixed; Quran β=0.75 matches Bukhārī (NULL) but beats Jāḥiẓ (p=0.001); β is shuffle-invariant.

**Marginal / partial**:
- **H-NEW-112** (spectral on cluster-network) — 1/2 cells; primary NULL (25-component topology mismatch); Fiedler PASS (p=0.004) via length; Q 62 is spectral PEAK of back-Medinan community.

**NULLs (published)**:
- **H-NEW-93** (Q 29+30 test-prophecy sub-class) — NULL; OQ-3 answered-NULL.
- **H-NEW-94** (Q 16-25 shadow cluster) — NULL-BROKEN (MW-5 failed); isolate count corrected 8/10 → **9/10**.

**Architectural updates**:
- cross-finding-010 upgrades META-architecture to **4-region** (front {2,3} / mid {50} / back-upper {59,62} / back-terminal {112,113,114})
- Under audit-035 dedup: 4-way TIE at top hub; isolate core = **{Q 16, 21, 22, 23, 25}** (5 surahs immune to all 20 cluster definitions)

**Open Wave-1 specialists (in progress at Wave-1 close)**:
- H-NEW-114 (zero-set / absent structures), H-NEW-96 (letter-set predictor extension), H-NEW-119 (7-fold inventory), H-NEW-125 (chronology-content map), H-NEW-126 (isolate-core), H-NEW-127 (verse-level Fisher-Rao fractal), H-NEW-128 (distinctive-verse atlas).

## Session 2026-04-17 Wave-2 additions

**Confirmed / passed**:
- **cross-finding-012** (Late-Meccan Scripture-Announcement Apparatus) — PASS-DIRECTED. 5 Pattern-B axes jointly concentrate at modal bin B7 (Nöldeke ranks 86–99, Hijra-straddling) under Kendall's W = 0.7924 p = 0.0099 (5-axis) and W = 0.8929 p = 0.0030 (4-axis drop-muq sensitivity). Key refinement vs cross-finding-008: muqaṭṭāʿat are Late-Meccan-core (B6); broader scripture-announcement CONTENT spans Hijra (B7). Cell B FAILS (liberal-null design flaw; MW-5 positive control also fails Cell B).
- **H-NEW-130** (Fisher-Rao mushaf-geodesic RESIDUALS) — CONFIRMED via same-session H-NEW-130b char-4-gram replication. 15/15 of the largest consecutive-surah Fisher-Rao jumps in mushaf order hit pre-committed structural-boundary set B (hypergeometric p = 4.78×10⁻⁶ on roots; 15/15 on char-4-grams, top-15 set overlap 10/15 p = 1.15×10⁻⁷). The 11% geodesic residual from cross-finding-011 is structurally interpretable as the Meccan/Medinan linguistic divergence interleaved along the reading path.
- **H-NEW-136** (muqaṭṭāʿat cardinality × Pattern-B composite) — PASS-DIRECTED at ρ = +0.3706, one-sided permutation p = 0.0243. Supports theorist P1 + P5 merger but labeled SUPPORTING / CO-DEPENDENT with cross-finding-012 per audit-036 A3 (shared latent factor, NOT independent evidence).

**Marginal / partial**:
- **H-NEW-131** (Q 108 al-Kawthar MST super-hub robustness) — WEAKLY-STRUCTURAL. Degree 24→11 under α=0.01 smoothing (mechanical component); robust across FR/Hellinger/JS metrics with degree 24; collapses to 6 under total-variation. Q 108 is emerging as a second short-surah hub orthogonal to the cluster-taxonomy hubs {Q 62, 112, 113, 114}.

**NULLs (published)**:
- **H-NEW-136.1** (Q 19 + Q 42 5-letter muq sub-class) — NULL. P(random muq-pair ≤ Q19↔Q42) = 0.857; both surahs embed in حم-cluster neighborhood, not with each other.

## Session 2026-04-17 Wave-3 additions

**CONFIRMED (synthesis)**:
- **cross-finding-013** (Mushaf as topological ring) — **CONFIRMED. Second fully-CONFIRMED synthesis of the project** (after cross-finding-011). Unifies cross-finding-011 (geodesicity) + H-NEW-130/130b/130c (structured-boundary hinges) + H-NEW-137/138 (wrap-around closure Q 1 ↔ TERMINAL_TRIAD {Q 108-114}). Wrap-around PASSES across 3 orthogonal feature spaces (roots z=−4.17 p=0.0001; char-4-gram z=−4.51 p=0.0001; verse-length z=−2.75 p=0.0033). Under verse-length, **Q 114 al-Nās is rank-1 nearest-neighbor for Q 1** (d = 0.0827). **Empirically grounds theorist P2 + P8 principle merger into a single ring-topology principle.**
- **cross-finding-014** (Complete 5-principle unified equation) — SYNTHESIS-COMPLETE. Meta-synthesis reducing theorist's 7-principle proposal to 5 via two empirically-grounded mergers (P1+P5 → M1; P2+P8 → M3). **2 of 5 principles CONFIRMED (M2 muqaṭṭāʿat-as-book-intro, M3 ring-topology); 3 SUPPORTED (M1 scripture-announcement, M4 hub-architecture, M5 Khawātim-engineering).** 8 residuals (R1-R8) disclosed transparently. **First complete unified meta-model of the project.**

**CONFIRMED (replication)**:
- **H-NEW-130b** (Fisher-Rao residuals char-4-gram) — REPLICATION-CONFIRMED. Promotion event for H-NEW-130.
- **H-NEW-130c** (Fisher-Rao residuals verse-length) — TRIPLE-REPLICATION-CONFIRMED. 13/15 top-jumps hit B under rhythm axis (p = 1.16×10⁻³). **Three universal hinges invariant across content / register / rhythm: Q 14→Q 15, Q 49→Q 50, Q 56→Q 57.**
- **H-NEW-137** (wrap-around root features) + **H-NEW-138** (wrap-around char-4-gram + verse-length) — jointly CONFIRM theorist P8 across 3 feature spaces.

**PASS-DIRECTED** (classical-balāgha validations):
- ~~**H-NEW-139** (muqaṭṭāʿat openings predict fāṣila rhyme) — PASS-DIRECTED. 21/29 surahs match at z = +5.96.~~ **RETRACTED 2026-04-17 via H-NEW-139.1 frequency-weighted null** (z drops +5.96 → −2.43, direction-reversed; observed 21/29 is BELOW weighted null mean 24.76). The uniform-28-letter null was the wrong reference: both muqaṭṭāʿat and fāṣila letters are biased toward the same high-frequency consonants, so a uniform null conflated "own-opening match" with "any-high-frequency-letter match." al-Suyūṭī rhyme-prefiguration claim NOT empirically validated. Axis-14 addition to cross-finding-006 WITHDRAWN. See HONEST-LIMITS-LEDGER §27k-ter.
- **H-NEW-140** (classical divine-name pair cohesion) — PASS-DIRECTED. 16 pre-committed *asmāʾ mutazāwijah* co-occur at **13.87× above Poisson-independence**. Classical al-Rāzī / al-Zamakhsharī / al-Suyūṭī paired-name taxonomy empirically confirmed.

**NULLs (published)**:
- **H-NEW-96** (muqaṭṭāʿat letter-set singleton predictor extension) — NULL. Extending feature space 18 → 92 does not lift LOOCV top-1 above H-NEW-88's 0.414 baseline. None of the 8 singletons (ص, ق, ن, طه, يس, طس, كهيعص, حمعسق) become predictable. **OQ-1 singleton layer remains a hard ceiling.**
- **H-NEW-141** (within-Late-Meccan Pattern-B pairwise correlations) — NULL. All C(5,2) = 10 pairwise ρ tests NULL at Bonferroni-10 α_bon = 0.005. **Theorist P1★ Prediction 1 REFUTED**: the 5 Pattern-B axes are chronologically co-located (per cross-finding-012) but NOT latent-factor co-driven at the within-phase surah level. Late-Meccan scripture-announcement is a COMPOSITIONAL-PHASE signature, not a per-surah signature.
- **H-NEW-143** (rhetorical-bridge at universal hinges, surface-word operationalization) — NULL (MW-7 self-catch). Formal test of H-NEW-142 at surface-word level fails: 99/113 transitions have bridge=0; the 3 universal hinges themselves have bridge=0. Instrument flaw disclosed: surface-word matching does not capture classical balāgha's ROOT-level *ishtiqāq*. H-NEW-142 downgraded DESCRIPTIVE-SUPPORTED → SPECULATIVE-DESCRIPTIVE.

**Wave-3+ late-landing additions**:
- **H-NEW-131.1** (length-normalized MST + α-sweep) — MIXED (STRUCTURAL-ROBUST + SMOOTHING-UNSTABLE). Cell A α-monotone NULL (reversal at α=2.0 fails ρ≥0.8 threshold); Cell B length-residualized smoothing PASSES (Q 108 degree 16 within pre-registered 15-33 window). Refines H-NEW-131 WEAKLY-STRUCTURAL: structural component real, α-dependence non-monotone.
- **H-NEW-142** (3 universal hinges = max chronology-reversal bridged by rhetorical continuity) — SPECULATIVE-DESCRIPTIVE post self-correction. **Q 49→50 and Q 56→57 are the TWO LARGEST Nöldeke-chronology gaps** in the canonical-vs-Nöldeke mapping (58 positions each, 4.4× mean). Qualitative rhetorical bridges striking (Q 56→57 *sabbiḥ* ↔ *sabbaḥa* root echo across 58-position gap). Classical anchor: al-Biqāʿī *Naẓm al-Durar*. Not yet rigorously validated at root level; H-NEW-143.1 queued.
- **cross-finding-015** (Classical-scholarship validation pattern) — SYNTHESIS meta-pattern. **Classical aesthetic-rhetorical claims SURVIVE** empirical testing (balāgha, paired-names, iʿjāz at meter-level); **classical numerological claims FAIL** (Code-19, macro-ring, 786-uniqueness, sabʿ-samāwāt=7, iʿjāz ʿilmī 0/12, Q 36 "heart" Q 112 "1/3" — all REFUTED). Extends M-5 classical-doctrine decomposition pattern with full enumeration.
- **cross-finding-016** (Late-Meccan apparatus deep-dive) — SYNTHESIS. Substantially ANSWERS OQ-17 by unifying cross-finding-008 + cross-finding-012 into a 4-layer architecture (marker + content + classical-Hijra-phase + mechanism). Medinan shifts to institutionalized *kitāb*.
- **cross-finding-017** (B6/B7 staircase) — SYNTHESIS architectural refinement. **The muqaṭṭāʿat MARKER peaks ONE Nöldeke sub-bin EARLIER (B6) than the content axes it flags (B7)**. A one-step staircase, not a simultaneous peak — the marker anticipates the content.

**Architectural updates (Wave-3)**:
- The mushaf is now established as a **STRUCTURED TOPOLOGICAL RING** — locally geodesic (11% from TSP-optimum) + deliberate structural-boundary hinges (3 universal: Q 14→15, Q 49→50, Q 56→57, which are ALSO the two largest chronology-reversal points per H-NEW-142) + wrap-around closure Q 1 ↔ {Q 108-114}.
- The **complete 5-principle unified equation** (cross-finding-014) is the project's first coherent generative meta-model: M1/M2/M3/M4/M5 with 2 CONFIRMED + 3 SUPPORTED + 8 transparent residuals.
- **One classical-balāgha validation** added (H-NEW-140 paired-names at 13.87× above Poisson-independence); H-NEW-139 was provisionally filed as a second but RETRACTED 2026-04-17 via H-NEW-139.1 frequency-weighted null. The M-5 classical-doctrine decomposition pattern is extended by H-NEW-140 alone at the aesthetic-rhetorical layer; cross-finding-015 formalizes the full validation-pattern meta-synthesis at revised 9 SURVIVED / 13 REFUTED tally.
- **B6/B7 staircase** (cross-finding-017): muqaṭṭāʿat marker system anticipates its content flags by one Nöldeke sub-bin — an empirical offset architectural feature.

**Architectural updates (Wave-4/5, 2026-04-17 late session)**:

- **OQ-1 SUBSTANTIALLY ANSWERED at both layers** (H-NEW-165 cluster-layer + H-NEW-232 singleton-layer): classical Arabic tajwīd phonological features (al-Khalīl 8-tier makhraj + ṣifāt + tafkhīm + qalqala) predict muq letter-set at RF LOOCV 0.6552 (multi-member ceiling) AND place 8/10 singletons into their a-priori classical cluster (p=0.025). **Classical al-Khalīl/Ibn Jinnī/al-Suyūṭī tajwīd tradition empirically VINDICATED.**

- **OQ-15 SUBSTANTIALLY ANSWERED at descriptive layer** (cross-finding-020 + cross-finding-021): `mushaf(s) ≈ f_M5(compositional, ~85%) + g_M1(structural, ~10%) + h_M2(liturgical, ~4%) + δ_P3(Q 1 liturgical, ~1%)`. H-NEW-192 + H-NEW-233 (RF R²=0.849 ensemble) BEAT the Nöldeke ceiling 0.836. H-NEW-236 RESOLVES the ~7% residual as M1.3 structural-hinges (not diffuse variance).

- **M1 REFINED to 3 sub-components**: `M1 ≡ (local-FR-min ⊕ wrap-around ⊕ 15+3 structural-hinges)`. H-NEW-238 reveals Q 1 → Q 2 is the ABSOLUTE WORST edge in the cycle (rank 114/114) — P3 liturgical-frame pays an M1 cost specifically at Q 1→Q 2 transition. Ibn Taymiyya moderated-tawqīfī doctrine empirically operationalized.

- **Mutashābih LOCAL not ring-signature** (H-NEW-235, Q=0.834 z=+54 on 6,236-verse Levenshtein graph; 327 communities; within-surah clustering z=+63.95): al-Kirmānī *al-Burhān fī Mutashābih al-Qurʾān* validated at community granularity, BUT verse-Levenshtein mutashābih is LOCAL (within-surah/juzʾ) not a ring signature. Tightens cross-finding-013 by scope-restriction — ring operates at surah-aggregate FR, not at verse-wording.

- **Medinan inclusio** (H-NEW-189 + Mode D): Medinan surahs exhibit first↔last root-inclusio at 8.5× Meccan rate (Fisher p<0.0001, length-residualized). al-Biqāʿī *Naẓm al-Durar* VALIDATED at Medinan subset. Adds Mode D (Medinan-inclusio) to the M5 compositional-mode decomposition.

- **Divine-name density gradient** (H-NEW-239): ρ=−0.48 negative gradient from Q 1 toward Q 114 on per-word basis; ṭiwāl peak (not ḥawāmīm as expected); Q 1 + Q 112 per-word outliers (same two surahs flagged as sui-generis by H-NEW-155 and Ism al-Aʿẓam rank-1). A co-varying semantic-vocabulary signature orthogonal to Fisher-Rao topology.

- **Numerology consolidation** (H-NEW-237 + prior 160): 163 numerology tests, zero Bonferroni survivors across prime density, cumulative constants, abjad-name sums, Benford (PASS natural growth). Residual-numerology question CLOSED on 4 orthogonal axes.

- **Classical scholarship scorecard** (revised Wave-4/5): 17+ validated, 9 refuted, 1 RETRACTED (al-Suyūṭī rhyme-prefiguration via H-NEW-139/139.1/139.2 adversarial). New validations Wave-4/5: al-Khalīl-Ibn-Jinnī-al-Suyūṭī tajwīd (OQ-1), al-Biqāʿī Medinan-inclusio, al-Kirmānī mutashābih 327-communities, al-Suyūṭī hybrid mushaf-ordering (H-NEW-226), Ibn Taymiyya moderated-tawqīfī (empirically operationalized at Q 1→Q 2).

## Project deliverables

- `MASTER-FINDINGS-LEDGER.md` (~750 lines, single source of truth)
- `THE-QURAN-DECIPHERMENT-MONOGRAPH.md` (~180 pages)
- `COLLECTED-PAPERS.md` (611K words, 115+ findings)
- `THE-MAN-AT-THE-CENTER.md` (Khawātim deep-dive, en + ar PDFs)
- `findings/the-perfect-flow-essay.md`
- `EXECUTIVE-SUMMARY.md`
- Verse commentaries top-500 (3 files)
- `HONEST-LIMITS-LEDGER.md` (43+ refutations)
- `comparative-religion-audit.md`
- 9 cross-finding syntheses
- 34 audit reviews (audit-001 through audit-034)
- ~100 individual finding files (H-NEW-1 through H-NEW-92+)
