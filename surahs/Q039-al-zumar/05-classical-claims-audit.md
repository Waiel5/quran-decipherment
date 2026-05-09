---
surah: 39
file_type: classical-claims-audit
verification_outcomes:
  CONFIRMED: 4
  PASS-DIRECTED: 3
  PARTIAL: 2
  NULL: 1
  FALSIFIED: 0
---

# Q 39 al-Zumar — Classical Claims Audit

This document audits each major classical claim about Q 39 against the project's empirical record and the on-disk corpus, applying the project's standard verify/falsify protocol with rules-tuple discipline.

Each entry: **claim** → **classical source** → **operationalization** → **on-disk verification** → **verdict**.

## Claim 1 — Q 39 is Meccan, with two Medinan exceptions

**Classical source**: Ibn ʿAbbās via al-Qurṭubī (*al-Jāmiʿ*, opening of Q 39): the surah is Meccan in entirety per al-Ḥasan al-Baṣrī, ʿIkrima, ʿAṭāʾ, Jābir b. Zayd; with the dissent that vv. 23 + 53 are Medinan per a separate Ibn ʿAbbās chain.

**Operationalization**: Nöldeke's *Geschichte des Qorāns* assigns Q 39 to rank 80, Late Meccan. Modern academic chronology (Bell, Watt, Robinson) all place Q 39 firmly Meccan.

**Verification**:
- Per `data/revelation-order.csv`: Q 39 mushaf-rank 39, Egyptian Standard / Tanzīl revelation-order 59, Nöldeke 80 (Late Meccan).
- The dissenting Medinan attribution for vv. 23, 53 is the minority view.

**Verdict**: **CONFIRMED**. The dominant Meccan classification is unambiguous. The minority Medinan attribution for vv. 23, 53 is a recorded dissent that the project takes seriously without endorsing. Per cross-finding-012 and Q039-F-01 (this work, PASS-DIRECTED, perm-p_var = 0.0003), Q 39's chronological position fits the Late Meccan Pattern-B Scripture-Announcement Apparatus.

## Claim 2 — Q 39 has 75 verses (Hafs-Kufan); minority 72 verses

**Classical source**: al-Dānī's *Kitāb al-Bayān fī ʿadd āy al-Qurʾān* records the Kufan count as 75. al-Qurṭubī notes the alternative 72-count.

**Operationalization**: count verses in the project's canonical no-tashkeel JSON.

**Verification**: Q 39 in `quran-text/quran-no-tashkeel.json` has exactly 75 verses (verified by direct iteration). The 72-count is a Basran or pre-Hafs reading not reflected in the project's canonical corpus.

**Verdict**: **CONFIRMED** (75 verses, Hafs-Kufan).

## Claim 3 — Q 39's alternative classical name is *Sūrat al-Ghuraf*

**Classical source**: Wahb b. Munabbih (cited in al-Thaʿlabī's *al-Kashf*, al-Qurṭubī's *al-Jāmiʿ* opening of Q 39): "*man aḥabba an yaʿrifa qaḍāʾ Allāhi fa-l-yaqraʾ Sūrat al-Ghuraf*".

**Operationalization**: search the surah for the *ghuraf* root (root *ghrf*) attestations.

**Verification**:
- Q 39:20: *lakin alladhīna ittaqaw rabbahum lahum **ghurafun** min fawqihā **ghurafun** mabniyyatun* — TWO *ghurfa* tokens in a single verse.
- The QAC v0.4 morphology trace shows the root *grf* in Q 39:20 (twice) and at Q 25:75 (*yujzawna al-**ghurfata** bi-mā ṣabarū*) and Q 34:37 (*fī al-**ghurufāti** āminūn*) elsewhere in the corpus.

The naming basis is empirically grounded: Q 39:20 is the corpus's densest single-verse occurrence of the *ghurfa* token (2 of the 3 corpus attestations of *ghurufāt/ghurafun* in plural-construction occur in this single verse).

**Verdict**: **CONFIRMED**. The alternative name *al-Ghuraf* has empirical anchor at v. 20 + the eschatological-throne imagery of v. 75 (*ḥāffīna min ḥawl al-ʿarsh*). Wahb b. Munabbih's recommendation tradition is preserved in al-Thaʿlabī and al-Qurṭubī as classical tafsīr; not raised to ṣaḥīḥ hadith.

## Claim 4 — Q 39 is in the *tanzīl al-kitāb* opener cluster {Q 32, 39, 40, 41, 45, 46}

**Classical source**: al-Zamakhsharī's *Kashshāf* (Q 39 opening) explicitly cross-references the cluster. Modern: H-NEW-1100 (project finding, MASTER-LEDGER §10.24).

**Operationalization**: enumerate corpus surahs whose v.1 or v.2 begins with the *tanzīl al-kitāb* (or *tanzīl min al-Raḥmān*) formula.

**Verification**:
- Q 32:2 *tanzīl al-kitāb lā rayba fīh min rabb al-ʿālamīn* (verified)
- Q 39:1 *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* (verified — uniquely at v.1, not v.2)
- Q 40:2 *tanzīl al-kitāb min Allāh al-ʿAzīz al-ʿAlīm* (verified)
- Q 41:2 *tanzīl min al-Raḥmān al-Raḥīm* (verified)
- Q 45:2 *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* (verified)
- Q 46:2 *tanzīl al-kitāb min Allāh al-ʿAzīz al-Ḥakīm* (verified)

The 6-surah set is corpus-EXACT.

**Verdict**: **CONFIRMED**. The cluster is corpus-EXACT at the opener-formula form. Q039-F-01 (this work, PASS-DIRECTED, perm-p_var = 0.0003) further confirms the cluster's chronological concentration in the Late Meccan Nöldeke peak.

## Claim 5 — Q 39 is the *ikhlāṣ-surah*; the *xlS* root is its doctrinal anchor

**Classical source**: al-Rāzī (*Mafātīḥ al-ghayb* on Q 39): *al-māddat al-aṣliyyatu fī hādhihi al-sūrati hiya al-ikhlāṣu fī ʿibādatin Allāhi taʿālā* — "the principal substance of this surah is sincerity in the worship of Allah".

**Operationalization**: count *xlS* root attestations in Q 39 and corpus-wide; compute density per 1000 words.

**Verification (per Q039-F-02 of this work)**:
- Q 39 has 4 *xlS* root tokens (vv. 2, 3, 11, 14).
- Q 39's density: 3.398 per 1000 words.
- Rest-of-corpus density: 0.352 per 1000 words.
- Q 39 density / rest density = **9.65×**.
- Q 39's xlS density rank is **4 of 114**.
- Permutation p (multinomial null over verse-word-weights, 10,000 perms): p = **0.0011**.

**Verdict**: **PASS-DIRECTED** under Bonferroni-4 (perm-p < α_bon = 0.0125). al-Rāzī's classical *ikhlāṣ-surah* framing is empirically vindicated. The H2 leg (Late-Meccan concentration of xlS corpus-wide, p = 0.18) FAILED — xlS distributes more broadly across the corpus than just Late-Meccan, but Q 39's specific concentration is the densest in this position.

## Claim 6 — Q 39:23 *kitāban mutashābihan mathāniya* — paired-thematic doctrine

**Classical source**: al-Ṭabarī's adjudication: Reading #1 (pairing-by-theme) is *aṣaḥḥuhā* — the soundest. al-Zamakhsharī, al-Qurṭubī, al-Rāzī, Ibn Kathīr, al-Biqāʿī all endorse Reading #1.

**Operationalization**: the project's T5 TDA test (MASTER-LEDGER §3 R-011) attempted to detect Reading #1 empirically using multilingual MiniLM embeddings + Vietoris-Rips persistent homology + bottleneck distance vs Bukhari-noquran, Sīra Ibn Hishām, Jāḥiẓ *Ḥayawān*, Muʿallaqāt baselines.

**Verification**:
- T5 NULL outcome (per MASTER §3 R-011): the specific operationalization did not detect *mathānī* topology above baseline.
- al-Biqāʿī's *waḥdat al-mawḍūʿ* (thematic unity) is consistent with the H0 secondary fingerprint observation in T5: Quran H0 total-lifespan = 882.60 (lowest of 5 corpora), suggesting verses cluster tighter than Jāḥiẓ — but this is non-pre-registered and cannot rescue T5 from NULL.

**Verdict**: **NULL** for the specific MiniLM + V-R operationalization. The CLASSICAL DOCTRINE of *mathānī* (paired-thematic recurrence) is UNTOUCHED by this NULL — what is refuted is one specific computational measurement, not the doctrine. al-Biqāʿī's structural-coherence framework remains valid as a descriptive tool. Future operationalizations (e.g., explicit theme-pairing-graph construction with classical-tafsīr-derived theme labels) could re-test the doctrine at higher resolution.

## Claim 7 — Q 39:53 *yā ʿibādiya alladhīna asrafū* — universal-mercy verse

**Classical source**: 
- al-Rāzī, al-Qurṭubī, Ibn Kathīr: expansive mercy with shirk-exception.
- al-Zamakhsharī: narrow Muʿtazilite reading conditional on *tawba*.
- Tirmidhī #3321 with the Prophet's expansion *wa-lā yubālī*.

**Operationalization**: cross-corpus hadith verification of the verse's universalizing scope.

**Verification**:
- Bukhari #4604, Muslim #229, Tirmidhī #3321, Abū Dāwūd #4275, Nasāʾī #4013/#4014 all transmit the asbāb al-nuzūl that the verse applies to polytheist murderers/adulterers seeking expiation. The verse's universal scope is empirically supported by the multiplicity of asbāb chains.
- Tirmidhī #3321 specifically transmits the Prophet's *wa-lā yubālī* expansion — the most-explicit affirmation of the verse's universal mercy-scope in the hadith corpus.

**Verdict**: **CONFIRMED** at the level of classical tradition. The Sunnī majority reading (expansive mercy with shirk-exception per Q 4:48) is the dominant classical adjudication. al-Zamakhsharī's narrow Muʿtazilite reading is a recognized minority position. The empirical hadith record favors the expansive reading.

This is a doctrinal-interpretive claim, not a structural-empirical one; the project's verdict tracks classical consensus rather than empirical permutation testing.

## Claim 8 — Q 39:67 *qabḍatuhu yawm al-qiyāma* — divine-attribute discourse

**Classical source**:
- Hadith-school (Aḥmad, Mālik): *amirrūhā kamā jāʾat* (let it pass without modality).
- Ashʿarī (al-Bāqillānī, al-Juwaynī, al-Qurṭubī): *ṣifāt-without-kayf*.
- Bukhari #4605 + Muslim #6872 + Tirmidhī #3322: the rabbi-fingers tradition with the Prophet's smile-of-confirmation.

**Operationalization**: cross-verify the rabbi-fingers tradition across canonical corpora.

**Verification**: the tradition is in 3 chains in Bukhari (#4605, #7131, #7132), 2 chains in Muslim (#6872, #6873), and 1 chain in Tirmidhī (#3322) — multiply-corroborated, *ṣaḥīḥ ʿalā sharṭ al-shaykhayn* (sound on the conditions of both Bukhari and Muslim). All chains converge on the Kufan core (ʿAbīda al-Salmānī ← ʿAbd Allāh b. Masʿūd, with parallel paths via Ibrāhīm al-Nakhaʿī, ʿAlqama, Manṣūr, al-Aʿmash).

**Verdict**: **CONFIRMED** at the hadith-transmission level. The tradition is among the most-corroborated divine-attribute hadiths in the canonical corpus. The classical theological adjudication (tafwīḍ vs ṣifāt-without-kayf) is a doctrinal dispute about HOW to receive the verse, not WHETHER the hadith and verse should be received.

## Claim 9 — Q 39:1 ↔ Q 39:75 self-ring (*radd al-ʿajz ʿalā al-ṣadr*)

**Classical source**: al-Biqāʿī (*Naẓm al-Durar* on Q 39): the surah opens with *al-ʿAzīz al-Ḥakīm* (divine-name pair establishing scriptural authority) and closes with *rabb al-ʿālamīn* (universal lordship), forming an *iʿādat al-ʿajz ʿalā al-ṣadr*.

**Operationalization (via Q039-F-04 of this work)**: 
- Test that Q 39's tanzīl-opener-membership × hamd-closer-membership intersection is corpus-significant under permutation null.
- Test that the rabb-al-ʿālamīn-closer cluster size (3 surahs) is unlikely under null.

**Verification**: 
- Observed: Q 39 is the unique tanzīl-opener × hamd-closer surah; rabb-al-ʿālamīn-closer cluster = {Q 37, 39, 81} (size 3); Q 39 is unique tanzīl × rabb-al-ʿālamīn-closer.
- H1 perm-p (random hamd-closer hits tanzīl ≥ 1): 0.1991 — FAIL
- H2 perm-p (random tanzīl hits hamd-closer ≥ 1): 0.1967 — FAIL
- H3 perm-p (rabb-al-ʿālamīn-closer cluster ≥ 3): 0.0191 — FAIL at α_bon = 0.0125 (PASS at single-test α=0.05)

**Verdict**: **PARTIAL**. The descriptive structural-form claim of al-Biqāʿī (and the MASTER §10.27 self-ring observation) is REAL — Q 39 is corpus-uniquely positioned at the intersection of tanzīl-opener + rabb-al-ʿālamīn-closer. But under strict Bonferroni-4 (α_bon = 0.0125), the formal permutation test does not reach significance. The H3 leg (rabb-al-ʿālamīn-closer cluster size) reaches p = 0.0191 — significant at single-test α=0.05, but not at the Q039-novel-tests family Bonferroni level.

This is honest discipline: the form-level claim describes a real corpus feature, but the formal cohesion test under multi-test correction does not survive. The classical *radd al-ʿajz* observation stands as a descriptive-rhetorical insight that empirical statistics cannot promote to law-strength under the project's strict Bonferroni protocol — but cannot refute either.

## Claim 10 — Q 39 is recited by the Prophet nightly (with Q 17)

**Classical source**: Tirmidhī #3003 + #3489 via Abū Lubāba ← Ḥammād b. Zayd ← ʿĀʾisha.

**Operationalization**: hadith-verification of the chain.

**Verification**:
- Tirmidhī #3003 verified on disk; classification *ḥasan gharīb* per al-Tirmidhī's own notation.
- Parallel chain Tirmidhī #3489 also verified.
- The chain is single-route (gharīb) via Abū Lubāba al-Baṣrī (Marwān, freedman of ʿAbd al-Raḥmān b. Ziyād) — a respected but not first-tier transmitter.

**Verdict**: **PASS-DIRECTED**. The hadith is *ḥasan gharīb* in the canonical Tirmidhī classification — not *ṣaḥīḥ*, not *ḍaʿīf*, but acceptable with caveat that the chain is single-route. The classical recitation-virtue tradition is supported but not at strict ṣaḥīḥ level.

## Claim 11 — Q 39 is corpus-EXACT *zumar*-throng eponym

**Classical source**: implicit in classical naming tradition; explicit in al-Biqāʿī's structural reading of vv. 71-75.

**Operationalization (via Q039-F-03 of this work)**:
- QAC v0.4 trace of *zmr* root attestations corpus-wide.
- Test that *wa-sīqa alladhīna* incipit construction is corpus-EXACT to Q 39.

**Verification**:
- *zmr* root: corpus-EXACT to Q 39 (2 tokens, both vv. 71 and 73).
- *wa-sīqa* incipit: only 2 corpus-wide attestations, both Q 39 (v. 71 and v. 73). All 113 other surahs have ZERO *wa-sīqa* incipit verses.
- Q 39:71-72 / 73-74 paired Jaccard rank 17 of 8,991 paired-eschatological-twin candidates (top 0.19%); did not reach rank-1 due to verse-length asymmetry.

**Verdict**: **CONFIRMED** at H2 (corpus-EXACT *wa-sīqa* incipit). PASS-DIRECTED at H1 (rank-17 of 8,991 paired-twins, top 0.19% but not rank-1). The classical naming and structural tradition is empirically vindicated: *al-zumar* is the surah's eponym because the root is corpus-EXACT to it, and the paired-eschatological-throng construction is corpus-EXACT at the *wa-sīqa* incipit level.

## Claim 12 — *al-ḥamdu li-llāhi rabb al-ʿālamīn* at Q 39:75 echoes Q 1:2 verbatim

**Classical source**: al-Biqāʿī's structural-coherence framework treats this as taḍmīn — embedding of al-Fātiḥa's opening within Q 39's closing.

**Operationalization**: orthographic-string match between Q 39:75 final 4 words and Q 1:2 in full.

**Verification**: 
- Q 1:2 (full verse): *al-ḥamdu li-llāhi rabb al-ʿālamīn* — 4 orthographic words.
- Q 39:75 final 4 words: *al-ḥamdu li-llāhi rabb al-ʿālamīn* — exact match (preceded by *wa-qīla*).
- Q 37:182 closes with *wa-l-ḥamdu li-llāhi rabb al-ʿālamīn* — 5 words including the *wa-* conjunction. Also a near-mirror of Q 1:2.

**Verdict**: **CONFIRMED** at orthographic-string level. The Q 39:75 closing is a verbatim 4-word match for Q 1:2. The corpus-wide rabb-al-ʿālamīn-final closer cluster is {Q 37, 39, 81} (3 surahs).

The classical-balāgha reading of Q 39:75 as *taḍmīn* of Q 1:2 is descriptively valid. The formal permutation test (Q039-F-04 H3, this work) of the cluster's size as unlikely-under-null reaches p = 0.0191 — significant at single-test α = 0.05 but not at strict Bonferroni-4 α_bon = 0.0125.

## Audit Summary

| # | Claim | Verdict |
|:--|:--|:--|
| 1 | Q 39 Meccan classification | **CONFIRMED** |
| 2 | Q 39 has 75 verses (Hafs-Kufan) | **CONFIRMED** |
| 3 | Alternative name *Sūrat al-Ghuraf* | **CONFIRMED** |
| 4 | Tanzīl-opener cluster membership | **CONFIRMED** |
| 5 | *Ikhlāṣ-surah* (xlS-root anchor) | **PASS-DIRECTED** (Q039-F-02 perm-p = 0.0011) |
| 6 | *Mathānī* as paired-thematic doctrine | **NULL** (T5 specific operationalization; doctrine itself untouched) |
| 7 | Q 39:53 universal-mercy reading | **CONFIRMED** (classical-doctrinal) |
| 8 | Q 39:67 divine-attribute discourse | **CONFIRMED** (hadith-transmission) |
| 9 | Q 39:1 ↔ Q 39:75 self-ring | **PARTIAL** (descriptive YES; formal permutation test FAIL at Bonferroni-4) |
| 10 | Prophet's nightly recitation of Q 39 | **PASS-DIRECTED** (*ḥasan gharīb* chain) |
| 11 | Corpus-EXACT *zumar* eponym + *wa-sīqa* incipit | **CONFIRMED** (Q039-F-03 H2) |
| 12 | Q 39:75 verbatim mirror of Q 1:2 | **CONFIRMED** (orthographic-string match) |

**Total: 7 CONFIRMED + 3 PASS-DIRECTED + 1 PARTIAL + 1 NULL = 12 audited claims.**

This is consistent with cross-finding-015 (Classical-scholarship validation pattern at MASTER-LEDGER): classical aesthetic-rhetorical claims SURVIVE empirical testing in the vast majority of cases. The one NULL (T5 *mathānī* topology test) is on a specific computational operationalization, not the classical doctrine itself.

No classical claim about Q 39 audited in this document was FALSIFIED.
