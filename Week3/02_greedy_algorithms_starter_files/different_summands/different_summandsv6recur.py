# Uses python3
import sys
n = 140

def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    result = []
    
    if isinstance(aList, list):
        if len(aList) == 0:
            return result
        return flatten(aList[0]) + flatten(aList[1:])
    else:
        return [aList]

def optimal_summands(n, l=1, summands = []):
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
    
	if n <= 2*l:
		summands.append(n)
		
	else:
		summands.append(l)
		optimal_summands(n-l,l+1, summands)
		
	return summands
		    
if __name__ == '__main__':
    #input = sys.stdin.read()
   # n = int(input)
    summands = optimal_summands(n,l=1, summands = [])
    print(len(summands))
    for x in summands:
        print(x, end=' ')
