#!/usr/bin/env python3
"""
Q005 al-Māʾida deep-dive — all 5 pre-registered tests (Q005-F-01..F-05)
========================================================================

Pre-reg files (with locked SHA256 verified at runtime):
  Q005-F-01-potb-density-prereg.md            → sha 1edccc500ffad015aebe957e112d3826355f451c66aa37463bf2d56ceb05c165
  Q005-F-02-maida-episode-isolation-prereg.md → sha e8b0885729bb87d77565c57e1c59414bea682c5cefd32f4dcca02d04f6ea9e9d
  Q005-F-03-akmaltu-cluster-prereg.md         → sha c91092c51bc85bd8dab7ebaf8f5a965b0ff432e2af2a7c501b40cc033286a179
  Q005-F-04-covenants-density-prereg.md       → sha 2a1d8cdd705b842926527112671d1871f1f2a96a155c32222c199c9b6e68946d
  Q005-F-05-late-medinan-signature-prereg.md  → sha 74117716db9861e84ad2dc3e4f51c8324b1115dde2ae4786f75fb4afd36c84a4

Seed: 20260507. n_perm: 10000. Bonferroni-k: 5; α_bon = 0.01.
Rules-tuple: (no-tashkeel, QAC v0.4 LEMMA + ROOT, basmala-counted-only-in-surah-1, Hafs-Kufan, Mashriqi).

Outputs:
  surahs/Q005-al-maida/csv/Q005-F-01.json
  surahs/Q005-al-maida/csv/Q005-F-02.json
  surahs/Q005-al-maida/csv/Q005-F-03.json
  surahs/Q005-al-maida/csv/Q005-F-04.json
  surahs/Q005-al-maida/csv/Q005-F-05.json
"""

from __future__ import annotations
import hashlib, json, math, os, random, re, sys
from collections import defaultdict, Counter

# ---------- paths ----------
BASE = "/Users/grey/Downloads/quran"
SURAH_DIR = f"{BASE}/surahs/Q005-al-maida"
CSV_DIR = f"{SURAH_DIR}/csv"
QAC = f"{BASE}/data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN_NT = f"{BASE}/quran-text/quran-no-tashkeel.json"
HNEW111 = f"{BASE}/findings/phase-b-hypotheses/csv/h-new-111.json"
HNEW750 = f"{BASE}/findings/phase-b-hypotheses/csv/h-new-750.json"

EXPECTED_SHA = {
    "Q005-F-01-potb-density-prereg.md":            "1edccc500ffad015aebe957e112d3826355f451c66aa37463bf2d56ceb05c165",
    "Q005-F-02-maida-episode-isolation-prereg.md": "e8b0885729bb87d77565c57e1c59414bea682c5cefd32f4dcca02d04f6ea9e9d",
    "Q005-F-03-akmaltu-cluster-prereg.md":         "c91092c51bc85bd8dab7ebaf8f5a965b0ff432e2af2a7c501b40cc033286a179",
    "Q005-F-04-covenants-density-prereg.md":       "2a1d8cdd705b842926527112671d1871f1f2a96a155c32222c199c9b6e68946d",
    "Q005-F-05-late-medinan-signature-prereg.md":  "74117716db9861e84ad2dc3e4f51c8324b1115dde2ae4786f75fb4afd36c84a4",
}
SEED = 20260507
N_PERM = 10000
BONF_K = 5
ALPHA_BON = 0.01

# ---------- pre-reg SHA verification ----------
def verify_prereg_shas():
    print("[verify] checking pre-reg SHAs...")
    for fn, expected in EXPECTED_SHA.items():
        p = f"{SURAH_DIR}/{fn}"
        with open(p, "rb") as f:
            got = hashlib.sha256(f.read()).hexdigest()
        status = "OK" if got == expected else "MISMATCH"
        print(f"  {fn}: {status}")
        if got != expected:
            print(f"    expected {expected}\n    got     {got}")
            sys.exit(2)
    print("[verify] all SHAs match. Proceeding.\n")


# ---------- QAC parser ----------
QAC_LINE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t(\S+)\t(\S+)\t(.+)$")
ROOT_RE = re.compile(r"\|ROOT:([^\s\|]+)")
LEM_RE = re.compile(r"\|LEM:([^\s\|]+)")

def load_qac():
    """Return:
      tokens_per_verse: dict[(s,v)] -> list of (surface, lemma, root)
      lemma_per_surah: dict[s] -> dict[lemma] -> count
      root_per_surah: dict[s] -> dict[root] -> count
      lemma_attest_surahs: dict[lemma] -> set of surahs
      root_attest_surahs: dict[root] -> set of surahs
      lemma_per_verse: dict[(s,v)] -> Counter[lemma]
      root_per_verse: dict[(s,v)] -> Counter[root]
    """
    tokens_per_verse = defaultdict(list)
    lemma_per_surah = defaultdict(lambda: Counter())
    root_per_surah = defaultdict(lambda: Counter())
    lemma_attest_surahs = defaultdict(set)
    root_attest_surahs = defaultdict(set)
    lemma_per_verse = defaultdict(Counter)
    root_per_verse = defaultdict(Counter)
    with open(QAC) as f:
        for ln in f:
            if not ln.startswith("("):
                continue
            m = QAC_LINE.match(ln)
            if not m:
                continue
            s, v, w, p = (int(x) for x in m.groups()[:4])
            feats = m.group(7)
            rm = ROOT_RE.search(feats)
            lm = LEM_RE.search(feats)
            root = rm.group(1) if rm else None
            lemma = lm.group(1) if lm else None
            tokens_per_verse[(s, v)].append((m.group(5), lemma, root))
            if root:
                root_per_surah[s][root] += 1
                root_attest_surahs[root].add(s)
                root_per_verse[(s, v)][root] += 1
            if lemma:
                lemma_per_surah[s][lemma] += 1
                lemma_attest_surahs[lemma].add(s)
                lemma_per_verse[(s, v)][lemma] += 1
    return (
        tokens_per_verse,
        lemma_per_surah,
        root_per_surah,
        lemma_attest_surahs,
        root_attest_surahs,
        lemma_per_verse,
        root_per_verse,
    )


def load_word_counts():
    """words per surah and per verse using whitespace split on no-tashkeel."""
    with open(QURAN_NT) as f:
        q = json.load(f)
    wc_surah = {}
    wc_verse = {}
    for s in q:
        sid = s["id"]
        total = 0
        for v in s["verses"]:
            words = v["text"].split()
            wc_verse[(sid, v["id"])] = len(words)
            total += len(words)
        wc_surah[sid] = total
    return wc_surah, wc_verse


# ---------- Q005-F-01: PoTB-density ----------
POTB_LEMMAS = [
    "yahuwdiy~",       # al-yahūd
    "naSoraAniy~",     # al-naṣārā
    "t~aworaY`p",      # al-tawrāh
    "<injiyl",         # al-injīl
    "<isoraA}iyl",     # Banī Isrāʾīl
    "EiysaY",          # ʿĪsā
    "muwsaY`",         # Mūsā
    "HawaAriy~uwn",    # al-ḥawāriyyūn
    "{lomasiyH",       # al-masīḥ — to lookup; alternative form may be "masiyH"
]


def run_F01(lemma_per_surah, wc_surah, rng):
    # find all attested PoTB lemma forms
    # First, identify the masīḥ lemma form
    masih_candidates = [l for l in lemma_per_surah[5] if "masiyH" in l]
    family = list(POTB_LEMMAS)
    # remove {lomasiyH if not present, add real form
    family = [l for l in family if l != "{lomasiyH"]
    family.extend(masih_candidates)

    per_surah_count = {}
    per_surah_density = {}
    for s in range(1, 115):
        n = sum(lemma_per_surah[s].get(l, 0) for l in family)
        per_surah_count[s] = n
        per_surah_density[s] = 100.0 * n / wc_surah[s]

    # Ranking
    order = sorted(per_surah_density.items(), key=lambda x: -x[1])
    rank = {sid: i + 1 for i, (sid, _) in enumerate(order)}

    medinan5 = [2, 3, 4, 5, 9]
    med5_order = sorted(medinan5, key=lambda s: -per_surah_density[s])
    med5_rank = {s: i + 1 for i, s in enumerate(med5_order)}

    # Permutation null: shuffle counts across surah-positions, recompute Q5's corpus rank
    counts = [per_surah_count[s] for s in range(1, 115)]
    words = [wc_surah[s] for s in range(1, 115)]
    q5_idx = 4  # 0-based for surah 5
    n_top2_med5 = 0
    n_top5_corpus = 0
    for _ in range(N_PERM):
        perm = counts[:]
        rng.shuffle(perm)
        densities = [100.0 * perm[i] / words[i] for i in range(114)]
        # rank Q5
        sorted_idx = sorted(range(114), key=lambda i: -densities[i])
        ridx = sorted_idx.index(q5_idx) + 1
        if ridx <= 5:
            n_top5_corpus += 1
        # med5 rank
        med_idx = [s - 1 for s in medinan5]
        med_dens = [(s, densities[s - 1]) for s in medinan5]
        med_sorted = sorted(med_dens, key=lambda x: -x[1])
        ridx_med = next(i for i, (s, _) in enumerate(med_sorted, 1) if s == 5)
        if ridx_med <= 2:
            n_top2_med5 += 1
    p_top2_med5 = n_top2_med5 / N_PERM
    p_top5_corpus = n_top5_corpus / N_PERM

    primary_rank = med5_rank[5]
    primary_pass = primary_rank <= 2
    p_primary = p_top2_med5
    if primary_pass and p_primary < ALPHA_BON:
        verdict = "VINDICATED al-Rāzī PoTB-density (rank-{} of 5; corpus-rank {}; p_perm={:.4f} < α_bon={})".format(
            primary_rank, rank[5], p_primary, ALPHA_BON
        )
    elif primary_pass:
        verdict = "DIRECTIONAL — rank passes but p_perm ≥ α_bon"
    else:
        verdict = "NULL — Q 5 PoTB-density ranks {} of 5 in Medinan cluster".format(primary_rank)

    return {
        "id": "Q005-F-01",
        "title": "People-of-the-Book vocabulary density",
        "prereg_sha_expected": EXPECTED_SHA["Q005-F-01-potb-density-prereg.md"],
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel, QAC-LEMMA, QAC v0.4)",
        "lemma_family": family,
        "per_surah_count": per_surah_count,
        "per_surah_density": per_surah_density,
        "Q5_density": per_surah_density[5],
        "Q5_count": per_surah_count[5],
        "Q5_corpus_rank": rank[5],
        "Q5_med5_rank": med5_rank[5],
        "med5_ranking": med5_order,
        "top10_corpus": order[:10],
        "p_top2_med5": p_top2_med5,
        "p_top5_corpus": p_top5_corpus,
        "verdict": verdict,
    }


# ---------- Q005-F-02: māʾida-episode lexical isolation ----------
def run_F02(lemma_per_surah, lemma_attest_surahs, rng):
    family_targets = ["maA^}idap", "HawaAriy~uwn", "{l>akomah", ">akomah", ">aboraS", "{l>aboraS"]
    # select forms attested in Q5 specifically
    attested = []
    for f in family_targets:
        if f in lemma_per_surah[5]:
            attested.append(f)
    # also collect all forms whose stem matches māʾida or akma or abraṣ
    extra = set()
    for lemma in lemma_per_surah[5]:
        if "maA^}idap" in lemma or "akomah" in lemma or "aborS" in lemma or "aboraS" in lemma or "HawaAriy" in lemma:
            extra.add(lemma)
    family = sorted(set(attested) | extra)

    # Mark hapax: lemma's surah-set == {5}
    hapax = []
    for l in family:
        attest = lemma_attest_surahs.get(l, set())
        if attest == {5}:
            hapax.append(l)
    n_hapax = len(hapax)

    # Permutation null: 10000 random 4-lemma samples drawn from full QAC lemma inventory (all lemmas attested somewhere)
    # weighted by total count
    all_lemmas = list(lemma_attest_surahs.keys())
    weights = []
    for l in all_lemmas:
        # total count via sum across surahs (use lemma_per_surah)
        tot = sum(lemma_per_surah[s].get(l, 0) for s in range(1, 115))
        weights.append(tot)
    # cumulative for sampling
    total_w = sum(weights)
    cum = []
    s = 0
    for w in weights:
        s += w
        cum.append(s)

    def weighted_sample_4():
        out = []
        used = set()
        while len(out) < 4:
            r = rng.random() * total_w
            # binary search
            lo, hi = 0, len(cum) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if cum[mid] < r:
                    lo = mid + 1
                else:
                    hi = mid
            if lo not in used:
                used.add(lo)
                out.append(all_lemmas[lo])
        return out

    n_perm_match = 0
    target_size = max(4, len(family))
    for _ in range(N_PERM):
        sample = weighted_sample_4()
        # restricted to surah 5? hapax with attest = {5}? Note: most random lemmas attest in many surahs.
        # We test: ≥ 2 of the 4 sampled lemmas have attest-set = {ANY single surah}, AND that surah is the same.
        # Actually direct comparable: ≥ 2 lemmas in sample with attest-set == {Q*}, and if so, do they coincide on the same surah?
        per_lem = [lemma_attest_surahs[l] for l in sample]
        candidate_surahs = []
        for s_set in per_lem:
            if len(s_set) == 1:
                candidate_surahs.append(next(iter(s_set)))
        if len(candidate_surahs) >= 2:
            # require all of them to coincide
            from collections import Counter as Ctr
            mode_s, mode_n = Ctr(candidate_surahs).most_common(1)[0]
            if mode_n >= 2:
                n_perm_match += 1
    p_perm = n_perm_match / N_PERM

    primary_pass = n_hapax >= 2
    if primary_pass and p_perm < ALPHA_BON:
        verdict = f"VINDICATED — {n_hapax} corpus-hapax lemmas attested only in Q 5; p_perm={p_perm:.4f} < α_bon={ALPHA_BON}"
    elif primary_pass:
        verdict = f"DIRECTIONAL — {n_hapax} hapax but p_perm={p_perm:.4f} ≥ α_bon"
    else:
        verdict = f"NULL — {n_hapax} of family are corpus-hapax"

    return {
        "id": "Q005-F-02",
        "title": "māʾida-episode lexical isolation",
        "prereg_sha_expected": EXPECTED_SHA["Q005-F-02-maida-episode-isolation-prereg.md"],
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "family": family,
        "n_hapax": n_hapax,
        "hapax_lemmas": hapax,
        "lemma_attest_surah_sets": {l: sorted(lemma_attest_surahs.get(l, set())) for l in family},
        "p_perm": p_perm,
        "verdict": verdict,
    }


# ---------- Q005-F-03: Q 5:3 completion-cluster density ----------
def run_F03(lemma_per_verse, root_per_verse, wc_verse, rng):
    # 5-cluster: {LEMMA diyn, LEMMA niEomap, ROOT kml, ROOT tmm, ROOT rDw}
    LEM_TARGETS = ["diyn", "niEomap"]
    ROOT_TARGETS = ["kml", "tmm", "rDw"]

    per_verse_data = []
    for sv, wc in wc_verse.items():
        if wc == 0:
            continue
        lem_ct = sum(lemma_per_verse[sv].get(l, 0) for l in LEM_TARGETS)
        rt_ct = sum(root_per_verse[sv].get(r, 0) for r in ROOT_TARGETS)
        total_ct = lem_ct + rt_ct
        # distinct member count
        distinct = sum(1 for l in LEM_TARGETS if lemma_per_verse[sv].get(l, 0) > 0) + \
                   sum(1 for r in ROOT_TARGETS if root_per_verse[sv].get(r, 0) > 0)
        density = total_ct / wc
        per_verse_data.append({
            "sv": sv,
            "wc": wc,
            "total_ct": total_ct,
            "distinct": distinct,
            "density": density,
        })

    # Filter to verses with distinct ≥ 3
    qualifying = [v for v in per_verse_data if v["distinct"] >= 3]
    qualifying_sorted = sorted(qualifying, key=lambda x: (-x["density"], -x["distinct"]))
    q53 = next((v for v in per_verse_data if v["sv"] == (5, 3)), None)
    q53_distinct = q53["distinct"] if q53 else 0
    q53_density = q53["density"] if q53 else 0.0
    q53_total_ct = q53["total_ct"] if q53 else 0

    if q53 and q53["distinct"] >= 3:
        rank = next(i for i, v in enumerate(qualifying_sorted, 1) if v["sv"] == (5, 3))
    else:
        rank = None

    # Permutation null: shuffle the 5-cluster token-counts across all verses, preserving wc.
    # Build tuples of (lem_ct, rt_ct, distinct) and shuffle indices.
    # Simpler: shuffle the (total_ct, distinct) tuple and recompute density.
    pairs = [(v["total_ct"], v["distinct"]) for v in per_verse_data]
    wcs = [v["wc"] for v in per_verse_data]
    q53_idx = next(i for i, v in enumerate(per_verse_data) if v["sv"] == (5, 3))

    n_rank1 = 0
    for _ in range(N_PERM):
        perm = pairs[:]
        rng.shuffle(perm)
        # Build qualifying set under perm
        densities = []
        for i, (tot, dist) in enumerate(perm):
            if dist >= 3:
                densities.append((i, tot / wcs[i]))
        if not densities:
            continue
        densities_sorted = sorted(densities, key=lambda x: -x[1])
        # Q 5:3's permuted index is q53_idx (the position) but with shuffled (tot,dist) — the permuted assignment for q53_idx
        # We need to check: at q53_idx, the permuted (tot,dist) — does the density at q53_idx attain rank 1 in the permuted set?
        if perm[q53_idx][1] >= 3:
            top_idx = densities_sorted[0][0]
            if top_idx == q53_idx:
                n_rank1 += 1
    p_perm = n_rank1 / N_PERM

    if rank == 1 and p_perm < ALPHA_BON:
        verdict = f"VINDICATED — Q 5:3 corpus-rank-1 verse density (5-cluster); p_perm={p_perm:.4f} < α_bon={ALPHA_BON}"
    elif rank == 1:
        verdict = f"DIRECTIONAL — rank-1 but p_perm={p_perm:.4f} ≥ α_bon"
    elif rank is None:
        verdict = "NULL — Q 5:3 has fewer than 3 distinct cluster-members"
    else:
        verdict = f"NULL — Q 5:3 ranks {rank} (not 1)"

    top10 = [{"sv": list(v["sv"]), "density": v["density"], "distinct": v["distinct"], "total_ct": v["total_ct"], "wc": v["wc"]} for v in qualifying_sorted[:10]]
    return {
        "id": "Q005-F-03",
        "title": "Q 5:3 completion-of-religion cluster density",
        "prereg_sha_expected": EXPECTED_SHA["Q005-F-03-akmaltu-cluster-prereg.md"],
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "Q5_3_distinct": q53_distinct,
        "Q5_3_total_ct": q53_total_ct,
        "Q5_3_density": q53_density,
        "Q5_3_wc": q53["wc"] if q53 else 0,
        "Q5_3_rank_among_qualifying": rank,
        "n_qualifying_verses": len(qualifying),
        "top10": top10,
        "p_perm": p_perm,
        "verdict": verdict,
    }


# ---------- Q005-F-04: covenants density ----------
def run_F04(root_per_surah, wc_surah, rng):
    family = ["wvq", "Ehd", "Eqd", "nqD"]
    per_surah = {}
    for s in range(1, 115):
        c = sum(root_per_surah[s].get(r, 0) for r in family)
        per_surah[s] = (c, 100.0 * c / wc_surah[s])
    order = sorted(per_surah.items(), key=lambda x: -x[1][1])
    rank = {s: i + 1 for i, (s, _) in enumerate(order)}

    medinan5 = [2, 3, 4, 5, 9]
    med5_order = sorted(medinan5, key=lambda s: -per_surah[s][1])

    counts = [per_surah[s][0] for s in range(1, 115)]
    words = [wc_surah[s] for s in range(1, 115)]
    q5_idx = 4
    n_top3_corpus = 0
    n_rank1_med5 = 0
    for _ in range(N_PERM):
        perm = counts[:]
        rng.shuffle(perm)
        densities = [100.0 * perm[i] / words[i] for i in range(114)]
        sorted_idx = sorted(range(114), key=lambda i: -densities[i])
        ridx = sorted_idx.index(q5_idx) + 1
        if ridx <= 3:
            n_top3_corpus += 1
        # med5 rank
        med_dens = [(s, densities[s - 1]) for s in medinan5]
        med_sorted = sorted(med_dens, key=lambda x: -x[1])
        if med_sorted[0][0] == 5:
            n_rank1_med5 += 1
    p_top3 = n_top3_corpus / N_PERM
    p_rank1_med5 = n_rank1_med5 / N_PERM

    primary_rank = rank[5]
    primary_pass = primary_rank <= 3
    if primary_pass and p_top3 < ALPHA_BON:
        verdict = f"VINDICATED al-Rāzī multi-covenant claim — Q 5 corpus-rank {primary_rank}; p_perm={p_top3:.4f} < α_bon={ALPHA_BON}"
    elif primary_pass:
        verdict = f"DIRECTIONAL — rank ≤ 3 but p_perm={p_top3:.4f} ≥ α_bon"
    else:
        verdict = f"NULL — Q 5 covenant-density ranks {primary_rank} corpus-wide"

    return {
        "id": "Q005-F-04",
        "title": "Multiple-covenants vocabulary density",
        "prereg_sha_expected": EXPECTED_SHA["Q005-F-04-covenants-density-prereg.md"],
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "family": family,
        "Q5_count": per_surah[5][0],
        "Q5_density": per_surah[5][1],
        "Q5_corpus_rank": rank[5],
        "med5_ranking": med5_order,
        "top10_corpus": [(s, c, d) for s, (c, d) in order[:10]],
        "p_top3_corpus": p_top3,
        "p_rank1_med5": p_rank1_med5,
        "verdict": verdict,
    }


# ---------- Q005-F-05: late-Medinan signature triangulation ----------
def run_F05(rng):
    # FR-mean distances per surah
    with open(HNEW111) as f:
        d111 = json.load(f)
    n = 114
    D = [[0.0] * (n + 1) for _ in range(n + 1)]
    for i, j, v in d111["D_matrix_upper_triangular"]:
        D[i][j] = v
        D[j][i] = v
    fr_mean = [0.0] * (n + 1)
    for s in range(1, n + 1):
        ds = [D[s][t] for t in range(1, n + 1) if t != s]
        fr_mean[s] = sum(ds) / len(ds)

    # H-NEW-750 sig_A, sig_B, rhyme_entropy
    with open(HNEW750) as f:
        d750 = json.load(f)
    sig_A = [0.0] * (n + 1)
    sig_B = [0.0] * (n + 1)
    rhyme = [0.0] * (n + 1)
    for r in d750["per_surah"]:
        s = r["surah"]
        sig_A[s] = r["sig_A"]
        sig_B[s] = r["sig_B"]
        rhyme[s] = r["rhyme_entropy_nats"]

    def zify(arr):
        vals = arr[1:]
        mu = sum(vals) / len(vals)
        sd = (sum((x - mu) ** 2 for x in vals) / len(vals)) ** 0.5
        return [0.0] + [(x - mu) / sd for x in vals]

    z_fr = zify(fr_mean)
    z_A = zify(sig_A)
    z_B = zify(sig_B)
    z_rh = zify(rhyme)

    def vec(s):
        return [z_fr[s], z_A[s], z_B[s], z_rh[s]]

    def dist2(a, b):
        return sum((a[i] - b[i]) ** 2 for i in range(len(a))) ** 0.5

    v5 = vec(5)
    v9 = vec(9)
    v110 = vec(110)
    v2 = vec(2)
    LM = [(v9[i] + v110[i]) / 2 for i in range(4)]
    EM = v2  # Q 2 sole reference centroid for early-Medinan-ṭiwāl
    d_LM = dist2(v5, LM)
    d_EM = dist2(v5, EM)
    primary_pass = d_LM < d_EM

    # Per-axis
    per_axis = []
    for i, name in enumerate(["FR_mean", "sig_A", "sig_B", "rhyme_entropy"]):
        d_lm_i = abs(v5[i] - LM[i])
        d_em_i = abs(v5[i] - EM[i])
        per_axis.append({"axis": name, "v5": v5[i], "LM": LM[i], "EM": EM[i], "d_LM": d_lm_i, "d_EM": d_em_i, "closer_to_LM": d_lm_i < d_em_i})

    # Permutation null: redraw two random non-Q5 surahs S1,S2 to form a control LM-prime
    # and a single random non-Q5 surah S3 as control EM-prime.
    # p = fraction of permutations where d(v5, LM-prime) < d(v5, EM-prime).
    # NOTE: this is the chance-baseline distribution for the binary inequality.
    pool = [s for s in range(1, n + 1) if s != 5]
    n_lower = 0
    for _ in range(N_PERM):
        s1, s2 = rng.sample(pool, 2)
        s3 = rng.choice(pool)
        lmp = [(vec(s1)[i] + vec(s2)[i]) / 2 for i in range(4)]
        emp = vec(s3)
        if dist2(v5, lmp) < dist2(v5, emp):
            n_lower += 1
    p_chance_baseline = n_lower / N_PERM
    # The empirical observation is binary; under permutation, the CHANCE of d_LM' < d_EM' is p_chance_baseline.
    # Our observed inequality is statistically informative if it is rare under the chance distribution;
    # but for binary outcomes, p-value reduces to: if our outcome is "TRUE" then p = P(perm = TRUE) = p_chance_baseline.
    # Lower p_chance_baseline means our observed direction is rarer under random centroid pairing.
    # Bonferroni: report as is. Also report full per-axis view.

    if primary_pass and p_chance_baseline < ALPHA_BON:
        verdict = f"VINDICATED late-Medinan signature on Q 5 — d_LM={d_LM:.4f} < d_EM={d_EM:.4f}; chance-baseline p={p_chance_baseline:.4f} < α_bon={ALPHA_BON}"
    elif primary_pass:
        verdict = f"DIRECTIONAL — d_LM<d_EM but chance-baseline p={p_chance_baseline:.4f} ≥ α_bon"
    else:
        verdict = f"NULL — d_LM={d_LM:.4f} ≥ d_EM={d_EM:.4f}; Q 5 architecturally clusters with EARLY-Medinan-ṭiwāl head, NOT late-creedal"

    return {
        "id": "Q005-F-05",
        "title": "Late-Medinan signature triangulation",
        "prereg_sha_expected": EXPECTED_SHA["Q005-F-05-late-medinan-signature-prereg.md"],
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "v_Q5": v5,
        "v_Q9": v9,
        "v_Q110": v110,
        "v_Q2": v2,
        "LM_centroid": LM,
        "EM_reference": EM,
        "d_Q5_LM": d_LM,
        "d_Q5_EM": d_EM,
        "primary_passes_direction": primary_pass,
        "per_axis": per_axis,
        "p_chance_baseline": p_chance_baseline,
        "verdict": verdict,
        "interpretation_note": "Binary inequality d_LM<d_EM; chance-baseline p is the random-centroid probability of observing this direction. Under MW-7, this is a single-test-α=0.05 outcome unless replicated independently.",
    }


# ---------- main ----------
def main():
    verify_prereg_shas()
    print("[load] QAC v0.4 + Quran no-tashkeel...")
    (
        tokens_per_verse,
        lemma_per_surah,
        root_per_surah,
        lemma_attest_surahs,
        root_attest_surahs,
        lemma_per_verse,
        root_per_verse,
    ) = load_qac()
    wc_surah, wc_verse = load_word_counts()
    print(f"[load] done. Q 5 distinct lemmas: {len(lemma_per_surah[5])}; Q 5 distinct roots: {len(root_per_surah[5])}; words: {wc_surah[5]}")

    rng = random.Random(SEED)
    print("\n[run] Q005-F-01 PoTB density...")
    r1 = run_F01(lemma_per_surah, wc_surah, rng)
    print(f"  -> {r1['verdict']}")
    print("\n[run] Q005-F-02 māʾida-episode lexical isolation...")
    r2 = run_F02(lemma_per_surah, lemma_attest_surahs, rng)
    print(f"  -> {r2['verdict']}")
    print("\n[run] Q005-F-03 Q 5:3 completion-cluster density...")
    r3 = run_F03(lemma_per_verse, root_per_verse, wc_verse, rng)
    print(f"  -> {r3['verdict']}")
    print("\n[run] Q005-F-04 covenants density...")
    r4 = run_F04(root_per_surah, wc_surah, rng)
    print(f"  -> {r4['verdict']}")
    print("\n[run] Q005-F-05 late-Medinan signature...")
    r5 = run_F05(rng)
    print(f"  -> {r5['verdict']}")

    os.makedirs(CSV_DIR, exist_ok=True)
    for r in (r1, r2, r3, r4, r5):
        out = f"{CSV_DIR}/{r['id']}.json"
        with open(out, "w") as f:
            json.dump(r, f, indent=2, default=str, ensure_ascii=False)
        print(f"[write] {out}")
    print("\n[done] all 5 tests written.")


if __name__ == "__main__":
    main()
