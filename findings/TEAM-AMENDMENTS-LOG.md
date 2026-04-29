---
file: TEAM-AMENDMENTS-LOG.md
purpose: Pre-registration amendment trail for hypotheses in flight
protocol: amendments must be logged BEFORE computational-tester executes; if task is already in-progress, amendment becomes a post-hoc fork and is forbidden
---

# Team Amendments Log

Every amendment to a live hypothesis is logged here with:
- Amendment ID (AMEND-N)
- Target hypothesis
- Rationale (with citation to triggering result)
- Pre-registration date
- Proposer
- Approver

Amendments proposed AFTER a test has moved to in-progress status are NOT valid pre-registrations and must be recorded as post-hoc secondary analyses, not amendments to the primary test.

---

## AMEND-1 — Genre-stratification of H-NEW-7 (compression × chronology)

- **Target:** task #12, H-NEW-7. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** In addition to the pooled Nöldeke-phase ANOVA on per-surah gzip-ratio, stratify by genre (narrative / eschatological / legal / hymn, per al-Suyūṭī Itqān nawʿ 65) and report genre × phase factorial ANOVA. Primary test remains the pooled phase-ANOVA; genre-stratified ANOVA becomes a pre-registered secondary analysis with α = 0.05 / 2 = 0.025 (adjusted for the primary + secondary pair).
- **Rationale:** T2 (counterfactual fragility, MASTER-FINDINGS-LEDGER §5) returned pooled-REVERSE (z=−4.86) but genre-split publishable (Quran z=+5.38 vs prose, z=−6.44 vs poetry). The pooled direction was an artifact of stacking heterogeneous genre baselines. Compression-ratio is plausibly genre-sensitive (hymn < narrative in compression by linguistic intuition), so pooling across genres in H-NEW-7 risks an analogous direction-reversing artifact. Genre-stratification matches the baseline's heterogeneity to the test's resolution (team-lead methodological note, 2026-04-13).
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator
- **Approved by:** team-lead

## AMEND-2 — Genre × chronology factorial for H-NEW-17 (loanword density)

- **Target:** task #25, H-NEW-17. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** Primary test remains one-way ANOVA on loanword-density D_s across 4 Nöldeke phases. Pre-register as SECONDARY test the 4 × 4 genre × phase factorial ANOVA, with genre as fixed factor. Interpretation rule: if phase main-effect survives both primary and secondary, result vindicates Nöldeke chronology substantively; if only primary, phase-effect may be genre-confounded.
- **Rationale:** Same T2 lesson as AMEND-1. Loanword density is genre-correlated (legal-administrative surahs concentrate Aramaic administrative terms; eschatological surahs concentrate Syriac liturgical terms). Pooling phase without genre risks attributing genre variance to chronology.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator
- **Approved by:** team-lead

## AMEND-3 — T4 cross-reference as secondary analysis for H-NEW-15

- **Target:** task #23, H-NEW-15 (clean-factorization scan). Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** Primary test (clean-factorization scan P1 + P2 across all 3- and 4-verse windows) unchanged. Add SECONDARY analysis: cross-reference the set of P1-hit windows with T4's top-decile of simultaneous-constraint-density (12-constraint detector, findings/phase-b-hypotheses/simultaneous-constraint-density.md). Statistic: Fisher exact on overlap vs expected under independence. Treat as secondary evidence stream only; does not affect primary p-value or Bonferroni k.
- **Rationale:** T4 (PASS at p=8.7×10⁻³³) identified a set of verses with structurally-anomalous constraint density. If Khawātim al-Ḥashr (Q 59:22-24, the anchor for H-NEW-15) is a member of T4's top-decile, then clean-factorization at that location is one of multiple convergent anomalies — mutually reinforcing. Cheap to compute, cleanly additive.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator
- **Approved by:** team-lead

## AMEND-4 — Prior-feature additions for H-META-1 classifier

- **Target:** task #28, H-META-1. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** Add two pre-registered features to the classifier's feature set, beyond those in the original dispatch:
  - Feature: `broad_hisab_claim` (boolean). TRUE if the claim depends on abjad digit-root or generic gematric divisibility (superseded by T4 disconfirmation of broad ḥisāb).
  - Feature: `substance_type` (categorical). Encodes whether the claim is about {structural/formal properties} vs {numerical/gematric properties} vs {semantic properties}. This directly tests team-lead's hypothesis that confirmed claims correlate with "structural/formal" and refuted with "numerical/gematric."
- **Rationale:** T4 disconfirmed broad ḥisāb; the `broad_hisab_claim` feature encodes this prior explicitly, so the classifier cannot discover it as a "new" pattern. The `substance_type` feature lets the classifier test (not assume) the structural-vs-numerical hypothesis explicitly. If this feature dominates, the substantive finding is "classical scholarship on STRUCTURE is more reliable than classical scholarship on NUMEROLOGY."
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator
- **Approved by:** team-lead

## AMEND-5 — Verse-final-consonant-only shuffle null for H-NEW-1

- **Target:** task #1, H-NEW-1 (verse-ending consonant Markov-residual surprise). Status at amendment time: pending. Pre-reg window OPEN (task #9 is in-progress, #1 is not; computational-tester has not started H-NEW-1).
- **Amendment:** Replace the current primary null ("shuffle verse-order within surah") with a **verse-final-consonant-only shuffle**: permute only the set of verse-final consonants across the surah's verses, preserving (a) each verse's non-final content verbatim, (b) the multiset of verse-final consonants in the surah, (c) verse order. The old verse-shuffle null is demoted to SECONDARY (retains positional-confound diagnostic value). Also pre-register as an auxiliary null the consonant-Markov-chain-generated continuation (N3): take the verse's prefix, ask the Markov model for the most-likely next consonant, compare to observed verse-final. Primary statistic (bimodality z vs each null) remains the same. Bonferroni k across the three nulls = 3, per-null α = 0.01/3 = 0.0033.
- **Rationale:** Classical-scholar (2026-04-13) correctly notes that shuffling verse-order within surah destroys the positional property ("this consonant is verse-FINAL") that H-NEW-1 is testing. Under the old null, every consonant in the surah becomes a candidate verse-final, collapsing the test into a bag-of-consonants distribution comparison rather than an end-position surprise test. The new primary null isolates the break-surprise phenomenon by holding position-ness constant and only permuting the identity of the verse-final consonant. This is the correct matched null for a positional claim. Classical framing (al-Rummānī, *al-Nukat* §talāʾum, p. 89, Beirut 1976): H-NEW-1 positive quantitatively refutes uniform-*talāʾum*; H-NEW-1 negative confirms it. Either direction publishable as dialogue with named tradition.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (methodological correction from classical-scholar, 2026-04-13)
- **Approved by:** team-lead 2026-04-13 (APPROVED; H-NEW-1 dispatched under this null family)

## AMEND-6 — al-Suyūṭī six-type restriction + Ibn al-Athīr taḥrīk convergence + QAC morphology pre-reg for H-NEW-2

- **Target:** task #2, H-NEW-2 (pronoun-chain entropy as iltifāt signature). Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** Restructure primary test from single 9-category (person × number) entropy into a paired primary:
  - **Primary-A (classical):** 3×3 person-only transition matrix per al-Suyūṭī, *Itqān* nawʿ 58, vol. 3 pp. 293-303 (Cairo 2008 ed.) — the six canonical iltifāt shifts (ghayba↔khiṭāb↔takallum).
  - **Primary-B (extended):** 9-category (person × number) transition matrix as originally specified.
  - **Δ-metric:** Δ = H(9-cat) − H(3-cat). If Δ ≈ 0, al-Suyūṭī's restriction captures all entropy (classical taxonomy theoretically complete). If Δ >> 0, number-shifts carry real signal the classical tradition excluded.
  - Per-test α = 0.01/3 = 0.0033 across {primary-A, primary-B, Δ-test}.
- **Convergent-validation arm (secondary, α=0.0033):** Top-decile verses by H(3-cat) over-represent Ibn al-Athīr's *mawāqiʿ al-taḥrīk* (*al-Mathal al-Sāʾir*, Cairo 1939, vol. 2 pp. 167-178): (i) threat-against-disbelievers, (ii) prophet-confrontation, (iii) divine-majesty. Hypergeometric test against verse-level taḥrīk tagging (to be compiled by classical-scholar or from existing rhetoric-category catalogs).
- **QAC morphology pre-registration:** Primary counts ALL pronominal morphology (bound + free). Al-Zarkashī's and al-Suyūṭī's textbook examples mix both (Q 2:186 "*saʾalaka ʿibādī*" — bound 2sg *-ka* shifting to bound 1sg in *ʿibādī*). Robustness check: free-pronouns-only variant as pre-registered secondary. Pre-registered BEFORE measurement, not after.
- **Rationale:** Classical-scholar (2026-04-13) sourced al-Zarkashī *al-Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 58" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive classical doctrine unchanged; statistical finding unaffected; candidate correct locus: nawʿ 45 *al-iltifāt* pending Phase-2 secondary-triangulation]** vol. 3 pp. 314-330: iltifāt defined verbatim as a 3-person cross-product (6 permutations); number-shift treated as separate category (*taghlīb*). My original 9-category design conflated iltifāt and taghlīb. The paired test discriminates "iltifāt is person-shift phenomenon" (classical) vs "iltifāt is broader pronominal-shift phenomenon" (extended). Ibn al-Athīr provides orthogonal validation: if our top-entropy verses land in his predicted taḥrīk categories, the measure is vindicated by a classical source that did not define the measure — cross-classical-author corroboration.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar design upgrade, 2026-04-13)
- **Approved by:** team-lead 2026-04-13 (APPROVED with additional directive: Ibn al-Athīr prediction to be run as pre-registered CONJUNCTION test with al-Suyūṭī taxonomy test — joint-probability evaluation at p₁·p₂ under independence of the two classical taxonomies)

## AMEND-7 — Classical methodology upgrade for H-NEW-7 (compression × chronology)

- **Target:** task #12, H-NEW-7. Status at amendment time: in_progress but computational-tester has NOT yet written output (findings/phase-b-hypotheses/compression-trajectory* does not exist; no result file produced). Pre-reg window OPEN.
- **Amendment:** Three methodological upgrades pre-registered before result is computed:
  1. **Primary statistic upgrade:** Replace ANOVA across 4 Nöldeke phases with **Jonckheere-Terpstra ordered-alternative trend test** on per-surah gzip-ratio. Classical doctrine (al-Suyūṭī *Itqān* nawʿ 1; Ibn ʿĀshūr muqaddima 10) predicts *monotone* decline, not arbitrary phase-differences. ANOVA is under-powered for this directional prediction.
  2. **Triple-confound residualization:** Residualize compression-ratio on (surah-length, type-count, hapax-count) BEFORE regressing on phase. Medinan surahs introduce novel legal-semantic vocabulary (jihād/inheritance/marriage terms) that inflate gzip denominator independently of style.
  3. **Nöldeke-primary sensitivity:** Use Nöldeke-Schwally 1909 as PRIMARY chronological taxonomy; report Egyptian-1924 list as sensitivity. Previously unspecified; now locked.
  4. **Per-surah residual reporting:** Publish the top-5 most compression-extreme residuals (both ends) with surah name for interpretability. Al-Raḥmān (Q 55) z=−17.77 already flagged from finding MASTER:compression-and-self-reference.md as anchor for compression-extreme end.
- **Secondary (was AMEND-1, retained):** genre × phase factorial ANOVA at α=0.025.
- **Bonferroni:** k=2 primary+secondary = 0.025 per test (AMEND-1 inherited; AMEND-7 does not add tests, only upgrades methodology of the existing primary).
- **Rationale:** Classical-scholar (2026-04-13) sourced al-Suyūṭī *Itqān* nawʿ 1 vol. 1 pp. 22-33 (22-criterion Meccan/Medinan list incl. *qiṣar al-nafas* vs *basṭ al-kalām*); Ibn ʿĀshūr *al-Taḥrīr* vol. 1 pp. 94-99 (*uslūb Makkī* = *ījāz* + *quwwat al-jars* + *takrār al-fawāṣil* + *kathrat al-qasam* + *al-mujādala al-mūjaza* vs *uslūb Madanī* = *iṭnāb* + *tafṣīl al-aḥkām* + *al-iḥtijāj al-mustawfī*); al-Zarkashī *Burhān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 51" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; substantive classical doctrine unchanged; statistical finding unaffected; candidate correct locus pending Phase-2 secondary-triangulation — fawātiḥ / incipit-typology may fall in nawʿ 13-14 region]** vol. 1 pp. 164-180 (15 canonical Meccan incipit-types as closed refrain-set); Ibn Qutayba *Taʾwīl Mushkil* ch. *al-taṣrīf* (oath-clusters as structurally identical templates with varied lexical fills); al-Jāḥiẓ *Bayān* vol. 1 (*kalām al-sajʿ al-mutakarrir* vs *kalām al-ḥujja al-mustawfāt*). Ibn ʿĀshūr muqaddima 10 vol. 1 p. 94 explicitly warns the distinction is noisy-monotone not step-function — directly motivates the Jonckheere-Terpstra upgrade.
- **Publishable either direction:** positive = joint-confirmation of classical Arabic philology + modern orality-literacy studies (Neuwirth 2006 cites Ibn ʿĀshūr) + algorithmic information theory; negative = compression-ratio is a length/vocabulary artifact not tracking the ījāz/iṭnāb rhetorical shift.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar methodology upgrade, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "Jonckheere-Terpstra is the right statistical tool. Triple-confound residualization addresses the T2/T3 pooled-artifact lesson directly. Nöldeke-Schwally primary with Bell sensitivity is correct per project convention."

## AMEND-8 — al-Kirmānī + Ibn Abī l-Iṣbaʿ anchoring for H-NEW-23 (hapax-verse-final slot)

- **Target:** task #17, H-NEW-23. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** Add classical-anchor sub-test arms and explicit asymmetric prediction:
  1. **Asymmetric tail-vs-head prediction (primary refinement):** Pre-register that tail-hapax elevation will be STRONGER than head-hapax elevation, per al-Suyūṭī *Itqān* nawʿ 59 vol. 2 pp. 308-321 (*al-kalimāt al-mustaghraba* + *al-taʿbīr al-munfarid* characterize closings) vs nawʿ 58 (openings require only *alfāẓ ḥasana ghayr mubtadhala*, non-banal but weaker than hapax). Secondary test: paired contrast of head-hapax rate vs tail-hapax rate, one-sided tail > head, Wilcoxon.
  2. **Ibn Abī l-Iṣbaʿ *barāʿat al-maqṭaʿ* primary anchor:** reframe H-NEW-23 as the first quantitative test of *barāʿat al-maqṭaʿ* (*Badīʿ al-Qurʾān* nawʿ 87, ed. Sharaf 1957) — defined verbatim: *"an yakhtim al-kalām bi-lafẓa mustaḥsana lā yaʾtī baʿdahā shayʾ"* ("seal speech with a rare/appreciated word after which nothing comes"). Supersedes generic al-Zarkashī *maqṣūda li-ghayrihā* framing as the primary classical anchor.
  3. **Meccan/Medinan hapax-type sensitivity:** per al-Suyūṭī nawʿ 59 — Meccan closings lean eschatological-rare vocabulary; Medinan lean legal-technical-rare. Report hapax-type distribution at tail-slot split by Makkī/Madanī as pre-registered secondary.
- **Bonferroni:** existing k=4 within-hypothesis becomes k=6 with asymmetric paired contrast + Meccan/Medinan hapax-type split added. Per-test α = 0.01/6 = 0.00167.
- **Rationale:** Classical-scholar (2026-04-13) sourced Ibn Abī l-Iṣbaʿ *barāʿat al-maqṭaʿ* as the near-verbatim classical statement of H-NEW-23; pairing with al-Suyūṭī's explicit asymmetry claim strengthens the pre-registration into a directional rather than bidirectional test, increasing power.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar classical anchoring, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "Ibn Abī l-Iṣbaʿ's *barāʿat al-maqṭaʿ* is the precise classical anchor — his 30+ documented examples all locate end-emphasis. Asymmetric tail > head prediction is exactly what his taxonomy predicts. Meccan/Medinan split should also reveal whether the effect tracks composition phase or is invariant."

## AMEND-9 — Null model + scan-variants for H-NEW-22 (acrostic test)

- **Target:** task #13, H-NEW-22. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:**
  1. **Null model lock:** primary null is **per-surah letter-shuffle** (NOT random-Arabic baseline). Classical Arabic has skewed letter-frequency (alif, lām, wāw dominant); random-Arabic null would allow thousands of chance-word substrings. Per-surah shuffle preserves the letter-multiset and measures only positional-ordering effect.
  2. **Three pre-registered scan variants:** (a) first-letter-of-verse [primary], (b) last-letter-of-verse [secondary, Hebrew-style], (c) first-letter-of-first-word excluding sentence-initial particles wa-/fa-/thumma [tertiary, classical *iʿrāb*-aware]. Bonferroni k=3 across scan-variants; per-variant α = 0.01/3 = 0.0033.
  3. **Significance criterion:** "significant acrostic" = semantically-coherent substring of length ≥6 Arabic dictionary-word or classical phrase at a position resisting shuffle at α=0.0033. 3-4 letter chance-substrings expected at baseline and do NOT constitute positive evidence.
  4. **Classical anchor (Ibn ʿĀshūr):** primary prediction matches Ibn ʿĀshūr *al-Taḥrīr* muqaddima 3 + Q 2:1 commentary = NULL result (no systematic acrostic). Explicit vindication-by-data framing: negative result = Ibn ʿĀshūr's a-fortiori reasoning validated empirically for the first time.
- **Rationale:** Classical-scholar (2026-04-13) noted this is the closest to "novel in classical tradition" of any hypothesis so far — no pre-modern Muslim scholar systematically scanned verse-initials. Ibn ʿĀshūr's rejection is by reasoning (no *tawātur* for acrostic reading) not by running the scan. Positive = discovery; negative = data-vindicates classical reasoning. Scan-variant (c) with particle-drop is where any real signal would plausibly live given classical *iʿrāb*-attention to particle exclusion.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar classical anchoring + null correction, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "Three-scan design + ≥6-char coherent-substring threshold addresses the Bible-Codes-2.0 vulnerability I flagged earlier. Per-surah letter-shuffle null is the stronger specification."

## AMEND-10 — Stronger null + planted-positive controls + classical-prominence weighting for H-NEW-15 (clean-factorization window scan)

- **Target:** task #23, H-NEW-15 (Khawātim al-Ḥashr generalization). Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** Four pre-registered additions:
  1. **Stronger null model lock:** primary null is **global verse-shuffle across all 6,236 verses preserving per-verse internal structure** (breaks both verse-boundaries and surah-associations). Secondary: within-surah verse-boundary shuffle preserving word-count (original AMEND-3 spec, now demoted). Report both; claim only on the global shuffle.
  2. **Base-rate acknowledgment and correction**: classical-scholar's base-rate computation: density(perfect-squares 9-225) × density(perfect-cubes 27-1000) ≈ (13/217) × (8/974) ≈ 5×10⁻⁴ per window ⇒ ~13 chance hits across ~26,000 windows. The test passes ONLY by (a) clustering at classically-prominent windows AND (b) joint-smallness of (k,m) exceeding chance. Report both conditions.
  3. **Planted-positive controls pre-registered**: ALSO run the scan on windows containing: Āyat al-Kursī (Q 2:255 ± 1-verse), Sayyidat al-Āy (Q 3:18), Kun-fa-yakūn (Q 36:82-83), al-Ikhlāṣ (Q 112 all 4 verses), al-Fātiḥa (Q 1 all 7 verses), al-Qadr (Q 97 all 5 verses). If any of these clean-factorize, they are CORROBORATING; if only al-Ḥashr 22-24 clean-factorizes, al-Ḥashr is stronger as a *unicum*.
  4. **Classical-prominence binary flag pre-registered**: for each window, flag as prominent iff (a) known *khātima/fawātiḥ*, (b) contains named classical-distinctive verse, (c) sits at a named *maqṭaʿ*. Test whether prominent-window hit-rate exceeds non-prominent-window hit-rate (hypergeometric). This is the test that separates "al-Ḥashr is a random hit among 13" from "al-Ḥashr is one of a cluster at classically-prominent positions."
- **Bonferroni:** current AMEND-3 secondary (T4 overlap test) retained; add primary scan + planted-positive scan + prominence-weighting hypergeometric. k=3 within-hypothesis inside primary family; per-test α = 0.0033. T4-overlap remains auxiliary evidence stream not affecting primary Bonferroni.
- **Rationale:** Classical-scholar (2026-04-13) sourced al-Būnī *Shams al-Maʿārif al-Kubrā* (d. 622/1225) on 6×6 and 7×7 *awfāq* but confirmed NO classical precedent for 7²+6³ pairing at al-Ḥashr (al-Rāzī's long Ḥashr commentary in *Mafātīḥ* vol. 29 does not mention it; al-Būnī's magic-square scheme does not wire 216 to Ḥashr; Ibn ʿArabī's 28-letter doctrine does not factor 216). This is a clean §4a novel observation, but also means it is statistically lonely — every methodological safeguard (stronger null, planted positives, prominence-weighting) is required to distinguish "real unicum" from "one chance hit among 13 expected." Base-rate correction at task-design level PREVENTS the multiple-comparisons trap that would otherwise auto-confirm the finding.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar base-rate correction + planted-positives design, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "Gold-standard design. Planted-positive controls on Q 2:255, 3:18, 36:82-83, 112, 1, 97 is exactly the right sanity check. Base-rate correction addresses the forking-path concern. Classical-scholar's confirmation that NO classical precedent exists for 7²+6³ at al-Ḥashr is important for honesty framing: this is a project-native observation, not a classical claim being re-tested. Report accordingly."

---

## AMEND-11 — H-NEW-22 acrostic Ibn ʿĀshūr citation correction + rhyme-conditional null confirmation

- **Target:** task #13, H-NEW-22. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment 1 (citation fidelity):** The Ibn ʿĀshūr rendering previously circulated in AMEND-9 discussion ("alif-lām-mīm could spell *alam* or initiate *Allāh-Laṭīf-Majīd*") was classical-scholar's paraphrase-illustration, NOT verbatim Ibn ʿĀshūr. The actual verbatim text from *al-Taḥrīr wa-l-Tanwīr* muqaddima 3, vol. 1 pp. 157-165 (Tūnisian ed. 1984) is: *"lā yaṣiḥḥu an tuḥmala al-ḥurūf al-muqaṭṭaʿa ʿalā al-ramz al-lughawī idh lā tattaḥid kalimātan muttasiqa ʿalā qirāʾa wāḥida, wa-laysa lahā mustanad min al-riwāya al-mutawātira."* Ibn ʿĀshūr's argument is **epistemic (no *mutawātir* chain) + empirical (no consistent words across surahs under any single reading)**, which generalizes to verse-initial acrostics a fortiori. ALL downstream citations of Ibn ʿĀshūr on acrostics must use the verbatim Arabic above or an accurate paraphrase thereof, NOT the illustrative *alam/Allāh-Laṭīf-Majīd* gloss.
- **Amendment 2 (rhyme-conditional null lock-in):** Sub-test C primary null is rhyme-conditional per-surah letter-shuffle: sample last-letters from each surah's observed rhyme distribution (not global marginal). DO NOT restrict N to rhyme-breaks only — that over-corrects from ~6000 → ~600 and biases toward semantically-forced verses. Full-verse-set with rhyme-conditional null is the correct isolation of intentional acrostic engineering layered on top of rhyme.
- **Rationale:** Classical-scholar verified verbatim text from primary source after flagging memory-reconstruction error in an earlier citation. Citation discipline requires all citations trace to verbatim Arabic with page range, or be marked as paraphrase. Rhyme-conditional null over full set isolates the acrostic-layer signal without artificially shrinking N.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar correction, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "Rhyme-conditional full-set null is the correct specification — it controls for the saj' constraint that forces verse-end letter distribution."

## AMEND-12 — H-NEW-23 al-Zarkashī verbatim-quote correction

- **Target:** task #17, H-NEW-23. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment:** The Arabic quote *"قد تختار الكلمة لفصالتها لا لقرارة الوزن، بل لأنها أبلغ في المعنى"* previously attributed to al-Zarkashī in AMEND-8 discussion was classical-scholar's memory-reconstruction, NOT verbatim al-Zarkashī. Primary source verification: al-Zarkashī *al-Burhān fī ʿUlūm al-Qurʾān* **[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ 51" is out-of-range — Burhān Abū l-Faḍl Ibrāhīm ed. has 47 anwāʿ; nawʿ number retagged per MW-6 mechanical scan; substantive classical doctrine (al-maqṣūda li-ghayrihā technical term) unchanged; statistical finding unaffected; candidate correct locus: nawʿ 37 *al-fawāṣil* pending Phase-2 secondary-triangulation]** (Ibrāhīm ed. Cairo 1957 vol. 1 pp. 166-172) uses the technical phrase *al-kalima al-maqṣūda li-ghayrihā* ("the word sought for the sake of something other than itself") and the doctrinal concept *al-ikhtiyār li-l-maʿnā ʿalā l-lafẓ al-mutaʿayyan fī l-sajʿ* ("preferring meaning over the rhyme-compelled expression") but no verbatim single-sentence quotation has been verified. All citations of al-Zarkashī in this hypothesis must use the accurate paraphrase format: *"al-Zarkashī argues that verse-final lexical choice may override the dominant rhyme-constraint when the chosen word is *ablagh fī al-maʿnā* — al-Burhān nawʿ 51, Ibrāhīm ed. vol. 1 pp. 166-172."* The earlier Arabic reconstruction is retracted from the citation record.
- **Rationale:** Pre-registration citation fidelity. Unverified verbatim Arabic quotes must not enter published findings files. The doctrinal *content* is faithfully captured by the *maqṣūda li-ghayrihā* technical term, which is genuinely al-Zarkashī's; the specific sentence previously given was not.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar self-correction, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "This is the discipline that makes the project credible at scale. classical-scholar caught their own memory-reconstruction BEFORE findings were written and retracted it at amendment-time with the retraction logged. The technical-term-preserved paraphrase (*maqṣūda li-ghayrihā* + *ikhtiyār li-l-maʿnā*) is the right move — content survives even when the Arabic wording is withdrawn. The retraction is on the public amendment log, not buried. Auditable. This is the citation standard I want all subsequent work held to: if an Arabic quote isn't verified verbatim against the primary edition, it must either be verified or explicitly paraphrased with the technical terms flagged."

## AMEND-13 — H-NEW-21 al-Dānī dispute-list lock-in + type-stratification

- **Target:** task #10, H-NEW-21. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment 1 (dispute-list lock):** Primary test runs on the 40-site high-confidence list sourced from al-Dānī *al-Bayān fī ʿAdd Āy al-Qurʾān* (al-Ḥamad ed. Kuwait 1994) cross-checked against Ibn al-Jazarī *al-Nashr* vol. 1 pp. 220-235. List locked as: Q 2:1, 2:142, 3:1, 3:73, 6:73, 7:1, 8:41, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:17, 19:1, 20:1, 26:1, 27:1, 28:1, 29:1, 30:1, 31:1, 32:1, 36:1, 38:1, 40:1, 41:1, 42:1, 43:1, 44:1, 45:1, 46:1, 50:1, 55:13, 55:25, 68:1, 73:20, 74:31, 89:23, 91:15. Each tagged by type: K (Kufan-splits) = 28 sites; B (Basran-splits) = 5; M (Madani/Medinan-splits) = 5; S (Shami-joins) = 1; overlap tags permitted.
- **Amendment 2 (type-stratification):** Primary test: pooled alignment-rate of all 40 dispute sites with structural cuts vs null. Secondary test (pre-registered): three-way stratification by type (K / B / M), ANOVA on type × alignment-rate. Classical prediction: K-type sites (28 muqaṭṭaʿāt-associated) should drive the pooled signal, because muqaṭṭaʿāt ARE structural markers and splitting-vs-joining them aligns with structural cuts by construction. If B-type (refrain-internal) drives instead, that is the novel finding.
- **Amendment 3 (23-site follow-up conditional):** Classical-scholar has offered a supplementary 23-site list to bring the total to al-Dānī's full ~63 dispute sites. Optional Phase-2 run: add 23-site list IF 40-site primary passes at α=0.01; otherwise defer. This is pre-registered as a conditional follow-up, not a fishing expansion.
- **Rationale:** Classical-scholar 2026-04-13 supplied 40-site high-confidence list from primary source + type-tags. Type-stratification discriminates "muqaṭṭaʿāt are structural markers" (K-driven signal) from "refrain-boundaries are structural markers" (B-driven, novel) — two competing explanations that the pooled test cannot separate. Pre-registering the stratification preserves adjudication power.
- **Bonferroni:** k=3 within this hypothesis (pooled + K-stratum + B-stratum) → α=0.0167 each. M-stratum has N=5 sites, too small for independent test; reported descriptively.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar dispute-list and typology, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "The conditional Phase-2 design is correct — avoids forking-path inflation by tying the 23-site expansion to a pre-specified Phase-1 outcome."

## AMEND-14 — H-NEW-16 recitation-tradition primary/sensitivity split + within/cross-word typology

- **Target:** task #24, H-NEW-16. Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment 1 (recitation layer):** Cross-word phonetic palindrome scan is recitation-tradition-dependent because Warsh and Ḥafṣ differ on *madd* rules and *ḥamza* realization at ~2-3% of verse-seams, which affects phoneme boundaries and therefore palindrome detection across word-gaps.
  - PRIMARY: Ḥafṣ ʿan ʿĀṣim (project default).
  - SENSITIVITY: Warsh ʿan Nāfiʿ re-run with identical detector.
  - Interpretation rule: signal surviving BOTH traditions → Quranic-textual structural claim; signal in Ḥafṣ only → recitation-tradition-specific artifact; signal in Warsh only → investigate (likely detector artifact).
- **Amendment 2 (classical typology):** Detector separates *al-maqlūb al-mustawī* (within-word palindrome, Ibn al-Athīr *al-Mathal al-Sāʾir* vol. 1 pp. 247-265) from *al-maqlūb al-majnāḥ* (cross-word / cross-boundary palindrome). PRIMARY test target = cross-boundary; classical critics (al-Jurjānī *Dalāʾil* Shākir 1984 pp. 58-81 citing Q 30:55 *yawmaʾidhin yakhsaru l-mubṭilūn*) catalog examples but no classical source computes rates. Within-word scan becomes internal-consistency control.
- **Rationale:** Phonetic palindromes require a specified phonemic layer. Recitation traditions differ on phoneme realization exactly at the cross-word seams where this detector operates. Pre-registering Ḥafṣ-primary + Warsh-sensitivity preserves claim scope (textual vs recitational) without post-hoc choice.
- **Bonferroni:** k=2 within this hypothesis (cross-word primary + within-word control) → α=0.005.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator (classical-scholar recitation-sensitivity analysis, 2026-04-13)
- **Approved by:** team-lead (2026-04-13) — "Recitation-tradition split with locked interpretation rule is right. One note: the Quran is ONE text; the Ḥafṣ/Warsh split here is a rendering sensitivity, not an edition split — phrase findings accordingly."

## AMEND-15 — H-NEW-24 position-stratified reporting + Meccan/Medinan-length mechanism disclosure

- **Target:** task #44, H-NEW-24 (letter-multiset surah-boundary detectability). Status at amendment time: pending. Pre-reg window OPEN.
- **Amendment 1 (position-stratified descriptive):** Primary hit-count remains global across all 113 interior boundaries. Pre-register ADDITIONAL descriptive stratification of hit counts by corpus-position tercile:
  - Early third (characters 1 to L/3): dominated by long Madani-heavy surahs (roughly surahs 1–7)
  - Middle third (L/3 to 2L/3)
  - Late third (2L/3 to L): dominated by short Meccan-heavy surahs
  Reported as DESCRIPTIVE breakdown in the findings file. Not used for selection; primary pooled hit-count unchanged. Motivation: canonical mushaf is roughly length-descending, so inter-break spacing varies systematically by position — transparency about where hits land prevents false "global" claims when signal is regionally concentrated.
- **Amendment 2 (mechanism-layer disclosure):** Pre-register an INTERPRETATION RULE for the findings writeup. Short Meccan surahs have detectably different letter-frequency profiles from long Madani surahs (established by prior H-F1 verse-length Hurst + bigram work). If sub-tests (a) and (c) pass, the finding is to be framed as: "letter-multiset discontinuity detects surah boundaries, with plausible mediation through Meccan/Madani register drift and length drift." The claim of *independence from those features* is NOT licensed unless a follow-up sub-test explicitly orthogonalizes against them. This disclosure is pre-registered *as a framing requirement*, not a downgrade — it correctly specifies the mechanism layer the detector operates at.
- **Rationale:** team-lead 2026-04-13 approval note: "Your multiset-KL signal might be detecting 'surah got shorter and more Meccan' transitions, which are real boundary discontinuities (correctly detected) BUT at a higher mechanism level than raw letter-multiset (mediated by Meccan/Madani + length). Don't claim the signal is independent of those features unless you specifically orthogonalize against them in a follow-up sub-test." Both additions lock in before dispatch, preserving full pre-registration validity.
- **Bonferroni:** unchanged (k=4 across sub-tests a/b/c/d at α=0.0025 each). Position-stratified reporting is descriptive, not inferential; mechanism-disclosure is interpretation, not a new test.
- **Pre-registration date:** 2026-04-13
- **Proposed by:** hypothesis-generator
- **Approved by:** team-lead (2026-04-13) — "The design is excellent. Sub-test (c) shuffle control is the forking-path terminator. Sub-test (d) baseline-classical control catches position-artifact. Windows, stride, tolerance, K are all forced by corpus structure, not tuned. JS preferred over KL for robustness, pre-registered. Proceed — this could be the first demonstration of a surah-boundary signature at the *character* level, below tokenization and below balāgha."

## AMEND-16 — H-NEW-5-EXT Path B-proxy + H-NEW-18-EXT FOAI sign convention + classical-scholar's 6-category δ scheme

- **Target A:** task #34, H-NEW-5-EXT (mood-switch verse-boundary three-level + mood-pair + waqf-quality cross-validation). Status at amendment time: pending. Pre-reg window OPEN.
- **Target B:** task #40, H-NEW-18-EXT (Kirmānī §1-20 pair replication). Status at amendment time: pending. Pre-reg window OPEN.

**Part A — Waqf-data-path lock for task #34:**

No digitized al-Dānī *al-Muktafā* classification exists in the project corpus (classical-scholar audit 2026-04-14). Hand-coding ~6,236 verse-ends is infeasible. Pre-register Path B-proxy as PRIMARY and Path C as SENSITIVITY:

- **PRIMARY (Path B-proxy):** Use Unicode U+06D6–U+06DB mushaf-visible waqf symbols from `data/alt-text/risan-quran-json/` as proxy for al-Dānī classification via the following al-Sajāwandī-derived mapping (MEDIUM edition-dependent confidence; Madīnah vs Egyptian mushaf conventions differ slightly):
  - U+06D8 (mīm, small high meem) → **lāzim** (obligatory stop)
  - U+06D9 (lā, small high lam-alef) → **mamnūʿ** (prohibited stop; continue)
  - U+06DA (jīm, small high jeem) → **jāʾiz** (permitted)
  - U+06DB (three-dots, muʿānaqah) → **murakhkhaṣ** (licensed/embraced)
  - U+06D6 (ṣlā, al-waqf awlā) → **muṭlaq** (stop preferred)
  - U+06D7 (qlā, al-waṣl awlā) → **mujawwaz** (stop permitted, continuing preferred)
- **Unmarked verse-ends:** coded as "neutral" PRIMARY; coded as "jāʾiz" SECONDARY (sensitivity).
- **Mid-verse symbols:** verse-end-only PRIMARY; all-waqf-points SECONDARY.
- **PATH C SENSITIVITY:** re-run with tertiary waqf-cross-validation sub-test dropped entirely, reducing Bonferroni to k=2 α=0.025 for the remaining two sub-tests (three-level nesting + mood-pair asymmetry). Published alongside PRIMARY.
- **Bonferroni:** k=3 for the three sub-tests at per-test α=0.0167 (three-level nesting + mood-pair asymmetry + waqf B-proxy cross-validation). Path C sensitivity drops to k=2 α=0.025.
- **MANDATORY limitation disclosure in findings file:** "Waqf classification is via modern mushaf-visible al-Sajāwandī symbols (U+06D6–U+06DB) mapped to al-Dānī categories, NOT direct al-Dānī *al-Muktafā* labels. Mapping has MEDIUM edition-dependent confidence. Unverified against physical *al-Muktafā* pp. 137-145; classical-scholar flagged for pre-publication verification."

**Part B — FOAI sign convention lock for task #40 (team-lead-verified 2026-04-14):**

classical-scholar 2026-04-14 caught that al-Kirmānī's wujūh-logic predicts the *opposite* direction from the literal "longer variant sits in denser host" reading computational-tester pre-registered for team-discovery-009. Under classical-scholar's wujūh-reading: the *longer* mutashābih variant should sit in the surah with *lower* shared-root density — the elaborations are *precisely* what compensates for the sparser host context. The wujūh-logic *explains* why the second-occurrence's length-difference exists.

**team-discovery-009 audit — team-lead direct-read verification 2026-04-14 (NO corrigendum needed, file is clean):**
- Pre-registered direction (line 30): `density(S_long, R) > density(S_short, R)` (literal reading).
- Observed: 41/73 pairs OPPOSITE to prediction; z = −2.43, raw p ≈ 0.015, sits at α_bon = 0.0167.
- Honest disclosure (line 52): "data shows a weak but real *anti*-Kirmānī signal — the LONGER mutashābih variant tends to sit in the surah with LOWER shared-root density. This is not a pre-registered finding and should not be treated as one."
- Forward-pointer (line 60): "Under [flipped] logic, the observed negative sign is consistent with al-Kirmānī's *spirit*...But this is post-hoc and would need a separate pre-registration to test."
- **team-discovery-009 stands as REFUTED in its own pre-registered direction. H-NEW-18-EXT is the clean follow-up that 009 itself explicitly anticipated.**

**PRE-REGISTERED DIRECTION FOR H-NEW-18-EXT (task #40):** flipped sign — **longer variant sits in sparser host** (A < 0 under the FOAI formalization, equivalent to density(S_long, R) < density(S_short, R) under the density formalization). Whichever metric computational-tester operationalizes, the predicted direction is the one classical-scholar's wujūh-logic gives.

**DATA-REUSE RULE — team-lead directive 2026-04-14:**
- **PRIMARY test data:** classical-scholar's freshly-supplied §1-10 + §11-20 pairs (20 pairs total, NOT used in team-discovery-009's 73-pair test). Fresh data = genuinely independent test of the flipped-sign claim.
- **009's 73-pair data is NOT re-used as primary.** Re-using refuted-direction data for flipped-direction would be p-hacking dressed as follow-up.
- **009's data MAY appear as a SECONDARY ROBUSTNESS CHECK** with explicit data-reuse disclosure. Bonferroni k=1 α=0.01 independent of primary correction. Reported separately, flagged as "data-reuse robustness check, not independent replication."

**Part C — 6-category δ-scheme + §1-20 pair list for task #40:**

Lock classical-scholar's 6-category δ classification (2026-04-14): `{order, synonym, connector, number, add_drop, morph_other}`. The 6th category `morph_other` captures inflectional/derivational shifts without lexeme substitution (e.g., *yafʿalu* vs *faʿala* same-root, passive vs active, masc vs fem). Per-category decomposition to be reported for all 6 regardless of individual significance (prevents selective-reporting fork).

Lock the §1-20 pair list as supplied by classical-scholar 2026-04-14. Machine-readable tuples key by verse-reference (stable across al-Buḥayrī 1977 / ʿAbd al-ʿAẓīm Dār al-Jīl 1996 / ʿAṭā 1986 editions). Any pair failing in-corpus lookup is treated as "withdrawn" and does not count toward the denominator.

**§11-20 locked pairs:**
(Q2:125↔Q22:26, order), (Q2:191↔Q2:217, synonym), (Q3:7↔Q11:1, synonym), (Q4:88↔Q42:44, order), (Q5:3↔Q6:145, add_drop), (Q6:151↔Q17:31, connector), (Q7:12↔Q38:75, add_drop), (Q7:54↔Q10:3, synonym), (Q11:69↔Q15:51, synonym), (Q16:125↔Q29:46, add_drop).

**Decisive test-case (H-NEW-18-EXT-b):** Pair #15 (Q5:3 Madanī ↔ Q6:145 Makkī). Kirmānī's aṣl/farʿ places 5:3 *before* 6:145; Nöldeke Makkī-before-Madanī chronology would reverse. Directional adjudication: canonical vs Nöldeke.

- **Rationale:** classical-scholar 2026-04-14 dispatch. Sign convention is load-bearing; 6-category scheme prevents garden-of-forking via selective δ-category reporting; §1-20 list locked for reproducibility. All three locked BEFORE computational-tester executes.
- **Bonferroni:** k=4 for H-NEW-18-EXT primary suite (pooled + per-category 6 within-secondary at α=0.0083 each, plus decisive pair #15 reported descriptively).
- **Pre-registration date:** 2026-04-14
- **Proposed by:** hypothesis-generator (classical-scholar inputs 2026-04-14)
- **Approved by:** team-lead (2026-04-14) — "AMEND-16 APPROVED in advance. Lock sign convention: flipped (longer variant in sparser host) per classical-scholar's wujūh-logic reading. This is a CLEAN pre-registration of the opposite sign, and team-discovery-009's documentation explicitly anticipates this follow-up. No corrigendum needed for team-discovery-009. Prefer fresh §11-20 pairs for the primary; 009's 73-pair data may only appear as a data-reuse robustness check. classical-scholar's wujūh-logic catch is valid AND team-discovery-009's discipline was also valid — this is how the team SHOULD catch its own potential sign-errors without invalidating prior work."

## AMEND-17 — H-NEW-25 al-Khalīl same-makhraj sub-test (e) + #19⊕#46 bundle dispatch + H-NEW-25/26/27 joint approval

- **Target A:** task #45, H-NEW-25 (phonotactic trigram entropy). Status at amendment time: pending. Pre-reg window OPEN.
- **Target B:** tasks #19 + #46 (H-NEW-12 spectral DAG + H-NEW-26 persistent-homology cycles). Bundled single-compute dispatch.
- **Target C:** task #47, H-NEW-27 (divine-name cooccurrence asymmetry vs al-Ghazālī). Approval-only — no spec change.

**Part A — H-NEW-25 sub-test (e) al-Khalīl same-makhraj constraint:**
Add pre-registered sub-test (e) testing al-Khalīl b. Aḥmad's DIFFERENT classical prediction: same-makhraj consonants DO NOT co-occur. The 28-letter inventory is partitioned into 8 makhraj groups (ḥalq, lahā, shajrī, asalī, nitʿī, lithawī, dhalqī, shafawī) per *Kitāb al-ʿAyn* ed. Makhzūmī/Sāmarrāʾī Baghdad 1980-1985 muqaddima (classical-scholar pre-publication verification pending). Statistic: observed mean same-makhraj bigram rate S̄ vs multiset-preserving shuffle expectation E[S̄]. Pre-reg direction: S̄ < E[S̄] at z < -2.326 (α=0.01 one-sided).

Joint-confirmation rule pre-locked:
- (a) AND (e) both fire → TIER-A joint confirmation of two structurally-distinct classical phonotactic predictions (al-Rummānī smoothness + al-Khalīl avoidance) at different orders of structure.
- (a) fires without (e) → al-Rummānī talāʾum fires; al-Khalīl same-makhraj rule doesn't.
- (e) fires without (a) → al-Khalīl fires; Quran inherits Arabic makhraj-avoidance without additional smoothness.
- Neither fires → both classical predictions falsified quantitatively for the first time; publishable null.

Bonferroni updated: **k=5** (was 4), **α=0.01** per sub-test (was 0.0125).

**Part B — Task #19 ⊕ Task #46 bundle dispatch:**
Per team-lead 2026-04-14: "Task #19's spectral analysis and H-NEW-26's persistent homology are complementary decompositions of the same underlying DAG. Running them together saves the graph-construction cost once and gets both Betti-series and eigen-spectrum at once. Mark as bundled dispatch: #19+#46 → single compute."

Bundle rule: ONE phrase-echo DAG construction (edges = verse pairs sharing ≥3 content-lemma trigram or ≥1 rare-lemma-trigram, directional j → i back-reference). From that single graph, compute:
- Task #19 sub-tests (a) out-degree power-law, (b) in-degree top-10 polemic/summary hypergeometric, (c) Laplacian spectral-gap vs degree-preserving rewiring null (1000 perms).
- Task #46 sub-tests (a) mean Betti-1 per surah > 1, (b) corpus Betti-2 > 0, (c) per-surah Betti-1 vs baseline z > +2.4.

Bundle-family Bonferroni: **k=6**, per-test **α=0.0083**. No double-counting; the Laplacian eigen-spectrum and persistent homology are computationally distinct statistics on the same graph, so each sub-test is an independent hypothesis under the bundle.

Shared output: `scripts/h_new_12_26_phrase_echo_bundle.py`, `findings/phase-b-hypotheses/csv/h-new-12-26-bundle.json`. Separate writeups: `findings/phase-b-hypotheses/phrase-echo-dag-spectral.md` (#19) + `findings/phase-b-hypotheses/phrase-echo-higher-cycles.md` (#46).

**Part C — H-NEW-27 approved:**
Team-lead 2026-04-14: "This is the test I most want to see. al-Ghazālī's *al-Maqṣad al-Asnā* pairs divine attributes into theological opposites and complements — a classical prediction of a COMPUTATIONAL structure. If the cooccurrence matrix asymmetry matches his pairing table above chance, that's a 900-year-old classical prediction of a 21st-century computational test passing. Strong candidate for Tier-A if it lands."

H-NEW-27 approved as specified in task #47 (divine-name cooccurrence asymmetry graph). Blocked on classical-scholar delivery of (i) 99-name canonical TSV (already in MASTER-FINDINGS-LEDGER §2 from al-Walīd b. Muslim via al-Tirmidhī #3507), (ii) al-Ghazālī *al-Maqṣad al-Asnā* ~20-30 attribute-pairs TSV (in classical-scholar queue).

- **Rationale:** Three approvals bundled. (A) al-Khalīl sub-test (e) is a non-obvious falsification trap — two classically-distinct predictions at different orders of structure, with pre-locked joint-confirmation rule preventing any post-hoc cherry-picking of which classical source "counts." (B) DAG bundle saves compute without inflating false-positive rate via shared-Bonferroni discipline. (C) H-NEW-27 approval unblocks dispatch as soon as classical-scholar delivers the al-Ghazālī pair list.
- **Pre-registration date:** 2026-04-14
- **Proposed by:** hypothesis-generator
- **Approved by:** team-lead (2026-04-14) — "H-NEW-25, H-NEW-26, H-NEW-27 all APPROVED. Sub-test (d) shuffle-preserving-unigram control is the critical discriminator — same logic as H-NEW-24's shuffle control. al-Khalīl's *Kitāb al-ʿAyn* organized the Arabic lexicon by articulation point (*makhraj*), which is an older-than-talāʾum layer. The two predictions are at different orders of structure. Pre-register as sub-test (e) if feasible. Bundle #19+#46 → single compute. H-NEW-27 is the test I most want to see — 900-year-old classical prediction of 21st-century computational structure."

---

## AMEND-18 — Classical-scholar FOAI sign-direction self-correction (TSV-file alignment) [RENUMBERED from duplicate AMEND-15 by hypothesis-generator 2026-04-14]

**NUMBERING CORRECTION NOTE (hypothesis-generator 2026-04-14):** This amendment was originally filed by classical-scholar under number "AMEND-15", which collided with hypothesis-generator's AMEND-15 (H-NEW-24 position-stratified reporting, filed 2026-04-13, at line 186 above). The single-point-of-truth protocol requires unique sequential numbering. classical-scholar's self-correction is renumbered here to AMEND-18 to preserve filing-order uniqueness. The original AMEND-15 at line 186 stands as the canonical AMEND-15.

- **Target:** `findings/classical-sources/kirmani-30-pair-tuples.tsv` (file created 2026-04-12 by classical-scholar for task #26 operationalization). Status at amendment time: file dispatched with WRONG sign-column; corrected on-write. Test #40 (H-NEW-18-EXT) already uses correct sign per AMEND-16.
- **Amendment:** In the initial prose-dispatch of the 30-pair TSV (2026-04-12 message to hypothesis-generator), the `predicted_FOAI_sign` column was tagged `A>0` for all 17 usable directional rows. This was INCORRECT. The correct prediction under al-Kirmānī's context-optimality semantics is `A<0` for all 17 rows. The TSV file on disk (`findings/classical-sources/kirmani-30-pair-tuples.tsv`) was written with the CORRECTED `A<0` sign. Wajh-category tags, kirmani_quote_gist, verse references, and the 17-usable sub-count are unchanged.
- **Rationale:** Under al-Kirmānī's claim that each variant is context-optimal, both cross-swaps are low-fit, with the primary-context swap being WORSE than the echo-context swap. Therefore `A = S(V_B|C_A) − S(V_A|C_B) = (very low) − (low) = NEGATIVE`. This is consistent with hypothesis-generator's pre-compaction flag and with team-lead's AMEND-16 approval (2026-04-14) locking "flipped sign per classical-scholar's wujūh-logic reading."
- **Relationship to AMEND-16:** AMEND-18 is a FILE-LEVEL alignment, not a protocol amendment. AMEND-16 is the canonical pre-registration of the sign for H-NEW-18-EXT (task #40). AMEND-18 only retracts and corrects the TSV-column in the supplementary data file, which downstream tests source from. Nothing about the H-NEW-18-EXT primary test-design changes.
- **Pre-registration date:** 2026-04-12 (classical-scholar self-audit after hypothesis-generator confirmation message)
- **Proposed by:** classical-scholar (self-correction)
- **Approved by:** team-lead (via AMEND-16, 2026-04-14, which had already locked the corrected sign for task #40)

## AMEND-19 — H-NEW-24 length-confound orthogonalization re-run

- **Target:** task #44, H-NEW-24 (letter-multiset surah-boundary detectability). Status at amendment time: completed PARTIAL (a∧c∧d PASS, b FAIL). Ledger promotion REVERTED to wait-state by team-lead 2026-04-14 pending length-orthogonalization audit (skeptical-auditor audit-019).
- **Protocol note:** This is NOT a post-hoc amendment to the primary test — the primary test stands as completed/partial. This IS a new pre-registered secondary orthogonalization whose direction is locked BEFORE the residual regression is run. Approved in advance per team-lead 2026-04-14: "I trust hypothesis-generator to file it as a clean orthogonalization amendment; I approve in advance."

**Amendment — length-regression residual pipeline:**

Context: AMEND-15's mechanism-layer disclosure already acknowledged "plausible mediation through Meccan/Madani register drift and length drift" for H-NEW-24's signal. AMEND-19 operationalizes the mediation test via a post-hoc-independent secondary-analysis on the EXISTING JS-divergence outputs.

**Procedure (locked BEFORE residual execution):**
1. For each of the 113 interior boundary positions, compute the scalar feature Δℓ_i = |length(surah_left) − length(surah_right)| in characters.
2. Regress observed JS-divergence peaks against Δℓ_i via ordinary least squares: JS_i = β₀ + β₁·Δℓ_i + ε_i.
3. Compute residual ε_i = JS_i − (β₀ + β₁·Δℓ_i).
4. Compute residual hit-count at the pre-registered primary operating point (w=2000, ε=500): how many of the 113 true boundaries are recovered when detection is performed on ε_i instead of raw JS_i?
5. Compute residual z-score = (residual-hit-count − shuffle-null-mean) / shuffle-null-std, where shuffle-null is computed on the SAME residualized signal.

**Pre-registered interpretation rule (locked by team-lead 2026-04-14):**
- **Residual z > +2.58 at Bonferroni-adjusted threshold** (k=1 independent of primary Bonferroni since this is a separate secondary test) → **LENGTH-ORTHOGONAL signal confirmed**. Letter-multiset boundary detection is a real structural signature independent of length drift. Ledger promotion to Tier-A authorized. Headline framing: "tokenization-free structural signature independent of surah-length drift."
- **Residual z > +1 but ≤ +2.58** → **PARTIAL orthogonality**. Signal has BOTH a length-mediated component AND a length-orthogonal component. Ledger demotion to "partial Tier-B." Honest mixed finding.
- **Residual z ≤ +1** → **LENGTH-MEDIATED signal**. Primary detection result stands as factual ("letter-multiset discontinuity detects surah boundaries") but mechanism is demoted: "the detection works because adjacent surah lengths differ sharply enough to shift letter-multiset distributions; the signal is NOT a content-specific structural fingerprint, it's a register/length drift proxy." Ledger demotion to Tier-B honest-mediation result.

All three outcomes are publishable. Team-lead 2026-04-14: "Either outcome is publishable: survives orthogonalization → Tier-A; length-mediated → still a real finding but demoted."

**Data reuse:**
- This pipeline operates on the EXISTING JS-divergence outputs from the original H-NEW-24 run. No re-run of the multiset scan is needed; only the regression-residual layer.
- Seed fixed at 20260413 (same as primary H-NEW-24).
- Output: append residual analysis to `findings/phase-b-hypotheses/letter-multiset-boundary-detection.md` as "§Length-orthogonalization (AMEND-19)" section; update `csv/h-new-24.json` with `residual_analysis` sub-key.

**Bonferroni:** k=1 for AMEND-19's residual test, α=0.01 independent of primary H-NEW-24 k=4. This test is a secondary analysis answering a distinct mechanism question; no multiple-testing correction with primary.

**Connection to prior skeptical-auditor audit-019 + MW-1-GATE-A precedent:** this is the second instance of a length-orthogonalization amendment in the current pipeline (MW-1-GATE-A / task #52 is the same pattern applied to H-NEW-20 al-Rāzī autocorrelation). Establishing a standing orthogonalization-amendment pattern: when a completed test is flagged for a length-or-register confound, the fix is a residual-regression secondary pipeline with pre-registered interpretation rule, NOT a post-hoc re-run with tweaked primary design.

- **Pre-registration date:** 2026-04-14
- **Proposed by:** hypothesis-generator (length-confound flagged by skeptical-auditor audit-019; remediation spec directed by team-lead 2026-04-14)
- **Approved by:** team-lead (2026-04-14) — approved in advance: "skeptical-auditor's audit-019 flagged this correctly. I reverted the ledger promotion to wait-state pending length-orthogonalization. The finding's a∧c∧d signature is real but may be *mediated* by surah-length drift, which the pre-registered design didn't orthogonalize against. I trust hypothesis-generator to file it as a clean orthogonalization amendment; I approve in advance."

---

## AMEND-20 — [REJECTED 2026-04-14 Turn-6] H-NEW-29 rate-matched per-root Poisson null — REDIRECTED to H-NEW-29.1 as independent follow-up

**STATUS: REJECTED as amendment by team-lead 2026-04-14 Turn-6.** This filing stood as AMEND-20 for <24h before the origin-qualifier review rejected it. Rationale from team-lead: *"the MOTIVATION was improving the primary test, not auditing it after a confound flag. That's the critical difference."* The rate-matched Poisson layer is re-filed as an **independent follow-up hypothesis H-NEW-29.1**, with H-NEW-29's MIXED primary verdict standing verbatim. The three-way interpretation rule below is preserved by reference for H-NEW-29.1 pre-registration. Do NOT cite AMEND-20 as an active amendment; cite H-NEW-29.1 instead.

**Retained for traceability only (original text below, superseded):**

**TIMING DISCLOSURE (critical for honesty):** Team-lead's rate-matched-null suggestion (2026-04-14) arrived AFTER the H-NEW-29 primary run completed (task #54 finished, finding file at `findings/phase-b-hypotheses/root-renewal-cv.md` with MIXED verdict: absolute CV<1 REFUTED, comparative Quran<baseline PASS). Under normal pre-registration discipline this would be a **post-hoc robustness check**, not a pre-registered amendment. I am filing it as AMEND-20 with the timing explicitly disclosed rather than quietly re-running — protocol reminder at log-bottom applies.

- **Target:** task #54, H-NEW-29 (root inter-occurrence renewal-process signature). Status at amendment time: completed MIXED. Absolute sub-(a)/(c)/(d) REFUTED under uniform-token-permutation shuffle null (CV = 1.37, shuffle-null CV ≈ 0.98, z = +94.89). Comparative sub-(b) PASSED (Quran vs Bukhari/Jahiz Mann-Whitney z < −7.9 in regularization direction).
- **Why this is an amendment rather than a re-run:** The rate-matched-null layer does NOT re-operationalize any pre-registered sub-test. It ADDS a fourth null-comparison (alongside the uniform-shuffle null already in the finding) to answer a separable statistical question: "after controlling for per-root frequency, is there residual regularity above what rate-matched Poisson predicts?" This is a mechanism-layer robustness check, identical in pattern to MW-1-GATE-A (H-NEW-20 length-residualization) and AMEND-19 (H-NEW-24 length-residualization), both of which layer a secondary null over an existing primary result.

**Procedure (locked BEFORE execution of the rate-matched-null layer, after primary result known):**

1. For each of the 833 roots with n_R ≥ 5 in the Quranic corpus, determine n_R (event count) and N = 77,915 (STEM token count).
2. For each root, simulate n_R events placed uniformly at random over the N-token span (draw n_R distinct uniform integers in [0, N), sort, compute inter-arrival distances, compute CV of that simulated series). Repeat 1,000 simulations per root. Aggregate to get per-root expected-CV distribution under rate-matched Poisson.
3. For each root, compute Δ_r = CV_observed(r) − E[CV_rate_matched(r)].
4. Weighted-mean Δ across roots, weights = n_R (same weighting as primary).
5. 1,000-bootstrap 99% CI for weighted-mean Δ.
6. Additionally: per-frequency-bin weighted-mean Δ for the four bins already in the primary analysis (rare / mid / frequent / super-frequent).

**Pre-registered interpretation rule (locked BEFORE the rate-matched-null layer is run):**
- **Weighted-mean Δ < 0 with 99% CI entirely below 0** → **Quran is MORE REGULAR than rate-matched Poisson** controlling for per-root frequency. This would REVERSE the absolute-claim failure in the primary — the primary's failure was against CV = 1, but the more faithful null is rate-matched per-root. If Δ < 0 under rate-matched null, the comparative claim (already PASSED vs Bukhari/Jahiz) is strengthened, AND the absolute claim gets a second chance under the correct null. Finding upgraded from MIXED to **Tier-B PASS (comparative + rate-matched regularity)**.
- **Weighted-mean Δ ≈ 0 (99% CI crosses 0)** → Quran is statistically equivalent to rate-matched Poisson. The primary's super-Poisson observation (CV = 1.37) was driven entirely by per-root frequency heterogeneity, not by any regularity beyond what corpus-finite sampling forces. Primary MIXED verdict stands as-is; no upgrade, no demotion.
- **Weighted-mean Δ > 0 with 99% CI entirely above 0** → Quran is MORE CLUMPED than rate-matched Poisson. Primary super-Poisson result is NOT just a finite-corpus artifact; there is genuine excess clumping on top of rate-matched expectation. This strengthens the refutation of the absolute al-Jāḥiẓ claim AND means the comparative Quran-vs-Bukhari result must be re-interpreted through the same lens (probably also still clumpier than rate-matched Poisson, but less so than Bukhari). Primary MIXED verdict stands.

**Per-frequency-bin rule:** if super-frequent bin Δ is significantly different from rare bin Δ, the signal lives in one bin and not the other. al-Jāḥiẓ's empirical target is the super-frequent bin (content words). If super-frequent Δ < 0 while rare Δ ≈ 0, the refined al-Jāḥiẓ claim is: "Quranic content-word spacing is more regular than rate-matched Poisson." A stronger positive for the classical prediction than the primary delivered.

**Bonferroni:** k=1 for the aggregate weighted-mean Δ test (independent post-hoc secondary). Per-bin sub-tests are exploratory and will be reported without Bonferroni correction, flagged as exploratory.

**Data reuse:** this pipeline uses the existing per-root observed-CV table from the primary H-NEW-29 output. Only the per-root rate-matched-Poisson simulation layer is new. Cost: 833 roots × 1,000 simulations × ~O(n_R) per sim = ~cheap (< 1 second in Python).

**Pre-registered output:**
- Append §Rate-matched-null-robustness-check (AMEND-20) section to `findings/phase-b-hypotheses/root-renewal-cv.md`.
- Update `findings/phase-b-hypotheses/csv/h-new-29.json` with `rate_matched_analysis` sub-key containing: weighted_mean_delta, bootstrap_99_CI, per_bin_delta (4 bins), seed.
- Seed fixed at 20260414 (new for this layer; primary used 20260413).

**Honesty note:** the weighted-mean Δ direction is a statistical outcome I cannot predict from classical reasoning alone — the classical prediction (al-Jāḥiẓ *takrār maqbūl*) translates to Δ < 0 (more regular than Poisson), but whether finite-corpus frequency-dependent bounding produces Δ ≈ 0 or Δ < 0 on its own is an empirical fact about the corpus, not a theoretical prediction. I am pre-registering **all three outcomes as publishable** with their specific interpretations above, locked before the run.

**Connection to the orthogonalization-amendment pattern:** AMEND-20 is the THIRD instance of a post-primary secondary-null robustness amendment, after MW-1-GATE-A (length-residualization for H-NEW-20) and AMEND-19 (length-orthogonalization for H-NEW-24). At three instances, this is now a formal standing pattern. I will propose to team-lead that we codify it in MASTER-FINDINGS-LEDGER §6 as the "secondary-null amendment protocol" so future audits default to this treatment.

- **Pre-registration date:** 2026-04-14 (filed AFTER primary run completed, timing disclosed above)
- **Proposed by:** team-lead (2026-04-14 approval message to hypothesis-generator, rate-matched-null addition)
- **Filed by:** hypothesis-generator (2026-04-14)
- **Approved by:** team-lead (2026-04-14) — "Pre-register: for each root, compute the expected CV under a rate-matched Poisson null... the aggregate claim then becomes: weighted mean of (observed CV − expected rate-matched null CV) per root is significantly below zero under bootstrap. This addresses the finite-corpus edge effect vulnerability that would otherwise give a spurious regular spacing signal for any high-frequency root in any finite text... the addition is cheap to compute and makes the finding robust against the sharpest likely auditor critique."

---

## AMEND-21 — H-NEW-30 hypergeometric-against-91-name-baseline correction (Faʿʿāl base-rate control)

**Target:** task #57, H-NEW-30 (morphological-class signature of Khawātim al-Ḥashr exclusive-8 divine names). Status at amendment time: PENDING, classical-scholar blockers not yet resolved (wazn TSV, 99-name morphological class tagging). Primary test has NOT yet been executed. This is a clean PRE-EXECUTION amendment, not post-hoc.

**Team-lead's concern (2026-04-14):** "Faʿʿāl is one of the most common intensive-form patterns in Arabic theological vocabulary; a naive Fisher test against uniform over morphological classes would spuriously fire for Faʿʿāl even in random name samples. The correct test is: 'is the exclusive-8 Faʿʿāl rate above the expected rate under sampling from the 91 non-exclusive names?'"

**Amendment:** The null distribution for morphological-class enrichment in the exclusive-8 set must be **hypergeometric sampling from the 99-name morphological-class distribution**, NOT uniform over morphological classes.

**Procedure (locked BEFORE execution):**
1. Using the classical-scholar-delivered 99-name × wazn TSV, compute the full morphological-class distribution over all 99 names: {Faʿʿāl: n₁, Fāʿil: n₂, Muf'il: n₃, Faʿʿūl: n₄, ...} summing to 99.
2. For the exclusive-8 set (names appearing ONLY in the Khawātim al-Ḥashr cluster and nowhere else in the canonical 99), compute observed morphological-class counts {Faʿʿāl: k₁, Fāʿil: k₂, ...} summing to 8.
3. For EACH morphological class C in the scheme, compute the hypergeometric p-value: P(X ≥ k_C) where X ~ Hypergeometric(N=99, K=n_C, n=8). This answers: "if we drew 8 names uniformly at random from the 99-name corpus, what is the probability we'd get at least k_C of class C?"
4. Bonferroni k = number-of-classes (typically 5-8 classes; locked by classical-scholar TSV delivery). Per-class α = 0.01 / k.
5. Joint PASS: **any single class significantly over-represented** at Bonferroni-corrected α.

**Pre-registered interpretation (locked):**
- Hypergeometric p < α_Bonferroni for any class → that class is a **genuine structural signature** of the exclusive-8, not a base-rate artifact. PASS.
- All hypergeometric p > α_Bonferroni → NULL. The exclusive-8's morphological distribution is indistinguishable from random sampling of 8 names from the 99-corpus, so morphological class is NOT the structural marker distinguishing the exclusive-8.
- If the exclusive-8 Faʿʿāl count k_Faʿʿāl happens to equal the expected value 8·n_Faʿʿāl/99 exactly, that's the "base-rate only" scenario and the null is confirmed.

**Why this matters:** hypergeometric-against-baseline is the correct test for "class-enrichment in a sub-sample drawn from a known population." Fisher against uniform would be measuring "is the exclusive-8 balanced across classes?", which is a DIFFERENT question that doesn't address structural enrichment. Team-lead caught this correctly — the naive uniform test would spuriously fire on any common-intensive form regardless of which 8 names we drew.

**Bonferroni within H-NEW-30:** k = number-of-morphological-classes in classical-scholar's wazn TSV (expected 5-8, locked after delivery). Per-class α = 0.01 / k. No additional family-wise correction with H-NEW-29..33 — each H-NEW-N is an independent hypothesis.

**Data dependency unchanged:** still blocked on classical-scholar wazn-TSV delivery for full 99-name list + exclusive-8 identification.

- **Pre-registration date:** 2026-04-14 (filed BEFORE execution — clean pre-reg, not post-hoc)
- **Proposed by:** team-lead (2026-04-14 approval message, baseline-control correction)
- **Filed by:** hypothesis-generator (2026-04-14)
- **Approved by:** team-lead (2026-04-14) — "This is a hypergeometric-distribution test, not Fisher against uniform. Lock before dispatch."

---

## AMEND-22 — [REJECTED 2026-04-14 Turn-6] H-NEW-31 post-primary OATH category addition — REDIRECTED to H-NEW-31.2 as independent follow-up

**STATUS: REJECTED as amendment by team-lead 2026-04-14 Turn-6.** Rejected on two grounds: (a) class-scheme expansion (6-class → 7-class with re-prioritized classification order) is **feature re-operationalization**, prohibited as amendment regardless of honesty disclosures; (b) origin was hypothesis-proposer initiative, not adversarial-flag. The 7-class OATH-inclusive scheme is re-filed as **independent follow-up hypothesis H-NEW-31.2**, with pre-registered OATH reassignments (Q 79, 85, 86, 89, 91, 92, 93, 95, 100, 103, 104) locked BEFORE re-classification, and H-NEW-31's PARTIAL primary verdict (SPACE PASS p=0.0146, TIME direction-reverse) standing verbatim. Data reuse from H-NEW-31 is disclosed in H-NEW-31.2 pre-registration. Team-lead quote: *"the test has been re-specified"* — that alone disqualifies amendment treatment. Do NOT cite AMEND-22; cite H-NEW-31.2 instead.

**Retained for traceability only (original text below, superseded):**

**TIMING DISCLOSURE (critical for honesty):** H-NEW-31 (task #58) has ALREADY BEEN EXECUTED with the 6-class TIME/COSMOS/PRAISE/IMPER/SPACE/OTHER scheme. PARTIAL verdict already in `findings/phase-b-hypotheses/incipit-time-space.md` (SPACE sub-test PASS at p=0.0146; TIME sub-test FAIL direction-reversed). Team-lead's OATH-category addition (2026-04-14) arrived AFTER the primary run. Under pre-registration discipline this is a **post-primary secondary-class-redefinition**, structurally similar to AMEND-20. I am filing it as AMEND-22 with timing explicitly disclosed, not as a silent re-run of the primary.

**Target:** task #58, H-NEW-31. Primary finding stands as reported; AMEND-22 adds a seventh category (OATH) and re-runs the classification + χ² contingency on the new 7-class scheme as a **post-primary secondary analysis**.

**Team-lead's reasoning:** "al-Suyūṭī will catch [the OATH category] if you don't, and *qasam*-opening is a strong Meccan signature worth testing independently. al-Suyūṭī *Itqān* nawʿ 59 classifies surah openings into 10 types including *qasam* (oath). The 6-class scheme was incomplete."

**Amendment procedure (locked BEFORE re-classification):**

1. Define OATH class: surah-incipit (first 5 tokens post-basmala, post-muqaṭṭaʿāt) contains a **wāw-qasam** (وَ + nominal-object) as the first content token. Canonical archetypes: Q 91 (*wa-l-shamsi wa-ḍuḥāhā*), Q 92 (*wa-l-layli idhā yaghshā*), Q 93 (*wa-l-ḍuḥā*), Q 95 (*wa-l-tīni wa-l-zaytūni*), Q 100 (*wa-l-ʿādiyāti ḍabḥan*), Q 103 (*wa-l-ʿaṣri*).
2. Classification priority (updated): **OATH > TIME > COSMOS > PRAISE > IMPER > SPACE > OTHER**. OATH takes priority over TIME because wāw-qasam is the grammatical head even when followed by an *idhā*-clause (e.g., Q 91:1-2 is OATH-by-qasam even though Q 91:2 contains *idhā*).
3. Re-classify all 114 surah-incipits under the 7-class scheme.
4. Re-compute the 2×7 Meccan/Medinan contingency.
5. Fisher exact one-tailed test: Meccan > Medinan on OATH at α = 0.01 (k=1, independent secondary test).
6. Report which surahs shifted from prior classes (expected: Q 79, Q 85, Q 86, Q 89, Q 91, Q 92, Q 93, Q 95, Q 100, Q 103, Q 104 — candidates for TIME/COSMOS → OATH reassignment).

**Pre-registered interpretation (locked BEFORE computation):**
- OATH-Meccan at p < 0.01 → **classical confirmation** of al-Suyūṭī's *qasam* as a Meccan incipit signature. H-NEW-31 primary verdict upgraded to **Tier-B + 1 secondary confirmation**: SPACE-Medinan + OATH-Meccan both classical-anchored PASS.
- OATH-Meccan p ≥ 0.01 → NULL on the oath-opening hypothesis (would be surprising given the archetypal Q 91/92/93/95 oath-surahs are all Early Meccan).
- TIME class after OATH reassignment: if TIME-Meccan now passes at α = 0.01 (after OATH absorbs the wāw-qasam cases), then the original H-NEW-31 TIME failure was caused by the OATH-contamination and the finding upgrades; if TIME-Meccan still fails post-reassignment, the original TIME FAIL-reversal stands as reported.

**Bonferroni:** k=1 for the OATH-Meccan secondary test (independent post-primary). TIME-post-reassignment is exploratory and reported without correction, flagged as such.

**Output:** append §OATH-category secondary-analysis (AMEND-22) to `findings/phase-b-hypotheses/incipit-time-space.md`; update `csv/h-new-31.json` with `oath_category_analysis` sub-key.

**Honesty note:** the 7-class scheme shifts classification priority in a way that RE-CLASSIFIES existing surahs, which is a re-operationalization of the primary test's classification layer, not a pure secondary-null addition. This is a weaker form of amendment than AMEND-20 (which added a null comparison without changing any surah's classification). I am flagging this as a **class-scheme expansion post-primary amendment**, a distinct sub-pattern. The key honesty protection: the interpretation rule for OATH-Meccan is pre-registered BEFORE the re-classification is run, and the primary's TIME/SPACE sub-test verdicts are preserved as reported (not retroactively restated).

- **Pre-registration date:** 2026-04-14 (filed AFTER primary run, timing disclosed above)
- **Proposed by:** team-lead (2026-04-14 approval message, OATH category addition)
- **Filed by:** hypothesis-generator (2026-04-14)
- **Approved by:** team-lead (2026-04-14) — "Pre-register: add OATH as 7th category explicitly. al-Suyūṭī will catch it if you don't, and *qasam*-opening is a strong Meccan signature worth testing independently."

---

## AMEND-23 — H-NEW-33 low-power-fallback binary test (verse-initial vs anywhere-else loanword)

**Target:** task #60, H-NEW-33 (loanword verse-positional gradient). Status at amendment time: PENDING (not yet executed; blocked on classical-scholar source-language catalog verification). Clean pre-execution amendment.

**Team-lead's concern (2026-04-14):** "The loanword catalog in findings/phase-b-hypotheses/foreign-loanwords.md has ~42 Jeffery-verified loans. That's a small n for KS testing at 4 positional bins. Consider: if KS at verse-quarter resolution is underpowered, fall back to binary test (verse-initial vs anywhere-else) which has higher power at small n. Pre-register both primary and fallback."

**Amendment — dual-statistic pre-registration:**

1. **Primary (as originally pre-registered):** 4-bin positional KS test on verse-quarter bins (Q1, Q2, Q3, Q4 of each verse by token-position), comparing loanword positional distribution to baseline Arabic-root positional distribution in the same verses. Bonferroni k=4 (per source-language + pooled). α = 0.0025.

2. **Fallback (new, pre-registered as AMEND-23):** If the primary KS has fewer than 25 loanword occurrences in any single positional bin (fewer than expected under the small-n distribution, rendering KS unreliable), use a **binary Fisher exact test** on the 2×2 contingency:
   - Row 1: verse-initial (Q1 position-bin) counts for loanwords vs native roots
   - Row 2: non-initial (Q2+Q3+Q4) counts for loanwords vs native roots
   - Fisher exact one-tailed test: are loanwords over-represented in verse-initial position vs native-root base rate?
   
3. The decision rule for primary-vs-fallback is locked **BEFORE data inspection**: if min(bin count across Q1..Q4) < 25, use fallback; else use primary KS. This rule is computed mechanically on the loanword-count table BEFORE any significance test is run.

4. Bonferroni within H-NEW-33: k=4 if primary KS path taken (per-language: Syriac, Persian, Greek, other + pooled); k=2 if fallback binary path taken (pooled + Syriac-only, with other languages merged due to small n). Per-path α locked independently.

**Pre-registered interpretation (locked):**
- Primary KS PASS at p < 0.0025 per-language → positional-gradient signal confirmed, publishable as Tier-B or Tier-A depending on how many languages fire.
- Fallback Fisher PASS at p < 0.005 (k=2) → **coarser-grain signal confirmed**: loanwords concentrate in verse-initial position above native-root base rate.
- Both paths NULL → loanword position is indistinguishable from native-root position, NULL result publishable.

**Why include this amendment:** underpowered tests with many bins and small n are the classic way good pre-registrations fail even when a real signal exists. Pre-registering a coarser fallback that preserves Bonferroni discipline protects against "underpowered null" which is methodologically weak. This is the same pattern as T4 Tomorrow-Test used (coarse 12-constraint + fine-grain secondary).

**Additional protection against cherry-picking:** the min-bin-count < 25 rule is mechanical and decided by the data AFTER loading but BEFORE any test, and it's locked in the script output so auditor can verify the path selection wasn't post-hoc. The fallback is NOT a "try primary, if it fails fall back to something easier" — it's a "the data's shape determines which test is appropriate, decided mechanically".

- **Pre-registration date:** 2026-04-14 (filed BEFORE execution — clean pre-reg)
- **Proposed by:** team-lead (2026-04-14 approval message, low-power fallback addition)
- **Filed by:** hypothesis-generator (2026-04-14)
- **Approved by:** team-lead (2026-04-14) — "Consider: if KS at verse-quarter resolution is underpowered, fall back to binary test (verse-initial vs anywhere-else) which has higher power at small n. Pre-register both primary and fallback."

---

*Protocol reminder: if a hypothesis shows RESULT-DEPENDENT changes in design AFTER computational-tester has executed, it is no longer a valid pre-registration. Such changes must be labeled as post-hoc exploratory analyses in the final findings file, not as amendments.*

*Protocol clarification added 2026-04-14 (re: AMEND-20 filing): a secondary-null robustness check whose result-direction interpretation is locked BEFORE running the secondary layer is NOT a "result-dependent design change to the primary test" — it is an **additional** null comparison that does not alter the primary test's pre-registered operationalization. It should be labeled clearly as post-primary (timing disclosed) and the interpretation rule must be locked BEFORE computation. MW-1-GATE-A (H-NEW-20), AMEND-19 (H-NEW-24), and AMEND-20 (H-NEW-29) are the three instances establishing this standing pattern.*

---

## AMEND-24 — H-NEW-SURVEY meta-hypothesis: unified cross-scale mirror-string suppression/enrichment confirmation (bifurcated Path B)

**Timing: PRE-EXECUTION. Clean pre-registration.** Filed 2026-04-14 BEFORE the confirmation run against baseline corpora is dispatched.

**META-NULL RETRACTION COMMITMENT (pre-registered header, locked 2026-04-14 Turn-5 per team-lead approval):** If the joint meta-verdict lands on **META-NULL** (EQUIVALENT-A AND EQUIVALENT-B on matched-Arabic baselines), the following retractions are pre-committed and MUST be executed without further deliberation:
- The in-corpus headline framing in `findings/phase-b-hypotheses/palindrome-full-sweep.md` §H11 ("Quranic letter-palindromes are SUPPRESSED vs shuffle") is retracted to a neutral framing: "below within-Quran shuffle expectation, equivalent to matched Arabic prose — likely Arabic-phonotactic base-rate artifact."
- Same retraction applied to `findings/phase-b-hypotheses/cross-word-phonetic-palindromes.md` (H-NEW-16) for the phonetic-palindrome suppression framing.
- Project-pattern M-3 ("surface-layer mirror-string suppression") is downgraded from a candidate meta-pattern to an NULL-OUT entry in the honest-limits ledger.
- MASTER-FINDINGS-LEDGER §5 palindrome entries are re-annotated with "META-NULL on matched-Arabic control (H-NEW-SURVEY-A, 2026-04-14)."

This pre-commitment is the **META-NULL retraction clause** — its existence in the pre-registration header protects against motivated re-interpretation of a null meta-result. If PASS-A, PARTIAL, or META-REVERSE fires, the retraction clause does not trigger.

**Target:** NEW pre-registered test family, not an amendment to an existing test. H-NEW-SURVEY is a joint meta-hypothesis that treats the accumulated palindrome / mirror-string findings as prior-generated effect sizes and locks a single confirmation test that predicts their joint direction on fresh baseline comparisons.

**Motivation (per team-lead 2026-04-14 Turn-4 directive):**
> *"draft an H-NEW-SURVEY meta-hypothesis that reviews the palindrome-suppression across scales (letter at z=−6.75, phonetic at z=−6.38, word-length TBD) as a unified 'Quran suppresses mirror-string structure across all scales' finding. This is emerging as a project-level pattern that deserves its own pre-registered confirmation test."*

**Exploratory effect-size inventory (NOT load-bearing; listed as prior signal only):**

| Scale | Operationalization | Observed | Null | z | Source |
|---|---|---|---|---|---|
| S1 letter | ℓ≥7 odd letter palindromes per verse, within-verse char-shuffle null, 1000 perms | 19 | 79.9 | **−6.75** | palindrome-full-sweep.md (H11, pre-registered) |
| S1′ letter, Markov | same observation, 3-gram Markov-letter surrogate, 1000 draws | 19 | 50.8 | **−4.37** | palindrome-full-sweep.md (H11 secondary) |
| S2 phonetic | ℓ≥7 tajwid-collapsed cross-word phonetic palindromes, bigram-Markov null | 67 | 148 / 129 | **−6.38 / −4.73** | cross-word-phonetic-palindromes.md (H-NEW-16) |
| S3 root | root-palindrome windows ≥3, bag-of-roots shuffle | 1170 | 882.7 | **+10.51** (ENRICHED) | palindrome-full-sweep.md (H12) |
| S4 5-word ABCBA | A-B-C-B-A word-token windows, within-surah word-shuffle | 13 | 2.4 | **+6.84** (ENRICHED) | palindrome-full-sweep.md (H13) |
| S4′ 3-word ABA | A-B-A word-token windows | 420 | 387.2 | +1.67 (nominal) | palindrome-full-sweep.md (H13) |

**Observed asymmetry.** The prior signal is NOT "mirror-string suppression at all scales." It is a **bifurcated** pattern: the **grapheme / phoneme surface layers are suppressed** (S1, S1′, S2) and the **semantic / phrase-template layers are enriched** (S3, S4). S4′ is nominal. H-NEW-SURVEY must test this bifurcation, NOT a unidirectional "all scales suppressed" claim, to avoid the pre-registration failure mode where the hypothesis-generator collapses a two-direction pattern into one direction and discovers mid-run that the data moves in opposite directions on different scales.

**Two pre-registered primary hypotheses (joint family, not sequential):**

**H-NEW-SURVEY-A — Surface-layer suppression confirmation.**
> The Quran's letter-level palindrome count AND phonetic-palindrome count are BOTH below matched non-Quranic Arabic baselines, at simultaneous one-tailed significance after Bonferroni correction within this family.

- **Scales tested:** S1 (letter ℓ≥7 palindromes per 1000 verses) and S2 (phonetic ℓ≥7 palindromes per 1000 verses).
- **Baselines:** matched-length Bukhari (non-Quran Arabic prose, from `data/baseline-corpora/raw/bukhari-noquran.txt`) and Jāḥiẓ *al-Ḥayawān* (classical prose, from `data/baseline-corpora/raw/jahiz-hayawan.txt`). Muʿallaqāt reserved as held-out control (NOT used in primary).
- **Observation statistic:** per-corpus palindrome-density (count per 1000 verses for Quran; per 1000 length-matched verse-equivalents for baselines — verse-equivalents defined as Quran-median-letter-count blocks).
- **Null model:** NOT a shuffle — instead, a **rank-based empirical null from the two baseline corpora themselves**. Under the null "Quran is indistinguishable from matched Arabic prose in mirror-string structure," the Quran's per-block density should rank within the middle 80% of the combined Bukhari + Jāḥiẓ per-block density distribution.
- **Test statistic:** Mann-Whitney U for Quran-blocks vs baseline-blocks, reported as a two-tailed z.
- **Acceptance (PASS-A):** BOTH S1 and S2 yield z ≤ −2.81 (one-tailed p < 0.0025, Bonferroni k=2 within family A, α_family = 0.005). Direction pre-registered: Quran BELOW baseline (SUPPRESSED).
- **Acceptance (REVERSE-A):** either scale yields z ≥ +2.81 → reverse signal, MUST be reported as contradictory evidence against the "suppression" reading.
- **Acceptance (EQUIVALENT-A):** neither direction fires → mirror-string suppression NULL on the matched-Arabic comparison, the in-corpus shuffle-null suppression signal is explained by general Arabic phonotactics / obligatory-contour morphology, not Quran-specific.

**H-NEW-SURVEY-B — Semantic-layer enrichment confirmation.**
> The Quran's root-level palindrome count AND 5-word ABCBA phrase-template count are BOTH above matched non-Quranic Arabic baselines, at simultaneous one-tailed significance after Bonferroni correction within this family.

- **Scales tested:** S3 (root-palindrome windows ≥3 non-trivial per 1000 root-tokens) and S4 (5-word A-B-C-B-A phrase windows per 1000 word-tokens).
- **Baselines:** same Bukhari + Jāḥiẓ; same Muʿallaqāt held-out.
- **Root extraction for baselines:** Arabic stemmer (ISRI or similar) applied uniformly; for Quran, QAC v0.4 canonical roots. **Note:** this introduces a stemmer-vs-QAC asymmetry that is a limitation of the test; Muʿallaqāt control later will use the same stemmer on Quran for an apples-to-apples version.
- **Test statistic:** Mann-Whitney U, two-tailed z.
- **Acceptance (PASS-B):** BOTH S3 and S4 yield z ≥ +2.81 (Quran ABOVE baseline). Bonferroni k=2 within family B, α_family = 0.005.
- **Acceptance (REVERSE-B):** either yields z ≤ −2.81 → reverse signal, contradictory.
- **Acceptance (EQUIVALENT-B):** neither direction fires → enrichment NULL on matched-Arabic comparison, in-corpus shuffle-null enrichment explained by Arabic base rate.

**Joint meta-verdict rules (locked pre-execution):**
- **STRONG META-PASS:** PASS-A AND PASS-B. Quran is jointly suppressed on surface scales AND enriched on semantic scales vs matched Arabic prose. This is the strongest outcome — it confirms the **bifurcated structural signature** and makes the "Quran hides the mirror at the grapheme layer while placing it at the root layer" reading publishable.
- **PARTIAL META-PASS (suppression-only):** PASS-A, EQUIVALENT-B or REVERSE-B. The surface-suppression signal is Quran-specific; the semantic enrichment is either a general-Arabic effect or not real. Publishable as surface-suppression-only.
- **PARTIAL META-PASS (enrichment-only):** EQUIVALENT-A or REVERSE-A, PASS-B. The enrichment is Quran-specific; the surface-suppression is general-Arabic phonotactics. Publishable as enrichment-only.
- **META-NULL:** EQUIVALENT-A, EQUIVALENT-B. Neither direction is Quran-specific. Entire palindrome-asymmetry collapses to Arabic-language baseline artifact. MUST be reported; would trigger retraction of the in-corpus headline framing in palindrome-full-sweep.md and cross-word-phonetic-palindromes.md.
- **META-REVERSE:** any REVERSE outcome published as contradictory. Forces revisiting the in-corpus results.

**Bonferroni across meta-family:** k=2 for the two sub-families (A and B). Family-wise α=0.005 ≈ z=±2.81 per-scale, equivalent to family α=0.01 after the sub-family nesting. Nested-family protection: within A, k=2 for (S1, S2); within B, k=2 for (S3, S4); total across meta-family = 4 scales tested, α per scale = 0.05/4 = 0.0125 ≈ z=±2.50 minimum. **We use the stricter z=±2.81 requirement per scale** — tighter than strict Bonferroni — to front-load protection.

**Held-out Muʿallaqāt control (pre-registered, run AFTER primary meta-family completes):** for each of S1..S4, compute the same statistic on the 7 Muʿallaqāt odes vs Quran. Report alongside primary; do NOT gate the primary verdict on the Muʿallaqāt outcome. If Muʿallaqāt tracks Bukhari+Jāḥiẓ, the matched-Arabic baseline is robust; if Muʿallaqāt tracks Quran, the matched-Arabic signal is genre-specific (prose vs poetry) not Quran-specific, and the STRONG META-PASS (if obtained) must be re-read as "Quran resembles pre-Islamic oral poetry in mirror-string structure," which is a narrower classical claim already partially attested in Arab literary theory.

**Mechanisms the test does NOT adjudicate:**
- Whether the surface-layer suppression is a consequence of Semitic triconsonantal root morphology (obligatory contour principle)
- Whether the root-layer enrichment is driven by the *yūliju l-layla fī l-nahāri* cosmic-inversion formulaic couple alone or is broader
- Whether the 5-word ABCBA enrichment is a saj'-specific phenomenon or a Quran-specific one
All three questions are held for H-NEW-SURVEY-EXT follow-ups and do NOT affect the primary verdict.

**Relation to H-NEW-22 anti-signal:** H-NEW-22 found that verse-boundary letter strings yield FEWER dictionary substrings than chance (anti-signal). That is a **lexical-mirror-via-boundary-reading** phenomenon, not a palindrome phenomenon, so it is NOT included in this meta-family. It is noted in project-pattern M-3 as a possibly-related axis but tested separately to avoid meta-family inflation.

**Data sources:**
- Quran: `quran-text/quran-no-tashkeel.json`
- Bukhari: `data/baseline-corpora/raw/bukhari-noquran.txt`
- Jāḥiẓ: `data/baseline-corpora/raw/jahiz-hayawan.txt`
- Muʿallaqāt: `data/baseline-corpora/raw/muallaqat.txt` (if present; if missing, fetch from canonical source before run)
- Roots for baselines: ISRI Arabic stemmer via NLTK or Farasa if available
- Roots for Quran: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4)

**Output target:** `findings/phase-b-hypotheses/h-new-survey-mirror-strings.md`

**Script target:** `scripts/h_new_survey_mirror_strings.py`

**Computational budget estimate:** ~30 minutes (baselines must be tokenized, stemmed, blocked, and scanned for palindromes at 4 scales; Mann-Whitney trivial afterward).

- **Pre-registration date:** 2026-04-14 (filed BEFORE execution — clean pre-reg)
- **Proposed by:** team-lead (2026-04-14 Turn-4 directive)
- **Filed by:** hypothesis-generator (2026-04-14)
- **Awaiting approval:** team-lead (this filing serves as the formal AMEND-24 draft)

**Honesty disclosure:** the effect sizes in the inventory table above are from tests that were pre-registered against within-Quran shuffle / Markov nulls, not against matched-Arabic baselines. The pre-registration fork here is legitimate because H-NEW-SURVEY asks a DIFFERENT question ("Quran vs matched-Arabic" rather than "Quran vs its own shuffle"), with DIFFERENT null models, DIFFERENT statistics, DIFFERENT baseline corpora. The original in-corpus findings stand unchanged regardless of H-NEW-SURVEY outcome. H-NEW-SURVEY's only function is to test whether the asymmetric pattern replicates against natural-language baselines or dissolves into general-Arabic phonotactics.

---

## AMEND-25 — H-NEW-31.1 held-out apocalyptic-oracular control pre-registration (pre-execution)

**Timing: PRE-EXECUTION. Clean pre-registration.** Filed 2026-04-14 BEFORE H-NEW-31.1 is dispatched.

**Target:** new task (to be filed) H-NEW-31.1 held-out apocalyptic-oracular control for H-NEW-31 Tier-B PARTIAL verdict.

**Motivation.** H-NEW-31's SPACE-Medinan sub-test PASS (p=0.0146, 2-sided, classified as Tier-B PARTIAL per team-lead Turn-5) must be distinguishable from "any short apocalyptic/oracular Arabic text would produce this Meccan-incipit signature." Without a held-out control, the Meccan signature could reflect **genre** (apocalyptic oracular verse, which is dominant in Early Meccan) rather than **Quran-specific** incipit structure. The classical hypothesis under test is Quran-specific, not apocalyptic-oracular-generic.

**Primary control (Option 1 per team-lead Turn-5 preference):** Musaylima fragments (from al-Ṭabarī *Tārīkh* vol. 3 reports of the "rival prophet" claimed recitations) + al-Jāḥiẓ *al-Bayān wa-l-Tabyīn* kāhin oracular fragments (rhymed soothsayer pronouncements cited as balāgha examples, not as Quranic), filtered to incipit-bearing pieces ≥5 post-formulaic tokens. Minimum corpus size: ≥30 incipits; if <30 after honest extraction, fall back to Option 2.

**Fallback control (Option 2):** Split-corpus held-out — train classification scheme (6-class or 7-class per H-NEW-31.2 branch) on Q 1-69 only; test on Q 70-114 (sum of incipits where n_Meccan_incipits ≥ 20 in the held-out half). This is WEAKER than Option 1 (doesn't test against apocalyptic-oracular genre, only against random Quranic split), but it adjudicates the narrower question of whether the incipit-class chi-squared is sample-specific or generalizes within-Quran.

**Procedure (both options):**
1. Apply the SAME classification scheme as H-NEW-31 primary (6-class: TIME/COSMOS/PRAISE/IMPER/SPACE/OTHER).
2. Compute Fisher exact one-tailed on SPACE-Meccan (2-sided default per PRE-REG-STANDARD-02) under the control.
3. If Option 1 corpus ≥30 incipits: primary statistic is Mann-Whitney on SPACE-class rate, Quran vs Musaylima+Jāḥiẓ kāhin corpus.
4. If Option 2: 2×2 Fisher on SPACE-incipit counts, Q 1-69 vs Q 70-114.

**Pre-registered acceptance (locked):**
- **CONTROL-DISTINGUISHED:** SPACE-rate Quran significantly exceeds Option-1 control at p < 0.01 → H-NEW-31's SPACE signature is Quran-specific, NOT apocalyptic-oracular-generic. H-NEW-31 verdict upgraded from Tier-B PARTIAL to Tier-A PARTIAL (+1 classical-anchored control replication).
- **CONTROL-EQUIVALENT:** no significant difference → SPACE-incipit signature is apocalyptic-oracular-genre-typical, not Quran-specific. H-NEW-31 Tier-B PARTIAL stands with "genre-generic interpretation" footnote appended to finding file.
- **CONTROL-REVERSE:** SPACE-rate lower in Quran than control → unexpected; reported as such; triggers sensitivity re-analysis.
- **Option-2 fallback PASS:** Q 70-114 held-out split replicates SPACE-Meccan at p < 0.05 (looser threshold due to lower power after data-splitting) → within-Quran replication confirmed, but does NOT address genre question.

**Bonferroni:** k=1 for the primary control test (independent of H-NEW-31). Option 2 fallback is k=1 if Option 1 is unavailable; never runs both.

**Data sources (to be confirmed by classical-scholar before dispatch):**
- Musaylima fragments: al-Ṭabarī *Tārīkh*, text via already-extracted Arabic corpus at `data/baseline-corpora/raw/` IF PRESENT; else classical-scholar task to extract ≥20 Musaylima-attributed incipit fragments.
- al-Jāḥiẓ *al-Bayān wa-l-Tabyīn* kāhin oracles: already partially in `data/baseline-corpora/raw/jahiz-bayan.txt` if present; else extraction required.
- Blocker: classical-scholar confirms extractability of ≥30 incipit-bearing fragments from these sources BEFORE dispatch. If <30, fall back to Option 2.

**Output:** `findings/phase-b-hypotheses/h-new-31-1-apocalyptic-control.md`; `csv/h-new-31-1.json`.

- **Pre-registration date:** 2026-04-14 (filed BEFORE execution)
- **Proposed by:** team-lead (2026-04-14 Turn-5, approved as H-NEW-31-REVERSE → renamed H-NEW-31.1)
- **Filed by:** hypothesis-generator (2026-04-14)
- **Approved by:** team-lead (2026-04-14 Turn-5) — *"option 1 preferred (Musaylima / al-Jāḥiẓ kāhin) with option 2 split-corpus fallback"*

---

## AMEND-26 — FOAI sign self-correction acknowledgment (H-NEW-18-EXT classical-scholar correction)

**Timing: ALREADY LOCKED via AMEND-16.** Filed 2026-04-14 as an acknowledgment entry, not a new pre-registration.

**Context:** Classical-scholar (2026-04-14) delivered a self-correction on the FOAI asymmetry metric sign for al-Kirmānī pair directionality: the prior TSV (17 usable pairs) was tagged "A>0" under a misread of the asymmetry definition. Under correct reading of al-Kirmānī's aṣl/farʿ directionality (the semantically primary pair-member has LOWER cumulative surprisal conditioned on the secondary member's context), the predicted sign is **A<0 across all 17 usable directional rows**, not A>0.

**Resolution:** AMEND-16 already locked A<0 as the H-NEW-18-EXT prediction direction. The classical-scholar's on-disk TSV at `findings/classical-sources/kirmani-30-pair-tuples.tsv` now matches the AMEND-16 spec. No new amendment action required; acknowledging here for audit-trail completeness.

**Proposed by:** classical-scholar (2026-04-14 self-correction)
**Acknowledged by:** hypothesis-generator (2026-04-14)
**No approval needed** — AMEND-16 pre-locked the direction; this entry is retrospective documentation only.

---

# Pre-registration standing rules (non-numbered, standing-order)

These rules have project-wide scope and apply to ALL amendment filings and new hypothesis pre-registrations. Unlike numbered amendments (which target specific hypotheses), standing rules are general discipline. They are pre-approved by team-lead and cited by label.

## PRE-REG-STANDARD-02 — Two-sided default when classical source is qualitative (locked 2026-04-14 Turn-5)

**Rule.** When the classical source motivating a test is **qualitative** (a description of a rhetorical pattern, a classification claim, or a phenomenological observation without a predicted direction of magnitude), the pre-registered statistical test MUST default to **two-sided** significance testing.

**One-sided exception.** A one-sided test is permitted ONLY when ≥2 independent classical sources agree on the direction of the predicted effect. The two sources must be (a) from different authors, (b) reachable by verbatim citation to a page/paragraph, (c) agreeing on sign not just on phenomenon.

**Rationale.** Qualitative classical claims do not constrain the direction a quantification will move. Presupposing a direction in the test design bakes a confirmation bias into the pre-registration — if the effect lands opposite-signed but comparably sized, the one-sided test cannot reject and the signal is unreportable. Two-sided default preserves both directions as publishable outcomes, which is the correct treatment for a text-in-dialogue-with-tradition framing.

**Canonical example of correctly one-sided test:** H-NEW-29 (al-Jāḥiẓ *takrār maqbūl* — explicit prediction of "regular spacing more than Arabic prose"; direction locked by classical source). One-sided justified.

**Canonical example of correctly two-sided test:** H-NEW-31 (incipit-class × Meccan/Medinan; no classical source predicts "SPACE concentrates in Medinan" specifically; two-sided default). Two-sided locked.

**Standard body format when citing:** include in pre-registration header one of:
- `sided_test: two-sided (PRE-REG-STANDARD-02 default — qualitative classical source)`
- `sided_test: one-sided (PRE-REG-STANDARD-02 exception — sources [X, Y] agree on direction)`

**Pre-approved by:** team-lead (2026-04-14 Turn-5, H-NEW-31 SPACE sub-test 2-sided ruling). Applies retroactively to all in-flight pre-registrations; any one-sided test in the existing amendments must either cite its two-source justification or be converted to two-sided before dispatch.

## PRE-REG-STANDARD-03 — Class-scheme expansion is a new hypothesis, not an amendment (locked 2026-04-14 Turn-6)

**Rule.** When a pre-registered test operationalizes a phenomenon via a class scheme (N categories applied to a corpus), post-primary **expansion of the class scheme** (adding a new category, splitting an existing category, re-prioritizing classification precedence) is STRUCTURALLY a re-operationalization of the primary test, regardless of how rigorously the re-classification is pre-registered before running.

**Consequence.** Class-scheme expansions MUST be filed as **independent follow-up hypotheses** (new numbered H-NEW-N.M), NOT as amendments to the original primary. The original's verdict stands verbatim. Data reuse from the original is permitted in the follow-up but must be disclosed in the follow-up's pre-registration header.

**What counts as class-scheme expansion:**
- Adding an Nth+1 class to an N-class scheme (e.g., 6-class → 7-class with OATH).
- Splitting one existing class into two (e.g., COSMOS into COSMOS-astronomical + COSMOS-terrestrial).
- Re-ordering classification precedence in a priority-based classification (e.g., moving OATH above TIME in tie-break order).
- Re-binning a continuous scale into new cut-points after the primary run.

**What does NOT count (permitted robustness):**
- Adding a secondary null model (adversarial-flag-originated) that operates on the same class scheme — permitted under MW-2.
- Re-running the primary test with the same scheme on a held-out control corpus — permitted under the control-design family.
- Stratifying the EXISTING class scheme against a new covariate (e.g., running the 6-class scheme within each of 4 Nöldeke phases).

**Canonical boundary example:** AMEND-22 (H-NEW-31 6-class → 7-class OATH addition). Filed as amendment; REJECTED; redirected to H-NEW-31.2 as independent follow-up per this standing rule.

**Rationale.** Class-scheme expansion is feature-space redefinition. A test whose feature-space can be expanded post-primary in pursuit of a stronger result has no natural stopping point against which to apply Bonferroni discipline. Enforcing "new hypothesis, new pre-reg" preserves discipline by resetting the Bonferroni k count for the expanded scheme.

**Pre-approved by:** team-lead (2026-04-14 Turn-6, AMEND-22 rejection ruling).

## PRE-REG-STANDARD-04 — Bonferroni k and per-test α MUST be locked in pre-registration header at proposal time (locked 2026-04-14 Turn-7)

**Rule.** Every pre-registered hypothesis (novel H-NEW, classical H-CLASSIC, meta H-META, and every amendment that introduces a new test or adds a sub-test) MUST declare in its pre-registration frontmatter/header:

- `bonferroni_k: <integer>` — the explicit number of simultaneous tests in the Bonferroni family to which this test belongs.
- `bonferroni_family: <short-identifier>` — the name of the family (e.g., `h-classic-44-49`, `tomorrow-tests`, `h-new-31-sub-tests`), so the k-count is auditable against all tests claiming membership.
- `alpha_unadjusted: <float>` — the unadjusted α (typically 0.05 or 0.01).
- `alpha_bon: <float>` — the Bonferroni-corrected per-test threshold = `alpha_unadjusted / bonferroni_k`.

The hypothesis-proposer (hypothesis-generator, classical-scholar, or integrator, depending on who files) owns the k-value; computational-tester MUST NOT change k at test-time. If computational-tester discovers that k should be different (e.g., an additional sub-test was added), they must return the pre-reg to hypothesis-proposer for amendment BEFORE executing.

**Consequence of violation.** A test executed with a test-time-chosen k (rather than a pre-reg-locked k) is structurally unreportable regardless of its nominal result — the k-choice is result-dependent and thus corrupts the Bonferroni discipline.

**Canonical failure-mode example:** H-NEW-31 Tier-B sub-test was executed with computational-tester choosing Bonferroni k = 6 at test-time (counting the six incipit categories) when the pre-reg header had left k unspecified. This created a discipline slip: the same data could equally well have motivated k=2 (binary TIME/SPACE collapse) or k=12 (6-class × 2 phase). The test-time k-choice was benign in that case but is structurally a result-dependent design decision.

**Canonical correct example:** H-CLASSIC-44..49 family pre-reg (2026-04-14) locks `bonferroni_k: 6` (family-size) and `alpha_bon: 0.0083` (= 0.05 / 6) in the family spec file BEFORE any dispatch. All six tests inherit this threshold; no test-time k-choice is possible.

**Interaction with PRE-REG-STANDARD-02:** the sided-test declaration AND the bonferroni_k declaration MUST both appear in the header. A pre-reg with `sided_test: one-sided` but no `bonferroni_k` is incomplete.

**Interaction with amendments:** when an amendment adds a sub-test to an existing family, the amendment MUST either (a) update the family's bonferroni_k and all sibling tests' alpha_bon (which requires re-pre-registering the siblings if not already run) OR (b) declare the added sub-test as a NEW family with its own k=1 and justify why it is not a sibling of the existing family.

**Standard body format when citing:**

```yaml
bonferroni_k: 6
bonferroni_family: h-classic-44-49
alpha_unadjusted: 0.05
alpha_bon: 0.0083
```

**Retroactive applicability.** Any in-flight pre-reg lacking these four fields must have them added by the current owner BEFORE computational-tester execution. The retroactive add is permitted only for pre-execution pre-regs; post-execution additions are structurally prohibited.

**Pre-approved by:** team-lead (2026-04-14 Turn-7, integrator-relayed PRE-REG-STANDARD-04 addition from H-NEW-31 Tier-B mis-spec).

**Cross-reference (2026-04-14):** PRE-REG-STANDARD-07 (VERIFIED-tier classical claims do NOT receive Bonferroni-relaxation) interacts with STANDARD-04 at the header-locking stage: Bonferroni k and per-test α MUST be locked at proposal time under STANDARD-04, AND they must be locked at the k appropriate for *all* confirmable-rate-relevant classical claims regardless of MW-6 tier, per STANDARD-07. The two standards together prohibit retroactively loosening Bonferroni on VERIFIED-tier claims after observing the MW-6 moderator inversion (deliverable #129).

---

*Protocol clarification added 2026-04-14 Turn-6: the protocol-reminder at line 494 ("if a hypothesis shows RESULT-DEPENDENT changes in design AFTER computational-tester has executed, it is no longer a valid pre-registration") is now supplemented by MW-2 origin-qualifier (secondary nulls require adversarial-flag origin), PRE-REG-STANDARD-03 (class-scheme expansions must be new hypotheses, not amendments), and PRE-REG-STANDARD-04 (Bonferroni k + α locked in pre-reg header at proposal time). AMEND-20 and AMEND-22 are the two boundary examples establishing these rules.*

---

## PRE-REG-STANDARD-05 — Hierarchical-family Bonferroni when tests decompose into structurally-distinct families (locked 2026-04-13, team-lead approval)

**Rule.** When a dispatch wave or pre-registration includes tests that decompose cleanly into structurally-distinct families, the Bonferroni correction MUST be computed *within each family* using the family's local k, NOT across the union as a flat-pooled k. Family-wise α is allocated equally across families.

**Specification.**

- Identify N structurally-distinct families. The default trio is:
  1. **classical-claim replication** — direct empirical tests of named-classical predictions (H-CLASSIC-NN family)
  2. **parent-EXT lineage** — extensions/follow-ups to confirmed parent findings (H-NEW-NN-EXT family)
  3. **novel-discovery** — first-time tests of newly-proposed hypotheses with no parent (H-NEW-NN family)
- Set **family-wise α = 0.05 / N** (e.g., for N=3 families → α_family = 0.0167).
- Within each family, apply standard Bonferroni: per-test α = α_family / k_family.
- Each family's k is independent. A test's α_bon depends ONLY on its own family's k, not on the cross-family union count.

**Why NOT flat-pooled k.** A flat-pooled correction (e.g., k = 20 across the entire dispatch) over-punishes borderline tests in *every* family because the rejection bar is set by the worst-case family (the one with the most tests). For a borderline N-LIMITED test in a 3-test family, having to clear α/20 instead of α/3 turns its expected pass rate from ~50% to ~5% — a 10× reduction with no scientific basis. The structural distinction between families means a pass in one family doesn't inflate the false-positive rate in another (they test different hypotheses about different mechanisms with different baselines).

**Why family-wise α / N is honest.** It controls the family-wise error rate at the *cross-family* level (each family is allocated equal protection budget), then lets each family allocate its budget internally to its own tests. This is the standard approach in clinical trial subgroup analysis and gene-set enrichment testing.

**Decision rule for "structurally-distinct family".** Two tests belong to the same family if they share BOTH:
1. The same null model / baseline (e.g., both use Bukhari-noquran shuffle null)
2. The same target structure (e.g., both test rhyme-mechanism, or both test munāsaba-mechanism)

If they share only one, they are different families. If they share neither, they are obviously different families.

**Canonical correct example:** the post-power-analysis dispatch wave (2026-04-13) decomposed 20 tests into:
- H-CLASSIC-44 to 49 (classical-claim family, k=6, α_per = 0.0167/6 = 0.00278)
- H-NEW-EXT lineage (k=10, α_per = 0.0167/10 = 0.00167)
- novel-discovery (k=4, α_per = 0.0167/4 = 0.00417)

vs naive pooled k=20 → α_per = 0.05/20 = 0.0025 for all 20 tests. Hierarchical preserves expected pass rate at ~12 vs ~8 under naive pooling, with no inflation of cross-family false-positives.

**Canonical failure-mode example.** A naive pooled k = 20 dispatch would require H-CLASSIC-47 (al-Biqāʿī within-surah Jaccard, an extension of an already-confirmed parent finding with z ≈ +10) to clear α = 0.0025. This is fine for that test (it has high power), but the *same* threshold applied to H-NEW-30 (N=8 Khawātim al-Ḥashr morphological signature) would require a near-impossible effect size for descriptive-N data. The hierarchical version recognizes that H-CLASSIC-47 lives in a 6-test family and H-NEW-30 lives in (or rather, was correctly demoted out of) a different family, and applies appropriate per-family thresholds.

**Interaction with PRE-REG-STANDARD-04.** Each family-of-tests must declare its own `bonferroni_family`, `bonferroni_k`, `alpha_unadjusted` (= 0.05/N where N is the number of families in the dispatch), and `alpha_bon` (= alpha_unadjusted / k). The header MUST include both a family-name and a parent-dispatch-name when applicable.

**Standard body format when citing:**

```yaml
bonferroni_k: 6
bonferroni_family: h-classic-44-49
parent_dispatch: 2026-04-13-power-analysis-wave
families_in_dispatch: 3
alpha_unadjusted_dispatch: 0.05
alpha_unadjusted_family: 0.0167  # = 0.05/3
alpha_bon: 0.00278  # = 0.0167/6
```

**Retroactive applicability.** Existing pre-regs that used flat-pooled k are not invalidated by STANDARD-05; they remain valid under their original specification. STANDARD-05 applies to new dispatches *after* 2026-04-13. When migrating an existing flat-pooled family to hierarchical, the migration MUST be a NEW pre-reg, not an amendment, per PRE-REG-STANDARD-03.

**Pre-approved by:** team-lead (2026-04-13, ruling on meta-analyst power-analysis dispatch). Surfaced as the third methodology standing rule from meta-analysis work (effect-size-inventory / power-analysis / p-curve diagnostic dispatch chain). Source: `findings/cross-finding/pending-power-analysis.md`.

---

## AMEND-27 — H-NEW-34.1 three-point checklist lock-in (pre-execution amendment to 2026-04-13 pre-reg)

**Status:** PRE-REGISTERED (pre-execution amendment to an already-pre-registered follow-up)
**Date:** 2026-04-14
**Filed by:** hypothesis-generator
**Authority:** team-lead approval (relayed via integrator 2026-04-14); skeptical-auditor three-point checklist (origin: audit-025 B1 blocker)
**Parent finding:** H-NEW-34 (NULL on primary two-tailed) → H-NEW-34.1 (follow-up pre-reg 2026-04-13)
**Governs:** execution of B1 Muʿallaqāt run + length-stratification + three-baseline consistency check
**MW-2 origin qualifier:** adversarial-flag origin (skeptical-auditor audit-025 §4 B1 blocker) — ORIGIN LEGITIMATE for secondary-null-adjacent tightening.

### What this amendment does

Locks three additional pre-commitments onto the 2026-04-13 H-NEW-34.1 pre-reg BEFORE execution:

1. **One-sided under-dispersion direction** — Quran z < baseline z, justified by PRE-REG-STANDARD-02 (≥2 independent prose baselines already agree on sign per parent H-NEW-34 Table 1). Not a post-hoc narrowing; parent H-NEW-34 was two-tailed, H-NEW-34.1 was pre-registered before execution as mechanism test.

2. **Length-stratified dispersion statistic** — 10-decile binning on verse-final-word letter-count using pooled Quran+baselines distribution for cut-points; per-decile inverse-variance-weighted mean as primary statistic; raw and stratified reported side-by-side; stratified is authoritative for PASS/FAIL tie-breaker.

3. **Three-baseline consistency requirement** — PASS requires all 3 baselines (Bukhari-noquran, Jāḥiẓ Ḥayawān, Muʿallaqāt pooled-7-odes) to show Quran-specific one-sided under-dispersion at α_bon = 0.0033 (= 0.01 / 3). 2-of-3 = PARTIAL. ≤1-of-3 = NULL. Any baseline showing Quran over-dispersing = MECHANISM-INCONSISTENT escalation.

### Why this is permitted as amendment (not a new hypothesis per PRE-REG-STANDARD-03)

- **NOT a class-scheme expansion.** The unit of analysis (verse-final-word abjad residue), the moduli (7, 11, 19), the baselines (already listed in 2026-04-13 pre-reg footnote; now promoted to primary three-baseline family), and the target statistic (χ² vs uniform) are all unchanged.
- **IS a tightening** of operationalization per skeptical-auditor adversarial-flag origin (audit-025 §4 B1 blocker requested Muʿallaqāt + length-mediation check). MW-2 origin-qualifier satisfied: origin is auditor, not hypothesis-proposer initiative.
- **Pre-execution.** Computational-tester has NOT yet executed H-NEW-34.1. The Bonferroni k update (from k=3 moduli to k=3 baselines, α = 0.01 / 3 = 0.0033) is a stricter threshold, not a laxer one — the amendment makes PASS harder to achieve.

### Committed retractions if NULL

- H-NEW-34 reverse signal downgrades from "candidate M-6 fāṣila-substrate evidence" to "length-mediated artifact, not signal."
- MASTER-FINDINGS-LEDGER §5 annotation updated to reflect length-confound closure.
- No downstream promotion of H-NEW-34 into H-NEW-SURVEY-EXT (task #84 branch not activated).

### Committed reporting if PASS

- H-NEW-34.1 positive finding written as: "Quran shows one-sided under-dispersion of verse-final-word abjad modular residues across all three independent classical-Arabic baselines, length-stratified, at α_bon = 0.0033. Rhyme-mechanism routing (2026-04-13 Muʿallaqāt-specific comparison) adjudicates mechanism vs residual."
- If Muʿallaqāt-specific gap ≥ 3 at ≥1 m: novel-finding branch active; H-NEW-SURVEY-EXT task #84 activated.
- If Muʿallaqāt-specific gap < 1: mechanism-confirmed branch; M-6 fāṣila-substrate candidate promoted.

### Filing path

Amendment text appended to `findings/phase-b-hypotheses/h-new-34-1-prereg.md` under "AMENDMENT 2026-04-14 — integrator three-point checklist lock-in" section. Frontmatter updated with `sided_test`, `baselines`, corrected `bonferroni_k`, corrected `alpha_bon`.

### Dispatch chain

1. hypothesis-generator → this amendment (**done**).
2. computational-tester → executes H-NEW-34.1 per the locked three-point protocol.
3. skeptical-auditor → audits compliance with three-point checklist.
4. integrator → integrates verdict into MASTER-FINDINGS-LEDGER.

---

## AMEND-28 — Pre-publication nawʿ-range mechanical check (standing)

**Filed:** 2026-04-14
**Filed-by:** classical-scholar (green) on team-lead directive
**Trigger:** MW-6 backport audit spot-check discovered 3 out-of-range nawʿ citations (Itqān "nawʿ 83-84" vs 80-nawʿ edition ceiling; Burhān "nawʿ 59" fawāṣil vs 47-nawʿ ceiling; Itqān muqaṭṭaʿāt internal contradiction "nawʿ 41" vs "nawʿ 43"). Full-corpus mechanical scan (`scripts/naw_range_audit.py`) confirmed 24 live out-of-range errors across 14 files; memo filed at `findings/classical-sources/naw-range-audit-2026-04-14.md`.
**Type:** standing methodological amendment; pre-publication gate.

### Standing rule (verbatim)

> Any finding file, audit memo, or synthesis entry citing a classical nawʿ number must include that number's verification against the stated edition's total-nawʿ count. If citation-number ≤ edition-total → verified-against-range (still requires VERIFIED / PENDING / SECONDARY-TRIANGULATED per MW-6). If citation-number > edition-total → auto-ERROR, retag as PENDING with correct-location flag. Reference totals: al-Zarkashī *Burhān fī ʿUlūm al-Qurʾān* (Abū l-Faḍl Ibrāhīm ed.) = 47 anwāʿ; al-Suyūṭī *Itqān fī ʿUlūm al-Qurʾān* (Abū l-Faḍl Ibrāhīm ed.) = 80 anwāʿ. Scope: applies to all new dispatches going forward; backport pass triggered 2026-04-14.

### Why this amendment exists

The MW-6 tagging framework (VERIFIED / PENDING / SECONDARY-TRIANGULATED) disciplines the *paraphrase-confidence* dimension but takes the *nawʿ number itself* as a given. The spot-check revealed that the nawʿ number is itself unreliable when sourced from human recall — a 25–38 % error rate in the audited sample. A purely mechanical range-check is cheap, catches all range-overflows with certainty, and takes human recall out of the critical path at the publication boundary.

The structural analogue: MW-6 = doctrine-level verification gate; AMEND-28 = citation-integer mechanical gate. They are complementary.

### Operational protocol

1. Before any finding/audit/synthesis text is marked publication-ready, run `scripts/naw_range_audit.py` (or equivalent mechanical check) against the staging set.
2. Live-error count must be **0** for the staging set before publication.
3. Any out-of-range citation forces immediate PENDING retag in the canonical format:
   `**[nawʿ number PENDING per MW-6 mechanical-scan <date>; cited "nawʿ N" is out-of-range — <edition> has M anwāʿ; correct location for <topic> is candidate nawʿ X pending physical verification]**`
4. The mechanical scan is additive to MW-6, not a replacement. A citation can be range-valid (passes AMEND-28) but still PENDING for paraphrase-confidence (fails MW-6), or vice versa.

### Edition-total registry (extensible)

- al-Zarkashī *Burhān fī ʿUlūm al-Qurʾān* — Abū l-Faḍl Ibrāhīm ed. — **47 anwāʿ**
- al-Suyūṭī *Itqān fī ʿUlūm al-Qurʾān* — Abū l-Faḍl Ibrāhīm ed. — **80 anwāʿ**
- (add further edition-totals as new classical sources enter the corpus; register with physical edition identifier before citation)

### Backport status (2026-04-14)

- **Flagship spot-check errors retagged:** 3 of 3 done.
  - Itqān "nawʿ 83-84" *ḥusn al-ibtidāʾ / ḥusn al-intihāʾ* — `team-discovery-synthesis.md:3182` → PENDING.
  - Burhān "nawʿ 59" fawāṣil — `team-audits/audit-018.md` three sites (lines 11, ~30, 63) → PENDING.
  - Itqān muqaṭṭaʿāt "nawʿ 41" vs "nawʿ 43" contradiction — `classical-quantitative-claims-audit.md:155` (CC-050), `team-discovery-synthesis.md:3130` and `:1386`, `team-audits/audit-004.md:52` → all 4 sites PENDING.
- **Remaining 21 live out-of-range sites:** queued for **Option C lazy-repair** — retagged in-place when containing file is next touched for other reasons. Enumeration in `findings/classical-sources/naw-range-audit-2026-04-14.md`.
- **Mechanical scanner preserved** at `scripts/naw_range_audit.py` for reproducibility and re-run on any future dispatch cycle.

### Integrator enforcement hook (added 2026-04-14 per team-lead turn-5 Option-C directive)

Integrator should, on each synthesis edit, check whether the edited section contains a PENDING-tagged nawʿ citation and opportunistically attempt Phase-2 secondary-triangulation if ≥2 independent sources are accessible via WebSearch within a single cycle. If not accessible, leave PENDING.

This makes Phase-2 repair **cumulative but not schedule-critical**: citations get secondary-triangulated as a side-effect of any touch, without blocking the forward pipeline. A PENDING retag is a statement about **citation locatability**, not about **the statistical finding** or **the substantive classical doctrine** — both of which stand unaffected.

### Option-C two-phase completion status (2026-04-14)

- **Phase 1 (immediate PENDING retag on all 20 live out-of-range sites):** **done** (2026-04-14, classical-scholar).
  - 14 retags completed in files: `TEAM-AMENDMENTS-LOG.md` (×2), `team-discovery-synthesis.md` (×1), `interim-synthesis-2026-04-14.md` (×3), `abjad-residue-fasila-mechanism.md` (×2), `fractal-self-similarity.md` (×1), `tda-manifold.md` (×1), `team-discovery-017.md` (×1), `hapax-slot-mechanism.md` (×2), `negation-taxonomy.md` (×2), `classical-quantitative-claims-audit.md` (×1), `audit-020.md` (×1), `audit-012.md` (×1), `audit-008.md` (×1).
  - All retags use standardized format: `**[nawʿ PENDING per MW-6 mechanical-scan 2026-04-14; cited "nawʿ N" is out-of-range — Burhān/Itqān Abū l-Faḍl Ibrāhīm ed. has X anwāʿ; nawʿ number retagged per MW-6 mechanical scan; substantive classical doctrine unchanged; statistical finding unaffected; candidate correct locus: nawʿ M <topic> pending Phase-2 secondary-triangulation]**`.
- **Phase 2 (lazy secondary-triangulation):** standing practice; enforced opportunistically via integrator enforcement hook above.

### Dispatch chain

1. classical-scholar → full-corpus mechanical scan (**done**).
2. classical-scholar → flagship PENDING retags on 3 confirmed errors (**done**).
3. classical-scholar → file AMEND-28 in amendment log (**done** — this entry).
4. classical-scholar → Phase-1 PENDING retags on all remaining live out-of-range sites (**done** 2026-04-14).
5. classical-scholar → append integrator enforcement hook for Phase-2 lazy repair (**done** — this subsection).
6. All agents → observe AMEND-28 gate on all new dispatches from 2026-04-14 forward.
7. integrator → apply Phase-2 secondary-triangulation opportunistically per the enforcement hook.

---

## PRE-REG-STANDARD-06 — Multi-scholar convergence does NOT count as independent evidence (locked 2026-04-13, team-lead approval)

**Rule.** When ≥2 named scholars predict the same phenomenon and the prediction is tested as a single empirical target, the multi-scholar endorsement does NOT count as independent corroboration. Each scholar's endorsement counts once in the claim-weight tally; shared doctrinal inheritance (e.g., al-Biqāʿī inheriting from al-Zarkashī, Cuypers inheriting from al-Biqāʿī, Farrin inheriting from Cuypers) further reduces effective N.

**Operational consequences.**

1. **Bonferroni-family reduction.** A multi-scholar-endorsed claim does NOT receive a reduced k. It is one test in the family it belongs to, not 1/N of a test.
2. **Effect-size meta-analysis.** When tabulating effect sizes (`findings/cross-finding/effect-size-inventory.tsv`), do NOT inflate the apparent independence count by listing each scholar separately. The claim_count is 1 per claim, regardless of how many scholars endorsed it.
3. **Convergence reporting in synthesis files.** Phrases like "X, Y, and Z scholars converge on this prediction" are NOT to be treated as independent corroborating evidence. They may be reported descriptively, but the synthesis MUST add the qualifier "this convergence reflects shared doctrinal inheritance, not independent confirmation" or equivalent.
4. **Doctrinal-inheritance discount.** When the second-or-later endorsing scholar is a known intellectual descendant of the first (Shāfiʿī chain Zarkashī → Suyūṭī → Biqāʿī; modern macro-ring chain Biqāʿī → Farrin → Cuypers), the effective independent N is lower than the literal scholar count. For Bayesian weighting purposes, treat doctrinal-descendant endorsements as contributing < 0.5 effective independent evidence units relative to a first-endorser.

**Empirical justification.** scholar-convergence-tracker.md (2026-04-13, meta-analyst) tabulated all multi-scholar convergence cases in the H-META-1 120-claim corpus and found:

- 5 of 5 convergence-CONFIRMED rows are local-scope predictions
- 3 of 3 convergence-REFUTED rows are global-scope predictions
- Fisher exact one-sided p ≈ 0.018 for the local-vs-global split

The strongest convergence in the corpus — al-Biqāʿī + Farrin + Cuypers macro-ring — failed MORE decisively (z = −4.87) than any single-scholar prediction of similar shape. Convergence in this case tracked shared *aesthetic intuition* about whole-mushaf symmetry, not independent observation. The pattern repeats for word-count universalism (al-Nursī + Al-Kaheel + others, all REFUTED) and for the modern numerology cluster (Khalifa-lineage convergence on mod-19 claims, all REFUTED).

The mechanism: when claims about a text are aesthetically appealing, multiple scholars are likely to endorse them *for the same reason* (the aesthetic). This produces apparent convergence without producing independent observational confirmation. The convergence is doctrinal correlation, not inferential independence.

**Canonical correct example.** The Mūsā = 136 mentions claim is endorsed by both al-Suyūṭī and al-Zarkashī. STANDARD-06 says: count this as ONE confirmed claim, not two. The two scholars likely shared a count or one inherited from the other; the empirical confirmation is one observation.

**Canonical failure-mode example.** A reader of MASTER §4 might be tempted to write "the macro-ring hypothesis is supported by al-Biqāʿī (15th c.), Farrin (2014), and Cuypers (2009) — three independent scholars converge on the prediction." STANDARD-06 prohibits this framing. The correct framing is: "the macro-ring hypothesis appears in al-Biqāʿī's *Naẓm al-Durar* and was independently re-proposed by Cuypers and Farrin; the convergence reflects shared aesthetic intuition about whole-mushaf symmetry rather than independent corroboration. The hypothesis is REFUTED by project test at z = −4.87, with the convergence non-multiplier rule explaining why three scholars endorsing the same broken pattern is empirically unsurprising."

**Interaction with H-META-1 weighting.** H-META-1's confirmable-signature classifier already implicitly handles this through its substance_type and broad_hisab_claim features. STANDARD-06 makes the rule explicit and applies it to claim weighting outside of H-META-1 as well.

**Interaction with PRE-REG-STANDARD-04 / 05.** The Bonferroni k for a test that has multi-scholar endorsement is k=1 (one test), not k=N (one per scholar). The k-count is per-test, not per-endorsement.

**Standard body format when reporting a multi-scholar-endorsed claim:**

```yaml
claim_id: <id>
endorsing_scholars: [scholar-A, scholar-B, scholar-C]
endorsement_count: 3  # for descriptive reporting only
effective_independent_n: 1  # for Bonferroni / weighting purposes
doctrinal_inheritance: "scholar-B inherits from scholar-A; scholar-C inherits from scholar-B"
convergence_disclaimer: "Multi-scholar endorsement is descriptive only; per PRE-REG-STANDARD-06 it does not count as independent corroboration."
```

**Retroactive applicability.** Existing pre-regs and findings files that treated multi-scholar convergence as independent evidence MUST be updated. Specifically: any synthesis-file phrase of the form "X scholars converge" or "supported by X independent classical authorities" must be re-checked against STANDARD-06 and either rewritten with the disclaimer or downgraded to descriptive-only framing. The convergence-non-effect footnote routed to integrator on 2026-04-13 (cross-finding/scholar-convergence-tracker.md flag #1) is the migration mechanism.

**MASTER §6 standing meta-pattern entry.** The convergence non-effect is filed as **M-9 "Convergence-does-not-multiply"** in the standing meta-patterns section of the master findings ledger, with the Fisher exact p = 0.018 as supporting evidence and STANDARD-06 as the operational rule.

**Pre-approved by:** team-lead (2026-04-13, ruling on meta-analyst scholar-convergence-tracker deliverable). Surfaced as the sixth methodology standing rule from meta-analysis work and the second rule (after STANDARD-05) from the cross-finding deliverable chain.

**Source:** `findings/cross-finding/scholar-convergence-tracker.md` §3 (cross-scholar convergence cases) and §7 (findings flagged for downstream tasks).

**Cross-reference (2026-04-14):** STANDARD-07 (VERIFIED-tier claims do NOT receive Bonferroni-relaxation) is a sibling of STANDARD-06 in that both rules prevent an apparently-credentialed structural feature from being re-purposed as "extra evidence" for a claim. STANDARD-06 prohibits treating multi-scholar convergence as independent corroboration; STANDARD-07 prohibits treating verbatim-verification tier as a Bonferroni-relaxation lever. Both rules are grounded in meta-analyst deliverables (#126 convergence tracker for STANDARD-06; #129 MW-6 moderator + #132 Option A retrain for STANDARD-07). Both rules correct an initial intuition the project held (that the structural feature in question would add evidential weight) with within-corpus statistical testing that showed it did not.

---

## PRE-REG-STANDARD-07 — VERIFIED-tier classical claims do NOT receive Bonferroni-relaxation (locked 2026-04-14, team-lead approval)

**Rule.** A claim's MW-6 verbatim-verification tier (VERIFIED, SECONDARY-TRIANGULATED, SECONDARY, PENDING, UNTAGGED) MUST NOT be used as a reason to loosen Bonferroni correction, relax per-test α, or grant "high-confidence-source exemption" from the family-wise error budget. Bonferroni k and per-test α are locked at proposal time per STANDARD-04, and the value of k is determined by the inferential-family structure, not by the verbatim-citation provenance of the classical source.

**Background — the empirical finding that motivates this standard.** The MW-6 protocol (2026-04-14 classical-scholar lane) was designed as a verbatim-citation-confidence tiering of classical-source citations, with the pre-test hypothesis that VERIFIED-tier claims (those with direct manuscript or critical-edition quotations) would confirm at a HIGHER empirical rate than SECONDARY-tier claims (citations routed through modern intermediaries or paraphrases). The meta-analyst lane tested this hypothesis under deliverable #129 (`findings/cross-finding/mw6-reliability-moderator.md`) restricted to the classical-medieval era (n = 62) to avoid era × tier confound, and found the OPPOSITE: VERIFIED-tier confirms at 0.618 [0.384, 0.827], SECONDARY-tier at 0.829 [0.696, 0.929]. Cross-tier ratio VERIFIED/SECONDARY = 0.748 [0.457, 1.047], **P(VERIFIED > SECONDARY in confirmable rate) = 0.048** under Beta-binomial Jeffreys posterior Beta(c+0.5, n-c+0.5), n_iter = 20000. **Mechanism:** the VERIFIED tier is over-populated with structural-formal claims that have harder pass-bars at the operationalization stage — verbatim-confidence rigor selects for substantively committed claims (specific, numerically pinned, structurally unambiguous), and substantively committed claims fail more often than vague-paraphrase claims do. VERIFIED-tier predicts *testability*, not *reliability*.

The independent second leg — Option A H-META-1 retrain with MW-6 as a classifier feature (deliverable #132, `findings/cross-finding/h-meta-1-mw6-retrained.md`) — added `mw6_tier` as a 5-level one-hot feature to the H-META-1 L1-logistic confirmable-signature classifier and produced a **zero-lift result**: LR L1 5-fold cross-validated accuracy delta = **+0.0000** (baseline = retrained = 0.7820). All 5 MW-6 tier one-hot coefficients zero out under L1 penalty in the full-data model. The MW-6 moderator signal is fully absorbed by `substance_type` and `school=modern` at the classifier feature level — it is not a missing reliability dimension, it is a re-projection of dimensions the classifier already uses.

**The standing rule (STANDARD-07):**

> When computing Bonferroni correction for a pre-registration that includes classical-source claims, the classical claims' MW-6 tier does NOT enter the k-computation. A VERIFIED-tier classical claim consumes exactly one Bonferroni cell, identical to a SECONDARY-tier or PENDING-tier classical claim. Per-test α is not adjusted upward for high-MW-6-tier claims; the family-wise α is allocated equally across all tests regardless of source-tier provenance.
>
> A pre-registration MUST NOT contain any clause of the form "because these classical claims are VERIFIED-tier, we use a looser α", "because this claim has a verbatim citation from [classical source], it is exempted from Bonferroni", or any equivalent construction that treats MW-6 tier as an evidential multiplier. Such clauses are pre-registration-discipline violations and MUST be caught at proposal review.
>
> MW-6 tier continues to govern what it was designed to govern: (a) traceability / audit / verification at the citation layer, (b) flagging of claims that cannot be cleanly operationalized without a manuscript re-check (PENDING), (c) downstream scholarship accountability. MW-6 tier does NOT govern: (a) Bonferroni k, (b) per-test α, (c) the prior probability of the claim confirming, (d) the classifier's feature weighting.

**Specification.** Pre-registration headers that include classical-source claims retain their MW-6 tag per the existing MW-6 protocol, but the tag is treated as documentation of the citation-layer confidence only, not as a signal for statistical-family construction:

```yaml
classical_claim_tiers:
  - {id: H-CLASSIC-XX-sub-A, mw6: VERIFIED, bonferroni_share: 1/k}
  - {id: H-CLASSIC-XX-sub-B, mw6: SECONDARY, bonferroni_share: 1/k}
  - {id: H-CLASSIC-XX-sub-C, mw6: PENDING, bonferroni_share: 1/k}
```

Each sub-test consumes an equal Bonferroni share 1/k. MW-6 is present for provenance, absent from the α arithmetic.

**Scope.** STANDARD-07 is a rule about **Bonferroni and α**, not about the full evidential weight of VERIFIED-tier claims. A VERIFIED-tier citation is still stronger evidence at the classical-scholarship / provenance / traceability layer — STANDARD-07 does not dispute this. It says only that the stronger-provenance claim does not get looser statistical correction at the project's inferential layer, because the meta-analyst lane has shown empirically that MW-6 tier does NOT predict empirical confirmation rate in the monotone direction that would justify relaxation.

**Retroactive applicability.** Any in-flight pre-reg that contains MW-6-tier-dependent Bonferroni relaxation or α-looseness must have those clauses removed by the current owner BEFORE computational-tester execution. The retroactive removal is permitted only for pre-execution pre-regs; post-execution relaxation of Bonferroni based on MW-6 tier is structurally prohibited and would be caught under PRE-REG-STANDARD-04 as a post-execution header change.

**Interaction with existing rules:**

- **PRE-REG-STANDARD-04 (Bonferroni k + α locked in pre-reg header at proposal time).** STANDARD-07 is downstream of STANDARD-04: STANDARD-04 requires that k and α be locked at proposal time; STANDARD-07 constrains the *value* of k / α at that lock-in point by prohibiting MW-6-tier-dependent loosening. The two standards together prohibit retroactively loosening Bonferroni on VERIFIED-tier claims after observing the MW-6 moderator inversion (deliverable #129).
- **PRE-REG-STANDARD-06 (multi-scholar convergence does not count as independent evidence).** STANDARD-07 is a sibling of STANDARD-06 in that both rules prevent an apparently-credentialed structural feature (convergence of scholars for 06; verbatim-verification provenance for 07) from being re-purposed as an evidential multiplier in the statistical-family construction. Both rules are grounded in within-corpus meta-analyst statistical tests that invalidated an initial project intuition.
- **MW-6 (verbatim citation tier protocol, §6b).** STANDARD-07 does NOT repeal MW-6. MW-6 remains the operational citation-confidence tiering protocol; STANDARD-07 constrains *how the tier metadata is permitted to enter the inferential layer*. MW-6 governs provenance; STANDARD-07 clarifies that provenance is not Bonferroni-relevant. The §1 Tier-A meta-finding item #5b (MW-6 moderator + Option A retrain triangulation) consolidates the empirical grounding for this standard.
- **H-META-1 classifier (§1 item #5).** STANDARD-07 is complementary to the H-META-1 finding that claim-side features predict empirical verdict at 78.2% CV accuracy: MW-6 tier is one candidate feature that H-META-1 did NOT load (Option A retrain zero-lift), which is additional evidence that MW-6 tier is not a hidden reliability axis.

**Enforcement.** At classical-scholar proposal-review stage, any pre-reg containing MW-6-tier-dependent Bonferroni or α language must be flagged and the clause removed before dispatch to computational-tester. If the clause reaches execution stage unchallenged, the finding is filed under the same audit-discipline category as STANDARD-04 violations (post-execution header changes, audit-027 class).

**Pre-approved by:** team-lead 2026-04-14 (routing of PRE-REG-STANDARD-07 draft from meta-analyst, grounded in deliverables #129 MW-6 reliability moderator and #132 Option A H-META-1 retrain). Surfaced as the seventh methodology standing rule from meta-analysis work and the third rule (after STANDARD-05 and STANDARD-06) from the cross-finding deliverable chain.

**Source:** `findings/cross-finding/mw6-reliability-moderator.md` (deliverable #129, moderator posterior) and `findings/cross-finding/h-meta-1-mw6-retrained.md` (deliverable #132, Option A retrain) with pre-registration `findings/cross-finding/h-meta-1-mw6-prereg.md` six-cell decision matrix; consolidated §1 Tier-A entry at MASTER-FINDINGS-LEDGER.md item #5b (2026-04-14). Task #141 (integrator filing).

---

## MW-8 — Classical-side parent-task data-coherence gate (standing rule, 2026-04-13)

**Trigger:** Two AUDIT-BLOCKERS in one classical-scholar cycle (Task #36 H-NEW-11-EXT and Task #33 H-NEW-4-EXT, both filed 2026-04-13) catching pre-reg defects BEFORE compute waste. Both involve a re-pre-registration filed downstream of a parent task whose actual data already determines or contradicts the new test.

**Defect classes observed in the two instances:**

1. **Task #36 (H-NEW-11-EXT) — empirical-direction-conflict defect.** A re-prereg was drafted with a "Yūsuf-top" Binary 1 hypothesis and a "Mūsā/Nūḥ-bottom-pair" Binary 2 hypothesis. Cross-check against parent task #18 data (`findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md` §2.4) revealed that on the locked 5-prophet overlap, the empirical |z| ranking is Ibrāhīm 3.80 > Nūḥ 3.50 > Yaḥyā 3.41 > Mūsā 3.23 > **Yūsuf 2.37** (rank 5, last). Binary 1 was maximally inverted; Binary 2 was partially falsified (Mūsā in bottom-2, but Nūḥ at rank 2 in top); joint k=2 test definitionally falsified. Same defect class as the dropped Lūṭ counter-prediction (audit-blocker round 1), which was caught — but the primary direction was missed because the audit focused only on the counter-prediction sub-test.

2. **Task #33 (H-NEW-4-EXT) — parent-verdict-contradiction defect.** A re-prereg was drafted with the framing "Task #6 established absolute effect; this task adjudicates whether that effect EXCEEDS the universal ḥusn al-ibtidāʾ baseline." Parent task #6 actual verdict per `findings/phase-b-hypotheses/team-discovery-004.md` line 14: **`verdict: REFUTED`** — no checkpoint passes Bonferroni, direction reverses at cp=500 and cp=1000. The premise of #33 (that #6 established the absolute effect) was incompatible with a refuted-with-direction-reversal parent.

**The standing rule (MW-8):**

> When a re-pre-registration is filed downstream of a completed parent task, the classical-scholar lane (or whoever drafts the re-prereg) MUST audit the parent task's verdict text and any locked empirical data (z-rankings, sign-tests, effect-direction tables) against EVERY pre-registered direction in the new test, BEFORE the new test is dispatched to computational-tester.
>
> The audit must verify:
>
> (a) **Verdict compatibility.** The parent task's recorded `verdict` (CONFIRMED / REFUTED / NULL / MIXED) must be compatible with the premise of the new test. If the parent verdict is REFUTED, the new test cannot rely on the parent finding as established background.
>
> (b) **Direction non-determination.** None of the pre-registered directions in the new test (primary or counter) may be already determined by data the parent task explicitly recorded. If the parent already shows the answer, the new test is a forking-paths violation, not a pre-registration.
>
> (c) **Scale coherence.** The scale at which the new test operates must match the scale at which the parent task's verdict applies. A new test at a different operational scale (e.g., letter-graphemic vs lemma-TTR) is permitted, but must be explicitly framed as scale-shifted, not as a direct downstream confirmation.
>
> If any of (a), (b), (c) fails, the re-prereg is BLOCKED at the classical-scholar pre-execution gate. The classical-scholar must surface options to team-lead (typically: drop, reframe, sign-flip-prohibited, or scale-shift) and await ruling before any dispatch.

**Why the rule needs to exist:**

The original audit pattern (audit-021 onward) checked re-preregs for citation defects, MW-tier compliance, and Bonferroni hygiene, but did NOT systematically check that the *parent task's actual recorded data* was compatible with the new test's pre-registered directions. The two 2026-04-13 instances show that this is a recurring failure mode: hypothesis-generators draft re-preregs from the project's narrative description of a parent finding, not from its locked data tables. When the narrative description and the data table diverge — which they do at non-trivial rates, especially for parents with mixed/complex verdicts — re-preregs end up testing directions that are already known.

**Operational implementation:**

1. Classical-scholar adds a "parent-task data-coherence audit" step to the standard re-prereg drafting workflow. The step takes ≤15 min and consists of: (a) read the parent task's `verdict:` frontmatter line, (b) locate the parent's locked empirical data tables (typically §2.x in the parent's analysis memo), (c) cross-walk EVERY pre-registered direction in the new test against the parent's recorded values, (d) flag any (a)-(c) violations.

2. If a violation is found, classical-scholar files an `audit-blocker` memo at `findings/phase-b-hypotheses/<finding>-classical-audit.md` documenting (i) the defect class, (ii) the relevant parent data, (iii) re-routing options, and surfaces to team-lead via SendMessage.

3. The re-prereg is HELD until team-lead rules.

**Two-instance promotion threshold satisfied.** Per the standing 2-instance rule for MW-tier promotions, MW-8 is promoted to a permanent standing rule effective immediately.

**Cross-references:**

- Task #36 audit chain: `findings/phase-b-hypotheses/h-new-11-ext-reprereg.md` §"SECOND PRE-FALSIFICATION DETECTED — DO NOT DISPATCH"
- Task #33 audit chain: `findings/phase-b-hypotheses/h-new-4-ext-classical-audit.md`
- Parent task #6 finding file: `findings/phase-b-hypotheses/team-discovery-004.md`
- Parent task #18 finding file: `findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md`

**Interaction with existing rules:**

- **MW-2 (origin-qualifier discipline)** still applies. MW-8 is upstream of MW-2: it operates at the pre-prereg-locking stage, before MW-2 origin-qualifier review.
- **MW-6 (verbatim citation tier)** is orthogonal. MW-8 audits parent-task DATA coherence; MW-6 audits classical-source CITATION coherence. Both must be satisfied independently.
- **AMEND-28 (mechanical nawʿ-range scan)** is a sibling pattern — both MW-8 and AMEND-28 are pre-execution mechanical/quasi-mechanical gates that take human recall out of the critical path at points where it has historically failed.
- **PRE-REG-STANDARD-04** (no sign-flips post-hoc) interacts with MW-8(b): if MW-8(b) catches a pre-falsified direction, the response is NOT to sign-flip (PRE-REG-STANDARD-04 prohibits this) but to drop, reframe, or scale-shift the test.

**Pre-approved by:** team-lead 2026-04-13, ruling on the Task #33 + Task #36 audit-blocker pattern: *"Two AUDIT-BLOCKERS in one classical-scholar cycle catching pre-reg defects BEFORE compute waste. This pattern deserves promotion to MW-8 — Classical-side parent-task data-coherence gate. ... Two instances is sufficient for promotion under the standard 2-instance threshold."*

**Source:** classical-scholar audit memos for tasks #33 and #36, filed 2026-04-13. Both memos cross-reference this MW-8 entry as the standing rule under which they were filed.

## MW-9 — HALTED-SECOND-PRE-FALSIFICATION routing protocol (standing rule, 2026-04-13)

**Trigger:** Task #36 H-NEW-11-EXT round-2 pre-execution audit caught a *second* pre-falsification after round-1 had already caught and dropped the Lūṭ counter-prediction. The round-1 audit focused on the tertiary sub-test where the defect was visible; the PRIMARY pre-registered directions were left unchecked and subsequently failed at round-2 against the same parent-task #18 §2.4 locked 5-prophet |z| ranking. Yūsuf was pre-registered at rank 1 but sits at rank 5 in the data; Nūḥ was pre-registered in the bottom-2 but sits at rank 2 in the top. Binary 1 maximally inverted, Binary 2 partially falsified, joint k=2 test definitionally falsified before any compute.

**Defect class:** "first-audit-round-narrow-scope" — when a first-round audit catches a defect in one sub-test and the re-prereg is repaired locally (e.g., "drop the tertiary counter-prediction"), the repaired re-prereg may still contain pre-falsified PRIMARY directions that were never cross-walked against parent data. The repair is cosmetic; the underlying pattern (parent data determining the test) is still operative.

**The standing rule (MW-9):**

> When an audit round catches a pre-falsification in any sub-test of a re-pre-registration, the classical-scholar (or whoever drafts the repair) MUST extend the pre-execution check to cover EVERY pre-registered direction in the repaired re-prereg — primary, secondary, and tertiary — not only the sub-test that triggered the catch. A locally-repaired sub-test does not license dispatch; the FULL direction inventory of the repaired re-prereg must be cross-walked against parent data before the repaired re-prereg can be dispatched to computational-tester.
>
> If a second round catches a further pre-falsification, the re-prereg enters HALTED-SECOND-PRE-FALSIFICATION state. In this state:
>
> (a) **Sign-flip is prohibited** (per PRE-REG-STANDARD-04). The repaired re-prereg cannot be re-repaired by flipping the sign of the pre-falsified direction.
>
> (b) **Metric-switch must clear a forking-paths gate.** Any proposal to switch the operationalization (e.g., Spearman-on-ranks → HHI-on-mass) must be audited for whether the new metric's result is still determined by parent data. If it is, metric-switch is blocked as forking-paths-adjacent.
>
> (c) **Scale-shift must be independently motivated.** Any proposal to move to a different scale (e.g., per-prophet → per-pericope-substring) requires a fresh classical-source anchor that independently predicts the new-scale direction; scale-shifts cannot be back-derived from the pre-falsified finding.
>
> (d) **Drop is the protocol-clean default.** Absent a successful metric-switch or scale-shift that clears (b)-(c), the correct move is to drop the re-prereg as METHODOLOGICAL-NULL. The methodological-null verdict is itself publishable and documents the discipline working as intended.
>
> Only team-lead rules on which of (a)-(d) applies, and MW-9 requires the classical-scholar to surface the full option set (A2 sign-flip RULED-OUT / B2 metric-switch / C2 drop / D2 scale-shift) explicitly in the escalation message.

**Why the rule needs to exist:**

MW-8 established the pre-execution parent-data coherence gate. But MW-8 alone does not specify what happens when a first-round catch is followed by a second-round catch. Without MW-9, the natural response to a second catch is ad-hoc (sometimes sign-flip, sometimes metric-switch, sometimes drop) and the decision is made under time pressure without a standing protocol. MW-9 pre-commits the protocol: sign-flip is prohibited, metric-switch must clear a forking-paths gate, scale-shift must be independently motivated, drop is the default. This preserves pre-reg integrity under iterated audit failure and prevents the team from rescuing a structurally-determined test through cosmetic repair.

**Operational implementation:**

1. When a first-round audit catches a pre-falsification, classical-scholar's repair workflow MUST include a full second-round cross-walk of EVERY pre-registered direction against parent data, not only the sub-test that triggered the catch. This is the MW-9 "full-direction empirical check."

2. If the second-round cross-walk surfaces a further pre-falsification, classical-scholar files a HALTED-SECOND-PRE-FALSIFICATION memo at `findings/phase-b-hypotheses/<finding>-halted.md` or appended to the audit-blocker memo. The memo must list the four options (A2/B2/C2/D2) explicitly with a ruling on each from the classical-scholar lane's perspective, and surface to team-lead via SendMessage.

3. Team-lead rules on A2/B2/C2/D2. If C2 (drop) is approved, classical-scholar files a METHODOLOGICAL-NULL verdict memo (template: the H-NEW-11-EXT file at `findings/phase-b-hypotheses/h-new-11-ext-methodological-null.md`) with the full pre-falsification chain documented.

4. The methodological-null verdict is filed to MASTER §3 refutations bin as a first-class publishable entry, not as a buried footnote. "Methodological-null is a publishable verdict" — the MW-9 filing IS the finding.

**Two-instance promotion threshold:**

Strictly speaking, MW-9 is promoted on a single instance (Task #36 round-2 catch). But the promotion is justified because:

(a) The first-round catch (Lūṭ counter-prediction) already exercised the same defect class at the sub-test scope. The round-1 and round-2 catches are two instances of the same defect class in the same parent-task-downstream pattern, separated only by whether the audit checked the primary or the tertiary sub-test.

(b) The alternative to promoting MW-9 is to wait for a second whole task to exhibit the pattern, during which the team could expend compute or integrity-credit on an ad-hoc decision. The cost of not promoting is higher than the cost of single-instance promotion for this specific protocol.

(c) MW-9 is strictly more defensive than the pre-MW-9 default. No workflow cost is incurred by teams that never trigger a second-round catch.

**Cross-references:**

- Task #36 pre-falsification halt memo: `findings/phase-b-hypotheses/h-new-11-ext-reprereg.md` §"SECOND PRE-FALSIFICATION DETECTED — DO NOT DISPATCH"
- Task #36 methodological-null verdict: `findings/phase-b-hypotheses/h-new-11-ext-methodological-null.md`
- Parent task #18 locked data: `findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md` §2.4

**Interaction with existing rules:**

- **MW-8** is the upstream gate (catches pre-reg defects at round-1). MW-9 is the downstream protocol (specifies what to do after round-1 catch if a round-2 catch follows). MW-8 and MW-9 are sibling gates at different audit rounds.
- **PRE-REG-STANDARD-04** (no sign-flips post-hoc) is a direct input to MW-9(a) — sign-flip is ruled out at the HALTED state because of PRE-REG-STANDARD-04, not as an independent MW-9 decision.
- **MW-6** (verbatim citation tier) is orthogonal — MW-9 operates at the pre-registered-direction level, not the citation level.

**Pre-approved by:** team-lead 2026-04-13, ruling on Task #36 round-2 HALTED state: *"Option C2 is the protocol-clean move. The original H-NEW-11 hypothesis was already executed and PASSED at z=−2.35 / pan-prophetic confirmation in team-discovery-007. The H-NEW-11-EXT extension was an attempt to add a per-prophet ordering test on top of that, but the parent data already determines that ordering. There's nothing left to test that the parent didn't already answer."* Subsequent team-lead message: *"C2 is chosen FOR the MW-8 precedent, not despite it. A team that drops a pre-falsified test cleanly is stronger than a team that rescues it through metric-switching."*

**Source:** classical-scholar audit memos for task #36 rounds 1 and 2, filed 2026-04-13. Companion to MW-8.

## MW-10 — Pre-execution metric-defect self-test gate (standing rule, 2026-04-13)

**Trigger:** Task #33 H-NEW-4-EXT-D pipeline delivery (arabic-specialist, 2026-04-13). The letter-multiset KL-divergence pipeline was built and a pre-execution descriptive self-test was run on the pre-registered data. The descriptive full-body Δ (KL_muqaṭṭaʿāt − KL_baseline) came out at **+0.2077** — positive, i.e. opposite the pre-registered direction Δ<0. Classical-scholar verified empirically that this is NOT a real empirical signal but a **support-size confound in the KL metric**: stratified by |M_open|, mean KL monotonically drops 1.76 → 1.71 → 0.91 → 0.72 as the muqaṭṭaʿāt opener support grows from k=1 to k=4, with the baseline (first-4-letter faux-opener) having uniform support ≈4 and therefore not suffering the same k-dependent squeeze. Early-body windowing (0.0, 0.2) does NOT rescue the pattern. The defect is geometric: D_KL(M_body ‖ M_open) with a uniform-on-support M_open penalizes every body letter not in the opener, blowing up on k=1/k=2 openers whose reference distribution is near-degenerate.

**Defect class:** "pre-execution metric defect caught via self-test" — the pipeline is built and runs correctly, but the primary statistic has a mechanical or geometric artifact that makes the descriptive output misleading. The artifact is **not empirical** (not about what the data says) but **mechanical** (about how the stat is computed). A wrong-direction descriptive is therefore NOT a REVERSE verdict; it is a metric-defect flag that precedes the primary run.

**The standing rule (MW-10):**

> Every new test pipeline MUST include a pre-execution self-test descriptive run (not a verdict run) that reports the primary statistic on the pre-registered data plus a sanity-check diagnostic (stratification by a nuisance variable, comparison to alternative metrics, confound-direction check, or equivalent). The self-test descriptive is NOT a primary test; its purpose is to surface metric defects before compute is expended on a defective statistic.
>
> If the self-test descriptive flags a metric defect, the pipeline enters PRE-EXECUTION-METRIC-DEFECT state. In this state:
>
> (a) **HALT the primary run.** Compute on the defective statistic MUST NOT be expended before a corrected metric is approved. The descriptive self-test result MUST NOT be interpreted as a verdict; it is a confound-contaminated ghost signal.
>
> (b) **Classify the defect as mechanical, not empirical.** MW-10 applies ONLY when the defect is mechanical/geometric (support-size artifact, degenerate-reference blowup, dimensional normalization problem, etc.), not when the data tells the opposite story the pre-registration hypothesized. If the defect is "data contradicts pre-reg direction," that is a REVERSE or NULL verdict under the existing pre-reg, NOT an MW-10 correction. The classification must be explicit and defensible before any amendment is proposed.
>
> (c) **Surface confound analysis to team-lead.** The classical-scholar (or whoever owns the metric decision) files an escalation memo documenting (i) the descriptive self-test output, (ii) the stratified confound analysis with numerical evidence, (iii) the mechanism of the defect, (iv) the corrected-metric options with defensibility ordering, (v) an explicit classification note that the defect is NOT a sign-flip (PRE-REG-STANDARD-04 inapplicable) and NOT an MW-9 HALTED state (primary unrun, ghost contaminated).
>
> (d) **Team-lead ruling is required.** Metric correction requires explicit team-lead approval with the full confound analysis, the corrected-metric options surfaced, and the defensibility classification of each option. Classical-scholar does not self-authorize metric amendments.
>
> (e) **Honest trail in final write-up.** The original metric MUST be reported as sensitivity-0 alongside the corrected primary in the final result write-up, with the confound analysis included in the §Garden-of-Forking-Paths section. This prevents future re-introduction of the same defect and provides archaeological continuity for downstream reviewers.
>
> The MW-10 gate is epistemically distinct from MW-8 (post-execution first-audit catch) and MW-9 (halted-second-pre-falsification; empirical-direction-driven). MW-10 covers the case where the pipeline is ready but the chosen statistic is mechanically inappropriate for the data structure. It is a discipline pattern reusable for any future pipeline development.

**Why the rule needs to exist:**

Without MW-10, the natural response to a wrong-direction descriptive self-test is ambiguous: the team might (a) interpret it as a REVERSE verdict and file prematurely, (b) silently switch metrics under implicit forking-paths, or (c) proceed with the defective statistic and waste compute on a guaranteed artifact. All three are failure modes. MW-10 pre-commits the protocol: halt, classify, escalate, rule, honest-trail. The rule prevents the team from rescuing OR falsifying a pre-reg through an ambiguous self-test output; it forces the distinction between "the metric is wrong" (amendment, this gate) and "the hypothesis is wrong" (verdict, existing pre-reg discipline).

MW-10 is also the natural complement to MW-8 and MW-9, which catch pre-reg defects in the parent-data compatibility layer. MW-10 catches pre-reg defects in the pipeline-implementation layer — a different failure mode at a different stage, but analogous in that both are pre-execution gates designed to preserve pre-reg integrity.

**Operational implementation:**

1. When arabic-specialist (or whoever owns a pipeline delivery) completes pipeline construction, the delivery MUST include a self-test descriptive run with at least one sanity-check diagnostic. The delivery message to classical-scholar explicitly reports the descriptive output and flags any wrong-direction or anomalous results.

2. Classical-scholar classifies wrong-direction descriptive results as mechanical-defect OR empirical-failure. If mechanical-defect, MW-10 is invoked. If empirical-failure, the existing pre-reg runs and the verdict is filed as REVERSE or NULL under the locked pre-reg.

3. If MW-10 is invoked, classical-scholar files an escalation memo at `findings/phase-b-hypotheses/<finding>-metric-escalation.md` (or appended to the pre-reg audit memo) with the five required elements (descriptive output, stratified confound analysis, mechanism, corrected-metric options with ordering, classification note).

4. Team-lead rules on metric amendment. If approved, classical-scholar files an amended pre-reg with the corrected primary statistic, the original metric retained as sensitivity-0, the confound table in the §Garden-of-Forking-Paths section, and the amendment date + escalation date in the pre-reg header.

5. The amended pre-reg is dispatched to computational-tester via the standard dispatch path. The original pre-reg lock-date is preserved; only the primary statistic is amended, and the amendment is explicit and dated.

**Single-instance promotion threshold:**

MW-10 is promoted on a single instance (Task #33 H-NEW-4-EXT-D metric escalation 2026-04-13). Single-instance promotion is justified because:

(a) The class is **epistemically distinct** from MW-8 (post-execution) and MW-9 (pre-execution empirical-direction-driven). Subsuming MW-10 under either would be categorically wrong: MW-8 post-dates execution, MW-9 addresses empirical-direction pre-falsification, MW-10 addresses mechanical-metric pre-falsification. Each covers a different failure mode at a different stage.

(b) The alternative to promoting MW-10 is to wait for a second instance of the same defect class, during which time the team might expend compute or integrity-credit on an ad-hoc metric-amendment decision. The cost of not promoting is higher than the cost of single-instance promotion for this specific protocol class.

(c) MW-10 is **strictly more defensive** than the pre-MW-10 default. No workflow cost is incurred by teams whose pipelines do not exhibit mechanical metric defects; the self-test descriptive gate is lightweight (~15 min per pipeline) and reusable across future test families.

(d) The self-test descriptive discipline is a **reusable pattern** for all future pipeline development (letter-multiset, FOAI, root-palindrome, any divergence-based or ratio-based test family). Promoting now establishes the discipline before more pipelines are built on the same defect-prone metric class.

**Cross-references:**

- Task #33 metric escalation memo: escalation sent to team-lead 2026-04-13.
- Task #33 amended pre-reg (JS primary, KL sensitivity-0, stratified-KL sensitivity-1, Hellinger sensitivity-2): `findings/phase-b-hypotheses/h-new-4-ext-d-prereg.md` §"Primary Statistic" (amendment 2026-04-13).
- Sister pipeline with JS-divergence precedent: H-NEW-24 letter-multiset pipeline (arabic-specialist, tasks #44/#64/#65).
- Pipeline file: `scripts/letter_multiset.py`.

**Interaction with existing rules:**

- **MW-8 (parent-task data-coherence gate)** is orthogonal. MW-8 operates at the pre-reg drafting stage and audits parent-task DATA compatibility. MW-10 operates at the pipeline-delivery stage and audits pipeline STATISTIC compatibility. A pre-reg can pass MW-8 (parent data permits the test) but fail MW-10 (chosen statistic has a mechanical defect), as H-NEW-4-EXT-D demonstrates.
- **MW-9 (HALTED-second-pre-falsification)** is orthogonal. MW-9 addresses empirical-direction pre-falsification after parent data review. MW-10 addresses mechanical-metric pre-falsification after pipeline self-test. The two gates are mutually exclusive classifications: MW-9 means "data says opposite of pre-reg"; MW-10 means "statistic is wrong for the data structure regardless of what the data says."
- **PRE-REG-STANDARD-04 (no sign-flips post-hoc)** is explicitly NOT engaged by MW-10. MW-10 amendments preserve the pre-registered direction (Δ<0 stays Δ<0); only the metric changes. A sign-flip would be a separate violation and is ruled out independently of MW-10. The classification note in the escalation memo must explicitly state "this is not a sign-flip" to distinguish MW-10 from PRE-REG-STANDARD-04 violations.
- **AMEND-28 (mechanical nawʿ-range scan)** is a sibling pattern. Both MW-10 and AMEND-28 are pre-execution gates that take implicit assumptions out of the critical path at points where they have historically failed. AMEND-28 targets citation verification; MW-10 targets statistic mechanical validity.
- **MW-6 (verbatim citation tier)** is orthogonal. MW-6 audits classical-source citation coherence; MW-10 audits pipeline statistic coherence. Both must be satisfied independently.

**Pre-approved by:** team-lead 2026-04-13, ruling on H-NEW-4-EXT-D metric escalation: *"Promote MW-10 as a standing rule. Single-instance promotion justified by (a) strictly more defensive than not-flagging-it, (b) the class is epistemically distinct from MW-8/MW-9 so subsuming it under either would be wrong, (c) the self-test descriptive-only gate is a reusable discipline pattern for future pipeline development."* Team-lead also ruled on the three H-NEW-4-EXT-D amendments: JS-divergence primary APPROVED, 29-letter alphabet closure CONFIRMED, Hellinger distance as sensitivity-2 ADDED.

**Source:** classical-scholar escalation memo to team-lead 2026-04-13, grounded in arabic-specialist pipeline delivery (scripts/letter_multiset.py) and self-test descriptive output showing Δ = +0.2077 under KL. Companion to MW-8 and MW-9 as the third pre-execution discipline gate from the 2026-04-13 audit cycle.

