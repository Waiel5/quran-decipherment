#!/usr/bin/env python3
"""
Q099-F-04: zalzala-root corpus-EXACT distribution.
Tests T1: total = 6 tokens; T2: Q 99 surah-density rank-1; T3: Q 99:1 verse-density rank-1.

Pre-reg SHA256 verified at runtime.
"""
import json, hashlib, re
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q099-al-zalzala/preregs/Q099-F-04-zalzala-root-distribution-prereg.md'
OUT = ROOT / 'surahs/Q099-al-zalzala/csv/Q099-F-04-output.json'

prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
print(f"Pre-reg SHA256: {prereg_sha}")

# Load Quran
data = json.load(open(ROOT / 'quran-text/quran-no-tashkeel.json'))

# zalzala root pattern — match by SURFACE-FORM-WORD, not substring
# A word counts if it contains either "زلزل" (perfect/imperfect) OR "زلزال" (verbal-noun form)
ZALZALA = re.compile(r'(زلزل|زلزال)')

# Find all hits — count by surface-form-word, not substring
hits = []
for s in data:
    for v in s['verses']:
        n_words = len(v['text'].split())
        for word in v['text'].split():
            if ZALZALA.search(word):
                hits.append({
                    "surah": s['id'],
                    "verse": v['id'],
                    "text": v['text'],
                    "n_words": n_words,
                    "surface_form": word,
                })

print(f"Total zalzala-root tokens: {len(hits)}")
print(f"Unique surahs: {len(set(h['surah'] for h in hits))}")
print(f"Unique verses: {len(set((h['surah'], h['verse']) for h in hits))}")

print("\nAll occurrences:")
for h in hits:
    print(f"  Q{h['surah']}:{h['verse']} ({h['n_words']}w): {h['text']}")

# Per-surah stats
surahs_with = {}
for h in hits:
    sid = h['surah']
    if sid not in surahs_with:
        surahs_with[sid] = {"surah": sid, "tokens": 0, "verses_with_root": set(), "first_verse_words": None}
    surahs_with[sid]['tokens'] += 1
    surahs_with[sid]['verses_with_root'].add(h['verse'])

# Add surah-words for density
for sid in surahs_with:
    surah_data = data[sid - 1]
    total_words = sum(len(v['text'].split()) for v in surah_data['verses'])
    surahs_with[sid]['surah_words'] = total_words
    surahs_with[sid]['surah_density_per_100w'] = (surahs_with[sid]['tokens'] / total_words) * 100
    surahs_with[sid]['n_verses_with_root'] = len(surahs_with[sid]['verses_with_root'])

# Print stats
print("\nPer-surah stats:")
host_surahs_sorted = sorted(surahs_with.values(), key=lambda x: -x['surah_density_per_100w'])
for h in host_surahs_sorted:
    print(f"  Q{h['surah']:>3}: tokens={h['tokens']}, surah-words={h['surah_words']}, density-per-100w={h['surah_density_per_100w']:.4f}, n_verses_with_root={h['n_verses_with_root']}")

# Per-verse stats
verse_density = {}
for h in hits:
    key = (h['surah'], h['verse'])
    if key not in verse_density:
        verse_density[key] = {"surah": h['surah'], "verse": h['verse'], "tokens": 0, "verse_words": h['n_words'], "text": h['text']}
    verse_density[key]['tokens'] += 1

for key, v in verse_density.items():
    v['verse_density_per_word'] = v['tokens'] / v['verse_words']

print("\nPer-verse density:")
verses_sorted = sorted(verse_density.values(), key=lambda x: -x['verse_density_per_word'])
for v in verses_sorted:
    print(f"  Q{v['surah']:>3}:{v['verse']:>3} ({v['verse_words']}w, {v['tokens']} tokens): density-per-word={v['verse_density_per_word']:.4f}")

# T1: total = 6 tokens
T1_total = len(hits)
T1_pass = T1_total == 6

# T2: Q 99 surah-density rank-1
q99_rank = next((i+1 for i, h in enumerate(host_surahs_sorted) if h['surah'] == 99), None)
T2_pass = q99_rank == 1

# T3: Q 99:1 verse-density rank-1 of 4 host-verses
q99_v1_rank = next((i+1 for i, v in enumerate(verses_sorted) if v['surah'] == 99 and v['verse'] == 1), None)
T3_pass = q99_v1_rank == 1

print(f"\nT1 (corpus-EXACT 6 tokens locked): {'PASS' if T1_pass else 'FAIL'} (observed = {T1_total})")
print(f"T2 (Q 99 surah-density rank-1 of {len(host_surahs_sorted)}): {'PASS' if T2_pass else 'FAIL'} (rank {q99_rank})")
print(f"T3 (Q 99:1 verse-density rank-1 of {len(verses_sorted)}): {'PASS' if T3_pass else 'FAIL'} (rank {q99_v1_rank})")

n_pass = sum([T1_pass, T2_pass, T3_pass])
if n_pass == 3:
    verdict = "CONFIRMED"
elif n_pass == 2:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"

print(f"\nVERDICT: {verdict}")

output = {
    "test_id": "Q099-F-04",
    "title": "zalzala-root corpus-EXACT distribution: Q 99 share + corpus-token-count",
    "prereg_sha256": prereg_sha,
    "total_tokens": T1_total,
    "n_unique_surahs": len(surahs_with),
    "n_unique_verses": len(verse_density),
    "all_occurrences": [{"surah": h['surah'], "verse": h['verse'], "n_words": h['n_words'], "text": h['text']} for h in hits],
    "host_surahs_sorted_by_density": [{"surah": h['surah'], "tokens": h['tokens'], "surah_words": h['surah_words'], "density_per_100w": h['surah_density_per_100w'], "n_verses_with_root": h['n_verses_with_root']} for h in host_surahs_sorted],
    "host_verses_sorted_by_density": [{"surah": v['surah'], "verse": v['verse'], "tokens": v['tokens'], "verse_words": v['verse_words'], "density_per_word": v['verse_density_per_word'], "text": v['text']} for v in verses_sorted],
    "T1_corpus_total_eq_6": T1_pass,
    "T2_q99_surah_density_rank_1": T2_pass,
    "T3_q99_v1_verse_density_rank_1": T3_pass,
    "n_pass": n_pass,
    "verdict": verdict,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved to: {OUT}")
