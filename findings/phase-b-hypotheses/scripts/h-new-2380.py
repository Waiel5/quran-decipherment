#!/usr/bin/env python3
"""
H-NEW-2380 — Cross-surah NEAR-twin verse census (token edit-distance <= k) and
revelation-order proximity. Extends H-NEW-2350 (exact twins) to near-twins.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2380-near-twin-census.md
Direction LOCKED: near-twin surah-pairs are CLOSER in revelation order than random.
Seed 20260509, 10000 perms. Author: Waiel Al-Shujaa.

Honesty notes:
  - quran-no-tashkeel still carries waqf/pause marks as standalone glyph-tokens;
    these are codex/recitation annotations, NOT lexical words -> STRIPPED.
  - True token-level Levenshtein (sub/ins/del, unit cost), cross-surah only.
  - d=0 (exact after strip) excluded -> exact-twin domain (H-NEW-2350); reported separately.
  - NOT qira'at / naskh: this is compositional repetition in ONE canonical text.
"""
import json, hashlib, random, os, csv, unicodedata, itertools, statistics
from collections import defaultdict, Counter

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2380-near-twin-census.md")
EXPECTED_SHA = "42828931e11e5d432a1b570adb98071c1a58f053ccfcfeefdfc4b219a24ae8b9"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
REVCSV = os.path.join(ROOT, "data/revelation-order.csv")
SEED, NPERM = 20260509, 10000
K_PRIMARY, L_PRIMARY = 2, 8   # locked

with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
sname = {s["id"]: s["name"] for s in quran}

rev, nold = {}, {}
with open(REVCSV) as f:
    for row in csv.DictReader(f):
        mid = int(row["mushaf_order"])
        rev[mid] = int(row["revelation_order"])
        nold[mid] = int(row["noldeke_order"]) if row.get("noldeke_order") else None

# ---- lexical tokenization: strip Quranic waqf/pause/codex marks ----
PAUSE = set('ۖۗۘۙۚۛۜ۝۞۟'
            'ۣ۠ۡۢۤۥۦۧۨ۩'
            '۪ۭ۫۬')
def lex_tokens(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(c for c in t if c not in PAUSE)
    return t.split()

verses = []  # (sid, vid, tokens)
for s in quran:
    for v in s["verses"]:
        verses.append((s["id"], v["id"], lex_tokens(v["text"])))

def ed_cap(a, b, cap):
    """Token Levenshtein capped at cap (returns cap+1 if exceeded)."""
    la, lb = len(a), len(b)
    if abs(la - lb) > cap:
        return cap + 1
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        cur = [i] + [0] * lb
        rowmin = cur[0]
        ai = a[i - 1]
        for j in range(1, lb + 1):
            c = 0 if ai == b[j - 1] else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + c)
            if cur[j] < rowmin:
                rowmin = cur[j]
        if rowmin > cap:
            return cap + 1
        prev = cur
    return prev[lb]

def near_twin_pairs(min_tok, k):
    """All cross-surah verse-pairs with 1<=edit<=k, both verses >=min_tok tokens.
    Blocking: candidate j shares >=1 token with i (necessary for edit<=k when
    both long), then length-filter, then capped Levenshtein."""
    cand = [(s, v, t) for s, v, t in verses if len(t) >= min_tok]
    tsets = [set(t) for _, _, t in cand]
    inv = defaultdict(list)
    for idx, ts in enumerate(tsets):
        for tok in ts:
            inv[tok].append(idx)
    pairs = []  # (dist, (si,vi), (sj,vj), ti, tj)
    seen = set()
    for i in range(len(cand)):
        si, vi, ti = cand[i]
        li = len(ti)
        cs = set()
        for tok in tsets[i]:
            for j in inv[tok]:
                if j > i:
                    cs.add(j)
        for j in cs:
            sj, vj, tj = cand[j]
            if si == sj:
                continue
            if abs(li - len(tj)) > k:
                continue
            d = ed_cap(ti, tj, k)
            if 1 <= d <= k:
                key = tuple(sorted([(si, vi), (sj, vj)]))
                if key in seen:
                    continue
                seen.add(key)
                pairs.append((d, (si, vi), (sj, vj), ti, tj))
    return pairs

def exact_strip_pairs(min_tok):
    """Cross-surah pairs that are identical after pause-strip (d=0). Exact-twin domain."""
    m = defaultdict(list)
    for s, v, t in verses:
        if len(t) >= min_tok:
            m[" ".join(t)].append((s, v))
    pairs = []
    for txt, occ in m.items():
        surahs = sorted({s for s, _ in occ})
        if len(surahs) >= 2:
            for a, b in itertools.combinations(surahs, 2):
                pairs.append((a, b))
    return pairs

# ---- align differing tokens (for census + taxonomy) ----
def align_edits(a, b, k):
    """Backtrace token Levenshtein -> list of edits among {sub,ins,del}."""
    la, lb = len(a), len(b)
    INF = 10**9
    dp = [[INF] * (lb + 1) for _ in range(la + 1)]
    for i in range(la + 1):
        dp[i][0] = i
    for j in range(lb + 1):
        dp[0][j] = j
    for i in range(1, la + 1):
        for j in range(1, lb + 1):
            c = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + c)
    i, j = la, lb
    edits = []
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

CONNECTIVES = {"و", "ف", "ثم", "إن", "وإن", "أن", "وأن", "بل", "أم", "ل", "قد", "لقد",
               "إذ", "وإذ", "إذا", "وإذا", "ما", "لا", "ولا", "هو", "هم"}
PRONOUN_HINT = ("كم", "هم", "نا", "ه", "ها", "ني", "ك", "ي", "تم", "وا", "ون", "ين")
def classify_edit(op, x, y):
    """Lightweight edit-type taxonomy (descriptive)."""
    if op in ("ins", "del"):
        w = x if op == "del" else y
        if w in CONNECTIVES:
            return "connective/particle ins-del"
        return "single-word ins-del"
    # substitution
    if x in CONNECTIVES and y in CONNECTIVES:
        return "connective/particle swap"
    # shared trilateral-ish stem (first 3 consonantal chars) -> inflection/pronoun
    def stem(w):
        return "".join(ch for ch in w if ch not in "اوي")[:3]
    if stem(x) == stem(y) and stem(x):
        # differ by clitic/affix
        return "pronoun/inflection shift"
    # rhyme-driven: same length region, differ in final word only handled by caller
    return "name/epithet or lexical substitution"

# ============================ PRIMARY ============================
def surah_pairs_from(pairs):
    sp = set()
    for d, (si, vi), (sj, vj), ti, tj in pairs:
        sp.add(tuple(sorted((si, sj))))
    return sorted(sp)

def mean_pair_distance(surah_pairs, order):
    ds = [abs(order[a] - order[b]) for a, b in surah_pairs if order.get(a) and order.get(b)]
    return statistics.mean(ds) if ds else None, ds

primary_pairs = near_twin_pairs(L_PRIMARY, K_PRIMARY)
nt_surah_pairs = surah_pairs_from(primary_pairs)
D_obs, obs_ds = mean_pair_distance(nt_surah_pairs, rev)
n_sp = len(nt_surah_pairs)

ALL = [tuple(sorted(p)) for p in itertools.combinations(range(1, 115), 2)]
rng = random.Random(SEED)
nulls = []
le = 0
for _ in range(NPERM):
    pick = rng.sample(ALL, n_sp)
    dn = statistics.mean(abs(rev[a] - rev[b]) for a, b in pick)
    nulls.append(dn)
    if dn <= D_obs:
        le += 1
p_one = (le + 1) / (NPERM + 1)
null_mean = statistics.mean(nulls)

# Noldeke robustness
nold_ok = {k: v for k, v in nold.items() if v}
D_nold, _ = mean_pair_distance(nt_surah_pairs, nold_ok)

# period concordance
same = sum(1 for a, b in nt_surah_pairs if region[a] == region[b])
rng2 = random.Random(SEED + 1)
cgeq = 0
for _ in range(NPERM):
    pick = rng2.sample(ALL, n_sp)
    c = sum(1 for a, b in pick if region[a] == region[b])
    if c >= same:
        cgeq += 1
p_conc = (cgeq + 1) / (NPERM + 1)

verdict = ("CONFIRMED" if (D_obs < null_mean and p_one < 0.05)
           else ("NULL-REVERSED" if D_obs > null_mean else "NULL"))

# ============================ S3: EXACT vs NEAR ============================
exact_sp = sorted(set(exact_strip_pairs(L_PRIMARY)))
D_exact, _ = mean_pair_distance(exact_sp, rev)
n_exact = len(exact_sp)
rng3 = random.Random(SEED + 2)
le_e = 0; nulls_e = []
for _ in range(NPERM):
    pick = rng3.sample(ALL, n_exact)
    dn = statistics.mean(abs(rev[a] - rev[b]) for a, b in pick)
    nulls_e.append(dn)
    if dn <= D_exact:
        le_e += 1
p_exact = (le_e + 1) / (NPERM + 1)
null_mean_e = statistics.mean(nulls_e)

# ============================ S6: k / L ladder ============================
ladder = {}
for L in (6, 8, 10):
    for k in (1, 2, 3):
        ps = near_twin_pairs(L, k)
        sp = surah_pairs_from(ps)
        d, _ = mean_pair_distance(sp, rev)
        ladder[f"L{L}_k{k}"] = {"verse_pairs": len(ps), "surah_pairs": len(sp),
                                "D_obs_rev": round(d, 3) if d else None}

# ============================ S1/S2: census + taxonomy ============================
def ref(p): return f"{p[0]}:{p[1]}"
census = []
taxo = Counter()
for d, (si, vi), (sj, vj), ti, tj in sorted(primary_pairs, key=lambda r: (r[0], r[1], r[2])):
    edits = align_edits(ti, tj, K_PRIMARY)
    etypes = []
    for op, x, y in edits:
        # rhyme-driven detection: substitution at final token
        if op == "sub" and (ti[-1] == x and tj[-1] == y):
            t = "rhyme/final-word swap"
        else:
            t = classify_edit(op, x, y)
        etypes.append(t)
        taxo[t] += 1
    census.append({
        "dist": d,
        "ref_a": ref((si, vi)), "ref_b": ref((sj, vj)),
        "surah_a": si, "surah_b": sj,
        "name_a": sname[si], "name_b": sname[sj],
        "region_a": region[si], "region_b": region[sj],
        "rev_a": rev[si], "rev_b": rev[sj], "rev_dist": abs(rev[si] - rev[sj]),
        "tok_a": len(ti), "tok_b": len(tj),
        "text_a": " ".join(ti), "text_b": " ".join(tj),
        "edits": [{"op": o, "from": x, "to": y, "type": tp}
                  for (o, x, y), tp in zip(edits, etypes)],
    })

out = {
    "finding": "H-NEW-2380",
    "title": "Cross-surah near-twin verse census (<=k token edits) + revelation proximity",
    "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "k_primary": K_PRIMARY, "min_tokens_primary": L_PRIMARY,
    "tokenization": "no-tashkeel, waqf/pause-marks stripped, NFC, whitespace; cross-surah only; d=0 excluded",
    "counts": {
        "near_twin_verse_pairs": len(primary_pairs),
        "near_twin_verse_pairs_d1": sum(1 for r in census if r["dist"] == 1),
        "near_twin_verse_pairs_d2": sum(1 for r in census if r["dist"] == 2),
        "near_twin_distinct_surah_pairs": n_sp,
        "exact_strip_surah_pairs": n_exact,
    },
    "primary": {
        "D_obs_mean_rev_distance": round(D_obs, 3),
        "null_mean": round(null_mean, 3),
        "p_one_sided_closer": round(p_one, 5),
        "direction_locked": "near-twins closer than random",
        "verdict": verdict,
    },
    "s3_exact_vs_near": {
        "D_obs_near": round(D_obs, 3), "p_near": round(p_one, 5),
        "D_obs_exact": round(D_exact, 3), "p_exact": round(p_exact, 5),
        "null_mean": round(null_mean, 3),
        "more_clustered": "exact" if D_exact < D_obs else "near",
    },
    "robustness": {
        "D_obs_noldeke": round(D_nold, 3) if D_nold else None,
        "period_concordant_pairs": same, "total_surah_pairs": n_sp,
        "p_concordance": round(p_conc, 5),
    },
    "s6_ladder": ladder,
    "edit_taxonomy": dict(taxo.most_common()),
    "census": census,
}
json.dump(out, open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2380.json"), "w"),
          ensure_ascii=False, indent=2)

print(json.dumps(out["counts"], indent=2, ensure_ascii=False))
print(json.dumps(out["primary"], indent=2, ensure_ascii=False))
print("S3 exact vs near:", json.dumps(out["s3_exact_vs_near"], ensure_ascii=False))
print("period concordance:", same, "/", n_sp, "p=", round(p_conc, 4),
      "| Noldeke D=", out["robustness"]["D_obs_noldeke"])
print("edit taxonomy:", json.dumps(out["edit_taxonomy"], ensure_ascii=False))
print("k/L ladder:")
for kk, vv in ladder.items():
    print(f"  {kk}: {vv}")
print(f"[VERDICT] {verdict}")
