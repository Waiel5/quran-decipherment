#!/usr/bin/env python3
"""
H-NEW-1740 — COMPLETE 29-surah al-Khalifa muqaṭṭāʿat-letter audit.

For each of the 29 muqaṭṭāʿat-bearing surahs in the Hafs-Kūfan canonical mushaf,
count the named muqaṭṭaʿ letter(s) and test divisibility by 19.

Rules-tuple:
  (no-tashkeel, orthographic-token, graphemes,
   basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)

Outputs JSON to findings/phase-b-hypotheses/csv/h-new-1740.json
"""

import hashlib
import json
import random
import sys
from pathlib import Path

PRE_REG_PATH = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/"
    "prereg-h-new-1740-khalifa-muqattaat-complete-audit.md"
)
EXPECTED_SHA = "5aae04c37cdb05742df2c78e292c89f98a6aede3068700f64cdd655a236b0516"

QURAN_PATH = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
OUT_PATH = Path(
    "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-1740.json"
)

SEED = 20260509
N_PERMS = 10000


def verify_prereg_sha():
    """Fail-fast SHA check on the pre-reg file."""
    h = hashlib.sha256(PRE_REG_PATH.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH:\n  expected: {EXPECTED_SHA}\n  observed: {h}\n"
        )
        sys.exit(1)
    return h


# 29-surah catalogue (LOCKED).
# (surah_id_1based, label, [strict_letters], [folded_alif_letters_if_any])
# folded_alif version differs only when ا is one of the named letters.
CATALOGUE = [
    (2,  "Q 2 الم",       ["ا", "ل", "م"]),
    (3,  "Q 3 الم",       ["ا", "ل", "م"]),
    (7,  "Q 7 المص",      ["ا", "ل", "م", "ص"]),
    (10, "Q 10 الر",      ["ا", "ل", "ر"]),
    (11, "Q 11 الر",      ["ا", "ل", "ر"]),
    (12, "Q 12 الر",      ["ا", "ل", "ر"]),
    (13, "Q 13 المر",     ["ا", "ل", "م", "ر"]),
    (14, "Q 14 الر",      ["ا", "ل", "ر"]),
    (15, "Q 15 الر",      ["ا", "ل", "ر"]),
    (19, "Q 19 كهيعص",    ["ك", "ه", "ي", "ع", "ص"]),
    (20, "Q 20 طه",       ["ط", "ه"]),
    (26, "Q 26 طسم",      ["ط", "س", "م"]),
    (27, "Q 27 طس",       ["ط", "س"]),
    (28, "Q 28 طسم",      ["ط", "س", "م"]),
    (29, "Q 29 الم",      ["ا", "ل", "م"]),
    (30, "Q 30 الم",      ["ا", "ل", "م"]),
    (31, "Q 31 الم",      ["ا", "ل", "م"]),
    (32, "Q 32 الم",      ["ا", "ل", "م"]),
    (36, "Q 36 يس",       ["ي", "س"]),
    (38, "Q 38 ص",        ["ص"]),
    (40, "Q 40 حم",       ["ح", "م"]),
    (41, "Q 41 حم",       ["ح", "م"]),
    (42, "Q 42 حم عسق",   ["ح", "م", "ع", "س", "ق"]),
    (43, "Q 43 حم",       ["ح", "م"]),
    (44, "Q 44 حم",       ["ح", "م"]),
    (45, "Q 45 حم",       ["ح", "م"]),
    (46, "Q 46 حم",       ["ح", "م"]),
    (50, "Q 50 ق",        ["ق"]),
    (68, "Q 68 ن",        ["ن"]),
]

ALIF_FOLDED = {"ا", "أ", "إ", "آ", "ٱ"}


def load_quran():
    with QURAN_PATH.open() as f:
        return json.load(f)


def surah_letters(surah, fold_alif=False):
    """Return list of letters (no whitespace) for a surah."""
    txt = "".join(v["text"] for v in surah["verses"])
    txt = txt.replace(" ", "")
    if fold_alif:
        return "".join("ا" if c in ALIF_FOLDED else c for c in txt)
    return txt


def count_letters(text, letters):
    s = set(letters)
    n = 0
    for c in text:
        if c in s:
            n += 1
    return n


def main():
    sha = verify_prereg_sha()

    quran = load_quran()
    by_id = {s["id"]: s for s in quran}

    # ----------------------------------------------------------------
    # Primary 29-surah audit
    # ----------------------------------------------------------------
    rows = []
    hits_strict = 0
    hits_folded = 0
    for surah_id, label, letters in CATALOGUE:
        s = by_id[surah_id]
        text_strict = surah_letters(s, fold_alif=False)
        text_folded = surah_letters(s, fold_alif=True)
        c_strict = count_letters(text_strict, letters)
        # for folded, replace ا in the named-letter set if it's present
        if "ا" in letters:
            folded_letters = ["ا" if x == "ا" else x for x in letters]
        else:
            folded_letters = letters
        c_folded = count_letters(text_folded, folded_letters)
        mod_strict = c_strict % 19
        mod_folded = c_folded % 19
        is_hit_strict = (mod_strict == 0)
        is_hit_folded = (mod_folded == 0)
        if is_hit_strict:
            hits_strict += 1
        if is_hit_folded:
            hits_folded += 1
        rows.append({
            "surah_id": surah_id,
            "label": label,
            "letters_named": letters,
            "n_chars_no_space": len(text_strict),
            "count_strict": c_strict,
            "mod19_strict": mod_strict,
            "hit_strict": is_hit_strict,
            "count_folded_alif": c_folded,
            "mod19_folded": mod_folded,
            "hit_folded_alif": is_hit_folded,
        })

    # ----------------------------------------------------------------
    # Permutation null: redraw each surah's letter-positions from
    # corpus-wide letter-frequency distribution, scaled to the surah's
    # total letter-count. Recompute hit-count. 10,000 perms.
    # ----------------------------------------------------------------
    # Build corpus letter-frequency distribution (no-tashkeel, no-space).
    corpus_text = "".join(
        surah_letters(by_id[i + 1], fold_alif=False) for i in range(114)
    )
    from collections import Counter
    corp_freq = Counter(corpus_text)
    alphabet = list(corp_freq.keys())
    weights = [corp_freq[c] for c in alphabet]
    total = sum(weights)
    probs = [w / total for w in weights]

    # cumulative for inverse-CDF sampling
    cum = []
    s_acc = 0.0
    for p in probs:
        s_acc += p
        cum.append(s_acc)

    rng = random.Random(SEED)

    def perm_count_letter_in_n(letter_set, n):
        # P(any letter in letter_set) under corp_freq:
        p_named = sum(probs[i] for i, c in enumerate(alphabet) if c in letter_set)
        # n is letter-budget; sample n letters; count fraction in letter_set
        # For efficiency use binomial sampling
        # via random.Random — use sum of Bernoulli over n trials? for n up to 60k this is slow
        # Use a direct binomial via normal approximation? but we want exact under perm null.
        # Use n trials of random.random() < p_named
        # For speed use builtin random.choices
        # But we just need a count: use random.gauss approximation? no — use binomial directly via random
        return _binomial(rng, n, p_named)

    def _binomial(rng, n, p):
        # for moderate n (up to ~60k), repeated sampling is OK if vectorized
        # using inverse method via rng.random() loop
        if p <= 0:
            return 0
        if p >= 1:
            return n
        # Fast: use sum of Bernoulli? slow for n=60k * 29 * 10000 perms
        # Use normal approximation with continuity correction? lose exactness.
        # Compromise: use rng.binomialvariate if available (Python 3.12+).
        try:
            return rng.binomialvariate(n, p)
        except AttributeError:
            pass
        # Inverse-CDF for small n; for large n use normal approx with cc.
        if n <= 200:
            k = 0
            for _ in range(n):
                if rng.random() < p:
                    k += 1
            return k
        # Normal approx with continuity-correction (acceptable for large n).
        import math
        mu = n * p
        sigma = math.sqrt(n * p * (1 - p))
        z = rng.gauss(0.0, 1.0)
        k = int(round(mu + sigma * z))
        if k < 0:
            k = 0
        if k > n:
            k = n
        return k

    # Precompute per-surah named-letter probability mass
    perm_hits_distribution = [0] * 30  # k can be 0..29
    perm_p_letter = []
    for (sid, _lab, letters) in CATALOGUE:
        p_named = sum(probs[i] for i, c in enumerate(alphabet) if c in set(letters))
        perm_p_letter.append((sid, p_named, len(surah_letters(by_id[sid], False))))

    for _ in range(N_PERMS):
        k = 0
        for (sid, p_named, n_chars) in perm_p_letter:
            c = _binomial(rng, n_chars, p_named)
            if c % 19 == 0:
                k += 1
        perm_hits_distribution[k] += 1

    # Permutation p-value: P(k_perm >= k_obs)
    p_perm = sum(perm_hits_distribution[k] for k in range(hits_strict, 30)) / N_PERMS
    p_perm_folded = None  # not computed under perm null; null structure same

    # ----------------------------------------------------------------
    # Compound counts (Section 6.1 of pre-reg)
    # ----------------------------------------------------------------
    families = []

    def family(name, surah_ids, letters):
        total = 0
        per = []
        for sid in surah_ids:
            t = surah_letters(by_id[sid], fold_alif=False)
            n = count_letters(t, letters)
            per.append({"surah_id": sid, "count": n})
            total += n
        families.append({
            "family": name,
            "surahs": surah_ids,
            "letters": letters,
            "per_surah": per,
            "total": total,
            "mod19": total % 19,
            "hit": (total % 19) == 0,
            "khalifa_claim_if_known": None,
        })

    family("الم-family (Q 2,3,29,30,31,32)", [2,3,29,30,31,32], ["ا","ل","م"])
    family("المص (Q 7 alone)", [7], ["ا","ل","م","ص"])
    family("الر-family (Q 10,11,12,14,15)", [10,11,12,14,15], ["ا","ل","ر"])
    family("المر (Q 13 alone)", [13], ["ا","ل","م","ر"])
    family("كهيعص (Q 19 alone)", [19], ["ك","ه","ي","ع","ص"])
    family("طه (Q 20 alone)", [20], ["ط","ه"])
    family("طسم-family (Q 26,28)", [26,28], ["ط","س","م"])
    family("طس (Q 27 alone)", [27], ["ط","س"])
    family("يس (Q 36 alone)", [36], ["ي","س"])
    family("ص (Q 38 alone)", [38], ["ص"])
    family("ص-combined (Q 7,19,38)", [7,19,38], ["ص"])
    family("حم-family (Q 40-46)", [40,41,42,43,44,45,46], ["ح","م"])
    family("حم عسق (Q 42 alone)", [42], ["ح","م","ع","س","ق"])
    family("ق (Q 50 alone)", [50], ["ق"])
    family("ن (Q 68 alone)", [68], ["ن"])

    family_hits = sum(1 for f in families if f["hit"])

    # ----------------------------------------------------------------
    # Residue distribution across 29 sub-claims
    # ----------------------------------------------------------------
    residue_dist = [0] * 19
    for r in rows:
        residue_dist[r["mod19_strict"]] += 1

    # ----------------------------------------------------------------
    # Decision rule
    # ----------------------------------------------------------------
    if hits_strict >= 5:
        verdict = "PATTERN"
    elif hits_strict >= 3:
        verdict = "AMBIGUOUS"
    else:
        verdict = "NULL"

    out = {
        "finding_id": "H-NEW-1740",
        "pre_reg_sha": sha,
        "seed": SEED,
        "n_perms": N_PERMS,
        "rules_tuple": ("no-tashkeel, orthographic-token, graphemes, "
                        "basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi"),
        "n_sub_claims": len(CATALOGUE),
        "expected_under_uniform_null": len(CATALOGUE) / 19.0,
        "observed_hits_strict": hits_strict,
        "observed_hits_folded_alif": hits_folded,
        "permutation_p_value_strict": p_perm,
        "perm_hits_distribution": perm_hits_distribution,
        "residue_distribution_strict": residue_dist,
        "decision_thresholds": {"PATTERN": ">=5", "AMBIGUOUS": "3-4", "NULL": "<=2"},
        "verdict": verdict,
        "rows": rows,
        "compound_families": families,
        "family_hits": family_hits,
        "notes": [
            "Permutation null draws each surah's letters from corpus-wide letter-frequency "
            "distribution; surah length is preserved.",
            "Folded-alif column is a sensitivity check; PRIMARY verdict uses strict-grapheme.",
            "Compound counts are DESCRIPTIVE; NOT part of the primary 29-surah hit count.",
        ],
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    # Print summary to stdout
    print(f"PRE-REG SHA verified: {sha}")
    print(f"Observed hits (strict): {hits_strict}/{len(CATALOGUE)}")
    print(f"Observed hits (folded alif): {hits_folded}/{len(CATALOGUE)}")
    print(f"Expected under uniform null: {len(CATALOGUE)/19:.3f}")
    print(f"Permutation p-value (k_perm >= k_obs): {p_perm:.4f}")
    print(f"Verdict: {verdict}")
    print()
    print("Per-surah breakdown (strict):")
    print(f"  {'#':>3} {'surah':<18} {'letters':<18} {'count':>6} {'mod19':>6} {'hit':>4}")
    for i, r in enumerate(rows, start=1):
        print(f"  {i:>3} {r['label']:<18} {''.join(r['letters_named']):<18} "
              f"{r['count_strict']:>6} {r['mod19_strict']:>6} {'YES' if r['hit_strict'] else '':>4}")
    print()
    print(f"Compound family hits: {family_hits}/{len(families)}")
    for f in families:
        marker = "HIT" if f["hit"] else ""
        print(f"  {f['family']:<40} total={f['total']:>6} mod19={f['mod19']:>3} {marker}")

    print()
    print(f"Output: {OUT_PATH}")


if __name__ == "__main__":
    main()
