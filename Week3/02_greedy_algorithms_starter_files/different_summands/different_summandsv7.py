# Uses python3
import sys
n = 8

def optimal_summands(n, l = 1):
    summands = []
    
    k = n
    l = 1
    
    if k <= 2*l:
    	summands.append(k)
    	return summands
    else:
    	while k > 0:
    			print(k)
    		
    			summands.append(l)
    			k -= l
    			l += 1	
    return summands
    
if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    summands = optimal_summands(n, l = 1)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
