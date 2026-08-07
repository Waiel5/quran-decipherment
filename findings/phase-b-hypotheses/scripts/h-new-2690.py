#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2690 — Real quantitative scansion of the Qurʾān against the 16 al-Khalīlian buḥūr.

Unlike H-NEW-48 (which compares verse LETTER-COUNT distributions against Gaussians
centred at 1.6 x syllables_per_bayt, and never extracts a CV template), this script
performs actual scansion: vocalised orthography -> phonemes -> light/heavy syllable
string -> matched against the al-Khalīlian foot inventory.

THE GATE: the muʿallaqāt positive control runs FIRST and is asserted. If the scanner
cannot recover the known meters of poets whose meter is known, no Qurʾānic number is
reported at all.

Pre-reg: prereg-h-new-2690-quantitative-scansion.md (SHA-256 embedded, verified).
stdlib only. seed 20260509, replication 20260519, 10000 perms, Bonferroni k=3.

Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""
import json, re, os, sys, math, random, hashlib, unicodedata, datetime, platform, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(ROOT))
CSV = os.path.join(ROOT, "csv")
PREREG = os.path.join(ROOT, "prereg-h-new-2690-quantitative-scansion.md")
PREREG_SHA256 = "00ecfe67c21633491d80f7aff7f2dce39c1bd7c754ea5fbdc67a07304babe679"

SEED, SEED_REPL, N_PERM = 20260509, 20260519, 10000
BONF_K = 3
ALPHA_BON = 0.05 / BONF_K
ALPHA_METER = 0.05 / 16          # H2 inner Bonferroni over the 16 buḥūr

QURAN = os.path.join(REPO, "quran-text", "quran-full-tashkeel.json")
REVORD = os.path.join(REPO, "data", "revelation-order.csv")
DARIMI = os.path.join(REPO, "data", "literature", "hadith", "ahmedbaset-json",
                      "db", "by_book", "the_9_books", "darimi.json")
MUAL = os.path.join(REPO, "data", "baseline-corpora", "raw")
GROUND = {"muallaqa-imru-al-qais": "tawil", "muallaqa-zuhayr": "tawil",
          "muallaqa-amr-bin-kulthum": "wafir"}

FROZEN = {
    QURAN:  "382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715",
    REVORD: "74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7",
    DARIMI: "45ec3ac92b072287e6c7451084f55f50a2676e0eab2ec165c4ffecfa57f41d2a",
    os.path.join(MUAL, "muallaqa-imru-al-qais.txt"):
        "06f05f6a299d989fcaf330f43f7fba9116b373f94096d38ec07df71432f59c14",
    os.path.join(MUAL, "muallaqa-zuhayr.txt"):
        "9a8aac1838323aaa65f916f597ec38c842b74eed77ce44f53c2932b52e6610c2",
    os.path.join(MUAL, "muallaqa-amr-bin-kulthum.txt"):
        "d93a81bd2095c7db00417650f883c834077fac12668e50002c8b35f26e2ef720",
}


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def die(m):
    raise SystemExit(f"[FATAL] {m}")


_a = sha256_file(PREREG)
if _a != PREREG_SHA256:
    die(f"pre-reg SHA mismatch\n  expected {PREREG_SHA256}\n  actual   {_a}")
print(f"[SHA-OK] pre-reg locked: {_a}")
for p, want in FROZEN.items():
    g = sha256_file(p)
    if g != want:
        die(f"frozen input mismatch {p}\n  expected {want}\n  actual {g}")
print(f"[SHA-OK] {len(FROZEN)} frozen inputs verified")

# ---------------------------------------------------------------------------
# 1. Syllabifier — prereg §2.1, verbatim
# ---------------------------------------------------------------------------
FATHA, DAMMA, KASRA = "َ", "ُ", "ِ"
FATHATAN, DAMMATAN, KASRATAN = "ً", "ٌ", "ٍ"
SHADDA, SUKUN = "ّ", "ْ"
SUP_ALEF = "ٰ"
ALEF, WAW, YA = "ا", "و", "ي"
ALEF_MAQ, ALEF_MADDA, ALEF_WASLA = "ى", "آ", "ٱ"
SHORT = {FATHA: "a", DAMMA: "u", KASRA: "i"}
TANWIN = {FATHATAN: "an", DAMMATAN: "un", KASRATAN: "in"}
CONS = set("ءآأؤإئابةتثجحخدذرزسشصضطظعغفقكلمنهوىيٱ")
DROP = set("ـۖۗۘۙۚۛۜ۞۟۠"
           "ۣۧۨ۩۪ۭ۫۬"
           "ٕٖٜٟٓٔٗ٘ٙٚٛٝٞ"
           "۝ࣰࣱࣲ")
SUKUN_ALT, SMALL_WAW, SMALL_YA = "ۡ", "ۥ", "ۦ"
FINAL_VOWELS = set(SHORT) | set(TANWIN)


def normalize(t):
    t = unicodedata.normalize("NFC", t)
    t = "".join(c for c in t if c not in DROP)
    t = t.replace(SUKUN_ALT, SUKUN).replace(SMALL_WAW, WAW).replace(SMALL_YA, YA)
    t = t.replace(ALEF_MADDA, "أ" + FATHA + ALEF).replace(ALEF_WASLA, ALEF)
    t = re.sub(ALEF + FATHA, FATHA + ALEF, t)                       # order variance 1
    t = re.sub("([" + FATHA + DAMMA + KASRA + FATHATAN + DAMMATAN + KASRATAN + "])"
               + SHADDA, SHADDA + r"\1", t)                          # order variance 2
    return t


def phonemes(word):
    out, i = [], 0
    w = normalize(word)
    if len(w) > 1 and w[0] in (WAW, "ف") and w[1] not in SHORT and w[1] != SUKUN \
       and w[1] not in TANWIN and w[1] != SHADDA and w[1] != ALEF:
        w = w[0] + FATHA + w[1:]                                     # bare proclitic
    while i < len(w):
        ch = w[i]
        if ch in CONS:
            nxt = w[i + 1] if i + 1 < len(w) else ""
            if out and out[-1][0] == "V":
                pv = out[-1][1]
                if (ch in (ALEF, ALEF_MAQ) and pv == "a") \
                   or (ch == WAW and pv == "u" and nxt not in SHORT and nxt != SHADDA
                       and nxt not in TANWIN) \
                   or (ch == YA and pv == "i" and nxt not in SHORT and nxt != SHADDA
                       and nxt not in TANWIN):
                    out[-1] = ("VV", pv)
                    i += 1
                    if i < len(w) and w[i] == SUKUN:
                        i += 1
                    continue
            out.append(("C", ch)); i += 1
            if i < len(w) and w[i] == SHADDA:
                out.append(("C", ch)); i += 1
            if i < len(w) and w[i] == SUP_ALEF:
                out.append(("VV", "a")); i += 1; continue
            if i < len(w) and w[i] in SHORT:
                out.append(("V", SHORT[w[i]])); i += 1
            elif i < len(w) and w[i] in TANWIN:
                v = TANWIN[w[i]]
                out.append(("V", v[0])); out.append(("C", "n")); i += 1
                if i < len(w) and w[i] == ALEF:
                    i += 1
            elif i < len(w) and w[i] == SUKUN:
                i += 1
        elif ch == SUP_ALEF:
            out.append(("VV", "a")); i += 1
        else:
            i += 1
    return out


def syllables(ph):
    syl, i = [], 0
    while i < len(ph):
        if ph[i][0] != "C":
            i += 1; continue
        if i + 1 < len(ph) and ph[i + 1][0] in ("V", "VV"):
            if ph[i + 1][0] == "VV":
                syl.append("-"); i += 2
            elif (i + 2 < len(ph) and ph[i + 2][0] == "C"
                  and not (i + 3 < len(ph) and ph[i + 3][0] in ("V", "VV"))):
                syl.append("-"); i += 3
            else:
                syl.append("v"); i += 2
        else:
            i += 1
    return syl


def strip_pausal(text):
    """waqf: drop the unit-final short vowel / tanwin."""
    t = normalize(text).rstrip()
    while t and t[-1] in FINAL_VOWELS:
        t = t[:-1]
    return t


# Three pausal treatments. P_forceheavy is what the §4 control benchmark was calibrated
# on; P_pausal is prereg §5 T1 read literally; P_none is T2.
def scan(text, mode):
    t = strip_pausal(text) if mode == "P_pausal" else text
    s = []
    for w in t.split():
        s.extend(syllables(phonemes(w)))
    if s and mode in ("P_pausal", "P_forceheavy"):
        s[-1] = "-"
    return "".join(s)


# ---------------------------------------------------------------------------
# 2. The 16 buḥūr — prereg §2.2, verbatim
# ---------------------------------------------------------------------------
METERS = [
    ("tawil",     "الطويل",   "v--" + "v---" + "v--" + "v-v-"),
    ("madid",     "المديد",   "-v--" + "-v-" + "-v--"),
    ("basit",     "البسيط",   "--v-" + "-v-" + "--v-" + "-v-"),
    ("wafir",     "الوافر",   "v-vv-" + "v-vv-" + "v--"),
    ("kamil",     "الكامل",   "vv-v-" * 3),
    ("hazaj",     "الهزج",    "v---" * 2),
    ("rajaz",     "الرجز",    "--v-" * 3),
    ("ramal",     "الرمل",    "-v--" * 3),
    ("sari",      "السريع",   "--v-" + "--v-" + "-v-"),
    ("munsarih",  "المنسرح",  "--v-" + "---v" + "--v-"),
    ("khafif",    "الخفيف",   "-v--" + "--v-" + "-v--"),
    ("mudari",    "المضارع",  "v---" + "-v--"),
    ("muqtadab",  "المقتضب",  "---v" + "--v-"),
    ("mujtathth", "المجتث",   "--v-" + "-v--"),
    ("mutaqarib", "المتقارب", "v--" * 4),
    ("mutadarik", "المتدارك", "-v-" * 4),
]
MNAMES = [m[0] for m in METERS]


def lev(a, b):
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def best_meter(obs):
    """16-way meter ID against the doubled hemistich (a full bayt). Ties -> table order."""
    bk, bd = None, None
    for k, ar, h in METERS:
        c = h * 2
        d = lev(obs, c) / max(len(c), len(obs))
        if bd is None or d < bd - 1e-12:
            bd, bk = d, k
    return bk, bd


_TILE = {}


def tiled(pat, L, ph):
    key = (pat, L, ph)
    r = _TILE.get(key)
    if r is None:
        p = pat[ph:] + pat[:ph]
        r = (p * (L // len(p) + 2))[:L]
        _TILE[key] = r
    return r


def lev_band(a, b, cap):
    """Exact Levenshtein when the result is <= cap; otherwise returns cap+1.
    Verified identical to the unbanded `lev` on 150/150 sampled strings, on both
    d_min/argmin and the full 16-meter vector, before being adopted."""
    n = len(a)
    if n == 0:
        return min(len(b), cap + 1)
    INF = cap + 1
    m = len(b)
    prev = [j if j <= cap else INF for j in range(m + 1)]
    for i in range(1, n + 1):
        lo = max(1, i - cap); hi = min(m, i + cap)
        cur = [INF] * (m + 1)
        cur[lo - 1] = i if (lo - 1 == 0 and i <= cap) else INF
        ca = a[i - 1]; best = INF
        for j in range(lo, hi + 1):
            c = prev[j - 1] if ca == b[j - 1] else prev[j - 1] + 1
            v = cur[j - 1] + 1
            if v < c: c = v
            v = prev[j] + 1
            if v < c: c = v
            if c > INF: c = INF
            cur[j] = c
            if c < best: best = c
        if best >= INF:
            return INF
        prev = cur
    return prev[m] if prev[m] <= cap else INF


def metricality(obs):
    """Length-invariant, phase-invariant d_min + argmin meter. prereg §2.3.
    Since obs and every tiled canon have equal length, Hamming distance is an upper
    bound on edit distance, so it supplies an exact band for each meter."""
    L = len(obs)
    if L < 4:
        return 1.0, None, {}
    per = {}
    bd, bk = None, None
    for k, ar, h in METERS:
        cands = []
        capk = None
        for ph in range(len(h)):
            c = tiled(h, L, ph)
            ham = sum(1 for x, y in zip(obs, c) if x != y)
            cands.append((ham, c))
            if capk is None or ham < capk:
                capk = ham
        best = capk
        for ham, c in cands:
            d = lev_band(obs, c, best)
            if d < best:
                best = d
        per[k] = best / L
        if bd is None or per[k] < bd - 1e-12:
            bd, bk = per[k], k
    return bd, bk, per


# ---------------------------------------------------------------------------
# 3. POSITIVE CONTROL — runs FIRST, and gates everything (prereg §4)
# ---------------------------------------------------------------------------
AR = re.compile("[ء-ي]")
DIAC = re.compile("[ً-ْٰٓ-ٕۡ]")
VOC_THRESH = 0.55


def load_muallaqat():
    out = {}
    for stem, known in GROUND.items():
        keep = []
        for l in open(os.path.join(MUAL, stem + ".txt"), encoding="utf-8", errors="replace"):
            a = len(AR.findall(l))
            if a >= 12 and len(DIAC.findall(l)) / a >= VOC_THRESH:
                keep.append(l.strip())
        out[stem] = (known, keep)
    return out


MU = load_muallaqat()
print("\n" + "=" * 78)
print("POSITIVE CONTROL (prereg §4) — reported BEFORE any Qurʾānic number")
print("=" * 78)

control = {}
for mode in ("P_forceheavy", "P_pausal", "P_none"):
    tot = cor = poem_ok = 0
    per_poet = {}
    for stem, (known, lines) in MU.items():
        votes, n = {}, 0
        for l in lines:
            o = scan(l, mode)
            if len(o) < 8:
                continue
            b, d = best_meter(o)
            votes[b] = votes.get(b, 0) + 1
            n += 1
            tot += 1
            cor += (b == known)
        top = sorted(votes.items(), key=lambda kv: (-kv[1], MNAMES.index(kv[0])))[0][0]
        poem_ok += (top == known)
        per_poet[stem] = {"known": known, "n": n, "top": top,
                          "acc": round(votes.get(known, 0) / n, 4) if n else 0.0}
    acc = cor / tot if tot else 0.0
    control[mode] = {"per_bayt_acc": round(acc, 4), "n_bayts": tot,
                     "per_poem_correct": poem_ok, "per_poet": per_poet}
    print(f"  {mode:<14} n={tot:>4}  per-bayt top-1 = {acc:>6.1%}  per-poem = {poem_ok}/3  "
          + "  ".join(f"{k.split('-', 1)[1][:9]}={v['acc']:.0%}" for k, v in per_poet.items()))

# GATE
G = control["P_forceheavy"]
if G["per_poem_correct"] < 2 or G["per_bayt_acc"] < 0.40:
    die("POSITIVE-CONTROL GATE FAILED — scanner not fit for purpose; "
        "no Qurʾānic result may be reported (prereg §4, §10).")
print(f"  [GATE PASS] per-poem {G['per_poem_correct']}/3, per-bayt {G['per_bayt_acc']:.1%} "
      f"(chance 6.25%, 16-way)")

# Frozen-benchmark conformance (§4). Reported, not fatal: the pre-registration's §5
# description of T1 is internally inconsistent with the §4 calibration (see finding).
BENCH = {"per_bayt_acc": 0.7708, "per_poem_correct": 3, "n_bayts": 240}
bench_ok = (G["per_poem_correct"] == BENCH["per_poem_correct"]
            and abs(G["per_bayt_acc"] - BENCH["per_bayt_acc"]) < 0.005
            and G["n_bayts"] == BENCH["n_bayts"])
print(f"  [§4 benchmark conformance, P_forceheavy] {'MATCHES' if bench_ok else 'DIFFERS'} "
      f"(frozen {BENCH['per_bayt_acc']:.1%} / {BENCH['per_poem_correct']}/3 / n={BENCH['n_bayts']})")

# ---------------------------------------------------------------------------
# 4. Corpora
# ---------------------------------------------------------------------------
quran = json.load(open(QURAN, encoding="utf-8"))
QV = []          # (surah, verse, text)
for si, su in enumerate(quran, 1):
    for vi, v in enumerate(su["verses"], 1):
        QV.append((si, vi, v["text"] if isinstance(v, dict) else str(v)))
if len(QV) != 6236:
    die(f"Qurʾān verses {len(QV)} != 6236")

dar = json.load(open(DARIMI, encoding="utf-8"))
SENT = re.compile(r"[.؟!]")


def prose_units(matn_only):
    out = []
    for h in dar["hadiths"]:
        t = h.get("arabic") or ""
        if matn_only:
            k = t.rfind("قَالَ")
            if k >= 0:
                t = t[k + 5:]
        for s in SENT.split(t):
            s = s.strip()
            if len(AR.findall(s)) >= 10:
                out.append(s)
    return out


PERIOD, NVERSE = {}, {}
for i, line in enumerate(open(REVORD, encoding="utf-8")):
    if i == 0:
        continue
    f = line.rstrip("\n").split(",")
    PERIOD[int(f[1])] = f[4]
for s, v, t in QV:
    NVERSE[s] = NVERSE.get(s, 0) + 1

print(f"\n[corpora] Qurʾān verses={len(QV)}  Dārimī ḥadīth={len(dar['hadiths'])}  "
      f"muʿallaqāt baytss={G['n_bayts']}")

# ---------------------------------------------------------------------------
# 5. Statistics
# ---------------------------------------------------------------------------
def perm_median_diff(A, B, seed, n_perm=N_PERM):
    """Two-sided-agnostic: p = P(median(permA) - median(permB) >= observed)."""
    obs = statistics.median(A) - statistics.median(B)
    pool = A + B
    nA = len(A)
    rng = random.Random(seed)
    ge = 0
    for _ in range(n_perm):
        rng.shuffle(pool)
        d = statistics.median(pool[:nA]) - statistics.median(pool[nA:])
        if d >= obs:
            ge += 1
    return obs, (ge + 1) / (n_perm + 1)


def matched_noise(strings, seed):
    rng = random.Random(seed)
    out = []
    for o in strings:
        if not o:
            out.append(o); continue
        p = o.count("-") / len(o)
        out.append("".join("-" if rng.random() < p else "v" for _ in o))
    return out


RESULTS = {}
for mode in ("P_forceheavy", "P_pausal", "P_none"):
    print(f"\n--- scanning under {mode} ---")
    qs = [scan(t, mode) for _, _, t in QV]
    ps = []
    for stem, (known, lines) in MU.items():
        ps.extend(scan(l, mode) for l in lines)
    rs = [scan(t, mode) for t in prose_units(False)]
    rs_matn = [scan(t, mode) for t in prose_units(True)]

    # qs stays index-aligned with QV (H3 selects verses by index); short units are
    # masked out of the statistics rather than filtered out of the list.
    keep_q = [i for i, o in enumerate(qs) if len(o) >= 4]
    ps = [o for o in ps if len(o) >= 8]
    rs = [o for o in rs if len(o) >= 8]
    rs_matn = [o for o in rs_matn if len(o) >= 8]

    # Comparison arms are capped at a seed-locked sample (ARM_CAP) purely for runtime;
    # the Qurʾān arm is always complete. Medians are stable at this n.
    ARM_CAP = 2500
    rng = random.Random(SEED)
    rs_s = rs if len(rs) <= ARM_CAP else rng.sample(rs, ARM_CAP)
    rs_m = rs_matn if len(rs_matn) <= ARM_CAP else random.Random(SEED).sample(rs_matn, ARM_CAP)
    qn = matched_noise(qs, SEED)
    qn_s = qn if len(qn) <= ARM_CAP else random.Random(SEED).sample(qn, ARM_CAP)
    pn = matched_noise(ps, SEED)

    # profiles computed ONCE per string and reused by H1/H2/H3
    def prof(strs, tag):
        out = []
        for i, o in enumerate(strs):
            out.append(metricality(o))
            if i and i % 1000 == 0:
                print(f"      [{tag}] {i}/{len(strs)}", flush=True)
        return out

    P_q = prof(qs, "quran")
    P_p = prof(ps, "poetry")
    P_r = prof(rs_s, "prose")
    P_rm = prof(rs_m, "prose-matn")
    P_qn = prof(qn_s, "noise-Q")
    P_pn = prof(pn, "noise-P")

    q_d = [P_q[i][0] for i in keep_q]           # masked, not index-aligned — stats only
    p_d = [x[0] for x in P_p]; r_d = [x[0] for x in P_r]
    rm_d = [x[0] for x in P_rm]; qn_d = [x[0] for x in P_qn]; pn_d = [x[0] for x in P_pn]
    r_d_full = r_d

    med = lambda x: round(statistics.median(x), 5)
    mean = lambda x: round(statistics.mean(x), 5)
    print(f"   median d_min  Qurʾān={med(q_d)}  poetry={med(p_d)}  prose={med(r_d)}  "
          f"| noise(Q)={med(qn_d)} noise(P)={med(pn_d)}")

    # H1
    h1a_obs, h1a_p = perm_median_diff(q_d, p_d, SEED)
    h1b_obs, h1b_p = perm_median_diff(r_d, q_d, SEED)
    h1a_r, h1a_pr = perm_median_diff(q_d, p_d, SEED_REPL)
    h1b_r, h1b_pr = perm_median_diff(r_d, q_d, SEED_REPL)

    # H2 — per-meter Qurʾān conformity vs matched noise (read from stored profiles)
    q_sub = ([P_q[i] for i in keep_q] if len(keep_q) <= ARM_CAP else
             [P_q[i] for i in sorted(random.Random(SEED).sample(keep_q, ARM_CAP))])
    per_meter = {}
    for k, ar, h in METERS:
        obs_k = [x[2].get(k, 1.0) for x in q_sub if x[2]]
        noi_k = [x[2].get(k, 1.0) for x in P_qn if x[2]]
        d, p = perm_median_diff(noi_k, obs_k, SEED, n_perm=2000)
        per_meter[k] = {"median_obs": med(obs_k), "median_noise": med(noi_k),
                        "noise_minus_obs": round(d, 5), "p": round(p, 6),
                        "matches": bool(d > 0 and p < ALPHA_METER)}
    matched = [k for k, v in per_meter.items() if v["matches"]]

    # H3
    A = [i for i, (s, v, t) in enumerate(QV) if s >= 78]
    B = [i for i, (s, v, t) in enumerate(QV)
         if PERIOD.get(s) == "Medinan" and NVERSE.get(s, 0) >= 100]
    kq = set(keep_q)
    a_d = [P_q[i][0] for i in A if i in kq]
    b_d = [P_q[i][0] for i in B if i in kq]
    h3_obs, h3_p = perm_median_diff(b_d, a_d, SEED)
    h3_r, h3_pr = perm_median_diff(b_d, a_d, SEED_REPL)
    votesA = {}
    for i in A:
        if i < len(P_q):
            k = P_q[i][1]
            if k:
                votesA[k] = votesA.get(k, 0) + 1
    modeA = sorted(votesA.items(), key=lambda kv: (-kv[1], MNAMES.index(kv[0])))[0][0]

    RESULTS[mode] = {
        "n": {"quran": len(keep_q), "poetry": len(ps), "prose_sampled": len(rs_s),
              "prose_full": len(rs), "prose_matn": len(rm_d),
              "mufassal_A": len(a_d), "long_medinan_B": len(b_d)},
        "median_d_min": {"quran": med(q_d), "poetry": med(p_d), "prose": med(r_d),
                         "prose_full": med(r_d_full), "prose_matn": med(rm_d),
                         "noise_quran": med(qn_d), "noise_poetry": med(pn_d)},
        "mean_d_min": {"quran": mean(q_d), "poetry": mean(p_d), "prose": mean(r_d)},
        "H1a_quran_gt_poetry": {"diff": round(h1a_obs, 5), "p": round(h1a_p, 6),
                                "p_repl": round(h1a_pr, 6),
                                "direction_ok": h1a_obs > 0,
                                "PASS": h1a_obs > 0 and h1a_p < ALPHA_BON},
        "H1b_prose_gt_quran": {"diff": round(h1b_obs, 5), "p": round(h1b_p, 6),
                               "p_repl": round(h1b_pr, 6),
                               "direction_ok": h1b_obs > 0,
                               "PASS": h1b_obs > 0 and h1b_p < ALPHA_BON},
        "H2_per_meter": per_meter,
        "H2_matched_meters": matched,
        "H2_PASS_no_match": len(matched) == 0,
        "H3": {"diff_B_minus_A": round(h3_obs, 5), "p": round(h3_p, 6),
               "p_repl": round(h3_pr, 6), "modal_meter_A": modeA,
               "modal_ok": modeA in ("rajaz", "sari"),
               "direction_ok": h3_obs > 0,
               "PASS": h3_obs > 0 and h3_p < ALPHA_BON and modeA in ("rajaz", "sari")},
        "meter_votes_mufassal": dict(sorted(votesA.items(), key=lambda kv: -kv[1])[:6]),
    }
    R = RESULTS[mode]
    print(f"   H1a Qurʾān>poetry  diff={R['H1a_quran_gt_poetry']['diff']:+.5f} "
          f"p={R['H1a_quran_gt_poetry']['p']:.5f} -> {R['H1a_quran_gt_poetry']['PASS']}")
    print(f"   H1b prose>Qurʾān   diff={R['H1b_prose_gt_quran']['diff']:+.5f} "
          f"p={R['H1b_prose_gt_quran']['p']:.5f} -> {R['H1b_prose_gt_quran']['PASS']}")
    print(f"   H2 matched buḥūr: {matched or 'NONE'} -> PASS={R['H2_PASS_no_match']}")
    print(f"   H3 B-A diff={R['H3']['diff_B_minus_A']:+.5f} p={R['H3']['p']:.5f} "
          f"modal(A)={modeA} -> {R['H3']['PASS']}")

# ---------------------------------------------------------------------------
# 6. Verdict — must hold under both pausal tuples (prereg §10)
# ---------------------------------------------------------------------------
def verdict_for(key, getter):
    t1 = getter(RESULTS["P_pausal"])
    t2 = getter(RESULTS["P_none"])
    tc = getter(RESULTS["P_forceheavy"])
    if not tc["PASS"]:
        return "REVERSED-PRECOMMIT-VIOLATION" if not tc.get("direction_ok", True) else "NULL"
    return "PASS" if (t1["PASS"] and t2["PASS"]) else "RULES-TUPLE-FRAGILE"


FINAL = {
    "H1": ("PASS" if all(verdict_for(k, g) == "PASS" for k, g in
                         (("a", lambda R: R["H1a_quran_gt_poetry"]),
                          ("b", lambda R: R["H1b_prose_gt_quran"])))
           else "; ".join(f"{k}:{verdict_for(k, g)}" for k, g in
                          (("a", lambda R: R["H1a_quran_gt_poetry"]),
                           ("b", lambda R: R["H1b_prose_gt_quran"])))),
    "H2": ("PASS" if all(RESULTS[m]["H2_PASS_no_match"] for m in RESULTS)
           else "FALSIFIED-buhur-matched"),
    "H3": verdict_for("H3", lambda R: R["H3"]),
}
VERDICT = ("CONFIRMED" if all(v == "PASS" for v in FINAL.values())
           else ("NULL" if all(v in ("NULL", "FALSIFIED-buhur-matched") for v in FINAL.values())
                 else "PARTIAL"))
print(f"\n[VERDICT] {FINAL}\n[OVERALL] {VERDICT}")

# ---------------------------------------------------------------------------
# 7. Immutable run directory
# ---------------------------------------------------------------------------
stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
RUN = os.path.join(ROOT, "runs", "h-new-2690", stamp)
if os.path.exists(RUN):
    die(f"run dir exists (immutability): {RUN}")
os.makedirs(RUN)

out = {
    "id": "H-NEW-2690",
    "title": "Real quantitative scansion — the Qurʾān's syllable-weight profile vs the 16 buḥūr",
    "prereg_sha256": PREREG_SHA256,
    "seed": SEED, "seed_replication": SEED_REPL, "n_perm": N_PERM,
    "bonferroni_k": BONF_K, "alpha_bonferroni": ALPHA_BON,
    "alpha_meter_inner": ALPHA_METER,
    "differs_from_h_new_48": "H-NEW-48 compares verse LETTER-COUNT distributions to "
                             "Gaussians at 1.6*syllables_per_bayt and never extracts a CV "
                             "template. This performs actual scansion and measures "
                             "length-invariant metricality d_min.",
    "positive_control": control,
    "control_gate_passed": True,
    "prereg_s4_benchmark_conformance": {"expected": BENCH, "matched": bench_ok},
    "vocalisation_survey": {
        "quran_full_tashkeel": 0.918, "muallaqa_zuhayr": 0.839,
        "muallaqa_imru_al_qais": 0.777, "muallaqa_amr_bin_kulthum": 0.722,
        "muallaqa_harith": 0.205, "muallaqa_labid": 0.164, "muallaqa_antara": 0.068,
        "muallaqa_tarafa": 0.031, "diwans_all": 0.0, "bukhari_baseline_txt": 0.006,
        "jahiz": 0.0, "darimi_hadith": 0.866},
    "meters": {k: h for k, ar, h in METERS},
    "tuples": RESULTS,
    "inference_verdicts": FINAL,
    "verdict": VERDICT,
}
json.dump(out, open(os.path.join(RUN, "result.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
json.dump({"id": "H-NEW-2690", "utc": stamp,
           "script_sha256": sha256_file(os.path.abspath(__file__)),
           "prereg_sha256": PREREG_SHA256,
           "inputs_sha256": {os.path.relpath(p, REPO): FROZEN[p] for p in FROZEN},
           "python": platform.python_version(), "seeds": [SEED, SEED_REPL],
           "n_perm": N_PERM, "verdict": VERDICT,
           "immutability": "Immutable. Never delete or overwrite, per prereg §8."},
          open(os.path.join(RUN, "manifest.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
json.dump(out, open(os.path.join(CSV, "h-new-2690.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print(f"\n[run] {RUN}")
