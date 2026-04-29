# toolsmith run 1 — core analysis library

Date: 2026-04-12
Agent: toolsmith
Status: complete — all anchors green

## Mission

Build the stdlib-only Python analysis library under
`/Users/grey/Downloads/quran/analysis/tools/` that the rest of the
team will use for Phase A replications and Phase B hypothesis
hunting. Tests must reproduce every locked anchor in
`docs/methodology.md` §8.

## Files written

- `/Users/grey/Downloads/quran/analysis/tools/__init__.py` — empty package marker
- `/Users/grey/Downloads/quran/analysis/tools/loader.py` — `load_quran(variant)` + `Surah` / `Verse` dataclasses; documents amrayn's `counted-only-in-surah-1` state by construction
- `/Users/grey/Downloads/quran/analysis/tools/tokenize.py` — `RECITATION_MARKS`, `LETTER_RANGES`, `whitespace_tokens`, `real_words`, `is_letter`, `is_recitation_mark`, `graphemes`, `graphemes_with_shadda_doubled`
- `/Users/grey/Downloads/quran/analysis/tools/gematria.py` — `ABJAD_MASHRIQI`, `ABJAD_MAGHRIBI`, `abjad_value`, `word_value`, `text_value`; warns (doesn't error) on non-table letters, silently skips tashkeel/hamza-carriers/recitation marks/digits
- `/Users/grey/Downloads/quran/analysis/tools/basmala.py` — canonical basmala strings per variant, `basmala_stats`, `apply_basmala_policy` with the three policies
- `/Users/grey/Downloads/quran/analysis/tools/shuffler.py` — `shuffle_characters`, `shuffle_words`, `shuffle_verse_order`, `shuffle_surah_indices`, all seeded via `random.Random(seed)`
- `/Users/grey/Downloads/quran/analysis/tools/README.md` — public API + one example per function + dependencies (stdlib only)
- `/Users/grey/Downloads/quran/analysis/tests/__init__.py` — package marker
- `/Users/grey/Downloads/quran/analysis/tests/test_anchors.py` — stdlib unittest, 22 tests covering every §8 anchor

## Test output (final summary line)

```
Ran 22 tests in 0.645s

OK
```

Breakdown (one line per test):

```
test_basmala_abjad_mashriqi_is_786 ... ok
test_basmala_letters ... ok
test_basmala_real_words ... ok
test_basmala_stats_dict ... ok
test_always_separator_letter_delta ... ok
test_always_separator_word_delta ... ok
test_counted_in_surah_letter_delta ... ok
test_counted_in_surah_word_delta ... ok
test_letter_graphemes (FullTashkeelAnchors) ... ok          # 327038
test_letter_plus_shadda (FullTashkeelAnchors) ... ok        # 349716
test_real_words (FullTashkeelAnchors) ... ok                # 77429
test_shadda_count (FullTashkeelAnchors) ... ok              # 22678
test_real_words (MinTashkeelAnchors) ... ok                 # 77430
test_recitation_mark_only_tokens (MinTashkeelAnchors) ... ok # 4578
test_whitespace_tokens_raw (MinTashkeelAnchors) ... ok      # 82008
test_letter_graphemes (NoTashkeelAnchors) ... ok            # 330709
test_real_words (NoTashkeelAnchors) ... ok                  # 77797
test_recitation_mark_only_tokens (NoTashkeelAnchors) ... ok # 4578
test_whitespace_tokens (NoTashkeelAnchors) ... ok           # 82375
test_surah_count_every_variant ... ok                       # 114
test_verse_count_every_variant ... ok                       # 6236
test_unknown_variant_raises_valueerror ... ok
```

All 22 anchor tests pass on first run (after the one implementation
fix noted below).

## Anchors that required code/anchor adjustment

**None of the headline anchors were wrong. One implementation detail
in `basmala.apply_basmala_policy` needed fixing:**

My first pass prepended the basmala to 112 surahs (excluding both
surah 1 — because Al-Fatiha already has verse 1 = basmala — and surah
9 At-Tawba). That produced deltas of +448 words / +2128 letters under
`counted-in-surah`, which is **not** what methodology §8 and
`text-shape-investigation.md` lock in. The locked anchor is
**+452 words / +2147 letters = exactly 113 × basmala**, meaning the
methodology's `counted-in-surah` policy is to prepend a basmala at the
head of every non-At-Tawba surah **including surah 1**. Under this
reading, Al-Fatiha ends up with the basmala counted twice: once as the
prepended header, once as its verse 1. I rewrote `apply_basmala_policy`
to match the anchor (only At-Tawba is excluded), added a docstring
note explaining the double-counting of Fatiha, and added four new
tests (`test_counted_in_surah_{word,letter}_delta`,
`test_always_separator_{word,letter}_delta`) so this adjustment is
locked by the test suite.

`always-separator` matched the anchor (-4 words / -19 letters) on the
first implementation: clearing surah 1 verse 1 to empty string is the
right operation.

No headline anchor values were "adjusted to match a buggy tool." The
code was wrong and I fixed the code.

## Methodology issues noticed

1. **`counted-in-surah` under-specified re: surah 1.** The methodology
   text says "the opening basmala of each surah counts toward that
   surah's letter/word totals," but doesn't say whether surah 1's
   basmala should be counted once (as its verse 1) or twice (as verse
   1 AND as an additional opening). The locked anchor arithmetic
   (113 × basmala) forces the "count twice" reading but the prose
   doesn't say so. I documented the resolution in the
   `apply_basmala_policy` docstring. Suggest adding one sentence to
   `docs/methodology.md` §4: "Under `counted-in-surah`, Al-Fatiha's
   basmala is counted twice — once as its verse 1 (by construction of
   the amrayn data) and once as the surah's opening header. This is
   the arithmetic that produces the §8 anchor +113 × basmala."
2. **`maghribi` abjad table is cited but not tabulated.** Methodology
   §6 mentions that Maghribi "differs in the assignments of س ص ض ظ
   غ ش ث خ ذ" but does not list the actual assignments. I wrote a
   standard widely-cited Maghribi table from memory (ص=60, ض=90, س=300,
   ظ=800, غ=900, ش=1000). Any future Phase A claim that requires
   Maghribi should cite its source table and we should lock a canonical
   Maghribi abjad in methodology.md §6 before it's trusted. Filing
   this as a to-fix, not a blocker, since no current anchor depends on
   Maghribi values.
3. **Hamza carriers and abjad.** The classical tables don't assign an
   abjad value to hamza-on-alif (أ), hamza-on-waw (ؤ), hamza-on-ya
   (ئ), standalone hamza (ء), alif-maqsura (ى), ta-marbuta (ة),
   dagger-alif (ٰ), or alif-with-wasla (ٱ). I silently skip all of
   these in `gematria.py` rather than warning, because warning on every
   occurrence would flood the logs on Uthmani text. A future refinement
   should pick an explicit policy per character (e.g. "alif-with-wasla
   counts as alif = 1") and document it in methodology §6 as a
   `hamza_policy` sub-rule. Not a blocker for current anchors.
4. **Aside: `graphemes_with_shadda_doubled` is simple on full-tashkeel
   but degenerate on no-tashkeel.** Since no-tashkeel has no U+0651
   characters at all, the function collapses to plain `graphemes` on
   that variant. I mention this in the docstring; Phase B hypothesis
   testers should be aware that if they want shadda-doubled counts on
   a no-tashkeel claim, they need to load full-tashkeel.

## Notes for other agents

- The shufflers are deep-copying; they're safe to call with fresh
  seeds per surrogate draw without worrying about state leakage. They
  use `random.Random(seed)` rather than a module-level random, so they
  compose cleanly with any outer reproducibility scheme Phase B adopts.
- `tools.loader.load_quran` returns plain dataclasses; callers can
  mutate the result without affecting future calls (the loader re-reads
  the JSON on each invocation, and dataclasses are not frozen).
- All counting functions take `str` or loaded `Surah` lists — never
  raw JSON paths. This is deliberate so tests are deterministic and
  callers control exactly which variant they're measuring.
- Tests can be run from anywhere via
  `python3 -m unittest analysis.tests.test_anchors -v` from the
  project root, or directly via
  `python3 /Users/grey/Downloads/quran/analysis/tests/test_anchors.py`.
