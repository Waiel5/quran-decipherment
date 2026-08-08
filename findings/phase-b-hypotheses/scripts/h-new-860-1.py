#!/usr/bin/env python3
"""
H-NEW-860.1 -- a formal per-verse hadith reception weight over the full on-disk corpus,
replacing H-NEW-860's hand-built "rough rubric".

H-NEW-860 stated that a formal count "would require a hadith-database ... which is not on
disk". The claim is FALSE: data/literature/hadith/ahmedbaset-json/ is a sunnah.com scrape of
50,884 records across 17 books, committed 2026-04-28 (ABSENCE-CLAIMS.md, FALSE #3).

Pre-registration locked at
  findings/phase-b-hypotheses/prereg-h-new-860-1-fadail-formal.md
  SHA-256 15f3940478d1842a22ab99fee41e831e22934c7766d299339f477d824444c7f1
verified at runtime.

IMPLEMENTATION CONSTRAINT, prereg 3.1: every Arabic string in this file is built from
integer codepoints. Arabic literals inside a regex character class are reordered by
bidirectional text handling when the source is written, which rewrites the deletion range
into one covering U+0621-U+064A and strips every Arabic letter in the corpus. A probe run
died of exactly this. norm() is self-tested at runtime against a fixed vector.

Waiel Al-Shujaa, 2026-08-08.
"""
import csv
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
from scipy import stats

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)

PREREG = "findings/phase-b-hypotheses/prereg-h-new-860-1-fadail-formal.md"
PREREG_SHA256 = "15f3940478d1842a22ab99fee41e831e22934c7766d299339f477d824444c7f1"

SEED, SEED_REP = 20260509, 20260519
N_PERM = 10000
BONFERRONI_K = 18
ALPHA_BON = 0.05 / BONFERRONI_K
ALPHA_PRIMARY = 0.05                      # prereg 6.1 -- the published bar, like-for-like
RHO_PUB = 0.330                           # prereg 2
RHO_HALF = 0.5 * RHO_PUB

QURAN = "quran-text/quran-no-tashkeel.json"
HDIR = "data/literature/hadith/ahmedbaset-json/db/by_book"
BOOKS9 = ["bukhari", "muslim", "abudawud", "tirmidhi", "nasai",
          "ibnmajah", "malik", "ahmed", "darimi"]
BOOKS_OTHER = ["forties/nawawi40", "forties/qudsi40", "forties/shahwaliullah40",
               "other_books/aladab_almufrad", "other_books/bulugh_almaram",
               "other_books/mishkat_almasabih", "other_books/riyad_assalihin",
               "other_books/shamail_muhammadiyah"]
UAS_JSON = "findings/phase-b-hypotheses/csv/h-new-840.json"
OUT590 = "findings/phase-b-hypotheses/csv/h-new-590.json"
RUBRIC = "findings/phase-b-hypotheses/csv/h-new-860.json"
POETRY_GLOB = "data/baseline-corpora/raw/diwan-*.openiti.raw.txt"

MINW = 4                                  # prereg 3.3(b)
SPAN_ARMS = [4, 5, 6]                     # prereg 3.3; 5 is primary
SPAN_PRIMARY = 5
IDX_N = 4                                 # inverted-index shingle length; == MINW

DELIVERABLE = "findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv"

# ---------------------------------------------------------------- Arabic, from codepoints
_DEL_RANGES = [(0x0610, 0x061A), (0x064B, 0x065F), (0x0670, 0x0670),
               (0x06D6, 0x06ED), (0x0640, 0x0640)]
DIAC = re.compile("[" + "".join(f"\\u{a:04x}-\\u{b:04x}" for a, b in _DEL_RANGES) + "]")
NONAR = re.compile("[^\\u0621-\\u064a ]+")
WS = re.compile(r"\s+")
TRANS = str.maketrans({0x0622: 0x0627, 0x0623: 0x0627, 0x0625: 0x0627, 0x0671: 0x0627,
                       0x0649: 0x064A, 0x0629: 0x0647, 0x0624: 0x0648, 0x0626: 0x064A})
WORD_SURA = "".join(chr(c) for c in (0x0633, 0x0648, 0x0631, 0x0647))   # suura, normalised
AL = "".join(chr(c) for c in (0x0627, 0x0644))                          # al-


def norm(s):
    s = unicodedata.normalize("NFC", s or "")
    s = DIAC.sub("", s).translate(TRANS)
    return WS.sub(" ", NONAR.sub(" ", s)).strip()


def norm_selftest():
    """prereg 3.1 -- abort if BiDi reordering has corrupted the character classes."""
    basmala = "".join(chr(c) for c in (
        0x0628, 0x0633, 0x0645, 0x0020, 0x0627, 0x0644, 0x0644, 0x0647, 0x0020,
        0x0627, 0x0644, 0x0631, 0x062D, 0x0645, 0x0646, 0x0020,
        0x0627, 0x0644, 0x0631, 0x062D, 0x064A, 0x0645))
    vocalised = "".join(chr(c) for c in (
        0x0628, 0x0650, 0x0633, 0x0652, 0x0645, 0x0650, 0x0020,
        0x0627, 0x0644, 0x0644, 0x064E, 0x0651, 0x0647, 0x0650, 0x0020,
        0x0627, 0x0644, 0x0631, 0x064E, 0x0651, 0x062D, 0x0652, 0x0645, 0x064E, 0x0670, 0x0646, 0x0650,
        0x0020, 0x0627, 0x0644, 0x0631, 0x064E, 0x0651, 0x062D, 0x0650, 0x064A, 0x0645, 0x0650))
    assert norm(basmala) == basmala, "norm() altered an already-plain string"
    assert norm(vocalised) == basmala, "norm() failed to strip harakat / superscript alif"
    assert len(norm(vocalised).split()) == 4
    ta_marbuta = chr(0x0629)
    assert norm(ta_marbuta) == chr(0x0647), "ta marbuta mapping broken"
    assert norm(chr(0x0623)) == chr(0x0627), "alif mapping broken"
    return hashlib.sha256(norm(vocalised).encode()).hexdigest()


# ---------------------------------------------------------------- helpers
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def log(msg):
    print(msg, flush=True)
    LOGLINES.append(msg)


LOGLINES = []


def checkpoint(tag, payload):
    """prereg 9 -- checkpoints are written PER ARM, OUTSIDE the immutable run directory."""
    with open(os.path.join(CKPT_DIR, f"ckpt-{tag}.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, default=str)


def spearman(x, y):
    if len(set(x)) < 2 or len(set(y)) < 2:
        return float("nan"), float("nan")
    r = stats.spearmanr(x, y)
    return float(r.statistic), float(r.pvalue)


def kendall(x, y):
    r = stats.kendalltau(x, y)
    return float(r.statistic), float(r.pvalue)


def pearson(x, y):
    r = stats.pearsonr(x, y)
    return float(r.statistic), float(r.pvalue)


def partial_spearman(x, y, z):
    """Spearman of x,y controlling z -- correlation of the residuals of the rank variables."""
    rx, ry, rz = stats.rankdata(x), stats.rankdata(y), stats.rankdata(z)
    def resid(a, b):
        b1 = np.column_stack([np.ones(len(b)), b])
        beta, *_ = np.linalg.lstsq(b1, a, rcond=None)
        return a - b1 @ beta
    ex, ey = resid(rx, rz), resid(ry, rz)
    r, p = stats.pearsonr(ex, ey)
    return float(r), float(p)


def gini(v):
    v = np.sort(np.asarray(v, dtype=float))
    n = len(v)
    if n == 0 or v.sum() == 0:
        return float("nan")
    return float((2 * np.arange(1, n + 1) - n - 1).dot(v) / (n * v.sum()))


# ---------------------------------------------------------------- run directory
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-860-1", STAMP)
os.makedirs(RUNDIR, exist_ok=False)                     # prereg 9
CKPT_DIR = os.path.join("scratch", "h-new-860-1-checkpoints")
os.makedirs(CKPT_DIR, exist_ok=True)                    # OUTSIDE the run directory

log(f"H-NEW-860.1  run {STAMP}")
log(f"rundir {RUNDIR}")

got = sha256_file(PREREG)
if got != PREREG_SHA256:
    sys.exit(f"ABORT: prereg SHA-256 mismatch\n  expected {PREREG_SHA256}\n  got      {got}")
log(f"prereg SHA-256 verified: {got}")
log(f"norm() self-test passed, vector {norm_selftest()}")

# ---------------------------------------------------------------- load corpora
quran = json.load(open(QURAN, encoding="utf-8"))
verses = []
for su in quran:
    for v in su["verses"]:
        verses.append((su["id"], v["id"], norm(v["text"]).split()))
assert len(verses) == 6236, len(verses)
assert len(quran) == 114
VW = {(s, a): w for s, a, w in verses}
SNAME = {su["id"]: norm(su["name"]) for su in quran}
SUR_WORDS = Counter()
SUR_VERSES = Counter()
for s, a, w in verses:
    SUR_WORDS[s] += len(w)
    SUR_VERSES[s] += 1
log(f"Quran: 114 surahs, {len(verses)} verses, {sum(SUR_WORDS.values()):,} normalised words")


def load_book(rel):
    d = json.load(open(os.path.join(HDIR, rel + ".json"), encoding="utf-8"))
    return d["hadiths"]


recs, rec_book = [], []
for b in BOOKS9:
    for h in load_book("the_9_books/" + b):
        recs.append(norm(h.get("arabic") or ""))
        rec_book.append(b)
N9 = len(recs)
for b in BOOKS_OTHER:
    for h in load_book(b):
        recs.append(norm(h.get("arabic") or ""))
        rec_book.append(b.split("/")[-1])
N17 = len(recs)
assert N9 == 40943, N9
assert N17 == 50884, N17
HW = [t.split() for t in recs]
PAD = [" " + t + " " for t in recs]
NH_WORDS9 = sum(len(HW[i]) for i in range(N9))
log(f"hadith: {N9:,} records in the nine books, {N17:,} in all seventeen; "
    f"{NH_WORDS9:,} normalised words in the nine")

# ---------------------------------------------------------------- inverted index
def build_index(idxs):
    d = defaultdict(list)
    for i in idxs:
        w = HW[i]
        seen = set()
        for j in range(len(w) - IDX_N + 1):
            g = " ".join(w[j:j + IDX_N])
            if g not in seen:
                seen.add(g)
                d[g].append(i)
    return d


IDX_ALL = build_index(range(N17))
log(f"inverted index: {len(IDX_ALL):,} distinct {IDX_N}-grams over all 17 books")

# ---------------------------------------------------------------- the link rule
def spans_and_ownership(N):
    """prereg 3.3 -- ownership computed across EVERY span length in play, from EVERY verse."""
    spans_of, lens = {}, set()
    for s, a, w in verses:
        if len(w) < MINW:
            spans_of[(s, a)] = []
            continue
        n = min(N, len(w))
        lens.add(n)
        spans_of[(s, a)] = [" ".join(w[j:j + n]) for j in range(len(w) - n + 1)]
    own = defaultdict(set)
    for s, a, w in verses:
        for L in lens:
            for j in range(len(w) - L + 1):
                own[" ".join(w[j:j + L])].add((s, a))
    return spans_of, own


def link(N, level, universe_hi, index):
    """Return per-verse record sets. universe_hi = exclusive upper record index."""
    spans_of, own = spans_and_ownership(N)
    dist, ambig, driver, maxlen = {}, {}, {}, {}
    ineligible_short, nondistinctive = set(), set()
    for s, a, w in verses:
        key = (s, a)
        if len(w) < MINW:
            ineligible_short.add(key)
            dist[key], ambig[key] = set(), set()
            driver[key], maxlen[key] = "", 0
            continue
        keep, rest = [], []
        for sp in spans_of[key]:
            o = own[sp]
            ok = (len(o) == 1) if level == "verse" else (len({x[0] for x in o}) == 1)
            (keep if ok else rest).append(sp)
        if not keep:
            nondistinctive.add(key)
        dhits, ahits, cnt, ml = set(), set(), Counter(), 0
        for bucket, lst, is_dist in ((dhits, keep, True), (ahits, rest, False)):
            for sp in lst:
                cands = index.get(" ".join(sp.split()[:IDX_N]))
                if not cands:
                    continue
                t = " " + sp + " "
                k = 0
                for i in cands:
                    if i < universe_hi and t in PAD[i]:
                        bucket.add(i)
                        k += 1
                if k and is_dist:
                    cnt[sp] += k
                    ml = max(ml, len(sp.split()))
        dist[key], ambig[key] = dhits, ahits
        driver[key] = cnt.most_common(1)[0][0] if cnt else ""
        maxlen[key] = ml
    return dict(dist=dist, ambig=ambig, driver=driver, maxlen=maxlen,
                short=ineligible_short, nondist=nondistinctive)


LINKS = {}
for N in SPAN_ARMS:
    for level in ("verse", "surah"):
        LINKS[(N, level)] = link(N, level, N9, IDX_ALL)
        r = LINKS[(N, level)]
        nl = sum(len(v) for v in r["dist"].values())
        log(f"  arm N={N} {level:5s}: {sum(1 for v in r['dist'].values() if v):5d} verses matched, "
            f"{nl:6d} links, {len(r['short'])} short, {len(r['nondist'])} non-distinctive")
        checkpoint(f"link-N{N}-{level}", {"links": nl})

# all-17 tertiary, primary span, verse level (prereg 4.1 -- not verdict-bearing)
LINK17 = link(SPAN_PRIMARY, "verse", N17, IDX_ALL)

# ---------------------------------------------------------------- naming instrument
def naming_links():
    out = defaultdict(set)
    for sid, nm in SNAME.items():
        core = nm[len(AL):] if nm.startswith(AL) else nm
        pat = re.compile("(?<![\\u0621-\\u064a])" + WORD_SURA + r"\s+(?:" + AL + ")?"
                         + re.escape(core) + "(?![\\u0621-\\u064a])")
        for i in range(N9):
            if pat.search(recs[i]):
                out[sid].add(i)
    return out


NAMING = naming_links()
log(f"naming instrument: {sum(len(v) for v in NAMING.values())} links over "
    f"{len(NAMING)} surahs (canonical names only, prereg 3.6)")
checkpoint("naming", {s: len(v) for s, v in NAMING.items()})

# ---------------------------------------------------------------- false-positive control
import glob as _glob
poe_words = []
for f in sorted(_glob.glob(POETRY_GLOB)):
    poe_words.append(norm(open(f, encoding="utf-8", errors="ignore").read()).split())
NP_WORDS = sum(len(w) for w in poe_words)
_saveHW, _savePAD = HW, PAD
poe_recs = [w[j:j + 80] for w in poe_words for j in range(0, len(w), 80)]
HW = poe_recs
PAD = [" " + " ".join(w) + " " for w in poe_recs]
POE_IDX = build_index(range(len(poe_recs)))
FP = {}
for N in SPAN_ARMS:
    r = link(N, "verse", len(poe_recs), POE_IDX)
    FP[N] = sum(len(v) for v in r["dist"].values())
HW, PAD = _saveHW, _savePAD
log("FP control (pre-Islamic diwans, %d words): " % NP_WORDS +
    ", ".join(f"N={N}: {FP[N]} links = {FP[N]/NP_WORDS*1e6:.1f}/Mw" for N in SPAN_ARMS))

# ---------------------------------------------------------------- surah aggregation
def surah_counts(N, instrument):
    """prereg 4.2 -- distinct records linked to >=1 verse of the surah."""
    per = defaultdict(set)
    if instrument in ("Q", "U"):
        d = LINKS[(N, "surah")]["dist"]
        for (s, a), v in d.items():
            per[s] |= v
    if instrument in ("N", "U"):
        for s, v in NAMING.items():
            per[s] |= v
    return {s: len(per.get(s, set())) for s in range(1, 115)}


SC = {(N, ins): surah_counts(N, ins) for N in SPAN_ARMS for ins in ("Q", "N", "U")}

# ---------------------------------------------------------------- deliverable table
prim_v = LINKS[(SPAN_PRIMARY, "verse")]
prim_s = LINKS[(SPAN_PRIMARY, "surah")]
book_of = {i: rec_book[i] for i in range(N17)}
rows = []
for s, a, w in verses:
    key = (s, a)
    dv = prim_v["dist"][key]
    bks = sorted({book_of[i] for i in dv})
    per_book = Counter(book_of[i] for i in dv)
    if key in prim_v["short"]:
        elig, why = 0, "under_4_words"
    elif key in prim_v["nondist"]:
        elig, why = 0, "no_verse_distinctive_span"
    else:
        elig, why = 1, ""
    rows.append(dict(
        sura=s, aya=a, surah_name=SNAME[s], n_words=len(w),
        eligible=elig, ineligible_reason=why,
        n_hadith=len(dv),
        n_hadith_ambiguous=len(prim_v["ambig"][key]),
        n_books=len(bks),
        n_hadith_all17=len(LINK17["dist"][key]),
        n_hadith_surah_level=len(prim_s["dist"][key]),
        max_span_words=prim_v["maxlen"][key],
        driver_span=prim_v["driver"][key],
        **{f"b_{b}": per_book.get(b, 0) for b in BOOKS9},
    ))
FIELDS = list(rows[0].keys())
with open(DELIVERABLE, "w", encoding="utf-8", newline="") as f:
    wtr = csv.DictWriter(f, fieldnames=FIELDS)
    wtr.writeheader()
    wtr.writerows(rows)
log(f"deliverable written: {DELIVERABLE} ({len(rows)} verses, {len(FIELDS)} columns)")

# ---------------------------------------------------------------- concentration (prereg 7.2)
elig_rows = [r for r in rows if r["eligible"]]
counts = [r["n_hadith"] for r in elig_rows]
tot = sum(counts)
top = sorted(rows, key=lambda r: -r["n_hadith"])
CONC = dict(
    n_eligible=len(elig_rows), total_links=tot,
    n_ineligible_short=len(prim_v["short"]), n_nondistinctive=len(prim_v["nondist"]),
    n_verses_cited=sum(1 for c in counts if c > 0),
    share_top20=sum(r["n_hadith"] for r in top[:20]) / tot,
    share_top100=sum(r["n_hadith"] for r in top[:100]) / tot,
    gini_eligible=gini(counts),
    top20=[dict(ref=f"Q{r['sura']}:{r['aya']}", n=r["n_hadith"], books=r["n_books"],
                span=r["driver_span"], words=r["n_words"]) for r in top[:20]],
)
log(f"concentration: top-20 hold {CONC['share_top20']:.1%} of all links; "
    f"Gini {CONC['gini_eligible']:.3f}; {CONC['n_verses_cited']} of "
    f"{CONC['n_eligible']} eligible verses cited at all")

# ---------------------------------------------------------------- outcome data
uas_raw = json.load(open(UAS_JSON, encoding="utf-8"))["all_uas"]
UAS = {d["surah"]: d["UAS"] for d in uas_raw}
UAS_RANK = {d["surah"]: i + 1 for i, d in enumerate(
    sorted(uas_raw, key=lambda d: -d["UAS"]))}
o590 = json.load(open(OUT590, encoding="utf-8"))["all_surahs_results"]
OUT = {d.get("X", d.get("surah")): d.get("delta_pct", d.get("delta")) for d in o590}
rub_raw = json.load(open(RUBRIC, encoding="utf-8"))["hadith_emphasis_scores"]
RUB = {int(k[1:]): v["score"] for k, v in rub_raw.items()}
RUB_SET = sorted(RUB)
log(f"UAS on {len(UAS)} surahs; outlier on {len(OUT)}; rubric on {len(RUB)} surahs")
assert len(UAS) == 114 and len(OUT) == 114

# sanity: our reconstructed UAS ranks must reproduce the ones H-NEW-860 published
pub_rank = {int(k[1:]): v["uas_rank"] for k, v in rub_raw.items()}
mism = {s: (UAS_RANK[s], pub_rank[s]) for s in pub_rank if UAS_RANK[s] != pub_rank[s]}
log(f"UAS-rank reconstruction: {len(pub_rank)-len(mism)}/{len(pub_rank)} match H-NEW-860; "
    f"mismatches {mism if mism else 'none'}")

LOGWORDS = {s: math.log(SUR_WORDS[s]) for s in range(1, 115)}

# ---------------------------------------------------------------- the 18 arms
ARMS = []
for ins in ("Q", "N", "U"):
    for N in SPAN_ARMS:
        c = SC[(N, ins)]
        for cell, subset in (("A", RUB_SET), ("B", list(range(1, 115)))):
            x = [c[s] for s in subset]
            y = [UAS_RANK[s] for s in subset]
            rho, p = spearman(x, y)
            ARMS.append(dict(instrument=ins, span=N, cell=cell, n=len(subset),
                             rho_vs_uas_rank=rho, p=p,
                             sig_bonferroni=bool(p < ALPHA_BON)))
checkpoint("arms", ARMS)

PRIMARY = [a for a in ARMS if a["instrument"] == "Q" and a["span"] == SPAN_PRIMARY
           and a["cell"] == "A"][0]
rho_f, p_f = PRIMARY["rho_vs_uas_rank"], PRIMARY["p"]
log(f"\nPRIMARY ARM (Q, N={SPAN_PRIMARY}, cell A, n={PRIMARY['n']}): "
    f"rho(formal count, UAS_rank) = {rho_f:+.4f}, p = {p_f:.4f}")
log("  sign convention: UAS_rank 1 = most architecturally distinct, so POSITIVE rho = "
    "more hadith attention -> WORSE architectural rank = ANTI-alignment")

# ---------------------------------------------------------------- nulls on the primary arm
xA = [SC[(SPAN_PRIMARY, "Q")][s] for s in RUB_SET]
yA = [UAS_RANK[s] for s in RUB_SET]
zA = [LOGWORDS[s] for s in RUB_SET]
pr, pp = partial_spearman(xA, yA, zA)
log(f"  partial Spearman controlling log surah word count: {pr:+.4f}, p = {pp:.4f}")

def strat_perm(x, y, z, k, seed):
    rng = random.Random(seed)
    obs, _ = spearman(x, y)
    qs = np.quantile(z, np.linspace(0, 1, k + 1)[1:-1])
    binid = np.digitize(z, qs)
    idx_by_bin = defaultdict(list)
    for i, b in enumerate(binid):
        idx_by_bin[b].append(i)
    ge = 0
    draws = []
    for _ in range(N_PERM):
        yp = list(y)
        for b, ids in idx_by_bin.items():
            vals = [y[i] for i in ids]
            rng.shuffle(vals)
            for i, v in zip(ids, vals):
                yp[i] = v
        d, _ = spearman(x, yp)
        draws.append(d)
        if abs(d) >= abs(obs):
            ge += 1
    return dict(k=k, seed=seed, observed=obs, p_two_sided=(ge + 1) / (N_PERM + 1),
                null_mean=float(np.mean(draws)), null_sd=float(np.std(draws)),
                null_absmax=float(np.max(np.abs(draws))))

NULLS = []
for k in (5, 10):
    for sd in (SEED, SEED_REP):
        r = strat_perm(xA, yA, zA, k, sd)
        NULLS.append(r)
        log(f"  stratified permutation k={k} seed={sd}: p = {r['p_two_sided']:.4f} "
            f"(null sd {r['null_sd']:.3f}, |max| {r['null_absmax']:.3f})")
        checkpoint(f"null-k{k}-s{sd}", r)

# STATE-OF-THE-PROJECT 0 -- the cheapest diagnostic, before any p-value
rng = random.Random(SEED)
obs_med = float(np.median([LOGWORDS[s] for s in RUB_SET]))
draws_med = []
allsur = list(range(1, 115))
for _ in range(N_PERM):
    draws_med.append(float(np.median([LOGWORDS[s] for s in rng.sample(allsur, len(RUB_SET))])))
frac_ge = sum(1 for d in draws_med if d >= obs_med) / N_PERM
log(f"  cheapest diagnostic: the rubric's 36-surah set has median log word count "
    f"{obs_med:.3f}; a random 36 reaches it {frac_ge*100:.2f}% of the time")

null_pass = all(r["p_two_sided"] < ALPHA_PRIMARY for r in NULLS) and pp < ALPHA_PRIMARY

# ---------------------------------------------------------------- verdict (prereg 6.2)
same_sign = (rho_f > 0) == (RHO_PUB > 0)
if (not same_sign) and p_f < ALPHA_PRIMARY:
    VERDICT = "REVERSES"
elif same_sign and p_f < ALPHA_PRIMARY and rho_f >= RHO_HALF:
    VERDICT = "SURVIVES" if null_pass else "WEAKENS (confounded by length)"
elif same_sign and (p_f >= ALPHA_PRIMARY or rho_f < RHO_HALF):
    VERDICT = "WEAKENS"
else:
    VERDICT = "UNDETERMINED"

log("\n--- verdict logic, diffed against prereg 6.2 ---")
log(f"  rho_pub = {RHO_PUB:+.3f}   half-bar = {RHO_HALF:+.3f}   alpha = {ALPHA_PRIMARY}")
log(f"  rho_f = {rho_f:+.4f}  p_f = {p_f:.4f}  same_sign = {same_sign}  "
    f"clears_half = {rho_f >= RHO_HALF}  nulls_pass = {null_pass}")
log(f"  REVERSES  <- (not same_sign) and p<0.05          : {(not same_sign) and p_f < 0.05}")
log(f"  SURVIVES  <- same_sign and p<0.05 and rho>=half  : "
    f"{same_sign and p_f < 0.05 and rho_f >= RHO_HALF}")
log(f"  WEAKENS   <- same_sign and (p>=0.05 or rho<half) : "
    f"{same_sign and (p_f >= 0.05 or rho_f < RHO_HALF)}")
log(f"  UNDETERM. <- (not same_sign) and p>=0.05         : {(not same_sign) and p_f >= 0.05}")
log(f"  VERDICT = {VERDICT}")

# ---------------------------------------------------------------- rubric agreement (6.4)
def agreement(subset, label):
    r = [RUB.get(s, 0) for s in subset]
    q = [SC[(SPAN_PRIMARY, "Q")][s] for s in subset]
    n = [SC[(SPAN_PRIMARY, "N")][s] for s in subset]
    u = [SC[(SPAN_PRIMARY, "U")][s] for s in subset]
    out = dict(label=label, n=len(subset))
    for nm, v in (("quotation", q), ("naming", n), ("union", u)):
        rho, p = spearman(r, v)
        tau, pt = kendall(r, v)
        out[nm] = dict(spearman=rho, p_spearman=p, kendall=tau, p_kendall=pt)
    return out


AGREE = [agreement(RUB_SET, "36 rubric-listed surahs"),
         agreement(list(range(1, 115)), "all 114, unlisted-as-zero")]
for a in AGREE:
    log(f"\nrubric agreement ({a['label']}, n={a['n']}):")
    for nm in ("quotation", "naming", "union"):
        log(f"    rubric x {nm:9s}: rho = {a[nm]['spearman']:+.4f} (p={a[nm]['p_spearman']:.4g}), "
            f"tau = {a[nm]['kendall']:+.4f}")

uq = SC[(SPAN_PRIMARY, "U")]
rub_top = lambda k: [s for s in sorted(RUB, key=lambda s: (-RUB[s], s))[:k]]
frm_top = lambda k: [s for s in sorted(range(1, 115), key=lambda s: (-uq[s], s))[:k]]
OVERLAP = {f"top{k}": dict(rubric=rub_top(k), formal=frm_top(k),
                           overlap=sorted(set(rub_top(k)) & set(frm_top(k))),
                           n_overlap=len(set(rub_top(k)) & set(frm_top(k))))
           for k in (10, 20)}
for k in (10, 20):
    log(f"  top-{k} overlap rubric vs formal (union instrument): "
        f"{OVERLAP[f'top{k}']['n_overlap']}/{k}")

rr = {s: i + 1 for i, s in enumerate(sorted(RUB, key=lambda s: (-RUB[s], s)))}
fr = {s: i + 1 for i, s in enumerate(sorted(RUB, key=lambda s: (-uq[s], s)))}
DISAGREE = sorted(((fr[s] - rr[s]), s) for s in RUB)
BIGGEST = dict(
    rubric_overrated=[dict(surah=s, rubric_score=RUB[s], rubric_rank=rr[s],
                           formal_rank=fr[s], formal_count=uq[s], drop=d)
                      for d, s in DISAGREE[-10:][::-1]],
    rubric_underrated=[dict(surah=s, rubric_score=RUB[s], rubric_rank=rr[s],
                            formal_rank=fr[s], formal_count=uq[s], gain=-d)
                       for d, s in DISAGREE[:10]])

# ---------------------------------------------------------------- residual roster (7.3)
def rank_desc(d, keys):
    return {s: i + 1 for i, s in enumerate(sorted(keys, key=lambda s: (-d[s], s)))}


allS = list(range(1, 115))
rec_rank = rank_desc(uq, allS)
uas_rank = UAS_RANK
out_rank = rank_desc(OUT, allS)
ROSTER = dict(
    structurally_extreme_rarely_cited=[
        dict(surah=s, uas_rank=uas_rank[s], outlier_rank=out_rank[s],
             reception_rank=rec_rank[s], formal_count=uq[s],
             quotation_count=SC[(SPAN_PRIMARY, "Q")][s], naming_count=SC[(SPAN_PRIMARY, "N")][s],
             residual=rec_rank[s] - min(uas_rank[s], out_rank[s]))
        for s in sorted(allS, key=lambda s: -(rec_rank[s] - min(uas_rank[s], out_rank[s])))[:15]],
    heavily_cited_structurally_ordinary=[
        dict(surah=s, uas_rank=uas_rank[s], outlier_rank=out_rank[s],
             reception_rank=rec_rank[s], formal_count=uq[s],
             quotation_count=SC[(SPAN_PRIMARY, "Q")][s], naming_count=SC[(SPAN_PRIMARY, "N")][s],
             residual=rec_rank[s] - max(uas_rank[s], out_rank[s]))
        for s in sorted(allS, key=lambda s: (rec_rank[s] - max(uas_rank[s], out_rank[s])))[:15]],
)
ROSTER["verse_level_top_cited"] = CONC["top20"]

SUPP = dict(
    rho_reception_vs_outlier_A=spearman([uq[s] for s in RUB_SET], [OUT[s] for s in RUB_SET]),
    rho_reception_vs_outlier_B=spearman([uq[s] for s in allS], [OUT[s] for s in allS]),
    rho_reception_vs_uasvalue_B=spearman([uq[s] for s in allS], [UAS[s] for s in allS]),
    pearson_like_for_like_B=pearson([uq[s] for s in allS], [UAS[s] for s in allS]),
    drift_surah_words=spearman([SUR_WORDS[s] for s in allS],
                               [SC[(SPAN_PRIMARY, 'Q')][s] for s in allS]),
    drift_surah_verses=spearman([SUR_VERSES[s] for s in allS],
                                [SC[(SPAN_PRIMARY, 'Q')][s] for s in allS]),
    drift_naming_words=spearman([SUR_WORDS[s] for s in allS],
                                [SC[(SPAN_PRIMARY, 'N')][s] for s in allS]),
    rho_quotation_naming=spearman([SC[(SPAN_PRIMARY, 'Q')][s] for s in allS],
                                  [SC[(SPAN_PRIMARY, 'N')][s] for s in allS]),
    drift_verse_words=spearman([len(VW[(r['sura'], r['aya'])]) for r in elig_rows],
                               [r["n_hadith"] for r in elig_rows]),
)
for k, v in SUPP.items():
    log(f"  {k}: rho = {v[0]:+.4f}, p = {v[1]:.4g}")

BOOK_SHARE = Counter()
for r in rows:
    for b in BOOKS9:
        BOOK_SHARE[b] += r[f"b_{b}"]

# ---------------------------------------------------------------- write results
RESULT = dict(
    id="H-NEW-860.1", run=STAMP, prereg=PREREG, prereg_sha256=PREREG_SHA256,
    seed=SEED, seed_replication=SEED_REP, n_perm=N_PERM,
    bonferroni_k=BONFERRONI_K, alpha_bonferroni=ALPHA_BON,
    python=platform.python_version(), numpy=np.__version__, scipy=__import__('scipy').__version__,
    corpus=dict(n_verses=len(verses), n_records_9=N9, n_records_17=N17,
                n_words_hadith9=NH_WORDS9, n_words_quran=sum(SUR_WORDS.values())),
    instrument=dict(span_primary=SPAN_PRIMARY, min_words=MINW,
                    fp_control_poetry_words=NP_WORDS,
                    fp_links_per_Mword={str(N): FP[N] / NP_WORDS * 1e6 for N in SPAN_ARMS},
                    hadith_links_per_Mword={
                        str(N): sum(len(v) for v in LINKS[(N, 'verse')]['dist'].values())
                        / NH_WORDS9 * 1e6 for N in SPAN_ARMS},
                    records_linked=len({i for v in prim_v["dist"].values() for i in v}),
                    naming_links=sum(len(v) for v in NAMING.values()),
                    book_share=dict(BOOK_SHARE)),
    published_reference=dict(rho_pub=RHO_PUB, note="H-NEW-860 Spearman(rubric, UAS_rank), N=36"),
    primary_arm=PRIMARY, all_arms=ARMS,
    nulls=dict(partial_spearman=dict(rho=pr, p=pp), stratified=NULLS,
               set_median_logwords=dict(observed=obs_med, frac_random_ge=frac_ge)),
    verdict=VERDICT, verdict_inputs=dict(rho_f=rho_f, p_f=p_f, same_sign=same_sign,
                                         clears_half_bar=bool(rho_f >= RHO_HALF),
                                         nulls_pass=bool(null_pass)),
    rubric_agreement=AGREE, top_overlap=OVERLAP, biggest_disagreements=BIGGEST,
    concentration=CONC, residual_roster=ROSTER, supplementary=SUPP,
    surah_counts={str(s): dict(quotation=SC[(SPAN_PRIMARY, 'Q')][s],
                               naming=SC[(SPAN_PRIMARY, 'N')][s],
                               union=SC[(SPAN_PRIMARY, 'U')][s],
                               rubric=RUB.get(s), uas=UAS[s], uas_rank=UAS_RANK[s],
                               outlier=OUT[s], words=SUR_WORDS[s], verses=SUR_VERSES[s])
                  for s in allS},
)
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(RESULT, f, ensure_ascii=False, indent=2, default=str)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOGLINES) + "\n")
INPUTS = [PREREG, QURAN, UAS_JSON, OUT590, RUBRIC, os.path.relpath(__file__, REPO)] + \
         [os.path.join(HDIR, "the_9_books", b + ".json") for b in BOOKS9] + \
         [os.path.join(HDIR, b + ".json") for b in BOOKS_OTHER]
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as f:
    f.write(f"H-NEW-860.1 run {STAMP}\nverdict: {VERDICT}\n\nINPUTS\n")
    for p in INPUTS:
        f.write(f"{sha256_file(p)}  {p}\n")
    f.write("\nOUTPUTS\n")
    for p in [DELIVERABLE, os.path.join(RUNDIR, "result.json")]:
        f.write(f"{sha256_file(p)}  {p}\n")
print(f"\nDONE. verdict={VERDICT}\nrundir {RUNDIR}\ndeliverable {DELIVERABLE}")
