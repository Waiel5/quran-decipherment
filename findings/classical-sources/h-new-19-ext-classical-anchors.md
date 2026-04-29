---
finding_id: h-new-19-ext-classical-anchors
phase: B
status: classical-leg-DELIVERED — dispatching to computational-tester
date: 2026-04-13
task_ref: #41 H-NEW-19-EXT
parent_task: #27 H-NEW-19 v1 (team-discovery-011.md, CONFIRMED)
parent_catalog: #67 Ibn Abī l-Iṣbaʿ taṣdīr catalog (ibn-abi-l-isba-tasdir-catalog.tsv, 134 entries)
owner: classical-scholar
rules_tuple: (no-tashkeel, lemma QAC v0.4, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
classical_sources:
  - al-Suyūṭī al-Itqān fī ʿUlūm al-Qurʾān, Shamela0011728 ed., nawʿ 65 (al-ʿulūm al-mustanbaṭa)
  - Ibn Abī l-Iṣbaʿ al-Miṣrī Badīʿ al-Qurʾān (Sharaf 1957 ed., physically inaccessible — secondary triangulation per #67 catalog)
  - al-Hāshimī Aḥmad, Jawāhir al-Balāgha (verbatim Ibn Abī l-Iṣbaʿ taṣdīr taxonomy preserved)
  - al-Jārim ʿAlī & Amīn Muṣṭafā, al-Balāgha al-Wāḍiḥa Cairo 1966 (taṣdīr/radd al-ʿajz pedagogical citation chain)
mw_tier: MW-3 secondary-triangulated for Ibn Abī l-Iṣbaʿ (no physical primary); MW-6 for al-Suyūṭī genre adjudications
---

# H-NEW-19-EXT — Classical anchors for expanded genre partition + taṣdīr-narrow retest

## Purpose

Task #41 H-NEW-19-EXT extends the parent task #27 H-NEW-19 v1 (CONFIRMED, 2-of-3 elision signals at Bonferroni-k3) in two directions:

1. **Sub-test (a)**: re-run the elision compression-density test on an EXPANDED 4-genre partition (eschatological 20, narrative 11, legal 12, hymn/doxology 6) per al-Suyūṭī al-Itqān nawʿ 65 adjudications.

2. **Sub-test (c)**: re-run the taṣdīr sub-test under Ibn Abī l-Iṣbaʿ's NARROW definition (verbal-lexical only, excluding semantic radd al-ʿajz).

Sub-test (b) is a sensitivity run on whether Q 55 al-Raḥmān is classified as primary-eschatological or primary-doxological.

## Classical anchor 1 — al-Suyūṭī Itqān nawʿ 65 expanded genre adjudications

### Source

al-Suyūṭī, al-Itqān fī ʿUlūm al-Qurʾān, Shamela0011728 ed. (4 vols), nawʿ 65 fī al-ʿulūm al-mustanbaṭa min al-qurʾān, vol. 4 pp. 36-58 (Suyūṭī's tafṣīl of which surahs are sūrat al-aḥkām, sūrat al-qiṣaṣ, sūrat al-tawḥīd, sūrat al-taḥdhīr/al-takhwīf, sūrat al-mawāʿiẓ, sūrat al-tasbīḥ).

al-Suyūṭī's nawʿ 65 contains a sub-discussion of which surahs are primarily characterized by which discursive function. He does not give an exhaustive partition; he gives example assignments. The expanded partition below is built by:
- Taking al-Suyūṭī's explicit assignments where present
- Triangulating against the standard tafsīr commentary tradition (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī) for surahs al-Suyūṭī does not explicitly assign
- Cross-checking against al-Zarkashī al-Burhān nawʿ 47 al-mūqiʿāt al-balāghiyya for genre fingerprints

### Expanded partition (classical-scholar's adjudications)

#### Eschatological (20 surahs)

Original H-NEW-19 v1 set (12): Q 56 al-Wāqiʿa, Q 69 al-Ḥāqqa, Q 70 al-Maʿārij, Q 73 al-Muzzammil, Q 74 al-Muddaththir, Q 78 al-Nabaʾ, Q 81 al-Takwīr, Q 82 al-Infiṭār, Q 83 al-Muṭaffifīn, Q 84 al-Inshiqāq, Q 99 al-Zalzala, Q 101 al-Qāriʿa.

Expansion (8 added):
- **Q 75 al-Qiyāma** — al-Suyūṭī's tasmiya alone makes the case; entire surah is resurrection-discourse.
- **Q 79 al-Nāziʿāt** — opening 5 oaths (the snatchers, the swimmers, the racers) all reference angelic eschatological agents per al-Ṭabarī Jāmiʿ al-Bayān 30:46-50; second half is the Pharaoh/Mūsā parable framing the Hour.
- **Q 80 ʿAbasa** (second half from v.33 onward) — al-Ṣākhkha eschatological description.
- **Q 89 al-Fajr** — apodosis after the dawn-oath is the eschatological warning at vv. 21-30. al-Zamakhsharī Kashshāf 4:744 reads the entire surah as eschatological framing for the dawn-oath.
- **Q 100 al-ʿĀdiyāt** — al-Rāzī Mafātīḥ 32:67 reads the closing 5 verses as the eschatological apodosis to the warhorse-oath; the surah is not military but eschatological.
- **Q 102 al-Takāthur** — entirely eschatological warning per all major tafāsīr.
- **Q 103 al-ʿAṣr** — eschatological loss-frame; per al-Shāfiʿī's famous saying, "if only this sūra had been revealed, it would have sufficed".
- **Q 55 al-Raḥmān** — PRIMARY eschatological (refrain *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* punctuates ascending eschatological description), SECONDARY doxology. **Sub-test (b) sensitivity**: also run with Q 55 in doxology/hymn bucket.

**Total eschatological: 20** (or 19 if Q 55 is moved to doxology in sub-test (b)).

#### Narrative (11 surahs)

Original H-NEW-19 v1 set (6): Q 7 al-Aʿrāf, Q 12 Yūsuf, Q 18 al-Kahf, Q 19 Maryam, Q 20 Ṭāhā, Q 26 al-Shuʿarāʾ.

Expansion (5 added):
- **Q 11 Hūd** — wholly prophet-narrative (Nūḥ, Hūd, Ṣāliḥ, Ibrāhīm, Lūṭ, Shuʿayb, Mūsā). al-Suyūṭī's nawʿ 65 explicitly cites Hūd as exemplar of *qaṣaṣ al-anbiyāʾ* density.
- **Q 14 Ibrāhīm** — surah named after the patriarch and dominated by his prayer-narrative (vv. 35-41).
- **Q 21 al-Anbiyāʾ** — surah literally titled "The Prophets" and surveys multiple prophet-narratives.
- **Q 27 al-Naml** — Sulaymān-narrative dominant (vv. 15-44), Ṣāliḥ and Lūṭ secondary.
- **Q 37 al-Ṣāffāt** — Nūḥ, Ibrāhīm + Ismāʿīl (sacrifice), Mūsā, Ilyās, Lūṭ, Yūnus successive narratives (vv. 75-148).

**Total narrative: 11.**

#### Legal (12 surahs)

Original H-NEW-19 v1 set (5): Q 2 al-Baqara, Q 4 al-Nisāʾ, Q 5 al-Māʾida, Q 24 al-Nūr, Q 65 al-Ṭalāq.

Expansion (7 added):
- **Q 8 al-Anfāl** — surah of war-spoils law, military-jurisprudence dominant.
- **Q 9 al-Tawba** — surah of treaty law, ḥajj-decree, jihād, war-tax (jizya).
- **Q 47 Muḥammad** — military-engagement law (vv. 4 *fa-iḍribū l-riqāb*), prisoner-policy.
- **Q 48 al-Fatḥ** — Ḥudaybiya treaty law, military oath of allegiance (bayʿat al-riḍwān).
- **Q 49 al-Ḥujurāt** — interpersonal social-conduct law (privacy, gossip, salutation, brotherhood).
- **Q 58 al-Mujādila** — ẓihār-divorce law in opening verses; munāfiqūn social law in closing.
- **Q 66 al-Taḥrīm** — Prophetic-household law, oath-dispensation law.
- al-Baqara retained as legal despite narrative interpolations (Bani Isrāʾīl, Hārūt/Mārūt) per al-Suyūṭī's *sūrat al-aḥkām* designation in nawʿ 65.

**Total legal: 12.**

#### Hymn/doxology (narrow, 6 surahs)

- **Q 1 al-Fātiḥa** — opening prayer-hymn, recited at every ṣalāt.
- **Q 17:1 only** (not full Q 17) — *subḥāna alladhī asrā* opening verse is doxological isrāʾ-hymn; rest of surah is mixed.
- **Q 87 al-Aʿlā** — *sabbiḥ isma rabbika* opening, hymn-frame.
- **Q 112 al-Ikhlāṣ** — pure tawḥīd doxology.
- **Q 113 al-Falaq** — protective hymn.
- **Q 114 al-Nās** — protective hymn.
- Q 55 al-Raḥmān **only** in sub-test (b) when assigned to doxology.

**Total doxology: 6** (or 7 with Q 55 reassignment).

### Summary table

| Genre | Original v1 N | Expanded N | New surahs added |
|---|---|---|---|
| Eschatological | 12 | 20 (or 19 in sub-test b) | Q 75, 79, 80(b), 89, 100, 102, 103, 55(*) |
| Narrative | 6 | 11 | Q 11, 14, 21, 27, 37 |
| Legal | 5 | 12 | Q 8, 9, 47, 48, 49, 58, 66 |
| Doxology | — (not partitioned in v1) | 6 (or 7 in sub-test b) | Q 1, 17:1, 87, 112, 113, 114, [Q 55 only in (b)] |

(*) Q 55 is the sensitivity hinge. Sub-test (b) runs both Q 55-eschatological (N=20 esch) and Q 55-doxology (N=19 esch + 7 dox) configurations.

### MW-tier flagging

- **al-Suyūṭī Itqān nawʿ 65 verbatim citations** confirming the partition: MW-6 (physically read in Shamela0011728 nawʿ 65 vol. 4 pp. 36-58 during my prior work on tasks #67 and #103, MW-6 backport-audited).
- **Genre-assignment adjudications for individual surahs**: MW-4 to MW-5 (classical-scholar inference from primary tafsīr cross-reference; not literal Itqān assignments since Itqān gives examples, not exhaustive partition). The adjudications are reproducible from the tafsīr literature but are not single-source verbatim quotations.
- **The expansion as a whole is a CLASSICAL-SCHOLAR'S WORKING PARTITION**, not a verbatim Suyūṭī quotation. Skeptical-auditor should flag this — the genre labels are interpretive even though they are well-grounded.

## Classical anchor 2 — Ibn Abī l-Iṣbaʿ NARROW taṣdīr definition

### Source

Ibn Abī l-Iṣbaʿ al-Miṣrī (d. 654/1256), Badīʿ al-Qurʾān fī ʿulūm al-balāgha wa-asrār al-iʿjāz, ed. Ḥifnī Muḥammad Sharaf, Cairo: Dār Nahḍat Miṣr 1957. **Primary edition not physically accessible**; classical-scholar working from MW-3 secondary triangulation per the citation chain documented in `findings/classical-sources/ibn-abi-l-isba-tasdir-catalog.tsv` lines 11-22.

### The narrow vs broad distinction

Ibn Abī l-Iṣbaʿ's taṣdīr concept has TWO operative definitions in the classical literature:

**BROAD definition (al-radd al-ʿajz ʿalā al-ṣadr, "returning the end onto the beginning"):**
Includes any echo between the opening and closing of a verse — lexical, root-level, derivative, semantic, or paronomastic. This is the definition operative in the pedagogical tradition (al-Jārim/Amīn al-Balāgha al-Wāḍiḥa, al-Hāshimī Jawāhir al-Balāgha) and is what the #67 catalog tracks across Classes 1-5 (134 entries total).

**NARROW definition (verbal-lexical taṣdīr only):**
Restricted to **same-root or same-lemma repetition** at verse-start and verse-end. This excludes:
- Class 4 (semantic / radd al-ʿajz proper) — same concept, different roots
- Class 5 (jinās) — same consonant skeleton, different meaning

Ibn Abī l-Iṣbaʿ's own Badīʿ al-Qurʾān, per the secondary tradition (al-Hāshimī Jawāhir al-Balāgha p. 358 in the standard edition; al-Subkī ʿArūs al-Afrāḥ in commentary on al-Qazwīnī's Talkhīṣ al-Miftāḥ), distinguishes:

> ومنه ما يكون لفظيًّا محضًا، وهو إعادة اللفظة بعينها أو من جنسها في صدر البيت وعجزه. وأقواه ما اتفق فيه اللفظان رسمًا ونطقًا واتحدا في المعنى. وأضعفه ما اشتركا في الحروف الأصول ولم يتفقا في المعنى — وهذا هو الجناس.

*"Among it [taṣdīr] is what is purely verbal-lexical, namely the repetition of the same word or one of its kind at the opening and closing of the verse. The strongest of it is what the two words agree on in script, pronunciation, and meaning. The weakest is what they share only in root letters but differ in meaning — and this is jinās."*

**This passage establishes the narrow scale**: STRONG narrow taṣdīr = same lemma; WEAK narrow taṣdīr = same root; jinās (Class 5) is explicitly demoted as "weakest" but still verbal-lexical; semantic-only (Class 4) is NOT narrow.

### Operationalization for sub-test (c)

From the #67 catalog (134 total entries):

| Class | Definition | N in #67 catalog | Included in NARROW set? |
|---|---|---|---|
| 1_lexical | Same lemma at verse-start and verse-end | 5 | YES (strong narrow) |
| 2_root | Same root, different lemma | 4 | YES (weak narrow) |
| 3_derivative | Related roots, morphological family | 0 | YES (per Ibn Abī l-Iṣbaʿ's verbal-lexical scale) but catalog has no entries |
| 4_semantic | Same concept, different root | 125 | **NO** (excluded under narrow) |
| 5_jinās | Same consonant skeleton, different meaning | 0 | YES per the citation above (verbal-lexical "weakest") but catalog has no entries |

**Narrow taṣdīr set from #67 catalog**: **9 entries** (Class 1: 5 + Class 2: 4).

This is a small N and represents the catalog's coverage gap. The narrow set is **not exhaustive** — it is the subset of the catalog's secondary-triangulated entries that are verbal-lexical. A computational scan for narrow taṣdīr (every verse where first-token-root == last-token-root, computed directly from QAC) would yield a much larger N (estimated ~250-400 verses based on QAC root-frequency). I recommend the computational pipeline use BOTH:

- **Catalog-narrow stratum** (N=9): the secondary-triangulated verbal-lexical entries from #67. Pre-registered, low power, high classical authority.
- **Computational-narrow stratum** (N=catalog-derived from QAC): every verse where the first content token's root equals the last content token's root (excluding particles). Pre-registered as a sensitivity stratum, higher power, lower classical authority.

### Mutual-exclusion logic (recap from #67)

The hapax-final slot theory (H-NEW-23) predicts that hapax words occupy the verse-final slot at elevated rate. The narrow-taṣdīr verses CANNOT have a hapax in the final slot, because the final word repeats (or shares root with) a word that already appeared at the opening — by definition, not a hapax for that verse. So narrow-taṣdīr verses and hapax-final verses are **mutually exclusive at the verse level** under Ibn Abī l-Iṣbaʿ's narrow definition.

The H-NEW-23 sub-4 surface-proxy retest (#67 catalog, broad-pooled) returned z = +1.52, directionally correct but Bonferroni-fail. The narrow stratum should produce a CLEANER signal because the broad pool is contaminated by Class 4 semantic taṣdīr where the final word may still happen to be a hapax (semantic relation does not preclude lexical novelty).

## Pre-registration deliverable for sub-test (c)

### Test specification

For each of the 6,236 verses, compute:
- `is_hapax_final`: Boolean. Does the verse-final content word appear ≤1 time across the corpus? (Drop particles; use QAC lemma counts.)
- `is_narrow_tasdir_catalog`: Boolean. Is the verse in the 9-entry catalog narrow stratum?
- `is_narrow_tasdir_computational`: Boolean. Does the first content-token root equal the last content-token root in the verse? (Drop particles, vocatives, and basmala.)

### Primary test (sub-c-1, catalog stratum)

Mutual-exclusion test on N=9 narrow taṣdīr verses:
- Observed: count of (is_narrow_tasdir_catalog == TRUE AND is_hapax_final == TRUE) verses
- Pre-registered prediction: 0 of 9
- Null model: hypergeometric draw — under the null that taṣdīr is independent of hapax-final placement, expected count = 9 × P(hapax_final). P(hapax_final) is the global rate; if it's ~5%, expected ≈ 0.45. Observing 0 is slightly under expectation but not significantly so at N=9.
- One-sided exact hypergeometric test, observed ≤ expected.
- α = 0.0167 (Bonferroni k=3 within H-NEW-19-EXT family).
- **Honest power note**: with N=9 and expected ~0.45, even a perfect 0-of-9 mutual exclusion gives only p ≈ 0.64. **Sub-c-1 cannot achieve significance at N=9.** It is registered as a directional-confirmation test only.

### Secondary test (sub-c-2, computational stratum)

Mutual-exclusion test on N≈250-400 computational narrow taṣdīr verses (exact N to be computed from QAC):
- Observed: count of (is_narrow_tasdir_computational == TRUE AND is_hapax_final == TRUE) verses
- Null model: length-stratified label permutation, 10,000 draws, seed 20260413
- α = 0.0167 (Bonferroni k=3 within H-NEW-19-EXT family)
- **Power**: at N=300 with global hapax-final rate ~5%, expected = 15. Observing 0-3 is significant (z ≈ −3.0 to −3.9). The computational stratum has the power that the catalog stratum lacks.

### Tertiary test (sub-c-3, narrow vs broad differential)

Test whether narrow taṣdīr's mutual-exclusion is STRONGER than broad taṣdīr's:
- Observed: rate(hapax_final | narrow_tasdir) vs rate(hapax_final | broad_tasdir_classes_1_2_4)
- Pre-registered prediction: rate(narrow) < rate(broad), one-sided
- Test: Fisher's exact, one-sided
- α = 0.0167
- **Discrimination logic**: if narrow-taṣdīr verses are MORE strictly hapax-excluded than broad-taṣdīr verses, this validates Ibn Abī l-Iṣbaʿ's narrow definition as the operative classical concept. If the rates are equal, broad and narrow definitions are interchangeable for this purpose.

## Pre-registration deliverable for sub-test (a) — expanded genre partition

### Test specification

Re-run H-NEW-19 v1's elision compression-density test (triple-proxy C_syn + C_lex + C_gzip) on the expanded 4-genre partition:

- Eschatological: N=20 surahs (or N=19 in sub-test b)
- Narrative: N=11 surahs
- Legal: N=12 surahs
- Doxology: N=6 surahs (or N=7 in sub-test b)

Total partitioned surahs: 49 (or 48 in sub-test b). Remaining 65 surahs unclassified — exclude from primary test; include in sensitivity ANOVA as an "unclassified" baseline bucket.

### Primary test (sub-a-1)

Mann-Whitney U one-sided: eschatological > legal on triple-proxy compression density C.
- α = 0.0167 (Bonferroni k=3)
- Pre-registered prediction: U significant in the same direction as v1.
- This is a higher-power replication of v1's finding with the larger N.

### Secondary test (sub-a-2)

4-way Kruskal-Wallis: eschatological vs narrative vs legal vs doxology on C.
- α = 0.0167
- Pre-registered prediction: K-W significant; pairwise post-hoc shows eschatological > legal AND eschatological > doxology.

### Tertiary test (sub-a-3)

Length-residualized regression: C ~ genre + log(surah_length) + Meccan_Medinan + position_in_canon
- α = 0.0167
- Pre-registered prediction: genre coefficient survives length and Meccan/Medinan controls.

### Confound controls
- Length residualization (already in v1)
- Meccan/Medinan classification (Nöldeke)
- Mean word length per surah
- Position-in-surah (within-surah verse position)
- Restricted length-band 10-25 tokens as additional sensitivity stratum

## Pre-registration deliverable for sub-test (b) — Q 55 al-Raḥmān assignment sensitivity

Run sub-test (a) twice:
- Configuration B1: Q 55 in eschatological (N_esch=20, N_dox=6)
- Configuration B2: Q 55 in doxology (N_esch=19, N_dox=7)

Report both effect sizes and significance. **If the primary signal flips on this single reassignment, the v1 finding is structurally fragile and must be downgraded.** This is a stress test of the classical genre adjudication, not a separate Bonferroni-counted test (the two configurations are alternative operationalizations of the same hypothesis).

## Bonferroni budget

Within H-NEW-19-EXT family:
- sub-a-1 primary Mann-Whitney
- sub-a-2 secondary Kruskal-Wallis
- sub-a-3 tertiary regression
- sub-b alt-configuration sensitivity (NOT Bonferroni-counted; reported as fragility check)
- sub-c-1 catalog narrow taṣdīr (registered as directional only, N=9)
- sub-c-2 computational narrow taṣdīr (primary power)
- sub-c-3 narrow-vs-broad differential

**Total k=6 within-hypothesis (sub-a × 3 + sub-c × 3)**, α_bon = 0.05/6 = 0.0083 per test. Outside Tomorrow Tests Bonferroni family.

(Task #41 description specifies k=3; on closer reading I think the correct k is 6 because sub-c was in the original task listing as 1 sub-test but I'm splitting it into 3 sub-cases. Computational-tester or hypothesis-generator: please confirm or revert k to 3 if you want sub-c collapsed to a single test on the union stratum.)

## Seed
20260413 (universal task seed)

## Rules tuple
(no-tashkeel, lemma QAC v0.4, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)

## Output expected
- `findings/phase-b-hypotheses/h-new-19-ext-results.md` — computational-tester
- `findings/phase-b-hypotheses/csv/h-new-19-ext.json` — raw output
- `scripts/h_new_19_ext_expanded_genre_tasdir_narrow.py` — pipeline

## MW-tier disclosure (skeptical-auditor must read)

- **Genre partition (sub-a)**: classical-scholar's interpretive aggregation from al-Suyūṭī Itqān nawʿ 65 + tafsīr cross-reference. NOT a verbatim Suyūṭī quotation. MW-4 to MW-5 reliability tier.
- **Narrow taṣdīr definition (sub-c)**: classical citation chain via secondary balāgha sources (al-Hāshimī Jawāhir al-Balāgha p. 358; al-Subkī ʿArūs al-Afrāḥ; al-Jārim/Amīn al-Balāgha al-Wāḍiḥa). NOT a physical reading of Sharaf 1957 Badīʿ al-Qurʾān. MW-3 reliability tier.
- **Catalog narrow stratum N=9**: subset of the #67 catalog, which is itself secondary-triangulated. Power-limited; cannot achieve significance. Registered as directional confirmation only.
- **Computational narrow stratum**: primary-source-of-power for sub-c. Operationalization (first content root == last content root) is faithful to Ibn Abī l-Iṣbaʿ's narrow definition AS PRESERVED IN THE SECONDARY CHAIN. If the Sharaf 1957 edition is later accessed and the narrow definition turns out to be different (e.g., requires same lemma, not same root), the computational stratum will need re-running.

The sub-a expanded partition is internally well-grounded in al-Suyūṭī nawʿ 65 + tafsīr; the sub-c narrow definition is more reliant on the secondary chain. Both are publishable with the MW-tier disclosure.

## Related findings
- Parent: #27 H-NEW-19 v1 (CONFIRMED, 2-of-3 elision signals)
- Sibling: #41 H-NEW-19-EXT (this task, classical-scholar dispatch)
- Catalog: #67 Ibn Abī l-Iṣbaʿ taṣdīr catalog (134 entries, 9 narrow + 125 broad-semantic)
- Downstream of H-NEW-23 sub-4: see hapax-slot-mechanism.md
