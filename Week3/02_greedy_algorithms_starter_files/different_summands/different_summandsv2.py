# Uses python3
import sys
n = 140

def optimal_summands(n):
    summands = []
    
    k = n
    l = 1
    
    if k <= 2*l:
    	summands.append(k)
    	return summands
    else:
    	summands.append(l)
    	k -= l
    	l += 1
    	return optimal_summands(k)
    
    #write your code here
    #return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
