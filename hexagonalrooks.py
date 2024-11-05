def transformCoord(a):
    l=ord(a[0])-97
    c=int(a[1:])+max(l-5,0)-1
    return [l,c]

def inBounds(c,d):
    if(c<0):
        return False
    if(c<=5):
        return (d-c)<=5 and d>=0
    else:
        return d<=10 and (c-5)<=d and c<11

def Parcour(dir, c1):
    dirx=dir[0]
    diry=dir[1]
    curx=c1[0]
    cury=c1[1]
    t=[]
    while(inBounds(curx,cury)):
        t+=[[curx,cury]]
        curx+=dirx
        cury+=diry
    s=[]
    curx=c1[0]
    cury=c1[1]
    while(inBounds(curx,cury)):
        s+=[[curx,cury]]
        curx-=dirx
        cury-=diry
    return t[1:]+s[1:]

a,b=input().split()
c1=transformCoord(a)
c2=transformCoord(b)
pos=[]
for dir in [[1,1],[0,1],[1,0]]:
    pos+=Parcour(dir,c1)
n=0
for i in pos:
    cx=c2[0]-i[0]
    cy=c2[1]-i[1]
    if(cy==0 and cx == 0):
        continue
    elif(cx==cy):
        n+=1
    elif(cx == 0):
        n+=1
    elif(cy ==0):
        n+=1
print(n)