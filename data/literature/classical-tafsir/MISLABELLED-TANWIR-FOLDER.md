---
title: "DATA-INTEGRITY WARNING — ar-tafseer-tanwir-al-miqbas is NOT Tanwīr al-Miqbās"
date: 2026-08-08
author: Waiel Al-Shujaa
severity: any finding citing "Ibn ʿAbbās" from this folder is citing Ibn ʿĀshūr instead
---

# `spa5k-tafsir-api/ar-tafseer-tanwir-al-miqbas/` is Ibn ʿĀshūr, not Ibn ʿAbbās

**The folder slug collided on the word "Tanwīr".** It contains **Ibn ʿĀshūr's
*al-Taḥrīr wa'l-Tanwīr*** (d. 1393 AH / 1973 CE), not *Tanwīr al-Miqbās*, the recension
attributed to **Ibn ʿAbbās (d. 68 AH)**. `editions.json` lists the author as the bare string
`"Tanweer"`, which is where the error entered.

## Verified on disk

Counted directly in `ar-tafseer-tanwir-al-miqbas/2/2.json`:

| cited authority | death | occurrences |
|:--|:--|--:|
| al-Zamakhsharī (*al-Kashshāf*) | 538 AH | 5 |
| al-Raḍī al-Astarābādhī | ~686 AH | 3 |
| al-Sakkākī (*al-Miftāḥ*) | 626 AH | 3 |
| Ibn Mālik (*al-Tashīl*) | 672 AH | 2 |

**Ibn ʿAbbās died in 68 AH. He does not quote al-Raḍī.** The scan of the first 60 āyāt of
al-Baqara adds al-Jurjānī (d. 471) ×2. `ar-tafseer-tanwir-al-miqbas/1/1.json` opens with a
discussion of *naḥt* in the basmala quoting Sībawayh's *bāb al-iḍāfa* — unmistakably Ibn ʿĀshūr.

## Where the genuine text is

**`spa5k-tafsir-api/en-tafsir-ibn-abbas/` — English only.** Its Q 2:2 entry is **962 characters**
against the mislabelled folder's **17,227**, and it renders the verse *"(This is the Scripture),
i.e. this is the Book that Muhammad (pbuh) is reciting to you"* — silently taking *dhālika* as a
proximal, with no deictic discussion at all.

## Consequence

**Any finding in this repository that cites "Tanwīr al-Miqbās" or "Ibn ʿAbbās" from the Arabic
folder is citing a 20th-century commentator as a first-generation Companion.** That is a
1,300-year attribution error and it inverts the evidential weight of the citation entirely — a
Companion gloss and a modern scholar's reading are not interchangeable authorities.

**This repository has not been audited for such citations.** Doing so is queued work.

## The rule this instantiates

`findings/PROXY-CLAIMS.md` §6 already names **the name-collision trap in both directions**
(*Mishkāt al-Maṣābīḥ* is not *Mishkāt al-Anwār*; `dani-23-site-supplement.tsv` is al-Dānī's
verse-counting work, not *al-Muqniʿ*). This is a third instance, found independently.

**Standing requirement:** before citing any classical source from a slug-named directory, verify
the author from the text's own internal citations — who does it quote, and when did they die? A
folder name is metadata, and metadata is not evidence.
