s=input()
i=1
while(s!="END"):
    ind=s.find(".")
    while(s[ind]!="*"):
        ind+=1
    if(ind==-1):
        print(f"{i} EVEN")
    elif(s[1]=="*" or len(s)%(ind)!=1):
        print(f"{i} NOT EVEN")
    else:
        pat=s[:ind]
        pos=True
        for j in range((len(s)-1)//ind):
            if(pat!=s[j*ind:(j+1)*ind]):
                pos=False
                break
        if(pos):
            print(f"{i} EVEN")
        else:
            print(f"{i} NOT EVEN")
    s=input()
    i+=1