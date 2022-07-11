# Uses python3
import sys

def fibmodm(n,m):
	result = []
	result.append(0 % m)
	result.append(1 % m)
	for i in range(2, n+1):
		result.append((result[i-1] + result[i-2]) % m)
	return result[n]
	
def get_fibonaccihuge(n, m):
	
	#find Pisano period length
	
	
	if n == 2:
		pisanoPeriodLength = 3
	else:
		pisanoPeriodLength = 2
		a = 0
		b = 1
		for i in range(2, (m**2) + 1):
			a = (b + a) % m
			b = (a + b) % m
			 
			pisanoPeriodLength += 2
				
			if a == 0 and b == 1:
				pisanoPeriodLength -= 2
				break
	
	d = n % pisanoPeriodLength
	
	return fibmodm(d,m)
	

input = input();
n, m = map(int, input.split())
print(get_fibonaccihuge(n, m))
