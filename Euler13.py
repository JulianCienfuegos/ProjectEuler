def Add(col, carry):
    if col != None and carry != None:
        return col + carry
    elif col == None:
        return carry
    else:
        return col
def TryToAccess(n, l):
    try:
        return l[n]
    except:
        return None

      
f = open('Euler13Nums.dat')
nums = f.readlines()
#nums = ['1234\n', '5678\n'] # For testing.
nums = [i.rstrip('\n') for i in nums]
nums = [[int(j) for j in list(i)] for i in nums]
nums = [i[::-1] for i in nums]
Cols = zip(*nums)
Cols = [list(i) for i in Cols]
# Now we have a 2D list  where each row corresponds to a digit, i.e. units, tens, hundreds, etc.
ColSums = [sum(i) for i in Cols]
# Now we have the sums for the digits appearing for each unit.
# keep the first digit, add the rest to the next position.
print(ColSums)
n = 0
col = ColSums[n]
carry = 0
Result = []
print('col, carry, curr, digit')
while(col != None)or(carry != 0):
    curr = Add(col, carry)
    digit = curr - 10*(curr//10)
    print(col, carry, curr, digit)
    Result.append(digit)
    n += 1
    col = TryToAccess(n, ColSums)
    carry = curr // 10
Result.reverse()
#print(str(''.join(Result)))
print(''.join([str(i)for i in Result[:10]]))
