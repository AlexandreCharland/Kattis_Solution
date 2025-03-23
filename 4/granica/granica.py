a=[]
m1=1000000001
m2=1000000002
for i in" "*int(input()):
    j=int(input())
    a+=[j]
    if(j<m1):
        m2=m1
        m1=j
    elif(j<m2):
        m2=j
def pgcd(x, y):
    if(y==0):
        return x
    else:
        return pgcd(y,x%y)
m=m2-m1
for i in range(len(a)):
    for j in range(i+1,len(a)):
        m=pgcd(m,abs(a[i]-a[j]))  
def div(m):
    res=[]
    d=1
    while(d**2<=m):
        if(m%d==0):
            if(d!=1):
                res.append(str(d))
            if(d**2!=m):
                res.append(str(m//d))
        d+=1
    return res
print(" ".join(div(m)))