# Uses python3
import sys

starts = [0, -3, 7]
ends = [5, 2, 10]
points = [1, 6]



def binary_search(a, b, x):
    low = 0
    high = len(a) - 1
    
    while True:
    	if high < low:
    		return -1
    	mid = (low + high)//2
    	#midval = a[mid]
    	if a[mid] <= x <= b[mid]:
    		return 1
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
    	if binary_search(starts, ends, p) == 1:
    		cnt.append(1)
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
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #m = data[1]
    #starts = data[2:2 * n + 2:2]
    #ends   = data[3:2 * n + 2:2]
    #points = data[2 * n + 2:]
    #use fast_count_segments
    #cnt = naive_count_segments(starts, ends, points)
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
