def inc(sol):
    newSol=[]
    for i in sol:
        if(i==1):
            newSol+=[0]
        else:
            newSol+=[1]
            break
    newSol+=sol[len(newSol):]
    return newSol,sum(newSol)

def test(b,sol):
    return ((b[0]+sol[0]+sol[1]+sol[3])%2)*((b[1]+sol[0]+sol[1]+sol[2]+sol[4])%2)*((b[2]+sol[1]+sol[2]+sol[5])%2)*((b[3]+sol[0]+sol[3]+sol[4]+sol[6])%2)*((b[4]+sol[1]+sol[3]+sol[4]+sol[5]+sol[7])%2)*((b[5]+sol[2]+sol[4]+sol[5]+sol[8])%2)*((b[6]+sol[3]+sol[6]+sol[7])%2)*((b[7]+sol[4]+sol[6]+sol[7]+sol[8])%2)*((b[8]+sol[5]+sol[7]+sol[8])%2)


def SolvingProblem(a):
    sol=[0,0,0,0,0,0,0,0,0]
    b=[]
    for i in a:
        b+=[i=="."]
    best=9
    for _ in range(2**9):
        c=b.copy()
        sol,a=inc(sol)
        if(a<best):
            if(test(b,sol)):
                best=a
    print(best)

for i in range(int(input())):
    SolvingProblem(input()+input()+input())