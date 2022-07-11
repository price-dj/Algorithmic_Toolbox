# Uses python3
import sys, random

def fibmodm(n,m):
	result = []
	result.append(0 % m)
	result.append(1 % m)
	for i in range(2, n+1):
		result.append((result[i-1] + result[i-2]) % m)
	return result[n]


# (Private) Returns the tuple (F(n), F(n+1)).
def _fib(n,m):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2, m)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d % m, (c + d) % m)
	
def get_fibonaccihuge(n, m):
	
	#find Pisano period length
	pisanoPeriod = []
	pisanoPeriodLength = 2
	
	p0 = 0
	p1 = 1
	for i in range(2, (m**2) + 1):
		(b, c) = _fib(i, m)
		 
		pisanoPeriodLength += 1
				
		if b == 0 and c == 1:
			break
	
	d = n % pisanoPeriodLength
	
	return fibmodm(d,m)
	
#stress test
while(True):

	n = random.randint(1,10000)
	m = random.randint(2,1000)

	result1 = fibmodm(n,m)
	result2 = get_fibonaccihuge(n, m)
	
	print(n, m)
	if result1 == result2:
		print("OK")
	else:
		print("Wrong answer: Result1: " + str(result1) + " Result2: " + str(result2))
		break
	


#input = input();
#n, m = map(int, input.split())
#print(get_fibonaccihuge(n, m))
