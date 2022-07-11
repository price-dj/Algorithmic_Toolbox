# Uses python3
import sys, math

def binary_search(a, x):
    low = 0
    high = len(a) - 1
    
    while True:
    	if high < low:
    		return -1
    	mid = math.floor(float(low + high)/2.0)
    	midval = a[mid]
    	if midval < x:
    		low = mid + 1
    	elif midval > x:
    		high = mid - 1
    	else:
    		return mid

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')
