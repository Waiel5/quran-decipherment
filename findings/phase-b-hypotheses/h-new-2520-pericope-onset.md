---
id: H-NEW-2520
title: "Pericope-onset / narrative-onset formula census — wa-idh / wa-lammā / wa-qālū: the qaṣaṣ-recall register concentrates in the long surahs (CONFIRMED 3/3, the inverse of the idhā juzʾ-30 cascade)"
type: finding
phase: B
date: 2026-05-30
author: Waiel Al-Shujaa
verdict: CONFIRMED-DIRECTED (3/3 families; Bonferroni-3, α=0.0167)
prereg_sha256: 3cb30e7cc34d567deaf20d8f9c694f9284d7558f799198edadeb844dcc148517
seed: 20260509
replication_seed: 20260511
n_perm: 10000
---

# H-NEW-2520 — Pericope-Onset / Narrative-Onset Formula Census


> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline

The classical **narrative-onset markers** that open *qaṣaṣ* (story) pericopes —
**wa-idh / idh** (وَإِذْ / إِذْ "and recall when…"), **wa-lammā / lammā** (وَلَمَّا / لَمَّا
"and when…"), and **wa-qālū / qālū** (وَقَالُوا / قَالُوا "they said") — concentrate in the
**LONG narrative/legal surahs (s ≤ 50)** at law-strength, **all three families CONFIRMED-DIRECTED**
at the pre-registered direction (Bonferroni-3, α=0.0167, both seeds p=0.00010).

This is the **exact INVERSE of H-NEW-2250**: where the eschatological conditional **idhā** (إِذَا)
concentrates in juzʾ-30 (short-mufaṣṣal, s≥78), the past-recall **idh** (إِذْ) — a grammatically
distinct lemma (`LEM:<i*` vs `LEM:<i*aA`) — concentrates in the long-surah head. The two
homographs occupy **opposite registers**: idh = *qaṣaṣ* memory, idhā = eschatological cascade.
QAC lemma-disambiguation makes this clean separation possible.

| Family | dens(s≤50) | dens(s>50) | ratio | Δ | p (seed A / B) | Verdict |
|:--|:-:|:-:|:-:|:-:|:-:|:--|
| **idh** (وَإِذْ recall) | 0.0235 | 0.0051 | **4.6×** | +0.0184 | 0.00010 / 0.00010 | CONFIRMED-DIRECTED |
| **lammā** (وَلَمَّا event) | 0.0178 | 0.0013 | **13.7×** | +0.0165 | 0.00010 / 0.00010 | CONFIRMED-DIRECTED |
| **qālū** (قَالُوا dialogue) | 0.0289 | 0.0070 | **4.1×** | +0.0218 | 0.00010 / 0.00010 | CONFIRMED-DIRECTED |

*(density = onset-marked verses per verse; permutation null shuffles the head-indicator across
all 6236 slots, 10000 perms; one-sided locked direction.)*

## 2. The onset-marker inventory (the GENERATOR census)

Rules-tuple: `(QAC-v0.4 POS+LEM, verse-initial = word-1, basmala-counted-only-in-Q1, Hafs-Kufan,
Mashriqi)`. Source: `quran-text/quran-no-tashkeel.json` (6236 verses, 100% QAC word-1 coverage) ×
`data/morphology/quranic-corpus-morphology-0.4.txt`.

| Family | Verse-initial total | wa- (وَ) | bare | fa- (فَ) |
|:--|:-:|:-:|:-:|:-:|
| **idh** (إِذْ, `POS:T LEM:<i*`) | 118 | 64 | 54 | 0 |
| **lammā** (لَمَّا, `POS:T LEM:lam~aA`) | 85 | 26 | 1 (other) | 58 |
| **qālū** (قَالُوا, `POS:V ROOT:qwl LEM:qaAla PERF 3MP`) | 146 | 40 | 101 | 4 |

**Disambiguation control (the central methodological point).** The idh lemma `<i*` is matched
EXACTLY (`LEM:<i*` then `|` or end-of-features), so it does NOT capture:
- `<i*aA` (إِذَا) = the conditional/eschatological idhā of H-NEW-2250 (423 POS:T tokens),
- `<i*FA` (إِذَن) = idhan, the answer-particle (31, POS:ANS),
- `<i*on` (إِذْن) = idhn, "permission" noun (39, POS:N).

The 118 verse-initial idh occurrences are the **pure narrative-recall** marker — *udhkur idh…*
"recall when…" — exactly the *qaṣaṣ*-onset.

**Sub-census note (lammā):** lammā's verse-initial form is dominated by *fa-lammā* (58, "and so
when…", the narrative-result connective) and *wa-lammā* (26). This *fa-lammā* dominance is itself
a narrative-structural signature: lammā chains episode-beats with a result-fāʾ, not a
coordinating-wāw.

## 3. Where the narrative skeleton lives — most onset-dense surahs

Combined narrative-onset density (idh + lammā + qālū per verse), surahs ≥10 verses:

| Surah | onset / verses | dens | idh | lammā | qālū | character |
|:--|:-:|:-:|:-:|:-:|:-:|:--|
| **Q12 Yūsuf** | 34/111 | **0.306** | 2 | 15 | 17 | continuous-narrative outlier — the single sustained story |
| Q8 al-Anfāl | 11/75 | 0.147 | 11 | 0 | 0 | Badr covenant-recall (*wa-idh* battle-memory) |
| Q2 al-Baqara | 37/286 | 0.129 | **24** | 4 | 9 | Banū-Isrāʾīl covenant-recall corpus-MAX idh |
| Q43 al-Zukhruf | 11/89 | 0.124 | 1 | 6 | 4 | prophet-cycle pericopes |
| Q11 Hūd | 15/123 | 0.122 | 0 | 7 | 8 | prophet-cycle (Nūḥ/Hūd/Ṣāliḥ/Lūṭ/Shuʿayb) |
| Q7 al-Aʿrāf | 22/206 | 0.107 | 6 | 9 | 7 | the great prophet-cycle |
| Q28 al-Qaṣaṣ | 9/88 | 0.102 | 0 | 8 | 1 | the Mūsā narrative ("al-Qaṣaṣ" = "The Stories") |
| Q15 al-Ḥijr | 10/99 | 0.101 | 2 | 1 | 7 | angel-guest / prophet pericopes |

**Raw-count leaders:** Q2 (37), Q12 (34), Q7 (22), Q26 al-Shuʿarāʾ (22), Q11 (15). Every one is a
**long narrative/legal surah** (all s ≤ 28). The qaṣaṣ skeleton is concentrated in the early mushaf.

- **Q2 al-Baqara** carries the corpus-MAX of verse-initial idh (24, of which 22 are *wa-idh*) — the
  Banū-Isrāʾīl + Ibrāhīm **covenant-recall** litany (*wa-idh akhadhnā mīthāqakum*, *wa-idh qulnā*,
  *wa-idh najjaynākum*). This is precisely the Medinan covenant-recall register the pre-reg locked.
- **Q12 Yūsuf** is the density-extreme (0.306): as the Quran's one sustained continuous narrative
  it is built of dialogue (qālū 17) and event-beats (lammā 15) rather than recall-idh — the
  signature of a *running story* vs a *recall litany*.

## 4. Maximal narrative-onset runs (the episode-boundary cascades)

| Family | max run | coordinates | content |
|:--|:-:|:--|:--|
| **qālū** | **5** | **Q12:71-75** | the Yūsuf-cup dialogue — five consecutive *qālū* turns (corpus-extreme dialogue cascade) |
| idh | **4** | **Q2:124-127** | the Ibrāhīm covenant — four consecutive *wa-idh* (ابتلى / جعلنا البيت / قال إبراهيم / يرفع القواعد) |
| qālū | 4 | Q21:59-62 | the idol-smashing interrogation of Ibrāhīm |
| lammā | 3 | Q6:76-78, Q12:68-70 | star/moon/sun argument; Yūsuf brothers' entry |
| idh | 3 | Q2:49-51, Q2:53-55, Q5:110-112, Q8:42-44 | Exodus-recall, Sinai-recall, ʿĪsā-favors, Badr |

These runs are the **pericope-boundary skeleton**: a *wa-idh* tetrad opens four successive recall
units (Q2:124-127), and a *qālū* pentad sustains a single dialogue scene (Q12:71-75). All verified
against `quran-text/quran-no-tashkeel.json`.

## 5. The idh ≠ idhā register split (genre-specificity, MW-6)

The built-in instrument-control is idhā itself. H-NEW-2250 found idhā concentrating at s≥78
(juzʾ-30) at density 0.0532 vs 0.0205. Here idh concentrates at the OPPOSITE pole:

- **idh secondary lens** (s≤78 vs s>78): dens 0.0201 vs 0.0057, Δ=+0.0144, two-sided p=0.0268.
- Of 118 verse-initial idh, **110 are in s≤50** and only **8 in s>50** — and those 8 are precisely
  the surahs carrying embedded narrative recall: Q51:25 (*ḍayf Ibrāhīm*, "the guests"), Q53:16
  (al-Najm, *idh yaghshā al-sidrata*), Q61:5+61:6 (*wa-idh qāla Mūsā* / *wa-idh qāla ʿĪsā*),
  Q66:3 (*wa-idh asarra al-Nabī*), Q79:16 (*idh nādāhu rabbuhu* — Mūsā at the sacred valley),
  Q85:6 (the trench-people *idh hum ʿalayhā quʿūd*), Q91:12 (Thamūd *idh inbaʿatha ashqāhā*).
  Even the leakage is qaṣaṣ (all 8 verified against `quran-text/quran-no-tashkeel.json`).

**Two homographic time-adverbs, two opposite mushaf-registers**, separable only by QAC
lemma-disambiguation: idh (إِذْ) = past-recall *qaṣaṣ* of the long head; idhā (إِذَا) =
eschatological conditional of the short tail. This is a new corpus-structural pillar — the
narrative/eschatological register split is encoded at the **single-particle** grain.

## 6. Classical anchoring

- **al-Suyūṭī**, *al-Itqān fī ʿulūm al-Qurʾān* (English transl., PDF on disk
  `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`): treats the
  *qaṣaṣ* of the Quran as a distinct genre — "the stories relating to Noah's people as well as
  those of the ʿĀd, the Thamūd, the building of the Kaʿbah." Ibn Abī al-Iṣbaʿ (cited there): "all
  the narratives of the Qurʾān appear … a single story … appears in multiple forms." The
  *wa-idh* / *qālū* skeleton is the grammatical realization of that genre, and this census shows
  it lives — quantitatively — in the long surahs al-Suyūṭī's chronology marks as the narrative
  body.
- **al-Zarkashī**, *al-Burhān fī ʿulūm al-Qurʾān* (PDF on disk): the *mufaṣṣal* classification and
  makkī/madanī register-split underwrite the s≤50 (narrative head) vs s>50 (mufaṣṣal tail)
  contrast. The empirical density-flip confirms the register boundary at the particle level.
- **al-Zamakhsharī / al-Rāzī** *taʿdīd* (serial enumeration) — the *wa-idh… wa-idh…* tetrad of
  Q2:124-127 is the recall-analogue of the *idhā… idhā…* eschatological taʿdīd of Q81 (H-NEW-2250).

## 7. Relation to prior findings

- **H-NEW-2250** (§10.88): the eschatological idhā cascade (juzʾ-30). H-NEW-2520 is its directional
  complement — the same generator-logic applied to the recall-idh / lammā / qālū families yields
  the OPPOSITE concentration. Together they establish a **register-dichotomy law**.
- **H-NEW-2260** (§10.89, prophet-cycle pericopes): the Nūḥ/Mūsā/Ibrāhīm episodes that cohere are
  bounded by exactly these onset markers; Q7/Q11/Q26/Q28 (the prophet-cycle surahs) are among the
  most onset-dense here.
- **cross-finding-025/026** (pericope structure, scale-of-aggregation): the onset markers are the
  *boundary-marking* skeleton of the pericope grain — the verse-head device, not the verse-block
  content; consistent with the scale-ladder.
- **H-NEW-590 / UAS**: Q2, Q12 (continuous-narrative outlier), Q9 — the narrative-onset-dense
  surahs overlap the high-outlier / high-UAS architectural anchors.

## 8. Honest limits

- The density test compares two coarse bands (s≤50 vs s>50); it does not model the within-band
  gradient. A finer per-surah regression is left to follow-up (the per-surah counts are in the
  JSON).
- *qālū* (qwl 3MP PERF) excludes singular *qāla* "he said" (531 tokens) and *qul* imperatives —
  by design (dialogue-onset = plural reported speech). The broader qāla speech-frame would be a
  separate, larger census.
- The s>50 idh leakage (8 tokens) is small-N; the qaṣaṣ-character of each was inspected
  individually (§5), not formally tested.
- This is a register/distribution finding, not a claim that onset markers EXHAUSTIVELY bound
  pericopes; they are a high-precision subset of episode boundaries.

## 9. Verdict

**CONFIRMED-DIRECTED (3/3 families).** The pre-registered direction — narrative-onset markers
concentrate in the long narrative/legal surahs (s≤50), the inverse of the idhā juzʾ-30 cascade —
holds for idh, lammā, and qālū, each at p=0.00010 under both seeds, all passing Bonferroni-3.
No pre-commit reversal. The GENERATOR census (inventory + per-surah map + maximal runs) is
delivered in `csv/h-new-2520.json`.

Files: `prereg-h-new-2520-pericope-onset.md`, `scripts/h-new-2520.py`, `csv/h-new-2520.json`,
`h-new-2520-pericope-onset.md`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
