# Wave-A Acquisition Run — 2026-04-28

Operator: Acquisition Specialist (Quran Decipherment Project, Wave A support).
Trigger: Wave-A per-surah specialists need primary classical tafsir + hadith sources for Q 1 al-Fātiḥa and Q 2 al-Baqara coverage.

## Summary

| Metric | Value |
|---|---:|
| New tafsir corpora acquired | 16 distinct works (10 fresh + 6 leveraged via OpenITI raw text) |
| New hadith collections acquired | 9 books (Bukhari, Muslim, Tirmidhi, Abu Dawud, Nasa'i, Ibn Majah, Malik, Ahmad, Darimi) |
| Per-surah tafsir extraction files | 46 (23 corpora × {Q001, Q002}) |
| Hadith citation indices | 2 (Q001-citations.md, Q002-citations.md) — 59 Q1 hits + 126 Q2 hits = **185 high-confidence citations across 9 books** |
| Total disk added | ~1.0 GB tafsir + 143 MB hadith |
| Failures | 0 critical (all priority targets acquired) |

## Sources successfully fetched

### A. spa5k/tafsir_api (GitHub) — JSON-formatted, surah-numbered tafsir corpora

Cloned `https://github.com/spa5k/tafsir_api.git` (1.3 GB total; copied 13 relevant tafsirs to `/Users/grey/Downloads/quran/data/literature/classical-tafsir/spa5k-tafsir-api/`). Schema: per-surah JSON `N.json` containing `{"ayahs": [{"ayah": V, "surah": N, "text": "..."}, ...]}`.

| Slug (= directory name) | Author | Title | Lang | Source-of-record |
|---|---|---|---|---|
| `ar-tafsir-ibn-kathir` | Ibn Kathīr (d. 774) | Tafsīr al-Qurʾān al-ʿaẓīm | AR | quran.com mirror |
| `en-tafisr-ibn-kathir` | Ibn Kathīr | (abridged English) | EN | quran.com |
| `ar-tafsir-al-tabari` | al-Ṭabarī (d. 310) | Jāmiʿ al-bayān | AR | quran.com |
| `ar-tafseer-al-qurtubi` | al-Qurṭubī (d. 671) | al-Jāmiʿ li-aḥkām al-Qurʾān | AR | quran.com |
| `ar-tafsir-al-baghawi` | al-Baghawī (d. 510) | Maʿālim al-tanzīl | AR | quran.com |
| `ar-tafseer-al-saddi` | al-Saʿdī (d. 1956) | Taysīr al-karīm al-raḥmān | AR | quran.com |
| `ar-tafsir-al-wasit` | (multiple, mod.) | al-Tafsīr al-Wasīṭ (al-Azhar) | AR | quran.com |
| `ar-tafsir-muyassar` | (King Fahd Complex) | al-Tafsīr al-Muyassar | AR | quran.com |
| `ar-tafseer-tanwir-al-miqbas` | (attr. Ibn ʿAbbās) | Tanwīr al-Miqbās | AR | quran.com |
| `en-al-jalalayn` | Jalāl al-Dīn al-Maḥallī + al-Suyūṭī (d. 911) | Tafsīr al-Jalālayn (English) | EN | altafsir.com |
| `en-asbab-al-nuzul-by-al-wahidi` | al-Wāḥidī (d. 468) | Asbāb al-nuzūl (English) | EN | altafsir.com |
| `en-tafsir-ibn-abbas` | (attr. Ibn ʿAbbās) | Tanwīr al-Miqbās (English) | EN | altafsir.com |
| `en-tafsir-maarif-ul-quran` | Mufti Muḥammad Shafīʿ | Maʿārif al-Qurʾān (English) | EN | quran.com |

License: each `editions.json` records `source` (quran.com or altafsir.com). The clone is non-commercial / open-tafsir.

### B. OpenITI canonical raw mARkdown texts (GitHub)

Direct fetch from `raw.githubusercontent.com/OpenITI/<XAH>/master/data/<author>/<work>/<file>`. These are the gold-standard machine-readable Arabic editions used in computational Quranic studies. Saved to `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/`.

| File | Bytes | Author | Title | Source URI (Shamela ID) |
|---|---:|---|---|---|
| `tabari-jami-bayan.openiti.raw.txt` | 28,566,686 | al-Ṭabarī (d. 310) | Jāmiʿ al-bayān ʿan taʾwīl āy al-Qurʾān | Shamela_0007798 |
| `qurtubi-jami-ahkam.openiti.raw.txt` | 20,485,460 | al-Qurṭubī (d. 671) | al-Jāmiʿ li-aḥkām al-Qurʾān | Shamela_0020855 |
| `ibn-kathir-tafsir-quran.openiti.raw.txt` | 15,422,327 | Ibn Kathīr (d. 774) | Tafsīr al-Qurʾān al-ʿaẓīm (mARkdown-tagged) | Shamela_0008473 |
| `tabarsi-majma-bayan.openiti.raw.txt` | 14,403,574 | al-Ṭabarsī (d. 548, Imāmī) | Majmaʿ al-bayān fī tafsīr al-Qurʾān | Shia 002359 (multi-vol) |
| `suyuti-durr-manthur.openiti.raw.txt` | 15,457,321 | al-Suyūṭī (d. 911) | al-Durr al-manthūr fī l-tafsīr bi-l-maʾthūr | Shamela_0012884 |
| `thaclabi-kashf-bayan.openiti.raw.txt` | 10,484,602 | al-Thaʿlabī (d. 427) | al-Kashf wa-l-Bayān ʿan tafsīr al-Qurʾān (mARkdown) | Shamela_0023578 |
| `zamakhshari-kashshaf.openiti.raw.txt` | 7,839,909 | al-Zamakhsharī (d. 538) | al-Kashshāf ʿan ḥaqāʾiq al-tanzīl | Shamela_0023627 |

(Already on disk from prior runs: Bīqāʿī, Suyūṭī al-Itqān, Rāzī Mafātīḥ — re-extracted alongside.)

### C. Internet Archive — Tafsīr Ibn Kathīr Darussalam (10-volume English)

`https://archive.org/details/tafsir-ibn-kathir-10.-Volumes` — Mubarakpuri ed., 2003. Saved to `/Users/grey/Downloads/quran/data/literature/classical-tafsir/ibn-kathir-english-darussalam/`.

| File | Bytes | Coverage |
|---|---:|---|
| `tafsir-ibn-kathir-vol-01.pdf` | 26,034,546 | Vol 1: Q1 + Q2:1-252 |
| `tafsir-ibn-kathir-vol-01.djvu.txt` | 1,257,493 | Vol 1 OCR plaintext |
| `tafsir-ibn-kathir-vol-02.djvu.txt` | 1,069,416 | Vol 2 OCR plaintext (Q2:253 → mid-Q4) |

Q2 Ibn Kathīr English is reconstituted from Vol 1 (verses 1-252) + Vol 2 (verses 253-286 incl. Āyat al-Kursī 2:255 and the last two verses 2:284-286). 

### D. Internet Archive — Zamakhsharī al-Kashshāf supplemental plaintext

`https://archive.org/details/TafsirAlKashaf` — saved to `/Users/grey/Downloads/quran/data/literature/classical-tafsir/zamakhshari-kashshaf/zamakhshari-kashshaf.djvu.txt` (8,727,829 bytes). Independent OCR-plaintext companion to the OpenITI mARkdown version (cross-validation source).

### E. AhmedBaset/hadith-json (GitHub) — 9-book hadith corpus

Cloned `https://github.com/AhmedBaset/hadith-json.git` (176 MB). Copied to `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/`. Schema: `by_book/the_9_books/<book>.json` containing `{metadata, chapters, hadiths}` with each ḥadīth carrying both `arabic` (fully-pointed, original isnād + matn) and `english` (sunnah.com translation) fields, plus `idInBook` and global `id`.

| Book | Author | Total ḥadīth |
|---|---|---:|
| `bukhari.json` | al-Bukhārī (d. 256) | 7,277 |
| `muslim.json` | Muslim (d. 261) | (~7,000) |
| `tirmidhi.json` | al-Tirmidhī (d. 279) | (~3,950) |
| `abudawud.json` | Abū Dāwūd (d. 275) | (~5,275) |
| `nasai.json` | al-Nasāʾī (d. 303) | (~5,750) |
| `ibnmajah.json` | Ibn Mājah (d. 273) | (~4,340) |
| `malik.json` | Mālik b. Anas (d. 179) | (~1,800) |
| `ahmed.json` | Aḥmad b. Ḥanbal (d. 241) | (~26,000) |
| `darimi.json` | al-Dārimī (d. 255) | (~3,400) |

(Sunan al-Tirmidhī's grading metadata — ṣaḥīḥ/ḥasan/ḍaʿīf — is sometimes embedded in the matn text but is NOT a structured field; specialists must extract from `english` field's "Hasan/Sahih/Daif" tags.)

## Sources that failed (with reason)

None of the **priority targets** failed. A few **bonus** attempts:

| Target | Attempted approach | Outcome |
|---|---|---|
| OpenITI Qurṭubī initial directory probe | `0700AH/data/0671Qurtubi` | 404 — wrong AH bucket; resolved by checking `0675AH/data/0671AbuCabdAllahQurtubi` (correct) |
| sunnah.com REST API | direct call without API key | Skipped: AhmedBaset/hadith-json is a complete sunnah.com mirror; no need to hit live API and risk rate limits |
| Ibn Kathīr English Vol 2 PDF | not pulled (1 GB+ for all 10 vols) | Only Vol 2 djvu_txt (1 MB) acquired since Q2 boundary lies inside Vol 2; the rest is out-of-scope for Wave A |

## Per-surah tafsir extraction files

Each tafsir has been split into `<label>-Q001.txt` (al-Fātiḥa) and `<label>-Q002.txt` (al-Baqara). Two parallel extraction strategies were used:

### Strategy 1: spa5k/tafsir_api JSON → per-verse plaintext

Per-verse text concatenated with `## Verse N:V` headers. Files written to `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/`:

| Tafsir label | Q001 size | Q002 size |
|---|---:|---:|
| `ibn-kathir-ar` | 126,579 | 1,862,905 |
| `ibn-kathir-en` (abridged) | 110,218 | 2,254,849 |
| `tabari-ar` | 221,602 | 6,219,878 |
| `qurtubi-ar` | 153,659 | 3,195,041 |
| `baghawi-ar` | 23,734 | 925,039 |
| `saddi-ar` | 9,653 | 588,920 |
| `wasit-ar` | 39,314 | 1,998,646 |
| `muyassar-ar` | 4,389 | 158,990 |
| `tanwir-miqbas-ar` | 217,492 | 3,386,985 |
| `jalalayn-en` | 4,324 | 194,902 |
| `asbab-nuzul-wahidi-en` | 21,757 | 248,161 |
| `ibn-abbas-en` | 2,806 | 185,445 |
| `maarif-ul-quran-en` | 77,163 | 1,715,632 |

### Strategy 2: OpenITI raw mARkdown → surah-section slice

Section boundaries detected by header lines `### | سورة الفاتحة` / `### | سورة البقرة` / `### | سورة آل عمران` (with Q3 as terminator), preferring header markers over inline mentions and enforcing Q1 < Q2 < Q3 ordering (this fixed an initial bug where Q2-marker hits inside Q1's introductory matter were being mis-selected). Files in `raw/`:

| Tafsir label | Q001 size | Q002 size |
|---|---:|---:|
| `tabari-ar-openiti` | 149,665 | 5,126,058 |
| `ibn-kathir-ar-openiti` | 131,133 | 1,469,716 |
| `qurtubi-ar-openiti` | 165,533 | 3,289,676 |
| `zamakhshari-kashshaf-ar-openiti` | 30,539 | 802,815 |
| `tabarsi-majma-bayan-ar-openiti` | 81,754 | 1,933,773 |
| `suyuti-durr-manthur-ar-openiti` | 11,981 | 2,558,830 |
| `thaclabi-kashf-bayan-ar-openiti` | 121,313 | 1,328,257 |
| `razi-mafatih-ar-openiti` | 944,841 | 5,177,651 |
| `biqai-nazm-ar-openiti` | 40,748 | 313,930 |
| `ibn-kathir-en-darussalam` | 100,447 | 1,234,864 |

(Sizes shown are post-extraction; UTF-8 bytes including a ~150-byte header per file.)

## Per-surah hadith citation indices

Files in `/Users/grey/Downloads/quran/data/literature/hadith/`:

- `Q001-citations.md` (133 KB, 59 high-confidence citations) — searches matched against tightened Arabic patterns (`الفاتحة`, `فاتحة الكتاب`, `أم الكتاب`, `السبع المثاني`, `أم القرآن`) and English patterns (`Al-Fatihah`, `Mother of the Book`, `Umm al-Kitab`, `Seven Oft-Repeated`, `Sab' al-Mathani`, `Mathani`, context-restricted `Opening of the…`, `the Opener`).
- `Q002-citations.md` (227 KB, 126 high-confidence citations) — searches matched against (`سورة البقرة`, `آية الكرسي`, `الكرسي`, `خواتيم البقرة`, `آخر سورة البقرة`, `\bالبقرة\b`) AR and (`Al-Baqarah`, `Surat al-Baqarah`, `Ayat al-Kursi`, `Throne Verse`, `last two verses of Baqarah`, `Khawatim al-Baqarah`) EN.

Initial run (broader patterns) returned 139 Q1 + 250 Q2 = 389 hits, but bare patterns like `opening` (matching prayer-start) and `cow` (matching actual cattle) generated ~50% false positives. Refinement to named-entity-only patterns yielded 59 + 126 = 185 high-confidence citations. Refined patterns are documented inline in the citation MD files.

| Book | Q1 hits | Q2 hits |
|---|---:|---:|
| Sahih al-Bukhari | 5 | 9 |
| Sahih Muslim | 5 | 18 |
| Jami` at-Tirmidhi | 3 | 12 |
| Sunan Abi Dawud | 16 | 10 |
| Sunan an-Nasa'i | 10 | 22 |
| Sunan Ibn Majah | 10 | 6 |
| Muwatta Malik | 0 | 2 |
| Musnad Ahmad | 2 | 2 |
| Sunan al-Darimi | 8 | 45 |
| **TOTAL** | **59** | **126** |

Each hit records: book, idInBook, global_id, chapter (Arabic + English), matched terms (AR + EN), and full Arabic + English text (truncated to 1500 chars for any single citation).

Spot-checks confirm canonical hits are present: Bukhari 4273/4441/4497 (the "greatest sūra in the Qurʾān" hadith linking al-Fātiḥa = al-Sabʿ al-Mathānī), Bukhari 4800 (the ruqya hadith citing al-Fātiḥa as Umm al-Kitāb), and the Bukhari/Muslim "khawātim al-Baqara" cluster about the last two verses sufficing the believer at night.

## Specific gaps / remaining work

1. **al-Tirmidhī ḥasan/ṣaḥīḥ/ḍaʿīf gradings** are embedded in the English `text` field of his hadiths rather than as a structured grading column. Wave-A specialists who need stratified-by-grade analysis will need to regex-extract grading tags (e.g., `Grade: Sahih`, `Hasan`, `Daif`) from the `english` field of `tirmidhi.json`. The unstructured-grade limitation is a property of sunnah.com, not this acquisition.

2. **Ibn Kathīr English Darussalam Vol 3-10** were NOT acquired (would add ~250 MB). Out of scope for Wave A (Q1, Q2). When Wave B/C reaches Q3+, a follow-up acquisition should pull `Tafsir_Ibn_Kathir_Vol._N.djvu.txt` for N=3..10.

3. **al-Suyūṭī Tafsīr al-Jalālayn Arabic** is present via OpenITI catalog (`0911Suyuti.TafsirJalalayn`) but was not fetched — `en-al-jalalayn` from spa5k provides the English translation already, and the Arabic Jalālayn is famously brief (a single thin volume). Not a priority gap. Direct URL recorded: `https://github.com/OpenITI/0925AH/tree/master/data/0911Suyuti/0911Suyuti.TafsirJalalayn`.

4. **Tafsīr al-Māturīdī, al-Ṭūsī al-Tibyān, Ibn ʿAṭiyya al-Muḥarrar al-wajīz** — these are valuable mid-tier classical tafsirs not currently acquired. OpenITI hosts at least al-Māturīdī and Ibn ʿAṭiyya. Out of scope for the priority list given.

5. **OpenITI corpus download — full** would be ~5-10 GB and contains a rich library of balāgha, qiraʾāt, ḥadīth-rijāl, and uṣūl works. Not requested. The targeted single-file fetches done here are far cheaper and already cover the named priority targets.

6. **Hadith grading dataset** — for Bukhari/Muslim everything is ṣaḥīḥ by definition. For Tirmidhī/Abū Dāwūd/Nasāʾī/Ibn Mājah/Ahmad, gradings vary and a separate grading database (e.g., `dorar.net` API) would be needed for proper isnād-tier analysis. Not requested for this run.

## File inventory (relative paths from `/Users/grey/Downloads/quran/data/literature/`)

```
classical-tafsir/
  raw/
    [PRIOR]    biqai-nazm-al-durar.openiti.raw.txt           17,599,119
    [PRIOR]    biqai-nazm-al-durar.ShamAY.raw.txt            18,543,763
    [PRIOR]    razi-mafatih-al-ghayb.openiti.raw.txt         29,672,464
    [PRIOR]    suyuti-itqan.openiti.raw.txt                   2,404,336
    [NEW]      ibn-kathir-tafsir-quran.openiti.raw.txt       15,422,327
    [NEW]      tabari-jami-bayan.openiti.raw.txt             28,566,686
    [NEW]      qurtubi-jami-ahkam.openiti.raw.txt            20,485,460
    [NEW]      zamakhshari-kashshaf.openiti.raw.txt           7,839,909
    [NEW]      tabarsi-majma-bayan.openiti.raw.txt           14,403,574
    [NEW]      suyuti-durr-manthur.openiti.raw.txt           15,457,321
    [NEW]      thaclabi-kashf-bayan.openiti.raw.txt          10,484,602
    [NEW]      <26 spa5k Q001/Q002 extraction files>
    [NEW]      <18 OpenITI Q001/Q002 section extracts>
    [NEW]      <2  Ibn Kathir English Darussalam Q001/Q002 extracts>
  spa5k-tafsir-api/
    <13 sub-directories, one per tafsir, each with 114 surah JSON files>
    editions.json
    LICENSE  README.md
  ibn-kathir-english-darussalam/
    tafsir-ibn-kathir-vol-01.pdf                             26,034,546
    tafsir-ibn-kathir-vol-01.djvu.txt                         1,257,493
    tafsir-ibn-kathir-vol-02.djvu.txt                         1,069,416
  zamakhshari-kashshaf/
    zamakhshari-kashshaf.djvu.txt                             8,727,829

hadith/
  Q001-citations.md                                             132,989
  Q002-citations.md                                             227,210
  ahmedbaset-json/
    db/
      by_book/the_9_books/{bukhari,muslim,tirmidhi,abudawud,nasai,ibnmajah,malik,ahmed,darimi}.json
      by_chapter/the_9_books/<book>/<chapter>.json
      <plus forties + other_books bonus>
  bukhari/  muslim/  tirmidhi/  abu-dawud/  nasai/  ibn-majah/  scratch/
    (empty subdirs reserved for per-book future per-Q extraction)
```

## Methodology notes for downstream specialists

1. **Two parallel Arabic Tabari/Qurtubi/Ibn Kathir/Zamakhshari extracts exist**: the `spa5k-tafsir-api` JSON (verse-keyed but lighter, sourced from quran.com) and the `OpenITI` raw text (full prose, sourced from al-Maktaba al-Shāmila). Use **OpenITI for full-text searches and prose continuity**; use **spa5k for verse-aligned tafsir-per-ayah lookups**. They occasionally disagree on minor wording — both are legitimate manuscript transmissions.

2. **The OpenITI raw files preserve `PageEndV<vol>P<page>` markers** and `~~` continuation marks. Strip these only at analysis time (preserving in stored extracts allows page-level cross-reference back to the print Shamela editions).

3. **For Q 1 hadith analysis**, the canonical Bukhari clusters are 4273 (Tafsīr / Q15:87), 4441 (Tafsīr / Q1), 4497 (Tafsīr / Q1), 4800 (Faḍāʾil al-Qurʾān / ruqya). Check Muslim's parallel chains via same-isnād matching on Abū Saʿīd b. al-Muʿallā / Abū Saʿīd al-Khudrī / Anas. The Q002-citations.md surfaces the Bukhari/Muslim "two verses suffice" cluster.

4. **Garden-of-forking-paths declaration for hadith pattern selection**: my refined patterns explicitly DROPPED `\bopening\b` (lowercase, generic) and `\bcow\b` (lowercase, generic) because manual sampling showed these matched generic prayer-opening hadiths and actual cattle/livestock hadiths respectively. The cost is that genuine but non-canonical references using only English `opening` / `cow` (rare) are missed. Trade-off accepted: precision over recall, since Wave-A specialists will be searching FROM these citations OUTWARD (i.e., expanding via isnād) rather than relying solely on this index.

— end of acquisition log —
