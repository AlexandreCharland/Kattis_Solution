a=0
b=0
c=0
m=1
for i in input():
    if(i=="A"):
        a+=1
    elif(i=="B"):
        b+=1
    else:
        c+=1
    m=max(m,abs(a-b),abs(a-c),abs(b-c))
print(m)