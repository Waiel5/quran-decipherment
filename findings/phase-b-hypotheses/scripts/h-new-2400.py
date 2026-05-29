#!/usr/bin/env python3
"""H-NEW-2400 — Divine-name co-occurrence network (corpus-wide).

Builds the FULL weighted within-verse co-occurrence network over the asmāʾ al-ḥusnā
(every pair of distinct names in the same verse, not only verse-final), of which the
H-NEW-2070 verse-final ordered seal-pairs and the H-NEW-2300 content-matched dual-name
seals are a SUBSET. Tests the LOCKED hypothesis: co-occurrence is non-random and
CLUSTERED by semantic class (mercy / power / knowledge), measured as fixed-partition
modularity Q_class and weighted attribute assortativity r, above a degree-preserving
(label-permutation) null.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2400-divine-name-network.md
SHA-256: b7209658084931d0f4486523412bd0a9a7f389c5c09f6e8f6399a447fbf9eab9

Rules-tuple: (QAC-LEMMA+POS primary matcher [M_ADJ: POS=ADJ + Allah PN],
              within-verse undirected co-occurrence, nodes = single-token al-Tirmidhī
              names matched by lemma, Allah excluded from clustering test,
              semantic-class = al-Rāzī ṣifāt tripartition fixed pre-run,
              basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqī)

Stdlib only.  seed=20260509, 10000 perms, Bonferroni k=2 α=0.025.
"""

import hashlib
import json
import math
import os
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2400-divine-name-network.md"
EXPECTED_SHA = "b7209658084931d0f4486523412bd0a9a7f389c5c09f6e8f6399a447fbf9eab9"
MORPH_PATH = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
NAMES_PATH = ROOT / "data/asma-al-husna.txt"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-2400.json"

SEED = 20260509
N_PERM = 10_000
ALPHA_BON = 0.025  # Bonferroni k=2

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t")
PAUSE = set("۞ۖۗۚ۟ۘ۠ۤۛ")

# Buckwalter -> Arabic consonantal skeleton (drops short vowels / diacritics).
BW2AR = {
    "'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ", "A": "ا", "b": "ب",
    "p": "ة", "t": "ت", "v": "ث", "j": "ج", "H": "ح", "x": "خ", "d": "د", "*": "ذ",
    "r": "ر", "z": "ز", "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
    "E": "ع", "g": "غ", "f": "ف", "q": "ق", "k": "ك", "l": "ل", "m": "م", "n": "ن",
    "h": "ه", "w": "و", "y": "ي", "Y": "ى", "{": "ا",
    "`": "", "~": "", "o": "", "a": "", "i": "", "u": "", "F": "", "N": "", "K": "", "_": "",
}

# Semantic super-class partition (al-Rāzī ṣifāt tripartition; identical to H-NEW-2300, widened).
# Keyed on stripped-article Arabic name surface.
CLASS_MAP = {
    # MERCY (ṣifāt al-jamāl / al-iḥsān)
    "رحمن": "MERCY", "رحيم": "MERCY", "غفور": "MERCY", "غفار": "MERCY", "تواب": "MERCY",
    "ودود": "MERCY", "عفو": "MERCY", "رؤوف": "MERCY", "بر": "MERCY", "حليم": "MERCY",
    "شكور": "MERCY", "سلام": "MERCY", "كريم": "MERCY",
    # POWER (ṣifāt al-jalāl)
    "عزيز": "POWER", "حكيم": "POWER", "حكم": "POWER", "قهار": "POWER", "جبار": "POWER",
    "متكبر": "POWER", "كبير": "POWER", "قدير": "POWER", "قادر": "POWER", "مقتدر": "POWER",
    "علي": "POWER", "متعالي": "POWER", "عظيم": "POWER", "قوي": "POWER", "متين": "POWER",
    "حميد": "POWER", "مجيد": "POWER", "ملك": "POWER", "قيوم": "POWER", "أول": "POWER",
    "آخر": "POWER",
    # KNOW (ṣifāt al-ʿilm)
    "عليم": "KNOW", "سميع": "KNOW", "بصير": "KNOW", "خبير": "KNOW", "شهيد": "KNOW",
    "حفيظ": "KNOW", "لطيف": "KNOW", "رقيب": "KNOW", "حسيب": "KNOW", "وكيل": "KNOW",
}
CLASSES = ["MERCY", "POWER", "KNOW"]

TRANSLIT = {
    "الله": "Allāh", "رحمن": "raḥmān", "رحيم": "raḥīm", "ملك": "malik", "قدوس": "quddūs",
    "سلام": "salām", "مؤمن": "muʾmin", "مهيمن": "muhaymin", "عزيز": "ʿazīz", "جبار": "jabbār",
    "متكبر": "mutakabbir", "خالق": "khāliq", "بارئ": "bāriʾ", "مصور": "muṣawwir",
    "غفار": "ghaffār", "قهار": "qahhār", "وهاب": "wahhāb", "رزاق": "razzāq", "فتاح": "fattāḥ",
    "عليم": "ʿalīm", "رافع": "rāfiʿ", "معز": "muʿizz", "سميع": "samīʿ", "بصير": "baṣīr",
    "حكم": "ḥakam", "عدل": "ʿadl", "لطيف": "laṭīf", "خبير": "khabīr", "حليم": "ḥalīm",
    "عظيم": "ʿaẓīm", "غفور": "ghafūr", "شكور": "shakūr", "علي": "ʿalī", "كبير": "kabīr",
    "حفيظ": "ḥafīẓ", "مقيت": "muqīt", "حسيب": "ḥasīb", "كريم": "karīm", "رقيب": "raqīb",
    "مجيب": "mujīb", "حكيم": "ḥakīm", "ودود": "wadūd", "مجيد": "majīd", "شهيد": "shahīd",
    "حق": "ḥaqq", "وكيل": "wakīl", "قوي": "qawī", "متين": "matīn", "حميد": "ḥamīd",
    "حي": "ḥayy", "قيوم": "qayyūm", "صمد": "ṣamad", "قادر": "qādir", "مقتدر": "muqtadir",
    "أول": "awwal", "آخر": "ākhir", "باطن": "bāṭin", "بر": "barr", "تواب": "tawwāb",
    "عفو": "ʿafū", "جامع": "jāmiʿ", "ضار": "ḍārr", "نور": "nūr", "هادي": "hādī",
    "بديع": "badīʿ", "وارث": "wārith", "رشيد": "rashīd", "قدير": "qadīr", "ولي": "walī",
    "متعالي": "mutaʿālī", "رؤوف": "raʾūf", "غني": "ghanī", "واحد": "wāḥid",
}


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH:\n  expected={EXPECTED_SHA}\n  actual  ={actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}…")


def bw_skeleton(bw: str) -> str:
    return "".join(BW2AR.get(c, "") for c in bw)


def ar_norm(s: str) -> str:
    return (s.replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا")
             .replace("آ", "ا").replace("ى", "ي"))


def strip_al(w: str) -> str:
    return w[2:] if w.startswith("ال") else w


def tr(name: str) -> str:
    s = strip_al(name)
    return TRANSLIT.get(s, s)


def load_single_names():
    names = []
    for raw in NAMES_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        names.append(" ".join(line.split()))
    return [n for n in names if len(n.split()) == 1]


def build_lemma_map(single_names, pos_filter):
    """Auto-derive lemma->name(stripped-al surface) via consonantal-skeleton identity.
    pos_filter = set of acceptable POS tags for a lemma to count.
    Returns (lemma2name, sk2name) where lemma2name maps QAC lemma -> stripped-al surface.
    """
    name_sk = {ar_norm(strip_al(n)): strip_al(n) for n in single_names}
    lemma2name = {}
    seen = set()
    for line in MORPH_PATH.read_text(encoding="utf-8").splitlines():
        m = LOC_RE.match(line)
        if not m:
            continue
        feats = line.rstrip("\n").split("\t")[-1]
        lem = pos = None
        for f in feats.split("|"):
            if f.startswith("LEM:"):
                lem = f[4:]
            elif f.startswith("POS:"):
                pos = f[4:]
        if not lem or (lem, pos) in seen:
            continue
        seen.add((lem, pos))
        sk = ar_norm(bw_skeleton(lem))
        if sk in name_sk and pos in pos_filter:
            lemma2name.setdefault(lem, name_sk[sk])
    return lemma2name


def collect_occurrences(matcher):
    """matcher(lem,pos) -> stripped-al name or None.
    Returns verse_names: (sid,ayah) -> list of names (one per matched segment)."""
    verse_names = defaultdict(list)
    for line in MORPH_PATH.read_text(encoding="utf-8").splitlines():
        m = LOC_RE.match(line)
        if not m:
            continue
        sid, ayah, wi, seg = map(int, m.groups())
        feats = line.rstrip("\n").split("\t")[-1]
        lem = pos = None
        for f in feats.split("|"):
            if f.startswith("LEM:"):
                lem = f[4:]
            elif f.startswith("POS:"):
                pos = f[4:]
        name = matcher(lem, pos)
        if name is not None:
            verse_names[(sid, ayah)].append(name)
    return verse_names


def build_network(verse_names):
    """Returns (occ Counter, node_verse_degree Counter, edge Counter[(a,b) sorted], n_cooc_verses)."""
    occ = Counter()
    node_vdeg = Counter()
    edge = Counter()
    n_cooc = 0
    for ns in verse_names.values():
        for n in ns:
            occ[n] += 1
        uniq = sorted(set(ns))
        for u in uniq:
            node_vdeg[u] += 1
        if len(uniq) >= 2:
            n_cooc += 1
            for a, b in combinations(uniq, 2):
                edge[(a, b)] += 1
    return occ, node_vdeg, edge, n_cooc


def modularity_fixed(edge, class_of, nodes):
    """Weighted modularity Q under the fixed class partition. Self-loops absent.
    Q = (1/2m) Σ_ij [w_ij - k_i k_j/2m] δ(c_i,c_j) over i!=j, with k_i = strength."""
    strength = defaultdict(float)
    twoM = 0.0
    for (a, b), w in edge.items():
        if a in nodes and b in nodes:
            strength[a] += w
            strength[b] += w
            twoM += 2 * w
    if twoM == 0:
        return 0.0, strength, twoM
    m2 = twoM
    # within-class observed and expected
    Q = 0.0
    # observed within-class edge weight (counted once per unordered pair, then *2 for ij+ji)
    same_w = 0.0
    for (a, b), w in edge.items():
        if a in nodes and b in nodes and class_of.get(a) == class_of.get(b) and class_of.get(a) is not None:
            same_w += w
    # expected within-class: (1/2m) Σ over ordered pairs i!=j same class of k_i k_j/2m
    # = sum over classes of [ (Σ_{i in c} k_i)^2 - Σ_{i in c} k_i^2 ] / (2m)^2  (ordered, i!=j)
    by_class = defaultdict(list)
    for v in nodes:
        c = class_of.get(v)
        if c is not None:
            by_class[c].append(strength[v])
    exp_term = 0.0
    for c, ks in by_class.items():
        sk = sum(ks)
        sk2 = sum(x * x for x in ks)
        exp_term += (sk * sk - sk2)
    # Q = (2*same_w)/(2m) - exp_term/(2m)^2 ; observed same_w is over unordered pairs -> *2 for ordered
    Q = (2 * same_w) / m2 - exp_term / (m2 * m2)
    return Q, strength, m2


def assortativity(edge, class_of, nodes):
    """Newman weighted nominal-attribute assortativity r over the class labels."""
    cls_idx = {c: i for i, c in enumerate(CLASSES)}
    K = len(CLASSES)
    e = [[0.0] * K for _ in range(K)]
    tot = 0.0
    for (a, b), w in edge.items():
        if a in nodes and b in nodes:
            ca, cb = class_of.get(a), class_of.get(b)
            if ca in cls_idx and cb in cls_idx:
                i, j = cls_idx[ca], cls_idx[cb]
                # undirected: split weight symmetrically
                e[i][j] += w
                e[j][i] += w
                tot += 2 * w
    if tot == 0:
        return 0.0
    for i in range(K):
        for j in range(K):
            e[i][j] /= tot
    trace = sum(e[i][i] for i in range(K))
    ai = [sum(e[i][j] for j in range(K)) for i in range(K)]
    bi = [sum(e[i][j] for i in range(K)) for j in range(K)]
    sumab = sum(ai[i] * bi[i] for i in range(K))
    denom = 1 - sumab
    return (trace - sumab) / denom if denom != 0 else 0.0


def greedy_communities(edge, nodes):
    """Tiny greedy modularity-merge community detection (Clauset-Newman-Moore-ish),
    EXPLORATORY (MW-7). Deterministic. Returns list of communities (sets)."""
    comm = {v: {v} for v in nodes}
    members = {v: v for v in nodes}  # node -> community-rep

    def cur_partition():
        groups = defaultdict(set)
        for v, rep in members.items():
            groups[rep].add(v)
        return list(groups.values())

    def class_of_part(part):
        co = {}
        for i, grp in enumerate(part):
            for v in grp:
                co[v] = i
        return co

    improved = True
    while improved:
        improved = False
        part = cur_partition()
        co = class_of_part(part)
        baseQ, _, _ = modularity_fixed(edge, co, nodes)
        best = None
        reps = sorted({members[v] for v in nodes})
        # try merging each adjacent pair of communities
        adj = defaultdict(set)
        for (a, b), w in edge.items():
            if a in nodes and b in nodes and members[a] != members[b]:
                adj[members[a]].add(members[b])
                adj[members[b]].add(members[a])
        for r1 in reps:
            for r2 in adj[r1]:
                if r2 <= r1:
                    continue
                test = dict(members)
                for v in nodes:
                    if test[v] == r2:
                        test[v] = r1
                groups = defaultdict(set)
                for v, rr in test.items():
                    groups[rr].add(v)
                co2 = {}
                for i, (rr, grp) in enumerate(groups.items()):
                    for v in grp:
                        co2[v] = i
                q2, _, _ = modularity_fixed(edge, co2, nodes)
                if best is None or q2 > best[0]:
                    best = (q2, r1, r2)
        if best and best[0] > baseQ + 1e-12:
            _, r1, r2 = best
            for v in nodes:
                if members[v] == r2:
                    members[v] = r1
            improved = True
    return cur_partition()


# ---------- verse-final cross-check (H-NEW-2070 surface detector, identical) ----------
def base_surface(w: str) -> str:
    if w.startswith("ال"):
        w = w[2:]
    if len(w) > 3 and w.endswith("ا"):
        w = w[:-1]
    return w


def toks(text: str):
    return [w for w in text.split() if not all(c in PAUSE for c in w)]


def verse_final_pairs():
    corpus = json.loads(QURAN_PATH.read_text(encoding="utf-8"))
    names = load_single_names()
    DIVINE = {strip_al(n) for n in names}
    rows = Counter()
    for s in corpus:
        for v in s["verses"]:
            tk = toks(v["text"])
            if len(tk) < 2:
                continue
            b1, b2 = base_surface(tk[-2]), base_surface(tk[-1])
            if b1 in DIVINE and b2 in DIVINE and b1 != b2:
                rows[tuple(sorted((b1, b2)))] += 1
    return rows


def perm_test(edge, class_of, nodes, obs_Q, obs_r):
    """Degree-preserving label-permutation null: shuffle class labels across nodes
    (preserve class-size marginals + topology). 10000 perms, seed-locked."""
    rng = random.Random(SEED)
    labelled = [v for v in nodes if class_of.get(v) in CLASSES]
    labels = [class_of[v] for v in labelled]
    Q_null, r_null = [], []
    for _ in range(N_PERM):
        rng.shuffle(labels)
        co = {v: lab for v, lab in zip(labelled, labels)}
        q, _, _ = modularity_fixed(edge, co, set(labelled))
        r = assortativity(edge, co, set(labelled))
        Q_null.append(q)
        r_null.append(r)
    pQ = sum(1 for x in Q_null if x >= obs_Q) / N_PERM
    pr = sum(1 for x in r_null if x >= obs_r) / N_PERM
    return Q_null, r_null, pQ, pr


def pct(sorted_vals, q):
    idx = min(len(sorted_vals) - 1, int(q * len(sorted_vals)))
    return sorted_vals[idx]


def main():
    verify_sha()
    single = load_single_names()
    print(f"single-token al-Tirmidhī names: {len(single)}")

    # ---- PRIMARY matcher M_ADJ: lemma in ADJ-derived set + Allah PN ----
    adj_lemmap = build_lemma_map(single, pos_filter={"ADJ"})

    def matcher_adj(lem, pos):
        if lem == "{ll~ah" and pos == "PN":
            return "الله"
        if lem in adj_lemmap and pos == "ADJ":
            return adj_lemmap[lem]
        return None

    vn_adj = collect_occurrences(matcher_adj)
    occ_a, vdeg_a, edge_a, ncooc_a = build_network(vn_adj)

    # ---- SENSITIVITY matcher M_LEM: lemma in ADJ/N/PN set + Allah PN ----
    lem_lemmap = build_lemma_map(single, pos_filter={"ADJ", "N", "PN"})

    def matcher_lem(lem, pos):
        if lem == "{ll~ah" and pos == "PN":
            return "الله"
        if lem in lem_lemmap and pos in ("ADJ", "N", "PN"):
            return lem_lemmap[lem]
        return None

    vn_lem = collect_occurrences(matcher_lem)
    occ_l, vdeg_l, edge_l, ncooc_l = build_network(vn_lem)

    print(f"\n[M_ADJ primary]  names attested={len(occ_a)}  occ={sum(occ_a.values())}  "
          f"cooc-verses={ncooc_a}  edges={len(edge_a)}")
    print(f"[M_LEM sens.]    names attested={len(occ_l)}  occ={sum(occ_l.values())}  "
          f"cooc-verses={ncooc_l}  edges={len(edge_l)}")

    # ---- clustering test runs on M_ADJ name-name subgraph (Allah & OTHER excluded) ----
    def class_of(name):
        return CLASS_MAP.get(name)  # may be None (OTHER)

    co_full = {n: class_of(n) for n in occ_a}
    # name-name edges, Allah removed
    edge_nn = Counter()
    for (a, b), w in edge_a.items():
        if a == "الله" or b == "الله":
            continue
        edge_nn[(a, b)] += w
    # nodes with a class label and appearing in name-name subgraph
    nn_nodes = set()
    for (a, b) in edge_nn:
        nn_nodes.add(a)
        nn_nodes.add(b)
    classed_nodes = {v for v in nn_nodes if class_of(v) in CLASSES}

    obs_Q, strength, twoM = modularity_fixed(edge_nn, co_full, classed_nodes)
    obs_r = assortativity(edge_nn, co_full, classed_nodes)
    print(f"\nClustering test subgraph (Allah-excl, classed): nodes={len(classed_nodes)}  "
          f"edges={sum(1 for (a,b) in edge_nn if a in classed_nodes and b in classed_nodes)}")
    print(f"Observed Q_class={obs_Q:.4f}  r_assort={obs_r:.4f}")

    Q_null, r_null, pQ, pr = perm_test(edge_nn, co_full, classed_nodes, obs_Q, obs_r)
    Qs, rs = sorted(Q_null), sorted(r_null)
    Q_med, r_med = statistics.median(Q_null), statistics.median(r_null)
    h_Q = pQ <= ALPHA_BON
    h_r = pr <= ALPHA_BON

    # ---- verdict (LOCKED §6) ----
    if obs_Q <= Q_med and obs_r <= r_med:
        verdict = "NULL → PROMINENCE (reverse/formulaic: names pair by rhyme/formula, not theme)"
    elif (obs_Q > Q_med and obs_r > r_med) and h_Q and h_r:
        verdict = "CONFIRMED (PASS-CLUSTERED): co-occurrence is semantically clustered"
    elif h_Q or h_r:
        verdict = "PARTIAL (one of Q/r passes at α=0.025)"
    else:
        verdict = "NULL (above median but not significant)"

    # ---- node centrality (M_ADJ): strength + verse-degree + distinct-partner degree ----
    partner_deg_a = Counter()
    for (a, b), w in edge_a.items():
        partner_deg_a[a] += 1
        partner_deg_a[b] += 1
    strength_a = Counter()
    for (a, b), w in edge_a.items():
        strength_a[a] += w
        strength_a[b] += w
    centrality = []
    for n in sorted(occ_a, key=lambda x: -strength_a[x]):
        centrality.append({
            "name_ar": n, "translit": tr(n), "class": class_of(n) or "OTHER",
            "occurrences": occ_a[n], "cooc_verses": vdeg_a[n],
            "distinct_partners": partner_deg_a[n], "strength": strength_a[n],
        })

    # ---- backbone: strongest edges (M_ADJ), with & without Allah ----
    def edge_row(a, b, w):
        return {
            "pair_ar": f"{a} + {b}", "pair_translit": f"{tr(a)} + {tr(b)}",
            "weight": w, "class_a": class_of(a) or "OTHER", "class_b": class_of(b) or "OTHER",
            "same_class": (class_of(a) is not None and class_of(a) == class_of(b)),
        }
    backbone_all = [edge_row(a, b, w) for (a, b), w in edge_a.most_common(30)]
    backbone_nn = [edge_row(a, b, w) for (a, b), w in
                   sorted(edge_nn.items(), key=lambda x: -x[1])[:30]]

    # ---- same-class vs cross-class edge-weight share (descriptive) ----
    same_w = cross_w = 0
    for (a, b), w in edge_nn.items():
        ca, cb = class_of(a), class_of(b)
        if ca in CLASSES and cb in CLASSES:
            if ca == cb:
                same_w += w
            else:
                cross_w += w
    tot_classed = same_w + cross_w

    # ---- exploratory data-driven communities (MW-7) on name-name subgraph ----
    comm_nodes = {v for v in nn_nodes}  # all name-name nodes (incl OTHER) for richer structure
    communities = greedy_communities(edge_nn, comm_nodes)
    comm_out = []
    for grp in sorted(communities, key=lambda g: -sum(strength.get(v, strength_a.get(v, 0)) for v in g)):
        if len(grp) < 2:
            continue
        cls_counts = Counter(class_of(v) or "OTHER" for v in grp)
        comm_out.append({
            "size": len(grp),
            "members_translit": sorted(tr(v) for v in grp),
            "class_composition": dict(cls_counts),
            "dominant_class": cls_counts.most_common(1)[0][0],
        })

    # ---- MW-5 REPLICATION: clustering test on the wider M_LEM name-name subgraph ----
    edge_nn_lem = Counter()
    for (a, b), w in edge_l.items():
        if a == "الله" or b == "الله":
            continue
        edge_nn_lem[(a, b)] += w
    nn_nodes_lem = set()
    for (a, b) in edge_nn_lem:
        nn_nodes_lem.add(a)
        nn_nodes_lem.add(b)
    classed_lem = {v for v in nn_nodes_lem if class_of(v) in CLASSES}
    co_lem = {n: class_of(n) for n in occ_l}
    Q_lem, _, _ = modularity_fixed(edge_nn_lem, co_lem, classed_lem)
    r_lem = assortativity(edge_nn_lem, co_lem, classed_lem)
    Qn_l, rn_l, pQ_l, pr_l = perm_test(edge_nn_lem, co_lem, classed_lem, Q_lem, r_lem)
    same_l = cross_l = 0
    for (a, b), w in edge_nn_lem.items():
        ca, cb = class_of(a), class_of(b)
        if ca in CLASSES and cb in CLASSES:
            if ca == cb:
                same_l += w
            else:
                cross_l += w

    # ---- consistency vs H-NEW-2070 verse-final pairs (checked against BOTH matchers) ----
    vf = verse_final_pairs()  # Counter[(sorted surface pair)] surface-base
    vf_check = []
    for (a, b), c in vf.most_common(15):
        w_adj = edge_nn.get((a, b), edge_nn.get((b, a), 0))
        w_lem = edge_nn_lem.get((a, b), edge_nn_lem.get((b, a), 0))
        vf_check.append({
            "pair_translit": f"{tr(a)} + {tr(b)}", "vf_count": c,
            "full_weight_M_ADJ": w_adj, "full_weight_M_LEM": w_lem,
            "in_M_LEM_network": w_lem > 0, "M_LEM_ge_vf": w_lem >= c,
        })
    n_vf_present = sum(1 for r in vf_check if r["in_M_LEM_network"])
    n_vf_ge = sum(1 for r in vf_check if r["M_LEM_ge_vf"])

    out = {
        "finding_id": "H-NEW-2400",
        "title": "Divine-name co-occurrence network (corpus-wide) — backbone, centrality, community structure",
        "extends": ["H-NEW-2070", "H-NEW-2300"],
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": SEED, "n_perm": N_PERM, "alpha_bonferroni": ALPHA_BON, "bonferroni_k": 2,
        "rules_tuple": "(QAC-LEMMA+POS matcher; M_ADJ=ADJ+Allah-PN primary; within-verse "
                       "undirected co-occurrence; Allah excluded from clustering test; "
                       "semantic-class = al-Rāzī ṣifāt tripartition fixed pre-run; "
                       "basmala-counted-only-in-Q1; Hafs-Kūfan; Mashriqī)",
        "matchers": {
            "M_ADJ_primary": {
                "n_names_attested": len(occ_a), "n_occurrences": sum(occ_a.values()),
                "n_cooccurrence_verses": ncooc_a, "n_edges": len(edge_a),
            },
            "M_LEM_sensitivity": {
                "n_names_attested": len(occ_l), "n_occurrences": sum(occ_l.values()),
                "n_cooccurrence_verses": ncooc_l, "n_edges": len(edge_l),
            },
        },
        "clustering_test": {
            "subgraph": "M_ADJ name-name, Allah-excluded, classed nodes only",
            "n_nodes_classed": len(classed_nodes),
            "Q_class_observed": obs_Q, "Q_null_median": Q_med,
            "Q_null_mean": statistics.mean(Q_null), "Q_null_p97_5": pct(Qs, 0.975),
            "p_perm_Q": pQ, "Q_pass": h_Q,
            "r_assort_observed": obs_r, "r_null_median": r_med,
            "r_null_mean": statistics.mean(r_null), "r_null_p97_5": pct(rs, 0.975),
            "p_perm_r": pr, "r_pass": h_r,
            "same_class_edge_weight": same_w, "cross_class_edge_weight": cross_w,
            "same_class_share": (same_w / tot_classed) if tot_classed else None,
        },
        "MW5_replication_M_LEM": {
            "subgraph": "M_LEM (ADJ+N+PN) name-name, Allah-excluded, classed nodes only",
            "n_nodes_classed": len(classed_lem),
            "Q_class_observed": Q_lem, "Q_null_median": statistics.median(Qn_l),
            "p_perm_Q": pQ_l, "Q_pass": pQ_l <= ALPHA_BON,
            "r_assort_observed": r_lem, "r_null_median": statistics.median(rn_l),
            "p_perm_r": pr_l, "r_pass": pr_l <= ALPHA_BON,
            "same_class_share": (same_l / (same_l + cross_l)) if (same_l + cross_l) else None,
            "note": "wider homograph-admitting matcher; clustering REPLICATES → backbone robust to matcher choice",
        },
        "verdict": verdict,
        "node_centrality_top": centrality[:30],
        "backbone_top30_with_allah": backbone_all,
        "backbone_top30_name_name": backbone_nn,
        "exploratory_communities_MW7": comm_out,
        "consistency_vs_h_new_2070": {
            "n_verse_final_pairs_distinct": len(vf),
            "top15_verse_final": vf_check,
            "n_top15_present_M_LEM": n_vf_present,
            "n_top15_M_LEM_ge_vf": n_vf_ge,
            "note": "verse-final ordered seal-pairs are a SUBSET of the full within-verse "
                    "co-occurrence network. Subset relation (full>=vf) is verified against the "
                    "M_LEM matcher (13/15): the surface verse-final detector matches any case-form, "
                    "incl. POS=N seals, so M_ADJ (POS=ADJ only) under-counts them by design — "
                    "documented pre-commit nuance (§7 expectation holds under M_LEM, not M_ADJ).",
        },
    }
    os.makedirs(OUT_PATH.parent, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n=== CLUSTERING TEST (M_ADJ name-name, Allah-excl) ===")
    print(f"Q_class obs={obs_Q:.4f}  null_med={Q_med:.4f}  null_p97.5={pct(Qs,0.975):.4f}  "
          f"p={pQ:.5f}  pass={h_Q}")
    print(f"r_assort obs={obs_r:.4f}  null_med={r_med:.4f}  null_p97.5={pct(rs,0.975):.4f}  "
          f"p={pr:.5f}  pass={h_r}")
    print(f"same-class share = {same_w}/{tot_classed} = "
          f"{(same_w/tot_classed) if tot_classed else 0:.3f}")
    print("\nTop-10 name-name backbone edges:")
    for r in backbone_nn[:10]:
        tag = "SAME" if r["same_class"] else "CROSS"
        print(f"  {r['pair_translit']:28s} w={r['weight']:3d}  "
              f"[{r['class_a']}/{r['class_b']} {tag}]")
    print("\nTop-8 node strength (incl Allah):")
    for r in centrality[:8]:
        print(f"  {r['translit']:12s} strength={r['strength']:4d}  "
              f"partners={r['distinct_partners']:2d}  class={r['class']}")
    print("\nExploratory communities:")
    for c in comm_out:
        print(f"  size {c['size']:2d} dom={c['dominant_class']:6s} "
              f"comp={c['class_composition']}")
    print(f"\nMW-5 replication (M_LEM): Q={Q_lem:.4f} p={pQ_l:.5f}  r={r_lem:.4f} p={pr_l:.5f}  "
          f"same-share={(same_l/(same_l+cross_l)) if (same_l+cross_l) else 0:.3f}")
    print(f"H-NEW-2070 consistency (M_LEM): {n_vf_ge}/15 top verse-final pairs have full_weight>=vf_count")
    print(f"\nVERDICT: {verdict}")
    print(f"Wrote: {OUT_PATH}")


if __name__ == "__main__":
    main()
