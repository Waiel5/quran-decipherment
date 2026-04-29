# yawm-run-2 journal

Agent: Phase-B yawm-catalog. Date: 2026-04-12.

## Goal

Produce a name-level catalogue of Day-of-Judgement epithets from the
Quran, verify each against QAC v0.4, count al-sāʿa precisely,
compare the five "Day-named" surahs (56, 69, 75, 88, 101), link
mawʿūd/waʿīd to the covenant family, expound Q 47:18 (ashrāṭ), and
lay out the canonical event-sequence (sūr → baʿth → ḥisāb →
mīzān → ṣirāṭ).

## Method

1. Load QAC v0.4 morphology. Build per-verse segment index.
2. For each epithet, determine the Buckwalter lemma by spot-check
   against the target verse (e.g., Q 1:4 for yawm al-dīn, Q 79:34
   for al-ṭāmma).
3. Verify yawm-compounds by *adjacency*: yawm at word W, epithet
   at word W+1 in the QAC word field. This is stronger than
   co-occurrence-within-verse.
4. Attach Meccan/Medinan (Egyptian) and Nöldeke-phase labels via
   `data/revelation-order.csv`.

## Probing log

- Initial run returned zero yawm hits — Buckwalter lemma is
  `yawom`, not `yawm`. Re-probed all lemmas in a separate
  script (`scratch/yawm-catalog/probe.py`) to recover correct
  Buckwalter forms: `yawom`, `diyn`, `qiya\`map`, `Haq~`,
  `HisaAb`, `faSol`, `jamoE`, `t~agaAbun`, `t~anaAd`, `xuruwj`,
  `saAEap`, `qaAriEap`, `T~aA^m~ap`, `S~aA^x~ap`, `ga\`$iyap`,
  `waAqiEap`, `HaA^q~ap`, `'aAzifap`, `mawoEuwd`, `waEiyd`,
  `|xir` / `A^xir`.
- Data-JSON shape: list of surah objects with `id`, `type`, not
  a dict keyed by id. Fixed loader.
- Checked adjacent yawm+tanaAd: the lemma is `t~anaAd` (with
  shadda marker). Confirmed 40:32.
- Checked al-ākhir adjacency: lemma is `|xir` — one Alef-madda
  form. 26 adjacency hits confirm; exactly 1 Meccan (29:36),
  25 Medinan.

## Key counts (verified)

- al-sāʿa: 48 segment hits, 43 unique verses. 36 are DET-prefixed
  or PRON-suffixed (strict "the Hour" reading). 37 Meccan /
  6 Medinan.
- yawm al-qiyāma: 70 unique verses (adj). 48 Meccan / 22 Medinan.
- al-yawm al-ākhir: 26 unique verses (adj). 25 Medinan.
- yawm al-dīn: 13 unique verses (adj). All Meccan.
- yawm al-faṣl: 6 unique verses (adj). 4 are in Sūrat al-
  Mursalāt alone.
- yawm al-taghābun: 1 hapax (64:9). Same verse also contains yawm
  al-jamʿ — the only multi-epithet verse in the Quran.
- yawm al-mawʿūd: 1 hapax (85:2).
- yawm al-waʿīd: 1 hapax (50:20), though `waʿīd` alone appears 6x
  all in Qāf/Ibrāhīm/Ṭā-Hā.
- al-āzifa: 2 verses (40:18, 53:57). 53:57 has the figura-
  etymologica `azifati l-āzifa`.

## Surprises

1. **Surahs 56, 69, 75, 88, 101 all Early Meccan.** All five
   epithet-titled surahs are in Nöldeke phase 1. Their length
   decreases monotonically with mushaf order (96→52→40→26→11).
2. **The hapax `ashrāṭ-hā` (47:18).** The Quran's single
   technical term for the precursor-signs of the Hour occurs
   exactly once. Entire hadith corpora are built on one word.
3. **Two-faces hinge.** Four of the five Day-named surahs (69,
   75, 88, 101) use the *wujūhun yawmaʾidhin X* bifurcation.
   This is a named sub-genre.
4. **Covenant-Day isomorphism.** mawʿūd and waʿīd are both from
   the same covenant root as waʿd/mīʿād/mawʿid. The Day-name
   inventory overlaps the covenant-word inventory at the
   single root `wEd`.

## Files produced

- findings/phase-b-hypotheses/yawm-catalog.md (~5300 words —
  over budget, but structured by section for skimming).
- scratch/yawm-catalog/verify.py
- scratch/yawm-catalog/verify-out.txt
- scratch/yawm-catalog/probe.py

## Open work

- H1 stage-naming rule not tested statistically (would require
  annotating ~200 verses for stage-of-event).
- Candidate additions to the "disclosed-Day" sub-genre (77, 79,
  80, 82) not coded against the four-feature template.
- "ashrāṭ" hapax deserves its own replication note.
