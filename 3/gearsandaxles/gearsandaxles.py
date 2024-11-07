import math
n = int(input())
res=0
if(n!=0):
    gears = {}
    for i in range(n):
        size_teeth,count_teeth = map(int, input().split())
    
        if size_teeth not in gears:
            gears[size_teeth] = []
        gears[size_teeth].append(count_teeth)
    for v in gears.values():
        v.sort(reverse=True)
        for i in range(len(v)//2):
            res+=math.log(v[i]/v[-1-i])
print(res)