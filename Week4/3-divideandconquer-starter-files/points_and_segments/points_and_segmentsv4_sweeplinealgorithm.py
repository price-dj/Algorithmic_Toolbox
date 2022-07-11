# Uses python3
import sys

#starts = [-100000000]
#ends = [100000000]
#points = [0]



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
    '''
    starts = list of starting points for segments, 
    ends = list of corresponding ending points for segments
    points = list of points for which we must count number of segments each point can be covered by.
    cnt = list of count for each point of segments covering each corresponding point
    '''
    
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

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
