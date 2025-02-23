a,b=map(int,input().split())
def f(move,t,n):
    if(n==b):
        return 1
    for i in range(a-1):
        if(move[i]):
            move2=move.copy()
            move2[i]=0
            t2=t.copy()
            t2[i]=0
            t2[i+1]=2
            if(i>0):
                if(t2[i-1]>0):
                    move2[i-1]=1
            if(i<a-2):
                if(t2[i+2]<2):
                    move2[i+1]=1
            if(f(move2,t2,n+1)):
                return 1
    return 0

c={"R":0,"F":1,"L":2}
t=[]
cur=0
move=[0]*(a-1)
for i,j in enumerate(input()):
    right=c.get(j)
    if(cur>0 and right<2):
        move[i-1]=1
    t+=[right]
    cur=right
print(f(move,t,0))