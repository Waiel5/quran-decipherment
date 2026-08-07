#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2730 — Does H-NEW-2690's scansion ordering survive a matched-partition control,
and is d_min length-invariant in practice?

The parent finding (H-NEW-2690) reported poetry < Qurʾān < prose on d_min and named the
missing control in its own honest limits: "designed-to-be-invariant is not the same as
verified-invariant.  A matched-partition control on this statistic is REQUIRED."

This runs it.

  * The SCANNER is lifted verbatim from scripts/h-new-2690.py (two contiguous source
    regions, SHA-gated).  Nothing is retyped.
  * The PARTITION is lifted verbatim from scripts/h-new-2680.py (the same three fragments
    H-NEW-2720 verified, same digests).
  * `normalise_words` strips every diacritic, so it cannot be used on a scansion test.  A
    vocalisation-preserving tokeniser is used and PROVED token-for-token equivalent to it.
  * A fast d_min is used for the bulk arms and PROVED identical to the lifted metricality()
    on 1500 units drawn from all four corpora.

Pre-reg : findings/phase-b-hypotheses/prereg-h-new-2730-scansion-genre-control.md
          SHA-256 embedded below, verified at runtime; mismatch -> SystemExit.
Seeds   : 20260509 primary / 20260519 replication.
Author  : Waiel Al-Shujaa.  Bismillāhi al-Raḥmāni al-Raḥīm.

Declared INVESTIGATION-PROTOCOL 7.1 deviation: multiprocessing is used (stdlib) purely to
parallelise a pure function of a string; results are order-preserving and seed-independent.
No numpy.
"""
import hashlib
import json
import math
import os
import platform
import random
import re
import statistics
import sys
import time
import unicodedata
from collections import Counter
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                      # findings/phase-b-hypotheses
REPO = os.path.dirname(os.path.dirname(ROOT))     # repo root
CSVDIR = os.path.join(ROOT, "csv")

PREREG_REL = "findings/phase-b-hypotheses/prereg-h-new-2730-scansion-genre-control.md"
PREREG_SHA256 = "a5f742e15a8be6393b049ec2add61f237c36f165c884b54e0a17fb22c3578c25"

SRC2690_REL = "findings/phase-b-hypotheses/scripts/h-new-2690.py"
SRC2680_REL = "findings/phase-b-hypotheses/scripts/h-new-2680.py"

QURAN_FULL_REL = "quran-text/quran-full-tashkeel.json"
QURAN_NONE_REL = "quran-text/quran-no-tashkeel.json"
DARIMI_REL = "data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/darimi.json"
BUKHARI_REL = "data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/bukhari.json"
MUAL_DIR_REL = "data/baseline-corpora/raw"
MUAL_STEMS = ["muallaqa-imru-al-qais", "muallaqa-zuhayr", "muallaqa-amr-bin-kulthum"]
GROUND = {"muallaqa-imru-al-qais": "tawil", "muallaqa-zuhayr": "tawil",
          "muallaqa-amr-bin-kulthum": "wafir"}

FROZEN = {
    QURAN_FULL_REL: "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    QURAN_NONE_REL: "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
    DARIMI_REL:     "45ec3ac92b072287e6c7451084f55f50a2676e0eab2ec165c4ffecfa57f41d2a",
    BUKHARI_REL:    "9d2e4194786c275f64f627c834711ea0e339a8fe226d5e9569ef962595a562f1",
    MUAL_DIR_REL + "/muallaqa-imru-al-qais.txt":
        "06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14",
    MUAL_DIR_REL + "/muallaqa-zuhayr.txt":
        "9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2",
    MUAL_DIR_REL + "/muallaqa-amr-bin-kulthum.txt":
        "d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720",
    SRC2690_REL:    "3262dd417b0fa4edef28ecb939a6ac57f5e0059309257c030891a56d54034672",
    SRC2680_REL:    "57d6b214344ea81433e9f840524e6259953657fbf60e8fd54fdd8d2706b88497",
}

SEED, SEED_REPL = 20260509, 20260519
N_PERM = 10000
BONF_K = 4
ALPHA_BON = 0.05 / BONF_K            # 0.0125, prereg §5
N_OFF_FULL, N_DRAW_FULL = 200, 200   # prereg §4.2, §4.3
N_OFF_SENS = 60                      # sensitivity + replication cells, prereg §5
N_SUB = 500                          # units scored per offset partition, prereg §4.2
NATIVE_PROSE_CAP = 2500              # 2690's ARM_CAP
IDENTITY_GATE_N = 1500               # prereg §3.2
QURAN_NGRAM = 7                      # prereg §2.2
MIN_BIN_PER_ARM = 30                 # prereg §4.5b
POOL_MIN = 96                        # farm a batch out once it is worth the round-trip
PERM_N = N_PERM                      # explicit; equals perm_median_diff's locked default


def P(rel):
    return os.path.join(REPO, rel)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def die(msg):
    raise SystemExit("[FATAL] " + msg)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ===========================================================================
# 0. LOCKS
# ===========================================================================
def verify_locks():
    got = sha256_file(P(PREREG_REL))
    if got != PREREG_SHA256:
        die("PRE-REG SHA MISMATCH\n  expected %s\n  got      %s" % (PREREG_SHA256, got))
    log("[lock] pre-reg %s VERIFIED" % PREREG_SHA256[:16])
    for rel, want in sorted(FROZEN.items()):
        g = sha256_file(P(rel))
        if g != want:
            die("FROZEN INPUT MISMATCH %s\n  expected %s\n  got      %s" % (rel, want, g))
    log("[lock] %d frozen inputs VERIFIED" % len(FROZEN))


verify_locks()

# ===========================================================================
# 1. THE SCANNER — LIFTED VERBATIM FROM H-NEW-2690 (prereg §3.1)
#    Two contiguous source regions are extracted, SHA-checked and exec'd.
# ===========================================================================
_S2690 = open(P(SRC2690_REL), encoding="utf-8").read()

_R1_A = _S2690.index('FATHA, DAMMA, KASRA')
_R1_B = _S2690.index('# ---------------------------------------------------------------------------\n'
                     '# 3. POSITIVE CONTROL')
_R1 = _S2690[_R1_A:_R1_B].rstrip() + "\n"          # syllabifier + METERS + metricality
_R2_A = _S2690.index('def perm_median_diff')
_R2_B = _S2690.index('RESULTS = {}')
_R2 = _S2690[_R2_A:_R2_B].rstrip() + "\n"          # perm_median_diff + matched_noise

_EXPECT_2690 = {"scanner_region": "013d8ee0ea231c22", "stats_region": "01c105b800e89fd9"}
for _name, _txt in (("scanner_region", _R1), ("stats_region", _R2)):
    _got = hashlib.sha256(_txt.encode()).hexdigest()[:16]
    if _got != _EXPECT_2690[_name]:
        die("MW-6 FAIL: 2690 %s changed (sha %s, expected %s)"
            % (_name, _got, _EXPECT_2690[_name]))

_SCAN_NS = {"re": re, "unicodedata": unicodedata, "random": random,
            "statistics": statistics, "N_PERM": N_PERM}
exec(compile(_R1, "<h-new-2690:scanner>", "exec"), _SCAN_NS)
exec(compile(_R2, "<h-new-2690:stats>", "exec"), _SCAN_NS)

scan = _SCAN_NS["scan"]
metricality = _SCAN_NS["metricality"]
best_meter = _SCAN_NS["best_meter"]
tiled = _SCAN_NS["tiled"]
lev_band = _SCAN_NS["lev_band"]
METERS = _SCAN_NS["METERS"]
MNAMES = [m[0] for m in METERS]
perm_median_diff = _SCAN_NS["perm_median_diff"]
matched_noise = _SCAN_NS["matched_noise"]
log("[MW-6] 2690 scanner lifted verbatim, 2 regions SHA-verified "
    "(%d meters, defines %s)" % (len(METERS), ", ".join(sorted(
        k for k in ("scan", "metricality", "best_meter", "matched_noise",
                    "perm_median_diff") if k in _SCAN_NS))))

# ===========================================================================
# 2. THE PARTITION — LIFTED VERBATIM FROM H-NEW-2680 (prereg §3.3)
#    Same three fragments, same digests, that H-NEW-2720 verified.
# ===========================================================================
_S2680 = open(P(SRC2680_REL), encoding="utf-8").read()


def _grab2680(name):
    m = re.search(r"^def %s\(.*?(?=\n\ndef |\n\n# ===|\Z)" % name, _S2680, re.S | re.M)
    if not m:
        die("MW-6 FAIL: could not locate %s() in the frozen 2680 source" % name)
    return m.group(0).rstrip() + "\n"


_regex_block = re.search(r"AR_DIAC = .*?\nNON_AR = .*?\n", _S2680, re.S).group(0)
_FRAG2680 = {"regex": _regex_block,
             "normalise_words": _grab2680("normalise_words"),
             "build_pseudo_corpus": _grab2680("build_pseudo_corpus")}
_EXPECT_2680 = {"regex": "2cd4d0ca289fd137",
                "normalise_words": "8e49ae080acc6335",
                "build_pseudo_corpus": "6931e0863f09a79c"}
for _k, _t in _FRAG2680.items():
    _got = hashlib.sha256(_t.encode()).hexdigest()[:16]
    if _got != _EXPECT_2680[_k]:
        die("MW-6 FAIL: 2680 fragment %r changed (sha %s, expected %s)"
            % (_k, _got, _EXPECT_2680[_k]))

_PART_NS = {"re": re}
for _k in ("regex", "normalise_words", "build_pseudo_corpus"):
    exec(compile(_FRAG2680[_k], "<h-new-2680:%s>" % _k, "exec"), _PART_NS)
AR_DIAC = _PART_NS["AR_DIAC"]
NON_AR = _PART_NS["NON_AR"]
normalise_words = _PART_NS["normalise_words"]
_build_pseudo_corpus_2680 = _PART_NS["build_pseudo_corpus"]
log("[MW-6] 2680 partition lifted verbatim, 3 fragments SHA-verified "
    "(identical digests to H-NEW-2720's)")


def part2680(words, profile):
    """Call 2680's build_pseudo_corpus verbatim, supplying the QVERSE_WLEN it reads
    from its own module globals.  The only thing that varies is which of the two
    locked word-length profiles (prereg §3.4) is installed."""
    _PART_NS["QVERSE_WLEN"] = profile
    return _build_pseudo_corpus_2680(words)


# ---------------------------------------------------------------------------
# 2a. Vocalisation-preserving tokeniser + its locked equivalence gate (§3.3)
# ---------------------------------------------------------------------------
def normalise_words_voc(text):
    """2680's normalise_words, but retaining every character AR_DIAC deletes.

    AR_DIAC covers U+0610-U+061A, U+0640, U+064B-U+065F, U+0670, U+06D6-U+06ED — i.e.
    every diacritic the scanner reads.  Those characters are DELETED by normalise_words
    without creating a token boundary, so keeping them cannot move a boundary.  Every
    other non-Arabic-letter character becomes a boundary in both functions.
    """
    out = []
    for ch in text:
        if NON_AR.match(ch) is None or AR_DIAC.match(ch) is not None:
            out.append(ch)
        else:
            out.append(" ")
    return "".join(out).split()


def gate_tokeniser(label, raw):
    voc = normalise_words_voc(raw)
    stripped = [s for s in (AR_DIAC.sub("", w) for w in voc) if s]
    plain = normalise_words(raw)
    if stripped != plain:
        n = min(len(stripped), len(plain))
        i = next((j for j in range(n) if stripped[j] != plain[j]), n)
        die("TOKENISER EQUIVALENCE GATE FAILED for %s: %d vs %d tokens; first diff at %d "
            "(%r vs %r)" % (label, len(stripped), len(plain), i,
                            stripped[i:i + 3], plain[i:i + 3]))
    return voc


# ---------------------------------------------------------------------------
# 2b. Cyclic partition + its locked equivalence gate (§4.3)
# ---------------------------------------------------------------------------
def build_pseudo_corpus_cyclic(words, profile, profile_start=0, offset=0):
    """2680's cut, extended to streams too short to complete one pass of the profile.

    Cuts `words[offset:]` into units of length profile[(profile_start+i) % len(profile)]
    until the stream is exhausted; the final partial unit is discarded.  With
    profile_start=0, offset=0 and a stream of at least sum(profile) words this returns
    exactly what build_pseudo_corpus returns (asserted at runtime).
    """
    n = len(profile)
    units, p, i, W = [], offset, 0, len(words)
    while True:
        L = profile[(profile_start + i) % n]
        if p + L > W:
            break
        units.append(words[p:p + L])
        p += L
        i += 1
        if i >= n and profile_start == 0 and offset == 0:
            break
    return units


def gate_cyclic(label, words, profile):
    ref, err = part2680(words, profile)
    if err:
        die("CYCLIC GATE: 2680 build_pseudo_corpus refused %s: %s" % (label, err))
    got = build_pseudo_corpus_cyclic(words, profile, 0, 0)
    if got != ref:
        die("CYCLIC EQUIVALENCE GATE FAILED for %s: %d vs %d units" % (label, len(got), len(ref)))
    log("[MW-6] cyclic partition == 2680 build_pseudo_corpus on %s (%d units)"
        % (label, len(ref)))


# ===========================================================================
# 3. FAST d_min + its locked identity gate (prereg §3.2)
# ===========================================================================
_CANON = {}


def _canons(L):
    r = _CANON.get(L)
    if r is None:
        d = {}
        for mi, (k, ar, h) in enumerate(METERS):
            for ph in range(len(h)):
                c = tiled(h, L, ph)
                if c not in d or mi < d[c]:
                    d[c] = mi
        r = [(c, mi, int(c.replace("-", "1").replace("v", "0"), 2), c.count("-"))
             for c, mi in d.items()]
        _CANON[L] = r
    return r


def dmin_fast(obs):
    """d_min and argmin meter, identical to metricality()[0:2].  See prereg §3.2."""
    L = len(obs)
    if L < 4:
        return 1.0, None
    ob = int(obs.replace("-", "1").replace("v", "0"), 2)
    nh = obs.count("-")
    scored = sorted((((ob ^ cb).bit_count(), mi, c, abs(nh - ch))
                     for c, mi, cb, ch in _canons(L)), key=lambda t: (t[0], t[1]))
    best = scored[0][0]
    bestmi = len(METERS)
    for ham, mi, c, lb in scored:
        if lb > best or (lb == best and mi > bestmi):
            continue
        d = lev_band(obs, c, best)
        if d < best:
            best, bestmi = d, mi
        elif d == best and mi < bestmi:
            bestmi = mi
    return best / L, METERS[bestmi][0]


def gate_identity(strings):
    bad = 0
    for s in strings:
        a = metricality(s)
        b = dmin_fast(s)
        if abs(a[0] - b[0]) > 1e-12 or a[1] != b[1]:
            bad += 1
            if bad <= 3:
                log("  identity mismatch: %r -> %s/%s vs %s/%s" % (s[:40], a[0], a[1], b[0], b[1]))
    if bad:
        die("dmin_fast IDENTITY GATE FAILED on %d/%d units (prereg §3.2, §11)"
            % (bad, len(strings)))
    log("[MW-6] dmin_fast identity gate PASSED on %d units across 4 corpora" % len(strings))


# ---------------------------------------------------------------------------
# 3a. memoised, parallel d_min over string batches
# ---------------------------------------------------------------------------
DCACHE = {}
_POOL = None


def _worker(batch):
    return [dmin_fast(s) for s in batch]


def dmin_many(strings):
    """Return [(d_min, argmin), ...] aligned with `strings`, memoised across calls."""
    todo = []
    seen = set()
    for s in strings:
        if s not in DCACHE and s not in seen:
            seen.add(s)
            todo.append(s)
    if todo:
        if _POOL is None or len(todo) < POOL_MIN:
            for s in todo:
                DCACHE[s] = dmin_fast(s)
        else:
            # d_min cost grows with unit length, and unit lengths are very unevenly
            # distributed (Qurʾānic verses median 28 syllables, prose sentences 75).
            # Stride-chunking interleaves long and short units so no worker is left
            # holding all the expensive ones.
            nw = os.cpu_count() * 4
            chunks = [todo[i::nw] for i in range(min(nw, len(todo)))]
            for ch, res in zip(chunks, _POOL.map(_worker, chunks)):
                for s, r in zip(ch, res):
                    DCACHE[s] = r
    return [DCACHE[s] for s in strings]


def _perm_worker(job):
    A, B, sd = job
    return perm_median_diff(A, B, sd, PERM_N)


def run_perms(jobs):
    """Execute independent perm_median_diff calls, in the pool when one exists.

    Each job is (A, B, seed) and the lifted perm_median_diff is a pure function seeded
    per call, so farming them out cannot change any p-value: every call sees the
    identical random.Random(seed) stream it would see sequentially.
    """
    if _POOL is not None and len(jobs) > 1:
        return _POOL.map(_perm_worker, jobs)
    return [_perm_worker(j) for j in jobs]


# ===========================================================================
# 4. CORPORA
# ===========================================================================
log("\n[corpora] loading")
_QF = json.load(open(P(QURAN_FULL_REL), encoding="utf-8"))
_QN = json.load(open(P(QURAN_NONE_REL), encoding="utf-8"))
QVERSE_TEXT = [v["text"] for s in _QF for v in s["verses"]]
if len(QVERSE_TEXT) != 6236:
    die("Qurʾān verses %d != 6236" % len(QVERSE_TEXT))
NV = [len(s["verses"]) for s in _QF]

PROFILES = {
    "W_2680": [len(v["text"].split()) for s in _QN for v in s["verses"]],
    "W_lex":  [len(v["text"].split()) for s in _QF for v in s["verses"]],
}
for k, v in PROFILES.items():
    log("  profile %-7s n=%d sum=%d" % (k, len(v), sum(v)))

# Qurʾān's own vocalised word stream, for the baseline-free self-recut arm (§4.4).
# NOT passed through normalise_words_voc: that tokeniser reproduces 2680's word
# boundaries, and 2680's NON_AR treats U+0671 (alef waṣla, 13,483 occurrences here) as a
# boundary, which would shatter Qurʾānic words.  The self-recut arm cuts the Qurʾān's own
# stream and is compared only to itself, so it takes the verse texts' own whitespace
# tokens — the same tokens scan() reads in the native arm.
QURAN_WORDS_D8 = " ".join(QVERSE_TEXT).split()
log("  quran self-recut word stream: %d tokens (verse whitespace tokens, as scanned)"
    % len(QURAN_WORDS_D8))

# ---- Qurʾānic-quotation strip (§2.2) --------------------------------------
_QPLAIN = normalise_words(" ".join(QVERSE_TEXT))
_QGRAMS = frozenset(tuple(_QPLAIN[i:i + QURAN_NGRAM])
                    for i in range(len(_QPLAIN) - QURAN_NGRAM + 1))
log("  quran %d-gram set: %d grams" % (QURAN_NGRAM, len(_QGRAMS)))


def strip_quran_quotation(voc_words):
    plain = [AR_DIAC.sub("", w) for w in voc_words]
    n = len(plain)
    mark = bytearray(n)
    for i in range(n - QURAN_NGRAM + 1):
        if tuple(plain[i:i + QURAN_NGRAM]) in _QGRAMS:
            for j in range(i, i + QURAN_NGRAM):
                mark[j] = 1
    kept = [w for w, m in zip(voc_words, mark) if not m]
    return kept, n - len(kept)


SENT = re.compile(r"[.؟!]")
AR = re.compile("[ء-ي]")


def load_hadith(rel, label):
    d = json.load(open(P(rel), encoding="utf-8"))
    texts = [(h.get("arabic") or "") for h in d["hadiths"]]
    raw = " ".join(texts)
    voc = gate_tokeniser(label, raw)
    kept, dropped = strip_quran_quotation(voc)
    sents = []
    for t in texts:
        for s in SENT.split(t):
            s = s.strip()
            if len(AR.findall(s)) >= 10:
                sents.append(s)
    log("  %-8s hadith=%d  voc_words=%d  quran-quote dropped=%d (%.2f%%)  stream=%d  "
        "sentences=%d" % (label, len(texts), len(voc), dropped,
                          100.0 * dropped / max(1, len(voc)), len(kept), len(sents)))
    return {"label": label, "stream": kept, "n_voc": len(voc), "dropped": dropped,
            "sentences": sents, "n_hadith": len(texts)}


PROSE = [load_hadith(DARIMI_REL, "darimi"), load_hadith(BUKHARI_REL, "bukhari")]

# ---- poetry ---------------------------------------------------------------
VOC_THRESH = 0.55
DIAC = re.compile("[ً-ْٰٓ-ٕۡ]")
POET_LINES = []          # (poet_stem, known_meter, line_text)
for stem in MUAL_STEMS:
    for line in open(P(MUAL_DIR_REL + "/" + stem + ".txt"), encoding="utf-8",
                     errors="replace"):
        a = len(AR.findall(line))
        if a >= 12 and len(DIAC.findall(line)) / a >= VOC_THRESH:
            POET_LINES.append((stem, GROUND[stem], line.strip()))
POETRY_TOKENS = []       # (word, poet_stem)
for stem in MUAL_STEMS:
    voc = gate_tokeniser(stem, open(P(MUAL_DIR_REL + "/" + stem + ".txt"),
                                    encoding="utf-8", errors="replace").read())
    POETRY_TOKENS.extend((w, stem) for w in voc)
log("  poetry   abyat=%d  voc_words=%d  (partition needs %d — %.1f%%)"
    % (len(POET_LINES), len(POETRY_TOKENS), sum(PROFILES["W_2680"]),
       100.0 * len(POETRY_TOKENS) / sum(PROFILES["W_2680"])))

for pr in PROSE:
    for pname in ("W_2680", "W_lex"):
        need = sum(PROFILES[pname])
        if len(pr["stream"]) < need:
            die("%s fell below %d words after the Qurʾān strip (%d) — prereg §11"
                % (pr["label"], need, len(pr["stream"])))
    gate_cyclic(pr["label"], pr["stream"], PROFILES["W_2680"])


# ===========================================================================
# 5. ARMS
# ===========================================================================
def med(x):
    return statistics.median(x) if x else float("nan")


def r2_on_log_len(strings, ds):
    xs = [math.log(len(s)) for s, d in zip(strings, ds) if len(s) >= 4]
    ys = [d for s, d in zip(strings, ds) if len(s) >= 4]
    n = len(xs)
    if n < 10:
        return None, None, None, None
    mx, my = sum(xs) / n, sum(ys) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    sxx = sum((a - mx) ** 2 for a in xs)
    syy = sum((b - my) ** 2 for b in ys)
    if sxx <= 0 or syy <= 0:
        return None, None, None, None
    beta = sxy / sxx
    return sxy * sxy / (sxx * syy), beta, my - beta * mx, sxy / math.sqrt(sxx * syy)


def bootstrap_medians(vals, n_draw, n_sub, seed):
    rng = random.Random(seed)
    return [statistics.median(rng.sample(vals, min(n_sub, len(vals)))) for _ in range(n_draw)]


def offset_partition_medians(stream, profile, n_off, n_sub, seed, mode, tag):
    """Median d_min of a seed-locked n_sub sub-sample of each of n_off offset partitions."""
    need = sum(profile)
    slack = len(stream) - need
    rng = random.Random(seed)
    offsets = [rng.randrange(0, slack + 1) for _ in range(n_off)]
    meds, t0 = [], time.time()
    for j, off in enumerate(offsets):
        units, err = part2680(stream[off:], profile)
        if err:
            die("offset partition failed for %s at offset %d: %s" % (tag, off, err))
        sub = random.Random(seed + j).sample(range(len(units)), n_sub)
        strs = [scan(" ".join(units[i]), mode) for i in sub]
        dmin_many(strs)
        ds = [DCACHE[s][0] for s in strs if len(s) >= 4]
        meds.append(statistics.median(ds))
        if (j + 1) % 50 == 0:
            log("      [%s] %d/%d offsets  %.0fs" % (tag, j + 1, n_off, time.time() - t0))
    return meds, offsets


def cyclic_partition_medians(tokens, profile, n_draw, seed, mode, tag,
                             n_sub=None, with_meter=False):
    """Cyclic-profile cut of a stream too short for one full pass (prereg §4.3)."""
    rng = random.Random(seed)
    words = [t[0] if isinstance(t, tuple) else t for t in tokens]
    tags = [t[1] if isinstance(t, tuple) else None for t in tokens]
    meds, sizes, meter_hits, meter_n = [], [], 0, 0
    argmin_hits, argmin_n = 0, 0
    draws = [(0, 0)] + [(rng.randrange(len(profile)), rng.randrange(0, 100))
                        for _ in range(n_draw - 1)]
    for j, (ps, off) in enumerate(draws):
        n = len(profile)
        units, starts, p, i = [], [], off, 0
        while True:
            L = profile[(ps + i) % n]
            if p + L > len(words):
                break
            units.append(words[p:p + L])
            starts.append(p)
            p += L
            i += 1
        if n_sub and len(units) > n_sub:
            keep = sorted(random.Random(seed + j).sample(range(len(units)), n_sub))
            units = [units[i] for i in keep]
            starts = [starts[i] for i in keep]
        strs = [scan(" ".join(u), mode) for u in units]
        pairs = dmin_many(strs)
        ds = [d for s, (d, k) in zip(strs, pairs) if len(s) >= 4]
        if not ds:
            continue
        meds.append(statistics.median(ds))
        sizes.append(len(ds))
        if with_meter:
            for s, st, (dm, am) in zip(strs, starts, pairs):
                if len(s) < 8:
                    continue
                b, _ = best_meter(s)
                meter_n += 1
                meter_hits += (b == GROUND[tags[st]])
                if am is not None:
                    argmin_n += 1
                    argmin_hits += (am == GROUND[tags[st]])
    return {"medians": meds, "n_units": sizes,
            "meter_acc": (meter_hits / meter_n) if meter_n else None,
            "meter_n": meter_n,
            "argmin_acc": (argmin_hits / argmin_n) if argmin_n else None,
            "argmin_n": argmin_n}


def pct_le(band, q):
    """percentile of q inside band, and how many band values are <= q."""
    n_le = sum(1 for b in band if b <= q)
    return 100.0 * sum(1 for b in band if b < q) / len(band), n_le


# ---------------------------------------------------------------------------
def run_cell(name, mode, profile_name, n_off, n_draw, seed, full):
    profile = PROFILES[profile_name]
    log("\n" + "=" * 78)
    log("CELL %s   pausal=%s  profile=%s  n_off=%d  n_draw=%d  seed=%d  full=%s"
        % (name, mode, profile_name, n_off, n_draw, seed, full))
    log("=" * 78)
    C = {"cell": name, "pausal_tuple": mode, "word_profile": profile_name,
         "n_offsets": n_off, "n_draws": n_draw, "seed": seed, "full_arms": full}
    t0 = time.time()

    # ---- native arms -----------------------------------------------------
    q_str = [scan(t, mode) for t in QVERSE_TEXT]
    dmin_many(q_str)
    q_d = [DCACHE[s][0] for s in q_str if len(s) >= 4]

    p_str = [scan(l, mode) for _, _, l in POET_LINES]
    p_str = [s for s in p_str if len(s) >= 8]
    dmin_many(p_str)
    p_d = [DCACHE[s][0] for s in p_str if len(s) >= 4]

    prose_native = {}
    for pr in PROSE:
        rs = [scan(t, mode) for t in pr["sentences"]]
        rs = [s for s in rs if len(s) >= 8]
        rs = rs if len(rs) <= NATIVE_PROSE_CAP else random.Random(SEED).sample(rs, NATIVE_PROSE_CAP)
        dmin_many(rs)
        prose_native[pr["label"]] = {"strings": rs, "d": [DCACHE[s][0] for s in rs if len(s) >= 4]}

    C["native"] = {
        "quran": {"n": len(q_d), "median": round(med(q_d), 5),
                  "mean": round(statistics.mean(q_d), 5),
                  "median_syllables": statistics.median([len(s) for s in q_str if len(s) >= 4])},
        "poetry": {"n": len(p_d), "median": round(med(p_d), 5),
                   "mean": round(statistics.mean(p_d), 5),
                   "median_syllables": statistics.median([len(s) for s in p_str])},
    }
    for k, v in prose_native.items():
        C["native"][k] = {"n": len(v["d"]), "median": round(med(v["d"]), 5),
                          "mean": round(statistics.mean(v["d"]), 5),
                          "median_syllables": statistics.median([len(s) for s in v["strings"]])}
    log("  NATIVE median d_min: poetry=%.5f  quran=%.5f  %s"
        % (med(p_d), med(q_d), "  ".join("%s=%.5f" % (k, med(v["d"]))
                                         for k, v in prose_native.items())))
    log("  NATIVE median syllable length: poetry=%d  quran=%d  %s"
        % (C["native"]["poetry"]["median_syllables"], C["native"]["quran"]["median_syllables"],
           "  ".join("%s=%d" % (k, C["native"][k]["median_syllables"]) for k in prose_native)))

    Q = med(q_d)
    C["quran_band"] = sorted(bootstrap_medians(q_d, 200, N_SUB, seed))

    # ---- D1: matched-partition prose ------------------------------------
    # Permutation tests are collected and run together (run_perms); each is a pure,
    # per-call-seeded function, so batching cannot alter a p-value.
    C["D1"] = {}
    perm_jobs, perm_slots = [], []
    d1_pre = {}
    for pr in PROSE:
        meds, offs = offset_partition_medians(pr["stream"], profile, n_off, N_SUB,
                                              seed, mode, "%s/%s" % (name, pr["label"]))
        pctl, n_le = pct_le(meds, Q)
        units, _ = part2680(pr["stream"][offs[0]:], profile)
        sub = random.Random(seed).sample(range(len(units)), min(3000, len(units)))
        pooled = [scan(" ".join(units[i]), mode) for i in sub]
        dmin_many(pooled)
        pooled_d = [DCACHE[s][0] for s in pooled if len(s) >= 4]
        d1_pre[pr["label"]] = (meds, pctl, n_le)
        perm_jobs.append((pooled_d, q_d, seed))           # locked: prose - quran > 0
        perm_slots.append(("D1", pr["label"]))

    # ---- D2 + D7: matched-cut poetry, with the positive control ----------
    po = cyclic_partition_medians(POETRY_TOKENS, profile, n_draw, seed, mode,
                                  "%s/poetry" % name, with_meter=True)
    pmeds = po["medians"]
    n_ge = sum(1 for m in pmeds if m >= Q)
    ppct = 100.0 * sum(1 for m in pmeds if m < Q) / len(pmeds)
    words = [w for w, _ in POETRY_TOKENS]
    u0 = build_pseudo_corpus_cyclic(words, profile, 0, 0)
    s0 = [scan(" ".join(u), mode) for u in u0]
    dmin_many(s0)
    pool_pd = [DCACHE[s][0] for s in s0 if len(s) >= 4]
    perm_jobs.append((q_d, pool_pd, seed))                # locked: quran - poetry > 0
    perm_slots.append(("D2", None))

    # ---- D6: excess over matched noise (computed here so its perms batch too) ----
    ex = {}
    if full:
        def excess(strings, sd):
            noi = matched_noise(strings, sd)
            dmin_many(noi)
            return [DCACHE[o][0] - DCACHE[n][0]
                    for o, n in zip(strings, noi) if len(o) >= 4 and len(n) >= 4]
        ex["quran"] = excess(q_str, seed)
        ex["poetry"] = excess(p_str, seed)
        for k, v in prose_native.items():
            ex[k] = excess(v["strings"], seed)
        perm_jobs.append((ex["quran"], ex["poetry"], seed))   # locked: quran - poetry > 0
        perm_slots.append(("D6a", None))
        for k in prose_native:
            perm_jobs.append((ex[k], ex["quran"], seed))      # locked: prose - quran > 0
            perm_slots.append(("D6b", k))

    log("  [perm] running %d permutation tests (%d perms each)" % (len(perm_jobs), N_PERM))
    tp = time.time()
    perm_res = dict(zip([tuple(s) for s in perm_slots], run_perms(perm_jobs)))
    log("  [perm] done in %.0fs" % (time.time() - tp))

    for pr in PROSE:
        meds, pctl, n_le = d1_pre[pr["label"]]
        diff, p = perm_res[("D1", pr["label"])]
        C["D1"][pr["label"]] = {
            "median_native": round(med(prose_native[pr["label"]]["d"]), 5),
            "partition_median_mean": round(statistics.mean(meds), 5),
            "partition_median_min": round(min(meds), 5),
            "partition_median_max": round(max(meds), 5),
            "quran_median": round(Q, 5),
            "quran_percentile_in_band": round(pctl, 1),
            "n_offsets_le_quran": n_le, "n_offsets": len(meds),
            "perm_diff_prose_minus_quran": round(diff, 5), "perm_p": round(p, 6),
            "medians": [round(m, 5) for m in meds],
        }
        log("  D1 %-8s native=%.5f -> partition mean=%.5f [%.5f, %.5f]  quran=%.5f  "
            "offsets<=quran %d/%d  perm diff=%+.5f p=%.5f"
            % (pr["label"], med(prose_native[pr["label"]]["d"]), statistics.mean(meds),
               min(meds), max(meds), Q, n_le, len(meds), diff, p))

    diff2, p2 = perm_res[("D2", None)]
    C["D2"] = {"median_native": round(med(p_d), 5),
               "partition_median_mean": round(statistics.mean(pmeds), 5),
               "partition_median_min": round(min(pmeds), 5),
               "partition_median_max": round(max(pmeds), 5),
               "deterministic_draw": round(pmeds[0], 5),
               "quran_median": round(Q, 5),
               "n_draws_ge_quran": n_ge, "n_draws": len(pmeds),
               "quran_percentile_in_band": round(ppct, 1),
               "median_units_per_draw": statistics.median(po["n_units"]),
               "perm_diff_quran_minus_poetry": round(diff2, 5), "perm_p": round(p2, 6),
               "medians": [round(m, 5) for m in pmeds]}
    # native-poetry argmin baseline, for the MW-7 diagnostic below
    nat_arg_n = nat_arg_hit = 0
    for (_, known, line) in POET_LINES:
        ss = scan(line, mode)
        if len(ss) < 8:
            continue
        am = DCACHE[ss][1] if ss in DCACHE else dmin_fast(ss)[1]
        if am is not None:
            nat_arg_n += 1
            nat_arg_hit += (am == known)
    C["D7"] = {"partitioned_meter_acc": round(po["meter_acc"], 4) if po["meter_acc"] else None,
               "partitioned_meter_n": po["meter_n"],
               "MW7_diagnostic": {
                   "note": "best_meter() compares against a DOUBLED hemistich of fixed "
                           "length and normalises by max(len) — it is NOT length-invariant, "
                           "so on units that are not bayt-length it is being used outside "
                           "its calibration. d_min's argmin IS length-invariant (tiled to L "
                           "at every phase). Both are reported so the D7 failure can be "
                           "attributed. Descriptive only; changes no verdict.",
                   "partitioned_argmin_acc": round(po["argmin_acc"], 4) if po["argmin_acc"] else None,
                   "partitioned_argmin_n": po["argmin_n"],
                   "native_argmin_acc": round(nat_arg_hit / nat_arg_n, 4) if nat_arg_n else None,
                   "native_argmin_n": nat_arg_n,
                   "chance_16_way": round(1 / 16, 4)}}
    log("  D2 poetry native=%.5f -> cut mean=%.5f [%.5f, %.5f]  quran=%.5f  "
        "draws>=quran %d/%d  perm diff=%+.5f p=%.5f"
        % (med(p_d), statistics.mean(pmeds), min(pmeds), max(pmeds), Q, n_ge,
           len(pmeds), diff2, p2))
    log("  D7 partitioned-poetry meter recovery: %s on n=%d (native benchmark 0.771, "
        "chance 0.0625)" % (("%.4f" % po["meter_acc"]) if po["meter_acc"] else "n/a",
                            po["meter_n"]))
    log("     [MW-7] d_min argmin-meter recovery: partitioned=%s (n=%d)  native=%s (n=%d)"
        % (po["argmin_acc"], po["argmin_n"],
           C["D7"]["MW7_diagnostic"]["native_argmin_acc"], nat_arg_n))

    if not full:
        C["seconds"] = round(time.time() - t0, 1)
        return C

    # ---- D4: length-invariance regression --------------------------------
    C["D4"] = {}
    arms = [("poetry", p_str), ("quran", q_str)] + \
           [(k, v["strings"]) for k, v in prose_native.items()]
    all_s, all_d = [], []
    for k, ss in arms:
        ds = [DCACHE[s][0] for s in ss]
        r2, beta, alpha, r = r2_on_log_len(ss, ds)
        C["D4"][k] = {"r2": round(r2, 5) if r2 else None,
                      "beta_log_len": round(beta, 5) if beta else None,
                      "r": round(r, 5) if r else None}
        all_s.extend(ss)
        all_d.extend(ds)
    r2, beta, alpha, r = r2_on_log_len(all_s, all_d)
    C["D4"]["pooled"] = {"r2": round(r2, 5), "beta_log_len": round(beta, 5),
                         "intercept": round(alpha, 5), "r": round(r, 5), "n": len(all_s)}
    # gap predicted by length alone
    Lp = statistics.median([len(s) for s in p_str])
    Lq = C["native"]["quran"]["median_syllables"]
    pred = {}
    for k, v in prose_native.items():
        Lr = statistics.median([len(s) for s in v["strings"]])
        obs_qp = med(q_d) - med(p_d)
        obs_rq = med(v["d"]) - med(q_d)
        pred[k] = {
            "obs_quran_minus_poetry": round(obs_qp, 5),
            "pred_quran_minus_poetry_from_length": round(beta * (math.log(Lq) - math.log(Lp)), 5),
            "frac_qp": round(beta * (math.log(Lq) - math.log(Lp)) / obs_qp, 4) if obs_qp else None,
            "obs_prose_minus_quran": round(obs_rq, 5),
            "pred_prose_minus_quran_from_length": round(beta * (math.log(Lr) - math.log(Lq)), 5),
            "frac_rq": round(beta * (math.log(Lr) - math.log(Lq)) / obs_rq, 4) if obs_rq else None,
        }
    C["D4"]["length_predicted_gaps"] = pred
    log("  D4 pooled R²(d_min ~ log L) = %.5f  (r=%+.4f, beta=%+.5f)  per-arm: %s"
        % (r2, r, beta, ", ".join("%s=%.3f" % (k, C["D4"][k]["r2"] or 0) for k, _ in arms)))
    for k, v in pred.items():
        log("     length alone predicts %.1f%% of the quran-poetry gap and %.1f%% of the "
            "%s-quran gap" % (100 * (v["frac_qp"] or 0), 100 * (v["frac_rq"] or 0), k))

    # ---- D5: length-stratified ordering -----------------------------------
    prose_all_s = [s for v in prose_native.values() for s in v["strings"]]
    pool = ([(len(s), "poetry", DCACHE[s][0]) for s in p_str] +
            [(len(s), "quran", DCACHE[s][0]) for s in q_str if len(s) >= 4] +
            [(len(s), "prose", DCACHE[s][0]) for s in prose_all_s])
    Ls = sorted(x[0] for x in pool)
    edges = [Ls[int(round(q * (len(Ls) - 1)))] for q in [i / 10 for i in range(11)]]
    bins = []
    for i in range(10):
        lo, hi = edges[i], edges[i + 1]
        sel = [x for x in pool if (lo <= x[0] < hi) or (i == 9 and x[0] == hi)]
        by = {a: [x[2] for x in sel if x[1] == a] for a in ("poetry", "quran", "prose")}
        usable = all(len(by[a]) >= MIN_BIN_PER_ARM for a in by)
        row = {"bin": i + 1, "L_lo": lo, "L_hi": hi,
               "n": {a: len(by[a]) for a in by}, "usable": usable}
        if usable:
            row["median"] = {a: round(med(by[a]), 5) for a in by}
            row["ordering_holds"] = (med(by["poetry"]) < med(by["quran"]) < med(by["prose"]))
        bins.append(row)
    us = [b for b in bins if b["usable"]]
    hold = sum(1 for b in us if b["ordering_holds"])
    C["D5"] = {"bins": bins, "n_usable": len(us), "n_holding": hold}
    log("  D5 usable length bins: %d/10   ordering holds in %d of them" % (len(us), hold))
    for b in us:
        log("     L[%d,%d) n=%s  medians=%s  ordering=%s"
            % (b["L_lo"], b["L_hi"], b["n"], b["median"], b["ordering_holds"]))

    # ---- D6: excess over matched noise (arrays built above, perms batched) ------
    exq, exp_ = ex["quran"], ex["poetry"]
    exr = {k: ex[k] for k in prose_native}
    d6a, p6a = perm_res[("D6a", None)]
    C["D6"] = {"median_excess": {"poetry": round(med(exp_), 5), "quran": round(med(exq), 5)},
               "mean_excess": {"poetry": round(statistics.mean(exp_), 5),
                               "quran": round(statistics.mean(exq), 5)},
               "frac_units_more_metrical_than_own_noise": {
                   "poetry": round(sum(1 for x in exp_ if x < 0) / len(exp_), 4),
                   "quran": round(sum(1 for x in exq if x < 0) / len(exq), 4)},
               "median_noise_floor": {
                   "poetry": round(med([DCACHE[n][0] for n in matched_noise(p_str, seed)
                                        if len(n) >= 4]), 5),
                   "quran": round(med([DCACHE[n][0] for n in matched_noise(q_str, seed)
                                       if len(n) >= 4]), 5)},
               "a_quran_gt_poetry": {"diff": round(d6a, 5), "p": round(p6a, 6),
                                     "direction_ok": d6a > 0,
                                     "PASS": d6a > 0 and p6a < ALPHA_BON},
               "b_prose_gt_quran": {}}
    for k, v in exr.items():
        C["D6"]["median_excess"][k] = round(med(v), 5)
        C["D6"]["mean_excess"][k] = round(statistics.mean(v), 5)
        C["D6"]["frac_units_more_metrical_than_own_noise"][k] = round(
            sum(1 for x in v if x < 0) / len(v), 4)
        C["D6"]["median_noise_floor"][k] = round(
            med([DCACHE[n][0] for n in matched_noise(prose_native[k]["strings"], seed)
                 if len(n) >= 4]), 5)
        d6b, p6b = perm_res[("D6b", k)]
        C["D6"]["b_prose_gt_quran"][k] = {"diff": round(d6b, 5), "p": round(p6b, 6),
                                          "direction_ok": d6b > 0,
                                          "PASS": d6b > 0 and p6b < ALPHA_BON}
    log("  D6 noise floor:  poetry=%.5f quran=%.5f %s"
        % (C["D6"]["median_noise_floor"]["poetry"], C["D6"]["median_noise_floor"]["quran"],
           " ".join("%s=%.5f" % (k, C["D6"]["median_noise_floor"][k]) for k in exr)))
    log("  D6 median excess over matched noise: poetry=%.5f quran=%.5f %s"
        % (med(exp_), med(exq), " ".join("%s=%.5f" % (k, med(v)) for k, v in exr.items())))
    log("     D6a quran>poetry diff=%+.5f p=%.5f PASS=%s | D6b %s"
        % (d6a, p6a, C["D6"]["a_quran_gt_poetry"]["PASS"],
           " ".join("%s diff=%+.5f p=%.5f PASS=%s" % (k, x["diff"], x["p"], x["PASS"])
                    for k, x in C["D6"]["b_prose_gt_quran"].items())))

    # ---- D8: Qurʾān self-recut (baseline-free) ---------------------------
    bayt_profile = [len(normalise_words(l)) for _, _, l in POET_LINES]
    sent_profile = [len(normalise_words(t)) for t in PROSE[0]["sentences"]]
    C["D8"] = {}
    for tgt, prof, native_target in (
            ("cut_to_prose_sentence_lengths", sent_profile, med(prose_native["darimi"]["d"])),
            ("cut_to_bayt_lengths", bayt_profile, med(p_d))):
        res = cyclic_partition_medians(QURAN_WORDS_D8, prof, 60, seed, mode,
                                       "%s/selfrecut-%s" % (name, tgt), n_sub=N_SUB)
        m = statistics.mean(res["medians"])
        span = native_target - Q
        moved = (m - Q) / span if abs(span) > 1e-12 else None
        C["D8"][tgt] = {"quran_native": round(Q, 5),
                        "quran_recut_mean": round(m, 5),
                        "quran_recut_min": round(min(res["medians"]), 5),
                        "quran_recut_max": round(max(res["medians"]), 5),
                        "target_native": round(native_target, 5),
                        "fraction_of_distance_moved": round(moved, 4) if moved is not None else None,
                        "median_units_per_draw": statistics.median(res["n_units"]),
                        "profile_median_words": statistics.median(prof)}
        log("  D8 %-32s quran %.5f -> %.5f  (target %.5f)  moved %.1f%% of the distance"
            % (tgt, Q, m, native_target, 100 * (moved or 0)))

    C["seconds"] = round(time.time() - t0, 1)
    return C


# ===========================================================================
# 6. VERDICT — a literal transcription of prereg §7.  Diffed in §7 below.
# ===========================================================================
def verdict_D1(cell):
    labels = {}
    for k, v in cell["D1"].items():
        if v["n_offsets_le_quran"] == 0 and v["perm_p"] < ALPHA_BON \
                and v["perm_diff_prose_minus_quran"] > 0:
            labels[k] = "SURVIVES"
        elif v["n_offsets_le_quran"] >= v["n_offsets"] / 2:
            labels[k] = "ARTEFACT"
        else:
            labels[k] = "ATTENUATED"
    overall = ("SURVIVES" if all(x == "SURVIVES" for x in labels.values())
               else ("ARTEFACT" if any(x == "ARTEFACT" for x in labels.values())
                     else "ATTENUATED"))
    return overall, labels


def verdict_D2(cell):
    v = cell["D2"]
    if cell["D7"]["partitioned_meter_acc"] is None or cell["D7"]["partitioned_meter_acc"] < 0.40:
        return "UNINTERPRETABLE"
    if v["n_draws_ge_quran"] == 0 and v["perm_p"] < ALPHA_BON \
            and v["perm_diff_quran_minus_poetry"] > 0:
        return "SURVIVES"
    if v["n_draws_ge_quran"] >= v["n_draws"] / 2:
        return "ARTEFACT"
    return "ATTENUATED"


def verdict_D4(cell):
    r2 = cell["D4"]["pooled"]["r2"]
    if r2 >= 0.50:
        return "NOT-LENGTH-INVARIANT"
    if r2 >= 0.20:
        return "PARTIALLY-LENGTH-DRIVEN"
    return "LENGTH-INVARIANT-IN-PRACTICE"


def verdict_D5(cell):
    n, h = cell["D5"]["n_usable"], cell["D5"]["n_holding"]
    if n < 3:
        return "NON-OVERLAPPING-SUPPORT"
    if h >= 2 * n / 3:
        return "STRATIFIED-SURVIVES"
    if h < n / 2:
        return "STRATIFIED-FAILS"
    return "MIXED"


def verdict_D6(cells):
    ok = all(c["D6"]["a_quran_gt_poetry"]["PASS"] and
             all(x["PASS"] for x in c["D6"]["b_prose_gt_quran"].values())
             for c in cells)
    fails = []
    for c in cells:
        if not c["D6"]["a_quran_gt_poetry"]["PASS"]:
            fails.append("%s:a_quran_gt_poetry" % c["cell"])
        for k, x in c["D6"]["b_prose_gt_quran"].items():
            if not x["PASS"]:
                fails.append("%s:b_prose_gt_%s" % (c["cell"], k))
    return ("EXCESS-SURVIVES" if ok else "EXCESS-FAILS"), fails


def verdict_D7(cell):
    a = cell["D7"]["partitioned_meter_acc"]
    return "CONTROL-HOLDS" if (a is not None and a >= 0.40) else "CONTROL-FAILS"


def verdict_D8(cell):
    fr = [abs(v["fraction_of_distance_moved"] or 0.0) for v in cell["D8"].values()]
    if any(f >= 0.50 for f in fr):
        return "SELF-RECUT-CONFIRMS-LENGTH"
    if all(f <= 0.10 for f in fr):
        return "SELF-RECUT-REFUTES-LENGTH"
    return "PARTIAL"


# ===========================================================================
# 7. MAIN
# ===========================================================================
def main():
    global _POOL, N_OFF_FULL, N_DRAW_FULL, N_OFF_SENS, N_SUB, PERM_N, IDENTITY_GATE_N
    t_start = time.time()
    smoke = "--smoke" in sys.argv
    if smoke:
        # calibration run only — writes to runs/h-new-2730-SMOKE/, never deleted
        N_OFF_FULL = N_DRAW_FULL = 6
        N_OFF_SENS = 4
        N_SUB = 60
        PERM_N = 200
        IDENTITY_GATE_N = 200
        log("[SMOKE] reduced parameters — calibration only, not a result")

    # identity gate (prereg §3.2): 1500 units across all four corpora
    rng = random.Random(SEED)
    gate_pool = []
    for mode in ("P_forceheavy", "P_pausal"):
        gate_pool += [scan(t, mode) for t in rng.sample(QVERSE_TEXT, 300)]
        gate_pool += [scan(l, mode) for _, _, l in rng.sample(POET_LINES, 120)]
        for pr in PROSE:
            gate_pool += [scan(t, mode) for t in rng.sample(pr["sentences"], 165)]
    gate_pool = [s for s in gate_pool if len(s) >= 4][:IDENTITY_GATE_N]
    log("\n[gate] dmin_fast identity check on %d units..." % len(gate_pool))
    gate_identity(gate_pool)

    try:
        import multiprocessing as mp
        _POOL = mp.get_context("fork").Pool(os.cpu_count())
        log("[perf] multiprocessing pool: %d workers" % os.cpu_count())
    except Exception as e:                                  # pragma: no cover
        log("[perf] pool unavailable (%s) — single process" % e)
        _POOL = None

    CELLS = []
    CELLS.append(run_cell("PRIMARY", "P_forceheavy", "W_2680",
                          N_OFF_FULL, N_DRAW_FULL, SEED, full=True))
    CELLS.append(run_cell("TUPLE_SENS", "P_pausal", "W_2680",
                          N_OFF_FULL, N_DRAW_FULL, SEED, full=True))
    CELLS.append(run_cell("PROFILE_SENS", "P_forceheavy", "W_lex",
                          N_OFF_SENS, N_OFF_SENS, SEED, full=False))
    CELLS.append(run_cell("REPLICATION_forceheavy", "P_forceheavy", "W_2680",
                          N_OFF_SENS, N_OFF_SENS, SEED_REPL, full=False))
    CELLS.append(run_cell("REPLICATION_pausal", "P_pausal", "W_2680",
                          N_OFF_SENS, N_OFF_SENS, SEED_REPL, full=False))

    if _POOL is not None:
        _POOL.close()
        _POOL.join()
        _POOL = None

    by = {c["cell"]: c for c in CELLS}
    prim, tsens = by["PRIMARY"], by["TUPLE_SENS"]
    full_cells = [prim, tsens]

    V = {}
    for c in CELLS:
        d1, d1l = verdict_D1(c)
        V[c["cell"]] = {"D1": d1, "D1_per_corpus": d1l, "D2": verdict_D2(c),
                        "D7": verdict_D7(c)}
        if c["full_arms"]:
            V[c["cell"]].update({"D4": verdict_D4(c), "D5": verdict_D5(c),
                                 "D8": verdict_D8(c)})
    d6, d6_fails = verdict_D6(full_cells)
    V["D6"] = {"label": d6, "failing_arms": d6_fails}

    # D3 — prereg §7: ordering survives iff D1 and D2 both SURVIVE in PRIMARY and TUPLE_SENS
    d3 = ("ORDERING-SURVIVES"
          if all(V[c]["D1"] == "SURVIVES" and V[c]["D2"] == "SURVIVES"
                 for c in ("PRIMARY", "TUPLE_SENS"))
          else "ORDERING-DOES-NOT-SURVIVE")
    V["D3"] = d3

    profile_fragile = (V["PRIMARY"]["D1"] != V["PROFILE_SENS"]["D1"] or
                       V["PRIMARY"]["D2"] != V["PROFILE_SENS"]["D2"])
    tuple_fragile = (V["PRIMARY"]["D1"] != V["TUPLE_SENS"]["D1"] or
                     V["PRIMARY"]["D2"] != V["TUPLE_SENS"]["D2"])

    # §7.1 overall
    if d3 == "ORDERING-SURVIVES" and d6 == "EXCESS-SURVIVES" \
            and V["PRIMARY"]["D4"] != "NOT-LENGTH-INVARIANT":
        overall = "DISCRIMINATES"
    elif V["PRIMARY"]["D1"] == "ARTEFACT" or \
            (V["PRIMARY"]["D4"] == "NOT-LENGTH-INVARIANT"
             and V["PRIMARY"]["D8"] == "SELF-RECUT-CONFIRMS-LENGTH"):
        overall = "ARTEFACT-OF-UNIT-LENGTH"
    else:
        overall = "ATTENUATED"
    prefix = ("PROFILE-FRAGILE " if profile_fragile else "") + \
             ("RULES-TUPLE-FRAGILE " if tuple_fragile else "")
    VERDICT = (prefix + overall).strip()
    V["profile_fragile"] = profile_fragile
    V["rules_tuple_fragile"] = tuple_fragile
    V["overall"] = VERDICT

    log("\n" + "=" * 78)
    log("VERDICT SUMMARY (decision rules transcribed from prereg §7)")
    log("=" * 78)
    for c in CELLS:
        log("  %-24s D1=%-11s %-46s D2=%-15s D7=%s"
            % (c["cell"], V[c["cell"]]["D1"], V[c["cell"]]["D1_per_corpus"],
               V[c["cell"]]["D2"], V[c["cell"]]["D7"]))
    log("  D3 ordering : %s" % d3)
    log("  D4 (primary): %s  pooled R²=%.5f" % (V["PRIMARY"]["D4"], prim["D4"]["pooled"]["r2"]))
    log("  D5 (primary): %s" % V["PRIMARY"]["D5"])
    log("  D6          : %s  %s" % (d6, d6_fails))
    log("  D8 (primary): %s" % V["PRIMARY"]["D8"])
    log("  OVERALL     : %s" % VERDICT)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    RUN = os.path.join(ROOT, "runs", "h-new-2730-SMOKE" if smoke else "h-new-2730", stamp)
    if os.path.exists(RUN):
        die("run dir exists (immutability): %s" % RUN)
    os.makedirs(RUN)

    out = {
        "id": "H-NEW-2730",
        "title": "Genre control on H-NEW-2690's scansion ordering — matched partition, "
                 "length-invariance, and the three-way ordering",
        "parent": "H-NEW-2690", "method_parent": ["H-NEW-2680", "H-NEW-2720"],
        "prereg_sha256": PREREG_SHA256,
        "seeds": {"primary": SEED, "replication": SEED_REPL},
        "n_perm": N_PERM, "bonferroni_k": BONF_K, "alpha_bonferroni": ALPHA_BON,
        "n_offsets_full": N_OFF_FULL, "n_offsets_sens": N_OFF_SENS, "n_sub": N_SUB,
        "corpora": {
            "quran_verses": len(QVERSE_TEXT),
            "poetry_abyat": len(POET_LINES), "poetry_voc_words": len(POETRY_TOKENS),
            "partition_requires_words": {k: sum(v) for k, v in PROFILES.items()},
            "prose": {p["label"]: {"n_hadith": p["n_hadith"], "voc_words": p["n_voc"],
                                   "quran_quote_words_dropped": p["dropped"],
                                   "stream_words": len(p["stream"]),
                                   "native_sentences": len(p["sentences"])}
                      for p in PROSE},
            "untestable": {"jahiz-hayawan.txt": "diacritic ratio 0.000 — unscannable",
                           "bukhari-noquran.txt": "diacritic ratio 0.000 — unscannable",
                           "diwan-*.txt": "diacritic ratio 0.000 — unscannable"},
        },
        "gates": {"prereg_sha": True, "frozen_inputs": len(FROZEN),
                  "scanner_lift_2690": _EXPECT_2690,
                  "partition_lift_2680": _EXPECT_2680,
                  "tokeniser_equivalence": "PASSED (token-for-token vs normalise_words)",
                  "cyclic_partition_equivalence": "PASSED (== build_pseudo_corpus)",
                  "dmin_fast_identity": "PASSED on %d units, 4 corpora" % len(gate_pool)},
        "cells": CELLS,
        "verdicts": V,
        "verdict": VERDICT,
        "wall_seconds": round(time.time() - t_start, 1),
    }
    json.dump(out, open(os.path.join(RUN, "result.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    json.dump({"id": "H-NEW-2730", "utc": stamp,
               "script": "findings/phase-b-hypotheses/scripts/h-new-2730.py",
               "script_sha256": sha256_file(os.path.abspath(__file__)),
               "prereg": PREREG_REL, "prereg_sha256": PREREG_SHA256,
               "inputs_sha256": dict(sorted(FROZEN.items())),
               "lifted_fragments": {"h-new-2690": _EXPECT_2690, "h-new-2680": _EXPECT_2680},
               "python": platform.python_version(),
               "seeds": [SEED, SEED_REPL], "n_perm": N_PERM,
               "verdict": VERDICT,
               "immutability": "Immutable. Never delete or overwrite, per prereg §8."},
              open(os.path.join(RUN, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    if not smoke:
        json.dump(out, open(os.path.join(CSVDIR, "h-new-2730.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
    log("\n[run] %s" % os.path.relpath(RUN, REPO))
    log("[wall] %.1f s" % (time.time() - t_start))


if __name__ == "__main__":
    main()
