#!/usr/bin/env python3
"""Per-lemma Meccan/Medinan permutation test."""
import json, random, re, math
from pathlib import Path
from collections import defaultdict

random.seed(42)

ROOT = Path("/Users/grey/Downloads/quran")
with open(ROOT/"quran-text"/"quran-no-tashkeel.json") as f:
    quran = json.load(f)

SELF_REF_FORMS = {
    "qur'an": ["قرآن","القرآن","قرآنا","قرءان","القرءان","قرءانا"],
    "kitab": ["كتاب","الكتاب","كتابا","كتب","بكتاب","بالكتاب","للكتاب","وكتاب","والكتاب","فالكتاب","كتابه","كتابي","كتابنا","كتابك","كتابكم","كتابهم"],
    "furqan": ["فرقان","الفرقان","بالفرقان","والفرقان"],
    "dhikr": ["ذكر","الذكر","ذكرى","الذكرى","ذكرا","بالذكر","للذكر","والذكر","بذكر","وذكر","وذكرى","وذكرا","فذكر"],
    "tanzil": ["تنزيل","التنزيل","تنزيلا","بتنزيل","وتنزيل"],
    "wahy": ["وحي","الوحي","وحيا","بالوحي","ووحي"],
    "ayat": ["آية","آيات","الآية","الآيات","آياتنا","آياته","آياتي","آياتك","آياتهم","ءاية","ءايات","الءاية","الءايات","ءاياته","ءاياتنا","بآياتنا","بآياته","وآياته","وآياتنا","فآياتنا","فآياته","بآيات","وآيات","لآيات","لآية"],
    "kalam": ["كلام","الكلام","كلاما","كلامي","كلامه","كلمات","الكلمات","بكلام","وكلام","كلمة","الكلمة","بكلمة"],
    "mathani": ["مثاني","المثاني"],
    "nur": ["نور","النور","نورا","نوره","بنور","ونور","ونوره","لنور"],
}
form_to_lemma = {}
for l, fs in SELF_REF_FORMS.items():
    for f in fs:
        form_to_lemma.setdefault(f, []).append(l)

PUNCT = re.compile(r"[^\u0600-\u06FF\s]")
def tok(t):
    return PUNCT.sub(" ", t).split()

CTX = {
    "prior_scrip": {"التوراة","الإنجيل","الانجيل","موسى","عيسى","داود","داوود","زكريا","يحيى","إبراهيم","ابراهيم","هارون","يعقوب","إسحاق","اسحاق","إسرائيل","اسرائيل","صحف","الزبور","اليهود","النصارى"},
    "male_prog": {"ذكرا","ذكور","والأنثى","أنثى","الأنثى","وأنثى","الأنثيين"},
    "revelation": {"أنزل","أنزلنا","نزل","نزلنا","أوحى","أوحينا","الكتاب","كتاب","رسول","الرسول","النبي","نبي","القرآن","قرآن","المبين","مبين","التنزيل","تنزيل"},
    "allah": {"الله","اللّه","ربك","ربه","ربهم","الرحمن","رب"},
}

verses_by_surah = {}  # sid -> [(vid, text, tokens)]
surah_type = {}
for s in quran:
    sid = s["id"]
    surah_type[sid] = s["type"]
    verses_by_surah[sid] = [(v["id"], v["text"], tok(v["text"])) for v in s["verses"]]

def count_lemma_in_verse(lemma, tokens):
    cnt = 0
    tset = set(tokens)
    for t in tokens:
        if t in form_to_lemma and lemma in form_to_lemma[t]:
            if lemma == "kitab":
                if tset & CTX["prior_scrip"]: continue
            elif lemma == "dhikr":
                if tset & CTX["male_prog"]: continue
                if "أهل" in tset and "الذكر" in tset: continue
            elif lemma == "nur":
                if not (tset & CTX["revelation"]): continue
            elif lemma == "kalam":
                if not (tset & CTX["allah"]): continue
            cnt += 1
    return cnt

# Per-surah per-lemma counts + n_verses
surah_lemma = {}
for sid, verses in verses_by_surah.items():
    cnts = {l: 0 for l in SELF_REF_FORMS}
    for vid, text, tokens in verses:
        for l in SELF_REF_FORMS:
            cnts[l] += count_lemma_in_verse(l, tokens)
    surah_lemma[sid] = {"n_verses": len(verses), "lemmas": cnts}

meccan = [s for s in range(1,115) if surah_type[s]=="meccan"]
medinan = [s for s in range(1,115) if surah_type[s]=="medinan"]

def phase_per_verse(surahs, lemma):
    t = sum(surah_lemma[s]["lemmas"][lemma] for s in surahs)
    v = sum(surah_lemma[s]["n_verses"] for s in surahs)
    return t/v

# Observed
print(f"{'lemma':<10} {'mec/v':>8} {'med/v':>8} {'diff':>8} {'null_mean':>10} {'null_sd':>8} {'z':>7} {'p_tail':>7}")
print("-"*80)

NPERM = 2000

all_surahs = list(range(1,115))
N_mec = len(meccan)

for lemma in SELF_REF_FORMS:
    mec_v = phase_per_verse(meccan, lemma)
    med_v = phase_per_verse(medinan, lemma)
    obs = mec_v - med_v
    nulls = []
    for _ in range(NPERM):
        shuf = all_surahs[:]
        random.shuffle(shuf)
        m_ids = shuf[:N_mec]
        md_ids = shuf[N_mec:]
        t_m = sum(surah_lemma[s]["lemmas"][lemma] for s in m_ids)
        v_m = sum(surah_lemma[s]["n_verses"] for s in m_ids)
        t_d = sum(surah_lemma[s]["lemmas"][lemma] for s in md_ids)
        v_d = sum(surah_lemma[s]["n_verses"] for s in md_ids)
        nulls.append(t_m/v_m - t_d/v_d)
    mu = sum(nulls)/len(nulls)
    sd = math.sqrt(sum((x-mu)**2 for x in nulls)/len(nulls))
    z = (obs-mu)/sd if sd else 0
    # one-tail on prediction direction (Meccan > Medinan)
    rank_ge = sum(1 for x in nulls if x >= obs) / len(nulls)
    rank_le = sum(1 for x in nulls if x <= obs) / len(nulls)
    p_two = 2 * min(rank_ge, rank_le)
    print(f"{lemma:<10} {mec_v:>8.4f} {med_v:>8.4f} {obs:>+8.4f} {mu:>+10.4f} {sd:>8.4f} {z:>+7.2f} {p_two:>7.4f}")

# Also: total self-ref density aggregated
mec_total = sum(phase_per_verse(meccan, l)*surah_lemma[meccan[0]]["n_verses"] for l in SELF_REF_FORMS)  # wrong formulation; redo
mec_tokens = sum(surah_lemma[s]["lemmas"][l] for s in meccan for l in SELF_REF_FORMS)
med_tokens = sum(surah_lemma[s]["lemmas"][l] for s in medinan for l in SELF_REF_FORMS)
mec_verses = sum(surah_lemma[s]["n_verses"] for s in meccan)
med_verses = sum(surah_lemma[s]["n_verses"] for s in medinan)
print()
print(f"TOTAL: Meccan {mec_tokens}/{mec_verses}={mec_tokens/mec_verses:.4f} per verse")
print(f"       Medinan {med_tokens}/{med_verses}={med_tokens/med_verses:.4f} per verse")
print(f"       Difference = {mec_tokens/mec_verses - med_tokens/med_verses:+.4f}")
