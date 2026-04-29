#!/usr/bin/env python3
"""H-NEW-197: Prophet-narrative parallelism across surahs.

Pre-registration: findings/phase-b-hypotheses/h-new-197-prophet-cycle-prereg.md
Seed: 20260419.  Bonferroni k = 2.
"""
from __future__ import annotations

import json
import re
import pathlib
import itertools
import numpy as np


ROOT = pathlib.Path("/Users/grey/Downloads/quran")
QURAN = ROOT / "quran-text" / "quran-min-tashkeel.json"
OUTDIR = ROOT / "findings" / "phase-b-hypotheses" / "h-new-197-work"
OUTDIR.mkdir(parents=True, exist_ok=True)
SEED = 20260419
N_NULL = 2000

# ---- pre-registered event atoms ----
# NB: we operate on min-tashkeel text so we DO have hamza + long vowels but
# limited diacritics.  Each entry is a list of substrings; if ANY substring
# appears in the verse text, the atom fires.

MOSES_ATOMS = [
    ("MU", ["موسى", "موسىٰ", "مُوسىٰ", "موسيٰ"]),
    ("FR", ["فرعون"]),
    ("RB", ["ربك", "ربنا", "ربي", "ربه"]),
    ("SG", ["ءاي", "اٰي", "آي"]),
    ("ST", ["عصا", "حية", "ثعبان"]),
    ("HA", ["بيضاء", "يده"]),
    ("SO", ["سحر", "ساحر", "سحرة", "السحر"]),
    ("SE", ["بحر", "غرق", "اليم", "يم"]),
    ("CH", ["بني اسر", "بنى اسر", "اسرٰءيل", "إسرائيل", "اسرائيل", "بنى إسرٰ"]),
    ("CA", ["عجل", "العجل"]),
    ("MT", ["طور", "الطور", "الواح", "الألواح"]),
]

ABRAHAM_ATOMS = [
    ("IB", ["ابرٰه", "ابراه", "إبراه", "إِبرٰه"]),
    ("FT", ["ءازر", "ازر", "ابيه", "أبيه", "اباه", "لابيه"]),
    ("ID", ["اصنام", "أصنام", "تماثيل", "وثن", "اوثٰن"]),
    ("AS", ["نجم", "النجم", "شمس", "الشمس", "قمر", "القمر", "كوكب", "الكوكب"]),
    ("FI", ["نارا", "النار", "حرق", "احرقوه", "حرّقوه"]),
    ("SC", ["اسمٰع", "إسماع", "اسماع", "اسحٰق", "إسحاق", "اسحاق", "ذبح", "غلٰم", "الذبح", "غلام"]),
    ("GU", ["ضيف", "رسلنا", "المرسلون", "ضيوف"]),
    ("PR", ["مقام", "ادع", "اجعل", "ربنا"]),
    ("HA", ["البيت", "بيت", "حج", "كعب", "قبل"]),
    ("LO", ["لوط", "لوطا", "مؤتفك"]),
]


def load_quran():
    with open(QURAN, encoding="utf-8") as f:
        return json.load(f)


def strip_diacritics(s: str) -> str:
    # remove all combining marks (tashkeel, hamza-on-carrier marks, dagger alif etc.)
    t = re.sub(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0656-\u065F]", "", s)
    # normalise alef variants (pre-registered choice: merge أ,إ,آ,ا → ا)
    t = t.translate(str.maketrans({"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا"}))
    # normalise ya variants
    t = t.translate(str.maketrans({"ى": "ي"}))
    # normalise ta marbuta / ha
    t = t.replace("ة", "ه")
    return t


def verse_atoms(text: str, atoms):
    """Return list of atom codes that fire in this verse (order = atom list order)."""
    t = strip_diacritics(text)
    # also strip tatweel and normalise some letters
    t = t.replace("ـ", "")
    fired = []
    for code, needles in atoms:
        for n in needles:
            nn = strip_diacritics(n)
            if nn and nn in t:
                fired.append(code)
                break
    return fired


def build_sequence(surah_verses, atoms, anchor_code, window=1):
    """Build per-surah ordered atom string.
    surah_verses: list of dicts {id, text}
    anchor_code: which atom marks the prophet mention
    """
    n = len(surah_verses)
    # first compute per-verse atom set
    per_verse = [verse_atoms(v["text"], atoms) for v in surah_verses]
    anchor_idx = [i for i, av in enumerate(per_verse) if anchor_code in av]
    # collect verses within ±window of any anchor verse
    keep = set()
    for i in anchor_idx:
        for j in range(max(0, i - window), min(n, i + window + 1)):
            keep.add(j)
    # ordered list of kept verse indices
    kept = sorted(keep)
    # build ordered atom string; for each kept verse, append atoms in their
    # pre-registered order (atom-list order), skipping duplicates within the verse
    seq = []
    for j in kept:
        seen = set()
        for c in per_verse[j]:
            if c in seen:
                continue
            seen.add(c)
            seq.append(c)
    # collapse *adjacent* repeats
    collapsed = []
    for c in seq:
        if not collapsed or collapsed[-1] != c:
            collapsed.append(c)
    return collapsed, per_verse, kept


def levenshtein(a, b):
    if len(a) < len(b):
        a, b = b, a
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(
                prev[j] + 1,
                cur[-1] + 1,
                prev[j - 1] + (ca != cb),
            ))
        prev = cur
    return prev[-1]


def pair_sim(a, b):
    if not a and not b:
        return 1.0
    m = max(len(a), len(b))
    if m == 0:
        return 1.0
    return 1 - levenshtein(a, b) / m


def mean_pairwise(seqs):
    keys = list(seqs.keys())
    vals = []
    for i, j in itertools.combinations(keys, 2):
        vals.append(pair_sim(seqs[i], seqs[j]))
    return float(np.mean(vals)), vals, list(itertools.combinations(keys, 2))


def null_A(per_verse_by_surah, atoms, anchor_code, rng, window=1):
    """Null A: within each surah, shuffle the per-verse atom-bags, preserving the
    multiset of verse bags but re-deriving anchor positions & window from the
    shuffled ordering.  Then rebuild sequences."""
    seqs = {}
    for s, per_verse in per_verse_by_surah.items():
        pv = list(per_verse)
        idx = list(range(len(pv)))
        rng.shuffle(idx)
        pv_shuf = [pv[i] for i in idx]
        anchor_idx = [i for i, av in enumerate(pv_shuf) if anchor_code in av]
        keep = set()
        for i in anchor_idx:
            for j in range(max(0, i - window), min(len(pv_shuf), i + window + 1)):
                keep.add(j)
        seq = []
        for j in sorted(keep):
            seen = set()
            for c in pv_shuf[j]:
                if c in seen:
                    continue
                seen.add(c)
                seq.append(c)
        coll = []
        for c in seq:
            if not coll or coll[-1] != c:
                coll.append(c)
        seqs[s] = coll
    m, _, _ = mean_pairwise(seqs)
    return m


def null_B(observed_seqs, rng):
    """Null B: shuffle the atom string within each surah."""
    seqs = {}
    for s, seq in observed_seqs.items():
        arr = list(seq)
        rng.shuffle(arr)
        seqs[s] = arr
    m, _, _ = mean_pairwise(seqs)
    return m


def run_cycle(name, surahs, atoms, anchor, quran, rng):
    # extract per-verse atom matrix + observed sequence for each target surah
    seqs = {}
    per_verse_by_surah = {}
    per_surah_keep = {}
    for s in surahs:
        surah = quran[s - 1]
        verses = surah["verses"]
        seq, pv, kept = build_sequence(verses, atoms, anchor, window=1)
        seqs[s] = seq
        per_verse_by_surah[s] = pv
        per_surah_keep[s] = kept
    obs, pairvals, pairs = mean_pairwise(seqs)
    # null distributions
    null_a_vals = np.array([null_A(per_verse_by_surah, atoms, anchor, rng) for _ in range(N_NULL)])
    null_b_vals = np.array([null_B(seqs, rng) for _ in range(N_NULL)])
    p_a = (1 + int(np.sum(null_a_vals >= obs))) / (1 + N_NULL)
    p_b = (1 + int(np.sum(null_b_vals >= obs))) / (1 + N_NULL)
    return {
        "name": name,
        "surahs": surahs,
        "seqs": seqs,
        "observed_mean_sim": obs,
        "pair_vals": list(zip(pairs, pairvals)),
        "null_A_mean": float(null_a_vals.mean()),
        "null_A_sd": float(null_a_vals.std()),
        "null_A_q975": float(np.quantile(null_a_vals, 0.975)),
        "null_B_mean": float(null_b_vals.mean()),
        "null_B_sd": float(null_b_vals.std()),
        "p_A": p_a,
        "p_B": p_b,
    }


def main():
    quran = load_quran()
    rng = np.random.default_rng(SEED)

    moses = run_cycle(
        "Moses",
        [7, 10, 11, 20, 26, 28, 79],
        MOSES_ATOMS,
        "MU",
        quran,
        rng,
    )
    abraham = run_cycle(
        "Abraham",
        [14, 19, 21, 26, 37],
        ABRAHAM_ATOMS,
        "IB",
        quran,
        rng,
    )

    # decision rule, bonferroni k=2
    alpha = 0.025
    def verdict(r):
        sig = r["p_A"] < alpha
        strong = sig and r["observed_mean_sim"] >= 0.50
        mod = sig and r["observed_mean_sim"] >= 0.40
        if strong:
            return "STRONG"
        if mod:
            return "MODERATE"
        if sig:
            return "SIGNIFICANT_BUT_WEAK_EFFECT"
        return "NULL"
    moses["verdict"] = verdict(moses)
    abraham["verdict"] = verdict(abraham)

    # write TSVs
    def dump_seqs(r, fname):
        lines = ["surah\tlen\tsequence"]
        for s, seq in r["seqs"].items():
            lines.append(f"{s}\t{len(seq)}\t{' '.join(seq)}")
        (OUTDIR / fname).write_text("\n".join(lines) + "\n", encoding="utf-8")

    dump_seqs(moses, "moses_sequences.tsv")
    dump_seqs(abraham, "abraham_sequences.tsv")

    def dump_pairs(r, fname):
        lines = ["surah_a\tsurah_b\tsim"]
        for (a, b), v in r["pair_vals"]:
            lines.append(f"{a}\t{b}\t{v:.4f}")
        (OUTDIR / fname).write_text("\n".join(lines) + "\n", encoding="utf-8")

    dump_pairs(moses, "moses_pairwise_sim.tsv")
    dump_pairs(abraham, "abraham_pairwise_sim.tsv")

    report = {
        k: v for k, v in moses.items() if k not in ("seqs", "pair_vals")
    }
    report2 = {
        k: v for k, v in abraham.items() if k not in ("seqs", "pair_vals")
    }
    (OUTDIR / "summary.json").write_text(
        json.dumps({"moses": report, "abraham": report2, "seed": SEED, "n_null": N_NULL}, indent=2, default=str),
        encoding="utf-8",
    )

    # print human summary
    def show(r):
        print(f"\n=== {r['name']} cycle (surahs {r['surahs']}) verdict={r['verdict']} ===")
        print(f"observed mean pairwise sim = {r['observed_mean_sim']:.4f}")
        print(f"Null A mean/sd/q97.5       = {r['null_A_mean']:.4f} / {r['null_A_sd']:.4f} / {r['null_A_q975']:.4f}")
        print(f"Null B mean/sd             = {r['null_B_mean']:.4f} / {r['null_B_sd']:.4f}")
        print(f"p_A = {r['p_A']:.4f}  p_B = {r['p_B']:.4f}  (bonferroni α = 0.025)")
        print("  sequences:")
        for s, seq in r["seqs"].items():
            print(f"    Q{s:<3d} ({len(seq):3d}): {' '.join(seq) if seq else '(empty)'}")
        print("  pairwise sim:")
        for (a, b), v in r["pair_vals"]:
            print(f"    {a}↔{b}: {v:.3f}")

    show(moses)
    show(abraham)


if __name__ == "__main__":
    main()
