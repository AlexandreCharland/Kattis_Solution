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

def SolvingProblem(s):
    l=len(s)
    d=prediv(l)
    prev=0
    cur=0
    pos=True
    tot=1
    for i in d:
        if(prev==i):
            if(pos):
                cur*=i
            else:
                continue
        else:
            cur=i
        m=l//cur
        sub=s[:m]
        for j in range(cur):
            pos=sub==s[j*m:(j+1)*m]
            if(not pos):
                break
        if(pos):
            tot*=i
        prev=i
    print(tot)

s=input()
while(s!="."):
    SolvingProblem(s)
    s=input()