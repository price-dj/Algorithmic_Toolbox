# Uses python3
import sys
W = 10
w = [1, 4, 8]
def optimal_weight(W, w):
    
	n = len(w)
    
	valueTot = [[0 for x in range(W)] for y in range(n+1)] 
    
	#print(valueTot)
    
	v = w[:]
	
	for i in range(1, n+1):
		for j in range(1, W+1):
			valueTot[j][i] = valueTot[j][i-1]
			if w[i-1] <= j:
				val = valueTot[j-w[i-1]][i-1] + v[i-1]
				if valueTot[j][i] < val:
					valueTot[j][i] = val
	return valueTot[W+1][n+1]
    
	
    
    
    #result = 0
    #for x in w:
    #    if result + x <= W:
    #        result = result + x
    #return result

#if __name__ == '__main__':
    #input = sys.stdin.read()
    #W, n, *w = list(map(int, input.split()))
print(optimal_weight(W, w))
