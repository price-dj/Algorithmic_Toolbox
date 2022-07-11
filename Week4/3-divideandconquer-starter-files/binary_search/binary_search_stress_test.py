# Uses python3
import sys, math, random, bisect

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
    		
def binary_search2(a,x,lo=0,hi=-1):
    i = bisect.bisect(a,x,lo,hi)
    if i == 0:
        return -1
    elif a[i-1] == x:
        return i-1
    else:
        return -1

def binary_search_rec(a, x, high, low = 0):
	
	if high < low:
		return -1
	
	mid = (low + high)//2
	
	if x == a[mid]:
		return mid
	elif x < a[mid]:
		return binary_search_rec(a, x,mid - 1, low)
	else:
		return binary_search_rec(a, x, high, mid + 1)
	    

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

#if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #m = data[n + 1]
    #a = data[1 : n + 1]
    #for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
       # print(binary_search(a, x), end = ' ')
        
        
#stress test
while(True):

	a = []
	for i in range(0,random.randint(1,1000)):
		a.append(random.randint(1,10000))
	
	x = random.randint(1,10000)
	
	a.sort()
	
	result1 = linear_search(a, x)
	#result2 = binary_search2(a,x,lo=0,hi=-1)
	result2 = binary_search(a, x)
	#result2 = binary_search_rec(a, x, high=len(a)-1, low=0)
	
	print(x)
	if result1 == result2:
		print("OK")
	else:
		print("Wrong answer: Result1: " + str(result1) + " Result2: " + str(result2))
		break
