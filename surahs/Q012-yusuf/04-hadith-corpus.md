---
surah: 12
surah_name_ar: يوسف
surah_name_translit: Yūsuf
file_type: hadith-corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE
---

# Q 12 Yūsuf — Ḥadīth Corpus

This file indexes ḥadīth from the canonical 9 books that cite Q 12, the prophet Yūsuf, or related themes (the *aḥsan al-qaṣaṣ* tradition, the *karīm ibn al-karīm* chain, the "half of beauty" tradition, the famine-of-Yūsuf invocation, and Surah-Yūsuf-recitation reports).

**Source**: `/Users/grey/Downloads/quran/data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` (sunnah.com-derived). All ḥadīth IDs given are *idInBook* (sunnah.com book-numbering). Search performed 2026-04-28 with regex over Arabic and English fields.

## 1. The "*al-karīm ibn al-karīm ibn al-karīm ibn al-karīm*" tradition (Yūsuf's nobility chain)

This is the iconic ḥadīth most-cited for Q 12. The Prophet ﷺ, when asked about the "noblest of people", named Yūsuf with a four-generation pedigree.

### Ṣaḥīḥ al-Bukhārī

**Bukhārī #3243** (*Kitāb al-anbiyāʾ*, ch 60):

> The Prophet (ﷺ) said: "The honorable, the son of the honorable, the son of the honorable, (was) Joseph, the son of Jacob, the son of Isaac, the son of Abraham."

Arabic (from `bukhari.json` `idInBook=3243`):
> حَدَّثَنَا إِسْحَاقُ بْنُ مَنْصُورٍ، أَخْبَرَنَا عَبْدُ الصَّمَدِ، حَدَّثَنَا عَبْدُ الرَّحْمَنِ بْنُ عَبْدِ اللَّهِ، عَنْ أَبِيهِ، عَنِ ابْنِ عُمَرَ ـ رضى الله عنهما...

Isnād: ʿAbd al-Raḥmān b. ʿAbd Allāh ← his father (ʿAbd Allāh) ← Ibn ʿUmar ← the Prophet ﷺ. Ṣaḥīḥ.

**Bukhārī #3251** (*Kitāb al-anbiyāʾ*, ch 60), parallel via Ibn ʿUmar:

> The Prophet (ﷺ) said, "The honorable, the son of the honorable, the son of the honorable, (was) Joseph, the son of Jacob, the son of Isaac, the son of Abraham."

**Bukhārī #4482** (*Kitāb al-tafsīr*, ch 65, on Q 12 directly):

> The Prophet (ﷺ) said, "The honorable, the son of the honorable, the son of the honorable, i.e. Joseph, the son of Jacob, the son of Isaac, the son of Abraham."

**Bukhārī #3215, #3235, #3244** (*Kitāb al-anbiyāʾ*, ch 60, via Abū Hurayra):

The variant chain via Abū Hurayra:
> "The people said, 'O Allah's Messenger! Who is the most honorable amongst the people (in Allah's Sight)?' He said, 'The most righteous amongst them.' They said, 'We do not ask you about this.' He said, 'Then Joseph, Allah's Prophet, the son of Allah's Prophet, the son of Allah's Prophet, the son of Allah's Khalil (i.e. Abraham).'"

This is the *interrogated* form of the same tradition, specifying the four-generation chain.

### Cross-attestation
- Bukhārī #4483 (*Kitāb al-tafsīr*) repeats the Abū Hurayra version in the tafsīr-on-Q-12 section.
- Wide attestation across al-Ṭabarānī, al-Bayhaqī, and others (extra-9-books) is reported in classical tafsir but not in our 9-books extraction.

**Verdict on this tradition**: Locked-in ṣaḥīḥ chain via Bukhārī (multiple isnād-paths: Ibn ʿUmar AND Abū Hurayra). The four-generation noble-prophet-pedigree is **the Prophet ﷺ's own tafsīr-key** for the Yūsuf narrative — the surah's protagonist is uniquely positioned as the convergence of four prophetic generations. This is theologically the deepest *aḥsan al-qaṣaṣ* gloss the Prophet himself supplied.

## 2. The "half of all beauty" (*shaṭr al-ḥusn*) tradition

The classical tradition is that during the Isrāʾ wa-Miʿrāj, the Prophet ﷺ saw Yūsuf in the third heaven and said he had been given **half of all beauty** (*shaṭr al-ḥusn*).

### Audit of the in-archive 9 books

A regex search across all 9 canonical books in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` for:
- Arabic: `شطر الحسن`, `شطر`, `يوسف.*الحسن`
- English: `half of beauty`, `half the beauty`

returned **0 hits**. The "half of beauty" wording is **not present in this archive's 9 canonical books extraction**.

### What IS in the 9 books re: Yūsuf and beauty

The Isrāʾ ḥadīth in **Bukhārī (long form, multiple parallels) and Muslim (#315 ff.)** describes the Prophet's encounter with the prophets in the heavens, including Yūsuf in the third heaven. The English text in `muslim.json` `idInBook=315` (Isrā ḥadīth via Anas):
- Joseph is mentioned as one of the prophets the Prophet ﷺ met during the ascent.
- The specific descriptor *shaṭr al-ḥusn* is **not** present in the matched English snippet.

### Provenance of the "*shaṭr al-ḥusn*" wording

The wording *uʿṭiya shaṭr al-ḥusn* ("he was given half of [all] beauty") is most precisely attested in **Ṣaḥīḥ Muslim** (Kitāb al-īmān, the long Isrāʾ via Anas — typically Muslim ḥadīth #162 / #259 / #261 in some chapter-numberings; in the sunnah.com numbering used by AhmedBaset, the Isrāʾ ḥadīth is at *idInBook* 315–319 area). The specific *shaṭr al-ḥusn* clause is a **textually-variable element** across ḥadīth-collections; some recensions include it, others omit it. al-Nawawī's commentary on Muslim affirms the *shaṭr al-ḥusn* wording.

**Honest verdict**: The "half of beauty" tradition is **classical and widely attested**, particularly in al-Nawawī's *Sharḥ Muslim* and al-Bayhaqī's *Dalāʾil al-nubuwwa*. Within the *current local 9-books JSON archive*, however, the *shaṭr al-ḥusn* wording is NOT present in the searchable text — the more-elaborate Isrāʾ recensions that include this clause are likely in extra-9-books collections (al-Bayhaqī, al-Ṭabarānī, ʿAbd al-Razzāq's *Muṣannaf*).

**Audit verdict (this project)**: **DATA-GAP**. The tradition is real and classically grounded, but the precise *shaṭr al-ḥusn* wording requires a non-9-books source-extraction that is not currently in our local literature archive. Flagged for follow-up source-acquisition. The *aṣl* (substance) of Yūsuf's exceptional beauty is unambiguously locked in via Q 12:31 itself (the women cutting their hands at the sight of him) and the multiple-Bukhārī Isrāʾ ḥadīth.

## 3. The "Surah Hūd and Surah Yūsuf" recitation hadith

The Prophet ﷺ was asked by a man (`ʿUqba b. ʿĀmir`, by widely-cited isnād) to teach him **Surah Hūd** and **Surah Yūsuf**.

### Sunan al-Nasāʾī

**Nasāʾī #955**:

> "I followed the Messenger of Allah (ﷺ) when he was riding, and I placed my hand on his foot and said: 'O Messenger of Allah, teach me Surah Hud and Surah Yusuf.' He said: 'You will never recite anything more precious before Allah than [...]'."

**Nasāʾī #5448** (variant):

> "I came to the Messenger of Allah while he was riding, and I put my hand on his foot and said: 'Teach me Surah Hud, teach me Surah Yusuf.' He said: 'You will never recite anything more precious before Allah than [...]'."

**Note**: the conclusion of the ḥadīth in both Nasāʾī parallels is that the Prophet ﷺ then taught the man **the muʿawwidhāt** (Q 113 + Q 114), not Surah Hūd or Surah Yūsuf. The *fadāʾil* implication for Q 12 is **indirect**: the surah was recognized as a major-recitation surah during the Prophet's lifetime, but the specific *fadāʾil* response that the man received was the muʿawwidhāt's superior protective virtue. This is consistent with the *dual-iʿjāz typology* finding ([[h-new-840-unified-architectural-score]], [[h-new-860-hadith-architectural-alignment]]): the muʿawwidhāt sit at the *theological-iʿjāz / fadāʾil-iʿjāz* axis, not the structural-iʿjāz axis where Q 12 ranks high.

## 4. The "famine of Yūsuf" invocation tradition

The Prophet ﷺ invoked against the polytheists of Quraysh: "*allāhumma ājʿalhā ʿalayhim sinīna ka-sinī Yūsuf*" — "O Allah, make their years like the years of [the famine of] Yūsuf."

### Ṣaḥīḥ Muslim
- **Muslim #1435**, **#1436**, **#1437**, **#1438** (*Kitāb al-masājid wa-mawāḍiʿ al-ṣalāh*, ch 5): all parallel reports of the same tradition with variant wordings:
  - #1435: "...and cause them a famine (which broke out at the time) of Joseph..."
  - #1436: "...And cause them a famine like that (which broke out at the time) of Joseph..."
  - #1437: "...cause them a famine like that (which was caused at the time) of Joseph..."
  - #1438: variant chain.

### Ṣaḥīḥ al-Bukhārī
- **Bukhārī #4487** (*Kitāb al-tafsīr*, ch 65): "Allah! Protect me against their evil by afflicting them with seven (years of famine) like the seven years of (Prophet) Joseph." So they were struck (with famine).

This tradition has direct **textual ground** in Q 12: the seven-year drought that Yūsuf forecast from Pharaoh's dream (vv. 47–48). The Prophet ﷺ used the historical-famine as an invocational template — the explicit citation of Yūsuf-narrative within the prophetic ḥadīth corpus is one of the strongest *intra-Quranic* cross-references in the canon.

## 5. The "if I were in prison the time Yūsuf was..." tradition

### Ṣaḥīḥ al-Bukhārī
- **Bukhārī #3248** (*Kitāb al-anbiyāʾ*, ch 60):

> "May Allah bestow His Mercy on Lot. He wanted to have a powerful support. If I were to stay in prison (for a period equal to) the stay of Joseph (in prison) and then the offer of freedom came to me, then I would have accepted it (without delay)."

- **Bukhārī #4488** (*Kitāb al-tafsīr*, ch 65, on Q 12): same tradition restated in tafsīr context.

This ḥadīth comments **directly on the Yūsuf narrative**. It interprets v. 50–53 (Yūsuf's reluctance to accept exoneration before the king investigates the women's claims): the Prophet ﷺ says he himself would have accepted exoneration immediately. This is a remarkably **self-effacing prophetic gloss on Yūsuf's superior patience** — the Prophet ﷺ explicitly defers to Yūsuf's higher rank in patient endurance.

This ḥadīth is a **gold-standard intra-Quranic cross-reference**: the Prophet ﷺ ﺑreads Yūsuf's behavior (v. 50) against his own and concludes Yūsuf's was greater. Theologically, this anchors the surah's epithet *aḥsan al-qaṣaṣ* in part on Yūsuf's *ṣabr-min-al-ṣabr* (patience-beyond-patience).

## 6. ʿĀʾisha's reference to Yūsuf in the *ifk* (slander) hadith

### Ṣaḥīḥ al-Bukhārī
- **Bukhārī #2556** (*Kitāb al-shahādāt*, ch 52), **#3969** (*Kitāb al-maghāzī*, ch 64), **#4544** (*Kitāb al-tafsīr*, ch 65), **#4551**: the *ḥadīth al-ifk* — ʿĀʾisha narrating her ordeal of being slandered. ʿĀʾisha herself invoked the words of Yaʿqūb (Q 12:18 / 12:83):

> "By Allah, I don't compare my situation with you except to the situation of Joseph's (i.e. Yaʿqūb's response in Q 12:18). I will say what Joseph's father said: 'So (for me) patience is most fitting [fa-ṣabrun jamīl]. And it is Allah Whose help can be sought against that which you assert.'"

This is a **scriptural performative**: ʿĀʾisha responds to her false accusation by direct citation of Q 12:18. The *fa-ṣabrun jamīl* refrain (vv. 18, 83) thus has a Prophetic-household intra-Quranic afterlife.

## 7. Summary table

| Tradition | Primary collection | ID | Strength | Empirical correlate |
|:--|:--|:--:|:--:|:--|
| *al-karīm ibn al-karīm* (4-gen pedigree) | Bukhārī | #3243, #3251, #4482; #3215, #3235, #3244, #4483 (Abū Hurayra) | ṣaḥīḥ, multiple-isnād | Q 12's protagonist is uniquely 4-generation prophet — supports the *aḥsan al-qaṣaṣ* claim's content-vector |
| *shaṭr al-ḥusn* (half of beauty) | Muslim Isrāʾ tradition (extra-text expansions: Bayhaqī, Nawawī's commentary) | not in 9-books JSON | classical, source-gap in our archive | direct gloss on Q 12:31 |
| Surah Hūd + Surah Yūsuf request | Nasāʾī | #955, #5448 | (response defers to muʿawwidhāt) | Q 12 not in *fadāʾil*-top-tier; consistent with [[h-new-860-hadith-architectural-alignment]] |
| Famine-of-Yūsuf invocation | Bukhārī, Muslim | Bukh #4487; Muslim #1435–1438 | ṣaḥīḥ, multiple-isnād | direct textual import from Q 12:47–48 |
| Yūsuf's prison vs. Prophet's | Bukhārī | #3248, #4488 | ṣaḥīḥ | Prophet's gloss on Q 12:50: Yūsuf > Prophet in this domain |
| ʿĀʾisha in *ḥadīth al-ifk* citing Q 12:18 | Bukhārī | #2556, #3969, #4544, #4551 | ṣaḥīḥ | scriptural performative use of Q 12:18 |

## 8. Asbāb al-nuzūl (occasion of revelation)

al-Wāḥidī's *Asbāb al-nuzūl* (the standard reference): Q 12 was revealed in Mecca, after the Companions asked the Prophet for narrative. Some traditions report the revelation came after Jewish converts of Madīna asked the Prophet about Yūsuf. The 9-books JSON archive does not contain a dedicated Q 12 asbāb extraction (the available `asbab-nuzul-wahidi-en-Q002.txt` covers Q 1–Q 2 only). For Q 12 specifically, the asbāb material is broadly attested in al-Ṭabarī and al-Suyūṭī's *Lubāb al-nuqūl*; flagged for follow-up local source-extraction.

## 9. Honest limits

- The 9-books JSON regex search uses Arabic and English string-match. It misses ḥadīth that reference Q 12 *implicitly* (e.g. by quoting a Q 12 verse without naming the surah). A more thorough audit would require rooting on Q 12 verse-text matches against the full ḥadīth-text corpus.
- The *shaṭr al-ḥusn* tradition is real and classically locked but **not findable** in the current JSON archive. Source-acquisition flagged.
- Bukhārī attestations are densely concentrated in *Kitāb al-anbiyāʾ* (Book 60) and *Kitāb al-tafsīr* (Book 65, on Q 12) — entries #3215, 3235, 3243-3251, 4482-4488. This concentration is itself the empirical content of "Q 12 is heavily commented in canonical ḥadīth", which is consistent with the surah's classical status.

## 10. Cross-references

- [[h-new-860-hadith-architectural-alignment]] — Q 12's *fadāʾil*-rank vs UAS-rank (UAS top-10 but *fadāʾil* mid-tier; consistent with structural-not-theological-iʿjāz).
- `03-tafsir-survey.md` §8.1 (the 4-generation pedigree as classical *aḥsan al-qaṣaṣ* gloss).
- `05-classical-claims-audit.md` §5 (audit of the *shaṭr al-ḥusn* tradition).
- `data/literature/classical-tafsir/classical-on-yusuf-sijn.md` (post-classical novel observation: s-j-n = 12 in Surah 12).
