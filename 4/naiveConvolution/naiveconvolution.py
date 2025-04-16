a,b=map(int,input().split())
p1=[int(i)for i in input().split()]
p2=[int(i)for i in input().split()]
l=a+b-1
s=[0]*l
for i in range(a):
    for j in range(b):
        s[i+j]+=p1[i]*p2[j]
c=1
for i in range(1,l):
    if(s[-i]!=0):
        c=l-i+1
        break
print(" ".join(map(str,s[:c])))