#!/usr/bin/env python3
"""
H-NEW-2470 — ORDERING-BY-DISPERSION as a formal corpus law.

A per-surah GENERATOR that promotes the 3-finding convergence (H-NEW-2310 refrain
spacing + H-NEW-2420 Q55 z=-5.32 anti-adjacency + H-NEW-2450 adjacent reprise NULL)
to a direction-locked, Bonferroni-corrected corpus law.

For EVERY surah:
  1. Build the set S_s of SIMILAR unordered verse-pairs among substantive verses
     (root-Jaccard >= 0.80  OR  char-edit <= 5).
  2. A_obs(s) = how many of those similar-pairs are ADJACENT (|pos diff| = 1) in
     canonical Hafs-Kufan order.
  3. Within-surah verse-order SHUFFLE null (10000 perms): recount adjacency of the
     SAME pair set; a surah DISPERSES if A_obs < null_mean (left tail).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2470-dispersion-law.md
Direction LOCKED (family of 2 arms, Bonferroni alpha = 0.025):
  H1 (PRIMARY)  : corpus-wide, similar pairs are LESS adjacent than chance
                  (A_total_obs < within-surah-shuffle null total).  LEFT tail.
  H2 (SECONDARY): the effect concentrates in {Q55,Q77,Q26,Q37,Q54} (named a priori).
Seed 20260509, 10000 perms. Author: Waiel Al-Shujaa.

Instruments (byte-identical to prior project findings, by design):
  - verse text + PAUSE-strip + char-edit  : H-NEW-2450 §1.3 / Q094-F-01 Arm B
  - per-verse QAC v0.4 ROOT-set + Jaccard  : H-NEW-2420 / H-NEW-2280
"""
import json, hashlib, random, os, math, unicodedata
from collections import defaultdict

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2470-dispersion-law.md")
EXPECTED_SHA = "f29185599deda238b9d5c4492a2b68a2287d64f3190ec2af552aec3e87ea7e6d"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2470.json")
SEED, NPERM = 20260509, 10000
SUB = 3          # substantive: verse has >= 3 lexical tokens
J_THR = 0.80     # root-Jaccard threshold (primary)
C_THR = 5        # char-edit threshold (primary)
NAMED = [55, 77, 26, 37, 54]   # pre-registered refrain/repetition-heavy set (H2)

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

def lev_le(a, b, cap):
    """True iff char-Levenshtein(a,b) <= cap. Length-prefilter + band early-exit."""
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

def jaccard(a, b):
    if not a and not b:
        return 0.0
    u = len(a | b)
    return (len(a & b) / u) if u else 0.0

# ---- load verse text + region ----
quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
sname = {s["id"]: s["name"] for s in quran}
# per-surah ordered list of (verse_id, tokens, concat_string)
by_surah = {}
for s in quran:
    seq = []
    for v in s["verses"]:
        toks = lex(v["text"])
        seq.append((v["id"], toks, "".join(toks)))
    by_surah[s["id"]] = seq

# ---- load QAC v0.4 root-sets per verse (first ROOT per segment; 2420 convention) ----
verse_roots = defaultdict(set)
with open(MORPH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()
        if not line or line.startswith("#") or line.startswith("LOCATION"):
            continue
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        loc = parts[0].strip("()")
        try:
            sv = loc.split(":")
            sid, vid = int(sv[0]), int(sv[1])
        except (ValueError, IndexError):
            continue
        for tok in parts[3].split("|"):
            if tok.startswith("ROOT:"):
                verse_roots[(sid, vid)].add(tok[len("ROOT:"):])
                break
verse_roots = dict(verse_roots)


def build_surah(sid):
    """Return (L, pair_set, sub_idx_meta). pair_set = list of (pi, pj) 0-based positions
    of SIMILAR substantive verse-pairs; L = total verse count; also returns diagnostics."""
    seq = by_surah[sid]
    L = len(seq)
    # substantive positions (0-based) with their root-set + concat string
    subs = []   # (pos, rootset, concat)
    for pos, (vid, toks, cs) in enumerate(seq):
        if len(toks) >= SUB:
            subs.append((pos, verse_roots.get((sid, vid), set()), cs))
    pairs = []          # (pos_i, pos_j) with pos_i < pos_j
    n_root = n_char = n_both = 0
    for a in range(len(subs)):
        pa, ra, ca = subs[a]
        for b in range(a + 1, len(subs)):
            pb, rb, cb = subs[b]
            jr = jaccard(ra, rb)
            root_hit = jr >= J_THR
            char_hit = lev_le(ca, cb, C_THR)
            if root_hit or char_hit:
                pairs.append((pa, pb))
                if root_hit:
                    n_root += 1
                if char_hit:
                    n_char += 1
                if root_hit and char_hit:
                    n_both += 1
    return L, pairs, {"n_sub": len(subs), "n_pairs": len(pairs),
                      "n_root_hits": n_root, "n_char_hits": n_char, "n_both": n_both}


def adjacency_count(pairs, posmap, gap):
    """# pairs whose mapped positions differ by exactly/at-most `gap`."""
    if gap == 1:
        return sum(1 for pi, pj in pairs if abs(posmap[pi] - posmap[pj]) == 1)
    return sum(1 for pi, pj in pairs if abs(posmap[pi] - posmap[pj]) <= gap)


def run_surah_null(L, pairs, seed_offset, gap=1):
    """Within-surah shuffle null on the FIXED pair set. Returns
    (A_obs, null_mean, null_std, p_left, perm_counts)."""
    identity = list(range(L))
    A_obs = adjacency_count(pairs, identity, gap)
    rng = random.Random(SEED + seed_offset)
    perm_counts = []
    perm = list(range(L))
    for _ in range(NPERM):
        rng.shuffle(perm)
        # perm[new_position] = original_position ; we need posmap[original]=new_position
        posmap = [0] * L
        for newpos, orig in enumerate(perm):
            posmap[orig] = newpos
        perm_counts.append(adjacency_count(pairs, posmap, gap))
    nm = sum(perm_counts) / len(perm_counts)
    var = sum((c - nm) ** 2 for c in perm_counts) / len(perm_counts)
    sd = var ** 0.5
    le = sum(1 for c in perm_counts if c <= A_obs)
    p_left = (le + 1) / (NPERM + 1)
    return A_obs, nm, sd, p_left, perm_counts


def _inv_norm(p):
    """Acklam inverse-normal CDF (for Stouffer)."""
    if p <= 0:
        return -1e9
    if p >= 1:
        return 1e9
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
               ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / \
           (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)

# ============================ GENERATOR: build all surahs ============================
print("[..] building similar-pair sets per surah")
surah_pairs = {}   # sid -> (L, pairs, diag)
for sid in by_surah:
    surah_pairs[sid] = build_surah(sid)

total_pairs = sum(surah_pairs[sid][2]["n_pairs"] for sid in surah_pairs)
print(f"[ok] total SIMILAR unordered substantive pairs corpus-wide: {total_pairs}")

# ============================ H1 PRIMARY: per-surah + aggregate ============================
# We accumulate the AGGREGATE corpus null by summing per-surah perm-counts across the SAME
# permutation index p (each surah independently shuffled with seed SEED + p-driven RNG).
print("[..] running per-surah within-surah-shuffle nulls (primary, strict adjacency)")

per_surah = []
# For the aggregate corpus null we need synchronized per-perm sums. Use a single RNG stream
# per surah seeded deterministically by surah, accumulate perm_counts, then sum element-wise.
agg_perm_counts = [0] * NPERM
A_total_obs = 0
eligible = []   # surahs with >=1 pair and non-degenerate null (null_std>0)

# deterministic per-surah seeding so the aggregate sum is reproducible
for sid in sorted(by_surah):
    L, pairs, diag = surah_pairs[sid]
    if not pairs:
        per_surah.append({"surah": sid, "name": sname[sid], "region": region[sid],
                          "L": L, "n_pairs": 0, "A_obs": 0, "null_mean": 0.0,
                          "null_std": 0.0, "z": 0.0, "p_left": 1.0,
                          "dispersing": False, "eligible": False, **diag})
        continue
    A_obs, nm, sd, p_left, pc = run_surah_null(L, pairs, seed_offset=sid * 1000, gap=1)
    A_total_obs += A_obs
    for i in range(NPERM):
        agg_perm_counts[i] += pc[i]
    z = (A_obs - nm) / sd if sd > 0 else 0.0
    elig = sd > 0
    rec = {"surah": sid, "name": sname[sid], "region": region[sid], "L": L,
           "n_pairs": len(pairs), "A_obs": A_obs, "null_mean": round(nm, 4),
           "null_std": round(sd, 4), "z": round(z, 4), "p_left": round(p_left, 5),
           "depletion": round(nm - A_obs, 4),
           "dispersing": A_obs < nm, "eligible": elig, **diag}
    per_surah.append(rec)
    if elig:
        eligible.append(rec)

k = len(eligible)
bonf_alpha = 0.05 / k if k else 0.05

# aggregate corpus null
agg_mean = sum(agg_perm_counts) / NPERM
agg_var = sum((c - agg_mean) ** 2 for c in agg_perm_counts) / NPERM
agg_sd = agg_var ** 0.5
agg_le = sum(1 for c in agg_perm_counts if c <= A_total_obs)
p_agg_left = (agg_le + 1) / (NPERM + 1)
agg_z = (A_total_obs - agg_mean) / agg_sd if agg_sd > 0 else 0.0

# per-surah corroboration: sign-test + Stouffer (LEFT tail = depletion)
n_disp = sum(1 for r in eligible if r["dispersing"])
n_clump = sum(1 for r in eligible if r["A_obs"] > r["null_mean"])
n_tie = k - n_disp - n_clump
# sign-test (two-sided binomial on disp vs clump, exact)
def binom_sf(k_obs, n, p=0.5):
    # P(X >= k_obs) for Binom(n,0.5)
    from math import comb
    return sum(comb(n, i) for i in range(k_obs, n + 1)) * (p ** n) if n <= 1000 else None
nn = n_disp + n_clump
sign_p = None
if 0 < nn <= 1000:
    bigger = max(n_disp, n_clump)
    tail = binom_sf(bigger, nn)
    sign_p = min(1.0, 2 * tail) if tail is not None else None
# Stouffer on per-surah LEFT-tail p (small p_left -> strong depletion -> large +Z)
floor = 0.5 / NPERM
zs = []
for r in eligible:
    pp = min(max(r["p_left"], floor), 1 - floor)
    zs.append(_inv_norm(1 - pp))   # invert: small p_left -> large positive
stouffer_z = sum(zs) / math.sqrt(len(zs)) if zs else 0.0

H1_reversed = A_total_obs >= agg_mean
H1_dir_ok = A_total_obs < agg_mean
H1_pass = H1_dir_ok and (p_agg_left < 0.025) and (n_disp > n_clump)
if H1_reversed:
    H1_verdict = "NULL (pre-commit violation: reversed — similar-pairs NOT depleted)"
elif H1_pass:
    H1_verdict = "PASS"
else:
    H1_verdict = "NULL (direction held but not significant)"

# ============================ H2 SECONDARY: named-set concentration ============================
named_set = set(NAMED)
elig_ids = {r["surah"] for r in eligible}
named_elig = [r for r in eligible if r["surah"] in named_set]
other_elig = [r for r in eligible if r["surah"] not in named_set]
def mean_dep(rs):
    return (sum(r["depletion"] for r in rs) / len(rs)) if rs else 0.0
mean_named = mean_dep(named_elig)
mean_other = mean_dep(other_elig)
delta_obs = mean_named - mean_other

# label-permutation null: choose len(named_elig) eligible surahs at random as "named"
rng2 = random.Random(SEED + 2)
all_dep = [r["depletion"] for r in eligible]
n_named_e = len(named_elig)
ge2 = 0
for _ in range(NPERM):
    idx = set(rng2.sample(range(len(eligible)), n_named_e)) if n_named_e else set()
    nm_ = sum(all_dep[i] for i in idx) / n_named_e if n_named_e else 0.0
    oth = [all_dep[i] for i in range(len(eligible)) if i not in idx]
    mo_ = sum(oth) / len(oth) if oth else 0.0
    if (nm_ - mo_) >= delta_obs:
        ge2 += 1
p_h2 = (ge2 + 1) / (NPERM + 1)
H2_reversed = delta_obs <= 0
H2_pass = (delta_obs > 0) and (p_h2 < 0.025)
H2_verdict = ("NULL (pre-commit violation: reversed)" if H2_reversed
              else ("PASS" if H2_pass else "NULL (direction held but not significant)"))

# ============================ MW-5 replication (H1 aggregate, second seed) ============================
print("[..] MW-5 replication at seed+10")
rep_perm = [0] * NPERM
for sid in sorted(by_surah):
    L, pairs, diag = surah_pairs[sid]
    if not pairs:
        continue
    _, _, sd, _, pc = run_surah_null(L, pairs, seed_offset=(sid * 1000 + 10) + 7_000_000, gap=1)
    for i in range(NPERM):
        rep_perm[i] += pc[i]
rep_mean = sum(rep_perm) / NPERM
rep_le = sum(1 for c in rep_perm if c <= A_total_obs)
p_rep_left = (rep_le + 1) / (NPERM + 1)

# ============================ MW-3 robustness variants (H1 aggregate only) ============================
print("[..] MW-3 robustness variants V1-V4")
def variant_pairs(sid, j_thr, c_thr, use_root, use_char):
    seq = by_surah[sid]
    L = len(seq)
    subs = [(pos, verse_roots.get((sid, seq[pos][0]), set()), seq[pos][2])
            for pos in range(L) if len(seq[pos][1]) >= SUB]
    pairs = []
    for a in range(len(subs)):
        pa, ra, ca = subs[a]
        for b in range(a + 1, len(subs)):
            pb, rb, cb = subs[b]
            hit = False
            if use_root and jaccard(ra, rb) >= j_thr:
                hit = True
            if (not hit) and use_char and lev_le(ca, cb, c_thr):
                hit = True
            if hit:
                pairs.append((pa, pb))
    return L, pairs

def variant_aggregate(j_thr, c_thr, use_root, use_char, gap, seed_tag):
    perm_tot = [0] * NPERM
    obs_tot = 0
    npairs = 0
    for sid in sorted(by_surah):
        L, pairs = variant_pairs(sid, j_thr, c_thr, use_root, use_char)
        if not pairs:
            continue
        npairs += len(pairs)
        A_obs, _, _, _, pc = run_surah_null(L, pairs, seed_offset=sid * 1000 + seed_tag, gap=gap)
        obs_tot += A_obs
        for i in range(NPERM):
            perm_tot[i] += pc[i]
    m = sum(perm_tot) / NPERM
    le = sum(1 for c in perm_tot if c <= obs_tot)
    return {"A_total_obs": obs_tot, "null_mean_total": round(m, 4),
            "p_left": round((le + 1) / (NPERM + 1), 5), "n_pairs": npairs,
            "reversed": obs_tot >= m}

variants = {
    "V1_root0.60_char3": variant_aggregate(0.60, 3, True, True, 1, 101),
    "V2_root_only_0.80": variant_aggregate(0.80, 0, True, False, 1, 102),
    "V3_char_only_5":    variant_aggregate(0.0, 5, False, True, 1, 103),
    "V4_near_adjacent_le2": variant_aggregate(J_THR, C_THR, True, True, 2, 104),
}

# ============================ rosters ============================
disp_sorted = sorted([r for r in eligible], key=lambda r: (-r["depletion"], r["surah"]))
top_dispersers = [{"surah": r["surah"], "name": r["name"], "region": r["region"],
                   "L": r["L"], "n_pairs": r["n_pairs"], "A_obs": r["A_obs"],
                   "null_mean": r["null_mean"], "depletion": r["depletion"],
                   "z": r["z"], "p_left": r["p_left"],
                   "bonf_sig": (r["p_left"] < bonf_alpha) and r["dispersing"]}
                  for r in disp_sorted[:25]]
bonf_dispersers = [r["surah"] for r in eligible
                   if r["dispersing"] and r["p_left"] < bonf_alpha]

# ============================ OUTPUT ============================
out = {
    "finding": "H-NEW-2470",
    "title": "Ordering-by-dispersion as a formal corpus law (per-surah similar-pair adjacency-depletion)",
    "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "rules_tuple": "(no-tashkeel, QAC-v0.4-ROOT + orthographic-graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    "similar_pair_def": f"root-Jaccard >= {J_THR} OR char-edit <= {C_THR}; substantive verses (>= {SUB} tokens)",
    "adjacency_def": "canonical position-difference == 1 (strict); near-adjacent <= 2 reported as V4",
    "counts": {
        "total_similar_unordered_pairs": total_pairs,
        "eligible_surahs_in_family": k,
        "bonferroni_alpha": round(bonf_alpha, 6),
        "n_dispersing_eligible": n_disp,
        "n_clumping_eligible": n_clump,
        "n_tie_eligible": n_tie,
    },
    "H1_corpus_dispersion": {
        "statistic": "A_total = sum over surahs of #similar-pairs adjacent (|pos diff|=1)",
        "A_total_obs": A_total_obs,
        "null_mean_total": round(agg_mean, 4),
        "null_std_total": round(agg_sd, 4),
        "z_aggregate": round(agg_z, 4),
        "p_aggregate_left_one_sided": round(p_agg_left, 5),
        "direction_locked": "observed < null (similar-pairs LESS adjacent than chance = dispersion)",
        "sign_test_n_dispersing": n_disp,
        "sign_test_n_clumping": n_clump,
        "sign_test_two_sided_p": (round(sign_p, 6) if sign_p is not None else None),
        "stouffer_z_left_tail": round(stouffer_z, 4),
        "replication_seed_plus10_null_mean": round(rep_mean, 4),
        "replication_seed_plus10_p_left": round(p_rep_left, 5),
        "verdict": H1_verdict,
    },
    "H2_named_set_concentration": {
        "named_set": NAMED,
        "named_eligible": [r["surah"] for r in named_elig],
        "statistic": "Delta = mean depletion(named eligible) - mean depletion(other eligible)",
        "mean_depletion_named": round(mean_named, 4),
        "mean_depletion_other": round(mean_other, 4),
        "delta_obs": round(delta_obs, 4),
        "p_label_perm_one_sided": round(p_h2, 5),
        "direction_locked": "named-set depletion > other (concentration)",
        "verdict": H2_verdict,
    },
    "robustness_variants_MW3": variants,
    "bonferroni_dispersers": bonf_dispersers,
    "top25_dispersers": top_dispersers,
    "named_set_detail": [r for r in per_surah if r["surah"] in named_set],
    "per_surah": per_surah,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)

# ---- console summary ----
print(f"\n=== GENERATOR ===")
print(f"total SIMILAR unordered substantive pairs: {total_pairs}")
print(f"eligible surahs in family: {k}  Bonferroni alpha = {bonf_alpha:.6f}")
print(f"\n=== H1 CORPUS DISPERSION (PRIMARY, LEFT tail) ===")
print(f"A_total_obs={A_total_obs}  null_mean={agg_mean:.3f}  z={agg_z:.3f}  p_left={p_agg_left:.5f}")
print(f"sign-test: dispersing={n_disp} clumping={n_clump} tie={n_tie}  p={sign_p}")
print(f"Stouffer z (left)={stouffer_z:.3f}  | repl(+10) null_mean={rep_mean:.3f} p_left={p_rep_left:.5f}")
print(f"H1 -> {H1_verdict}")
print(f"\n=== H2 NAMED-SET CONCENTRATION (SECONDARY) ===")
print(f"named eligible={[r['surah'] for r in named_elig]}")
print(f"mean dep named={mean_named:.3f}  other={mean_other:.3f}  Delta={delta_obs:.3f}  p={p_h2:.5f}")
print(f"H2 -> {H2_verdict}")
print(f"\n=== MW-3 VARIANTS (aggregate H1) ===")
for kk, vv in variants.items():
    print(f"  {kk}: A_obs={vv['A_total_obs']} null={vv['null_mean_total']:.2f} "
          f"p_left={vv['p_left']:.5f} pairs={vv['n_pairs']} reversed={vv['reversed']}")
print(f"\n=== TOP DISPERSERS (by absolute depletion) ===")
for r in top_dispersers[:12]:
    print(f"  Q{r['surah']:>3} {r['name']:<12} pairs={r['n_pairs']:>4} A_obs={r['A_obs']:>2} "
          f"null={r['null_mean']:>7.3f} dep={r['depletion']:>7.3f} z={r['z']:>7.3f} p_left={r['p_left']:.5f}")
print(f"\nBonferroni-significant dispersers ({len(bonf_dispersers)}): {bonf_dispersers}")
print(f"\nWrote {OUT}")
