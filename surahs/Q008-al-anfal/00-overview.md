---
surah: 8
surah_name_ar: الأنفال
surah_name_translit: al-Anfāl
surah_name_english: The Spoils (of War)
file_type: overview
date_last_updated: 2026-04-28
phase: B+
verdict: WAVE-E COMPLETE — 9-file template + JOURNAL written; H-NEW-890 Q8-Q9 unity FALSIFIED replicated at surah level; *anfāl* corpus-hapax cohesion established; Battle-of-Badr asbāb chain audited.
---

# Q 8 al-Anfāl — Overview

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 8 | canonical |
| Arabic name | الأنفال | canonical |
| Transliteration | al-Anfāl | canonical |
| English meaning | "The Spoils [of War]" | from opening word *al-anfāl* (booty / supererogatory gain) |
| Verse count | 75 | Hafs-Kufan, `data/hafs-verse-counts.tsv` |
| Position in mushaf | 8 | canonical |
| Type | Medinan | classical (al-Suyūṭī, *al-Itqān*, nawʿ 1, Medinan-list); revealed after Q 2 al-Baqara, post-Badr (2 AH/624 CE) |
| Position in revelation order (al-Suyūṭī chronology) | 88 of 114 | `data/revelation-order.csv` |
| Word count (no-tashkeel) | 1,320 | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel) | 5,465 | same |
| Bismala status | present (114-prefix default) | canonical |
| Opening | يسألونك عن الأنفال — "They ask you about the spoils-of-war" | direct legal-question form (rare) |

## 2. Classical names

- **al-Anfāl** (الأنفال) — "The Spoils [of War]" / supererogatory gains; from v.1.
- **Sūrat Badr** (سورة بدر) — "The Surah of Badr"; al-Bukhārī ḥadīth #3953 (Saʿīd b. Jubayr asked Ibn ʿAbbās about al-Anfāl, who replied: "It is *Sūrat Badr*"; cf. al-Suyūṭī, *al-Itqān*, nawʿ 17).
- The surah's classical identity is double-anchored: as the legal-apparatus of *anfāl* AND as the asbāb-narrative of Badr.

## 3. Opening formula

Q 8 opens with a direct **legal-question protocol**: *yasʾalūnaka ʿan al-anfāl* ("They ask you about the spoils"). This is one of approximately 15 corpus *yasʾalūnaka* legal-questions; structurally, the opening is **interrogative-law**, not muqaṭṭaʿāt or *al-ḥamd*. Compare Q 2 *yasʾalūnaka* sequences (vv.189, 215, 217, 219, 220, 222) — Q 8 is the only surah where the *yasʾalūnaka*-form constitutes the opening.

## 4. Length classification

- **al-sabʿ al-ṭiwāl debate**: classical lists differ on whether Q 8 is the seventh of the seven-long (the "Q 8+9 = one surah" tradition pairs them as the seventh; the "Q 8 alone" tradition assigns Q 9 separately — see al-Suyūṭī *al-Itqān* nawʿ 7 and §3 of `Q009-al-tawba/00-overview.md`).
- 75 verses, 1,320 words, 5,465 letters — substantial Medinan-ṭiwāl proper.

## 5. Rhyme structure

Final-letter distribution across 75 verses (computed from `quran-text/quran-min-tashkeel.json`):

| Rāwī | Count | Frac |
|:-:|:-:|:-:|
| **ن** (nūn) | 39 | 0.520 |
| م (mīm) | ~25 | ~0.33 |
| ر (rāʾ) | small | ~0.05 |
| (other) | small | balance |

- **Top final-letter fraction: 0.520** (per `findings/phase-b-hypotheses/csv/h-new-750.json`).
- **Rhyme entropy (Shannon, nats): 1.286** (z = +0.93, *high* — Medinan-ṭiwāl pattern).

## 6. Empirical architectural profile

See `01-empirical-profile.md`. Headline (locked from H-NEW JSONs):

- **UAS rank**: **22/114** (UAS = 1.036). Top quintile — structural-iʿjāz cell.
- **Outlier-strength Δ%ile**: **+9.81 pp** (window [5–11], `WEAK_OUTLIER`, p_greater=0.621).
- **iʿjāz signature**: sig_A = **−0.557** (rank 75/114, mid-low — Q 8 is NOT al-fawāṣil-tight); sig_B = +0.234 (rank 53/114, near-median).
- **Mean content distance**: 1.075 (z = +1.49 — content-distinctive).
- **Local cohesion**: 1.004 (z = −0.70 — slightly below median).
- **FR-roots top-3 nearest**: Q 3 (d=0.807), Q 22 (d=0.851), Q 2 (d=0.874). All Medinan-ṭiwāl or near-it.
- **d_FR(Q 8, Q 9) = 0.911** — rank **81/113** in adjacent-pair distribution (above-median dissimilarity). The Q 8+Q 9 unity claim of Ibn ʿAbbās/Ubayy b. Kaʿb is **FALSIFIED** by FR-distance (per [[h-new-890-numerical-reaudit|H-NEW-890]] T1).
- **Q 7 → Q 8 canonical-adjacency cost**: **0.212** (rank **10/113**, expensive — top decile of architectural seams). The mushaf pays a high TSP-cost transitioning from the ALMṢ-singleton long-Meccan Q 7 to the Medinan post-Hijra Q 8.
- **Q 8 → Q 9 cost**: 0.061 (rank 58/113, moderate-cheap — adjacency is permissive but the surahs are *content-distant*; cf. cross-finding-026 §13 cell typology).

**Architectural-type classification**: structural-distinct + content-distant; sits in cross-finding-026 §13 *outlier-anchor* cell (top-quintile UAS but sig_A negative — outlier-driven, not fawāṣil-driven).

## 7. Quick content structure

- vv. 1–4: legal verdict on *anfāl* (spoils-of-war) → divine-Messenger ownership; *al-muʾminūn ḥaqqan* definition.
- vv. 5–19: Badr-narrative onset; God's intervention; angel-host promise; *yawm al-furqān*.
- vv. 20–29: ethical commands (obey God+Messenger; ḥikma of obedience; do not betray covenant).
- vv. 30–40: Quraysh-plot recall (Hijra context); call to repent; pre-Badr theological framing.
- vv. 41–48: explicit Battle-of-Badr legal sequel — *yawm al-furqān* (v.41), 1/5 booty division (*khums*), patience-in-battle ethic.
- vv. 49–58: hypocrites and idolaters' Badr-day reactions; covenant-breaking warnings.
- vv. 59–66: war-time ratio commands (originally 1:10 endurance, then relaxed to 1:2 — naskh-trigger pair).
- vv. 67–71: prisoners-of-war legal apparatus; Badr-prisoners episode.
- vv. 72–75: walāʾ structure of muhājirūn / anṣār / non-emigrants — Medinan polity foundation.

## 8. Why this surah is structurally distinctive

Three signature facts:

1. **Lexical hapax-class**: the lemma *anfāl* (root nfl, "supererogatory gain / spoils") attests only **4 times** corpus-wide (per `data/morphology/root-index.json`): Q 8:1 (×2), Q 17:79, Q 21:72. **Q 8 holds 50% of all nfl-root attestations**; the surah is *literally named for a corpus-rare lemma*. Q 17:79 and Q 21:72 use *nāfila(tan)* in supererogatory-prayer/grandson senses — semantically distinct from Q 8's spoils-of-war sense. Q 8's *anfāl*-sense is therefore **2/2 = 100% surah-monopoly** of the spoils-sense.

2. **Asbāb-anchored**: the surah is the densest Quranic source for Battle-of-Badr legal-narrative. al-Bukhārī's *Kitāb al-Maghāzī* anchors over a dozen ḥadīth at this surah (ḥadīth #3950–4030 range, with Badr cluster around #3953, #3960, #3982 — see `04-hadith-corpus.md`).

3. **Architectural seam-marker**: Q 7 → Q 8 is rank **10/113** most-expensive canonical adjacency (the chronology break: late-Meccan ALMṢ-singleton Q 7 → post-Hijra Medinan Q 8). The mushaf places its highest-cost Meccan→Medinan transitions at content-driven seams, not at simple length-graded boundaries.

## 9. Cross-references

- [[h-new-590-outlier-spectrum|H-NEW-590]] — Q 8 Δ%ile = +9.81 pp WEAK_OUTLIER.
- [[h-new-720-canonical-adjacency-cost|H-NEW-720]] — Q 7→Q 8 rank 10/113; Q 8→Q 9 rank 58/113.
- [[h-new-750-per-surah-iʿjāz-signature|H-NEW-750]] — sig_A = −0.557 (rank 75/114).
- [[h-new-840-unified-architectural-score|H-NEW-840]] — UAS rank 22/114.
- [[h-new-890-numerical-reaudit|H-NEW-890]] — T1: Q 8+Q 9 unity FALSIFIED (rank 81/113).
- [[Q009-al-tawba/00-overview|Q 9 al-Tawba]] — sister-surah; basmala-asymmetry pair.
- [[Q002-al-baqara/00-overview|Q 2 al-Baqara]] — Q 8 FR-near (rank 3 nearest); thematic legal-Medinan kinship.
- [[cross-finding-026-iʿjāz-architecture|cross-finding-026]] — Q 8 placement in §13 4-cell typology.

## 10. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
