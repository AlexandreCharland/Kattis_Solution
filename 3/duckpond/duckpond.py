a,b=map(int,input().split())
c=-1
t=[i for i in range(a)]
s=["0"]*a
for i in range(a):
    c=(c+b)%(a-i)
    s[t.pop(c)]=str(i+1)
    c-=1
print(" ".join(s))