#!/usr/bin/env python3
"""
H-NEW-2450 — The ADJACENT NEAR-VERBATIM REPRISE: corpus census + adjacency-excess
and genre-concentration tests.

The within-surah (i, i+1) rung of the project's repetition scale-ladder
(H-NEW-2100/2140 -> 2310 refrain -> 2350 exact cross-surah twin -> 2380 near
cross-surah twin -> Q094-F-01 the tightest adjacent couplet -> THIS census).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2450-adjacent-reprise.md
Direction LOCKED (family k=2, Bonferroni alpha = 0.025):
  H1 (PRIMARY)  : true verse-order places near-identical verses ADJACENT more
                  than a within-surah shuffle (N_low = # substantive adjacent
                  pairs with char-edit <= 3 is GREATER than null).
  H2 (SECONDARY): the device concentrates in juzz-amma (mushaf id 78-114) vs rest.
Seed 20260509, 10000 perms. Author: Waiel Al-Shujaa.

Honesty / instrument notes:
  - quran-no-tashkeel carries waqf/pause/codex glyphs (U+06D6-U+06ED) as
    standalone glyph-tokens -> STRIPPED before tokenizing (the H-NEW-2380 lesson).
  - Adjacency = same-surah (i, i+1) only; 113 cross-surah junctions EXCLUDED.
  - char-edit = Levenshtein over tokens joined with no separator (Q094-F-01 Arm B);
    token-edit = Levenshtein over token sequence. char-edit is the PRIMARY ranking.
  - Substantive = both verses >= 3 lexical tokens (Q094-F-01 SUB=3).
  - This is compositional repetition in ONE canonical text -- NOT qira'at/naskh.
"""
import json, hashlib, random, os, csv, unicodedata
from collections import Counter, defaultdict

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2450-adjacent-reprise.md")
EXPECTED_SHA = "11f93da43357ff93bb6efdcdd26d716cb3ded2218e4896b897fb776cb69bf6bd"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
REVCSV = os.path.join(ROOT, "data/revelation-order.csv")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2450.json")
SEED, NPERM = 20260509, 10000
SUB = 3            # substantive: both verses >= 3 lexical tokens (locked)
LOW_BAND = 3       # locked test band: char-edit <= 3
ROSTER_BAND = 6    # descriptive reporting roster: char-edit <= 6

# ---- pre-reg lock ----
with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

# ---- locked PAUSE set: waqf / codex annotation glyphs U+06D6..U+06ED ----
PAUSE = set(chr(c) for c in range(0x06D6, 0x06EE))

def lex(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(c for c in t if c not in PAUSE)
    return t.split()

def lev(a, b):
    """Levenshtein (unit cost) over any sequences a, b. Exact (for census/true-order)."""
    m, n = len(a), len(b)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [i] + [0] * n
        ca = a[i - 1]
        for j in range(1, n + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != b[j - 1]))
        prev = cur
    return prev[n]

def lev_le(a, b, cap):
    """True iff Levenshtein(a,b) <= cap. Length-prefilter + capped band with row-min
    early-exit. Used ONLY in the null (which only needs the c_ed<=cap indicator)."""
    m, n = len(a), len(b)
    if abs(m - n) > cap:
        return False
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [i] + [0] * n
        ca = a[i - 1]
        rowmin = cur[0]
        for j in range(1, n + 1):
            v = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != b[j - 1]))
            cur[j] = v
            if v < rowmin:
                rowmin = v
        if rowmin > cap:
            return False
        prev = cur
    return prev[n] <= cap

def align(a, b):
    """Backtrace token-Levenshtein -> list of (op, from, to) edits."""
    la, lb = len(a), len(b)
    INF = 10 ** 9
    dp = [[INF] * (lb + 1) for _ in range(la + 1)]
    for i in range(la + 1):
        dp[i][0] = i
    for j in range(lb + 1):
        dp[0][j] = j
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            c = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + c)
    i, j, edits = la, lb, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1]:
            i, j = i - 1, j - 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            edits.append(("sub", a[i - 1], b[j - 1])); i, j = i - 1, j - 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            edits.append(("del", a[i - 1], None)); i -= 1
        else:
            edits.append(("ins", None, b[j - 1])); j -= 1
    return list(reversed(edits))

CONNECTIVES = {"و", "ف", "ثم", "إن", "وإن", "فإن", "أن", "وأن", "بل", "أم",
               "ل", "قد", "لقد", "إذ", "وإذ", "إذا", "وإذا", "ولا", "لا", "ما", "ثُم"}

def classify(op, x, y, a, b):
    """Differing-token mechanism taxonomy (links H-NEW-2380's 4 mechanisms)."""
    # rhyme-driven final-word swap: substitution at the LAST token of both
    if op == "sub" and x == a[-1] and y == b[-1]:
        return "rhyme-driven final-word swap (fasila re-tuning)"
    if op in ("ins", "del"):
        w = x if op == "del" else y
        if w in CONNECTIVES:
            return "connective/particle prepend or drop"
        return "single-word insert/delete"
    # substitution
    if x in CONNECTIVES and y in CONNECTIVES:
        return "connective/particle swap"
    def stem(w):
        return "".join(ch for ch in w if ch not in "اوي")[:3]
    if stem(x) and stem(x) == stem(y):
        return "pronoun/inflection shift"
    return "parallel-template noun/verb swap"

# ---- load ----
quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
sname = {s["id"]: s["name"] for s in quran}

# verses by surah, canonical order
by_surah = {}
for s in quran:
    by_surah[s["id"]] = [(v["id"], lex(v["text"])) for v in s["verses"]]

# ============================ CENSUS ============================
char_hist_all = Counter(); tok_hist_all = Counter()
char_hist_sub = Counter(); tok_hist_sub = Counter()
sub_pairs = []     # all substantive pairs: (c_ed, t_ed, sid, vi, vj, A, B)
n_adj = 0
n_sub = 0
for sid, verses in by_surah.items():
    for k in range(len(verses) - 1):
        (vi, A), (vj, B) = verses[k], verses[k + 1]
        n_adj += 1
        ced = lev("".join(A), "".join(B))
        ted = lev(A, B)
        char_hist_all[ced] += 1
        tok_hist_all[ted] += 1
        if len(A) >= SUB and len(B) >= SUB:
            n_sub += 1
            char_hist_sub[ced] += 1
            tok_hist_sub[ted] += 1
            sub_pairs.append((ced, ted, sid, vi, vj, A, B))

sub_pairs.sort(key=lambda r: (r[0], r[1], r[2], r[3]))

# observed N_low (test statistic): substantive pairs with char-edit <= LOW_BAND
N_low_obs = sum(1 for ced, *_ in sub_pairs if ced <= LOW_BAND)

# ---- low-edit roster (char-edit <= ROSTER_BAND) with full coordinates ----
def juzz_amma(sid):
    return sid >= 78
roster = []
for ced, ted, sid, vi, vj, A, B in sub_pairs:
    if ced > ROSTER_BAND:
        continue
    edits = align(A, B)
    mech = [classify(op, x, y, A, B) for (op, x, y) in edits]
    roster.append({
        "char_edit": ced, "token_edit": ted,
        "ref": f"Q{sid}:{vi}-{vj}", "surah": sid, "name": sname[sid],
        "region": region[sid], "juzz_amma": juzz_amma(sid),
        "text_i": " ".join(A), "text_j": " ".join(B),
        "edits": [{"op": o, "from": x, "to": y, "mechanism": m}
                  for (o, x, y), m in zip(edits, mech)],
    })

# mechanism tally over the roster
mech_tally = Counter()
for r in roster:
    for e in r["edits"]:
        mech_tally[e["mechanism"]] += 1

# edit-1 / edit-2 / edit-3 families
fam = {1: [], 2: [], 3: []}
for r in roster:
    if r["char_edit"] in fam:
        fam[r["char_edit"]].append(r["ref"])

# ============================ H1 — ADJACENCY-EXCESS ============================
def count_low_in_sequence(seq):
    """seq = list of (concat_string, ntok, clen) in order; count substantive adjacent
    pairs with char-edit <= LOW_BAND. Inlined char-length prefilter (rejects the vast
    majority in O(1)) then the capped band-limited indicator lev_le."""
    n = 0
    cap = LOW_BAND
    prev = seq[0]
    for k in range(1, len(seq)):
        cur = seq[k]
        # prev=(ca,na,la), cur=(cb,nb,lb)
        if prev[1] >= SUB and cur[1] >= SUB and abs(prev[2] - cur[2]) <= cap:
            if lev_le(prev[0], cur[0], cap):
                n += 1
        prev = cur
    return n

# pre-build per-surah (concat_string, ntok, clen) lists once (avoid re-joining each perm)
surah_units = {}
for sid, verses in by_surah.items():
    units = []
    for _, tl in verses:
        cs = "".join(tl)
        units.append((cs, len(tl), len(cs)))
    surah_units[sid] = units

# ---- per-permutation null (deterministic seeding: perm p uses Random((seed, p)),
#      reproducible regardless of single/multi-process scheduling) ----
_surah_unit_list = [surah_units[sid] for sid in surah_units]   # ordered list of unit-lists
all_units = [u for units in _surah_unit_list for u in units]
lengths = [len(units) for units in _surah_unit_list]

def _ws_perm(args):
    """One within-surah-shuffle permutation -> N_low count."""
    seed, p = args
    rng = random.Random(seed * 100003 + p)
    tot = 0
    for units in _surah_unit_list:
        seq = units[:]
        rng.shuffle(seq)
        tot += count_low_in_sequence(seq)
    return tot

def _global_perm(args):
    """One global-shuffle permutation (re-segmented into surah-length blocks) -> N_low."""
    seed, p = args
    rng = random.Random(seed * 100003 + p)
    perm = all_units[:]
    rng.shuffle(perm)
    tot = 0; idx = 0
    for L in lengths:
        tot += count_low_in_sequence(perm[idx:idx + L]); idx += L
    return tot

def run_null(fn, seed, pool):
    counts = pool.map(fn, [(seed, p) for p in range(NPERM)], chunksize=200)
    ge = sum(1 for c in counts if c >= N_low_obs)
    return (ge + 1) / (NPERM + 1), sum(counts) / len(counts)

import multiprocessing as mp
# fork start-method: workers inherit computed globals, do NOT re-run module top-level,
# so the downstream module-level code (verdicts/H2/output) executes ONLY in the parent.
try:
    mp.set_start_method("fork")
except RuntimeError:
    pass
with mp.Pool(processes=min(8, mp.cpu_count())) as pool:
    # PRIMARY: within-surah shuffle
    p_ws, mean_ws = run_null(_ws_perm, SEED, pool)
    # replication seed (MW-5)
    p_ws_rep, mean_ws_rep = run_null(_ws_perm, SEED + 10, pool)
    # robustness: global verse-sequence shuffle
    p_global, mean_global = run_null(_global_perm, SEED + 1, pool)

H1_pass = (N_low_obs > mean_ws) and (p_ws < 0.025)
H1_reversed = N_low_obs <= mean_ws
if H1_reversed:
    H1_verdict = "NULL (pre-commit violation: reversed)"
elif H1_pass:
    H1_verdict = "PASS"
else:
    H1_verdict = "NULL (direction held but not significant)"

# ============================ H2 — GENRE-CONCENTRATION ============================
# per-surah low-edit RATE = (#substantive pairs c_ed<=LOW_BAND) / (#substantive pairs)
surah_low = defaultdict(int); surah_subN = defaultdict(int)
for ced, ted, sid, vi, vj, A, B in sub_pairs:
    surah_subN[sid] += 1
    if ced <= LOW_BAND:
        surah_low[sid] += 1
rates = {}
for sid in by_surah:
    if surah_subN[sid] > 0:
        rates[sid] = surah_low[sid] / surah_subN[sid]
amma = [sid for sid in rates if sid >= 78]
rest = [sid for sid in rates if sid < 78]
mean_amma = sum(rates[s] for s in amma) / len(amma)
mean_rest = sum(rates[s] for s in rest) / len(rest)
delta_obs = mean_amma - mean_rest

# label-permutation null
rng2 = random.Random(SEED + 2)
labeled = list(rates.keys())
n_amma = len(amma)
ge2 = 0; nulls2 = []
for _ in range(NPERM):
    pick = set(rng2.sample(labeled, n_amma))
    ma = sum(rates[s] for s in pick) / n_amma
    others = [s for s in labeled if s not in pick]
    mr = sum(rates[s] for s in others) / len(others)
    d = ma - mr
    nulls2.append(d)
    if d >= delta_obs:
        ge2 += 1
p_h2 = (ge2 + 1) / (NPERM + 1)
H2_pass = (delta_obs > 0) and (p_h2 < 0.025)
H2_reversed = delta_obs <= 0
H2_verdict = ("NULL (pre-commit violation: reversed)" if H2_reversed
              else ("PASS" if H2_pass else "NULL (direction held but not significant)"))

# region split of roster (descriptive)
roster_region = Counter(r["region"] for r in roster)
roster_amma = sum(1 for r in roster if r["juzz_amma"])

# ============================ OUTPUT ============================
out = {
    "finding": "H-NEW-2450",
    "title": "Adjacent near-verbatim reprise: corpus census + adjacency-excess / genre-concentration",
    "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    "tokenization": "NFC; waqf/codex glyphs U+06D6-U+06ED stripped; whitespace split; same-surah (i,i+1) only",
    "bands": {"substantive_min_tokens": SUB, "test_band_char_edit_le": LOW_BAND,
              "roster_band_char_edit_le": ROSTER_BAND},
    "counts": {
        "within_surah_adjacent_pairs": n_adj,
        "substantive_adjacent_pairs": n_sub,
        "N_low_observed_char_edit_le3_substantive": N_low_obs,
        "exact_verbatim_adjacent_substantive": char_hist_sub.get(0, 0),
        "roster_size_char_edit_le6": len(roster),
        "roster_juzz_amma": roster_amma,
    },
    "char_edit_histogram_all": dict(sorted(char_hist_all.items())),
    "token_edit_histogram_all": dict(sorted(tok_hist_all.items())),
    "char_edit_histogram_substantive": dict(sorted(char_hist_sub.items())),
    "token_edit_histogram_substantive": dict(sorted(tok_hist_sub.items())),
    "families": {"edit1": fam[1], "edit2": fam[2], "edit3": fam[3]},
    "mechanism_tally": dict(mech_tally.most_common()),
    "roster_region": dict(roster_region),
    "H1_adjacency_excess": {
        "statistic": "N_low = # substantive within-surah adjacent pairs with char-edit <= 3",
        "N_low_obs": N_low_obs,
        "primary_null": "within-surah verse-order shuffle",
        "null_mean_within_surah": round(mean_ws, 4),
        "p_within_surah_one_sided": round(p_ws, 5),
        "replication_seed_p": round(p_ws_rep, 5),
        "replication_null_mean": round(mean_ws_rep, 4),
        "robustness_global_shuffle_null_mean": round(mean_global, 4),
        "robustness_global_shuffle_p": round(p_global, 5),
        "direction_locked": "observed > null (adjacent more than chance)",
        "verdict": H1_verdict,
    },
    "H2_genre_concentration": {
        "statistic": "Delta = mean per-surah low-edit rate (juzz-amma 78-114) - rest (1-77)",
        "mean_rate_juzz_amma": round(mean_amma, 5),
        "mean_rate_rest": round(mean_rest, 5),
        "delta_obs": round(delta_obs, 5),
        "n_juzz_amma_surahs_with_substantive_pairs": len(amma),
        "n_rest_surahs": len(rest),
        "p_label_perm_one_sided": round(p_h2, 5),
        "direction_locked": "juzz-amma rate > rest",
        "verdict": H2_verdict,
    },
    "bonferroni_alpha": 0.025,
    "roster": roster,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)

# ---- console summary ----
print(f"\n=== CENSUS ===")
print(f"within-surah adjacent pairs: {n_adj}  | substantive (>=3 tok both): {n_sub}")
print(f"char-edit hist (substantive, low tail): "
      + " ".join(f"{k}:{char_hist_sub[k]}" for k in sorted(char_hist_sub) if k <= 8))
print(f"token-edit hist (substantive, low tail): "
      + " ".join(f"{k}:{tok_hist_sub[k]}" for k in sorted(tok_hist_sub) if k <= 6))
print(f"exact-verbatim adjacent (substantive): {char_hist_sub.get(0,0)}")
print(f"edit-1 family: {fam[1]}")
print(f"edit-2 family: {fam[2]}")
print(f"edit-3 family: {fam[3]}")
print(f"roster (c_ed<=6): {len(roster)} pairs; juzz-amma {roster_amma}; region {dict(roster_region)}")
print(f"mechanism tally: {dict(mech_tally.most_common())}")
print(f"\n=== H1 ADJACENCY-EXCESS (PRIMARY) ===")
print(f"N_low_obs={N_low_obs}  within-surah null mean={mean_ws:.3f}  p={p_ws:.5f}  (repl p={p_ws_rep:.5f})")
print(f"global-shuffle robustness: null mean={mean_global:.3f}  p={p_global:.5f}")
print(f"H1 -> {H1_verdict}")
print(f"\n=== H2 GENRE-CONCENTRATION (SECONDARY) ===")
print(f"rate juzz-amma={mean_amma:.5f}  rate rest={mean_rest:.5f}  Delta={delta_obs:.5f}  p={p_h2:.5f}")
print(f"H2 -> {H2_verdict}")
print(f"\nWrote {OUT}")
