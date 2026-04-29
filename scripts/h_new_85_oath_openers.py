"""
H-NEW-85 — Comprehensive analysis of oath-opening surahs.
Locked spec: findings/phase-b-hypotheses/h-new-85-oath-openers-prereg.md

Inputs:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - findings/phase-b-hypotheses/csv/h-new-61.json (for the 21-list)

Output:
  - findings/phase-b-hypotheses/csv/h-new-85.json
  - findings/phase-b-hypotheses/csv/h-new-85-oath-items.csv
"""
from __future__ import annotations
import json, os, re, math, csv, statistics, random
from collections import defaultdict, Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN = ROOT / "quran-text" / "quran-no-tashkeel.json"
QAC = ROOT / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
H61 = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-61.json"
OUT_DIR = ROOT / "findings" / "phase-b-hypotheses" / "csv"
SEED = 20260416

# --- 1. Load H-NEW-61 OATH list (LOCK) ---
h61 = json.load(open(H61))
OATH_SURAHS = sorted([int(k) for k, v in h61["opening_data"].items()
                      if v["class"] == "OATH_PARTICLE"])
assert len(OATH_SURAHS) == 21, f"Expected 21 oath surahs from H-NEW-61, got {len(OATH_SURAHS)}"

# --- 2. Load QAC morphology rows ---
def load_qac():
    """Yield rows (surah, ayah, word, seg, form, tag, features) from QAC."""
    qac = defaultdict(list)  # (s,a) -> list of segments in word-segment order
    rgx = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t(\S+)\t(\S+)\t(.*)$")
    with open(QAC, "r", encoding="utf-8") as f:
        for line in f:
            m = rgx.match(line.rstrip("\n"))
            if not m:
                continue
            s, a, w, seg = (int(x) for x in m.group(1, 2, 3, 4))
            form, tag, feat = m.group(5), m.group(6), m.group(7)
            qac[(s, a)].append({
                "word": w, "seg": seg,
                "form": form, "tag": tag, "feat": feat,
            })
    return qac

QAC_ROWS = load_qac()

# --- 3. Group QAC into "head-NPs" inside an oath cluster ---
# A head-NP starts at a token whose PREFIX has w:P+ (oath waw),
# w:CONJ+ (continuation waw), f:CONJ+ (fa-continuation), or no prefix
# but the segment is a STEM N/PN/ADJ with case GEN.
# A head-NP CONTINUES through DET prefix and ends BEFORE the next w:CONJ+ /
# f:CONJ+ / new-word boundary that starts a fresh head, OR at the verse
# boundary.

MUQATTAAT_TAGS = {"INL"}  # POS:INL == initial letters

def is_gen_noun(seg):
    """Segment is a STEM noun-like with case GEN."""
    if seg["tag"] not in {"N", "PN", "ADJ"}:
        return False
    feat = seg["feat"]
    return "STEM|" in feat and "|GEN" in feat


def get_root(seg):
    feat = seg["feat"]
    m = re.search(r"\|ROOT:([^|]+)", feat)
    return m.group(1) if m else None


def get_lem(seg):
    feat = seg["feat"]
    m = re.search(r"\|LEM:([^|]+)", feat)
    return m.group(1) if m else None


def get_prefix_kind(seg):
    """Return 'wP', 'wCONJ', 'fCONJ', 'Al', 'lP', 'lEMPH', or None."""
    feat = seg["feat"]
    if not feat.startswith("PREFIX"):
        return None
    if "w:P+" in feat:
        return "wP"
    if "w:CONJ+" in feat:
        return "wCONJ"
    if "f:CONJ+" in feat:
        return "fCONJ"
    if "Al+" in feat:
        return "Al"
    if "l:P+" in feat:
        return "lP"
    if "l:EMPH+" in feat:
        return "lEMPH"
    if "f:REM+" in feat or "f:RSLT+" in feat:
        return "fREM"
    if "b:P+" in feat:
        return "bP"
    return None


def parse_word_segments(segs):
    """Given segments of one word, separate (prefix_kinds list, stem_seg or None,
    suffix_segs list)."""
    prefixes = []
    stem = None
    suffixes = []
    for s in segs:
        if s["feat"].startswith("PREFIX"):
            prefixes.append(get_prefix_kind(s))
        elif s["feat"].startswith("SUFFIX"):
            suffixes.append(s)
        elif s["feat"].startswith("STEM"):
            stem = s
    return prefixes, stem, suffixes


# Group segments by (surah, ayah, word)
def get_words(s, a):
    rows = QAC_ROWS.get((s, a), [])
    by_w = defaultdict(list)
    for r in rows:
        by_w[r["word"]].append(r)
    out = []
    for w in sorted(by_w):
        segs = sorted(by_w[w], key=lambda x: x["seg"])
        prefixes, stem, suffixes = parse_word_segments(segs)
        out.append({"w": w, "prefixes": prefixes, "stem": stem,
                    "suffixes": suffixes, "raw_segs": segs})
    return out


def n_verses_in_surah(s):
    a = 1
    while (s, a) in QAC_ROWS:
        a += 1
    return a - 1


# --- 4. Walk a surah to identify oath-cluster ---
# Starting position: the first word AFTER any leading muqaṭṭaʿāt (POS:INL),
# AFTER any basmala (only Q1 has the basmala counted as v1; for the 21 oath
# surahs, basmala is not counted as v1, so we start at v1).
# In the QAC, the basmala of Q1 is at (1,1,*); for surahs 2-114, the basmala
# is NOT in the QAC (only Tanzil-text-based; QAC excludes it).

def find_first_real_word(s):
    """Return (a, w_idx) of the first non-muqaṭṭaʿāt word in surah s,
    skipping basmala-as-v1 (Q1 only)."""
    a = 1
    if s == 1:
        # skip al-Fātiḥa basmala = v1
        a = 2
    while True:
        words = get_words(s, a)
        # skip leading muqaṭṭaʿāt-words at this verse
        first_real = None
        for w in words:
            if w["stem"] is not None and w["stem"]["tag"] in MUQATTAAT_TAGS:
                continue
            first_real = w["w"]
            break
        if first_real is not None:
            return a, first_real
        a += 1
        if a > 300:
            raise RuntimeError(f"surah {s}: no real word found")


def is_oath_head(word, allow_first=False, next_word=None):
    """Decide if this word starts a new sworn-by head-NP.
    Returns ('wP' | 'wCONJ' | 'fCONJ' | 'bare') or None.

    The 'allow_first' flag permits a bare GEN-noun start ONLY at the very
    first word of an oath cluster.

    If the word is `wa-hādhā` (wCONJ + DEM) and next_word is a GEN-noun, this
    counts as a wCONJ head-NP (per locked extractor: "optionally with
    intervening DET (Al+) or DEM").
    """
    if word["stem"] is None:
        return None
    pref = word["prefixes"]
    sig = [p for p in pref if p not in {"Al", None}]
    is_dem = word["stem"]["tag"] == "DEM"
    # Case A: this word IS a GEN-noun
    if is_gen_noun(word["stem"]):
        if not sig:
            return "bare" if allow_first else None
        if sig[0] == "wP":
            return "wP"
        if sig[0] == "wCONJ":
            return "wCONJ"
        if sig[0] == "fCONJ":
            return "fCONJ"
        return None
    # Case B: this word is a DEM with wCONJ/wP/fCONJ prefix and next word is
    # a GEN-noun (e.g., "wa-hādhā l-balad").
    if is_dem and sig:
        if sig[0] in ("wP", "wCONJ", "fCONJ"):
            if next_word is not None and next_word["stem"] is not None \
                    and is_gen_noun(next_word["stem"]):
                return sig[0] + "+DEM"
    return None


def parse_oath_cluster(s):
    """Walk surah s from its first real word and collect consecutive oath
    head-NPs, staying within a contiguous run of oath-bearing verses.
    Returns dict with n_verses_in_cluster, n_head_NPs, head_list."""
    a_start, w_start = find_first_real_word(s)
    head_list = []
    last_oath_verse = None
    a = a_start
    cluster_active = True
    while cluster_active:
        words = get_words(s, a)
        if not words:
            break
        # filter out muqaṭṭaʿāt only at the surah-start verse
        idx0 = 0
        if a == a_start:
            for i, w in enumerate(words):
                if w["w"] >= w_start:
                    idx0 = i
                    break
        # scan
        verse_heads_count = 0
        first_word_of_verse = words[idx0] if idx0 < len(words) else None
        if first_word_of_verse is None:
            break
        # Determine if this verse begins with an oath construction.
        # For continuation verses (not the surah-start verse), the FIRST word
        # MUST be a wCONJ/fCONJ/wP+GEN-noun head; otherwise the cluster has ended.
        next_w = words[idx0 + 1] if idx0 + 1 < len(words) else None
        if a == a_start:
            kind0 = is_oath_head(first_word_of_verse, allow_first=True, next_word=next_w)
        else:
            kind0 = is_oath_head(first_word_of_verse, allow_first=False, next_word=next_w)
            if kind0 is None:
                # cluster has ended
                break
        if kind0 is None:
            break
        # Record heads in this verse
        for i in range(idx0, len(words)):
            w = words[i]
            allow_first_inside = (i == idx0 and a == a_start)
            nw = words[i + 1] if i + 1 < len(words) else None
            kind = is_oath_head(w, allow_first=allow_first_inside, next_word=nw)
            if kind is None:
                continue
            # If kind is "+DEM" we extract the FOLLOWING noun's root/lem
            if kind.endswith("+DEM"):
                stem = nw["stem"] if nw and nw["stem"] else w["stem"]
            else:
                stem = w["stem"]
            head_list.append({
                "surah": s,
                "ayah": a,
                "word": w["w"],
                "kind": kind,
                "form_buck": stem["form"],
                "lem": get_lem(stem),
                "root": get_root(stem),
            })
            verse_heads_count += 1
        last_oath_verse = a
        a += 1
        # safety
        if a - a_start > 30:
            break
    return {
        "surah": s,
        "a_start": a_start,
        "a_last_oath_verse": last_oath_verse,
        "n_verses_in_cluster": (last_oath_verse - a_start + 1) if last_oath_verse else 0,
        "n_head_NPs": len(head_list),
        "head_list": head_list,
        "first_post_oath_verse": (last_oath_verse + 1) if last_oath_verse else a_start,
    }


# --- 5. Sworn-by category map (LOCKED) ---
ROOT_CAT = {
    # CELESTIAL
    "$ms": "CELESTIAL", "qmr": "CELESTIAL", "njm": "CELESTIAL",
    "smw": "CELESTIAL", "brj": "CELESTIAL", "Trq": "CELESTIAL",
    # TEMPORAL
    "lyl": "TEMPORAL", "nhr": "TEMPORAL", "fjr": "TEMPORAL",
    "DHw": "TEMPORAL", "E$r": "TEMPORAL", "ywm": "TEMPORAL",
    "sjw": "TEMPORAL",
    # TERRESTRIAL
    "Twr": "TERRESTRIAL", "ArD": "TERRESTRIAL", "bld": "TERRESTRIAL",
    "byt": "TERRESTRIAL", "sqf": "TERRESTRIAL", "sjr": "TERRESTRIAL",
    "tyn": "TERRESTRIAL", "zyt": "TERRESTRIAL",
    "bHr": "TERRESTRIAL",  # sea (Q 52:6)
    "rqq": "INSTRUMENTAL_SCRIPTURAL",
    # KINETIC_NATURAL
    "*rw": "KINETIC_NATURAL", "ESf": "KINETIC_NATURAL",
    "n$r": "KINETIC_NATURAL", "jry": "KINETIC_NATURAL",
    "frq": "KINETIC_NATURAL", "Hml": "KINETIC_NATURAL",
    # KINETIC_AGENTIVE
    "Sff": "KINETIC_AGENTIVE", "zjr": "KINETIC_AGENTIVE",
    "tlw": "KINETIC_AGENTIVE", "nzE": "KINETIC_AGENTIVE",
    "n$T": "KINETIC_AGENTIVE", "sbH": "KINETIC_AGENTIVE",
    "sbq": "KINETIC_AGENTIVE", "dbr": "KINETIC_AGENTIVE",
    "Edw": "KINETIC_AGENTIVE", "qdH": "KINETIC_AGENTIVE",
    "gyr": "KINETIC_AGENTIVE", "vwr": "KINETIC_AGENTIVE",
    "rsl": "KINETIC_AGENTIVE",
    "qsm": "KINETIC_AGENTIVE",  # muqassimāt = those who apportion (Q 51:4)
    "lqy": "KINETIC_AGENTIVE",  # mulqiyāt = those who deliver (Q 77:5)
    "wry": "KINETIC_AGENTIVE",  # mūriyāt = strikers of fire (Q 100:2)
    "ESr": "TEMPORAL",          # al-ʿaṣr = late afternoon (Q 103:1)
    # INSTRUMENTAL_SCRIPTURAL
    "qlm": "INSTRUMENTAL_SCRIPTURAL", "ktb": "INSTRUMENTAL_SCRIPTURAL",
    "sTr": "INSTRUMENTAL_SCRIPTURAL", "qrA": "INSTRUMENTAL_SCRIPTURAL",
    "*kr": "INSTRUMENTAL_SCRIPTURAL",  # dhikr
    "Hkm": "INSTRUMENTAL_SCRIPTURAL",  # the Wise (modifier of qrA)
    "byn": "INSTRUMENTAL_SCRIPTURAL",  # the Clarifying (modifier of ktb)
    "mjd": "INSTRUMENTAL_SCRIPTURAL",  # the Glorious (modifier of qrA)
    "noun": "INSTRUMENTAL_SCRIPTURAL",
    # DIVINE_NAME
    "rbb": "DIVINE_NAME",
    # PSYCHOLOGICAL
    "nfs": "PSYCHOLOGICAL", "Sdr": "PSYCHOLOGICAL",
    "qlb": "PSYCHOLOGICAL", "lwm": "PSYCHOLOGICAL",
    # NUMERIC_PAIR
    "$fE": "NUMERIC_PAIR", "wtr": "NUMERIC_PAIR",
    # ABSTRACT
    "$hd": "ABSTRACT", "wEd": "ABSTRACT",
    # OTHER (residual; intentionally empty, captured by fallback)
}

PRIORITY = ["TEMPORAL", "KINETIC_AGENTIVE", "KINETIC_NATURAL", "CELESTIAL",
            "TERRESTRIAL", "INSTRUMENTAL_SCRIPTURAL", "DIVINE_NAME",
            "PSYCHOLOGICAL", "NUMERIC_PAIR", "ABSTRACT", "OTHER"]


def categorize(root):
    if root is None:
        return "OTHER"
    return ROOT_CAT.get(root, "OTHER")


# --- 6. Run extraction over the 21 oath surahs ---
results = {}
for s in OATH_SURAHS:
    r = parse_oath_cluster(s)
    # categorize each head
    for h in r["head_list"]:
        h["cat"] = categorize(h["root"])
    r["cat_seq"] = [h["cat"] for h in r["head_list"]]
    r["cat_count"] = dict(Counter(r["cat_seq"]))
    r["n_distinct_cats"] = len(r["cat_count"])
    results[s] = r

# --- 7. Cell 1: verify 21/21 with ≥1 head ---
cell1_pass = all(results[s]["n_head_NPs"] >= 1 for s in OATH_SURAHS)
cell1_details = [(s, results[s]["n_head_NPs"], results[s]["n_verses_in_cluster"])
                 for s in OATH_SURAHS]

# Meccan check: load period from h-new-61
periods = {int(k): v["period"] for k, v in h61["opening_data"].items()}
cell1_meccan = all(periods[s] == "Meccan" for s in OATH_SURAHS)
cell1_meccan_count = sum(1 for s in OATH_SURAHS if periods[s] == "Meccan")

# --- 8. Cell 2: Q 91 max verses ---
verse_counts = {s: results[s]["n_verses_in_cluster"] for s in OATH_SURAHS}
max_v = max(verse_counts.values())
q91_v = verse_counts[91]
cell2_q91_unique = (q91_v == max_v) and (sum(1 for v in verse_counts.values() if v == max_v) == 1)
cell2_runners_up = sorted(verse_counts.items(), key=lambda x: -x[1])[:5]

# --- 9. Cell 2b: Q 91 max head-NPs ---
item_counts = {s: results[s]["n_head_NPs"] for s in OATH_SURAHS}
max_i = max(item_counts.values())
q91_i = item_counts[91]
cell2b_q91_unique = (q91_i == max_i) and (sum(1 for v in item_counts.values() if v == max_i) == 1)
cell2b_runners_up = sorted(item_counts.items(), key=lambda x: -x[1])[:5]

# --- 10. Cell 3: category χ² ---
all_heads = [h for s in OATH_SURAHS for h in results[s]["head_list"]]
total_cats = Counter(h["cat"] for h in all_heads)
N = sum(total_cats.values())
present_cats = list(total_cats.keys())
expected = N / len(present_cats)
chi2 = sum((total_cats[c] - expected) ** 2 / expected for c in present_cats)
df = len(present_cats) - 1


def chi2_p(x, df):
    """Survival function for chi^2 (regularized upper-incomplete gamma).
    Pure-Python; sufficient for our k <= 11."""
    # Use series for regularized lower P, then 1-P.
    # For df>=2 even, p = exp(-x/2) * sum_{k=0..df/2-1} (x/2)^k / k!
    # For df odd, use erfc-based; here df is small and we approximate via
    # Wilson-Hilferty as fallback, then refine via series for our case.
    if df <= 0:
        return 1.0
    if df % 2 == 0:
        m = df // 2
        s = 0.0
        term = 1.0
        for k in range(m):
            if k > 0:
                term *= (x / 2.0) / k
            s += term
        return math.exp(-x / 2.0) * s
    # Wilson-Hilferty: chi2 ~ df*(1 - 2/(9 df) + Z*sqrt(2/(9 df)))^3
    # Z = ((chi2/df)^(1/3) - (1 - 2/(9 df))) / sqrt(2/(9 df))
    a = 2.0 / (9.0 * df)
    z = ((x / df) ** (1.0 / 3.0) - (1.0 - a)) / math.sqrt(a)
    return 0.5 * math.erfc(z / math.sqrt(2.0))


cell3_p = chi2_p(chi2, df)
cell3_pass = cell3_p < 0.010

# --- 11. Cell 4: surah-length test ---
quran = json.load(open(QURAN))
# index by id
surah_verses = {}
for s in quran:
    sid = int(s["id"])
    surah_verses[sid] = int(s.get("total_verses", len(s.get("verses", []))))
assert surah_verses[91] == 15, f"Q91 has {surah_verses[91]}, expected 15"
assert surah_verses[103] == 3, f"Q103 has {surah_verses[103]}, expected 3"

oath_lens = [surah_verses[s] for s in OATH_SURAHS]
non_oath_meccan = [s for s in range(1, 115)
                    if s in periods and periods[s] == "Meccan"
                    and s not in OATH_SURAHS]
no_meccan_lens = [surah_verses[s] for s in non_oath_meccan]

# Mann-Whitney U two-sided
def mannwhitney_u(a, b):
    """Return (U_a, p_two_sided) using normal approximation with tie correction."""
    combined = sorted((v, 0) for v in a) + sorted((v, 1) for v in b)
    combined.sort(key=lambda x: x[0])
    # rank with tie averaging
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg_rank = (i + 1 + j + 1) / 2.0
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    R_a = sum(r for r, (v, g) in zip(ranks, combined) if g == 0)
    n_a = len(a)
    n_b = len(b)
    U_a = R_a - n_a * (n_a + 1) / 2.0
    U_b = n_a * n_b - U_a
    mu = n_a * n_b / 2.0
    # tie correction
    tie_groups = []
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        if j > i:
            tie_groups.append(j - i + 1)
        i = j + 1
    n = n_a + n_b
    tie_term = sum(t ** 3 - t for t in tie_groups)
    sigma = math.sqrt((n_a * n_b / 12.0) * ((n + 1) - tie_term / (n * (n - 1))))
    if sigma == 0:
        return U_a, 1.0
    z = (U_a - mu) / sigma
    # two-sided
    p = math.erfc(abs(z) / math.sqrt(2.0))
    return U_a, p, z


U_oath, p_mw, z_mw = mannwhitney_u(oath_lens, no_meccan_lens)
cell4_pass = p_mw < 0.010
cell4_dir = "SHORTER" if statistics.median(oath_lens) < statistics.median(no_meccan_lens) else "LONGER"

# --- 12. Cell 5: jawāb-theme classification (LOCKED hand-classification per
# pre-reg, taken from oath-clusters.md §4 and re-checked against jawāb verse) ---
# Each surah gets ONE primary jawāb theme.
JAWAB = {
    36:  "PROPHETHOOD",   # Q36:3 "innaka la-mina l-mursalīn"
    37:  "PROPHETHOOD",   # Q37:4 "inna ilāhakum la-wāḥid" — actually monotheism
    38:  "QURAN_STATUS",  # Q38:1 "wa-l-qurʾāni dhī l-dhikr" → Q38:2 "bal alladhīna kafarū" (rebuke); but the dhi-l-dhikr is itself a Qur'an-status frame
    43:  "QURAN_STATUS",  # Q43:3 "innā jaʿalnāhu qurʾānan ʿarabīyan"
    44:  "QURAN_STATUS",  # Q44:3 "innā anzalnāhu fī laylatin mubārakatin"
    50:  "PROPHETHOOD",   # Q50:2 "bal ʿajibū an jāʾahum mundhirun minhum" (rejection of warner)
    51:  "ESCHATOLOGY",   # Q51:5 "innamā tūʿadūna la-ṣādiq"
    52:  "ESCHATOLOGY",   # Q52:7 "inna ʿadhāba rabbika la-wāqiʿ"
    53:  "PROPHETHOOD",   # Q53:2 "mā ḍalla ṣāḥibukum"
    68:  "PROPHETHOOD",   # Q68:2 "mā anta bi-niʿmati rabbika bi-majnūn"
    77:  "ESCHATOLOGY",   # Q77:7 "innamā tūʿadūna la-wāqiʿ"
    79:  "ESCHATOLOGY",   # Q79:6 "yawma tarjufu l-rājifa"
    85:  "ESCHATOLOGY",   # Q85:4-7 "qutila aṣḥābu l-ukhdūd" → punishment narrative
    86:  "PROPHETHOOD",   # Q86:13 "innahu la-qawlun faṣl" (the Word/Qur'an)  -- alt: QURAN_STATUS
    89:  "ESCHATOLOGY",   # Q89:5 "hal fī dhālika qasamun li-dhī ḥijr" → punishments of past nations
    91:  "HUMAN_NATURE",  # Q91:7-10 nafs / fa-alhamahā fujūrahā wa-taqwāhā
    92:  "HUMAN_NATURE",  # Q92:4 "inna saʿyakum la-shattā"
    93:  "PROPHETHOOD",   # Q93:3 "mā waddaʿaka rabbuka wa-mā qalā"
    95:  "HUMAN_NATURE",  # Q95:4 "khalaqnā l-insāna fī aḥsani taqwīm"
    100: "HUMAN_NATURE",  # Q100:6 "inna l-insāna li-rabbihi la-kanūd"
    103: "HUMAN_NATURE",  # Q103:2 "inna l-insāna la-fī khusr"
}
assert all(s in JAWAB for s in OATH_SURAHS), "JAWAB missing a surah"
theme_counts = Counter(JAWAB[s] for s in OATH_SURAHS)
themes = sorted(theme_counts.keys())
n_themes = len(themes)
expected_t = len(OATH_SURAHS) / n_themes
chi2_t = sum((theme_counts[t] - expected_t) ** 2 / expected_t for t in themes)
df_t = n_themes - 1
cell5_p = chi2_p(chi2_t, df_t)
cell5_pass = cell5_p < 0.010

# --- 13. Bonus: get Arabic name + period from h-new-61 ---
metadata = {int(k): v for k, v in h61["opening_data"].items()}

# --- 14. Per-surah summary table ---
table = []
for s in OATH_SURAHS:
    r = results[s]
    md = metadata[s]
    table.append({
        "surah": s,
        "name_ar": md["name_ar"],
        "name_tl": md["name_tl"],
        "period": md["period"],
        "phase": md["phase"],
        "n_verses_total": surah_verses[s],
        "n_verses_in_cluster": r["n_verses_in_cluster"],
        "n_head_NPs": r["n_head_NPs"],
        "n_distinct_cats": r["n_distinct_cats"],
        "cat_seq": r["cat_seq"],
        "cat_count": r["cat_count"],
        "jawab_theme": JAWAB[s],
        "head_roots": [h["root"] for h in r["head_list"]],
        "head_lems": [h["lem"] for h in r["head_list"]],
    })

# --- 15. Write JSON + CSV outputs ---
OUT_DIR.mkdir(exist_ok=True, parents=True)
out = {
    "seed": SEED,
    "hypothesis_id": "H-NEW-85",
    "rules_tuple": "(no-tashkeel, hafs-kufan, canonical-114, oath-set=H-NEW-61 OATH_PARTICLE)",
    "n_oath_surahs": len(OATH_SURAHS),
    "oath_surahs": OATH_SURAHS,
    "bonferroni_k": 5,
    "alpha_bon": 0.010,
    "cell1": {
        "all_have_head": cell1_pass,
        "all_meccan": cell1_meccan,
        "n_meccan": cell1_meccan_count,
        "details": cell1_details,
    },
    "cell2_max_verses": {
        "verse_counts": verse_counts,
        "max": max_v,
        "q91": q91_v,
        "q91_unique_max": cell2_q91_unique,
        "top5": cell2_runners_up,
    },
    "cell2b_max_items": {
        "item_counts": item_counts,
        "max": max_i,
        "q91": q91_i,
        "q91_unique_max": cell2b_q91_unique,
        "top5": cell2b_runners_up,
    },
    "cell3_categories": {
        "totals": dict(total_cats),
        "n_present_cats": len(present_cats),
        "chi2": chi2,
        "df": df,
        "p": cell3_p,
        "pass": cell3_pass,
    },
    "cell4_length": {
        "n_oath": len(oath_lens),
        "n_other_meccan": len(no_meccan_lens),
        "median_oath": statistics.median(oath_lens),
        "median_other_meccan": statistics.median(no_meccan_lens),
        "mean_oath": statistics.mean(oath_lens),
        "mean_other_meccan": statistics.mean(no_meccan_lens),
        "U": U_oath,
        "z": z_mw,
        "p": p_mw,
        "direction": cell4_dir,
        "pass": cell4_pass,
    },
    "cell5_themes": {
        "theme_counts": dict(theme_counts),
        "n_themes": n_themes,
        "chi2": chi2_t,
        "df": df_t,
        "p": cell5_p,
        "pass": cell5_pass,
    },
    "table": table,
}

with open(OUT_DIR / "h-new-85.json", "w", encoding="utf-8") as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

# Per-head-NP CSV
with open(OUT_DIR / "h-new-85-oath-items.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["surah", "ayah", "word", "kind", "form_buck", "lem", "root", "cat"])
    for s in OATH_SURAHS:
        for h in results[s]["head_list"]:
            w.writerow([h["surah"], h["ayah"], h["word"], h["kind"],
                        h["form_buck"], h["lem"] or "", h["root"] or "", h["cat"]])

# Per-surah CSV
with open(OUT_DIR / "h-new-85-per-surah.csv", "w", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["surah", "name_tl", "n_verses_total", "n_verses_in_cluster",
                "n_head_NPs", "n_distinct_cats", "cat_seq",
                "jawab_theme", "head_lems"])
    for r in table:
        w.writerow([r["surah"], r["name_tl"], r["n_verses_total"],
                    r["n_verses_in_cluster"], r["n_head_NPs"],
                    r["n_distinct_cats"], "|".join(r["cat_seq"]),
                    r["jawab_theme"], "|".join(str(x) for x in r["head_lems"])])

print("Done.")
print(f"  Cell 1 (21/21 with head, all Meccan): pass={cell1_pass and cell1_meccan} "
      f"({cell1_meccan_count}/21 Meccan)")
print(f"  Cell 2 (Q 91 max verses): {q91_v}; max={max_v}; unique={cell2_q91_unique}")
print(f"    top5: {cell2_runners_up}")
print(f"  Cell 2b (Q 91 max items): {q91_i}; max={max_i}; unique={cell2b_q91_unique}")
print(f"    top5: {cell2b_runners_up}")
print(f"  Cell 3 (cat χ²): chi2={chi2:.2f}, df={df}, p={cell3_p:.4g}, pass={cell3_pass}")
print(f"    totals: {dict(total_cats)}")
print(f"  Cell 4 (length MW): median oath={statistics.median(oath_lens)}, "
      f"median other-Meccan={statistics.median(no_meccan_lens)}, "
      f"z={z_mw:.3f}, p={p_mw:.4g}, dir={cell4_dir}, pass={cell4_pass}")
print(f"  Cell 5 (theme χ²): {dict(theme_counts)} chi2={chi2_t:.2f}, df={df_t}, "
      f"p={cell5_p:.4g}, pass={cell5_pass}")
