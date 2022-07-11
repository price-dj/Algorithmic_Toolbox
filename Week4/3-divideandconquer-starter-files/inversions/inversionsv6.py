# Uses python3
import sys

#a = [10,2,3,22,33,7,4,1,2]
a = [2, 3, 9, 2, 9]

#n = len(a)

def get_number_of_inversions(a, left, right, b = []):
	number_of_inversions = 0
	if right - left <= 1:
		return number_of_inversions
	ave = (left + right) // 2
	number_of_inversions += get_number_of_inversions(a, left, ave, b)
	number_of_inversions += get_number_of_inversions(a, ave, right, b)
    
	i = 0
	j = 0
    
	b = []
	
	while ((left + i < ave) and (ave + j < right)):
		if a[left + i] <= a[ave + j]:
			b.append(a[left + i])
			i += 1
		else:
			b.append(a[ave + j])
			j += 1
			number_of_inversions += (len(a[left:ave+1])-i)
	
	b += a[i:ave]
	b += a[ave+j:]
	
	#print(b)
	
	for k in range(left, right):
		a[k] = b[k]
	
	print(a)
    
	return number_of_inversions

if __name__ == '__main__':
	#input = sys.stdin.read()
	#n, *a = list(map(int, input.split()))
	#b = []
	print(get_number_of_inversions(a, 0, len(a), b = []))
	
    
