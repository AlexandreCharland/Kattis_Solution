import sys
a=sys.stdin.readlines()
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
for i in a:
    n=int(i)
    if(n<0):
        s=["-1"]
        n*=-1
    else:
        s=[]
    fact=prediv(n)
    prev=fact[0]
    oc=0
    for j in fact:
        if(j==prev):
            oc+=1
        else:
            if(oc>1):
                s+=[str(prev)+"^"+str(oc)]
            else:
                s+=[str(prev)]
            prev=j
            oc=1
    if(oc>1):
        s+=[str(prev)+"^"+str(oc)]
    else:
        s+=[str(prev)]
    print(" ".join(s))
