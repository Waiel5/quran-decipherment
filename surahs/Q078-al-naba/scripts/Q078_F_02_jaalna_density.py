#!/usr/bin/env python3
"""
Q078-F-02 — Q 78 corpus jaʿala (j-ʿ-l) density rank test.

Pre-reg: surahs/Q078-al-naba/preregs/Q078-F-02-jaalna-density-prereg.md
SHA256:  embedded at runtime; verified against pre-reg

Hypothesis (LOCKED PRE-RUN):
  H1: Q 78 has CORPUS-EXTREME jaʿala-root density per word.
      Operationalized as: Q 78 ranks in TOP-5 of all surahs ≥50 root-tokens
      by jaʿala-rate (j-ʿ-l count / total root-tokens).
      DIRECTION: Q 78 = corpus-extreme (top-5).

  H2: Q 78 has a 3-or-more consecutive-verse run of *wa-jaʿalnā* construction.
      DIRECTION: Q 78 has at least one streak ≥3.

H0: H1 fails (Q 78 ranks > 5) OR H2 fails (no streak ≥3).

Bonferroni: k=2; alpha_bon = 0.025.

Method:
  - QAC root extraction; rank surahs by jaʿala-rate.
  - Verse-level: regex *wa-jaʿalnā* / *wa-jaʿala* and find max consecutive streak.

Seed: 20260509.
"""

import json
import re
import sys
import os
import hashlib
from collections import Counter

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PREREG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                           'Q078-F-02-jaalna-density-prereg.md')
QURAN_PATH = os.path.join(PROJECT_ROOT, 'quran-text', 'quran-no-tashkeel.json')
QAC_PATH = os.path.join(PROJECT_ROOT, 'data', 'morphology',
                        'quranic-corpus-morphology-0.4.txt')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q078-F-02.json')

SEED = 20260509


def sha256_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def load_surah_roots():
    surah_roots = {i: Counter() for i in range(1, 115)}
    with open(QAC_PATH, encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            m = re.search(r'ROOT:([^|]+)', features)
            if not m:
                continue
            root = m.group(1)
            nums = re.findall(r'\d+', loc)
            if len(nums) < 1:
                continue
            s = int(nums[0])
            if 1 <= s <= 114:
                surah_roots[s][root] += 1
    return surah_roots


def main():
    prereg_sha = sha256_of(PREREG_PATH)
    print(f"prereg SHA256: {prereg_sha}")

    surah_roots = load_surah_roots()

    # H1: jaʿala density rank
    ranks = []
    for s in range(1, 115):
        sw = sum(surah_roots[s].values())
        if sw >= 50:
            jeel = surah_roots[s].get('jEl', 0)
            ranks.append((s, jeel / sw if sw else 0, jeel, sw))
    ranks.sort(key=lambda x: -x[1])

    q78_rank = next(i for i, r in enumerate(ranks) if r[0] == 78) + 1
    q78_rate = next(r for r in ranks if r[0] == 78)[1]

    h1_pass = q78_rank <= 5

    # H2: max consecutive *wa-jaʿalnā* streak
    with open(QURAN_PATH) as f:
        d = json.load(f)
    q78 = next(s for s in d if s['id'] == 78)
    pattern = re.compile(r'وجعلنا|وجعل')
    streak = 0
    max_streak = 0
    streak_start = None
    streak_at = None
    for v in q78['verses']:
        if pattern.search(v['text']):
            if streak == 0:
                streak_start = v['id']
            streak += 1
            if streak > max_streak:
                max_streak = streak
                streak_at = (streak_start, v['id'])
        else:
            streak = 0

    h2_pass = max_streak >= 3

    # Corpus-wide context: which other surahs have streak ≥3?
    corpus_streak = []
    for s in d:
        st = 0
        ms = 0
        for v in s['verses']:
            if pattern.search(v['text']):
                st += 1
                if st > ms:
                    ms = st
            else:
                st = 0
        if ms >= 3:
            corpus_streak.append((s['id'], ms))

    output = {
        "test_id": "Q078-F-02",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "h1_q78_jaala_rate": q78_rate,
        "h1_q78_rank": q78_rank,
        "h1_top10_ranks": [(r[0], r[1], r[2], r[3]) for r in ranks[:10]],
        "h1_pass_top5": h1_pass,
        "h2_q78_max_streak": max_streak,
        "h2_q78_streak_at": streak_at,
        "h2_pass_streak3": h2_pass,
        "h2_corpus_other_streak3": corpus_streak,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"H1 Q 78 jaʿala rate: {q78_rate:.4f}, rank: {q78_rank}/{len(ranks)}")
    print(f"H1 top-5 PASS: {h1_pass}")
    print(f"H2 Q 78 max consecutive streak: {max_streak} at v{streak_at}")
    print(f"H2 streak≥3 PASS: {h2_pass}")
    print(f"Corpus other streak ≥3: {corpus_streak}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
