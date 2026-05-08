#!/usr/bin/env python3
"""Q037-F-01 — corpus-share of the *salāmun ʿalā [PROPHET-NAME]* construction.

Pre-reg: surahs/Q037-al-saffat/Q037-F-01-salam-ala-prophet-prereg.md
Pre-reg SHA256: 59f7afd2ea1e00d969c03a0ee9db531d28bec3e6eec679e292449b5b6f4d658b
Rules-tuple: (no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, re, hashlib, sys, os, random

PREREG = '/Users/grey/Downloads/quran/surahs/Q037-al-saffat/Q037-F-01-salam-ala-prophet-prereg.md'
EXPECTED_SHA = '59f7afd2ea1e00d969c03a0ee9db531d28bec3e6eec679e292449b5b6f4d658b'
SEED = 20260508
N_PERM = 10000

PROPHET_NAMES = [
    'آدم', 'نوح', 'إدريس', 'هود', 'صالح', 'إبراهيم', 'لوط',
    'إسماعيل', 'إسحاق', 'يعقوب', 'يوسف', 'شعيب',
    'أيوب', 'موسى', 'هارون', 'داوود', 'سليمان',
    'إلياس', 'إل ياسين', 'اليسع', 'يونس', 'زكريا', 'يحيى', 'عيسى', 'محمد',
    'المرسلين',
]


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    salam_pat = re.compile(r'\bسلام على\b')
    instances = []  # list of (sid, vid, text)
    for s in quran:
        for v in s['verses']:
            if salam_pat.search(v['text']):
                instances.append((s['id'], v['id'], v['text']))

    # Filter: addressee must include a named prophet from the list (within same verse).
    valid = []
    for sid, vid, t in instances:
        for name in PROPHET_NAMES:
            if name in t:
                valid.append((sid, vid, t, name))
                break

    n_total = len(valid)
    n_q37 = sum(1 for r in valid if r[0]==37)
    share_q37 = n_q37 / n_total if n_total else 0.0

    # surah word counts for length-weighted null
    surah_words = {s['id']: sum(len(v['text'].split()) for v in s['verses']) for s in quran}
    total_words = sum(surah_words.values())

    rng = random.Random(SEED)
    # Null A: length-weighted
    surah_ids = list(surah_words.keys())
    weights = [surah_words[sid]/total_words for sid in surah_ids]
    cum = []
    c = 0.0
    for w in weights:
        c += w; cum.append(c)
    def draw():
        r = rng.random()
        for i, c in enumerate(cum):
            if r <= c:
                return surah_ids[i]
        return surah_ids[-1]
    null_A_q37 = []
    for _ in range(N_PERM):
        c37 = sum(1 for _ in range(n_total) if draw()==37)
        null_A_q37.append(c37)
    p_A = sum(1 for x in null_A_q37 if x >= n_q37) / N_PERM

    # Null B: uniform-surah
    null_B_q37 = []
    for _ in range(N_PERM):
        c37 = sum(1 for _ in range(n_total) if rng.randint(1,114)==37)
        null_B_q37.append(c37)
    p_B = sum(1 for x in null_B_q37 if x >= n_q37) / N_PERM

    # Verdict
    h1a = n_q37 >= 3
    h1b = share_q37 >= 0.75
    alpha_bon = 0.025
    if h1a and h1b and p_A <= alpha_bon and p_B <= alpha_bon:
        verdict = 'CONFIRMED'
    elif h1a and h1b:
        verdict = 'CONFIRMED-WEAK-NULL'
    elif h1a:
        verdict = 'DIRECTIONAL'
    elif n_q37 == 0:
        verdict = 'PRE-COMMIT-VIOLATION'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q037-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'instances_corpus': [{'surah': r[0], 'verse': r[1], 'text': r[2], 'matched_name': r[3]} for r in valid],
        'all_pre_filter_instances': [{'surah': r[0], 'verse': r[1], 'text': r[2]} for r in instances],
        'n_total': n_total,
        'n_q37': n_q37,
        'share_q37': share_q37,
        'h1a_pass_threshold_3': h1a,
        'h1b_pass_threshold_75pct': h1b,
        'p_lengthweighted_null_A': p_A,
        'p_uniform_null_B': p_B,
        'alpha_bon': alpha_bon,
        'verdict': verdict,
        'honest_limits': 'Post-hoc origin disclosed in pre-reg §6; verdict ceiling = PASS-DIRECTED until INDEPENDENT REPLICATION.',
    }

    print('=== Q037-F-01 SALĀM-ʿALĀ corpus-share ===')
    print(f'Total instances of "سلام على [PROPHET-NAME]": {n_total}')
    print(f'In Q 37: {n_q37}; share: {share_q37:.4f}')
    for r in valid:
        print(f'  Q{r[0]}:{r[1]}: {r[2][:80]}  (match: {r[3]})')
    print(f'\nLength-weighted null p (Q 37 ≥ {n_q37} hits): {p_A:.4f}')
    print(f'Uniform null p: {p_B:.4f}')
    print(f'Verdict: {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q037-al-saffat/csv/Q037-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
