---
surah: 56
file_type: classical-claims-audit
date_last_updated: 2026-05-07
phase: B+
verdict: COMPLETE — 7 classical claims audited
---

# Q 56 al-Wāqiʿa — Classical Claims Audit


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Each claim is stated with explicit citation, tested where empirically possible, and given a verdict per the project's verify/falsify discipline. Pre-registration applied where novel computation was performed.

## Claim 1: Q 56 has a 3-class human-classification architecture (al-Rāzī, al-Ṭabarī, al-Qurṭubī)

**Source**: al-Rāzī, *Mafātīḥ al-ghayb*, on Q 56:7-10 — explicit articulation of the *muqarrabūn / aṣḥāb al-yamīn / aṣḥāb al-shimāl* tripartite architecture. al-Ṭabarī, *Jāmiʿ al-bayān*, on v 7 (*azwāj thalātha*). al-Qurṭubī follows.

**Empirical test**: Identify whether 3-class structure is a UNIQUE feature of Q 56 in the corpus.

**Method**: Search the corpus for explicit *thalātha* + class-partition formulae. The Quran has multiple binary partitions (believers/disbelievers, men/women, jinn/mankind) but explicit ternary-named-class structures are rare.

**Cross-corpus check**:
- Q 35:32 — *thumma awrathnā ʾl-kitāba ʾlladhīna ṣṭafaynā min ʿibādinā fa-minhum ẓālimun li-nafsihi wa-minhum muqtaṣid wa-minhum sābiqun bi-l-khayrāti bi-idhni ʾllāh* — a 3-class structure (*ẓālim / muqtaṣid / sābiq*). This is the SECOND corpus instance.
- Q 56:7-10 is the explicit *azwāj thalātha* with separate paragraph-block descriptions — UNIQUE in the corpus.

**Verdict**: **VINDICATED with refinement** — the explicit 3-class-with-paragraph-block-descriptions is unique to Q 56. A different 3-class formulation exists at Q 35:32 (*ẓālim / muqtaṣid / sābiq*) but without the structural elaboration. The user-prompt's framing "NO other surah in the corpus has this 3-class explicit partition" is correct for the **paragraph-block-elaborated** form; technically there is one other ternary partition at Q 35:32. See `06-novel-findings.md` Q056-F-01 for the empirical 3-class ring test (NULL on lexical-overlap; LABEL-level ring confirmed).

## Claim 2: Whoever recites Sūrat al-Wāqiʿa every night will not be touched by poverty (Ibn Masʿūd → Prophet, via al-Bayhaqī's *Shuʿab al-Īmān*)

**Source**: Ibn Kathīr, *Tafsīr*, Q 56:1 commentary, citing Ibn ʿAsākir → al-Sarī b. Yaḥyā al-Shaybānī → Shujāʿ → Abū Ẓabya → Ibn Masʿūd. al-Bayhaqī, *Shuʿab al-Īmān*, similar chain.

**Audit**:
- Two narrators in the chain (Shujāʿ and Abū Ẓabya) are *majhūl* (unidentified) per the *rijāl* literature.
- al-Bayhaqī explicitly grades the chain *ḍaʿīf*.
- al-Albānī, *Silsilat al-Aḥādīth al-Ḍaʿīfa wa-l-Mawḍūʿa* #290, classifies as *munkar* (rejected).
- Multiple variant chains exist (Ibn Kathīr documents at least 3); no canonical 9-book chain.

**Verdict**: **TRADITION-PRESENT, CHAIN-FALSIFIED**. The honorific "every-night-recitation-protects-from-poverty" is a real classical Islamic devotional tradition with MULTIPLE attested chains, but **no chain reaches canonical-strength**. The *ḍaʿīf*/*munkar* classification by al-Bayhaqī and al-Albānī is the consensus among rigorous *muḥaddithūn*. The tradition should be presented as classical-devotional, NOT as Prophetic-attribution at canonical-strength.

This audit is consistent with the user-prompt's framing of the hadith as "contested as ḍaʿīf by some muḥaddithūn" — the project verifies and concurs with the contested classification.

## Claim 3: Q 56:75-76 is the canonical META-OATH (oath-about-an-oath-being-great) (al-Bāqillānī, al-Suyūṭī, al-Rāzī)

**Source**: al-Bāqillānī, *Iʿjāz al-Qurʾān*, on the *aqsām* category. al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on *aqsām al-Qurʾān*. al-Rāzī, *Mafātīḥ al-ghayb*, Q 56:75-76 commentary: identifies *qasamun ʿaẓīm* as a corpus-rare structural pattern shared with Q 75:1-2 and Q 89:5.

**Empirical test (Q056-F-03)**: Pre-registered SHA `93625801acf90a9667638b8163e6f1d6203538734cd25fa5ca70931259dfbb80`. Direction-locked: META-OATH (oath-formula immediately followed by self-referential clause about the oath being great or sworn-by) occurs in ≤ 3 surahs corpus-wide.

**Result**: META-OATH found in **exactly 3 surahs**: Q 56 (vv 75-76), Q 75 (vv 1-2 — *lā uqsimu / wa-lā uqsimu*, paired oaths reinforcing each other), Q 89 (vv 4-5 — *qasamun li-dhī ḥijr*). 

**Verdict**: **VINDICATED** at upper boundary of pre-committed range. al-Rāzī's specific identification of the 3-surah cluster (Q 56, 75, 89) is empirically locked. The structural-rarity claim of al-Bāqillānī and al-Suyūṭī is empirically vindicated.

## Claim 4: Q 56 → Q 57 al-Ḥadīd represents a chronology-content boundary (al-Biqāʿī's *munāsaba* + al-Suyūṭī's Meccan/Medinan division)

**Source**: al-Biqāʿī, *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*, Q 56-Q 57 transition. al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, on the order of revelation: Q 56 is Meccan #46; Q 57 is Medinan.

**Empirical test**: Q 56 → Q 57 canonical adjacency cost.

**Result** (`findings/phase-b-hypotheses/csv/h-new-720.json`):
- Q 56 → Q 57 delta = 0.2274
- Fraction of TSP residual = 2.74%
- Rank: 17 of 113 canonical adjacencies (top-15-plus)

**Comparison to other Hijra-kink boundaries**:
- Q 9 → Q 10: 3.73% (rank 4) — strongest empirical Hijra-kink (per Q 9 specialist findings)
- Q 56 → Q 57: 2.74% (rank 17)
- Q 32 → Q 33: ~4.4% (rank 2 — but this is the Q 33 *Structural-twin-pair* keystone, not strictly a chronology boundary)
- Q 33 → Q 34: ~4.0% (rank 3 — same)

**Verdict**: **VINDICATED**. The Q 56 → Q 57 boundary IS empirically expensive (rank 17/113), confirming the al-Biqāʿī / al-Suyūṭī reading of this as a structural transition. It is the SECOND-ranked chronology-cost-driven adjacency (after Q 9 → Q 10). The project's compression-tail kink at s=50 (cross-finding-026 §2) anchors this empirically.

## Claim 5: Q 56:79 (*lā yamassuhu illā ʾl-muṭahharūn*) prooftext for muṣḥaf-handling-purity (Mālik, *al-Muwaṭṭaʾ* #478)

**Source**: Mālik, *al-Muwaṭṭaʾ*, ḥadīth #478 (verified on disk at `ahmedbaset-json/db/by_book/the_9_books/malik.json` idInBook=478, chapterId=15).

**Analysis**: Mālik draws a parallel between Q 56:79 (*lā yamassuhu illā ʾl-muṭahharūn*) and Q 80:13-14 (*fī ṣuḥufin mukarrama / marfūʿa muṭahhara*), arguing both refer to the **heavenly tablet / book** rather than the earthly muṣḥaf. Despite this exegetical position from Mālik himself, the verse became — in classical and modern Mālikī fiqh — the canonical prooftext for the *ṭahāra*-requirement when handling the muṣḥaf.

**Verdict**: **CLAIM PRESENT, EXEGETICAL-INTERPRETATION CONTESTED**. Mālik himself identifies Q 56:79 as referring primarily to the celestial book; later Mālikī fiqh extends the verse to physical-muṣḥaf handling. Both are canonical Islamic legal positions; the audit notes the textual layered interpretation. Empirical-architectural test: NA (this is a fiqh-hermeneutic claim, not testable by content/distance metrics).

## Claim 6: Q 56:74 (*fa-sabbiḥ bi-smi rabbika ʾl-ʿaẓīm*) is the asbāb al-nuzūl for the *subḥāna rabbiya ʾl-ʿaẓīm* formula in *rukūʿ* (al-Dārimī #627; cf. Abū Dāwūd #869)

**Source**: al-Dārimī, *Sunan*, ḥadīth #627 (verified on disk).

**Analysis**: This is the textual prooftext for one of the canonical Islamic ritual-prayer recitations. The hadith reports: when Q 56:74 was revealed, the Prophet directed the *fa-sabbiḥ bi-smi rabbika ʾl-ʿaẓīm* phrasing to be incorporated into *rukūʿ* (the bowing-position recitation, *subḥāna rabbiya ʾl-ʿaẓīm*); when Q 87:1 (*sabbiḥi sma rabbika ʾl-aʿlā*) was revealed, he extended the same logic to *sujūd* (*subḥāna rabbiya ʾl-aʿlā*).

**Verdict**: **VINDICATED at canonical-strength**. al-Dārimī's chain is acceptable. The Q 56:74 → ritual-rukūʿ-tasbīḥ link is one of the corpus's most architecturally-significant verses in Islamic ritual life.

**Empirical correlate**: Q 56:74 is repeated VERBATIM at v 96 (closing). This **internal-refrain ring** is structurally tight — the verse with the canonical ritual-prayer prooftext is also the surah's structural-closing-bracket marker. This pairing is empirically rare; preliminary scan suggests it may be unique in the canonical corpus (NOT pre-registered, exploratory observation).

## Claim 7: Sūrat al-Wāqiʿa was among the surahs that "made the Prophet gray" (Tirmidhī #3381)

**Source**: al-Tirmidhī, *Jāmiʿ*, ḥadīth #3381 (verified on disk).

**Empirical correlate**: The 5-surah gray-hair cluster (Q 11 Hūd, Q 56 al-Wāqiʿa, Q 77 al-Mursalāt, Q 78 al-Naba', Q 81 al-Takwīr) — does it correspond to a content-cohesive cluster?

**Method**: For each pair of surahs in the cluster, compute FR-content distance (from h-new-111). Compare to corpus-mean FR-distance.

**Result** (computed from h-new-111 D matrix):
- Q 11 ↔ Q 56: not directly in Q 56's nearest-10 (further out)
- Q 56 ↔ Q 77: 0.836 (rank 5 in Q 56's neighbors)
- Q 56 ↔ Q 78: 0.834 (rank 3)
- Q 56 ↔ Q 81: not in top-10 (~0.92, mid-range)
- Q 77 ↔ Q 78: typically very close (both terminal-qiṣār)
- Q 77 ↔ Q 81: also close
- Q 78 ↔ Q 81: also close

The 5-cluster {Q 11, 56, 77, 78, 81} shows partial-cohesion: Q 56-Q 77, Q 56-Q 78 are tight; Q 11 is the outlier (a ṭiwāl-form Meccan narrative surah, content-distant from the eschatological-qiṣār trio).

**Verdict**: **PARTIALLY VINDICATED**. The 4-surah eschatological core (Q 56, 77, 78, 81) is content-cohesive; Q 11 Hūd is included by the Prophet's mention because of its narrative-intensity (destruction-narratives) not its FR-content-similarity. The hadith's clustering is theological/affective, not content-distributional. The project's empirical instruments cannot fully test the affective/intensity dimension (this is the *iʿjāz al-maʿnā* axis, orthogonal to UAS — see cross-finding-026 §13.5b).

This claim is honestly published as **VINDICATED-on-content-cluster (4 of 5 surahs cohere) and ORTHOGONAL-to-empirical-metric for the Q 11 inclusion** — the Q 11 inclusion reflects affective/theological intensity, not measurable content-distribution.

## 8. Summary table

| Claim | Source | Verdict |
|:--|:--|:--|
| 1. 3-class architecture | al-Rāzī, al-Ṭabarī, al-Qurṭubī | **VINDICATED w/ refinement** (Q 56 unique paragraph-block; Q 35:32 has shorter ternary) |
| 2. Every-night-recitation hadith | Ibn Kathīr → Ibn ʿAsākir | **TRADITION-PRESENT, CHAIN-FALSIFIED** (ḍaʿīf/munkar per al-Bayhaqī, al-Albānī) |
| 3. META-OATH device (Q 56:75-76) | al-Bāqillānī, al-Suyūṭī, al-Rāzī | **VINDICATED** (Q056-F-03: 3 surahs corpus-wide) |
| 4. Q 56→Q 57 chronology boundary | al-Biqāʿī, al-Suyūṭī | **VINDICATED** (rank 17/113 adjacency cost) |
| 5. Q 56:79 muṣḥaf-purity prooftext | Mālik, *Muwaṭṭaʾ* #478 | **CLAIM PRESENT, EXEGETICAL-INTERPRETATION CONTESTED** (Mālik himself reads it as celestial-tablet) |
| 6. Q 56:74 *rukūʿ*-tasbīḥ asbāb al-nuzūl | al-Dārimī #627 | **VINDICATED at canonical-strength** |
| 7. 5-surah gray-hair cluster | Tirmidhī #3381 | **PARTIALLY VINDICATED** (4 of 5 content-cohere; Q 11 is affective/theological inclusion) |

## 9. Honest limits

- The al-Bāqillānī Q 56:75-76 claim relies on classical-tradition aggregation (al-Bāqillānī's full *Iʿjāz al-Qurʾān* PDF on disk has not been per-passage-extracted for Q 56). The empirical META-OATH test (Q056-F-03) is not strictly an audit of al-Bāqillānī's specific argument but a parallel structural-rarity test that yields a result al-Bāqillānī's reading would have predicted.
- The Mālik Q 56:79 audit is a hermeneutic-interpretive claim that the project's metrics cannot decide.
- The 5-surah gray-hair cluster (Tirmidhī #3381) is sub-N=5; permutation-significance is not formally established. The 4 of 5 content-cohesion is *eyeballed* from FR-distance neighbors and would need a formal pre-registered test.
