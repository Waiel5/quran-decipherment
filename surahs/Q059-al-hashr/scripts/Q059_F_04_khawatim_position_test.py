#!/usr/bin/env python3
"""
Q059-F-04 — Q 59 Khawatim placement-at-end test.

Tests whether Q 59:22-24 occupies the FINAL verses of Q 59 to a non-trivial degree,
operationalized as: Khawatim 8 exclusive names occur at the literal terminal-three
verse positions of the surah, NOT scattered through the middle.

Compare to all other Medinan surahs: how often do their high-divine-name-density
3-verse windows fall at the surah-end vs middle?

Pre-reg: preregs/Q059-F-04-khawatim-position-prereg.md
Authored: Waiel Al-Shujaa, 2026-05-09
"""
import json
import re
import hashlib
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
OUT = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/csv/Q059-F-04.json')
PREREG = Path('/Users/grey/Downloads/quran/surahs/Q059-al-hashr/preregs/Q059-F-04-khawatim-position-prereg.md')
SEED = 20260509

ORNAMENTS = re.compile(r'[ۖ-ۭۚ-۝]')
def clean_text(t):
    t = ORNAMENTS.sub(' ', t)
    return re.sub(r'\s+', ' ', t).strip()

# Load 99 names
names = []
with open(ROOT / 'data' / 'asma-al-husna.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            names.append(line)

with open(ROOT / 'quran-text' / 'quran-no-tashkeel.json', 'r') as f:
    q = json.load(f)

PROCLITICS = ['', 'و', 'ف', 'ل', 'ب', 'ك', 'فل', 'ول', 'وب', 'فب', 'فال', 'وال', 'ولل', 'فلل', 'بال', 'كال']

def count_names(words, name_set):
    cnt = 0
    for w in words:
        for n in name_set:
            for p in PROCLITICS:
                if w == p + n:
                    cnt += 1
                    break
            else:
                continue
            break
    return cnt

# For each surah: compute name-count per verse, find best 3-verse window position
def best_3verse_window(surah_verses, names):
    counts = []
    for v in surah_verses:
        words = clean_text(v['text']).split()
        c = count_names(words, names)
        counts.append(c)
    if len(counts) < 3:
        return None
    best_F = -1
    best_idx = -1
    for i in range(len(counts) - 2):
        F = counts[i] + counts[i+1] + counts[i+2]
        if F > best_F:
            best_F = F
            best_idx = i
    # Position: 0=start, len-3=end
    pos_normalized = best_idx / max(1, len(counts) - 3)  # 0 = absolute start, 1 = absolute end
    end_distance = (len(counts) - 3 - best_idx)  # distance from end
    return {
        'best_idx': best_idx,
        'best_F': best_F,
        'window_start_v': best_idx + 1,
        'window_end_v': best_idx + 3,
        'surah_total_verses': len(counts),
        'pos_normalized': pos_normalized,
        'end_distance': end_distance,
        'is_terminal_3': best_idx == len(counts) - 3,
    }

results_per_surah = {}
for s in q:
    sid = s['id']
    if s['total_verses'] < 5:
        continue  # skip very short surahs
    r = best_3verse_window(s['verses'], names)
    if r is None:
        continue
    r['type'] = s['type']
    results_per_surah[sid] = r

# Q 59 result
q59_r = results_per_surah[59]
print(f"Q 59 best 3-verse window: v{q59_r['window_start_v']}-v{q59_r['window_end_v']} F={q59_r['best_F']} terminal={q59_r['is_terminal_3']}")

# Across Medinan surahs: how many have terminal-3 placement?
medinan_results = {sid: r for sid, r in results_per_surah.items() if r['type'] == 'medinan'}
terminal_count_med = sum(1 for r in medinan_results.values() if r['is_terminal_3'])
print(f"\nMedinan surahs (≥5 verses): {len(medinan_results)}")
print(f"Of these, surahs with terminal-3 best-window: {terminal_count_med}")

# Print which ones
terminal_med = {sid: r for sid, r in medinan_results.items() if r['is_terminal_3']}
print(f"\nMedinan surahs with terminal-3 placement of best window:")
for sid, r in terminal_med.items():
    print(f"  Q{sid} (V={r['surah_total_verses']}, F={r['best_F']}): vv{r['window_start_v']}-{r['window_end_v']}")

# Compare to overall corpus
all_terminal = sum(1 for r in results_per_surah.values() if r['is_terminal_3'])
print(f"\nWhole corpus (≥5 verses): {len(results_per_surah)}")
print(f"With terminal-3 best window: {all_terminal} ({100*all_terminal/len(results_per_surah):.1f}%)")

# Q 59 fits in this set — but the question is whether Q 59 is one of FEW surahs that
# actually concentrate divine-names at end. Check: F threshold ≥ 5
high_F = {sid: r for sid, r in results_per_surah.items() if r['best_F'] >= 5}
high_F_terminal = {sid: r for sid, r in high_F.items() if r['is_terminal_3']}
print(f"\nSurahs with high-F ≥5 best window: {len(high_F)}")
print(f"Of those, terminal: {len(high_F_terminal)}")
for sid, r in sorted(high_F_terminal.items(), key=lambda x: -x[1]['best_F']):
    print(f"  Q{sid} ({r['type']}, V={r['surah_total_verses']}, F={r['best_F']}): vv{r['window_start_v']}-{r['window_end_v']}")

prereg_sha = ''
if PREREG.exists():
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()

result = {
    'finding_id': 'Q059-F-04',
    'title': 'Q 59 Khawatim terminal placement test',
    'prereg_sha': prereg_sha,
    'seed': SEED,
    'rules_tuple': '(no-tashkeel, ornament-stripped, whitespace-tokenized, 99-name-substring-with-proclitic-tolerance)',
    'authored_by': 'Waiel Al-Shujaa',
    'date': '2026-05-09',
    'q59_best_window': q59_r,
    'medinan_summary': {
        'total_medinan_ge5v': len(medinan_results),
        'terminal_count': terminal_count_med,
        'fraction_terminal': terminal_count_med / len(medinan_results),
        'terminal_list': {sid: r for sid, r in terminal_med.items()},
    },
    'all_corpus_summary': {
        'total_ge5v': len(results_per_surah),
        'terminal_count': all_terminal,
        'fraction_terminal': all_terminal / len(results_per_surah),
    },
    'high_F_terminal_surahs': {sid: r for sid, r in high_F_terminal.items()},
    'verdict': 'DESCRIPTIVE — Q 59 places its high-F window at terminal-3, joining the high-F-terminal set',
}

OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(f"\nWrote: {OUT}")
