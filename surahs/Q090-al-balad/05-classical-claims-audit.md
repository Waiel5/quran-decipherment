---
surah: 90
surah_name_ar: البلد
surah_name_translit: al-Balad
file_type: classical-claims-audit
date_last_updated: 2026-05-30
phase: B+
verdict: 6 claims audited — 3 VINDICATED, 1 RULES-TUPLE-FRAGILE, 1 NOT-TESTABLE (exegetical), 1 VINDICATED-AS-STRUCTURAL
---

# Q 90 al-Balad — Classical Claims Audit

Each non-trivial classical claim is stated with citation, given a rules-tuple, tested against on-disk
data where testable, and verdicted. Default rules-tuple unless noted:
`(no-tashkeel, QAC-v0.4 STEM root-tokens, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

---

## Claim 1 — "Sūrat al-Balad is Meccan by agreement, and it is twenty verses."

**Source:** al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, on Q 90:1 ("سورة البلد مكية باتفاق . وهي عشرون آية")
— `spa5k-tafsir-api/ar-tafseer-al-qurtubi/90/1.json`.

**Test (verse count + type):** `data/hafs-verse-counts.tsv` line 90 → **20**;
`quran-text/quran-no-tashkeel.json` Q 90 `total_verses` = **20**, `type` = `meccan`;
`data/revelation-order.csv` → revelation #35, "Early Meccan."

**Verdict: VINDICATED.** Verse count (20) and Meccan type are exact matches across all on-disk artifacts.
The one classical dissent (al-Wāsiṭī: *al-balad* = Madina) al-Qurṭubī himself rejects ("wa-l-awwal aṣaḥḥ
li-anna al-sūra nazalat bi-Makka bi-l-ittifāq").

---

## Claim 2 — "v 4 (*la-qad khalaqnā al-insān fī kabad*) is the jawāb al-qasam of v 1."

**Source:** al-Ṭabarī, *Jāmiʿ al-bayān*, on Q 90:4 ("وهذا هو جواب القسم") — `ar-tafsir-al-tabari/90/4.json`;
al-Zamakhsharī, *al-Kashshāf* (line 69406: "alā tarā kayfa laqqā *lā uqsimu bi-hādhā al-balad* bi-qawlihi
*la-qad khalaqnā al-insān*").

**Test:** The H-NEW-2210 qasam GENERATOR (`csv/h-new-2210.json`) independently parses Q 90's cluster:
opening = *uqsimu* at 90:1; coordinated object *wālid* at 90:3; **jawāb marker = `la-(tawkīd)` at 90:4**,
qasam→jawāb distance = 3 verses. The morphology (`data/morphology/...`) confirms 90:4:1 = `la(EMPH) +
qad(CERT)` — the canonical lām-al-tawkīd apodosis.

**Verdict: VINDICATED (structurally).** The project's morphology-grounded jawāb-detector, run blind across
the whole corpus, lands the apodosis on v 4 with the lām-al-tawkīd marker — exactly al-Ṭabarī's reading.
(The intervening *wa-anta ḥill* (v 2) is the *iʿtirāḍ* / parenthesis, per al-Zamakhsharī and al-Rāzī; the
generator correctly skips it as a non-opening coordinate.)

---

## Claim 3 — "The opening *lā* is *zāʾida* (redundant emphatic), not a genuine negation, parallel to
*lā uqsimu bi-yawmi-l-qiyāma* (Q 75:1)."

**Source:** al-Akhfash via al-Qurṭubī on Q 90:1; al-Qurṭubī lists six positions (zāʾida / =*alā* / Arab-idiom
/ genuine-negation / *radd* [Mujāhid, Ibn al-ʿArabī] / Qushayrī's denier-refutation).

**Test (rules-tuple = QAC-morphology-POS, the H-NEW-2210 lens):** The morphology tags 90:1:1 as
`laA^ NEG STEM|POS:NEG|LEM:laA` — i.e. QAC parses the *lā* as a **negation particle (NEG)**, not a
zāʾida/emphatic. The H-NEW-2210 generator nonetheless counts the `>aqosamu` form as a genuine oath-opening
(8 corpus attestations: Q 56:75, 69:38, 70:40, 75:1×2, 81:15, 84:16, **90:1**) because the *oath
semantics* hold regardless of the *lā*-parse. The classical claim that Q 90:1 ∥ Q 75:1 is **confirmed
structurally**: these are the corpus's only two *surah-initial* *lā uqsimu* openers.

**Verdict: RULES-TUPLE-FRAGILE.** Whether *lā* is "redundant" is a **grammatical-interpretive** question
that the data underdetermines: QAC tags it NEG (favouring a real-particle reading), while the oath clearly
functions (favouring al-Akhfash's *zāʾida*/affirmative reading). Both the classical majority (affirmative
oath) and the QAC tagger (NEG particle) are internally consistent — the *lā* is genuinely two-valued at
the morphology↔semantics interface. The project does not adjudicate the grammar; it confirms that the
**oath function** is real and that Q 90:1 and Q 75:1 are a true structural doublet.

---

## Claim 4 — "*al-najdayn* (v 10) = the two ways (good and evil)" (majority) vs. "the two breasts" (minority).

**Source:** al-Ṭabarī, al-Qurṭubī, al-Rāzī, Ibn Kathīr (two-ways, via Ibn Masʿūd ← Zirr); ʿIkrima,
al-Ḍaḥḥāk, Saʿīd b. al-Musayyab (two-breasts).

**Test:** This is a **semantic** disagreement, not a structural/numerical one. What IS testable: `njd`
(*najd*) is a **corpus-hapax root** — it occurs only at 90:10 in the entire Quran
(`data/morphology/...`, verified in Q090-F-01: `root_surahs['njd'] == {90}`). So *al-najdayn* is a true
Quranic hapax-form whichever gloss is adopted.

**Verdict: NOT-TESTABLE (the gloss) / VINDICATED (the hapax status).** The two-ways vs. two-breasts split
cannot be resolved empirically (both are lexically possible for the dual of *najd* "elevation"). But the
claim implicit in every commentary — that *al-najdayn* is a striking, unique image — is empirically
underwritten: `njd` is one of Q 90's four corpus-hapax roots.

---

## Claim 5 — "The oath surahs cluster as a coherent group (the *aqsām al-Qurʾān* class)."

**Source:** Ibn al-Qayyim, *al-Tibyān fī aqsām al-Qurʾān* (via H-NEW-2210 §4); the *ʿulūm al-Qurʾān*
tradition (al-Suyūṭī *al-Itqān* nawʿ on al-aqsām; al-Zarkashī *al-Burhān*).

**Test:** Does the *(lā) uqsimu* opener-set {Q 56, 69, 70, 75, 81, 84, 90} cluster in Fisher-Rao content
space relative to Q 90? From `h-new-111.json`: the six co-members rank **28, 30, 37, 38, 42, 57** of 113
in Q 90's neighbor-list — **none in the top-25**, and the co-*surah-initial* opener Q 75 is only rank
37/113 (FR 0.6695). Q 90's *actual* nearest neighbors are the muʿawwidhāt/short-mufaṣṣal tail (Q 112, 103,
107…), not the oath-surahs.

**Verdict: VINDICATED-AS-STRUCTURAL, FALSIFIED-AS-CONTENT.** The oath surahs are a real **opener-grammar /
register class** (H-NEW-2210 confirms the *density* concentration: 3.4× short-mufaṣṣal enrichment, 7.6×
Meccan-enriched, p < 0.0001). But they do **NOT** form a content-FR cluster — the qasam-form is an
opener-grammar axis **orthogonal to content**, reinforcing the project's established letter/opener-axis ⊥
content-axis law. The classical *aqsām* class is a grammatical-rhetorical category, not a content-cohesion
one. (Descriptive, MW-7-capped — the FR ranks were inspected during scoping; no inferential verdict beyond
the H-NEW-2210 density test.)

---

## Claim 6 — "Reciting al-Balad grants security from Allah's anger on the Day of Resurrection."

**Source:** al-Zamakhsharī, *al-Kashshāf*, end of Q 90 commentary (line 71967) — the Ubayy b. Kaʿb
faḍāʾil-al-suwar chain.

**Test:** Substring search across all 9 canonical books (ahmedbaset JSON) for any al-Balad faḍīla:
**zero matches**. The Ubayy faḍāʾil-al-suwar series is classically judged **fabricated (mawḍūʿ)** (Ibn
al-Jawzī, *al-Mawḍūʿāt*).

**Verdict: FALSIFIED (fabricated source).** Not a sound ḥadīth; carries no evidentiary weight. Flagged
per the project's anti-hallucination discipline (see `04-hadith-corpus.md` §4).

---

## Summary

| # | Claim | Verdict |
|:-:|:--|:--|
| 1 | Meccan by agreement; 20 verses | **VINDICATED** |
| 2 | v 4 = jawāb al-qasam | **VINDICATED (structural)** |
| 3 | opening *lā* is *zāʾida* / Q 90:1 ∥ Q 75:1 | **RULES-TUPLE-FRAGILE** (oath-function real; grammar two-valued) |
| 4 | *al-najdayn* = two ways / two breasts | **NOT-TESTABLE (gloss)** / hapax-status **VINDICATED** |
| 5 | oath surahs form a coherent class | **VINDICATED-as-structural / FALSIFIED-as-content** (opener-axis ⊥ content-axis) |
| 6 | al-Balad recitation faḍīla | **FALSIFIED (fabricated)** |

**Net:** The defensible structural claims (verse count, jawāb identification, the Q 75/Q 90 *lā uqsimu*
doublet, the oath-class as a register category) all hold. The semantic disagreements (the *lā*, the
*najdayn*) are genuinely underdetermined by data — honestly verdicted as fragile/not-testable rather than
forced. The recitation-faḍīla is fabricated and excluded.

---

*All claims cited scholar + work + passage; all tests traced to on-disk data. 2026-05-30.*
