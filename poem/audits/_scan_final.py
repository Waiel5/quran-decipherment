import sys
sys.path.insert(0,'/Users/grey/Downloads/quran/poem/audits')
from _scan_engine import scan_sadr, scan_ajuz
def P(s):
    o=[]
    for t in s.split():
        a,b=t.rsplit(':',1); o.append((a,b))
    return o
def M(sy): return ''.join(w for _,w in sy)

# FINAL authoritative transcription of the PROMPT poem (30 bayts).
# hāʾ-ḍamīr policy: LONG (ṣila/ishbāʿ) by default after a moving letter in waṣl;
#   SHORT only (a) after sākin/long-vowel (fīhi, ʿanhu, ʿalayhi), (b) before a following sākin
#   (bihi l-..), or (c) by licensed qaṣr where the long form would break (flagged).
B=[]
def add(b,h,s,tag=''): B.append((b,h,P(s),tag))

add(1,'sadr',"ʿaf:- fat:- ma:u ʿaa:- li:u mu:u kul:- li:u daa:- rin:- wal:- hu:u daa:-")
add(1,'ajuz',"ghaḍ:- ḍun:- wa:u ras:- mul:- waḥ:- yi:u ẓal:- lal:- mak:- nuun:-")
add(2,'sadr',"kam:- ḥaa:- wa:u lash:- shu:u ʿa:u raa:- ʾu:u naẓ:- man:- mith:- la:u huu:-",'sila:mithlahū')
add(2,'ajuz',"fa:u na:u bat:- qa:u waa:- fii:- him:- wa:u khaa:- bal:- magh:- buun:-")
add(3,'sadr',"baḥ:- run:- ta:u ghuu:- ṣu:u wa:u laa:- ta:u naa:- lu:u qa:u raa:- ra:u huu:-",'sila:qarārahū')
add(3,'ajuz',"wad:- dur:- ru:u fil:- aʿ:- maa:- qi:u ẓal:- lal:- mad:- fuun:-")
add(4,'sadr',"wa:u wa:u rith:- tu:u sir:- ral:- qaw:- li:u fas:- tan:- zal:- tu:u huu:-",'sila:-tuhū')
add(4,'ajuz',"aḥ:- kii:- hi:u ḥat:- tal:- ʿaq:- lu:u min:- nil:- maf:- tuun:-")
add(5,'sadr',"ḥa:u shad:- tu:u aq:- laa:- mii:- wa:u jar:- rad:- tul:- qu:u waa:-",'WAQS-foot1')
add(5,'ajuz',"wa:u na:u faḍ:- tu:u aw:- zaa:- nan:- wa:u hij:- tul:- makh:- zuun:-")
add(6,'sadr',"ḥan:- nat:- bi:u hil:- aj:- yaa:- lu:u taḥ:- duu:- ʿii:- sa:u haa:-")  # bihi+l -> bihil short
add(6,'ajuz',"wal:- lay:- lu:u daa:- jin:- wad:- da:u lii:- lul:- maʾ:- muun:-")
add(7,'sadr',"wa:u ta:u naẓ:- ẓa:u mat:- ma:u naa:- zi:u lu:u ka:u fa:u raa:- qi:u din:-",'BREAK?')
add(7,'ajuz',"sar:- dan:- ʿa:u laa:- qaṣ:- dis:- sa:u bii:- lil:- maq:- ruun:-")
add(8,'sadr',"law:- zaa:- gha:u jad:- yun:- aw:- ta:u nak:- ka:u ra:u man:- zi:u lun:-")
add(8,'ajuz',"bi:u hi:u taa:- ha:u khir:- rii:- tun:- wa:u ḍal:- lal:- mash:- ḥuun:-",'haa-qasr:bihi')
add(9,'sadr',"ḥat:- taa:- wa:u qaf:- tu:u bi:u baa:- bi:u hii:- mu:u ta:u hay:- yi:u ban:-",'sila-medial:bābihī')
add(9,'ajuz',"khaa:- rat:- qu:u wan:- duu:- nii:- wa:u ʿaz:- zal:- mar:- huun:-")
add(10,'sadr',"as:- sad:- yu:u wal:- luḥ:- mus:- ta:u waa:- fii:- nas:- ji:u hii:-",'sila:nasjihī')
add(10,'ajuz',"laḥ:- nun:- wa:u maʿ:- nan:- thum:- ma:u naẓ:- mun:- maw:- ḍuun:-")
add(11,'sadr',"qaa:- lul:- ma:u ʿaa:- nii:- fiṭ:- ṭa:u rii:- qi:u ṭa:u rii:- ḥa:u tun:-")
add(11,'ajuz',"wal:- faḍ:- lu:u fii:- ḥus:- nil:- ba:u yaa:- nil:- maḍ:- muun:-")
add(12,'sadr',"fa:u i:u ḏaa:- ṣa:u qal:- tul:- laf:- ẓa:u raq:- qa:u ma:u ʿii:- nu:u huu:-",'sila:maʿīnuhū')
add(12,'ajuz',"wa:u na:u ʾal:- maʿ:- naa:- wal:- ba:u yaa:- nul:- maṭ:- ʿuun:-",'BREAK?')
add(13,'sadr',"wa:u i:u ḏaa:- gha:u mas:- tul:- qaw:- la:u fii:- aʿ:- maa:- qi:u hii:-",'sila:aʿmāqihī')
add(13,'ajuz',"ḏa:u bu:u lar:- ra:u nii:- nu:u wa:u khaa:- ra:u laḥ:- nun:- maw:- huun:-")
add(14,'sadr',"naa:- run:- wa:u ghay:- thun:- lam:- u:u ṭiq:- jam:- ʿay:- hi:u maa:-")
add(14,'ajuz',"fii:- bur:- da:u tin:- wal:- waṣ:- lu:u ghay:- rul:- mar:- ṣuun:-")
add(15,'sadr',"hu:u wa:u aw:- wa:u lun:- hu:u wa:u aa:- khi:u run:- hu:u wa:u waa:- ḥi:u dun:-")
add(15,'ajuz',"ṣa:u ma:u dun:- ʿa:u lay:- hil:- lay:- lu:u daa:- ral:- may:- muun:-")
add(16,'sadr',"laa:- kuf:- ʾa:u laa:- nid:- dan:- ta:u haa:- kul:- lul:- ma:u daa:-")
add(16,'ajuz',"lil:- waa:- ḥi:u dil:- far:- diṭ:- ma:u ʾan:- nal:- maw:- zuun:-")
add(17,'sadr',"min:- waa:- ḥi:u din:- laa:- yuḥ:- ta:u ḏaa:- naẓ:- mun:- la:u huu:-",'sila:lahū')
add(17,'ajuz',"fal:- far:- du:u laa:- yuḥ:- kaa:- ḥi:u maa:- hul:- maḍ:- nuun:-")  # ḥimāhu+l -> ḥimāhul short
add(18,'sadr',"wal:- ʿaj:- zu:u ʿan:- hu:u hu:u wad:- da:u lii:- lu:u fa:u mith:- la:u huu:-",'sila:mithluhū')
add(18,'ajuz',"laa:- yus:- ta:u ṭaa:- ʿu:u wa:u ḏuul:- ba:u yaa:- nil:- maḥ:- ṣuun:-")
add(19,'sadr',"maṣ:- ṣar:- fu:u ṣad:- dal:- qaa:- ʾi:u lii:- na:u wa:u in:- na:u maa:-")
add(19,'ajuz',"ʿaj:- zun:- bi:u him:- fa:u ma:u qaa:- lu:u hum:- maẓ:- nuun:-",'BREAK?')
add(20,'sadr',"kul:- lat:- ti:u saa:- ʿin:- lir:- ru:u ʾaa:- ḍaa:- qat:- bi:u hii:-",'sila:bihī')
add(20,'ajuz',"lu:u gha:u tun:- wa:u ḍaa:- qa:u bi:u hil:- li:u saa:- nul:- mas:- juun:-")  # bihi+l short
add(21,'sadr',"duu:- nal:- mu:u sam:- maa:- yaq:- ṣu:u rul:- maʿ:- naa:- fa:u maa:-")
add(21,'ajuz',"lil:- laf:- ẓi:u il:- laa:- an:- ya:u ẓal:- lal:- mad:- yuun:-")
add(22,'sadr',"ʿad:- dul:- qu:u shuu:- ra:u wa:u faa:- ta:u hum:- sir:- rul:- hu:u daa:-")
add(22,'ajuz',"fa:u ba:u qaw:- ʿa:u laa:- wah:- mil:- ḥi:u saa:- bil:- maʾ:- fuun:-")
add(23,'sadr',"ʿad:- dul:- fa:u waa:- ti:u ḥa:u wal:- ḥu:u ruu:- fa:u fa:u agh:- fa:u luu:-")
add(23,'ajuz',"naẓ:- mal:- hu:u daa:- thum:- man:- za:u waa:- taa:- jun:- nuun:-")
add(24,'sadr',"laa:- kin:- hu:u nal:- ta:u ḥa:u mal:- mu:u sam:- maa:- bis:- mi:u hii:-",'sila:bismihī')
add(24,'ajuz',"wal:- laf:- ẓu:u bil:- maʿ:- naa:- fa:u lay:- sa:u bi:u mam:- nuun:-",'DARB uu-- not ---')
add(25,'sadr',"ḥay:- yun:- ba:u yaa:- nul:- aw:- wa:u lii:- na:u wa:u aq:- fa:u rat:-")
add(25,'ajuz',"ṣuḥ:- ful:- u:u laa:- fa:u gha:u dat:- kha:u raa:- ban:- mas:- kuun:-")
add(26,'sadr',"fa:u kha:u rar:- tu:u laa:- ʿaj:- zan:- fa:u qaṭ:- bal:- saj:- da:u tan:-")
add(26,'ajuz',"wal:- ʿaj:- zu:u nus:- kii:- wal:- ja:u bii:- nul:- maṭ:- ḥuun:-")
add(27,'sadr',"maa:- zin:- tu:u bish:- shiʿ:- ril:- ki:u taa:- ba:u wa:u in:- na:u maa:-")
add(27,'ajuz',"zaa:- nal:- qa:u rii:- ḍa:u fa:u khuṭ:- ṭa:u wah:- wal:- maw:- ṭuun:-")
add(28,'sadr',"wa:u ta:u laa:- ḥa:u qat:- su:u wa:u rul:- hu:u daa:- wa:u ka:u ʾan:- na:u haa:-")
add(28,'ajuz',"qa:u ma:u run:- ya:u ʾuu:- bu:u i:u lal:- qa:u dii:- mil:- ʿur:- juun:-")
add(29,'sadr',"la:u ka:u yaa:- i:u laa:- hid:- dur:- ru:u an:- ta:u mu:u thii:- ru:u huu:-",'sila:muthīruhū')
add(29,'ajuz',"min:- luj:- ja:u tin:- wa:u a:u nal:- gha:u rii:- qul:- maḥ:- zuun:-")
add(30,'sadr',"wa:u ra:u jaʿ:- tu:u naḥ:- wal:- bad:- ʾi:u baʿ:- da:u khi:u taa:- mi:u hii:-",'sila:khitāmihī')
add(30,'ajuz',"fa:u qa:u raʾ:- tu:u huu:- wal:- khat:- mu:u bad:- ʾun:- maḥ:- ḍuun:-",'sila:qaraʾtuhū')

print("="*100)
nclean=0; faults=[]
res={}
for (b,h,sy,note) in B:
    m=M(sy)
    f=scan_sadr if h=='sadr' else scan_ajuz
    tag,_,best=f(m)
    ok=(tag=='OK')
    res[(b,h)]=(ok,tag,m,best,note)
    feet=' '.join(best) if best else '(no parse)'
    flag='' if ok else '  <<< '+tag
    print(f"B{b:>2} {h:<5} [{m:<16}] {'OK' if ok else tag:<9} {note:<22} {feet}{flag}")

print("\n========= BAYT-LEVEL METER VERDICT (both hemistichs must pass) =========")
for b in range(1,31):
    so,st,_,_,sn=res[(b,'sadr')]; ao,at,_,_,an=res[(b,'ajuz')]
    waqs = ('WAQS' in st) or ('WAQS' in at)
    if so and ao and not waqs:
        verdict='CLEAN'; nclean+=1
    elif so and ao and waqs:
        verdict='CLEAN-but-WAQS(qabīḥ)'
        faults.append((b,'waqṣ',f"sadr={st} ajuz={at}"))
    else:
        bad=[]
        if not so: bad.append(f"ṣadr {st}")
        if not ao: bad.append(f"ʿajuz {at}")
        verdict='BREAK: '+'; '.join(bad)
        faults.append((b,'break',verdict))
    print(f"  B{b:>2}: {verdict}")

print(f"\nMETER-CLEAN (no break, no waqṣ): {nclean}/30")
print("FAULTS:")
for b,k,d in faults: print(f"   B{b} [{k}] {d}")
