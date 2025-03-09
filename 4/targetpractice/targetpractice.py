import math
def generateDict(a,b,points):
    c={}
    for i in points:
        if(b==i[1]):
            r=(math.inf,0)
        else:
            p=(a-i[0])/(b-i[1])
            q=b-a*p
            r=(p,q)
        if(r not in c):
            c[r]=[[i[0],i[1]]]
        else:
            c[r]+=[[i[0],i[1]]]
    return c

n=int(input())
if(n<=4):
    print("success")
else:
    a,b=map(int,input().split())
    l=[]
    for i in range(n-1):
        c,d=map(int,input().split())
        l+=[[c,d]]
    m=2
    pos=True
    l1=[]
    for i in generateDict(a,b,l).values():
        if(len(i)>1):
            m-=1
            if(m==0):
                pos=False
                break
        else:
            l1+=i
    if(m==1):
        if(len(l1)<=2):
            print("success")
        else:
            a,b=l1.pop()
            c=generateDict(a,b,l1)
            if(len(c)!=1):
                print("failure")
            else:
                print("success")
    elif(m==2):
        if(len(l1)<=2):
            print("success")
        else:
            a,b=l1.pop()
            c=generateDict(a,b,l1)
            if(len(c)==1):
                print("success")
            elif(len(c)>2):
                print("failure")
            else:
                l2=[]
                for i in c.values():
                    l2+=[i]
                if(len(l2[0])==1 or len(l2[1])==1):
                    print("success")
                else:
                    print("failure")
    else:
        print("failure")