---
surah: 66
surah_name_ar: التحريم
surah_name_translit: al-Taḥrīm
surah_name_english: "The Prohibition"
file_type: overview
date_last_updated: 2026-05-29
phase: B+
verdict: 1 pre-registered 2-arm test landed — Arm A CONFIRMED (verbatim verse-twin) + Arm B NULL (dual-exemplar seal pre-commit violation)
---

# Q 66 al-Taḥrīm — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 66 | canonical |
| Arabic name | التحريم | canonical (verbal-noun *taḥrīm*, "making-forbidden"; from v 1 *li-ma tuḥarrimu*) |
| Transliteration | al-Taḥrīm | canonical |
| English meaning | "The Prohibition / The Forbidding" | classical |
| Alternative name | *Sūrat al-Nabī* ("the surah of the Prophet") | al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 66:1 |
| Verse count | 12 | Hafs-Kufan (`data/hafs-verse-counts.tsv` line 66); al-Qurṭubī "اثنتا عشرة آية" |
| Position in mushaf | 66 | canonical |
| Revelation order | #107 (Tanzil Egyptian Standard); Nöldeke #109 | `data/revelation-order.csv` |
| Type | Medinan ("مدنية في قول الجميع" — Medinan by all accounts) | al-Qurṭubī on v 1 |
| Word count (no-tashkeel, marks stripped) | 254 | computed (`scripts/Q066_F_01_tahrim_seal.py` pipeline) |
| Letter count (no-tashkeel) | 1,105 | computed |
| Distinct QAC roots | 96 (171 root-tokens) | `data/morphology/root-index.json` |
| Opening | يا أيها النبي — "O Prophet" | prophet-vocative (the *yā-ayyuhā al-nabī* family) |
| Predominant rhyme (rāwī) | ن (nūn), 5/12 verses (41.7%) | `h-new-700.json` rhyme_letter_diagnostics; `h-new-750.json` |
| Length class | mufaṣṣal-awsāṭ (short Medinan; al-mufaṣṣal mid-tier) | al-Zarkashī mufaṣṣal-3-tier |

## 2. Why Q 66 matters for the project

1. **Verbatim verse-twin carrier.** Q 66:9 (`yā ayyuhā al-nabī jāhid al-kuffāra wa-l-munāfiqīna
   wa-ghluẓ ʿalayhim wa-maʾwāhum jahannamu wa-biʾsa al-maṣīr`) is **character-for-character identical**
   to Q 9:73 — one of only **11 verbatim full-verse twin groups (≥10 tokens)** in the entire corpus
   (Q066-F-01 Arm A, CONFIRMED). This is the project's first per-surah landing of the long-verse-twin
   roster, and it cross-anchors the H-NEW-1520 prophet-vocative pericope finding (where Q 9:73-75 ×
   Q 66:9-11 was the #2 directive pair).

2. **Corpus-exclusive antithetical exemplar-frame.** The seal vv 10-11 carry the only place in the
   corpus where `ḍaraba Allāh mathalan li-lladhīna kafarū` is immediately followed by `wa-ḍaraba Allāh
   mathalan li-lladhīna āmanū` (Q066-F-01 Arm B, B-H1 PASS). The believer/disbeliever exemplar-frame
   set in direct adjacency is a Q 66 structural singleton.

3. **The seal's content-cohesion is frame-driven, not woman-driven (honest NULL).** Q066-F-01 Arm B is
   a **pre-commit violation NULL**: the disbeliever-exemplar verse v 10 is lexically *closer* to the
   first believer-exemplar v 11 (Āsiya) than the two believer-exemplars (v 11 Āsiya, v 12 Maryam) are
   to each other — because the shared `ḍaraba … mathalan li-lladhīna … imraʾat` parable-frame binds
   the two parable-halves, while Maryam's verse (no frame, virginity/spirit vocabulary) is the
   lexical outlier of the seal. Published with full prominence per PRE-REG-STANDARD-04.

4. **Asbāb al-nuzūl locus.** Q 66:1-5 is the densest asbāb-al-nuzūl cluster in the short-Medinan block:
   the honey/Maghāfir episode (ʿĀʾisha + Ḥafṣa) and the Māriya episode, both attested across the
   canonical ḥadīth (Bukhārī Book of Tafsīr #4704-4705, Muslim #3555-3556, al-Tirmidhī #3402, and
   parallels) and across the classical tafsīr split (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī).

5. **Prophet-vocative family member.** Q 66 belongs to the *yā-ayyuhā al-nabī* set {Q 8, 9, 33, 60, 65, 66}
   (H-NEW-1360 whole-surah NULL → H-NEW-1520 pericope PASS). Q 66 carries TWO of the corpus's 13
   prophet-vocative attestations (v 1, v 9) — a within-surah double, shared only with Q 33 (which has
   five) among Medinan surahs.

6. **Seamless backward seam.** Q 65 al-Ṭalāq → Q 66 al-Taḥrīm is a clamped-zero / negative-delta
   transition (delta_raw = −0.03397, ascending-rank 5/113, one of the 13 seamless seams of H-NEW-720).
   The al-Ṭalāq→al-Taḥrīm pair is among the corpus's smoothest mushaf joints — al-Rāzī's munāsaba
   (both surahs concern women's rulings, both open on prohibition/divorce) has a direct FR/TSP correlate.

## 3. Empirical anchor summary (all from on-disk artifacts — see `01-empirical-profile.md`)

| Instrument | Value | Source |
|---|---|---|
| FR mean to all 113 surahs | 0.9093 | `h-new-111.json` (Q66 row) |
| Top-3 FR neighbors | Q 110, Q 112, Q 98 | `h-new-111.json` |
| Q 65 (prev surah) rank in Q 66's FR list | 49/113 (FR 0.8705) | `h-new-111.json` |
| Q 65 → Q 66 seam | delta_raw = −0.03397, rank 5/113 (seamless) | `h-new-720.json` |
| Q 66 → Q 67 seam | delta_raw = +0.07804, rank 67/113 | `h-new-720.json` |
| H-NEW-590 outlier | delta_pct = −1.90, **NULL** (cohesion member of Q 63-69 window) | `h-new-590.json` |
| H-NEW-700 monorhyme | ن (nūn), 41.7%; entropy 1.237 nats | `h-new-700.json` / `h-new-750.json` |
| H-NEW-750 sig_A | +0.9856 (rank 34/114) | `h-new-750.json` |
| H-NEW-750 sig_B | +0.3466 (rank 48/114) | `h-new-750.json` |
| H-NEW-840 UAS | −1.0521 (rank 77/114) | `h-new-840.json` |
| Allāh-substring | 13 tokens, 8/12 verses (66.7%) | computed |

## 4. Surface structure

| Block | Verses | Function |
|---|---|---|
| Prophet-vocative opening + prohibition | 1 | *yā ayyuhā al-nabī li-ma tuḥarrimu mā aḥalla Allāhu lak* |
| Oath-dissolution (taḥilla) ruling | 2 | *qad faraḍa Allāhu lakum taḥillata aymānikum* |
| The confided-secret episode | 3 | the Prophet confides a matter; it is disclosed; partial confrontation |
| The two-wives admonition | 4 | *in tatūbā ilā Allāh* … *wa-in taẓāharā ʿalayhi* (Jibrīl + the righteous believers + angels backing) |
| The divorce-replacement threat | 5 | *ʿasā rabbuhu in ṭallaqakunna an yubdilahu azwājan khayran minkunna* (8 wife-virtues + thayyibāt/abkār) |
| Believer fire-guarding charge | 6 | *yā ayyuhā alladhīna āmanū qū anfusakum wa-ahlīkum nāran* (the 19-angel guard) |
| Disbeliever no-excuse charge | 7 | *yā ayyuhā alladhīna kafarū lā taʿtadhirū al-yawm* |
| Tawba naṣūḥ + light-of-believers | 8 | the surah's longest verse (46 words) — sincere repentance + the running light |
| Prophet-vocative jihad charge | 9 | **verbatim twin of Q 9:73** |
| Disbeliever-wife exemplars | 10 | wife of Nūḥ + wife of Lūṭ (the negative parable) |
| Believer-wife exemplar Āsiya | 11 | wife of Firʿawn (the positive parable) |
| Believer-virgin exemplar Maryam | 12 | Maryam bint ʿImrān (the seal) |

## 5. Pre-registered novel finding (full detail in `06-novel-findings.md`)

| ID | Verdict | One-liner |
|---|---|---|
| Q066-F-01 Arm A | **CONFIRMED** | Q 66:9 ≡ Q 9:73 verbatim — one of only 11 long-verse (≥10-tok) twin groups in the corpus |
| Q066-F-01 Arm B | **NULL (pre-commit violation)** | Antithetical exemplar-frame corpus-exclusive to Q 66:10-11 (B-H1 ✓), but believer-pair v11/v12 LESS cohesive than the disbeliever/Āsiya frame-pair v10/v11 — the parable-frame binds harder than the believer-women theme |

## 6. Cross-references

- **H-NEW-1520 / H-NEW-1360** — prophet-vocative family {Q 8, 9, 33, 60, 65, 66}; pericope-scale flip; Q 66 carries vocatives at v 1 and v 9
- **H-NEW-720** — Q 65 → Q 66 seamless seam (rank 5/113); Q 66 → Q 67 mid-spectrum
- **H-NEW-590** — Q 66 is a COHESION member of the Q 63-69 window (delta_pct = −1.90, NULL)
- **Cross-finding-025** (scale-of-aggregation): Q 66's prophet-vocative content lives at pericope scale, not whole-surah — consistent with the family NULL
- **Q 9 al-Tawba** — Q 9:73 ≡ Q 66:9 verbatim twin; the jihād-against-kuffār-and-munāfiqīn directive is shared verbatim
- **Q 65 al-Ṭalāq** — backward-adjacent women's-rulings munāsaba (al-Rāzī)

## 7. Classical-tradition status

- al-Qurṭubī (*al-Jāmiʿ li-aḥkām*): Medinan by consensus; 12 verses; also called *Sūrat al-Nabī*; the
  honey-version asbāb from Ṣaḥīḥ Muslim; the dual-exemplar seal read as an admonition to ʿĀʾisha and
  Ḥafṣa (citing Yaḥyā b. Sallām).
- al-Ṭabarī (*Jāmiʿ al-bayān*): the exegetical split — the forbidden-thing is either Māriya (Zayd b.
  Aslam, al-Shaʿbī ← Masrūq) or the honey; *anta ʿalayya ḥarām* is *laghw* (idle speech).
- al-Zamakhsharī (*al-Kashshāf*): the Māriya narration in full; legal *taḥrīm al-ḥalāl* survey
  (Abū Ḥanīfa vs al-Shāfiʿī; ṣaḥāba positions); kaffāra question (al-Ḥasan: no kaffāra; Muqātil: freed a slave).
- al-Rāzī (*Mafātīḥ al-ghayb*): the Q 65→Q 66 munāsaba (shared women's-rulings + prohibition/divorce);
  three *masāʾil* on whether v 1 is *ʿitāb* (reproach) or *tanbīh* (gentle alert), and the metaphysics
  of "forbidding the lawful." al-Rāzī explicitly cites al-Kashshāf verbatim.
- al-Bāqillānī (iʿjāz al-fawāṣil): nūn-dominant fawāṣil; sig_A rank 34/114 — mid-upper structural significance.

## 8. Open questions / queued tests

- Q066-F-02 (queued): is the Q 9:73 ≡ Q 66:9 verbatim twin a *directional* import (Q 9 earlier in
  revelation order #113 vs Q 66 #107 — actually Q 66 is EARLIER) — test the chronology of the twin.
- Q066-F-03 (queued): the 8-virtue wife-list of v 5 (*muslimāt muʾmināt qānitāt tāʾibāt ʿābidāt
  sāʾiḥāt thayyibāt abkār*) — is this the corpus's densest single-verse feminine-virtue enumeration?
- Q066-F-04 (queued): re-test the dual-exemplar seal at the *parable-pair* scale (v10-v11 vs v11-v12
  as two competing groupings) to formalize the frame-vs-theme tension surfaced by Q066-F-01 Arm B.

---

*Investigation: Wave-N (2026-05-29) Q 66 al-Taḥrīm full deep-dive. See JOURNAL.md for the method log;
06-novel-findings.md for test detail; 04-hadith-corpus.md for the verified asbāb al-nuzūl chain.*
