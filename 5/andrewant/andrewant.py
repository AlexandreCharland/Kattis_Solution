import sys
a=sys.stdin.readlines()
i=0
def sol(f,i):
    l=[]
    for j in f[::i]:
        l+=[j[0]]
        if(j[1]!=i):
            l.pop(0)
    return l[0]


while(i<len(a)):
    d,n=map(int,a[i].split())
    f=[]
    lead=[-1,-1]
    i+=1
    for j in range(n):
        p,dir=a[i].split()
        p=int(p)
        i+=1
        if(dir=="R"):
            f+=[[p,1]]
            m1=d-p
            if(m1>lead[0]):
                lead[0]=m1
        else:
            f+=[[p,-1]]
            if(p>lead[1]):
                lead[1]=p
    f.sort(key=lambda x : x[0])
    if(lead[0]==lead[1]):
        m=lead[0]
        p=sol(f,1)
        q=sol(f,-1)
        s=f"{min(p,q)} and {max(p,q)}."
    elif(lead[0]>lead[1]):
        m=lead[0]
        s=str(sol(f,1))+"."
    else:
        m=lead[1]
        s=str(sol(f,-1))+"."
    print(f"The last ant will fall down in {m} seconds - started at "+s)