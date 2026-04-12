"""Phase B gematria landscape analysis.

Computes per-surah and per-verse abjad totals, runs a battery of
anomaly scans, writes CSVs, and returns a result dict that the
markdown-writer step consumes.

Rules tuple for all sums below:
    orthography:      no-tashkeel
    word_definition:  not-applicable (letter-level gematria)
    letter_definition: graphemes (no shadda doubling; no
                       hamza-distinct since no-tashkeel already
                       collapses tashkeel; hamza carriers on alif/waw/ya
                       are silently skipped per analysis.tools.gematria)
    basmala_policy:   counted-only-in-surah-1 (as stored in JSON)
    verse_numbering:  hafs-kufan
    abjad_table:      mashriqi  (primary)   +  maghribi (contrast)
    null_model:       (§1.5 permutation of surah indices for ordering
                       claims; §1.3 letter-level Markov for sum claims
                       when a specific cell is promoted)
"""

from __future__ import annotations

import csv
import json
import math
import os
import statistics
import sys
from collections import Counter
from typing import Dict, List, Tuple

sys.path.insert(0, "/Users/grey/Downloads/quran")
from analysis.tools.gematria import text_value, word_value, ABJAD_MASHRIQI
from analysis.tools.loader import load_quran


# -------------------------------------------------------------------
# Output paths
# -------------------------------------------------------------------
OUT_DIR = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses"
SURAH_CSV = os.path.join(OUT_DIR, "gematria-surah-totals.csv")
VERSE_CSV = os.path.join(OUT_DIR, "gematria-verse-totals.csv")


# -------------------------------------------------------------------
# Helpers
# -------------------------------------------------------------------
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def count_letters(text: str) -> int:
    """Count letters that contribute to the abjad sum (table-present)."""
    return sum(1 for ch in text if ch in ABJAD_MASHRIQI)


def is_palindrome_digits(n: int) -> bool:
    s = str(n)
    return s == s[::-1] and len(s) >= 2


def binomial_tail_ge(n: int, k: int, p: float) -> float:
    """Upper-tail binomial P(X >= k) with n trials, success prob p."""
    if k <= 0:
        return 1.0
    from math import comb
    total = 0.0
    for i in range(k, n + 1):
        total += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total


def binomial_tail_le(n: int, k: int, p: float) -> float:
    if k >= n:
        return 1.0
    from math import comb
    total = 0.0
    for i in range(0, k + 1):
        total += comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    return total


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------
def main() -> Dict:
    surahs = load_quran("no-tashkeel")
    assert len(surahs) == 114

    # Anchor sanity: bismillah = 786 mashriqi
    bism = "بسم الله الرحمن الرحيم"
    assert text_value(bism, "mashriqi") == 786, "FATAL: basmala anchor failed"
    maghribi_basmala = text_value(bism, "maghribi")
    print(f"[anchor] bismillah mashriqi=786 OK; maghribi={maghribi_basmala}")

    # ---------- Per-surah and per-verse totals ----------
    surah_rows: List[Dict] = []
    verse_rows: List[Dict] = []
    n_verses_total = 0
    total_abjad_all = 0

    for s in surahs:
        s_letters = 0
        s_abjad = 0
        for v in s.verses:
            text = v.text
            ab = text_value(text, "mashriqi")
            letters = count_letters(text)
            verse_rows.append(
                {
                    "surah_id": s.id,
                    "verse_id": v.id,
                    "n_letters": letters,
                    "abjad_total": ab,
                    "text": text,
                }
            )
            s_abjad += ab
            s_letters += letters
        surah_rows.append(
            {
                "surah_id": s.id,
                "name": s.name,
                "transliteration": s.transliteration,
                "n_verses": len(s.verses),
                "n_letters": s_letters,
                "abjad_total": s_abjad,
                "abjad_per_letter": s_abjad / s_letters if s_letters else 0.0,
            }
        )
        n_verses_total += len(s.verses)
        total_abjad_all += s_abjad

    assert n_verses_total == 6236, f"verse count wrong: {n_verses_total}"

    # ---------- Save CSVs ----------
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(SURAH_CSV, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "surah_id",
                "name",
                "transliteration",
                "n_verses",
                "n_letters",
                "abjad_total",
                "abjad_per_letter",
            ],
        )
        w.writeheader()
        for r in surah_rows:
            w.writerow(r)

    with open(VERSE_CSV, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["surah_id", "verse_id", "n_letters", "abjad_total", "text"],
        )
        w.writeheader()
        for r in verse_rows:
            w.writerow(r)

    # ---------- Anomaly scans — surah level ----------
    prime_surahs = [r for r in surah_rows if is_prime(r["abjad_total"])]
    mod19_surahs = [r for r in surah_rows if r["abjad_total"] % 19 == 0]
    near_19_plus = [r for r in surah_rows if (r["abjad_total"] - 1) % 19 == 0]
    near_19_minus = [r for r in surah_rows if (r["abjad_total"] + 1) % 19 == 0]
    small_multiples: List[Tuple[int, int, int]] = []
    for r in surah_rows:
        sid = r["surah_id"]
        tot = r["abjad_total"]
        for K in range(1, 11):
            if tot == sid * K:
                small_multiples.append((sid, K, tot))

    # Famous Arabic word values (see §6 of methodology)
    FAMOUS = {
        "Allah (الله)": 66,
        "Muhammad (محمد)": 92,
        "Rabb (رب)": 202,
        "Nur (نور)": 256,
        "Rahman (الرحمن)": 329,
        "Rahim (الرحيم)": 289,
        "Qur'an (القرآن)": 352,
        "Kitab (الكتاب)": 454,
        "Iman (الإيمان)": 133,
        "Islam (الإسلام)": 163,
        "Din (الدين)": 95,
        "Hikma (الحكمة)": 78,
        "Haqq (الحق)": 139,
        "Salat (الصلاة)": 126,
        "Zakat (الزكاة)": 64,
        "Sawm (صوم)": 136,
        "Hajj (الحج)": 42,
        "Malik (ملك)": 90,
        "Adam (آدم)": 45,
        "Bismillah (bism allah al-rahman al-rahim)": 786,
    }
    famous_hits: List[Tuple[str, int, int]] = []
    for r in surah_rows:
        for name, val in FAMOUS.items():
            if r["abjad_total"] == val:
                famous_hits.append((name, val, r["surah_id"]))

    # ---------- Verse-level anomaly scans ----------
    verses_abjad_equals_letters = [
        r for r in verse_rows if r["abjad_total"] == r["n_letters"]
    ]
    verses_abjad_equals_product = [
        r for r in verse_rows if r["abjad_total"] == r["surah_id"] * r["verse_id"]
    ]
    verses_palindrome = [
        r for r in verse_rows if is_palindrome_digits(r["abjad_total"])
    ]

    # Arithmetic / geometric word sequences within a verse
    arith_verses: List[Dict] = []
    geom_verses: List[Dict] = []
    for r in verse_rows:
        words = r["text"].split()
        if len(words) < 3:
            continue
        vals = [word_value(w, "mashriqi") for w in words]
        if any(v == 0 for v in vals):
            continue
        diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        if len(set(diffs)) == 1 and diffs[0] != 0:
            arith_verses.append(
                {"surah_id": r["surah_id"], "verse_id": r["verse_id"],
                 "n_words": len(vals), "vals": vals, "diff": diffs[0]}
            )
        ratios = []
        ok = True
        for i in range(len(vals) - 1):
            if vals[i] == 0 or vals[i + 1] % vals[i] != 0:
                ok = False
                break
            ratios.append(vals[i + 1] // vals[i])
        if ok and ratios and len(set(ratios)) == 1 and ratios[0] > 1:
            geom_verses.append(
                {"surah_id": r["surah_id"], "verse_id": r["verse_id"],
                 "n_words": len(vals), "vals": vals, "ratio": ratios[0]}
            )

    max_verse = max(verse_rows, key=lambda r: r["abjad_total"])
    min_verse = min(verse_rows, key=lambda r: r["abjad_total"])
    abjad_counts = Counter(r["abjad_total"] for r in verse_rows)
    most_common_abjad = abjad_counts.most_common(1)[0]
    top10_most_common_abjad = abjad_counts.most_common(10)

    # ---------- Word-value histogram ----------
    word_value_counter: Counter = Counter()
    example_word_by_value: Dict[int, str] = {}
    for r in verse_rows:
        for w in r["text"].split():
            v = word_value(w, "mashriqi")
            word_value_counter[v] += 1
            if v not in example_word_by_value:
                example_word_by_value[v] = w
    top20_word_values = word_value_counter.most_common(20)
    round_hundreds_missing = [
        h for h in range(100, 2001, 100) if word_value_counter.get(h, 0) == 0
    ]
    round_values_present = [
        h for h in range(10, 2001, 10) if word_value_counter.get(h, 0) > 0
    ]
    top10_round_words = sorted(
        [(h, word_value_counter[h], example_word_by_value[h]) for h in round_values_present],
        key=lambda x: x[1],
        reverse=True,
    )[:10]
    total_word_tokens = sum(word_value_counter.values())

    # ---------- Prime-mod hunt ----------
    prime_mod_results: List[Dict] = []
    totals = [r["abjad_total"] for r in surah_rows]
    for p in (7, 11, 13, 17, 19, 23, 29, 31):
        hits = sum(1 for t in totals if t % p == 0)
        expected = 114 / p
        if hits >= expected:
            pv = binomial_tail_ge(114, hits, 1 / p)
        else:
            pv = binomial_tail_le(114, hits, 1 / p)
        prime_mod_results.append(
            {
                "p": p,
                "observed": hits,
                "expected": expected,
                "p_value_one_sided": pv,
                "bonferroni_p": min(1.0, pv * 8),
            }
        )

    # ---------- Surah-name abjad coincidences ----------
    surah_name_hits: List[Dict] = []
    surah_name_values: List[Tuple[int, str, int]] = []
    for s in surahs:
        nm = s.name
        val = text_value(nm, "mashriqi")
        surah_name_values.append((s.id, nm, val))
        hit = {}
        if val == len(s.verses):
            hit["equals_n_verses"] = True
        if val == s.id:
            hit["equals_surah_id"] = True
        if val % 19 == 0:
            hit["divisible_by_19"] = True
        tri = s.id * (s.id + 1) // 2
        if val == tri:
            hit["equals_triangular_of_id"] = True
        if hit:
            hit["surah_id"] = s.id
            hit["name"] = nm
            hit["value"] = val
            surah_name_hits.append(hit)

    # ---------- 114 sequence features ----------
    seq = [r["abjad_total"] for r in surah_rows]
    max_idx = seq.index(max(seq)) + 1
    min_idx = seq.index(min(seq)) + 1

    def longest_monotonic(xs, inc=True):
        best = cur = 1
        best_end = 0
        for i in range(1, len(xs)):
            if (inc and xs[i] > xs[i - 1]) or ((not inc) and xs[i] < xs[i - 1]):
                cur += 1
                if cur > best:
                    best = cur
                    best_end = i
            else:
                cur = 1
        return best, best_end - best + 2, best_end + 1

    longest_inc = longest_monotonic(seq, inc=True)
    longest_dec = longest_monotonic(seq, inc=False)

    def _rank(xs):
        pairs = sorted(range(len(xs)), key=lambda i: xs[i])
        rk = [0] * len(xs)
        for r, idx in enumerate(pairs, 1):
            rk[idx] = r
        return rk

    def _pearson(x, y):
        n = len(x)
        mx = sum(x) / n
        my = sum(y) / n
        num = sum((x[i] - mx) * (y[i] - my) for i in range(n))
        dx = math.sqrt(sum((xi - mx) ** 2 for xi in x))
        dy = math.sqrt(sum((yi - my) ** 2 for yi in y))
        return num / (dx * dy) if dx and dy else 0.0

    rho = _pearson(_rank(list(range(1, 115))), _rank(seq))

    # ---------- Null: permutation test (surah index shuffle) ----------
    import random
    random.seed(20260412)
    N_SHUFFLE = 20000

    obs_div_by_id = sum(1 for r in surah_rows if r["abjad_total"] % r["surah_id"] == 0)
    baseline_div_by_id = 0
    sample_list = []
    for _ in range(N_SHUFFLE):
        perm = list(totals)
        random.shuffle(perm)
        count = sum(1 for i, t in enumerate(perm, 1) if t % i == 0)
        sample_list.append(count)
        if count >= obs_div_by_id:
            baseline_div_by_id += 1
    div_by_id_p = baseline_div_by_id / N_SHUFFLE
    mean_null_div_by_id = statistics.mean(sample_list)

    # For mod19 hits, a shuffle of totals is invariant (number divisible
    # by 19 is preserved). Use analytic binomial null instead.
    pv_mod19 = binomial_tail_ge(114, len(mod19_surahs), 1 / 19)

    # Primeness is also invariant under shuffle. Use expected prime
    # density at that scale.
    # Approximation: P(n is prime) ~ 1/ln(n) for random n near n.
    # Use mean(1/ln(t)) across totals as a very rough expected rate.
    primness_exp = sum(1 / math.log(t) for t in totals if t > 2)
    n_primes = len(prime_surahs)

    result = {
        "anchor": {"mashriqi_basmala": 786, "maghribi_basmala": maghribi_basmala},
        "totals": {
            "n_surahs": 114,
            "n_verses": n_verses_total,
            "grand_total_abjad_mashriqi": total_abjad_all,
            "total_word_tokens": total_word_tokens,
        },
        "surah_rows": surah_rows,
        "verse_rows_count": len(verse_rows),
        "prime_surahs": prime_surahs,
        "prime_surah_expected": primness_exp,
        "mod19_surahs": mod19_surahs,
        "near_19_plus": near_19_plus,
        "near_19_minus": near_19_minus,
        "small_multiples": small_multiples,
        "famous_hits": famous_hits,
        "verses_abjad_equals_letters_count": len(verses_abjad_equals_letters),
        "verses_abjad_equals_letters_sample": verses_abjad_equals_letters[:20],
        "verses_abjad_equals_product": verses_abjad_equals_product,
        "verses_palindrome_count": len(verses_palindrome),
        "verses_palindrome_sample": verses_palindrome[:20],
        "arith_verses_sample": arith_verses[:20],
        "geom_verses_sample": geom_verses[:20],
        "arith_verses_total": len(arith_verses),
        "geom_verses_total": len(geom_verses),
        "max_verse": max_verse,
        "min_verse": min_verse,
        "most_common_abjad": most_common_abjad,
        "top10_most_common_abjad": top10_most_common_abjad,
        "top20_word_values": [
            (v, c, example_word_by_value[v]) for v, c in top20_word_values
        ],
        "round_hundreds_missing": round_hundreds_missing,
        "top10_round_words": top10_round_words,
        "prime_mod_results": prime_mod_results,
        "surah_name_values": surah_name_values,
        "surah_name_hits": surah_name_hits,
        "seq_max_idx": max_idx,
        "seq_max_val": max(seq),
        "seq_min_idx": min_idx,
        "seq_min_val": min(seq),
        "longest_inc": longest_inc,
        "longest_dec": longest_dec,
        "spearman_id_vs_total": rho,
        "div_by_id": {
            "observed": obs_div_by_id,
            "mean_null": mean_null_div_by_id,
            "p_value": div_by_id_p,
            "n_trials": N_SHUFFLE,
        },
        "mod19_test": {
            "observed": len(mod19_surahs),
            "expected": 114 / 19,
            "p_value": pv_mod19,
        },
    }

    return result


if __name__ == "__main__":
    r = main()
    # JSON dump (slim fields only)
    slim = {k: v for k, v in r.items() if k not in ("surah_rows",)}
    # Drop texts from verse samples to keep console legible
    with open("/tmp/gematria_landscape.json", "w", encoding="utf-8") as fh:
        json.dump(slim, fh, default=str, ensure_ascii=False, indent=1)
    print(f"total abjad (mashriqi): {r['totals']['grand_total_abjad_mashriqi']}")
    print(f"prime surah count: {len(r['prime_surahs'])} (expected ~ {r['prime_surah_expected']:.1f})")
    print(f"mod19 surahs: {len(r['mod19_surahs'])} (exp 6.0, p={r['mod19_test']['p_value']:.4f})")
    print(f"near-19 +1: {len(r['near_19_plus'])}; near-19 -1: {len(r['near_19_minus'])}")
    print(f"famous hits: {r['famous_hits']}")
    print(f"small multiples (tot = sid*K, K<=10): {r['small_multiples']}")
    print(f"verses abjad==letters: {r['verses_abjad_equals_letters_count']}")
    print(f"verses abjad==sid*vid: {len(r['verses_abjad_equals_product'])}")
    print(f"verses palindrome: {r['verses_palindrome_count']}")
    print(f"arith verse count: {r['arith_verses_total']}; geom: {r['geom_verses_total']}")
    mv = r['max_verse']
    mv2 = r['min_verse']
    print(f"max verse: S{mv['surah_id']}:{mv['verse_id']} ab={mv['abjad_total']} letters={mv['n_letters']}")
    print(f"min verse: S{mv2['surah_id']}:{mv2['verse_id']} ab={mv2['abjad_total']}")
    print(f"most common abjad (value, count): {r['most_common_abjad']}")
    print(f"top10 most common abjad totals: {r['top10_most_common_abjad']}")
    print(f"top20 word values (first 8): {r['top20_word_values'][:8]}")
    print(f"round hundreds missing: {r['round_hundreds_missing']}")
    print(f"top10 round-value words: {r['top10_round_words']}")
    print(f"seq max idx (surah): {r['seq_max_idx']} val {r['seq_max_val']}; min idx {r['seq_min_idx']} val {r['seq_min_val']}")
    print(f"longest inc run length: {r['longest_inc'][0]}; longest dec run: {r['longest_dec'][0]}")
    print(f"spearman(id, total): {r['spearman_id_vs_total']:.3f}")
    print(f"div by id observed: {r['div_by_id']['observed']} null mean {r['div_by_id']['mean_null']:.2f} p={r['div_by_id']['p_value']:.4f}")
    print("prime-mod results:")
    for pm in r['prime_mod_results']:
        print(f"  p={pm['p']} obs={pm['observed']} exp={pm['expected']:.2f} raw_p={pm['p_value_one_sided']:.4f} bonf={pm['bonferroni_p']:.4f}")
    print(f"surah name hits count: {len(r['surah_name_hits'])}")
    for h in r['surah_name_hits'][:30]:
        print(f"  {h}")
