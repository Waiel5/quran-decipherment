#!/usr/bin/env python3
"""H-NEW-2620 — cross-edition exegetical attention/disagreement per verse, and its
relation to per-surah structural extremeness.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-2620-tafsir-contested.md
The pre-reg SHA-256 is embedded below and verified at runtime; a mismatch aborts.

Author: Waiel Al-Shujaa.
Stdlib only (Investigation Protocol §7.1).
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
from datetime import datetime, timezone
from statistics import NormalDist

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2620-tafsir-contested.md")
EXPECTED_PREREG_SHA = "8826da50f861405478664097399264784bf52745a8986921c8290b23f600bc63"

MANIFEST = os.path.join(ROOT, "findings/phase-b-hypotheses/data/h-new-2620-tafsir-manifest.tsv")
EXPECTED_MANIFEST_SHA = "2ce03c91087fad7a357c130a496e2557a07dd6a6a1b6e8df8e8b7d15cf1bcff6"
MANIFEST_ROWS = 77437
MANIFEST_BYTES = 407169153

TAFSIR_ROOT = os.path.join(ROOT, "data/literature/classical-tafsir/spa5k-tafsir-api")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
H590 = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-590.json")
H840 = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-840.json")

EXPECTED_INPUT_SHA = {
    QURAN: "253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a",
    MORPH: "a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46",
    H590: "cf69308553ad2d60fee4a456c0979892e1b4f45bb36e8e044d40e261c1f4c476",
    H840: "e16a0f70aa842fbe650f2b14874a3f27b176193b86d7964fa9c6b76620ff2aa0",
}

# Pre-reg §1.3
AR_EDITIONS = [
    "ar-tafsir-al-tabari",
    "ar-tafseer-al-qurtubi",
    "ar-tafsir-ibn-kathir",
    "ar-tafsir-al-baghawi",
    "ar-tafseer-tanwir-al-miqbas",
    "ar-tafseer-al-saddi",
    "ar-tafsir-al-wasit",
    "ar-tafsir-muyassar",
]
AR_CLASSICAL = AR_EDITIONS[:5]  # pre-reg §6.1 — the five pre-modern Arabic editions
EN_EDITIONS = [
    "en-al-jalalayn",
    "en-tafisr-ibn-kathir",
    "en-tafsir-ibn-abbas",
    "en-tafsir-maarif-ul-quran",
]
EXCLUDED_EDITION = "en-asbab-al-nuzul-by-al-wahidi"  # pre-reg §1.3

# Pre-reg §3.1 / §7.7 — H-NEW-2320 census totals, asserted
EXPECTED_ROOT_TOKENS = 49968
EXPECTED_DISTINCT_ROOTS = 1642
EXPECTED_HAPAX_ROOTS = 395

N_PERM = 10000
BONFERRONI_K = 6
ALPHA_BON = 0.05 / BONFERRONI_K
SEED_BASE = 20260509  # I1..I6 -> 20260509..20260514 (pre-reg §4.5)
N_VERSES = 6236
N_SURAHS = 114

# Pre-reg §2.5 — dispute markers, already in normalised form
UNIGRAM_MARKERS = {
    "اختلف", "اختلفوا", "اختلفت", "اختلاف", "الاختلاف",
    "قيل", "قولان", "القولان", "قولين",
    "اقوال", "الاقوال", "وجهان", "الوجهان", "وجهين", "مذهبان",
}
BIGRAM_MARKERS = {
    ("قال", "اخرون"), ("قال", "بعضهم"), ("قالت", "طايفه"), ("قال", "قوم"),
}
DISPUTE_COVERAGE_GATE = 0.05  # pre-reg §2.5

ARABIC_WORD_RE = re.compile(r"[ء-ي]+")
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
WS_RE = re.compile(r"\s+")

NORM = NormalDist()


# --------------------------------------------------------------------------- #
# integrity
# --------------------------------------------------------------------------- #
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def die(msg):
    print("ABORT: " + msg, file=sys.stderr)
    sys.exit(1)


def verify_integrity():
    actual = sha256_file(PREREG)
    if actual != EXPECTED_PREREG_SHA:
        die("pre-reg SHA mismatch\n  expected %s\n  actual   %s" % (EXPECTED_PREREG_SHA, actual))
    print("[ok] pre-reg SHA-256 verified: %s" % actual)

    actual = sha256_file(MANIFEST)
    if actual != EXPECTED_MANIFEST_SHA:
        die("manifest SHA mismatch\n  expected %s\n  actual   %s" % (EXPECTED_MANIFEST_SHA, actual))
    print("[ok] tafsir manifest SHA-256 verified: %s" % actual)

    for path, expected in EXPECTED_INPUT_SHA.items():
        got = sha256_file(path)
        if got != expected:
            die("input SHA mismatch for %s\n  expected %s\n  actual   %s" % (path, expected, got))
    print("[ok] %d further input hashes verified" % len(EXPECTED_INPUT_SHA))


def load_manifest():
    table = {}
    total = 0
    with open(MANIFEST, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        if header != ["relpath", "sha256", "bytes"]:
            die("manifest header unexpected: %r" % (header,))
        for line in fh:
            rel, digest, nbytes = line.rstrip("\n").split("\t")
            table[rel] = digest
            total += int(nbytes)
    if len(table) != MANIFEST_ROWS:
        die("manifest row count %d != %d" % (len(table), MANIFEST_ROWS))
    if total != MANIFEST_BYTES:
        die("manifest byte total %d != %d" % (total, MANIFEST_BYTES))
    print("[ok] manifest loaded: %d files, %d bytes" % (len(table), total))
    return table


# --------------------------------------------------------------------------- #
# rank / stat helpers  (rank-based statistics only)
# --------------------------------------------------------------------------- #
def midranks(values):
    """1-based mid-ranks, ties averaged."""
    n = len(values)
    order = sorted(range(n), key=lambda i: values[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and values[order[j + 1]] == values[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pct_ranks(values):
    """Pre-reg §2.3: r = (mid_rank - 0.5)/n, in (0,1)."""
    n = len(values)
    return [(r - 0.5) / n for r in midranks(values)]


def normal_scores(values):
    """van der Waerden: z = Phi^-1(midrank/(n+1)). Pre-reg §3.2."""
    n = len(values)
    return [NORM.inv_cdf(r / (n + 1.0)) for r in midranks(values)]


def quantile_linear(sorted_vals, q):
    """numpy 'linear' quantile, stdlib implementation."""
    n = len(sorted_vals)
    if n == 1:
        return float(sorted_vals[0])
    pos = (n - 1) * q
    lo = int(math.floor(pos))
    hi = min(lo + 1, n - 1)
    frac = pos - lo
    return sorted_vals[lo] * (1.0 - frac) + sorted_vals[hi] * frac


def iqr(vals):
    s = sorted(vals)
    return quantile_linear(s, 0.75) - quantile_linear(s, 0.25)


def median(vals):
    s = sorted(vals)
    n = len(s)
    return s[n // 2] if n % 2 else 0.5 * (s[n // 2 - 1] + s[n // 2])


def solve_sym(a, b):
    """Solve a x = b for symmetric positive-definite a (Gaussian elimination)."""
    n = len(b)
    m = [row[:] + [b[i]] for i, row in enumerate(a)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(m[r][c]))
        if abs(m[piv][c]) < 1e-12:
            die("singular normal-equations matrix in OLS")
        m[c], m[piv] = m[piv], m[c]
        inv = 1.0 / m[c][c]
        for r in range(c + 1, n):
            f = m[r][c] * inv
            if f:
                for k in range(c, n + 1):
                    m[r][k] -= f * m[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        s = m[r][n] - sum(m[r][k] * x[k] for k in range(r + 1, n))
        x[r] = s / m[r][r]
    return x


def ols_residuals(y, cols):
    """Residuals of y on design [1] + cols. cols is a list of column vectors."""
    n = len(y)
    X = [[1.0] + [c[i] for c in cols] for i in range(n)]
    p = len(X[0])
    xtx = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(p)] for a in range(p)]
    xty = [sum(X[i][a] * y[i] for i in range(n)) for a in range(p)]
    beta = solve_sym(xtx, xty)
    return [y[i] - sum(beta[a] * X[i][a] for a in range(p)) for i in range(n)], beta


def r_squared(y, resid):
    ybar = sum(y) / len(y)
    ss_tot = sum((v - ybar) ** 2 for v in y)
    ss_res = sum(v * v for v in resid)
    return 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")


def pearson(a, b):
    n = len(a)
    ma = sum(a) / n
    mb = sum(b) / n
    num = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    da = math.sqrt(sum((v - ma) ** 2 for v in a))
    db = math.sqrt(sum((v - mb) ** 2 for v in b))
    return num / (da * db) if da > 0 and db > 0 else 0.0


def spearman(a, b):
    return pearson(midranks(a), midranks(b))


class PartialEngine:
    """Partial correlation of z(a) and z(b) after removing nuisance design X.

    r = a'Mb / sqrt(a'Ma * b'Mb) with M = I - X(X'X)^-1 X'.  Because a null
    permutation only reorders `a`, ||a||^2 is invariant and only X'a changes, so
    each permutation costs a handful of dot products. Identical code path is used
    for the observed value and every permutation.
    """

    def __init__(self, nuisance_cols, n):
        self.n = n
        self.X = [[1.0] + [c[i] for c in nuisance_cols] for i in range(n)]
        self.p = len(self.X[0])
        xtx = [[sum(self.X[i][a] * self.X[i][b] for i in range(n))
                for b in range(self.p)] for a in range(self.p)]
        self.xtx = xtx
        # explicit inverse of the small p x p matrix
        self.xtx_inv = []
        for j in range(self.p):
            e = [1.0 if k == j else 0.0 for k in range(self.p)]
            self.xtx_inv.append(solve_sym([row[:] for row in xtx], e))
        # xtx_inv is built column-wise; transpose to row-major
        self.xtx_inv = [[self.xtx_inv[c][r] for c in range(self.p)] for r in range(self.p)]

    def _xt(self, v):
        return [sum(self.X[i][a] * v[i] for i in range(self.n)) for a in range(self.p)]

    def _quad(self, u, w):
        return sum(u[a] * sum(self.xtx_inv[a][b] * w[b] for b in range(self.p))
                   for a in range(self.p))

    def prep(self, v):
        return {"v": v, "xt": self._xt(v), "ss": sum(x * x for x in v)}

    def corr(self, pa, pb):
        n = self.n
        a, b = pa["v"], pb["v"]
        amb = sum(a[i] * b[i] for i in range(n)) - self._quad(pa["xt"], pb["xt"])
        ama = pa["ss"] - self._quad(pa["xt"], pa["xt"])
        bmb = pb["ss"] - self._quad(pb["xt"], pb["xt"])
        if ama <= 0 or bmb <= 0:
            return 0.0
        return amb / math.sqrt(ama * bmb)


# --------------------------------------------------------------------------- #
# text normalisation
# --------------------------------------------------------------------------- #
def collapse(text):
    return WS_RE.sub(" ", text).strip()


_AR_MAP = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ى": "ي", "ة": "ه", "ؤ": "و", "ئ": "ي"}


def normalise_arabic(text):
    """Strip combining marks, then apply the pre-reg §2.5 letter folding."""
    stripped = "".join(c for c in unicodedata.normalize("NFD", text)
                       if not unicodedata.combining(c))
    return "".join(_AR_MAP.get(c, c) for c in stripped)


def count_markers(text):
    words = ARABIC_WORD_RE.findall(normalise_arabic(text))
    stripped = []
    for w in words:
        if len(w) > 1 and w[0] in ("و", "ف"):
            stripped.append(w[1:])
        else:
            stripped.append(w)
    total = sum(1 for w in stripped if w in UNIGRAM_MARKERS)
    total += sum(1 for i in range(len(stripped) - 1)
                 if (stripped[i], stripped[i + 1]) in BIGRAM_MARKERS)
    return total


# --------------------------------------------------------------------------- #
# loaders
# --------------------------------------------------------------------------- #
def load_quran():
    data = json.load(open(QURAN, encoding="utf-8"))
    if len(data) != N_SURAHS:
        die("quran-no-tashkeel.json has %d surahs" % len(data))
    keys, meta = [], {}
    for s in data:
        sid = s["id"]
        for v in s["verses"]:
            key = (sid, v["id"])
            keys.append(key)
            t = collapse(v["text"])
            meta[key] = {"len_char": len(t), "len_word": len(t.split(" ")) if t else 0}
    if len(keys) != N_VERSES:
        die("verse count %d != %d" % (len(keys), N_VERSES))
    return keys, meta


def load_qac(keys):
    root_freq = {}
    tokens = []  # (verse_key, root)
    with open(MORPH, encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            rm = ROOT_RE.search(parts[3])
            if not rm:
                continue
            rt = rm.group(1).strip()
            root_freq[rt] = root_freq.get(rt, 0) + 1
            tokens.append(((int(m.group(1)), int(m.group(2))), rt))

    hapax = {r for r, c in root_freq.items() if c == 1}
    if len(tokens) != EXPECTED_ROOT_TOKENS:
        die("root-bearing tokens %d != %d (H-NEW-2320)" % (len(tokens), EXPECTED_ROOT_TOKENS))
    if len(root_freq) != EXPECTED_DISTINCT_ROOTS:
        die("distinct roots %d != %d (H-NEW-2320)" % (len(root_freq), EXPECTED_DISTINCT_ROOTS))
    if len(hapax) != EXPECTED_HAPAX_ROOTS:
        die("hapax roots %d != %d (H-NEW-2320)" % (len(hapax), EXPECTED_HAPAX_ROOTS))
    frac = round(100.0 * len(hapax) / len(root_freq), 1)
    if frac != 24.1:
        die("hapax fraction %.1f%% != 24.1%% (H-NEW-2320)" % frac)
    print("[ok] QAC census reproduces H-NEW-2320: %d tokens, %d roots, %d hapax (%.1f%%)"
          % (len(tokens), len(root_freq), len(hapax), frac))

    n_hapax = {k: 0 for k in keys}
    rar_sum = {k: 0.0 for k in keys}
    rar_n = {k: 0 for k in keys}
    for key, rt in tokens:
        if key not in n_hapax:
            die("QAC location %r absent from quran text" % (key,))
        if rt in hapax:
            n_hapax[key] += 1
        rar_sum[key] += -math.log2(root_freq[rt] / float(len(tokens)))
        rar_n[key] += 1
    rarity = {k: (rar_sum[k] / rar_n[k] if rar_n[k] else 0.0) for k in keys}
    return n_hapax, rarity


def load_edition(edition, keys, manifest, arabic):
    """Return per-verse amortised length and amortised marker count for one edition."""
    raw_len, raw_mark, texts = {}, {}, {}
    empty = short = 0
    for (sid, vid) in keys:
        rel = "%s/%d/%d.json" % (edition, sid, vid)
        path = os.path.join(TAFSIR_ROOT, rel)
        if rel not in manifest:
            die("file not in frozen manifest: %s" % rel)
        with open(path, "rb") as fh:
            blob = fh.read()
        if hashlib.sha256(blob).hexdigest() != manifest[rel]:
            die("file content differs from frozen manifest: %s" % rel)
        obj = json.loads(blob.decode("utf-8"))
        t = collapse(obj["text"])
        texts[(sid, vid)] = t
        raw_len[(sid, vid)] = len(t)
        raw_mark[(sid, vid)] = count_markers(t) if arabic else 0
        if not t:
            empty += 1
        elif len(t) < 20:
            short += 1

    groups = {}
    for k, t in texts.items():
        groups.setdefault(t, []).append(k)
    gsize = {k: len(groups[t]) for k, t in texts.items()}
    in_group = sum(1 for k in keys if gsize[k] > 1)

    amort_len = {k: raw_len[k] / gsize[k] for k in keys}
    amort_mark = {k: raw_mark[k] / gsize[k] for k in keys}
    marker_verses = sum(1 for k in keys if raw_mark[k] > 0)

    cov = {
        "edition": edition,
        "files": len(keys),
        "empty": empty,
        "short_lt20": short,
        "distinct_blocks": len(groups),
        "verses_in_shared_blocks": in_group,
        "pct_in_shared_blocks": round(100.0 * in_group / len(keys), 2),
        "median_raw_len": median([raw_len[k] for k in keys]),
        "verses_with_marker": marker_verses,
        "pct_verses_with_marker": round(100.0 * marker_verses / len(keys), 2),
    }
    return amort_len, amort_mark, raw_len, cov


# --------------------------------------------------------------------------- #
# score assembly
# --------------------------------------------------------------------------- #
def build_scores(keys, per_ed_len, editions):
    ranks = {e: dict(zip(keys, pct_ranks([per_ed_len[e][k] for k in keys]))) for e in editions}
    A = [sum(ranks[e][k] for e in editions) / len(editions) for k in keys]
    D = [iqr([ranks[e][k] for e in editions]) for k in keys]
    return A, D, ranks


def build_dispute(keys, per_ed_mark, cov_by_ed, editions):
    eligible = [e for e in editions
                if cov_by_ed[e]["pct_verses_with_marker"] >= DISPUTE_COVERAGE_GATE * 100]
    if not eligible:
        die("no edition passes the dispute coverage gate")
    ranks = {e: pct_ranks([per_ed_mark[e][k] for k in keys]) for e in eligible}
    disp = [sum(ranks[e][i] for e in eligible) / len(eligible) for i in range(len(keys))]
    return disp, eligible


def residualise(keys, A, D, DISP, meta, n_hapax, rarity):
    z_len = normal_scores([meta[k]["len_char"] for k in keys])
    z_wrd = normal_scores([meta[k]["len_word"] for k in keys])
    z_hap = normal_scores([n_hapax[k] for k in keys])
    z_rar = normal_scores([rarity[k] for k in keys])
    base = [z_len, z_wrd, z_hap, z_rar]

    zA = normal_scores(A)
    zD = normal_scores(D)
    zP = normal_scores(DISP)

    rA, _ = ols_residuals(zA, base)
    rP, _ = ols_residuals(zP, base)
    # pre-reg §2.4/§3.2 — D additionally residualised on A and A^2
    zA2 = [v * v for v in zA]
    rD, _ = ols_residuals(zD, base + [zA, zA2])

    diag = {
        "R2_attention": r_squared(zA, rA),
        "R2_disagreement": r_squared(zD, rD),
        "R2_dispute": r_squared(zP, rP),
        "spearman_A_vs": {
            "len_char": spearman(A, [meta[k]["len_char"] for k in keys]),
            "len_word": spearman(A, [meta[k]["len_word"] for k in keys]),
            "n_hapax": spearman(A, [n_hapax[k] for k in keys]),
            "rarity": spearman(A, [rarity[k] for k in keys]),
        },
        "spearman_D_vs": {
            "len_char": spearman(D, [meta[k]["len_char"] for k in keys]),
            "A": spearman(D, A),
        },
        "spearman_DISPUTE_vs": {
            "len_char": spearman(DISP, [meta[k]["len_char"] for k in keys]),
            "n_hapax": spearman(DISP, [n_hapax[k] for k in keys]),
            "A": spearman(DISP, A),
        },
    }
    return rA, rD, rP, diag


def surah_aggregate(keys, values, how="median"):
    bysur = {}
    for k, v in zip(keys, values):
        bysur.setdefault(k[0], []).append(v)
    fn = median if how == "median" else (lambda xs: sum(xs) / len(xs))
    return [fn(bysur[s]) for s in range(1, N_SURAHS + 1)]


def run_inference(label, R_s, S_s, nuisance, seed, engine):
    zR = normal_scores(R_s)
    zS = normal_scores(S_s)
    pR = engine.prep(zR)
    obs = engine.corr(engine.prep(zS), pR)

    rng = random.Random(seed)
    perm = list(zS)
    ge = le = 0
    null_sum = 0.0
    for _ in range(N_PERM):
        rng.shuffle(perm)
        val = engine.corr(engine.prep(perm), pR)
        if val >= obs:
            ge += 1
        if val <= obs:
            le += 1
        null_sum += val
    p_one = (1 + ge) / (1.0 + N_PERM)
    p_lower = (1 + le) / (1.0 + N_PERM)
    return {
        "inference": label,
        "seed": seed,
        "n_perm": N_PERM,
        "partial_rho": obs,
        "bare_spearman": spearman(R_s, S_s),
        "p_one_sided_positive": p_one,
        "p_one_sided_negative": p_lower,
        "alpha_bonferroni": ALPHA_BON,
        "pass": bool(obs > 0 and p_one < ALPHA_BON),
        # a significant effect in the direction OPPOSITE to the locked one
        "reverse_direction_flag": bool(obs < 0 and p_lower < ALPHA_BON),
        "null_mean": null_sum / N_PERM,
    }


# --------------------------------------------------------------------------- #
def main():
    t0 = datetime.now(timezone.utc)
    stamp = t0.strftime("%Y%m%dT%H%M%SZ")
    outdir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2620", stamp)
    if os.path.exists(outdir):
        die("run directory already exists: %s" % outdir)
    # The directory is created only once every computation has succeeded, so that a
    # failed execution leaves no directory behind. Run directories, once created, are
    # never deleted or overwritten (pre-reg §8).
    print("[run] target %s" % outdir)

    verify_integrity()
    manifest = load_manifest()

    keys, meta = load_quran()
    n_hapax, rarity = load_qac(keys)

    # ---- structural instruments
    d590 = json.load(open(H590, encoding="utf-8"))
    rows590 = d590["all_surahs_results"]
    if len({r["X"] for r in rows590}) != N_SURAHS:
        die("h-new-590 does not cover 114 surahs")
    S590 = [abs([r for r in rows590 if r["X"] == s][0]["delta_pct"]) for s in range(1, 115)]
    d840 = json.load(open(H840, encoding="utf-8"))
    rows840 = {r["surah"]: r["UAS"] for r in d840["all_uas"]}
    if len(rows840) != N_SURAHS:
        die("h-new-840 does not cover 114 surahs")
    S840 = [rows840[s] for s in range(1, 115)]
    print("[ok] structural instruments loaded (H-NEW-590 |delta_pct|, H-NEW-840 UAS)")

    # ---- editions
    per_len, per_mark, per_raw, cov = {}, {}, {}, {}
    for ed in AR_EDITIONS + EN_EDITIONS:
        arabic = ed.startswith("ar-")
        a, m, r, c = load_edition(ed, keys, manifest, arabic)
        per_len[ed], per_mark[ed], per_raw[ed], cov[ed] = a, m, r, c
        print("[ok] %-30s blocks=%5d shared=%5d (%5.2f%%) marker%%=%5.2f"
              % (ed, c["distinct_blocks"], c["verses_in_shared_blocks"],
                 c["pct_in_shared_blocks"], c["pct_verses_with_marker"]))

    # excluded edition — coverage reported only (pre-reg §1.3)
    wah_dir = os.path.join(TAFSIR_ROOT, EXCLUDED_EDITION)
    wah_files = wah_surahs = 0
    for s in range(1, 115):
        d = os.path.join(wah_dir, str(s))
        if not os.path.isdir(d):
            continue
        n = len([f for f in os.listdir(d) if f.endswith(".json") and f != "empty_ayahs.json"])
        if n:
            wah_surahs += 1
            wah_files += n
    excluded_cov = {"edition": EXCLUDED_EDITION, "verses": wah_files, "surahs": wah_surahs,
                    "pct_of_corpus": round(100.0 * wah_files / N_VERSES, 2)}
    print("[ok] excluded %s: %d verses across %d surahs (%.2f%%)"
          % (EXCLUDED_EDITION, wah_files, wah_surahs, excluded_cov["pct_of_corpus"]))

    # ---- primary scores (8 Arabic)
    A, D, ranks = build_scores(keys, per_len, AR_EDITIONS)
    DISP, disp_eds = build_dispute(keys, per_mark, cov, AR_EDITIONS)
    print("[ok] dispute channel editions (>=5%% marker coverage): %s" % ", ".join(disp_eds))

    rA, rD, rP, diag = residualise(keys, A, D, DISP, meta, n_hapax, rarity)
    print("[H2] R2 attention=%.4f  disagreement=%.4f  dispute=%.4f"
          % (diag["R2_attention"], diag["R2_disagreement"], diag["R2_dispute"]))

    # positive control (pre-reg §6.8)
    pos_ctrl = spearman(A, [meta[k]["len_char"] for k in keys])
    print("[MW-6] positive control rho(A, verse length) = %.4f" % pos_ctrl)
    if pos_ctrl < 0.3:
        print("[WARN] positive control weak — instrument may be broken", file=sys.stderr)

    # ---- surah level nuisance design (pre-reg §4.2): mushaf position, and total
    # orthographic tokens in the surah.
    surah_tokens = [0] * N_SURAHS
    for k in keys:
        surah_tokens[k[0] - 1] += meta[k]["len_word"]
    nuis = [normal_scores([float(s) for s in range(1, 115)]),
            normal_scores([math.log(t) for t in surah_tokens])]
    engine = PartialEngine(nuis, N_SURAHS)

    # cross-check the algebraic identity against a direct OLS residual computation
    _chk_a, _ = ols_residuals(normal_scores(S590), nuis)
    _chk_b, _ = ols_residuals(normal_scores(surah_aggregate(keys, rA)), nuis)
    direct = pearson(_chk_a, _chk_b)
    fast = engine.corr(engine.prep(normal_scores(S590)),
                       engine.prep(normal_scores(surah_aggregate(keys, rA))))
    if abs(direct - fast) > 1e-9:
        die("partial-correlation identity check failed: %.12f vs %.12f" % (direct, fast))
    print("[ok] partial-correlation identity check passed (%.9f)" % direct)

    outcomes = {"A_resid": rA, "D_resid": rD, "DISPUTE_resid": rP}
    plan = [("I1", "A_resid", "S590", S590), ("I2", "A_resid", "S840", S840),
            ("I3", "D_resid", "S590", S590), ("I4", "D_resid", "S840", S840),
            ("I5", "DISPUTE_resid", "S590", S590), ("I6", "DISPUTE_resid", "S840", S840)]

    inferences = []
    for i, (tag, oname, sname, S) in enumerate(plan):
        R_s = surah_aggregate(keys, outcomes[oname])
        res = run_inference("%s: %s ~ %s" % (tag, oname, sname), R_s, S, nuis,
                            SEED_BASE + i, engine)
        res.update({"tag": tag, "outcome": oname, "structural": sname,
                    "locked_direction": "positive"})
        inferences.append(res)
        print("[%s] %-14s ~ %-5s  partial_rho=%+.4f  bare_rho=%+.4f  p=%.5f  %s"
              % (tag, oname, sname, res["partial_rho"], res["bare_spearman"],
                 res["p_one_sided_positive"], "PASS" if res["pass"] else "null"))

    # diagnostics: same tests on the UN-residualised scores (non-confirmatory)
    zA_raw = normal_scores(A)
    zD_raw = normal_scores(D)
    zP_raw = normal_scores(DISP)
    diagnostics = []
    for oname, vals in (("A_raw", zA_raw), ("D_raw", zD_raw), ("DISPUTE_raw", zP_raw)):
        for sname, S in (("S590", S590), ("S840", S840)):
            R_s = surah_aggregate(keys, vals)
            rho = engine.corr(engine.prep(normal_scores(S)),
                              engine.prep(normal_scores(R_s)))
            diagnostics.append({"outcome": oname, "structural": sname,
                                "partial_rho": rho, "bare_spearman": spearman(R_s, S),
                                "confirmatory": False})
            print("[diag] %-12s ~ %-5s partial_rho=%+.4f bare=%+.4f"
                  % (oname, sname, rho, spearman(R_s, S)))

    # ---- sensitivities
    sens = {}

    def quick(name, A_, D_, P_, use_dispute=True):
        ra, rd, rp, dg = residualise(keys, A_, D_, P_, meta, n_hapax, rarity)
        block = {"R2": {k: dg[k] for k in ("R2_attention", "R2_disagreement", "R2_dispute")}}
        for tag, vals in (("A_resid", ra), ("D_resid", rd), ("DISPUTE_resid", rp)):
            if tag == "DISPUTE_resid" and not use_dispute:
                continue
            for sname, S in (("S590", S590), ("S840", S840)):
                R_s = surah_aggregate(keys, vals)
                block["%s~%s" % (tag, sname)] = engine.corr(
                    engine.prep(normal_scores(S)), engine.prep(normal_scores(R_s)))
        sens[name] = block
        return block

    # S1 classical-only
    Ac, Dc, _ = build_scores(keys, per_len, AR_CLASSICAL)
    Pc, cls_eds = build_dispute(keys, per_mark, cov, AR_CLASSICAL)
    quick("S1_classical_only_5ed", Ac, Dc, Pc)
    sens["S1_classical_only_5ed"]["editions"] = AR_CLASSICAL
    sens["S1_classical_only_5ed"]["dispute_editions"] = cls_eds

    # S2 raw (un-amortised) length
    Ar, Dr, _ = build_scores(keys, per_raw, AR_EDITIONS)
    quick("S2_raw_unamortised", Ar, Dr, DISP)

    # S5 English set
    Ae, De, _ = build_scores(keys, per_len, EN_EDITIONS)
    quick("S5_english_4ed", Ae, De, DISP, use_dispute=False)
    sens["S5_english_4ed"]["editions"] = EN_EDITIONS
    sens["S5_english_4ed"]["caveat"] = (
        "en-tafisr-ibn-kathir 92.2% and en-tafsir-maarif-ul-quran 69.7% of verses sit in "
        "shared commentary blocks; this score largely measures the API's segmentation.")

    # S4 mean instead of median aggregation
    s4 = {}
    for tag, vals in (("A_resid", rA), ("D_resid", rD), ("DISPUTE_resid", rP)):
        for sname, S in (("S590", S590), ("S840", S840)):
            R_s = surah_aggregate(keys, vals, "mean")
            s4["%s~%s" % (tag, sname)] = engine.corr(
                engine.prep(normal_scores(S)), engine.prep(normal_scores(R_s)))
    sens["S4_mean_aggregation"] = s4

    # S6 leave-one-surah-out on I1 and I3
    loo = {}
    for tag, vals in (("I1_A_resid~S590", rA), ("I3_D_resid~S590", rD)):
        R_all = surah_aggregate(keys, vals)
        vs = []
        for drop in range(N_SURAHS):
            idx = [i for i in range(N_SURAHS) if i != drop]
            sub_n = [[c[i] for i in idx] for c in nuis]
            eng = PartialEngine(sub_n, N_SURAHS - 1)
            vs.append(eng.corr(eng.prep(normal_scores([S590[i] for i in idx])),
                               eng.prep(normal_scores([R_all[i] for i in idx]))))
        loo[tag] = {"min": min(vs), "max": max(vs), "observed": engine.corr(
            engine.prep(normal_scores(S590)), engine.prep(normal_scores(R_all)))}
    sens["S6_leave_one_surah_out"] = loo

    # S7 leave-one-edition-out on I1
    l1o = {}
    for drop in AR_EDITIONS:
        subset = [e for e in AR_EDITIONS if e != drop]
        Ax, _, _ = build_scores(keys, per_len, subset)
        rx, _, _, _ = residualise(keys, Ax, D, DISP, meta, n_hapax, rarity)
        l1o[drop] = engine.corr(engine.prep(normal_scores(S590)),
                                engine.prep(normal_scores(surah_aggregate(keys, rx))))
    sens["S7_leave_one_edition_out_I1"] = l1o

    print("[sens] complete: %s" % ", ".join(sorted(sens)))

    # ---- H4 rosters
    idx = list(range(len(keys)))
    ed_rank = {k: {e: ranks[e][k] for e in AR_EDITIONS} for k in keys}

    def row(i):
        k = keys[i]
        return {
            "surah": k[0], "verse": k[1], "ref": "Q %d:%d" % k,
            "A_resid": rA[i], "D_resid": rD[i], "DISPUTE_resid": rP[i],
            "A": A[i], "D": D[i], "DISPUTE": DISP[i],
            "len_char": meta[k]["len_char"], "len_word": meta[k]["len_word"],
            "n_hapax": n_hapax[k], "rarity": rarity[k],
            "S590_surah": S590[k[0] - 1], "S840_surah": S840[k[0] - 1],
            "edition_ranks": {e: round(ed_rank[k][e], 4) for e in AR_EDITIONS},
        }

    roster_A = [row(i) for i in sorted(idx, key=lambda i: (-rD[i], keys[i]))[:30]]
    roster_Ap = [row(i) for i in sorted(idx, key=lambda i: (-rP[i], keys[i]))[:30]]

    q590 = sorted(range(1, 115), key=lambda s: -S590[s - 1])[:28]
    q840 = sorted(range(1, 115), key=lambda s: -S840[s - 1])[:28]
    sub590 = [i for i in idx if keys[i][0] in set(q590)]
    sub840 = [i for i in idx if keys[i][0] in set(q840)]
    roster_B = [row(i) for i in sorted(sub590, key=lambda i: (rA[i], keys[i]))[:30]]
    roster_Bp = [row(i) for i in sorted(sub840, key=lambda i: (rA[i], keys[i]))[:30]]

    # ---- outputs
    os.makedirs(outdir)
    with open(os.path.join(outdir, "verse-scores.tsv"), "w", encoding="utf-8") as fh:
        fh.write("surah\tverse\tA\tD\tDISPUTE\tA_resid\tD_resid\tDISPUTE_resid"
                 "\tlen_char\tlen_word\tn_hapax\trarity\t"
                 + "\t".join(AR_EDITIONS) + "\n")
        for i, k in enumerate(keys):
            fh.write("%d\t%d\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%.6f\t%d\t%d\t%d\t%.6f\t%s\n"
                     % (k[0], k[1], A[i], D[i], DISP[i], rA[i], rD[i], rP[i],
                        meta[k]["len_char"], meta[k]["len_word"], n_hapax[k], rarity[k],
                        "\t".join("%.6f" % ed_rank[k][e] for e in AR_EDITIONS)))

    with open(os.path.join(outdir, "coverage.tsv"), "w", encoding="utf-8") as fh:
        cols = ["edition", "files", "empty", "short_lt20", "distinct_blocks",
                "verses_in_shared_blocks", "pct_in_shared_blocks", "median_raw_len",
                "verses_with_marker", "pct_verses_with_marker"]
        fh.write("\t".join(cols) + "\n")
        for ed in AR_EDITIONS + EN_EDITIONS:
            fh.write("\t".join(str(cov[ed][c]) for c in cols) + "\n")

    n_pass = sum(1 for r in inferences if r["pass"])
    result = {
        "id": "H-NEW-2620",
        "prereg_sha256": EXPECTED_PREREG_SHA,
        "tafsir_manifest_sha256": EXPECTED_MANIFEST_SHA,
        "tafsir_files_frozen": MANIFEST_ROWS,
        "seed_base": SEED_BASE,
        "n_perm": N_PERM,
        "bonferroni_k": BONFERRONI_K,
        "alpha_bonferroni": ALPHA_BON,
        "arabic_editions": AR_EDITIONS,
        "english_editions": EN_EDITIONS,
        "excluded_edition_coverage": excluded_cov,
        "dispute_channel_editions": disp_eds,
        "coverage": [cov[e] for e in AR_EDITIONS + EN_EDITIONS],
        "H2_residualisation": diag,
        "MW6_positive_control_rho_A_vs_len": pos_ctrl,
        "H3_inferences": inferences,
        "H3_family_verdict": ("NULL — 0/6 registered inferences pass" if n_pass == 0
                              else "%d/6 registered inferences pass" % n_pass),
        "diagnostics_unresidualised_NONCONFIRMATORY": diagnostics,
        "sensitivities": sens,
        "rosters": {
            "A_most_disagreement": roster_A,
            "A_prime_most_dispute_markers": roster_Ap,
            "B_structurally_extreme_exegetically_ignored_S590": roster_B,
            "B_prime_structurally_extreme_exegetically_ignored_S840": roster_Bp,
        },
    }
    with open(os.path.join(outdir, "result.json"), "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)
    with open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2620.json"),
              "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)

    manifest_out = {
        "utc_start": t0.isoformat(),
        "utc_end": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "script_sha256": sha256_file(os.path.abspath(__file__)),
        "prereg_sha256": EXPECTED_PREREG_SHA,
        "tafsir_manifest_sha256": EXPECTED_MANIFEST_SHA,
        "input_sha256": {os.path.relpath(p, ROOT): s for p, s in EXPECTED_INPUT_SHA.items()},
        "seeds": {("I%d" % (i + 1)): SEED_BASE + i for i in range(6)},
        "n_perm": N_PERM,
    }
    with open(os.path.join(outdir, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(manifest_out, fh, ensure_ascii=False, indent=2)

    print("\n[VERDICT] %s" % result["H3_family_verdict"])
    print("[done] %s" % outdir)


if __name__ == "__main__":
    main()
