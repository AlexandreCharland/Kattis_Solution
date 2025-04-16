n=int(input())
m=int(input())
if(m%2!=0):
    print("Rong talning")
else:
    l=(m-2*n)//2
    if(l>n or l<0):
        print("Rong talning")
    else:
        print(l)