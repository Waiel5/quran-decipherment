#!/usr/bin/env python3
"""Q073-F-01 — Q 73:20 ↔ Q 96:1+3 IMPV-qrA prophetic-revelation pair (verse-twin test).

Pre-reg: surahs/Q073-al-muzzammil/Q073-F-01-iqra-pair-q96-prereg.md
Pre-reg SHA256: a477010077cd15340b209ba24e73b1a666de95cb410215e0963b696d41b3e2b0
Rules-tuple: (no-tashkeel, char-Levenshtein for sim, regex tokens for co-occurrence, basmala-counted-only-in-Q1, Hafs-Kufan)
"""
import json, re, hashlib, sys, os, random
from difflib import SequenceMatcher

PREREG = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/Q073-F-01-iqra-pair-q96-prereg.md'
EXPECTED_SHA = 'a477010077cd15340b209ba24e73b1a666de95cb410215e0963b696d41b3e2b0'
SEED = 20260509
N_PERM = 10000

QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q073-al-muzzammil/csv/Q073-F-01.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def char_sim(a, b):
    """Character-level similarity using SequenceMatcher (Levenshtein-style ratio)."""
    return SequenceMatcher(None, a, b).ratio()


def main():
    verify_sha()
    quran = json.load(open(QURAN_PATH))

    # Flatten verses with (surah_id, ayah_id, text)
    verses = []
    for s in quran:
        for v in s['verses']:
            verses.append({'sid': s['id'], 'aid': v['id'], 'text': v['text']})

    # Locate the 3 reference verses
    by_key = {(v['sid'], v['aid']): v['text'] for v in verses}
    text_q73_20 = by_key[(73, 20)]
    text_q96_1 = by_key[(96, 1)]
    text_q96_3 = by_key[(96, 3)]

    # === Class A regex: IMPV qrA — match اقرء / اقرأ at start of word, with optional fa-/wa- prefix ===
    iqraa_pat = re.compile(r'(?:^|\s)(?:ف|و)?ا?قر[ءأؤا]')

    # === Class B: qurʾān-or-kitāb stem ===
    qurankitab_pat = re.compile(r'قرءان|قرآن|كتاب|كتب')  # broad (also picks up جا verb-forms but rare)

    # === Class C: addressee-marker ===
    addressee_pat = re.compile(r'يا أيها|إنك|أنك|عليك|إليك|لك\s+(?:في|من)|ربك|نفسك|كتابك|قلبك')

    # 2MS-strict (sensitivity check): must have explicit 2MS marker (ك-suffix on noun, or vocative-singular)
    addressee_2ms_pat = re.compile(r'يا أيها|إنك|أنك|ربك|نفسك|كتابك')

    def class_score(text, strict=False):
        a = bool(iqraa_pat.search(text))
        b = bool(qurankitab_pat.search(text))
        if strict:
            c = bool(addressee_2ms_pat.search(text))
        else:
            c = bool(addressee_pat.search(text))
        return (a, b, c)

    pair_texts = {'Q 73:20': text_q73_20, 'Q 96:1': text_q96_1, 'Q 96:3': text_q96_3}
    co_pair_results = {}
    for label, txt in pair_texts.items():
        s_lib = class_score(txt, strict=False)
        s_strict = class_score(txt, strict=True)
        n_lib = sum(s_lib)
        n_strict = sum(s_strict)
        co_pair_results[label] = {
            'A_iqraa': bool(s_lib[0]),
            'B_qurankitab': bool(s_lib[1]),
            'C_addressee_lib': bool(s_lib[2]),
            'C_addressee_2ms_strict': bool(s_strict[2]),
            'score_lib': int(n_lib),
            'score_strict': int(n_strict),
            'word_count': len(txt.split()),
            'char_count': len(txt),
        }

    # H1a co-occurrence test: cluster-score = sum(score_lib) / 3 (max=9 if all 3 verses get all 3 classes)
    cluster_score_lib = sum(d['score_lib'] for d in co_pair_results.values())  # max 9
    cluster_score_strict = sum(d['score_strict'] for d in co_pair_results.values())

    # Length-matched permutation null
    rng = random.Random(SEED)

    # Length-band-matched draw: each null sample = 3 verses with word-counts in ±25% of (w1, w2, w3)
    target_wcs = [d['word_count'] for d in co_pair_results.values()]

    def in_band(wc, target):
        lo, hi = target * 0.75, target * 1.25
        return lo <= wc <= hi

    # bucket verses by word-count band membership for each target
    bands = []
    for tw in target_wcs:
        band = [v for v in verses if in_band(len(v['text'].split()), tw)]
        bands.append(band)

    null_scores = []
    for _ in range(N_PERM):
        sample_score = 0
        for band in bands:
            v = rng.choice(band)
            sample_score += sum(class_score(v['text'], strict=False))
        null_scores.append(sample_score)

    p_co_lib = sum(1 for s in null_scores if s >= cluster_score_lib) / N_PERM

    # Repeat for strict
    null_scores_strict = []
    rng = random.Random(SEED)
    for _ in range(N_PERM):
        sample_score = 0
        for band in bands:
            v = rng.choice(band)
            sample_score += sum(class_score(v['text'], strict=True))
        null_scores_strict.append(sample_score)
    p_co_strict = sum(1 for s in null_scores_strict if s >= cluster_score_strict) / N_PERM

    # === H1b: verse-twin similarity ===
    sim_q73_q96_1 = char_sim(text_q73_20, text_q96_1)
    sim_q73_q96_3 = char_sim(text_q73_20, text_q96_3)
    sim_max = max(sim_q73_q96_1, sim_q73_q96_3)

    # Q 73:20 vs all corpus verses similarities
    all_sims = []
    for v in verses:
        if v['sid'] == 73 and v['aid'] == 20:
            continue
        s = char_sim(text_q73_20, v['text'])
        all_sims.append(((v['sid'], v['aid']), s))

    all_sims.sort(key=lambda x: -x[1])
    n_above_q96_1 = sum(1 for ref, s in all_sims if s > sim_q73_q96_1)
    n_above_q96_3 = sum(1 for ref, s in all_sims if s > sim_q73_q96_3)
    n_total = len(all_sims)

    pct_q96_1 = n_above_q96_1 / n_total
    pct_q96_3 = n_above_q96_3 / n_total
    pct_min = min(pct_q96_1, pct_q96_3)
    rank_q96_1 = n_above_q96_1 + 1
    rank_q96_3 = n_above_q96_3 + 1

    # === Verdict ===
    h1a_pass_lib = (p_co_lib <= 0.025)
    h1a_pass_strict = (p_co_strict <= 0.025)
    h1b_pass = (pct_min <= 0.05)

    n_pass = (1 if h1a_pass_lib else 0) + (1 if h1b_pass else 0)
    if n_pass == 2:
        verdict = "CONFIRMED"
    elif n_pass == 1:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    # If observed direction reversed, flag pre-commit-violation
    null_mean = sum(null_scores) / N_PERM
    if cluster_score_lib < null_mean:
        verdict += " (pre-commit-violation: direction-reversed)"

    out = {
        "test_id": "Q073-F-01",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "pair_verses": co_pair_results,
        "cluster_score_lib": int(cluster_score_lib),
        "cluster_score_strict": int(cluster_score_strict),
        "null_lib": {
            "mean": null_mean,
            "min": min(null_scores),
            "max": max(null_scores),
            "p_one_sided_geq": p_co_lib,
        },
        "null_strict": {
            "mean": sum(null_scores_strict) / N_PERM,
            "p_one_sided_geq": p_co_strict,
        },
        "h1a_co_occurrence_pass": h1a_pass_lib,
        "h1a_co_occurrence_pass_strict": h1a_pass_strict,
        "verse_twin_sim": {
            "Q73_20_vs_Q96_1": sim_q73_q96_1,
            "Q73_20_vs_Q96_3": sim_q73_q96_3,
            "max_sim": sim_max,
            "rank_Q96_1_in_Q73_20_neighbors": rank_q96_1,
            "rank_Q96_3_in_Q73_20_neighbors": rank_q96_3,
            "pct_min": pct_min,
            "n_total_compared": n_total,
        },
        "h1b_pass": h1b_pass,
        "n_pass_axes": n_pass,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Verdict: {verdict}")
    print(f"  cluster_score_lib = {cluster_score_lib} / 9; null_mean = {null_mean:.3f}; p = {p_co_lib:.4f}")
    print(f"  H1b: max_sim = {sim_max:.4f}; pct_min = {pct_min:.4f}; rank_Q96_1 = {rank_q96_1}; rank_Q96_3 = {rank_q96_3}")
    print(f"Written to: {OUT_PATH}")


if __name__ == '__main__':
    main()
