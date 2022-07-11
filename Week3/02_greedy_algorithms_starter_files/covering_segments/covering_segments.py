# Uses python3
import sys
from collections import namedtuple
#segments = [(4,7), (1,3), (2,5), (5,6)]
Segment = namedtuple('Segment', 'start end')



def optimal_points(segments):
    points = []
    
    while segments != []:
    	(a,b) = min(segments, key = lambda x: x[1])
    	points.append(b)
    	
    	segmentsCopy = segments[:]
    	
    	for s in segmentsCopy:
    		if (s[0] <= b <= s[1]):
    			segments.remove(s)
    
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
