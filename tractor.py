for _ in" "*int(input()):
 a,b=map(int,input().split());m=min(a,b);c=a+b+2;t=1;j=2
 while(j<c):t+=[min(m+1,c-j),j][j<=m];j*=2
 print(t)