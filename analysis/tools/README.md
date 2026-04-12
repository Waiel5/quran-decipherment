# `analysis/tools/` — Core Python analysis library

Small, single-purpose modules for loading and counting the amrayn
`quran-text` JSON corpora under explicit, disclosed counting rules.

**Dependencies:** Python 3 stdlib only. No NumPy, pandas, or third-party
packages. Tested with Python 3.9+.

**Primary corpus:** `quran-no-tashkeel.json`, per the `text-shape`
investigation (the flat `min`/`full` files are truncated; only the JSON
files are intact). See `docs/methodology.md` §1 and
`journal/text-shape-investigation.md` for details.

All counting functions operate on **already-loaded text** (a `str` or
a list of `Surah` dataclasses) so callers control the orthography
variant via one explicit call to `load_quran`.

Every public function documents which fields of the rules tuple
(`orthography`, `word_definition`, `letter_definition`,
`basmala_policy`, `abjad_table`) it operates on.

---

## Modules

### `loader.py` — JSON loader

```python
from tools.loader import load_quran, Surah, Verse

quran = load_quran("no-tashkeel")          # 114 Surah dataclasses
quran = load_quran("min-tashkeel")
quran = load_quran("full-tashkeel")
load_quran("uthmani-rasm")                  # raises ValueError
```

Each `Surah` has `(id, name, transliteration, type, total_verses, verses)`;
each `Verse` has `(id, surah_id, text)`. Verse `text` is the raw JSON
value — no normalization, no recitation-mark filtering.

**Basmala policy by construction:** the amrayn dataset stores the
basmala **only** as surah 1 verse 1. The loaded data is therefore in
the `basmala-counted-only-in-surah-1` state. Use
`tools.basmala.apply_basmala_policy` to switch.

### `tokenize.py` — Whitespace tokens and letter counts

```python
from tools.tokenize import (
    RECITATION_MARKS, LETTER_RANGES, SHADDA,
    whitespace_tokens, real_words,
    is_letter, is_recitation_mark,
    graphemes, graphemes_with_shadda_doubled,
)

text = "بسم الله الرحمن الرحيم"
whitespace_tokens(text)                # ['بسم', 'الله', 'الرحمن', 'الرحيم']
real_words(text)                       # same, with rec-mark-only tokens dropped
is_letter("ب")                         # True
is_letter("\u06D6")                    # False (recitation mark)
graphemes(text)                        # 19
graphemes_with_shadda_doubled(text)    # 19 (no shadda in no-tashkeel)
```

- `whitespace_tokens` implements `word_definition = orthographic-token`
  with **no** data cleaning.
- `real_words` implements the same with the text-shape data-cleaning
  filter: tokens made up entirely of recitation marks (U+06D6..U+06ED)
  are dropped. These ~4578 pseudo-tokens inflate the naive whitespace
  count in the no- and min-tashkeel JSONs.
- `graphemes` implements `letter_definition = graphemes`: Arabic
  letters in `U+0621..U+064A ∪ U+0671..U+06D3`, excluding tashkeel,
  tatweel, and recitation marks.
- `graphemes_with_shadda_doubled` implements
  `letter_definition = with-shadda-doubled`.

### `gematria.py` — Abjad / gematria

```python
from tools.gematria import (
    ABJAD_MASHRIQI, ABJAD_MAGHRIBI,
    abjad_value, word_value, text_value,
)

abjad_value("ب")                              # 2 (mashriqi default)
word_value("بسم")                             # 2 + 60 + 40 = 102
text_value("بسم الله الرحمن الرحيم")          # 786 (canonical anchor)
text_value("بسم الله الرحمن الرحيم", "maghribi")  # different value
```

Unknown letters trigger `warnings.warn` but contribute zero — the call
never fails. Tashkeel, hamza carriers, tanwin, and recitation marks
are silently skipped (no warning, no contribution).

### `basmala.py` — Basmala strings and policy

```python
from tools.basmala import (
    BASMALA_NO_TASHKEEL, BASMALA_FULL_TASHKEEL,
    basmala_stats, apply_basmala_policy,
)

basmala_stats("no-tashkeel")
# {'letters': 19, 'real_words': 4,
#  'graphemes_with_shadda': 19, 'abjad_mashriqi': 786}

quran = load_quran("no-tashkeel")
q_in_surah = apply_basmala_policy(quran, "counted-in-surah")
q_separator = apply_basmala_policy(quran, "always-separator")
```

Policies:

- `counted-only-in-surah-1` — unchanged (the data's natural state).
- `counted-in-surah` — prepends the canonical basmala to verse 1 of
  each of the 112 surahs that don't already carry it (Al-Fatiha is
  unchanged, At-Tawba is excluded by tradition). Net effect:
  **+113 basmalas** across the corpus.
- `always-separator` — strips surah 1 verse 1 to empty.

### `shuffler.py` — Seeded null-model shufflers

```python
from tools.shuffler import (
    shuffle_characters, shuffle_words,
    shuffle_verse_order, shuffle_surah_indices,
)

shuffle_characters("بسم الله", seed=0)          # length-preserving char shuffle
shuffle_words("بسم الله الرحمن الرحيم", seed=0) # word-order shuffle within verse
shuffle_verse_order(quran[0], seed=0)           # shuffle verses within a surah
shuffle_surah_indices(quran, seed=0)            # permute surah order
```

All shufflers use `random.Random(seed)` for strict reproducibility. None
mutates the input. These are the primitive null-model operations for
Phase B; see `docs/statistical-rigor-protocol.md` §1.1, §1.2, §1.5.

---

## Tests

```
python3 -m unittest discover /Users/grey/Downloads/quran/analysis/tests -v
```

All tests pass against the locked anchors in `docs/methodology.md` §8.
If any test fails, the code and/or the anchors are out of sync —
investigate before "fixing."
