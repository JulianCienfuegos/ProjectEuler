upper = 2000000
numbers = range(upper)
numbers[1] = 0 # 1 isn't prime
sum = 0 
for n in range(upper):
    if (numbers[n]!=0):
        sum += n
        numbers[::n] = [0]*len(numbers[::n])
        #print sum, n, numbers
print sum
