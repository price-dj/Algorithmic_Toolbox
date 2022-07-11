# Uses python3
import sys

n = 5

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def DPmin_operations(n):
	
	numbers = []
	minNumOperations = [0]*(n+1)
	numOps = 0
	numbers.append(1)
	
	for k in range(1,n+1):
		minNumOperations[k] = 10000
		if k % 3 == 0:
			numOps = minNumOperations[k//3] + 1
			if numOps < minNumOperations[k]:
				minNumOperations[k] = numOps
				numbers.append(k)
		if k % 2 == 0:
			numOps = minNumOperations[k//2] + 1
			if numOps < minNumOperations[k]:
				minNumOperations[k] = numOps
				numbers.append(k)
		if k >= 1:
			numOps = minNumOperations[k - 1] + 1
			if numOps < minNumOperations[k]:
				minNumOperations[k] = numOps
				numbers.append(k)
	
	return (minNumOperations, numbers)

#input = sys.stdin.read()
#n = int(input)
#print(len(sequence) - 1)
#for x in sequence:
    #print(x, end=' ')
print(DPmin_operations(n))
