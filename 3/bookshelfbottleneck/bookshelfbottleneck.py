a,b=map(int,input().split())
s=0
pos=True
for i in range(a):
    t=sorted([int(i)for i in input().split()])
    if(t[1]<=b):
        s+=t[0]
    elif(t[0]<=b):
        s+=t[1]
    else:
        pos=False
        break
if(pos):
    print(s)
else:
    print("impossible")