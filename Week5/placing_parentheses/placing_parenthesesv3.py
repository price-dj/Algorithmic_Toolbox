# Uses python3

dataset = '5-8'



    


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, M, m, op):
	
	Min = 100000
	Max = -100000
	
	for k in range(i, j):
		a = evalt(M[i][k], M[k+1][j], op[k])
		b = evalt(M[i][k], m[k+1][j], op[k])
		c = evalt(m[i][k], M[k+1][j], op[k])
		d = evalt(m[i][k], m[k+1][j], op[k])
		
		Min = min(Min, a, b, c, d)
		Max = max(Max, a, b, c, d)
	
	return (Min, Max)

def get_maximum_value(dataset):

	a = list(dataset)
		
	d = a[::2]
	d = list(map(int, d))
	op = a[1::2]
	n = len(d)
	
	m = [[0 for i in range(n)] for j in range(n)]
		
	M = [[0 for i in range(n)] for j in range(n)]
	
	for i in range(n):
		m[i][i] = d[i]
		M[i][i] = d[i]
		
	for s in range(1,n):
		for i in range(n-s):
			j = i + s
			(m[i][j], M[i][j]) = MinAndMax(i, j, M, m, op)
	
	print(M)
	
	return M[0][-1]
	
	


#if __name__ == "__main__":
    #print(get_maximum_value(input()))
print(get_maximum_value(dataset))
