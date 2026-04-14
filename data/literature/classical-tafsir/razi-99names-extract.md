# Al-Razi on the Muqatta'at as Divine-Name Abbreviations

## Source attribution

Fakhr al-Dīn al-Rāzī (d. 606 H / 1209 CE), *Mafātīḥ al-Ghayb* (also called
*al-Tafsīr al-Kabīr*), in his commentary on the openings of Sūrat al-Baqarah,
Āl ʿImrān, and the other muqatta'at-bearing surahs, lists ~20 opinions on the
huruf muqatta'at. The opinions of relevance to H20 are:

### Opinion (a) — Names of the surahs

The muqatta'at are names by which God designates each surah (e.g. Sūrat ALM,
Sūrat ALR). This is one of the ~20 opinions and the one al-Razi treats most
extensively, but it does NOT make the divine-names claim per se.

### Opinion (b) — Initials of divine names / divine attributes

This is the opinion most relevant to H20. Al-Razi reports it as held by some
of the salaf, including statements attributed to **ʿAbd Allāh ibn ʿAbbās** and
**ʿAbd Allāh ibn Masʿūd**. The structure is that each muqatta'at letter is the
first letter of one of God's names or attributes, so the combination as a
whole is a memnonic abbreviation of a divine list.

Example decompositions reported in classical sources (collected from al-Razi,
al-Suyūṭī's *al-Itqān*, al-Ṭabarī, al-Qurṭubī, al-Zamakhsharī, and Tafsīr Ibn
ʿAbbās / Tanwīr al-Miqbās):

- **ALM** (الم): Different decompositions are reported.
  - Variant 1: ا = Allāh, ل = Laṭīf, م = Majīd ("Allāh, the Subtle, the
    Glorious"). Attributed to some early companions.
  - Variant 2 (the *phrase* reading): ا-ل-م = "Anā Allāhu Aʿlam" ("I, Allāh,
    am the All-Knowing"). This is reported by Ibn ʿAbbās via al-Tabarānī /
    Bahr al-Muhīṭ.

- **ALR** (الر): "Anā Allāhu Raʾā" / "Anā Allāhu Arā" ("I, Allāh, see"); or
  decomposition Allāh / Laṭīf / Raḥmān or Allāh / Laṭīf / Rabb. Attributed
  variously.

- **ALMS** (المص) and **ALMR** (المر): treated as lengthened versions of the
  same phrase.

- **KHYAS** (كهيعص): The decomposition reported on Ibn ʿAbbās's authority
  (transmitted via al-Suyūṭī's *al-Durr al-Manthūr* 4/679):
    ك = al-Kabīr / al-Kāfī
    ه = al-Hādī
    ي = al-Amīn  ← *NOTE: starts with hamza/alif, NOT yāʾ — see analysis*
    ع = al-ʿAzīz
    ص = al-Ṣādiq

- **HM** (حم): "Ḥamīd Majīd" or "Ḥalīm Majīd"; sometimes "Ḥaqq Mubīn".

- **YS** (يس): "Yā Sayyid" / "Yā Sayyid al-mursalīn" — vocative address to
  the Prophet, NOT a divine-name abbreviation in this reading.

- **TH** (طه): same as YS — vocative ("O man" / "Yā rajul" in Nabataean), or
  divine-name abbreviation Ṭāhir / Hādī.

- **TSM** (طسم): Ṭāhir / Salām / Majīd, or Ṭayyib / Samīʿ / Malik.

- **Q** (ق): "Qādir" / "Qayyūm" / "Qarīb"; or the name of a mountain
  surrounding the world; or a name of God known only to Him.

- **N** (ن): Nūr / Nāṣir; or "ḥūt" (whale); or the inkwell.

## Al-Razi's own position

Al-Razi himself does NOT commit to the divine-names theory as the correct
opinion. He lists it as one of ~20 plausible interpretations and notes that
many of the early companions held variant decompositions, which weakens the
case that any single decomposition is the intended one. He explicitly says
that since the early scholars themselves disagreed on which divine names the
letters abbreviate, the strict letter-to-name decomposition cannot be the
unique intended meaning.

His own preferred position (per the standard summaries of *Mafātīḥ al-Ghayb*
on Q. 2:1) is closer to the *iʿjāz* opinion: the muqatta'at challenge the
Arabs by demonstrating that the same letters they use to compose poetry are
used by God to compose a book they cannot match.

## Caveats important for H20 testing

1. The "Allāh / Laṭīf / Majīd" decomposition for ALM is only one of several
   classical readings. The "Anā Allāhu Aʿlam" PHRASE reading is competing.
2. Several decompositions (KHYAS = Kabīr/Hādī/Amīn/ʿAzīz/Ṣādiq) use Arabic
   words whose first letter does NOT match the muqatta'at letter. ي → al-Amīn
   starts with alif, not yāʾ. So the classical "abbreviation" theory itself
   does not strictly require first-letter matching — it allows phonetic /
   meaningful association.
3. This means the strict computational test (luminous letters as initial
   letters of the canonical 99 names) is testing a STRONGER claim than what
   al-Razi or Ibn ʿAbbās themselves actually defended. They allowed loose
   matching; we test strict matching.
4. The classical decompositions also draw from divine ATTRIBUTES that are
   not necessarily in the canonical 99 (e.g. Rabb, Aʿlam, Sayyid, Hādī
   sometimes), so even a relaxed test would need to expand the candidate
   pool beyond the 99.

## Sources

- https://en.wikipedia.org/wiki/Muqatta%CA%BFat
- al-Suyūṭī, *al-Durr al-Manthūr fī Tafsīr al-Maʾthūr*, vol. 4, p. 679 (on Q. 19:1)
- Tafsīr Ibn ʿAbbās (Tanwīr al-Miqbās min Tafsīr Ibn ʿAbbās), entries on
  Q. 2:1, Q. 10:1, Q. 19:1, Q. 38:1, Q. 50:1, Q. 68:1
- Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-Ghayb* (al-Tafsīr al-Kabīr), 32 vols,
  Cairo edition; commentary on Q. 2:1 and Q. 19:1
- Internet Archive copy of al-Razi's tafsir:
  https://archive.org/details/mafatihalghayb06raziuoft
