# Weapons & Warfare Run 1 — Journal

Agent: Phase B weapons/warfare vocabulary.
Data: `data/morphology/quranic-corpus-morphology-0.4.txt` (Buckwalter) + `quran-text/quran-min-tashkeel.json` + `data/morphology/root-stats.csv`.

## Method
1. Pulled root-level counts from `root-stats.csv` for each candidate weapon/warfare root.
2. Extracted all occurrences of low-frequency roots (1–15 tokens) from the Buckwalter morphology file to verify locations and check for polysemy (e.g. `shm`, `xyl`, `qws`).
3. Pulled verse text (minimal tashkeel) for each battle passage and legal-warfare pericope; for David's armor-craft; for the Ṣāliḥ she-camel cycle.
4. Counted `fī sabīl Allāh` as a phrase using unvocalised text regex (43 verses, 45 occurrences). Measured co-occurrence with q-t-l (19 verses) and j-h-d (11 verses).
5. Built by-surah distribution for q-t-l and j-h-d directly from morphology ROOT fields.

## Key findings that surprised me
- **No `s-y-f` (sword) root, no `t-r-s` (shield) root.** Zero. The classic Arabian warrior noun `sayf` is absent from the Qurʾān. This is the single most striking datum.
- **`sahm` (37:141) is not a weapon** — it is Yūnus casting lots (`sāhama`), semantically "share, allotment".
- **`qaws` (53:9) is not a weapon either** — `qāba qawsayni aw adnā` is a distance idiom at the Lote-tree, not an archer's bow.
- **`rimāḥ` (5:94) — the only true weapon noun used as a weapon** — and it is for pilgrims hunting game, not combat.
- **`Hrb` root (war): of 11 tokens, 5 are `miḥrāb` (prayer niche).** Only 6 mean "war"; the rest describe Mary's and Zakariyya's sanctuary.
- **David's "iron-armour" in Q 34:10–11 uses root `sbg` (sābighāt = flowing full-length mail), not `msd`**. The user's prompt flagged `miswad Q 34:10`; the actual root at 34:10 is `Hdd` (al-ḥadīd = iron) + `sbg` at 34:11. The lemma `msd` appears only at Q 111:5 (Abū Lahab's wife's fibre rope). I record the correction.
- **`ghazwa` (raid) — 1 token total** (Q 3:156, `ghuzzā`), and it appears in a verse *criticising* those who speak of raiding. There is no celebratory "ghazwa" vocabulary.
- **`maʿraka` — 0 tokens.** The Qurʾān never uses the word "battle" in that technical sense. Fighting is described with verbs (`qātala`), `qitāl` (the masdar), `liqā'` (encounter), or `yawm` + place-name (Ḥunayn, Badr).
- Battle-days are referenced by **place-name** + `yawm`: Badr (3:123), Ḥunayn (9:25), al-Aḥzāb (33:9–27). Uḥud is *never named*; it is referred to obliquely (3:140–144, 152–155) through its consequences.
- `jund`/`junūd` (troops) — 29 tokens, 18 surahs — is the real warfare noun. Often the "troops" are **angelic or invisible** (9:26, 33:9, 48:4/7).
- The `fī sabīl Allāh` formula (45 occurrences, 43 verses) is the true organising frame: 19/43 pair it with q-t-l, 11/43 with j-h-d, remainder with `anfaqa` (spending), `hijra` (migration), `qaʿada` (sitting back). Warfare is one sub-category of "in the way of God", not its definition.

## Output
- 3000-word findings document at `findings/phase-b-hypotheses/weapons-warfare.md`.
- 400-word executive summary appended to this journal at bottom.

## Limitations
- Regex counts of `fī sabīl Allāh` used bare text (no tashkeel); may include 1–2 false positives or miss verses where a particle breaks the phrase.
- `jund` and `bāʾs` (might) were included as contextual, not primary targets.
- No manuscript/qirāʾāt variation checked.

## Executive summary (400 words)

The Qurʾānic Arabic of warfare is almost entirely a vocabulary of *action and actor*, not of *implement*. The weapons-naming lexicon — sword, shield, spear, arrow, bow, armour — is astonishingly thin. The root `s-y-f` (sword) and `t-r-s` (shield) do not appear at all. `r-m-ḥ` (spear) appears once (5:94), describing pilgrims reaching game animals. `q-w-s` appears once (53:9) as a distance measure at the Lote-tree vision ("two bow-lengths or nearer"), not a bow in combat. `s-h-m` appears once (37:141) and means "cast lots", not "arrow". The nearest thing to a sustained weapon mention is `aslihah` (arms), confined to a single verse on congregational prayer in combat-proximity (4:102, four tokens). Armour (`labūs`, `sābighāt`, `ḥadīd`) clusters in two passages about David's craft (21:80, 34:10–11).

By contrast, the verbs and masdars of fighting are very dense. `q-t-l` occurs ~170 times across 33 surahs — concentrated in Q 2 (31), Q 4 (25), Q 3 (21), Q 5 (13), Q 9 (13). Legal-war pericopes (2:190–194; 8:60–66; 9:5, 9:29; 47:4; 48:15–17) provide doctrinal infrastructure. `j-h-d` occurs 41 times, with its densest node in Q 9 (11 tokens); in Meccan-period usage (e.g. Q 25:52, Q 29:6, 29:8, 29:69, 31:15) it clearly extends to non-violent striving — refusing parents, bearing polytheist pressure, striving against one's own soul.

Named battles are anchored by place + `yawm` rather than `maʿraka` (never used). Badr (3:123), Ḥunayn (9:25), and al-Aḥzāb (33:9–27) are named; Uḥud is the great un-named defeat, alluded to via "wound", "losing position", and dissension (3:140–155). Across all three, divine agency displaces human weaponry: angelic `junūd` descend (9:26, 33:9), wind is sent (33:9), tranquillity (`sakīnah`) is "sent down", `ruʿb` (terror) is cast in enemy hearts (33:26). Prisoners-of-war receive a deliberately non-warlike norm (8:67–70, 47:4): freeing or ransom is preferred; `ḥattā taḍaʿa l-ḥarbu awzārahā` ("until war lays down its burdens", 47:4) is framed as war's *termination*, not its celebration.

The Ṣāliḥ she-camel cycle (7:73, 11:64, 26:155, 54:27, 91:13) encodes the anti-warfare counterpoint: a `nāqah` sent as `āyah`, destroyed by `ʿaqr` (hamstringing) — the lexeme of unilateral violence against a peace-sign. The Qurʾānic ideal of right-ordered force is David's armour-weaving (21:80), which is defensive (`li-tuḥṣinakum min ba'sikum`, "to fortify you from your own violence").
