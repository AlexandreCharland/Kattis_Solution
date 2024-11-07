for i in range(int(input())):
    a,b=input().split()
    a=int(a);b=int(b)
    if(b<a):
        a,b=b,a
    c=a+b+1
    t=1
    j=2
    while(j<=c):
        if(j<=a):
            t+=j
        else:
            t+=min(a+1,c-j+1)
        j=j<<1
    print(t)