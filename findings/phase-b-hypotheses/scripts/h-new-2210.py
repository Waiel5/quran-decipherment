#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2210 — Qasam / jawāb al-qasam structural inventory + oath-density concentration test.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-2210-qasam-jawab-inventory.md
SHA-256 embedded below; verified at runtime.

Author: Waiel Al-Shujaa
Seed: 20260509  |  10000 permutations  |  Bonferroni k=2, alpha_bon=0.025

Method:
  * Oath-introducer = QAC POS-tagged `PREFIX|w:P+` (waaw al-qasam) OR `PREFIX|ta+` (ta-llahi)
    OR a (laa) uqsimu verb (LEM:>aqosamu form-IV imperfect 1S).
  * This morphological separation distinguishes the 28 oath-waaws from ~8500 conjunction-waaws.
  * Sworn-object = the genitive NP immediately governed by the oath particle.
  * Jawaab al-qasam = first canonical apodosis marker (inna/anna, la-EMPH, qad, in/maa, or bare)
    after the final sworn-object of a cluster.
  * Stacked-oath count = maximal run of consecutive oath-introducers sharing one jawaab.
  * Test: oath density per verse in short-mufassal (s>=78) > corpus mean (Cell A);
          Meccan > Medinan (Cell B). 10000-perm null shuffling surah->bin labels.

No external dependencies (stdlib only).
"""
import json, re, hashlib, random, sys, os

# ---------------------------------------------------------------------------
PREREG = "findings/phase-b-hypotheses/prereg-h-new-2210-qasam-jawab-inventory.md"
PREREG_SHA = "b47aaa5017e118b80b1b07b9a6c6da70eae3b89ba8cce79866cf0f18f281f75d"
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.025  # Bonferroni k=2

ROOT = "/Users/grey/Downloads/quran"
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
TEXT = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
VC = os.path.join(ROOT, "data/hafs-verse-counts.tsv")

def verify_sha():
    h = hashlib.sha256(open(os.path.join(ROOT, PREREG), "rb").read()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch\n  expected {PREREG_SHA}\n  got      {h}")
    print(f"[ok] pre-reg SHA verified: {h}")

# ---------------------------------------------------------------------------
# Parse QAC into ordered token list per (surah,verse,word,part)
TOKEN_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]+)\t([^\t]+)\t(.*)$")

def parse_qac():
    """Return list of token dicts in corpus order."""
    toks = []
    with open(QAC, encoding="utf-8") as f:
        for line in f:
            m = TOKEN_RE.match(line.rstrip("\n"))
            if not m:
                continue
            s, v, w, p = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
            form, pos, feat = m.group(5), m.group(6), m.group(7)
            toks.append(dict(s=s, v=v, w=w, p=p, form=form, pos=pos, feat=feat))
    return toks

# ---------------------------------------------------------------------------
# Sworn-object semantic-class mapping (locked in pre-reg), keyed by QAC ROOT.
SEM = {
    # cosmic / celestial
    "smw": "cosmic", "njm": "cosmic", "qmr": "cosmic", "$ms": "cosmic", "ArD": "cosmic",
    "Trq": "cosmic", "wqE": "cosmic",
    "$rq": "place/other", "grb": "place/other",
    # temporal
    "fjr": "temporal", "ESr": "temporal", "DHw": "temporal", "lyl": "temporal", "ywm": "temporal",
    "nhr": "temporal", "SbH": "temporal", "E$r": "temporal",
    # scriptural
    "qrA": "scriptural", "ktb": "scriptural", "qlm": "scriptural",
    # divine
    "Alh": "divine", "rbb": "divine",
    # agentive / eschatological-instrument (angels, winds, chargers, pluckers...)
    "Sff": "agentive", "rsl": "agentive", "nzG": "agentive", "nzE": "agentive",
    "Edw": "agentive", "*rw": "agentive", "*ry": "agentive", "xns": "agentive",
    "zjr": "agentive", "tlw": "agentive", "ESf": "agentive", "n$r": "agentive",
    "frq": "agentive", "lqy": "agentive", "n$T": "agentive", "sbH": "agentive",
    "sbq": "agentive", "dbr": "agentive", "wry": "agentive", "gyr": "agentive",
    # place / sacred-place / botanical
    "bld": "place/other", "tyn": "place/other", "zyt": "place/other", "Twr": "place/other",
    # human / soul / witness
    "nfs": "human/soul", "lwm": "human/soul", "wld": "human/soul", "$hd": "human/soul",
    # eschatological-temporal markers
    "$fE": "eschatological", "wtr": "eschatological", "$fq": "eschatological", "Hjr": "eschatological",
}

def classify(root, lemma, pos_feat=""):
    if root in SEM:
        return SEM[root]
    # fall-back: feminine/plural ACT participle governed by oath = agentive class
    if "ACT|PCPL" in pos_feat and ("FP|" in pos_feat or "MP|" in pos_feat):
        return "agentive"
    return "other"

def get_root(tok):
    m = re.search(r"ROOT:([^|]+)", tok["feat"])
    return m.group(1) if m else None

def get_lemma(tok):
    m = re.search(r"LEM:([^|]+)", tok["feat"])
    return m.group(1) if m else None

# ---------------------------------------------------------------------------
def is_oath_waaw(t):
    return t["pos"] == "P" and "PREFIX|w:P+" in t["feat"]

def is_ta_oath(t):
    return t["pos"] == "P" and "PREFIX|ta+" in t["feat"]

def is_uqsimu(t):
    return (t["pos"] == "V" and "LEM:>aqosamu" in t["feat"]
            and "IMPF" in t["feat"] and "1S" in t["feat"])

def _lem(f):
    m = re.search(r"LEM:([^|]+)", f)
    return m.group(1) if m else None

def is_jawab_marker(t):
    """Canonical apodosis markers (POS-anchored; lemmas matched exactly, not as substrings)."""
    f = t["feat"]; pos = t["pos"]; lem = _lem(f)
    # inna / anna (ACC particle <in~ / >an~)
    if pos == "ACC" and lem in ("<in~", ">an~"):
        return "inna/anna"
    # laam al-tawkiid (EMPH prefix) — only as a true prefix particle
    if "PREFIX|l:EMPH+" in f:
        return "la-(tawkid)"
    # qad — only the CERT particle
    if pos == "CERT" and lem == "qad":
        return "qad"
    # negative-oath jawaab: maa (NEG) / in (COND)
    if pos == "NEG" and lem == "maA":
        return "maa(neg-jawab)"
    if pos == "COND" and lem == "<in":
        return "in(neg-jawab)"
    return None

# ---------------------------------------------------------------------------
def build_inventory(toks):
    """
    Walk corpus; whenever an oath-introducer begins a new word, start a cluster.

    GARDEN-OF-FORKING-PATHS NOTE (logged 2026-05-29, BEFORE re-run, specialist judgment):
    The QAC tags ONLY the first oath of a stack as `w:P+` (waaw al-qasam); the subsequent
    coordinated sworn-objects are tagged `w:CONJ`/`f:CONJ` + GEN noun (the maʿṭūf / coordinated
    object series under one oath). Verified directly on Q 91 al-Shams (7 objects: shams DHw qmr
    nahaar layl samaaʾ arD nafs — only 91:1:1 is w:P+, the rest w:CONJ) and Q 79 al-Naziʿaat
    (5 objects: naaziʿaat naashiTaat saabiHaat saabiqaat mudabbiraat — fa/wa CONJ). Therefore the
    classical "stacked oath" (taʿaddud al-muqsam bihi) is realised as one oath-waaw + a coordinated
    GEN-object chain. The stacked-oath COUNT extends the cluster through that coordinated chain:
    a following word headed by w:CONJ / f:CONJ whose head noun is GENITIVE (matching the oath's
    GEN object) is counted as an additional sworn-object, until a jawaab marker / non-GEN-coordination
    appears. This affects only the DESCRIPTIVE stack-count (MW-7 capped); the verdict-bearing
    concentration test counts oath OPENINGS per surah and is unchanged.

    A cluster = an oath-opening (waaw/ta/uqsimu) + its coordinated GEN sworn-object chain, sharing
    one jawaab. We then scan forward for the first jawaab marker.

    Further during-run refinements (all logged BEFORE verdict acceptance; none touch the locked
    direction or null model — they only make the morphological inventory exhaustive):
      (R1) Predication-boundary stop: the coordinated-object chain closes at a verse-initial
           interrogative (INTG hal/a-) / finite-verb / relative predication that is NOT an
           idhā-temporal modifier. This prevents over-running into the post-oath narrative
           (e.g. Q 89 al-Fajr stops at 5 sworn objects and does NOT sweep in thamūd/firʿawn at 89:9-10).
      (R2) Oath-particle detected in ANY part of the word, not only tk[0]: captures the
           fa-wa-rabbika resumption form (fa REM + w:P+, Q 15:92 / 19:68 / 51:23) and the
           wa-ta-llaahi conjunction+oath form (Q 21:57).
      (R3) (wa/fa-)laa uqsimu continuation inside one series captured (Q 75:1 + 75:2).
      (R4) jawaab markers POS-anchored + lemma matched exactly (fixes a substring false-positive
           where the noun qadoH 'sparks' matched 'qad', Q 100:2).
    Net captured oath-openings: 28 oath-waaw + 9 ta-oath + 8 uqsimu = 45, matching the raw
    QAC morphological counts exactly. 44 clusters (Q 75 carries two stacked uqsimu).
    """
    # index tokens by word position for forward scanning, in corpus order.
    n = len(toks)
    # Map: identify the FIRST token (p==1) headers that are oath-introducers.
    # Build per-word grouping in order.
    words = []  # list of (s,v,w, [tokens])
    cur = None
    for t in toks:
        key = (t["s"], t["v"], t["w"])
        if cur is None or cur[0] != key:
            cur = (key, [t])
            words.append(cur)
        else:
            cur[1].append(t)
    word_list = [(k[0], k[1], k[2], tk) for (k, tk) in words]

    def word_is_oath_head(tk):
        # an oath-waaw (w:P+) OR a ta-oath particle (ta+) appearing in ANY part of the word.
        # This covers bare wa-l-X / ta-llaahi, the fa-wa-rabbika resumption form (fa REM + w:P+,
        # e.g. Q 15:92, 19:68, 51:23), and the wa-ta-llaahi conjunction+oath form (Q 21:57).
        if not tk:
            return False
        if any(is_oath_waaw(x) or is_ta_oath(x) for x in tk):
            return True
        return False

    def word_kind(tk):
        if any(is_ta_oath(x) for x in tk):
            return "ta"
        return "waaw"

    def word_has_uqsimu(tk):
        return any(is_uqsimu(x) for x in tk)

    def sworn_object(tk):
        """Return (text, root, lemma, sem-class) of the governed NP in this word (after prefix+det)."""
        for x in tk:
            if x["pos"] in ("N", "PN", "ADJ"):
                r = get_root(x); l = get_lemma(x)
                return (x["form"], r, l, classify(r, l, x["feat"]))
        return (None, None, None, "other")

    def head_noun_is_genitive(tk):
        """A coordinated sworn-object: w/f-CONJ-led word whose head noun is GEN."""
        if not tk:
            return False
        if tk[0]["pos"] != "CONJ":
            return False
        if not ("PREFIX|w:CONJ+" in tk[0]["feat"] or "PREFIX|f:CONJ+" in tk[0]["feat"]):
            return False
        for x in tk[1:]:
            if x["pos"] in ("N", "PN", "ADJ"):
                return "|GEN" in x["feat"]
            # skip a leading DET
            if x["pos"] == "DET":
                continue
            # any other head (REL maa, verb, etc.) -> not a coordinated GEN object
            return False
        return False

    clusters = []
    i = 0
    L = len(word_list)
    while i < L:
        s, v, w, tk = word_list[i]
        start_oath = word_is_oath_head(tk) or word_has_uqsimu(tk)
        if not start_oath:
            i += 1
            continue
        # begin a cluster.
        members = []
        kind_set = set()
        n_openings = 0  # explicit oath particles (w:P+ / ta / uqsimu)
        first_v = v
        # 1) the opening word + its directly governed sworn-object
        if word_has_uqsimu(tk):
            obj = (None, None, None, "other")
            if i + 1 < L:
                _, _, _, tknext = word_list[i + 1]
                obj = sworn_object(tknext)  # bi- governed object
            members.append(dict(s=s, v=v, w=w, kind="uqsimu", obj=obj, opening=True))
            kind_set.add("uqsimu"); n_openings += 1
            j = i + 2  # skip the bi-object word
        else:
            kind = word_kind(tk)
            members.append(dict(s=s, v=v, w=w, kind=kind, obj=sworn_object(tk), opening=True))
            kind_set.add(kind); n_openings += 1
            j = i + 1
        # 2) forward-scan: simultaneously locate the jawaab marker AND collect the coordinated
        #    GEN sworn-object chain (taʿaddud al-muqsam bihi) + any further explicit oath particles.
        #    Intervening idhā / mā / verb modifier clauses are skipped; coordinated GEN objects resume.
        jawab = None
        chain_open = True   # coordinated-object chain stays open until a predication boundary
        scan = j
        while scan < L:
            s3, v3, w3, tk3 = word_list[scan]
            if s3 != s:               # crossed surah boundary
                break
            if v3 - first_v > 12:     # forward-scan cap
                break
            # jawaab marker check first (terminates the oath cluster)
            mk = None
            for x in tk3:
                mk = is_jawab_marker(x)
                if mk:
                    break
            if mk:
                jawab = dict(s=s3, v=v3, w=w3, marker=mk)
                break
            # another explicit oath particle (always reopens / continues the oath series)
            if word_is_oath_head(tk3):
                kind = word_kind(tk3)
                members.append(dict(s=s3, v=v3, w=w3, kind=kind, obj=sworn_object(tk3), opening=True))
                kind_set.add(kind); n_openings += 1
                chain_open = True
                scan += 1
                continue
            # a further (wa-/fa-)laa uqsimu in the same oath series (e.g. Q 75:1 + 75:2)
            if word_has_uqsimu(tk3):
                obju = (None, None, None, "other")
                if scan + 1 < L:
                    _, _, _, tku = word_list[scan + 1]
                    obju = sworn_object(tku)
                members.append(dict(s=s3, v=v3, w=w3, kind="uqsimu", obj=obju, opening=True))
                kind_set.add("uqsimu"); n_openings += 1
                chain_open = True
                scan += 2  # skip the bi-object word
                continue
            # coordinated GEN sworn object (maʿTuf ʿalā al-muqsam bihi) — only while chain is open
            if chain_open and head_noun_is_genitive(tk3):
                members.append(dict(s=s3, v=v3, w=w3, kind="coord", obj=sworn_object(tk3), opening=False))
                scan += 1
                continue
            # predication-boundary detector: a verse-initial interrogative / NEG+verb / finite-verb
            # clause that is NOT part of an idhā-temporal modifier closes the coordinated chain.
            head = tk3[0]
            is_idha_modifier = (head["pos"] == "T" and "LEM:<i*aA" in head["feat"])
            is_verse_initial = (w3 == 1)
            if not is_idha_modifier:
                # an interrogative, a hal/a- question, or a finite-verb / particle predication
                # at a verse head signals the oath-series is closed.
                if is_verse_initial and head["pos"] in ("INTG", "V", "REL", "SUB", "INL"):
                    chain_open = False
                if head["pos"] == "INTG":
                    chain_open = False
            scan += 1
        # bare-jawaab fallback: first non-oath, non-coordinated word after the opening run
        if jawab is None:
            k = j
            while k < L:
                s4, v4, w4, tk4 = word_list[k]
                if s4 != s:
                    break
                if word_is_oath_head(tk4) or head_noun_is_genitive(tk4):
                    k += 1
                    continue
                jawab = dict(s=s4, v=v4, w=w4, marker="bare")
                break
        j = scan  # advance main pointer past the cluster
        dist = (jawab["v"] - first_v) if jawab else None
        clusters.append(dict(
            surah=s, first_verse=first_v,
            n_stacked=len(members),       # total sworn objects (openings + coordinated)
            n_openings=n_openings,         # explicit oath particles (w:P+ / ta / uqsimu)
            kinds=sorted(kind_set),
            members=members,
            jawab=jawab,
            qasam_to_jawab_verse_distance=dist,
            sem_classes=[m["obj"][3] for m in members],
        ))
        i = j  # continue after this cluster
    return clusters

# ---------------------------------------------------------------------------
def load_meta():
    data = json.load(open(TEXT, encoding="utf-8"))
    types = {s["id"]: s["type"] for s in data}
    verses = {s["id"]: s["total_verses"] for s in data}
    return types, verses

# ---------------------------------------------------------------------------
def run_test(clusters, types, verses):
    """
    Oath-introducer counts per surah = number of oath WORDS (members), not clusters,
    so stacked oaths each count. Density = oaths / verses.
    """
    # Verdict-bearing density uses oath OPENINGS (explicit oath particles), not coordinated objects.
    per_surah_oaths = {s: 0 for s in range(1, 115)}
    for c in clusters:
        per_surah_oaths[c["surah"]] += c["n_openings"]

    total_oaths = sum(per_surah_oaths.values())
    total_verses = sum(verses.values())
    corpus_density = total_oaths / total_verses

    surahs = list(range(1, 115))

    # --- Cell A: short-mufassal s>=78 enrichment ratio ---
    def cellA_stat(bin_set):
        o = sum(per_surah_oaths[s] for s in bin_set)
        v = sum(verses[s] for s in bin_set)
        dens = o / v if v else 0.0
        return dens / corpus_density if corpus_density else 0.0
    binA = set(s for s in surahs if s >= 78)
    obsA = cellA_stat(binA)
    nA = len(binA)

    # --- Cell B: Meccan vs Medinan density ratio ---
    mecc = set(s for s in surahs if types[s] == "meccan")
    medi = set(s for s in surahs if types[s] == "medinan")
    def density(bin_set):
        o = sum(per_surah_oaths[s] for s in bin_set)
        v = sum(verses[s] for s in bin_set)
        return o / v if v else 0.0
    dens_mecc = density(mecc)
    dens_medi = density(medi)
    obsB = (dens_mecc / dens_medi) if dens_medi > 0 else float("inf")

    # --- Permutation null (shuffle surah->bin labels) ---
    rng = random.Random(SEED)
    # Cell A: shuffle which surahs are in the "size-nA" bin
    geA = 0
    for _ in range(N_PERM):
        permset = set(rng.sample(surahs, nA))
        if cellA_stat(permset) >= obsA:
            geA += 1
    pA = geA / N_PERM

    # Cell B: shuffle Meccan/Medinan labels (hold counts) -> reassign types randomly
    n_mecc = len(mecc)
    geB = 0
    for _ in range(N_PERM):
        perm_mecc = set(rng.sample(surahs, n_mecc))
        perm_medi = set(surahs) - perm_mecc
        dm = density(perm_mecc); dn = density(perm_medi)
        ratio = (dm / dn) if dn > 0 else float("inf")
        if ratio >= obsB:
            geB += 1
    pB = geB / N_PERM

    # --- MW-5 replication: s>=93 cut ---
    bin93 = set(s for s in surahs if s >= 93)
    obsA93 = cellA_stat(bin93)
    n93 = len(bin93)
    rng2 = random.Random(SEED + 1)
    ge93 = 0
    for _ in range(N_PERM):
        permset = set(rng2.sample(surahs, n93))
        if cellA_stat(permset) >= obsA93:
            ge93 += 1
    pA93 = ge93 / N_PERM

    return dict(
        per_surah_oaths={k: v for k, v in per_surah_oaths.items() if v > 0},
        total_oaths=total_oaths, total_verses=total_verses,
        corpus_density=corpus_density,
        cellA=dict(bin="s>=78 short-mufassal", n_surahs=nA,
                   oaths=sum(per_surah_oaths[s] for s in binA),
                   verses=sum(verses[s] for s in binA),
                   density=density(binA), enrichment_ratio=obsA,
                   p_perm_one_sided=pA, locked_direction="short-mufassal > corpus mean",
                   direction_observed="short-mufassal > corpus mean" if obsA > 1 else "REVERSED (<= corpus mean)"),
        cellB=dict(comparison="Meccan vs Medinan", dens_meccan=dens_mecc, dens_medinan=dens_medi,
                   ratio=obsB, p_perm_one_sided=pB, locked_direction="Meccan > Medinan",
                   direction_observed="Meccan > Medinan" if obsB > 1 else "REVERSED (Medinan >= Meccan)"),
        mw5_replication=dict(bin="s>=93", n_surahs=n93, enrichment_ratio=obsA93,
                             p_perm_one_sided=pA93),
        bonferroni=dict(k=2, alpha_bon=ALPHA_BON,
                        cellA_pass=(pA < ALPHA_BON and obsA > 1),
                        cellB_pass=(pB < ALPHA_BON and obsB > 1)),
    )

# ---------------------------------------------------------------------------
def main():
    verify_sha()
    toks = parse_qac()
    print(f"[ok] parsed {len(toks)} QAC tokens")
    # raw counts of oath introducers
    n_waaw = sum(1 for t in toks if is_oath_waaw(t))
    n_ta = sum(1 for t in toks if is_ta_oath(t))
    n_uqsimu = sum(1 for t in toks if is_uqsimu(t))
    print(f"[ok] oath-waaw (w:P+)={n_waaw}, ta-oath={n_ta}, uqsimu(1S)={n_uqsimu}")

    clusters = build_inventory(toks)
    print(f"[ok] {len(clusters)} oath clusters")

    types, verses = load_meta()
    test = run_test(clusters, types, verses)

    # semantic-class tally across all oath members
    sem_tally = {}
    for c in clusters:
        for sc in c["sem_classes"]:
            sem_tally[sc] = sem_tally.get(sc, 0) + 1

    # sworn-object-count distribution (taʿaddud al-muqsam bihi): how many objects per oath-cluster
    stack_dist = {}
    for c in clusters:
        stack_dist[c["n_stacked"]] = stack_dist.get(c["n_stacked"], 0) + 1
    # max-stack clusters (the famous multi-oath openings)
    max_stack = max(c["n_stacked"] for c in clusters)
    biggest = sorted([(c["surah"], c["first_verse"], c["n_stacked"],
                       [m["obj"][0] for m in c["members"]]) for c in clusters],
                     key=lambda x: -x[2])[:8]

    # distance distribution
    dist_dist = {}
    for c in clusters:
        d = c["qasam_to_jawab_verse_distance"]
        dist_dist[str(d)] = dist_dist.get(str(d), 0) + 1

    # ta-oath control: which surahs
    ta_surahs = sorted(set(c["surah"] for c in clusters if "ta" in c["kinds"]))

    out = dict(
        meta=dict(id="H-NEW-2210", seed=SEED, n_perm=N_PERM, prereg_sha=PREREG_SHA,
                  rules_tuple="(no-tashkeel, QAC-morphology-POS, Hafs-Kufan, Mashriqi)"),
        counts=dict(oath_waaw=n_waaw, ta_oath=n_ta, uqsimu_1S=n_uqsimu, clusters=len(clusters)),
        clusters=clusters,
        semantic_class_tally=sem_tally,
        sworn_object_count_distribution=stack_dist,
        max_stacked_objects=max_stack,
        biggest_stacks=biggest,
        qasam_to_jawab_distance_distribution=dist_dist,
        ta_oath_control_surahs=ta_surahs,
        concentration_test=test,
    )
    os.makedirs(os.path.join(ROOT, "findings/phase-b-hypotheses/csv"), exist_ok=True)
    with open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2210.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # console summary
    print("\n===== H-NEW-2210 SUMMARY =====")
    print(f"clusters: {len(clusters)} | oath-waaw={n_waaw} ta={n_ta} uqsimu={n_uqsimu}")
    print(f"semantic-class tally: {sem_tally}")
    print(f"sworn-object-count dist: {stack_dist}  (max stack={max_stack})")
    print(f"biggest stacks: {[(b[0],b[1],b[2]) for b in biggest]}")
    ca = test["cellA"]; cb = test["cellB"]
    print(f"\nCell A (s>=78): enrich={ca['enrichment_ratio']:.3f} p={ca['p_perm_one_sided']:.4f} -> {ca['direction_observed']}")
    print(f"Cell B (Mecc/Med): ratio={cb['ratio']:.3f} p={cb['p_perm_one_sided']:.4f} -> {cb['direction_observed']}")
    print(f"MW-5 (s>=93): enrich={test['mw5_replication']['enrichment_ratio']:.3f} p={test['mw5_replication']['p_perm_one_sided']:.4f}")
    print(f"Bonferroni: cellA_pass={test['bonferroni']['cellA_pass']} cellB_pass={test['bonferroni']['cellB_pass']}")
    print(f"ta-oath control surahs: {ta_surahs}")

if __name__ == "__main__":
    main()
