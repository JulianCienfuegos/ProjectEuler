"""Solution to Project Euler problem 22.
Begin by sorting subsets of the 46K file and writing to file.
Then sort the files together. 
This is merge sort but with files instead of simply values.
When the list is all sorted, compute the values for each name, multiply by the proper position, and then print the score.

THIS PROBLEM WOULD HAVE BEEN MORE INTERESTING IF THERE HAD BEEN 46GB of names, then we would have had
to have been clever. As it is, I use just the basic Python routines and get an instant solution.
Pushing this to github.
"""

f = open('names.txt', 'r')
names = f.readlines()
names = names[0].split(',')
names.sort()
f.close()

# Dictionary for letter values.
letters = [str(unichr(i)) for i in range(65, 91)]
values = range(1, 27)
let_val = dict(zip(letters, values))

def nameScore(name):
	nameList = list(name)[1:-1]
	score = 0
	for i in range(len(nameList)):
		score += let_val[nameList[i]]
	return score
	
sum = 0
for i in range(len(names)):
	sum += (i+1) * nameScore(names[i])
print sum

