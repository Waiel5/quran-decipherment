#!/usr/bin/env python3
"""
H-NEW-2890 — the vocalised-prose negative control that H-NEW-2870 and H-NEW-2880 reported
as NOT COMPUTABLE.

Both parents censused data/baseline-corpora/ only and concluded no vocalised Arabic prose
existed on disk. A repository-wide census found data/literature/hadith/ahmedbaset-json/ --
50,884 fully vocalised hadith, at harakat densities of 0.77-0.88 against the Qur'an's own
0.78. The control can be run, and this runs it.

The instrument is H-NEW-2880's, unmodified and SHA-pinned: phonemiser, the four conventions,
both rime extractors, the readability criterion, and the exact zero-variance-floor null. No
parameter is re-tuned for prose.

Pre-registration locked at
  findings/phase-b-hypotheses/prereg-h-new-2890-prose-control.md
  SHA-256 8d5a8af94a49b901e5109a658c22d7f4dce1edf70e9766a1b92b5646bb5a6aec
verified at runtime. Reporting order locked by prereg §9.

Waiel Al-Shujaa, 2026-08-07.
"""
import hashlib
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

PREREG = "findings/phase-b-hypotheses/prereg-h-new-2890-prose-control.md"
PREREG_SHA256 = "8d5a8af94a49b901e5109a658c22d7f4dce1edf70e9766a1b92b5646bb5a6aec"
PARENT = "findings/phase-b-hypotheses/scripts/h-new-2880.py"

HADITH_DIR = "data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books"
FROZEN = {
    PARENT: "c9577870b2a4bc3451344031f46f192795534af0ef56f4f46be57f07db7c7074",
    f"{HADITH_DIR}/bukhari.json":
        "9d2e4194786c275f64f627c834711ea0e339a8fe226d5e9569ef962595a562f1",
    f"{HADITH_DIR}/muslim.json":
        "12e3cbe8e2c83acc787b3e1e644877eff0feab11f1b32493386c60703d9076ae",
}
# all nine are reported (prereg §3.1); only the two primary texts are SHA-frozen as inputs
ALL_BOOKS = ["bukhari", "muslim", "abudawud", "tirmidhi", "nasai", "ibnmajah",
             "malik", "ahmed", "darimi"]
PRIMARY_TEXTS = ["bukhari", "muslim"]

SEED, SEED_REP = 20260509, 20260519
N_PERM = 10000
N_PROSE_CUT = 200
BONFERRONI_K = 36
ALPHA = 0.05 / BONFERRONI_K

# prereg §3.1 -- inherited verbatim from H-NEW-2870 §6.4
VOC_THRESHOLD = 0.90
# prereg §7 -- the parents' PUBLISHED values, fixed before any prose number
QURAN_DELTA_P1 = 0.18686703691604045
QURAN_DELTA_P2 = 0.1880104540999673
QURAN_RECUT_DELTA_P1 = 0.0284
QURAN_Z_P1 = 15.03
DAMAGE_HALF = 0.5 * QURAN_DELTA_P1        # 0.09343
DAMAGE_QUARTER = 0.25 * QURAN_DELTA_P1    # 0.04672

STRIP_SETTINGS = ["S5", "S3", "S0"]

SMOKE = "--smoke" in sys.argv
if SMOKE:
    N_PERM, N_PROSE_CUT = 200, 5

CHECKPOINT_DIR = os.path.join("scratch", "h-new-2890-checkpoints")   # OUTSIDE the run dir
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


_ck = [0]


def checkpoint(tag, obj):
    if SMOKE:
        return
    os.makedirs(CHECKPOINT_DIR, exist_ok=True)
    _ck[0] += 1
    p = os.path.join(CHECKPOINT_DIR, f"snapshot-{_ck[0]:03d}-{tag}.json")
    if os.path.exists(p):
        return
    with open(p, "x", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, default=float)


# ---------------------------------------------------------------- 0. SHA gates
_a = sha256_file(PREREG)
if _a != PREREG_SHA256:
    die(f"pre-reg SHA mismatch\n  expected {PREREG_SHA256}\n  actual   {_a}")
say(f"[SHA-OK] pre-reg locked: {_a}")
for p, want in FROZEN.items():
    g = sha256_file(p)
    if g != want:
        die(f"frozen input mismatch {p}\n  expected {want}\n  actual {g}")
say(f"[SHA-OK] {len(FROZEN)} frozen inputs verified (the parent runner among them)")

# ---------------------------------------------------------------- 1. instrument
say("\n" + "=" * 78)
say("INSTRUMENT — H-NEW-2880's machinery, loaded unmodified (prereg §4).")
say("It re-verifies its own pre-reg and frozen inputs, and re-runs Gates A and B.")
say("=" * 78)
_src = open(PARENT, encoding="utf-8").read()
_cut = _src.index("# ---------------------------------------------------------------- 4. ANTI-GAMING AUDIT")
NS = {"__name__": "instrument-2880", "__file__": PARENT}
_argv = sys.argv
sys.argv = [_argv[0], "--smoke"]     # machinery only; the parent writes nothing
_buf = []


class _Tee:
    def __init__(self, real):
        self.real = real

    def write(self, s):
        self.real.write(s)
        _buf.append(s)

    def flush(self):
        self.real.flush()


_old = sys.stdout
sys.stdout = _Tee(_old)
try:
    exec(compile(_src[:_cut], "h-new-2880-machinery", "exec"), NS)
finally:
    sys.stdout = _old
    sys.argv = _argv
LOG.extend("".join(_buf).rstrip("\n").split("\n"))

SURAHS = NS["SURAHS"]
LENS = NS["LENS"]
INNER = NS["NS"]                       # the H-NEW-2870 namespace, one level down
apply_convention, phonemes = INNER["apply_convention"], INNER["phonemes"]
PUNCT = INNER["PUNCT"]
floor_of = NS["floor_of"]
set_variant = NS["set_variant"]        # the parent's own; it targets the right namespace
QAGREE, QDELTA = NS["AGREE"], NS["DELTA"]
CONVS = ["C", "P1", "P2", "P3"]

if abs(QDELTA["R2"]["P1"] - QURAN_DELTA_P1) > 1e-9:
    die("the Qur'an delta recomputed here differs from the value locked in prereg §7")
say(f"[OK] Qur'an Δ(P1) recomputed = {QDELTA['R2']['P1']:.6f}, matches the locked target")


def arabic_words(t):
    return [w for w in t.split() if any("ء" <= c <= "ي" for c in w)]


# ---------------------------------------------------------------- 2. load prose
say("\n" + "=" * 78)
say("RESULT 1 — THE ACQUISITION (prereg §9 step 1), and the defect in the parents")
say("=" * 78)
say("   H-NEW-2870 §6.2 and H-NEW-2880 §5.2 both report NO vocalised Arabic prose on disk.")
say("   Both censused data/baseline-corpora/ ONLY. This corpus has been committed since")
say("   2026-04-28 at data/literature/hadith/ahmedbaset-json/. The parents' conclusion that")
say("   the control could not be run was wrong; their prose NUMBERS are unaffected, because")
say("   the baseline-corpora files really do carry zero harakat.")
say("   Source manifest, licence position and SHA-256: data/literature/hadith/VOCALISED-HADITH-SOURCE.md")

HARAKAT = set("ًٌٍَُِّْٰ")
SUP_ALEF = "ٰ"
SH, TN, SK = set("َُِ"), set("ًٌٍٖٗٞ"), set("ْۡ")


def final_word_of(t):
    toks = arabic_words(t)
    if not toks:
        return ""
    return "".join(c for c in toks[-1] if c not in PUNCT)


def lastmark(w):
    for ch in reversed(w):
        if ch in TN:
            return "tanwin"
        if ch in SH:
            return "short-vowel"
        if ch in SK:
            return "sukun"
        if "ء" <= ch <= "ي" or ch == SUP_ALEF:
            return "bare"
    return "none"


def skel_words(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(c for c in t if c not in HARAKAT and c not in PUNCT)
    t = t.replace("ٱ", "ا").replace("آ", "ا").replace("أ", "ا")
    t = t.replace("إ", "ا").replace("ى", "ي").replace("ة", "ه")
    t = re.sub(r"[ؐ-ؚۖ-ۭـ]", "", t)
    return arabic_words(t)


QVERSES = [t for _, _, _, vs in SURAHS for t in vs]
QGRAM = {}
for n in (3, 5):
    g = set()
    for v in QVERSES:
        w = skel_words(v)
        for i in range(len(w) - n + 1):
            g.add(" ".join(w[i:i + n]))
    QGRAM[n] = g
say(f"\n   Qur'anic skeleton n-gram types: trigram {len(QGRAM[3])}, 5-gram {len(QGRAM[5])}")

BOOKS = {}
say("\n   VOCALISATION SCREEN (prereg §3.1) — threshold >= 0.90 inherited from H-NEW-2870 §6.4")
say(f"   {'book':11s} {'units':>7s} {'chapters':>9s} {'har/char':>9s} "
    f"{'UNIT-FINAL VOC':>15s} {'mean_len':>9s} {'contam3':>8s} {'contam5':>8s} {'admit':>6s}")
for key in ALL_BOOKS:
    d = json.load(open(os.path.join(HADITH_DIR, key + ".json"), encoding="utf-8"))
    recs = [h for h in d["hadiths"] if h.get("arabic") and arabic_words(h["arabic"])]
    txts = [h["arabic"] for h in recs]
    full = "\n".join(txts)
    ar = sum(1 for c in full if "ء" <= c <= "ي")
    hk = sum(1 for c in full if c in HARAKAT)
    marks = Counter(lastmark(final_word_of(t)) for t in txts)
    n = len(txts)
    voc = (marks["short-vowel"] + marks["tanwin"] + marks["bare"]) / n
    lens = [len(arabic_words(t)) for t in txts]
    c3 = c5 = 0
    contam = []
    for t in txts:
        w = skel_words(t)
        g3 = {" ".join(w[i:i + 3]) for i in range(len(w) - 2)}
        g5 = {" ".join(w[i:i + 5]) for i in range(len(w) - 4)}
        h3, h5 = bool(g3 & QGRAM[3]), bool(g5 & QGRAM[5])
        contam.append((h3, h5))
        c3 += h3
        c5 += h5
    admit = voc >= VOC_THRESHOLD
    BOOKS[key] = {"records": recs, "texts": txts, "contam": contam,
                  "chapters": [h["chapterId"] for h in recs],
                  "n": n, "density": hk / ar, "unit_final_vocalised": voc,
                  "mean_len": sum(lens) / n, "words": sum(lens),
                  "contam3": c3 / n, "contam5": c5 / n, "admissible": bool(admit),
                  "marks": dict(marks), "n_chapters": len(set(h["chapterId"] for h in recs))}
    b = BOOKS[key]
    say(f"   {key:11s} {n:7d} {b['n_chapters']:9d} {hk / ar:9.4f} {voc:15.4f} "
        f"{b['mean_len']:9.1f} {100 * c3 / n:7.1f}% {100 * c5 / n:7.1f}% "
        f"{'PASS' if admit else 'FAIL':>6s}")
say(f"   {'QURAN':11s} {len(QVERSES):7d} {len(SURAHS):9d} {'0.7801':>9s} {'0.9843':>15s} "
    f"{'12.4':>9s} {'-':>8s} {'-':>8s} {'-':>6s}")
admissible = [k for k in ALL_BOOKS if BOOKS[k]["admissible"]]
say(f"   admissible: {len(admissible)}/9 — {', '.join(admissible)}")
if not admissible:
    die("no text clears prereg §3.1 — CONTROL UNAVAILABLE (prereg §8)")
checkpoint("acquisition", {k: {kk: vv for kk, vv in v.items()
                              if kk not in ("records", "texts", "contam", "chapters")}
                           for k, v in BOOKS.items()})


# ---------------------------------------------------------------- 3. prose analysis
def strip_mask(book, setting):
    """prereg §5.3."""
    c = BOOKS[book]["contam"]
    if setting == "S0":
        return [True] * len(c)
    if setting == "S5":
        return [not h5 for (h3, h5) in c]
    return [not h3 for (h3, h5) in c]


def prose_arm_B(book, setting, variant):
    """prereg §5.1 — composed boundaries: unit = one hadith, block = one chapter."""
    set_variant(variant)
    rime_of, readable_of = INNER["rime_of"], INNER["readable_of"]
    keep = strip_mask(book, setting)
    txts = [t for t, k in zip(BOOKS[book]["texts"], keep) if k]
    chaps = [c for c, k in zip(BOOKS[book]["chapters"], keep) if k]
    lab = {c: [rime_of(t, c) for t in txts] for c in CONVS}
    rd = [readable_of(t) for t in txts]
    pairs = [i for i in range(len(txts) - 1) if chaps[i] == chaps[i + 1]]
    keepr = [i for i in pairs if rd[i] and rd[i + 1]]
    out = {"n_units": len(txts), "n_pairs": len(pairs), "n_pairs_readable": len(keepr),
           "readable_share": sum(rd) / len(rd), "n_dropped": len(keep) - len(txts)}
    for tag, ps in (("all", pairs), ("readable", keepr)):
        A = {c: (sum(1 for i in ps if lab[c][i] == lab[c][i + 1]) / len(ps)) if ps else float("nan")
             for c in CONVS}
        out[f"A_{tag}"] = A
        out[f"delta_{tag}"] = {p: A[p] - A["C"] for p in ("P1", "P2", "P3")}
    out["K"] = {c: len(set(lab[c])) for c in CONVS}
    out["floor"] = {c: floor_of(Counter(lab[c]).values()) for c in CONVS}
    out["K_eff"] = {}
    for c in CONVS:
        n = len(lab[c])
        h = -sum((v / n) * math.log(v / n) for v in Counter(lab[c]).values())
        out["K_eff"][c] = math.exp(h)
    return out, lab, pairs, keepr


def prose_arm_A(book, setting, variant, seed, n_cut):
    """prereg §5.2 — the parent's length-matched cut construction."""
    set_variant(variant)
    rime = INNER["rime"]
    keep = strip_mask(book, setting)
    words = [w for t, k in zip(BOOKS[book]["texts"], keep) if k for w in arabic_words(t)]
    cache = {}

    def rw(w, conv):
        k = (w, conv)
        r = cache.get(k)
        if r is None:
            r = rime(apply_convention(phonemes("".join(c for c in w if c not in PUNCT)), conv))
            cache[k] = r
        return r

    rng = random.Random(seed)
    prof = [LENS[sid] for sid, _, _, _ in SURAHS]
    vals = {p: [] for p in ("P1", "P2")}
    for _ in range(n_cut):
        off = rng.randrange(0, max(len(words) - 100000, 1))
        pos = off
        ac = {p: 0 for p in ("P1", "P2")}
        agc = tot = 0
        for lens in prof:
            fins = []
            for L in lens:
                pos += L
                if pos - 1 >= len(words):
                    pos = off
                fins.append(pos - 1)
            for i in range(len(fins) - 1):
                a, b = words[fins[i]], words[fins[i + 1]]
                agc += rw(a, "C") == rw(b, "C")
                for p in ("P1", "P2"):
                    ac[p] += rw(a, p) == rw(b, p)
                tot += 1
        for p in ("P1", "P2"):
            vals[p].append(ac[p] / tot - agc / tot)
    return {p: {"mean": sum(v) / len(v), "min": min(v), "max": max(v),
                "sd": math.sqrt(sum((x - sum(v) / len(v)) ** 2 for x in v) / len(v)),
                "n_cut": n_cut} for p, v in vals.items()}


say("\n" + "=" * 78)
say("RESULT 2 — CLASS-COLLAPSE MAGNITUDE FOR PROSE, reported before any delta (prereg §9.3)")
say("=" * 78)
ARMB, ARMA = {}, {}
for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        r, lab, pairs, keepr = prose_arm_B(book, setting, "R2")
        ARMB[f"{book}_{setting}_R2"] = r
        if setting == "S5":
            say(f"\n   {book} [{setting}] units={r['n_units']} "
                f"(dropped {r['n_dropped']}), within-chapter pairs={r['n_pairs']}, "
                f"readable pairs={r['n_pairs_readable']} "
                f"({r['n_pairs_readable'] / max(r['n_pairs'], 1):.3f})")
            for c in CONVS:
                say(f"      {c:3s} K={r['K'][c]:5d}  K_eff={r['K_eff'][c]:8.3f}  "
                    f"floor={r['floor'][c]:.6f}  A={r['A_readable'][c]:.4f}")
            say(f"      collapse C->P1: K {r['K']['C']}/{r['K']['P1']} = "
                f"{r['K']['C'] / r['K']['P1']:.3f}x   free arithmetic gain = "
                f"{r['floor']['P1'] - r['floor']['C']:+.4f}")
say(f"\n   [Qur'an, for reference: K 397->116 = 3.422x, floor 0.1068->0.1687, "
    f"free gain +0.0619, Δ = {QURAN_DELTA_P1:+.4f}]")

say("\n" + "=" * 78)
say("RESULT 3 — ARM B: COMPOSED BOUNDARIES. PRIMARY. (prereg §5.1)")
say(f"Locked comparison target: the Qur'an's own Δ(P1) = {QURAN_DELTA_P1:+.4f}")
say(f"Locked damage thresholds: >= {DAMAGE_HALF:+.5f} = COMPARABLE; "
    f">= {DAMAGE_QUARTER:+.5f} = PARTIAL")
say("=" * 78)
for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        r = ARMB[f"{book}_{setting}_R2"]
        say(f"   {book:9s} [{setting}] readable pairs n={r['n_pairs_readable']:5d}  "
            f"A(C)={r['A_readable']['C']:.4f}  A(P1)={r['A_readable']['P1']:.4f}  "
            f"Δ(P1)={r['delta_readable']['P1']:+.4f}  Δ(P2)={r['delta_readable']['P2']:+.4f}"
            f"   [all pairs: Δ(P1)={r['delta_all']['P1']:+.4f}]")
checkpoint("armB", ARMB)

say("\n" + "=" * 78)
say("RESULT 4 — ARM A: LENGTH-MATCHED CUTS (prereg §5.2)")
say(f"Locked comparison target: the Qur'an's own pseudo-fāṣila re-cut Δ = "
    f"{QURAN_RECUT_DELTA_P1:+.4f} (arbitrary cuts against arbitrary cuts)")
say("=" * 78)
for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        a = prose_arm_A(book, setting, "R2", SEED, N_PROSE_CUT)
        ARMA[f"{book}_{setting}_R2"] = a
        say(f"   {book:9s} [{setting}] {N_PROSE_CUT} matched cuts:  "
            f"Δ(P1) mean={a['P1']['mean']:+.4f} sd={a['P1']['sd']:.4f} "
            f"max={a['P1']['max']:+.4f}   Δ(P2) mean={a['P2']['mean']:+.4f}")
checkpoint("armA", ARMA)

# ---------------------------------------------------------------- 4. the tests
say("\n" + "=" * 78)
say("RESULT 5 — THE REGISTERED TESTS (prereg §8)")
say("=" * 78)


def label_exchange(dq, dp, seed, n_perm):
    """D-P1 / D-P2: is the Qur'an's per-pair gain larger than prose's? Same machinery the
    parents used for D4b."""
    dq = np.asarray(dq, dtype=np.float64)
    dp = np.asarray(dp, dtype=np.float64)
    obs = float(dq.mean() - dp.mean())
    allv = np.concatenate([dq, dp])
    nq, tot = len(dq), len(dq) + len(dp)
    rng = np.random.default_rng(seed)
    ge = 0
    for _ in range(n_perm):
        s = allv[rng.permutation(tot)]
        if s[:nq].mean() - s[nq:].mean() >= obs:
            ge += 1
    return obs, (1 + ge) / (1 + n_perm)


# the Qur'an's own per-pair gain vectors, from the pinned instrument
QLAB = NS["LABS"]["R2"]
QPAIRS = NS["PAIRS"]
QGAIN = {p: np.array([(QLAB[p][sid][i] == QLAB[p][sid][i + 1])
                      - (QLAB["C"][sid][i] == QLAB["C"][sid][i + 1])
                      for sid, i in QPAIRS], dtype=np.float64) for p in ("P1", "P2")}

TESTS = {}
for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        r, lab, pairs, keepr = prose_arm_B(book, setting, "R2")
        for p in ("P1", "P2"):
            pg = np.array([(lab[p][i] == lab[p][i + 1]) - (lab["C"][i] == lab["C"][i + 1])
                           for i in keepr], dtype=np.float64)
            o, pv = label_exchange(QGAIN[p], pg, SEED, N_PERM)
            _, pv2 = label_exchange(QGAIN[p], pg, SEED_REP, N_PERM)
            TESTS[f"DP1_{book}_{setting}_{p}"] = {
                "obs_diff": o, "p": pv, "p_replication": pv2,
                "delta_prose": float(pg.mean()), "delta_quran": float(QGAIN[p].mean()),
                "pass": pv < ALPHA}
            say(f"   D-P1 {book:9s} [{setting}] {p}: Δ_Qurʾān({QGAIN[p].mean():+.4f}) − "
                f"Δ_prose({pg.mean():+.4f}) = {o:+.4f}  p={pv:.5f} (rep {pv2:.5f})  "
                f"{'PASS' if pv < ALPHA else 'FAIL'}")

say("")
for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        a = ARMA[f"{book}_{setting}_R2"]
        for p in ("P1", "P2"):
            TESTS[f"DP2_{book}_{setting}_{p}"] = {
                "prose_recut_mean": a[p]["mean"], "prose_recut_max": a[p]["max"],
                "quran_recut": QURAN_RECUT_DELTA_P1,
                "prose_below_quran_recut": bool(a[p]["mean"] <= QURAN_RECUT_DELTA_P1)}
            say(f"   D-P2 {book:9s} [{setting}] {p}: prose matched-cut Δ={a[p]['mean']:+.4f} "
                f"vs the Qurʾān's own re-cut Δ={QURAN_RECUT_DELTA_P1:+.4f}  -> "
                f"{'prose <= Qurʾān re-cut' if a[p]['mean'] <= QURAN_RECUT_DELTA_P1 else 'prose ABOVE'}")

say("\n   D-P3 — prose against ITS OWN exact zero-variance-floor null (prereg §6).")
say("   NOTE, locked in prereg §7: z is NOT comparable across corpora of different size and")
say("   class structure. Δ is the primary comparison; this is secondary and descriptive.")


class ProseTuple:
    """The 2880 exact-null machinery, re-pointed at a prose partition."""

    def __init__(self, lab, pairs, conv):
        cit = sorted(set(lab["C"]))
        self.CIDX = {t: i for i, t in enumerate(cit)}
        self.M = len(cit)
        size = [0] * self.M
        for t in lab["C"]:
            size[self.CIDX[t]] += 1
        self.SIZE = size
        self.SIZE_A = np.asarray(size, dtype=np.float64)
        self.N = len(lab["C"])
        blocks = sorted(set(lab[conv]))
        BIDX = {b: i for i, b in enumerate(blocks)}
        self.K = len(blocks)
        amap = {}
        self.coarsening = True
        for ct, pt in zip(lab["C"], lab[conv]):
            j = self.CIDX[ct]
            if j in amap and amap[j] != BIDX[pt]:
                self.coarsening = False
            amap[j] = BIDX[pt]
        self.OBS = np.array([amap[i] for i in range(self.M)], dtype=np.int32)
        self.tgt = np.bincount(self.OBS, weights=self.SIZE_A, minlength=self.K).astype(np.int64)
        self.tgt_sorted = np.sort(self.tgt)[::-1]
        self.floor_obs = float(sum((s / self.N) ** 2
                                   for s in sorted((int(x) for x in self.tgt), reverse=True)))
        self.PA = np.array([self.CIDX[lab["C"][i]] for i in pairs], dtype=np.int32)
        self.PB = np.array([self.CIDX[lab["C"][i + 1]] for i in pairs], dtype=np.int32)
        self.n_pairs = len(pairs)
        self.A_obs = float(np.count_nonzero(self.OBS[self.PA] == self.OBS[self.PB])) / self.n_pairs
        self.E_obs = self.A_obs - self.floor_obs
        groups = defaultdict(list)
        for ti, s in enumerate(size):
            groups[s].append(ti)
        self.SIZE_GROUPS = [groups[s] for s in sorted(groups, reverse=True)]


def prose_exact_null(T, seed, n_perm):
    rng = random.Random(seed)
    A, FL = [], []
    redraw = 0
    for _ in range(n_perm):
        for _try in range(50):
            rem = T.tgt.copy()
            blk = np.empty(T.M, dtype=np.int32)
            for grp in T.SIZE_GROUPS:
                g = grp if len(grp) == 1 else rng.sample(grp, len(grp))
                for t in g:
                    s = T.SIZE[t]
                    w = np.where(rem >= s, rem, 0)
                    tot = int(w.sum())
                    if tot > 0:
                        cw = np.cumsum(w)
                        k = int(np.searchsorted(cw, rng.random() * tot, side="right"))
                        if k >= T.K:
                            k = T.K - 1
                    else:
                        k = int(rem.argmax())
                    blk[t] = k
                    rem[k] -= s
            ach = np.bincount(blk, weights=T.SIZE_A, minlength=T.K).astype(np.int64)
            if np.array_equal(np.sort(ach)[::-1], T.tgt_sorted):
                break
            redraw += 1
        else:
            die("prose exact null: 50 consecutive draws failed exactness (prereg §11)")
        A.append(float(np.count_nonzero(blk[T.PA] == blk[T.PB])) / T.n_pairs)
        FL.append(float(sum((s / T.N) ** 2
                            for s in sorted((int(x) for x in ach), reverse=True))))
    A = np.asarray(A)
    FL = np.asarray(FL)
    E = A - FL
    return {"observed_A": T.A_obs, "observed_E": T.E_obs, "observed_floor": T.floor_obs,
            "null_E_mean": float(E.mean()), "null_E_sd": float(E.std()),
            "null_E_max": float(E.max()), "null_A_mean": float(A.mean()),
            "n_ge_observed_E": int((E >= T.E_obs - 1e-15).sum()),
            "p_E": (1 + int((E >= T.E_obs - 1e-15).sum())) / (1 + n_perm),
            "z_E": float((T.E_obs - E.mean()) / E.std()) if E.std() > 0 else float("nan"),
            "null_floor_max_abs_dev": float(np.abs(FL - T.floor_obs).max()),
            "redraws": redraw, "K": T.K, "M": T.M, "n_pairs": T.n_pairs}


for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        r, lab, pairs, keepr = prose_arm_B(book, setting, "R2")
        rlab = {c: [lab[c][i] for i in range(len(lab[c]))] for c in CONVS}
        for p in ("P1", "P2"):
            T = ProseTuple(rlab, keepr, p)
            if not T.coarsening:
                say(f"   D-P3 {book} [{setting}] {p}: the prose pausal partition is NOT a "
                    f"coarsening of its citation partition — the exact null is UNDEFINED "
                    f"here and is not run (prereg §11).")
                TESTS[f"DP3_{book}_{setting}_{p}"] = {"undefined": True}
                continue
            res = prose_exact_null(T, SEED, N_PERM)
            res2 = prose_exact_null(T, SEED_REP, N_PERM)
            res["p_replication"] = res2["p_E"]
            res["z_replication"] = res2["z_E"]
            res["quran_z"] = QURAN_Z_P1
            res["pass"] = res["p_E"] < ALPHA
            TESTS[f"DP3_{book}_{setting}_{p}"] = res
            say(f"   D-P3 {book:9s} [{setting}] {p}: E_obs={res['observed_E']:.4f} "
                f"null E mean={res['null_E_mean']:.4f} sd={res['null_E_sd']:.4f} "
                f"#>=obs={res['n_ge_observed_E']} p={res['p_E']:.5f} z={res['z_E']:+.2f}"
                f"  [Qurʾān z={QURAN_Z_P1:+.2f}]  floor dev={res['null_floor_max_abs_dev']:.1e}")
checkpoint("tests", TESTS)

# ---------------------------------------------------------------- 5. verdict
say("\n" + "=" * 78)
say("VERDICT — logic diffed against prereg §8, printed before declaration.")
say("=" * 78)
say("   prereg §8 grid, verbatim:")
say("     no admissible text                                  -> CONTROL UNAVAILABLE")
say("     Δ_prose(Arm B) >= +0.09343 under ANY of S5/S3/S0     -> H-NEW-2880 DAMAGED")
say("     +0.04672 <= Δ_prose < +0.09343 under any setting     -> PARTIAL, amend 2880's limits")
say("     Δ_prose < +0.04672 under ALL three AND D-P1 passes   -> CONTROL PASSES")
say("     Δ_prose < +0.04672 but D-P1 fails                    -> INCONCLUSIVE")
say("   The verdict is taken on the WORST setting, not the best.")
say(f"   Bonferroni k = {BONFERRONI_K} -> alpha = {ALPHA:.8f}")

worst = None
for book in PRIMARY_TEXTS:
    for setting in STRIP_SETTINGS:
        d = ARMB[f"{book}_{setting}_R2"]["delta_readable"]["P1"]
        if worst is None or d > worst[0]:
            worst = (d, book, setting)
WORST_DELTA, WORST_BOOK, WORST_SET = worst
DP1_ALL = all(v["pass"] for k, v in TESTS.items() if k.startswith("DP1_"))
say(f"\n   worst-case Δ_prose(Arm B, P1, readable) = {WORST_DELTA:+.5f} "
    f"({WORST_BOOK}, {WORST_SET})")

# DISCLOSURE, added after a --smoke run that writes nothing and BEFORE the real run.
# It changes NO gate. prereg §7 defines the threshold quantity on tuple P1 explicitly
# ("Arm B, P1, rime R2"), and §8 extends the worst case over the three stripping settings
# only -- so the locked verdict is computed on P1, as above. A reader could instead take the
# worst case over BOTH tuples. That reading is printed here so the choice is visible rather
# than buried, and so that a near-threshold P2 value cannot look like it was hidden.
_strict = None
for _b in PRIMARY_TEXTS:
    for _s in STRIP_SETTINGS:
        for _p in ("P1", "P2"):
            _d = ARMB[f"{_b}_{_s}_R2"]["delta_readable"][_p]
            if _strict is None or _d > _strict[0]:
                _strict = (_d, _b, _s, _p)
STRICT_DELTA, STRICT_BOOK, STRICT_SET, STRICT_TUPLE = _strict
STRICT_VERDICT = ("H-NEW-2880 DAMAGED" if STRICT_DELTA >= DAMAGE_HALF
                  else "PARTIAL" if STRICT_DELTA >= DAMAGE_QUARTER
                  else "CONTROL PASSES")
say(f"   [disclosure, gates nothing] worst case over BOTH tuples = {STRICT_DELTA:+.5f} "
    f"({STRICT_BOOK}, {STRICT_SET}, {STRICT_TUPLE}); quarter threshold = "
    f"{DAMAGE_QUARTER:+.5f}; that reading would give: {STRICT_VERDICT}")
say(f"   D-P1 passes at alpha in all {sum(1 for k in TESTS if k.startswith('DP1_'))} arms: {DP1_ALL}")

if not admissible:
    VERDICT = "CONTROL UNAVAILABLE"
elif WORST_DELTA >= DAMAGE_HALF:
    VERDICT = "H-NEW-2880 DAMAGED — prose gains comparably"
elif WORST_DELTA >= DAMAGE_QUARTER:
    VERDICT = "PARTIAL — amend H-NEW-2880's honest limits"
elif DP1_ALL:
    VERDICT = "CONTROL PASSES — H-NEW-2880's interpretation survives"
else:
    VERDICT = "INCONCLUSIVE"
say(f"\n   VERDICT: {VERDICT}")

# ---------------------------------------------------------------- 6. write
if SMOKE:
    say("\n[SMOKE] no run directory written, no JSON written. Exiting.")
    raise SystemExit(0)
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-2890", STAMP)
os.makedirs(RUNDIR, exist_ok=False)
out = {
    "id": "H-NEW-2890",
    "title": "The vocalised-prose negative control H-NEW-2870/2880 reported as not computable",
    "run_utc": STAMP, "prereg": PREREG, "prereg_sha256": PREREG_SHA256,
    "parents": ["H-NEW-2870", "H-NEW-2880"], "frozen_inputs": FROZEN,
    "seed": SEED, "seed_replication": SEED_REP, "n_perm": N_PERM,
    "n_prose_cut": N_PROSE_CUT, "bonferroni_k": BONFERRONI_K, "alpha": ALPHA,
    "python": sys.version.split()[0], "platform": platform.platform(),
    "acquisition": {k: {kk: vv for kk, vv in v.items()
                        if kk not in ("records", "texts", "contam", "chapters")}
                    for k, v in BOOKS.items()},
    "vocalisation_threshold": VOC_THRESHOLD, "admissible": admissible,
    "locked_targets": {"quran_delta_P1": QURAN_DELTA_P1,
                       "quran_recut_delta_P1": QURAN_RECUT_DELTA_P1,
                       "damage_half": DAMAGE_HALF, "damage_quarter": DAMAGE_QUARTER},
    "arm_B_composed": ARMB, "arm_A_matched_cuts": ARMA, "tests": TESTS,
    "worst_case": {"delta": WORST_DELTA, "book": WORST_BOOK, "setting": WORST_SET},
    "worst_case_both_tuples_disclosure": {
        "delta": STRICT_DELTA, "book": STRICT_BOOK, "setting": STRICT_SET,
        "tuple": STRICT_TUPLE, "verdict_under_that_reading": STRICT_VERDICT,
        "note": "gates nothing; prereg §7 defines the threshold quantity on tuple P1"},
    "verdict": VERDICT,
}
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as f:
    f.write(f"H-NEW-2890 run {STAMP}\nprereg {PREREG} {PREREG_SHA256}\n"
            f"script findings/phase-b-hypotheses/scripts/h-new-2890.py "
            f"{sha256_file('findings/phase-b-hypotheses/scripts/h-new-2890.py')}\n")
    for p, s in FROZEN.items():
        f.write(f"input {p} {s}\n")
    f.write(f"source-manifest data/literature/hadith/VOCALISED-HADITH-SOURCE.md\n")
    f.write(f"output {RUNDIR}/result.json\noutput {RUNDIR}/console.log\n")
    f.write(f"checkpoints {CHECKPOINT_DIR}/  (OUTSIDE the run directory, write-once)\n")
os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2890.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
print(f"\n[WROTE] {RUNDIR}/result.json")
print(f"[WROTE] findings/phase-b-hypotheses/csv/h-new-2890.json")
