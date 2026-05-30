---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 6 claims audited — 4 VINDICATED, 1 SUPPORTED-as-asbāb (not-architectural), 1 NOT-TESTABLE; 1 NOTED data-correction (no orchard-owner sabab on disk for Q 92)
---

# Q 92 al-Layl — Classical Claims Audit

Each claim is stated with citation, given a rules-tuple, tested where empirically testable, and given an
honest verdict. Default rules-tuple: `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`. Verse text from `quran-text/quran-no-tashkeel.json`; classical passages read in
Arabic from `data/literature/classical-tafsir/spa5k-tafsir-api/{edition}/92(/{ayah}).json`.

## Claim 1 — "Sūrat al-Layl is Meccan; it is twenty-one verses by consensus" (al-Qurṭubī)

**Claim:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 92:1 (`ar-tafseer-al-qurtubi/92/1.json`):
*"Sūrat al-Layl: makkiyya. wa-qīl: madaniyya. wa-hiya iḥdā wa-ʿishrūna āya bi-l-ijmāʿ"* — "Meccan; and it
is said [also]: Medinan. And it is twenty-one verses by consensus."

**Test:** (a) Cross-check chronology in `data/revelation-order.csv`. (b) Count verses in
`quran-text/quran-no-tashkeel.json` (id 92) and cross-check `data/hafs-verse-counts.tsv`.

**Result:**
- Chronology: `revelation-order.csv` row `mushaf_order = 92` → period **Meccan**, revelation_order **#9**,
  Nöldeke **#10**, phase **Early Meccan**. The minority Medinan view al-Qurṭubī notes is *not* represented
  on disk; the standard chronologies are unanimously Meccan.
- Verse count: `quran-no-tashkeel.json` id 92 `total_verses = 21`; `hafs-verse-counts.tsv` mushaf-92 line = **21**.

**Verdict: VINDICATED.** Q 92 is Meccan (early-Meccan, rev-order #9) and 21 verses in both the
Egyptian-standard/Nöldeke chronologies and the Hafs verse-count on disk. al-Qurṭubī's *bi-l-ijmāʿ* for
the verse-count is corroborated (Q 92 is below the threshold where the Kūfan/Baṣran/Madanī counting
schools diverge); his minority "wa-qīl madaniyya" has no on-disk chronology variant.

## Claim 2 — al-Ṭabarī: v 4 *inna saʿyakum la-shattā* is the *jawāb al-qasam* (the answer to the oath)

**Claim:** al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 92:4 (`ar-tafsir-al-tabari/92.json` ayah 4): marks v 4 as the
oath's answer on Qatāda's authority and glosses *shattā* as *mukhtalif* — "your deeds are divergent: among
you the disbeliever in his Lord and the believer in Him."

**Test:** Does the surah's block architecture place a hinge at v 4? The empirical correlate is structural,
not numerical: v 1–3 swear by three opposed cosmic pairs; v 4 delivers the divergence-thesis; vv 5–10
realise the divergence as the two-pole moral antithesis. (See `02-content-analysis.md` §§1–2.)

**Result:** The oath-triad (vv 1–3: night/day, *yaghshā*/*tajallā*, male/female) and the giver/miser
antithesis (vv 5–10) are bridged by exactly one verse, v 4 (*la-shattā*). The giver/miser antithesis tested
in **Q092-F-01 Arm A** is the lexical realisation of the "divergence" v 4 announces — and it is
**frame-driven** (Arm B): a constant antithesis scaffold with swapped poles, i.e. divergence built on a
shared frame. al-Ṭabarī's *mukhtalif* (divergent) reading is precisely what the surah's architecture enacts.

**Verdict: VINDICATED (structural-descriptive).** v 4 is the architectural hinge between the cosmic-pair
oath and the moral bifurcation; al-Ṭabarī's *jawāb al-qasam* reading maps onto the surah's block structure.
(This is a rhetorical-structure claim, not a numerical one; verdict is descriptive.)

## Claim 3 — al-Suyūṭī: Q 92:5–10 is a paradigm *muqābala* (*al-ṭibāq wa-l-muqābala*, Itqān nawʿ 59)

**Claim:** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 59 (*al-ṭibāq wa-l-muqābala*; PDF
`suyuti-al-itqan-fi-ulum-al-quran-english.pdf`): antithesis (*ṭibāq*) and the placing of one set of items
against an opposed set (*muqābala*) are marked Quranic figures. Q 92:5–10 sets three giver-items
(*aʿṭā / ittaqā / ṣaddaqa*) against three miser-items (*bakhila / istaghnā / kadhdhaba*), with paired
outcomes (*yusrā ↔ ʿusrā*).

**Test (PRE-REGISTERED as Q092-F-01 Arm A + Arm B):** Does this textbook muqābala behave as the project's
own corpus law **H-NEW-2360** (§10.103) predicts — content-**OVERLAPPING** and **frame-driven** (the jadal
signature) — or as the *rejected* "muqābala = minimal frame + disjoint content" candidate law predicted
(content-**depleted**)? Direction LOCKED to the H-NEW-2360 prior (OVERLAP-positive) before computation.

**Result (from `csv/Q092-F-01.json`, pre-reg SHA verified at runtime):**
- **Arm A — content overlap.** J(giver-block, miser-block) = **0.2222** (shared roots {Hsn, ysr});
  permutation null (same-surah length-matched 3-verse block-pairs, seed 20260509, 10,000 perms):
  null-mean 0.0342, **z = +2.646, p_upper = 0.0327 < α = 0.05**; replication seed 20260601 p = 0.0329.
  Direction = **OVERLAP-positive (TIGHTER than random)** — matches the lock.
- **Arm B — frame-vs-pole.** Shared roots = exactly the frame {Hsn (*al-ḥusnā*), ysr (*nuyassiruhu …
  yusrā/ʿusrā*)}; the three giver poles {ETw, wqy, Sdq} and three miser poles {bxl, gny, k\*b} are
  pairwise **disjoint**. **PASS** — the overlap is the antithesis scaffold, the divergence is in the poles.

**Verdict: VINDICATED — and refined.** al-Suyūṭī's identification of Q 92:5–10 as a muqābala is correct.
The project's empirical refinement: this muqābala is **content-overlapping and frame-driven**, confirming
the corpus jadal law **H-NEW-2360** at the single-surah showcase scale (z = +2.65). It is the **opposite**
of the hand-selected Q 83 sijjīn↔ʿilliyyīn showcase (Q083-F-01, which found disjoint destiny-lexica) — and
thereby a third independent vindication of H-NEW-2360 over the rejected disjoint-content candidate law (see
`06-novel-findings.md` and §10.103, §10.99 of the ledger). al-Suyūṭī's nawʿ 59 figure is real and marked;
the *generalizing* "disjoint-content" form is the part that fails, and Q 92 confirms it fails here too.

## Claim 4 — The asbāb al-nuzūl of vv 5–7 / 17–21: the giver and the *atqā* are Abū Bakr al-Ṣiddīq

**Claim:** al-Qurṭubī, on Q 92:5 (`ar-tafseer-al-qurtubi/92/5.json`): *"fa-ammā man aʿṭā wa-ttaqā — qāla
Ibn Masʿūd: yaʿnī Abā Bakr … wa-qālahu ʿāmmat al-mufassirīn"* (Ibn Masʿūd: it means Abū Bakr; and the
generality of the exegetes said so), narrating Abū Bakr manumitting elderly Muslims/weak women and his
father Abū Quḥāfa objecting. And on Q 92:17 (`…/17.json`): *"al-atqā … qāla Ibn ʿAbbās: huwa Abū Bakr …
yuzaḥzaḥ ʿan dukhūl al-nār"* (Ibn ʿAbbās: it is Abū Bakr, removed from entering the Fire). And on Q 92:19
(`…/19.json`): the manumission of **Bilāl** — Abū Bakr buying him with *raṭl* of gold; the polytheists
sneering "he freed him only to repay a debt," whereupon *wa-mā li-aḥadin ʿindahu min niʿmatin tujzā* (v 19)
was revealed.

**Test:** This is a historical-occasion (asbāb/isnād) claim about *who* the verses describe, not a
structural-numerical claim about the text. The text's own wording is general (*man aʿṭā* / *al-atqā*), and
the exegetes themselves preserve a general reading (Ibn Kathīr: *al-ʿibra bi-ʿumūm al-lafẓ* — the wording's
generality governs; `en-tafisr-ibn-kathir` / `ar-tafsir-ibn-kathir/92.json`).

**Result:** The Abū-Bakr/Bilāl asbāb is on-disk attested in al-Qurṭubī (vv 5, 17, 19) and the shared
classical chain (al-Baghawī, Ibn Kathīr report it while noting the general wording). It is **not**
empirically adjudicable by the project's architectural instruments (it concerns referent, not structure).

**Verdict: SUPPORTED-as-asbāb (NOT architecturally testable).** The Abū Bakr identification is the
mainstream sabab and is fully on disk; the verses' wording is general (so Ibn Kathīr's *ʿumūm al-lafẓ* and
the Abū Bakr sabab coexist). This is a riwāya matter, outside the empirical-architectural scope; documented,
not adjudicated.

## Claim 5 — al-Qurṭubī's two-paths theme: the surah teaches two divergent destinies (*yusrā* ↔ *ʿusrā*)

**Claim:** al-Qurṭubī / al-Ṭabarī (and the predestination ḥadīth-family, see `04-hadith-corpus.md`): the
surah's payload is that humans diverge into two paths — *We shall ease the giver toward ease (yusrā)* and
*ease the miser toward hardship (ʿusrā)* — God *facilitating* each soul toward what was written for it
(*iʿmalū fa-kullun muyassar*, ʿAlī, Bukhārī #1315 / #4740, Muslim #6566).

**Test:** Is the two-paths divergence lexically realised as a *symmetric* antithesis (constant frame,
opposed poles, opposed outcomes), and does the *ysr* root literally span both paths (the surah easing
toward *both* yusrā and ʿusrā)?

**Result:** The QAC root **ysr** (ease/facilitate) is the apodosis of *both* poles — *fa-sa-nuyassiruhu
li-l-yusrā* (v 7) and *fa-sa-nuyassiruhu li-l-ʿusrā* (v 10) — i.e. the very root that names "easing" is
applied to the hard path too (the *muyassar* of the ḥadīth). It is a **frame root** shared by both blocks
(Q092-F-01 Arm B: ysr ∈ shared). The two-paths divergence is thus carried by *opposed poles inside a
constant easing-frame*, exactly the two-paths structure al-Qurṭubī describes. (Root-echo support: *gny* —
the miser *istaghnā* v 8 but his wealth *lā yughnī* v 11; *wqy* — the giver *ittaqā* v 5 → *al-atqā* v 17;
see `02-content-analysis.md`.)

**Verdict: VINDICATED (structural).** The two-paths theme is lexically grounded: the *ysr* "facilitation"
root spans both destinies (yusrā/ʿusrā) inside the antithesis frame, matching the ḥadīth's *iʿmalū
fa-kullun muyassar* reading and al-Qurṭubī's two-paths exposition. (Theme-grounding, not a null-tested
numerical claim; verdict is structural-descriptive.)

## Claim 6 (NOT-TESTABLE) — the qirāʾa of v 3: *wa-mā khalaqa al-dhakara wa-l-unthā* vs *wa-l-dhakara wa-l-unthā*

**Claim:** Ibn Masʿūd's reading of v 3 was *wa-l-dhakara wa-l-unthā* (without *wa-mā khalaqa*), affirmed by
Abū al-Dardāʾ as heard from the Prophet (al-Bukhārī #4736–4737, see `04-hadith-corpus.md`). The canonical
Ḥafṣ/ʿuthmānī text is *wa-mā khalaqa al-dhakara wa-l-unthā*.

**Test:** This is a qirāʾāt (reading-tradition) question, not a structural claim about the canonical text.

**Verdict: NOT-TESTABLE (empirically) — documented.** The project's canonical text is the Ḥafṣ reading
(`quran-no-tashkeel.json` v 3 = وما خلق الذكر والأنثى). The Ibn Masʿūd variant is ḥadīth-attested and noted
in `04-hadith-corpus.md`; it does not enter the Q092-F-01 root-set (the v 3 roots *xlq, \*kr, Anv* are not
part of the giver/miser blocks). Documented, not adjudicated.

## Data-correction note — the "orchard-owner" sabab is NOT a Q 92 sabab on disk

The orchard-owner / *aṣḥāb al-janna* occasion belongs to **Q 68 al-Qalam (68:17–33)**, not to Q 92. No
orchard-owner sabab appears in any on-disk Q 92 tafsīr (al-Ṭabarī, al-Qurṭubī, al-Baghawī, Ibn Kathīr 92.json).
The Q 92 asbāb on disk are the Abū-Bakr-giving (vv 5–7) and the Bilāl-manumission (vv 19–21). This is flagged
for honesty; the orchard-owner claim is not asserted for al-Layl.

## Summary table

| # | Claim | Source | Verdict |
|:--|:--|:--|:--|
| 1 | Meccan; 21 verses by consensus | al-Qurṭubī (92:1) | **VINDICATED** |
| 2 | v 4 is the *jawāb al-qasam* / divergence-hinge | al-Ṭabarī (92:4, Qatāda) | VINDICATED (structural) |
| 3 | Q 92:5–10 is a muqābala | al-Suyūṭī (Itqān nawʿ 59) | **VINDICATED — refined: frame-driven OVERLAP (Q092-F-01, H-NEW-2360)** |
| 4 | giver / *atqā* = Abū Bakr (vv 5, 17, 19) | al-Qurṭubī (Ibn Masʿūd, Ibn ʿAbbās) | SUPPORTED-as-asbāb (not architectural) |
| 5 | two-paths divergence (*yusrā* ↔ *ʿusrā*) | al-Qurṭubī / al-Ṭabarī / qadar ḥadīth | VINDICATED (structural; *ysr* spans both) |
| 6 | v 3 qirāʾa variant (Ibn Masʿūd) | al-Bukhārī #4736–4737 | NOT-TESTABLE (documented) |
| — | orchard-owner sabab | (mis-attribution) | NOT a Q 92 sabab on disk (belongs to Q 68) |

## Honest limits

- Claim 3's vindication rests on the QAC root-Jaccard instrument and a same-surah length-matched null; a
  lemma/surface-token level or a different block definition would shift J and the null-mean, but Arm A's
  z = +2.65 and the deterministic frame/pole partition (Arm B) are robust to small block re-definitions.
- Claims 2 and 5 are structural-descriptive (mapping a qualitative exegetical reading onto the surah's block
  architecture and root-echoes), not null-tested numerical claims; they are not promoted to CONFIRMED-finding
  status — only Q092-F-01 (Arms A/B/C) carries a pre-registered verdict.
- The minority "madaniyya" view (Claim 1) and the v 3 qirāʾa (Claim 6) are reading/chronology traditions
  with no on-disk numerical variant; treated as documented, not adjudicated.

---

*All testable claims pre-registered before computation (Q092-F-01) or deterministic. 2026-05-30 by Waiel Al-Shujaa.*
