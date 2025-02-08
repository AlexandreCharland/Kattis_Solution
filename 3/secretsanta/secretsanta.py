import math
def f(cur,chois):
    if(len(cur)==len(chois)):
        return 1
    else:
        t=0
        for i in range(len(chois)):
            if(chois[i] and i!=len(cur)):
                chois[i]=False
                t+=f(cur+[i],chois)
                chois[i]=True
        return t

def g(n):
    if(n==1):
        return 1
    else:
        return n*g(n-1)
n=int(input())
if(n<=10):
    print(1-f([],[True]*n)/g(n))
else:
    print("0.63212056")