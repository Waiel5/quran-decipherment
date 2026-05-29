#!/usr/bin/env python3
"""
H-NEW-2410 — Explicit number-word census + counted-referent distribution.
CENSUS, NOT NUMEROLOGY. No miracle-claim. Descriptive-primary + ONE locked
inferential test (Test A collocation, Test B register density; Bonferroni k=2).

Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2410-number-word-census.md
Direction LOCKED before computation:
  A) sabʿ(7) modal counted-noun = samāwāt (root smw), beyond base-rate.
  B) number-word density Medinan > Meccan.
Seed 20260509, 10000 permutations. Rules-tuple: QAC v0.4 lemma+root+POS, words.

Author: Waiel Al-Shujaa.
"""
import json, re, hashlib, random, os, statistics

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2410-number-word-census.md")
EXPECTED_SHA = "1fdf55d1c8193dc299f87ceac66342482e44106f210689bd741329a7ebb3191f"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2410.json")
SEED = 20260509
NPERM = 10000

# --- runtime pre-reg integrity check ---
with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

# ============================================================
# LOCKED number-lemma whitelist (root, lemma) -> (kind, value, gloss)
# kind in {cardinal, ordinal, fraction, distributive}
# value is the numeric value (None for distributive/oft-repeated)
# ============================================================
CARD = {
    ("wHd", "wa`Hid"): (1, "wahid"),
    ("wHd", "wa`Hidap"): (1, "wahida"),
    ("vny", "{vonayon"): (2, "ithnan"),
    ("vny", "{vonatayon"): (2, "ithnatan"),
    ("vlv", "vala`v"): (3, "thalath"),
    ("vlv", "vala`vap"): (3, "thalatha"),
    ("vlv", "v~aAlivap"): (3, "thulatha"),
    ("rbE", ">arobaE"): (4, "arbaA"),
    ("rbE", ">arobaEap"): (4, "arbaAa"),
    ("rbE", "ruba`E"): (4, "rubaA"),
    ("xms", "xamosap"): (5, "khamsa"),
    ("xms", "xamos"): (5, "khams"),
    ("stt", "sit~ap"): (6, "sitta"),
    ("sbE", "saboE"): (7, "sabA"),
    ("sbE", "saboEap"): (7, "sabAa"),
    ("vmn", "vama`niyap"): (8, "thamaniya"),
    ("vmn", "vama`niY"): (8, "thamani"),
    ("tsE", "tisoE"): (9, "tisA"),
    ("tsE", "tisoEap"): (9, "tisAa"),
    ("E$r", "Ea$or"): (10, "ashr"),
    ("E$r", "Ea$orap"): (10, "ashara"),
    ("E$r", "Ea$ar"): (10, "ashar"),
    ("mAy", "miA}ap"): (100, "mia"),
    ("Alf", ">alof"): (1000, "alf"),
    ("E$r", "Ei$oruwn"): (20, "ishrun"),
    ("xms", "xamosiyn"): (50, "khamsin"),
    ("vmn", "vama`niyn"): (80, "thamanin"),
    ("stt", "sit~iyn"): (60, "sittin"),
    ("vlv", "vala`viyn"): (30, "thalathin"),
}
# tens that QAC stores under the base cardinal lemma + suffix in FORM:
#   >arobaE + -iyn = 40 ;  saboE + -uwn = 70
TENS_BY_FORM = {  # (root,lemma): {suffix: value}
    ("rbE", ">arobaE"): {"iyn": 40},
    ("sbE", "saboE"): {"uwn": 70},
}
ORD = {
    ("Awl", ">aw~al"): (1, "awwal"),
    ("vny", "vaAniY"): (2, "thani"),
    ("vlv", "vaAliv"): (3, "thalith"),
    ("rbE", "raAbiE"): (4, "rabiA"),
    ("xms", "xa`misap"): (5, "khamisa"),
    ("sds", "saAdis"): (6, "sadis"),
    ("vmn", "vaAmin"): (8, "thamin"),
}
FRAC = {
    ("nSf", "niSof"): ("1/2", "nisf"),
    ("vlv", "v~uluv"): ("1/3", "thuluth"),
    ("rbE", "r~ubuE"): ("1/4", "rubu"),
    ("xms", "xumus"): ("1/5", "khumus"),
    ("sds", "s~udus"): ("1/6", "sudus"),
    ("vmn", "v~umun"): ("1/8", "thumun"),
    ("E$r", "miEo$aAr"): ("1/10", "mishar"),
}
DISTRIB = {  # distributive / oft-repeated — reported separately
    ("vny", "mavonaY`"): ("mathna", "two-by-two"),
    ("vny", "m~avaAniY"): ("mathani", "oft-repeated (al-mathani)"),
}
ISOLATION = {  # wHd isolation-sense, NOT cardinal one
    ("wHd", "waHod"): "wahda (alone/by-itself)",
    ("wHd", "waHiyd"): "wahid (alone, Q74:11)",
}
ZAWJ = {("zwj", "zawoj"), ("zwj", "zuw~ijato")}  # pair/spouse — separate line

# ============================================================
# parse QAC
# ============================================================
loc_re = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
def feat(feats, key):
    m = re.search(key + r":([^|]+)", feats)
    return m.group(1) if m else ""

rows = []  # (s,v,w,seg, form, tag, feats, lem, root, pos, is_stem)
for line in open(MORPH, encoding="utf-8"):
    if not line.startswith("("):
        continue
    p = line.rstrip("\n").split("\t")
    if len(p) < 4:
        continue
    m = loc_re.match(p[0])
    if not m:
        continue
    s, v, w, seg = map(int, m.groups())
    feats = p[3]
    lem = feat(feats, "LEM")
    rt = feat(feats, "ROOT")
    pos = feat(feats, "POS")
    rows.append((s, v, w, seg, p[1], p[2], feats, lem, rt, pos, "STEM" in feats))

# word-level stem (first stem segment of each word) -> (lem, root, pos)
word_stem = {}
for s, v, w, seg, form, tag, feats, lem, rt, pos, is_stem in rows:
    if is_stem and (s, v, w) not in word_stem:
        word_stem[(s, v, w)] = (lem, rt, pos)

quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
total_words_surah = {}   # words per surah (QAC word count = max word index per verse summed)
for s in quran:
    pass
# QAC word count per surah from morphology (count distinct (s,v,w))
wkeys = set((s, v, w) for (s, v, w) in word_stem.keys())
total_words_surah = {i: 0 for i in range(1, 115)}
for (s, v, w) in wkeys:
    total_words_surah[s] += 1

# ============================================================
# CENSUS
# ============================================================
from collections import defaultdict, Counter

card_hits = []   # (value, gloss, s, v, w, head_root, head_lem)
ord_hits = []
frac_hits = []
distrib_hits = []
isolation_hits = []
zawj_hits = []
card_by_value = Counter()
card_surahs = defaultdict(set)
lemma_count = Counter()
lemma_surahs = defaultdict(set)
tens_hits = []   # (value, s,v,w)

def head_noun(s, v, w):
    """immediate syntactic head = next stem-bearing content word."""
    for nxt in (w + 1, w + 2):
        st = word_stem.get((s, v, nxt))
        if st and st[2] in ("N", "PN", "ADJ"):
            return st[1], st[0]  # (root, lemma)
    return ("", "")

for s, v, w, seg, form, tag, feats, lem, rt, pos, is_stem in rows:
    if not is_stem:
        continue
    key = (rt, lem)
    # tens stored under base cardinal lemma + suffix in FORM
    if key in TENS_BY_FORM:
        matched_ten = None
        for suf, val in TENS_BY_FORM[key].items():
            if suf in form:
                matched_ten = val
                break
        if matched_ten is not None:
            tens_hits.append((matched_ten, s, v, w))
            card_by_value[matched_ten] += 1
            card_surahs[matched_ten].add(s)
            lemma_count[f"{lem}({matched_ten})"] += 1
            lemma_surahs[f"{lem}({matched_ten})"].add(s)
            continue  # do not also count as base cardinal
    if key in CARD:
        val, gloss = CARD[key]
        hr, hl = head_noun(s, v, w)
        card_hits.append((val, gloss, s, v, w, hr, hl))
        card_by_value[val] += 1
        card_surahs[val].add(s)
        lemma_count[f"{lem}({val})"] += 1
        lemma_surahs[f"{lem}({val})"].add(s)
    elif key in ORD:
        val, gloss = ORD[key]
        ord_hits.append((val, gloss, s, v, w))
        lemma_count[f"{lem}(ord{val})"] += 1
        lemma_surahs[f"{lem}(ord{val})"].add(s)
    elif key in FRAC:
        val, gloss = FRAC[key]
        frac_hits.append((val, gloss, s, v, w))
        lemma_count[f"{lem}({val})"] += 1
        lemma_surahs[f"{lem}({val})"].add(s)
    elif key in DISTRIB:
        g, d = DISTRIB[key]
        distrib_hits.append((g, s, v, w))
    elif key in ISOLATION:
        isolation_hits.append((ISOLATION[key], s, v, w))
    elif key in ZAWJ:
        zawj_hits.append((lem, s, v, w))

# counted-noun distribution per cardinal value
head_dist = defaultdict(Counter)  # value -> Counter(head_root)
for val, gloss, s, v, w, hr, hl in card_hits:
    if hr:
        head_dist[val][hr] += 1

# global most-counted referents (across all cardinals)
global_heads = Counter()
for val, gloss, s, v, w, hr, hl in card_hits:
    if hr:
        global_heads[hr] += 1

# ============================================================
# TEST A — sabA(7) modal counted-noun = smw, beyond base-rate
# ============================================================
sabA_heads = [hr for val, g, s, v, w, hr, hl in card_hits if val == 7 and hr]
sabA_head_counter = Counter(sabA_heads)
empirical_argmax = sabA_head_counter.most_common(1)[0] if sabA_head_counter else ("", 0)
obs_smw = sabA_head_counter.get("smw", 0)
n_sabA_with_head = len(sabA_heads)

# control bag = head-noun multiset of ALL cardinals (instrument-control, MW-6)
control_bag = [hr for val, g, s, v, w, hr, hl in card_hits if hr]
rngA = random.Random(SEED)
null_max_collocate = []
for _ in range(NPERM):
    draw = [rngA.choice(control_bag) for _ in range(n_sabA_with_head)]
    null_max_collocate.append(Counter(draw).most_common(1)[0][1])
# how often does any single noun reach >= observed smw count under the null
ge = sum(1 for x in null_max_collocate if x >= obs_smw)
pA = (ge + 1) / (NPERM + 1)
p95_null_max = sorted(null_max_collocate)[int(0.95 * NPERM)]
A_argmax_is_smw = (empirical_argmax[0] == "smw")
A_pass = bool(A_argmax_is_smw and obs_smw > p95_null_max)

# ============================================================
# TEST B — number-word density Medinan > Meccan
# density = ALL number-tokens (card+ord+frac+tens) per 1000 words
# ============================================================
num_tokens_surah = {i: 0 for i in range(1, 115)}
for val, gloss, s, v, w, hr, hl in card_hits:
    num_tokens_surah[s] += 1
for val, s, v, w in tens_hits:
    num_tokens_surah[s] += 1
for val, gloss, s, v, w in ord_hits:
    num_tokens_surah[s] += 1
for val, gloss, s, v, w in frac_hits:
    num_tokens_surah[s] += 1

density = {}
for i in range(1, 115):
    tw = total_words_surah[i]
    density[i] = (num_tokens_surah[i] / tw * 1000.0) if tw else 0.0

meccan = [i for i in range(1, 115) if region[i] == "meccan"]
medinan = [i for i in range(1, 115) if region[i] == "medinan"]
mean_mec = statistics.mean(density[i] for i in meccan)
mean_med = statistics.mean(density[i] for i in medinan)
obs_dB = mean_med - mean_mec  # locked direction: > 0

labels = [region[i] for i in range(1, 115)]
dvals = [density[i] for i in range(1, 115)]
rngB = random.Random(SEED)
n_med = len(medinan)
ge_B = 0
idx = list(range(114))
for _ in range(NPERM):
    rngB.shuffle(idx)
    med_idx = idx[:n_med]
    mec_idx = idx[n_med:]
    dm = statistics.mean(dvals[j] for j in med_idx)
    dc = statistics.mean(dvals[j] for j in mec_idx)
    if (dm - dc) >= obs_dB:
        ge_B += 1
pB = (ge_B + 1) / (NPERM + 1)
ALPHA = 0.025  # Bonferroni k=2
B_direction_ok = obs_dB > 0
B_pass = bool(B_direction_ok and pB < ALPHA)
B_reversed = (obs_dB < 0)

# variant: root-bearing-token density (MW-3 alt model)
root_tok_surah = {i: 0 for i in range(1, 115)}
for (s, v, w), (lem, rt, pos) in word_stem.items():
    if rt:
        root_tok_surah[s] += 1
densB2 = {}
for i in range(1, 115):
    rt = root_tok_surah[i]
    densB2[i] = (num_tokens_surah[i] / rt * 1000.0) if rt else 0.0
mean_mec2 = statistics.mean(densB2[i] for i in meccan)
mean_med2 = statistics.mean(densB2[i] for i in medinan)
obs_dB2 = mean_med2 - mean_mec2

# ============================================================
# emit
# ============================================================
def name_of(i):
    return next(s["transliteration"] for s in quran if s["id"] == i) if any(s["id"]==i for s in quran) else str(i)

out = {
    "finding": "H-NEW-2410",
    "prereg_sha256": actual,
    "seed": SEED, "nperm": NPERM,
    "note": "CENSUS not numerology. Single-lexeme counts are facts; only Tests A/B carry verdicts.",
    "census": {
        "cardinal_by_value": {str(k): card_by_value[k] for k in sorted(card_by_value)},
        "cardinal_surahs": {str(k): sorted(card_surahs[k]) for k in sorted(card_surahs)},
        "total_cardinal_tokens": len(card_hits) + len(tens_hits),
        "total_ordinal_tokens": len(ord_hits),
        "total_fraction_tokens": len(frac_hits),
        "lemma_count": dict(lemma_count.most_common()),
        "tens_detail": [{"value": v, "ref": f"{s}:{vv}:{w}"} for (v, s, vv, w) in tens_hits],
        "ordinals": [{"value": v, "gloss": g, "ref": f"{s}:{vv}:{w}"} for (v, g, s, vv, w) in ord_hits],
        "fractions": [{"value": v, "gloss": g, "ref": f"{s}:{vv}:{w}"} for (v, g, s, vv, w) in frac_hits],
        "distributive": [{"gloss": g, "ref": f"{s}:{vv}:{w}"} for (g, s, vv, w) in distrib_hits],
        "isolation_sense_excluded": [{"gloss": g, "ref": f"{s}:{vv}:{w}"} for (g, s, vv, w) in isolation_hits],
        "zawj_excluded_count": len(zawj_hits),
    },
    "counted_referents": {
        "per_value_head_root": {str(v): dict(head_dist[v].most_common()) for v in sorted(head_dist)},
        "global_most_counted_root": dict(global_heads.most_common(20)),
    },
    "test_A_seven_heavens": {
        "claim": "sabA(7) modal counted-noun is smw (heaven), beyond base-rate",
        "sabA_head_distribution": dict(sabA_head_counter.most_common()),
        "n_sabA_with_determinable_head": n_sabA_with_head,
        "obs_sabA_smw_count": obs_smw,
        "empirical_argmax": list(empirical_argmax),
        "argmax_is_smw": A_argmax_is_smw,
        "null_p95_max_collocate": p95_null_max,
        "p_value": pA,
        "PASS": A_pass,
    },
    "test_B_register_density": {
        "claim": "number-word density Medinan > Meccan (locked direction)",
        "mean_density_meccan_per1000word": round(mean_mec, 4),
        "mean_density_medinan_per1000word": round(mean_med, 4),
        "obs_delta_med_minus_mec": round(obs_dB, 4),
        "p_value": pB,
        "alpha_bonferroni_k2": ALPHA,
        "direction_ok": B_direction_ok,
        "reversed_precommit_violation": B_reversed,
        "PASS": B_pass,
        "variant_root_token_density": {
            "mean_meccan": round(mean_mec2, 4),
            "mean_medinan": round(mean_med2, 4),
            "obs_delta": round(obs_dB2, 4),
        },
    },
    "per_surah_density_top15": sorted(
        [{"surah": i, "name": name_of(i), "region": region[i],
          "num_tokens": num_tokens_surah[i], "words": total_words_surah[i],
          "density_per1000": round(density[i], 3)} for i in range(1, 115)],
        key=lambda d: -d["density_per1000"])[:15],
}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# ---- console summary ----
print("\n========== CENSUS ==========")
print("Cardinal tokens (incl tens):", len(card_hits) + len(tens_hits))
print("By value:", {k: card_by_value[k] for k in sorted(card_by_value)})
print("Ordinal tokens:", len(ord_hits), "| Fraction tokens:", len(frac_hits))
print("zawj (pair) excluded:", len(zawj_hits), "| isolation-sense excluded:", len(isolation_hits))
print("\nGlobal most-counted head-roots:", global_heads.most_common(10))
print("\n========== TEST A (seven-heavens) ==========")
print("sabA head dist:", sabA_head_counter.most_common())
print(f"obs sabA+smw={obs_smw}, argmax={empirical_argmax}, argmax_is_smw={A_argmax_is_smw}")
print(f"null p95 max-collocate={p95_null_max}, p={pA:.5f}, PASS={A_pass}")
print("\n========== TEST B (register density) ==========")
print(f"density Meccan={mean_mec:.4f} Medinan={mean_med:.4f} (per 1000 words)")
print(f"Delta(med-mec)={obs_dB:.4f}, p={pB:.5f}, alpha={ALPHA}, dir_ok={B_direction_ok}, PASS={B_pass}, reversed={B_reversed}")
print(f"[variant root-token density] Meccan={mean_mec2:.4f} Medinan={mean_med2:.4f} Delta={obs_dB2:.4f}")
print(f"\n[ok] wrote {OUT}")
