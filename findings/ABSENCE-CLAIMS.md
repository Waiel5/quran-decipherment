---
title: Absence claims — the least audited claims in the repository
author: Waiel Al-Shujaa
date: 2026-08-07
status: STANDING METHODOLOGICAL RULE — applies to every claim that data is missing
established_by: [H-NEW-2890, H-NEW-2900]
companion: findings/UNIT-DRIFT-DEFECT.md
---

# Absence claims

## 1. The rule

> **A claim of absence is a claim about a search, not about the world. It is only as wide as
> the search that produced it. State the search — the command, the paths, the measured
> property and its threshold — or do not make the claim.**

And the clause that does the real work:

> **An absence claim may not be inherited. A second finding that repeats "not on disk" must
> re-run the search itself, and must re-check the findings it cites as parents.**

**Nothing downstream fails when an absence claim is wrong.** A wrong positive result gets
contradicted by the next test that touches it. A wrong absence produces no contradiction at
all, because the experiment it blocked is simply never run. **This is why absence claims
accumulate errors faster than any other kind of claim in a project, and why they are the
cheapest to audit and the least audited.**

---

## 2. The case that established it

**Three consecutive findings declared the vocalised-prose negative control impossible. The
data was on disk the whole time, and it was on disk *in the finding they cited as their own
method parent*.**

| step | what was said, and by whom |
|:--|:--|
| **H-NEW-2730** | Ran *"an exhaustive sweep of `data/`"*, found the vocalised ḥadīth, **measured Ṣaḥīḥ al-Bukhārī at diacritic ratio 0.770 and Sunan al-Dārimī at 0.866**, named the edition, used both as its prose control, and even stripped Qurʾānic quotation from them by 7-gram match |
| `STATE-OF-THE-PROJECT-2026-08-07.md` §5.4a | *"on disk only this corpus, **the ḥadīth collections** and three of the seven muʿallaqāt have them"* — the canonical orientation document, which every pre-flight requires |
| **H-NEW-2870** §6.2 | *"The citation form cannot be recovered… Δ is not computable for either prose baseline."* Its own frontmatter reads `method_parent_2: H-NEW-2730` |
| **H-NEW-2880** §5.2 | *"A census of all 36 baseline corpora on disk found no vocalised prose at all."* |
| **H-NEW-2890** | Repository-wide census: **50,884 fully vocalised ḥadīth** at `data/literature/hadith/ahmedbaset-json/`, al-Bukhārī at **0.7702**, committed since 2026-04-28 |

**The two independent measurements agree to three decimals — 0.770 and 0.7702 — which is the
proof that nothing changed on disk. Only the claim changed.**

The census behind H-NEW-2880's sentence enumerated **`data/baseline-corpora/` only**. The
sentence is true of that directory and false of the repository, and nothing in it declared
which one had been searched.

**What it cost.** The negative control of an entire finding family — the control an informed
sceptic reaches for first — went unrun across three findings. When finally run it took under
an hour and returned a clean result: prose gains Δ = +0.030 to +0.033 against this corpus's
+0.1869, and does not clear its own matched null.

**Why this is worse than a narrow census, and the reason for §1's second clause:** the datum
was not merely findable. It was *published, measured, and named* in the finding cited three
lines above in the asserting finding's own frontmatter. **No amount of searching would have
been needed. Reading the parent would have done it.**

---

## 3. The detection screen

A claim is **FLAGGED** if it hits A and B. Apply to the sentence, not to the prose around it.

### Screen A — is it an absence claim?
Grep for: `not on disk`, `NOT COMPUTABLE`, `cannot be run`, `not available`, `is absent`,
`no such corpus`, `would require acquiring`, `we do not have`, `not in the repository`,
`binary not committed`, `unavailable`, `acquisition need`, `no text layer`, `not acquirable`,
`does not exist`, `NOT FOUND`.

```bash
grep -rniE "not on disk|NOT COMPUTABLE|cannot be run|no such corpus|would require acquiring|\
we do not have|not in the repository|binary not committed|acquisition need|no text layer" \
  --include='*.md' findings/ surahs/ HANDOFF/ *.md
```

### Screen B — does the claim state its search?
**Does the sentence say what was searched, with what command, over what paths, against what
measured property and threshold?** If it says only *that* something is missing and not *how
that was established*, it is unverified regardless of how confident it sounds.

### Screen C — the parent check, which is cheaper than any search
**Before asserting an absence, grep the findings you cite as parents for the thing you are
about to declare missing.** H-NEW-2870 would have needed one command:

```bash
grep -riE "vocalis|diacritic|harakat" findings/phase-b-hypotheses/h-new-2730-*.md
```

**One line, and it returns `al-Bukhārī … vocalised at ratio 0.770`.**

---

## 4. The standing requirement

**Any claim in this repository that data is missing must state, in the claim itself:**

1. **The command actually run**, with its paths — not "a census", not "an exhaustive sweep",
   the command.
2. **The scope searched**, named explicitly: one directory, `data/`, or the repository.
3. **The measured property and its threshold**, where the claim is about adequacy rather than
   existence — "0 ḥarakāt over 2,056,880 Arabic characters" is a claim; "unvocalised" is not.
4. **A positive control on the search itself** where one is available: search for something
   you know is present and confirm the instrument finds it. An absence returned by an
   instrument never shown to detect a presence is not evidence.

Three further clauses, each earned:

- **Distinguish ABSENT from NOT-YET-DERIVED.** H-NEW-930 recorded that a per-poem line-count
  tabulation was *"not on disk in tabular form"*. The 14 dīwān files and their 17,196 lines
  were present; only the table had never been made. **Derivable is not missing**, and writing
  it as missing retires a question that a `wc -l` would have answered.
- **A refuted absence must be corrected in the document that carries it, not only in the
  document that refutes it.** H-NEW-2740 §10 found that `STATE-OF-THE-PROJECT` §5's *"a
  rasm/imlāʾ divergence set… not on disk"* was wrong, built the set from two files already
  present (6,919 tokens, 2,093 skeleton-pairs), and flagged it *"for the ledger keeper; not
  mine to edit"*. **It is still uncorrected in the canonical document.** A correction that
  lands only in the child finding does not stop the parent from being inherited again.
- **An absence claim ages badly.** Corpora get committed; this one was committed on
  2026-04-28 and asserted missing on 2026-08-07. **Date every absence claim, and treat any
  claim older than the most recent data acquisition as unverified.**
- **A property of one file is not a property of the work.** The single most consequential
  false absence in §6 — *"no citable primary waqf source is on disk"* — came from correctly
  establishing that a **partial English translation** lacked the nawʿ, and then generalising
  from the file to the repository. **The complete Arabic text was in the same directory.**
  Before declaring a *work* unavailable, search for every edition of it, in every language,
  by author name and by title, not by the filename you happened to open.
- **Watch for name collisions in both directions.** `find -iname "*mishkat*"` returns
  *Mishkāt al-Maṣābīḥ* (a ḥadīth collection, present) when the claim concerns al-Ghazālī's
  *Mishkāt al-Anwār* (absent); `dani-23-site-supplement.tsv` is not al-Dānī's *al-Muqniʿ*.
  **A hit is not a verification, and neither is a miss — open the file.**

---

## 5. What FLAGGED means

**Flagging is not refuting.** Most absence claims in this repository are TRUE, and several are
models of how to make one — see §6's TRUE block, and in particular `cross-finding-028`, which
dropped three ḥadīth pairs for want of attestation, **named the corpus it searched, and cited
the positive cases it did find**. Re-verified here: its dropped pairs return 0 co-occurrences
in the 50,884-record corpus, and a positive control reproduces the very citation it verified
(`tirmidhi#2975`). **That is what an absence claim should look like.**

What flagging means is that **the claim has not been separated from the search that produced
it**, and that no work should be declined on its authority until it has.

**A FALSE absence is more valuable to find than a FALSE positive**, because it does not
merely correct the record — it returns a test to the queue.

---

## 6. The inventory, 2026-08-07

Verified against the filesystem, with the verifying command. Ranked by consequence: a false
absence that blocked a **control** outranks one that blocked a convenience.

### FALSE — the thing is present

| # | claim, and where | verification | what it blocked |
|:--|:--|:--|:--|
| **1** | *"No citable primary waqf source is on disk"* / *"the nawʿ is absent from this translation"* / *"Acquisition need: a text-layer al-Burhān or al-Nashr vol. 1"* — H-NEW-2870 §12 and prereg §10, H-NEW-2880 §9.6, H-NEW-2890, FRONTIER-MAP F-16 | **FALSE.** `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` — the **Arabic** Itqān, 1,018,548 Arabic chars — contains `النوع الثامن والعشرون: في معرفة الوقف والابتداء` **with its body text at PageV01P281**, naming al-Nahhās, Ibn al-Anbārī, al-Zajjāj, al-Dānī, al-ʿUmānī and al-Sajāwandī. 140 hits for `الوقف`, 74 for `الابتداء` | **The classical anchor for the entire pausal-rhyme family.** Three findings state *"No page citation is given and none was invented."* **It is citable now: al-Suyūṭī, al-Itqān, nawʿ 28, V01 p. 281.** The parents searched the **English partial-translation PDF** — a true result for that file — and generalised it to the repository |
| **2** | *"no vocalised prose on disk"* — H-NEW-2870 §6.2/§13.1, H-NEW-2880 §5.2 and their pre-registrations | 50,884 records; al-Bukhārī 0.7702 ḥarakāt/char, unit-final vocalisation 0.9426. Already at 0.770 in H-NEW-2730 | **The negative control of the whole pausal-rhyme family, three findings deep.** Run as H-NEW-2890; corrected in 2880 §5.2 |
| **3** | *"A formal count would require a ḥadīth-database (Maktaba Shamela, lidwa.com, or **sunnah.com index**) which is not on disk"* — H-NEW-860 | The on-disk corpus **is** a sunnah.com scrape: 50,884 records, per-book and per-chapter indices, Arabic + English + narrator fields | **A formal fadāʾil count.** The finding substituted a hand-built "rough-rubric" and its UAS correlation rests on that rubric. **Re-runnable now** — it was already named H-NEW-860.1 |
| **4** | *"Qirāʾāt data and a rasm/imlāʾ divergence set, **neither of which is on disk**"* — `STATE-OF-THE-PROJECT-2026-08-07.md` §5 item 5 | **Already refuted in writing** by H-NEW-2740 §10: the divergence set is constructible from two on-disk files — 6,919 tokens, 2,093 skeleton-pairs — and was built there | The orthographic questions §5 calls *"never been able to touch"*. **Half of item 5 is wrong and uncorrected**; the qirāʾāt half is TRUE |
| **5** | *"al-Ṭabarsī, Majmaʿ al-bayān — not on disk. **AWAITING ACQUISITION**"*; same for *al-Durr al-manthūr* and al-Zamakhsharī's *Kashshāf* — `surahs/Q001-al-fatiha/03-tafsir-survey.md` and its JOURNAL | All three present: `tabarsi-majma-bayan.openiti.raw.txt` (14.4 MB), `suyuti-durr-manthur.openiti.raw.txt` (15.5 MB), `zamakhshari-kashshaf/` — **plus per-surah extractions already cut for Q001/Q002** | Three mufassirūn excluded from the Q001 tafsir survey and from any survey that copied its "awaiting acquisition" list. al-Ālūsī, al-Saʿdī and al-Ghazālī's *Mishkāt al-Anwār* on the same list are genuinely absent |

### PARTIAL — related material present, stated requirement not met

| # | claim | gap, numerically |
|:--|:--|:--|
| 6 | H-NEW-930: per-poem line-count tabulation *"not on disk in tabular form"* | The 14 `diwan-*.txt` files are present, 17,196 lines total. **Not absent — underived.** `wc -l` closes it |
| 7 | H-NEW-2870/2880: *"the prose delta is not computable"* | True of `data/baseline-corpora/` (0 ḥarakāt over 2,056,880 and 1,422,374 chars); false of the repository. Now computed |
| 8 | **The largest single class in the repository**: *"Per-Q044 raw extractions of all 7 mufassirūn are NOT on disk as discrete files"* and its siblings across Q044, Q056, Q112 | The **consolidated** OpenITI sources are present (10 files, 7.8–29.7 MB each) and the findings say so in the same breath, citing line-offsets within them. **Underived, not absent.** Writing it as a data-gap retires a question a `grep` would answer |

### TRUE — verified absent, with what would be needed

| claim | verification | what would be needed |
|:--|:--|:--|
| Dependency treebank / syntax data (FRONTIER C-12, STATE §5.1) | `data/syntax/` contains exactly one file, `UD-QURAN-SOURCE.md` | The UD-Quran package; the manifest gives the recipe and SHA-256s |
| al-Zarkashī *al-Burhān* has no text layer (cited by 2610, 2630, 2640, 2800, 2870, 2880) | `pdftotext -l 40` returns **0 characters, 0 Arabic** | OCR, or a text-layer edition |
| ~~al-Suyūṭī *Itqān* lacks the *waqf* nawʿ~~ — **REFUTED, see FALSE #1** | True only of the English PDF: 28,680 lines, **0 hits**. The Arabic Itqān in the same directory has the nawʿ in full | Nothing — it is on disk |
| Ibn al-Jazarī *al-Nashr*; al-Dānī *al-Muqniʿ*; al-Sajāwandī *ʿIlal al-wuqūf*; al-Sakkākī *Miftāḥ*; al-Khalīl *Kitāb al-ʿAyn*; al-Jawālīqī *al-Muhadhdhab* | `find` returns **NONE** for each | Acquisition; do not mistake `dani-23-site-supplement.tsv` for *al-Muqniʿ* |
| Lane's Lexicon, Hans Wehr (H-NEW-41-B) | `find` returns nothing outside unrelated library files | Blocks the H-NEW-41 repair |
| Pickthall translation (H-NEW-710) | `data/translations/` holds Sahih International only | — |
| Tao Te Ching, Psalms, Mishnah, Mahābhārata, Avesta (H-NEW-900) | `find` returns **NONE** for each | Blocks the cross-text generality claim |
| Vocalised *adab* prose (al-Jāḥiẓ) and vocalised dīwāns (STATE §5.4a) | 0 ḥarakāt over 1,422,374 chars; all 8 dīwāns at ratio 0.000 | Still the real gap — the ḥadīth find does **not** close it |
| `cross-finding-028` pairs 7, 8, 9 not attested in the 9-book corpus | Re-verified: **0 co-occurrences** in 50,884 records; positive control reproduces `tirmidhi#2975` | Nothing — the claim is sound |

---

## 7. How to apply this in a future session

1. Run §3 Screen A's grep. Expect on the order of a hundred hits.
2. For each, apply Screen B: **does the claim state its search?** If not, it is unverified.
3. Apply Screen C: **grep the cited parents for the missing thing** before anything else. It
   is one command and it is the step that would have caught the case in §2.
4. Verify against the filesystem — `find`, real file contents, measured properties — **never
   against another document's summary of the filesystem.** The summary is the thing that
   propagates.
5. Classify TRUE / FALSE / PARTIAL. For FALSE, **name every finding that was weakened,
   limited, or declined because of it** — those are the re-runs, and they are the output that
   matters.
6. Correct the document that *carries* the claim, not only the one that refutes it (§4).

**Expect to find more than one.** Absence claims compound precisely because they are
invisible: nobody notices the experiment that was never run.

---

*Written 2026-08-07 by Waiel Al-Shujaa, after asserting three times over that a corpus was
missing which my own cited parent had already measured at 0.770. A claim of absence is a claim
about a search. Bismillāhi al-Raḥmāni al-Raḥīm.*
