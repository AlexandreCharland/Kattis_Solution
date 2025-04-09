a,b,c=map(int,input().split())
v=str((a*b*(10**15))//c)
if(len(v)<=15):
    print("0."+"0"*(15-len(v))+v)
else:
    print(v[:-15]+"."+v[-15:])