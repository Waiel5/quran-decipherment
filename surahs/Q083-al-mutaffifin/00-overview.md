---
surah: 83
surah_name_ar: المطففين
surah_name_translit: al-Muṭaffifīn
surah_name_english: "The Defrauders / Those Who Give Short Measure"
file_type: overview
date_last_updated: 2026-05-29
phase: B+
verdict: SCAFFOLD complete — full 8-file investigation; Q083-F-01 DIRECTIONAL (pre-commit violation on H1, H3 CONFIRMED)
---

# Q 83 al-Muṭaffifīn — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 83 | canonical |
| Arabic name | المطففين | named after v.1 *al-muṭaffifīn* ("the defrauders / short-measurers") |
| Transliteration | al-Muṭaffifīn | canonical |
| English meaning | "The Defrauders" / "Those Who Give Short Measure" | from *taṭfīf* = skimping on weight/measure |
| Verse count | 36 | Hafs-Kūfan — `data/hafs-verse-counts.tsv` line `83	36`; verified `quran-text/quran-no-tashkeel.json` (36 verses) |
| Position in mushaf | 83 | canonical |
| Type (project data) | **Meccan** | `data/revelation-order.csv` (period=Meccan, source = Tanzil Egyptian Standard + Wikipedia Nöldeke) |
| Revelation order (Egyptian std) | **86 of 114** — the LAST Meccan surah before Q 2 al-Baqara (#87, first Medinan) | `data/revelation-order.csv` (revelation_order=86) |
| Nöldeke order | **37** | `data/revelation-order.csv` (noldeke_order=37, phase "Early Meccan") |
| Classical Meccan/Medinan status | **DISPUTED** — Meccan (Ibn Masʿūd, al-Ḍaḥḥāk, Muqātil); Medinan (al-Ḥasan, ʿIkrima); "between Mecca and Medina / during the Hijra" (al-Kalbī, Jābir b. Zayd, al-Nasafī) | al-Qurṭubī *al-Jāmiʿ* ad Q 83:1; al-Suyūṭī *al-Itqān* (raw, nawʿ on Makkī/Madanī) |
| Word count (no-tashkeel, marks stripped) | **169** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no spaces, marks stripped) | **750** | computed |
| Distinct words | **118** | TTR = 0.698 (moderate; lower than the extreme short-tail surahs because of the repeated frame) |
| Avg verse length | **4.69 words / 20.8 letters** | computed — short-Meccan-tail stylistic class |
| Opening | **ويل للمطففين** *Wayl li-l-muṭaffifīn* — "Woe to the defrauders!" (a *wayl*-threat opening, NOT oath, NOT muqaṭṭaʿāt, NOT ḥamd) | `quran-text/quran-no-tashkeel.json` |
| Rhyme | **nūn-dominant monorhyme: 27/36 verses (75%) end in ن; 9/36 in م** | computed; matches `h-new-700.json` rhyme_letter_diagnostics (top ن, frac 0.75) |
| Length class | *qiṣār al-mufaṣṣal* / lower *awsāṭ al-mufaṣṣal* (al-Zarkashī hierarchy) | classical |

## 2. The name and the *taṭfīf* opening

The surah is named after its first word, **al-muṭaffifīn** (Q 83:1) — those who commit *taṭfīf*, the
act of skimping when measuring out goods to others while demanding full measure for oneself
(vv. 2–3: *"who, when they take measure from people, take in full; but when they measure or weigh for
them, give less"*). It is the only surah named for a commercial-ethics term, and its opening *Wayl*
("Woe!") places it in the corpus's small set of *wayl*-threat openers.

**al-Ṭabarī** (*Jāmiʿ al-bayān* ad Q 83:1) glosses *al-muṭaffifīn* as "those who diminish people, who
defraud them of their rights in measure or weight." al-Zajjāj (via al-Baghawī ad loc.) explains the
morphology: one is called *muṭaffif* precisely because the amount skimmed in measure/weight is *ṭafīf*
— a small, trifling quantity stolen by stealth (so the sin is severe relative to its pettiness).

## 3. ⭐ Boundary surah — the Meccan/Medinan hinge (see 05-classical-claims-audit Claim 1)

Q 83 is one of the corpus's most-discussed **boundary surahs**. In the Tanzil Egyptian Standard
chronology used by the project (`data/revelation-order.csv`), Q 83 is **revelation #86 — the single last
Meccan surah revealed before Q 2 al-Baqara (#87), the first Medinan surah.** It sits exactly at the
Meccan→Medinan hinge of the revelation sequence.

The classical sources record an unusually rich Makkī/Madanī dispute (al-Qurṭubī *al-Jāmiʿ* ad Q 83:1):
- **Meccan** — Ibn Masʿūd, al-Ḍaḥḥāk, Muqātil (al-Qurṭubī attributes to Ibn al-Faras the rationale "for
  the mention of *asāṭīr al-awwalīn* in it", a Meccan polemic motif).
- **Medinan** — al-Ḥasan al-Baṣrī, ʿIkrima; Muqātil even calls it **"the first surah revealed in
  Medina"**; Ibn ʿAbbās and Qatāda: **Medinan except the eight verses from *inna lladhīna ajramū*
  (v.29) to the end, which are Meccan**.
- **Transitional** — al-Kalbī and Jābir b. Zayd: **"revealed between Mecca and Medina."** al-Suyūṭī
  (*al-Itqān*, raw) cites al-Nasafī and others that it (or part of it) **was revealed during the journey
  of the Hijra, before the Prophet entered Medina.**

This last position — revealed *in transit* during the Hijra — is the explicit empirical anchor for
"boundary surah," and it harmonises with both the Egyptian-order placement (#86, last-Meccan) and the
*asbāb al-nuzūl* about the Medinan merchants' short-measuring (which presumes a Medinan audience).

## 4. ⭐ The SIJJĪN ↔ ʿILLIYYĪN antithesis (the surah's signature structure)

The structural heart of Q 83 is a deliberate **muqābala** (antithetical parallelism) between two
destiny-record scenes, each opened by the rebuke-particle *kallā*:

| | FUJJĀR scene (vv. 7–17) | ABRĀR scene (vv. 18–28) |
|:--|:--|:--|
| opener | *kallā inna kitāba l-fujjāri la-fī **sijjīn*** (7) | *kallā inna kitāba l-abrāri la-fī **ʿilliyyīn*** (18) |
| "what is it?" | *wa-mā adrāka mā sijjīn* (8) | *wa-mā adrāka mā ʿilliyyūn* (19) |
| the record | ***kitābun marqūm*** (9) | ***kitābun marqūm*** (20) |
| destiny | *jaḥīm* (Hell, 16); *maḥjūbūn* (veiled from the Lord, 15) | *naʿīm* (bliss, 22); *raḥīq makhtūm / misk / tasnīm* (25–27) |

The two scenes share the **exact same announcement frame** (*kallā inna kitāba …, wa-mā adrāka mā …,
kitābun marqūm*) while their destiny-vocabularies are **mutually disjoint**. This is the surah's
signature — and the target of the pre-registered test **Q083-F-01** (06-novel-findings). The empirical
result is more interesting than the hypothesis: the two 11-verse blocks share only **3 roots**
(`kitāb`, `marqūm`, `adrāka` — the bare frame) against a random-block-pair null mean of **12.7**, i.e.
the antithesis is built on near-total lexical DISJUNCTION, not lexical mirroring (a pre-committed
direction was reversed and is reported as a violation; H3 destiny-disjunction CONFIRMED at zero
leakage).

## 5. ⭐ The *rān* verse (Q 83:14) and its famous hadith

Q 83:14 — *kallā bal rāna ʿalā qulūbihim mā kānū yaksibūn* ("Nay! Rather, what they were earning has
RUSTED over their hearts") — is the corpus's locus classicus for the doctrine of the **heart's rust
(*al-rān*)**. It is directly explicated by the *ṣaḥīḥ* "black-spot" hadith of Abū Hurayra (al-Tirmidhī,
*Chapters on Tafsīr*, graded *ḥasan ṣaḥīḥ*; also Ibn Mājah *Kitāb al-Zuhd*) — see 04-hadith-corpus.
The root ر-و-ن (*rān*) is rare in the corpus; this verse is its theological anchor.

## 6. ⭐ The standing-on-Judgment-Day verse (Q 83:6) and its ṣaḥīḥ hadith

Q 83:6 — *yawma yaqūmu l-nāsu li-rabbi l-ʿālamīn* ("the Day when mankind will stand before the Lord of
the worlds") — is explicated by a directly-citing Bukhārī/Muslim hadith of Ibn ʿUmar (Bukhārī
*Kitāb al-Tafsīr*; Muslim): people will stand until one sinks in his own sweat "to the middle of his
ears." See 04-hadith-corpus.

## 7. ⭐ The rebuke-*kallā* maximum (link to §10.80 H-NEW-2160)

Q 83 contains **4 genuine rebuke-*kallā*** (QAC POS:AVR, LEM `kal~aA`) at verses **7, 14, 15, 18** —
**tied with Q 74 al-Muddaththir for the corpus maximum** (no surah has more than 4). This is the
disambiguated, homograph-clean count: Q 4 al-Nisāʾ also shows "4 كلا" by raw substring, but ALL of Q 4's
are the homograph *kullā/kilā* ("both/all"), with ZERO genuine rebuke-*kallā* — exactly the homograph
trap documented in §10.80 (H-NEW-2160). Q 83's 4 are all clause-initial rebuke particles, all in the
mushaf second half, directly substantiating al-Dānī's classical "second-half-only" observation
(total genuine AVR-*kallā* corpus-wide = **33**, matching the classical count). See 07-cross-references.

## 8. Empirical architectural profile (headline)

See `01-empirical-profile.md`. Key numbers (all from `findings/phase-b-hypotheses/csv/`):
- **FR-mean to corpus = 0.8653** (BELOW corpus mean 0.9235 by Δ=−0.058 — Q 83 is FR-CENTRAL; centrality
  rank 38/114).
- **FR top-neighbour structure: short-Meccan-tail-dominated**; Q 82 al-Infiṭār is the **2nd-nearest**
  (0.5770) — a strong mushaf-neighbour signal (Q 81/82/83/84 are a thematically-linked
  judgment-scene cluster).
- **Outlier-strength (H-NEW-590): delta_pct = −0.26, classification NULL** — Q 83 is INTERIOR to its
  FR-cluster, NOT an outlier.
- **UAS (H-NEW-840): rank 110/114, UAS = −2.49** — among the corpus's LOWEST architectural-significance
  scores (matches Protocol §3.3 bottom-10 listing of Q 83). Q 83 is an **anti-iʿjāz / low-UAS**
  short-tail surah on the structural-significance axis.
- **iʿjāz signature (H-NEW-750): sig_A = +0.198 (rank 55), sig_B = −0.339 (rank 64)** — middling
  al-Bāqillānī fawāṣil score, slightly-negative al-Sakkākī iqāʿ score.
- **Rhyme: nūn-monorhyme, 0.75 fraction; rhyme entropy 0.562 nats** (LOW — near-monorhyme, contrast
  with multi-rhyme short-tail surahs).
- **Adjacency (H-NEW-720): Q 82→83 delta_raw = +0.0355 (rank 38/113, smooth); Q 83→84 = +0.0646
  (rank 59/113, middle-pack).**

## 9. Quick content structure (4 blocks)

- **vv. 1–6:** TAṬFĪF threat + resurrection-denial — *Wayl* to the short-measurers; "do they not think
  they will be raised … the Day mankind stands before the Lord of the worlds?"
- **vv. 7–17:** FUJJĀR scene — *kallā! the record of the wicked is in sijjīn … a written record … woe
  that Day to the deniers … they will burn in the Blaze … this is what you used to deny."*
- **vv. 18–28:** ABRĀR scene — *kallā! the record of the righteous is in ʿilliyyīn … a written record …
  the righteous are in bliss, on couches gazing … given to drink of sealed nectar, its seal is musk …
  mixed with Tasnīm."*
- **vv. 29–36:** REVERSAL OF SCORN — in this world the sinners laughed at the believers and winked at
  them; "but Today the believers laugh at the disbelievers, on couches gazing — have the disbelievers
  [not] been paid back for what they used to do?"

The block-architecture is itself a chiastic-justice structure: the surah opens with worldly fraud (the
defrauders take full, give short) and closes with eschatological RECTIFICATION (the mockers are mocked;
the believers are repaid in full) — the *taṭfīf* / short-changing theme inverted into divine
full-measure recompense.

## 10. Length classification

36 verses, 169 words, 750 letters. In al-Zarkashī's mufaṣṣal hierarchy Q 83 sits in the lower
*al-mufaṣṣal al-awsāṭ* / upper *al-qiṣār*, near the boundary. Mushaf position s=83 places it deep inside
the short-Meccan-tail compression regime (s ≫ kink-50). Its near-monorhyme nūn-ending and repeated
announcement-frame give it a lower lexical-diversity (TTR 0.698) than the extreme-diversity short-tail
oath surahs.

## 11. Cross-references

- [[h-new-111-fisher-rao-mushaf|H-NEW-111]] — Q 83 FR-central (mean 0.8653); Q 82 2nd-nearest.
- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 83 INTERIOR (delta_pct −0.26, NULL).
- [[h-new-700-phonological-compression-tail|H-NEW-700]] — Q 83 nūn-monorhyme 0.75.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 82→83 rank 38; Q 83→84 rank 59.
- [[h-new-750-ijaz-signature|H-NEW-750]] — sig_A +0.198, sig_B −0.339.
- [[h-new-840-unified-architectural-score|H-NEW-840]] — Q 83 UAS rank 110/114 (low; Protocol §3.3 bottom-10).
- §10.80 H-NEW-2160 (rebuke-*kallā* census) — Q 83 corpus-MAX (4) tie with Q 74.
- al-Qurṭubī *al-Jāmiʿ li-aḥkām al-Qurʾān* ad Q 83 — the Makkī/Madanī dispute.
- al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* — Q 83 Hijra-transit revelation tradition; *kallā* in al-waqf nawʿ.
- [[surahs/Q082-al-infitar]] — mushaf-left-neighbour + FR 2nd-nearest (judgment-scene twin; specialist file pending).
- [[surahs/Q084-al-inshiqaq]] — mushaf-right-neighbour (specialist file pending).

## 12. Investigation status

- [x] 00-overview.md (this file)
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 1 pre-reg `preregs/Q083-F-01-sijjin-illiyyin-antithesis-prereg.md` (SHA acd67eb3…)
- [x] 1 script `scripts/Q083_F_01_sijjin_illiyyin_antithesis.py` (SHA-verified at runtime)
- [x] 1 JSON output `csv/Q083-F-01.json`
