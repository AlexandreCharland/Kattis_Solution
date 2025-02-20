for i in readlines()
    j=parse(Int,i)
    n=1
    cur=1
    mul=10%j
    t=1%j
    while (t!=0)
        cur=(cur*mul)%j
        t=(t+cur)%j
        n+=1
    end
    println(n)
end