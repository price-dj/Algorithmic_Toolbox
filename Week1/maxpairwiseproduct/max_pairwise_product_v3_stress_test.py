# Uses python3
import random

def maxPairwiseProdFast(a):
	result1 = 0
	maxIndex1 = 0

	for i in range(0, n):
		if ((maxIndex1 == 0) or (a[i] > a[maxIndex1])):
			maxIndex1 = i

	maxIndex2 = 0

	for j in range(0, n):
		if ((j != maxIndex1) and ((maxIndex2 == 0) or (a[j] > a[maxIndex2]))):
			maxIndex2 = j

	result1 = a[maxIndex1]*a[maxIndex2]
	
	return result1

def maxPairwiseProdSlow(a):

	result2 = 0

	for i in range(0, n):
		for j in range(i+1, n):
		    if a[i]*a[j] > result2:
		        result2 = a[i]*a[j]

	return result2


#stress test
while(True):

	random.seed(0)
	n = random.randint(2,11)
	
	print(n)
	
	a = []

	for i in range(n):
		a.append(random.randint(0,9999))

	assert(len(a) == n)

	result1 = maxPairwiseProdFast(a)
	result2 = maxPairwiseProdSlow(a)
	
	print(a)
	if result1 == result2:
		print("OK")
	else:
		print("Wrong answer: Result1:" + str(result1) + " Result2: " + str(result2))
		break




