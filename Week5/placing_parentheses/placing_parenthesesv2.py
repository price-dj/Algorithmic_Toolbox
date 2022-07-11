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

def get_maximum_value(dataset):
    a = list(dataset)
    
    s = a[::2]
    s = list(map(int, s))
    op = a[1::2]
    
    n = len(s)
    
    m = [[0] * n for y in range(n)]
    
    for i in range(1, n+1):
    	m[i, i+1] = evalt(s[i], s[i+1], op[i])
    
    for u in range(2, n+1):
    	for i in range(1, n-u + 2):
    		j = i + u -1
    		m[i, j] = -100000
    		for k in range(i, j-1):
    			q = evalt(m[i, k], m[k+1, j], op[k])
    			if q > m[i, j]:
    				m[i, j] = q
    return m[-1][-1]
    
    #print(a)
    #print(s)
    #print(op)
    #return 0


#if __name__ == "__main__":
    #print(get_maximum_value(input()))
print(get_maximum_value(dataset))
