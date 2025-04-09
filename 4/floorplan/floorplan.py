n=int(input())
r=n%4
v=n//4
if(r==0):
    print(f"{v+1} {v-1}")
elif(r==1):
    print(f"{2*v+1} {2*v}")
elif(r==2):
    print("impossible")
else:
    print(f"{2*v+2} {2*v+1}")