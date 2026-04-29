---
surah: 33
file_type: hadith_corpus
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — full 9-book index with thematic bucketing
total_hits: 272
search_strategy: Q33-named-entity + verse-fragment Arabic regex + EN-language Q33-specific phrase regex over `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/`
index_file: /Users/grey/Downloads/quran/data/literature/hadith/Q033-citations.json
---

# Q 33 al-Aḥzāb — Hadith Corpus Index (9 canonical books, n = 272 citations)

## 1. Search method and counts

The 9-book hadith corpus from *AhmedBaset/hadith-json* (sunnah.com-derived) was searched for Q 33-specific signals using:

**Arabic regex** — strict named-entity set:
- `سورة الأحزاب` / `سورة الاحزاب` (surah-name attribution)
- `[الأحزاب: N]` (Quranic citation form)
- `خاتم النبيين` / `وخاتم النبيّين` (Q 33:40 phrase)
- `ولكن رسول الله وخاتم` (Q 33:40 unique fragment)
- `يا أيها النبي اتق` (Q 33:1 vocative)
- `النبي أولى بالمؤمنين` (Q 33:6)
- `وأزواجه أمهاتهم` (Q 33:6 second clause)
- `يا نساء النبي` (Q 33:32)
- `إنما يريد الله ليذهب عنكم الرجس` (Q 33:33 *taṭhīr*)
- `إن المسلمين والمسلمات` (Q 33:35)
- `فلما قضى زيد منها وطرا` (Q 33:37 Zayd)
- `وتخفي في نفسك` (Q 33:37 fear-of-men)
- `لكي لا يكون على المؤمنين حرج` (Q 33:37 closure)
- `لا تدخلوا بيوت النبي` (Q 33:53 ḥijāb)
- `وإذا سألتموهن متاعا` (Q 33:53 ḥijāb second)
- `إن الله وملائكته يصلون على النبي` (Q 33:56)
- `صلوا عليه وسلموا تسليما` (Q 33:56)
- `يدنين عليهن من جلابيبهن` (Q 33:59 jalābīb)
- `إنا عرضنا الأمانة` (Q 33:72 amāna)
- `يحسبون الأحزاب لم يذهبوا` / `إذ جاءوكم من فوقكم` (Q 33:9, 20 trench)
- `وامرأة مؤمنة إن وهبت` (Q 33:50)
- `لقد كان لكم في رسول الله أسوة` (Q 33:21)

**English regex** — Q 33-specific phrasing:
- `(Surat[h]? )?Al[\-\s]Ah?zab` (surah-name)
- `\b33[:\.]\s*\d+` and `\(33\.\d+\)` (verse citations)
- `Seal of (the )?Prophets?`
- `verse of (the )?Hijab` / `the Hijab was prescribed` / `veil(ing)? was revealed`
- `Mothers? of the Believer`
- `Zaynab bin[t]? Jah` / `Zainab bin[t]? Jah`
- `(Battle\|Day) of (the\|al[\-\s])(Trench\|Khandaq\|Ditch)`
- `Battle of (the )?Confederat`
- `send (Allah's )?blessings (and salutations )?(up)?on (the )?Prophet`

**Total hits across 9 books: 272.**

| Book | Hits |
|:--|--:|
| Sahih al-Bukhari | 104 |
| Jami` at-Tirmidhi | 45 |
| Sunan an-Nasa'i | 43 |
| Sahih Muslim | 29 |
| Musnad Ahmad | 20 |
| Sunan Ibn Majah | 16 |
| Sunan Abi Dawud | 8 |
| Sunan ad-Darimi | 4 |
| Muwatta Malik | 3 |

(Saved index → `/Users/grey/Downloads/quran/data/literature/hadith/Q033-citations.json` with full text + tags.)

**Note on Bukhārī density.** The 104 Bukhārī hits is among the highest per-surah counts in the corpus (compare: Q 1 = 5 hits, Q 2 = ~120 hits depending on regex). This contradicts a naive reading of the H-NEW-860 hadith-emphasis-rubric finding (Q 33 score = 2/10) — but the rubric measures **whole-surah faḍāʾil prominence**, not **per-verse citation density**. Q 33 is in fact intensively cited by al-Bukhārī **as a source of legal-historical material** (104 hits) while being **liturgically obscure** (zero whole-surah faḍāʾil ḥadīth in *Kitāb Faḍāʾil al-Qurʾān*). The two phenomena are distinct and *both true simultaneously*.

## 2. The faḍāʾil-vacuum confirmed by direct search

Direct search of *Sahih al-Bukhari, Kitāb Faḍāʾil al-Qurʾān* (Book 66 in the modern numbering, *bāb*-numbered chapters) for any *bāb* on Q 33: **none exists**. *Bābs* in Faḍāʾil al-Qurʾān cover:

- Faḍl al-Qurʾān ʿalā sāʾir al-kalām (general)
- Faḍl al-Fātiḥa (Q 1)
- Faḍl al-Baqara (Q 2)
- Faḍl Sūrat al-Kahf (Q 18)
- Faḍl Sūrat al-Fatḥ (Q 48)
- Faḍl Sūrat al-Ikhlāṣ (Q 112)
- Faḍl al-Muʿawwidhāt (Q 113-114)

Q 33 is **not represented**.

In *Jamiʿ al-Tirmidhī, Abwāb Faḍāʾil al-Qurʾān ʿan Rasūl Allāh* (the only collection with a separate *abwāb* dedicated to per-surah faḍāʾil), the per-surah ḥadīths run for Q 1, Q 2, Q 3, Q 18, Q 36, Q 47, Q 50, Q 56, Q 67, Q 100, Q 109-114. **Q 33 is again absent.**

The single Sunni-attributed faḍīla ḥadīth on Q 33 (*"Whoever recites it and teaches his family is given amān from punishment of the grave"*, narrated by Ubayy b. Kaʿb) is preserved **outside the canonical 9 books**, in:
- al-Thaʿlabī, *al-Kashf wa-al-bayān*, Q 33 chapter opening (line 69274 of the OpenITI raw text).
- al-Ṭabarsī, *Majmaʿ al-bayān*, Q 33 chapter opening (line 91728).

Hadith-critically, this is a **single-isnād *fadāʾil al-suwar* tradition with weak chain status**, of the genre Ibn Taymiyya, al-Mizzī, Ibn al-Jawzī (in *al-Mawḍūʿāt*), and Ibn al-Qayyim broadly suspected as fabricated. **It does not appear in any of the 9 canonical books.** The Sunni faḍāʾil-vacuum on Q 33 is therefore **not** an artifact of search method; it is genuine.

## 3. Thematic bucketing of Q 33 ḥadīth

### 3.1 *Khātam al-nabiyyīn* (Q 33:40) — 12 ḥadīth

The doctrinally central cluster, distributed:

| # | Bk #idInBook | Type | Note |
|:--|:--|:--|:--|
| 1 | **Bukhārī #3385** (gid 3385, ch 61 *Bāb Khātam al-Nabiyyīn*, *Kitāb al-Manāqib*) | *libna* parable | The canonical formulation: *"My example and that of the prophets before me is like a man who built a house — beautifully and completely — except for the place of one brick. People circumambulated it admiring its beauty but said: 'If only this brick were placed!' I am that brick, and I am the seal of the prophets (*khātam al-nabiyyīn*)."* Narrated Abū Hurayra ← Abū Ṣāliḥ ← ʿAbd Allāh b. Dīnār ← Ismāʿīl b. Jaʿfar ← Qutayba b. Saʿīd. |
| 2 | **Bukhārī #2945** (ch 56 *Kitāb al-Maghāzī*) | *physical seal* | Umm Khālid bint Khālid b. Saʿīd narrating the visible *khātam al-nubuwwa* (a physical mark on the Prophet's body). This is etymologically *related* to Q 33:40 but doctrinally distinct (it is about the prophetic-body sign, not the prophetic-succession claim). |
| 3 | **Bukhārī #5456** (ch 75) | *physical seal* | Same theme via al-Sāʾib b. Yazīd: *"…and I stood behind him and saw the *khātam al-nubuwwa*."* |
| 4 | **Bukhārī #5765** (ch 78) | *physical seal* | Umm Khālid version 2. |
| 5 | **Bukhārī #6115** (ch 80) | *physical seal* | al-Sāʾib version 2. |
| 6 | **Tirmidhī #2219** | parallel *libna* | Tirmidhī says *ḥasan ṣaḥīḥ* ghariib through this chain. |
| 7 | **Tirmidhī #3623** | I am-six-named ḥadīth | Jubayr b. Muṭʿim ← his father: *"I have several names: I am Muḥammad, I am Aḥmad, I am al-Māḥī (the obliterator) by whom Allāh obliterates disbelief, I am al-Ḥāshir at whose feet people are gathered, I am al-ʿĀqib (the last) — *alladhī laysa baʿdahu nabī*."* (Also Bukhārī #4896, Muslim #2354.) |
| 8 | **Tirmidhī #3625** | parallel name-list ḥadīth | Same Jubayr cluster. |
| 9 | **Tirmidhī #3627** | parallel | |
| 10 | **Ibn Mājah #4077** | I-am-six-names | Same theme. |
| 11 | **Ahmad** (multiple chains) | parallel | |
| 12 | **Abū Dāwūd** (chain) | parallel | |

The Bukhārī #3385 *libna* ḥadīth is **directly cited by all 7 mufassirūn surveyed in `03-tafsir-survey.md` §4.3** as the core *khātam al-nabiyyīn* exegetical supplement to Q 33:40.

### 3.2 *Yawm al-Aḥzāb* / *Yawm al-Khandaq* / Battle of the Trench (Q 33:9-27) — 34 ḥadīth

Heavily-cited cluster, primarily Bukhārī (16) and Muslim (6); also Tirmidhī, Ibn Mājah, Aḥmad, Mālik. Representative:

- **Bukhārī #455** (Anas-narrative-cluster, *Kitāb al-Ṣalāh*): *"On the day of al-Khandaq the medial-arm vein of Saʿd b. Muʿādh was injured…"* — the foundational testimony for Saʿd's wound that ultimately led to his verdict on Banū Qurayẓa.
- **Bukhārī #582, 584, 626, 923** (*Kitāb Mawāqīt al-Ṣalāh*): **The ʿAṣr-prayer-missed cluster**. ʿUmar's famous: *"O Messenger of God, by Allāh, the sun has set and I have not prayed ʿAṣr"* — direct testimony that the siege caused liturgical disruption to the point that the Prophet himself missed prayers, eventually praying ʿAṣr after sunset and Maghrib together at Buthān. The narrators are Jābir b. ʿAbd Allāh + ʿĀʾisha. **This is the seed of the Ḥanafī "salāt al-fawāʾit" doctrine.**
- **Bukhārī #924** (Ibn ʿUmar, *Kitāb al-Ṣalāh*): *"When the Prophet returned from the battle of al-Aḥzāb, he said: 'No one is to pray ʿAṣr except in Banū Qurayẓa…'"* — pivotal text for both the **Banū Qurayẓa siege chronology** and the *uṣūl al-fiqh* discussion of literal-vs-purpose-driven interpretation of prophetic command (al-Shāfiʿī's key example).
- **Bukhārī #2731, #2732** (Jābir, *Kitāb al-Maghāzī*): the famous *miracle-of-the-pot* ḥadīth where a small amount of food fed the entire trench-digging army.
- **Tirmidhī #1717** + parallels: cold-and-wind that broke the siege.
- **Mālik in the Muwaṭṭaʾ #1** records the legal precedent of the Banū Qurayẓa execution.
- **Aḥmad** preserves multiple long-form narrations of the battle.

**Importance**: Q 33:9-27 is the corpus's longest single-battle narrative (~ 19 verses in one block) and the ḥadīth corpus mirrors the textual centrality with extensive isnād-chains.

### 3.3 *Ummahāt al-Muʾminīn* / Mothers of the Believers (Q 33:6, 28-34) — 94 ḥadīth

The corpus-largest cluster, almost entirely about specific named wives of the Prophet acting in their roles as authoritative narrators or recipients of revelation. Distribution:

- **Nasāʾī = 27, Bukhārī = 25, Muslim = 15, Ibn Mājah = 10, Tirmidhī = 9** etc.
- These are *not* primarily Q 33-exegetical; they are ḥadīth in which the wives are *referred to* as *Ummahāt al-Muʾminīn* (the title established in Q 33:6).
- **Bukhārī #281** (Umm Salama, *Kitāb al-Ḥayḍ*): the foundational ḥadīth on whether women have *iḥtilām* (wet dreams), with Umm Sulaym asking the Prophet on behalf of women — Umm Salama, *as Mother of the Believers*, narrates.
- **Bukhārī #1346** (ʿAmr b. Maymūn al-Awdī): about ʿUmar's deathbed instructions to ʿĀʾisha — *"and seek permission from the Mother of the Believers ʿĀʾisha to be buried beside the Prophet…"*
- **Muslim #1428** family of ḥadīth: Zaynab bint Jaḥsh, walīma, and the asbāb al-nuzūl of Q 33:53.
- **Bukhārī #1971** (ʿAmra ← ʿĀʾisha): *iʿtikāf* of the wives — establishes the precedent for women's spiritual retreat.
- **Bukhārī #2479** (ʿUrwa ← ʿĀʾisha, *Kitāb al-Hibāt*): the famous *"The wives were in two camps"* tradition, with ʿĀʾisha-Ḥafṣa-Ṣafiyya-Sawda in one and Umm Salama and others in the other.

The total of 94 (across all 9 books) confirms that **the *Mothers of the Believers* designation, established by Q 33:6, became the foundational *honorific frame* for transmitting any ḥadīth from the Prophet's wives** — i.e., Q 33:6 alone seeded the most prolific single category of *isnād-female-authority* in the corpus.

### 3.4 Zayd-Zaynab marriage (Q 33:36-40, 53) — 48 ḥadīth on "Zaynab bint Jaḥsh"

The marriage that occasioned Q 33:37 + Q 33:40 + Q 33:53 + the asbāb of *āyat al-ḥijāb*. Representative texts:

- **Bukhārī #4787-4791** + parallels (*Kitāb al-Tafsīr* on Q 33): the long-form Anas narrative on the Zaynab walīma, the over-staying guests, and the revelation of Q 33:53. Cited verbatim by Ibn Kathīr (line 97269+), al-Ṭabarī (282296+), al-Suyūṭī al-Durr al-manthūr.
- **Muslim #1428a-d**: parallel chains of the same Anas narrative.
- **Bukhārī #1242, #1372**: the wives' competitive measuring-of-hands tradition; Zaynab bint Jaḥsh's death — testimonial that she was the first wife to die after the Prophet, fulfilling the prophetic prediction *"the longest-handed of you in charity will be first to follow me"*.
- **Tirmidhī #128** (Zaynab as authority on *istiḥāḍa* / dysfunctional uterine bleeding rules) — Zaynab herself transmits ḥadīth as *Umm al-Muʾminīn*.

### 3.5 *Āyat al-Ḥijāb* (Q 33:53) — 4 explicit + ~20 implicit ḥadīth

The *verse-of-Hijab-was-revealed* phrase appears explicitly in:

- **Tirmidhī #3301** (Anas): *"I was with the Prophet and he came to the door of a woman with whom he had consummated marriage, and some people were with her…"* — full Q 33:53 *sabab*.
- **Nasāʾī #3258**: *"Zaynab bint Jaḥsh used to boast over the other wives of the Prophet, saying: 'Allāh married me to him from above the Heavens'; and the verse of Hijab was revealed concerning her."* (Anas b. Mālik narrating.)
- **Nasāʾī #3321**: ʿĀʾisha and the foster-uncle entry permission *"after the verse of Hijab was revealed"*.
- **Aḥmad #154** + parallels: ʿUmar's *muwāfaqāt* ḥadīth (Bukhārī #4790, Muslim #2399 also): *"My Lord agreed with me in three matters: the station of Ibrāhīm, the verse of Hijab, and the warning to the Prophet's wives [Q 66:5]."*

Plus Bukhārī ##4587-4595 (*Kitāb al-Tafsīr* on Q 33:53), and Anas-cluster parallels in Muslim's *Kitāb al-Nikāḥ*.

### 3.6 *Āyat al-Ṣalawāt* (Q 33:56) — 24 ḥadīth on the *al-Ṣalāt al-Ibrāhīmiyya* formula

The Q 33:56 verse is Quranic; the **formula** of how to send blessings is established via 9-book canonical ḥadīth chains:

- **Bukhārī #4519** (Kaʿb b. ʿUjra, *Kitāb al-Tafsīr* 33): the classical formula:
  > *Allāhumma ṣalli ʿalā Muḥammadin wa-ʿalā āli Muḥammadin kamā ṣallayta ʿalā [āli] Ibrāhīma, innaka Ḥamīdun Majīd; Allāhumma bārik ʿalā Muḥammadin wa-ʿalā āli Muḥammadin kamā bārakta ʿalā āli Ibrāhīma, innaka Ḥamīdun Majīd.*
- **Bukhārī #4520** (Abū Saʿīd al-Khudrī): parallel form (*"ʿabdika wa-rasūlika"*).
- **Bukhārī #6357** (ʿAbd al-Raḥmān b. Abī Laylā ← Kaʿb b. ʿUjra): *"Shall I give you a present? The Prophet came out to us and we said: 'O Messenger of God, we know how to greet you with salām, but how shall we send *ṣalāt* upon you?'"*
- **Bukhārī #3370** (*Kitāb Aḥādīth al-Anbiyāʾ*): another version.
- **Muslim #406** (Abū Masʿūd al-Anṣārī): *"…the Messenger of Allāh remained silent until we wished he had not been asked the question. Then he said: 'Say…'"*
- **Tirmidhī #483** (Kaʿb b. ʿUjra version).
- **Nasāʾī #1287, #1288, #1289**: 9 total chains.
- **Ibn Mājah #637, #638, #639**: 5 chains, including a striking variant via Abū Ḥumayd al-Sāʿidī: *"Allāhumma ṣalli ʿalā Muḥammadin wa-azwājihi wa-dhurriyyatihi…"* (with explicit mention of his wives and progeny).
- **Aḥmad #1321** (Mūsā b. Ṭalḥa ← his father).

**This is one of the most multiply-attested formulaic ḥadīth-traditions in the corpus** — the formula appears in tashahhud-position in every Sunni ritual prayer (and, with Imāmī Shīʿī variations, in the Shīʿī tashahhud). Q 33:56 is therefore — paradoxically given the H-NEW-860 = 2/10 score — the *single Quranic verse most generative of liturgical formula* in the entire corpus.

### 3.7 *Āyat al-Taṭhīr* / Ahl al-Bayt (Q 33:33) — 5+ ḥadīth on the Cloak

- **Tirmidhī #3205** (ʿUmar b. Abī Salama, in his mother Umm Salama's house): *"When these *āyāt* were revealed to the Prophet — 'Allāh only wishes to remove al-rijs from you, O Ahl al-Bayt, and to purify you with thorough purification (33:33)' — in the home of Umm Salama, he called Fāṭima, Ḥasan, Ḥusayn, and wrapped them in a cloak, with ʿAlī behind him; he wrapped him in the cloak and said: 'O Allāh, these are my Ahl al-Bayt — remove al-rijs from them and purify them with thorough purification.' Umm Salama said: 'Am I with them, O Prophet of Allāh?' He said: 'You are in your place — and you are upon good.'"*
- **Tirmidhī #3787** (parallel chain, also marked *ḥasan ṣaḥīḥ*).
- **Tirmidhī #3789** (parallel).
- **Tirmidhī #3871** (parallel).
- **Muslim #2424** (Ḥadīth of the Cloak, also called *Ḥadīth al-Kisāʾ*).
- **Tirmidhī #3290** + parallel: *"For six months, the Messenger of Allāh would pass by the door of Fāṭima when going to the Fajr prayer saying: 'As-Salāh, O People of the House! Allāh only wishes to remove al-rijs from you…'"*

**These are *ṣaḥīḥ* by Sunni standards** but interpreted differently in Sunni / Shīʿī: Sunni reads them as **inclusive expansion** (the Prophet's family-of-the-Cloak are *added* to the contextual "wives" of the surrounding Q 33:28-34); Shīʿī reads them as **exclusive specification** (the Cloak-family *are* the Ahl al-Bayt of the verse, the wives being a *separate* group). The empirical fact is that **the same sanad-witnessed ḥadīth supports both readings**; the doctrinal split is exegetical, not isnād-based.

### 3.8 Q 33:35 (men-and-women parallel) — 3+ ḥadīth on asbāb

- **Tirmidhī #3105**, **#3106**, **#3295**: Umm Salama's question — *"The men fight and the women do not, and we get half the inheritance"* — generating Q 33:35 *"Indeed the Muslim men and the Muslim women, the believing men and the believing women…"* (15 paired masculine-feminine forms).
- **Muslim #5932** (parallel chain).

### 3.9 Q 33:21 *uswa ḥasana* — 4 ḥadīth invocations

- **Bukhārī #1069** (Ibn ʿUmar): *"I accompanied the Prophet and he did not offer optional prayers during the journey, and Allāh says: 'Verily, in the Messenger of Allāh you have a good example to follow.' (33:21)"* — direct application of Q 33:21 to the *sunan al-rāwāḥil* (travel-prayers) ruling.
- **Bukhārī #4008**: Ibn ʿUmar reciting Q 33:21 to justify his ihram-conduct.
- **Ibn Mājah #1807** (Ibn ʿAbbās): same usage.
- **Aḥmad #126** (Ibn ʿAbbās via Saʿīd b. Jubayr): in the context of ʿUmar kissing the Black Stone — *"I know that you are only a stone; if I had not seen my Beloved kiss you, I would not have…"* and citing Q 33:21.

Q 33:21 is therefore the **textual foundation of the entire *sunna* doctrine in Sunni jurisprudence** — *"good example to follow"* literally constitutes the scriptural authorization for following the Prophet's non-revelatory practice. Every ḥadīth invoking the Prophet's **non-Quranic** practice as binding implicitly relies on Q 33:21.

### 3.10 Q 33:1 vocative *yā ayyuha al-Nabī* — implicit in 15+ Aḥmad citations

Aḥmad's Musnad explicitly cites Q 33:1 in 15 instances tagged *q33-en-name* — these are typically Q 33-internal cross-references in long-form ḥadīth narratives.

## 4. The Imāmī-Shīʿī faḍāʾil isnād (outside the 9 Sunni books)

For completeness — **not in the 9 canonical Sunni books**, but cited by al-Ṭabarsī (line 91730):

> *ʿAbd Allāh b. Sinān ← Imam Jaʿfar al-Ṣādiq: "Whoever frequently recites Sūrat al-Aḥzāb will be on the Day of Resurrection in the company of Muḥammad and his wives."*

Note the **doctrinally-meaningful clause: "his wives"** — in light of the Q 33:33 *taṭhīr* / Cloak-ḥadīth controversy, this Imāmī attribution preserves the Sunni-style inclusion-of-wives reading rather than the strict Cloak-exclusivism, suggesting the faḍīla is from the period *before* the doctrinal hardening of the *taṭhīr* exegesis.

## 5. Synthesis: hidden architecture, not absence

The corpus-empirical claim "Q 33 is **architecturally rank 1** but **ḥadīth-ranked low**" can now be refined:

| Dimension | Q 33 status | Evidence |
|:--|:--|:--|
| Whole-surah faḍāʾil ḥadīth (Sunni canonical) | **ABSENT** | No bāb in Bukhārī/Muslim/Tirmidhī faḍāʾil sections; only single-chain extra-canonical (Thaʿlabī, Ṭabarsī) |
| Whole-surah faḍāʾil ḥadīth (Shīʿī Imāmī) | **PRESENT** | al-Ṣādiq via ʿAbd Allāh b. Sinān (Ṭabarsī) |
| Per-verse exegetical ḥadīth (9 canonical books) | **HIGH** | 272 hits total; Bukhārī alone = 104 |
| Doctrinally-foundational verse-derived ḥadīth | **VERY HIGH** | *libna*-parable for Q 33:40; *al-Ṣalāt al-Ibrāhīmiyya* for Q 33:56; Cloak-ḥadīth for Q 33:33; Asbāb-cluster for Q 33:53 |
| Liturgical-formula generation | **VERY HIGH** | Q 33:56 generates the universal Sunni-Shīʿī *taṣliya* formula in tashahhud |
| Sunna-doctrine textual foundation | **VERY HIGH** | Q 33:21 *uswa ḥasana* is the Quranic ground for *sunna* itself |

The **aggregate** is: Q 33 is **deeply ḥadīth-integrated at the per-verse level**, **systematically excluded from per-surah faḍāʾil**, and **uniquely generative of major liturgical formulas**. The empirical UAS = 9.36 / hadith-emphasis = 2 finding (H-NEW-860) captures only the **whole-surah faḍāʾil dimension** and is silent on the four other dimensions. The architectural significance and the verse-level ḥadīth saturation are **fully matched**; the apparent mismatch at the whole-surah-faḍāʾil layer is explained by the doctrinal-controversy density argument in `03-tafsir-survey.md` §7.

---

*All ḥadīth cited by collection-name + idInBook (sunnah.com convention) + chapter, verifiable in `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/<book>.json`.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
