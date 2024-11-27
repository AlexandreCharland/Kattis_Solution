a,b=map(int,input().split())
count={}
h=0
t=0
for i in map(int,input().split()):
    val=i//b
    if(val not in count):
        count[val]=1
    else:
        count[val]+=1
t=0
for i in count.values():
    t+=(i*(i-1))>>1
print(t)