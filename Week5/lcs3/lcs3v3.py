#Uses python3

import sys

def lcs3(a, b, c):
	l = len(a)
	n = len(b)
	m = len(c)
    
	E = [[[0 for k in range(l+1)] for j in range(m+1)] for i in range(n+1)]
	common = []
    
	for i in range(1,n+1):
		E[i][0][0] = i
    
	for j in range(1,m+1):
		E[0][j][0] = j

	for k in range(1,l+1):
		E[0][0][k] = k    
    
    
	for j in range(1,m+1):
		for i in range(1,n+1):
			for k in range(1,l+1):
				insertionij = E[i][j-1][k] + 1
				insertionjk = E[i][j][k-1] + 1
				deletionij = E[i-1][j][k] + 1
				deletionjk = E[i][j-1][k] + 1
				matchijk = E[i-1][j-1][j-1]
				mismatchijk = E[i-1][j-1][k-1] + 1
				
				if a[i-1] == b[j-1] == c[k-1]:
					E[i][j][k] = min(insertionij, insertionjk, deletionij, deletionjk, matchijk)
					
					common.append(a[i-1])
					
				else:
					E[i][j][k] = min(insertionij, insertionjk, deletionij, deletionjk, mismatchijk)
    
	common = list(set(common))
	
	value = len(common)
    
	return value


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
