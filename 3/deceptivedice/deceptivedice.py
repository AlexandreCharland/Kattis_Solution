import math
def f(n,k):
    if(k==1):
        return (n+1)/2
    else:
        v=f(n,k-1)
        vf=math.floor(v)
        c=vf*v/n
        d=(n*(n+1)-vf*(vf+1))/(2*n)
        return c+d
a,b=map(int,input().split())
print(f(a,b))