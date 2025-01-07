n,m=map(int,input().split())
p=[]
for i in range(n):
    p+=[[100]*m]

inp=[]
for i in range(n):
    inp+=[input()]

info=[0]*m
for i in range(n):
    for j in range(m):
        if(inp[i][j]=="T"):
            info[j]=min(p[i][j],info[j]+1)
            p[i][j]=info[j]
        else:
            p[i][j]=0
            info[j]=0

info=[0]*m
for k in range(n):
    i=n-1-k
    for j in range(m):
        if(inp[i][j]=="T"):
            info[j]=min(p[i][j],info[j]+1)
            p[i][j]=info[j]
        else:
            p[i][j]=0
            info[j]=0

info=[0]*n
for j in range(m):
    for i in range(n):
        if(inp[i][j]=="T"):
            info[i]=min(p[i][j],info[i]+1)
            p[i][j]=info[i]
        else:
            p[i][j]=0
            info[i]=0
mx=0
info=[0]*n
for k in range(m):
    j=m-1-k
    for i in range(n):
        if(inp[i][j]=="T"):
            info[i]=min(p[i][j],info[i]+1)
            p[i][j]=info[i]
            mx=max(p[i][j],mx)
        else:
            p[i][j]=0
            info[i]=0

if(mx<10):
    for i in range(n):
        s=""
        for j in range(m):
            s+="."
            if(p[i][j]==0):
                s+="."
            else:
                s+=str(p[i][j])
        print(s)
else:
    for i in range(n):
        s=""
        for j in range(m):
            s+="."
            if(p[i][j]==0):
                s+=".."
            elif(p[i][j]<10):
                s+="."+str(p[i][j])
            else:
                s+=str(p[i][j])
        print(s)