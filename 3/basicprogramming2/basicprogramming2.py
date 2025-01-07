a,b=map(int,input().split())
t=input().split()
if(b==1):
    t=[int(i)for i in t]
    t.sort()
    i=0
    j=-1
    l=len(t)
    tab=[i for i in range(l)]
    while(t[tab[i]]+t[tab[j]]!=7777 and i<(l+j)):
        if(t[tab[i]]+t[tab[j]]<7777):
            i+=1
        else:
            j-=1
    if(i<(l+j)):
        print("Yes")
    else:
        print("No")
elif(b==2):
    t2=set(t)
    if(len(t2)!=len(t)):
        print("Contains duplicate")
    else:
        print("Unique")
elif(b==3):
    t=[int(i)for i in t]
    t.sort()
    i=len(t)//2
    if(len(t)%2==1):
        if(t[0]==t[i] or t[i]==t[-1]):
            print(t[i])
        else:
            print(-1)
    elif(len(t)==2):
        if(t[0]==t[1]):
            print(t[0])
        else:
            print(-1)
    else:
        if(t[0]==t[i] or t[i-1]==t[-1]):
            print(t[i])
        else:
            print(-1)
elif(b==4):
    t=[int(i)for i in t]
    t.sort()
    l=len(t)
    if(l%2==1):
        print(t[l//2])
    else:
        print(f"{t[l//2-1]} {t[l//2]}")
else:
    t=[i for i in t if 99<int(i) and int(i)<1000]
    t.sort()
    print(" ".join(t))