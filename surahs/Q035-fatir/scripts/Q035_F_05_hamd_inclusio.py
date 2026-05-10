#!/usr/bin/env python3
"""Q035-F-05 — Q 35 within-surah al-hamdu li-llah inclusio test (v.1 + v.34).

Pre-reg: surahs/Q035-fatir/preregs/Q035-F-05-hamd-inclusio-prereg.md
Pre-reg SHA256: 9be71e5053fc7ce3fb3f40e7496b0dbb2be94370af619dc06c52a5a0b3923bbd
Rules-tuple: (no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1: n_q35_al_hamd >= 2 (Q35 contains v.1 + v.34 instances of al-hamdu li-llah).
H2: Q35 is in TOP-5 by within-surah al-hamdu li-llah occurrences.
Bonferroni k=2, alpha_bon=0.025.
"""
import json, hashlib, sys, os, re

PREREG = '/Users/grey/Downloads/quran/surahs/Q035-fatir/preregs/Q035-F-05-hamd-inclusio-prereg.md'
EXPECTED_SHA = '9be71e5053fc7ce3fb3f40e7496b0dbb2be94370af619dc06c52a5a0b3923bbd'
SEED = 20260509
ALPHA_BON = 0.05 / 2


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
        qtxt = json.load(f)

    pat_alhamd = re.compile(r'الحمد لله')

    per_surah_count = {}
    per_surah_verses = {}
    for s_obj in qtxt:
        s = int(s_obj['id'])
        count = 0
        verses_hit = []
        for v_obj in s_obj['verses']:
            v = int(v_obj['id'])
            t = v_obj['text']
            matches = pat_alhamd.findall(t)
            if matches:
                count += len(matches)
                verses_hit.append({'verse': v, 'n_matches': len(matches), 'text_snippet': t[:120]})
        per_surah_count[s] = count
        per_surah_verses[s] = verses_hit

    n_q35 = per_surah_count.get(35, 0)
    h1_pass = n_q35 >= 2

    # Top-5 by count
    sorted_surahs = sorted(per_surah_count.items(), key=lambda x: -x[1])
    top5 = sorted_surahs[:5]
    q35_in_top5 = any(s == 35 for s, _ in top5)
    q35_rank = next((rk for rk, (s, _) in enumerate(sorted_surahs, 1) if s == 35), None)
    h2_pass = q35_in_top5

    n_pass = sum([h1_pass, h2_pass])
    if n_pass == 2: verdict = 'CONFIRMED'
    elif n_pass == 1: verdict = 'DIRECTIONAL'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q035-F-05',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1_q35_count': {
            'n_q35_al_hamd': n_q35,
            'verses_in_q35': per_surah_verses.get(35, []),
            'pass': h1_pass,
        },
        'h2_top5_rank': {
            'q35_rank': q35_rank,
            'top10_table': [{'surah': s, 'count': c, 'verses': per_surah_verses.get(s, [])} for s, c in sorted_surahs[:10]],
            'pass': h2_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'Surface-form regex test deterministic; Q35 pre-flight 2 occurrences (v.1, v.34).',
    }

    print('=== Q035-F-05 al-hamdu inclusio test ===')
    print(f'H1: n_q35_al_hamd={n_q35} -> pass(>=2)? {h1_pass}')
    print('  Q35 verses:')
    for v in per_surah_verses.get(35, []):
        print(f'    v.{v["verse"]}: n={v["n_matches"]} text="{v["text_snippet"]}"')
    print(f'H2: Q35 rank={q35_rank}, top-5? {h2_pass}')
    print('  Top-10 ranked:')
    for rk, (s, c) in enumerate(sorted_surahs[:10], 1):
        print(f'    rank {rk}: Q{s} count={c}')
    print(f'\nN pass: {n_pass}/2 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q035-fatir/csv/Q035-F-05.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
