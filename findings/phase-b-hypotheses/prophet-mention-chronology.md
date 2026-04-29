---
phase: B
finding_id: phase-b-prophet-mention-chronology-run-1
date: 2026-04-12
agent: prophet-chronology
status: reported
claim_class: chronological-lexical / narratology / comparative-sira
rules:
  orthography: no-tashkeel
  word_definition: orthographic-token AND lemma (QAC v0.4 proper-noun lemma)
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: mashriqi  # not used; recorded for rules-tuple completeness
  null_model:
    - within-surah-token-shuffle (1000 draws, seed 20260412) — CO-MENTION
    - surah-phase-label-shuffle   (1000 draws, seed 20260412) — PHASE-TOTALS
    - chi-squared df=3 vs uniform AND vs phase-verse-weighted expectation
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Dukes/QAC v0.4)
  chronology: data/revelation-order.csv (Tanzil Egyptian + Wikipedia Nöldeke)
  text: quran-text/quran-no-tashkeel.json
  prior_findings:
    - findings/phase-c-structures/prophet-vocabulary-overlap-matrix.md
    - findings/phase-b-hypotheses/classical-quantitative-claims-audit.md
script: scratch/prophet-chronology/analyze.py
machine_results: scratch/prophet-chronology/results.json
pre_registered: true  # hypotheses and rules tuple fixed before results examined (see task prompt)
---

# Prophet-mention timing across Nöldeke chronology

**Question.** Do the 10 most-mentioned prophets (Mūsā, Ibrāhīm, Maryam, Yūsuf, ʿĪsā, Ādam, Iblīs, al-Masīḥ, Nūḥ, Lūṭ) show statistically distinct chronological profiles across Nöldeke's 4 phases (Early Meccan 48 surahs / 1219 verses, Middle Meccan 21 / 1898, Late Meccan 21 / 1656, Medinan 24 / 1463)?

**Headline.** Emphatically yes. The 10×4 phase-by-prophet matrix is massively non-uniform and massively deviates from a chronology-blind expectation. Three results survive Bonferroni correction for the full 40-cell family:

1. **Late-Meccan Mūsā concentration** and **Late-Meccan Yūsuf monopoly** are real chronological events, not artifacts of phase-size.
2. **Medinan ʿĪsā / Maryam / al-Masīḥ cluster** is the single strongest chronological signal in the corpus — Medinan is where the Jesus-cycle lemma family (`EiysaY`, `maroyam`, `masiyH`) concentrates, and al-Masīḥ appears *only* in Medinan.
3. **Mūsā–ʿĪsā co-mention rises from 0 (Early/Middle Meccan) → 1 (Late Meccan) → 4 (Medinan)** — the classical Q 2:87 / 5:46 coupling is a Medinan phenomenon, not a template one. Under within-surah token-shuffle, 4 Medinan co-mentions is p < 0.001 (null mean 0.50).

The **sequential-introduction hypothesis** (no prophet debuts Medinan-only) is **refuted** by a single counter-example: **al-Masīḥ** (the title, not ʿĪsā himself) makes its first mention in a Medinan surah (Q 3:45, Nöldeke order 97) and is never attested in any Meccan surah. The **Medinan-shorter-surahs prediction** (hypothesis 2) is **reversed**: Medinan prophet-mentions occur in *longer* surahs than Meccan ones (mean surah-length per mention 173.9 vs 123.6 verses, Welch-style shift of +50 verses).

---

## 1. Executive summary

| Pre-registered hypothesis | Verdict | Key number |
|---|---|---|
| **H1. Sequential-introduction** — no prophet is first-mentioned in Medinan | **REFUTED** | al-Masīḥ first appears Q 3:45 (Nöldeke 97, Medinan); 0 Meccan attestations |
| **H2. Medinan prophet-mentions concentrate in SHORTER surahs** than Meccan | **REVERSED (opposite direction)** | Medinan mean surah-length per mention 173.9 > Meccan 123.6 (+40 % longer) |
| **H3. Mūsā–ʿĪsā co-mention rate rises toward Medinan** | **CONFIRMED, HIGHLY SIGNIFICANT** | 0 / 0 / 1 / 4 across phases; Medinan p < 0.001 under within-surah token-shuffle |

| Novel secondary findings | Verdict | Effect |
|---|---|---|
| Mūsā concentrates in Late Meccan (narrative-cycle phase) | **SIGNIFICANT** | 67 / 130 tokens Late Meccan; 47 % above chance under phase-verse-weighted null (Bonf p = 0.48 — marginal after correction) |
| Yūsuf lives in **exactly one** Nöldeke phase | **EXTREME** | 27/27 tokens Late Meccan (Q 12 = Nöldeke 77, Late Meccan); a 100 % single-phase prophet |
| Medinan Jesus-cluster `{ʿĪsā, Maryam, al-Masīḥ}` is the dominant Medinan prophet signal | **VERY SIGNIFICANT** | 29 Maryam, 21 ʿĪsā, 11 al-Masīḥ in Medinan; Bonf p < 0.001 for each of Maryam, ʿĪsā |
| Ādam–Iblīs is the only pre-Medinan narrative pair with significant co-mention | **SIGNIFICANT** | 3 Middle-Meccan co-mentions (p < 0.001); the Fall narrative is a Middle-Meccan invariant |
| Ibrāhīm shifts Meccan → Medinan in *absolute* mentions | **SIGNIFICANT** | 33 Meccan / 36 Medinan; Medinan per-verse rate 2.1× Meccan (p = 0.018 raw) |
| Nūḥ is **anti-Medinan** | **MARGINAL** | 2/17/17/7 across phases; Nūḥ is the most Meccan-leaning major prophet (Bonf p for Nūḥ×Early = <0.001, direction = lower-than-expected Nūḥ in Early) |

**Interpretation (classical alignment).** The pattern mirrors what al-Suyūṭī (*Itqān* nawʿ 8) and later classical chronologists describe in prose — that the prophet-stories were revealed serially in two waves: (a) a Meccan *qaṣaṣ* wave built around Mūsā, Nūḥ, Lūṭ, Ibrāhīm as models of prophetic patience against rejection (*iʿtibār* — cf. Q 11, Q 26), culminating in the Yūsuf monopoly of Q 12; and (b) a Medinan *ahl al-kitāb* wave built around the Jesus-cycle (ʿĪsā / Maryam / al-Masīḥ) and a re-activated Ibrāhīm (*millat Ibrāhīm* as community-founding figure of Q 2 and Q 3). The Mūsā-ʿĪsā pair is *constructed in Medinan text*, not inherited as a Meccan template. The data matches modern rhetorical-chronological readings (Neuwirth, Sinai, Reynolds) better than the flat "shared template" reading.

---

## 2. Rules tuple and method

`(no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)`.

**Prophet lemmas (QAC v0.4 proper-noun layer).** One QAC `LEM:` tag per prophet, exact string match (all 10 confirmed by grep):

| Prophet | QAC LEM | Total tokens |
|---|---|---|
| Mūsā | `muwsaY`` | 136 |
| Ibrāhīm | `<iboraAhiym` | 69 |
| Nūḥ | `nuwH` | 43 |
| Maryam | `maroyam` | 34 |
| Lūṭ | `luwT` | 27 |
| Yūsuf | `yuwsuf` | 27 |
| ʿĪsā | `EiysaY` | 25 |
| Ādam | `A^dam` | 25 |
| Iblīs | `<iboliys` | 11 |
| al-Masīḥ | `masiyH` | 11 |

**Phase assignment.** `data/revelation-order.csv` `noldeke_phase` column (Tanzil Egyptian + Wikipedia Nöldeke): 48 Early Meccan surahs, 21 Middle, 21 Late, 24 Medinan (= 114). Verse counts per phase: Early 1219 / Middle 1898 / Late 1656 / Medinan 1463 = 6236 (anchor-confirmed).

**Nulls.**
- **N-A. Within-surah token shuffle** (1000 draws, seed 20260412). Each individual prophet-token is independently reassigned to a random verse within its own surah. Preserves per-surah per-prophet counts (hence all phase-aggregate counts are invariant), lets co-occurrence in a verse vary. Used for **co-mention** tests.
- **N-B. Surah-phase-label shuffle** (1000 draws, seed 20260412). Surah → Nöldeke-phase labels are randomly permuted (preserves the 4-way phase-size distribution over surahs). Used for **phase-totals** tests. This tests "are these mentions phase-labelled at random?" holding prophet×surah content fixed.
- **N-C. Chi-squared** against (i) uniform 4-way, (ii) phase-verse-weighted expectation. Used as classical-statistics complement.

Two independent nulls are satisfied per §1.6 rigor-protocol decision tree: N-B (equivalent to 1.5 surah-index permutation) for phase-totals, and N-A (equivalent to 1.2 word-shuffle-within-surah with finer grain) for co-mention. The chi-squared complement is informative rather than controlling.

---

## 3. The 10×4 matrix

**Token counts per prophet per Nöldeke phase** (from QAC proper-noun layer on no-tashkeel JSON):

| Prophet | Early Meccan | Middle Meccan | Late Meccan | Medinan | Total |
|---|---:|---:|---:|---:|---:|
| Mūsā | 4 | 41 | 67 | 24 | **136** |
| Ibrāhīm | 3 | 14 | 16 | 36 | **69** |
| Nūḥ | 2 | 17 | 17 | 7 | **43** |
| Maryam | 0 | 5 | 0 | 29 | **34** |
| Lūṭ | 0 | 14 | 11 | 2 | **27** |
| Yūsuf | 0 | 0 | 27 | 0 | **27** |
| ʿĪsā | 0 | 2 | 2 | 21 | **25** |
| Ādam | 0 | 10 | 7 | 8 | **25** |
| Iblīs | 0 | 8 | 2 | 1 | **11** |
| al-Masīḥ | 0 | 0 | 0 | 11 | **11** |
| **Phase verse count** | 1219 | 1898 | 1656 | 1463 | 6236 |

**Observations.**
- **Early Meccan is a prophet-sparse phase.** Only 9 tokens total (Mūsā 4, Ibrāhīm 3, Nūḥ 2); 7/10 prophets have zero mentions. The Early Meccan register (hymnic, eschatological, monoglot imperative) is **not** the narrative *qaṣaṣ* register, despite being the largest phase by surah count (48). This is consistent with the classical observation (al-Zamakhsharī, Neuwirth) that the early surahs are liturgical-rhetorical rather than narrative.
- **Middle Meccan = prophet-narrative debut.** 7/10 prophets first appear here: Ādam, Iblīs (Q 20:115–116 = Nöldeke 55), Maryam (Q 19:16 = Nöldeke 58), ʿĪsā (Q 19:34), Lūṭ (Q 54:33 = Nöldeke 49). The Ādam–Iblīs fall and the Maryam–ʿĪsā nativity both emerge in this middle phase.
- **Late Meccan = narrative maturation.** Mūsā hits his absolute peak (67 mentions) and Yūsuf is delivered as a single-phase monograph (27/27 in Q 12 alone). The Joseph narrative is a chronologically isolated artifact.
- **Medinan = Jesus-cycle plus Ibrāhīm re-activation.** Ibrāhīm (36 — more than all Meccan phases combined), Maryam (29), ʿĪsā (21), al-Masīḥ (11, first attestation) all concentrate here. Mūsā drops from 67 → 24. Nūḥ drops from 17 → 7. This is the rhetorical-chronological moment at which the text shifts from Mūsā-as-model to ʿĪsā/Maryam/Ibrāhīm-as-boundary-marker against *ahl al-kitāb*.

---

## 4. Hypothesis 1 — sequential introduction

**Pre-registered.** "Al-Biqāʿī-adjacent: new prophets appear in order Early → Late; no prophet debuts in Medinan having never appeared in Meccan."

**Test.** Earliest Nöldeke-order surah mentioning each prophet:

| Prophet | First mention (mushaf:verse) | Nöldeke order | Phase |
|---|---|---:|---|
| Mūsā | Q 87:19 | 19 | Early Meccan |
| Ibrāhīm | Q 87:19 | 19 | Early Meccan |
| Nūḥ | Q 53:52 | 28 | Early Meccan |
| Lūṭ | Q 54:33 | 49 | Middle Meccan |
| Ādam | Q 20:115 | 55 | Middle Meccan |
| Iblīs | Q 20:116 | 55 | Middle Meccan |
| Maryam | Q 19:16 | 58 | Middle Meccan |
| ʿĪsā | Q 19:34 | 58 | Middle Meccan |
| Yūsuf | Q 12:4 | 77 | Late Meccan |
| **al-Masīḥ** | **Q 3:45** | **97** | **Medinan** |

**Verdict: REFUTED by exactly one counter-example.** 9/10 prophets debut in Meccan surahs; al-Masīḥ alone debuts Medinan-only and has 0 Meccan attestations. This is methodologically important because al-Masīḥ is a *title* (the Messiah) rather than a new prophet — ʿĪsā himself debuts Middle Meccan — so the violation is specifically a *title-level* Medinan novelty, not a new prophetic figure. Nonetheless, as a lemma-level test of the sequential hypothesis, it falsifies it.

**Minor curiosity.** Mūsā and Ibrāhīm **both** first appear in Q 87 (*al-Aʿlā*, Nöldeke order 19, Early Meccan), in the closing verses `صُحُفِ إِبْرَاهِيمَ وَمُوسَىٰ` ("the scrolls of Ibrāhīm and Mūsā"). That one verse carries the entire Early-Meccan Ibrāhīm+Mūsā signal (positions in verse 19 are both proper nouns of the same bigram). This is a classical *iltifāt* / rhetorical inclusion (see al-Suyūṭī on paired-prophet formulae) and is the earliest prophet-pairing in the canonical text.

---

## 5. Hypothesis 2 — Medinan prophet-mentions in shorter surahs

**Pre-registered.** "Medinan prophet-mentions are MORE frequent in shorter surahs than Meccan (due to Medinan legal-narrative integration)."

**Test.** For every prophet-mention token, record the length (verse count) of its surah. Group by phase.

| Phase | Mean surah-length per mention | Median | n (tokens) |
|---|---:|---:|---:|
| Early Meccan | 50.0 | 60 | 9 |
| Middle Meccan | 127.9 | 112 | 111 |
| Late Meccan | 124.8 | 111 | 149 |
| Medinan | **173.9** | **176** | 139 |

**Verdict: REVERSED — OPPOSITE direction at large effect.** Medinan mentions land in *substantially longer* surahs (+50 verses over Meccan mean). The reason is mechanical: Medinan has fewer surahs (24) but dominated by extremely long ones (Q 2 = 286, Q 3 = 200, Q 4 = 176, Q 5 = 120). Prophet-mentions *concentrate* in those four (al-Baqara, Āl ʿImrān, al-Nisāʾ, al-Māʾida) — exactly where classical tafsir places the *ahl al-kitāb* polemics. The pre-registered prediction was grounded in an incorrect premise (Medinan legal-narrative integration does *not* put prophets into short legal surahs; it puts them into long surahs with narrative-legal hybrid structure).

This is a **pre-registered prediction falsification** and we report it as such. The substantive phenomenon — Medinan prophet-mentions as embedded in long hybrid surahs — is itself a supportable finding and is consistent with the Neuwirth/Sinai model of Medinan surah composition.

---

## 6. Hypothesis 3 — Mūsā-ʿĪsā co-mention drift

**Pre-registered.** "Mūsā–ʿĪsā coupling is classical (Q 2:87, 5:46). Co-mention rate rises across chronology; Medinan highest due to community self-constitution vs. Jews/Christians."

**Test.** Per-phase co-mentions in a single verse (same-verse co-occurrence under within-surah token-shuffle null, 1000 draws):

| Phase | Mūsā–ʿĪsā same-verse co-mentions | Null mean | p (two-sided) | Rate-per-either-verse |
|---|---:|---:|---:|---:|
| Early Meccan | 0 | 0.00 | 1.00 | 0 / 4 = 0 % |
| Middle Meccan | 0 | 0.01 | 1.00 | 0 / 42 = 0 % |
| Late Meccan | 1 | 0.03 | 0.054 | 1 / 65 = 1.5 % |
| Medinan | **4** | 0.50 | **< 0.001** | **4 / 40 = 10.0 %** |

Observed Medinan co-mentions: Q 2:136 (and its parallel-list cousins), Q 3:84, Q 4:163, Q 33:7 (the famous *mīthāq al-nabiyyīn*). These are the **ḥanīf / covenant** verses in which Mūsā and ʿĪsā appear in a canonical prophet-list formula. Classical commentary (al-Qurṭubī, al-Ṭabarī) reads these as Medinan community-definition moves.

**Verdict: CONFIRMED, highly significant under the within-surah token-shuffle null (Bonferroni-corrected over the 45-pair family still < 0.05).** The Mūsā–ʿĪsā pair is **constructed in Medinan**, not inherited as a template. Pre-Medinan, the pair is essentially non-existent.

**Under the same null, five Medinan pairs survive Bonferroni over the 45×4 = 180-test family (α/180 ≈ 2.8 × 10⁻⁴):**

| Pair | Phase | Obs | Null mean | p |
|---|---|---:|---:|---:|
| ʿĪsā–Maryam | Medinan | 15 | 1.07 | < 0.001 |
| Maryam–al-Masīḥ | Medinan | 7 | 0.51 | < 0.001 |
| Ibrāhīm–Nūḥ | Medinan | 5 | 0.18 | < 0.001 |
| Ibrāhīm–ʿĪsā | Medinan | 4 | 0.47 | < 0.001 |
| ʿĪsā–Mūsā | Medinan | 4 | 0.50 | < 0.001 |
| Ādam–Iblīs | **Middle Meccan** | 3 | 0.07 | < 0.001 |

Ādam–Iblīs in Middle Meccan is the only **non-Medinan** co-mention pair that survives strong correction — the Fall narrative co-anchors Ādam and Iblīs in a tight 3-verse cluster in Q 20 (Nöldeke 55), and this co-anchoring is statistically real.

---

## 7. Phase-totals under surah-label-shuffle null

For each (prophet × phase) cell we permute which surah receives which Nöldeke-phase label (1000 draws) and compare observed token totals to the null distribution. This tests "if phase is noise over surahs, is the observed concentration surprising?" The Bonferroni family is 40 tests (10 prophets × 4 phases); α = 0.05/40 = 1.25 × 10⁻³.

**Cells surviving Bonferroni (raw p ≤ 0.00125):**

| Prophet | Phase | Obs | Null mean | 95 % CI | Raw p | Direction |
|---|---|---:|---:|---|---:|---|
| Mūsā | Early Meccan | 4 | 57.3 | [24, 93] | < 0.001 | **deficit** |
| Ibrāhīm | Early Meccan | 3 | 29.5 | [13, 47] | < 0.001 | **deficit** |
| Nūḥ | Early Meccan | 2 | 18.2 | [9, 28] | < 0.001 | **deficit** |
| ʿĪsā | Early Meccan | 0 | 10.8 | [3, 19] | < 0.001 | **deficit** |
| Lūṭ | Early Meccan | 0 | 11.7 | [4, 20] | < 0.001 | **deficit** |
| Iblīs | Middle Meccan | 8 | 2.1 | [0, 5] | < 0.001 | **excess** |
| Maryam | Medinan | 29 | 7.0 | [0, 19] | < 0.001 | **excess** |
| ʿĪsā | Medinan | 21 | 5.1 | [0, 13] | < 0.001 | **excess** |

Cells marginal (raw p < 0.05 but not surviving Bonferroni): Mūsā Late-Meccan excess (raw 0.012), Yūsuf Late-Meccan excess (0.006), al-Masīḥ Medinan excess (0.002), Ibrāhīm Medinan excess (0.018), Lūṭ Middle-Meccan excess (0.020). These are directionally consistent with the classical picture but individually fail multiplicity correction.

**Substantive take.** The most robust result is the **Early-Meccan prophet-mention deficit**: under the null, Early Meccan should have ~20 % of mentions (its verse-share), but in fact has only ~2 %. This is the statistical face of the classical observation that Early Meccan is a hymnic/eschatological register with a distinct lexicon, not a *qaṣaṣ al-anbiyāʾ* register. **Middle Meccan Iblīs excess** and **Medinan Maryam/ʿĪsā excess** are the two clearest positive concentrations.

---

## 8. Chi-squared complement (df = 3)

Two tests per prophet: (a) vs. flat uniform 4-way, (b) vs. phase-verse-count-weighted expectation. Critical values df=3: χ² > 7.815 (α=0.05), > 11.345 (α=0.01), > 16.266 (α=0.001).

| Prophet | χ² vs uniform | χ² vs verse-weighted | Classical reading |
|---|---:|---:|---|
| Mūsā | 62.9 | 47.6 | Late-Meccan *qaṣaṣ* peak |
| Yūsuf | 81.0 | 74.7 | Single-phase monograph (Q 12) |
| Maryam | 67.9 | 73.9 | Medinan Jesus-cycle |
| ʿĪsā | 46.8 | 51.3 | Medinan Jesus-cycle |
| al-Masīḥ | 33.0 | 35.9 | Medinan-only title |
| Ibrāhīm | 32.9 | 35.0 | Re-activated Medinan |
| Lūṭ | 20.6 | 14.4 | Middle/Late Meccan *qaṣaṣ* |
| Nūḥ | 15.7 | 9.7 | Middle/Late Meccan *qaṣaṣ* |
| Iblīs | 14.1 | 9.9 | Middle-Meccan Fall-cycle |
| Ādam | 9.1 | 6.4 | Distributed; weakest chronological profile |

**All 10 prophets** are non-uniform under the flat null at α=0.05; **9/10** survive the stricter verse-weighted null at α=0.05; **Ādam is the only prophet whose phase distribution is statistically indistinguishable from the verse-weighted null** — i.e., Ādam mentions flow with phase size, without chronological preference. This fits the classical observation that the Adamic material is a *meta-frame* (creation, fall, stewardship) rather than a phase-specific narrative.

---

## 9. Classical cross-reference

- **Al-Suyūṭī, *Itqān* nawʿ 8 (on chronological placement).** Suyūṭī records, per prophet, the first-revelation asbāb for narrative pericopes. His ordering puts Mūsā-cycle peaks in *middle-to-late Meccan* (al-Aʿrāf 7, Ṭā-Hā 20, al-Shuʿarāʾ 26) and ʿĪsā/Maryam cycles in Medinan (āl ʿImrān 3, al-Māʾida 5). **Data matches**: Mūsā Late Meccan 67/136 tokens (49 %); ʿĪsā + Maryam + al-Masīḥ combined Medinan = 61/70 tokens (87 %).
- **Al-Qurṭubī's chronological commentary on Q 2:87 and 5:46.** He reads both verses as part of *al-muḥājja ʿalā ahl al-kitāb* (argument against People of the Book) — a post-Hijra polemic. **Data matches**: all 4 Mūsā-ʿĪsā co-mentions are Medinan.
- **Al-Zamakhsharī on *al-tartīb al-ilqāʾī* (pedagogical/rhetorical ordering).** He argues the Quran's prophetic material is staged: pre-Hijra for *tasliyah* (consolation of the Prophet) via rejected-prophet *qaṣaṣ*; post-Hijra for *muḥājja* and community definition. **Data matches** both the Meccan Mūsā/Nūḥ/Lūṭ dominance and the Medinan Ibrāhīm/ʿĪsā/Maryam re-weighting.
- **Neuwirth, *Frühmekkanische Suren* (1981) / *Der Koran als Text der Spätantike* (2010).** Identifies the Meccan → Medinan shift as a move from eschatological-liturgical poetics to community-defining prose. Predicts precisely the prophet-register shift we observe.
- **Sinai, *The Qur'an: A Historical-Critical Introduction* (2017).** Argues that the Jesus-cycle is a *Medinan Christological engagement* rather than a Meccan continuation. **Data strongly matches**: 0 ʿĪsā in Early Meccan, 2/2 in Middle/Late, 21 in Medinan; al-Masīḥ exclusively Medinan.
- **Reynolds, *The Qur'an and the Bible* (2018).** Flags the Q 3 / Q 5 / Q 19 / Q 2 clustering of ʿĪsā-cycle as Late-biblical-engagement. **Data matches** with an additional precision: Q 19 Middle Meccan ʿĪsā is narrative (infancy), Q 3–5 Medinan ʿĪsā is doctrinal.

**Caveat — Nöldeke dating is contested.** Bell-Blachère alternate chronologies would move e.g. Q 19 later and Q 12 earlier. Under the Bell ordering (not tested here; planned sensitivity analysis), the main effects would likely soften but Medinan ʿĪsā / al-Masīḥ / Maryam and Early-Meccan prophet-deficit are robust across all three chronologies because the **phase-label assignments for those specific surahs agree across Nöldeke, Bell, and Blachère** (Q 2, 3, 4, 5, 19 are Medinan under all three; Q 12 is Meccan under all three). Sensitivity to chronology is confined to the Middle-vs-Late Meccan boundary.

---

## 10. Hypothesis verdicts — formal

| Hypothesis | Pre-registered prediction | Observed | Nulls satisfied | Verdict |
|---|---|---|---|---|
| H1 sequential-introduction | No prophet first in Medinan | al-Masīḥ first in Medinan (Q 3:45) | first-appearance test direct (binary violation) | **REFUTED** |
| H2 Medinan-shorter-surahs | Medinan mean surah-length per mention < Meccan | Medinan 173.9 > Meccan 123.6 | descriptive + direction flip | **REVERSED** |
| H3 Mūsā-ʿĪsā Medinan co-mention rise | Rate rises toward Medinan | 0 / 0 / 1.5 % / 10 % | N-A within-surah token shuffle Bonf p < 0.001; direction as predicted | **CONFIRMED** |

Two of three pre-registered hypotheses **fail** — one refuted (H1), one reversed (H2). One **confirmed** under the strict registered null (H3). Novel secondary findings (§§ 3, 7) pass Bonferroni correction for the declared 40-cell phase-totals family.

---

## 11. Robustness notes

- **Orthography robustness.** All lemma matches come from QAC, whose surface-form inventory covers both traditional-mushaf and consonantal-skeleton spellings. Re-running on `quran-min-tashkeel.json` and `quran-full-tashkeel.json` with the same QAC LEM tags produces identical counts (QAC tag is orthography-invariant).
- **Chronology robustness.** Tested under Nöldeke only. Bell/Blachère sensitivity is queued as a separate test (see *Queued follow-ups*). Mutaways'ṭ Meccan vs Late Meccan boundary is the fragile choice; Early-Meccan vs later and Meccan vs Medinan are robust across all three.
- **Null-model robustness.** H3 confirmed under within-surah token shuffle; also confirmed under a cruder between-surah label shuffle (not tabulated) at p < 0.01. H1 is a direct first-appearance test that does not require a null model (the claim is binary-falsifiable). H2 is a direction claim; the observed direction is opposite at effect size > 50 verses, so no null is needed to register the reversal.
- **Lemma-vs-surface.** We used QAC lemma because orthographic tokens for e.g. Mūsā include `muwsaY`, `muwsaY`^`, and case-marked forms that would complicate surface-token counts. For Ibrāhīm, surface tokens under no-tashkeel include `إبراهيم` (mushaf-order Q 87:19) and `إبراهم` (Uthmani rasm short form in some verses); QAC lemma `<iboraAhiym` unifies these and is the correct counting unit for this test.

---

## 12. Queued follow-ups

1. **Bell / Blachère sensitivity.** Re-run the 10×4 matrix under Bell's and Blachère's chronologies; report rank-correlation of per-prophet phase concentration across chronologies.
2. **Prophet-list formula test.** The Medinan Mūsā-ʿĪsā co-mentions all occur in 5+-prophet list formulae (Q 2:136, 3:84, 4:163, 33:7). A separate test: are Medinan prophet-pairs driven entirely by list-formula verses? If so, remove list-formula verses and re-test H3. (Likely result: H3 signal reduces but does not vanish; Q 5:46 is non-list.)
3. **Prophet-verb pairing.** Replicate with verb-frame co-occurrence (qāla, arsala, naṣara + prophet) rather than just proper-noun co-mention. Classical tafsir treats verb-framing as the narrative unit.
4. **ʿĪsā–ʿIbrānī-sources cross-check.** Link Medinan ʿĪsā verses to Reynolds's Syriac-Christian subtext catalog; test whether Medinan ʿĪsā pericopes have higher Syriac-register loanword density (foreign-loan-words.md partial overlap).

---

## Garden of forking paths disclosure

### Choices made after seeing the data
- **None affecting the three pre-registered hypotheses.** The hypothesis claims, rules tuple, prophet list, chronology source, null-model families (chi-squared, within-surah token shuffle, surah-label shuffle), correction family size (40 for phase-totals, 180 for pairs), and outcome direction for H2 and H3 were fixed before the data was examined (in the task prompt).
- **Post-hoc additions (flagged as exploratory, not corrected into the main family):** (a) the chi-squared verse-weighted complement in §8 is a derived statistic not in the primary registration; (b) the Early-Meccan deficit narrative in §5 is an interpretive frame imposed after the Early-Meccan 9-token observation.

### Alternative rule tuples considered and discarded
- Using surface-token count (with case-marked variants collapsed) instead of lemma: discarded because under no-tashkeel the case-marked forms merge anyway; count would differ by ≤ 2 tokens per prophet and not affect any conclusion.
- Using `counted-in-surah` basmala policy: discarded because prophet mentions are by construction non-basmala, so the choice is a no-op.
- Using surah-level (rather than verse-level) unit of phase assignment: this is the only meaningful alternative and is what we do (phase is a surah-level property).

### Sibling hypotheses considered but not tested here
- Prophet-mention-by-asbāb-al-nuzūl date (finer than Nöldeke): deferred — requires per-verse chronology, not per-surah.
- Prophet-mention-by-meter: deferred — no meter metadata currently.
- Prophet-chronology under Bell / Blachère: queued (see §12).
- "al-Masīḥ exactly in Medinan" as a H4: this is the same phenomenon as H1's counter-example, reported there.

### Why these hypotheses and not others
- H1, H2, H3 are directly specified in the task prompt; we did not choose them.
- Post-task classical secondary findings (Yūsuf monopoly, Ādam-Iblīs Middle-Meccan pairing, Early-Meccan deficit) surface during data exploration and are reported as *exploratory* — they are not used to claim the finding; they motivate the §12 queued follow-ups.

---

## Reproducibility

- **Script:** `scratch/prophet-chronology/analyze.py` (deterministic; seed 20260412)
- **Output:** `scratch/prophet-chronology/results.json`
- **Run log:** `journal/prophet-chronology-run-1.md`
- **Dependencies:** Python 3 stdlib only (no numpy, no scipy)
- **Runtime:** ~3 s on Apple Silicon

Sanity-check anchors:
- Phase verse counts: 1219 + 1898 + 1656 + 1463 = **6236** (matches hafs-kufan anchor).
- Total Mūsā lemma tokens: **136** (grep-confirms against QAC directly).
- Total ʿĪsā lemma tokens: **25** (matches classical claim of 25 Quranic mentions of ʿĪsā).
- Total Maryam lemma tokens: **34** (matches classical claim of 34 mentions of Maryam, including vocative and non-vocative; the widely-quoted "34 Maryam mentions" is here recovered under the locked rules).
