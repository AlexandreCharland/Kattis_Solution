for i in range(int(input())):
    t=1
    t2=1
    for _ in range(int(input())):
        p,v=map(int,input().split())
        t=(t*(((p**v)-1)//(p-1)+(v+1)*p**v))%1000000007
        t2=(t2*(p**v))%1000000007
    print(f"Case {i+1}: {(t+t2)%1000000007}")