# Uses python3
import sys
W = 10
w = [1, 4, 8]
def optimal_weight(W, w):
    
	n = len(w)
    
	# Create n nested arrays of 0 * (W + 1)
	valueTot = [[0] * (W + 1) for y in range(n)] 
    
	# Set valueTot[0] to w[0] if w[0] <= j
	valueTot[0] = [w[0] if w[0] <= j else 0 for j in range(W + 1)]
    
	#print(valueTot)
    
	#v = w[:]
	
	for i in range(1, n):
		for j in range(1, W+1):
			value = valueTot[i-1][j]  # previous i @ same j
			if w[i] <= j:
				val = valueTot[i-1][j-w[i]] + w[i]
				if value < val:
					value = val
					valueTot[i][j] = value
				else:
					valueTot[i][j] = value  
			else:
				valueTot[i][j] = value  
	return valueTot[-1][-1]
    
	

#if __name__ == '__main__':
    #input = sys.stdin.read()
    #W, n, *w = list(map(int, input.split()))
print(optimal_weight(W, w))
