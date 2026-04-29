#!/usr/bin/env python3
"""
Pre-registered Test 4 — Simultaneous N-constraint density.
Executes 12 binary constraint indicators per verse for the Quran and for
matched-Arabic pseudo-verses. Reports per-constraint rates, distribution
of simultaneous-count, KS test, tail analysis.

Rules tuple: (no-tashkeel, orthographic-token, graphemes,
counted-only-in-surah-1, hafs-kufan, mashriqi)

Seed: 20260412
"""
import json, re, csv, random, os, math, collections, unicodedata
from pathlib import Path
from collections import Counter, defaultdict

import numpy as np
from scipy.stats import ks_2samp

SEED = 20260412
random.seed(SEED)
np.random.seed(SEED)

ROOT = Path("/Users/grey/Downloads/quran")
OUT_DIR = ROOT / "findings/phase-b-hypotheses/analysis/simultaneous-constraint-density"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------- Arabic normalization ----------
# Strip tashkeel/diacritics, keep letters. Normalize to "graphemes" level:
# we keep hamza variants as-is (orthographic tokens), but remove tatweel and diacritics.
TASHKEEL = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u08D3-\u08E1\u08E3-\u08FF]")
TATWEEL = "\u0640"
QURAN_MARKS = re.compile(r"[\u06DD\u06DE\u06E9\u06DA\u06DB\u06DC\u06D6\u06D7\u06D8\u06D9\u06E0-\u06E8\u06EA-\u06ED]")
# unified sajavand / ornaments
SAFE_PUNCT = re.compile(r"[^\u0621-\u064A\u0660-\u0669\s]")  # keep only Arabic letters+digits+space
def strip_diacritics(s):
    s = TASHKEEL.sub("", s)
    s = s.replace(TATWEEL, "")
    s = QURAN_MARKS.sub("", s)
    return s

def orth_norm(s):
    s = strip_diacritics(s)
    s = SAFE_PUNCT.sub(" ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# letters-only (for counting graphemes length)
LETTER_RE = re.compile(r"[\u0621-\u064A]")
def letters_only(s):
    return "".join(LETTER_RE.findall(s))

def tokens(s):
    s = orth_norm(s)
    if not s: return []
    return s.split()

# ---------- Abjad (mashriqi) ----------
# Standard Mashriqi (Eastern) Abjad values: ا1 ب2 ج3 د4 ه5 و6 ز7 ح8 ط9 ي10
# ك20 ل30 م40 ن50 س60 ع70 ف80 ص90 ق100 ر200 ش300 ت400 ث500 خ600 ذ700 ض800 ظ900 غ1000
ABJAD = {
    'ا':1,'أ':1,'إ':1,'آ':1,'ء':1,'ؤ':1,'ئ':1,
    'ب':2,'ج':3,'د':4,'ه':5,'ة':5,'و':6,'ز':7,'ح':8,'ط':9,'ي':10,'ى':10,
    'ك':20,'ل':30,'م':40,'ن':50,'س':60,'ع':70,'ف':80,'ص':90,'ق':100,
    'ر':200,'ش':300,'ت':400,'ث':500,'خ':600,'ذ':700,'ض':800,'ظ':900,'غ':1000
}
def abjad_sum(s):
    s = strip_diacritics(s)
    return sum(ABJAD.get(c,0) for c in s)

def digit_root(n):
    if n == 0: return 0
    r = n % 9
    return 9 if r == 0 else r

# ---------- Load Quran ----------
def load_quran():
    with open(ROOT/"quran-text/quran-no-tashkeel.json",encoding="utf-8") as f:
        data = json.load(f)
    verses = []  # (surah, ayah, text_orth)
    for s in data:
        sid = s["id"]
        for v in s["verses"]:
            verses.append((sid, v["id"], orth_norm(v["text"])))
    return verses

# ---------- Load asma al-husna ----------
def load_divine_names():
    names = []
    with open(ROOT/"data/asma-al-husna.txt",encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith("#"): continue
            names.append(orth_norm(ln))
    # also add variants without الـ
    extra = set()
    for n in names:
        if n.startswith("ال") and len(n) > 3:
            extra.add(n[2:])
    return sorted(set(names) | extra, key=lambda x: -len(x))

DIVINE_NAMES = None

def has_divine_name(text):
    global DIVINE_NAMES
    toks = text.split()
    tset = set(toks)
    for name in DIVINE_NAMES:
        if name in tset:
            return 1
        # multi-word (rare), substring match
        if " " in name and name in text:
            return 1
    # also any inflected Allah (الله, لله, بالله, والله, فالله)
    for t in toks:
        if "الله" in t:
            return 1
    return 0

# ---------- Iltifat from catalog ----------
def load_iltifat_flags():
    flags = {}
    with open(ROOT/"findings/phase-b-hypotheses/iltifat-per-verse.csv",encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            k = (int(row["surah"]), int(row["ayah"]))
            # use strict inter-verse shift OR intra-verse shift
            v = 0
            try:
                if int(row.get("inter_shift_strict","0") or 0) == 1: v = 1
                elif int(row.get("intra_strict","0") or 0) == 1: v = 1
            except:
                v = 0
            flags[k] = v
    return flags

# ---------- Jinas catalog ----------
def load_jinas_flags():
    flags = set()
    path = ROOT/"findings/phase-b-hypotheses/jinas-all-instances.csv"
    with open(path,encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            try:
                s = int(row["surah"]); v = int(row["verse"])
                flags.add((s,v))
            except:
                pass
    return flags

# ---------- Morphology: tokens + roots per verse ----------
def load_morphology():
    """Parse Quranic morphology to get per-verse list of roots (bw) and lemma/tokens."""
    verse_roots = defaultdict(list)  # (s,a) -> list of roots in order
    verse_tokens = defaultdict(list) # (s,a) -> list of (lemma, tag)
    path = ROOT/"data/morphology/quranic-corpus-morphology-0.4.txt"
    with open(path,encoding="utf-8") as f:
        for ln in f:
            if not ln.startswith("("): continue
            parts = ln.strip().split("\t")
            if len(parts) < 4: continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", loc)
            if not m: continue
            s,a,w,sg = map(int, m.groups())
            # root
            root = None
            lemma = None
            for chunk in feats.split("|"):
                if chunk.startswith("ROOT:"):
                    root = chunk[5:]
                if chunk.startswith("LEM:"):
                    lemma = chunk[4:]
            if root:
                # only add once per word position
                verse_roots[(s,a)].append((w, root))
            verse_tokens[(s,a)].append((w, tag, lemma or form, root))
    # de-duplicate roots at word level (keep order per first occurrence in word)
    vr = {}
    for k, lst in verse_roots.items():
        seen = set()
        out = []
        for w, r in lst:
            key = (w, r)
            if key in seen: continue
            seen.add(key)
            out.append(r)
        vr[k] = out
    return vr, verse_tokens

# ---------- Load root stats for frequency quartiles ----------
def load_root_freqs():
    freqs = {}
    with open(ROOT/"data/morphology/root-stats.csv",encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            freqs[row["root"]] = int(row["total_occurrences"])
    return freqs

# ---------- Constraint computations ----------

def last_consonant(word):
    w = strip_diacritics(word)
    w = letters_only(w)
    if not w: return ""
    # skip weak endings (ا,ي,و,ه,ة) only if strong consonant exists before
    weak = set("ايوهة")
    for ch in reversed(w):
        if ch not in weak:
            return ch
    return w[-1]

def assonance_density(text):
    """Vowel/weak-letter density — proxy for assonance."""
    s = letters_only(text)
    if not s: return 0.0
    vowels = sum(1 for c in s if c in "اويى")
    return vowels/len(s)

def entropy_chars(text):
    s = letters_only(text)
    if not s: return 0.0
    c = Counter(s); n = len(s)
    return -sum((v/n)*math.log2(v/n) for v in c.values())

# ---------- Incipit patterns ----------
INCIPITS = [
    "قل","يا أيها","إن","إنا","إنما","و","لم","أم","الذي","الذين","بسم","كن","سبح","هو","الم","المر","الر","طه","يس","حم","طس","كهيعص","ن","ق","ص"
]
# For the 12-formula test: Qul, Yā ayyuhā, Inna, Wa, Lam, Am, Alladhī, Bismi, Kun, Sabbaḥa, Huwa, Alif-Lām-Mīm
CANONICAL_INCIPITS_12 = ["قل","يا أيها","إن","و","لم","أم","الذي","الذين","بسم","كن","سبح","سبحان","يسبح","هو","الم","المر","الر","طه","يس","حم","كهيعص","ن ","ق ","ص "]

def opens_with_canonical(text):
    t = text.strip()
    # check token-level for short words
    toks = t.split()
    if not toks: return 0
    first = toks[0]
    second = toks[1] if len(toks)>1 else ""
    two = first + " " + second
    for pat in CANONICAL_INCIPITS_12:
        if " " in pat:
            if two.startswith(pat): return 1
        else:
            if first == pat: return 1
    return 0

# ---------- Chiastic root-palindrome ----------
def has_root_palindrome(roots, min_len=3):
    """Any contiguous window of length >=3 that is a palindrome (roots)."""
    n = len(roots)
    if n < min_len: return 0
    # check windows of odd length >= 3
    for L in range(min_len, n+1):
        for i in range(0, n-L+1):
            w = roots[i:i+L]
            if w == w[::-1] and len(set(w)) >= 2:
                return 1
    return 0

# ---------- Baseline sampling ----------
def sample_pseudo_verses(text, lengths, rng):
    """Given a large text and target char-length distribution, sample
    contiguous pseudo-verses of those lengths (on letters-only stream)."""
    cleaned = orth_norm(text)
    words = cleaned.split()
    # reconstruct with word boundaries
    joined = " ".join(words)
    L = len(joined)
    verses = []
    for target in lengths:
        if target < 5: target = 5
        if target > L-10: target = L-10
        start = rng.randrange(0, max(1, L-target-1))
        # expand to word boundary
        while start>0 and joined[start] != " ":
            start -= 1
        end = min(L, start + target)
        while end<L and joined[end] != " ":
            end += 1
        chunk = joined[start:end].strip()
        verses.append(chunk)
    return verses

# ---------- Constraint evaluator ----------
def compute_constraints(verses, roots_by_verse=None, verse_keys=None,
                        root_freqs=None, jinas_flags=None, iltifat_flags=None,
                        entropy_baseline_median=None, assonance_baseline_by_bucket=None):
    """verses: list of verse_text (orthographically normalized)
       returns: N x 12 binary matrix, plus a dict of auxiliary data."""
    N = len(verses)
    M = np.zeros((N,12), dtype=np.int8)

    # Precompute letter-counts, last consonants, abjad
    letter_lens = [len(letters_only(v)) for v in verses]
    last_cons = [last_consonant(v.split()[-1]) if v.split() else "" for v in verses]
    abjad_roots = [digit_root(abjad_sum(v)) for v in verses]
    assonances = [assonance_density(v) for v in verses]
    entropies = [entropy_chars(v) for v in verses]

    # hapax/rare last word: need frequency of word across corpus
    all_words = Counter()
    for v in verses:
        for t in v.split(): all_words[t] += 1

    # particles list
    PARTICLES = set("و ف ثم بل أو أم إذ إذا إن أن ألا لا ما من في على إلى عن لم لن قد ل ب ك".split())

    # rhyme: group by surah if verse_keys provided (else sequential)
    for i,v in enumerate(verses):
        if verse_keys is not None:
            s,a = verse_keys[i]
            # find neighbors in same surah
            prev_last = next_last = None
            if i>0 and verse_keys[i-1][0]==s: prev_last = last_cons[i-1]
            if i<N-1 and verse_keys[i+1][0]==s: next_last = last_cons[i+1]
        else:
            prev_last = last_cons[i-1] if i>0 else None
            next_last = last_cons[i+1] if i<N-1 else None
        if last_cons[i] and (last_cons[i]==prev_last or last_cons[i]==next_last):
            M[i,0] = 1

        # 2. verse-end dispreference
        toks = v.split()
        if toks:
            lw = toks[-1]
            if all_words[lw] <= 1:
                M[i,1] = 1
            elif lw in PARTICLES:
                # particle-less? No — inverse: contains particle. Spec: "particle-less OR hapax OR rare root".
                pass
            else:
                # rare root: use roots_by_verse if available
                if roots_by_verse is not None and verse_keys is not None and root_freqs is not None:
                    rs = roots_by_verse.get(verse_keys[i], [])
                    if rs:
                        last_root = rs[-1]
                        freq = root_freqs.get(last_root, 0)
                        # bottom quartile
                        M[i,1] = 1 if freq <= 5 else 0

        # 3. divine name
        M[i,2] = has_divine_name(v)

        # 4. root palindrome
        if roots_by_verse is not None and verse_keys is not None:
            rs = roots_by_verse.get(verse_keys[i], [])
            M[i,3] = has_root_palindrome(rs, 3)
        else:
            # for baseline: no root data; fall back to token-lemma palindrome using orthographic stems (drop prefix ال, و, ف, ب, ل)
            stems = []
            for t in toks:
                t2 = t
                for pref in ("وال","فال","بال","لل","ال","و","ف","ب","ل"):
                    if t2.startswith(pref) and len(t2)>len(pref)+1:
                        t2 = t2[len(pref):]; break
                stems.append(t2)
            M[i,3] = has_root_palindrome(stems, 3)

        # 5. jinas
        if jinas_flags is not None and verse_keys is not None:
            M[i,4] = 1 if verse_keys[i] in jinas_flags else 0
        else:
            # fallback heuristic: any two tokens sharing same 3-char prefix after stripping common prefixes
            stems = []
            for t in toks:
                t2 = t
                for pref in ("وال","فال","بال","لل","ال","و","ف","ب","ل"):
                    if t2.startswith(pref) and len(t2)>len(pref)+1:
                        t2 = t2[len(pref):]; break
                stems.append(t2)
            c = Counter()
            for st in stems:
                if len(st)>=3:
                    c[st[:3]] += 1
            M[i,4] = 1 if any(cnt>=2 for cnt in c.values()) else 0

        # 6. abjad digit-root
        M[i,5] = 1 if abjad_roots[i] in (3,6,9) else 0

        # 7. assonance top-quartile vs length bucket (computed later with pooled thresholds)
        # placeholder — set later

        # 8. length Fibonacci band (letters)
        Lc = letter_lens[i]
        if any(abs(Lc-k)<=2 for k in (13,21,34,55,89)):
            M[i,7] = 1

        # 9. canonical incipit
        M[i,8] = opens_with_canonical(v)

        # 10. iltifat
        if iltifat_flags is not None and verse_keys is not None:
            M[i,9] = iltifat_flags.get(verse_keys[i], 0)
        else:
            # person-shift from previous pseudo-verse: approximate via pronoun surface forms
            prev = verses[i-1] if i>0 else ""
            def persons(t):
                p = set()
                tks = t.split()
                for x in tks:
                    if x in ("أنا","نحن","إنا","إني","إنني"): p.add(1)
                    elif x in ("أنت","أنتم","أنتما","أنتن","إنك","إنكم"): p.add(2)
                    elif x in ("هو","هي","هم","هن","إنه","إنها","إنهم","إنهن"): p.add(3)
                    # verb prefixes
                    if x.startswith("ن") and len(x)>3: p.add(1)
                    if x.startswith("ت") and len(x)>3: p.add(2)
                    if x.startswith("ي") and len(x)>3: p.add(3)
                return p
            if persons(prev) and persons(v) and persons(prev) != persons(v):
                M[i,9] = 1

        # 11. rare-root: any root in bottom decile
        if roots_by_verse is not None and verse_keys is not None and root_freqs is not None:
            rs = roots_by_verse.get(verse_keys[i], [])
            # bottom decile threshold — compute once
            if rs:
                for r in rs:
                    if root_freqs.get(r,0) <= 3:  # bottom decile empirically ≤ ~3 occurrences
                        M[i,10] = 1; break
        else:
            # fallback: any word with freq <= 2 in the corpus
            if any(all_words[t] <= 2 for t in toks):
                M[i,10] = 1

        # 12. surprisal > baseline median — done post-hoc

    # Populate 7 and 12 with length-stratified thresholds
    # Bucket by letter length
    def bucket(L):
        if L<20: return 0
        if L<40: return 1
        if L<80: return 2
        if L<160: return 3
        return 4
    buckets = [bucket(L) for L in letter_lens]

    if assonance_baseline_by_bucket is None:
        # compute 75th percentile per bucket from this corpus
        by_b = defaultdict(list)
        for i,b in enumerate(buckets): by_b[b].append(assonances[i])
        thr = {b: np.percentile(vals, 75) for b,vals in by_b.items()}
    else:
        thr = assonance_baseline_by_bucket
    for i in range(N):
        if assonances[i] > thr.get(buckets[i], 0):
            M[i,6] = 1

    if entropy_baseline_median is None:
        med = float(np.median(entropies))
    else:
        med = entropy_baseline_median
    for i in range(N):
        if entropies[i] > med:
            M[i,11] = 1

    return M, {"assonance_thr":thr, "entropy_median":med,
               "letter_lens":letter_lens, "abjad_roots":abjad_roots,
               "entropies":entropies}

# ---------- Main ----------
def main():
    print("Loading Quran...")
    verses = load_quran()
    verse_keys = [(s,a) for s,a,_ in verses]
    verse_texts = [t for _,_,t in verses]
    assert len(verses) == 6236, f"Expected 6236 verses, got {len(verses)}"

    global DIVINE_NAMES
    DIVINE_NAMES = load_divine_names()
    print(f"Divine names: {len(DIVINE_NAMES)}")

    print("Loading iltifat/jinas flags...")
    iltifat_flags = load_iltifat_flags()
    jinas_flags = load_jinas_flags()
    print(f"iltifat flags={sum(iltifat_flags.values())} jinas verses={len(jinas_flags)}")

    print("Loading morphology...")
    verse_roots, _ = load_morphology()
    root_freqs = load_root_freqs()
    print(f"Morphology verses with roots: {len(verse_roots)}  Roots in stats: {len(root_freqs)}")

    print("Computing Quran constraints...")
    M_quran, aux_q = compute_constraints(
        verse_texts, roots_by_verse=verse_roots, verse_keys=verse_keys,
        root_freqs=root_freqs, jinas_flags=jinas_flags, iltifat_flags=iltifat_flags)

    # Baseline: sample pseudo-verses matched to Quranic character-length distribution
    print("Sampling baseline pseudo-verses...")
    rng = random.Random(SEED)
    base_corpora = []
    for name in ["bukhari-noquran.txt","sira-ibn-hisham.txt","jahiz-hayawan.txt",
                 "muallaqa-amr-bin-kulthum.txt","muallaqa-antara.txt","muallaqa-harith.txt",
                 "muallaqa-imru-al-qais.txt","muallaqa-labid.txt","muallaqa-tarafa.txt",
                 "muallaqa-zuhayr.txt"]:
        p = ROOT/f"data/baseline-corpora/raw/{name}"
        if p.exists():
            with open(p,encoding="utf-8") as f:
                base_corpora.append(orth_norm(f.read()))
    # Ratio by length
    total_chars = sum(len(c) for c in base_corpora)
    weights = [len(c)/total_chars for c in base_corpora]

    # Target char-lengths: sample from Quran letter-length distribution (but use full orth-length so we can map back)
    target_lens = [len(v) for v in verse_texts]  # orthographic character lengths
    assigned = [rng.choices(range(len(base_corpora)), weights=weights, k=1)[0] for _ in target_lens]
    per_src = defaultdict(list)  # idx -> list of (i, target_len)
    for i, src_idx in enumerate(assigned):
        per_src[src_idx].append((i, target_lens[i]))
    base_verses_indexed = [None]*len(target_lens)
    for src_idx, items in per_src.items():
        lens = [L for _,L in items]
        pvs = sample_pseudo_verses(base_corpora[src_idx], lens, rng)
        for (i,_), pv in zip(items, pvs):
            base_verses_indexed[i] = pv
    base_verses = base_verses_indexed

    print("Computing baseline constraints...")
    # For baseline, we don't have morphology/iltifat/jinas catalogs — use fallbacks.
    M_base, aux_b = compute_constraints(
        base_verses, roots_by_verse=None, verse_keys=None,
        root_freqs=None, jinas_flags=None, iltifat_flags=None)

    # Also re-run Quran using the same FALLBACK detectors, for apples-to-apples on 4,5,10,11
    print("Computing Quran under fallback detectors (for apples-to-apples comparison)...")
    M_quran_fb, _ = compute_constraints(
        verse_texts, roots_by_verse=None, verse_keys=None,
        root_freqs=None, jinas_flags=None, iltifat_flags=None)

    # Save arrays
    np.save(OUT_DIR/"M_quran.npy", M_quran)
    np.save(OUT_DIR/"M_quran_fallback.npy", M_quran_fb)
    np.save(OUT_DIR/"M_baseline.npy", M_base)

    # Summaries
    def summarize(M, label):
        rates = M.mean(axis=0)
        counts = M.sum(axis=1)
        return {
            "label": label,
            "n": int(len(M)),
            "rates": rates.tolist(),
            "count_hist": np.bincount(counts, minlength=13).tolist(),
            "count_mean": float(counts.mean()),
            "count_std": float(counts.std()),
            "count_median": float(np.median(counts)),
            "tail_ge8": int((counts>=8).sum()),
            "tail_ge8_rate": float((counts>=8).mean()),
            "tail_ge9": int((counts>=9).sum()),
            "tail_ge10": int((counts>=10).sum()),
        }

    sum_q  = summarize(M_quran, "quran_catalog")
    sum_qf = summarize(M_quran_fb, "quran_fallback")
    sum_b  = summarize(M_base, "baseline_fallback")

    # KS tests
    c_q  = M_quran.sum(axis=1)
    c_qf = M_quran_fb.sum(axis=1)
    c_b  = M_base.sum(axis=1)
    ks_cat = ks_2samp(c_q, c_b)
    ks_fb  = ks_2samp(c_qf, c_b)

    # Tail z-test (two-proportion)
    def prop_z(k1,n1,k2,n2):
        p1,p2 = k1/n1, k2/n2
        p = (k1+k2)/(n1+n2)
        se = math.sqrt(p*(1-p)*(1/n1+1/n2)) if p*(1-p)>0 else 0
        return (p1-p2)/se if se else 0.0, p1, p2

    z_cat, p1_cat, p2_cat = prop_z(sum_q["tail_ge8"], sum_q["n"], sum_b["tail_ge8"], sum_b["n"])
    z_fb,  p1_fb,  p2_fb  = prop_z(sum_qf["tail_ge8"], sum_qf["n"], sum_b["tail_ge8"], sum_b["n"])

    results = {
        "seed": SEED,
        "rules_tuple": ["no-tashkeel","orthographic-token","graphemes","counted-only-in-surah-1","hafs-kufan","mashriqi"],
        "constraint_names":[
            "rhyme_continuity","verse_end_dispreference","divine_name_present","chiastic_root_palindrome_ge3",
            "jinas_catalog","abjad_digit_root_3_6_9","assonance_top_quartile","length_fibonacci_band",
            "canonical_incipit","iltifat_shift","rare_root","surprisal_gt_baseline_median"
        ],
        "quran_catalog": sum_q,
        "quran_fallback": sum_qf,
        "baseline_fallback": sum_b,
        "ks_catalog_vs_baseline": {"stat": float(ks_cat.statistic), "p": float(ks_cat.pvalue)},
        "ks_fallback_vs_baseline": {"stat": float(ks_fb.statistic), "p": float(ks_fb.pvalue)},
        "tail_ge8_catalog": {"z": float(z_cat), "quran": p1_cat, "baseline": p2_cat,
                             "ratio": (p1_cat/p2_cat) if p2_cat>0 else None},
        "tail_ge8_fallback":{"z": float(z_fb), "quran": p1_fb, "baseline": p2_fb,
                             "ratio": (p1_fb/p2_fb) if p2_fb>0 else None},
    }

    with open(OUT_DIR/"results.json","w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(json.dumps({k:v for k,v in results.items() if k not in ("quran_catalog","quran_fallback","baseline_fallback")}, indent=2))
    print("Quran catalog hist:", sum_q["count_hist"])
    print("Quran fallback hist:", sum_qf["count_hist"])
    print("Baseline hist:", sum_b["count_hist"])
    print("Done. Results saved to", OUT_DIR/"results.json")

if __name__ == "__main__":
    main()
