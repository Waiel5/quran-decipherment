#!/usr/bin/env python3
"""
Comprehensive oath-cluster detection for the Quran.

Oath patterns detected:

  A. waw-oath:   verse opens with [w tagged P or CONJ] + (optional DET) + N/PN/ADJ
                 (the sworn-by noun). Cluster = >=2 consecutive such verses.
  B. qsm-oath:   verse contains "(la) uqsimu bi-..." (V with ROOT=qsm in imperfect
                 1st-singular) + bi + noun. Can be fronted with "fa la" / "la".
  C. muqatta'at-preceded oath: first word is INL (initial letter) and the second
                 word is waw-oath (e.g. Q 50:1, Q 68:1). Treated as same as A.

We build the full catalog per-verse, then collapse runs into clusters.
For a cluster, we record:
  - sequence of sworn-by objects (form, lemma, root, category)
  - sworn-about verse(s): look for the first verse AFTER the cluster
    that does not open with oath. If that verse opens with <in~a / >in~a (ACC),
    qad, la+verb, etc., it is the sworn-about. We record the first verse.
  - category tags per sworn-by
  - detection of chiastic/mirrored category sequences
  - length, whether it opens the surah, final fasila for phonetic tie-in.
"""
import json, re, csv, os
from collections import defaultdict, Counter

QURAN_JSON = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
MORPH      = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
TRANS      = "/Users/grey/Downloads/quran/data/translations/en.sahih.txt"
OUT_DIR    = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses"

# ---------- Load Quran ----------
quran = json.load(open(QURAN_JSON))
surah_info = {}
for s in quran:
    surah_info[s["id"]] = {
        "name": s["transliteration"],
        "type": s["type"],
        "verses": {v["id"]: v["text"] for v in s["verses"]},
        "n_verses": s["total_verses"],
    }

# ---------- Translation ----------
trans = {}
for ln in open(TRANS):
    ln = ln.strip()
    if not ln or ln.startswith("#"): continue
    parts = ln.split("|", 2)
    if len(parts) != 3: continue
    try:
        s = int(parts[0]); v = int(parts[1])
    except ValueError: continue
    trans[(s,v)] = parts[2]

# ---------- Morphology ----------
loc_re = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
verse_segs = defaultdict(list)

def parse_features(s):
    d = {}
    for t in s.split("|"):
        t = t.strip()
        if ":" in t:
            k,v = t.split(":",1); d[k]=v
        else: d[t]=True
    return d

for ln in open(MORPH):
    if not ln.strip() or ln.startswith("#") or ln.startswith("LOCATION"): continue
    parts = ln.rstrip("\n").split("\t")
    if len(parts) < 4: continue
    loc, form, tag, feat = parts
    m = loc_re.match(loc)
    if not m: continue
    s,v,w,sg = map(int, m.groups())
    verse_segs[(s,v)].append({
        "w": w, "sg": sg, "form": form, "tag": tag,
        "feat": parse_features(feat),
    })
for k in verse_segs:
    verse_segs[k].sort(key=lambda x:(x["w"],x["sg"]))

# ---------- Oath detection ----------

def is_waw_prefix(seg):
    return seg["tag"] in ("P","CONJ") and seg["form"].startswith("w")

def is_fa_prefix(seg):
    return seg["tag"] in ("CONJ","REM","P","RSLT") and seg["form"].startswith("f")

def is_noun_like(seg):
    return seg["tag"] in ("N","PN","ADJ")

def has_gen_case(seg):
    """Check GEN in Leeds feature field"""
    feat = seg["feat"]
    # Some nouns have GEN as a bare key; others have it as value of case.
    return feat.get("GEN") is True or "GEN" in feat

def skip_det(segs, idx):
    while idx < len(segs) and segs[idx]["tag"] in ("DET","DEM"):
        idx += 1
    return idx

def all_oath_items_in_verse(s, v):
    """
    Scan the entire verse and return all waw-oath or fa-oath items: list of
    {pos, oath_type, root, lemma, form}. Useful for single-verse clusters
    that pack multiple sworn-by objects (e.g. Q 86:1 "wa-l-samāʾi wa-l-ṭāriq").
    """
    segs = verse_segs.get((s,v), [])
    items = []
    # Walk through segs and find each occurrence of (P|CONJ|REM "w"/"f" starter +
    # optional DET + N-GEN). We require GEN so we don't pick up coordinated
    # accusatives.
    i = 0
    while i < len(segs):
        seg = segs[i]
        if seg["tag"] in ("P","CONJ","REM") and seg["form"] and seg["form"][0] in "wf":
            k = i + 1
            while k < len(segs) and segs[k]["tag"] == "DET":
                k += 1
            if k < len(segs) and is_noun_like(segs[k]) and has_gen_case(segs[k]):
                sw = segs[k]
                items.append({
                    "pos": i,
                    "oath_type": "waw" if seg["form"].startswith("w") else "fa",
                    "root": sw["feat"].get("ROOT",""),
                    "lemma": sw["feat"].get("LEM",""),
                    "form": sw["form"],
                })
        i += 1
    return items


def oath_info_for_verse(s, v, allow_fa_continuation=False):
    """
    Detect oath structure at verse start.
    Patterns:
      A. waw-oath:     [INL?] (P|CONJ "w") [DET]? N/PN/ADJ[GEN]
      B. fa-oath cont: [INL?] (CONJ|REM "f") [DET]? N/PN/ADJ[GEN]    (only valid as continuation)
      C. qsm-oath:     [INL?] [REM?] [NEG?] V(root=qsm) [PRON]* P(bi) [DET]? N[GEN]
    Returns None, or dict {oath_type, sworn_root, sworn_lemma, sworn_form}.
    """
    segs = verse_segs.get((s,v), [])
    if not segs: return None

    idx = 0
    if idx < len(segs) and segs[idx]["tag"] == "INL":
        idx += 1

    # Pattern C: qsm verb somewhere at opening
    j = idx
    pre_tags_allowed = {"REM", "NEG", "CONJ"}
    while j < len(segs) and segs[j]["tag"] in pre_tags_allowed:
        j += 1
    if j < len(segs) and segs[j]["tag"] == "V" and segs[j]["feat"].get("ROOT") == "qsm":
        k = j + 1
        while k < len(segs) and segs[k]["tag"] == "PRON":
            k += 1
        if k < len(segs) and segs[k]["tag"] == "P" and segs[k]["form"] == "bi":
            m = skip_det(segs, k+1)
            if m < len(segs) and is_noun_like(segs[m]):
                sw = segs[m]
                # REQUIRE GEN (genitive) case since bi takes genitive
                if has_gen_case(sw):
                    return {
                        "oath_type": "qsm",
                        "sworn_root": sw["feat"].get("ROOT",""),
                        "sworn_lemma": sw["feat"].get("LEM",""),
                        "sworn_form": sw["form"],
                    }

    # Pattern A: waw-oath
    if idx < len(segs) and is_waw_prefix(segs[idx]):
        k = skip_det(segs, idx+1)
        if k < len(segs) and is_noun_like(segs[k]):
            sw = segs[k]
            # REQUIRE GEN — this is what distinguishes oath waw from conjunction waw
            if has_gen_case(sw):
                return {
                    "oath_type": "waw",
                    "sworn_root": sw["feat"].get("ROOT",""),
                    "sworn_lemma": sw["feat"].get("LEM",""),
                    "sworn_form": sw["form"],
                }

    # Pattern B: fa-continuation (only if caller says it's a legit continuation)
    if allow_fa_continuation and idx < len(segs) and is_fa_prefix(segs[idx]):
        k = skip_det(segs, idx+1)
        if k < len(segs) and is_noun_like(segs[k]):
            sw = segs[k]
            if has_gen_case(sw):
                return {
                    "oath_type": "fa",
                    "sworn_root": sw["feat"].get("ROOT",""),
                    "sworn_lemma": sw["feat"].get("LEM",""),
                    "sworn_form": sw["form"],
                }

    return None

# Build per-verse oath table (strict = waw/qsm only)
oath_verse_strict = {}
for s in surah_info:
    for v in sorted(surah_info[s]["verses"]):
        oi = oath_info_for_verse(s, v, allow_fa_continuation=False)
        if oi:
            oath_verse_strict[(s,v)] = oi

# ---------- Cluster assembly with fa-continuation ----------
# Start a cluster at any verse with waw or qsm oath opening (where previous
# verse does NOT have waw/qsm oath). Extend forward: include next verse iff
# it is a waw-oath OR a fa-oath (using allow_fa_continuation=True).

clusters = []
for s in surah_info:
    verses = sorted(surah_info[s]["verses"].keys())
    i = 0
    while i < len(verses):
        v = verses[i]
        if (s,v) not in oath_verse_strict:
            i += 1; continue
        # start only if previous is not part of ongoing cluster
        if i > 0 and verses[i-1] in [cl_end for cl in clusters
                                     if cl["surah"]==s
                                     for cl_end in range(cl["start_verse"], cl["end_verse"]+1)]:
            i += 1; continue
        items = []
        verse_spans = []  # list of (v, num_items_in_that_verse)
        j = i
        # First verse: get ALL oath items within the verse
        first_items = all_oath_items_in_verse(s, v)
        if oath_verse_strict[(s,v)]["oath_type"] == "qsm":
            # qsm verse: just record one item (the bi- noun)
            oi = oath_verse_strict[(s,v)]
            first_items = [{
                "pos": 0, "oath_type": "qsm",
                "root": oi["sworn_root"], "lemma": oi["sworn_lemma"],
                "form": oi["sworn_form"],
            }]
        for it in first_items:
            items.append({**it, "v": v})
        verse_spans.append((v, len(first_items)))
        j = i + 1
        # extend across verses
        while j < len(verses):
            vj = verses[j]
            oi_j = oath_info_for_verse(s, vj, allow_fa_continuation=True)
            if oi_j is None:
                break
            # take ALL oath items in this continuation verse
            vj_items = all_oath_items_in_verse(s, vj)
            if not vj_items:
                vj_items = [{"pos":0, "oath_type": oi_j["oath_type"],
                             "root": oi_j["sworn_root"], "lemma": oi_j["sworn_lemma"],
                             "form": oi_j["sworn_form"]}]
            for it in vj_items:
                items.append({**it, "v": vj})
            verse_spans.append((vj, len(vj_items)))
            j += 1
        clusters.append({
            "surah": s,
            "surah_name": surah_info[s]["name"],
            "surah_type": surah_info[s]["type"],
            "start_verse": items[0]["v"],
            "end_verse": items[-1]["v"],
            "n_verses": len(verse_spans),
            "n_items": len(items),
            "length": len(items),   # n_items (total sworn-by objects)
            "items": items,
            "verse_spans": verse_spans,
            "is_opening": items[0]["v"] == 1,
            "first_oath_type": items[0]["oath_type"],
            "oath_types": [it["oath_type"] for it in items],
        })
        i = j if j > i else i+1

# ---------- Sworn-about extraction ----------
# Look for the first verse AFTER the cluster that begins with one of:
#   - ACC (inna / <in~a): "indeed / verily"
#   - "la+V" (emphatic+verb)
#   - a plain declarative (we just take the next verse)
# We record the first post-cluster verse as the primary sworn-about, plus
# up to 2 more.

def post_cluster_verses(cl, n=3):
    s = cl["surah"]
    end = cl["end_verse"]
    verses = sorted(surah_info[s]["verses"].keys())
    post = [v for v in verses if v > end][:n]
    return post

for cl in clusters:
    pv = post_cluster_verses(cl, 3)
    cl["post_verses"] = pv
    cl["sworn_about_ar"] = [surah_info[cl["surah"]]["verses"][v] for v in pv]
    cl["sworn_about_en"] = [trans.get((cl["surah"], v), "") for v in pv]

# ---------- Semantic categories ----------
CATEGORY = {
    # celestial
    "$ms":"celestial","qmr":"celestial","smw":"celestial","njm":"celestial",
    "brj":"celestial","kwkb":"celestial",
    # temporal
    "lyl":"temporal","nhr":"temporal","DHw":"temporal","fjr":"temporal",
    "Sbh":"temporal","ESr":"temporal","ywm":"temporal","sry":"temporal",
    "sjw":"temporal","yqt":"temporal","wEd":"temporal","E$r":"temporal",
    "Trq":"celestial",
    # terrestrial
    "Twr":"terrestrial","tyn":"terrestrial","zyt":"terrestrial","bld":"terrestrial",
    "bHr":"terrestrial","ArD":"terrestrial","jbl":"terrestrial","wAd":"terrestrial",
    "byt":"terrestrial","sjr":"terrestrial","sqf":"terrestrial",
    # psychological
    "nfs":"psychological","qlb":"psychological","rwH":"psychological",
    "lwm":"psychological",
    # instrumental
    "qlm":"instrumental","ktb":"instrumental","sTr":"instrumental",
    "qrA":"instrumental","nwn":"instrumental","rqq":"instrumental",
    # warrior/kinetic (Q 100)
    "Edw":"warrior","qdH":"warrior","gyr":"warrior","vwr":"warrior",
    "wsT":"warrior","SbH":"warrior","DbH":"warrior",
    # wind-kinetic (Q 51, 77)
    "*rw":"wind","Hml":"wind","jry":"wind","qsm":"wind",
    "rsl":"wind","ESf":"wind","n$r":"wind","frq":"wind","lqy":"wind",
    # angelic (Q 37, 79)
    "Sff":"angelic","zjr":"angelic","tlw":"angelic",
    "nzE":"angelic","n$T":"angelic","sbH":"angelic","sbq":"angelic",
    "dbr":"angelic",
    # divine attribute / abstract
    "mjd":"abstract","rbb":"divine-lord","$hd":"abstract","qwm":"eschatological",
    "$fE":"numeric","wtr":"numeric","Hwl":"abstract",
    # Q 52 list
    "rfE":"celestial",
}

def category_of(root):
    return CATEGORY.get(root, "other")

for cl in clusters:
    for it in cl["items"]:
        it["category"] = category_of(it["root"])
    cl["category_sequence"] = [it["category"] for it in cl["items"]]
    cl["category_set"] = sorted(set(cl["category_sequence"]))
    cl["category_mixed"] = len(cl["category_set"]) > 1
    # detect chiastic sequence (palindromic category list)
    cs = cl["category_sequence"]
    cl["chiastic_categories"] = cs == cs[::-1] and len(cs) >= 3 and len(set(cs)) > 1

# ---------- Length distribution ----------
len_dist = Counter(cl["length"] for cl in clusters)
len_dist_multi = Counter(cl["length"] for cl in clusters if cl["length"]>=2)

# Classical candidate surahs
CANDIDATES = sorted(set([36,37,43,44,50,51,52,53,56,68,69,70,74,75,77,79,80,
                          81,84,85,86,89,90,91,92,93,95,100,103]))

# ---------- Saj' fasila for oath-cluster verses vs. rest of same surah ----------
# Load saj fasila per-verse CSV from earlier run if available
SAJ_CSV = os.path.join(OUT_DIR, "saj-fasila-per-verse.csv")
saj = {}
if os.path.exists(SAJ_CSV):
    with open(SAJ_CSV) as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                key = (int(row["surah"]), int(row["verse"]))
                saj[key] = row
            except (KeyError, ValueError):
                pass

# For each cluster surah compute: uniformity of fasila_2 within cluster vs. rest
def fasila_uniformity(values):
    if not values: return None
    c = Counter(values); return c.most_common(1)[0][1] / len(values)

for cl in clusters:
    s = cl["surah"]
    cluster_verses = [v for v in range(cl["start_verse"], cl["end_verse"]+1)]
    if not saj:
        cl["in_cluster_U2"] = None; cl["out_cluster_U2"] = None; continue
    in_f = [saj[(s,v)]["fasila_2char"] for v in cluster_verses if (s,v) in saj]
    out_f = [saj[(s,v)]["fasila_2char"] for v in surah_info[s]["verses"]
             if v not in cluster_verses and (s,v) in saj]
    cl["in_cluster_U2"] = fasila_uniformity(in_f)
    cl["out_cluster_U2"] = fasila_uniformity(out_f)

# ---------- Output ----------
os.makedirs(os.path.join(OUT_DIR, "csv"), exist_ok=True)

with open(os.path.join(OUT_DIR, "csv", "oath-clusters.json"), "w") as f:
    json.dump(clusters, f, ensure_ascii=False, indent=2)

with open(os.path.join(OUT_DIR, "csv", "oath-clusters.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["surah","surah_name","type","start","end","length","is_opening",
                "first_oath_type","sworn_by_forms","sworn_by_roots","categories",
                "mixed","chiastic_cats","in_U2","out_U2","post_v","post_en"])
    for cl in clusters:
        w.writerow([cl["surah"], cl["surah_name"], cl["surah_type"],
                    cl["start_verse"], cl["end_verse"], cl["length"],
                    cl["is_opening"], cl["first_oath_type"],
                    " | ".join(it["form"] for it in cl["items"]),
                    " | ".join(it["root"] for it in cl["items"]),
                    " | ".join(it["category"] for it in cl["items"]),
                    cl["category_mixed"], cl["chiastic_categories"],
                    cl.get("in_cluster_U2",""), cl.get("out_cluster_U2",""),
                    cl["post_verses"][0] if cl["post_verses"] else "",
                    cl["sworn_about_en"][0] if cl["sworn_about_en"] else ""])

# ---------- Print summary ----------
print(f"Total oath clusters (any length, incl. singletons): {len(clusters)}")
print(f"Multi-verse clusters (length ≥ 2): {sum(1 for c in clusters if c['length']>=2)}")
print(f"  Length distribution (≥2): {sorted(len_dist_multi.items())}")
print(f"  Total length-1 (singleton oath verses): {len_dist[1]}")

mv = [c for c in clusters if c["length"]>=2]
print("\n== MULTI-VERSE CLUSTERS ==\n")
for cl in sorted(mv, key=lambda c:(c["surah"], c["start_verse"])):
    forms = " | ".join(it["form"] for it in cl["items"])
    cats = "/".join(it["category"] for it in cl["items"])
    flag = "★" if cl["is_opening"] else " "
    print(f" {flag} S{cl['surah']:>3}:{cl['start_verse']:>3}-{cl['end_verse']:<3} "
          f"len={cl['length']} type={cl['first_oath_type']:<3} "
          f"cats=[{cats}]")
    print(f"       sworn-by: {forms}")
    if cl["sworn_about_en"]:
        sa = cl["sworn_about_en"][0]
        if len(sa) > 110: sa = sa[:107]+"..."
        print(f"       sworn-about v{cl['post_verses'][0]}: {sa}")

print("\n== OPENINGS ONLY (classical famous oaths) ==")
for cl in sorted([c for c in clusters if c["is_opening"] and c["length"]>=1],
                 key=lambda c:c["surah"]):
    cats = "/".join(it["category"] for it in cl["items"])
    mark = "[CAND]" if cl["surah"] in CANDIDATES else "[-   ]"
    print(f"  {mark} S{cl['surah']:>3} v1-{cl['end_verse']} len={cl['length']} "
          f"type={cl['first_oath_type']:<3} cats=[{cats}]")

# Chiastic category detection
print("\n== CLUSTERS WITH CHIASTIC CATEGORY SEQUENCE ==")
for cl in clusters:
    if cl.get("chiastic_categories"):
        cats = "/".join(cl["category_sequence"])
        print(f"  S{cl['surah']}:{cl['start_verse']}-{cl['end_verse']} [{cats}]")

# Non-classical "discoveries"
print("\n== NON-CANDIDATE CLUSTERS (length ≥ 2) ==")
for cl in mv:
    if cl["surah"] not in CANDIDATES:
        print(f"  S{cl['surah']}:{cl['start_verse']}-{cl['end_verse']} len={cl['length']}"
              f"  translation: {(cl['sworn_about_en'][0] or '')[:80]}")

# Size-order check: decreasing cosmic → terrestrial → personal
SIZE_ORDER = {"celestial":1,"terrestrial":2,"temporal":1.5,"warrior":3,
              "wind":2,"angelic":0,"instrumental":3,"psychological":4,
              "abstract":0,"divine-lord":0,"numeric":0,"eschatological":0,
              "other":0}
print("\n== SIZE-ORDER CANDIDATES (cosmic→terrestrial→personal) ==")
for cl in mv:
    seq = [SIZE_ORDER.get(c,0) for c in cl["category_sequence"]]
    if len(set(seq)) > 1 and seq == sorted(seq):
        print(f"  S{cl['surah']}:{cl['start_verse']}-{cl['end_verse']} "
              f"cats={cl['category_sequence']}  sizes={seq}")

# Export stats
stats = {
    "n_clusters": len(clusters),
    "n_multiverse": sum(1 for c in clusters if c["length"]>=2),
    "length_distribution": {str(k):v for k,v in len_dist.items()},
    "n_opening_clusters": sum(1 for c in clusters if c["is_opening"]),
    "n_chiastic_category": sum(1 for c in clusters if c.get("chiastic_categories")),
    "n_outside_candidate_list": sum(1 for c in clusters
                                    if c["length"]>=2 and c["surah"] not in CANDIDATES),
}
with open(os.path.join(OUT_DIR, "csv", "oath-clusters-stats.json"), "w") as f:
    json.dump(stats, f, indent=2)
print("\nStats saved to", os.path.join(OUT_DIR, "csv", "oath-clusters-stats.json"))
