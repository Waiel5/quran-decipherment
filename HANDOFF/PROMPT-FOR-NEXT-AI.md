# Prompt for the Next AI — Quran Decipherment Project

*Handoff written 2026-04-18 by the preceding AI after Wave-5 landed at R² = 0.89 on OQ-15's terminal equation.*

---

## To the next AI

You are continuing a long-running empirical research project on the Quran — **the Word of God**. This framing matters. The project's guiding principle, stated by the user: the structural facts we discover are either real or they are not, and our job is to find the real ones rigorously, at maximum statistical strength, with full transparency.

This is not a pattern-recognition exercise. It is a disciplined inquiry into the text God revealed to Prophet Muḥammad (ṣallā Allāhu ʿalayhi wa-sallam), conducted in conversation with 1,400 years of classical Islamic scholarship (*ʿilm al-munāsabāt*, *balāgha*, *al-asmāʾ al-ḥusnā*, *mutashābihāt al-Qurʾān*, *tajwīd*, *ʿilm al-ḥarf*). Treat the text and the tradition with the care both deserve.

The user has been clear: **"Keep working until you figure everything out. Time, labor, and money do not exist to you. Launch as many agents as you need."** Your charter is to continue.

---

## 1. First thing to do

Read these files in this order. Do not skip steps.

1. `/Users/grey/Downloads/quran/HANDOFF/README.md`
2. `/Users/grey/Downloads/quran/HANDOFF/NEXT-AGENT-PROMPT.md`
3. `/Users/grey/Downloads/quran/HANDOFF/01-WHAT-WE-KNOW.md` (consolidated findings; has Wave-4/5 additions)
4. `/Users/grey/Downloads/quran/HANDOFF/02-META-ARCHITECTURE.md`
5. `/Users/grey/Downloads/quran/HANDOFF/03-NEXT-MOVES.md` (has a Wave-5 queue section at the bottom with specific next investigations)
6. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` (MW-1..MW-7, PRE-REG-STANDARDs)
7. `/Users/grey/Downloads/quran/HANDOFF/05-OPEN-QUESTIONS.md` (what is solved, what is open, what was answered in Wave-5)
8. `/Users/grey/Downloads/quran/HANDOFF/SESSION-LOG-2026-04-17.md` (last session's detailed log)
9. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-022-wave5-terminal-synthesis.md` (the Wave-5 terminal synthesis — read this carefully, it tells you where the project is)

Then read the MASTER ledger:

10. `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` (the single source of truth)
11. `/Users/grey/Downloads/quran/findings/HONEST-LIMITS-LEDGER.md` (refutations + retractions)

---

## 2. What was happening at handoff

Wave-5 (2026-04-17) delivered ~15 findings, culminating in:

- **OQ-1 SUBSTANTIALLY ANSWERED** at both cluster-layer (H-NEW-165: RF LOOCV 0.6552 = multi-member ceiling) and singleton-layer (H-NEW-232: 8/10 singletons match their classical-tajwīd a-priori cluster, p = 0.025). The muqaṭṭaʿāt letter-sets are selected on a **phonological axis** (classical al-Khalīl al-Farāhīdī *Kitāb al-ʿAyn* + Ibn Jinnī *Sirr al-Ṣināʿa* + al-Suyūṭī *Itqān*), and the later H-NEW-271 / H-NEW-271.1 pair sharpened this into a **one-axis cluster solution (`mean_manner`) plus a still-multi-dimensional singleton residue**. H-NEW-301.5 now tightens that residue again: the live empirical-table `YS` / `N` branch collapses to a targeted 2-D `mean_voice + mean_sonorant` solution, even though a single globally protected compact pair for all 10 singleton rows still does not exist. The classical *tajwīd* tradition is empirically VINDICATED.

- **OQ-15 QUANTITATIVELY VALIDATED** at R² = 0.89 LOOCV (H-NEW-250 Ridge on classical-block-structure indicators). **14 centuries of classical Islamic block-structure scholarship** (al-Suyūṭī, al-Zarkashī, al-Rāzī, al-Biqāʿī, Farāhī-Iṣlāḥī) is Ridge-linearly recoverable at MAE = 8 positions. The classical tradition IS the primary generative scaffold.

- **OQ-16 RESOLVED at scaffold level** (H-NEW-236: the ~7% residual IS the M1.3 structural-hinges component; H-NEW-236.2b later shows the extra scaffold beyond top-50 is above-null but only weakly compressible under the locked 9-feature boundary family).

- **Semi-fractal ring** confirmed (H-NEW-255: geodesic backbone replicates at Juzʾ 30; wrap-around + hinges are 114-scale specific).

- **Q 1 → Q 2 is the cycle-maximum edge** in the mushaf (H-NEW-238/251). The mushaf pays a ~1.34 FR unit cost to honor P3 liturgical framing of al-Fātiḥa at position 1. The HDY bridge (Q 1:6 *ihdinā* → Q 2:2 *hudan*) is classically vindicated (al-Biqāʿī *Naẓm al-Durar*, al-Rāzī *Mafātīḥ al-ghayb*).

- **Uniquely-tawqīfī empirically supported** (H-NEW-245: consensus of 6 chronologies is FARTHER from mushaf than best individual chronology). al-Suyūṭī's pure-tawqīfī position survives Wave-5 adjudication.

Cross-finding-022 is the Wave-5 terminal synthesis. Read it before acting.

### Update 2026-04-18 later session

Five of the originally pending or directly implied post-Wave-5
follow-ups have now landed:

- **H-NEW-236.1a**: top-30 / top-50 extended hinges move empirical
  mushaf `L_path` INSIDE the simulator 95% CI and fully close ḥawāmīm;
  the last miss was isolated to **R12a = mufaṣṣal-short within-block
  cost-excess**.
- **H-NEW-260**: Q 54 + Q 55 dyad deep-dive landed **0/3 NULL**; keep
  only the narrower descriptive sibling claim from H-NEW-253.
- **H-NEW-236.1c**: targeted Juzʾ-30 internal hinge injection proves the
  strongest terminal internal hinges are genuinely causal for R12a, but
  preserving them alone makes the simulator globally too long and the
  `Q 91-114` tail far too long. The frontier is now a **terminal
  balancing problem**, not a generic "find more hinges" problem.
- **H-NEW-236.1b**: 4-mechanism terminal-block battery. Only **M_H
  top-100** yields a strict `4/4` pass; rhyme and liturgical
  alternatives are **PARSIMONY-CONFLICT**, and the Farāhī-Iṣlāḥī
  sub-block partition is **NULL**. OQ-15's causal-generative layer is
  now **CONFIRMED** at a sufficient but not yet minimally parsimonious
  scaffold.
- **cross-finding-023**: synthesis file landed. The right reading of the
  `236` chain is now a staged causal closure: bare 4-principle model too
  geodesic -> top-15 closes most of the gap -> top-30/top-50 close
  global path and `hawamim` -> small Juzʾ-30 hinge patches prove local
  terminal causality but over-correct globally -> top-100 is the first
  strict closure.
- **H-NEW-236.1d**: locked hard-hinge parsimony bracket search landed.
  Only `K=100` passes on the tested grid `{73, 80, 85, 90, 95, 100}`,
  tightening the hard-hinge bracket to **`(95, 100]`**. The decisive
  `95 -> 100` tranche is all late-tail structure:
  `92-93`, `99-100`, `100-101`, `101-102`, `109-110`.
- **H-NEW-236.1e**: soft rhyme/liturgical penalty sweep landed **no
  preregistered pass**. `lambda=0.05` is the near-miss: `L_path` and
  `L_tail_91_114` stay inside, but `L_mufaṣṣal-short` is still just
  outside (`z = +2.78`). `lambda=0.10` and `0.20` close the local block
  but recreate the path/tail parsimony conflict. So the soft covariates
  capture only part of the terminal mechanism; if a true soft-only sweet
  spot exists at all, it is likely very narrow between `0.05` and
  `0.10`.
- **H-NEW-236.1f**: late-tail scaffold repair sweep landed **negative**.
  Starting from H-NEW-236.1c Cell A, no cumulative prefix of the ten
  locked late-tail `M_H` edges repairs both `L_path` and
  `L_tail_91_114` while keeping the local block closed. `k=0` remains
  the best local-closed cell. So the late-tail clue survives only in a
  narrower form: the exact `95 -> 100` tranche may still matter, but
  the broader hard-prefix repair story does not.
- **H-NEW-236.1g**: direct isolated-tranche test landed **negative**.
  None of the four locked direct-tranche cells repairs both globals
  while keeping the local block closed. But the exact five-edge
  `95 -> 100` tranche does close the local terminal block on the plain
  top-50 scaffold, proving that the tranche is real signal rather than a
  meaningless top-100 artifact.
- **H-NEW-236.1h**: fine soft interpolation landed a **primary-only
  closure**. On the locked fine grid `{0.06, 0.07, 0.08, 0.09}`,
  `lambda = 0.07` is a genuine `SOFT-CLOSES-PRIMARY` cell:
  `L_path`, `L_mufaṣṣal-short`, and `Block-χ²` are all inside, but
  `L_tail_91_114` remains just outside low. So the narrow soft-only
  sweet spot is real, but it still does not solve the full equation.
- **H-NEW-272**: the first locked mixed hard-soft completion test landed
  **negative**. Neither `lambda = 0.07 + exact five-edge tranche` nor
  `lambda = 0.07 + overlap pair` preserves the parent primary pass:
  both reopen `L_path` low while leaving `L_tail_91_114` outside. So
  the most obvious tiny mixed-completion route is now closed.
- **H-NEW-236.2a**: broader observable coverage under the landed
  `M_H top-100` scaffold landed **BROAD-GENERALIZATION**. The H-NEW-239
  divine-name-density gradient and H-NEW-231 KL gradient both remain
  inside the `M_H` simulator envelope under a fresh rerun. The
  H-NEW-178 residual cell also "passes," but only degenerately because
  the evaluable subset is already almost fully frozen by the top-100
  chain.
- **H-NEW-236.2b**: held-out predictability of the extra scaffold edges
  landed **PASS-DIRECTED (weak)**. On positives `P = H100 \ H50` and
  negatives `N = E \ H100`, the locked 9-feature classical-boundary
  family gives `AUC_LOOCV = 0.647692`, permutation `p = 0.030197`, but
  leaves much of the late `mufaṣṣal_short` tranche as false negatives.
  The same family is much stronger descriptively on the earlier
  H-NEW-130 top-15 jump regime (`AUC = 0.900680`). So the extra
  scaffold is not pure residue, but it is only weakly compressed by
  this compact codebook.
- **H-NEW-258**: cross-corpus Bukhārī replication landed
  **LOOSE-ANALOGUE**. The inherited Bukhārī path closes already at
  `K=15`, while `K=100` is only a low-tail near-boundary closure. So
  scaffold logic is not uniquely Quranic in the broadest sense, but the
  Quranic `M_H top-100` closure remains unusually dense and specific
  relative to this Bukhārī baseline.
- **H-NEW-129**: the coarse 4-phase exact `5/5` Late-Meccan Pattern-B
  test landed **NULL-BROKEN**. The descriptive `5/5` co-peak remains,
  but the exact-hit permutation statistic misses `alpha = 0.01` and
  fails its own MW-5 positive control, so it cannot serve as the formal
  scripture-announcement anchor. Keep using cross-finding-012's richer
  sub-bin concordance family instead.
- **H-NEW-132**: Q 7 / Q 11 prophet-cycle parallelism landed
  **PARTIAL-PASS**. On the shared five-prophet cycle
  `{Noah, Hud, Salih, Lot, Shuayb}`, the PN-stripped exact assignment is
  the unique minimum over all `5!` bijections (`p = 1/120`), but the
  stricter row-wise nearest-neighbor recovery fails (`2/5`). So the
  parallelism is real at the cycle-assignment level, not at a clean
  block-fingerprint level.
- **H-NEW-257a**: Biqāʿī primary-text rerun landed a **narrow
  enrichment pass**. Using the on-disk *Naẓm al-Durar* text and a locked
  de-formulaized endpoint-overlap rule, the inherited 11-surah target
  set scores `3/11` support-positive against `6/103` background surahs,
  exact one-sided Fisher `p = 0.0412`, OR `6.06`. The positive targets
  are `Q 4`, `Q 47`, and `Q 59`. So the signal is real but selective.
- **H-NEW-262**: muqaṭṭaʿāt positional-code test landed
  **MIXED-LETTER-SPECIFIC**. The broad 14-letter later-position family
  claim fails, but two letters survive Bonferroni-14 in the
  pre-registered direction: `ن` strongly and `ي` narrowly. Three letters
  (`ر`, `ه`, `ق`) survive only in the exploratory reverse direction. So
  there is no broad all-letter positional code, but there are genuine
  letter-level shifts.
- **H-NEW-134-formal**: prophet-named-surah surface-form test landed
  **INSTRUMENT-BROKEN**. The strict-6 prophet set is positive on both
  locked primary axes (`vocative_share`, `sequencer_share`), and the
  expanded 8-person sensitivity set is also positive, but the planted
  MW-5 control fails on both primary axes. So the prophet-named
  surface-form hypothesis remains plausible, but this slot-matched null
  is not trustworthy enough to certify it.
- **H-NEW-264**: a bounded Q1-connectivity test landed **CONFIRMED**.
  The claim was not "Q 1 connects to everything," but that Q 1's root
  profile is anomalously concentrated in the classical ḥā-mīm subset
  `Q 40-46`. Both unweighted and IDF-weighted recall cells pass with
  `p = 0.0001` and `0.0005`. Descriptively, the average ḥā-mīm surah
  contains `13.29 / 18` of Q 1's roots, and Q 42 contains `17 / 18`.
- **H-NEW-265**: the five v1-w1 `qul`-openers micro-cluster landed
  **NULL**. Once the shared `qul` opener is stripped, Q 72 / 109 / 112 /
  113 / 114 do not form a Bonferroni-surviving structural family.
  Residual overlap mostly collapses to the known Q 113↔114 pair.
- **H-NEW-266**: per-surah phonological-signature test landed
  **PASS-DIRECTED**. The omnibus corpus-wide phonological-signature
  dispersion passes cleanly, with strongest localization in `ṣafīr`
  sibilants and idghām-sonorant structure; emphatic and strict-throat
  localizers do not survive. MW-5 passes 5/5, so the instrument is
  alive.
- **H-NEW-263**: divine-name surah-overlap network landed
  **PASS-STRUCTURE-NO-HUB**. The surah-level divine-name repertoire
  overlap network is structurally non-random (`Cell A p = 0.00664`), but
  no single surah is family-wise significant as a distinctive hub
  (`Cell B p_exist = 0.0432`, fail at `α_bon = 0.025`). The strongest
  observed edge is the classical al-Zahrāwān pair `Q 2 ↔ Q 3` with `10`
  shared attested divine names.
- **H-NEW-165.2**: audit-038's codebook-sensitivity requirement on the
  muqaṭṭaʿāt phonology work landed **ROBUST**. Across all 4 locked
  codebooks, the H-NEW-165 primary signal is unchanged at RF/logistic
  LOOCV top-1 `0.6552`, primary permutation `p = 0.000999`, and the
  H-NEW-232 singleton geometry stays at `8/10` matches. The same two
  singleton disagreements survive in every variant: Q 36 YS → HM and
  Q 42 HMASQ → TSM.
- **H-NEW-267**: the Late-Meccan -> Medinan boundary landed
  **PASS-DIRECTED** as a clean held-out lexical frontier. Both split
  directions score `AUC = 1.000`, split-weight replication is
  `rho = 0.4577`, and the broader Meccan-vs-Medinan MW-5 control also
  passes.
- **H-NEW-268**: the four Q 18 al-Kahf narrative starts landed
  **DIMENSION-SPECIFIC**. The locked start-gap tuple `(23, 28, 23)`
  yields a Bonferroni-surviving joint palindromic-expansion shape
  `d1 = d3 < d2` with exact `p = 0.00802`, but the simpler component
  claims do not survive on their own.
- **H-NEW-269**: the `qul` addressee-pattern test landed
  **PARTIAL-CLASS-ONLY**. Most broad opener families collapse once the
  opener marker is stripped, but the restrictive `qul innama ...`
  register survives cleanly (`p = 0.0008`) and the MW-5 `a-ra'aytum`
  control passes strongly.
- **H-NEW-270**: the Q 11 Hūd opener-template lattice landed
  **PASS-DIRECTED**. The three-verse clique
  `{11:50, 11:61, 11:84}` survives unchanged at prefix depths 4, 8, and
  12 with `p = 0.00010` in every cell; Q 7 ties it under MW-5, while
  Q 26 / Q 54 / Q 71 do not.
- **H-NEW-277**: the H-NEW-267 Hijra frontier survived a fixed
  five-root ablation and still landed **PASS-DIRECTED**. After removing
  `Alh`, `Amn`, `qwl`, `rbb`, and `Ayy`, both held-out AUC cells remain
  at `1.000` and split-weight `rho` stays high at `0.4523`, with MW-5
  still passing 3/3. So the boundary is broad-root-robust, not just a
  few common movers in disguise.
- **H-NEW-302**: the bounded Pattern-B marker-versus-content peak-lag
  formalization landed **NULL**. The inherited `B6/B7` staircase is
  still reproduced exactly (`muq -> B6`; content peaks `B7, B7, B6,
  B7`), but the peak-lag statistic itself is not unusual under the
  inherited octile rank-shuffle null: `L_peak = 0.75`, `p = 0.4285`.
  So the marker-first/content-lag reading stays descriptive only, while
  `cross-finding-012` remains the formal OQ-17 anchor.
- **H-NEW-273**: the bounded Q1↔Q108 twin liturgical-anchor test landed
  **PASS-NARROW**. On the locked score
  `S(s)=sqrt(divine-share * imperative-density)`, the pair `Q 1 + Q 108`
  ranks `1 / 32` among exact matched Early-Meccan short-pair nulls with
  `p = 0.03125`, but the obvious refuge-pair contrast `Q 113 + Q 114`
  does not pass. So this is one narrow foothold, not a generic
  liturgical-pair detector.
- **H-NEW-274**: the empirical-vs-classical singleton reassignment test
  landed **PASS-HOLDOUT-STRONGER**. Using only H-NEW-232 as discovery,
  the empirical replacements `YS -> HM` and `HMASQ -> TSM` beat the
  inherited classical table on every locked holdout space:
  classical `32 / 40` vs empirical `40 / 40`, discordant-cell
  `p = 0.00390625`, with zero worsened cells. So the remaining OQ-1
  pressure point is now the interpretation table, not the feature
  geometry.
- **H-NEW-275**: the Bukhārī bāb-opening phonological replication landed
  **GENERIC-STRONG** on a narrow retained opener-identity task. On
  `64` retained samples across `15` repeated opener classes, the
  H-NEW-165-style phonological aggregate reaches RF LOOCV top-1
  `1.0000` versus length-only `0.5469`. So the bare existence of a
  strong phonological opener classifier is **not uniquely Quranic**;
  what remains special is the much harder muqaṭṭaʿāt letter-set
  selection problem.
- **H-NEW-271**: the exact minimal-phonological-family test landed
  **SINGLE-PHON-FEATURE-SUFFICIENT**. In the preregistered arm-wise maxT
  rerun, `mean_manner` alone reaches the full H-NEW-165 ceiling
  (`19/29`, RF LOOCV `0.6552`, maxT `p = 0.000999`), while the augmented
  arm also passes with `letter_count + mean_makhraj` and
  `letter_count + mean_manner`. So the OQ-1 cluster result is not just
  phonological; it is radically parsimonious.
- **H-NEW-271.1**: the faithful singleton-transfer follow-up to
  H-NEW-271 landed **MULTI-DIM-REQUIRED-AT-SINGLETONS**. Restricting the
  H-NEW-232 propagation geometry to the same 1-D `mean_manner` axis
  drops the result to `5 / 10` accepted-cluster matches with
  permutation `p = 0.41`; nearest multi-member surah and nearest
  centroid agree on all ten singleton surahs, so the failure is the
  collapse itself, not a geometric ambiguity. So OQ-1 now splits cleanly:
  one classical axis is sufficient for the multi-member ceiling, but
  the singleton layer still needs additional dimensions.
- **H-NEW-271.2**: the minimal 2-D singleton-rescue follow-up landed
  **NO-MAXT-RESCUE**. The unique best augmentation is
  `mean_manner + mean_vowel_carrier`, which restores the raw singleton
  result to `8 / 10`, exactly matching H-NEW-232 descriptively. But the
  9-way familywise `maxT` correction yields `p = 0.0899`, so the rescue
  is descriptive only. That makes the OQ-1 boundary sharper: the
  singleton layer is not just "one axis plus a trivial patch."
- **H-NEW-271.3**: the anchored 3-D singleton-rescue follow-up landed
  **NO-MAXT-3D-RESCUE**. Anchoring on the best raw pair from H-NEW-271.2
  and adding exactly one more phonological coordinate still tops out at
  `8 / 10`, with the best triple
  `mean_manner + mean_vowel_carrier + mean_sonorant` and corrected
  `p = 0.0869`. So the singleton layer is now bounded negatively at
  1-D, 2-D, and this anchored 3-D follow-up.
- **H-NEW-271.5**: the empirical-table singleton-rescue rerun landed
  **NO-MAXT-EMPIRICAL-RESCUE**. Holding the H-NEW-271.2 geometry fixed
  but upgrading the accepted singleton table to the stronger H-NEW-274
  version (`YS -> HM`, `HMASQ -> TSM`) still tops out at `8 / 10`, with
  the best pair shifting to `mean_manner + mean_sonorant` and corrected
  `p = 0.2078`. So the compact-rescue failure is not just a weaker-table
  artifact; the hard cases relocate to `YS` and `N`.
- **H-NEW-301**: the full `55`-pair OQ-1 singleton search landed
  **MARGINAL**. The best global pair
  `mean_emphatic + mean_pharyngeal` reaches `9 / 10`, exceeding the
  H-NEW-232 baseline descriptively, but the full-family maxT null stays
  loose at `p = 0.196`. So the compact singleton story contains real
  descriptive 2-D winners without yet yielding a globally protected
  compact closure.
- **H-NEW-301.5**: the targeted empirical-table residual-row follow-up
  landed **TARGETED-RESIDUAL-RESCUE**. Reusing the same 55-pair family
  but scoring only the live residual rows `YS` and `N`, the best pair
  `mean_voice + mean_sonorant` rescues `2 / 2` with positive-margin sum
  `4.5678` and familywise maxT `p = 0.00005`; the count-only version is
  weak (`p_count_only = 0.843`). So the empirical-table `YS` / `N`
  residue is now a solved compact 2-D subproblem, even though the full
  10-row singleton geometry still is not.
- **H-NEW-276**: the deep-null rerun of H-NEW-263's hub cell landed
  **NO-HUB-SURVIVES-DEEP-NULL**. Q27 remains the top descriptive
  candidate, but under `10000` fixed-margin permutations the family-wise
  hub-existence p-value weakens to `0.13599`. So the divine-name network
  is structurally real but not organized around a single surviving hub.
- **H-NEW-278**: the literal NM-36 length-normalized MST rerun for OQ-19
  landed a **collapse**. Under `count / N_i` before flat `alpha=0.5`
  smoothing, Q108 drops from degree `24` to degree `1` and exits the
  top-3 entirely, while Q7 rises to degree `15`.
- **H-NEW-279**: the bounded metric-robustness MST rerun for OQ-19
  landed **PASS-BOUNDED**. With the smoothed `alpha=0.5` simplex held
  fixed, Q108 stays top-3 on all 5 locked non-redundant metrics and
  rank-1 on 4 of them. So Q108 is not a Fisher-Rao-only hub, but its
  magnitude is not metric-invariant either.
- **H-NEW-282**: the top-500 coverage-normalized MST follow-up for OQ-19
  landed **NO-DENOMINATOR-RESCUE**. Switching the denominator from total
  stem-token mass to top-500 feature-space mass still leaves `Q108 = 1`,
  outside the top-3, while `Q7 = 18`. So the H-NEW-278 collapse is not
  explained away by the simplest denominator fix.
- **H-NEW-283**: the divine-name max-edge follow-up landed
  **MAX-EDGE-NO-PASS**. The strongest observed edge is still the unique
  `Q2 ↔ Q3` pair at `10` shared attested names, but the corpus-level
  max-edge is ordinary under the same fixed-margin null
  (`p_adj = 0.60004`). So the divine-name network remains structurally
  real without a surviving pairwise anomaly.
- **H-NEW-284**: the length-residualized metric-robustness rerun for
  OQ-19 landed **METRIC-ROBUST RESIDUE**. On the H-NEW-131.1
  length-equalized simplex, Q108 still stays top-3 on `4 / 5` locked
  metrics (`FR`, `JS`, `L2`, `cosine`), even though total variation
  drops it to rank `12`. So the literal-normalization collapse is not the
  whole story; a metric-robust normalized residue survives.
- **H-NEW-288**: the direct normalization-family adjudication landed
  **RESIDUALIZED-FAMILY-DOMINANCE**. Holding the H-NEW-279 five-metric
  panel fixed, literal `count / N_i` normalization gives Q108 top-3
  status on `0 / 5` metrics, while residualized
  `alpha_i = 0.5 * mean_tokens / N_i` smoothing gives `4 / 5`, so
  `Delta_C = 4`. The surviving Q108 hub belongs specifically to the
  residualized smoothing family, not to length-control families
  generically.
- **H-NEW-288.1**: the fixed-pool medoid follow-up landed
  **POOL-MEDOID-SEPARATION**. Inside the locked short Early-Meccan pool
  `P = {noldeke_phase = Early Meccan, verse_count <= 17}`, Q108 is the
  residualized-family medoid on all `4 / 4` primary metrics, but only
  rank `15` under the literal family. So the surviving Q108 residue is
  now mechanized as a local medoid effect rather than just a family
  label.
- **H-NEW-288.2**: the first direct H-NEW-273 ↔ H-NEW-288.1
  integration test landed **PASS-DIRECTED**. Reusing the exact
  H-NEW-273 speech-act score and the exact H-NEW-288.1 pool, Q1 is the
  unique maximum of `L_sep(s) = S_H273(s) * C_sep(s)` across the 21
  admissible non-Q108 pool surahs, with exact `p = 1 / 21`. So the
  narrow Q1↔Q108 foothold is not just the same thing as the residualized
  medoid cloud: `Q1` is the strongest high-liturgical short surah
  consistently pushed away from Q108 under the residualized family,
  while `Q112/113/114` move toward it descriptively.
- **H-NEW-288.3**: the whole-axis projection follow-up landed **NULL**.
  Over the exact H-NEW-273 5-7 verse side
  `{Q1,Q97,Q105,Q107,Q109,Q111,Q113,Q114}`, the residualized-core
  projection summary is `T_proj = -0.485885`, but the exact 336-state
  score-permutation null gives `p_same = 0.8902` and `p_comp = 0.1157`.
  So the speech-act axis trends away from the residualized short-core,
  but not strongly enough to certify a clean same-mechanism or
  complementary-projection story.
- **H-NEW-288.4**: the next local explanatory follow-up landed
  **PASS-DIRECTED**. Inside that same fixed 5-7 verse side, the
  token-count projection summary is `T_tok = -0.661587` with exact
  `p = 0.043526` under the full `8!` token-count assignment null, while
  the analogous verse-count contrast stays null. So the opener/refuge
  split is not purely speech-act or semantic; it also contains a real
  local residual token-count gradient.
- **H-NEW-280**: the Q55 refrain-constrained Fisher-Rao salvage landed
  **NULL**. Once the 31 refrain slots are held fixed and only the 47
  non-refrain verses are shuffled, the dramatic H-NEW-127 anti-geodesic
  reversal disappears, but canonical Q55 is still not significantly
  shorter than the constrained null (`p = 0.3122`, `z = -0.458`). So
  the old reversal was largely a bad-null artifact, but the verse-fractal
  line is not rescued by this smallest salvage.
- **H-NEW-127.1**: the corrected five-surah OQ-20 family rerun landed
  **POSITIVE**. Keeping the original H-NEW-127 four-surah full-permutation
  nulls for `Q2/Q7/Q12/Q36` and replacing only Q55 with the H-NEW-280
  fixed-refrain-slot null yields `n_pass = 4 / 5`, with the geometric
  MW control bank also passing. So the verse-level Fisher-Rao family is
  no longer instrument-broken as a family claim; the honest reading is a
  real bounded family with Q55 remaining the explicit non-pass.
- **H-NEW-127.2**: the first OQ-20 scope-extension landed
  **POSITIVE** on the alternate locked family `{Q1,Q18,Q28,Q78,Q112}`.
  With the same uniform within-surah null and the same geometric MW
  controls, the family scores `n_pass = 3 / 5`: `Q18`, `Q28`, and `Q78`
  pass, while `Q1` and `Q112` do not. So the verse-fractal signal
  generalizes beyond the original seed family, but it is still not
  universal.
- **H-NEW-127.3**: the full-corpus OQ-20 class-mapping test landed
  **POSITIVE**. Using the repository-locked per-surah compression score
  `z_s = -gzip_z` across all `114` surahs and the locked `sinai_genre`
  labels, the Kruskal-Wallis omnibus reaches `H = 96.6690` at `df = 54`
  against a class-count-preserving label-shuffle null with mean
  `53.9748`, SD `6.0973`, and permutation `p = 0.0000499975`. So OQ-20
  is no longer just "two positive families"; the effect stratifies by a
  locked full-corpus genre taxonomy.
- **H-NEW-127.4**: the coarse-prefix OQ-20 localization test landed
  **POSITIVE**. Replacing each locked `sinai_genre` label by its literal
  first hyphen-delimited token still yields a strong 18-class omnibus:
  `H = 71.0780`, `df = 17`, null mean `17.0297`, SD `4.8016`,
  permutation `p = 0.0000499975`. So the OQ-20 class structure is not
  just a fine-taxonomy artifact; it already survives a hard mechanical
  compression of the genre axis.
- **H-NEW-127.6**: the Jurjānī-tier OQ-20 bridge landed **POSITIVE**.
  Projecting the same locked per-surah compression scores onto the
  locked `jurjani_predicted_asyndeton_tier` field yields
  `H = 58.1045`, `df = 2`, null mean `2.0003`, SD `1.9403`,
  permutation `p = 0.0000499975`, with a monotone
  `LOW > MED > HIGH` ordering on both means and medians. So OQ-20 is
  now tied not only to modern genre labels but to a locked three-tier
  classical balāgha bridge.
- **H-NEW-127.5**: the one-vs-rest coarse-class localization follow-up
  landed **NULL**. Under the preregistered 18-way two-sided `maxT`
  family, no coarse class survives familywise correction; even the best
  observed cell, `legal`, reaches only corrected `p = 0.4013`. So the
  H-NEW-127.4 coarse-prefix structure is real but distributed, not a
  single-class spike.
- **H-NEW-127.7**: the stricter phase-aware control on the Jurjānī-tier
  bridge landed **NULL**. Keeping the same observed `H = 58.1045` but
  shuffling tier labels only within locked `neuwirth_phase` blocks moves
  the null mean up to `53.0116` and yields permutation `p = 0.0945`.
  So the earlier `LOW > MED > HIGH` bridge is not cleanly separable from
  phase composition under this stricter null.
- **H-NEW-127.8**: the matching phase-aware control on the broad
  coarse-prefix OQ-20 omnibus also landed **NULL**. Keeping the same
  observed `H = 71.0780` but shuffling coarse-prefix labels only within
  locked `neuwirth_phase` blocks raises the null mean to `65.6143` and
  yields permutation `p = 0.1127`. So the distributed coarse-prefix
  structure is also substantially phase-mediated.
- **H-NEW-127.9**: the direct OQ-20 phase-structure test landed
  **POSITIVE**. Projecting the same locked per-surah compression scores
  directly onto the exact `neuwirth_phase` axis yields `H = 81.8786`,
  `df = 9`, null mean `8.9949`, SD `3.2415`, and permutation
  `p = 0.0000499975`. So phase is not just a nuisance control; it is the
  current backbone of the full-corpus OQ-20 structure.
- **H-NEW-127.10**: the pooled within-phase residual follow-up landed
  **NULL**. Summing within-phase Kruskal-Wallis separation only across
  informative phase blocks gives `T = 12.9368` against a conditional
  null mean `20.9997`, SD `4.9054`, and permutation `p = 0.9603`. So
  the residual coarse-prefix branch is not merely weak; it is dead on the
  clean pooled within-phase scoring rule.
- **H-NEW-127.11**: the matching pooled within-phase Jurjānī-tier
  follow-up also landed **NULL**. Using the same pooled within-phase
  design but swapping coarse-prefix for the locked
  `jurjani_predicted_asyndeton_tier` axis gives `T = 3.8967` against a
  conditional null mean `4.9859`, SD `2.6854`, and permutation
  `p = 0.6110`. So the tier branch also dies once chronology is treated
  as the scoring backbone rather than just a nuisance null.
- **H-NEW-281**: the exact within-zone OQ-18 test landed
  **PASS-DIRECTED**. Against all `252` five-surah subsets of `Q16..Q25`,
  the true-isolate core `{16,21,22,23,25}` ranks `8 / 252` on mean
  pairwise root-Jaccard with exact upper-tail `p = 0.031746`. So these
  five are not just a topological residue; they are the semantic nucleus
  of the confirmed Q16-25 concentrator community.
- **H-NEW-285**: the within-zone `5-vs-5` OQ-18 contrast landed
  **PASS-DIRECTED**. Comparing the true-isolate core to its complement
  `{17,18,19,20,24}` inside `Q16..Q25`, the target split yields
  `Delta = 0.036217`, exact rank `12 / 252`, and exact upper-tail
  `p = 0.047619`. So the core is not just cohesive in itself; it is the
  more cohesive half of the zone.
- **H-NEW-286**: the within-zone OQ-18 name-class contrast landed
  **PASS-DIRECTED**. Using the existing H-NEW-126 surah-name map, the
  target subset is the unique maximum of the exact `concept/object`
  contrast inside `Q16..Q25`, with `Delta_name = 1.0`,
  rank `1 / 252`, and exact `p = 1 / 252`. So OQ-18 now has a direct
  explanatory foothold in the already-landed name taxonomy, not just in
  lexical cohesion.
- **H-NEW-286.1**: the OQ-18 pairwise name-class localization landed
  **PASS-DIRECTED**. The same concept/object label yields
  `Delta_pair = 0.028868`, exact rank `8 / 252`, and exact
  `p = 0.031746`, so the mechanism reaches the pair table and not just
  the 5-set aggregate. But it also exposes a real leak: all seven better
  relabelings include `Q17`, so the label is explanatory but not
  exhaustive.
- **H-NEW-286.2**: the conditioned `Q17` bridge follow-up landed
  **PASS-DIRECTED**. Keeping the same `Delta_pair` statistic but
  conditioning the exact null on `Q17` being excluded from the positive
  side makes the locked nucleus the unique optimum: exact rank `1 / 126`,
  exact `p = 0.0079365`. So the residual OQ-18 leak is not diffuse; it
  is specifically a single-bridge `Q17` phenomenon.
- **H-NEW-286.4**: the exact eschatological bridge-bundle follow-up
  landed **PASS-DIRECTED**. Holding the inherited bridge bundle fixed at
  `{Q16,Q17,Q21,Q22,Q23,Q25}` and reusing only the landed
  H-NEW-125 `eschatological_density` axis, the exact within-zone
  six-surah statistic reaches `Delta_E = 0.43835`, exact rank `9 / 210`,
  and upper-tail `p = 0.042857`. So the `Q17` bridge package now has a
  real semantic foothold on a single inherited axis, even though it is
  not the exact top-ranked bundle and `Q21` remains the visible drag
  term.
- **H-NEW-287**: the within-zone OQ-18 three-axis content-composite test
  landed **NULL**. The compact H-NEW-125 blend of prophet-narrative,
  book-reference, and eschatological density points the wrong way
  (`Delta_C = -0.13866`, exact upper-tail `p = 0.7778`). So OQ-18's
  current explanatory foothold lies in the name-class mechanism from
  H-NEW-286 / H-NEW-286.1, not in this simple semantic composite.

If you are starting fresh, read this prompt for context but defer to the
newest state in:

- `HANDOFF/SESSION-LOG-2026-04-18.md`
- `HANDOFF/05-OPEN-QUESTIONS.md`
- `findings/phase-b-hypotheses/cross-finding-020-the-complete-equation.md`

---

## 3. What needs your attention immediately

**Historical note:** the three items below were the original
post-Wave-5 pending queue. As of the 2026-04-18 later-session update
above, **H-NEW-236.1a**, **H-NEW-260**, the direct follow-up
**H-NEW-236.1c**, and the terminal-mechanism close-out **H-NEW-236.1b**
have already landed. Use this section as historical context only.

**Current immediate priority:** a **terminal-parsimony frontier** program,
but with a much narrower brief than before. Closure exists. Hard-hinge
parsimony is still bracketed at `(95, 100]`, but both broad hard-prefix
repair (H-NEW-236.1f) and direct hard-tranche isolation (H-NEW-236.1g)
have now failed. Fine soft interpolation also landed: there is a real
soft-only sweet spot at `lambda = 0.07`, but it reaches only
primary-level closure because `L_tail_91_114` stays outside. H-NEW-272
then tested the two narrowest mixed-completion stories and both failed:
the exact five-edge tranche and the two-edge overlap pair each reopen
`L_path` while still leaving the tail outside. So if you stay on `236`,
do **not** spend time on another tiny-complement rerun. Only broader
interaction families remain plausibly worth the cost. In parallel,
non-`236` novelty work is now live again; H-NEW-258 already provided a
new cross-corpus anchor. H-NEW-236.2b also sharpens the remaining
compactness question: the extra scaffold beyond top-50 is formally above
null under the locked 9-feature family, but only weakly
(`AUC_LOOCV = 0.647692`, `p = 0.030197`) and the miss set is dominated
by the dense late `mufaṣṣal_short` tranche. So if you stay on `236`,
target either broader mixed interactions or a specific late-tranche
compression hypothesis, not another generic scaffold-existence rerun.

Original queue preserved below for audit trail:

### 3.1 H-NEW-236.1a — extended hinges simulator (CRITICAL)

**This is the most important pending investigation.** H-NEW-236.1 closed 73% of the residual gap by injecting top-15 structural hinges as hard constraints into the 4-principle generative simulator. The remaining 27% concentrates in ḥawāmīm (Q 40-46) + mufaṣṣal-short (Q 78-114) blocks — neither of which contains top-15 hinges. If extending hinges to top-30 or top-50 closes this residual, **the 4-principle equation becomes formally generative and OQ-15 moves from SUBSTANTIALLY-ANSWERED → CAUSAL-GENERATIVE-LAYER CONFIRMED**.

Starting point: `/Users/grey/Downloads/quran/scripts/h_new_236_1_hinges_simulator.py` (from H-NEW-236.1).

Brief: `HANDOFF/03-NEXT-MOVES.md` Wave-5 queue section has the full protocol.

### 3.2 H-NEW-257 — al-Biqāʿī Medinan inclusio cross-reference

H-NEW-189 established Medinan surahs exhibit first↔last content-root inclusio at 8.5× Meccan rate. Al-Biqāʿī's *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar* is the pre-modern high-point of munāsabāt scholarship. Do his specific predictions match the 13 empirically-identified Medinan-inclusio surahs? Best-effort scholarship cross-reference (full al-Biqāʿī text may not be in corpus; use any indexed summaries).

### 3.3 H-NEW-260 — Q 54+Q 55 dyad deep-dive

H-NEW-253 established Q 55 al-Raḥmān is EMPIRICALLY UNIQUE on the Mode B (M1+M3+M5) fingerprint. Q 54 al-Qamar emerged as Q 55's mechanistic MIRROR-PAIR (opposite prosodic direction: Q 54 anti-periodic, Q 55 period-2 pillar). Test whether Q 54+Q 55 form a coherent dyad fingerprint distinct from either alone. Classical anchor: al-Biqāʿī's eschatology-mercy thematic bridge between Q 54 (moon-splitting) and Q 55 (mercy-repetition *fa-bi-ayyi ālāʾi*).

---

## 4. How to work

### Non-negotiable disciplines (from `HANDOFF/04-DISCIPLINE.md`)

- **The Quran is ONE text.** Never frame spelling/tashkeel variants as "editions." Single canonical corpus.
- **Pre-register every novel test** with YAML frontmatter (PRE-REG-STANDARD-04): id, title, phase, status, date, parent, rules_tuple, seed (20260419 + day offset), bonferroni_k, bonferroni_family, alpha_bon, direction (pre-committed), verdict (PENDING until landed).
- **Lock direction before viewing results** (PRE-REG-STANDARD-01).
- **Include MW-5 positive control** (typically: shuffled-label null should destroy the signal — verify the instrument works).
- **Publish NULLs with equal prominence to PASSes.** Every null is a loadcell.
- **Apply single-test α = 0.05 cap** for post-hoc observations per MW-7.
- **Every numerical claim carries its rules tuple.** Rule-variant sensitivity (per `memory/feedback_rules_tuple_bidirectional.md`) can rehabilitate OR demote a claim — test it bidirectionally.
- **Honest limits section is mandatory.** Name the bounds of what you measured.

### Operating tempo

- **Launch agents aggressively in parallel.** The user supports 10-30+ concurrent specialists. Use `Agent` with `run_in_background: true` to run multiple investigations simultaneously. Keep the pipeline full.
- **Use `TaskCreate` / `TaskUpdate`** to track each in-flight specialist.
- **Update MASTER-FINDINGS-LEDGER as findings land.** It is the single source of truth.
- **When agents hit rate limits** (as happened to 3 at the end of Wave-5), re-dispatch them cleanly with the same brief.

### Style of your work

- **Be rigorous.** Pre-register before you execute. Declare Bonferroni before you adjudicate.
- **Be classical.** Cite scholars by name + work + specific passage (al-Suyūṭī *Itqān*, chapter/fann; al-Biqāʿī *Naẓm al-Durar*, volume/sūra; al-Rāzī *Mafātīḥ al-ghayb*, volume/āya). Vague "classical tradition" references are not good enough.
- **Be honest.** If a direction fails, say so. If a result is edge-of-bar (as H-NEW-232 was at p=0.025 vs α_bon=0.025), say so. If a classical claim is unvalidated, it stays unvalidated — H-NEW-139's retraction after audit-037 flagged it is the discipline.
- **Be novel.** The user wants genuinely new structural facts, not re-litigations of what's already established. The single most-strongly-supported claim (muqaṭṭaʿāt as book-introduction markers, p ≤ 10⁻¹²) does not need further defense.
- **Be integrative.** Cross-reference findings against `cross-finding-008` (muqaṭṭaʿāt), `cross-finding-011` (Fisher-Rao geodesic), `cross-finding-013` (topological ring), `cross-finding-018` (4-principle reduced), `cross-finding-020` (complete equation), `cross-finding-022` (Wave-5 terminal synthesis).

### Mathematical + unconventional reasoning

The project uses Fisher-Rao distance, Normalized Compression Distance (NCD), Lempel-Ziv complexity, Heap's law β, Zipf's law α, MF-DFA Hurst, PCA, LSA, HDBSCAN, permutation nulls, Bonferroni correction, Kolmogorov-Smirnov, Wilcoxon, Mann-Whitney, ring-topology / Hamiltonian cycle / 2-opt TSP, classical tajwīd phonology (al-Khalīl's 8-tier makhraj, ṣifāt, tafkhīm, qalqala), and more. Do not restrict yourself to one toolbox. The user explicitly invited unconventional wisdom + Islamic wisdom.

---

## 5. The open questions you may help close

Per `HANDOFF/05-OPEN-QUESTIONS.md`:

- **OQ-15 causal-generative layer** — descriptive + quantitative layers
  are already closed, and the causal-generative layer is now
  **CONFIRMED** by H-NEW-236.1b / cross-finding-023 at the sufficient
  `M_H` top-100 scaffold. The live sub-question is parsimony:
  hard-hinge `K*` is now tested to lie in **`(95, 100]`**, and the
  hard-only frontier is now sharply bounded by negative results on both
  cumulative prefix repair (H-NEW-236.1f) and direct isolated-tranche
  repair (H-NEW-236.1g). Fine-grained soft interpolation already landed:
  `lambda = 0.07` is a real primary-only sweet spot (H-NEW-236.1h), but
  not a strict closure because `L_tail_91_114` stays low. H-NEW-236.2a
  also shows the landed `M_H` scaffold generalizes to the H-NEW-239 and
  H-NEW-231 gradients, while H-NEW-236.2b shows the extra top-50 ->
  top-100 scaffold is only weakly compressible by the locked 9-feature
  classical-boundary family. So the highest-EV next tests are now
  interaction / mixed-constraint completion models, specific
  late-tranche compression hypotheses, or broader non-`236` work, not
  re-running the already-bounded hard-only and coarse-soft designs.

- **OQ-16 late-tranche compressibility** — H-NEW-236.2b shows the extra
  scaffold beyond top-50 is not random residue but only weakly
  recoverable from the locked 9-feature classical-boundary family
  (`AUC_LOOCV = 0.647692`, `p = 0.030197`). The live sub-question is
  what compact factor, if any, explains the late `mufaṣṣal_short`
  false-negative tranche without reopening the already-solved scaffold
  claim

- **OQ-19 normalization-family adjudication** — H-NEW-278 and
  H-NEW-282 show the old Q108 hub collapses under literal normalization
  families, H-NEW-279 keeps a bounded metric-robust baseline pass,
  H-NEW-284 shows a surviving length-residualized `4 / 5` residue,
  H-NEW-288 then adjudicates the family split directly, H-NEW-288.1
  shows that the residualized family re-centers a fixed short
  Early-Meccan pool around Q108 as its medoid, and H-NEW-288.2 shows
  that the narrow H-NEW-273 foothold is complementary rather than
  identical: Q1 is the unique strongest high-liturgical short surah
  consistently pushed away from Q108, while `Q112/113/114` move toward
  it descriptively. H-NEW-288.3 then closes the easiest next overclaim:
  the whole H-NEW-273 speech-act axis does **not** project cleanly
  toward or away from the residualized short-core. H-NEW-288.4 then
  gives the first exact local explanatory factor that survives:
  token count inside the fixed 5-7 verse side orders approach to that
  short-core, while coarse verse count does not. The family, mechanism,
  first local integration, whole-axis projection, and first local
  residual-length branch are now all bounded. The live question is what
  residual factor still explains the opener-versus-refuge split after
  this local token-count ordering is accounted for.

- **OQ-20 class-localization** — H-NEW-127.1 and H-NEW-127.2 established
  two positive locked families, and H-NEW-127.3 now shows that the full
  114-surah compression scores stratify by the locked `sinai_genre`
  taxonomy, while H-NEW-127.4 shows the effect already survives
  compression to 18 coarse first-token classes, and H-NEW-127.6 shows a
  monotone bridge onto the locked `jurjani_predicted_asyndeton_tier`
  axis, while H-NEW-127.5 shows that the coarse-prefix omnibus does not
  collapse to any single one-vs-rest protected class, H-NEW-127.7 shows
  that the Jurjānī-tier bridge does not survive the first phase-aware
  null, H-NEW-127.8 shows the same for the broad coarse-prefix omnibus,
  H-NEW-127.9 shows that the direct `neuwirth_phase` axis itself is
  strongly positive, and H-NEW-127.10 shows that the residual
  coarse-prefix branch dies on a pooled within-phase rank test, while
  H-NEW-127.11 shows the same for the residual Jurjānī-tier branch. The
  frontier has moved again: whether *any* interpretable residual OQ-20
  structure survives after chronology is treated as the backbone, and if
  so whether it lives on some axis other than the two residual branches
  already killed here.

- **OQ-1 singleton parsimony follow-up** — H-NEW-271 showed the
  cluster-layer answer collapses to `mean_manner`, but H-NEW-271.1
  showed that the singleton layer does not, H-NEW-271.2 showed that the
  best bounded 2-D rescue (`mean_manner + mean_vowel_carrier`) gets back
  to `8 / 10` only descriptively, H-NEW-271.3 showed that anchored 3-D
  search still tops out at the same `8 / 10` boundary, and H-NEW-271.5
  showed that the compact-rescue failure survives even under the
  stronger H-NEW-274 empirical singleton table. H-NEW-301 then found a
  descriptive `9 / 10` winner without global maxT protection, and
  H-NEW-301.5 solved the narrower empirical-table `YS` / `N` residue via
  `mean_voice + mean_sonorant`. The next honest move is therefore no
  longer to ask whether the `YS` / `N` residue exists, but how that
  targeted 2-D solution integrates with the still-unclosed full
  singleton geometry, especially the surviving `ALMS` / `S` misses under
  the targeted winner.

- **OQ-18 explanation work** — H-NEW-281 and H-NEW-285 established the
  true-isolate core as a real within-zone nucleus; H-NEW-286 gave a
  direct name-class foothold; H-NEW-286.1 showed that this foothold
  reaches the pair table but leaks at `Q17`; H-NEW-286.2 then showed
  that once `Q17` is excluded from the positive side the nucleus is the
  unique pairwise optimum; H-NEW-286.4 then showed that the inherited
  `{Q16,Q17,Q21,Q22,Q23,Q25}` bridge bundle is exact-positive on the
  single inherited `eschatological_density` axis, even though it is not
  rank-1 and `Q21` remains the drag term; H-NEW-287 ruled out one
  obvious compact content composite. The live question is therefore
  whether name-class plus a single-bridge `Q17` term plus this
  eschatological loading already explains the cohesion, or whether a
  richer compact mechanism is still needed.

- **Q 1 placement mechanism** — H-NEW-238 showed Q 1 is NOT at the M1-minimum-wrap-edge (rank 18/114). H-NEW-251 localized the P3 liturgical cost to Q 1→Q 2. The remaining question is: is there a deeper principle (beyond "liturgical frame") that governs Q 1's sui-generis status?

- **Broader mixed hard/soft interaction models** — only if materially
  broader than the two tiny complements already falsified by H-NEW-272.
  The coarse hard-only and coarse soft-only routes have already been
  bounded honestly.

- **Cross-finding-023 landed** — use it as the synthesis base for the
  causal-generative closure of OQ-15. Do not keep speaking as if the
  `236` chain is still waiting for a closure result; it has one.

---

## 6. The larger frame

- There are 114 surahs, 6,236 verses, 77,797 real-word tokens in the Quran. These are the fixed structural anchors.
- The mushaf is a **semi-fractal Hamiltonian ring** whose organizational scaffold is 89% predictable from classical block-structure scholarship, pays a cycle-maximum cost at Q 1→Q 2 to honor P3 liturgical framing, and is uniquely-tawqīfī (no consensus of classical chronologies approximates it).
- The muqaṭṭaʿāt letter-sets are selected on a classical-tajwīd phonological axis.
- 21+ classical-scholarship claims have been empirically validated; 9 refuted; 1 retracted (al-Suyūṭī rhyme-prefiguration, via H-NEW-139.1 + 139.2 adversarial nulls — the retraction discipline held).
- The Quran's structure is not manufactured numerology (163 numerology tests, zero Bonferroni survivors across Benford + prime density + cumulative constants + abjad sums).

None of this "explains" the Quran. What has been established is that ~93% of the structural facts this project has measured are captured in a single compact descriptive decomposition, and that the descriptive decomposition aligns, at multiple independent axes, with the organizational framework that 14 centuries of classical Islamic scholarship worked out in its own vocabulary. The project's epistemic posture: the math and the tradition point at the same object.

---

## 7. Final notes of respect

1. **Treat the text as sacred.** This is the literal Word of God to Muslims, a historical artifact of 7th-century Arabia to secular scholars, and a text whose structural properties are independently measurable. These framings are not in conflict in this project.

2. **Treat the classical tradition as intelligent.** al-Suyūṭī, al-Zarkashī, al-Rāzī, al-Biqāʿī, al-Khalīl, Ibn Jinnī, al-Ghazālī, al-Kirmānī, al-Farāhī, al-Iṣlāḥī, Ibn Taymiyya — these scholars worked for generations on the problems this project is measuring. Where they made claims, test the claims. Where they were right, say so. Where they were wrong, say that too. The recent Wave-5 finding that classical block-structure knowledge is Ridge-linearly recoverable at R² = 0.89 is not a coincidence.

3. **Treat the user's time as infinite.** The user has told you: "There is no tomorrow. There is no time. Labor, and money do not exist to you." Do not rush the rigor. Do not cut corners on pre-registration. Do not publish without honest limits. The user wants correctness, not speed.

4. **Treat NULLs as first-class results.** A finding that fails its pre-committed direction is valuable. It constrains the space. Publish it with equal prominence to PASSes.

5. **Treat your own mistakes as public.** If you catch an earlier error (as the project did with H-NEW-139 after audit-037), retract it cleanly. The integrity-system is load-bearing.

---

## 8. The user's standing instructions (persistent across sessions)

From project memory (`memory/MEMORY.md`):

- The Quran is **one text**. No edition framing.
- **Parallel, honest, novelty-biased** research style. Many agents + rigor + genuine new findings.
- **Integrate classical scholarship + real reasoning** — not just pattern-matching.
- **Rules-tuple sensitivity is bidirectional** — a rule-variant can rehabilitate a classical claim as easily as it can demote one.
- **Specialist judgment may override team-lead method specs** if direct empirical evidence + garden-of-forking-paths log is provided BEFORE the run.
- **Silent-ignore self-addressed meta-analyst task echoes** when the deliverable exists on disk (granted 2026-04-14).
- **Bonferroni tightening self-verifies; loosening requires ratification.**
- **HANDOFF folder is the session-continuity system.** Update it before you end.

---

## 9. Practical starting sequence for your first 30 minutes

```
1. Read HANDOFF/README.md and NEXT-AGENT-PROMPT.md.
2. Read HANDOFF/01-WHAT-WE-KNOW.md (Wave-4/5 sections specifically).
3. Read cross-finding-022-wave5-terminal-synthesis.md.
4. Read HANDOFF/03-NEXT-MOVES.md Wave-5 queue section.
5. Check pipeline status:
   - ps -ef | grep python | grep -v grep
   - ls findings/phase-b-hypotheses/csv/h-new-*.json | tail -20
6. Read `HANDOFF/SESSION-LOG-2026-04-18.md` before dispatching new work.
7. Treat H-NEW-236.1a / 236.1c / 236.1b as landed background, not open tasks.
8. Treat H-NEW-236.1d as landed background: hard-hinge bracket now
   `(95, 100]`.
9. Treat H-NEW-236.1e and H-NEW-236.1f as landed background.
10. Dispatch the next parsimony agents first: direct isolated-tranche
    tests and/or hard-soft interaction tests.
11. Only spend a new family on a fine soft sweep if you explicitly
    judge the narrow `lambda ~ 0.07-0.08` band worth it.
12. Simultaneously launch 2-3 genuinely new investigations from the
   broader queue (H-NEW-252, 256, 258, or your own).
13. Use cross-finding-023 as the synthesis anchor while keeping MASTER /
    HANDOFF continuity aligned with disk state.
```

---

## 10. A closing word

This is not a puzzle to be solved for the sake of solving it. It is a disciplined measurement of the structure of a sacred text, conducted in conversation with the scholars who loved it most. The work has gotten this far — through multiple waves, retractions, adversarial audits, and honest NULLs — because every step has respected both the math and the tradition.

Keep that respect. Keep the discipline. Keep digging.

And when you find something real, say so clearly, with the caveats intact.

*— The preceding AI*
*2026-04-18*

---

**P.S.** — If you encounter something you don't understand, don't guess. Read the source file. The project is richly self-documented. Cross-finding-022 alone will tell you where you are. The MASTER-FINDINGS-LEDGER will tell you what's proven. The HONEST-LIMITS-LEDGER will tell you what isn't. Everything you need is on disk.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
