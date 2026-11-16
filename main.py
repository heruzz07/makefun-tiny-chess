import json,os,urllib.request as u
H=os.environ.get("MAKEFUN_ENV_URL") or exit(1)
def P(a,b):
 try:
  with u.urlopen(H+a,json.dumps(b).encode()) as r:return json.load(r)
 except:exit(1)
V=[100,320,330,500,900,0]
KN=[33,31,18,14,-14,-18,-31,-33]
KI=[1,-1,16,-16,15,17,-15,-17]
BI=KI[4:];RI=KI[:4]
ST=[[],[],KN,BI,RI,KI,KI]
J=['BBBBBBBBDGG88GGDD@=BB=@DBBBLLBBBDDGNNGDDGGLQQLGG[[[[[[[[BBBBBBBB',').3333.).8BBBB8.3BGJJGB33DJLLJD33BJLLJB33DGJJGD3.8BDDB8.).3333.)','B'*64,'B'*64,'B'*64,'3..))..33..))..33..))..33..))..3833..338=888888=LLBBBBLLLQGBBGQL']
T=[]
for x in J:
 t=[0]*128
 for i in range(64):t[i//8*16+i%8]=2*ord(x[i])-132
 T.append(t)
CM={0:2,7:1,4:3,112:8,119:4,116:12}
SQ=[r*16+f for r in range(8)for f in range(8)]
N=[0]
B=100000
class X(Exception):pass
def A(b,s,q):
 for o in(15,17):
  j=q-o*s
  if not j&0x88 and b[j]==s:return 1
 for o in KN:
  j=q+o
  if not j&0x88 and b[j]==2*s:return 1
 for o in KI:
  j=q+o
  if not j&0x88 and b[j]==6*s:return 1
 for o in KI:
  j=q+o
  while not j&0x88:
   if b[j]:
    if b[j]==5*s or b[j]==(3*s if abs(o)in(15,17) else 4*s):return 1
    break
   j+=o
 return 0
def G(b,s,c):
 m=[];w=s>0;pr=w*7;sr=6-5*w
 for i in SQ:
  p=b[i]
  if not p or(p>0)!=w:continue
  t=abs(p)
  if t==1:
   d=16*s;j=i+d;tg=[]
   if not j&0x88 and not b[j]:
    tg.append(j)
    if i>>4==sr and not b[i+2*d]:tg.append(i+2*d)
   for o in(d-1,d+1):
    j=i+o
    if not j&0x88 and b[j] and(b[j]>0)!=w:tg.append(j)
   for j in tg:
    if j>>4==pr:
     for q in(5,4,3,2):m.append(i|j<<7|q<<14)
    else:m.append(i|j<<7)
  else:
   for o in ST[t]:
    j=i+o
    while not j&0x88:
     if b[j]:
      if(b[j]>0)!=w:m.append(i|j<<7)
      break
     m.append(i|j<<7)
     if t in(2,6):break
     j+=o
 h=0 if w else 112;r=1 if w else 4
 if c&r and not b[h+5]and not b[h+6]and not A(b,-s,h+4)and not A(b,-s,h+5):m.append(h+4|(h+6)<<7)
 if c&r*2 and not b[h+3]and not b[h+2]and not b[h+1]and not A(b,-s,h+4)and not A(b,-s,h+3):m.append(h+4|(h+2)<<7)
 return m
def Y(b,m,c,w,k):
 n=b[:];f=m&127;t=m>>7&127;q=m>>14&7;p=n[f]
 if abs(p)==6 and abs(t-f)==2:
  r=f+3 if t>f else f-4;n[f+1 if t>f else f-1]=n[r];n[r]=0
 n[t]=q*p//abs(p)if q else p;n[f]=0
 if p==6:w=t
 elif p==-6:k=t
 return n,c&~CM.get(f,0)&~CM.get(t,0),w,k
def E(b,w,k):
 s=0
 for i in SQ:
  p=b[i]
  if p:
   t=abs(p);v=V[t-1]+T[t-1][i if p>0 else i^112];s+=v*(p>0 or -1)
 if abs(s)>800:
  s+=10*(7-max(abs((w>>4)-(k>>4)),abs((w&7)-(k&7))))*s//abs(s)
 return s
def O(b,ms):
 return sorted(ms,key=lambda m:10000+V[abs(b[m>>7&127])-1]*10-V[abs(b[m&127])-1] if b[m>>7&127] else 0,reverse=True)
def S(b,s,d,a,be,c,w,k):
 N[0]+=1
 if N[0]>B:raise X
 ck=A(b,-s,w if s>0 else k)
 if d<=0:
  st=E(b,w,k)*s
  if st>=be:return be
  if st>a:a=st
  ms=G(b,s,c)if ck else[m for m in G(b,s,c)if b[m>>7&127]or m>>14]
 else:ms=G(b,s,c)
 bs=-99999;n=0
 for m in O(b,ms):
  nn,nc,w2,k2=Y(b,m,c,w,k)
  if A(nn,-s,w2 if s>0 else k2):continue
  n+=1
  v=-S(nn,-s,d-1,-be,-a,nc,w2,k2)
  if v>bs:bs=v
  if v>a:a=v
  if a>=be:return a
 if not n:return -99999 if ck else(a if d<=0 else 0)
 return bs if d>0 else a
def F(f):
 z=f.split();b=[0]*128;q=112;w=k=-1
 for c in z[0]:
  if c=='/':q-=24
  elif c.isdigit():q+=int(c)
  else:
   p=('PNBRQK'.find(c.upper())+1)*(c.isupper()or -1);b[q]=p
   if p==6:w=q
   elif p==-6:k=q
   q+=1
 s=1 if z[1]=='w' else -1
 c=sum(1<<'KQkq'.find(ch) for ch in z[2] if ch in'KQkq')
 return b,s,c,w,k
def R(b,s,c,w,k):
 ms=[]
 for m in G(b,s,c):
  n,nc,w2,k2=Y(b,m,c,w,k)
  if not A(n,-s,w2 if s>0 else k2):ms.append(m)
 bm=ms[0];N[0]=0
 for d in range(1,99):
  try:
   a=cs=-999999;cb=bm
   for m in O(b,ms):
    n,nc,w2,k2=Y(b,m,c,w,k)
    v=-S(n,-s,d-1,-999999,-a,nc,w2,k2)-30*(tuple(n)in Hs)
    if v>cs:cs=v;cb=m
    if v>a:a=v
   bm=cb
  except X:break
 f=bm&127;t=bm>>7&127;q=bm>>14&7
 Hs.add(tuple(Y(b,bm,c,w,k)[0]))
 return chr(97+(f&7))+str((f>>4)+1)+chr(97+(t&7))+str((t>>4)+1)+(''if not q else 'nbrq'[q-2])
while True:
 g=P('/game',{})
 if g['status']=='done':break
 Hs=set()
 while g['status']=='your_move':
  b,s,c,w,k=F(g['fen']);g=P('/move',{'game':g['game'],'move':R(b,s,c,w,k)})
