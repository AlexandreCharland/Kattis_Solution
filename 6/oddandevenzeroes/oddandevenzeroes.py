import math

gt=[4]
def g(k):
    global gt
    l=len(gt)
    while(k>=l):
        if(l%2):
            gt+=[gt[-1]//2]
        else:
            gt+=[gt[-2]*5-10]
        l+=1
    return gt[k]

ut=[1]
def u(k):
    global ut
    l=len(ut)-1
    while(k>l):
        if(l%2):
            ut+=[(ut[-1]-2*(5**(l//2)))*5]
        else:
            ut+=[ut[-1]*5]      
        l+=1
    return ut[k]

def d(k):
    if(k%2):
        return 5**k
    else:
        return 5**k + 5**(k//2)

def t(k):
    if(k==1):
        return 10
    elif(k%2==0):
        return (g(k)-1)*5**(k//2)
    else:
        return (g(k)-1)*2*5**((k+1)//2)

def f(base,nombre):
    s=1
    if(base==[]):
        return 1
    a=base[0]
    k=len(base)-1
    #if(k==0):
    #    val=a+1
    if(a==0):
        val = 0
    elif(a==1):
        val = u(k)
        s=-1
    elif(a==2):
        val = d(k)
    elif(a==3):
        val = t(k)
        s=-1
    else:
        val = 2*d(k)
    if(s**k==-1):
        return val + 1+nombre[0] - f(base[1:],nombre[1:])
    else:
        return val + f(base[1:],nombre[1:])

def decompose(n):
    if(n==0):
        return [],[]
    k=math.floor(math.log(n,5))
    powow=5**k
    base=[]
    nombre=[]
    while(powow>0):
        a=n//powow
        base+=[a]
        n-=a*powow
        nombre+=[n]
        powow=powow//5
    return base,nombre
n=int(input())
while(n!=-1):
    base,nombre=decompose(n)
    print(f(base,nombre))
    n=int(input())