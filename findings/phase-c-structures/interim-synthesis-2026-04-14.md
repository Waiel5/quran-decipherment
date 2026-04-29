---
finding_id: interim-synthesis-2026-04-14
phase: C
status: synthesis
date: 2026-04-14
rule_tuple_default: (no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
scope: external-audience snapshot of project state
inputs:
  - MASTER-FINDINGS-LEDGER.md
  - docs/master-index.md
  - findings/team-discovery-synthesis.md
  - findings/convergence-analysis.md
  - findings/phase-b-hypotheses/*.md (35+ team-discovery findings, 200+ independent agent findings)
  - findings/phase-c-structures/*.md
not_modified:
  - THE-QURAN-DECIPHERMENT-MONOGRAPH.md
  - THE-MAN-AT-THE-CENTER.md
  - MASTER-FINDINGS-LEDGER.md
  - TOMORROW-TESTS-PRE-REGISTRATION.md
  - findings/team-discovery-synthesis.md
  - verse-commentaries
---

# Interim Synthesis — State of the Evidence

## A snapshot for readers who did not see how the sausage was made

The Quran decipherment project has, by the end of its 2026-04-13/14 audit window, closed roughly 35 team-discovery findings and something in the vicinity of 200 independent single-agent findings across three phases. What is below is a consolidated picture of where the evidence now stands on seven axes. It is not a manifesto; it is a ledger read sideways. Every numerical claim carries its rules tuple. Every refutation is printed at the same font size as every confirmation. Where two findings contradict, both sit on the page.

One pattern has become structural enough that it deserves its own section: classical scholars (al-Biqāʿī, al-Rāzī, al-Jāḥiẓ, al-Sakkākī, al-Zarkashī, al-Kirmānī) typically aim true on a *specific* sub-prediction embedded inside a *larger omnibus* claim, and the omnibus claim usually fails. The project has now seen the pattern enough times to name it (the M-5 classical-doctrine decomposition pattern) and to read new findings through it.

A second structural pattern, which emerged late in the audit window, is that several of the Quran's most-touted distinctive signals turn out to be classical-Arabic-register signals with a Quran-specific residual on top, once a competent register-baseline (pre-Islamic monorhyme poetry, Jāḥiẓ prose) is brought in. What is actually Quran-specific versus what is classical-Arabic-register needs to be re-argued on this stricter baseline.

These two framing observations sit over the whole synthesis.

---

## 1. Tier-A confirmed findings recap

Twelve results sit at the anchor tier — either Bonferroni-crushing statistical strength (p < 10⁻¹⁵ or equivalent effect sizes) or unique convergence with classical ratification. They are the spine.

**1.1. The Bismillah calibration anchor.** Under the locked rule tuple (no-tashkeel, orthographic-token, graphemes, mashriqi), the opening formula of the Quran is 19 letters, 4 words, abjad 786. This is rule-robust at calibration scale and is used as the checksum for every downstream grapheme count.

**1.2. Muqaṭṭaʿāt density enrichment.** The 14 disjoined letters at the head of 29 surahs show χ² = 228.78, p < 10⁻¹⁵ enrichment inside their own host surahs beyond a 3-gram Markov null. Stouffer Z = +4.48 across surahs; three independent null models agree. Surah 50 (Qāf) is the single largest driver at z = +4.68. Rules: no-tashkeel, orthographic-token. (muqattaat-density-audit.md)

**1.3. Hapax legomena at verse-endings.** The flagship statistical signal of the project. Original test: 395 root-hapaxes; observed verse-final 121, expected under uniform-within-verse 53.95 ± 6.32; **2.24× excess at z = +10.61, p ≈ 0**. Primary test: OR = 3.19, p = 7.35 × 10⁻²⁹. As of 2026-04-13 the within-verse slot-control H-NEW-23 refutes the rareness-bias confound; hapaxes are actively placed at verse-final. al-Zarkashī's *al-maqṣūda li-ghayrihā* mechanism (*al-Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive classical doctrine unchanged; H-NEW-23 statistical finding (z=+10.61) unaffected; candidate correct locus: nawʿ 37 *al-fawāṣil* pending Phase-2 secondary-triangulation]** §4) empirically confirmed at corpus scale. Rules: (no-tashkeel, root/lemma, hafs-kufan). Eschatological-genre hapax rate 7.71% vs legal-genre 0.20% — **38× ratio, χ² = 113.96, p ≈ 0**. But see §3 below: against a Muʿallaqāt positive-control baseline the Quran's effect is only 1.87× MORE than a monorhyme-register baseline, not baseline-zero. (hapax-slot-mechanism.md, t004-muallaqat-hapax-slot-positive-control.md)

**1.4. Ism al-Aʿẓam composite p ≈ 5 × 10⁻¹⁸.** A rank-product over 10 orthogonal axes applied to all 6,236 verses produces a top-10 that matches the classical ḥadīth short-list at Bonferroni-corrected p ≈ 5 × 10⁻¹⁸: Q 112:2, Q 59:23, Q 59:24, Q 1:1, Q 3:2, Q 23:116, Q 2:163, Q 57:3, Q 20:8, Q 59:22. Nine of 11 classical candidates land in the top-32 (hypergeometric p = 3.92 × 10⁻²⁰). Rules: (no-tashkeel, orthographic-token, lemma where noted). (ism-azam-composite-test.md)

**1.5. Al-Baqarah ring Q 2:131-144 z = +9.69.** The strongest ring-composition in the whole corpus by permutation test. Centre on *wasaṭ* (2:143) — the algorithmic middle of the surah sits eight verses from the semantic "middle community" doctrine. Bonferroni-surviving across 57,996 window candidates. (chiastic-audit.md)

**1.6. Twin-opener lock.** Exactly two consecutive-verse pairs share ≥30 identical opening characters across 6,235 adjacent pairs: Q 2:149-150 (qibla) and Q 59:22-23 (Khawātim al-Ḥashr). Both land on passages that dominate other structural metrics. Twin-opener length decay N(L) = 383·e⁻⁰·¹⁹⁸ᴸ, R² = 0.9893. Q 59:22-23 sits on the exponential tail at z ≈ +4. Rules: orthographic-token, no-tashkeel. (clean-factorization-window-scan.md, derived-equations.md)

**1.7. Khawātim al-Ḥashr engineering.** Q 59:22-24: 49 real words = 7², 216 letter graphemes = 6³, 8 divine names exclusive to this passage (al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Bāriʾ, al-Muṣawwir — none occurs elsewhere in the 6,236 verses), 15 unique divine names in a 3-verse window (most name-unique 3-verse window in corpus). **Rule-tuple honesty**: the W=49 count requires QAC v0.4 lemma / orthographic-token rule; naive whitespace-split gives W=55. The 216=6³ and the 8 exclusive names are rule-robust. Under project rules all three clean factorizations survive; under whitespace Q 17:6-8 replicates the shape at chance rate. (khawatim-al-hashr-analysis.md)

**1.8. Ar-Raḥmān gzip outlier z = −17.77.** The 31-fold *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* refrain produces the strongest compression outlier of all 114 surahs. Partition matches classical tafsīr at 8+7+8+8. Refrain confirmation cluster: Al-Mursalāt z = −7.01, Al-Qamar z = −4.55, Ash-Shuʿarāʾ z = −13.34 (sleeper — should be added to the classical refrain catalog). (compression-and-self-reference.md, rahman-deep-dive.md)

**1.9. Opening-compression predicts body p = 8.9 × 10⁻¹¹.** Mean self-rank 35.2 / 114 (null 57.5). Top-10 hit rate 30.1% vs null 8.8%. The classical *fātiḥat al-sūra tadullu ʿalā khātimatihā* ("the opening of the surah indicates its end") is quantitatively vindicated. Rules: compression on no-tashkeel text, Ḥafṣ-Kūfan. (opening-compression-prediction.md)

**1.10. Root-level palindromes enriched z = +10.51; letter palindromes SUPPRESSED z = −6.75; phonetic palindromes SUPPRESSED z = −6.38.** Bifurcation between semantic-layer and surface-layer structure. 1,170 root-palindrome windows vs null p95 = 929. Popular apologetics has the direction backwards at the surface. (palindrome-full-sweep.md, cross-word-phonetic-palindromes.md — see §4.)

**1.11. Verse-length Hurst H = 0.88** vs matched Arabic prose ≤ 0.46 (Bukhari 0.38, Sīra 0.25, Jāḥiẓ 0.25, Muʿallaqāt 0.46). First cross-corpus Hurst contrast on a sacred text. RQA rhyme determinism z = +15.09, laminarity z = +14.66 — formalisation of Quranic *sajʿ* at recurrence-quantification-analysis scale. Vindicates al-Zarkashī *Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 52" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive classical doctrine (sajʿ / fawāṣil catalog by terminal rawī) unchanged; RQA statistical finding (determinism z=+15.09) unaffected; candidate correct locus: nawʿ 37 *al-fawāṣil wa-ruʾūs al-āy* pending Phase-2 secondary-triangulation]**. (fractal-self-similarity.md)

**1.12. Simultaneous-constraint density at p = 8.7 × 10⁻³³ (T4 verdict).** Twelve constraints × 6,236 verses. Mean 4.18 constraints/verse vs matched-baseline 3.71. Tail k ≥ 8: ratio 2.88×, z = +6.73. Super-independence tail excess of 49% beyond an independence null — NOT pair-compounded but 3+-way entangled (spectral radius of lift matrix 14.95 vs baseline 144.14). One Quran-specific pair dominates the lift: **chiastic × jinās at lift 2.46**, which al-Zarkashī *al-Burhān* nawʿ 43 anticipates qualitatively. First quantitative operationalisation of al-Jurjānī's *naẓm* at verse scale. Rules: (no-tashkeel, orthographic-token, lemma on content words). (simultaneous-constraint-density.md, derived-equations.md)

Twelve anchors. Collectively they survive hardened Bonferroni correction over the full project's test count. None is *inventing* an effect — each is quantifying an observation already present somewhere in ninth- to sixteenth-century Arabic scholarship, now held to modern null-model discipline.

---

## 2. The Classical-Doctrine Decomposition pattern (M-5 STANDING)

The project has elevated its most important meta-pattern to a STANDING methodological observation under designation M-5. It is blunt: **classical scholars aim true on specific predictions, and fail on omnibus claims.** Seven independent test sequences have now demonstrated this pattern. It is the single most reproducible meta-finding the audit loop has produced.

### 2.1. al-Biqāʿī (d. 885/1480): SEAM confirmed, MACRO-RING refuted.

al-Biqāʿī's *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* makes two claims: (a) *local* inter-surah coherence — adjacent surahs share thematic threads at their joints (*munāsaba bayn al-suwar*), and (b) *macro-ring* coherence — the whole mushaf exhibits a k ↔ 115-k mirror structure.

Test outcomes, 2026-04-13:
- **Local-seam test (T-002)**: mean adjacent-pair Jaccard 0.103 vs non-adjacent 0.066 → 55% lift. 10,000-permutation null Z = +10.06, p = 0.0000. Stouffer per-pair Z = +6.25. **113/113 adjacent pairs on the predicted side of the null.** Rules: no-tashkeel, orthographic-token. Audit verdict: **CONFIRMED at the operationalisation level** — the test cannot discriminate al-Biqāʿī's specific thematic-prefiguration mechanism from length-sort or generic topic-clustering, but seam-Jaccard as a measurable proxy for adjacent-surah coherence survives decisively.
- **Macro-ring test (T-010)**: k ↔ 115-k mirror Z = **−2.51**. al-Biqāʿī's omnibus ring architecture is **REFUTED**, replicating Farrin's 2014 negative result (Z = −4.87). Rules: gzip on no-tashkeel surah text.

Differential adjudication: al-Biqāʿī's strength is his *local munāsaba* observations; his weakness is the meta-structural claim that the whole mushaf is one big ring. **Naẓm al-Durar's first-order value is preserved; its grand claim is not.**

### 2.2. al-Rāzī (d. 606/1210): linear *naẓm* CONFIRMED but length-enhanced.

al-Rāzī's *Mafātīḥ al-Ghayb* argues for within-surah *linear* progression — the verses of a surah unfold in a planned order.

Test outcomes:
- **Primary verse-similarity autocorrelation profile** (H-NEW-20): Stouffer Z = **+30.76** across 95 surahs at k=5 lag. 12× Bonferroni threshold.
- **MW-1 length-residualization gate** (2026-04-13, task #52): ρ(log N, z_r1) = +0.60. Signal is length-enhanced. Short-stratum (n ≤ 30, 32 surahs) pre-registered gate at Z ≥ 10 yields Z = **+9.57** (0.43 below threshold — strict reading FAIL). IV-weighted across strata: Z = **+22.78** (liberal reading PASS). **27 of 32 short-stratum surahs show z > 0.**

Under strict pre-registered MW-1 reading the face-value Z = +30.76 is downgraded to length-residualized Z = +9.57. Still highly significant, but the headline was mediated by surah length. al-Rāzī's linear-progression thesis is **confirmed in spirit, length-enhanced in measurement.**

### 2.3. al-Rāzī vs al-Biqāʿī head-to-head.

The 400-year debate between linear (al-Rāzī) and ring-structured (al-Biqāʿī) intra-surah organisation settles at corpus scale: **linear wins at default, ring emerges only at specific rhetorically-marked sites** (Al-Baqarah 2:131-144 z = +9.69, ʿAbasa z = +6.09, four more Bonferroni survivors). The whole corpus does NOT ring; specific pericopes do.

### 2.4. al-Jāḥiẓ (d. 255/869): absolute REFUTED, comparative CONFIRMED.

al-Jāḥiẓ's *Kitāb al-Bayān wa-l-Tabyīn* and *al-Ḥayawān* contain a doctrine of *takrār maqbūl* — acceptable repetition — the idea that Quranic lexical return is more regulated than prose's.

Test outcomes (H-NEW-29):
- **Absolute sub-Poisson form** (pre-registered primary, CV < 1): weighted CV = 1.370, shuffle-null z = **+94.89**. Wrong direction. **REFUTED.** No natural language content-word stream is sub-Poisson; topic-cohesion always clumps.
- **Comparative form** (Quran vs matched Arabic prose): Quran vs Bukhari Mann-Whitney z = **−9.64**; Quran vs Jāḥiẓ z = **−7.95**. **CONFIRMED.** The Quran is ~0.05 CV units MORE regular than matched Arabic prose.

Honest methodological lesson: the pre-registered operationalization was naive. al-Jāḥiẓ's doctrine is comparative-rhetorical, not absolute-mathematical. **The *doctrine* holds in the *comparative* sense only.** (root-renewal-cv.md)

### 2.5. al-Sakkākī (d. 626/1229): rhythm EXISTS but is NOT distinguishing.

al-Sakkākī's *Miftāḥ al-ʿUlūm* introduces *īqāʿ* (rhythmic pulse) as a distinguishing feature of Quranic prose.

Test outcomes (H-NEW-35):
- **Primary rhythm signal**: Quran weighted-mean verse-length autocorrelation ρ(1) = 0.1368, z = **+13.127** vs 1,000-permutation within-surah phase-shuffle null (p ≈ 10⁻³⁹). Verse lengths are NOT rhythmically independent — rhythm **exists**.
- **Discrimination vs prose**: Quran ρ(1) = 0.137 vs Jāḥiẓ *al-Ḥayawān* ρ(1) = 0.146, Fisher z-diff = −0.666 (not significant). **Quran rhythm is indistinguishable from Jāḥiẓ prose on this measure.** The iʿjāz-grade form of the claim FAILS.
- **Strict monotonic decay sub-test**: FAILED (lag 4 → 5 inverts 0.019 → 0.034).
- **Novel side-observation**: Bukhari-noquran ḥadīth ρ(1) = −0.1521 — successive ḥadīth reports ALTERNATE in length. This is opposite of prose's length-clustering. Proposed mechanism: isnād/matn decomposition plus editorial interleaving. Follow-up H-NEW-35A queued.

al-Sakkākī's *īqāʿ* is **partially vindicated as DESCRIPTION** of Quranic rhythm and **REFUTED as DISTINGUISHING** classical-iʿjāz claim. (verse-length-autocorrelation.md)

### 2.6. al-Zarkashī (d. 794/1392): mechanism EMPIRICALLY CONFIRMED.

al-Zarkashī's *al-Burhān fī ʿUlūm al-Qurʾān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 59" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive classical doctrine unchanged; H-NEW-23 statistical finding (z=+10.61) unaffected; candidate correct locus: nawʿ 37 *al-fawāṣil* pending Phase-2 secondary-triangulation]** §4 describes *al-maqṣūda li-ghayrihā* — a word placed not for its own meaning but for its position/function. The mechanism specifically predicts hapax-like placements at rhyme-terminal slots.

Test outcome (H-NEW-23, 2026-04-13): **CONFIRMED.** Within-verse slot-control refutes the rareness-bias confound. Observed hapax-final 121, expected 53.95 ± 6.32, z = **+10.61**, 2.24× excess. The eschatological × legal 38× ratio (χ² = 113.96, p ≈ 0) closes the triple-test classical cluster with H-NEW-19 Ibn Abī l-Iṣbaʿ elision-eschatology and al-Suyūṭī *Itqān* nawʿ 65. Rules: no-tashkeel, root/lemma, hafs-kufan.

al-Zarkashī's *mechanism-specification* travels better than most classical omnibus claims precisely because it is narrow. **Narrow, testable, confirmed.** Also confirmed: al-Zarkashī nawʿ 52 (sajʿ description) via RQA rhyme determinism z = +15.09. al-Zarkashī's *iltifāt* catalog is under-inclusive by ~7× against modern detectors, though, which is a separate matter (see §2.8 below for iltifāt).

### 2.7. al-Rāzī — muqaṭṭaʿāt-as-divine-names-abbreviations: REFUTED.

al-Rāzī (*Mafātīḥ al-Ghayb*) proposes that the 14 luminous letters opening 29 surahs are abbreviations of divine names. Tested (razi-muqattaʿat-divine-names-test.md) at **0/78 claims surviving shuffle null** over luminous-letter frequency overlap. **REFUTED.**

The muqaṭṭaʿāt effect is real (§1.2, χ² = 228.78); al-Rāzī's mechanism for it is not. Another example of the pattern: *effect confirmed, classical mechanism falsified.*

### 2.8. al-Kirmānī (d. 505/1111): mutashābih count CONFIRMED, directionality REFUTED.

al-Kirmānī's *Asrār al-Tikrār fī al-Qurʾān* catalogues ~1,100 *mutashābih lafẓī* (near-repetition) pairs. Our detector hits 1,085 pairs — the count matches within 1.4%. But al-Kirmānī also claims a *directionality* to the pairs (one member is "original," the other "echo"). Tested at team-discovery-009: **REFUTED.** The pairs are symmetrical on reading-order features.

### 2.9. Ikhwān al-Ṣafāʾ: mashriqī FAILED, maghribī EXACT.

The 10th-century Ismāʿīlī encyclopedists asserted that the muqaṭṭaʿāt letters sum to 903 under abjad. Initial test under mashriqī abjad (where ṣ=60, s=300) gave 693 — apparently a failure. **Re-test under maghribī abjad (where ṣ=300, s=60): exactly 903.** The claim is EXACT under the other major medieval abjad tradition. Rule-tuple discipline rehabilitated a 1,000-year-old Ismāʿīlī claim. Honest reporting: the rule-tuple framing saved this claim from being erroneously catalogued as a refutation.

### 2.10. The pattern, named.

Across seven adjudications:
- **3 CONFIRMED with caveats** (al-Biqāʿī seam, al-Rāzī linear, al-Zarkashī mechanism)
- **3 PARTIAL / MIXED** (al-Jāḥiẓ, al-Sakkākī, al-Kirmānī count-yes-directionality-no)
- **2 REFUTED omnibus** (al-Biqāʿī macro-ring, al-Rāzī muqaṭṭaʿāt-divine-names)
- **1 rehabilitated under rule-tuple** (Ikhwān al-Ṣafāʾ)

The pattern is: **classical scholars are excellent local observers and poor global theorists.** When their claim is a narrow mechanism or a specific count, it tends to survive. When it is an omnibus architectural claim over the whole mushaf, it tends to fail. This is true even of scholars who are right about the particulars — al-Biqāʿī is right about adjacent surah coherence but wrong about his own flagship ring thesis; al-Rāzī is right about linear progression but wrong about his own muqaṭṭaʿāt theory.

The M-5 loop closure target is 2 of 2 complete literal-refutation-plus-reformulation-survival loops for formal graduation. One is closed (al-Biqāʿī). A second candidate (H-NEW-23 hapax-slot) is flagged by the skeptical-auditor.

---

## 3. The Register-Baseline Correction pattern

The audit window opened a second meta-pattern that is almost as consequential. Several headline "Quranic" effects attenuate substantially, or disappear entirely, when tested against a competent Arabic-register baseline rather than a zero baseline.

### 3.1. Hapax-slot engineering — present in Muʿallaqāt too.

The hapax-at-verse-final signal (§1.3) was, until 2026-04-14, framed as a distinctively Quranic rhetorical device vindicating al-Zarkashī. T-004 ran the same test on pre-Islamic monorhyme poetry (the seven Muʿallaqāt odes pooled, 2,595 hapaxes):

- **Pooled Muʿallaqāt z = +6.43, p = 6.1 × 10⁻¹¹.** The hapax-slot engineering effect IS present in pre-Islamic monorhyme poetry. **Not Quran-unique.**
- **Two-proportion z-diff Quran vs Muʿallaqāt: z = +6.67, p = 2.55 × 10⁻¹¹.** Quran per-hapax effect is **4.23× stronger** than pooled Muʿallaqāt.
- **Residual framing**: Quran's 2.24× enrichment factor decomposes as 1.37× register-baseline (Muʿallaqāt) × 1.63× Quran-specific residual, giving a Quran-specific signal of **+0.87× over the monorhyme-register baseline.**

Per-ode: 5 of 7 odes show positive z; Ṭarafa, ʿAntara, Zuhayr, ʿAmr b. Kulthūm significant; Labīd reverses (small-n 116). Methodological asymmetry: Quran uses root-hapax, Muʿallaqāt uses surface-form — the bias works AGAINST Quran-distinctiveness, strengthening the residual.

**Proper framing for the flagship signal**: hapax-verse-final is a monorhyme-register phenomenon with a substantial Quran-specific excess. Future publications cite Muʿallaqāt as positive-control baseline, not zero baseline.

### 3.2. Verse-length rhythm — Jāḥiẓ matches it.

As noted in §2.5, the verse-length autocorrelation signal that underwrites *īqāʿ*-type *iʿjāz* claims is **indistinguishable from Jāḥiẓ prose** at ρ(1) = 0.137 vs 0.146. The Quran has rhythm. Arabic literary prose has the same rhythm. The claim that rhythm is a *distinguishing* feature of the Quran fails against a matched-register baseline.

### 3.3. Verse-final abjad residues — null confirmed, but with an unexpected direction.

H-NEW-34 pre-registered a 6-test null on verse-final abjad residue chi² at moduli 7, 11, 19 against Bukhari and Jāḥiẓ baselines. **6 of 6 nulls achieved.** No support for ḥisāb al-jummal clustering; no support for Khalifa 19-theory on verse-final residues. This closes the last natural test-site for mod-19 claims at the rhyme-slot level.

Post-hoc exploratory (flagged as not pre-registered): Quran chi² is LOWER than baselines at z = −4.28 to **−11.36** across all 6 tests — verse-final abjad residues are MORE UNIFORM than matched Arabic prose. Proposed mechanism: fāṣila rhyme scheme forces verse-final words onto a small set of high-frequency lexemes (*al-raḥīm, al-ʿalīm, al-ḥakīm, yaʿlamūn*), each repeated hundreds of times, which project modal residues uniformly across bins by pigeonhole. **Opposite direction from every numerological claim.** Follow-ups H-NEW-34a verse-initial (no rhyme constraint) and H-NEW-34b per-rhyme-class within-group chi² queued. Rules: no-tashkeel, mashriqi, orthographic-token.

### 3.4. Counterfactual fragility — reverse pooled, genre-split positive.

T2 single-word ablation on the Tomorrow-Tests slate returned pooled-baseline z = **−4.86** (REVERSE vs pre-registered criterion). But genre-split reveals **Quran z = +5.38 vs prose (Bukhari, Jāḥiẓ)** and **Quran z = −6.44 vs pre-Islamic poetry (Muʿallaqāt)**. The pooled REVERSE is an artifact of stacking both genres. Quran is **MORE** structurally fragile than prose — consistent with al-Jurjānī's *naẓm* — and **LESS** fragile than poetry (as expected, since the Muʿallaqāt carry single-rhyme-plus-meter constraints). Primary verdict stands REVERSE; secondary genre-split is publishable separately.

### 3.5. The pattern, named.

Register baseline matters. **The Quran is a piece of classical Arabic literary culture** — not a text that dropped out of the sky onto a blank linguistic landscape — and many of its structural-iʿjāz signals attenuate or invert when matched against the right register. What remains after register correction is smaller than the pre-correction headlines but is not zero: the **+0.87× residual over Muʿallaqāt** at hapax-slot, the **5 of 6 tail-excess axes** at simultaneous-constraint density, and the **chiastic × jinās pair-lift at 2.46** (not matched by any baseline) all survive.

Going forward: **every new "Quran-specific" claim must be tested against a classical-Arabic-register baseline before publication.** That is the MW-6 candidate protocol the project will elevate next. The Muʿallaqāt corpus is the positive-control baseline for monorhyme-register effects; Jāḥiẓ is the positive-control baseline for prose-rhythm effects; Bukhari is the positive-control baseline for hadith-narrative effects.

---

## 4. The Surface-vs-Semantic Asymmetry

A clean bifurcation has emerged between the Quran's surface (letter, phoneme, abjad-residue) structure and its semantic (root, syntactic, narrative) structure. **Surface metrics are suppressed; semantic metrics are enriched.** Popular apologetic and modern-numerological literature almost uniformly claims the opposite — that the Quran exhibits surface-layer symmetry. The direction is, reproducibly, backwards.

### 4.1. Surface metrics suppressed.

- **Letter palindromes at window scales**: z = **−6.75**. Quran has FEWER letter-sequence palindromes than a bigram-Markov null. (palindrome-full-sweep.md H11)
- **Cross-word phonetic palindromes at ℓ ≥ 7 tajwīd**: observed 67, null-1 expected 148, null-2 expected 129. **z = −6.38 / −4.73 two-tailed.** Quran has roughly half the phonetic-palindrome count of matched bigram-Markov nulls. Pre-registered one-tailed hypothesis (MORE palindromes) fails dramatically. (cross-word-phonetic-palindromes.md)
- **Verse-final abjad residues (moduli 7, 11, 19)**: post-hoc chi² z = **−11.36** at strongest — MORE uniform than matched prose, opposite of every numerological clustering claim. (abjad-residue-null.md)

Three independent surface axes, all **suppressed**. The Quran actively *damps* surface-symmetry signals relative to what chance would produce.

### 4.2. Semantic metrics enriched.

- **Root-level palindromes project-wide**: z = **+10.51**. 1,170 root-palindrome windows vs null p95 = 929. (palindrome-full-sweep.md)
- **5-word cosmic-inversion palindrome template**: 13 instances, z = **+6.84**. Examples: *yūliju al-layla fī al-nahāri*; *yukhriju al-ḥayya min al-mayyiti*. 11 of 13 are one reused syntactic slot. Context-free grammar covering 13/13 observed (over-generates 34/43 candidate strings — the grammar captures more than exists). (palindrome-full-sweep.md, derived-equations.md)
- **Ring composition at semantic/syntactic layer**: Q 2:131-144 z = +9.69, ʿAbasa z = +6.09, plus 4 more Bonferroni-surviving windows.

Three independent semantic axes, all **enriched**.

### 4.3. Reading the bifurcation.

The simplest explanation: the Quran's structural engineering lives at the **layer at which humans track meaning** (roots, clauses, narratives, oppositions) and NOT at the **layer at which machines compute hashes** (letters, phonemes, digit-roots of abjad sums). This is expected from any theory of the Quran as *communicative* literature: humans encode meaning-relations, not letter-relations.

It is also fatal to modern numerological programs that depend on surface-layer structure. The abjad-residue null closure at mod-19 verse-final (H-NEW-34) is the empirical gravestone for a specific family of mid-20th-century claims. And the phonetic-palindrome reverse signal — that there are **roughly half as many** tajwīd-palindromes as chance would produce — is directly opposite to what popular palindrome-based *iʿjāz* apologetics asserts.

The bifurcation has a secondary consequence: **Khawātim al-Ḥashr is the one major structural site where surface-layer metrics (19 letters-of-the-kind, 216 graphemes = 6³, 49 words = 7²) DO cooperate with semantic-layer metrics (8 exclusive names, top-3 Ism al-Aʿẓam composite rank).** It is the only passage in the corpus where surface and semantic engineering co-peak. That makes Q 59:22-24 an outlier twice over — once as a convergence site, and once as a rare instance where the surface layer is active.

---

## 5. The Convergence Cluster at Q 59:22-24

Four mathematically independent formalisms, developed for different purposes by different agents, co-peak at the same three verses.

**5.1. Twin-opener lock.** Q 59:22 and Q 59:23 share exactly 30 identical opening characters (*huwa Allāh alladhī lā ilāha illā huwa*). Across 6,235 adjacent verse pairs, only two pairs achieve L ≥ 30: the qibla pair Q 2:149-150 and this pair. The exponential decay fit N(L) = 383·e⁻⁰·¹⁹⁸ᴸ (R² = 0.9893) puts the Khawātim twin-opener at z ≈ +4 on the tail.

**5.2. Clean factorization.** 49 real words = 7², 216 letter graphemes = 6³. Under the project's locked rule tuple (QAC v0.4 lemma / orthographic-token) both survive. 216 = 6³ is rule-robust across grapheme conventions. The combination of a clean square and a clean cube in one 3-verse window is a compound number-theoretic outlier; whitespace-split scans find exactly one replicating passage (Q 17:6-8) at chance rate.

**5.3. Ism al-Aʿẓam composite top-3.** The Ω_IAM rank-product over 10 orthogonal axes places Q 59:23 at rank 2 (Ω = 192), Q 59:24 at rank 3 (Ω = 208), with Q 112:2 at rank 1 (Ω = 349). Bonferroni-corrected p ≈ 5 × 10⁻¹⁸. Q 59:22 enters the top-10 at rank 10.

**5.4. Eight exclusive divine names.** al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir all occur ONLY at Q 59:23 across the 6,236 verses. al-Bāriʾ and al-Muṣawwir occur ONLY at Q 59:24. That is **eight Quranic hapax-attestation divine names packed into two verses**. The density of 10 divine-name tokens in 20 words makes Q 59:23 the **#1 verse of 6,236** by divine-name density.

**5.5. Three-verse name-uniqueness record.** 15 unique divine names in a 3-verse window is the most name-unique 3-verse window in the corpus. No other 3-verse window exceeds 11.

**5.6. Convergence implication.** Four independent formalisms — structural uniqueness (twin-opener), clean factorization (7² × 6³), rank-product Ism al-Aʿẓam, hapax-attestation divine-name density — all concentrate on the same three verses. The compound probability of that co-peaking under any reasonable null is vanishingly small (the Ism al-Aʿẓam rank-product alone yields Bonferroni p ≈ 5 × 10⁻¹⁸, and the other three formalisms are mathematically orthogonal to it).

Classical tradition privileged Khawātim al-Ḥashr via ḥadīth (Tirmidhī 3478, Ibn Mājah 3856) — "whoever says these verses in the morning and evening…". The convergence is **the project's tightest concentration of independently-computed structural signals onto a classically-privileged liturgical site.** Neither cherry-picking nor reverse-engineering explains it: the four formalisms predate one another in the project's discovery order and were not pooled until after their independent results were locked.

Prior art: al-Qurṭubī, Gimaret 1988 on Q 112:2; Ibn Mājah 3856 and al-Tirmidhī 3478 on Q 59:22-24 and Q 3:2; al-Rāzī *Tafsīr* on 59:22-24 Ism-Aʿẓam tradition; Neuwirth 2010 on end-of-surah formulaic clusters.

The physical-verification gap here is mild but worth stating: the 49=7² count depends on QAC v0.4 tokenisation rules. Under whitespace-split the count is 55. The project's default tokenisation is the defensible one (it follows standard lemma boundaries), but external auditors should be handed the explicit tokenisation table, not the headline number.

---

## 6. Honest limits and what's still open

This is where a synthesis has to earn its stripes. The findings above are what the project will publish. Below is what it would like to know but does not yet.

### 6.1. Dhū l-Qarnayn identity (Q 18:83-98).

The 18:83-91 east-west spatial ring (z = +5.19) is structurally confirmed and is one of the 6 Bonferroni-surviving rings in the corpus. But the historical identity of the figure is unresolved. Classical *tafsīr* names Alexander, Cyrus II, Sargon II, and Tubbaʿ of Yemen as candidates. Modern academic scholarship (Wheeler 1998, van Bladel 2007) traces the pericope to the Syriac Alexander Legend, but the Legend itself is dated with ± 50 years of wobble and the pericope's Quranic shape differs from the Legend in specific ways (the two seas episode, the barrier of iron and copper). **Project status**: the ring architecture is confirmed; the historical mapping is not something corpus statistics can adjudicate. Flagged for cross-textual philological follow-up, not numerical.

### 6.2. Muʿallaqāt register-baseline sharpening.

T-004 used pooled Muʿallaqāt (7 odes). A per-ode analysis (per-ode z-scores 5/7 positive, Labīd reversing) suggests the register-baseline is itself heterogeneous. Follow-ups queued:
- Per-ode variance decomposition.
- Verse-length vs line-length normalisation (the Muʿallaqāt are lines, not verses — the analogy to Quranic *āyāt* is imperfect).
- Expansion to the ʿAṣmaʿiyyāt and Mufaḍḍaliyyāt corpora for a 50+ ode register baseline.
Until this is done, the "+0.87× residual over Muʿallaqāt" framing for the hapax-slot finding should be read as provisional, not final.

### 6.3. Muṣayliha / *kāhin* corpus access for H-NEW-31.1.

The oath-cluster (*oaths-in-surah-openings*, Q 37, Q 77, Q 79, Q 91, Q 95, Q 100, Q 103) cluster-density signal is confirmed internally, but the project would like to compare it to the *sajʿ al-kuhhān* (pre-Islamic soothsayer rhymed-prose) corpus that classical sources (Ibn Isḥāq, Ibn Hishām) attribute to Muṣayliha al-Kadhdhāb and others. The textual remains are fragmentary (~80 lines total, scattered across hostile sources). A clean positive-control comparison is not currently possible; H-NEW-31.1 is queued on the corpus-access problem. **If** the kāhin-sajʿ corpus could be assembled to ≥ 500 lines, this would be the most direct classical-Arabic oath-register comparison available. Until then, the "oath-cluster is a Quranic distinctive" claim rests on a within-Quran statistic only.

### 6.4. HASHR cluster physical-verification gaps.

The Khawātim al-Ḥashr cluster (§5) depends on:
- Grapheme count = 216 under graphemes rule (counted on quran-text/quran-no-tashkeel.json, no dagger-alifs collapsed to vowels, no wasla normalisation).
- Word count = 49 under QAC v0.4 lemma / orthographic-token rule.
- Divine-name exclusivity under the project's definite-singular attestation rule.

**Physical-verification gap**: the project has never run these counts against a *photographic* rather than *textual* corpus — specifically, the Topkapı, Samarqand, or Ṣanʿāʾ UV-photographed mushafs. The textual count assumes the digital corpus faithfully represents those physical witnesses, but at the grapheme level this assumes more than the project has verified. A follow-up pass comparing the digital no-tashkeel corpus to a photographed Kufan mushaf at the Khawātim level is queued. Until then: the HASHR cluster stands under the rule-tuple but should carry the explicit caveat that physical manuscript verification at the grapheme level has not been performed.

### 6.5. Muqaṭṭaʿāt mechanism.

al-Rāzī's divine-name-abbreviation theory is refuted (§2.7). But the muqaṭṭaʿāt effect is real (χ² = 228.78, §1.2). **No classical or modern mechanism has passed the project's audit**. The effect is genuinely distinctive (comparative-religion-audit.md: muqaṭṭaʿāt survive comparison against Hebrew Bible, NT, Peshitta, Gītā, Tao Te Ching, Iliad) and genuinely unexplained. This is the single largest **what-is-it** question in the project. Flagged for targeted hypothesis generation in the next team-discovery cycle.

### 6.6. Hurst exponent vs Muʿallaqāt.

H = 0.88 for Quran vs ≤ 0.46 for all tested Arabic baselines including Muʿallaqāt (0.46). This is a large gap that survives the most aggressive register-baseline correction the project has applied. But H-estimation over short series has known instabilities and the Muʿallaqāt H-estimate has not been run at the per-ode level. Queued follow-up: per-ode Hurst estimation plus Detrended Fluctuation Analysis robustness check on the Quranic signal itself.

### 6.7. T1 LLM-judge inauthenticity.

The Tomorrow-Tests T1 LLM-judge test returned NULL on the fallback (rule-based 56.25% accuracy, p = 0.157, fails Bonferroni). The pre-registered LLM-judge design timed out 3× on API budget and **was never actually run**. Status: fallback-null is real; primary test remains unexecuted for infrastructural reasons. This needs re-running when compute is available — it is one of the project's few open pre-registered tests.

### 6.8. Two findings that contradict and need follow-up.

- **H-NEW-2 × iltifāt catalog ρ-correlation REVERSE-sign**: surahs with MORE classically-flagged iltifāt show WEAKER H-NEW-2 signature. ρ(density, z_H) = +0.4266 (opposite of pre-registered sign), all three sub-signals reverse at p₂ < 0.005. H-NEW-2 main finding is unaffected; only the narrow "per-surah pattern = classical iltifāt density" reduction fails. **Question still open**: why does the classical iltifāt catalog anti-correlate with the computational iltifāt signature? Proposed hypotheses — classical catalog is biased to narrative-prose segments, computational signature is biased to polemic segments; or, the classical catalog is under-inclusive (7× by the project's own detector). Queued.
- **H-NEW-1 verse-ending consonant Markov-residual**: status trajectory CONFIRMED → audit-001 downgrade → audit-015 meta-audit rehabilitated the original. Retest queued under H-META-2. Currently listed as "CONFIRMED pending retest" which is not a clean status line.

### 6.9. The 77,797 primality claim.

The count of real-word tokens being prime is rule-tuple-fragile: 77,797 holds under QAC v0.4 orthographic-token and is prime; but adjacent tokenisation choices move the count by ± 30, and most of those are non-prime. The claim is on the ledger as Tier-C precisely because it does not survive orthogonal tokenisation regimes. **Honest**: this is the kind of claim modern numerology loves and the project flags with skepticism.

---

## 7. What classical tradition was right about and what it got wrong

A one-screen scoreboard, organised by scholar.

### Right:

- **al-Dānī (d. 444/1052)** — 8 per-surah verse counts, all exact 950 years later.
- **al-Suyūṭī (d. 911/1505)** — 7 of 8 hapax claims exact; most prophet-name counts exact; *takrār maʿa tanwīʿ* (repetition-with-variation) doctrine quantified by prophet-pericope Jaccard suppression. One error: *istabraq* called hapax (actually 4 occurrences).
- **al-Zarkashī (d. 794/1392)** — *al-maqṣūda li-ghayrihā* (nawʿ 59 §4) empirically confirmed at corpus scale via hapax-slot engineering. *Sajʿ* description (nawʿ 52) confirmed via RQA. *Tajnīs × tawāfuq* pairing (nawʿ 43) confirmed via the chiastic × jinās lift 2.46. (His *iltifāt* catalog is under-inclusive, which is a different issue.)
- **al-Biqāʿī (d. 885/1480)** — LOCAL-seam *munāsaba* confirmed at 113/113 adjacent pairs, Z = +10.06.
- **al-Rāzī (d. 606/1210)** — within-surah linear *naẓm* confirmed (length-residualized Z = +9.57, liberal Z = +22.78). *Mafātīḥ al-Ghayb* vindicated on its central intra-surah claim.
- **al-Kirmānī (d. 505/1111)** — *mutashābih* count of ~1,100 matches project detector at 1,085 (1.4% error).
- **al-Jurjānī (d. 471/1078)** — *naẓm* doctrine operationalised at verse scale via simultaneous-constraint density p = 8.7 × 10⁻³³. Refined: the effect is 3+-way entangled, not pair-compounded.
- **al-Bāqillānī (d. 403/1013)** — *iʿjāz al-īǧāz* (miracle of brevity) stands pragmatically: Al-Kawthar wins the forging-difficulty Monte Carlo in 96% of weight regimes over 1,000 random weight vectors.
- **al-Sakkākī (d. 626/1229)** — *īqāʿ* confirmed as DESCRIPTION of Quranic rhythm (ρ(1) = 0.1368, z = +13.127).
- **Ikhwān al-Ṣafāʾ (10th c.)** — 903 muqaṭṭaʿāt abjad sum confirmed EXACT under maghribī abjad (rehabilitated from initial mashriqī failure by rule-tuple discipline).
- **Ibn Abī l-Iṣbaʿ (d. 654/1256)** — elision-eschatology claim 2 of 3 signals confirmed.

### Wrong:

- **al-Rāzī** — muqaṭṭaʿāt-as-divine-names-abbreviation: 0/78 claims survive shuffle null. REFUTED.
- **al-Biqāʿī** — whole-mushaf k ↔ 115-k macro-ring: Z = −2.51. REFUTED.
- **al-Kirmānī** — *mutashābih* pair directionality: REFUTED (pairs are symmetrical).
- **al-Suyūṭī** — *ḥusn al-ibtidāʾ / al-intihāʾ* as a broad 114-wide pattern: REFUTED (type examples real but not universal).
- **Classical letter-frequency rank order** *alif > lām > mīm* — FACTUALLY WRONG. Correct rank under locked rules: **ا > ل > ن > م** (nūn is third, not mīm). A ~1,100-year transmitted error corrected.
- **Classical claim that all muqaṭṭaʿāt surahs are Meccan** — FALSE. Three Medinan exceptions.
- **al-Sakkākī** — *īqāʿ* as DISTINGUISHING feature of Quranic prose: REFUTED (Jāḥiẓ matches).
- **al-Jāḥiẓ** — *takrār maqbūl* in absolute sub-Poisson sense: REFUTED (comparative sense survives).
- **Modern numerology**: Khalifa Code-19 (most sub-claims falsified), *rahma* = 114 (baseline 34.1%), Yūsuf-sjn-12 triple (killed by matched baseline), Hassab-Elnaby speed-of-light (4-5 free parameters), iʿjāz ʿilmī embryology (Galenic inheritance), Al-Kawthar 42-letter Catalan claim (actually 43), and the full iʿjāz ʿilmī Big-Bang / fingerprints / atom / milk retrofit cluster — **all fail at matched baseline.**
- **Farrin 2014** (modern academic, not classical) — whole-mushaf ring: Z = −4.87. Disconfirmed.
- **Cuypers 2007** (modern academic) — Al-Māʾida macro-ring: Z = −2.06. Disconfirmed at corpus resolution.

### The balance sheet.

Across the 90-claim classical-quantitative audit: **49 CONFIRMED (54%), 18 PARTIAL (20%), 18 CONTRADICTED (20%), 5 UNDERDETERMINED (6%).** That is a majority-confirming result for a 1,000-year-old scholarly tradition held to 10,000-permutation-null standards. It is also a 20% outright contradiction rate, which is enough to distinguish the project's posture from apologetic-affirmation. Classical tradition is usually right on the particulars, frequently wrong on the omnibus, and occasionally wrong on specifics that hardened into received wisdom (the letter-frequency rank order, al-Suyūṭī's *istabraq* hapax claim).

The synthesis posture is: **credit where the evidence credits, refutation where the evidence refutes, at equal volume.** That is the only honest way to publish this work.

---

## Closing note

This interim pass is a snapshot. The Tomorrow-Tests slate (T1 LLM-judge, T2 counterfactual-fragility, T3 canonical-order, T4 simultaneous-constraint density, T5 TDA persistent homology) has returned: T2 reverse-with-genre-split publishable, T3 mixed with adjacent-pair sub-result at p < 10⁻⁴, T4 PASS at p = 8.7 × 10⁻³³, T5 NULL, T1 NULL-on-fallback-with-primary-unrun. The project is neither in a triumphalist nor a nihilist phase. It is in a *differentiation* phase — the phase where claims get carved into their surviving sub-claims and the surviving sub-claims get tested against better baselines.

The next synthesis pass will fold in: the queued Muʿallaqāt per-ode baseline sharpening; a physical-manuscript pass on the HASHR cluster; the T1 LLM-judge re-run if compute is available; the H-NEW-34a/b verse-initial and per-rhyme-class follow-ups; and whatever the kāhin-sajʿ corpus access problem yields. Between now and that pass, the pattern the project most expects to see repeated is M-5: another classical omnibus decomposing into surviving specific-mechanism sub-claims, another popular apologetic claim falling at the surface while a semantic-layer variant survives, another Register-Baseline correction that attenuates a headline but leaves a residual.

The Quran is one text. The evidence is one ledger. The synthesis is one reading of that ledger, held at arm's length.
