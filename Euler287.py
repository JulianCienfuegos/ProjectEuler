from fractions import Fraction
from math import log
 
calc_k = lambda x: x * (x - 1)
 
cant_perf = 1
cant_tot = 1
limit = Fraction(1, 12345)
 
if __name__ == '__main__':
    t = 3
#    while Fraction(cant_perf, cant_tot) >= limit:
    while Fraction(cant_perf, cant_tot) >= limit:
        log_2 = int(log(t,2)) # The base 2 logarithm of t.
        if 2 ** log_2 == t: # If t is a power of 2
            cant_perf += 1 # Increment the perfect one
        cant_tot += 1 # Increment the total number of partitions.
        t += 1
    t -= 1
    print("The result is:", calc_k(t))
