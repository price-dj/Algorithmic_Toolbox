# Uses python3
s = [1, 2, 3]
t = [3, 1, 2 ]
u = [1, 3, 5]


def lcs3(s, t, u):
    
	l = len(u)
	n = len(s)
	m = len(t)
    
    
	#D = [[0 for j in range(m+1)] for i in range(n+1)]
    
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
				
				if s[i-1] == t[j-1] == u[k-1]:
					E[i][j][k] = min(insertionij, insertionjk, deletionij, deletionjk, matchijk)
					
					common.append(s[i-1])
					
				else:
					E[i][j][k] = min(insertionij, insertionjk, deletionij, deletionjk, mismatchijk)
    
	common = list(set(common))
    
	return len(common)

#if __name__ == "__main__":
	#print(edit_distance(input(), input()))
    
print(lcs3(s, t, u))
