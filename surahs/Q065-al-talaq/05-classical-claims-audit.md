---
surah: 65
surah_name_ar: الطلاق
surah_name_translit: al-Ṭalāq
file_type: classical-claims-audit
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — 5 classical claims audited; 2 CONFIRMED, 1 RULES-TUPLE-FRAGILE, 1 NULL, 1 already-PROJECT-RETRACTED (sabʿ samāwāt = 7 occurrences)
---

# Q 65 al-Ṭalāq — Classical Claims Audit

This audit examines five classical claims about Q 65 (or about phrases/verses contained in Q 65) and adjudicates each against empirical-corpus data. Every claim's verdict is computed against the rules-tuple `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao, basmala-only-Q1, Hafs-Kūfan, Mashriqī)` unless otherwise noted.

## 1. CLAIM 1 (al-Biqāʿī's *Naẓm al-durar* tanāsub claim Q 64↔Q 65↔Q 66)

**Source claim**: al-Biqāʿī (d. 885/1480) in *Naẓm al-durar fī tanāsub al-āyāt wa-al-suwar* identifies Q 64 → Q 65 → Q 66 as a *tanāsub* sequence. The link Q 64 → Q 65 = *ʿāmm-piety → khāṣṣ-piety-applied-to-divorce*; the link Q 65 → Q 66 = *yā ayyuhā al-nabī continuous prophetic-domestic discourse*.

**Empirical test**: Compute H-NEW-720 canonical-adjacency cost for s=63 (Q 63 → Q 64), s=64 (Q 64 → Q 65), s=65 (Q 65 → Q 66), s=66 (Q 66 → Q 67). Lower cost = stronger geometric *tanāsub*.

**Computed result** (from `findings/phase-b-hypotheses/csv/h-new-720.json`):

| Seam | delta_raw | delta (clamped) | Cost rank /113 | Verdict |
|:--|:--:|:--:|:--:|:--|
| Q 63 → Q 64 (s=63) | 0.1435 | 0.1435 | rank 94 (top quintile EXPENSIVE) | UNUSUAL — high-cost seam |
| **Q 64 → Q 65** (s=64) | **−0.0087** | **0.0000** | **rank 5 (clamped-zero)** | **al-Biqāʿī CONFIRMED** |
| **Q 65 → Q 66** (s=65) | **−0.0340** | **0.0000** | **rank 6 (clamped-zero)** | **al-Biqāʿī CONFIRMED** |
| Q 66 → Q 67 (s=66) | 0.0780 | 0.0780 | rank 67 (mid-pack) | mid |

**Verdict**: **al-Biqāʿī's *tanāsub* claim Q 64→Q 65 + Q 65→Q 66 EMPIRICALLY CONFIRMED**. Both transitions register as CLAMPED-ZERO seams in H-NEW-720 — among the 13 lowest-cost mushaf transitions in the entire corpus (per H-NEW-1240). al-Biqāʿī's classical *tanāsub* claim is empirically vindicated at the geometric/structural level — the mushaf's Q 64→Q 65→Q 66 stretch is structurally seamless, supporting al-Biqāʿī's reading that the three surahs form a continuous discourse-block.

This is one of the **stronger classical-tanāsub vindications** in the project's audit (joins H-NEW-140 paired-divine-names cohesion at 13.87× as a confirmed classical-balāgha claim).

**Note**: the Q 63 → Q 64 transition is HIGH-cost (rank 94/113 = top-quintile expensive), so the *tanāsub* discontinuity is at the LEFT boundary of the Q 64-66 stretch — entering Q 64 al-Taghābun is structurally costly, but exiting it through Q 65 → Q 66 is structurally free. This places Q 64 al-Taghābun as a *register-pivot* surah: the mushaf compiler used Q 64's cosmological-warning content to BRIDGE between the heterogeneous post-musabbiḥāt cluster (Q 60-63) and the homogeneous *yā ayyuhā al-nabī* legal-domestic dyad Q 65-66.

## 2. CLAIM 2 (Ibn ʿUmar ṭalāq-during-ḥayḍ ↔ Q 65:1 *li-ʿiddatihinna* connection)

**Source claim**: Sunnī classical fiqh (al-Ṭabarī, Ibn Kathīr, al-Qurṭubī, al-Rāzī) treats the Bukhārī Ibn ʿUmar ṭalāq-during-ḥayḍ hadith as the canonical interpretive anchor for Q 65:1's *li-ʿiddatihinna* clause. The hadith is cited as the asbāb-al-nuzūl (occasion of revelation) by some classical sources, as a tafsīr-anchor by all.

**Empirical test**: This claim is HISTORICAL/HERMENEUTICAL, not strictly empirical-corpus-testable. The empirical question reduces to:
1. Is the hadith multi-chain (verifying its canonical-Sunnī acceptance)? — testable.
2. Is the hadith content-aligned with Q 65:1's *li-ʿiddatihinna* phrase? — testable.

**Result**:
1. The hadith is multi-chain: 4+ chains in Bukhārī alone (#5042, 5043, 5044, 5049), 4+ chains in Muslim (#1471a/b/c/d per ʿAbd al-Bāqī), additional chains in Abū Dāwūd, al-Tirmidhī, al-Nasāʾī, Ibn Mājah (verified §1-3 of `04-hadith-corpus.md`). The hadith is therefore *mutawātir-by-meaning* (multi-tradition convergent on the same content).
2. The hadith content (ṭalāq during purity not preceded by intercourse + counted-as-one + waiting through cycle) is content-aligned with Q 65:1's *li-ʿiddatihinna* phrase as the procedural-timing rule.

**Verdict**: **CONFIRMED at the multi-chain hadith level + content-aligned with Q 65:1**. The classical Sunnī interpretive linkage Q 65:1 ↔ Bukhārī Ibn ʿUmar ṭalāq-during-ḥayḍ is robustly attested. **Not strictly empirical-corpus-testable beyond this.**

**Garden-of-forking-paths note**: the *historical* question (is this the actual asbāb-al-nuzūl, or was the hadith constructed/transmitted to align with the verse) is a question for *ʿulūm al-ḥadīth* + *asbāb al-nuzūl* literature; the project's empirical-decipherment scope does not adjudicate the historicity question.

## 3. CLAIM 3 (sabʿ samāwāt = exactly 7 occurrences in the Quran)

**Source claim**: classical folk-tradition (cited in al-Suyūṭī's *al-Itqān* and various tafsir works) holds that *sabʿ samāwāt* (seven heavens) appears exactly 7 times in the Quran.

**Empirical test**: search the corpus for the strict construction *sabʿ + samāwāt / samāʾ*.

**Result** (from H-NEW-119 + verified inline `00-overview.md` §10):

The strict reading *sabʿ + samāwāt / samāʾ* yields **EXACTLY 5 occurrences**:
1. Q 2:29 — *fa-sawwāhunna sabʿa samāwāt* (creation context)
2. Q 41:12 — *fa-qaḍāhunna sabʿa samāwātin fī yawmayn* (Hawamim-Fuṣṣilat creation cosmology)
3. **Q 65:12** — *Allāh alladhī khalaqa sabʿa samāwātin wa-min al-arḍi mithlahunn* (the corpus-EXACT 7+7 verse)
4. Q 67:3 — *alladhī khalaqa sabʿa samāwātin ṭibāqā* (al-Mulk creation)
5. Q 71:15 — *alam taraw kayfa khalaqa llāhu sabʿa samāwātin ṭibāqā* (Nūḥ creation)

The extended cosmic-synonym reading (with *sabʿ* + various sky-related words) yields 8 occurrences.

**Verdict**: **the "exactly 7" claim is FALSIFIED** — already retracted at H-NEW-119 (project-wide). The actual strict count is 5. The "7" tally is a folk-convergence (7-symbolism × the iconic *sabʿ samāwāt* phrase), NOT a textual fact.

**Q 65 specialist refinement**: while H-NEW-119 falsifies the *count-7* claim, **Q 65:12 is THE corpus-EXACT 7+7 (heavens + earths-mithlahunn) verse — a UNIQUE corpus-architectural feature**. The *count-7* tally is wrong, but the *7+7-symmetric-pairing* claim — that 7 heavens are paired with 7 earths in a single Quranic phrase — is uniquely localized to Q 65:12 and corpus-EXACT in that sense. The classical "7+7" cosmology hadith (Bukhārī #2452 / Muslim #1610 *qīd shibr min al-arḍ → sabʿi araḍīn*) is the Sunna-side validator of this Q 65:12-localized 7+7 claim.

**This is a PROJECT-LEVEL project-relevant nuance**: the H-NEW-119 *count-7* falsification did NOT examine the *symmetric-7+7* corpus-EXACT phrasing at Q 65:12. This audit confirms that even though the count-7 claim is FALSIFIED, the symmetric-7+7-architectural claim (LOCATED EXCLUSIVELY at Q 65:12) is corpus-EXACT.

## 4. CLAIM 4 (Q 65 alif-monorhyme classification)

**Source claim**: al-Suyūṭī's *al-Itqān* (and various subsequent classical works) classify Q 65 al-Ṭalāq as an alif-monorhyme surah (*qaṣīda*-style alif-rāwī uniformity).

**Empirical test**: compute the final-letter distribution for Q 65 under both grapheme conventions (strict-grapheme and phonetic-pause).

**Result** (verified inline `00-overview.md` §10 and `01-empirical-profile.md` §6):

| Convention | Q 65 alif-final % | Verdict |
|:--|:--:|:--|
| Strict-grapheme (alif ا only) | **91.7% (11/12)**; Q 65:6 ends in alif-maqṣūra ى (*ukhrā*) | ALMOST monorhyme — but technically rules-tuple-fragile under strict convention |
| Phonetic-pause (alif ا = alif-maqṣūra ى, both realize as long-ā at pause) | **100% (12/12)** | FULLY monorhyme under phonetic-pause convention |

**Verdict**: **CONFIRMED-PHONETIC, RULES-TUPLE-FRAGILE under strict-grapheme convention**. The classical claim that Q 65 is alif-monorhyme is correct under the phonetic-pause convention used by classical *qaṣīda* scholars (where ا and ى pause-realize identically as long-ā). Under the project's strict-grapheme convention (cf. H-NEW-750), Q 65 is 91.67% alif and is one of 8 surahs that are TRUE phonetic-monorhyme but not strict-grapheme-monorhyme. The full set under MASTER-FINDINGS-LEDGER §line 1985: **8 surahs achieve perfect 1.0000 alif-final under phonetic-pause** = Q 18, Q 48, Q 65, Q 72, Q 76, Q 87, Q 91, Q 92; under strict-grapheme convention only 4 are (Q 48, 72, 76, 91).

**Substantive note**: the strict-grapheme defect at Q 65:6 is *ukhrā* (a fem. ordinal "another"). The fem-ordinal morphology is alif-maqṣūra-final by Arabic morphological rule; this is therefore NOT a rhyme-defect in the *qaṣīda*-style classical reading but a strict-grapheme-counting artifact. The classical claim is empirically robust under any convention that respects the morphological-equivalence of alif/alif-maqṣūra at pause.

## 5. CLAIM 5 (3-surah ṭalāq-legislation cluster {Q 2, Q 33, Q 65} cohesion)

**Source claim**: classical fiqh treatises (al-Jaṣṣāṣ, al-Sarakhsī, Ibn Qudāma) treat ṭalāq legislation as distributed across 3 surah-loci: Q 2:226-242 (the longest Quranic ṭalāq-block), Q 33:49 (single-verse rule on ṭalāq before consummation), and Q 65 (the only fully-dedicated ṭalāq surah). This implies a thematic-3-surah cluster.

**Empirical test**: compute Fisher-Rao cohesion of the 3-surah cluster {Q 2, Q 33, Q 65} at the WHOLE-SURAH aggregate level vs corpus pairwise mean.

**Result** (verified inline `00-overview.md` §5 and `01-empirical-profile.md`):

| Pair | FR-distance | corpus pairwise context |
|:--|:--:|:--|
| Q 2 ↔ Q 33 | 0.8829 | top-quartile FR-close |
| Q 2 ↔ Q 65 | 1.0062 | above corpus mean |
| Q 33 ↔ Q 65 | 1.0065 | above corpus mean |
| **3-cluster mean** | **0.9652** | corpus pairwise mean = 0.9235 |

The 3-cluster mean (0.9652) is **WORSE than corpus pairwise mean** (0.9235) — i.e. the 3-surah cluster is NOT FR-cohesive at the whole-surah level.

**Verdict**: **NULL at the WHOLE-SURAH level**. The classical 3-surah ṭalāq-legislation cluster is NOT geometrically-cohesive at the surah-aggregate Fisher-Rao level. The cluster lives at the *per-verse* level (the 17 verses of Q 2:226-242 + Q 33:49 + the 12 verses of Q 65 form a thematically-tight legal unit) but does NOT translate to whole-surah cohesion because Q 2 (286 verses) and Q 33 (73 verses) are far longer surahs whose themes range vastly beyond ṭalāq.

**This is consistent with the project's earlier finding** (Q033-F-05): "wives-cluster" (Q 33:28-34) ranks 4 of 5 Medinan-legal clusters tested; Q 4:11-14 inheritance is most cohesive. The classical *asbāb-al-nuzūl-thematic* clustering operates at the verse-block level, NOT at the whole-surah Fisher-Rao level. **This is a project-level architectural truth, not a Q 65-specific claim.**

**Substantive note**: this NULL is a methodologically-instructive result. It shows that classical *thematic* clusters (ṭalāq, inheritance, etc.) are LOCALLY-tight (verse-block level) but DO NOT propagate to the whole-surah Fisher-Rao-cohesive level when the surahs containing them are LARGE and multi-thematic. The 3-cluster {Q 2, Q 33, Q 65} is one such case.

## 6. Summary

| Claim | Source | Verdict | Comment |
|:--|:--|:--|:--|
| 1. al-Biqāʿī Q 64→65→66 *tanāsub* | *Naẓm al-durar* | **CONFIRMED** | Both seams clamped-zero (rank 5/6 of 113) — among H-NEW-1240's 13-seam set |
| 2. Ibn ʿUmar ↔ Q 65:1 hadith-anchor | Bukhārī, Muslim | **CONFIRMED-MULTI-CHAIN** | mutawātir-by-meaning |
| 3. *sabʿ samāwāt* = exactly 7 occurrences | classical folk-tradition | **PROJECT-FALSIFIED** (H-NEW-119); but Q 65:12 retains UNIQUE 7+7 corpus-EXACT pairing | Specialist refinement: count is 5, but symmetric-7+7 is corpus-EXACT at Q 65:12 |
| 4. Q 65 alif-monorhyme classification | al-Suyūṭī *Itqān* | **CONFIRMED-PHONETIC, RULES-TUPLE-FRAGILE under strict-grapheme** | Q 65:6 ends in alif-maqṣūra ى (*ukhrā*) |
| 5. 3-surah ṭalāq-legislation cluster {Q 2, Q 33, Q 65} cohesion | classical fiqh | **NULL at whole-surah FR level** | Cluster lives at verse-level only |

**Net audit**: 2 CONFIRMED, 1 PROJECT-FALSIFIED-with-specialist-refinement, 1 RULES-TUPLE-FRAGILE-but-classically-robust, 1 NULL. The 2 CONFIRMED + 1 specialist refinement at Q 65:12 are net positives for the classical-tradition's reading of Q 65; the 2 nuanced verdicts (4 + 5) are methodologically-instructive on rules-tuple sensitivity and verse-vs-surah aggregation.

## 7. Cross-references

- **H-NEW-1240 13-seamless-mushaf-transitions**: Q 65 sits at 2 of the 13 seams (s=64, s=65). See `07-cross-references.md` §3 for the full set.
- **H-NEW-1080 short-Medinan-block (Q 57-66) FR-cohesion**: Q 65 is a member; its *intra-block* mean (0.8479) is rank 9/10 = peripheral within the block.
- **H-NEW-119 sabʿ-samāwāt = 7 occurrences refutation**: this audit refines H-NEW-119 with the Q 65:12-localized 7+7-symmetric-pairing observation as a corpus-EXACT specialist finding.
- **H-NEW-140 paired-divine-names cohesion (13.87×)**: the al-Biqāʿī *tanāsub* CONFIRMATION at Q 64→65→66 joins H-NEW-140 as a 2-claim subset of confirmed classical-balāgha vindications.

---

*Specialist: Waiel Al-Shujaa, 2026-05-09. All numerical computations verified against `findings/phase-b-hypotheses/csv/` artifacts.*
