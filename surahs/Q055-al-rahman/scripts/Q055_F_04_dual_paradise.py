#!/usr/bin/env python3
"""
Q055-F-04 — Dual-paradise structural similarity.

Hypothesis: Q 55 vv. 46-61 (first paradise pair) and vv. 62-77 (second
paradise pair) form parallel descriptions; their normalized token-cosine
should exceed the cosine of either block to a length-matched non-paradise
control region (e.g., vv. 14-29).

Direction-locked: cos(P1, P2) > cos(P1, control) AND cos(P1, P2) > cos(P2, control).
Permutation null: shuffle verse-bag across the surah, recompute, p<0.05.
Both directions must hold.
"""
import json, os, re, unicodedata, random, math
from collections import Counter

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q055-al-rahman/csv/Q055-F-04.json')


def strip_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize_alif(s):
    s = re.sub(r'[إأآٱ]', 'ا', s)
    s = re.sub(r'ءا', 'ا', s)
    s = re.sub(r'ى', 'ي', s)
    return s


def get_q55_verses():
    with open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')) as f:
        data = json.load(f)
    q55 = next(s for s in data if s['id']==55)
    return [(v['id'], normalize_alif(strip_diacritics(v['text'])).strip()) for v in q55['verses']]


def cosine(a, b):
    """a, b are Counter objects."""
    keys = set(a) | set(b)
    dot = sum(a[k]*b[k] for k in keys)
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    if na == 0 or nb == 0: return 0
    return dot / (na * nb)


def block_counter(verses, lo, hi):
    c = Counter()
    for vid, txt in verses:
        if lo <= vid <= hi:
            c.update(txt.split())
    return c


def main():
    print("=== Q055-F-04: Dual-paradise structural similarity ===\n")
    out = {}
    verses = get_q55_verses()

    # Define blocks
    P1 = (46, 61)  # 16 verses
    P2 = (62, 77)  # 16 verses
    # Control: pick a length-matched non-paradise block
    # vv. 14-29 = 16 verses (jinn/mankind creation + judgement)
    CTRL = (14, 29)

    p1 = block_counter(verses, *P1)
    p2 = block_counter(verses, *P2)
    ctrl = block_counter(verses, *CTRL)

    cos_p1p2 = cosine(p1, p2)
    cos_p1c = cosine(p1, ctrl)
    cos_p2c = cosine(p2, ctrl)

    print(f"P1 ({P1[0]}-{P1[1]}) tokens: {sum(p1.values())}, types: {len(p1)}")
    print(f"P2 ({P2[0]}-{P2[1]}) tokens: {sum(p2.values())}, types: {len(p2)}")
    print(f"CTRL ({CTRL[0]}-{CTRL[1]}) tokens: {sum(ctrl.values())}, types: {len(ctrl)}")
    print()
    print(f"cos(P1, P2)   = {cos_p1p2:.4f}")
    print(f"cos(P1, CTRL) = {cos_p1c:.4f}")
    print(f"cos(P2, CTRL) = {cos_p2c:.4f}")
    print()

    # Direction-locked test: cos(P1,P2) > both controls
    direction_pass = cos_p1p2 > cos_p1c and cos_p1p2 > cos_p2c
    print(f"Direction (P1-P2 > both controls): {'PASS' if direction_pass else 'FAIL'}")

    # Permutation null: randomize verse-block assignment, recompute
    # Shuffle the 78 verse-IDs, take first 16 as P1', next 16 as P2', next 16 as CTRL'
    rng = random.Random(20260428)
    n_perm = 10000
    perm_count = 0
    for _ in range(n_perm):
        ids = list(range(1, 79))
        rng.shuffle(ids)
        # Random P1, P2 assignments
        p1_ids = set(ids[:16])
        p2_ids = set(ids[16:32])
        c1 = Counter()
        c2 = Counter()
        for vid, txt in verses:
            if vid in p1_ids: c1.update(txt.split())
            elif vid in p2_ids: c2.update(txt.split())
        cs = cosine(c1, c2)
        if cs >= cos_p1p2:
            perm_count += 1
    perm_p = (perm_count + 1) / (n_perm + 1)
    print(f"Permutation p (P1-P2 cos vs random pair): {perm_p:.4f}")

    # Excerpt of shared tokens between P1 and P2
    shared = sorted(set(p1) & set(p2), key=lambda k: -(p1[k] + p2[k]))[:20]
    print('\nTop shared tokens between P1 and P2:')
    for t in shared:
        print(f"  {t}: P1={p1[t]}, P2={p2[t]}")

    out['blocks'] = {'P1': P1, 'P2': P2, 'CTRL': CTRL}
    out['cos_p1p2'] = cos_p1p2
    out['cos_p1_ctrl'] = cos_p1c
    out['cos_p2_ctrl'] = cos_p2c
    out['direction_pass'] = direction_pass
    out['perm_p_p1p2'] = perm_p
    out['n_perm'] = n_perm
    out['top_shared_tokens'] = [{'token': t, 'p1': p1[t], 'p2': p2[t]} for t in shared]
    out['p1_unique'] = sorted(set(p1) - set(p2))[:30]
    out['p2_unique'] = sorted(set(p2) - set(p1))[:30]

    if direction_pass and perm_p < 0.05:
        out['verdict'] = f'CONFIRMED — P1 ~ P2 (cos={cos_p1p2:.3f}) > controls; perm-p={perm_p:.4f}'
    elif direction_pass:
        out['verdict'] = f'DIRECTIONAL — P1-P2 wins on direction, perm-p={perm_p:.4f}'
    else:
        out['verdict'] = f'NULL — direction failed (cos={cos_p1p2:.3f} vs ctrl={max(cos_p1c, cos_p2c):.3f})'

    print(f"\nVerdict: {out['verdict']}")
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote: {OUT}")


if __name__ == '__main__':
    main()
