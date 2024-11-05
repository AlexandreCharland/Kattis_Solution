N=int(input())
n=list(map(int,input().split()))
o=input().split()
p=list(map(int,o))
Prod1=1
Prod2=1
Tot1=0
Tot2=0
j1=0
h=[]
for k in range(N):
    i=n[k]
    j=p[k]
    Prod1=(Prod1*i)%300017
    Prod2=(Prod2*j)%300017
    Tot1=(Tot1+i)%300017
    Tot2=(Tot2+j)%300017
    if(Prod1==Prod2 and Tot1==Tot2):
        h+=o[j1:k+1]+["#"]
        j1=k+1
        Prod1=1
        Prod2=1
        Tot1=0
        Tot2=0
print(" ".join(h[:-1]))