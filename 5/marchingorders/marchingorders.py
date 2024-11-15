primal=[2,3,2,5,1,7,2,3, 1,11, 1,13, 1, 1, 2,17, 1,19, 1]
div   =[1,1,2,1,6,1,4,3,10, 1,12, 1,14,15, 8, 1,18, 1,20]
inv   =[1,2,1,3,1,2,1,1, 1, 1, 1,10, 1, 1, 1, 7, 1,15, 1]
input()
order = input()[::-1]
corps=1
leftover=0
t=[order[0]]
Pos=True
for k,i in enumerate(order[1:]):
    ajout = True
    l=len(t)
    for j in range(l):
        if t[j] > i:
            val=(j-leftover)%(l+1)
            if(val/div[k]==val//div[k]):
                leftover+=corps*((val*inv[k]//div[k])%(l+1))
            else:
                Pos=False
            corps*=primal[k]
            t.insert(j, i)
            ajout = False
            break
    if ajout:
        val=(l-leftover)%(l+1)
        if(val/div[k]==val//div[k]):
            leftover+=corps*((val*inv[k]//div[k])%(l+1))
        else:
            Pos=False
        corps*=primal[k]
        t.append(i)

if(Pos):
    print("YES")
    print(leftover)
else:
    print("NO")