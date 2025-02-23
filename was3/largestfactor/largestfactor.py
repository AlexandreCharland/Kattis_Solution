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

print(prediv(int(input()))[-1])