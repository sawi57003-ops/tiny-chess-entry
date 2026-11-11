import json,os,urllib.request as T
E=os.environ["MAKEFUN_ENV_URL"]
L=1.2e5
W=1e5
V=[0,100,320,330,500,900,0]
Q=(0,0,(31,33,14,18,-31,-33,-14,-18),(15,17,-15,-17),(1,-1,16,-16),(15,17,-15,-17,1,-1,16,-16),(1,-1,16,-16,15,17,-15,-17))
A=lambda s:(int(s[1])-1)*16+ord(s[0])-97
B=[0]*128
t=1;c=0;e=-1;w=4;b=116;n=0;F=0;Z=[]
def P(f):
 global B,t,c,e,w,b
 B=[0]*128;q=f.split();i=112
 for h in q[0]:
  if h=="/":i-=24
  elif h.isdigit():i+=int(h)
  else:
   v="PNBRQK".index(h.upper())+1
   if h>"Z":v=-v
   B[i]=v;i+=1
 w=B.index(6);b=B.index(-6)
 t=2*(q[1]=="w")-1
 c=sum(1<<i for i,k in enumerate("KQkq")if k in q[2])
 e=A(q[3])if q[3]!="-"else -1
def H(s,y):
 for z in(s-15*y,s-17*y):
  if not z&136 and B[z]==y:return 1
 for D,v in((Q[2],2),(Q[6],6)):
  for d in D:
   z=s+d
   if not z&136 and B[z]==v*y:return 1
 for d in Q[5]:
  z=s+d
  while not z&136 and not B[z]:z+=d
  if not z&136:
   p=B[z]
   if p==(3 if abs(d)in(15,17)else 4)*y or p==5*y:return 1
 return 0
def g(s):
 m=[]
 for q in range(128):
  if q&136:continue
  p=B[q]
  if not p or(p>0)!=(s>0):continue
  a=abs(p)
  if a==1:
   d=16*s;u=(7,0)[s<0];h=(1,6)[s<0]
   for z,k in((q+d,0),(q+d-1,1),(q+d+1,1)):
    if k and z&136:continue
    if k:
     if not((B[z]and(B[z]>0)!=(s>0))or z==e):continue
    elif B[z]:continue
    if(z>>4)==u:
     for v in(5,2,4,3):m.append(q|(z<<7)|(v<<14))
    else:m.append(q|(z<<7))
   if(q>>4)==h and not B[q+d]and not B[q+2*d]:m.append(q|((q+2*d)<<7))
  elif a in(2,6):
   for d in Q[a]:
    z=q+d
    if not z&136 and(not B[z]or(B[z]>0)!=(s>0)):m.append(q|(z<<7))
   if a==6:
    if s>0 and q==4:
     if c&1 and not B[5]and not B[6]and B[7]==4 and not H(4,-1)and not H(5,-1):m.append(4|(6<<7))
     if c&2 and not B[3]and not B[2]and not B[1]and B[0]==4 and not H(4,-1)and not H(3,-1):m.append(4|(2<<7))
    elif s<0 and q==116:
     if c&4 and not B[117]and not B[118]and B[119]==-4 and not H(116,1)and not H(117,1):m.append(116|(118<<7))
     if c&8 and not B[115]and not B[114]and not B[113]and B[112]==-4 and not H(116,1)and not H(115,1):m.append(116|(114<<7))
  else:
   for d in Q[a]:
    z=q+d
    while not z&136 and not B[z]:m.append(q|(z<<7));z+=d
    if not z&136 and B[z]and(B[z]>0)!=(s>0):m.append(q|(z<<7))
 return m
def K(m):
 global t,c,e,w,b
 Z.append((B[:],c,e,w,b,t))
 f=m&127;z=(m>>7)&127;r=m>>14;p=B[f]
 if abs(p)==1 and z==e and not B[z]:
  x=z-16*p;B[x]=0
 B[z]=r*p if r else p
 B[f]=0
 if abs(p)==6 and abs(z-f)==2:
  i,j=(z-1,z+1)if z>f else(z+1,z-2);B[i]=B[j];B[j]=0
 if abs(p)==6:
  if p>0:w=z
  else:b=z
 if p==6:c&=~3
 elif p==-6:c&=~12
 for k in(f,z):c&=~{0:2,7:1,112:8,119:4}.get(k,0)
 e=-1
 if abs(p)==1 and abs(z-f)==32:e=(f+z)//2
 t=-t
def U():
 global t,c,e,w,b
 B[:],c,e,w,b,t=Z.pop()
def Y():
 s=0
 for q in range(128):
  if q&136:continue
  p=B[q]
  if p:
   a=abs(p);v=V[a];f=q&7;r=q>>4
   if a==1:v+=(r if p>0 else 7-r)*6
   elif a in(2,3):v+=(7-abs(f-3)-abs(r-3))*2
   s+=v if p>0 else -v
 return s
def s(d,p,q):
 global n,F
 n+=1
 if n>L:F=1;return 0
 if d<=0:
  v=Y() if t>0 else -Y()
  if v>=q:return q
  if v>p:p=v
 m=g(t)
 m.sort(key=lambda x:-V[abs(B[x>>7&127])])
 l=0
 for mv in m:
  z=(mv>>7)&127
  if d<=0 and not B[z] and not(mv>>14)and z!=e:continue
  K(mv)
  if H((b,w)[t<0],t):U();continue
  l+=1
  v=-s(d-1,-q,-p)
  U()
  if F:return 0
  if v>p:p=v
  if p>=q:break
 if l==0 and d>0:return -W if H((b,w)[t>0],-t) else 0
 return p
def R(L):
 global n,F
 v=[A(x[:2])|(A(x[2:4])<<7)|("nbrq".index(x[4])+2 if len(x)==5 else 0)<<14 for x in L]
 n=0;F=0;h=v[0]
 for d in range(1,10):
  if F:break
  a=-W-1;k=h
  for mv in v:
   K(mv);x=-s(d-1,-W-1,-a);U()
   if F:break
   if x>a:a=x;k=mv
  if not F:h=k;v.remove(h);v.insert(0,h)
 return h
def q(p,j):
 return json.load(T.urlopen(E+p,json.dumps(j).encode()))
def C(m):
 r=m>>14
 return "".join(chr(97+(x&7))+str((x>>4)+1)for x in(m&127,(m>>7)&127))+("nbrq"[r-2] if r else "")
while 1:
 G=q("/game",{})
 if"game"not in G:break
 while"legal_moves"in G:
  if not G["legal_moves"]:break
  P(G["fen"]);G=q("/move",{"game":G["game"],"move":C(R(G["legal_moves"]))})
