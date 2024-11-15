def f(mot,dispo,best,i,curScore):
    if(i<0):
        return max(best,curScore)
    elif(i+curScore-best<0):
        return best
    else:
        new = dispo.copy()
        for j in mot[i]:
            if(new[j]==0):
                return f(mot,dispo,best,i-1,curScore)
            new[j]=0
        best=f(mot,new,best,i-1,curScore+1)
        return f(mot,dispo,best,i-1,curScore)


p,t = map(int, input().split())
dispo=[1]*p
name=[]
for i in range(t):
    cur=[]
    add=True
    for j in input():
        val=ord(j)-65
        if(val>=p or val in cur):
            add=False
            break
        cur+=[val]
    if(add):
        name+=[cur]
print(f(name,dispo,0,len(name)-1,0))