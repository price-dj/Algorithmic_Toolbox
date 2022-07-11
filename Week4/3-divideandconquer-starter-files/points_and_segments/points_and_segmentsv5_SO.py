# Uses python3
import sys


def count_segments(starts, ends, points):
    a = sorted([(s, 1) for s in starts] + [(e, -1) for e in ends] + [(p, 0, i) for i, p in enumerate(points)])
    
    print(a)
    
    r = [0] * len(points)
    c = 0
    for x in a:
        c += x[1]
        if not x[1]:
            r[x[2]] = c
    return r

print(count_segments([-10], [10], [-100, 100, 0]))


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
    #cnt = count_segments(starts, ends, points)
    #for x in cnt:
        #print(x, end=' ')
