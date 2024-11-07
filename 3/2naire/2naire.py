def f(n,t):
    e=1
    i=0
    while(1/(2*e)>=t and i<n):
        i+=1
        e=(1/(4*e)+e-t)/(1-t)
    e*=(1+t)**(n-i)
    return e
a,b=input().split()
a=int(a);b=float(b)
while(a!=0):
    res=f(a,b)
    print(f"{res:.3f}")
    a,b=input().split()
    a=int(a);b=float(b)