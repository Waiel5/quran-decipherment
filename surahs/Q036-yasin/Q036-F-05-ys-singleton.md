---
surah: 36
finding_id: Q036-F-05
title: YS muqaṭṭāʿat is the corpus-EXACT singleton surah-opener
date: 2026-05-09
phase: B+
verdict: PASS-DIRECTED-CORPUS-EXACT
pre_reg_sha256: 9cc710c5a340e52a98a9030c27edfe92031bad37b43b4a106dfdd33d62d6053f
---

# Q036-F-05 — YS muqaṭṭāʿat is the corpus-EXACT singleton (1/114)

## Result

Across all three orthographic conventions tested (`quran-no-tashkeel.json`, `quran-min-tashkeel.json`, `data/alt-text/quran-uthmani-consonantal.json`), the two-letter sequence **يس** appears as the entire opening verse of **exactly one** surah:

| Variant | Surahs with v1 == "يس" | Count |
|:--|:-:|:-:|
| no-tashkeel | `[36]` | 1 |
| min-tashkeel | `[36]` | 1 |
| Uthmani-consonantal | `[36]` | 1 |

**Verdict**: **PASS-DIRECTED-CORPUS-EXACT** — Q 36 is the only surah whose verse 1 is exactly "يس". The pre-committed singleton claim is upheld and is rules-tuple-stable across three independent orthographic lenses.

## Position in the muqaṭṭāʿat catalog

Q 36 is one of 29 muqaṭṭāʿat-opened surahs. The other 28 use different letter combinations:

- 1-letter: ص (Q 38), ق (Q 50), ن (Q 68) — 3 surahs.
- 2-letter: طه (Q 20), طس (Q 27) — 2 surahs.
- 3-letter: الم (Q 2, 3, 29, 30, 31, 32) — 6 surahs; الر (Q 10, 11, 12, 14, 15) — 5 surahs; طسم (Q 26, 28) — 2 surahs; حم (Q 40-46) — 7 surahs.
- 4-letter: المص (Q 7), المر (Q 13) — 2 surahs.
- 5-letter: كهيعص (Q 19) — 1 surah; حم عسق (Q 42, the 2-line composite) — 1 surah.

Q 36's "يس" is the **only YS combination in the corpus**, both as a 2-letter standalone and as a prefix/suffix of any other muqaṭṭāʿat string. Other 2-letter combinations (طه, طس) belong to distinct surahs with no other singleton claimant. This makes Q 36 a **structural fingerprint** in the muqaṭṭāʿat-axis: it is one of three "ungrouped" muqaṭṭāʿat openers (with Q 19 *kāf-hā-yā-ʿayn-ṣād* and Q 42's composite *ḥā-mīm | ʿayn-sīn-qāf*) that does not belong to any letter-family cluster (الم / الر / حم / طسم).

## Honest limits

- The "singleton" claim is at the level of the 2-letter ordered combination "يس" as an entire verse. The individual letters ي and س appear in countless other verses (as suffixes, pronouns, parts of common words).
- The 29-surah muqaṭṭāʿat catalog is a classical convention; we tested within it.
- The Uthmani-consonantal variant was used to confirm script-stability; the result is identical.

## Cross-references

- [[h-new-130-fisher-rao-residuals|H-NEW-130]] — muqaṭṭāʿat cluster identification at FR-residual level (Q 36 is in the YS-singleton sub-cluster).
- [[h-new-232-oq1-singleton-nearest-neighbor|H-NEW-232]] — YS-letter-centroid maps unexpectedly to the ḤM-cluster centroid.
- `00-overview.md` §3 — opening-formula catalog and the 3-surah cluster {Q 36, 38, 50} of muqaṭṭāʿat + Quran-oath openers.
- `05-classical-claims-audit.md` Audit 3 — corpus muqaṭṭāʿat-tier inventory.

## Cross-finding-008 marker function connection

[[cross-finding-008-muqattaat-marker-function|cross-finding-008]] frames muqaṭṭāʿat as a **structural marker** rather than a content-axis. Q 36's YS-singleton status reinforces that frame: the YS combination has no other corpus attestation as a surah-opener, so it cannot be a recurring "marker family" the way الم (6 surahs) or حم (7 surahs) are. Its function, if any, is **per-surah signature** rather than **cluster-membership**.

## Output

- `csv/Q036-F-05.json` — full JSON with all three variant survey results.

*Pre-reg sha-256 `9cc710c5a340…3d62d6053f` verified at runtime by the script's hash-check.*
