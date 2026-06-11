#!/usr/bin/env python3
# CERT-10 — full independent re-transcription of the PROMPT's 32-line poem from phonemes.
HASHW=['uu-u-','--u-','u-u-']; WAQS='u-u-'; DARB_T='---'
def feet_seg(m, inv, nfeet=None, darb=None):
    out=[]
    def rec(rem,acc):
        if not rem:
            if nfeet is not None and len(acc)!=nfeet: return
            if darb is not None and (not acc or acc[-1]!=darb): return
            out.append(acc[:]); return
        for f in inv:
            if rem.startswith(f): rec(rem[len(f):],acc+[f])
        if darb is not None and rem==darb: rec('',acc+[darb])
    rec(m,[]); return out
def sk(sy): return ''.join(w for _,w in sy)
def scan_sadr(sy):
    m=sk(sy); s=feet_seg(m,HASHW,nfeet=3)
    if not s: return ('BREAK',m,feet_seg(m,HASHW))
    b=s[0]; wp=[i for i,f in enumerate(b) if f==WAQS]
    return (('OK' if not wp else f'WAQS{wp}'),m,b)
def scan_ajuz_tamm(sy):
    m=sk(sy)
    if not m.endswith(DARB_T): return ('BREAK-not---',m,feet_seg(m,HASHW+[DARB_T]))
    s=feet_seg(m[:-3],HASHW,nfeet=2)
    if not s: return ('BREAK',m,feet_seg(m,HASHW+[DARB_T]))
    b=s[0]+[DARB_T]; wp=[i for i,f in enumerate(b) if f==WAQS]
    return (('OK' if not wp else f'WAQS{wp}'),m,b)
L={}
def put(b,h,*sy): L[(b,h)]=list(sy)
U='u'; H='-'
put(1,'s',('ʿaf',H),('fat',H),('ma',U),('ʿaa',H),('li',U),('mu',U),('kul',H),('li',U),('daa',H),('rin',H),('wal',H),('hu',U),('daa',H))
put(1,'a',('ghaḍ',H),('ḍun',H),('wa',U),('ras',H),('mul',H),('waḥ',H),('yi',U),('ẓal',H),('lal',H),('mak',H),('nuun',H))
put(2,'s',('kam',H),('ḥaa',H),('wa',U),('lash',H),('shu',U),('ʿa',U),('raa',H),('ʾu',U),('naẓ',H),('man',H),('mith',H),('la',U),('huu',H))
put(2,'a',('fa',U),('na',U),('bat',H),('qa',U),('waa',H),('fii',H),('him',H),('wa',U),('khaa',H),('bal',H),('magh',H),('buun',H))
put(3,'s',('baḥ',H),('run',H),('ta',U),('ghuu',H),('ṣu',U),('wa',U),('laa',H),('ta',U),('naa',H),('lu',U),('qa',U),('raa',H),('ra',U),('huu',H))
put(3,'a',('wad',H),('dur',H),('ru',U),('fil',H),('aʿ',H),('maa',H),('qi',U),('ẓal',H),('lal',H),('mad',H),('fuun',H))
put(4,'s',('wa',U),('wa',U),('rith',H),('tu',U),('sir',H),('ral',H),('qaw',H),('li',U),('fas',H),('tan',H),('zal',H),('tu',U),('huu',H))
put(4,'a',('aḥ',H),('kii',H),('hi',U),('ḥat',H),('tal',H),('ʿaq',H),('lu',U),('min',H),('nil',H),('maf',H),('tuun',H))
put(5,'s',('jam',H),('maʿ',H),('tu',U),('aq',H),('laa',H),('mii',H),('wa',U),('jar',H),('rad',H),('tul',H),('qu',U),('waa',H))
put(5,'a',('wa',U),('na',U),('faḍ',H),('tu',U),('aw',H),('zaa',H),('nan',H),('wa',U),('hij',H),('tul',H),('makh',H),('zuun',H))
put(6,'s',('ḥan',H),('nat',H),('bi',U),('hil',H),('aj',H),('yaa',H),('lu',U),('taḥ',H),('duu',H),('ʿii',H),('sa',U),('haa',H))
put(6,'a',('wal',H),('lay',H),('lu',U),('daa',H),('jin',H),('wad',H),('da',U),('lii',H),('lul',H),('maʾ',H),('muun',H))
put(7,'s',('wa',U),('ta',U),('naẓ',H),('ẓa',U),('mat',H),('ṣaf',H),('fan',H),('ka',U),('mith',H),('li',U),('fa',U),('raa',H),('qi',U),('din',H))
put(7,'a',('sar',H),('dan',H),('ʿa',U),('laa',H),('qaṣ',H),('dis',H),('sa',U),('bii',H),('lil',H),('maq',H),('ruun',H))
put(8,'s',('law',H),('zaa',H),('gha',U),('jad',H),('yun',H),('aw',H),('ta',U),('nak',H),('ka',U),('ra',U),('man',H),('zi',U),('lun',H))
put(8,'a',('bi',U),('hi',U),('taa',H),('ha',U),('khir',H),('rii',H),('tun',H),('wa',U),('ḍal',H),('lal',H),('mash',H),('ḥuun',H))
put(9,'s',('ḥat',H),('taa',H),('wa',U),('qaf',H),('tu',U),('bi',U),('baa',H),('bi',U),('hii',H),('mu',U),('ta',U),('hay',H),('yi',U),('ban',H))
put(9,'a',('khaa',H),('rat',H),('qu',U),('wan',H),('duu',H),('nii',H),('wa',U),('ʿaz',H),('zal',H),('mar',H),('huun',H))
put(10,'s',('as',H),('sad',H),('yu',U),('wal',H),('luḥ',H),('mus',H),('ta',U),('waa',H),('fii',H),('nas',H),('ji',U),('hii',H))
put(10,'a',('laḥ',H),('nun',H),('wa',U),('maʿ',H),('nan',H),('thum',H),('ma',U),('naẓ',H),('mun',H),('maw',H),('ḍuun',H))
put(11,'s',('qaa',H),('lul',H),('ma',U),('ʿaa',H),('nii',H),('fiṭ',H),('ṭa',U),('rii',H),('qi',U),('ṭa',U),('rii',H),('ḥa',U),('tun',H))
put(11,'a',('wal',H),('faḍ',H),('lu',U),('fii',H),('ḥus',H),('nil',H),('ba',U),('yaa',H),('nil',H),('maḍ',H),('muun',H))
put(12,'s',('fa',U),('i',U),('ḏaa',H),('ṣa',U),('qal',H),('tul',H),('laf',H),('ẓa',U),('raq',H),('qa',U),('ma',U),('ʿii',H),('nu',U),('huu',H))
put(12,'a',('wa',U),('na',U),('ʾat',H),('ma',U),('ʿaa',H),('nin',H),('wal',H),('ba',U),('yaa',H),('nul',H),('maṭ',H),('ʿuun',H))
put(13,'s',('wa',U),('i',U),('ḏaa',H),('gha',U),('mas',H),('tul',H),('qaw',H),('la',U),('fii',H),('aʿ',H),('maa',H),('qi',U),('hii',H))
put(13,'a',('ḏa',U),('bu',U),('lar',H),('ra',U),('nii',H),('nu',U),('wa',U),('khaa',H),('ra',U),('laḥ',H),('nun',H),('maw',H),('huun',H))
put(14,'s',('naa',H),('run',H),('wa',U),('ghay',H),('thun',H),('lam',H),('u',U),('ṭiq',H),('jam',H),('ʿay',H),('hi',U),('maa',H))
put(14,'a',('fii',H),('bur',H),('da',U),('tin',H),('wal',H),('waṣ',H),('lu',U),('ghay',H),('rul',H),('mar',H),('ṣuun',H))
put(15,'s',('ḥaa',H),('wal',H),('tu',U),('jam',H),('ʿa',U),('hu',U),('maa',H),('fa',U),('qaṣ',H))
put(15,'a',('ṣar',H),('tu',U),('wa',U),('ad',H),('ra',U),('ka',U),('nis',H),('su',U),('kuun',H))
put(16,'s',('hu',U),('wa',U),('aw',H),('wa',U),('lun',H),('hu',U),('wa',U),('aa',H),('khi',U),('run',H),('hu',U),('wa',U),('waa',H),('ḥi',U),('dun',H))
put(16,'a',('ṣa',U),('ma',U),('dun',H),('ʿa',U),('lay',H),('hil',H),('lay',H),('lu',U),('daa',H),('ral',H),('may',H),('muun',H))
put(17,'s',('laa',H),('kuf',H),('ʾa',U),('laa',H),('nid',H),('dan',H),('ta',U),('haa',H),('kul',H),('lul',H),('ma',U),('daa',H))
put(17,'a',('lil',H),('waa',H),('ḥi',U),('dil',H),('far',H),('diṭ',H),('ma',U),('ʾan',H),('nal',H),('maw',H),('zuun',H))
put(18,'s',('min',H),('waa',H),('ḥi',U),('din',H),('laa',H),('yuḥ',H),('ta',U),('ḏaa',H),('naẓ',H),('mun',H),('la',U),('huu',H))
put(18,'a',('fal',H),('far',H),('du',U),('laa',H),('yuḥ',H),('kaa',H),('ḥi',U),('maa',H),('hul',H),('maḍ',H),('nuun',H))
put(19,'s',('wal',H),('ʿaj',H),('zu',U),('ʿan',H),('hu',U),('hu',U),('wad',H),('da',U),('lii',H),('lu',U),('fa',U),('mith',H),('la',U),('huu',H))
put(19,'a',('laa',H),('yus',H),('ta',U),('ṭaa',H),('ʿu',U),('wa',U),('ḏuul',H),('ba',U),('yaa',H),('nil',H),('maḥ',H),('ṣuun',H))
put(20,'s',('wa',U),('li',U),('saa',H),('nu',U),('qaw',H),('mii',H),('ʿan',H),('sa',U),('naa',H),('hu',U),('mu',U),('qaṣ',H),('ṣi',U),('run',H))
put(20,'a',('fa',U),('na',U),('ḥat',H),('tu',U),('laf',H),('ẓan',H),('in',H),('na',U),('hul',H),('bay',H),('yuun',H))
put(21,'s',('maṣ',H),('ṣar',H),('fu',U),('ṣad',H),('dal',H),('qaa',H),('ʾi',U),('lii',H),('na',U),('wa',U),('in',H),('na',U),('maa',H))
put(21,'a',('ʿaj',H),('zun',H),('bi',U),('him',H),('wal',H),('qaw',H),('lu',U),('min',H),('hum',H),('maẓ',H),('nuun',H))
put(22,'s',('kul',H),('lat',H),('ti',U),('saa',H),('ʿin',H),('lir',H),('ru',U),('ʾaa',H),('ḍaa',H),('qat',H),('bi',U),('hii',H))
put(22,'a',('lu',U),('gha',U),('tun',H),('wa',U),('ḍaa',H),('qa',U),('bi',U),('hil',H),('li',U),('saa',H),('nul',H),('mas',H),('juun',H))
put(23,'s',('duu',H),('nal',H),('mu',U),('sam',H),('maa',H),('yaq',H),('ṣu',U),('rul',H),('maʿ',H),('naa',H),('fa',U),('maa',H))
put(23,'a',('lil',H),('laf',H),('ẓi',U),('il',H),('laa',H),('an',H),('ya',U),('ẓal',H),('lal',H),('mad',H),('yuun',H))
put(24,'s',('ʿad',H),('dul',H),('qu',U),('shuu',H),('ra',U),('wa',U),('faa',H),('ta',U),('hum',H),('sir',H),('rul',H),('hu',U),('daa',H))
put(24,'a',('fa',U),('ba',U),('qaw',H),('ʿa',U),('laa',H),('wah',H),('mil',H),('ḥi',U),('saa',H),('bil',H),('maʾ',H),('fuun',H))
put(25,'s',('ʿad',H),('dul',H),('fa',U),('waa',H),('ti',U),('ḥa',U),('wal',H),('ḥu',U),('ruu',H),('fa',U),('fa',U),('agh',H),('fa',U),('luu',H))
put(25,'a',('naẓ',H),('mal',H),('hu',U),('daa',H),('thum',H),('man',H),('za',U),('waa',H),('taa',H),('jun',H),('nuun',H))
put(26,'s',('laa',H),('kin',H),('hu',U),('nal',H),('ta',U),('ḥa',U),('mal',H),('mu',U),('sam',H),('maa',H),('bis',H),('mi',U),('hii',H))
put(26,'a',('wal',H),('laf',H),('ẓu',U),('wal',H),('maʿ',H),('naa',U),('sta',H),('qaa',H),('mal',H),('mam',H),('nuun',H))
put(27,'s',('ḥay',H),('yun',H),('ba',U),('yaa',H),('nul',H),('aw',H),('wa',U),('lii',H),('na',U),('wa',U),('aq',H),('fa',U),('rat',H))
put(27,'a',('ṣuḥ',H),('ful',H),('u',U),('laa',H),('fa',U),('gha',U),('dat',H),('kha',U),('raa',H),('ban',H),('mas',H),('kuun',H))
put(28,'s',('fa',U),('kha',U),('rar',H),('tu',U),('laa',H),('ʿaj',H),('zan',H),('fa',U),('qaṭ',H),('bal',H),('saj',H),('da',U),('tan',H))
put(28,'a',('wal',H),('ʿaj',H),('zu',U),('nus',H),('kii',H),('wal',H),('ja',U),('bii',H),('nul',H),('maṭ',H),('ḥuun',H))
put(29,'s',('maa',H),('zin',H),('tu',U),('bish',H),('shiʿ',H),('ril',H),('ki',U),('taa',H),('ba',U),('wa',U),('in',H),('na',U),('maa',H))
put(29,'a',('zaa',H),('nal',H),('qa',U),('rii',H),('ḍa',U),('fa',U),('khuṭ',H),('ṭa',U),('wah',H),('wal',H),('maw',H),('ṭuun',H))
put(30,'s',('wa',U),('ta',U),('laa',H),('ḥa',U),('qat',H),('su',U),('wa',U),('rul',H),('hu',U),('daa',H),('wa',U),('ka',U),('ʾan',H),('na',U),('haa',H))
put(30,'a',('qa',U),('ma',U),('run',H),('ya',U),('ʾuu',H),('bu',U),('i',U),('lal',H),('qa',U),('dii',H),('mil',H),('ʿur',H),('juun',H))
put(31,'s',('la',U),('ka',U),('yaa',H),('i',U),('laa',H),('hid',H),('dur',H),('ru',U),('an',H),('ta',U),('mu',U),('thii',H),('ru',U),('huu',H))
put(31,'a',('min',H),('luj',H),('ja',U),('tin',H),('wa',U),('a',U),('nal',H),('gha',U),('rii',H),('qul',H),('maḥ',H),('zuun',H))
put(32,'s',('wa',U),('ra',U),('jaʿ',H),('tu',U),('naḥ',H),('wal',H),('bad',H),('ʾi',U),('baʿ',H),('da',U),('khi',U),('taa',H),('mi',U),('hii',H))
put(32,'a',('fa',U),('qa',U),('raʾ',H),('tu',U),('huu',H),('wal',H),('khat',H),('mu',U),('bad',H),('ʾun',H),('maḥ',H),('ḍuun',H))

print("="*94)
print("CERT-10 INDEPENDENT SCAN — 32 prompt lines re-transcribed from phonemes")
print("="*94)
clean=0; faults=[]
for b in range(1,33):
    if b==15: continue
    so,sm,sb=scan_sadr(L[(b,'s')]); ao,am,ab=scan_ajuz_tamm(L[(b,'a')])
    ok=(so=='OK' and ao=='OK'); waqs=('WAQS' in so)or('WAQS' in ao)
    if ok: v='CLEAN'; clean+=1
    elif waqs and 'BREAK' not in so+ao: v='WAQS'; faults.append((b,'waqs',f's={so} a={ao}'))
    else: v='BREAK'; faults.append((b,'break',f's={so} a={ao}'))
    print(f"B{b:>2} s[{sm:<15}]{so:<7} a[{am:<13}]{ao:<6} -> {v}")
    if 'BREAK' in so: print(f"     ṣadr attempts: {sb}")
    if 'BREAK' in ao: print(f"     ʿajuz attempts: {ab}")
print(f"\nTĀMM lines CLEAN (all 31 except line 15): {clean}/31")
print("Faults:", faults if faults else "NONE")

print("\n"+"="*94); print("LINE 15 — majzūʾ al-Kāmil (2 feet/hemistich)"); print("="*94)
MAJD=['uu-u-','--u-','u-u-','uu-u--','--u--','u-u--','uu-u-u-','--u-u-','--u','-u-']
def scan_maj(sy):
    m=sk(sy); out=[]
    for f1 in HASHW:
        if m.startswith(f1) and m[len(f1):] in MAJD: out.append([f1,m[len(f1):]])
    return m,out
ms,mr=scan_maj(L[(15,'s')]); aS,ar=scan_maj(L[(15,'a')])
print(f"ṣadr  [{ms}] ({len(ms)} morae) -> {mr if mr else 'NO 2-foot majzūʾ parse'}")
print(f"ʿajuz [{aS}] ({len(aS)} morae) -> {ar if ar else 'NO 2-foot majzūʾ parse'}")
tamm_lens=[len(sk(L[(b,'s')])) for b in range(1,33) if b!=15]
print(f"\nTāmm ṣadr morae range: {min(tamm_lens)}-{max(tamm_lens)}; majzūʾ-15 ṣadr morae: {len(ms)}")

print("\n"+"="*94); print("īṭāʾ CHECK — 32 rhyme words"); print("="*94)
RH={1:'maknūn',2:'maghbūn',3:'madfūn',4:'maftūn',5:'makhzūn',6:'maʾmūn',7:'maqrūn',8:'mashḥūn',
9:'marhūn',10:'mawḍūn',11:'maḍmūn',12:'maṭʿūn',13:'mawhūn',14:'marṣūn',15:'sukūn',16:'maymūn',
17:'mawzūn',18:'maḍnūn',19:'maḥṣūn',20:'Bayyūn',21:'maẓnūn',22:'masjūn',23:'madyūn',24:'maʾfūn',
25:'nūn',26:'mamnūn',27:'maskūn',28:'maṭḥūn',29:'mawṭūn',30:'ʿurjūn',31:'maḥzūn',32:'maḥḍūn'}
seen={}; dups=[]
for b in range(1,33):
    r=RH[b]
    if r in seen: dups.append((b,r,seen[r]))
    else: seen[r]=b
print("words:", [RH[b] for b in range(1,33)])
print("\nDuplicate rhyme-words:", dups if dups else "NONE — all 32 distinct")
short=[b for b in range(1,33) if RH[b]=='sukūn']
print("short-penult closes:", short, "(sukūn = su-kūn, penult 'su' short) — legal ONLY as majzūʾ ḍarب")
