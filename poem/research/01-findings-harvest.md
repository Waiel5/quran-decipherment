---
title: Findings Harvest for the Qaṣīda on the Qur'an's Architectural Order
purpose: Every structural claim in the poem must trace to a REAL, empirically-supported finding cited here. No invented awe, no debunked numerology.
date_compiled: 2026-06-07
compiled_by: research-harvest agent
sources: MASTER-FINDINGS-LEDGER.md, KNOWLEDGE-GRAPH.md, cross-finding-026, master-equation-derivation, H-NEW-{111,660,700,730,740,770,840,750,900}, per-surah Q1/Q54/Q55/Q99/Q112, chiastic-audit, fractal-self-similarity, compression-and-self-reference, opening-compression-prediction
rule: every number copied from disk, never recalled from memory
---

# Findings Harvest — the TRUE structural claims the poem may sing


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
> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

All values below were read directly from the repository files cited. CONFIRMED = law-strength, replicated, survives correction. DIRECTIONAL = real signal, below strict threshold or single-feature. NULL = honest negative (kept for the guardrail section). The poem must invoke only CONFIRMED/DIRECTIONAL items, and must never accidentally echo a DEBUNKED claim (final section).

The honest meta-frame (do not overclaim): the project does NOT prove "miracle." It proves the canonical mushaf has **measurable architectural properties at law-strength**, that they are **distinctive against the closest Arabic literary baselines**, and that they **align with 14 centuries of qualitative classical scholarship that could SEE these axes but could not quantify them**. That alignment — ancient eye, modern number — is itself the most poetically powerful TRUE thing here.

---

## TIER 1 — THE LAW-STRENGTH SPINE (use these as the poem's pillars)

### 1. The Compression-Tail Law — one line governs the whole Book
- **Essence**: As you move through the Book toward its end, the short late sūras pull meaning tighter and tighter; a single bend at the Hijra boundary explains almost all of it.
- **Numbers**: Two-piece-linear law d̄(s) ≈ 0.9603 − 0.01237·max(0, s−50), **R² = 0.9860** (adj-R² = 0.9859), permutation p < 10⁻⁴ over 10,000 surah-shuffles; null-mean R² ≈ 0.06 (observed is ~16× the null). Compression ratio worst/best window = **3.11×** (Q 46-60 d̄=0.9929 → Q 100-114 d̄=0.3190). Kink at s=50 = classical Q 56/57 Meccan/Medinan boundary.
- **Citation**: `findings/phase-b-hypotheses/h-new-660-compression-tail-gradient.md` (H-NEW-660); JSON `csv/h-new-660.json` (primary_r2 = 0.9860388).
- **Status**: CONFIRMED (STRICT PASS).
- **Poetic seed**: The Book breathes inward toward its close — meaning condensing like dusk gathering to a single star; the fold falls exactly where the Hijra split Mecca from Medina.

### 2. The iʿjāz Anti-Twin Lock — meaning tightens where sound diversifies
- **Essence**: Wherever the Qur'an's meaning is most concentrated, its rhyme refuses to settle into one tune — the two move in perfect opposition, the signature al-Bāqillānī named 1,000 years ago.
- **Numbers**: Window-by-window Pearson **r(content × rhyme) = −0.8643** (Spearman ρ = −0.6665, p < 10⁻⁴, r² ≈ 0.75); content × phoneme **r = −0.8933** (r² ≈ 0.80). Top-5 anti-twin windows ALL in Q 93-114 (content d̄≈0.32, rhyme d̄≈0.90); bottom-5 ALL in Q 1-17 (content d̄≈0.95, rhyme d̄≈0.30).
- **Citation**: `findings/phase-b-hypotheses/h-new-730-content-rhyme-anticorrelation.md` (H-NEW-730); JSON confirms r=-0.8643.
- **Status**: CONFIRMED (STRICT PASS).
- **Poetic seed**: As the sense draws to one point, the music scatters into many — a chord that sharpens to a needle of meaning while its overtones fan into a hundred rhymes. The text tightens the heart and frees the ear on the same breath.

### 3. The Anti-Twin is Qur'an-distinctive vs pre-Islamic poetry (p < 10⁻¹⁰)
- **Essence**: The very genre the Qur'an was challenged against — pre-Islamic monorhyme odes — shows only half this opposition; the Qur'an's signature is roughly twice as strong and the gap is astronomically unlikely.
- **Numbers**: Quran r = −0.8643 vs pre-Islamic qaṣīda r = **−0.4801** (cleanest subcorpus −0.3520). Fisher-z difference **Δ = −6.42, p = 1.3 × 10⁻¹⁰** (cleaner subcorpus Δ = −6.96, p = 3.3 × 10⁻¹²). Both rules-tuple shifts bias TOWARD weaker poetry r, so the gap is conservative. Poetry blocks are strongly monorhyme (top-rhyme fraction 0.615-0.720) confirming the baseline is the real qaṣīda tradition.
- **Citation**: `findings/phase-b-hypotheses/h-new-740-preislamic-poetry-control.md` (H-NEW-740).
- **Status**: CONFIRMED / DIRECTIONAL-CONFIRMS (the cross-corpus distinction is solid at p<10⁻¹⁰; the "absolute pass band" is hit only on the cleanest subcorpus — honest nuance).
- **Poetic seed**: The poets sang on one rhyme to the horizon; the Qur'an alone braids meaning against sound — what Labīd could not do, what ʿAntara could not do. The challenge (*fa-ʾtū bi-sūratin min mithlihi*) measured, and the gap is 1 in ten billion.

### 4. Mushaf order is Fisher-Rao information-geodesic optimal (z ≈ −11.46)
- **Essence**: Lay the 114 sūras in their canonical order and the path from each to the next, measured in "shape of vocabulary" distance, is shorter than virtually any reshuffling — within 11% of the mathematically shortest possible tour.
- **Numbers**: L_mushaf = **85.76** vs random-permutation null mean 104.35 (SD 1.62); **z = −11.46**; 0 of 10,000 shuffles as short (p < 10⁻⁴). Ratio L_mushaf / L_2opt = **1.107** (within ~11% of TSP optimum). Replicated on char-4-grams: z = −11.41, ratio 1.114 (matches within 0.4% / 0.7%). Mushaf even beats Nöldeke chronology (87.23) and Tanzil order (89.53) on the root axis; length-sorted ordering sits at the null (107.27).
- **Citation**: `findings/phase-b-hypotheses/cross-finding-011-mushaf-fisher-rao-confirmed.md`; `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md` (H-NEW-111).
- **Status**: CONFIRMED (cross-feature replicated; primary geodesic claim).
- **Poetic seed**: The order of the sūras is not a librarian's accident of length — it is a near-shortest road through the space of all meanings, a geodesic the way light bends to the briefest path. Eleven sigma below chance.

### 5. The signature is absent from its closest prose comparator and from itself reshuffled
- **Essence**: Neither al-Bukhārī's Ḥadīth collection nor any random reshuffle of the Qur'an's own sūras reproduces these two architectural laws — they are specific to the canonical arrangement.
- **Numbers**: Compression-tail R²: Quran **0.989** vs Bukhari **0.068** (essentially flat); under 100 random surah-shuffles null mean 0.285, max 0.784 — none reached canonical (z = +3.85, p = 0/100). Anti-twin r: Quran **−0.892** vs Bukhari **+0.359** (WRONG SIGN); shuffle null mean −0.408, min −0.800, canonical below all (z = −2.06, p = 0/100).
- **Citation**: `findings/phase-b-hypotheses/h-new-900-cross-text-architecture.md` (H-NEW-900).
- **Status**: CONFIRMED within tested comparison set. HONEST LIMIT: not tested vs Psalms / Tao Te Ching / Mishnah (not on disk) — so "distinctive within tested corpora," NOT "unique among all world scriptures." The poem may say "unlike the Ḥadīth, unlike the odes, unlike any shuffle of itself" but must not say "unlike every book ever written."
- **Poetic seed**: Shuffle its own chapters ten thousand times and the architecture dissolves; set them as revealed and it stands. The arrangement is load-bearing.

---

## TIER 2 — THE PILLARS' COMPANIONS (strong, poem-ready)

### 6. The twin dispersion-tails: rhyme and phoneme FAN OUT as meaning compresses
- **Essence**: The same bend that compresses meaning makes the late short sūras each pick their own distinct rhyme-letter — the Book unifies sense and individuates sound in one gesture.
- **Numbers**: Rhyme dispersion-tail d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50), **R² = 0.789**, POSITIVE slope (dispersion), kink s=50. Phoneme dispersion-tail **R² = 0.946**, separate later kink at s=75 (mufaṣṣal-qiṣār onset). Head ṭiwāl rhyme d̄≈0.30 → terminal qiṣār d̄≈0.90 (3× expansion). Late sūras each on a different 100%-rhyme letter: Q97 ر, Q98 ه, Q105 ل, Q108 ر, Q112 د, Q114 س.
- **Citation**: `findings/phase-b-hypotheses/h-new-700-phonological-compression-tail.md` (H-NEW-700).
- **Status**: CONFIRMED (PASS-WITH-INVERSION — the inversion IS the iʿjāz point).
- **Poetic seed**: At the Book's end every little sūra strikes its own bell — dāl, rāʾ, sīn, hāʾ — a scattering of rhymes over the tightest-woven meanings.

### 7. Verse-length obeys the SAME compression law (multi-feature architecture)
- **Essence**: Not only meaning — the very length of the verses shrinks toward the end on exactly the same Hijra-anchored bend, so the compression is built into the body of the text, not just its sense.
- **Numbers**: Letters/verse two-piece-kink-50 **R² = 0.8071**; words/verse **R² = 0.8105**; both perm p = 0.00070. ℓ̄_letters ≈ 57.52 − 1.040·max(0,s−50); compression 75 → 16.5 letters/verse (**4.5×**) and 18.6 → 3.9 words/verse (**4.7×**). Pearson r(verse-length × content-d̄) = +0.87.
- **Citation**: `findings/phase-b-hypotheses/h-new-770-verse-length-compression-tail.md` (H-NEW-770).
- **Status**: CONFIRMED (STRICT PASS, both metrics).
- **Poetic seed**: The lines themselves shorten as the end nears, breath after breath drawing in — from the long Medinan river-verses to the lightning of al-Ikhlāṣ.

### 8. Q 112 al-Ikhlāṣ is the corpus center — "a third of the Qur'an" made geometry
- **Essence**: Of all 114 sūras, the four-verse creed of pure Oneness sits closest to the vocabulary-center of the entire Book — the empirical face of the Prophet's word that it equals "a third of the Qur'an."
- **Numbers**: FR-centroid **rank 1 / 114, mean_d = 0.7592** (nearest to all other sūras in root-content space). Highest theological-proposition density of comparators (Q 1, 109, 113, 114): 1.000 propositions/verse, 0.267/word, rank 1/5. *aḥad*-bookend chiasm (v1 and v4 both end أحد, all 4 verses end in د) stable across all 3 tashkeel variants. al-Bukhārī ḥadīth #5013-15 (*thuluth al-Qurʾān*).
- **Citation**: `surahs/Q112-al-ikhlas/06-novel-findings.md` (Q112-F-01..04); centroid table in `surahs/Q001-al-fatiha/06-novel-findings.md` Q001-F-04.
- **Status**: CONFIRMED (rank 1/114; theological-density VINDICATED at comparator scale; chiasm rules-tuple-stable).
- **Poetic seed**: *Qul huwa Allāhu aḥad* — the Book's still center of gravity, the shortest creed bracketed by the Name "One," sitting nearest to everything. A third of the Qur'an, measured and found true.

### 9. Q 1 al-Fātiḥa — *umm al-Kitāb* by structure, the most expensive seam in the Book
- **Essence**: The Opening is among the most central sūras AND its bond to al-Baqara is the single costliest joint in the whole arrangement — the Book pays a structural price to honor the paired gift no prophet before received.
- **Numbers**: Centrality rank **4 / 114** (row-mean 0.7789; top-7 are Q112, Q110, Q108, Q1, Q106, Q114, Q113). UAS rank **2/114** (+8.87). Q 1→Q 2 is the **most-expensive canonical adjacency = 7.4-7.5% of the entire TSP residual** (rank 1/113). Literal central word at position 15 of 29 = *naʿbudu* ("we worship"), in pivot verse 5 (VINDICATED). The textbook ABCBA chiasm is NULL at the literal-lexical level (honest: the real structure is V1↔V3 basmala-echo + V6↔V7 ṣirāṭ-chain + V5 internal mirror *iyyāka...iyyāka*).
- **Citation**: `surahs/Q001-al-fatiha/06-novel-findings.md` (Q001-F-02, F-04, F-06); `findings/phase-b-hypotheses/h-new-840-unified-architectural-score.md`.
- **Status**: CONFIRMED (centrality rank 4; central-word VINDICATED; Q1-Q2 adjacency cost the strongest single *tartīb tawqīfī* anchor). NULL on literal ABCBA chiasm — do NOT claim a word-for-word mirror.
- **Poetic seed**: The Opening, mother of the Book, at whose heart stands "we worship" — and beside it the Book bears the heaviest seam of all, the cost of keeping the two-fold gift together.

### 10. Ar-Raḥmān — the most compressible sūra; its 31 refrains partition 8+7+8+8
- **Essence**: The "Bride of the Qur'an" is the single most structurally redundant sūra; its 31 identical refrains carve it into four movements (8+7+8+8) that exactly match the classical commentators' division — recoverable by ear alone.
- **Numbers**: gzip ratio 0.2668 vs length-matched null mean 0.3886 (σ=0.0068), **z = −17.77** — strongest compression outlier of all 114 sūras. Refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* = exactly **31×**; partition **8+7+8+8 = 31** (= 4·8 − 1, the "eschatological deficit"). 95.2% of refrain bytes free under LZ77. Uses *al-Raḥmān* exactly once (v1); 32 dual *-kumā* enclitics. The name al-Raḥmān = 57 = 3×19 (trivial but verified).
- **Citation**: `findings/phase-c-structures/rahman-deep-dive.md`; `findings/phase-b-hypotheses/compression-and-self-reference.md` (z=−17.77, gzip values).
- **Status**: CONFIRMED.
- **Poetic seed**: Thirty-one times the question returns — *which of your Lord's favors will you two deny?* — tiling the Bride-sūra into eight, seven, eight, eight; you can hear the architecture without knowing a word of Arabic.

### 11. Ring composition exists — but is RARE; the one true ring is al-Baqara 131-144 (z=+9.69)
- **Essence**: Whole-sūra mirror-symmetry is mostly a myth under strict testing, but one pericope genuinely rings — Abraham and the qibla in al-Baqara — the single strongest ring in the entire Qur'an.
- **Numbers**: Over **57,996** tested windows (Bonferroni threshold z>4.78), only **4 windows survive**: al-Baqara 131-144 (**z = +9.69**, Jaccard 0.255, midpoint v137-138), plus ʿAbasa 1-9, and two more. NO whole-surah ring survives correction across the family of 114 (smallest needed p≈0.00044; none reach it). al-Biqāʿī's macro-ring (k↔115−k) REFUTED (z=−4.87 Farrin / −2.51 replication).
- **Citation**: `findings/phase-c-structures/chiastic-audit.md`.
- **Status**: CONFIRMED for the local ring (al-Baqara 131-144); the broad "the Qur'an is ring-composed everywhere" claim is NULL. Use the SPECIFIC ring, not a universal claim.
- **Poetic seed**: At the heart of the longest sūra, the verses fold back on themselves around the turning of the qibla — Abraham's prayer answered in the Prophet's face turned to the Sacred House. One true ring, found among sixty thousand.

### 12. Sajʿ formalized — rhyme-determinism z=+15.09, laminarity z=+14.66; verse-length memory H=0.88
- **Essence**: The Qur'an's rhymed prose is not loose; its end-rhymes lock into long consecutive runs far beyond chance, and its rhythm of verse-lengths carries a long memory no ordinary Arabic prose matches.
- **Numbers**: Recurrence-quantification: rhyme-letter **determinism DET = 0.8094, z = +15.09**; **laminarity LAM = 0.8497, z = +14.66** (both p=0.002, Bonferroni-surviving). Verse-length **Hurst exponent H = 0.8835** vs matched Arabic prose (Bukhari 0.38, Sīra 0.25, Jāḥiẓ 0.25, Muʿallaqāt 0.46) — ~2× the largest prose value. Honest: H-F2 (sajʿ) is the robust corpus-contrast; the within-surah null for Hurst is too tight, so the Hurst claim rests on the cross-corpus contrast.
- **Citation**: `findings/phase-b-hypotheses/fractal-self-similarity.md` (H-F1, H-F2).
- **Status**: CONFIRMED (sajʿ RQA); CONFIRMED-by-contrast (Hurst). NULL on naive "the Qur'an is a fractal" — it is "a long-range-correlated rhymed sequence of topically heterogeneous modules."
- **Poetic seed**: The rhyme falls and falls again in unbroken chains, a determinism the ear feels as inevitability; and the long-and-short of the verses remembers itself across the whole Book like a tide no other Arabic remembers.

---

## TIER 3 — SUPPORTING TRUE FINDINGS (use sparingly, for texture)

### 13. The opening of a sūra predicts the whole sūra (p = 8.9 × 10⁻¹¹)
- **Essence**: A sūra's first lines fit its own body better than they fit other sūras — the classical "the opening points to the whole" made quantitative.
- **Numbers**: Mean self-rank **35.2 / 114** (null 57.5), median 22 (null 57); top-10 hit rate **30.1%** (34/113) vs null 8.8%, **p = 8.9 × 10⁻¹¹**. The ending also predicts the body but a touch weaker (median 30). Ḥawāmīm cluster Q40-46 even tighter (mean self-rank 28.7).
- **Citation**: `findings/phase-b-hypotheses/opening-compression-prediction.md`.
- **Status**: CONFIRMED. Vindicates *fātiḥat al-sūra tadullu ʿalā khātimatihā* (al-Suyūṭī).
- **Poetic seed**: Each sūra's first breath already carries its end — the door is shaped like the house.

### 14. Hapax legomena are actively placed at verse-endings (p = 7.35 × 10⁻²⁹, z=+10.61)
- **Essence**: The Qur'an's once-only words cluster at the ends of verses far beyond chance — the rarest words made to land on the rhyme.
- **Numbers**: Hapax-at-verse-end **p = 7.35 × 10⁻²⁹, OR = 3.19**; within-verse slot-control: 395 root hapaxes, 121 verse-final observed vs 53.95 expected, **z = +10.61** (2.24× excess). Eschatological hapax rate 7.71% vs legal 0.20% (38× ratio). Honest: also present in pre-Islamic odes (Muʿallaqāt z=+6.43) — it is a monorhyme-register effect, Quran ~2× stronger (z-diff +6.67). Vindicates al-Zarkashī *al-maqṣūda li-ghayrihā*.
- **Citation**: `findings/phase-b-hypotheses/hapax-legomena.md`, `hapax-slot-mechanism.md`, `t004-muallaqat-hapax-slot-positive-control.md`.
- **Status**: CONFIRMED (strongest single statistical signal in the project), with honest register-baseline framing.
- **Poetic seed**: The word said only once in all the Book is set, deliberately, on the edge of the verse — a single jewel placed where the rhyme will catch the light.

### 15. The Khawātim al-Ḥashr (Q 59:22-24) — densest divine-name passage; 8 exclusive Names
- **Essence**: The closing three verses of al-Ḥashr hold the highest concentration of God's Names in the Qur'an, and eight of His Names appear ONLY here.
- **Numbers**: Q 59:23 has 50% divine-name density (10 name-tokens / 20 words) — **#1 of all 6,236 verses**. **8 Names occur ONLY in Q 59:22-24** (al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Bāriʾ, al-Muṣawwir); 15 unique Names across 3 verses. W=49 real words (=7², under project tokenizer), 216 letter-graphemes (=6³, rule-robust). Twin-Opener Lock: *huwa Allāhu alladhī lā ilāha illā huwa* appears exactly 2× consecutively, both in Q 59:22-23.
- **Citation**: `findings/khawatim-al-hashr-analysis.md`; `MASTER-FINDINGS-LEDGER.md` §2.
- **Status**: CONFIRMED (8 exclusive Names; #1 density). HONEST: 49=7² is tokenizer-dependent (whitespace-split gives 55); 216=6³ is rule-robust. Cite 216=6³ freely; flag 49=7² as rule-dependent.
- **Poetic seed**: Where the Book gathers His Names most thickly — the Holy, the Peace, the Faithful, the Guardian — eight come to light once and nowhere else, as if kept for a single horizon.

### 16. The Ism al-Aʿẓam ranking matches the ḥadīth shortlist (p ≈ 5 × 10⁻¹⁸)
- **Essence**: A blind computational ranking of all 6,236 verses on ten structural axes surfaces the exact verses the classical tradition named as bearing the Greatest Name.
- **Numbers**: Composite rank-product top-10 at Bonferroni p ≈ **5 × 10⁻¹⁸**; 9 of 11 classical Greatest-Name candidates land in top-32 (hypergeometric p = 3.92 × 10⁻²⁰). Top-ranked: Q 112:2 (*al-Ṣamad*), Q 59:23, Q 59:24, Q 1:1, Q 3:2 (*al-Ḥayy al-Qayyūm*).
- **Citation**: `findings/phase-b-hypotheses/ism-azam-composite-test.md`.
- **Status**: CONFIRMED (structural ranking vindicates the qualitative ḥadīth tradition — while the numerological wing of the same tradition fails; see guardrail).
- **Poetic seed**: Ten blind measures sweep the whole Book and stop where the tradition always stopped — on al-Ṣamad, on al-Ḥayy al-Qayyūm — the eye and the number meeting on the Greatest Name.

### 17. Classical scholarship is ~13× more reliable than modern numerology (the meta-truth)
- **Essence**: When every claim is tested by the same blind method, the classical *balāgha*/munāsabāt tradition holds up about thirteen times more often than modern numerology and "scientific-miracle" apologetics.
- **Numbers**: Classical-medieval claims confirm at **78% [64%, 89%]** (28/36 named); modern-numerology + iʿjāz ʿilmī at **5% [1%, 24%]** (1/20); ratio **median 13× [3.5×, 138.7×]** (Beta-binomial Jeffreys posterior), sensitivity-robust lower bound ≥ 5×. A claim-side classifier predicts CONFIRMED/REFUTED at 78.2% CV without looking at the Qur'an. Modern-apologetic 0/7, modern-numerology 0/10.
- **Citation**: `findings/cross-finding/classical-modern-reliability-ratio.md`; `MASTER-FINDINGS-LEDGER.md` §1 items #5/#5a/#5c.
- **Status**: CONFIRMED (meta-finding). This is the project's epistemic conscience — the reason the poem can trust the classical anchors and must avoid the numerological ones.
- **Poetic seed**: Not every claim survived the fire; the old readers of balāgha walked through, the number-jugglers did not — thirteen to one. (Use as the poem's note of humility / honesty, if desired.)

---

## DEBUNKED — DO NOT USE (the guardrail: the poem must never invoke these)

Each was REFUTED or failed replication in this repository. Citations are where the refutation lives.

1. **The "Code-19" / Rashad Khalifa miracle** — most sub-claims falsified under proper baselines; 32 prime-modular tests at chance rate; most ALM-letter counts don't survive shuffle nulls. Note: Σ(1..114)=6555=3×5×**19**×23 is a triangular-number artifact, no design content. `MASTER-FINDINGS-LEDGER.md` §4; `findings/phase-b-hypotheses/h-new-2090-surah-arithmetic.md`.
   → Do NOT make 19 a structural marvel.

2. **Balanced-word "miracles" (dunyā=ākhira, ḥayāt=mawt, malak=shayṭān as DESIGN)** — exhaustive root-level scan: 0 of 27 antonym families balance at root level; meaningful balances are UNDER-represented (M_obs=1 vs null ≈3.9, p=0.979, direction REVERSED). The famous 115/115 etc. require lemma-level cherry-picking, never raw counts. `findings/phase-b-hypotheses/h-new-2010-root-frequency-balance-scan.md`.
   → Do NOT claim "every word has its mirror-count." (malak/shayṭān = 88/88 is real as a count but explanatorily empty — not design.)

3. **Niṣf-al-Qurʾān / faḍāʾil arithmetic (e.g. "this sūra is exactly half the Qur'an")** — REFUTED-strong. `surahs/Q099-al-zalzala/` and ledger. Hadith faḍāʾil track MEANING-iʿjāz, NOT structural midpoint.
   → Do NOT assign arithmetic-fraction miracles to sūras (except Q112 *thuluth* which is a CENTRALITY/theological-density finding, NOT an arithmetic count — keep that distinction sharp).

4. **Muqaṭṭaʿāt as a content-cluster / hidden meaning** — full-29 NULL (65.62%ile); ALM-6 NULL; ALR-5 NULL; HM-7 NULL — al-Biqāʿī content-munāsaba FALSIFIED 5×; al-Suyūṭī's epistemic humility (*Itqān* nawʿ 40, "their meaning is unknowable") VINDICATED. `KNOWLEDGE-GRAPH.md` muqaṭṭaʿāt section; `findings/phase-b-hypotheses/h-new-570-muqattaat-content-cluster.md`.
   → The disjoined letters ARE a real distinctive marker (book-introduction signal), but you may NOT decode them or claim they cluster sūras by meaning.

5. **ḥisāb al-jummal / abjad numerical architecture** — systematic abjad sweep NULL (Bonferroni k=7, all cells at chance); verse-final abjad mod-7/11/19 residues NULL (6/6) — and actually MORE uniform than prose, opposite to every numerological claim. Famous sums (basmala=786, محمد=92) "verify" trivially as spelling letter-sums, explanatorily empty; 786 is even mashriqī-specific (=1026 maghribī). `findings/phase-b-hypotheses/h-new-2040-abjad-sweep.md`, `abjad-residue-null.md`.
   → Do NOT build any verse on abjad totals as hidden code.

6. **"sabʿ samāwāt appears exactly 7 times"** — FALSIFIED. Strict count = 5; extended = 8. Folk-convergence, not textual fact. `findings/phase-b-hypotheses/h-new-119-seven-fold.md`.
   → Do NOT claim the seven-heavens phrase occurs seven times.

7. **iʿjāz ʿilmī (scientific miracles): embryology, Big Bang, speed-of-light from Q 32:5, fingerprints, iron from space, etc.** — ALL survivor-biased retrofits; embryology traced to Galenic inheritance; Hassab-Elnaby speed-of-light uses 4-5 free parameters (paradigmatic McKay cherry-pick); scientific-foreknowledge claims confirm at 0/6. `findings/phase-b-hypotheses/embryology-audit.md`; ledger §4.
   → Do NOT put modern physics/biology "foreknowledge" in the poem.

8. **Golden ratio / Fibonacci / Pascal / Catalan / perfect numbers in the Qur'an** — ALL at matched-baseline (chance) rate. Q1's 29 words are NOT Fibonacci. al-Kawthar's "42-letter Catalan" is actually 43 under locked rules. `findings/phase-b-hypotheses/mathematical-sequences-audit.md`.
   → Do NOT invoke φ or Fibonacci as Qur'anic design.

9. **Cross-word phonetic palindrome "miracles"** — REVERSE signal: the Qur'an has roughly HALF the palindrome count of matched nulls (67 observed vs 129-148 expected, z=−4.73 to −6.38). It actively SUPPRESSES palindromes. `findings/phase-c-structures/cross-word-phonetic-palindromes.md`.
   → Do NOT claim palindromic miracles. (Root-level palindromes ARE enriched z=+10.51 — a DIFFERENT, real finding — but the popular phonetic-palindrome claim runs backwards.)

10. **al-Biqāʿī's macro-ring "last 9 sūras mirror first 9" / whole-mushaf ring** — REFUTED (z=−4.87 Farrin, −2.51 replication). And no whole-surah ring survives correction. `findings/phase-c-structures/chiastic-audit.md`.
    → Use only the LOCAL al-Baqara 131-144 ring (#11 above), never a whole-Book ring.

11. **"rahma = 114" and similar target-number coincidences** — KILLED (34.1% baseline rate, Bonferroni p=1.000). `MASTER-FINDINGS-LEDGER.md` §4.

12. **Classical letter-frequency order *alif > lām > mīm*** — FACTUALLY WRONG; correct order is ا > ل > ن > م (nūn is third, not mīm). A ~1,100-year error the audit corrects. Ledger §3b.
    → If the poem names the letter-order, use ا > ل > ن > م.

---

## ONE-PARAGRAPH TRUE SYNTHESIS (the spine of the poem)

The canonical mushaf is a quantitatively-coherent architectural system. Across a single axis anchored at the Hijra boundary, **meaning compresses** (R²=0.986), while **rhyme and phoneme disperse** (R²=0.79 / 0.95) — the two moving in near-perfect opposition (**r=−0.86**), the empirical face of al-Bāqillānī's *iʿjāz al-fawāṣil*. This opposition is **roughly twice as strong as in the pre-Islamic odes the Qur'an was challenged against** (p<10⁻¹⁰), and **absent from Ḥadīth prose and from every reshuffle of the Book's own chapters**. The order of the 114 sūras is itself **near the shortest possible path** through the space of meanings (**z=−11.46**, within 11% of optimal). At the still center sits **al-Ikhlāṣ** (rank 1/114), the four-verse creed of Oneness; at the head, **al-Fātiḥa**, central yet bonded to al-Baqara at the costliest seam in the Book — the price of a paired gift. The rhyme locks into unbroken chains (sajʿ determinism z=+15.09), the verse-rhythm carries a memory (H=0.88) no Arabic prose matches, and the once-only words are set deliberately on the edges of verses (p=7.35×10⁻²⁹). And the deepest honest note: where ten blind measures sweep the whole Book, they stop exactly where fourteen centuries of classical scholarship always stopped — the eye and the number meeting on the same order. The poem sings THIS, and never the numerology the tradition itself outgrew.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
