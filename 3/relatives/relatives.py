def prediv(num):
    d=[]
    while(num%2==0):
        num=num//2
        d+=[2]
    if(num==1):
        return d
    else:
        return d+div(3,num)

def div(start, num):
    d=start
    while(d**2<=num):
        if(num%d==0):
            a=div(d,num//d)
            return [d]+a
        else:
            d+=2
    return [num]

a=int(input())
while(a!=0):
    if(a==1):
        print(0)
    else:
        factor=prediv(a)
        prev=1
        val=1
        for i in factor:
            if(prev==i):
                val*=i
            else:
                val*=(i-1)
                prev=i
        print(val)
    a=int(input())