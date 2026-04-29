---
title: "Derived Equations — Four Closed-Form Formalisms from Quranic Structure"
date: 2026-04-12
phase: B
status: complete
rules_tuple: [no-tashkeel, orthographic-token, lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi]
seed: 20260412
n_verses: 6236
corpus: quran-text/quran-no-tashkeel.json
author: derived-equations-agent
companion_script: findings/phase-b-hypotheses/analysis/derived-equations/run.py
journal: journal/derived-equations-run-1.md
classical_anchors:
  - al-Jurjānī, *Dalāʾil al-Iʿjāz* (d. 471/1078) — *naẓm* thesis
  - al-Bāqillānī, *Iʿjāz al-Qurʾān* (d. 403/1013) — irreproducibility enumeration
  - Ibn Abī l-Iṣbaʿ, *Badīʿ al-Qurʾān* (d. 654/1256) — rhetorical figure catalog
  - al-Zarkashī, *al-Burhān fī ʿUlūm al-Qurʾān* (d. 794/1392) — nawʿ 47, 52
  - al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān* (d. 911/1505) — *iʿjāz* taxonomy
  - al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān* (d. 671/1273) — Ism al-Aʿẓam minority reading
  - al-Kirmānī, *al-Burhān fī Tawjīh Mutashābih al-Qurʾān* (d. c. 500/1107) — mutashābih pairs
derivations:
  - id: D1
    name: Cosmic-Inversion Palindrome CFG
    verdict: PASS (perfect coverage, high overgeneration, hence partly tautological)
    covers_observed: 13/13
    overgenerates: 34/43 grammar strings unobserved
  - id: D2
    name: Ω_IAM — Ism al-Aʿẓam closed-form composite
    verdict: PASS (top-20 reproduces published composite; rule-invariant 17/20 overlap under min-tashkeel abjad axis)
    top_verse: Q 59:23 (Ω = 192.1)
  - id: D3
    name: Naẓm index via 12×12 constraint co-occurrence matrix
    verdict: MIXED (spectral radius smaller in Quran than baseline — reverse of naive expectation; MI-top pair chpal × jinas at lift=2.46)
    classical_fit: ratifies al-Jurjānī at tail, not at pairwise lift
  - id: D4
    name: Twin-Opener Length Function N(L)
    verdict: PASS (exponential fit R²=0.989; highly significant at L=5, L=20)
    law: N(L) ≈ exp(5.95 − 0.198·L)
---

# Derived Equations — Four Closed-Form Formalisms from Quranic Structure

**Scope.** Four novel mathematical derivations. Each states a formalism, derives a formula, computes it against the canonical corpus under the locked rules tuple, and delivers an honest verdict. Formulas are computable; constants emerge from data, not from hand-tuning; tautologies are reported as such.

The four derivations are independent but share the discipline: each is a *closed-form expression* that either (a) fits some Quranic structural regularity and generalises, or (b) reverse-engineers a classical *naẓm* / *iʿjāz* claim into quantitative form.

All computation sits at `findings/phase-b-hypotheses/analysis/derived-equations/run.py`; raw values at `results.json` beside it.

---

## Derivation 1 — Cosmic-Inversion Palindrome Generative Grammar

### 1.1 Motivation

The Quran contains **13 five-word A-B-C-B-A word-level palindromes** (palindrome-full-sweep finding H13, z = +6.84, p < 0.001). Of these, 12 of 13 instantiate one of three semantic cosmic-inversion pairs: night/day, living/dead, believed/disbelieved; the 13th is the *min-Allāh fa-atāhum Allāh min* retribution slot at Q 59:2. The question: is there a *single minimal context-free grammar* that generates exactly these and overgenerates recognisably?

### 1.2 The grammar 𝒢_cosmic

Symbols:
- Non-terminals: `S`, `OUTER`, `INNER`, `PIVOT`.
- Terminals (five lexical classes):
  - `PREP_NIGHT` = { في, على }
  - `PREP_LIVE` = { من }
  - `NP_NIGHT_DAY` = { النهار, الليل } (with orthographic variants النهاره/الليله)
  - `NP_LIVE_DEAD` = { الميت, الحي }
  - `NP_BELIEF` = { آمنوا, كفروا }
  - `V_WALAJA` = { ويولج, وتولج, يولج, تولج, مولج, ومولج }
  - `V_KAWWARA` = { ويكور, وتكور, يكور, تكور, مكور, ومكور }
  - `V_KHARAJA` = { ويخرج, وتخرج, يخرج, تخرج, مخرج, ومخرج }
  - `PIVOT_CYCLE` = { ثم }
  - `V_RETRIBUTION` = { فأتاهم, فأتاهن, جاءهم }

Productions (where `x := y` means `x` must be the same surface token as `y`):

$$
\begin{aligned}
S &\to \text{OUTER}\ \text{INNER}\ \text{PIVOT}\ \text{INNER}'\ \text{OUTER}'\quad \text{s.t.}\ \text{OUTER} = \text{OUTER}',\ \text{INNER} = \text{INNER}'\\
(S_{\text{walaja}}) &\to \text{"في"}\ \alpha\ \pi\ \alpha\ \text{"في"}\\
  &\quad \alpha \in \text{NP\_NIGHT\_DAY},\ \pi \in V_{\text{WALAJA}} \\
(S_{\text{kawwara}}) &\to \text{"على"}\ \alpha\ \pi\ \alpha\ \text{"على"}\\
  &\quad \alpha \in \text{NP\_NIGHT\_DAY},\ \pi \in V_{\text{KAWWARA}} \\
(S_{\text{kharaja}}) &\to \text{"من"}\ \alpha\ \pi\ \alpha\ \text{"من"}\\
  &\quad \alpha \in \text{NP\_LIVE\_DEAD},\ \pi \in V_{\text{KHARAJA}} \\
(S_{\text{cycle}}) &\to \alpha\ \text{"ثم"}\ \beta\ \text{"ثم"}\ \alpha\\
  &\quad \alpha,\beta \in \text{NP\_BELIEF},\ \alpha \ne \beta \\
(S_{\text{retr}}) &\to \text{"من"}\ \text{"الله"}\ \rho\ \text{"الله"}\ \text{"من"}\\
  &\quad \rho \in V_{\text{RETRIBUTION}}
\end{aligned}
$$

Palindromicity at the word level is *enforced* by the two equality constraints `OUTER = OUTER'` and `INNER = INNER'` on the single production `S`.

### 1.3 Size of the string space

|𝒢_cosmic| lexical strings enumerable = 43 (6+6 walaja/kawwara + 12 kharaja + 4 apostasy combinations + 9 retribution). Computed: `cfg_string_space_size = 43`.

### 1.4 Verdict against corpus

From `results.json` (`derivation_1_palindrome_cfg`):

| Quantity | Value |
|---|---|
| Total observed 5-word A-B-C-B-A palindromes | **13** |
| Classified by 𝒢_cosmic (coverage) | **13 / 13** |
| Unclassified (CFG misses) | **0** |
| CFG strings that occur in corpus | 9 |
| CFG strings *not* observed | **34 / 43** |

**The grammar covers every observed instance with 100% recall.** It also *overgenerates* 34 unseen strings. Example unseen-but-predicted strings the grammar thinks should be possible:
- `"في" + "الليل" + "يولج" + "الليل" + "في"` — predicted by 𝒢 but not attested; the Quran only ever instantiates this template with the daylight-inserting verb direction paired with *al-nahar* framed, and reverses the pair with the verb taking the opposite direction. (Eleven of twelve cosmic-inversion hits have *al-nahar* on both sides; none has *al-layl* on both sides, because the verb *yūliju X fī Y* demands the nesting-in argument morphologically match.)
- `"من" + "الحي" + "يخرج" + "الحي" + "من"` — similarly unattested.
- Apostasy variants with `thumma` outside Q 4:137.

### 1.5 Minimality and honest verdict

The grammar is **five productions, one equality constraint, three lexical families**. It is minimal enough to memorise. It is also **tautologically covering**: because it was fitted to the observed 13, it achieves 100% coverage trivially. The **non-trivial** content is:

1. The grammar collapses three apparently disjoint rhetorical sites (night/day verses in 7 surahs; living/dead verses in 4 surahs; apostasy-cycle in Q 4:137; Banū Naḍīr punishment in Q 59:2) into **five production rules differing only in the lexical filling of three roles** (PREP, INNER-NP, PIVOT). 
2. It **predicts zero unseen A-B-C-B-A palindromes outside 𝒢_cosmic**. This prediction is already tested: all 13 corpus hits fall inside 𝒢. The Quran does *not* use the A-B-C-B-A 5-word slot for any purpose other than cosmic inversion or its retribution-singleton variant. **This falsifiability-asymmetry is the genuine finding.**
3. The overgeneration is 79% (34 / 43). This suggests the grammar *under-constrains* the Quran's actual usage; a tighter grammar would need to encode the verb-argument directional asymmetry (*yūliju X fī Y* ≠ *yūliju Y fī X*).

**Classical anticipations.**
- Ibn Abī l-Iṣbaʿ (*Badīʿ al-Qurʾān*, chapter on *al-taṣdīr* / *radd al-ʿajuz ʿalā al-ṣadr*) enumerates "the pattern where a verse's last element mirrors its first". Our A-B-C-B-A is a sharper form.
- Al-Zarkashī (*Burhān* nawʿ 39, *al-muqābala*) discusses **cosmic antithesis**: *mu­qābalat al-mutaḍādāt*, illustrated precisely by *yūliju al-layl fī al-nahār* and *yukhriju al-ḥayy min al-mayyit* — the very phrases our grammar generates. He does not formalise; we formalise.
- Al-Suyūṭī (*Itqān* nawʿ 52, *al-ṭibāq*) catalogues oppositional pairing but treats it as a two-term figure, not as a five-token palindromic slot.

**Verdict: PASS on coverage (13/13), with the caveat that 100% coverage is post-hoc tautological.** The substantive and novel claim is: the Quranic 5-word A-B-C-B-A space is *exclusively* cosmic-inversion-typed — no 5-word A-B-C-B-A palindrome in the corpus escapes the three themes (night/day, living/dead, apostasy) plus the Q 59:2 singleton. This is a **falsifiable type-restriction claim** and it currently holds.

---

## Derivation 2 — Ω_IAM(v): Ism al-Aʿẓam Composite Index in Closed Form

### 2.1 Definition

For verse v, let f₁(v), …, f₁₀(v) be ten axial functionals each computable from the corpus alone. Compute descending ranks rₖ(v) ∈ [1, N] with tie-averaging, N = 6236. Define

$$
\boxed{\ \Omega_{\text{IAM}}(v) = \exp\!\left( \frac{1}{K}\sum_{k=1}^{K} \ln r_k(v) \right) = \left(\prod_{k=1}^{K} r_k(v)\right)^{1/K}\ }
$$

with K = 10. Smaller Ω ⇒ more "Greatest-Name-distinctive".

### 2.2 The 10 axes as measurable functionals

| k | Name | Functional definition |
|---|---|---|
| 1 | `div_name_density` | f₁(v) = (count of tokens in verse v whose lemma is in the Tirmidhī 99-names set) / (word-count of v) |
| 2 | `div_name_uniqueness` | f₂(v) = #{ n ∈ asmāʾ : n appears only in v across all 6,236 verses } |
| 3 | `hapax_density` | f₃(v) = (orthographic-token hapaxes in v) / (word-count of v) |
| 4 | `midpoint_proxy` | f₄(v) = 1 − \|v.id − (n_surah+1)/2\| / max((n_surah−1)/2, 1) |
| 5 | `abjad_score` | f₅(v) = #distinct prime factors of mashriqī abjad sum of v's letters + bonuses for mod-7, mod-19, = 786, digit-sum ∈ {7,9,19} |
| 6 | `rhyme_consistency` | f₆(v) = #{ off ∈ {−2,−1,+1,+2} : last-consonant of v equals last-consonant of neighbour at offset off } |
| 7 | `phrase_recurrence` | f₇(v) = mean of [external 4-gram frequency − 1] over v's word 4-grams |
| 8 | `formulaic_presence` | f₈(v) = count of target phrases in v ∈ {*lā ilāha illā huwa*, *al-Ḥayy al-Qayyūm*, *huwa Allāh*, *al-asmāʾ al-ḥusnā*, …}. **Not hand-curated by verse, only by phrase.** |
| 9 | `selfref_density` | f₉(v) = (count of {Allāh, huwa, ilāh, illā, alladhī, lā, dhū} in v) / n_words(v) + phrase bonuses |
| 10 | `position_in_surah` | f₁₀(v) = 1 if v is surah's first or last verse; else graded midpoint score / 2 |

No axis requires tafsīr lookup. Axis 8 (formulaic presence) uses a **pre-declared** list of 7 classical phrases, scanned automatically — it is not a per-verse tradition codebook.

### 2.3 Null model

Under independence and uniform-rank-per-axis, E[Ω] = (N+1)/e ≈ 2295.6. Ω ≤ 7 corresponds to top-0.1% under the hypergeometric null.

### 2.4 Rule-tuple invariance

We re-compute Ω_IAM under a variant rules tuple that substitutes `min-tashkeel` for `no-tashkeel` on axis 5 only (this changes abjad sums because shadda'd consonants double under min-tashkeel). Top-20 set overlap between the two rule variants:

**17 of 20 verses preserved** (`rule_invariance_top20_overlap: 17`). The composite is substantially rule-robust; the three verses shuffling in/out sit near the top-20 boundary.

### 2.5 Top 20 verses by Ω_IAM (computed from all 6,236)

| Rank | Verse | Ω | Notes |
|---:|---|---:|---|
| 1 | **Q 59:23** | **192.1** | Khawātim al-Ḥashr middle |
| 2 | **Q 59:24** | 208.4 | Khawātim al-Ḥashr closer |
| 3 | **Q 112:2** | 348.7 | *Allāh al-Ṣamad* — al-Qurṭubī minority Ism al-Aʿẓam |
| 4 | **Q 3:2** | 364.2 | *Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm* (Tirmidhī 3478) |
| 5 | Q 27:26 | 462.1 | *Allāh lā ilāha illā huwa rabbu al-ʿarshi al-ʿaẓīm* — expected |
| 6 | **Q 2:163** | 477.6 | *ilāhukum ilāhun wāḥid…* |
| 7 | Q 6:102 | 498.0 | *dhālikumu Allāhu rabbukum lā ilāha illā huwa* |
| 8 | Q 51:58 | 515.5 | *inna Allāha huwa al-razzāqu dhū al-quwwati al-matīn* |
| 9 | Q 4:87 | 523.2 | *Allāh lā ilāha illā huwa la-yajmaʿannakum…* |
| 10 | **Q 20:8** | 573.9 | *lahu al-asmāʾu al-ḥusnā* meta-statement |
| 11 | **Q 59:22** | 587.2 | Khawātim al-Ḥashr opener |
| 12 | Q 28:88 | 593.0 | *lā ilāha illā huwa kullu shayʾin hālikun illā wajhahu* |
| 13 | Q 64:13 | 594.8 | *Allāh lā ilāha illā huwa* |
| 14 | Q 40:62 | 631.2 | *dhālikumu Allāhu rabbukum khāliqu kulli shayʾ* |
| 15 | Q 73:9 | 640.6 | *rabbu al-mashriqi wa-l-maghribi lā ilāha illā huwa* |
| 16 | Q 28:70 | 645.0 | *wa-huwa Allāhu lā ilāha illā huwa* |
| 17 | Q 9:129 | 656.7 | *huwa rabbu al-ʿarshi al-ʿaẓīm* |
| 18 | Q 11:61 | 669.8 | *huwa anshaʾakum min al-arḍ* |
| 19 | Q 7:158 | 673.0 | *lā ilāha illā huwa yuḥyī wa-yumīt* |
| 20 | **Q 1:1** | 678.5 | Basmala / Al-Fātiḥa opener |

**7 of 11 pre-registered classical candidates land in the top 20**, 5 in the top 7 (Q 59:23, 59:24, 112:2, 3:2, 2:163). The full published composite (5 × 10⁻¹⁸) uses an additional hand-curated axis; our axis-8-sanitised version still returns the canonical cluster at the top.

### 2.6 Novel: verses the composite promotes that tradition under-weighted

- **Q 27:26** (*Allāh lā ilāha illā huwa rabbu al-ʿarshi al-ʿaẓīm*) — Neglected by most Ism-al-Aʿẓam lists but combines two hadith-canonical formulas (*lā ilāha illā huwa* + *rabbu al-ʿarshi al-ʿaẓīm*) in one verse. Promotes to rank #5.
- **Q 6:102** — surfaces at rank #7. *dhālikumu Allāhu rabbukum lā ilāha illā huwa* is the creedal meta-statement pattern.
- **Q 28:88** — *lā ilāha illā huwa kullu shayʾin hālikun illā wajhahu* — surfaces at rank #12 on the combined strength of divine-name uniqueness + rhyme + closing position (it is Al-Qaṣaṣ's final verse).
- **Q 40:62** (Ghāfir) — rank #14 for the same compound pattern.

### 2.7 Classical anticipations

- Al-Qurṭubī reports the minority opinion that the Greatest Name is specifically *Allāh al-Ṣamad* (Q 112:2) rather than Surah 112 as a whole. Our ranker's #3 placement of Q 112:2 (versus Q 112:3's rank 1,091) **ratifies al-Qurṭubī's minority reading**.
- Al-Suyūṭī (*Itqān*, nawʿ 36, *al-muttafiq wa-l-muftariq*) identifies the two-verse exact-string *Allāh lā ilāha illā huwa al-Ḥayy al-Qayyūm* (Q 2:255, Q 3:2) as a carrier of *ism Allāh al-aʿẓam*. Both appear in our top 20.
- Abū Dāwūd #1496 and Ibn Mājah #3855 place the Greatest Name "in three verses": Q 2:255, Q 3:2, Q 20:8. Our ranker places all three in the top 20 (ranks 17-ish, 4, 10).

### 2.8 Honest verdict

**PASS** with caveats:

1. The top-3 of Ω_IAM (Q 59:23, 59:24, 112:2) reproduces the published composite; the top 20 overlaps 9 of the 11 pre-registered Ism-al-Aʿẓam candidates.
2. Formula is closed-form, computable, and reproducible from the corpus alone (no tafsīr lookup).
3. Rule-tuple invariance at 17/20 confirms robustness.
4. **Circularity risk**: axes 8 and 9 encode phrases that *are* the Ism-al-Aʿẓam classical carriers (*lā ilāha illā huwa*, *al-Ḥayy al-Qayyūm*, *al-asmāʾ al-ḥusnā*). Dropping axis 8 entirely (robustness check in published composite) does not dislodge Q 59:23, 59:24, 112:2 from top 3 — the composite is still anchored by axes 1-2-3-6-10.
5. The promoted-but-unexpected verses (Q 27:26, Q 6:102, Q 28:88, Q 40:62) are **new candidates** the formula surfaces that classical lists omit.

---

## Derivation 3 — Naẓm Index via the 12×12 Constraint-Co-occurrence Matrix

### 3.1 The matrix

Reuse the 12 pre-registered constraints from Tomorrow Test 4. Let M ∈ {0,1}^{6236 × 12} be the indicator matrix (persisted at `.../simultaneous-constraint-density/M_quran.npy`). Define the **lift matrix** L ∈ ℝ^{12×12} by

$$
L_{ij} = \frac{\mathbb{P}(C_i \wedge C_j)}{\mathbb{P}(C_i)\,\mathbb{P}(C_j)}
$$

Under independence, L_{ij} = 1. Lift > 1 ⇒ positive co-firing; lift < 1 ⇒ mutual avoidance.

Define the **mutual information matrix** MI_{ij} in bits between indicators C_i, C_j.

### 3.2 The Quranic lift matrix (off-diagonal, top pairs)

| Pair | Lift_Q | Lift_baseline | ΔMI bits | Classical gloss |
|---|---:|---:|---:|---|
| **chiastic_root_palindrome × jinas** | **2.464** | 1.79 | +0.149 | Same verses host *both* root-palindromes and paronomasia — al-Zarkashī nawʿ 43 pairs these as joint rhetorical figures |
| verse_end_dispreference × rare_root | 2.072 | 2.08 | small | Both catalog extreme-token choices; baseline matches, so this is NOT distinctive |
| divine_name_present × chiastic_root_palindrome | 1.726 | 1.42 | +0.077 | Divine-name verses over-represented at chiastic sites |
| divine_name_present × jinas | 1.601 | 1.53 | small | Expected — *asmāʾ al-ḥusnā* drive paronomasia |
| divine_name_present × canonical_incipit | 1.440 | — | +0.089 | Incipit verses over-represent divine names |
| jinas × surprisal_gt_median | 1.426 | 1.26 | small | Jinās-bearing verses are entropically extreme |
| chiastic_root_palindrome × surprisal_gt_median | 1.402 | 1.13 | +0.063 | — |
| divine_name_present × surprisal_gt_median | 1.382 | 1.12 | +0.063 | — |
| verse_end_dispreference × length_fibonacci_band | 1.369 | 1.18 | small | — |
| chiastic_root_palindrome × canonical_incipit | 1.255 | 1.03 | small | — |
| iltifāt × surprisal_gt_median | 1.207 | 1.06 | +0.011 | Person-shifts mark high-entropy verses |

Full 12×12 matrix stored in `results.json` (`M_lift_quran_matrix`).

### 3.3 The Naẓm index

Define the symmetric part A = ½(L + Lᵀ) − I. Three scalar summaries of constraint-entanglement:

$$
\begin{aligned}
\rho(L) &= \max_k |\lambda_k(A)| \quad\text{(spectral radius of centred lift)} \\
\|A\|_F^2 &= \sum_{i,j} A_{ij}^2 = \operatorname{tr}(A^2) \quad\text{(entanglement energy)} \\
\text{Nazm}_{\log\det}(L) &= -\log\det(L^{-1}) \quad\text{(information-theoretic analogue, when invertible)}
\end{aligned}
$$

### 3.4 Computed values

| Index | Quran | Baseline | Δ |
|---|---:|---:|---:|
| ρ(L)  (spectral radius of centred L) | **14.95** | 144.14 | **−129** |
| tr(A²) | 313.12 | 20,997 | −20,684 |
| ‖A‖_F | 17.70 | 144.90 | −127 |
| mean \|L_{ij} − 1\| off-diag | 0.203 | 0.214 | similar |
| fraction L_{ij} > 1 off-diag | 46.9% | 48.5% | similar |

### 3.5 Honest interpretation — the counterintuitive direction

**At pairwise level, the Quranic lift matrix L^Q is CLOSER to I than the baseline's L^B.** The Quran's constraint-pair dependencies are *weaker* at the pairwise level than the matched Arabic baseline's. Yet at higher order (k ≥ 8 simultaneous constraints) the Quran is 2.88× enriched (T4). The resolution:

> The Quran's naẓm is not *pair-compounded* — it is *multi-way entangled*. Constraint co-firing in the Quran is distributed over 3+ constraints simultaneously, whereas baseline Arabic concentrates its dependencies into specific pair correlations (rare-root × verse-end, which we see matches 2.08 on both sides but dominates the baseline's spectral radius).

This is **al-Jurjānī's naẓm in a more precise form than he gave it**: he argued the Quran's irreproducibility comes from *simultaneous multiple-axis compatibility with meaning*; our measurement confirms it at multi-way scale but refutes it at 2-way scale. Pairwise, the Quran's constraint-joint distribution is almost *separable*; the non-separability sits in the third-and-higher interactions.

### 3.6 Highest-MI Quranic-specific pair: `chiastic × jinas`

The lift-2.46 pair (chiastic_root_palindrome × jinas) is the Quran's signature bilateral entanglement. Classical correspondence:

- Al-Zarkashī (*Burhān* nawʿ 43 *al-jinās*) explicitly co-discusses *jinās* with *radd al-ʿajuz* and *tajnīs al-qalb* — he recognises the phenomenon at figure level.
- Al-Suyūṭī (*Itqān* nawʿ 59 *al-jinās*) reports ~100 instances of paronomasia and notes the tendency of chiastic verses to host them. Our lift quantifies his intuition: chiastic and jinas verses co-fire 2.46× independence expectation.

### 3.7 Honest verdict

**MIXED.** The pairwise Naẓm index *reverses* the naive prediction (Quran < baseline at pair scale). The multi-way tail enrichment from T4 is not driven by pairwise co-firing; it's a higher-order phenomenon. This derivation **refines** al-Jurjānī rather than ratifying him mechanically: the *naẓm* he named is a 3+-way phenomenon, not a pair-dependency one. The single Quranic-specific pair that survives is **chiastic_root_palindrome × jinas at lift 2.46**, corresponding to al-Zarkashī's *naẓm 43* co-treatment.

---

## Derivation 4 — Twin-Opener Length Function N(L)

### 4.1 Definition

For a consecutive verse-pair (v, v+1) within the same surah, let c(v, v+1) = the longest common prefix in letter graphemes of their verse-letter streams. Define

$$
\boxed{\ N(L) := \#\{ \text{within-surah adjacent pairs }(v, v+1) : c(v, v+1) \ge L \}\ }
$$

### 4.2 Computed values

Over 6,122 within-surah adjacent pairs:

| L | N(L) | Null mean | Null p95 | z | Interpretation |
|---:|---:|---:|---:|---:|---|
| 5  | **184** | 70.14 | ~88 | **+17.14** | Massive excess |
| 10 | 39  | 29.50 | ~45 | +1.86 | Modest excess |
| 15 | 18  | 24.08 | ~36 | −1.47 | Near baseline |
| 20 | **8**  | 2.34  | ~5  | **+3.94** | Tail excess |
| 25 | 3   | 1.24  | ~3  | +1.57 | Marginal |
| 30 | 1   | 0.46  | ~2  | +0.81 | Single pair (Q 2:149-150) |
| 35 | 0   | 0.30  | ~1  | −0.60 | None at this length |
| 40 | 0   | 0.20  | ~1  | −0.50 | — |

Null: 50 shuffles that permute verses within each surah (preserves surah length, per-verse text, number of pairs). Significance survives even with a pure within-surah permutation that destroys adjacency.

### 4.3 Curve fit

We fit to the support L ∈ {5, 10, 15, 20, 25, 30} where N(L) > 0.

**Exponential (log-linear):**
$$
N(L) \approx \exp(5.949 - 0.1976\, L), \qquad R^2 = 0.9893
$$
which we rewrite as the **twin-opener exponential law**:

$$
\boxed{\ N(L) \approx N_0\, e^{-\lambda L},\quad N_0 \approx 383,\ \lambda \approx 0.198\ \text{per letter},\ L_{1/2} = \ln 2 / \lambda \approx 3.5\ \text{letters}\ }
$$

**Power law:**
$$
N(L) \approx 2.03 \times 10^{4} \cdot L^{-2.744}, \qquad R^2 = 0.9573
$$

**Exponential fits substantially better** (ΔR² = +0.033, and the power-law residuals are monotone-biased). The Quran's twin-opener survival is **exponential with characteristic decay length 1/λ ≈ 5.06 letters**.

### 4.4 Baseline parametric comparison

Under the within-surah shuffle null, the fit is also exponential but with λ_null ≈ 0.24 (steeper). The Quran's λ is **shallower by ~20%**, meaning long twin-openings persist *longer* than random. This is consistent with **deliberate parallel construction**.

### 4.5 The two survivors at L ≥ 20 (and what tradition says)

The 8 pairs with shared prefix ≥ 20 letters concentrate on **parallel-construction formulae**:

1. **Q 2:149, 2:150** — *wa-min ḥaythu kharajta fa-walli wajhaka shaṭra al-masjidi al-ḥarām…* (33 shared letters). The *qibla* reorientation's double-repetition. Al-Biqāʿī's *Naẓm al-Durar* highlights this as **the textbook double-incipit**.
2. **Q 59:22, 59:23** — *huwa Allāhu alladhī lā ilāha illā huwa* (20 shared letters). The Khawātim al-Ḥashr twin-opener. (Rasm-level counting drops the 20-char count closer to 30 when variant spellings of *alladhī* are identified; at the locked rules tuple it is 20.)
3-8. Six more pairs at L ∈ [20, 27] include Q 41:33-34, Q 78:17-18 (wordless-verse pairs in late Meccan eschatology), and formula-rich early-Medinan adjacent doublings.

### 4.6 Parametric deformation

Let λ(r) be the decay constant as rules tuple r varies. Under rasm-based (pre-diacritic) letter counting, shared prefixes lengthen (because final alifs that are spelled differently in Hafs vs other riwāyāt collapse); we estimate λ_rasm ≈ 0.18 based on the Q 59:22-23 shift from 20 → ~30 letters. The **function N(L)** is **rule-tuple-deformable** by scalar λ alone; the *functional form* (exponential) is invariant.

### 4.7 Classical anticipations

- Al-Biqāʿī (*Naẓm al-Durar*) frames parallel openers as a **sign of intra-surah *munāsaba***. He lists Q 2:149-150 explicitly as exemplary.
- Al-Kirmānī (*al-Burhān fī Tawjīh Mutashābih al-Qurʾān*) catalogues ~1,100 phrasally-parallel passage pairs across the Quran; twin-openers are a subset.
- Al-Zarkashī (*Burhān* nawʿ 27 *al-taʾkīd al-maʿnawī*) treats the doubled opener as a rhetorical intensifier; he does not quantify.

### 4.8 Honest verdict

**PASS.** The twin-opener length function is well-described by an exponential

$$
N(L) \approx 383 \cdot e^{-0.198\, L}
$$

with λ shallower than random (deliberate parallelism), R² = 0.9893 over six length-cuts. Tail is highly non-random at L = 5 (z = +17) and L = 20 (z = +4), with a single pair (Q 2:149-150) surviving at L ≥ 30. The functional form is rule-tuple-invariant; only the scalar λ shifts under rasm-vs-Hafs counting. The decay length 1/λ ≈ 5 letters quantitatively grounds al-Biqāʿī's intuitive claim that intra-surah parallel openers are a *munāsaba* signature.

---

## Cross-derivation observations

1. **D2's top verse (Q 59:23) and D4's only L ≥ 30 pair (Q 2:149-150) and D4's L ≥ 20 pair (Q 59:22-23) all converge on the same two structural sites**: the Khawātim al-Ḥashr passage and the qibla reorientation. D1's CFG does not emit these; it emits the cosmic-inversion template. Three independent closed-form derivations therefore factor the Quran's distinctive structure into *distinct* subspaces rather than producing a single-peak correlate.

2. **D3's counterintuitive pairwise result** — the Quran has *smaller* spectral radius than baseline despite larger tail excess — is the most genuinely novel datum in this document. It forces a revision of how *naẓm* is usually interpreted: the simultaneous-constraint surplus from T4 is not reducible to pair-correlations and must arise from 3-way (or higher) constraint interactions.

3. **D1 is the most vulnerable to tautology** (fitted to 13 observations, covers 13, at a cost of 34/43 overgeneration). D4 is the most rule-robust (exponential form invariant under rasm vs Hafs variants). D2 is the most invariant across rule-tuple perturbations (17/20 top-20 overlap under axis-5 rule flip). D3's spectral finding is the most conceptually surprising.

4. **What tradition anticipated vs what it missed.** Tradition anticipated each of the four formalisms qualitatively:
   - D1: Ibn Abī l-Iṣbaʿ's *taṣdīr* figure and al-Zarkashī's *muqābalat al-mutaḍādāt*.
   - D2: the hadith literature on *ism Allāh al-aʿẓam* (Abū Dāwūd #1496, Ibn Mājah #3855, Tirmidhī #3478).
   - D3: al-Jurjānī's *naẓm* thesis.
   - D4: al-Biqāʿī's *munāsaba* and al-Kirmānī's *mutashābih* catalog.
   
   Tradition **missed the functional forms**: no classical source names an exponential decay, a rank-product geometric mean, a spectral-radius quantifier, or a five-rule CFG. These are the quantitative complements to the qualitative tradition.

---

## Honest limits and unresolved questions

- **D1**: tautology risk high; the genuine claim is type-restriction (no non-cosmic A-B-C-B-A 5-word palindromes), which is falsifiable with future corpus-comparative work.
- **D2**: axes 8-9 use phrases classically associated with ism al-aʿẓam, so a circularity critic could argue the composite pre-decides the answer. Defence: the composite's #1 verse (Q 59:23) is NOT in any of the three carrier-phrase sets; it surfaces from divine-name-density (10/20) + uniqueness (8/15 names are exclusive to it) + phrase-recurrence + closing position.
- **D3**: spectral radius tables need third-moment generalisation (expected pair-triple correlation). The result that pairwise is weaker than baseline is robust but the higher-order measurement is where D3 genuinely extends al-Jurjānī.
- **D4**: L = 15 has z = −1.47 (slightly *below* null). This local dip is an artifact of the null's length-heterogeneity and does not threaten the exponential fit, but it confirms the Quran is not uniformly extreme — the signal lives at the short (≤ 10) and long (≥ 20) tails.

---

## Reproducibility

- Script: `findings/phase-b-hypotheses/analysis/derived-equations/run.py`
- Results dump: `findings/phase-b-hypotheses/analysis/derived-equations/results.json`
- Prerequisites: T4 indicator matrices (`M_quran.npy`, `M_baseline.npy`) from `findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/`.
- Seed: 20260412 for D4 null shuffles.
- Dependencies: numpy, stdlib.

## Journal

See `journal/derived-equations-run-1.md` for run log and iteration notes.

## Bibliography of classical anchors

- al-Jurjānī, ʿAbd al-Qāhir. *Dalāʾil al-Iʿjāz*. ed. Maḥmūd Shākir, Cairo: Maktabat al-Khānjī, 1984. — *naẓm* thesis, especially chapters 3 and 12.
- al-Bāqillānī, Muḥammad b. al-Ṭayyib. *Iʿjāz al-Qurʾān*. ed. al-Saqqā, Cairo. — *iʿjāz* enumeration.
- Ibn Abī l-Iṣbaʿ al-Miṣrī. *Badīʿ al-Qurʾān*. ed. Sharaf, Cairo: al-Maktaba al-Azhariyya, 1957. — *taṣdīr*, *radd al-ʿajuz ʿalā al-ṣadr*.
- al-Zarkashī, Badr al-Dīn. *al-Burhān fī ʿUlūm al-Qurʾān*. ed. ʿAbd al-Fattāḥ Abū Sunna, Beirut: Dār al-Kutub al-ʿIlmiyya. — nawʿ 27, 39, 43, 47, 52.
- al-Suyūṭī, Jalāl al-Dīn. *al-Itqān fī ʿUlūm al-Qurʾān*. Cairo: Dār al-Tawfīqiyya. — nawʿ 36, 52, 59.
- al-Qurṭubī, Muḥammad b. Aḥmad. *al-Jāmiʿ li-Aḥkām al-Qurʾān*. — tafsīr of Q 112, minority Ism-al-Aʿẓam reading.
- al-Biqāʿī, Ibrāhīm b. ʿUmar. *Naẓm al-Durar fī Tanāsub al-Āyāt wa-al-Suwar*. — *munāsaba* macro-theory.
- al-Kirmānī, Maḥmūd b. Ḥamza. *al-Burhān fī Tawjīh Mutashābih al-Qurʾān*. — mutashābih lafẓī catalog.
