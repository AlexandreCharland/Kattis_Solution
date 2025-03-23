l=[]
h=[]
a,b=map(int,input().split())
for i in range(1,b+1):
    c,d=map(int,input().split())
    if(c<d):
        l+=[str(i)]
    else:
        h+=[str(i)]
if(len(l)<=len(h)):
    print(len(l))
    if(len(l)!=0):
        print("\n".join(l))
else:
    print(len(h))
    if(len(h)!=0):
        print("\n".join(h))