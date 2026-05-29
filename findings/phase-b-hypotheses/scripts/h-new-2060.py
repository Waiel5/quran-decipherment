#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2060 — First-word / last-word cross-surah taxonomy + strict word-level inclusio scan.

Builds the complete opener + closer taxonomy of all 114 surahs from QAC v0.4 morphology,
and runs a pre-registered strict single-word inclusio test (first-content-word root ==
last-word root) against a 10,000-permutation label-shuffle null.

Pre-registration: prereg-h-new-2060-first-last-word-scan.md (SHA256 verified at runtime).
Rules-tuple: no-tashkeel display forms; QAC v0.4 ROOT for inclusio; basmala-in-Q1-only;
Hafs-Kufan; seed 20260509 (replication 20260510).
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict

BASE = "/Users/grey/Downloads/quran"
PREREG = os.path.join(BASE, "findings/phase-b-hypotheses/prereg-h-new-2060-first-last-word-scan.md")
EXPECTED_SHA = "da16481730cd9f50697926877740bb3eb20d47ed7977f325f4b1b2b64ce87f1b"
MORPH = os.path.join(BASE, "data/morphology/quranic-corpus-morphology-0.4.txt")
QNT = os.path.join(BASE, "quran-text/quran-no-tashkeel.json")
ASMA = os.path.join(BASE, "data/asma-al-husna.txt")
OUT = os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-2060.json")
SEED = 20260509
SEED_REP = 20260510
N_PERM = 10000

# ---------- fail-fast SHA gate ----------
def verify_sha():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"FAIL-FAST: prereg SHA mismatch.\n  expected {EXPECTED_SHA}\n  got      {sha}")
    print(f"[SHA OK] prereg locked at {sha}")

# ---------- parse QAC morphology ----------
# Token line: (s:v:w:seg)\tFORM\tTAG\tFEATURES
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")

def parse_morph():
    # surah -> verse -> word -> list of (seg, form, tag, feats)
    data = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    max_verse = defaultdict(int)
    max_word = defaultdict(lambda: defaultdict(int))
    with open(MORPH, encoding="utf-8") as f:
        for line in f:
            m = LOC_RE.match(line.rstrip("\n"))
            if not m:
                continue
            s, v, w, seg = (int(m.group(i)) for i in range(1, 5))
            form, tag, feats = m.group(5), m.group(6), m.group(7)
            data[s][v][w].append((seg, form, tag, feats))
            max_verse[s] = max(max_verse[s], v)
            max_word[s][v] = max(max_word[s][v], w)
    return data, max_verse, max_word

def word_root(segs):
    """Return the ROOT of the first segment that carries one, else None."""
    for (_seg, _form, _tag, feats) in segs:
        rm = ROOT_RE.search(feats)
        if rm:
            return rm.group(1)
    return None

def word_has_inl(segs):
    return any(tag == "INL" for (_s, _f, tag, _ft) in segs)

def word_lemmas(segs):
    out = []
    for (_seg, _form, _tag, feats) in segs:
        lm = LEM_RE.search(feats)
        if lm:
            out.append(lm.group(1))
    return out

def word_tags(segs):
    return [tag for (_s, _f, tag, _ft) in segs]

# ---------- no-tashkeel display forms ----------
def load_display():
    arr = json.load(open(QNT, encoding="utf-8"))
    disp = {}  # surah -> {verse -> [words]}
    for su in arr:
        sid = su["id"]
        disp[sid] = {}
        for ve in su["verses"]:
            disp[sid][ve["id"]] = ve["text"].split()
    return disp

# ---------- asma al-husna roots ----------
AR_DIAC = re.compile(r"[ً-ْٰـ]")
def strip_diac(s):
    return AR_DIAC.sub("", s).replace("ـ", "")

def load_asma_forms():
    forms = set()
    for line in open(ASMA, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        forms.add(strip_diac(line))
        # also without leading definite article ال
        if line.startswith("ال"):
            forms.add(strip_diac(line[2:]))
    return forms

# QAC roots that correspond to the recurrent surah-final divine-attribute names.
# Derived from the asma list; used to detect divine-name closers robustly across inflection.
DIVINE_ROOTS = {
    "Hkm",  # al-Hakim
    "rHm",  # al-Rahman / al-Rahim
    "gfr",  # al-Ghafur
    "Elm",  # al-Alim
    "smE",  # al-Sami'
    "Ezz",  # al-Aziz
    "bSr",  # al-Basir
    "qdr",  # al-Qadir / Qadeer
    "wdd",  # al-Wadud
    "Hmd",  # al-Hamid
    "gny",  # al-Ghani
    "ftH",  # al-Fattah
    "Hfظ",  # placeholder (not used)
    "lطf",  # al-Latif
    "Hlm",  # al-Halim
    "twb",  # al-Tawwab
    "rOf",  # al-Ra'uf
    "wfy",  # not divine
    "kbr",  # al-Kabir
    "Aly",  # al-Ali
    "Hyy",  # al-Hayy
    "qwm",  # al-Qayyum
    "wHd",  # al-Wahid / al-Ahad-ish
    "AHd",  # ahad (Q112 close-ish)
    "Smd",  # al-Samad
    "xbr",  # al-Khabir
    "qhr",  # al-Qahhar
    "wsE",  # al-Wasi'
    "krm",  # al-Karim
    "Alh",  # Allah (the Name itself)
    "rbb",  # al-Rabb
    "mlk",  # al-Malik
}

# ---------- opener-class cascade ----------
def classify_opener(s, data, max_verse, max_word, disp):
    """Return (opener_class, first_word_disp, first_root, first_content_word_disp, detail)."""
    # first content verse: v2 for Q1, else v1
    first_verse = 2 if s == 1 else 1
    words_in_v = max_word[s][first_verse]
    # first word (w=1) of first content verse
    w1_segs = data[s][first_verse][1]
    # display form of the first word (no-tashkeel): join all orthographic tokens at w=1
    fv_words = disp.get(s, {}).get(first_verse, [])
    first_word_disp = fv_words[0] if fv_words else ""
    # ---- cascade ----
    cls = None
    detail = ""
    # 1 muqattaat
    if word_has_inl(w1_segs):
        cls = "muqattaat"
    if cls is None:
        lems = word_lemmas(w1_segs)
        tags = word_tags(w1_segs)
        root = word_root(w1_segs)
        lemstr = "|".join(lems)
        # 2 qul
        if root == "qwl" and any("IMPV" in feats for (_a, _b, _c, feats) in w1_segs):
            cls = "qul-imperative"
        # 3 al-hamdu
        elif root == "Hmd":
            cls = "al-hamdu"
        # 4 tasbih/glorification
        elif root in ("sbH", "brk"):
            cls = "tasbih-glorification"
        # 5 vocative
        elif "VOC" in tags:
            cls = "vocative"
        # 6 oath-waw: the waw-al-qasam (PREFIX|w:P+ = oath preposition) OR a
        #   sentence-initial conjunctive waw (PREFIX|w:CONJ+) bound to a definite
        #   noun, i.e. the qasam formula  wa-l-<noun>. First segment must be a w-
        #   prefix and the word must bear a root (the sworn-by noun).
        elif (root is not None
              and any(feats.startswith("PREFIX|w:P+") or feats.startswith("PREFIX|w:CONJ+")
                      for (_a, _b, _c, feats) in w1_segs)
              and w1_segs[0][3].startswith("PREFIX|w:")):
            cls = "oath-waw"
        # 7 idha
        elif any(lm == "<i*aA" or lm == "i*aA" or lm == "<i*A" for lm in lems) or any("COND" in feats or "POS:T" in feats for (_a, _b, _c, feats) in w1_segs):
            # idha temporal/conditional opener (verify lemma below)
            if any("i*aA" in lm or "i*A" in lm for lm in lems):
                cls = "idha-conditional"
        # 8 interrogative
        elif "INTG" in tags:
            cls = "interrogative"
        # 9 other imperative
        elif root and any("IMPV" in feats for (_a, _b, _c, feats) in w1_segs):
            cls = "other-imperative"
        # 10 other verb
        elif "V" in tags:
            cls = "other-verb"
        if cls is None:
            # 11/12 conditional-particle or nominal/other
            if any("COND" in feats for (_a, _b, _c, feats) in w1_segs):
                cls = "conditional-particle"
            else:
                cls = "nominal-other"
        detail = lemstr
    # ---- first CONTENT word (root-bearing) for inclusio ----
    # Skip any leading INL (muqattaat) tokens; if the first content verse is
    # muqattaat-only (e.g. Q2/Q3 'Alm' is a standalone verse) continue into the
    # following verses until a root-bearing word is found. Use the QAC FORM
    # (transliterated, then back-rendered) so the display word aligns with the
    # word that actually owns the root (the no-tashkeel split can desync on pause
    # marks for muqattaat surahs).
    first_content_word_disp = first_word_disp
    first_root = None
    v = first_verse
    while v <= max_verse[s] and first_root is None:
        words_in_vv = max_word[s][v]
        vv_words = disp.get(s, {}).get(v, [])
        for w in range(1, words_in_vv + 1):
            r = word_root(data[s][v][w])
            if r is not None:
                first_root = r
                # best-effort display: the QAC stem form for the root-bearing seg
                stem = None
                for (_sg, form, _tg, feats) in data[s][v][w]:
                    if ROOT_RE.search(feats):
                        stem = form
                        break
                first_content_word_disp = stem if stem else (
                    vv_words[w - 1] if w - 1 < len(vv_words) else first_content_word_disp)
                break
        v += 1
    return cls, first_word_disp, first_root, first_content_word_disp, detail

# ---------- closer-class cascade ----------
def classify_closer(s, data, max_verse, max_word, disp):
    """Return (closer_class, last_word_disp, last_root, final_verse_id, detail)."""
    lv = max_verse[s]
    nwords = max_word[s][lv]
    lv_words = disp.get(s, {}).get(lv, [])
    last_word_disp = lv_words[-1] if lv_words else ""
    last_segs = data[s][lv][nwords]
    last_root = word_root(last_segs)
    # roots of the final-verse words (for divine-name-pair detection)
    verse_word_roots = []
    verse_word_tags = []
    for w in range(1, nwords + 1):
        verse_word_roots.append(word_root(data[s][lv][w]))
        verse_word_tags.append(word_tags(data[s][lv][w]))
    # terminal divine roots (scan from the end, contiguous divine attribute names)
    term_divine = []
    for w in range(nwords, 0, -1):
        r = verse_word_roots[w - 1]
        tags = verse_word_tags[w - 1]
        if r in DIVINE_ROOTS and r != "Alh" and ("N" in tags or "ADJ" in tags or "PN" in tags):
            term_divine.append(r)
        elif r is None and ("CONJ" in tags or "P" in tags or "DET" in tags):
            # allow a connector between two names
            continue
        else:
            break
    term_divine = list(reversed(term_divine))
    cls = None
    detail = ""
    # 1 divine-name-pair
    if len(term_divine) >= 2:
        cls = "divine-name-pair"
        detail = ",".join(term_divine)
    elif len(term_divine) == 1:
        cls = "single-divine-name"
        detail = term_divine[0]
    else:
        # 3 command/imperative anywhere in final verse
        has_impv = any("IMPV" in feats for w in range(1, nwords + 1) for (_a, _b, _c, feats) in data[s][lv][w])
        # 4 eschatological terminal roots
        ESCHATO = {"jHm", "nEm", "xld", "nwr", "jnn", "wqy", "Hsb", "frq", "smw", "Arض"}
        if has_impv:
            cls = "command-imperative"
        elif last_root in ("jHm", "nEm", "xld", "nar", "jnn", "wqy"):
            cls = "exhortation-eschatological"
        else:
            cls = "other"
            detail = "|".join(word_lemmas(last_segs))
    return cls, last_word_disp, last_root, lv, detail

# ---------- permutation null ----------
def perm_null(first_roots, last_roots, seed, n_perm):
    import random
    rng = random.Random(seed)
    # observed
    obs = sum(1 for i in range(114)
              if first_roots[i] is not None and last_roots[i] is not None
              and first_roots[i] == last_roots[i])
    last_pool = list(last_roots)
    ge = 0
    null_counts = []
    for _ in range(n_perm):
        rng.shuffle(last_pool)
        c = sum(1 for i in range(114)
                if first_roots[i] is not None and last_pool[i] is not None
                and first_roots[i] == last_pool[i])
        null_counts.append(c)
        if c >= obs:
            ge += 1
    p = (1 + ge) / (1 + n_perm)
    mean = sum(null_counts) / len(null_counts)
    return obs, p, mean

def main():
    verify_sha()
    data, max_verse, max_word = parse_morph()
    disp = load_display()
    assert len(max_verse) == 114, f"expected 114 surahs, got {len(max_verse)}"

    rows = []
    first_roots = [None] * 114
    last_roots = [None] * 114
    for s in range(1, 115):
        ocls, fw_disp, froot, fcw_disp, odet = classify_opener(s, data, max_verse, max_word, disp)
        ccls, lw_disp, lroot, lv, cdet = classify_closer(s, data, max_verse, max_word, disp)
        match = (froot is not None and lroot is not None and froot == lroot)
        rows.append({
            "surah": s,
            "opener_class": ocls,
            "first_word": fw_disp,
            "first_content_word": fcw_disp,
            "first_root": froot,
            "opener_detail": odet,
            "closer_class": ccls,
            "last_word": lw_disp,
            "last_root": lroot,
            "closer_detail": cdet,
            "final_verse": lv,
            "inclusio_match": match,
        })
        first_roots[s - 1] = froot
        last_roots[s - 1] = lroot

    # taxonomies
    opener_counts = Counter(r["opener_class"] for r in rows)
    closer_counts = Counter(r["closer_class"] for r in rows)

    # corpus-unique openers (singleton opener classes)
    singleton_opener_classes = sorted([c for c, n in opener_counts.items() if n == 1])
    # corpus-unique first-content-word roots (appear at exactly one surah-opening)
    fr_counts = Counter(r["first_root"] for r in rows if r["first_root"])
    lr_counts = Counter(r["last_root"] for r in rows if r["last_root"])
    singleton_first_roots = sorted([r for r, n in fr_counts.items() if n == 1])
    singleton_last_roots = sorted([r for r, n in lr_counts.items() if n == 1])

    # inclusio test
    obs, p, null_mean = perm_null(first_roots, last_roots, SEED, N_PERM)
    obs2, p2, null_mean2 = perm_null(first_roots, last_roots, SEED_REP, N_PERM)
    matches = [r["surah"] for r in rows if r["inclusio_match"]]

    # verdict
    floor = 10
    if p <= 0.05 and obs >= floor:
        verdict = "PASS-DIRECTED"
    elif p <= 0.05 and obs < floor:
        verdict = "PARTIAL (significant but below the pre-stated >=10 floor)"
    else:
        verdict = "NULL"

    result = {
        "id": "H-NEW-2060",
        "prereg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "seed_replication": SEED_REP,
        "n_perm": N_PERM,
        "rows": rows,
        "opener_taxonomy": dict(opener_counts.most_common()),
        "closer_taxonomy": dict(closer_counts.most_common()),
        "singleton_opener_classes": singleton_opener_classes,
        "singleton_first_content_roots": singleton_first_roots,
        "singleton_last_word_roots": singleton_last_roots,
        "inclusio": {
            "observed_match_count": obs,
            "match_surahs": matches,
            "perm_p_seed1": p,
            "null_mean_seed1": null_mean,
            "perm_p_seed2_replication": p2,
            "null_mean_seed2": null_mean2,
            "effect_floor": floor,
            "verdict": verdict,
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # ---- console report ----
    print("\n=== OPENER TAXONOMY (114 surahs) ===")
    for c, n in opener_counts.most_common():
        print(f"  {c:24s} {n:3d}")
    print("\n=== CLOSER TAXONOMY (114 surahs) ===")
    for c, n in closer_counts.most_common():
        print(f"  {c:24s} {n:3d}")
    print("\n=== INCLUSIO (strict single-word) ===")
    print(f"  observed match count : {obs}")
    print(f"  match surahs         : {matches}")
    print(f"  null mean (seed1)    : {null_mean:.3f}")
    print(f"  perm p (seed1)       : {p:.5f}")
    print(f"  perm p (seed2 repl)  : {p2:.5f}")
    print(f"  VERDICT              : {verdict}")
    print("\n=== CORPUS-UNIQUE ===")
    print(f"  singleton opener classes : {singleton_opener_classes}")
    print(f"  singleton first-content roots (count): {len(singleton_first_roots)}")
    print(f"  singleton last-word roots (count)    : {len(singleton_last_roots)}")
    print(f"\nwrote {OUT}")

if __name__ == "__main__":
    main()
