#!/usr/bin/env python3
"""
H-NEW-2880 — the pausal-fāṣila question re-tested against a null matched on class
CONCENTRATION, not merely class COUNT.

H-NEW-2870's locked verdict is NULL and it stands. Its §9 established, post-hoc, that the
arm which produced that verdict was ill-posed: 57 of 57 null draws that beat the observation
were MORE concentrated than the real pausal partition, and agreement tracked each draw's own
chance floor at rho = +0.68. This runner rebuilds the null so that the concentration channel
has EXACTLY ZERO VARIANCE across draws, and gates itself on that fact before reporting any
p-value.

Pre-registration locked at
  findings/phase-b-hypotheses/prereg-h-new-2880-pausal-retest.md
  SHA-256 87083f50d56cd9802a5656ebc3049da98ee0397e6a0dda657e4d3dbbebe052ab
verified at runtime below. Frozen inputs SHA-256 verified, including the parent runner, whose
sections 0-6 are executed verbatim as the instrument so the two findings cannot drift apart.

Reporting order is locked by prereg §9:
  gates -> class-collapse magnitude -> ANTI-GAMING AUDIT -> the exact-null result -> the
  delta -> the three control texts -> per-surah.

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
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)

PREREG = "findings/phase-b-hypotheses/prereg-h-new-2880-pausal-retest.md"
PREREG_SHA256 = "87083f50d56cd9802a5656ebc3049da98ee0397e6a0dda657e4d3dbbebe052ab"
PARENT = "findings/phase-b-hypotheses/scripts/h-new-2870.py"

FROZEN = {
    PARENT:
        "9765a448256a93dc740ceb1dcd56ffbb58f33aa8a6192f855ad3579af07d2dde",
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
# prereg §8 enumerates 18 registered inferences.
BONFERRONI_K = 18
ALPHA = 0.05 / BONFERRONI_K
FLOOR_BAND = 0.02            # prereg §6 G4: +/-2% relative on the chance floor
MAX_REDRAW_RATE = 0.01       # prereg §5.2 / §6 G1
G2_MIN_RHO = 0.50            # prereg §6 G2
G3_MAX_ARI = 0.10            # prereg §6 G3
G3_MIN_SD = 0.001            # prereg §6 G3

SMOKE = "--smoke" in sys.argv
if SMOKE:
    N_PERM, N_RECUT, N_PROSE_CUT = 200, 20, 5

CHECKPOINT_DIR = os.path.join("scratch", "h-new-2880-checkpoints")   # OUTSIDE the run dir
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
    """prereg §13 / UNIT-DRIFT-DEFECT §7: snapshots go OUTSIDE the run directory, to
    distinct files that are never rewritten."""
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

# ---------------------------------------------------------------- 1. the instrument
# Sections 0-6 of the parent runner: SHA gates on its own frozen inputs, the phonemiser,
# the pausal conventions, both rime extractors, the corpus load, GATE A (orthography) and
# GATE B (instrument validation against H-NEW-2240). Executed verbatim; nothing is written.
say("\n" + "=" * 78)
say("INSTRUMENT — executing sections 0-6 of the pinned parent runner verbatim.")
say("Gates A and B below are the parent's, re-run, and are reported before any statistic.")
say("=" * 78)
_src = open(PARENT, encoding="utf-8").read()
_cut = _src.index("# ---------------------------------------------------------------- 7. the analysis")
NS = {"__name__": "instrument", "__file__": PARENT}
_stdout_lines = []


class _Tee:
    def __init__(self, real):
        self.real = real

    def write(self, s):
        self.real.write(s)
        _stdout_lines.append(s)

    def flush(self):
        self.real.flush()


_old = sys.stdout
sys.stdout = _Tee(_old)
try:
    exec(compile(_src[:_cut], "h-new-2870-instrument", "exec"), NS)
finally:
    sys.stdout = _old
LOG.extend("".join(_stdout_lines).rstrip("\n").split("\n"))

SURAHS, N_VERSES = NS["SURAHS"], NS["N_VERSES"]
flat = NS["flat"]
GATE_A = {"checks": NS["gate_a"], "pass": NS["gate_a_pass"]}
GATE_B = {"checks": NS["gate_b"], "n_pass": NS["gate_b_pass"]}
if not GATE_A["pass"] or GATE_B["n_pass"] != 6:
    die("parent gate failed — instrument broken (prereg §12)")

PAIRS = [(sid, i) for sid, _, _, vs in SURAHS for i in range(len(vs) - 1)]
N_PAIRS = len(PAIRS)
CONVS = ["C", "P1", "P2", "P3"]

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


def set_variant(v):
    exec(f"RIME_VARIANT = {v!r}", NS)


def keff(labels):
    n = len(labels)
    h = -sum((v / n) * math.log(v / n) for v in Counter(labels).values())
    return math.exp(h)


def floor_of(sizes):
    """Chance floor sum(p_i^2), summed over sizes in DESCENDING order so that two
    partitions with the identical size multiset give bit-identical floats."""
    return float(sum((s / N_VERSES) ** 2 for s in sorted((int(x) for x in sizes), reverse=True)))


def ari(a, b, ka, kb):
    """Adjusted Rand index between two labellings of the same M citation types."""
    a = np.asarray(a, dtype=np.int64)
    b = np.asarray(b, dtype=np.int64)
    n = len(a)
    tab = np.bincount(a * kb + b, minlength=ka * kb).astype(np.float64)
    c2 = lambda v: v * (v - 1.0) / 2.0
    idx = c2(tab).sum()
    ea = c2(np.bincount(a, minlength=ka).astype(np.float64)).sum()
    eb = c2(np.bincount(b, minlength=kb).astype(np.float64)).sum()
    exp = ea * eb / c2(float(n))
    mx = (ea + eb) / 2.0
    return float((idx - exp) / (mx - exp)) if mx != exp else 1.0


# ---------------------------------------------------------------- 2. labels
say("\n" + "=" * 78)
say("RESULT 1 — CLASS-COLLAPSE MAGNITUDE. Reported before any headline number (prereg §9).")
say("=" * 78)

LABS, FLATS, AGREE, DELTA, FLOOR, COLLAPSE, MAPVIOL = {}, {}, {}, {}, {}, {}, {}
for variant in ("R2", "R1"):
    set_variant(variant)
    rime_of = NS["rime_of"]
    LABS[variant] = {c: {sid: [rime_of(t, c) for t in vs] for sid, _, _, vs in SURAHS}
                     for c in CONVS}
    FLATS[variant] = {c: [x for sid, _, _, _ in SURAHS for x in LABS[variant][c][sid]]
                      for c in CONVS}
    L, F = LABS[variant], FLATS[variant]
    AGREE[variant] = {c: sum(1 for sid, i in PAIRS if L[c][sid][i] == L[c][sid][i + 1]) / N_PAIRS
                      for c in CONVS}
    DELTA[variant] = {p: AGREE[variant][p] - AGREE[variant]["C"] for p in ("P1", "P2", "P3")}
    FLOOR[variant] = {c: floor_of(Counter(F[c]).values()) for c in CONVS}
    COLLAPSE[variant] = {c: {"K": len(set(F[c])), "K_eff": keff(F[c])} for c in CONVS}
    say(f"\n   --- rime {variant} "
        f"({'tanwin-transparent repair — PRIMARY' if variant == 'R2' else 'as pre-registered by the parent'})")
    for c in CONVS:
        say(f"      {c:3s} K={COLLAPSE[variant][c]['K']:5d}  "
            f"K_eff={COLLAPSE[variant][c]['K_eff']:8.3f}  "
            f"chance floor sum(p^2)={FLOOR[variant][c]:.6f}  A={AGREE[variant][c]:.4f}")
    for p in ("P1", "P2", "P3"):
        COLLAPSE[variant][p]["collapse_K"] = COLLAPSE[variant]["C"]["K"] / COLLAPSE[variant][p]["K"]
        COLLAPSE[variant][p]["collapse_Keff"] = (COLLAPSE[variant]["C"]["K_eff"]
                                                 / COLLAPSE[variant][p]["K_eff"])
        say(f"      collapse C->{p}: K {COLLAPSE[variant]['C']['K']}/{COLLAPSE[variant][p]['K']} "
            f"= {COLLAPSE[variant][p]['collapse_K']:.3f}x   "
            f"K_eff {COLLAPSE[variant][p]['collapse_Keff']:.3f}x   "
            f"free arithmetic gain = {FLOOR[variant][p] - FLOOR[variant]['C']:+.4f}   "
            f"observed Δ = {DELTA[variant][p]:+.4f}")
    MAPVIOL[variant] = {}
    for p in ("P1", "P2"):
        m = defaultdict(set)
        for cl, pl in zip(F["C"], F[p]):
            m[cl].add(pl)
        sp = {k for k, v in m.items() if len(v) > 1}
        nv = sum(1 for cl in F["C"] if cl in sp)
        MAPVIOL[variant][p] = {"split_types": len(sp), "verses": nv, "rate": nv / N_VERSES}
        say(f"      map C->{p}: {len(sp)} citation types split, {nv} verses "
            f"({nv / N_VERSES:.4f}) — the null of §5 is defined only when this is 0")

say("\n   DECOMPOSITION of the delta (rime R2, tuple P1), restated from the parent:")
_d = DELTA["R2"]["P1"]
_ar = FLOOR["R2"]["P1"] - FLOOR["R2"]["C"]
say(f"      Δ = {_d:+.4f}   arithmetic (chance-collision) {_ar:+.4f} = {100 * _ar / _d:.1f}%"
    f"   compositional {_d - _ar:+.4f} = {100 * (_d - _ar) / _d:.1f}%")
checkpoint("collapse", {"agreement": AGREE, "delta": DELTA, "floor": FLOOR,
                        "collapse": COLLAPSE, "map_violation": MAPVIOL})

# ---------------------------------------------------------------- 3. the null machinery (R2)
set_variant("R2")
F2 = FLATS["R2"]
L2 = LABS["R2"]
CIT = sorted(set(F2["C"]))
CIDX = {t: i for i, t in enumerate(CIT)}
M = len(CIT)
SIZE = [0] * M
for t in F2["C"]:
    SIZE[CIDX[t]] += 1
SIZE_A = np.asarray(SIZE, dtype=np.float64)
PA = np.array([CIDX[L2["C"][sid][i]] for sid, i in PAIRS], dtype=np.int32)
PB = np.array([CIDX[L2["C"][sid][i + 1]] for sid, i in PAIRS], dtype=np.int32)
# N-STEM mask (prereg §5.5): adjacent pairs whose two ends differ under P3, the
# truncation-only tuple — pairs that cannot be merged by truncating a shared skeleton.
P3L = L2["P3"]
STEM_MASK = np.array([P3L[sid][i] != P3L[sid][i + 1] for sid, i in PAIRS], dtype=bool)
N_STEM_PAIRS = int(STEM_MASK.sum())

# descending-size processing order with random tie-breaking inside equal-size groups
_ord = sorted(range(M), key=lambda i: -SIZE[i])
SIZE_GROUPS = []
_i = 0
while _i < M:
    _j = _i
    while _j < M and SIZE[_ord[_j]] == SIZE[_ord[_i]]:
        _j += 1
    SIZE_GROUPS.append(_ord[_i:_j])
    _i = _j


class Tuple2:
    """Everything the exact nulls need for one pausal tuple under rime R2."""

    def __init__(self, conv):
        self.conv = conv
        blocks = sorted(set(F2[conv]))
        self.BIDX = {b: i for i, b in enumerate(blocks)}
        self.K = len(blocks)
        amap = {}
        for ct, pt in zip(F2["C"], F2[conv]):
            j = CIDX[ct]
            if j in amap and amap[j] != self.BIDX[pt]:
                die(f"{conv}: the pausal partition is not a coarsening of the citation "
                    f"partition — the null of prereg §5 is undefined (prereg §4.1)")
            amap[j] = self.BIDX[pt]
        self.OBS = np.array([amap[i] for i in range(M)], dtype=np.int32)
        self.tgt = np.bincount(self.OBS, weights=SIZE_A, minlength=self.K).astype(np.int64)
        if int(self.tgt.sum()) != N_VERSES:
            die(f"{conv}: block sizes do not sum to {N_VERSES}")
        chk = np.array([sum(1 for x in F2[conv] if self.BIDX[x] == k) for k in range(self.K)])
        if not np.array_equal(chk, self.tgt):
            die(f"{conv}: reconstructed block sizes differ from the observed ones")
        self.tgt_sorted = np.sort(self.tgt)[::-1]
        self.floor_obs = floor_of(self.tgt)
        self.A_obs = AGREE["R2"][conv]
        self.E_obs = self.A_obs - self.floor_obs
        self.stem_obs = (float(np.count_nonzero((self.OBS[PA] == self.OBS[PB]) & STEM_MASK))
                         / N_STEM_PAIRS)
        self.cards = np.bincount(self.OBS, minlength=self.K).astype(np.int64)


TUP = {c: Tuple2(c) for c in ("P1", "P2")}


def draw_exact(scheme, T, rng):
    """prereg §5.2. Returns (blk, ok) where ok is True iff the achieved block-size
    multiset is identical to the target. Types are placed largest-first with random
    tie-breaking inside each equal-size group."""
    rem = T.tgt.copy()
    blk = np.empty(M, dtype=np.int32)
    K = T.K
    for grp in SIZE_GROUPS:
        g = grp if len(grp) == 1 else rng.sample(grp, len(grp))
        for t in g:
            s = SIZE[t]
            if scheme == "S2":
                w = np.where(rem >= s, rem, 0)
                tot = int(w.sum())
                if tot > 0:
                    cw = np.cumsum(w)
                    k = int(np.searchsorted(cw, rng.random() * tot, side="right"))
                    if k >= K:
                        k = K - 1
                else:
                    k = int(rem.argmax())
            elif scheme == "S1":
                mx = rem.max()
                ks = np.flatnonzero(rem == mx)
                k = int(ks[rng.randrange(len(ks))])
            elif scheme == "S5":
                elig = rem >= s
                if elig.any():
                    r = np.where(elig, rem, 1 << 40)
                    mn = r.min()
                    ks = np.flatnonzero(r == mn)
                    k = int(ks[rng.randrange(len(ks))])
                else:
                    k = int(rem.argmax())
            else:
                raise ValueError(scheme)
            blk[t] = k
            rem[k] -= s
    ach = np.bincount(blk, weights=SIZE_A, minlength=K).astype(np.int64)
    ok = bool(np.array_equal(np.sort(ach)[::-1], T.tgt_sorted))
    return blk, ok, ach


def draw_na(T, rng):
    """prereg §5.4 — exact within-size-class permutation of the observed block labels."""
    blk = T.OBS.copy()
    for grp in SIZE_GROUPS:
        if len(grp) < 2:
            continue
        lab = [int(blk[t]) for t in grp]
        rng.shuffle(lab)
        for t, l in zip(grp, lab):
            blk[t] = l
    ach = np.bincount(blk, weights=SIZE_A, minlength=T.K).astype(np.int64)
    return blk, bool(np.array_equal(np.sort(ach)[::-1], T.tgt_sorted)), ach


def run_exact_null(scheme, T, seed, n_perm, want_ari=True, want_stem=False):
    rng = random.Random(seed)
    A, FL, ARI, STEM = [], [], [], []
    redraw = 0
    elementwise_exact = True
    for i in range(n_perm):
        for _ in range(50):
            blk, ok, ach = (draw_na(T, rng) if scheme == "NA"
                            else draw_exact(scheme, T, rng))
            if ok:
                break
            redraw += 1
        else:
            die(f"{scheme}/{T.conv}: 50 consecutive draws failed exactness")
        if not np.array_equal(ach, T.tgt):
            elementwise_exact = False
        A.append(float(np.count_nonzero(blk[PA] == blk[PB])) / N_PAIRS)
        FL.append(floor_of(ach))
        if want_stem:
            STEM.append(float(np.count_nonzero((blk[PA] == blk[PB]) & STEM_MASK))
                        / N_STEM_PAIRS)
        if want_ari:
            ARI.append(ari(blk, T.OBS, T.K, T.K))
        if (i + 1) % 2500 == 0:
            say(f"        .. {scheme}/{T.conv}/seed{seed}: {i + 1}/{n_perm}")
    A = np.asarray(A)
    FL = np.asarray(FL)
    E = A - FL
    p_E = (1 + int((E >= T.E_obs - 1e-15).sum())) / (1 + n_perm)
    p_A = (1 + int((A >= T.A_obs - 1e-15).sum())) / (1 + n_perm)
    inband = float(np.mean(np.abs(FL - T.floor_obs) <= FLOOR_BAND * T.floor_obs))
    beat = A >= T.A_obs - 1e-15
    out = {
        "scheme": scheme, "conv": T.conv, "seed": seed, "n_perm": n_perm,
        "redraws": redraw, "redraw_rate": redraw / max(n_perm + redraw, 1),
        "block_sizes_elementwise_identical": elementwise_exact,
        "observed_A": T.A_obs, "observed_E": T.E_obs, "observed_floor": T.floor_obs,
        "null_A_mean": float(A.mean()), "null_A_sd": float(A.std()),
        "null_A_min": float(A.min()), "null_A_max": float(A.max()),
        "null_E_mean": float(E.mean()), "null_E_sd": float(E.std()),
        "null_E_max": float(E.max()),
        "null_floor_mean": float(FL.mean()), "null_floor_sd": float(FL.std()),
        "null_floor_max_abs_dev": float(np.abs(FL - T.floor_obs).max()),
        "floor_in_band_share": inband,
        "n_ge_observed_E": int((E >= T.E_obs - 1e-15).sum()),
        "n_ge_observed_A": int(beat.sum()),
        "p_E": p_E, "p_A": p_A,
        "z_E": float((T.E_obs - E.mean()) / E.std()) if E.std() > 0 else float("nan"),
        "corr_A_floor": (float(np.corrcoef(A, FL)[0, 1]) if FL.std() > 0 else None),
        "corr_A_floor_note": ("UNDEFINED — the chance floor has exactly zero variance across "
                              "draws, which is the point of the construction"
                              if FL.std() == 0 else "defined; the floor varies"),
        "beat_floor_mean": (float(FL[beat].mean()) if beat.any() else None),
        "beat_more_concentrated_than_observed": int((FL[beat] > T.floor_obs).sum()) if beat.any() else 0,
        "mean_ARI_vs_observed": (float(np.mean(ARI)) if ARI else None),
        "max_ARI_vs_observed": (float(np.max(ARI)) if ARI else None),
    }
    if want_stem:
        S = np.asarray(STEM)
        out["stem_observed"] = T.stem_obs
        out["stem_null_mean"] = float(S.mean())
        out["stem_null_sd"] = float(S.std())
        out["stem_null_max"] = float(S.max())
        out["stem_n_ge"] = int((S >= T.stem_obs - 1e-15).sum())
        out["stem_p"] = (1 + out["stem_n_ge"]) / (1 + n_perm)
        out["n_stem_pairs"] = N_STEM_PAIRS
    return out


# --- the parent's two nulls, re-implemented verbatim, as DIAGNOSTICS ONLY (prereg §5.7)
def parent_n1a(T, seed, n_perm):
    target_sizes = sorted(Counter(F2[T.conv]).values(), reverse=True)
    rng = random.Random(seed)
    K = len(target_sizes)
    tgt = np.asarray(target_sizes, dtype=np.int64)
    order = list(range(M))
    A, FL, TV = [], [], []
    for _ in range(n_perm):
        rng.shuffle(order)
        heap = [(-target_sizes[k], k) for k in range(K)]
        heapq.heapify(heap)
        blk = [0] * M
        for t in order:
            negrem, k = heapq.heappop(heap)
            blk[t] = k
            heapq.heappush(heap, (negrem + SIZE[t], k))
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
        b = np.asarray(blk, dtype=np.int32)
        ach = np.bincount(b, weights=SIZE_A, minlength=K).astype(np.int64)
        TV.append(0.5 * float(np.abs(ach - tgt).sum()) / N_VERSES)
        A.append(float(np.count_nonzero(b[PA] == b[PB])) / N_PAIRS)
        FL.append(floor_of(ach))
    return np.asarray(A), np.asarray(FL), float(np.mean(TV))


def parent_n1b(T, seed, n_perm):
    grp = defaultdict(Counter)
    for ct, pt in zip(F2["C"], F2[T.conv]):
        grp[ct][pt] += 1
    blocks = defaultdict(list)
    for ct, c in grp.items():
        blocks[c.most_common(1)[0][0]].append(ct)
    cards = [len(v) for v in blocks.values()]
    K = len(cards)
    rng = random.Random(seed)
    order = list(range(M))
    A, FL = [], []
    for _ in range(n_perm):
        rng.shuffle(order)
        blk = [0] * M
        pos = 0
        for k, c in enumerate(cards):
            for t in order[pos:pos + c]:
                blk[t] = k
            pos += c
        b = np.asarray(blk, dtype=np.int32)
        ach = np.bincount(b, weights=SIZE_A, minlength=K).astype(np.int64)
        A.append(float(np.count_nonzero(b[PA] == b[PB])) / N_PAIRS)
        FL.append(floor_of(ach))
    return np.asarray(A), np.asarray(FL)


# ---------------------------------------------------------------- 4. ANTI-GAMING AUDIT
say("\n" + "=" * 78)
say("RESULT 2 — THE ANTI-GAMING AUDIT (prereg §6). Printed BEFORE any p-value.")
say("=" * 78)
say(f"   the real pausal partition's chance floor: P1 = {TUP['P1'].floor_obs:.6f}   "
    f"P2 = {TUP['P2'].floor_obs:.6f}")
say(f"   M = {M} citation types  ->  K = {TUP['P1'].K} (P1) / {TUP['P2'].K} (P2) pausal classes")
say(f"   adjacent pairs = {N_PAIRS}; of these {N_STEM_PAIRS} differ under the "
    f"truncation-only tuple P3 (the N-STEM sub-population)")

AUDIT = {"parent_nulls": {}, "exact_nulls": {}}
say("\n   (a) THE PARENT'S TWO NULLS, re-implemented verbatim — diagnostics only, gate nothing")
for cv in ("P1", "P2"):
    T = TUP[cv]
    A, FL, tv = parent_n1a(T, SEED, N_PERM)
    beat = A >= T.A_obs - 1e-15
    rho = float(np.corrcoef(A, FL)[0, 1])
    inb = float(np.mean(np.abs(FL - T.floor_obs) <= FLOOR_BAND * T.floor_obs))
    AUDIT["parent_nulls"][f"N1a_{cv}"] = {
        "profile_TV": tv, "floor_mean": float(FL.mean()), "floor_sd": float(FL.std()),
        "floor_min": float(FL.min()), "floor_max": float(FL.max()),
        "floor_in_band_share": inb, "corr_A_floor": rho,
        "n_beat": int(beat.sum()),
        "beat_floor_mean": float(FL[beat].mean()) if beat.any() else None,
        "beat_more_concentrated": int((FL[beat] > T.floor_obs).sum()) if beat.any() else 0,
        "observed_floor": T.floor_obs, "p_A_as_parent": (1 + int(beat.sum())) / (1 + N_PERM)}
    d = AUDIT["parent_nulls"][f"N1a_{cv}"]
    say(f"      N1-a {cv}: profile TV={tv:.4f}  floor mean={FL.mean():.4f} "
        f"(sd {FL.std():.4f}, range {FL.min():.4f}-{FL.max():.4f}) vs observed "
        f"{T.floor_obs:.4f}")
    say(f"               floor within ±2% of the observed: {100 * inb:.2f}% of draws | "
        f"corr(A_null, floor_null) = {rho:+.4f}")
    say(f"               draws beating the observation: {int(beat.sum())}; their mean floor "
        f"{d['beat_floor_mean'] if d['beat_floor_mean'] is None else round(d['beat_floor_mean'], 4)}"
        f"; more concentrated than the real partition: {d['beat_more_concentrated']}"
        f"/{int(beat.sum())}")
    A, FL = parent_n1b(T, SEED, N_PERM)
    E = A - FL
    rho = float(np.corrcoef(A, FL)[0, 1])
    inb = float(np.mean(np.abs(FL - T.floor_obs) <= FLOOR_BAND * T.floor_obs))
    AUDIT["parent_nulls"][f"N1b_{cv}"] = {
        "floor_mean": float(FL.mean()), "floor_sd": float(FL.std()),
        "floor_in_band_share": inb, "corr_A_floor": rho,
        "null_E_mean": float(E.mean()),
        "p_E_as_parent": (1 + int((E >= T.E_obs - 1e-15).sum())) / (1 + N_PERM),
        "observed_floor": T.floor_obs}
    say(f"      N1-b {cv}: floor mean={FL.mean():.4f} (sd {FL.std():.4f}) vs observed "
        f"{T.floor_obs:.4f} | within ±2%: {100 * inb:.2f}% | "
        f"corr(A_null, floor_null) = {rho:+.4f}")

rho_g2 = max(AUDIT["parent_nulls"][f"N1a_{c}"]["corr_A_floor"] for c in ("P1", "P2"))
G2_PASS = rho_g2 >= G2_MIN_RHO
say(f"\n   GATE G2 — does the diagnostic have teeth? corr(A_null, floor_null) on the known-"
    f"defective N1-a = {rho_g2:+.4f}, required >= {G2_MIN_RHO:+.2f}: "
    f"{'PASS' if G2_PASS else 'FAIL'}")
if not G2_PASS:
    die("G2 failed — the concentration diagnostic cannot see a defect known to be present "
        "(prereg §6, §12). Stopping.")
checkpoint("audit-parent", AUDIT["parent_nulls"])

# ---------------------------------------------------------------- 5. THE EXACT NULLS
say("\n" + "=" * 78)
say("RESULT 3 — THE EXACT-CONCENTRATION NULLS (prereg §5.2). S2 is primary.")
say("=" * 78)
EXACT = {}
for scheme in ("S2", "S1", "S5"):
    for cv in ("P1", "P2"):
        T = TUP[cv]
        for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
            r = run_exact_null(scheme, T, sd, N_PERM,
                               want_stem=(scheme == "S2" and tag == "primary"))
            EXACT[f"{scheme}_{cv}_{tag}"] = r
            say(f"   {scheme} {cv} [{tag} seed={sd}]  E_obs={r['observed_E']:.4f} | "
                f"null E mean={r['null_E_mean']:.4f} sd={r['null_E_sd']:.4f} "
                f"max={r['null_E_max']:.4f} | #>=obs={r['n_ge_observed_E']} "
                f"p={r['p_E']:.5f} z={r['z_E']:+.2f}")
            say(f"        A_obs={r['observed_A']:.4f} null A mean={r['null_A_mean']:.4f} "
                f"sd={r['null_A_sd']:.4f} max={r['null_A_max']:.4f} p_A={r['p_A']:.5f} | "
                f"floor dev max={r['null_floor_max_abs_dev']:.2e} in-band="
                f"{100 * r['floor_in_band_share']:.1f}% | redraws={r['redraws']} | "
                f"mean ARI vs observed={r['mean_ARI_vs_observed']:.4f}")
            checkpoint(f"exact-{scheme}-{cv}-{tag}", r)

say("\n   N-A — exact within-size-class permutation (prereg §5.4). LOW POWER, NON-GATING.")
_bysz = defaultdict(list)
for _t, _s in enumerate(SIZE):
    _bysz[_s].append(_t)
_mov = [t for s, ts in _bysz.items() if len(ts) >= 2
        and len({int(TUP['P1'].OBS[t]) for t in ts}) >= 2 for t in ts]
NA_FREEDOM = {"movable_types": len(_mov), "M": M, "movable_type_share": len(_mov) / M,
              "movable_verses": sum(SIZE[t] for t in _mov), "N_verses": N_VERSES,
              "movable_verse_share": sum(SIZE[t] for t in _mov) / N_VERSES}
say(f"      measured freedom: {NA_FREEDOM['movable_types']}/{M} types movable "
    f"({NA_FREEDOM['movable_type_share']:.3f}) carrying "
    f"{NA_FREEDOM['movable_verses']}/{N_VERSES} verses "
    f"({NA_FREEDOM['movable_verse_share']:.3f}) — declared in prereg §5.4 before locking")
for cv in ("P1", "P2"):
    for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
        r = run_exact_null("NA", TUP[cv], sd, N_PERM)
        EXACT[f"NA_{cv}_{tag}"] = r
        say(f"      NA {cv} [{tag}] E_obs={r['observed_E']:.4f} null E mean="
            f"{r['null_E_mean']:.4f} sd={r['null_E_sd']:.4f} max={r['null_E_max']:.4f} "
            f"#>=obs={r['n_ge_observed_E']} p={r['p_E']:.5f} z={r['z_E']:+.2f} | "
            f"floor dev max={r['null_floor_max_abs_dev']:.2e} | "
            f"mean ARI={r['mean_ARI_vs_observed']:.4f}")

say("\n   N-STEM — the lexical-repetition control (prereg §5.5). NON-GATING.")
for cv in ("P1", "P2"):
    r = EXACT[f"S2_{cv}_primary"]
    say(f"      {cv}: on the {r['n_stem_pairs']} adjacent pairs that DIFFER under the "
        f"truncation-only tuple P3 —")
    say(f"          observed merge rate {r['stem_observed']:.4f} | null mean "
        f"{r['stem_null_mean']:.4f} sd {r['stem_null_sd']:.4f} max {r['stem_null_max']:.4f} "
        f"| #>=obs={r['stem_n_ge']} p={r['stem_p']:.5f}")

# --- gates G1, G3, G4
G1_ITEMS = {k: v for k, v in EXACT.items()}
G1_PASS = all(v["null_floor_max_abs_dev"] == 0.0 and v["redraw_rate"] < MAX_REDRAW_RATE
              and v["p_E"] == v["p_A"] for v in G1_ITEMS.values())
G3_PASS = all(v["mean_ARI_vs_observed"] is not None
              and v["mean_ARI_vs_observed"] < G3_MAX_ARI
              and v["null_A_sd"] > G3_MIN_SD for v in G1_ITEMS.values())
G4 = {k: v["floor_in_band_share"] for k, v in G1_ITEMS.items()}
G4_PASS = all(x == 1.0 for x in G4.values())
say("\n   " + "-" * 74)
say("   GATES (prereg §6), printed before the verdict:")
say(f"      G1 exactness  : {'PASS' if G1_PASS else 'FAIL'}  — every draw's chance floor "
    f"deviates from the observed by exactly "
    f"{max(v['null_floor_max_abs_dev'] for v in G1_ITEMS.values()):.2e}; "
    f"max redraw rate {max(v['redraw_rate'] for v in G1_ITEMS.values()):.5f}; "
    f"p(E) == p(A) in every arm: "
    f"{all(v['p_E'] == v['p_A'] for v in G1_ITEMS.values())}")
say(f"      G2 teeth      : {'PASS' if G2_PASS else 'FAIL'}  — rho on the known-defective "
    f"N1-a = {rho_g2:+.4f}")
say(f"      G3 non-degen  : {'PASS' if G3_PASS else 'FAIL'}  — max mean ARI vs the real "
    f"partition = {max(v['mean_ARI_vs_observed'] for v in G1_ITEMS.values()):+.4f} "
    f"(< {G3_MAX_ARI}); min sd(A_null) = "
    f"{min(v['null_A_sd'] for v in G1_ITEMS.values()):.5f} (> {G3_MIN_SD})")
say(f"      G4 in-band    : {'PASS' if G4_PASS else 'FAIL'}  — share of exact-null draws "
    f"whose floor is within ±2% of the observed = "
    f"{100 * min(G4.values()):.1f}% (N1-a: "
    f"{100 * min(AUDIT['parent_nulls'][f'N1a_{c}']['floor_in_band_share'] for c in ('P1', 'P2')):.2f}%"
    f", N1-b: "
    f"{100 * min(AUDIT['parent_nulls'][f'N1b_{c}']['floor_in_band_share'] for c in ('P1', 'P2')):.2f}%)")
say("      corr(A_null, floor_null) for the exact nulls: UNDEFINED — the chance floor has "
    "exactly zero variance across draws.")
say("      Every exact-null draw carries the identical block-size multiset, hence the "
    "identical K, K_eff, maximum class size and Simpson index.")
if not (G1_PASS and G3_PASS):
    die("G1 or G3 failed — the null is defective or degenerate; no p-value may be reported "
        "(prereg §6, §12).")
AUDIT["gates"] = {"G1": G1_PASS, "G2": G2_PASS, "G3": G3_PASS, "G4": G4_PASS,
                  "G2_rho": rho_g2, "G4_shares": G4, "NA_freedom": NA_FREEDOM}
checkpoint("exact-all", EXACT)

# ---------------------------------------------------------------- 6. controls
say("\n" + "=" * 78)
say("RESULT 4 — CONTROLS RETAINED FROM THE PARENT (prereg §10)")
say("=" * 78)
CONTROLS = {}
PUNCT = NS["PUNCT"]
apply_convention, phonemes = NS["apply_convention"], NS["phonemes"]

for variant in ("R2", "R1"):
    set_variant(variant)
    rime = NS["rime"]
    rime_of = NS["rime_of"]
    readable_of = NS["readable_of"]
    L = LABS[variant]
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
                for Ln in ls:
                    pos += Ln
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

    say(f"\n   --- rime {variant}: D3, the within-corpus pseudo-fāṣila re-cut "
        f"(no baseline text)")
    for p in ("P1", "P2"):
        for tag, sd in (("primary", SEED), ("replication", SEED_REP)):
            ds, coin = recut(sd, N_RECUT, p)
            ge = sum(1 for x in ds if x >= DELTA[variant][p])
            pv = (1 + ge) / (1 + N_RECUT)
            mu = sum(ds) / len(ds)
            sdv = math.sqrt(sum((x - mu) ** 2 for x in ds) / len(ds))
            CONTROLS[f"recut_{variant}_{p}_{tag}"] = {
                "seed": sd, "n_recut": N_RECUT, "observed_delta": DELTA[variant][p],
                "recut_mean": mu, "recut_sd": sdv, "recut_max": max(ds),
                "n_ge_observed": ge, "p": pv,
                "boundary_coincidence": sum(coin) / len(coin),
                "z": (DELTA[variant][p] - mu) / sdv if sdv > 0 else float("nan")}
            say(f"      {p} [{tag}] Δ_obs={DELTA[variant][p]:+.4f} | re-cut mean={mu:+.4f} "
                f"sd={sdv:.4f} max={max(ds):+.4f} | #>=obs={ge} p={pv:.5f} "
                f"z={(DELTA[variant][p] - mu) / sdv if sdv > 0 else float('nan'):+.1f} | "
                f"boundary coincidence={sum(coin) / len(coin):.4f}")

    say(f"   --- rime {variant}: POSITIVE CONTROL, pre-Islamic poetry")
    pool = {c: [] for c in CONVS}
    pool_all = {c: [] for c in CONVS}
    per_poem = {}
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
        per_poem[nm] = {"n_lines": len(ls), "rime_readable": sum(rd) / len(ls),
                        "A_all": ap, "A_readable": apr, "n_pairs_readable": len(keep),
                        "delta_P1_readable": apr["P1"] - apr["C"]}
        say(f"      {nm:18s} n={len(ls):4d} readable={sum(rd) / len(ls):.3f} | "
            f"READABLE (n={len(keep):3d}): A(C)={apr['C']:.4f} A(P1)={apr['P1']:.4f} "
            f"Δ={apr['P1'] - apr['C']:+.4f}")
    A_poet = {c: sum(pool[c]) / len(pool[c]) for c in CONVS}
    A_poet_all = {c: sum(pool_all[c]) / len(pool_all[c]) for c in CONVS}
    say(f"      POOLED readable (n={len(pool['C'])}): A(C)={A_poet['C']:.4f} "
        f"A(P1)={A_poet['P1']:.4f} Δ={A_poet['P1'] - A_poet['C']:+.4f}   "
        f"[Qurʾān: A(C)={AGREE[variant]['C']:.4f} Δ={DELTA[variant]['P1']:+.4f}]")
    d4a = A_poet["C"] > AGREE[variant]["C"]
    say(f"      D4a — poetry out-rhymes the Qurʾān at citation form: {d4a}")

    def d4b(conv, seed):
        dq = np.array([(L[conv][sid][i] == L[conv][sid][i + 1])
                       - (L["C"][sid][i] == L["C"][sid][i + 1])
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

    for conv in ("P1", "P2"):
        o, pv = d4b(conv, SEED)
        _, pv2 = d4b(conv, SEED_REP)
        CONTROLS[f"poetry_{variant}_{conv}"] = {
            "obs_diff_of_deltas": o, "p": pv, "p_replication": pv2,
            "A_C_poetry_readable": A_poet["C"], "A_C_quran": AGREE[variant]["C"],
            "D4a": bool(d4a), "pooled_A_readable": A_poet, "pooled_A_all": A_poet_all,
            "per_poem": per_poem, "n_pairs_readable": len(pool["C"])}
        say(f"      D4b {conv}: Δ_Qurʾān − Δ_poetry = {o:+.4f}  p={pv:.5f} (rep {pv2:.5f})")
    checkpoint(f"controls-{variant}", {k: v for k, v in CONTROLS.items() if variant in k})

# --- prose: the delta remains NOT COMPUTABLE
say("\n   --- NEGATIVE CONTROL: prose. THE DELTA IS NOT COMPUTABLE (prereg §10).")
HARAKAT = set("ًٌٍَُِّْ")
prose_files = {"al-Bukhari": "data/baseline-corpora/raw/bukhari-noquran.txt",
               "al-Jahiz": "data/baseline-corpora/raw/jahiz-hayawan.txt"}
prose_voc = {}
for nm, p in prose_files.items():
    t = open(p, encoding="utf-8").read()
    ar = sum(1 for c in t if "ء" <= c <= "ي")
    hk = sum(1 for c in t if c in HARAKAT)
    prose_voc[nm] = {"arabic_chars": ar, "harakat": hk, "ratio": hk / max(ar, 1)}
    say(f"      {nm:12s} arabic={ar:9d} harakat={hk:6d} ratio={hk / max(ar, 1):.5f}"
        f"  -> the citation form is NOT RECOVERABLE; Δ is NOT COMPUTABLE for this text")
skel_rime = NS["skel_rime"]
q_skel = {sid: [skel_rime(t) for t in vs] for sid, _, _, vs in SURAHS}
A_q_skel = sum(1 for sid, i in PAIRS if q_skel[sid][i] == q_skel[sid][i + 1]) / N_PAIRS
say(f"      LEVEL comparison only, on the H-NEW-2240 skeleton instrument, length-matched:")
say(f"         Qurʾān A(skeleton) = {A_q_skel:.4f}")
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
            for Ln in lens:
                pos += Ln
                if pos - 1 >= len(words):
                    pos = off
                fins.append(pos - 1)
            for i in range(len(fins) - 1):
                agree += skel_rime(words[fins[i]]) == skel_rime(words[fins[i + 1]])
                tot += 1
        vals.append(agree / tot)
    mu = sum(vals) / len(vals)
    prose_level[nm] = {"n_cuts": N_PROSE_CUT, "mean": mu, "max": max(vals), "min": min(vals),
                       "quran_percentile": sum(1 for x in vals if x < A_q_skel) / len(vals)}
    say(f"         {nm:12s} mean={mu:.4f} max={max(vals):.4f} over {N_PROSE_CUT} matched "
        f"cuts | Qurʾān percentile {prose_level[nm]['quran_percentile']:.3f}")
poet_skel = []
set_variant("R2")
for nm, ls in poem_lines.items():
    lb = [skel_rime(l) for l in ls]
    poet_skel += [lb[i] == lb[i + 1] for i in range(len(ls) - 1)]
A_poet_skel = sum(poet_skel) / len(poet_skel)
say(f"         poetry A(skeleton) = {A_poet_skel:.4f}")
say("      This is a LEVEL statement about rhyme density and is NOT a control on the delta.")

# --- per-surah, under R2
say("\n" + "=" * 78)
say("RESULT 5 — PER-SURAH (rime R2, tuple P1). Descriptive.")
say("=" * 78)
per_surah = []
for sid, name, tr, vs in SURAHS:
    n = len(vs)
    if n < 2:
        continue
    pr = range(n - 1)
    ac = sum(1 for i in pr if L2["C"][sid][i] == L2["C"][sid][i + 1]) / (n - 1)
    a1 = sum(1 for i in pr if L2["P1"][sid][i] == L2["P1"][sid][i + 1]) / (n - 1)
    per_surah.append({"surah": sid, "name": tr, "n_verses": n, "A_C": ac, "A_P1": a1,
                      "delta_P1": a1 - ac, "K_C": len(set(L2["C"][sid])),
                      "K_P1": len(set(L2["P1"][sid]))})
nneg = sum(1 for r in per_surah if r["delta_P1"] < -1e-12)
nzero = sum(1 for r in per_surah if abs(r["delta_P1"]) <= 1e-12)
say(f"   Δ<0: {nneg}   Δ=0: {nzero}   Δ>0: {len(per_surah) - nneg - nzero}   "
    f"mean Δ = {sum(r['delta_P1'] for r in per_surah) / len(per_surah):+.4f}")
for r in sorted(per_surah, key=lambda r: -r["delta_P1"])[:8]:
    say(f"      Q{r['surah']:3d} {r['name'][:18]:18s} n={r['n_verses']:4d} "
        f"A(C)={r['A_C']:.3f} A(P1)={r['A_P1']:.3f} Δ={r['delta_P1']:+.3f} "
        f"K {r['K_C']}->{r['K_P1']}")

# ---------------------------------------------------------------- 7. verdict
say("\n" + "=" * 78)
say("VERDICT — logic diffed against prereg §8, printed before declaration.")
say("=" * 78)
say("   prereg §8 grid, verbatim:")
say("     Gate A/B or any of G1-G3 fails            -> INSTRUMENT BROKEN / NULL DEFECTIVE")
say("     D1 reverses                               -> REVERSED")
say("     D4a reverses                              -> CONTROL FAILED")
say("     ANY of registered tests 1-6 fails at alpha-> NULL (arithmetic); leads the write-up")
say("     tests 1-6 pass AND D3 passes both tuples  -> PASS")
say("     tests 1-6 pass but D3 fails               -> PARTIAL")
say("   tests 1-6 = D2 under {S2, S1, S5} x {P1, P2}, rime R2, on E = A - sum(p_i^2).")
say("   tests 7-10 (N-A, N-STEM), the R1 arms, P3, prose and the per-surah table gate nothing.")
say(f"   Bonferroni k = {BONFERRONI_K} -> alpha = {ALPHA:.8f}")

D1 = DELTA["R2"]["P1"] > 0 and DELTA["R2"]["P2"] > 0
D4A = CONTROLS["poetry_R2_P1"]["D4a"]
T16 = {f"{s}_{c}": EXACT[f"{s}_{c}_primary"]["p_E"] < ALPHA
       for s in ("S2", "S1", "S5") for c in ("P1", "P2")}
D3 = {c: CONTROLS[f"recut_R2_{c}_primary"]["p"] < ALPHA for c in ("P1", "P2")}
D2A = {c: EXACT[f"NA_{c}_primary"]["p_E"] < ALPHA for c in ("P1", "P2")}
D2S = {c: EXACT[f"S2_{c}_primary"]["stem_p"] < ALPHA for c in ("P1", "P2")}
D4B = {f"{v}_{c}": CONTROLS[f"poetry_{v}_{c}"]["p"] < ALPHA
       for v in ("R2", "R1") for c in ("P1", "P2")}

say(f"\n   D1  Δ>0 under P1 and P2 (R2)  : {D1}  "
    f"(Δ_P1={DELTA['R2']['P1']:+.4f}, Δ_P2={DELTA['R2']['P2']:+.4f})")
say(f"   D4a poetry A(C) > Qurʾān A(C) : {D4A}  "
    f"({CONTROLS['poetry_R2_P1']['A_C_poetry_readable']:.4f} vs "
    f"{CONTROLS['poetry_R2_P1']['A_C_quran']:.4f})")
for k in ("S2_P1", "S2_P2", "S1_P1", "S1_P2", "S5_P1", "S5_P2"):
    s, c = k.split("_")
    say(f"   D2  {k:6s} E > exact null   : {T16[k]}   p={EXACT[f'{s}_{c}_primary']['p_E']:.5f}  "
        f"(replication p={EXACT[f'{s}_{c}_replication']['p_E']:.5f})")
for c in ("P1", "P2"):
    say(f"   D2ᴀ NA_{c} (non-gating)       : {D2A[c]}   p={EXACT[f'NA_{c}_primary']['p_E']:.5f}")
for c in ("P1", "P2"):
    say(f"   D2ˢ STEM_{c} (non-gating)     : {D2S[c]}   p={EXACT[f'S2_{c}_primary']['stem_p']:.5f}")
for c in ("P1", "P2"):
    say(f"   D3  re-cut R2 {c}             : {D3[c]}   p={CONTROLS[f'recut_R2_{c}_primary']['p']:.5f}")
for k, v in D4B.items():
    say(f"   D4b poetry {k:6s}             : {v}   p={CONTROLS[f'poetry_{k[:2]}_{k[3:]}']['p']:.5f}")

if not (G1_PASS and G2_PASS and G3_PASS):
    VERDICT = "NULL DEFECTIVE — no p-value may be reported"
elif not D1:
    VERDICT = "REVERSED"
elif not D4A:
    VERDICT = "CONTROL FAILED — the positive control does not behave"
elif not all(T16.values()):
    VERDICT = "NULL — the gain is arithmetic even at matched concentration"
elif D3["P1"] and D3["P2"]:
    VERDICT = "PASS"
else:
    VERDICT = "PARTIAL"
say(f"\n   VERDICT: {VERDICT}")

# ---------------------------------------------------------------- 8. write
if SMOKE:
    say("\n[SMOKE] no run directory written, no JSON written. Exiting.")
    raise SystemExit(0)
STAMP = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUNDIR = os.path.join("runs", "h-new-2880", STAMP)
os.makedirs(RUNDIR, exist_ok=False)
out = {
    "id": "H-NEW-2880",
    "title": "The pausal fasila re-tested against a null matched on class CONCENTRATION",
    "run_utc": STAMP, "prereg": PREREG, "prereg_sha256": PREREG_SHA256,
    "parent": "H-NEW-2870", "frozen_inputs": FROZEN,
    "seed": SEED, "seed_replication": SEED_REP, "n_perm": N_PERM, "n_recut": N_RECUT,
    "n_prose_cut": N_PROSE_CUT, "bonferroni_k": BONFERRONI_K, "alpha": ALPHA,
    "python": sys.version.split()[0], "platform": platform.platform(),
    "n_verses": N_VERSES, "n_pairs": N_PAIRS, "n_stem_pairs": N_STEM_PAIRS,
    "gate_a_orthography": GATE_A, "gate_b_instrument": GATE_B,
    "class_collapse": COLLAPSE, "agreement": AGREE, "delta": DELTA,
    "chance_floor": FLOOR, "map_violation": MAPVIOL,
    "anti_gaming_audit": AUDIT,
    "exact_nulls": EXACT,
    "controls": CONTROLS,
    "prose": {"vocalisation": prose_voc, "delta_computable": False,
              "reason": "no harakat on disk; the citation form is not recoverable",
              "skeleton_level": prose_level, "quran_A_skeleton": A_q_skel,
              "poetry_A_skeleton": A_poet_skel},
    "per_surah": per_surah,
    "decisions": {"D1": D1, "D4a": D4A, "D2_tests_1_6": T16, "D2A_nongating": D2A,
                  "D2S_nongating": D2S, "D3": D3, "D4b": D4B},
    "verdict": VERDICT,
}
with open(os.path.join(RUNDIR, "result.json"), "x", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
with open(os.path.join(RUNDIR, "console.log"), "x", encoding="utf-8") as f:
    f.write("\n".join(LOG) + "\n")
with open(os.path.join(RUNDIR, "MANIFEST.txt"), "x", encoding="utf-8") as f:
    f.write(f"H-NEW-2880 run {STAMP}\nprereg {PREREG} {PREREG_SHA256}\n"
            f"script findings/phase-b-hypotheses/scripts/h-new-2880.py "
            f"{sha256_file('findings/phase-b-hypotheses/scripts/h-new-2880.py')}\n")
    for p, s in FROZEN.items():
        f.write(f"input {p} {s}\n")
    f.write(f"output {RUNDIR}/result.json\noutput {RUNDIR}/console.log\n")
    f.write(f"checkpoints {CHECKPOINT_DIR}/  (OUTSIDE the run directory, write-once)\n")
os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2880.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
print(f"\n[WROTE] {RUNDIR}/result.json")
print(f"[WROTE] findings/phase-b-hypotheses/csv/h-new-2880.json")
