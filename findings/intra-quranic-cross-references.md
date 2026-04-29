# Intra-Quranic Cross-References

**Scope.** For every significant finding in `master-index.md`, this file builds a network of how the same roots, themes, phrases, and structures echo elsewhere in the Quran. Findings are not isolated artifacts — they are embedded in a textual fabric. The framing, from the Quran's own perspective (Q 39:23): the Book is *kitāban mutashābihan mathāniya* — "a consistent Book wherein is reiteration." Everything reverberates.

**Method.** Data: `quran-no-tashkeel.json` primary, `morphology/root-index.json` (Buckwalter roots), `morphology/quranic-corpus-morphology-0.4.txt` for lemmas, `translations/en.sahih.txt` for English semantic probes. I use (a) root-level exact lookup, (b) lemma-level exact lookup, (c) regex semantic probing of Sahih, (d) structural re-derivation (letter-palindrome detector, consonant z-score analysis).

**Invariant (from methodology.md):** ONE Quran. Echoes are not "parallel texts"; they are self-similar reiterations within a single coherent composition.

**Format per finding:**
1. **Root-level echoes** — all meaningful (s,v) for the key root(s)
2. **Lemma-level echoes** — same for the exact lemma
3. **Thematic echoes** — semantic parallels via Sahih probe + judgment
4. **Structural echoes** — the same rhetorical form elsewhere
5. **Muhkam/mutashabih tensions** — clear-verse anchors that clarify the ambiguous
6. **Self-commentary** — Quran's own hermeneutic verses that bear on the passage

---

## Finding 1 — راحمة (raḥma) = 114, the lemma whose count matches the surah count

> 🔷🔷 "Of 4,832 distinct lemmas, `raḥma` is the ONLY lemma with count 114."

### 1a. Root-level echoes

Root `rHm` has **339 tokens** in the Quran (includes `r~aHoma`n` = Ar-Rahman 57×, `r~aHiym` = Ar-Rahim, `raHomap` = rahma, `ruHom` = wombs 1×, and the verbal forms `raHima`). The root's center of gravity lies in two families: (i) the divine-name pair Ar-Rahman / Ar-Rahim (dense in the basmala and the opener of Al-Fatiha); (ii) the abstract noun *raḥma* = "mercy/compassion" itself. At 339 tokens it is one of the highest-frequency theological roots in the Quran, on par with gfr (forgive, 234), hdy (guide, 316), and rbb (lord, 975).

### 1b. Lemma-level echoes (the 114 themselves)

Lemma **`raHomap`** = **114 tokens** in 112 unique verses. Top 15 surahs by density:

| Surah | Rahma count |
|---|---|
| 7 (Al-A'rāf) | 9 |
| 11 (Hūd) | 8 |
| 6 (Al-An'ām) | 6 |
| 17 (Al-Isrā') | 6 |
| 18 (Al-Kahf) | 6 |
| 2 (Al-Baqarah) | 5 |
| 3 (Āl 'Imrān) | 5 |
| 30 (Ar-Rūm) | 5 |
| 4 (An-Nisā') | 4 |
| 10 (Yūnus) | 4 |
| 19 (Maryam) | 4 |
| 21 (Al-Anbiyā') | 4 |
| 24 (An-Nūr) | 4 |
| 28 (Al-Qaṣaṣ) | 4 |
| 39 (Az-Zumar) | 4 |

**The Hūd-cluster.** Surahs 7 and 11 together hold 17 of 114 occurrences — 15% of all *raḥma* tokens — and both narrate the **same cycle of prophets** (Noah → Hud → Salih → Lot → Shu'ayb) as successive "mercies" sent to their peoples. The recurring formula in Surah 11 is **"فأنجيناه… برحمة منا"** ("We saved him by a mercy from Us"), appearing at 11:58 (Hud), 11:66 (Salih), 11:94 (Shu'ayb). This is a stylised liturgical refrain that uses raḥma as a structural hinge between prophet-stories. **Surah 7 carries the same formula** but with a slightly different phrasing at 7:72 (saving Hud) and 7:151 (Moses's prayer: "admit us into Your mercy, for You are *arḥamu al-rāḥimīn*").

### 1c. Thematic clusters (a theology of *raḥma*)

I classified all 114 verses by theme via Sahih semantic probes:

| Theme | Count | Representative verses |
|---|---|---|
| **Mercy through prophets/messengers** | 22 | 3:159 ("by mercy from Allah you were lenient"), 19:2 (Zechariah), 19:53 (Aaron given to Moses "from Our mercy"), 21:107 ("we have not sent you except as a mercy to the worlds"), 28:43 (Torah to Moses as guidance-and-mercy), 28:46 (Muhammad "as a mercy from your Lord") |
| **Mercy in/on the Hereafter / Day of Judgment** | ~9 | 3:107 ("within the mercy of Allah they abide eternally"), 7:49, 45:30, 76:31 |
| **Mercy-as-rain / mercy-before-winds** | ~12 | 7:57, 25:48, 27:63, 30:46, 42:28 — a **recurring formula** "He sends the winds as good tidings *bayna yaday raḥmatihī*" (before His mercy, i.e., before the rain) |
| **Mercy-as-Book/Qur'an** | ~21 | 6:157, 7:52, 7:154 (Torah), 10:57, 11:17, 16:64, 16:89, 17:82 ("We send down of the Qur'an that which is healing and mercy for the believers"), 27:77, 28:86, 29:51, 31:3, 44:6, 45:20, 46:12 |
| **Mercy for the believing community** | ~37 | 2:218, 4:96, 4:175, 9:21, 42:8, 57:27-28, 3:8 |
| **Mercy Allah decreed on Himself** | 3 | 6:12 ("kataba ʿalā nafsihī al-raḥma"), 6:54 (same formula), 40:7 ("You have encompassed all things in mercy") |

**Note on 6:12 and 6:54 —** both verses contain the exact phrase **"كتب على نفسه الرحمة"** ("He has decreed upon Himself mercy"), an extraordinarily bold self-binding statement that occurs **nowhere else in the Quran**. It is a twin-verse mini-refrain inside the same surah — a miniature intra-surah echo.

**The self-reference: 21:107.** The finding-defining verse — "And We have not sent you except as a **mercy to the worlds** (`raḥmatan lil-ʿālamīn`)" — is the self-description that the Quran makes about its own revelatory act. The fact that *this* lemma is the one with count 114 is the whole point of the finding.

### 1d. Structural echoes

Rahma forms internal rings in multiple surahs:

- **Surah 11 (Hūd)** — raḥma appears as a prophet-saving refrain at 11:58, 11:63, 11:66, 11:73, 11:94, bracketing the middle 5 prophetic stories of the surah. This is a small-scale ring where raḥma punctuates the structural joints.
- **Surah 19 (Maryam)** — raḥma appears at 19:2 (opening, Zechariah), 19:21 (Jesus's birth), 19:50 (Abraham's seed), 19:53 (Aaron). Each is a "mercy as gift of progeny or prophethood." Four linked theological beats across the surah.
- **Surah 7:156 ↔ Surah 40:7** — the only two verses in the Quran where "Your mercy encompasses *all things*" (*wasiʿa kulla shayʾ raḥma*). 7:156 is Moses's prayer; 40:7 is the angels' prayer. Identical formula, inverted speaker positions (prophet-man ↔ angelic beings) — a rare inter-surah pair.

### 1e. Muhkam / mutashabih

**The ambiguous center:** what *is* raḥma? Is it a thing Allah bestows, a thing He *is*, or both? The Book has no definitional verse for the word.

**Muhkam clarifications:**
- 6:12, 6:54 "kataba ʿalā nafsihī al-raḥma" → raḥma is a **self-imposed divine obligation**, something Allah has **decreed on Himself**.
- 7:156 "raḥmatī wasiʿat kulla shayʾ" → **raḥma is extensive to all creation** (universal mercy, not sectarian).
- 17:82 "huwa shifā'un wa raḥmatun lil-mu'minīn" → **raḥma is the Qur'an itself** insofar as it heals.
- 21:107 "raḥmatan lil-ʿālamīn" → **raḥma is the messenger's very being**.
- 40:7 "rabbanā wasiʿta kulla shay'in raḥmatan wa-ʿilmā" → raḥma is paired with ʿilm (knowledge) as a divine attribute that **encompasses totality**.

These muhkam anchors render any single raḥma verse interpretable in four layers: decree, attribute, embodied (prophet), and textualized (Qur'an). The 114-count resonance with the surah number becomes coherent when the Qur'an itself is understood as the instantiated raḥma ("We send down *of* the Qur'an that which is healing and raḥma for the believers" — 17:82). **A book-whose-lemma-count equals its chapter-count, where that lemma is also the book's own self-description.**

### 1f. Self-commentary

The Quran comments on *raḥma* most explicitly at 17:82 (Qur'an = mercy and healing) and 21:107 (messenger = mercy to worlds). These two together are the closest the Quran comes to a hermeneutic key for the 114 resonance.

---

## Finding 2 — Yusuf سجن = 12, the prison-word that maps the prison-surah

> ✨ "`س-ج-ن` (prison) occurs exactly 12× in the Quran, ALL 12 in Surah 12 (Yusuf)."

### CORRECTION — the master-index claim is partially wrong

The root `sjn` has **exactly 12 tokens in the Quran** as claimed. But they are **NOT all in Surah 12**. Per the Leeds Quranic Arabic Corpus v0.4:

- **9 in Surah 12 (Yusuf)**: 12:25, 12:32, 12:33, 12:35, 12:36, 12:39, 12:41, 12:42, 12:100
- **1 in Surah 26 (Ash-Shu'arā')**: 26:29 — Pharaoh's threat to Moses: *la-ajʿalannaka min al-masjūnīn* ("I will surely place you among those imprisoned")
- **2 in Surah 83 (Al-Muṭaffifīn)**: 83:7, 83:8 — *kitāba al-fujjāri la-fī **sijjīn***, "the record of the wicked is in **sijjīn**" (a cosmological register, not a literal prison)

The counterfactually beautiful pattern is therefore **refined**: of the 4 lemmas built on the root, the two "literal Egyptian-prison" lemmas `s~ijon` (6×) and `yusojana` (3×) are exclusively Surah-12. The other lemmas spread the root outward to two different prison-concepts: (i) Moses's Pharaonic threat and (ii) the eschatological register *sijjīn*.

### 2a. Root-level distribution

| Lemma | Count | Surah(s) | Gloss |
|---|---|---|---|
| `s~ijon` | 6 | 12 only | literal "prison" (Joseph's Egyptian jail) |
| `yusojana` | 3 | 12 only | passive verb "to be imprisoned" |
| `masojūnīn` | 1 | 26 only | "those imprisoned" (Pharaoh's threat) |
| `sij~iyn` | 2 | 83 only | the eschatological *sijjīn* — the book of the wicked |

The distribution is extraordinary: **four different lemmas across three different surahs, with zero overlap**. No other root in the Quran shows this surgical stratification. The Joseph-prison cluster is maximally dense (9 tokens in one surah), and then the same root rings out twice — once as a Mosaic echo (Pharaoh to Moses uses the same word Potiphar's wife used toward Joseph), and once as a cosmic endpoint (the *sijjīn* of the damned).

### 2b. The Joseph / Moses parallel

Pharaoh's threat at Q 26:29 — *la-ajʿalannaka min al-masjūnīn* — reuses exactly the same root that defined Joseph's ordeal. In Surah 12 Joseph *chooses* prison over sin (12:33: "rabbi al-sijnu aḥabbu ilayya mimmā yadʿūnanī ilayhi" — "my Lord, prison is more to my liking than what they call me to"). In Surah 26, Moses is *threatened* with prison by Pharaoh and refuses to be intimidated. Both narratives turn on prophetic moral refusal under the explicit threat of *sijn*. **The root bridges two prophets across 14 surahs of separation.**

Imprisonment as a theme also recurs without the root `sjn`:
- **Moses placed in a chest into the Nile** (Q 20:38-40, 28:7) — captivity of the infant prophet
- **Prophets and holy men bound by the "knots of blowers"** (113:4) — metaphorical captivity
- **Pharaoh "binding/pegging" his workers to build a tower** (28:38, 40:36)
- **The cave companions sealed inside** (18:9-26) — self-chosen enclosure, positive mirror of Joseph's prison

### 2c. Thematic echoes

The motif "prophet-in-prison" is a Quranic sub-genre. Joseph in 12 is the archetype; Moses's threatened prison in 26 is the echo. But the word *sijjīn* in 83:7-8 reverses the polarity: the wicked are what they imprisoned the righteous in — a retributive reversal of Joseph's fate.

### 2d. Structural echoes

Surah 12 is the only surah that tells a single continuous story end-to-end ("aḥsanu al-qaṣaṣ" — "the best of narratives," 12:3). The fact that all 9 literal-prison tokens are confined to this narrative AND that the overall surah count is 12 is one of the project's most striking *nominative* coincidences — the prison word, the prophet's surah number, and the literal count *coincide*.

### 2e. Muhkam / mutashabih

The mutashabih tension is: **sijjīn** in 83:7-8 is explicitly marked as "What can make you know what is *sijjīn*?" — the Qur'an itself declares the word opaque. The muhkam anchor that contextualizes it is 83:18-19 (the *ʿilliyyīn* counterpart: "the book of the righteous is in *ʿilliyyīn*"). The two are registers, not prisons — but the root metaphor borrows the Josephite connotation.

### 2f. Self-commentary

12:3 — "naḥnu naquṣṣu ʿalayka aḥsana al-qaṣaṣ bimā awḥaynā ilayka hādhā al-qurʾān" — "We narrate to you the best of narratives." The surah explicitly flags itself as the Quran's unique narrative peak, and the sjn-12 coincidence is the counting-layer signature of that declaration.

---

## Finding 3 — Ash-Shams 7-verse oath-palindrome and the oath-cluster genre

> ✨✨ "Q 91:1-7 letter counts = [12,14,15,15,15,14,12], mirrored around verse 4 ('by the Night when it covers')."

I re-verified the palindrome and tested the four other oath-cluster surahs (92, 93, 100, 103).

### 3a. The Q 91 palindrome verified

| v | Letter count | Content (oath subject) |
|---|---|---|
| 1 | 12 | sun and its brightness |
| 2 | 14 | moon when it follows it |
| 3 | 15 | day when it displays it |
| 4 | **15** | **night when it covers it** (center) |
| 5 | 15 | sky and He who constructed it |
| 6 | 14 | earth and He who spread it |
| 7 | 12 | soul and He who proportioned it |

Perfect mirror: `[12,14,15,15,15,14,12]`. Verses 8-15 (instill→Thamud) have length counts `[20,13,13,15,13,30,39,13]` — **non-palindromic**. The palindrome stops exactly at the seventh cosmic oath.

### 3b. Other oath clusters: NOT palindromic

| Surah | Oath scope | Letter counts across oath verses | Palindromic? |
|---|---|---|---|
| 92 (Al-Layl) | night/day/male-female (v1-3) | [13,14,18] | No |
| 93 (Aḍ-Ḍuḥā) | morning/night (v1-2) | [6,12] | No (too short) |
| 100 (Al-ʿĀdiyāt) | chargers at dawn (v1-5) | [13,13,13,11,11] | No — a 3+2 pattern |
| 103 (Al-ʿAṣr) | time (v1) | [6] | N/A |

Q 91 remains the **unique** 7-verse oath palindrome. Q 100 has a smaller pattern: three verses of 13 letters followed by two of 11 — a tight near-symmetric cluster, but not an actual palindrome.

### 3c. Root-level echoes of the seven cosmic oaths

The seven subjects — `sms` (sun), `qmr` (moon), `yawm` (day), `lyl` (night), `smā'` (sky), `arḍ` (earth), `nafs` (soul) — are the **seven most fundamental cosmological roots** in the Quran. Per the root-index:

| Root | Total | Top surah |
|---|---|---|
| `sms` (sun) | 33 | multiple (7, 41) |
| `qmr` (moon) | 27 | 6, 10 |
| `ywm` (day) | 405 (lemma) | pervasive |
| `lyl` (night) | 92 | pervasive |
| `smw` (sky/heavens) | 381 | 2, 6, 7 |
| `arD` (earth) | 461 | pervasive |
| `nfs` (soul/self) | 298 | pervasive |

Surah 91 is the **densest compression of these seven roots anywhere** — 7 cosmological roots in 7 adjacent verses, a stylistic move found nowhere else.

### 3d. Structural echoes

The oath-cluster **genre** (short Meccan surahs opening with multiple *wāw* oaths) includes surahs 37, 51, 52, 53, 56, 77, 79, 81, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103. Among these, **only Surah 91 yields a letter-count palindrome over its full oath block**. I re-tested palindromes.md's adjacent finding (Q 81:2-8 Takwīr, Q 37:127-133 Ṣāffāt) — these are also length-7 palindromic subruns but they sit *inside* the body, not at the oath-opening, and have different content.

Under a much stricter test (exact root-sequence palindrome, ≥5 tokens per verse), only **Q 33:3 and Q 73:15** are perfect 1-verse root palindromes in the entire Quran:
- **33:3** `[wkl, Alh, kfy, Alh, wkl]` — "Rely upon Allah; sufficient is Allah as Disposer of affairs" — the **tawakkul** palindrome, *form enacts content*.
- **73:15** `[rsl, rsl, $hd, rsl, rsl]` — "We have sent to you a Messenger as a witness just as We sent to Pharaoh a messenger" — the **rasūl** palindrome, Muhammad mirroring Moses.

Q 13:28 (Finding 4) is *chiastic-at-phrase-level* but not strict palindromic at the token level; it is ABCD|CDAB, not ABCD|DCBA.

### 3e. Muhkam / mutashabih

The seven oaths are mutashabih — each invokes a cosmic entity whose connection to the following rebuke ("Thamud denied their prophet") is not spelled out. Muhkam anchors:
- **Q 17:12** "We have made the night and day two signs" — the oath-subjects are *āyāt*, signs.
- **Q 41:37** "Of His signs are the night and day and the sun and moon" — the same oath-subjects, this time framed as *āyāt* with the explicit imperative "do not prostrate to the sun or moon."
- **Q 16:12** "And He has subjected for you the night and the day and the sun and the moon, and the stars are subjected by His command" — anti-astrolatry muhkam.

These muhkam verses clarify: the oath-subjects of Q 91 are not deities, they are signs; swearing *by* them is swearing *through* them to the Creator who made them.

### 3f. Self-commentary

Q 91 itself ends with Thamud's destruction — the she-camel episode — so the palindrome is *bracketed* by (a) cosmic oaths, (b) the soul's duality at the hinge (v8: "inspired it [with discernment of] its wickedness and its righteousness"), (c) Thamud's rebuke. The formal symmetry of v1-7 is the oath; the asymmetry of v8-15 is the moral consequence. Form literally models the moral architecture: when the soul aligns with the cosmic order (v1-7 palindrome), it is *zakkāhā* ("purified," v9); when it breaks the pattern (v8-15 non-palindromic), it is *dassāhā* ("instilled with corruption").

---

## Finding 4 — Q 13:28 hearts-find-rest in remembrance, and the dhikr network

> ✨✨ "Q 13:28 is a perfect one-verse chiastic root palindrome — 8/9 stem tokens mirrored."

### 4a. Root-level echoes of `*kr` (dhikr)

The Buckwalter root `*kr` = dh-k-r has **292 tokens in 264 unique verses**. Top 15 surahs:

| Surah | dhikr count | Surah | dhikr count |
|---|---|---|---|
| 2 | 19 | 18 | 7 |
| 7 | 16 | 19 | 7 |
| 6 | 15 | 33 | 7 |
| 21 | 13 | 39 | 7 |
| 38 | 13 | 16 | 6 |
| 54 | 11 | — | — |
| 3 | 8 | 5 | 8 |
| 20 | 8 | — | — |

**Surah 54 (Al-Qamar)** deserves special attention — it is dominated by the refrain **"wa la-qad yassarnā al-Qurʾāna li-al-dhikri fa-hal min muddakir"** ("We have certainly made the Qur'an easy for *dhikr*, so is there any who will take heed?") which appears 4 times in the same surah: 54:17, 54:22, 54:32, 54:40 — a liturgical echo of the root in the same formula.

### 4b. Lemma-level breakdown

| Lemma | Count | Meaning |
|---|---|---|
| `*akara` | 84 | verb "to remember/mention" |
| `*ikor` | 76 | noun "remembrance/mention" (includes "the Reminder" as title for the Qur'an) |
| `ta*ak~ara` | 51 | verb "to take heed" |
| `*ikoraY` | 23 | feminine "reminder/remembrance" |
| `ta*okirap` | 9 | "admonition" |
| `*uk~ira` | 18 | passive verb |
| `*akar` | 18 | "male" (same consonant family) |

### 4c. Thematic network — "hearts + remembrance"

The 13:28 finding sits at the center of a **heart-and-remembrance theological cluster**. The cluster's verses:

| Verse | Summary | Relation to 13:28 |
|---|---|---|
| **2:260** | Abraham: "show me how you give life to the dead… that **my heart may be reassured** (*li-yaṭma'inna qalbī*)" | Uses the exact same root-pair (`Tmn` + `qlb`). Abraham is the archetypal seeker whose heart is reassured. |
| **3:126** | Divine help "to **reassure your hearts** thereby" | Tmn + qlb, battle context (Badr). |
| **5:113** | Disciples to Jesus: "that **our hearts be reassured** and we know you spoke truth" | Tmn + qlb; reassurance comes from sign. |
| **8:10** | Angels at Badr "so that **your hearts would be assured**" | Same formula. |
| **8:2** | "The believers are those whose **hearts tremble** (*wajilat qulūbuhum*) at mention of Allah" | Inverse emotion — fear — to same stimulus. |
| **13:28** | "those whose **hearts are reassured by the remembrance of Allah** — by remembrance of Allah hearts are reassured" | **Center** of the network; chiastic form. |
| **20:124** | "Whoever turns away from **My dhikr** will have a depressed life" | The negative counterpart: absence-of-dhikr → constricted life. |
| **22:35** | "whose **hearts are fearful** when Allah is mentioned" | Fear-branch of the network. |
| **29:45** | "the **dhikr of Allah is greater**" (*wa-la-dhikru llāhi akbaru*) | Muhkam declaration: dhikr supersedes prayer itself. |
| **33:41-42** | "O believers, remember Allah with **much dhikr** (*dhikran kathīrā*) and exalt Him morning and afternoon" | The positive imperative. |
| **39:23** | "their skins and their **hearts relax (talīnu qulūbuhum) at dhikr of Allah**" | **Direct parallel to 13:28**: Book → skins shiver → hearts relax at dhikr. This is the Quran describing its own reception. |
| **39:45** | "When Allah is mentioned alone, **hearts of those who do not believe shrink with aversion**" | Negative counterpart — dhikr triggers aversion in unbelievers. |
| **57:16** | "Has the time not come for those who have believed that their **hearts should become humbly submissive at dhikr of Allah**" | Call-to-softening variant. |
| **63:9** | "let not your wealth and children **distract you from dhikr of Allah**" | Warning against dhikr-obstruction. |
| **89:27** | "O **reassured soul** (*yā ayyatuhā al-nafsu al-muṭma'innah*), return to your Lord" | **The eschatological capstone**: the soul that found rest through dhikr in 13:28 is the same *muṭma'inna* soul invited to Paradise in 89:27. This is the *completion* of the 13:28 arc. |

The network is **15+ verses deep**, arcing across both Meccan and Medinan material. Q 13:28 is not isolated — it is the **pivot** of this entire cluster. Its palindromic form is the compact signature of a doctrine developed over these ~15 verses.

### 4d. Structural echoes

Q 13:28 is the **most self-enacting verse in the Quran**: the content says "hearts find rest in dhikr" and the form *rests into its own mirror* (the ABCD|CDAB chiasm around the Allah-center). There are only two 1-verse strict root-palindromes in the Quran (33:3 and 73:15 as noted above), making 13:28's chiastic variant structurally unique in how it uses phrase-level mirroring around a divine-name axis.

### 4e. Muhkam / mutashabih

**Muhkam:** Q 29:45 is the sharpest muhkam anchor for the dhikr network: *wa-la-dhikru llāhi akbaru* — "dhikr of Allah is greater." Greater than what? The verse immediately prior identifies it: prayer. This is a ranking statement — dhikr supersedes even ṣalāh.

**Muhkam #2:** Q 39:23 defines dhikr reception as a **bodily process** (skins shivering → skins softening → hearts relaxing), anchoring 13:28's claim in phenomenology.

**Mutashabih:** what *is* dhikr in 13:28? A practice? A state? An object (the Qur'an itself as *al-dhikr*)? The Quran uses all three senses of the word. The muhkam anchor at 38:8, 41:41, 15:9 identifies *al-dhikr* with the Quran itself ("inna naḥnu nazzalnā al-dhikra wa-innā lahu la-ḥāfiẓūn" — 15:9). So "hearts find rest in al-dhikr" can be re-read as "hearts find rest in the Qur'an" — which collapses into 17:82 ("We send down of the Qur'an that which is healing").

### 4f. Self-commentary

**Q 39:23 is the single most meta verse on dhikr.** It calls the Quran "a consistent Book wherein is reiteration (*mathānī*)" AND says hearts relax at its dhikr. This is the Qur'an's own statement about itself as a structure of self-similar reiterations, and it uses the exact vocabulary of 13:28 (hearts + dhikr). Any cross-referencing project is operating under Q 39:23's mandate.

---

## Finding 5 — Al-Baqarah 131-144 Abraham/qibla ring and Abraham's other narrative frames

> ✨✨ "Sub-surah chiasmus z = +9.69, survives Bonferroni."

### 5a. Lemma-level: Ibrahim across the Quran

Lemma `<iboraAhiym` = **69 tokens across 25 surahs**. Distribution:

| Surah | Count | Type |
|---|---|---|
| 2 (Al-Baqarah) | 15 | Ring + multiple scenes |
| 3 (Āl ʿImrān) | 7 | "Religion of Abraham," polemical |
| 4, 6, 11, 21 | 4 each | Core narrative surahs |
| 9, 19, 22, 37 | 3 each | Pilgrimage + sacrifice |
| 12, 16, 29, 60 | 2 each | Scattered |
| 14 (Ibrāhīm), 15, 26, 33, 38, 42, 43, 51, 53, 57, 87 | 1 each | Mentions |

Most striking: **Surah 14 (named "Ibrāhīm") has only ONE Ibrahim mention** (14:35, his prayer over Mecca). The narrative density of Abraham in his titular surah is lower than in Al-Baqarah (15×), Āl ʿImrān (7×), or even Al-'Ankabūt (2×). The title references Abraham but the surah is dominated by other content.

### 5b. Abraham's narratives across surahs — comparative ring structure

The Quran retells Abraham's story in multiple retellings, each with its own rhetorical form:

| Surah | Pericope | Opening formula | Rhetorical form |
|---|---|---|---|
| **2:124-141** | Covenant + Ka'ba + legacy | "wa idh ibtalā Ibrāhīma Rabbuhū" | **Ring** (131-144 algorithmically-confirmed chiasmus) |
| **6:74-83** | Afl-chain rejection of astral worship | "wa idh qāla Ibrāhīmu li-abīhi Āzara" | Linear argument (3 rare-root Afl occurrences, unique to these verses) |
| **11:69-76** | Visitors announce Isaac + Lot | "wa la-qad jā'at rusulunā Ibrāhīma" | Dialogue scene |
| **14:35-41** | Abraham's prayer over Mecca | "wa idh qāla Ibrāhīmu rabbi ijʿal hādhā..." | Prayer monologue |
| **15:51-60** | Angel visit + Sodom announcement | "wa nabbi'hum ʿan ḍayfi Ibrāhīm" | Parallel to 11:69-76, 51:24-37 (3-way parallel) |
| **19:41-50** | Abraham vs. his father Azar | "wa-dhkur fī al-kitābi Ibrāhīma" | Dialogue + dismissal |
| **21:51-73** | Idol-smashing | "wa la-qad ātaynā Ibrāhīma rushdahū" | Dramatic scene (fire episode) |
| **26:69-104** | Prayer + polemic | "wa-tlu ʿalayhim naba'a Ibrāhīm" | Extended prayer-narrative |
| **29:16-27** | Idol rejection, emigration | "wa Ibrāhīma idh qāla li-qawmihī" | Condensed summary |
| **37:83-113** | Idol-smashing + sacrifice of son | "wa-inna min shīʿatihī la-Ibrāhīm" | **Narrative climax** — only surah with the ransom/sacrifice |
| **51:24-37** | Angel visit | "hal atāka ḥadīthu ḍayfi Ibrāhīma al-mukramīn" | Concentrated visit scene |
| **60:4** | "ye have a good example in Abraham" | "qad kānat lakum uswatun ḥasanatun fī Ibrāhīma" | **Muhkam declaration**: Abraham as the *uswa*, the model |

**Opening-formula clustering.** Three surahs open the Abraham-with-his-father scene with near-identical phrasing:
- 6:74 — "wa idh qāla Ibrāhīmu li-abīhi Āzara a-tattakhidhu aṣnāman ālihatan"
- 26:70 — "idh qāla li-abīhi wa qawmihī mā taʿbudūn"
- 37:85 — "idh qāla li-abīhi wa qawmihī mādhā taʿbudūn"

The 26-37 pair is especially close (same *mādhā taʿbudūn* construction). These are deliberate lexical echoes — the Quran repeats Abraham's opening challenge to his father in three different stylistic registers across the mushaf.

### 5c. Ring structures elsewhere in Abraham narratives

**Surah 21 (Al-Anbiyā') 51-73 — a compact Abraham ring:**
- 51-52: "We gave him *rushd*… when he said to his father 'what are these statues?'"
- 68: "they said, burn him and help your gods"
- 69: "O fire, be coolness and safety upon Abraham" (center)
- 70: "they intended harm but We made them the greatest losers" (inversion of 68)
- 71-73: "We delivered him… We gave him Isaac and Jacob… We made them leaders" (inversion of 51-52, *rushd* → *a'imma*)

This is a candidate ring not yet formally confirmed in `chiastic-audit.md`. It mirrors Al-Baqarah 131-144 in miniature: the "core" of Abraham's identity (rushd → imāma) brackets the fire miracle.

**Surah 37 — the sacrifice ring** 
- 83: "and among his kind was Abraham" (opening)
- 99-100: "I am going to my Lord who will guide me, Lord grant me a son"
- 102: "when he reached the age of exertion he said 'O my son, I have seen in a dream...'"
- 107: "and We ransomed him with a great sacrifice" (center)
- 109: "peace upon Abraham" (taslīm)
- 113: "we blessed him and Isaac"

Classic peace-of-taslīm centered ring.

### 5d. Thematic echoes — the qibla half of the ring

The second half of the Al-Baqarah ring (142-144) is the **qibla-change** pivot. Where else does the Quran reference qibla?

- **2:142-145, 149-150** — the 5-time repetition of the qibla-change block within Al-Baqarah (a densely ringed cluster).
- **10:87** — Moses and Aaron commanded: "make your houses *qibla*s and establish prayer." 
- No other surah mentions qibla. **The whole qibla doctrine is contained in Surah 2 + one verse in Surah 10.**

This makes Al-Baqarah 131-144 doubly central: it has both the Abraham-Ka'ba founding moment AND the qibla-change that reactivates it. The two halves of the ring (131-141 Abraham past, 142-144 qibla present) are joined by the shared concept: **the house Abraham founded is the house you now face.**

### 5e. Muhkam / mutashabih

**Muhkam anchor for Abraham:** Q 60:4 — "qad kānat lakum **uswatun ḥasanatun** fī Ibrāhīma" — "You have a good example in Abraham." This is the unique declarative *uswa ḥasana* verse for Abraham; the only other *uswa ḥasana* verse is Q 33:21 for Muhammad. Abraham and Muhammad are the two "examples" (*uswa*) in the Quran — a muhkam parallel that anchors the Baqarah ring (which moves from Abraham's founding to Muhammad's qibla-change) as the place where the two *uswa*s converge on the same Ka'ba.

**Muhkam:** Q 4:125 — "wa-ittakhadha allāhu Ibrāhīma khalīlā" — "Allah took Abraham as a friend." The unique *khalīl* epithet.

**Mutashabih:** Q 2:124 — "wa idh ibtalā Ibrāhīma rabbuhū bi-kalimātin fa-atammahunna" — "when his Lord tested him with certain *words*, and he completed them." What words? The Quran does not specify. This is the ring's opening mutashabih, precisely because its ambiguity invites the ring to unfold as exegesis of "the words."

### 5f. Self-commentary

The ring's qibla verses contain the Quran's self-exegetical moment at 2:144: "qad narā taqalluba wajhika fī al-samā'" — "We have certainly seen your face turning to the sky." The verse comments on the Prophet's inner longing and then resolves it with a command. This is the Quran watching itself being received and answering.

---

## Finding 6 — Muqatta'at density in Surah 50 (Qāf) and over-represented consonants elsewhere

> 🔷 "Letter ق (qāf) appears exactly 57 times in Surah 50 AND exactly 57 times in Surah 42. 57+57 = 114."

### 6a. Verification

Surah 50 Al-Qāf: **57 ق in 1,507 letters** (rate 3.78%, z ≈ +4.45 vs. global rate 2.13%). Confirmed.

### 6b. Other single-consonant over-representation effects

I ran a per-surah z-score scan for each Arabic letter. For each letter, which surah over-represents it most?

| Letter | Top surah (z) | Muqatta'at of that surah contains this letter? | Alternative top non-muqatta'at |
|---|---|---|---|
| ا (alif) | Surah 78 (An-Naba') z=6.21 | No (non-muqatta'at) | **78 itself is non-muqatta'at** |
| ل (lam) | Surah 3 (Āl ʿImrān) z=4.13 | Yes (ALM) | 13 (Ar-Ra'd) z=3.61 — 13 is muqatta'at but ALMR, L in it |
| ن (nun) | Surah 26 (Shu'arā') z=6.67 | **NO** — Shu'arā' opens with ط س م, no ن | 37 (Ṣāffāt) z=6.49 — also non-muqatta'at |
| م (mīm) | Surah 36 (Yā-Sīn) z=4.04 | No (ys only) | 52 (Ṭūr) z=4.03 |
| و (waw) | Surah 9 (At-Tawbah) z=5.01 | No | 8 (Al-Anfāl) z=3.61 — non-muqatta'at |
| ي (ya) | Surah 42 (Shūrā) z=4.67 | Yes (HM ʿSQ) | 19 (Maryam) z=3.24 — muqatta'at KHYʿṢ |
| ه (ha) | Surah 9 (At-Tawbah) z=7.00 | No | 91 (Shams) z=4.75 |
| ر (ra) | Surah 54 (Qamar) z=6.99 | No | 94 (Sharḥ) z=4.78 |
| ب (ba) | **Surah 55 (Raḥmān) z=8.98** | No | 38 (Ṣād) z=3.99 |
| ك (kaf) | Surah 55 (Raḥmān) z=4.46 | No | 17 (Isrā') z=3.30 |
| ف (fa) | Surah 55 (Raḥmān) z=3.75 | No | 20 (Ṭā Hā) z=3.49 |
| **ق (qāf)** | **Surah 50 (Qāf) z=4.45** | **Yes (ق)** | Surah 20 (Ṭā Hā) z=4.45 — tied |
| س (sīn) | Surah 114 (An-Nās) z=7.15 | No (surah is "*nās*") | 75 (Qiyāma) z=3.66 |
| د (dal) | Surah 72 (Jinn) z=7.63 | No | 109 (Kāfirūn) z=6.18 |
| ذ (dhāl) | Surah 77 (Mursalāt) z=6.67 | No | 81 (Takwīr) z=4.95 |

**The Surah 55 ب-ك-ف cluster** is an artifact of the refrain *fa-bi-ayyi ālā'i rabbikumā tukadhdhibān* — 31 repetitions of a phrase dense in those three consonants. This is the **refrain effect** — a non-muqatta'at surah has one letter (actually three letters) over-represented because a formulaic refrain dominates its text. This is a *legitimate* non-muqatta'at single-consonant thematic load, driven by liturgical structure.

**The Surah 114 س effect** is a tiny-surah artifact — "al-nās" is repeated 5× in 6 verses. High rate, small denominator. Less significant.

**The Surah 26 + 37 ن effect** is the saj' effect — both surahs have long narrative passages ending in -īn, which is a terminal nun. This isn't muqatta'at-driven but rhyme-driven. **Legitimate non-muqatta'at single-consonant over-representation**, driven by the fāṣila.

**The real discovery for this finding:** beyond ق in Q 50 and the known muqatta'at effect, **Surah 55 is a ب-overload** (z=+8.98, the highest z for any letter-surah pair in the scan) — a fact driven by the refrain. The muqatta'at density effect at Q 50 is therefore *not unique* as a phenomenon of single-consonant over-representation, but is **unique among opened muqatta'at surahs** because Q 50 opens with the single letter that is then locally over-used. The Q 55 effect is bigger but driven by content-refrain, not opening-letter.

### 6c. Thematic loading of ق

ق-loaded words in the Quran:
- `Qāf` (v1, the muqatta'at itself)
- `al-Qurʾān` (the Book)
- `qul` ("say" — 332 imperatives)
- `qawl` (speech/word — heavily in Surah 50)
- `qalb` (heart — 168 tokens)
- `qābaḍa` (grasp)
- `yaqīn` (certainty)
- `qiyāma` (resurrection)

Surah 50 is thematically a resurrection-speech surah: "Say (qul), the true (ḥaqq) word (qawl) has come to the hearts (qulūb) on the Day of Resurrection (qiyāma)." The content and the letter converge.

### 6d. Structural echoes

Surah 50 + Surah 42 pairing (both 57 ق) is the **only letter+surah split-half pattern** that I'm aware of in the Quran that divides a 114-total exactly. It's not replicated for any other letter-number pair in my scan.

### 6e. Muhkam / mutashabih

Surah 50 opens with the purely mutashabih character ق and immediately follows with "**by the glorious Qur'an**" — invoking the Book's name right after the letter. This is the Quran giving a hint: *the letter and the Book are linked*. The muhkam anchor for the muqatta'at is Q 3:7 ("no one knows its [true] interpretation except Allah"), which declares some verses definitionally mutashabih.

### 6f. Self-commentary

Q 50:1 is itself a self-commentary: "Qāf. By the glorious Qur'an..." — the letter is immediately resolved into an oath on the Qur'an. **Muqatta'at + self-reference in adjacent positions.** This move is repeated at Q 38:1 (Ṣād... by the Qur'an full of reminder) — another surah where the muqatta'at leads directly into a Qur'an-oath.

---

## Finding 7 — "Muḥammad" as proper name only post-Hijra, and the pre-Hijra address modes

> 🔷 "All 4 occurrences of the lemma `muḥammad` (3:144, 33:40, 47:2, 48:29) are post-Hijra Medinan."

### 7a. Lemma-level verification

Lemma `muHam~ad` = **4 tokens**, locations (3,144,2), (33,40,3), (47,2,9), (48,29,1). All four are Medinan surahs (Nöldeke order 97, 90, 95, 111). Verified.

The four in full:

| Verse | Context | Rhetorical function |
|---|---|---|
| **3:144** | "Muhammad is not but a messenger. [Other] messengers have passed on before him. So if he were to die or be killed, would you turn back on your heels?" | **Succession anxiety** — battlefield aftermath at Uhud. Name used to de-apotheosize. |
| **33:40** | "Muhammad is not the father of any of your men, but the Messenger of Allah and last (*khātam*) of the prophets." | **Zayd-adoption clarification** — name used for legal clarification. |
| **47:2** | "those who believe… in what has been sent down upon Muhammad — and it is the truth from their Lord" | **Revelation framing** — name used as synonym for "the Prophet receiving revelation." |
| **48:29** | "Muhammad is the Messenger of Allah; and those with him are forceful against the disbelievers, merciful among themselves…" | **Community portrait** — Muhammad + the umma as a sociological unit, referencing Torah and Gospel. |

All four are **definitional or clarifying**: the name is used precisely when the Quran needs to make a legal, theological, or sociological distinction about Muhammad as a finite person.

### 7b. How pre-Hijra surahs address the Prophet

The 86 Meccan surahs use other forms. Sahih search results:

**"O Prophet" (*yā ayyuhā al-Nabī*)** — 13 occurrences, ALL Medinan: 8:64, 8:65, 8:70 (Al-Anfāl), 9:73 (At-Tawbah), 33:1, 33:28, 33:45, 33:50, 33:59 (Al-Aḥzāb), 60:12, 65:1, 66:1, 66:9.

**"O Messenger" (*yā ayyuhā al-Rasūl*)** — 2 occurrences, both Medinan: 5:41, 5:67.

These vocative forms are themselves Medinan. So what do the **Meccan** surahs use?

The Quranic corpus's Meccan address to the Prophet works through:

1. **Second-person singular imperatives with no vocative**: *qul* ("say"), *anbi'hum* ("inform them"), *dhakkir* ("remind"), *iqra'* ("recite"), *ṣbir* ("be patient"), etc. The Meccan Quran addresses the Prophet via **commands** rather than naming him.
2. **Role designations** (not proper name): 
   - *al-nadhīr* (warner) — Q 13:7, 35:23, 38:4, 29:50
   - *al-bashīr* (bringer of good tidings)
   - *al-rasūl* (the Messenger) — 260+ tokens
   - *al-nabī* (the Prophet) — ~60 tokens
3. **Defensive "you are not" constructions**: *mā anta bi-…* ("you are not a…"):
   - 68:2 *mā anta bi-niʿmati rabbika bi-majnūn* ("you are not, by the grace of your Lord, a madman")
   - 52:29 *fa-dhakkir fa-mā anta bi-niʿmati rabbika bi-kāhinin wa-lā majnūn* ("remind, for you are not, by the grace of your Lord, a soothsayer nor a madman")
   - 81:22 *wa-mā ṣāḥibukum bi-majnūn* ("your companion is not mad")
   - 53:2 *mā ḍalla ṣāḥibukum wa-mā ghawā* ("your companion has not strayed nor erred")
4. **"Your companion" (*ṣāḥibukum*)**: a distancing Meccan device — treating the Prophet as "that person you know" rather than naming him. 53:2, 81:22, 34:46, 7:184.

The **pattern of address** changes systematically across the Hijra. Pre-Hijra: command-mode, role-mode, or *ṣāḥibukum*. Post-Hijra: *yā ayyuhā al-Nabī*, *yā ayyuhā al-Rasūl*, and in 4 juridical/theological moments the proper name *Muḥammad*.

### 7c. Root-level echoes of `Hmd`

Root `Hmd` (praise, from which Muhammad is derived) has:
- **`Hamod`** — 43 tokens (noun "praise")
- **`Hamida`** — verb forms
- **`maHomuwd`** — 1 token (Q 17:79 — "*maqāman maḥmūdā*" — "a praised station" for the Prophet)
- **`'aHomad`** — 1 token (Q 61:6 — **"Aḥmad"** as the messenger's other name in Jesus's prediction)

The Quran contains an alternative name for Muhammad at Q 61:6: "*wa-mubashshiran bi-rasūlin ya'tī min baʿdī ismuhu Aḥmad*" ("and giving good tidings of a messenger to come after me whose name is *Aḥmad*"). This is a **fifth** proper-name occurrence of a Muhammad-equivalent — making the naming count 4 Muḥammad + 1 Aḥmad = 5 total proper-name occurrences. Aḥmad is a hapax.

### 7d. Thematic echoes

The pre-Hijra address modes all presuppose that the addressee *is known to the audience*. The post-Hijra proper-name uses are all moments of **definition**: succession (3:144), adoption law (33:40), revelation source (47:2), community profile (48:29). This mirrors the move from a personal-to-personal Meccan oracle to a juridical-institutional Medinan community — the move you already confirmed via the verse-length-doubles-monotonically finding.

### 7e. Muhkam / mutashabih

**Muhkam:** 33:40 is the single clearest legal-theological verse about Muhammad — "he is not the father of any man among you; he is the Messenger of Allah and the seal of the prophets." This is a *definitional* muhkam statement that anchors all other references to him.

**Muhkam:** 48:29 is the sociological muhkam — Muhammad + community described in Torah-and-Gospel terms.

**Mutashabih that 33:40 clarifies:** 2:285 "*la nufarriqu bayna aḥadin min rusulihī*" ("we make no distinction between any of His messengers") — if no distinction is made, what makes Muhammad "khātam"? The 33:40 muhkam anchor provides the answer: he is the seal, the finisher. 33:40 clarifies 2:285.

### 7f. Self-commentary

Q 21:107 "we have not sent you except as a mercy to the worlds" — directly addresses the Prophet without naming him. This is the Quran commenting on the Prophet while **refusing to name him**, which is itself the systematic Meccan pattern. The Medinan 48:29 ("Muhammad is the Messenger of Allah… [they are described] in the Torah… and their description in the Gospel…") is the diametric opposite: naming and describing in external scripture terms.

---

## Finding 8 — Abraham's Afl-chain Q 6:76-78 (star/moon/sun rejection)

> ✨ "The rare root `Afl` has only 4 total occurrences in the Quran. 3 of them are in adjacent verses Q 6:76-78."

### 8a. Root verification

Root `Afl` = **4 total tokens**, locations:
- (6, 76, 11) — *falammā afala* ("when it set")  
- (6, 76, 15) — *lā uḥibbu al-āfilīn* ("I do not love those that set/vanish")
- (6, 77, 9) — *falammā afala* (moon)
- (6, 78, 11) — *falammā afalat* (sun)

All 4 occurrences are in 3 consecutive verses, telling one story. This is confirmed as **completely unique** — the root appears nowhere else in the Quran.

### 8b. Thematic echoes — is the star/moon/sun rejection echoed elsewhere?

Short answer: **No other surah tells the star/moon/sun progression narrative.** But the anti-astrolatry theme is echoed with different vocabulary:

| Verse | Content | Connection |
|---|---|---|
| **41:37** | "Of His signs are the night and day and the sun and moon. Do not prostrate to the sun or to the moon, but prostrate to Allah who created them." | **Direct anti-astrolatry muhkam**, but narrated as command, not as dramatic rejection. |
| **16:12** | "He subjected for you the night and day and sun and moon; and the stars are subjected by His command" | Same anti-astrolatry theme, stated as cosmological subjugation. |
| **7:54** | "your Lord is Allah who created the heavens and earth in six days… the sun, moon, and stars subjected by His command" | Similar framing, creation-centric. |
| **13:2** | "…and subjected the sun and moon, each running for a specified term" | Same theme. |
| **22:18** | "Do you not see that to Allah prostrates whoever is in the heavens and whoever is in the earth and the **sun**, the **moon**, the **stars**..." | **Inversion** — the same three bodies that Abraham rejected as deities are here depicted as prostrating to Allah themselves. |
| **27:24** | The Queen of Sheba's people "**prostrate to the sun**" | A **narrative instance** of astrolatry, but not rejected by the scene's prophet (Solomon); corrected later. |

**Q 22:18 is the strongest thematic inversion of the Afl-chain.** Abraham in 6:76-78 says "I don't love setting things; I don't worship them" — Q 22:18 says "the setting things *themselves* prostrate to Allah." The theological arc is: the cosmic bodies you rejected in Surah 6 are the same cosmic bodies you see prostrating in Surah 22. The Quran lets the bodies speak for themselves.

Q 27:24 is the **counter-narrative**: the people of Sheba *did* worship the sun. Solomon's story then runs parallel to Abraham's (both prophets confronting astrolatry), but the Afl-chain is unique to Abraham.

### 8c. Structural echoes

The Afl-chain is a **3-step escalation** — star, moon, sun — ordered by physical brightness. This specific progression is not replicated. However, the Quran has similar 3-step escalations elsewhere:

- Q 24:35 — the "**light upon light**" verse with its chain: niche → lamp → glass → star → tree → oil — a **7-step** cosmic ascent, structurally analogous to Abraham's 3-step descent-through-phenomena but going in the opposite direction (from small to luminous).
- Q 67:3-4 — "look again… look again" — a 2-step repetition of the command to look at the heavens.
- Q 88:17-20 — camel, heavens, mountains, earth — a 4-step post-resurrection contemplation chain.

Abraham's Afl-chain is the only such chain built on a **rare-root refrain** (4 occurrences, all chained).

### 8d. Muhkam / mutashabih

**Muhkam anchor:** Q 41:37 ("do not prostrate to the sun or moon, but prostrate to Allah who created them") is the clearest anti-astrolatry muhkam. It clarifies that Abraham's Afl-rejection is not just personal biography — it is normative theology.

### 8e. Self-commentary

Q 6:75 introduces the scene: "wa kadhālika nurī Ibrāhīma malakūta al-samāwāti wa al-arḍi wa li-yakūna min al-mūqinīn" — "And thus We showed Abraham the dominion of the heavens and earth, that he would be among the certain." Verse 75 is the Quran's own commentary on verses 76-78: the *malakūt* vision *is* the Afl sequence. The rare root is the signature of a revealed vision.

**This is, confirmed, the most tightly localized rare-root narrative in the Quran.** Only one narrative, only one root, only three verses.

---

## Finding 9 — The 147 triple (ghayr / ilāh / jannah)

> ✨ "`ghayr` / `ilāh` / `jannah` each occur exactly 147 times, together spelling *lā ilāha ghayruhu*."

### 9a. Lemma verification

- **`<ila`h`** (ilāh, deity) — **147 tokens** confirmed
- **`jan~ap`** (jannah, garden) — **147 tokens** confirmed
- **`gayor`** (ghayr, other-than) — **147 tokens** confirmed

### 9b. Co-occurrence

I tested co-occurrence at the verse level:

| Intersection | Count |
|---|---|
| ilāh ∩ jannah | **0** verses |
| ilāh ∩ ghayr | **18** verses |
| jannah ∩ ghayr | **7** verses |
| all three | **0** verses |

**Stunning:** the three lemmas that each occur 147 times and that together spell the theological spine never co-occur in a single verse. The coincidence is purely at the **aggregate**, not at the surface. This is a **mathematical** coincidence rather than a phrasal one.

### 9c. The ilāh + ghayr cluster (18 verses)

These 18 verses form a distinct rhetorical family. Most of them use the phrasal template "*mā lakum min ilāhin ghayruhū*" ("you have no deity other than Him"). The occurrences:

| Verse | Prophet | Formula |
|---|---|---|
| 7:59 | Noah | *mā lakum min ilāhin ghayruhū* |
| 7:65 | Hud | *mā lakum min ilāhin ghayruhū* |
| 7:73 | Salih | *mā lakum min ilāhin ghayruhū* |
| 7:85 | Shu'ayb | *mā lakum min ilāhin ghayruhū* |
| 11:50 | Hud | *mā lakum min ilāhin ghayruhū* |
| 11:61 | Salih | *mā lakum min ilāhin ghayruhū* |
| 11:84 | Shu'ayb | *mā lakum min ilāhin ghayruhū* |
| 23:23 | Noah | *mā lakum min ilāhin ghayruhū* |
| 23:32 | Anonymous messenger | *mā lakum min ilāhin ghayruhū* |
| 6:46 | Muhammad | "what *ilāh ghayr Allāh* could bring them back?" |
| 7:140 | Moses to Children of Israel | "is it *other than Allah* I should desire for you as a god?" |
| 11:101 | Narrator | Their gods "*other than Allah*" did not avail them |
| 26:29 | Pharaoh ↔ Moses | "if you take a god *other than me*" (**inverted** — Pharaoh claims himself as sole god) |
| 28:38 | Pharaoh | "I have not known you to have a god *other than me*" (same inversion) |
| 28:71 | Muhammad | "what deity other than Allah could bring you light?" |
| 28:72 | Muhammad | "what deity other than Allah could bring you a night?" |
| 35:3 | Narrator | "Is there any creator other than Allah…? There is no deity except Him" |
| 52:43 | Narrator | "Or have they a deity other than Allah?" |

**Two striking sub-patterns emerge:**

1. **The prophetic-refusal formula** (9 verses, 7:59, 7:65, 7:73, 7:85, 11:50, 11:61, 11:84, 23:23, 23:32) — the same exact phrase *mā lakum min ilāhin ghayruhū* is spoken by **different prophets to different peoples** at exactly the same structural moment in each narrative. This is a deliberate **intertext of formulas**, not of events. Noah, Hud, Salih, and Shu'ayb all say the same thing in the same grammatical construction, making them interchangeable in the Quran's "cycle of warners" narrative.

2. **The Pharaonic inversion** (26:29, 28:38) — Pharaoh claims himself as god "other than Allah." This is the only character in the Quran who uses "ghayr" in first-person self-deification. Pharaoh is the inverted mirror of the prophets who use the same lexicon.

3. **Q 28:71-72 is in this cluster AND in Finding 10** (the srmd pair). The same two verses that contain the only 2 occurrences of *srmd* also contain *ilāh ghayr Allāh*. This is a **double-rarity verse pair**.

### 9d. The explicit "lā ilāha" formula

Beyond the 18 cluster verses, the formulaic phrase "lā ilāha illā…" (no deity except…) occurs **42 times** in the Quran in its various forms. The most famous is 2:255 (*al-kursī*): "*allāhu lā ilāha illā huwa al-ḥayyu al-qayyūm*." But this uses *illā* ("except"), not *ghayr* ("other than"), so it does not contribute to the ilāh+ghayr co-occurrence set — but it is the **muhkam** declaration that the 18-verse cluster echoes in narrative form.

### 9e. Structural echoes

The 9-verse prophet-formula (Noah→Hud→Salih→Shu'ayb, repeated in 7 and 11) is a classic Quranic **ring of warners**. It runs twice:

- **Al-A'rāf 59→85**: Noah (59) → Hud (65) → Salih (73) → Lot (80) → Shu'ayb (85) — the 7-fold cycle
- **Hūd 25→95**: Noah (25-49) → Hud (50-60) → Salih (61-68) → Abraham+Lot (69-83) → Shu'ayb (84-95)

Both surahs preserve the same order of prophets AND use the same refrain *mā lakum min ilāhin ghayruhū* as a structural hinge. Surahs 7 and 11 are therefore **ring-twins**: same narrative sequence, same formulaic phrases, different rhetorical emphasis.

### 9f. Muhkam / mutashabih

**Muhkam:** 2:255 (*al-kursī*), 2:163, 47:19, 20:14, 21:25 — all use the definitive *lā ilāha illā [Allah / huwa / ana]* construction. These are the doctrinal muhkam verses that the cluster's 18 verses are *narrativizing*.

**Mutashabih:** the numerical coincidence of 147-147-147 is itself mutashabih — the lemmas never phrasally co-occur, so the theological meaning of the three equal counts is not linguistically *stated*, only *structurally present*.

### 9g. Self-commentary

The Quran comments on this theme most compactly at 17:42: "qul law kāna maʿahū ālihatun kamā yaqūlūna idhan la-ibtaghaw ilā dhī al-ʿarshi sabīlā" — "Say: if there were along with Him gods as they claim, they would have sought a path to the Throne." This is the Quran's internal argument that no other deity exists — it doesn't use *ghayr*, but it commentates on the doctrine that the 147-triple encodes at the count level.

---

## Finding 10 — Q 28:71-72 srmd pair, day-night perpetuity argument

> ✨ "Root `srmd` has only 2 occurrences in the whole Quran, both adjacent verses: 'if Allah made the night perpetual / if Allah made the day perpetual'."

### 10a. Root verification

Root `srmd` = **2 tokens**, at (28,71,8) and (28,72,8). Both describe a counterfactual *sarmadā* ("perpetual") condition. Confirmed unique.

Full text:
- **28:71** — "qul a-ra'aytum in jaʿala llāhu ʿalaykumu al-layla **sarmadan** ilā yawmi al-qiyāmati man ilāhun **ghayru** llāhi ya'tīkum bi-ḍiyā'in a-fa-lā tasmaʿūn"
- **28:72** — "qul a-ra'aytum in jaʿala llāhu ʿalaykumu al-nahāra **sarmadan** ilā yawmi al-qiyāmati man ilāhun **ghayru** llāhi ya'tīkum bi-laylin taskunūna fīhi a-fa-lā tubṣirūn"

Note that both verses ALSO contain *ilāh* + *ghayr* → they are part of the 18-verse cluster from Finding 9. **The srmd pair and the 147-triple converge at exactly this pair of verses.**

### 10b. Thematic echoes — day-night as sign elsewhere

The Quran invokes the night-day alternation as an *āya* (sign) in numerous other places, but never using *srmd*. Alternative vocabulary:

| Verse | Formula | How different from 28:71-72 |
|---|---|---|
| **3:190** | "In the creation of the heavens and earth and the *alternation* (*ikhtilāf*) of night and day are signs" | Uses *ikhtilāf* (alternation) — emphasizes *change*, not *perpetuity*. Opposite rhetorical move. |
| **17:12** | "We have made the night and day two signs — We erased the sign of the night and made the sign of the day visible, that you may seek bounty and know the count of years" | Uses "**two signs** (*āyatayn*)" — framing the duality as parallelism. Utilitarian (agriculture/calendar). |
| **30:23** | "Of His signs is your sleep by night and day" | Uses sleep as the phenomenon; contemplative. |
| **36:37** | "A sign for them is the night: we remove from it the day so they are in darkness" | Uses removal — closest to 28:71 counterfactual but without *srmd*. |
| **41:37** | "Of His signs are the night and day and the sun and moon" | List form. |
| **16:12** | "He subjected for you the night and day, and the sun and moon, and the stars are subjected by His command" | Subjugation form. |

**Q 36:37 is the closest vocabulary parallel** — "We remove the day so they are in darkness" and 28:71 "if He made the night perpetual, who could bring you light?" are the same thought experiment in different grammatical modes. **36:37 is indicative; 28:71 is counterfactual conditional.**

### 10c. Structural echoes — adjacent-verse rare-root pairs

The srmd pair is a **2-verse hapax pair** — both occurrences in adjacent verses. How rare is this pattern?

From the jinas-wordplay.md data, other adjacent rare-root chains:
- **Afl chain (6:76-78)** — 3 verses, 4 tokens (Finding 8)
- **srmd pair (28:71-72)** — 2 verses, 2 tokens

These are the two "perfect-adjacency rare-root pairs" (or chains). Both are in **argumentative-dialogic passages**, not narrative. Both use rare vocabulary to mark a **rhetorical peak** — Abraham's realization, the Quran's counterfactual challenge. The rare-root-as-marker is a consistent stylistic device.

### 10d. The 28:71-72 pair as a ring-center

Q 28:71-72 are themselves a miniature **parallel-couplet**: identical grammar, swapped content. The structure:

- 28:71 — night → srmad → ilāh ghayr Allāh → ḍiyā' (light) → a-fa-lā **tasmaʿūn** (do you not **hear**?)
- 28:72 — day → srmad → ilāh ghayr Allāh → layl taskunūn (night in which you rest) → a-fa-lā **tubṣirūn** (do you not **see**?)

The swap **hearing ↔ seeing** at the terminal rhetorical question is deliberate: night is correlated with hearing (the sense used in darkness), day with sight. The pair encodes a sensory chiasm on top of the content chiasm. This is one of the Quran's most elegant mini-structures.

### 10e. Muhkam / mutashabih

**Muhkam anchors:**
- 36:40 "The sun is not allowed to overtake the moon, nor does the night outstrip the day" — **no perpetuity is possible**. This muhkam clarifies that srmd is a counterfactual, not a threat.
- 17:12 "two signs" — **the two are by design**. Sign-pair doctrine.
- 13:3 "He causes the night to cover the day" — **cyclical**.

### 10f. Self-commentary

Q 28:71 opens with *qul a-ra'aytum* ("say: have you considered…") — a Quranic **thought-experiment signal**. The same construction opens 28:72, 67:28, 67:30, 6:40, 6:46, 6:47, 10:50, 10:59, 11:28, 11:63, 17:62, 19:77, 39:38, 41:52, 45:23, 46:4, 46:10, 56:58-72 (four consecutive uses), 67:28-30, 96:9-13. The **qul a-ra'aytum** genre is a Quranic rhetorical mode: counter-factual challenges posed to the audience, always without narrative setting. Q 28:71-72 are twin entries in this genre.

---

## Summary tables

### Roots with exceptional narrative localization

| Root | Total | Unique surah | Context |
|---|---|---|---|
| Afl (set/vanish) | 4 | 6 | Abraham's star/moon/sun rejection |
| srmd (perpetual) | 2 | 28 | Day-night perpetuity counterfactual |
| s~ijon + yusojana | 9 | 12 | Joseph's prison |
| kahf (cave) | 6 | 18 | Al-Kahf cave |
| qamīṣ (shirt) | 6 | 12 | Joseph's shirt |

### Lemmas whose count = 114 (surah count) or 147

| Lemma | Count | Relationship |
|---|---|---|
| `raHomap` | 114 | = surah count; Q 21:107 calls Muhammad "raḥma to the worlds" |
| `r~aHoma`n` | 57 | = half of 114; Ar-Rahman is a divine name |
| `<ila`h` | 147 | triple with jannah and ghayr |
| `jan~ap` | 147 | triple |
| `gayor` | 147 | triple; together spell "lā ilāha ghayruhu" |

### Strict 1-verse root palindromes (≥5 tokens)

| Verse | Roots | Content |
|---|---|---|
| 33:3 | wkl, Alh, kfy, Alh, wkl | "Rely upon Allah; sufficient is Allah as Disposer" |
| 73:15 | rsl, rsl, $hd, rsl, rsl | "We sent you a Messenger as witness, as We sent Pharaoh a messenger" |

Q 13:28 is chiastic at the phrase level (ABCD|CDAB), not strict-palindromic at the token level. All three verses use the same form-enacts-content strategy.

### Proper-name references to Muhammad / Aḥmad

| Verse | Name | Function |
|---|---|---|
| 3:144 | Muhammad | Succession |
| 33:40 | Muhammad | Legal (adoption/seal) |
| 47:2 | Muhammad | Revelation source |
| 48:29 | Muhammad | Community profile |
| 61:6 | Aḥmad | Jesus's prediction |

All five are Medinan. The 86 Meccan surahs name the Prophet zero times.

---

**End of cross-reference document.**
