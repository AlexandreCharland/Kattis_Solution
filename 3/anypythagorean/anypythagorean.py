def inc(sol):
    newSol=[]
    for i in sol:
        if(i==2):
            newSol+=[0]
        else:
            newSol+=[i+1]
            break
    newSol+=sol[len(newSol):]
    return newSol

def prediv(num):
    d=[]
    while(num%2==0):
        num=num//2
        d+=[2]
    if(num==1):
        return d
    else:
        return d+div(3,num)

def div(start, num):
    d=start
    while(d**2<=num):
        if(num%d==0):
            a=div(d,num//d)
            return [d]+a
        else:
            d+=2
    return [num]

n=int(input())
if(n%2==1):
    print("0 0 0")
else:
    n=n//2
    p=prediv(n)
    pos=False
    c=[0]*len(p)
    a=1
    b=1
    for _ in range(3**len(p)):
        a=1
        b=1
        for i,j in enumerate(c):
            if(j==2):
                a*=p[i]
            elif(j==1):
                b*=p[i]
        u=min(a,b)
        v=max(a,b)-u
        if(v<u and v!=0):
            pos=True
            break
        else:
            c=inc(c)
    if(pos):
        t=sorted([u**2-v**2,2*u*v,u**2+v**2])
        s=1
        for i,j in enumerate(c):
            if(j==0):
                s*=p[i]
        print(f"{s*t[0]} {s*t[1]} {s*t[2]}")
    else:
        print("0 0 0")