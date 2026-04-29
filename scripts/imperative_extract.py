#!/usr/bin/env python3
"""Phase B — Imperative-mood distribution.

Extract every imperative (IMPV) verb token, every prohibitive laA (POS:PRO)
and classify by addressee, semantic class, and surah location. Output CSVs
used by findings/phase-b-hypotheses/imperative-mood.md.
"""
import csv, os, re, json, collections

MORPH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
REV   = "/Users/grey/Downloads/quran/data/revelation-order.csv"
VCNTS = "/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv"
OUT   = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses"
CSVD  = os.path.join(OUT, "csv")
os.makedirs(CSVD, exist_ok=True)

LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")

# Load revelation metadata
meccan = {}
with open(REV) as f:
    for r in csv.DictReader(f):
        meccan[int(r["mushaf_order"])] = r["period"]

verse_counts = {}
with open(VCNTS) as f:
    for line in f:
        s, v = line.strip().split("\t")
        verse_counts[int(s)] = int(v)

# Parse morphology
segments = []  # every segment line
with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        loc, form, tag, feat = parts
        m = LOC_RE.match(loc)
        if not m:
            continue
        s, v, w, sg = [int(x) for x in m.groups()]
        segments.append({
            "s": s, "v": v, "w": w, "sg": sg,
            "form": form, "tag": tag, "feat": feat
        })

# Index by (s,v,w) → list of segments (ordered)
by_word = collections.defaultdict(list)
for seg in segments:
    by_word[(seg["s"], seg["v"], seg["w"])].append(seg)

# ---- (1) Collect imperatives ----
imperatives = [s for s in segments if s["tag"] == "V" and "|IMPV" in s["feat"]]

# Helper — extract lemma, root, person features
LEM_RE  = re.compile(r"LEM:([^\|]+)")
ROOT_RE = re.compile(r"ROOT:([^\|]+)")
PGN_RE  = re.compile(r"\|(\dM[SDP]|\dF[SDP]|\dMS|\dFS|\dMP|\dFP|\dMD|\dFD)(?:\||$)")

def feat_lookup(feat, pat):
    m = pat.search(feat)
    return m.group(1) if m else ""

for s in imperatives:
    s["lem"]  = feat_lookup(s["feat"], LEM_RE)
    s["root"] = feat_lookup(s["feat"], ROOT_RE)
    s["pgn"]  = feat_lookup(s["feat"], PGN_RE)

# ---- (2) Build helpers for addressee detection ----
# Look at surrounding context — previous word / particle of address.
# The context window = previous two words in the same verse, and the
# vocative yaA + following noun (nidaa).

# Precompute, per (s,v), ordered list of (w, [segs]).
verse_words = collections.defaultdict(list)
for (s, v, w), segs in by_word.items():
    verse_words[(s, v)].append((w, segs))
for key in verse_words:
    verse_words[key].sort()

def verse_form(s, v):
    """Return concatenated Buckwalter forms of a verse (spaces between words)."""
    return " ".join("".join(seg["form"] for seg in segs)
                    for w, segs in verse_words[(s, v)])

# Detect vocatives in a verse → list of (word_idx, callee_buckwalter)
VOC_NAMES = {
    # family of prophets — by root where handy
    "{ln~aAsu": "humanity",  "n~aAsu": "humanity",
    "{l~a*iyna": "believers-or-group",
}
# We use feat "VOC" for the vocative particle yaA, and inspect next token(s).
vocatives = collections.defaultdict(list)  # (s,v) -> [(w, target_form)]
for (s, v), wlist in verse_words.items():
    for i, (w, segs) in enumerate(wlist):
        first = segs[0]
        if first["tag"] == "VOC":
            # next word(s) — include up to 3 following words
            nxt_forms = []
            for w2, segs2 in wlist[i+1:i+4]:
                nxt_forms.append("".join(x["form"] for x in segs2))
            vocatives[(s, v)].append((w, " ".join(nxt_forms)))

# Named-prophet addressee detection (via LEM fields in following words of vocative)
PROPHET_LEMS = {
    "muwsaY": "Moses",
    "haAruwn": "Aaron",
    "yuwsufu": "Joseph",
    "<ibor`hiym": "Abraham",
    "nuwH": "Noah",
    "zakariy~aA": "Zechariah",
    "yaHoyaY": "John",
    "Eiysay": "Jesus",
    "daAwud": "David",
    "sulayom`n": "Solomon",
    "muHam~ad": "Muhammad",
}

def addressee(imp_seg):
    """Best-effort classification of the addressee of an imperative."""
    s, v, w = imp_seg["s"], imp_seg["v"], imp_seg["w"]
    pgn = imp_seg["pgn"]
    # (a) vocative in same verse?
    vocs = vocatives.get((s, v), [])
    if vocs:
        # check for named prophets in any vocative phrase
        for vw, phrase in vocs:
            for lem, name in PROPHET_LEMS.items():
                if lem in phrase:
                    return ("prophet:" + name, "voc")
            # common vocatives
            if "{ln~aAsu" in phrase or "n~aAsu" in phrase:
                return ("humanity", "voc")
            if "{l~a*iyna" in phrase or "l~a*iyna" in phrase:
                # "yaa ayyuhaa al-ladheena aamanuu"
                return ("believers", "voc")
            if "{lnabiy" in phrase or "lnabiy" in phrase or "n~abiy" in phrase:
                return ("prophet:Muhammad", "voc-nabi")
            if "rasuwl" in phrase or "{lr~asuwl" in phrase:
                return ("prophet:Muhammad", "voc-rasul")
            if "bani" in phrase and "<isor`'iyl" in phrase:
                return ("children-of-israel", "voc")
            if "kaAfir" in phrase or "kaAfiru" in phrase:
                return ("disbelievers", "voc")
    # (b) Is this a "qul" verb? — lemma qaAla with IMPV form
    if imp_seg["lem"] == "qaAla" and pgn == "2MS":
        return ("prophet:Muhammad", "qul")
    # (c) Singular masculine address w/o vocative → usually the Prophet
    if pgn == "2MS":
        return ("prophet:Muhammad", "2MS-default")
    # (d) Plural masculine → community (believers unless refuted)
    if pgn == "2MP":
        return ("believers-or-group", "2MP-default")
    if pgn == "2FS":
        return ("female-individual", "2FS")
    if pgn == "2FP":
        return ("women", "2FP")
    if pgn == "2MD":
        return ("dual-addressee", "2MD")
    return ("unknown", "unknown")

for s in imperatives:
    tgt, rule = addressee(s)
    s["addressee"] = tgt
    s["rule"] = rule

# ---- (3) Qul corpus ----
qul = [s for s in imperatives if s["lem"] == "qaAla" and s["pgn"] == "2MS"]
qul_verses = collections.Counter()
for q in qul:
    qul_verses[(q["s"], q["v"])] += 1

# ---- (4) Prohibitive laA + jussive ----
# Detect by scanning for POS:PRO laA, then check next verb is MOOD:JUS
prohibitive_pairs = []
for (s, v), wlist in verse_words.items():
    for i, (w, segs) in enumerate(wlist):
        for seg in segs:
            if seg["tag"] == "PRO" and seg["form"].startswith("laA"):
                # find the verb in the same word or the next word
                cand_verbs = []
                for seg2 in segs:
                    if seg2["tag"] == "V":
                        cand_verbs.append(seg2)
                for w2, segs2 in wlist[i+1:i+2]:
                    for seg2 in segs2:
                        if seg2["tag"] == "V":
                            cand_verbs.append(seg2)
                for vs in cand_verbs:
                    if "MOOD:JUS" in vs["feat"]:
                        prohibitive_pairs.append({
                            "s": s, "v": v, "w": w,
                            "laA_form": seg["form"],
                            "verb_form": vs["form"],
                            "verb_lem": feat_lookup(vs["feat"], LEM_RE),
                            "verb_root": feat_lookup(vs["feat"], ROOT_RE),
                            "verb_pgn": feat_lookup(vs["feat"], PGN_RE),
                        })
                        break

# ---- (5) Ritual imperatives ----
RITUAL_ROOTS = {"qwm", "zkw", "rkE", "sjd", "Swm", "Hjj", "*kr", "sbH"}
# We're interested in: aqImū Salāh (qwm form-IV imperative with object Salaah),
# ātū zakāh (Aty form IV imperative), but a safer proxy is to flag imperatives
# whose lemma root is in RITUAL_ROOTS or whose lemma is 'aqaAma/'aAtaY with
# certain typical objects.

# ---- (6) Emphatic imperative (iʿlam, ufhum) ----
EMPH_ROOTS = {"Elm", "fhm", "An*r", "n*r", "bSr"}

# ---- (7) Challenge imperatives (faʾtū bi-sūra etc.) ----
# detect IMPV from root Aty (come/bring) followed closely by a challenge context word (suwra / mivl / Ay`p)
challenge = []
for s in imperatives:
    if s["root"] == "Aty":
        v_forms = verse_form(s["s"], s["v"])
        if "suwr" in v_forms or "mivol" in v_forms or "Hadiyv" in v_forms or "burohaAn" in v_forms:
            challenge.append(s)

# ---- Write per-surah density ----
per_surah = collections.Counter()
for imp in imperatives:
    per_surah[imp["s"]] += 1

# ---- CSV 1: all imperative tokens ----
with open(os.path.join(CSVD, "imperatives-all-tokens.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["surah", "verse", "word", "seg", "form", "lemma", "root",
                "pgn", "addressee", "rule"])
    for s in imperatives:
        w.writerow([s["s"], s["v"], s["w"], s["sg"], s["form"],
                    s["lem"], s["root"], s["pgn"],
                    s["addressee"], s["rule"]])

# ---- CSV 2: per-surah density ----
with open(os.path.join(CSVD, "imperatives-per-surah.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["surah", "period", "verses", "impv_count",
                "impv_per_verse", "qul_count"])
    qul_per_s = collections.Counter(q["s"] for q in qul)
    for s in range(1, 115):
        vc = verse_counts.get(s, 0)
        ic = per_surah[s]
        w.writerow([s, meccan.get(s, ""), vc, ic,
                    round(ic / vc, 4) if vc else 0, qul_per_s[s]])

# ---- CSV 3: prohibitive pairs ----
with open(os.path.join(CSVD, "imperatives-prohibitive.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["surah", "verse", "word", "laA_form",
                "verb_form", "verb_lem", "verb_root", "verb_pgn"])
    for p in prohibitive_pairs:
        w.writerow([p["s"], p["v"], p["w"], p["laA_form"],
                    p["verb_form"], p["verb_lem"],
                    p["verb_root"], p["verb_pgn"]])

# ---- CSV 4: qul catalog ----
with open(os.path.join(CSVD, "imperatives-qul-catalog.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["surah", "verse", "word"])
    for q in qul:
        w.writerow([q["s"], q["v"], q["w"]])

# ---- Stats summary ----
stats = {
    "total_impv_tokens": len(imperatives),
    "unique_impv_lemmas": len({s["lem"] for s in imperatives}),
    "unique_impv_roots":  len({s["root"] for s in imperatives if s["root"]}),
    "qul_tokens": len(qul),
    "qul_unique_verses": len(qul_verses),
    "prohibitive_tokens": len(prohibitive_pairs),
    "challenge_aty_count": len(challenge),
}

# addressee distribution
addr_counter = collections.Counter(s["addressee"] for s in imperatives)
stats["addressee_distribution"] = dict(addr_counter.most_common())

# top lemmas
lem_counter = collections.Counter((s["lem"], s["root"]) for s in imperatives)
stats["top_20_lemmas"] = [
    {"lemma": l, "root": r, "count": c}
    for (l, r), c in lem_counter.most_common(20)
]

# pgn distribution
pgn_counter = collections.Counter(s["pgn"] for s in imperatives)
stats["pgn_distribution"] = dict(pgn_counter.most_common())

# ritual/emphatic counts
ritual_ct = sum(1 for s in imperatives if s["root"] in RITUAL_ROOTS)
emph_ct   = sum(1 for s in imperatives if s["root"] in EMPH_ROOTS)
stats["ritual_imperatives"] = ritual_ct
stats["emphatic_imperatives"] = emph_ct

# Meccan vs Medinan density
mc_imp = mc_v = md_imp = md_v = 0
for s in range(1, 115):
    vc = verse_counts.get(s, 0)
    ic = per_surah[s]
    p = meccan.get(s, "")
    if p == "Meccan":
        mc_imp += ic; mc_v += vc
    elif p == "Medinan":
        md_imp += ic; md_v += vc
stats["meccan_impv_per_verse"]  = round(mc_imp / mc_v, 4) if mc_v else 0
stats["medinan_impv_per_verse"] = round(md_imp / md_v, 4) if md_v else 0
stats["meccan_totals"]  = {"impv": mc_imp, "verses": mc_v}
stats["medinan_totals"] = {"impv": md_imp, "verses": md_v}

# top-density surahs
densities = []
for s in range(1, 115):
    vc = verse_counts.get(s, 0)
    if vc == 0: continue
    densities.append((s, meccan.get(s, ""), vc, per_surah[s],
                      per_surah[s] / vc))
densities.sort(key=lambda x: -x[4])
stats["top_20_density_surahs"] = [
    {"surah": s, "period": p, "verses": vc,
     "impv": ic, "impv_per_verse": round(d, 4)}
    for s, p, vc, ic, d in densities[:20]
]
stats["bottom_20_density_surahs"] = [
    {"surah": s, "period": p, "verses": vc,
     "impv": ic, "impv_per_verse": round(d, 4)}
    for s, p, vc, ic, d in densities[-20:]
]

# prohibitive pgn distribution
proh_pgn = collections.Counter(p["verb_pgn"] for p in prohibitive_pairs)
stats["prohibitive_pgn_dist"] = dict(proh_pgn.most_common())

# Top prohibitive roots (what are we being told NOT to do?)
proh_root = collections.Counter(p["verb_root"] for p in prohibitive_pairs)
stats["top_prohibitive_roots"] = [
    {"root": r, "count": c}
    for r, c in proh_root.most_common(20)
]

with open(os.path.join(CSVD, "imperatives-stats.json"), "w") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)

print(json.dumps(stats, indent=2, ensure_ascii=False))
