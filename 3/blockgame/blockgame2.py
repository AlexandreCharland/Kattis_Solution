def f(a,b):
    if(b%a==0 or b>2*a):
        return True
    else:
        return not f(b-a, a)

a,b=input().split()
a=int(a);b=int(b)
if(f(min(a,b),max(a,b))):
    print('win')
else:
    print('lose')