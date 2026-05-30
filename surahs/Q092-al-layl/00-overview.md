---
surah: 92
surah_name_ar: الليل
surah_name_translit: al-Layl
file_type: overview
date_last_updated: 2026-05-30
phase: B+
verdict: profile assembled from disk; Q092-F-01 CONFIRMS H-NEW-2360 (giver/miser muqābala is frame-driven overlap) + H-NEW-1820 (Q92 rank 48/49 in lyl)
---

# Q 92 al-Layl — Overview

| Field | Value | Source |
|:--|:--|:--|
| Surah number (mushaf) | 92 | `quran-text/quran-no-tashkeel.json` (id 92) |
| Name (Arabic) | الليل | id 92 |
| Transliteration | al-Layl ("The Night") | id 92 |
| English | The Night | — |
| Verse count | **21** | `total_verses` = 21 |
| Type | **Meccan** | `type` = meccan |
| Revelation order (Tanzil Egyptian) | **#9** | `data/revelation-order.csv` |
| Nöldeke order / phase | **10** / **Early Meccan** | `data/revelation-order.csv` |
| Opening formula | **oath-triad** (*wa-l-layl … wa-l-nahār … wa-mā khalaqa*) | text v1–3 |
| Basmala status | present as verse-0 header; not counted (basmala-counted-only-in-Q1) | rules-tuple |
| Words (whitespace tokens, marks stripped) | **71** | computed, `scripts/Q092_F_01_*.py` pipeline |
| Letters (non-space chars) | **314** | computed |
| Distinct QAC roots | **41** (48 root-tokens) | `data/morphology/root-index.json` |
| Predominant rhyme (rāwī) | **ي (yāʾ / alif-maqṣūra `-ā`), frac = 1.000 (21/21 verses)** | `h-new-700.json` rhyme_letter_diagnostics |
| Length classification | **al-mufaṣṣal al-qiṣār** (short mufaṣṣal) | al-Zarkashī *al-Burhān* mufaṣṣal-tier |

## Text (mark-stripped, no-tashkeel)

| v | Arabic | gloss |
|:-:|:--|:--|
| 1 | والليل إذا يغشى | By the night when it covers |
| 2 | والنهار إذا تجلى | and the day when it shines forth |
| 3 | وما خلق الذكر والأنثى | and That which created the male and the female |
| 4 | إن سعيكم لشتى | your strivings are indeed divergent (*la-shattā*) |
| 5 | فأما من أعطى واتقى | as for him who **gives and fears God** |
| 6 | وصدق بالحسنى | and affirms the best (*al-ḥusnā*) |
| 7 | فسنيسره لليسرى | We shall ease him toward **ease** (*al-yusrā*) |
| 8 | وأما من بخل واستغنى | and as for him who **is miserly and deems himself self-sufficient** |
| 9 | وكذب بالحسنى | and denies the best |
| 10 | فسنيسره للعسرى | We shall ease him toward **hardship** (*al-ʿusrā*) |
| 11 | وما يغني عنه ماله إذا تردى | his wealth will not avail him when he perishes |
| 12 | إن علينا للهدى | upon Us is the guidance |
| 13 | وإن لنا للآخرة والأولى | and to Us belong the Hereafter and the former |
| 14 | فأنذرتكم نارا تلظى | I have warned you of a blazing Fire |
| 15 | لا يصلاها إلا الأشقى | none shall burn in it but the most wretched (*al-ashqā*) |
| 16 | الذي كذب وتولى | who denied and turned away |
| 17 | وسيجنبها الأتقى | the most God-fearing (*al-atqā*) shall be kept far from it |
| 18 | الذي يؤتي ماله يتزكى | who gives his wealth to purify himself |
| 19 | وما لأحد عنده من نعمة تجزى | owing no one a favour to be repaid |
| 20 | إلا ابتغاء وجه ربه الأعلى | but only seeking the Face of his Lord, the Most High |
| 21 | ولسوف يرضى | and he shall surely be well-pleased |

## Architecture at a glance

- **Oath-triad opening (vv 1–3)** answered by *inna saʿyakum la-shattā* (v4): the oath's payload is the
  thesis "human strivings diverge." al-Ṭabarī takes v4 as the *jawāb al-qasam* (`spa5k-tafsir-api/ar-tafsir-al-tabari/92.json` ayah 4, citing Qatāda).
- **Two-pole moral antithesis (vv 5–10):** the giver (*aʿṭā wa-ttaqā*) vs the miser (*bakhila wa-staghnā*),
  each on the identical template `man V₁ wa-V₂ · wa-{ṣaddaqa/kadhdhaba} bi-l-ḥusnā · fa-sa-nuyassiruhu
  li-l-{yusrā/ʿusrā}`. This is the surah's structural centrepiece and the subject of **Q092-F-01**.
- **Eschatological turn (vv 11–16):** wealth-cannot-save → the divine claim (guidance + both worlds belong
  to God) → the warning of *nār talaẓẓā*, reserved for *al-ashqā* (who "denied and turned away").
- **The two superlatives (vv 15, 17): al-ashqā ↔ al-atqā** — a second, surface-rhyming antithesis closing
  the surah, with *al-atqā* glossed by classical exegesis as Abū Bakr (Qurṭubī, ayah 17, citing Ibn ʿAbbās).
- **Pure-intention coda (vv 18–21):** the *atqā* gives wealth not to repay a favour but *ibtighāʾa wajhi
  rabbihi al-aʿlā*; the surah ends on *wa-la-sawfa yarḍā* ("he shall be well-pleased").

## Naming paradox (H-NEW-1820 anchor)

Q 92 is named al-Layl ("The Night") yet the root `lyl` occurs in it **exactly once** — its opening word
*wa-l-layl* (v1). Among the 49 surahs that contain the root, Q 92 ranks **48/49** in `lyl`-density (Arm C
of Q092-F-01); the density peak is Q 2 al-Baqara (5×). The surah is named for its **rhetorical opening
image**, not its lexical frequency — a textbook confirmation of the title-density-independence law. See
`01-empirical-profile.md` §7 and `06-novel-findings.md` Arm C.

## God-naming note

The name **Allāh does not appear in Q 92 at all** (0 substring tokens). God is named once as *rabb*
(v20, *rabbihi al-aʿlā*) and otherwise carried by the divine first-person (*ʿalaynā* v12, *lanā* v13,
*fa-sa-nuyassiruhu* vv7,10, *anzartukum* v14). This is characteristic of the early-Meccan oath surahs in
Q 92's FR neighborhood (cf. `01-empirical-profile.md` §1).

## Cross-references

- [[Q091-al-shams/00-overview|Q 91 al-Shams]] — preceding surah; Q 91 → Q 92 is the **single cheapest seam in the mushaf** (H-NEW-720, rank 1/113).
- [[Q093-al-duha/00-overview|Q 93 al-Ḍuḥā]] — following surah; *wa-l-ḍuḥā wa-l-layli idhā sajā* mirrors Q 92's day/night oath.
- [[h-new-1820-title-density-independence-formal|H-NEW-1820]] — title-density-independence (Q 92 rank 48/49 in lyl).
- [[h-new-2360-antithesis-law|H-NEW-2360]] — antithesis = frame + overlapping content (Q092-F-01 Arm A confirms at showcase scale).

---

*All values traced to on-disk artifacts as cited. Assembled 2026-05-30 by Waiel Al-Shujaa.*
