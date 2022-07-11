# Uses python3
import sys
n = 1000000000
sys.setrecursionlimit(1500)

def optimalSummands(n, l=1, summands = []):
	'''
	The goal of this problem is to represent
	a given positive integer n as a sum of as many pairwise
	distinct positive integers as possible.
	In the first line, output the maximum number k such that n can be represented as a sum
	of k pairwise distinct positive integers. 
	In the second line, output k pairwise distinct positive integers
	that sum up to n (if there are many such representations, output any of them).
	Initially we have k = n and l = 1. 
	To solve a (k, l)-subproblem, we do the following. 
	If k ≤ 2l, we output just one summand k. 
	Otherwise we output l and then solve the subproblem (k − l, l + 1)
	'''
	#summands = []
	k = n
	
	if k <= 2*l:
		summands.append(k)
		
	else:
		summands.append(l)
		optimalSummands(k-l,l+1, summands)
		
	return summands
	    
if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    summands = optimalSummands(n,l=1, summands = [])
    print(summands)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
