t=0
for i in range(1,int(input())+1):
    t=(t+pow(i,i,10000000000))%10000000000
print(t)