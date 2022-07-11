# Uses python3
import sys, random

#starts = [-10]
#ends = [10]
#points = [-100, 100, 0]



def binary_search_mod(a, b, x):
	low = 0
	high = len(a) - 1
    
	count = 0
    
	while True:
		if high < low:
			return -1
		mid = (low + high)//2
    	
		if a[mid] <= x <= b[mid]:
			count +=1
    		#search either side of mid
    		
			#search left
			i = mid
			
			if i > 0:
				i -= 1
				while i >= 0 and (a[i] <= x <= b[i]):
					i -= 1
					count += 1
    		
    		#search right
			j = mid
			
			if j < len(a)-1:
				j +=1
				while j <= len(a)-1 and (a[j] <= x <= b[j]):
					j += 1
					count += 1
    		
			return count
    		 
		elif (a[mid] and b[mid]) < x:
			high = mid - 1
		elif (a[mid] and b[mid]) > x:
			low = mid + 1
		else:
			return -1

		


def fast_count_segments(starts, ends, points):
    cnt = []
    
    starts, ends = (list(x) for x in zip(*sorted(zip(starts, ends), key=lambda pair: pair[0])))
    
    for p in points:
    	count = binary_search_mod(starts, ends, p)
    	if  count != -1:
    		cnt.append(count)
    	else:
    		cnt.append(0)
    
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

#if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #m = data[1]
    #starts = data[2:2 * n + 2:2]
    #ends   = data[3:2 * n + 2:2]
    #points = data[2 * n + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    #cnt = fast_count_segments(starts, ends, points)
    #for x in cnt:
        #print(x, end=' ')
        
        
        
#stress test
while(True):

	starts = []
	ends = []
	
	a = random.randint(-1000,1000)
	b = random.randint(1,1000)
	
	for i in range(0,random.randint(1,100)):
		starts.append(a)
		ends.append(a + b)
	
	
	points = []
	
	for j in range(0,random.randint(1,100)):
		points.append(random.randint(-1000,1000))
	
	
	result1 = naive_count_segments(starts, ends, points)
	
	result2 = fast_count_segments(starts, ends, points)
	
	
	print(points)
	if result1 == result2:
		print("OK")
	else:
		print("Wrong answer: Result1: " + str(result1) + " Result2: " + str(result2))
		break
