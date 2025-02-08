for i in range(int(input())):
    a,b=input().split()
    a=int(a)
    b=int(b)
    e=pow(a,(b-1)//2,b)
    if(e==b-1 and a%b!=0):
        print("no")
    else:
        print("yes")