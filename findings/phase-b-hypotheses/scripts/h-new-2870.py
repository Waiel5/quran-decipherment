#!/usr/bin/env python3
"""
H-NEW-2870 — Is the fāṣila defined at PAUSAL phonology rather than citation form?

Runner. Pre-registration locked at
  findings/phase-b-hypotheses/prereg-h-new-2870-pausal-rhyme.md
  SHA-256 119753ad7862d66dfead2ff6de1032adee0a824cd7544cd8bc4d6688587508d4
verified at runtime below. Frozen inputs SHA-256 verified. Immutable run directory.

Reporting order is locked by prereg §9:
  gates -> class-collapse magnitude -> matched-collapse null -> delta -> controls -> per-surah.

Method parents: h-new-2690.py (phonemiser; scanner recovered 3/3 muʿallaqāt meters),
h-new-2730.py (within-corpus re-cut control), h-new-2240.py (skeleton rime classifier).

Waiel Al-Shujaa, 2026-08-07.
"""
import hashlib
import heapq
import json
import math
import os
import platform
import random
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)

PREREG = "findings/phase-b-hypotheses/prereg-h-new-2870-pausal-rhyme.md"
PREREG_SHA256 = "119753ad7862d66dfead2ff6de1032adee0a824cd7544cd8bc4d6688587508d4"

FROZEN = {
    "quran-text/quran-full-tashkeel.json":
        "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    "data/alt-text/quran-uthmani-txt.txt":
        "e5e7e54988877d6164832d55435135a563b9cfc249e0c8efd73e9e7f23231db8",
    "data/baseline-corpora/raw/muallaqa-imru-al-qais.txt":
        "06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14",
    "data/baseline-corpora/raw/muallaqa-zuhayr.txt":
        "9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2",
    "data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt":
        "d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720",
    "data/baseline-corpora/raw/bukhari-noquran.txt":
        "0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100",
    "data/baseline-corpora/raw/jahiz-hayawan.txt":
        "419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd",
}

SEED = 20260509
SEED_REP = 20260519
N_PERM = 10000
N_RECUT = 2000
N_PROSE_CUT = 200
# prereg §8 sets k=6 over {D2, D3, D4b} x {P1, P2}. REPAIR-1 splits D2 into two nulls
# (N1-a as pre-registered, N1-b the repair) and REPAIR-3 runs every test under two rime
# definitions, giving {D2a, D2b, D3, D4b} x {P1, P2} x {R1, R2} = 16. This TIGHTENS alpha
# from 0.008333 to 0.003125 and adds ten further ways to fail; a tightening self-verifies
# and needs no ratification (feedback_bonferroni_tightening_vs_loosening).
BONFERRONI_K = 16
ALPHA = 0.05 / BONFERRONI_K

# --smoke runs the identical code path at tiny replicate counts and writes NOTHING.
# Used only to debug the runner. Declared in the finding.
SMOKE = "--smoke" in sys.argv
if SMOKE:
    N_PERM, N_RECUT, N_PROSE_CUT = 50, 20, 5

LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s, flush=True)
    LOG.append(s)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def die(m):
    say(f"[FATAL] {m}")
    raise SystemExit(1)


# ---------------------------------------------------------------- 0. gates: SHA
_a = sha256_file(PREREG)
if _a != PREREG_SHA256:
    die(f"pre-reg SHA mismatch\n  expected {PREREG_SHA256}\n  actual   {_a}")
say(f"[SHA-OK] pre-reg locked: {_a}")
for p, want in FROZEN.items():
    g = sha256_file(p)
    if g != want:
        die(f"frozen input mismatch {p}\n  expected {want}\n  actual {g}")
say(f"[SHA-OK] {len(FROZEN)} frozen inputs verified")

# ---------------------------------------------------------------- 1. phonemiser
# Reused verbatim from scripts/h-new-2690.py §2.1 EXCEPT the tanwin-encoding fix
# declared in prereg §4.1/§4.2. See DECLARED_CHANGES below.
FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
SHADDA, SUKUN = "ّ", "ْ"
SUP_ALEF = "ٰ"
ALEF, WAW, YA = "ا", "و", "ي"
ALEF_MAQ, ALEF_MADDA, ALEF_WASLA = "ى", "آ", "ٱ"
TA_MARBUTA = "ة"
SHORT = {FATHA: "a", DAMMA: "u", KASRA: "i"}
TANWIN = {FATHATAN: "an", DAMMATAN: "un", KASRATAN: "in"}
CONS = set("ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيٱ")

# prereg §4.1: this file encodes 78% of its tanwin with three codepoints whose
# Unicode names do not describe their function. The method parent DROPs all three.
TANWIN_REMAP = {"ٗ": FATHATAN, "ٞ": DAMMATAN, "ٖ": KASRATAN}

# h-new-2690 DROP set MINUS ٖ ٗ ٞ (which are tanwin here, not noise).
DROP = set("ـۖۗۘۙۚۛۜ۞۟۠"
           "ۣۧۨ۩۪ۭ۫۬"
           "ٕٜٟٓٔ٘ٙٚٛٝ"
           "۝ࣰࣱࣲ")
SUKUN_ALT, SMALL_WAW, SMALL_YA = "ۡ", "ۥ", "ۦ"
FINAL_VOWELS = set(SHORT) | set(TANWIN)

DECLARED_CHANGES = [
    "prereg 4.2 change 1: U+0656/U+0657/U+065E remapped to the standard tanwin marks "
    "before normalisation, and removed from the inherited DROP set (h-new-2690 deletes "
    "6643 tanwin = 78% of the corpus total).",
    "prereg 4.2 change 2: U+0670 and U+06E1 handled as in the parent.",
    "CONSEQUENCE of change 1, not an independent modelling choice, declared in the "
    "finding: after a tanwin fath the parent skips a following ALEF only. Because the "
    "parent never reached this branch (the mark was dropped), ALEF_MAQSURA was not "
    "handled. Both are skipped here; hudan is one phoneme sequence, not two.",
]

# Three defects in the PRE-REGISTERED design, found by a --smoke run (which writes
# nothing) BEFORE the real run, and repaired by ADDING tests rather than replacing
# them. Every pre-registered quantity is still computed and still reported.
REPAIRS = [
    "REPAIR-1 (null): prereg §6.2's greedy cannot match the pausal verse-count profile "
    "-- measured total-variation distance ~0.6 -- because 116 target blocks must be "
    "built from only ~157 citation types, so most blocks receive exactly one type and "
    "the achievable profiles are pinned by the type-size multiset. prereg §6.2 itself "
    "instructs that an ill-posed null be reported as such. N1-a is therefore reported "
    "WITH its measured fidelity, and a second null N1-b is added: exact block-CARDINALITY "
    "match, compared on the excess over the chance floor E = A - sum(p_i^2). D2 now "
    "requires BOTH. Strictly a tightening.",
    "REPAIR-2 (poetry): the muallaqat carry harakat on only 72-84% of their characters, "
    "so a nucleus-bearing rime mis-reads any line-final word whose internal short vowels "
    "are unwritten (fa-hawmali parses as a 3-consonant coda and fails to rhyme with "
    "manzili, which it does rhyme with). A rime-region readability criterion is added -- "
    "no nucleus, or an apparent coda longer than the two consonants a word-final Arabic "
    "cluster can hold -- and the poetry arm is reported BOTH unrestricted and on "
    "readable-only pairs. Readability is measured on the INPUT, never on a result.",
    "REPAIR-3 (rime): under prereg §4.3 the tanwin nun is the last consonant and is "
    "therefore read as the rawi, so the citation rime of every tanwin word is just "
    "-un/-in/-an: azimun scores the same as mubinun, and hasanan the same as waladan. "
    "None of those rhyme. The defect is asymmetric across conventions -- for a tanwin "
    "word R1 reads the TANWIN syllable under C and the STEM-final syllable under P -- "
    "which is the like-for-like depth §4.3 was written to guarantee. R1 inflates A(C) "
    "and so UNDERSTATES the delta. A second rime definition R2 (tanwin-transparent) is "
    "added and EVERY test is run under both. R1 and R2 bracket the answer.",
]


def normalize(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(TANWIN_REMAP.get(c, c) for c in t)          # prereg §4.1
    t = "".join(c for c in t if c not in DROP)
    t = t.replace(SUKUN_ALT, SUKUN).replace(SMALL_WAW, WAW).replace(SMALL_YA, YA)
    t = t.replace(ALEF_MADDA, "أ" + FATHA + ALEF).replace(ALEF_WASLA, ALEF)
    t = re.sub(ALEF + FATHA, FATHA + ALEF, t)
    t = re.sub("([" + FATHA + DAMMA + KASRA + FATHATAN + DAMMATAN + KASRATAN + "])"
               + SHADDA, SHADDA + r"\1", t)
    return t


def phonemes(word):
    """Returns list of (kind, value, src). kind in C/V/VV. src tags tanwin origin
    and ta-marbuta so the pausal conventions can be applied to the phoneme list
    rather than by re-parsing text."""
    out, i = [], 0
    w = normalize(word)
    while i < len(w):
        ch = w[i]
        if ch in CONS:
            nxt = w[i + 1] if i + 1 < len(w) else ""
            if out and out[-1][0] == "V":
                pv = out[-1][1]
                if (ch in (ALEF, ALEF_MAQ) and pv == "a") \
                   or (ch == WAW and pv == "u" and nxt not in SHORT and nxt != SHADDA
                       and nxt not in TANWIN) \
                   or (ch == YA and pv == "i" and nxt not in SHORT and nxt != SHADDA
                       and nxt not in TANWIN):
                    out[-1] = ("VV", pv, out[-1][2])
                    i += 1
                    if i < len(w) and w[i] == SUKUN:
                        i += 1
                    continue
            src = "ta" if ch == TA_MARBUTA else ""
            out.append(("C", ch, src)); i += 1
            if i < len(w) and w[i] == SHADDA:
                out.append(("C", ch, src)); i += 1
            if i < len(w) and w[i] == SUP_ALEF:
                out.append(("VV", "a", "")); i += 1; continue
            if i < len(w) and w[i] in SHORT:
                out.append(("V", SHORT[w[i]], "")); i += 1
            elif i < len(w) and w[i] in TANWIN:
                v = TANWIN[w[i]]
                tag = "tanwin-" + v[0]
                out.append(("V", v[0], tag)); out.append(("C", "ن", tag)); i += 1
                if v[0] == "a" and i < len(w) and w[i] in (ALEF, ALEF_MAQ):
                    i += 1
            elif i < len(w) and w[i] == SUKUN:
                i += 1
        elif ch == SUP_ALEF:
            out.append(("VV", "a", "")); i += 1
        else:
            i += 1
    return out


# ---------------------------------------------------------------- 2. conventions
def apply_convention(ph, conv):
    """prereg §5. ph is the CITATION phoneme list; returns the list under `conv`."""
    ph = list(ph)
    if conv == "C":
        return ph
    # --- tanwin ---
    if len(ph) >= 2 and ph[-1][2].startswith("tanwin") and ph[-2][2].startswith("tanwin"):
        kind = ph[-1][2]
        ph = ph[:-2]
        if kind == "tanwin-a" and conv in ("P1", "P2"):
            ph.append(("VV", "a", ""))          # waqf bi-l-alif
        # P3: tanwin fath dropped WITHOUT the compensatory alif (deliberately wrong tuple)
    elif ph and ph[-1][0] == "V":
        ph = ph[:-1]                            # iskan: final short vowel drops
    if conv == "P2" and ph and ph[-1][0] == "C" and ph[-1][2] == "ta":
        ph = ph[:-1] + [("C", "ه", "")]         # ta marbuta -> ha
    return ph


VOWEL_LONG = {"a": "A", "u": "U", "i": "I"}


def rime_parts(ph):
    """prereg §4.3 — the classical ridf / rawi / majra, as an algorithm.
    Returns (rime_string, readable). `readable` is False when the rime cannot be
    read off the text because internal short vowels are not written: either no
    nucleus exists at all, or the apparent coda exceeds the two consonants that a
    word-final Arabic cluster can contain. See REPAIR-2 in the finding."""
    if not ph:
        return "∅", False
    majra = ""
    if ph[-1][0] == "V":
        majra = ph[-1][1]
        ph = ph[:-1]
    if not ph:
        return "∅" + majra, False
    j = len(ph)
    while j > 0 and ph[j - 1][0] == "C":
        j -= 1
    coda = "".join(x[1] for x in ph[j:])
    ncoda = len(ph) - j
    if j == 0:
        return "?" + coda + majra, False           # no nucleus at all (unvocalised)
    nuc = ph[j - 1]
    n = VOWEL_LONG[nuc[1]] if nuc[0] == "VV" else nuc[1]
    return n + coda + majra, (ncoda <= 2)


def rime2_parts(ph):
    """R2 — the tanwin-transparent rime. REPAIR-3.

    Under R1 the tanwin nun is the last consonant, so it is read as the rawi and the
    citation rime of ANY tanwin word is just -un / -in / -an: `azimun` and `mubinun`
    both score `un` and are counted as rhyming, as do `hasanan` and `waladan`. They do
    not rhyme; the tanwin nun is never the rawi. Worse, the defect is asymmetric across
    the two conventions — for a tanwin word R1 reads the rime of the TANWIN syllable
    under C and the rime of the STEM-final syllable under P, which is exactly the
    like-for-like depth that prereg §4.3 was written to guarantee.

    R2 strips the tanwin to expose the stem, computes the R1 rime of the stem, and
    appends the tanwin vowel as the majra (tagged `~`). R2 == R1 under P1/P2/P3, where
    the convention has already removed the tanwin. R1 inflates A(C) and therefore
    UNDERSTATES the delta; R1 and R2 bracket the answer and both are reported."""
    tan = ""
    if len(ph) >= 2 and ph[-1][2].startswith("tanwin") and ph[-2][2].startswith("tanwin"):
        tan = "~" + ph[-2][1]
        ph = ph[:-2]
    s, ok = rime_parts(ph)
    return s + tan, ok


RIME_VARIANT = "R1"


def rime_parts_v(ph):
    return rime_parts(ph) if RIME_VARIANT == "R1" else rime2_parts(ph)


def rime(ph):
    return rime_parts_v(ph)[0]


ANNOT = set("ۖۗۘۙۚۛۜ۞ۣ۟۠ۧۨ۩۪ۭ۫۬۝ـ")
PUNCT = set("؟،.!?:؛\"'»«()[]{}-–—*_/\\|~؍٪")


def final_word(text):
    toks = [t for t in text.split() if any("ء" <= c <= "ي" for c in t)]
    if not toks:
        return ""
    w = toks[-1]
    return "".join(c for c in w if c not in PUNCT)


def rime_of(text, conv):
    w = final_word(text)
    if not w:
        return "∅"
    return rime(apply_convention(phonemes(w), conv))


def readable_of(text):
    w = final_word(text)
    if not w:
        return False
    return rime_parts_v(apply_convention(phonemes(w), "C"))[1]


# ---------------------------------------------------------------- 3. skeleton rime
# Ported from scripts/h-new-2240.py classify(): the validated SKELETON instrument.
# Used ONLY for the cross-corpus level comparison (prereg §6.5), because the prose
# baselines carry no harakat and the phonemic instrument cannot read them.
S_LONG = set("اويى")
S_STRIP = set("ًٌٍَُِّْٕٓٔـۛۜ۝۞ۣ۟۠ۡۢۤۥۦۧۨ۩۪ۭٖ۫۬ٗٞۖۗۘ"
              "ۙۚۛۜۡ‌‍‎‏")
S_CARRIER = {"ؤ", "ئ", "أ", "إ", "آ"}


def skel_rime(text):
    w = final_word(text)
    if not w:
        return "∅"
    out = []
    for ch in w:
        if ch == SUP_ALEF:
            out.append("ا")
        elif ch in S_STRIP:
            continue
        else:
            out.append(ch)
    w = "".join(out)
    if not w:
        return "∅"
    if w[-1] == TA_MARBUTA:
        return "-ah"
    last, prev = w[-1], (w[-2] if len(w) >= 2 else "")
    if last in ("ا", "ى"):
        return "-A"
    if last == WAW:
        return "-U"
    if last == YA:
        return "-I"
    if last == "ء" or last in S_CARRIER:
        return {"ا": "-Aʾ", WAW: "-Uʾ", YA: "-Iʾ"}.get(prev, "-ʾ")
    if prev == "ا":
        return "-A" + last
    if prev == WAW:
        return "-U" + last
    if prev == YA:
        return "-I" + last
    return "-" + last


# ---------------------------------------------------------------- 4. load Quran
QJ = json.load(open("quran-text/quran-full-tashkeel.json", encoding="utf-8"))
SURAHS = [(s["id"], s["name"], s["transliteration"], [v["text"] for v in s["verses"]])
          for s in QJ]
N_VERSES = sum(len(x[3]) for x in SURAHS)
say(f"[LOAD] {len(SURAHS)} surahs, {N_VERSES} verses")

# ---------------------------------------------------------------- 5. GATE A: orthography
say("\n" + "=" * 78)
say("GATE A — orthography (prereg §4.1). Reported BEFORE any test statistic.")
say("=" * 78)
alt = open("data/alt-text/quran-uthmani-txt.txt", encoding="utf-8").read().split("\n")[:N_VERSES]
flat = [t for _, _, _, vs in SURAHS for t in vs]
if len(alt) != len(flat):
    die("Tanzil alignment: line count mismatch")
gate_a = {}
checks = [("ٗ", FATHATAN), ("ٞ", DAMMATAN), ("ٖ", KASRATAN),
          (FATHATAN, FATHATAN), (DAMMATAN, DAMMATAN), (KASRATAN, KASRATAN)]
for mark, std in checks:
    ok = bad = 0
    for a, b in zip(flat, alt):
        aw, bw = a.split(), b.split()
        if len(aw) != len(bw):
            continue
        for x, y in zip(aw, bw):
            if mark in x:
                if std in y:
                    ok += 1
                else:
                    bad += 1
    rate = ok / max(ok + bad, 1)
    gate_a[f"U+{ord(mark):04X}"] = {"predicts": f"U+{ord(std):04X}", "match": ok,
                                    "mismatch": bad, "rate": rate}
    say(f"   U+{ord(mark):04X} [{mark}] -> U+{ord(std):04X} [{std}] : "
        f"match={ok:5d} mismatch={bad:3d} rate={rate:.4f}")
gate_a_pass = all(v["rate"] >= 0.99 for v in gate_a.values())
n_special = sum(t.count(m) for t in flat for m in TANWIN_REMAP)
n_standard = sum(t.count(m) for t in flat for m in (FATHATAN, DAMMATAN, KASRATAN))
say(f"   tanwin encoded non-standard: {n_special}  standard: {n_standard}  "
    f"non-standard share = {n_special / (n_special + n_standard):.3f}")
say(f"   GATE A: {'PASS' if gate_a_pass else 'FAIL'}")
if not gate_a_pass:
    die("orthography gate failed — instrument broken, prereg §12")

# data-integrity fact (prereg §4.1 spirit): is the wasl i'rab actually written at verse ends?
_SH, _TN, _SK = set("َُِ"), set("ًٌٍ") | set(TANWIN_REMAP), set("ْۡ")


def lastmark(w):
    for ch in reversed(w):
        if ch in _TN:
            return "tanwin"
        if ch in _SH:
            return "short-vowel"
        if ch in _SK:
            return "sukun"
        if "ء" <= ch <= "ي" or ch == SUP_ALEF:
            return "bare(long-vowel/indeclinable)"
    return "none"


fin_marks = Counter(lastmark(final_word(t)) for t in flat)
say("   verse-final word, final vowel-bearing mark (recoverability of the citation form):")
for k, n in fin_marks.most_common():
    say(f"      {k:32s} {n:5d}  {n / N_VERSES:.4f}")

# ---------------------------------------------------------------- 6. GATE B: instrument
say("\n" + "=" * 78)
say("GATE B — instrument validation against H-NEW-2240 (prereg §4.4).")
say("=" * 78)
by_id = {sid: vs for sid, _, _, vs in SURAHS}
P1 = {sid: [rime_of(t, "P1") for t in vs] for sid, _, _, vs in SURAHS}
gate_b = []


def gb(name, cond, detail):
    gate_b.append({"check": name, "pass": bool(cond), "detail": detail})
    say(f"   [{'PASS' if cond else 'FAIL'}] {name}: {detail}")


c18 = Counter(P1[18]); gb("Q18 al-Kahf 110/110 open -A", c18.get("A", 0) == 110 and len(by_id[18]) == 110, f"{dict(c18)}")
c112 = Counter(P1[112]); gb("Q112 al-Ikhlas 4/4 -ad", c112.get("aد", 0) == 4, f"{dict(c112)}")
c108 = Counter(P1[108]); gb("Q108 al-Kawthar 3/3 -ar", c108.get("aر", 0) == 3, f"{dict(c108)}")
c114 = Counter(P1[114]); gb("Q114 al-Nas 6/6 -As", c114.get("Aس", 0) == 6, f"{dict(c114)}")
c1 = Counter(P1[1]); gb("Q1 al-Fatiha all in {Im, In}", set(c1) <= {"Iم", "Iن"}, f"{dict(c1)}")
c55 = Counter(P1[55]); gb("Q55 al-Rahman modal -An", c55.most_common(1)[0][0] == "Aن", f"modal={c55.most_common(3)}")
gate_b_pass = sum(1 for g in gate_b if g["pass"])
say(f"   GATE B: {gate_b_pass}/6 {'PASS' if gate_b_pass == 6 else 'FAIL'}")
if gate_b_pass != 6:
    die("instrument gate failed — instrument broken, prereg §12")

# ---------------------------------------------------------------- 7. the analysis
# Everything below runs TWICE — once under each rime definition (R1 as pre-registered
# in §4.3, R2 the tanwin-transparent repair). Both are primary; see REPAIR-3.
CONVS = ["C", "P1", "P2", "P3"]
POEMS = {
    "Imru' al-Qays": "data/baseline-corpora/raw/muallaqa-imru-al-qais.txt",
    "Zuhayr": "data/baseline-corpora/raw/muallaqa-zuhayr.txt",
    "'Amr b. Kulthum": "data/baseline-corpora/raw/muallaqa-amr-bin-kulthum.txt",
}
poem_lines = {}
for _nm, _p in POEMS.items():
    _ls = []
    for _line in open(_p, encoding="utf-8"):
        _line = _line.strip()
        if not _line or "=" in _line or "تصنيف" in _line or _line.startswith("#"):
            continue
        _toks = [w for w in _line.split() if any("ء" <= c <= "ي" for c in w)]
        if len(_toks) < 6:
            continue
        _ls.append(_line)
    poem_lines[_nm] = _ls

PAIRS = [(sid, i) for sid, _, _, vs in SURAHS for i in range(len(vs) - 1)]
N_PAIRS = len(PAIRS)

STREAM, LENS = {}, {}
for sid, _, _, vs in SURAHS:
    _words, _lens, _ends = [], [], set()
    for t in vs:
        _t = [w for w in t.split() if any("ء" <= c <= "ي" for c in w)]
        _words += _t
        _lens.append(len(_t))
        _ends.add(len(_words) - 1)
    STREAM[sid] = (_words, _ends)
    LENS[sid] = _lens


def keff(labels):
    n = len(labels)
    h = -sum((v / n) * math.log(v / n) for v in Counter(labels).values())
    return math.exp(h)


def analyse(variant):
    global RIME_VARIANT
    RIME_VARIANT = variant
    R = {"variant": variant}
    say("\n" + "#" * 78)
    say(f"#  RIME DEFINITION {variant}   "
        f"({'as pre-registered §4.3' if variant == 'R1' else 'tanwin-transparent repair'})")
    say("#" * 78)

    LAB = {c: {sid: [rime_of(t, c) for t in vs] for sid, _, _, vs in SURAHS} for c in CONVS}
    FLATLAB = {c: [x for sid, _, _, _ in SURAHS for x in LAB[c][sid]] for c in CONVS}

    def agreement(lab):
        return sum(1 for sid, i in PAIRS if lab[sid][i] == lab[sid][i + 1]) / N_PAIRS

    # ---- RESULT 1: class collapse (prereg §9 order — BEFORE the delta)
    say("\n=== RESULT 1 — CLASS-COLLAPSE MAGNITUDE (reported before the delta) ===")
    collapse = {}
    for c in CONVS:
        fl = FLATLAB[c]
        collapse[c] = {"K": len(set(fl)), "K_eff": keff(fl),
                       "top5": [list(x) for x in Counter(fl).most_common(5)]}
        say(f"   {c:3s}  K={collapse[c]['K']:5d}  K_eff={collapse[c]['K_eff']:8.3f}   "
            f"top: {collapse[c]['top5'][:3]}")
    for p in ("P1", "P2", "P3"):
        collapse[p]["collapse_K"] = collapse["C"]["K"] / collapse[p]["K"]
        collapse[p]["collapse_Keff"] = collapse["C"]["K_eff"] / collapse[p]["K_eff"]
        say(f"   collapse C->{p}:  K {collapse['C']['K']}/{collapse[p]['K']} = "
            f"{collapse[p]['collapse_K']:.3f}x    K_eff {collapse[p]['collapse_Keff']:.3f}x")
    R["class_collapse"] = collapse

    A = {c: agreement(LAB[c]) for c in CONVS}
    DELTA = {p: A[p] - A["C"] for p in ("P1", "P2", "P3")}
    floor = {c: sum((v / N_VERSES) ** 2 for v in Counter(FLATLAB[c]).values()) for c in CONVS}
    R["agreement"], R["delta"], R["chance_floor_sum_p2"] = A, DELTA, floor

    viol = {}
    for p in ("P1", "P2"):
        m = defaultdict(set)
        for cl, pl in zip(FLATLAB["C"], FLATLAB[p]):
            m[cl].add(pl)
        sp = {k for k, v in m.items() if len(v) > 1}
        nv = sum(1 for cl in FLATLAB["C"] if cl in sp)
        viol[p] = {"split_types": len(sp), "verses_in_split_types": nv, "rate": nv / N_VERSES}
        say(f"   map-violation C->{p}: {len(sp)} citation types split; {nv} verses "
            f"({nv / N_VERSES:.4f}) sit in a split type")
    R["map_violation"] = viol

    # ---- RESULT 2: the nulls
    say("\n=== RESULT 2 — MATCHED-COLLAPSE NULLS (the decisive control) ===")
    cit_types = sorted(set(FLATLAB["C"]))
    CIDX = {t: i for i, t in enumerate(cit_types)}
    M = len(cit_types)
    cit_size = [0] * M
    for t in FLATLAB["C"]:
        cit_size[CIDX[t]] += 1
    CIT_SIZE_A = np.asarray(cit_size, dtype=np.float64)
    PAIR_A = np.array([CIDX[LAB["C"][sid][i]] for sid, i in PAIRS], dtype=np.int32)
    PAIR_B = np.array([CIDX[LAB["C"][sid][i + 1]] for sid, i in PAIRS], dtype=np.int32)
    say(f"   M = {M} distinct citation rime types over {N_VERSES} verses")

    def matched_null(target_sizes, seed, n_perm):
        """N1-a, AS PRE-REGISTERED (§6.2): randomised largest-remaining-capacity greedy
        against the observed pausal VERSE-COUNT profile."""
        rng = random.Random(seed)
        K = len(target_sizes)
        tgt = np.asarray(target_sizes, dtype=np.int64)
        order = list(range(M))
        outs, fid = [], []
        for _ in range(n_perm):
            rng.shuffle(order)
            heap = [(-target_sizes[k], k) for k in range(K)]
            heapq.heapify(heap)
            blk = [0] * M
            for t in order:
                negrem, k = heapq.heappop(heap)
                blk[t] = k
                heapq.heappush(heap, (negrem + cit_size[t], k))
            used = Counter(blk)
            empty = [k for k in range(K) if used[k] == 0]
            if empty:
                donors = [t for t in order if used[blk[t]] > 1]
                for k in empty:
                    if not donors:
                        break
                    t = donors.pop()
                    used[blk[t]] -= 1
                    blk[t] = k
                    used[k] += 1
            blka = np.asarray(blk, dtype=np.int32)
            ach = np.bincount(blka, weights=CIT_SIZE_A, minlength=K).astype(np.int64)
            fid.append(0.5 * float(np.abs(ach - tgt).sum()) / N_VERSES)
            outs.append(float(np.count_nonzero(blka[PAIR_A] == blka[PAIR_B])) / N_PAIRS)
        return outs, fid

    def cardinality_null(conv, seed, n_perm):
        """N1-b, THE REPAIR (REPAIR-1). The observed pausal partition groups the M
        citation types into K blocks; deal a shuffled type list into blocks of exactly
        the observed per-block CARDINALITY — matched by construction. The comparison
        statistic is the EXCESS OVER THE CHANCE FLOOR, E = A - sum(p_i^2), because
        sum(p_i^2) IS the collision rate a merge buys for free."""
        grp = defaultdict(Counter)
        for ct, pt in zip(FLATLAB["C"], FLATLAB[conv]):
            grp[ct][pt] += 1
        blocks = defaultdict(list)
        for ct, c in grp.items():
            blocks[c.most_common(1)[0][0]].append(ct)
        cards = [len(v) for v in blocks.values()]
        K = len(cards)
        rng = random.Random(seed)
        order = list(range(M))
        outs = []
        for _ in range(n_perm):
            rng.shuffle(order)
            blk = [0] * M
            pos = 0
            for k, c in enumerate(cards):
                for t in order[pos:pos + c]:
                    blk[t] = k
                pos += c
            blka = np.asarray(blk, dtype=np.int32)
            sizes = np.bincount(blka, weights=CIT_SIZE_A, minlength=K)
            fl = float(((sizes / N_VERSES) ** 2).sum())
            a = float(np.count_nonzero(blka[PAIR_A] == blka[PAIR_B])) / N_PAIRS
            outs.append((a, fl, a - fl))
        return outs, cards

    null_a, null_b = {}, {}
    say("   N1-a — verse-profile-matched null, AS PRE-REGISTERED (§6.2), on raw A:")
    for p in ("P1", "P2"):
        tgt = sorted(Counter(FLATLAB[p]).values(), reverse=True)
        for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
            outs, fid = matched_null(tgt, sd, N_PERM)
            ge = sum(1 for x in outs if x >= A[p])
            pv = (1 + ge) / (1 + N_PERM)
            mu = sum(outs) / len(outs)
            sdv = math.sqrt(sum((x - mu) ** 2 for x in outs) / len(outs))
            null_a[f"{p}_{tag}"] = {
                "seed": sd, "n_perm": N_PERM, "observed_A": A[p], "null_mean": mu,
                "null_sd": sdv, "null_min": min(outs), "null_max": max(outs),
                "n_ge_observed": ge, "p": pv, "K_target": len(tgt),
                "profile_fidelity_TV_mean": sum(fid) / len(fid),
                "z": (A[p] - mu) / sdv if sdv > 0 else float("nan")}
            say(f"      {p} [{tag} seed={sd}] A={A[p]:.4f} | null mean={mu:.4f} "
                f"sd={sdv:.4f} max={max(outs):.4f} | #>=obs={ge} p={pv:.5f} "
                f"z={(A[p] - mu) / sdv if sdv > 0 else float('nan'):+.2f} "
                f"| profile TV={sum(fid) / len(fid):.4f}")
    say(f"   analytic chance floor sum(p_i^2): " +
        "  ".join(f"{c}={floor[c]:.4f}" for c in CONVS))
    say(f"   observed excess over chance floor: " +
        "  ".join(f"{c}={A[c] - floor[c]:+.4f}" for c in CONVS))
    say("   N1-b — cardinality-matched null on the EXCESS E = A - sum(p_i^2) (REPAIR-1):")
    for p in ("P1", "P2"):
        for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
            outs, cards = cardinality_null(p, sd, N_PERM)
            e_obs = A[p] - floor[p]
            es = [x[2] for x in outs]
            ge = sum(1 for x in es if x >= e_obs)
            pv = (1 + ge) / (1 + N_PERM)
            mu = sum(es) / len(es)
            sdv = math.sqrt(sum((x - mu) ** 2 for x in es) / len(es))
            null_b[f"{p}_{tag}"] = {
                "seed": sd, "K_blocks": len(cards), "observed_E": e_obs,
                "null_E_mean": mu, "null_E_sd": sdv, "null_E_max": max(es),
                "null_A_mean": sum(x[0] for x in outs) / len(outs),
                "null_floor_mean": sum(x[1] for x in outs) / len(outs),
                "n_ge_observed": ge, "p": pv,
                "z": (e_obs - mu) / sdv if sdv > 0 else float("nan")}
            say(f"      {p} [{tag} seed={sd}] E={e_obs:.4f} | null E mean={mu:.4f} "
                f"sd={sdv:.4f} max={max(es):.4f} | #>=obs={ge} p={pv:.5f} "
                f"z={(e_obs - mu) / sdv if sdv > 0 else float('nan'):+.2f} "
                f"| null A={sum(x[0] for x in outs) / len(outs):.4f}")
    R["null_N1a_verse_profile"] = null_a
    R["null_N1b_cardinality_excess"] = null_b

    # ---- RESULT 3: the delta
    say("\n=== RESULT 3 — THE DELTA ===")
    for c in CONVS:
        ex = f"   Δ vs C = {DELTA[c]:+.4f}" if c != "C" else ""
        say(f"   A({c}) = {A[c]:.4f}   ({round(A[c] * N_PAIRS)}/{N_PAIRS} adjacent pairs){ex}")

    # ---- RESULT 4: pseudo-fasila re-cut
    say("\n=== RESULT 4 — pseudo-fāṣila re-cut control (within-corpus, no baseline) ===")
    cache = {}

    def rw(w, conv):
        k = (w, conv)
        r = cache.get(k)
        if r is None:
            r = rime(apply_convention(phonemes("".join(c for c in w if c not in PUNCT)), conv))
            cache[k] = r
        return r

    def recut(seed, n, conv):
        rng = random.Random(seed)
        ds, coin = [], []
        for _ in range(n):
            ac = ap = tot = hit = nb = 0
            for sid in LENS:
                words, ends = STREAM[sid]
                ls = LENS[sid][:]
                rng.shuffle(ls)
                pos, fins = 0, []
                for L in ls:
                    pos += L
                    fins.append(min(pos - 1, len(words) - 1))
                for f in fins:
                    nb += 1
                    hit += f in ends
                for i in range(len(fins) - 1):
                    a, b = words[fins[i]], words[fins[i + 1]]
                    ac += rw(a, "C") == rw(b, "C")
                    ap += rw(a, conv) == rw(b, conv)
                    tot += 1
            ds.append(ap / tot - ac / tot)
            coin.append(hit / nb)
        return ds, coin

    recut_res = {}
    for p in ("P1", "P2"):
        for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
            ds, coin = recut(sd, N_RECUT, p)
            ge = sum(1 for x in ds if x >= DELTA[p])
            pv = (1 + ge) / (1 + N_RECUT)
            mu = sum(ds) / len(ds)
            sdv = math.sqrt(sum((x - mu) ** 2 for x in ds) / len(ds))
            recut_res[f"{p}_{tag}"] = {
                "seed": sd, "n_recut": N_RECUT, "observed_delta": DELTA[p],
                "recut_mean": mu, "recut_sd": sdv, "recut_min": min(ds),
                "recut_max": max(ds), "n_ge_observed": ge, "p": pv,
                "boundary_coincidence": sum(coin) / len(coin),
                "z": (DELTA[p] - mu) / sdv if sdv > 0 else float("nan")}
            say(f"      {p} [{tag} seed={sd}] Δ_obs={DELTA[p]:+.4f} | re-cut mean="
                f"{mu:+.4f} sd={sdv:.4f} max={max(ds):+.4f} | #>=obs={ge} p={pv:.5f} "
                f"z={(DELTA[p] - mu) / sdv if sdv > 0 else float('nan'):+.2f} "
                f"| boundary coincidence={sum(coin) / len(coin):.4f}")
    R["recut_N2"] = recut_res

    # ---- RESULT 5: poetry
    say("\n=== RESULT 5 — POSITIVE CONTROL: pre-Islamic poetry ===")
    q_readable = sum(1 for t in flat if readable_of(t)) / N_VERSES
    say(f"   rime-region readability (no unwritten internal vowel in the rime): "
        f"Qur'ān = {q_readable:.4f}")
    poetry = {}
    pool = {c: [] for c in CONVS}
    pool_all = {c: [] for c in CONVS}
    for nm, ls in poem_lines.items():
        rd = [readable_of(l) for l in ls]
        lb = {c: [rime_of(l, c) for l in ls] for c in CONVS}
        ap = {c: sum(1 for i in range(len(ls) - 1) if lb[c][i] == lb[c][i + 1]) / (len(ls) - 1)
              for c in CONVS}
        keep = [i for i in range(len(ls) - 1) if rd[i] and rd[i + 1]]
        apr = {c: (sum(1 for i in keep if lb[c][i] == lb[c][i + 1]) / len(keep))
               if keep else float("nan") for c in CONVS}
        for i in range(len(ls) - 1):
            for c in CONVS:
                pool_all[c].append(lb[c][i] == lb[c][i + 1])
                if rd[i] and rd[i + 1]:
                    pool[c].append(lb[c][i] == lb[c][i + 1])
        poetry[nm] = {"n_lines": len(ls), "rime_readable": sum(rd) / len(ls),
                      "A_all": ap, "A_readable": apr, "n_pairs_readable": len(keep),
                      "delta_P1_all": ap["P1"] - ap["C"],
                      "delta_P1_readable": apr["P1"] - apr["C"],
                      "K_C": len(set(lb["C"])), "K_P1": len(set(lb["P1"]))}
        say(f"   {nm:18s} n={len(ls):4d} readable={sum(rd) / len(ls):.3f} | ALL: "
            f"A(C)={ap['C']:.4f} A(P1)={ap['P1']:.4f} Δ={ap['P1'] - ap['C']:+.4f} | "
            f"READABLE (n={len(keep):3d}): A(C)={apr['C']:.4f} A(P1)={apr['P1']:.4f} "
            f"Δ={apr['P1'] - apr['C']:+.4f}")
    A_poet = {c: sum(pool[c]) / len(pool[c]) for c in CONVS}
    A_poet_all = {c: sum(pool_all[c]) / len(pool_all[c]) for c in CONVS}
    D_poet = {p: A_poet[p] - A_poet["C"] for p in ("P1", "P2", "P3")}
    say(f"   POOLED, ALL pairs      (n={len(pool_all['C'])}): A(C)={A_poet_all['C']:.4f} "
        f"A(P1)={A_poet_all['P1']:.4f} Δ={A_poet_all['P1'] - A_poet_all['C']:+.4f}")
    say(f"   POOLED, READABLE pairs (n={len(pool['C'])}): A(C)={A_poet['C']:.4f} "
        f"A(P1)={A_poet['P1']:.4f} Δ(P1)={D_poet['P1']:+.4f} Δ(P2)={D_poet['P2']:+.4f}  <- primary")
    say(f"   Qur'ān                 (n={N_PAIRS}): A(C)={A['C']:.4f} A(P1)={A['P1']:.4f} "
        f"Δ(P1)={DELTA['P1']:+.4f}")

    def d4b(conv, seed):
        dq = np.array([(LAB[conv][sid][i] == LAB[conv][sid][i + 1])
                       - (LAB["C"][sid][i] == LAB["C"][sid][i + 1])
                       for sid, i in PAIRS], dtype=np.int8)
        dp = np.array([int(b) - int(a) for a, b in zip(pool["C"], pool[conv])], dtype=np.int8)
        obs = float(dq.mean() - dp.mean())
        allv = np.concatenate([dq, dp]).astype(np.float64)
        nq, tot = len(dq), len(dq) + len(dp)
        rng = np.random.default_rng(seed)
        ge = 0
        for _ in range(N_PERM):
            s = allv[rng.permutation(tot)]
            if s[:nq].mean() - s[nq:].mean() >= obs:
                ge += 1
        return obs, (1 + ge) / (1 + N_PERM)

    d4b_res = {}
    for conv in ("P1", "P2"):
        o, pv = d4b(conv, SEED)
        _, pv2 = d4b(conv, SEED_REP)
        d4b_res[conv] = {"obs_diff_of_deltas": o, "p": pv, "p_replication": pv2}
        say(f"   D4b {conv}: Δ_Qurʾān − Δ_poetry = {o:+.4f}  p={pv:.5f}  (rep p={pv2:.5f})")
    R["poetry"] = {"per_poem": poetry, "pooled_A_readable": A_poet,
                   "pooled_A_all": A_poet_all, "pooled_delta": D_poet,
                   "n_pairs_readable": len(pool["C"]), "n_pairs_all": len(pool_all["C"]),
                   "D4b": d4b_res}
    R["quran_rime_readability"] = q_readable

    # ---- RESULT 7: per-surah
    say("\n=== RESULT 7 — PER-SURAH ===")
    per_surah = []
    for sid, name, tr, vs in SURAHS:
        n = len(vs)
        if n < 2:
            continue
        pr = range(n - 1)
        ac = sum(1 for i in pr if LAB["C"][sid][i] == LAB["C"][sid][i + 1]) / (n - 1)
        a1 = sum(1 for i in pr if LAB["P1"][sid][i] == LAB["P1"][sid][i + 1]) / (n - 1)
        a2 = sum(1 for i in pr if LAB["P2"][sid][i] == LAB["P2"][sid][i + 1]) / (n - 1)
        per_surah.append({"surah": sid, "name": tr, "n_verses": n, "n_pairs": n - 1,
                          "A_C": ac, "A_P1": a1, "A_P2": a2, "delta_P1": a1 - ac,
                          "K_C": len(set(LAB["C"][sid])), "K_P1": len(set(LAB["P1"][sid]))})
    for lbl, rows in (("LARGEST Δ (pausal reduction rescues the rhyme)",
                       sorted(per_surah, key=lambda r: -r["delta_P1"])[:12]),
                      ("SMALLEST / NEGATIVE Δ",
                       sorted(per_surah, key=lambda r: r["delta_P1"])[:12])):
        say(f"   {lbl}:")
        for r in rows:
            say(f"      Q{r['surah']:3d} {r['name'][:18]:18s} n={r['n_verses']:4d} "
                f"A(C)={r['A_C']:.3f} A(P1)={r['A_P1']:.3f} Δ={r['delta_P1']:+.3f} "
                f"K_C={r['K_C']:3d}->K_P1={r['K_P1']:3d}")
    nneg = sum(1 for r in per_surah if r["delta_P1"] < -1e-12)
    nzero = sum(1 for r in per_surah if abs(r["delta_P1"]) <= 1e-12)
    say(f"   Δ<0: {nneg}   Δ=0: {nzero}   Δ>0: {len(per_surah) - nneg - nzero}")
    R["per_surah"] = per_surah
    R["per_surah_summary"] = {"n_neg": nneg, "n_zero": nzero,
                              "n_pos": len(per_surah) - nneg - nzero}
    return R


RES = {v: analyse(v) for v in ("R1", "R2")}

# ---------------------------------------------------------------- 8. prose (blocked)
say("\n" + "=" * 78)
say("RESULT 6 — NEGATIVE CONTROL: prose. PARTIALLY BLOCKED (prereg §6.5).")
say("=" * 78)
HARAKAT = set("ًٌٍَُِّْ")
prose_files = {"al-Bukhari": "data/baseline-corpora/raw/bukhari-noquran.txt",
               "al-Jahiz": "data/baseline-corpora/raw/jahiz-hayawan.txt"}
prose_voc = {}
for nm, p in prose_files.items():
    t = open(p, encoding="utf-8").read()
    ar = sum(1 for c in t if "ء" <= c <= "ي")
    hk = sum(1 for c in t if c in HARAKAT)
    prose_voc[nm] = {"arabic_chars": ar, "harakat": hk, "ratio": hk / max(ar, 1)}
    say(f"   {nm:12s} arabic={ar:9d} harakat={hk:6d} ratio={hk / max(ar, 1):.5f}"
        f"  -> citation form NOT RECOVERABLE; Δ NOT COMPUTABLE")
say("   Level comparison on the SKELETON instrument (h-new-2240 classify), length-matched.")
q_skel = {sid: [skel_rime(t) for t in vs] for sid, _, _, vs in SURAHS}
A_q_skel = sum(1 for sid, i in PAIRS if q_skel[sid][i] == q_skel[sid][i + 1]) / N_PAIRS
say(f"      Qur'ān A(skeleton) = {A_q_skel:.4f}")
prose_level = {}
for nm, path in prose_files.items():
    raw = open(path, encoding="utf-8").read()
    units = [u for u in re.split(r"[.؟!\n]", raw)]
    units = [u for u in units
             if len([w for w in u.split() if any("ء" <= c <= "ي" for c in w)]) >= 3]
    words = [w for u in units for w in u.split() if any("ء" <= c <= "ي" for c in w)]
    rng = random.Random(SEED)
    prof = [LENS[sid] for sid, _, _, _ in SURAHS]
    vals = []
    for _ in range(N_PROSE_CUT):
        off = rng.randrange(0, max(len(words) - 100000, 1))
        pos = off
        agree = tot = 0
        for lens in prof:
            fins = []
            for L in lens:
                pos += L
                if pos - 1 >= len(words):
                    pos = off
                fins.append(pos - 1)
            for i in range(len(fins) - 1):
                agree += skel_rime(words[fins[i]]) == skel_rime(words[fins[i + 1]])
                tot += 1
        vals.append(agree / tot)
    mu = sum(vals) / len(vals)
    sdv = math.sqrt(sum((x - mu) ** 2 for x in vals) / len(vals))
    prose_level[nm] = {"n_cuts": N_PROSE_CUT, "mean": mu, "sd": sdv, "min": min(vals),
                       "max": max(vals),
                       "quran_percentile": sum(1 for x in vals if x < A_q_skel) / len(vals)}
    say(f"      {nm:12s} A(skeleton), {N_PROSE_CUT} matched cuts: mean={mu:.4f} "
        f"sd={sdv:.4f} max={max(vals):.4f} | Qur'ān percentile "
        f"{prose_level[nm]['quran_percentile']:.3f}")
poet_skel = []
for nm, ls in poem_lines.items():
    lb = [skel_rime(l) for l in ls]
    poet_skel += [lb[i] == lb[i + 1] for i in range(len(ls) - 1)]
A_poet_skel = sum(poet_skel) / len(poet_skel)
say(f"      poetry A(skeleton) = {A_poet_skel:.4f}  (n_pairs={len(poet_skel)})")

# ---------------------------------------------------------------- 9. verdict
say("\n" + "=" * 78)
say("VERDICT — logic diffed against prereg §8, printed before declaration.")
say("=" * 78)
say("   prereg §8 grid, verbatim:")
say("     D2 passes under BOTH P1 and P2 AND D3 passes under both -> PASS")
say("     D2 passes under both but D3 fails                        -> PARTIAL")
say("     D2 FAILS under either P1 or P2                           -> NULL (arithmetic); leads")
say("     D1 reverses                                              -> REVERSED")
say(f"   D2 is now the CONJUNCTION of D2a (N1-a, as pre-registered) and D2b (N1-b repair),")
say(f"   and every test is required under BOTH rime definitions R1 and R2.")
say(f"   Bonferroni k = {BONFERRONI_K}  ->  alpha = {ALPHA:.6f}")

DEC = {}
for v in ("R1", "R2"):
    r = RES[v]
    DEC[v] = {
        "D1": r["delta"]["P1"] > 0 and r["delta"]["P2"] > 0,
        "D2a": {p: r["null_N1a_verse_profile"][f"{p}_primary"]["p"] < ALPHA for p in ("P1", "P2")},
        "D2b": {p: r["null_N1b_cardinality_excess"][f"{p}_primary"]["p"] < ALPHA for p in ("P1", "P2")},
        "D3": {p: r["recut_N2"][f"{p}_primary"]["p"] < ALPHA for p in ("P1", "P2")},
        "D4a": r["poetry"]["pooled_A_readable"]["C"] > r["agreement"]["C"],
        "D4b": {p: r["poetry"]["D4b"][p]["p"] < ALPHA for p in ("P1", "P2")},
    }
    DEC[v]["D2"] = {p: DEC[v]["D2a"][p] and DEC[v]["D2b"][p] for p in ("P1", "P2")}
    d = DEC[v]
    say(f"\n   --- {v} ---")
    say(f"   D1  Δ>0 under P1 and P2   : {d['D1']}   "
        f"(Δ_P1={r['delta']['P1']:+.4f}, Δ_P2={r['delta']['P2']:+.4f})")
    for p in ("P1", "P2"):
        say(f"   D2a A({p}) > N1-a null     : {d['D2a'][p]}   "
            f"p={r['null_N1a_verse_profile'][f'{p}_primary']['p']:.5f}")
    for p in ("P1", "P2"):
        say(f"   D2b E({p}) > N1-b null     : {d['D2b'][p]}   "
            f"p={r['null_N1b_cardinality_excess'][f'{p}_primary']['p']:.5f}")
    for p in ("P1", "P2"):
        say(f"   D3  Δ > Δ_recut ({p})      : {d['D3'][p]}   "
            f"p={r['recut_N2'][f'{p}_primary']['p']:.5f}")
    say(f"   D4a A(C)_poetry > A(C)_Qurʾān : {d['D4a']}   "
        f"({r['poetry']['pooled_A_readable']['C']:.4f} vs {r['agreement']['C']:.4f})")
    for p in ("P1", "P2"):
        say(f"   D4b Δ_Qurʾān > Δ_poetry ({p}): {d['D4b'][p]}   p={r['poetry']['D4b'][p]['p']:.5f}")


def verdict_for(v):
    d = DEC[v]
    if not d["D1"]:
        return "REVERSED"
    if not (d["D2"]["P1"] and d["D2"]["P2"]):
        return "NULL — the gain is arithmetic"
    return "PASS" if (d["D3"]["P1"] and d["D3"]["P2"]) else "PARTIAL"


VERD = {v: verdict_for(v) for v in ("R1", "R2")}
VERDICT = VERD["R1"] if VERD["R1"] == VERD["R2"] else \
    f"SPLIT — R1: {VERD['R1']} / R2: {VERD['R2']}"
say(f"\n   verdict under R1: {VERD['R1']}")
say(f"   verdict under R2: {VERD['R2']}")
say(f"\n   VERDICT: {VERDICT}")

# ---------------------------------------------------------------- 10. write run dir
if SMOKE:
    say("\n[SMOKE] no run directory written, no JSON written. Exiting.")
    raise SystemExit(0)
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-2870", STAMP)
os.makedirs(RUNDIR, exist_ok=False)
out = {
    "id": "H-NEW-2870",
    "title": "Is the fasila defined at pausal phonology rather than citation form?",
    "run_utc": STAMP, "prereg": PREREG, "prereg_sha256": PREREG_SHA256,
    "frozen_inputs": FROZEN,
    "declared_changes_to_method_parent": DECLARED_CHANGES,
    "repairs_after_prereg": REPAIRS,
    "seed": SEED, "seed_replication": SEED_REP, "n_perm": N_PERM,
    "n_recut": N_RECUT, "n_prose_cut": N_PROSE_CUT,
    "bonferroni_k": BONFERRONI_K, "alpha": ALPHA,
    "python": sys.version.split()[0], "platform": platform.platform(),
    "n_verses": N_VERSES, "n_pairs": N_PAIRS,
    "gate_a_orthography": {"checks": gate_a, "pass": gate_a_pass,
                           "tanwin_nonstandard": n_special, "tanwin_standard": n_standard,
                           "verse_final_mark_census": dict(fin_marks)},
    "gate_b_instrument": {"checks": gate_b, "n_pass": gate_b_pass},
    "by_rime_variant": RES,
    "prose": {"vocalisation": prose_voc, "delta_computable": False,
              "reason": "no harakat on disk; the citation form is not recoverable",
              "skeleton_level": prose_level, "quran_A_skeleton": A_q_skel,
              "poetry_A_skeleton": A_poet_skel},
    "decisions": DEC, "verdict_by_variant": VERD, "verdict": VERDICT,
}
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as f:
    f.write(f"H-NEW-2870 run {STAMP}\nprereg {PREREG} {PREREG_SHA256}\n"
            f"script findings/phase-b-hypotheses/scripts/h-new-2870.py "
            f"{sha256_file('findings/phase-b-hypotheses/scripts/h-new-2870.py')}\n")
    for p, s in FROZEN.items():
        f.write(f"input {p} {s}\n")
    f.write(f"output {RUNDIR}/result.json\noutput {RUNDIR}/console.log\n")
os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2870.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\n[WROTE] {RUNDIR}/result.json")
print(f"[WROTE] findings/phase-b-hypotheses/csv/h-new-2870.json")
