"""Project Euler problem 21
Sounds like another application of dynamic programming. 
Evaluate the sum of all of the amicable numbers under 10000.



Find all the divisors of m. 
Add them to get n.
Find all the divisors of n.
Add them. 
If the sum equals m, 
Add either one of both of m and n to the sum, making sure the ones you add are under 10,000.

We will grab the elements from a list going from 221 to 10000 with 284 removed.

Note that divisor sums are not unique. i.e .1 + 2 + 7 are the divisors of 14. 

update after solving: I just realized that perfect numbers (where a == b) werent to be included. This was messing me up.
"""

def GetDivisorSum(N):
	sum = 0
	for i in range(1, N//2 + 1):
		#print i
		if N%i == 0:
			sum += i
	return sum

M = 10000
sum = 284 + 220
nums = range(221, M)
amicable = {284, 220}
for m in nums:
	if m not in amicable:
		sM = GetDivisorSum(m)
		sN = GetDivisorSum(sM) # We know sM == n
		if sN == sM:
			continue
		elif sN == m:	   # Does sN == m?
			if sM < M:	   # Is sN in our range?
				sum += sM
				amicable.add(sM)
			sum += sN
			amicable.add(sN)
print sum		
