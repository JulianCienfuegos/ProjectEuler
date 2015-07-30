def prime_factorization(n):
	# count the number of divisors of a number n.
	# we can count the prime divisors, and then use the formula (n_1 + 1)*...*(n_N + 1) to get the total number of factors.
	d = {}
	i = 2
	while i < (n + 1):
		if n%i==0:
			repeat = 1
			while repeat == 1:
				try:
					d[i] += 1
				except:
					d[i] = 1
				n = n/i
				if n == 1:
					return d
				if n%i != 0:
					repeat = 0
		i+=1
	return d

def count_divisors(d):
	# Accept the dictionary 
	divs = 1
	for k in d:
		divs *= (d[k] + 1)
	return divs
		

triangle = 0
i = 1
divs = 0
while divs < 501:
	triangle += i
	divs = count_divisors(prime_factorization(triangle))
	i += 1
print divs, triangle