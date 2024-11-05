n,m=map(int,input().split())
E=[int(input())for _ in" "*(n+m)]
d=[[0]*(m+1)for _ in" "*(n+1)]
for i in range(n):
 for j in range(m):s=abs(E[i]-E[n+j]);d[i+1][j+1]=max(d[i][j+1],d[i+1][j],(d[i][j]+(s<16)+2*((s<24)+(s<44)+1))*(s<103))
print(d[n][m])