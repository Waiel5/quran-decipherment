---
id: Q017-F-03
title: Q 17:88 (taḥaddī verse) — classical citation density across 9 tafsirs
date_locked: 2026-04-28
phase: B+
seed: 20260428
rules_tuple: (no-tashkeel, orthographic-token, exegetical-mention, scholar+work+passage, Hafs-Kufan, Mashriqi)
---

# Q017-F-03 — Taḥaddī verse Q 17:88 lexical signature + citation density (PRE-REG)

## Hypothesis (locked direction)

Q 17:88 *Qul la-ʾini ijtamaʿati al-insu wa-l-jinnu ʿalā an yaʾtū bi-mithli hādhā al-Qurʾāni lā yaʾtūna bi-mithlihi wa-law kāna baʿḍuhum li-baʿḍin ẓahīrā* — the **taḥaddī (challenge) verse** — is a lexical/theological hub. Two parts:

(A) **Lexical signature**: the verse contains the unique-form *al-insu wa-l-jinnu* (humans-and-jinn), and the phrase *bi-mithli hādhā al-Qurʾāni* (the like of this Qurʾān). Q 17:88 is the strongest *taḥaddī* formulation in the Qurʾān (cf. weaker forms at Q 2:23, Q 10:38, Q 11:13, Q 52:34).

Direction: Q 17:88 uses 5 unique iʿjāz-related lemmas (root م-ث-ل "mithl"; root ج-م-ع "ijtimāʿ"; root ج-ن-ن "jinn"; root ا-ن-س "ins"; root ظ-ه-ر "ẓahīr") in a single verse — a lemma-density compatible with hub-status.

(B) **Citation density**: Q 17:88 appears in ≥ 4 of the 9 mufassirūn extracted at `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/{ibn-kathir,tabari,qurtubi,razi,zamakhshari,biqai,tabarsi,thaclabi,suyuti-durr}-openiti-Q017.txt` with substantial commentary (≥ 200 chars on the verse).

Direction: Q 17:88 should appear with ≥ 200 chars commentary in ≥ 4 of the 9 tafsirs.

## Method (lexical)

1. Load `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
2. Extract Q 17:88 verse text.
3. Tokenize; map each token to its lemma/root via simple rule-based lookup against the listed roots.
4. Verify presence of the 5 expected lemmas.

## Method (citation density)

1. For each tafsir Q17 extract: search for the literal phrase "بمثل هذا القرآن" (or close variants), the verse-anchor "آية 88" pattern, and the phrase "اجتمعت الإنس والجن".
2. Count which tafsirs have ≥ 200 chars of contiguous commentary on Q 17:88.
3. Tabulate.

## Success criteria

- DIRECTIONAL VINDICATION (A+B): all 5 lemmas attested + ≥ 4 tafsirs cite the verse substantively.
- DIRECTIONAL FALSIFICATION: lemmas absent OR < 4 tafsirs cite.

## Bonferroni

Two-part family (lexical + citation): k=2, α_corrected = 0.025.

## NULL

If lexical lemmas missing OR citation density below threshold: publish as NULL.

## Classical anchor

The taḥaddī (challenge of inimitability) is a foundational claim in classical *iʿjāz* literature (al-Bāqillānī, al-Khaṭṭābī, al-Suyūṭī, al-Rāzī, al-Zamakhsharī all engage it). The five Qurʾānic taḥaddī verses (Q 2:23, 10:38, 11:13, 17:88, 52:34) are graded by classical tradition: Q 17:88 is the **maximal** form (challenging humans + jinn together with the entire Qurʾān). This pre-reg is empirically asking whether classical exegesis treats Q 17:88 as the hub the tradition claims.
