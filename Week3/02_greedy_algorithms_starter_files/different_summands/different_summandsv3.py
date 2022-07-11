# Uses python3
import sys
#n = 140

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
    	while k >= 0:
    		#print(k)
    		#if any(i in optimal_summands(k) for i in summands):
    		if k <= l + sum(summands):
    			summands.append(k)
    			break
    		else:
    			summands.append(l)
    			k -= l
    			l += 1	
    	return summands
    
    #write your code here
    #return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
