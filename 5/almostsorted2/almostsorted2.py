input()
pprev=-1
prev=-1
stage=0
end=0
beg=0
for i in input().split():
    j=int(i)
    if(stage==0):
        if(prev>j):
            stage=1
            beg=pprev
            end=prev
        if(prev<j):
            pprev=prev
    elif(stage==1):
        if(prev<j):
            if(end<=j and prev>=beg):
                stage=2
            else:
                stage=3
                break
    elif(stage==2):
        if(prev>j):
            stage=3
            break
    prev=j
if(stage<3):
    if(stage==1 and prev<beg):
        print("No")
    else:
        print("Yes")
else:
    print("No")