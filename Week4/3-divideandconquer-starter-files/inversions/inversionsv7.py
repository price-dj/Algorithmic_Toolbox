# Uses python3
import sys, operator


#a = [10,2,3,22,33,7,4,1,2]
#n = len(a)


def mergeList(left, right):
	result = []
	i = 0
	j = 0
	numInv = 0
	
	#compare = operator.lt
	
	while (i < len(left) and j < len(right)):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
			numInv += (len(left)-i)
	
	result += left[i:]
	result += right[j:]
	return result, numInv
	


def get_number_of_inversions(a):
	'''
	a = input and output list
	number_of_inversions are number of pairwise swaps needed to sort list 
	'''
    
	number_of_inversions = 0
	if len(a) <= 1:
		return a, number_of_inversions
	ave = len(a) // 2
	left, leftInv = get_number_of_inversions(a[:ave])
	right, rightInv = get_number_of_inversions(a[ave:])
	result, number_of_inversions = mergeList(left,right)
	number_of_inversions += (leftInv + rightInv)
	
	return result, number_of_inversions


	
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    
    (result, numInv) = get_number_of_inversions(a)
    print(numInv)
    #print(result)
    
    
