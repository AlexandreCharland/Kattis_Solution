a,b=map(int,input().split())
t=[]
s=[1]*a
for i in range(b):
    j=int(input())
    t+=[j]
    s[j-1]=0
f=0
p2=[]
for i in t:
    p=[str(i)]
    j=i-2
    p2+=[str(j+1)for j in range(f,i-1) if s[j]==1]+[str(i)]
    f=max(f,i)
p2+=[str(i+1)for i in range(f,a)]
print("\n".join(p2))