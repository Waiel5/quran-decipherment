import sys, re
sys.path.insert(0,'/Users/grey/Downloads/quran/poem/audits')
from _scan_engine import scan_sadr, scan_ajuz

# To eliminate my own typos, I now write each hemistich as an explicit list of
# (syllable, weight) pairs. weight is 'u' or '-'. The mora string is DERIVED.
# This is the authoritative transcription. Each syllable's weight is my judgment.

# Format: (bayt, 'sadr'/'ajuz', [ (syl, w), ... ], sila_bool)
B = []
def add(b,h,syls,note=''):
    B.append((b,h,syls,note))

# helper to parse a compact "syl:w syl:w" string
def P(s):
    out=[]
    for tok in s.split():
        syl,w = tok.rsplit(':',1)
        assert w in ('u','-'), (tok,)
        out.append((syl,w))
    return out

# ============ BAYT 1 ============
add(1,'sadr',P("ʿaf:- fat:- ma:u ʿaa:- li:u mu:u kul:- li:u daa:- rin:- wal:- hu:u daa:-"))
add(1,'ajuz',P("ghaḍ:- ḍun:- wa:u ras:- mul:- waḥ:- yi:u ẓal:- lal:- mak:- nuun:-"))
# ============ BAYT 2 ============
add(2,'sadr',P("kam:- ḥaa:- wa:u lash:- shu:u ʿa:u raa:- ʾu:u naẓ:- man:- mith:- la:u huu:-"))  # sila huu
add(2,'ajuz',P("fa:u na:u bat:- qa:u waa:- fii:- him:- wa:u khaa:- bal:- magh:- buun:-"))
# ============ BAYT 3 ============
add(3,'sadr',P("baḥ:- run:- ta:u ghuu:- ṣu:u wa:u laa:- ta:u naa:- lu:u qa:u raa:- ra:u huu:-")) # sila
add(3,'ajuz',P("wad:- dur:- ru:u fil:- aʿ:- maa:- qi:u ẓal:- lal:- mad:- fuun:-"))
# ============ BAYT 4 (reworded) ============
add(4,'sadr',P("wa:u wa:u rith:- tu:u sir:- ral:- qaw:- li:u fas:- tan:- zal:- tu:u huu:-")) # sila
add(4,'ajuz',P("aḥ:- kii:- hi:u ḥat:- tal:- ʿaq:- lu:u min:- nil:- maf:- tuun:-"))
# ============ BAYT 5 (reworded) ============
add(5,'sadr',P("ḥa:u shad:- tu:u aq:- laa:- mii:- wa:u jar:- rad:- tul:- qu:u waa:-"))
add(5,'ajuz',P("wa:u na:u faḍ:- tu:u aw:- zaa:- nan:- wa:u hij:- tul:- makh:- zuun:-"))
# ============ BAYT 6 ============
add(6,'sadr',P("ḥan:- nat:- bi:u hil:- aj:- yaa:- lu:u taḥ:- duu:- ʿii:- sa:u haa:-"))
add(6,'ajuz',P("wal:- lay:- lu:u daa:- jin:- wad:- da:u lii:- lul:- maʾ:- muun:-"))
# ============ BAYT 7 (reworded) ============
add(7,'sadr',P("wa:u ta:u naẓ:- ẓa:u mat:- ma:u naa:- zi:u lu:u ka:u fa:u raa:- qi:u din:-"))
add(7,'ajuz',P("sar:- dan:- ʿa:u laa:- qaṣ:- dis:- sa:u bii:- lil:- maq:- ruun:-"))
# ============ BAYT 8 ============
add(8,'sadr',P("law:- zaa:- gha:u jad:- yun:- aw:- ta:u nak:- ka:u ra:u man:- zi:u lun:-"))
add(8,'ajuz',P("bi:u hi:u taa:- ha:u khir:- rii:- tun:- wa:u ḍal:- lal:- mash:- ḥuun:-"))
# ============ BAYT 9 (reworded) ============
add(9,'sadr',P("ḥat:- taa:- wa:u qaf:- tu:u bi:u baa:- bi:u hi:u mu:u ta:u hay:- yi:u ban:-"))
add(9,'ajuz',P("khaa:- rat:- qu:u wan:- duu:- nii:- wa:u ʿaz:- zal:- mar:- huun:-"))
# ============ BAYT 10 ============
add(10,'sadr',P("as:- sad:- yu:u wal:- luḥ:- mus:- ta:u waa:- fii:- nas:- ji:u hii:-")) # sila
add(10,'ajuz',P("laḥ:- nun:- wa:u maʿ:- nan:- thum:- ma:u naẓ:- mun:- maw:- ḍuun:-"))
# ============ BAYT 11 (reworded) ============
add(11,'sadr',P("qaa:- lul:- ma:u ʿaa:- nii:- fiṭ:- ṭa:u rii:- qi:u ṭa:u rii:- ḥa:u tun:-"))
add(11,'ajuz',P("wal:- faḍ:- lu:u fii:- ḥus:- nil:- ba:u yaa:- nil:- maḍ:- muun:-"))
# ============ BAYT 12 (reworded) ============
add(12,'sadr',P("fa:u i:u ḏaa:- ṣa:u qal:- tul:- laf:- ẓa:u raq:- qa:u ma:u ʿii:- nu:u huu:-")) # sila
add(12,'ajuz',P("wa:u na:u ʾal:- maʿ:- naa:- wal:- ba:u yaa:- nul:- maṭ:- ʿuun:-"))
# ============ BAYT 13 (reworded) ============
add(13,'sadr',P("wa:u i:u ḏaa:- gha:u mas:- tul:- qaw:- la:u fii:- aʿ:- maa:- qi:u hi:u"))
add(13,'ajuz',P("ḏa:u bu:u lar:- ra:u nii:- nu:u wa:u khaa:- ra:u laḥ:- nun:- maw:- huun:-"))
# ============ BAYT 14 ============
add(14,'sadr',P("naa:- run:- wa:u ghay:- thun:- lam:- u:u ṭiq:- jam:- ʿay:- hi:u maa:-"))
add(14,'ajuz',P("fii:- bur:- da:u tin:- wal:- waṣ:- lu:u ghay:- rul:- mar:- ṣuun:-"))
# ============ BAYT 15 ============
add(15,'sadr',P("hu:u wa:u aw:- wa:u lun:- hu:u wa:u aa:- khi:u run:- hu:u wa:u waa:- ḥi:u dun:-"))
add(15,'ajuz',P("ṣa:u ma:u dun:- ʿa:u lay:- hil:- lay:- lu:u daa:- ral:- may:- muun:-"))
# ============ BAYT 16 ============
add(16,'sadr',P("laa:- kuf:- ʾa:u laa:- nid:- dan:- ta:u haa:- kul:- lul:- ma:u daa:-"))
add(16,'ajuz',P("lil:- waa:- ḥi:u dil:- far:- diṭ:- ma:u ʾan:- nal:- maw:- zuun:-"))
# ============ BAYT 17 (reworded) ============
add(17,'sadr',P("min:- waa:- ḥi:u din:- laa:- yuḥ:- ta:u ḏaa:- naẓ:- mun:- la:u huu:-")) # sila
add(17,'ajuz',P("fal:- far:- du:u laa:- yuḥ:- kaa:- ḥi:u maa:- hul:- maḍ:- nuun:-"))
# ============ BAYT 18 ============
add(18,'sadr',P("wal:- ʿaj:- zu:u ʿan:- hu:u hu:u wad:- da:u lii:- lu:u fa:u mith:- la:u huu:-")) # sila
add(18,'ajuz',P("laa:- yus:- ta:u ṭaa:- ʿu:u wa:u ḏuul:- ba:u yaa:- nil:- maḥ:- ṣuun:-"))
# ============ BAYT 19 (reworded) ============
add(19,'sadr',P("maṣ:- ṣar:- fu:u ṣad:- dal:- qaa:- ʾi:u lii:- na:u wa:u in:- na:u maa:-"))
add(19,'ajuz',P("ʿaj:- zun:- bi:u him:- fa:u ma:u qaa:- lu:u hum:- maẓ:- nuun:-"))
# ============ BAYT 20 (reworded) ============
add(20,'sadr',P("kul:- lat:- ti:u saa:- ʿin:- lir:- ru:u ʾaa:- ḍaa:- qat:- bi:u hii:-")) # sila
add(20,'ajuz',P("lu:u gha:u tun:- wa:u ḍaa:- qa:u bi:u hil:- li:u saa:- nul:- mas:- juun:-"))
# ============ BAYT 21 ============
add(21,'sadr',P("duu:- nal:- mu:u sam:- maa:- yaq:- ṣu:u rul:- maʿ:- naa:- fa:u maa:-"))
add(21,'ajuz',P("lil:- laf:- ẓi:u il:- laa:- an:- ya:u ẓal:- lal:- mad:- yuun:-"))
# ============ BAYT 22 (reworded) ============
add(22,'sadr',P("ʿad:- dul:- qu:u shuu:- ra:u wa:u faa:- ta:u hum:- sir:- rul:- hu:u daa:-"))
add(22,'ajuz',P("fa:u ba:u qaw:- ʿa:u laa:- wah:- mil:- ḥi:u saa:- bil:- maʾ:- fuun:-"))
# ============ BAYT 23 ============
add(23,'sadr',P("ʿad:- dul:- fa:u waa:- ti:u ḥa:u wal:- ḥu:u ruu:- fa:u fa:u agh:- fa:u luu:-"))
add(23,'ajuz',P("naẓ:- mal:- hu:u daa:- thum:- man:- za:u waa:- taa:- jun:- nuun:-"))
# ============ BAYT 24 ============
add(24,'sadr',P("laa:- kin:- hu:u nal:- ta:u ḥa:u mal:- mu:u sam:- maa:- bis:- mi:u hii:-")) # sila
add(24,'ajuz',P("wal:- laf:- ẓu:u bil:- maʿ:- naa:- fa:u lay:- sa:u bi:u mam:- nuun:-"))
# ============ BAYT 25 (reworded) ============
add(25,'sadr',P("ḥay:- yun:- ba:u yaa:- nul:- aw:- wa:u lii:- na:u wa:u aq:- fa:u rat:-"))
add(25,'ajuz',P("ṣuḥ:- ful:- u:u laa:- fa:u gha:u dat:- kha:u raa:- ban:- mas:- kuun:-"))
# ============ BAYT 26 ============
add(26,'sadr',P("fa:u kha:u rar:- tu:u laa:- ʿaj:- zan:- fa:u qaṭ:- bal:- saj:- da:u tan:-"))
add(26,'ajuz',P("wal:- ʿaj:- zu:u nus:- kii:- wal:- ja:u bii:- nul:- maṭ:- ḥuun:-"))
# ============ BAYT 27 ============
add(27,'sadr',P("maa:- zin:- tu:u bish:- shiʿ:- ril:- ki:u taa:- ba:u wa:u in:- na:u maa:-"))
add(27,'ajuz',P("zaa:- nal:- qa:u rii:- ḍa:u fa:u khuṭ:- ṭa:u wah:- wal:- maw:- ṭuun:-"))
# ============ BAYT 28 ============
add(28,'sadr',P("wa:u ta:u laa:- ḥa:u qat:- su:u wa:u rul:- hu:u daa:- wa:u ka:u ʾan:- na:u haa:-"))
add(28,'ajuz',P("qa:u ma:u run:- ya:u ʾuu:- bu:u i:u lal:- qa:u dii:- mil:- ʿur:- juun:-"))
# ============ BAYT 29 ============
add(29,'sadr',P("la:u ka:u yaa:- i:u laa:- hid:- dur:- ru:u an:- ta:u mu:u thii:- ru:u huu:-")) # sila
add(29,'ajuz',P("min:- luj:- ja:u tin:- wa:u a:u nal:- gha:u rii:- qul:- maḥ:- zuun:-"))
# ============ BAYT 30 ============
add(30,'sadr',P("wa:u ra:u jaʿ:- tu:u naḥ:- wal:- bad:- ʾi:u baʿ:- da:u khi:u taa:- mi:u hii:-")) # sila
add(30,'ajuz',P("fa:u qa:u raʾ:- tu:u huu:- wal:- khat:- mu:u bad:- ʾun:- maḥ:- ḍuun:-")) # sila on huu

# derive + scan
print("="*100)
def morastr(syls): return ''.join(w for _,w in syls)
issues=[]
for (b,h,syls,note) in B:
    mora=morastr(syls)
    if h=='sadr':
        tag,m,best=scan_sadr(mora)
    else:
        tag,m,best=scan_ajuz(mora)
    ok = (tag=='OK')
    feetstr=' '.join(best) if best else '(no parse)'
    flag='' if ok else '   <<<'
    print(f"B{b:>2} {h:<5} len={len(mora):>2} [{mora:<16}] {tag:<10} {feetstr}{flag}")
    if not ok: issues.append((b,h,tag,mora,feetstr))

print("\n--- ISSUES ---")
for b,h,tag,mora,feet in issues:
    print(f"  B{b} {h}: {tag}  [{mora}]  {feet}")

print("\n\n==================== DIAGNOSTIC: zoom on the 7 flags ====================")

def show(label, syls):
    mora=''.join(w for _,w in syls)
    pretty=' '.join(f"{s}:{w}" for s,w in syls)
    print(f"\n{label}")
    print(f"   syl: {pretty}")
    print(f"   mora({len(mora)}): {mora}")

# B7 sadr -- منازِلُ region
show("B7 sadr (wa-tanaẓẓamat manāzilu ka-farāqidin)",
    P("wa:u ta:u naẓ:- ẓa:u mat:- ma:u naa:- zi:u lu:u ka:u fa:u raa:- qi:u din:-"))
# Alt: if we read 'manāzilun' (tanwin, indefinite) instead of construct 'manāzilu'
show("B7 sadr ALT manāzilun-tanwin? (still u-u- end before ka...)",
    P("wa:u ta:u naẓ:- ẓa:u mat:- ma:u naa:- zi:u lun:- ka:u fa:u raa:- qi:u din:-"))

# B9 sadr -- bibābihi mutahayyiban
show("B9 sadr (ḥattā waqaftu bibābihi mutahayyiban)",
    P("ḥat:- taa:- wa:u qaf:- tu:u bi:u baa:- bi:u hi:u mu:u ta:u hay:- yi:u ban:-"))
# the region 'bi-hi mu-ta' = u u u u (bābihi mutahayyiban): bi(u) hi(u) mu(u) ta(u)
# ALT: bibābihī with sila? but it's mid-hemistich not end; ṣila only at hemistich end. So no.

# B12 ajuz -- wa-naʾā l-maʿnā ...
show("B12 ajuz (wa-naʾā l-maʿnā wal-bayānu l-maṭʿūn)",
    P("wa:u na:u ʾal:- maʿ:- naa:- wal:- ba:u yaa:- nul:- maṭ:- ʿuun:-"))
# wa-na-ʾal = u u - ; maʿ-naa = - - ; that's uu---  then wal-ba-yaa-nul = -u-- ; maṭ-ʿuun = --
# Hmm region uu---- : the '---' run. Let me reconsider: is it 'wa-naʾā' = wa(u) na(u) ʾaa(-)? 
#   naʾā = na-ʾā : na(CV u) ʾā(CVV -). 'wa-naʾā l-maʿnā': wa na ʾaa(+l) -> 'ʾā' + 'l' : ʾāl? 
#   The alif of naʾā is long; followed by al-maʿnā (hamzat waṣl drop) -> wa-na-ʾā-l-maʿ-nā
#   syllab: wa(u) na(u) ʾāl(- closed by l)  maʿ(-) nā(-)  => u u - - -
show("B12 ajuz RE-READ (naʾā+l merges: na-ʾāl)",
    P("wa:u na:u ʾaal:- maʿ:- naa:- wal:- ba:u yaa:- nul:- maṭ:- ʿuun:-"))

# B13 sadr -- ...fī aʿmāqihi  (ends u u -> need legal close)
show("B13 sadr (wa-iḏā ghamastu l-qawla fī aʿmāqihi)",
    P("wa:u i:u ḏaa:- gha:u mas:- tul:- qaw:- la:u fii:- aʿ:- maa:- qi:u hi:u"))
# ends 'qi hi' = u u  -> ṣadr must end u-. Could read 'aʿmāqihī' with sila (hemistich end!) -> qi(u) hī(-)
show("B13 sadr ALT with sila aʿmāqihī (qi-hī = u -)",
    P("wa:u i:u ḏaa:- gha:u mas:- tul:- qaw:- la:u fii:- aʿ:- maa:- qi:u hii:-"))

# B19 ajuz -- ʿajzun bihim fa-maqāluhum maẓnūn  (length issue)
show("B19 ajuz (ʿajzun bihim fa-maqāluhum maẓnūn)",
    P("ʿaj:- zun:- bi:u him:- fa:u ma:u qaa:- lu:u hum:- maẓ:- nuun:-"))
# ʿaj-zun=-- bi-him=u- fa-ma-qaa-lu-hum=uu-u- maẓ-nuun=-- -> --u-uu-u--  = 10 morae? 
# count: -- (2) u- (2) uu-u- (5) -- (2) = 11. mora '--u-uu-u---'? let me see: '-','-','u','-','u','u','-','u','-','-','-' wait that's missing
# Actually printed mora was --u-uu-u--- length 11; engine said BREAK. Let me brute:

from _scan_engine import seg, HASHW_FEET, DARB
for lbl,sy in [
  ("B19ajuz", P("ʿaj:- zun:- bi:u him:- fa:u ma:u qaa:- lu:u hum:- maẓ:- nuun:-")),
]:
    m=''.join(w for _,w in sy)
    print(f"\n{lbl} mora={m} len={len(m)}")
    print("  full segs(any):", seg(m, HASHW_FEET+[DARB]))

# B24 ajuz -- wal-lafẓu bil-maʿnā fa-laysa bi-mamnūn
show("B24 ajuz (wal-lafẓu bil-maʿnā fa-laysa bi-mamnūn)",
    P("wal:- laf:- ẓu:u bil:- maʿ:- naa:- fa:u lay:- sa:u bi:u mam:- nuun:-"))
# wal-laf-ẓu=--u bil-maʿ-naa=--- fa-lay-sa=u-u bi-mam-nuun=u-- 
# mora: --u ---  u-u u-- => --u---u-uu-- length 12 ; ends '- -' not '---'? 
# 'bi-mam-nūn' = bi(u) mam(-) nūn(-) -> u - - ; the ḍarب needs --- (three heavies). Here close is u-- => only 2 heavies preceded by light. BREAK confirmed (Sm darب would be uu-- ; this is u-- )
print("\nB24 ajuz close = ...fa-lay-sa bi-mam-nūn = u-u u-- ; darب region 'u--' is NOT '---' nor 'uu--'")

print("\n\n==================== ḌARب UNIFORMITY CHECK (last 3 morae of every ʿajuz) ====================")
for (b,h,syls,note) in B:
    if h!='ajuz': continue
    mora=''.join(w for _,w in syls)
    close=mora[-3:]
    # also show the 4-mora tail to see the head
    tail4=mora[-4:]
    mark = 'LOCKED ---' if close=='---' else ('SOUND uu-- !!' if tail4=='uu--' else f'?? {close}')
    print(f"  B{b:>2}: tail4={tail4}  close3={close}   {mark}")
