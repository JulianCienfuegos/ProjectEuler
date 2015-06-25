"""Find the pythagoean triplet for which a + b + c = 1000
A pythagorean triplet is a set of numbers, a<b<c, such that
a^2 + b^2 = c^2
"""

import numpy as np

nA = 167 # The biggest a, b should be is 500. 
nB = 125 # These give that bound.
A = 3*np.arange(nA)
B = 4*np.arange(nB)
A = np.delete(A, np.arange(0, A.size, 4)) # Remove multiples of 12. Exactly one of a and b will be divisible by 3, the other by 4. See wikipedia.
B = np.delete(B, np.arange(0, B.size, 3)) # ditto.
cat = np.append(A, B)
cat = np.sort(cat)
for a in range(len(cat)):
    for b in range (len(cat) - a - 1):
        p = cat[a]; q = cat[a + b  +1]
        if(p + 2*q) < 1000: # Don't bother if the value for r is going to be too big.
            r = np.sqrt(p**2  + q**2) 
            if( p + q + r)==1000:
                print p*q*r
                print p, q, r
