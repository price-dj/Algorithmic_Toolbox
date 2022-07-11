# Uses python3
import sys

#a = [1, 2, 3, 4, 4, 4]



def get_majority_element(a):
    
	dict1 = {}
	for i in range(len(a)):
		dict1[a[i]] = a.count(a[i])
		
	if (max(dict1.values()) > len(a)/2):
		return 1
	else:
		return -1
    

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
