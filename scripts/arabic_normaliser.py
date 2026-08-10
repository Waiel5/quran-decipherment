#!/usr/bin/env python3
"""Arabic normalisers for the Uthmani/simple orthography comparison (F-9 / H-NEW-3100).

Two functions, deliberately kept distinct, because *no single character-level
normaliser can satisfy all four of the assertions the task specifies* (see
`selftest()` and the proof in `PROOF_A1_A3_INCOMPATIBLE`).

  bare(s)      letter skeleton, ALEF-PRESERVING.
               Drops harakat, tanwin, sukun, shadda, maddah, tatweel and the
               Quranic recitation annotations; folds superscript alef and alef
               wasla onto plain alef; composes hamza carriers via NFC.
               Hamza carriers (alef/waw/yeh seats) are RETAINED as distinct
               letters -- they are letters of the rasm, not diacritics.

  skeleton(s)  consonantal skeleton, ALEF-DELETING and SEAT-NEUTRAL.
               bare(s), then every alef-family character removed and every
               hamza carrier folded to bare hamza. This is the level at which
               an *elisive* merge such as ya + ibna + umm -> yabna'umma is an
               exact concatenation.

Neither is "the" right answer. `bare` is the primary instrument; `skeleton` is
the fallback used to decide whether a merge that is not concatenative under
`bare` is concatenative once alef elision is allowed. Reporting both is what
keeps the two merge mechanisms separable instead of silently pooled
(cross-finding-030 mechanism 1: a class that is not homogeneous in its strata).

Run `python3 scripts/arabic_normaliser.py` to print the assertion results.
"""

import sys
import unicodedata


# --- character classes -------------------------------------------------------

# Harakat + tanwin + sukun + shadda + the two dagger-style marks and the
# combining hamza signs. NOT included: U+0670 (superscript alef) and U+0671
# (alef wasla), which are handled as letters below.
TASHKEEL = {
    "ً",  # FATHATAN
    "ٌ",  # DAMMATAN
    "ٍ",  # KASRATAN
    "َ",  # FATHA
    "ُ",  # DAMMA
    "ِ",  # KASRA
    "ّ",  # SHADDA
    "ْ",  # SUKUN
    "ٓ",  # MADDAH ABOVE
    "ٔ",  # HAMZA ABOVE
    "ٕ",  # HAMZA BELOW
    "ٖ",  # SUBSCRIPT ALEF
    "ٗ",  # INVERTED DAMMA
    "٘",  # MARK NOON GHUNNA
    "ٙ",  # ZWARAKAY
    "ٚ",  # VOWEL SIGN SMALL V ABOVE
    "ٛ",  # VOWEL SIGN INVERTED SMALL V ABOVE
    "ٜ",  # VOWEL SIGN DOT BELOW
    "ٝ",  # REVERSED DAMMA
    "ٞ",  # FATHA WITH TWO DOTS
    "ٟ",  # WAVY HAMZA BELOW
}

# Quranic recitation / waqf annotation marks: pause signs, sajdah, silent-letter
# zeros, and the small-letter vowel restorations. All are reading aids layered
# over the rasm, none is a letter of it.
QURANIC_ANNOTATION = {chr(c) for c in range(0x06D6, 0x06EE)}

TATWEEL = "ـ"

# Letters that are realisations of alef in the Uthmani rasm.
SUPERSCRIPT_ALEF = "ٰ"
ALEF_WASLA = "ٱ"
ALEF = "ا"

# Pure matres lectionis: alef and alef maksura carry no consonant of their own,
# and are exactly what an elisive merge deletes. `skeleton` drops these.
# Hamza-bearing alef (U+0622/0623/0625) is NOT here -- it is a hamza carrier,
# handled by HAMZA_SEATS below, and the two rules must not overlap.
ALEF_FAMILY = {ALEF, "ى"}

# Hamza carriers -> bare hamza, for `skeleton` only. Applied INSTEAD of, not
# after, the alef deletion: these characters carry a real consonant.
HAMZA_SEATS = {"آ": "ء", "أ": "ء", "إ": "ء",
               "ؤ": "ء", "ئ": "ء", "ء": "ء"}


PROOF_A1_A3_INCOMPATIBLE = """\
A1 requires bare("YA") == alef-bearing 2-letter string (ya + alef).
A3 requires bare("YABNA'UMMA") == bare("YA") + bare("IBNA") + bare("UMMA").
The Uthmani token YABNA'UMMA contains 5 letter characters (ya, ba, nun,
waw-with-hamza, mim) and NO alef. Any character-level normaliser is a map that
sends each input character to zero or more output characters; under A1 alef
survives (it is in the output of bare("YA")), so the right-hand side has at
least 2 + 3 + 2 = 7 letter characters while the left-hand side has at most 5.
7 > 5, so the two assertions cannot both hold. A3 is not a statement a
normaliser can be fixed to satisfy: it is a statement about the DATA, namely
that this merge deletes two alefs and changes a hamza seat."""


# --- normalisers -------------------------------------------------------------

def bare(text):
    """Letter skeleton, alef-preserving. Satisfies A1, A2, A4."""
    # NFC first: the Uthmani text writes some hamza carriers as base + U+0654,
    # and alef-madda as alef + U+0653. NFC folds those onto the precomposed
    # letters the simple text uses, so the two orthographies agree before any
    # stripping happens.
    text = unicodedata.normalize("NFC", text)
    out = []
    for ch in text:
        if ch in TASHKEEL or ch in QURANIC_ANNOTATION or ch == TATWEEL:
            continue
        if ch == SUPERSCRIPT_ALEF or ch == ALEF_WASLA:
            out.append(ALEF)
            continue
        out.append(ch)
    return "".join(out)


def skeleton(text):
    """Consonantal skeleton: bare(), minus alef, hamza seats neutralised.

    Satisfies A3. Does NOT satisfy A1 (by the proof above).
    """
    out = []
    for ch in bare(text):
        if ch in HAMZA_SEATS:          # checked first: a seat is a consonant
            out.append(HAMZA_SEATS[ch])
            continue
        if ch in ALEF_FAMILY:          # pure mater lectionis: elidable
            continue
        out.append(ch)
    return "".join(out)


# --- self test ---------------------------------------------------------------

# The four assertions as dispatched, written with explicit codepoints so the
# test does not depend on how this file was transported.
A_YA = "يَا"                                      # ya + fatha + alef
A_YA_AYYUHA = ("يَٰٓأَي"
               "ُّهَا")                 # ya'ayyuha, joined
A_AYYUHA = "أَيُّهَا"    # 'ayyuha
A_YABNAUMMA = ("يَبْنَؤ"
               "ُمَّ")                       # yabna'umma, joined
A_IBNA = "ابْنَ"                        # ibna
A_UMMA = "أُمَّ"                        # 'umma
A_ALNAS_U = "ٱلنَّاسُ"   # al-nasu, wasla
A_ALNAS_S = "النَّاسُ"   # al-nasu, plain


def selftest():
    checks = []

    def check(label, got, want, fn="bare"):
        ok = got == want
        checks.append((label, fn, ok, got, want))
        return ok

    check("A1  bare(ya) == 'ya'", bare(A_YA), "يا")
    check("A2  bare(ya'ayyuha) == bare(ya) + bare('ayyuha)",
          bare(A_YA_AYYUHA), bare(A_YA) + bare(A_AYYUHA))
    check("A3  bare(yabna'umma) == bare(ya)+bare(ibna)+bare('umma)",
          bare(A_YABNAUMMA), bare(A_YA) + bare(A_IBNA) + bare(A_UMMA))
    check("A4  bare(al-nasu wasla) == bare(al-nasu plain)",
          bare(A_ALNAS_U), bare(A_ALNAS_S))
    check("A3' skeleton(yabna'umma) == skeleton(ya)+skeleton(ibna)+skeleton('umma)",
          skeleton(A_YABNAUMMA),
          skeleton(A_YA) + skeleton(A_IBNA) + skeleton(A_UMMA), fn="skeleton")
    check("A1' skeleton(ya) == 'ya'  (EXPECTED TO FAIL - see proof)",
          skeleton(A_YA), "يا", fn="skeleton")

    width = max(len(c[0]) for c in checks)
    print("=" * 78)
    print("NORMALISER SELF-TEST")
    print("=" * 78)
    for label, fn, ok, got, want in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {label:<{width}}  ({fn})")
        print(f"         got  {got!r}")
        print(f"         want {want!r}")
    print("-" * 78)
    a1, a2, a3, a4, a3p, a1p = [c[2] for c in checks]
    print(f"bare():     A1 {'PASS' if a1 else 'FAIL'}   A2 {'PASS' if a2 else 'FAIL'}"
          f"   A3 {'PASS' if a3 else 'FAIL'}   A4 {'PASS' if a4 else 'FAIL'}")
    print(f"skeleton(): A3 {'PASS' if a3p else 'FAIL'}   A1 {'PASS' if a1p else 'FAIL'}"
          f" (fails by construction)")
    print("-" * 78)
    if not a3:
        print(PROOF_A1_A3_INCOMPATIBLE)
        print("-" * 78)
    required = a1 and a2 and a4 and a3p and not a1p
    print("GATE:", "PASS" if required else "FAIL",
          "- bare() satisfies A1/A2/A4 and skeleton() satisfies A3.")
    return 0 if required else 1


if __name__ == "__main__":
    sys.exit(selftest())
