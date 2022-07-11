# Uses python3
import sys, operator


a = [2, 3, 9, 2, 9]
n = len(a)
b = n * [0]

def get_number_of_inversions(a, b, left, right):
	'''
	a = input and output list, b = working list
	number_of_inversions are number of pairwise swaps needed to sort list 
	'''
    
	number_of_inversions = 0
	if right - left <= 1:
		return number_of_inversions
	ave = (left + right) // 2
	number_of_inversions += get_number_of_inversions(a, b, left, ave)
	number_of_inversions += get_number_of_inversions(a, b, ave, right)
    
	i = 0
	j = 0
	compare = operator.lt
    
	while (left + i < ave) and (ave + j < right):
		if compare(a[left +i], a[ave + j]):
			b[left + i + j] = a[left + i]
			i += 1
			
		else:
			b[left + i + j] = a[ave + j]
			number_of_inversions += 1 #(ave - (left + i))
			j += 1

	while left + i < ave:
		b[left + i + j] = b[left + i]
		i += 1

	while ave + j < right:
		b[left + i + j] = b[ave + j]
		j += 1

	for k in range(left, right):
		a[k] = b[k]

	return number_of_inversions

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
