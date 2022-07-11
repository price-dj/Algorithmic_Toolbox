# Uses python3
import sys

a = [10,2,3,22,33,7,4,1,2]
#a = [2, 3, 9, 2, 9]

n = len(a)

def get_number_of_inversions(a, b, left, right):
	number_of_inversions = 0
	if right - left <= 1:
		return number_of_inversions
	ave = (left + right) // 2
	number_of_inversions += get_number_of_inversions(a, b, left, ave)
	number_of_inversions += get_number_of_inversions(a, b, ave, right)
    
	i = 0
	j = 0
    
	while ( i < len(a[left:ave+1]) and j < len(a[ave:right+1])):
		if a[left + i] <= a[ave + j]:
			b[left + i] = a[left + i]
			i += 1
		else:
			b[left + i] = a[ave + j]
			j += 1
			number_of_inversions += (len(a[left:ave+1])-i)
	
	#while left + i < ave:
		#b[left + i + j] = a[left + i]
		#i += 1

	#while ave + j < right:
		#b[left + i + j] = a[ave + j]
		#j += 1
		
	for l in range(i, ave):
		b[l] = a[l]
		
	for m in range(j, right):
		b[m] = a[m]

	for k in range(left, right):
		a[k] = b[k]
	
	print(a)
    
	return number_of_inversions

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
