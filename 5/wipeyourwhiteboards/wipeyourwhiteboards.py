import math
def Euclide(a,b):
    pgcd=a
    p=[]
    while(b!=0):
        p+=[a//b]
        pgcd=b
        b=a%b
        a=pgcd
    c=1
    if(len(p)==1):
        return a,2,-(2*p[0]-1)
    d=-p[-2]
    for i in p[-3::-1]:
        t=c
        c=d
        d=t-i*d
    return pgcd,c,d

def SolvingProblem(a,b,p):
    pgcd,c,d=Euclide(a,b)
    e=p//pgcd
    c*=e;d*=-e
    k=max(math.ceil((1-c)*pgcd/b), math.ceil((1-d)*pgcd/a))
    print(f"{c+k*(b//pgcd)} {d+k*(a//pgcd)}")

for i in range(int(input())):
    a,b,c=map(int, input().split())
    SolvingProblem(a,-b,c)