# What is the first triangle number to have over five hundred divisors?
# for this we wil use dynamic programming

def triGen():
    total = 0
    for i in range(100000000000):
        total = i + total
        yield total

def countDivisors(N):
    n_divisors = 0
    for n in range(1, N//2  + 1):
        if N%n == 0:
            n_divisors += 1
    return n_divisors

tri = triGen()

def printTri(num):
    for j in range(num):
        l=[]
        for i in range(10):
            l.append(next(tri))
        print(l)
printTri(10)


"""
tri = triGen()
n_divisors = 0
while n_divisors < 500:
    N = next(tri)
    n_divisors = countDivisors(N)
    print(N, n_divisors)

print(N)
"""
