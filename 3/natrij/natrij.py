a=[int(i)for i in input().split(":")]
b=[int(i)for i in input().split(":")]
c=[]
if(a[2]>b[2]):
    a[1]+=1
c+=[(b[2]-a[2])%60]
if(a[1]>b[1]):
    a[0]+=1
c+=[(b[1]-a[1])%60]
c+=[(b[0]-a[0])%24]
if(c==[0,0,0]):
    c[2]=24
s=""
for i in c[::-1]:
    if(i<10):
        s+="0"
    s+=str(i)+":"
print(s[:-1])