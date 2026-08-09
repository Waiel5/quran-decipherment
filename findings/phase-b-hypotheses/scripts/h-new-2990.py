#!/usr/bin/env python3
"""H-NEW-2990: a corpus-wide per-verse structural profile for all 6,236 verses.

This is an INSTRUMENT, not a hypothesis test. There is no verdict, no null model and no
p-value. Its value is entirely in being correct, honestly documented, reusable -- and in
not silently encoding verse length as if it were structure.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-2990-verse-profile.md
Deliverable:      findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv

Order of operations is prereg §6 and is NOT cosmetic: the profile is written to disk
immediately after it is computed, before any correlation or composite is attempted.

Run:  python3 findings/phase-b-hypotheses/scripts/h-new-2990.py
"""

import csv
import hashlib
import json
import math
import os
import platform
import re
import shutil
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.stats import rankdata

REPO = Path(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")))
os.chdir(REPO)

# --------------------------------------------------------------------------------------
# Prereg §1 / §7 -- embedded literals, verified at runtime. A mismatch aborts BEFORE any
# run directory is created.
# --------------------------------------------------------------------------------------
PREREG = "findings/phase-b-hypotheses/prereg-h-new-2990-verse-profile.md"
EXPECTED_PREREG_SHA = "7a155da65a96eed918d2debf8f324df5b3e225d0ed8b4c8adde1ef70afe510ee"

QAC = "data/morphology/quranic-corpus-morphology-0.4.txt"
TEXT = "quran-text/quran-full-tashkeel.json"
HAPAX = "findings/phase-b-hypotheses/hapaxes-full-list.csv"

FROZEN = {
    QAC: "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    TEXT: "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    HAPAX: "50d77bd3f82792c739e57c47fbc39d3c67054c77c5a8026bfd08a9e4a27dcb2d",
}

SEED_PRIMARY = 20260509          # prereg §7 -- nothing here is stochastic; declared for the record
SEED_REPLICATION = 20260519

N_VERSES = 6236
RIME_CONVENTION = "P2"           # prereg §3.F, locked
LENGTH_DOMINATED_THRESHOLD = 0.70   # prereg §4 R2, locked before any rho was computed
COMPOSITE_GATE_THRESHOLD = 0.30     # prereg §5 G1
COMPOSITE_MIN_MEMBERS = 3           # prereg §5 G2
RARE_ROOT_CUTOFF = 5                # prereg §3.D

LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
ROOT_RE = re.compile(r"ROOT:([^|]*)")
LEM_RE = re.compile(r"LEM:([^|]*)")
POS_RE = re.compile(r"POS:(\w+)")
FORM_RE = re.compile(r"\((I{1,3}|IV|V|VI|VII|VIII|IX|X|XI|XII)\)")

# prereg §3.G -- an EXHAUSTIVE four-way partition of POS-bearing segments. The three
# membership sets are named; every other QAC tag falls to the PARTICLE catch-all, so a
# tag not anticipated here lands somewhere visible rather than disappearing.
POS_NOMINAL = {"N", "PN", "ADJ"}
POS_VERBAL = {"V", "IMPN"}
POS_PRONOMINAL = {"PRON", "DEM", "REL"}

# prereg §3.B -- the written skeleton. Superscript alef U+0670 is a diacritic and is NOT
# a letter of the rasm; it is absent from this set and is therefore removed.
ARABIC_LETTERS = set("ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيٱ")


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def die(msg):
    print("ABORT: " + msg, file=sys.stderr)
    sys.exit(2)


def say(*a):
    print(" ".join(str(x) for x in a), flush=True)


def git_output(*args):
    try:
        return subprocess.run(["git", *args], cwd=REPO, capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


# ======================================================================================
# GATE -- before anything else exists
# ======================================================================================
_prereg_sha = sha256_file(PREREG)
if _prereg_sha != EXPECTED_PREREG_SHA:
    die(f"pre-registration SHA mismatch\n  expected {EXPECTED_PREREG_SHA}\n  actual   {_prereg_sha}")
say(f"[SHA-OK] pre-registration locked: {_prereg_sha}")
for _p, _want in FROZEN.items():
    _got = sha256_file(_p)
    if _got != _want:
        die(f"frozen input mismatch {_p}\n  expected {_want}\n  actual   {_got}")
say(f"[SHA-OK] {len(FROZEN)} frozen inputs verified")


# ======================================================================================
# 1. The fasila instrument
#
# PORTED VERBATIM from findings/phase-b-hypotheses/scripts/h-new-2870.py sections 1-2
# (`normalize`, `phonemes`, `apply_convention`, `rime_parts`, `rime2_parts`,
# `final_word`, `rime_of`, `readable_of`), which itself declares its port from
# h-new-2690.py section 2.1. NO parameter is changed. That script's DECLARED_CHANGES and
# REPAIRS lists are its own and are not restated here; they are in force by the port.
#
# Convention locked at P2 (prereg §3.F). Under P1/P2 the convention has already removed
# the tanwin, so R1 and R2 coincide and REPAIR-3's rime-definition fork does not exist at
# this convention. RIME_VARIANT is left at its ported default and asserted below.
# ======================================================================================
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

TANWIN_REMAP = {"ٗ": FATHATAN, "ٞ": DAMMATAN, "ٖ": KASRATAN}

DROP = set("ـۖۗۘۙۚۛۜ۞۟۠"
           "ۣۧۨ۩۪ۭ۫۬"
           "ٕٜٟٓٔ٘ٙٚٛٝ"
           "۝ࣰࣱࣲ")
SUKUN_ALT, SMALL_WAW, SMALL_YA = "ۡ", "ۥ", "ۦ"
FINAL_VOWELS = set(SHORT) | set(TANWIN)


def normalize(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(TANWIN_REMAP.get(c, c) for c in t)          # h-new-2870 prereg §4.1
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


def apply_convention(ph, conv):
    """h-new-2870 prereg §5. ph is the CITATION phoneme list; returns the list under `conv`."""
    ph = list(ph)
    if conv == "C":
        return ph
    if len(ph) >= 2 and ph[-1][2].startswith("tanwin") and ph[-2][2].startswith("tanwin"):
        kind = ph[-1][2]
        ph = ph[:-2]
        if kind == "tanwin-a" and conv in ("P1", "P2"):
            ph.append(("VV", "a", ""))          # waqf bi-l-alif
    elif ph and ph[-1][0] == "V":
        ph = ph[:-1]                            # iskan: final short vowel drops
    if conv == "P2" and ph and ph[-1][0] == "C" and ph[-1][2] == "ta":
        ph = ph[:-1] + [("C", "ه", "")]         # ta marbuta -> ha
    return ph


VOWEL_LONG = {"a": "A", "u": "U", "i": "I"}


def rime_parts(ph):
    """h-new-2870 prereg §4.3 -- the classical ridf / rawi / majra, as an algorithm.
    Returns (rime_string, readable)."""
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
    """R2 -- the tanwin-transparent rime (h-new-2870 REPAIR-3). Identical to R1 under
    P1/P2/P3, where the convention has already removed the tanwin."""
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


# ======================================================================================
# 2. Statistics -- Spearman on average ranks, and the rank-partial
# ======================================================================================
def spearman(x, y):
    """Spearman rho = Pearson on tie-averaged ranks. Returns None if either side is
    constant (rho undefined, not zero)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = np.isfinite(x) & np.isfinite(y)
    if ok.sum() < 3:
        return None, int(ok.sum())
    rx, ry = rankdata(x[ok]), rankdata(y[ok])
    if rx.std() == 0 or ry.std() == 0:
        return None, int(ok.sum())
    return float(np.corrcoef(rx, ry)[0, 1]), int(ok.sum())


def partial_spearman(x, y, z):
    """rho(x,y | z) computed on tie-averaged ranks -- the standard rank-partial."""
    x, y, z = (np.asarray(v, dtype=float) for v in (x, y, z))
    ok = np.isfinite(x) & np.isfinite(y) & np.isfinite(z)
    if ok.sum() < 4:
        return None
    rx, ry, rz = rankdata(x[ok]), rankdata(y[ok]), rankdata(z[ok])
    if rx.std() == 0 or ry.std() == 0 or rz.std() == 0:
        return None
    rxy = np.corrcoef(rx, ry)[0, 1]
    rxz = np.corrcoef(rx, rz)[0, 1]
    ryz = np.corrcoef(ry, rz)[0, 1]
    denom = math.sqrt(max(0.0, (1 - rxz ** 2) * (1 - ryz ** 2)))
    if denom == 0:
        return None
    return float((rxy - rxz * ryz) / denom)


def eta_squared(values, labels):
    """Share of variance in `values` explained by categorical `labels`. Used for the one
    categorical column, where a Spearman rho does not exist (prereg §4)."""
    v = np.asarray(values, dtype=float)
    groups = defaultdict(list)
    for val, lab in zip(v, labels):
        groups[lab].append(val)
    grand = v.mean()
    ss_total = float(((v - grand) ** 2).sum())
    ss_between = float(sum(len(g) * (np.mean(g) - grand) ** 2 for g in groups.values()))
    return ss_between / ss_total if ss_total > 0 else None


# ======================================================================================
# 3. Load
# ======================================================================================
def load_qac():
    rows = []
    with open(QAC, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOCATION_RE.match(parts[0])
            if not m:
                continue
            s, v, w, g = (int(x) for x in m.groups())
            rows.append((s, v, w, g, parts[1], parts[2], parts[3]))
    return rows


def load_text():
    data = json.load(open(TEXT, encoding="utf-8"))
    out = {}
    for surah in data:
        for verse in surah["verses"]:
            out[(surah["id"], verse["id"])] = verse["text"]
    return out


def load_hapax_sets():
    """Prereg §1.1 -- the PUBLISHED census is the registered source. A fresh QAC
    derivation is computed alongside it and any disagreement is reported, not repaired."""
    rows = list(csv.DictReader(open(HAPAX, encoding="utf-8")))
    published_roots = {r["token"] for r in rows if r["type"] == "root-hapax"}
    published_lemmas = {r["token"] for r in rows if r["type"] == "lemma-hapax"}
    locations = defaultdict(Counter)
    for r in rows:
        if r["type"] in ("root-hapax", "lemma-hapax"):
            locations[(int(r["surah"]), int(r["verse"]))][r["type"]] += 1
    return published_roots, published_lemmas, locations, len(rows)


# ======================================================================================
# 4. Build the profile -- prereg §3
# ======================================================================================
def build_profile():
    qac = load_qac()
    text = load_text()
    pub_roots, pub_lemmas, pub_locations, n_hapax_rows = load_hapax_sets()

    root_freq, lemma_freq = Counter(), Counter()
    for _, _, _, _, _, _, feat in qac:
        m = ROOT_RE.search(feat)
        if m:
            root_freq[m.group(1)] += 1
        m = LEM_RE.search(feat)
        if m:
            lemma_freq[m.group(1)] += 1
    total_root_tokens = sum(root_freq.values())

    derived_roots = {k for k, n in root_freq.items() if n == 1}
    derived_lemmas = {k for k, n in lemma_freq.items() if n == 1}
    hapax_agreement = {
        "published_root_hapaxes": len(pub_roots),
        "qac_derived_root_hapaxes": len(derived_roots),
        "root_symmetric_difference": sorted(pub_roots ^ derived_roots),
        "published_lemma_hapaxes": len(pub_lemmas),
        "qac_derived_lemma_hapaxes": len(derived_lemmas),
        "lemma_symmetric_difference": sorted(pub_lemmas ^ derived_lemmas),
        "hapax_csv_rows": n_hapax_rows,
    }

    by_verse = defaultdict(list)
    for s, v, w, g, form, tag, feat in qac:
        by_verse[(s, v)].append((w, g, form, tag, feat))

    keys = sorted(by_verse)
    if len(keys) != N_VERSES:
        die(f"QAC yields {len(keys)} verses, expected {N_VERSES}")
    if set(keys) != set(text):
        die("QAC verse keys and text verse keys disagree")

    # --- rime pass 1: the class census (a corpus-wide constant, prereg §0.1 / §3.F)
    rimes = {k: rime_of(text[k], RIME_CONVENTION) for k in keys}
    rime_counts = Counter(rimes.values())

    # cross-check the R1 == R2 claim locked in prereg §3.F, on the data
    global RIME_VARIANT
    RIME_VARIANT = "R2"
    rimes_r2 = {k: rime_of(text[k], RIME_CONVENTION) for k in keys}
    RIME_VARIANT = "R1"
    rime_variants_identical = (rimes == rimes_r2)

    rows = []
    for idx, key in enumerate(keys, start=1):
        s, v = key
        segs = by_verse[key]

        n_words = max(w for w, *_ in segs)
        n_segments = len(segs)
        raw = unicodedata.normalize("NFC", text[key])
        n_letters_rasm = sum(1 for c in raw if c in ARABIC_LETTERS)

        roots, lemmas, poss = [], [], []
        n_derived_stems = 0
        for _, _, _, _, feat in segs:
            m = ROOT_RE.search(feat)
            if m:
                roots.append(m.group(1))
                if FORM_RE.search(feat):
                    n_derived_stems += 1
            m = LEM_RE.search(feat)
            if m:
                lemmas.append(m.group(1))
            m = POS_RE.search(feat)
            if m:
                poss.append(m.group(1))

        n_root_tokens, n_lemma_tokens, n_pos_segments = len(roots), len(lemmas), len(poss)

        # --- C, hapax
        n_hap_root = sum(1 for r in roots if r in pub_roots)
        n_hap_lemma = sum(1 for lm in lemmas if lm in pub_lemmas)

        # --- D, root rarity
        if n_root_tokens:
            freqs = [root_freq[r] for r in roots]
            logs = sorted(math.log10(f) for f in freqs)
            mid = len(logs) // 2
            median_log = logs[mid] if len(logs) % 2 else 0.5 * (logs[mid - 1] + logs[mid])
            surprisals = [-math.log2(f / total_root_tokens) for f in freqs]
            mean_log = sum(logs) / len(logs)
            mean_surp = sum(surprisals) / len(surprisals)
            sum_surp = sum(surprisals)
            min_freq = min(freqs)
            frac_le5 = sum(1 for f in freqs if f <= RARE_ROOT_CUTOFF) / n_root_tokens
        else:
            median_log = mean_log = mean_surp = sum_surp = min_freq = frac_le5 = None

        # --- E, repetition
        root_counts = Counter(roots)
        n_root_types = len(root_counts)
        ttr = n_root_types / n_root_tokens if n_root_tokens else None
        if n_root_tokens >= 2:
            simpson = sum(n * (n - 1) for n in root_counts.values()) / (
                n_root_tokens * (n_root_tokens - 1))
        else:
            simpson = None

        # --- G, morphology
        if n_pos_segments:
            c = Counter(poss)
            nom = sum(n for t, n in c.items() if t in POS_NOMINAL)
            vrb = sum(n for t, n in c.items() if t in POS_VERBAL)
            prn = sum(n for t, n in c.items() if t in POS_PRONOMINAL)
            part = n_pos_segments - nom - vrb - prn
            share_nom, share_vrb = nom / n_pos_segments, vrb / n_pos_segments
            share_prn, share_part = prn / n_pos_segments, part / n_pos_segments
        else:
            share_nom = share_vrb = share_prn = share_part = None

        rows.append({
            "surah": s,
            "verse": v,
            "mushaf_index": idx,
            "n_words": n_words,
            "n_segments": n_segments,
            "n_letters_rasm": n_letters_rasm,
            "n_root_tokens": n_root_tokens,
            "n_lemma_tokens": n_lemma_tokens,
            "n_pos_segments": n_pos_segments,
            "n_hapax_root_tokens": n_hap_root,
            "frac_hapax_root_tokens": n_hap_root / n_root_tokens if n_root_tokens else None,
            "n_hapax_lemma_tokens": n_hap_lemma,
            "frac_hapax_lemma_tokens": n_hap_lemma / n_lemma_tokens if n_lemma_tokens else None,
            "mean_log10_root_freq": mean_log,
            "median_log10_root_freq": median_log,
            "min_root_freq": min_freq,
            "mean_root_surprisal_bits": mean_surp,
            "sum_root_surprisal_bits": sum_surp,
            "frac_root_tokens_freq_le5": frac_le5,
            "n_root_types": n_root_types,
            "ttr_root": ttr,
            "root_simpson_repeat": simpson,
            "rime_pausal": rimes[key],
            "rime_class_size": rime_counts[rimes[key]],
            "fasila_readable": int(readable_of(text[key])),
            "share_nominal": share_nom,
            "share_verbal": share_vrb,
            "share_pronominal": share_prn,
            "share_particle": share_part,
            "segments_per_word": n_segments / n_words if n_words else None,
            "frac_derived_stems": n_derived_stems / n_root_tokens if n_root_tokens else None,
        })

    # prereg §1.1 -- the independent route to the same hapax counts, via the published
    # census's OWN location fields rather than via QAC membership lookup.
    loc_mismatch = []
    for r in rows:
        want = pub_locations.get((r["surah"], r["verse"]), Counter())
        if want["root-hapax"] != r["n_hapax_root_tokens"] or \
           want["lemma-hapax"] != r["n_hapax_lemma_tokens"]:
            loc_mismatch.append({
                "verse": f"{r['surah']}:{r['verse']}",
                "by_membership": [r["n_hapax_root_tokens"], r["n_hapax_lemma_tokens"]],
                "by_published_location": [want["root-hapax"], want["lemma-hapax"]],
            })

    census = {
        "n_verses": len(rows),
        "n_segments": len(qac),
        "n_root_bearing_tokens": total_root_tokens,
        "n_distinct_roots": len(root_freq),
        "n_lemma_bearing_tokens": sum(lemma_freq.values()),
        "n_distinct_lemmas": len(lemma_freq),
        "n_pos_bearing_segments": sum(r["n_pos_segments"] for r in rows),
        "rime_convention": RIME_CONVENTION,
        "n_rime_classes": len(rime_counts),
        "rime_R1_equals_R2_at_this_convention": rime_variants_identical,
        "n_fasila_readable": sum(r["fasila_readable"] for r in rows),
        "hapax_agreement": hapax_agreement,
        "hapax_location_route_mismatches": loc_mismatch,
    }
    return rows, census


# ======================================================================================
# 5. Column declarations -- prereg §3, fixed before any rho existed
# ======================================================================================
DECLARATIONS = [
    # (column, family, kind, denominator, note)
    ("surah", "A identity", "IDENTITY", "", ""),
    ("verse", "A identity", "IDENTITY", "", ""),
    ("mushaf_index", "A identity", "IDENTITY", "", ""),
    ("n_words", "B length", "COUNT", "", "PRIMARY LENGTH VARIABLE"),
    ("n_segments", "B length", "COUNT", "", ""),
    ("n_letters_rasm", "B length", "COUNT", "", "secondary length variable; U+0670 removed"),
    ("n_root_tokens", "B length", "COUNT", "", "denominator of the root family"),
    ("n_lemma_tokens", "B length", "COUNT", "", "denominator of the lemma family"),
    ("n_pos_segments", "B length", "COUNT", "", "denominator of the morphology family"),
    ("n_hapax_root_tokens", "C hapax", "COUNT", "", ""),
    ("frac_hapax_root_tokens", "C hapax", "RATE", "n_root_tokens", ""),
    ("n_hapax_lemma_tokens", "C hapax", "COUNT", "", ""),
    ("frac_hapax_lemma_tokens", "C hapax", "RATE", "n_lemma_tokens", ""),
    ("mean_log10_root_freq", "D rarity", "INVARIANT", "", ""),
    ("median_log10_root_freq", "D rarity", "INVARIANT", "", ""),
    ("min_root_freq", "D rarity", "COUNT-LIKE", "",
     "declared length-sensitive a priori by extreme-value logic"),
    ("mean_root_surprisal_bits", "D rarity", "INVARIANT", "", ""),
    ("sum_root_surprisal_bits", "D rarity", "COUNT", "",
     "length-dominated BY CONSTRUCTION; the instrument's own calibration case"),
    ("frac_root_tokens_freq_le5", "D rarity", "RATE", "n_root_tokens", ""),
    ("n_root_types", "E repetition", "COUNT", "", ""),
    ("ttr_root", "E repetition", "RATE", "n_root_tokens",
     "declared mechanically length-dependent a priori"),
    ("root_simpson_repeat", "E repetition", "INVARIANT", "",
     "length-honest counterpart of ttr_root; empty when n_root_tokens < 2"),
    ("rime_pausal", "F fasila", "INVARIANT-CATEGORICAL", "", "P2 pausal rime string"),
    ("rime_class_size", "F fasila", "INVARIANT", "", "corpus constant keyed by the verse's own fasila"),
    ("fasila_readable", "F fasila", "INVARIANT-BOOLEAN", "", ""),
    ("share_nominal", "G morphology", "RATE", "n_pos_segments", ""),
    ("share_verbal", "G morphology", "RATE", "n_pos_segments", ""),
    ("share_pronominal", "G morphology", "RATE", "n_pos_segments", ""),
    ("share_particle", "G morphology", "RATE", "n_pos_segments", ""),
    ("segments_per_word", "G morphology", "RATE", "n_words", ""),
    ("frac_derived_stems", "G morphology", "RATE", "n_root_tokens", ""),
]

IDENTITY_COLS = {"surah", "verse", "mushaf_index"}
LENGTH_COLS = {"n_words", "n_segments", "n_letters_rasm",
               "n_root_tokens", "n_lemma_tokens", "n_pos_segments"}

# prereg §5 -- members and signs, locked
COMPOSITE_MEMBERS = [
    ("frac_hapax_root_tokens", +1),
    ("mean_root_surprisal_bits", +1),
    ("frac_root_tokens_freq_le5", +1),
    ("root_simpson_repeat", -1),
    ("log10_rime_class_size", -1),
]

BASE_COLUMNS = [d[0] for d in DECLARATIONS]


def write_csv(path, rows, columns):
    """Mode 'x' -- write-once. Never overwrites."""
    with open(path, "x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            writer.writerow({c: ("" if r.get(c) is None else r.get(c)) for c in columns})


def publish(src, dst):
    """The published copy lives OUTSIDE the run directory and may be replaced."""
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copyfile(src, dst)


def main():
    say("[BUILD] computing 31 columns over 6,236 verses ...")
    rows, census = build_profile()
    say(f"[BUILD] done: {census['n_verses']} verses, {census['n_rime_classes']} rime classes")

    # ---- prereg §6 step 2: the immutable run directory
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = REPO / "findings/phase-b-hypotheses/runs/h-new-2990" / run_id
    os.makedirs(run_dir, exist_ok=False)
    say(f"[RUN] {run_dir.relative_to(REPO)}")

    # ---- prereg §6 step 3-4: PERSIST THE INSTRUMENT BEFORE ANY VALIDATION
    profile_path = run_dir / "verse-profile.csv"
    write_csv(profile_path, rows, BASE_COLUMNS)
    published = REPO / "findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv"
    publish(profile_path, published)
    say(f"[PERSIST] instrument on disk: {published.relative_to(REPO)} "
        f"({len(rows)} rows x {len(BASE_COLUMNS)} columns)")

    # ---- prereg §6 step 5: only now, the diagnostics
    col = {c: [r.get(c) for r in rows] for c in BASE_COLUMNS}
    n_words = col["n_words"]
    n_letters = col["n_letters_rasm"]
    mushaf = col["mushaf_index"]

    def numeric(values):
        return [float("nan") if v is None else float(v) for v in values]

    diagnostics = {}
    for name, family, kind, denom, note in DECLARATIONS:
        if name in IDENTITY_COLS:
            continue
        entry = {"family": family, "kind": kind, "denominator": denom, "note": note}
        if name == "rime_pausal":
            # A categorical column has no Spearman rho; prereg §4 substitutes eta^2 --
            # the share of length variance explained by rime-class membership.
            eta_w = eta_squared(numeric(n_words), col[name])
            eta_c = eta_squared(numeric(n_letters), col[name])
            entry["rho_vs_n_words"] = None
            entry["eta2_n_words_by_class"] = eta_w
            entry["eta2_n_letters_by_class"] = eta_c
            entry["n_defined"] = len(rows)
            entry["length_dominated"] = None
            entry["note"] = (f"{note}; categorical -- no rho. "
                             f"eta^2(n_words | class) = {eta_w:.4f}, "
                             f"eta^2(n_letters | class) = {eta_c:.4f}")
        else:
            vals = numeric(col[name])
            rho_w, n_def = spearman(vals, numeric(n_words))
            rho_c, _ = spearman(vals, numeric(n_letters))
            rho_m, _ = spearman(vals, numeric(mushaf))
            entry["rho_vs_n_words"] = rho_w
            entry["rho_vs_n_letters_rasm"] = rho_c
            entry["rho_vs_mushaf_index"] = rho_m
            entry["partial_rho_vs_mushaf_given_n_words"] = partial_spearman(
                vals, numeric(mushaf), numeric(n_words))
            entry["n_defined"] = n_def
            # prereg §3.B exempts the six B columns from the flag: they ARE length.
            if name in LENGTH_COLS:
                entry["length_dominated"] = "IS_LENGTH"
            elif rho_w is None:
                entry["length_dominated"] = None
            else:
                entry["length_dominated"] = bool(abs(rho_w) > LENGTH_DOMINATED_THRESHOLD)
        diagnostics[name] = entry

    # ---- prereg §5: the composite, under its locked gates
    log_rime = [math.log10(v) for v in col["rime_class_size"]]
    member_series = {}
    for name, sign in COMPOSITE_MEMBERS:
        member_series[name] = log_rime if name == "log10_rime_class_size" else numeric(col[name])

    composite_report = {"threshold": COMPOSITE_GATE_THRESHOLD, "min_members": COMPOSITE_MIN_MEMBERS,
                        "members": [], "dropped": [], "kept": []}
    kept = []
    for name, sign in COMPOSITE_MEMBERS:
        rho_w, _ = spearman(member_series[name], numeric(n_words))
        rec = {"member": name, "sign": sign, "rho_vs_n_words": rho_w}
        composite_report["members"].append(rec)
        if rho_w is not None and abs(rho_w) > COMPOSITE_GATE_THRESHOLD:
            composite_report["dropped"].append(rec)
        else:
            composite_report["kept"].append(rec)
            kept.append((name, sign))

    final_columns = list(BASE_COLUMNS)
    if len(kept) >= COMPOSITE_MIN_MEMBERS:
        z = {}
        for name, sign in kept:
            arr = np.asarray(member_series[name], dtype=float)
            ok = np.isfinite(arr)
            mu, sd = arr[ok].mean(), arr[ok].std(ddof=0)
            zz = np.full(len(arr), np.nan)
            zz[ok] = sign * (arr[ok] - mu) / sd
            z[name] = zz
        stack = np.vstack([z[n] for n, _ in kept])
        defined = np.isfinite(stack)
        n_defined = defined.sum(axis=0)
        sums = np.where(defined, stack, 0.0).sum(axis=0)
        comp = np.where(n_defined >= COMPOSITE_MIN_MEMBERS,
                        sums / np.maximum(n_defined, 1), np.nan)

        # residual on rank(n_words), OLS -- prereg §5
        rw = rankdata(numeric(n_words))
        ok = np.isfinite(comp)
        slope, intercept = np.polyfit(rw[ok], comp[ok], 1)
        resid = np.full(len(comp), np.nan)
        resid[ok] = comp[ok] - (slope * rw[ok] + intercept)

        for i, r in enumerate(rows):
            r["struct_z_composite"] = None if not np.isfinite(comp[i]) else round(float(comp[i]), 6)
            r["struct_z_composite_resid"] = None if not np.isfinite(resid[i]) else round(float(resid[i]), 6)
        final_columns += ["struct_z_composite", "struct_z_composite_resid"]

        rho_c, nc = spearman(comp, numeric(n_words))
        rho_r, _ = spearman(resid, numeric(n_words))
        composite_report["emitted"] = True
        composite_report["n_members_used"] = len(kept)
        composite_report["n_defined"] = int(np.isfinite(comp).sum())
        composite_report["rho_composite_vs_n_words"] = rho_c
        composite_report["rho_resid_vs_n_words"] = rho_r
        composite_report["ols_on_rank_n_words"] = {"slope": float(slope), "intercept": float(intercept)}
        for key, series in (("struct_z_composite", comp), ("struct_z_composite_resid", resid)):
            rho_w, n_def = spearman(series, numeric(n_words))
            rho_l, _ = spearman(series, numeric(n_letters))
            rho_m, _ = spearman(series, numeric(mushaf))
            diagnostics[key] = {
                "family": "H composite (SECONDARY)", "kind": "DERIVED", "denominator": "",
                "note": "prereg §5; secondary to the columns, never a replacement for them",
                "rho_vs_n_words": rho_w, "rho_vs_n_letters_rasm": rho_l,
                "rho_vs_mushaf_index": rho_m,
                "partial_rho_vs_mushaf_given_n_words": partial_spearman(
                    series, numeric(mushaf), numeric(n_words)),
                "n_defined": n_def,
                "length_dominated": bool(abs(rho_w) > LENGTH_DOMINATED_THRESHOLD) if rho_w is not None else None,
            }
        say(f"[COMPOSITE] emitted from {len(kept)} of {len(COMPOSITE_MEMBERS)} members; "
            f"rho vs n_words = {'n/a' if rho_c is None else f'{rho_c:+.4f}'}")
    else:
        composite_report["emitted"] = False
        composite_report["reason"] = (
            f"gate G2: only {len(kept)} member(s) survived gate G1 "
            f"(|rho| <= {COMPOSITE_GATE_THRESHOLD}); minimum is {COMPOSITE_MIN_MEMBERS}")
        say(f"[COMPOSITE] NOT emitted -- {composite_report['reason']}")

    # ---- prereg §6 step 6: a DISTINCT filename. Step 3's file is never touched again.
    final_path = run_dir / "verse-profile-final.csv"
    write_csv(final_path, rows, final_columns)
    publish(final_path, published)
    say(f"[PERSIST] final instrument: {published.relative_to(REPO)} "
        f"({len(rows)} rows x {len(final_columns)} columns)")

    # ---- prereg §6 step 7
    decl_rows = []
    for name in final_columns:
        d = diagnostics.get(name)
        if d is None:
            base = next((x for x in DECLARATIONS if x[0] == name), None)
            decl_rows.append({"column": name, "family": base[1], "kind": base[2],
                              "denominator": base[3], "note": base[4],
                              "rho_vs_n_words": "", "rho_vs_n_letters_rasm": "",
                              "rho_vs_mushaf_index": "",
                              "partial_rho_vs_mushaf_given_n_words": "",
                              "n_defined": len(rows), "length_dominated": "IDENTITY"})
            continue
        decl_rows.append({
            "column": name, "family": d["family"], "kind": d["kind"],
            "denominator": d.get("denominator", ""), "note": d.get("note", ""),
            "rho_vs_n_words": "" if d.get("rho_vs_n_words") is None else round(d["rho_vs_n_words"], 4),
            "rho_vs_n_letters_rasm": "" if d.get("rho_vs_n_letters_rasm") is None
            else round(d["rho_vs_n_letters_rasm"], 4),
            "rho_vs_mushaf_index": "" if d.get("rho_vs_mushaf_index") is None
            else round(d["rho_vs_mushaf_index"], 4),
            "partial_rho_vs_mushaf_given_n_words": ""
            if d.get("partial_rho_vs_mushaf_given_n_words") is None
            else round(d["partial_rho_vs_mushaf_given_n_words"], 4),
            "n_defined": d["n_defined"],
            "length_dominated": ("" if d.get("length_dominated") is None
                                 else d["length_dominated"]),
        })
    decl_cols = ["column", "family", "kind", "denominator", "rho_vs_n_words",
                 "rho_vs_n_letters_rasm", "rho_vs_mushaf_index",
                 "partial_rho_vs_mushaf_given_n_words", "n_defined",
                 "length_dominated", "note"]
    decl_path = run_dir / "column-declarations.csv"
    write_csv(decl_path, decl_rows, decl_cols)
    publish(decl_path, REPO / "findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv")

    payload = {
        "hypothesis": "H-NEW-2990",
        "kind": "INSTRUMENT -- no verdict, no null model, no p-value",
        "census": census,
        "column_count": len(final_columns),
        "columns": final_columns,
        "diagnostics": diagnostics,
        "composite": composite_report,
        "gates": {
            "length_dominated_threshold": LENGTH_DOMINATED_THRESHOLD,
            "composite_gate_threshold": COMPOSITE_GATE_THRESHOLD,
            "composite_min_members": COMPOSITE_MIN_MEMBERS,
        },
        "length_dominated_columns": sorted(
            k for k, d in diagnostics.items() if d.get("length_dominated") is True),
    }
    with open(run_dir / "result.json", "x", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)

    manifest = {
        "hypothesis": "H-NEW-2990",
        "run_id": run_id,
        "run_directory": str(run_dir.relative_to(REPO)),
        "script": str(Path(__file__).resolve().relative_to(REPO)),
        "prereg": PREREG,
        "prereg_sha256": _prereg_sha,
        "inputs": [{"path": p, "sha256": s} for p, s in sorted(FROZEN.items())],
        "outputs": [
            {"path": str(profile_path.relative_to(REPO)), "role": "instrument, pre-composite, write-once"},
            {"path": str(final_path.relative_to(REPO)), "role": "instrument, final"},
            {"path": str(decl_path.relative_to(REPO)), "role": "column declarations"},
            {"path": "findings/phase-b-hypotheses/csv/h-new-2990-verse-profile.csv",
             "role": "published deliverable (outside the run directory; replaceable)"},
            {"path": "findings/phase-b-hypotheses/csv/h-new-2990-column-declarations.csv",
             "role": "published declarations (outside the run directory; replaceable)"},
        ],
        "git_commit": git_output("rev-parse", "HEAD"),
        "git_status_porcelain": git_output("status", "--porcelain"),
        "seeds": {"primary": SEED_PRIMARY, "replication_declared_unused": SEED_REPLICATION},
        "deterministic": True,
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
        "utc": datetime.now(timezone.utc).isoformat(),
    }
    with open(run_dir / "manifest.json", "x", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2, sort_keys=True)

    say("\n[LENGTH DECLARATION] rho vs n_words, all non-identity columns:")
    for name in final_columns:
        if name in IDENTITY_COLS:
            continue
        d = diagnostics[name]
        rho = d.get("rho_vs_n_words")
        flag = ""
        if d.get("length_dominated") is True:
            flag = "  <-- LENGTH-DOMINATED"
        elif d.get("length_dominated") == "IS_LENGTH":
            flag = "  (is length)"
        say(f"  {name:34s} {'   n/a' if rho is None else f'{rho:+.4f}'}{flag}")
    say(f"\n[RUN DIR] {run_dir.relative_to(REPO)}")


if __name__ == "__main__":
    main()
