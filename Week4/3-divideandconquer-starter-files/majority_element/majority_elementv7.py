# Uses python3
import sys

#a = [2, 124554847, 2, 941795895, 2, 2, 2, 2, 792755190, 756617003]
#a = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]

#n=len(a)

#left = 0

#right = n


def get_majority_element(a, left, right):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
		
	
	mid = (left + right - 1)//2
	leftMaj = get_majority_element(a, left, mid + 1)
	rightMaj = get_majority_element(a, mid + 1, right)
	
	leftCount = 0
	
	for i in range(left, right):
		if a[i] == leftMaj:
			leftCount += 1
	if leftCount > (right-left)//2:
		return leftMaj
		
	rightCount = 0
	
	for j in range(left, right):
		if a[j] == rightMaj:
			rightCount += 1
	if rightCount > (right-left)//2:
		return rightMaj
	
	return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
