def Collatz(n):
    if n in distToOne:
        return distToOne[n]
    elif n % 2 == 0:
        distToOne[n] =  1 + Collatz(n/2)
        return distToOne[n]
    else:
        distToOne[n] =  1 + Collatz(3*n + 1)
        return distToOne[n]

distToOne = {1:0, 0:0} #A dynamic programming approach!
for n in range(1000000):
    Collatz(n)
    #print(n, Collatz(n))

res = dict((v,k) for k,v in distToOne.items())
print(res[524])
