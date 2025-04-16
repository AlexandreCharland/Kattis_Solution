for i in range(int(input())):
    a=input()
    b=input()
    val=True
    if(len(a)==len(b)):
        for i in range(len(a)):
            if(a[i]!=b[i]):
                if(a[i].isdigit() or b[i].isdigit()):
                    val=a[i]<b[i]
                elif(a[i].islower() and b[i].isupper()):
                    val=True
                elif(b[i].islower() and a[i].isupper()):
                    val=False
                else:
                    val=a[i]<b[i]
                break
    else:
        val=len(a)<len(b)
    if((a<b)==val):
        print("YES")
    else:
        print("NO")