n=int(input())
if(n<=2):
    print(0)
else:
    prime=[True for _ in range(n)]
    p=2
    while(p*p<n):
        if(prime[p]):
            for i in range(p*p,n,2*p):
                prime[i]=False
        p+=1
    t=2
    for p in range(3,n,2):
        t+=prime[p]*p
    print(t)