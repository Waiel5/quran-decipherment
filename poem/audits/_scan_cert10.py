#!/usr/bin/env python3
"""
INDEPENDENT re-derivation for cert-10 (Opus 4.8 strict critic).
Method: hand-transcribe each hemistich as a SYLLABLE skeleton (u=light CV, -=heavy CVC/CVV),
applying classical waṣl pronunciation by hand (hāʾ-ḍamīr ṣila by default after a moving letter;
short after sākin/long-vowel or before a following sākin). The engine ONLY foot-splits + checks
legality — it cannot see the words, keeping the mechanical part honest.

al-Kāmil feet (5 morae): sālim uu-u- | iḍmār --u- | waqṣ u-u- (qabīḥ).
ṢADR (ʿarūḍ ṣaḥīḥa): 3 feet, ends 'u-'.  ʿAJUZ (tāmm): 2 hashw feet + LOCKED ḍarب '---'.
MAJZŪʾ (line 15): each hemistich = 2 feet; majzūʾ ḍarب may be the maqṭūʿ '--' (mutaFAAilun->mutFAAil
catalexis) OR a full foot. We test line 15 explicitly against the majzūʾ inventory.
"""

SADR_FEET  = ['uu-u-', '--u-', 'u-u-']
HASHW_FEET = ['uu-u-', '--u-', 'u-u-']
DARB_TAMM  = '---'
WAQS = 'u-u-'

def seg(mora, inv, nfeet=None, last=None):
    out=[]
    def rec(rem, acc):
        if not rem:
            if nfeet is not None and len(acc)!=nfeet: return
            if last is not None and (not acc or acc[-1]!=last): return
            out.append(list(acc)); return
        for f in inv:
            if rem.startswith(f): rec(rem[len(f):], acc+[f])
    rec(mora, [])
    return out

def scan_sadr(m):
    m=m.replace(' ','')
    segs=seg(m, SADR_FEET, nfeet=3)
    if not segs:
        return ('BREAK', m, seg(m,SADR_FEET))
    best=segs[0]
    wp=[i for i,f in enumerate(best) if f==WAQS]
    return (('OK' if not wp else f'WAQS@{wp}'), m, best)

def scan_ajuz_tamm(m):
    m=m.replace(' ','')
    if not m.endswith(DARB_TAMM):
        return ('BREAK(not---)', m, seg(m,HASHW_FEET+[DARB_TAMM]))
    body=m[:-3]
    segs=seg(body,HASHW_FEET,nfeet=2)
    if not segs:
        return ('BREAK', m, seg(m,HASHW_FEET+[DARB_TAMM]))
    best=segs[0]+[DARB_TAMM]
    wp=[i for i,f in enumerate(best) if f==WAQS]
    return (('OK' if not wp else f'WAQS@{wp}'), m, best)

# ---------------- PROMPT POEM transcription (re-derived from phonemes) ----------------
# I list each hemistich's syllable skeleton. Comments give the phoneme reading.
# Only the 5 reworked lines (5,7,12,19,24), the two strokes (15,20) and a few cross-checks
# are re-transcribed from scratch; the 25 untouched lines match the locked audit-09 skeletons.

S={}  # (bayt,'s'/'a') -> skeleton
def put(b,h,s): S[(b,h)]=s

# B1
put(1,'s',"- - u - u u - u - - u -")   # ʿaf-fat ma-ʿaa-li-mu kul-li daa-rin wal-hu-daa
put(1,'a',"- - u - - - - - - - -")     # ghaḍ-ḍun wa-ras-mul-waḥ-yi ẓal-lal-mak-nuun
# B2  (sila mithlahū)
put(2,'s',"- - u - u u - u - - u -")   # kam-ḥaa-wa-lash-shu-ʿa-raa-ʾu-naẓ-man-mith-la-huu
put(2,'a',"u u - u - - - - - - -")     # fa-na-bat qa-waa-fii-him wa-khaa-bal-magh-buun
# B3 (sila qarārahū)
put(3,'s',"- - u - u u - u - u u - u -")
put(3,'a',"- - u - - - - - - - -")     # wad-dur-ru fil-aʿ-maa-qi ẓal-lal-mad-fuun
# B4 (sila -tuhū)
put(4,'s',"u u - u - - - u - - - u -")  # wa-wa-rith-tu sir-ral-qaw-li fas-tan-zal-tu-huu
put(4,'a',"- - u - - - - u - - -")      # aḥ-kii-hi ḥat-tal-ʿaq-lu min-nil-maf-tuun
# B5 *** REWORKED: jammaʿtu aqlāmī wa-jarradtu l-quwā ***
put(5,'s',"- - u - - - u - - - u -")    # jam-maʿ-tu aq-laa-mii wa-jar-rad-tul-qu-waa
put(5,'a',"u u - u - - - u - - -")      # wa-na-faḍ-tu aw-zaa-nan wa-hij-tul-makh-zuun
# B6 (bihil short)
put(6,'s',"- - u - - - u - - - u -")    # ḥan-nat bi-hil-aj-yaa-lu taḥ-duu-ʿii-sa-haa
put(6,'a',"- - u - - - u - - - -")      # wal-lay-lu daa-jin wad-da-lii-lul-maʾ-muun
# B7 *** REWORKED: wa-tanaẓẓamat ṣaffan ka-mithli farāqidin ***
put(7,'s',"u u - u - - - u - u u - u -")  # wa-ta-naẓ-ẓa-mat ṣaf-fan ka-mith-li fa-raa-qi-din
put(7,'a',"- - u - - - u - - - -")        # sar-dan ʿa-laa qaṣ-dis-sa-bii-lil-maq-ruun
# B8
put(8,'s',"- - u - - - u - u u - u -")
put(8,'a',"u u - u - - - u - - -")        # bi-hi taa-ha khir-rii-tun wa-ḍal-lal-mash-ḥuun (haa-qasr bihi)
# B9 (sila-medial bābihī)
put(9,'s',"- - u - u u - u - u u - u -")   # ḥat-taa wa-qaf-tu bi-baa-bi-hii mu-ta-hay-yi-ban
put(9,'a',"- - u - - - u - - - -")         # khaa-rat qu-wan duu-nii wa-ʿaz-zal-mar-huun
# B10 (sila nasjihī)
put(10,'s',"- - u - - - u - - - u -")
put(10,'a',"- - u - - - u - - - -")        # laḥ-nun wa-maʿ-nan thum-ma-naẓ-mun-maw-ḍuun
# B11
put(11,'s',"- - u - - - u - u u - u -")
put(11,'a',"- - u - - - u - - - -")        # wal-faḍ-lu fii ḥus-nil-ba-yaa-nil-maḍ-muun
# B12 *** REWORKED ʿajuz: wa-naʾat maʿānin wal-bayānu l-maṭʿūn ***
put(12,'s',"u u - u - - - u - u u - u -")   # fa-i-ḏaa ṣa-qal-tul-laf-ẓa raq-qa ma-ʿii-nu-huu (sila maʿīnuhū)
put(12,'a',"u u - u - - - u - - -")         # wa-na-ʾat ma-ʿaa-nin wal-ba-yaa-nul-maṭ-ʿuun
# B13 (sila aʿmāqihī)
put(13,'s',"u u - u - - - u - - - u -")
put(13,'a',"u u - u - u u - u - - -")       # ḏa-bu-lar-ra-nii-nu wa-khaa-ra laḥ-nun-maw-huun
# B14
put(14,'s',"- - u - - - u - - - u -")
put(14,'a',"- - u - - - u - - - -")
# --- B15 (STROKE 1 = majzūʾ) handled separately below ---
# B16
put(16,'s',"- - u - - - u - - - u -")
put(16,'a',"- - u - - - u - - - -")         # lil-waa-ḥi-dil-far-diṭ-ma-ʾan-nal-maw-zuun
# B17 (sila lahū; ḥimāhul short)
put(17,'s',"- - u - - - u - - - u -")
put(17,'a',"- - u - - - u - - - -")         # fal-far-du laa yuḥ-kaa ḥi-maa-hul-maḍ-nuun
# B18 (sila mithluhū)
put(18,'s',"- - u - u u - u - u u - u -")
put(18,'a',"- - u - u u - u - - -")          # laa yus-ta-ṭaa-ʿu wa-ḏuul-ba-yaa-nil-maḥ-ṣuun
# B19 *** REWORKED ʿajuz: ʿajzun bihim wal-qawlu minhum maẓnūn ***
put(19,'s',"- - u - - - u - u u - u -")      # maṣ-ṣar-fu ṣad-dal-qaa-ʾi-lii-na wa-in-na-maa
put(19,'a',"- - u - - - u - - - -")          # ʿaj-zun bi-him wal-qaw-lu min-hum-maẓ-nuun
# --- B20 (STROKE 2 = coinage) handled separately below ---
# B21 (madyūn diction flag; meter clean)
put(21,'s',"- - u - - - u - - - u -")        # duu-nal-mu-sam-maa yaq-ṣu-rul-maʿ-naa fa-maa
put(21,'a',"- - u - - - u - - - -")          # lil-laf-ẓi il-laa an-ya-ẓal-lal-mad-yuun
# B22
put(22,'s',"- - u - u u - u - - - u -")
put(22,'a',"u u - u - - - u - - -")          # fa-ba-qaw ʿa-laa wah-mil-ḥi-saa-bil-maʾ-fuun
# B23
put(23,'s',"- - u - u u - u - u u - u -")    # ʿad-dul-fa-waa-ti-ḥa wal-ḥu-ruu-fa fa-agh-fa-luu
put(23,'a',"- - u - - - u - - - -")          # naẓ-mal-hu-daa thum-man-za-waa taa-jun-nuun
# B24 *** REWORKED ʿajuz: wal-lafẓu wal-maʿnā staqāma l-mamnūn ***
put(24,'s',"- - u - u u - u - - - u -")      # laa-kin hu-nal-ta-ḥa-mal-mu-sam-maa bis-mi-hii (sila bismihī)
put(24,'a',"- - u - - - u - - - -")          # wal-laf-ẓu wal-maʿ-naa s-ta-qaa-mal-mam-nuun
# B25
put(25,'s',"- - u - - - u - u u - u -")
put(25,'a',"- - u - u u - u - - -")          # ṣuḥ-ful-u-laa fa-gha-dat kha-raa-ban-mas-kuun
# B26
put(26,'s',"u u - u - - - u - - - u -")      # fa-kha-rar-tu laa ʿaj-zan fa-qaṭ bal-saj-da-tan
put(26,'a',"- - u - - - u - - - -")          # wal-ʿaj-zu nus-kii wal-ja-bii-nul-maṭ-ḥuun
# B27
put(27,'s',"- - u - - - u - u u - u -")
put(27,'a',"- - u - u u - u - - -")          # zaa-nal-qa-rii-ḍa fa-khuṭ-ṭa wah-wal-maw-ṭuun
# B28
put(28,'s',"u u - u - u u - u - u u - u -")
put(28,'a',"u u - u - u u - u - - -")        # qa-ma-run ya-ʾuu-bu i-lal-qa-dii-mil-ʿur-juun
# B29 (sila muthīruhū)
put(29,'s',"u u - u - - - u - u u - u -")
put(29,'a',"- - u - u u - u - - -")          # min-luj-ja-tin wa-a-nal-gha-rii-qul-maḥ-zuun
# B30 (sila khitāmihī; sila qaraʾtuhū)
put(30,'s',"u u - u - - - u - u u - u -")
put(30,'a',"u u - u - - - u - - -")          # fa-qa-raʾ-tu-huu wal-khat-mu bad-ʾun-maḥ-ḍuun

print("="*92)
print("TĀMM LINES (all except 15) — independent re-scan")
print("="*92)
clean=0; faults=[]
for b in list(range(1,15))+list(range(16,31)):
    if b==20:
        continue  # stroke 2 checked below but it IS a tāmm line; include in loop after
    so,sm,sb=scan_sadr(S[(b,'s')])
    ao,am,ab=scan_ajuz_tamm(S[(b,'a')])
    waqs=('WAQS' in so) or ('WAQS' in ao)
    ok = so=='OK' and ao=='OK'
    v = 'CLEAN' if ok else ('WAQS' if (so.startswith('OK') or 'WAQS' in so or 'WAQS' in ao) and 'BREAK' not in so+ao else 'BREAK')
    if ok:
        clean+=1; v='CLEAN'
    else:
        if 'BREAK' in so or 'BREAK' in ao:
            v='BREAK'; faults.append((b,'break',f"s={so} a={ao}"))
        else:
            v='WAQS'; faults.append((b,'waqs',f"s={so} a={ao}"))
    print(f"B{b:>2} s[{sm:<14}]{so:<9} a[{am:<13}]{ao:<11} -> {v}")
    if 'BREAK' in so: print(f"      ṣadr parse attempts: {sb}")
    if 'BREAK' in ao: print(f"      ʿajuz parse attempts: {ab}")

print(f"\nTĀMM lines clean (excl. 15 & 20): {clean}/29")
print("FAULTS:", faults if faults else "NONE")

# ---------------- STROKE 2: line 20 as a TĀMM line ----------------
print("\n"+"="*92)
print("STROKE 2 — Line 20 (al-Bayyūn): must be a CLEAN tāmm maqṭūʿ line")
print("="*92)
# ṣadr: wa-li-saa-nu qaw-mii ʿan sa-naa-hu mu-qaṣ-ṣi-run
s20s="u u - u - - - u u - u - u -"
# ʿajuz: fa-na-ḥat-tu laf-ẓan in-na-hul-bay-yuun   (al-Bayyūn: penult 'bay' LONG = heavy)
# in-na-hu: hāʾ ṣila? "innahu" then sākin 'l' of al-Bayyūn -> innahu+l -> short hu (before sākin)
# so: fa(u) na(u) ḥat(-) tu(u) laf(-) ẓan(-) in(-) na(u) hul(-) bay(-) yuun(-)
s20a="u u - u - - - u - - -"
so,sm,sb=scan_sadr(s20s); ao,am,ab=scan_ajuz_tamm(s20a)
print(f"B20 ṣadr  [{sm}] -> {so}  feet={sb if 'BREAK' in so else scan_sadr(s20s)[2]}")
print(f"B20 ʿajuz [{am}] -> {ao}  feet={ab if 'BREAK' in ao else scan_ajuz_tamm(s20a)[2]}")
print("al-Bayyūn rhyme: bay(-) yuun(-) => penult 'bay' is HEAVY/long => Family-B long-penult -ūn  ✓" )

# ---------------- STROKE 1: line 15 as MAJZŪʾ al-Kāmil ----------------
print("\n"+"="*92)
print("STROKE 1 — Line 15 (majzūʾ al-Kāmil): 2 feet per hemistich")
print("="*92)
# ṣadr: ḥaa-wal-tu jam-ʿa-hu-maa fa-qaṣ   ==>  ḥaa(-) wal(-) tu(u) jam(-) ʿa(u) hu(u) maa(-) fa(u) qaṣ(-)
#   skeleton: - - u - u u - u -   = 9 units = mutFAAilun(--u-) + mutaFAAilun(uu-u-) ... check
ms_s="- - u - u u - u -"
# ʿajuz: ṣar-tu wa-ad-ra-ka-ni-s-su-kuun  ==> ṣar(-) tu(u) wa(u) ad(-) ra(u) ka(u) nis(-) su(u) kuun(-)
#   wait: wa-adrakanī as-sukūn -> "wa-adrakaniyi s-sukūn": ḏ adrakanī then sākin l -> short ī?
#   adrakanī + as-sukūn: the long ī of -nī before sākin 'ss' -> shortened by iltiqāʾ -> -ni-
#   ṣar(-) tu(u) wa(u) ad(-) ra(u) ka(u) nis(-) su(u) kuun(-)  = - u u - u u - u -  (9 units)
ms_a="- u u - u u - u -"

# Majzūʾ al-Kāmil hashw foot inventory (same 5-mora feet); majzūʾ ḍarب options:
#   (i) maqṭūʿ '--'  (mutaFAAilun -> mutFAAil, last sabab dropped & taskīn)
#   (ii) aḥadd / full foot.  Most common classical majzūʾ ḍarب used here = the one ending the
#   rhyme. al-sukūn = su(u) kuun(-). For a majzūʾ with 2 feet: foot1 + foot2(=ḍarب).
MAJZ_FOOT=['uu-u-','--u-','u-u-']
def scan_majz(m, darb_opts):
    m=m.replace(' ','')
    best=None
    for d in darb_opts:
        if m.endswith(d):
            body=m[:-len(d)]
            segs=seg(body,MAJZ_FOOT,nfeet=1)
            if segs:
                best=(segs[0]+[d], d); break
    return best
# try ḍarب inventory: full feet, maqṭūʿ '- -', and the 'u-' (catalexis) just in case
res_s=scan_majz(ms_s, ['uu-u-','--u-','u-u-','--','-'])
res_a=scan_majz(ms_a, ['uu-u-','--u-','u-u-','--','-'])
print(f"B15 ṣadr  [{ms_s.replace(' ','')}] -> feet={res_s}")
print(f"B15 ʿajuz [{ms_a.replace(' ','')}] -> feet={res_a}")
print(f"  ṣadr unit count = {len(ms_s.replace(' ',''))}; ʿajuz unit count = {len(ms_a.replace(' ',''))}")
print(f"  (tāmm ṣadr is ~13-14 units; majzūʾ ~9 units => ~30% shorter ✓ if both ~9)")
