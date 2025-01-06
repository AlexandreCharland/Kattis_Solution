for _ in range(int(input())):
    a,b=input().split();b=int(b)
    c=0
    d=[]
    while(c!=b):
        e=list(map(int,input().split()))
        c+=len(e)
        d+=e
    s=sorted(d)
    j=0
    for i in d:
        j+=(s[j]==i)
    print(f"{int(a)} {b-j}")