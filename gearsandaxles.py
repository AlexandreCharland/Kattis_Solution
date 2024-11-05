import math
n=int(input())
r=0
if n:
 g={}
 for i in range(n):
  s,c=map(int,input().split())
  if s not in g:g[s]=[]
  g[s].append(c)
 for v in g.values():v.sort();r+=sum(math.log(v[-1-i]/v[i])for i in range(len(v)//2))
print(r)