# Journal — naskh-run-1

Date: 2026-04-12. Agent: Phase-B naskh cataloguer. Task: produce defensible map of classical and modern abrogation theory, anchored to Q 2:106 and the famous candidate pairs.

## Method

1. Extracted root n-s-kh occurrences from the min-tashkeel JSON corpus at `/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json`, using a diacritics-stripped substring match over Arabic verse text. Confirmed four genuine root occurrences (2:106, 7:154, 22:52, 45:29) plus one false-positive (11:38, which is s-kh-r not n-s-kh — the string match caught the ن ... س ... خ sequence across a different root).
2. Pulled full Arabic verse text for all classical candidate pairs: 2:106, 2:142-144, 2:180, 2:219, 2:234, 2:240, 4:43, 5:90-91, 16:67, 16:101, 22:52, 73:1-4, 73:20. This gives the primary-source foundation for the catalog.
3. Synthesized classical naskh theory from working knowledge: al-Shāfiʿī's *al-Risāla* for the foundational articulation; al-Suyūṭī's *al-Itqān* ch. 47 for the late-classical shortlist; Ibn al-Jawzī and al-Nahhas for the maximalist lists; Shāh Walī Allāh, Muḥammad ʿAbduh/Rashīd Riḍā in *al-Manār*, and Ṣubḥī Ṣāliḥ's *Mabāḥith fī ʿulūm al-Qurʾān* for the modern minimalist trajectory; Abū Muslim al-Iṣfahānī as the classical outlier who rejected intra-Qurʾānic naskh entirely.
4. Organised the catalog along five axes as requested: (1) root semantics, (2) 2:106 exegesis, (3) maximalist-vs-minimalist lists, (4) four named candidate pairs, (5) tilāwah/ḥukm typology and the stoning verse.

## Key findings

- **Root n-s-kh is bipolar**: "cancel/efface" and "copy/transcribe" are the same root. The Qurʾān deploys both senses (22:52 cancel, 7:154 and 45:29 copy/transcribe, 2:106 contested). The classical doctrine reduces the root to the cancellation pole and loses information.
- **Q 2:106's key exegetical variables**:
  - *āya* — "sign" vs "verse" is a live ambiguity; classical reading narrows to "verse."
  - *nunsihā* vs *nansaʾhā* — qirāʾāt variation shifts the meaning from "cause-to-be-forgotten" to "defer/postpone," which is not the same legal-theological concept.
  - *aw mithlihā* — the "or the like of it" clause fits inter-dispensational succession better than intra-Qurʾānic cancellation.
- **Maximalist-to-minimalist shrinkage**: Ibn al-Jawzī ~247 cases, al-Suyūṭī ~20, Shāh Walī Allāh 5, Ṣubḥī Ṣāliḥ 4, Abū Muslim and modern Qurʾān-alone schools 0. The shrinkage is absorbed mostly by reclassification as *tadarruj* (progressive legislation), *takhṣīṣ* (specification), *taqyīd* (qualification), and *bayān* (clarification).
- **Wine sequence 16:67 → 2:219 → 4:43 → 5:90-91** is the clearest paradigm case of *tadarruj* rather than naskh — each stage is a waypoint, not a contradictor.
- **73:1-4 vs 73:20** and **2:234 vs 2:240** are the two strongest in-sūra grafting cases — both retain earlier and later material in the same sūra with the later material modifying the earlier, which is evidence for deliberate diachronic redaction.
- **Qibla** (2:144 vs 2:142-143) is not an intra-Qurʾānic abrogation because the Jerusalem qibla is nowhere legislated in the Qurʾān; at most this is a Qurʾānic ratification of a change in practice.
- **Widow provisions** 2:234 and 2:240 can be read non-abrogatively as mandatory ʿidda plus optional bequest — Rashīd Riḍā's harmonising reading is a live alternative to the dominant classical abrogation claim.
- **Āyat al-rajm** (stoning verse) is the strongest and weakest counter-witness simultaneously: strongest to the completeness of the muṣḥaf, weakest in evidentiary base. Treat as contested and do not rely on it.

## Uncertainties and open questions

- I have not cross-checked the Suyūṭī shortlist against the list of 21 in his printed *Itqān* chapter; the number "around 20" is the consensus reported figure but exact contents vary between editions.
- The qirāʾāt readings of 2:106 (nunsihā vs nansaʾhā) are well-attested but I relied on recall rather than a fresh collation against the ʿAshara qirāʾāt tables. A separate agent should validate against the mutashabih/qirāʾāt materials already in the project.
- The widow-bequest harmonisation reading (Riḍā/Ṭabāṭabāʾī) may deserve its own deep-dive, because if accepted it removes the single strongest "certain" case from the minimalist list and effectively collapses it toward Abū Muslim's zero-case position.
- I did not attempt statistical or structural analysis of whether the graft-points (2:234/240, 73:1-4/73:20, 58:12/58:13) cluster in detectable positions (e.g., near sūra midpoints, near ring-centers). That is a follow-up task for the ring-centers or surah-boundaries agents.

## Downstream handoffs

- To the ring-centers agent: check whether the three in-sūra graft-points sit at structurally significant positions.
- To the deep-hypotheses queue: the inter-dispensational reading of Q 2:106 is a candidate hypothesis worth testing against intertextual evidence with earlier scriptural traditions.
- To the chrono-revelation agent: the graft-cases (73, 58, 2) are evidence for deliberate placement of diachronic material within single sūras; worth cross-referencing with revelation-order data at `/Users/grey/Downloads/quran/data/revelation-order.csv`.

## Files written

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/naskh-catalog.md` — main deliverable, ~3000 words.
- `/Users/grey/Downloads/quran/journal/naskh-run-1.md` — this journal.
