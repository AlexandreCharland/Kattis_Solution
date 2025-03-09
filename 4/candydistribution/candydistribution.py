def pgcd(a,b):
    if(b==0):
        return a
    else:
        return pgcd(b,a%b)
for _ in range(int(input())):
    k,c=map(int,input().split())
    if(pgcd(k,c)!=1):
        print("IMPOSSIBLE")
    elif(k==1):
        print(2)
    elif(c==1):
        print(k+1)
    else:
        x=pow(c,-1,k)
        print(x)