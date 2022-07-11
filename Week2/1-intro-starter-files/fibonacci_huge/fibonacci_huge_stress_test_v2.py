# Uses python3
import sys, random

def fibmodm(n,m):
	result = []
	result.append(0 % m)
	result.append(1 % m)
	for i in range(2, n+1):
		result.append((result[i-1] + result[i-2]) % m)
	return result[n]
	
def get_fibonaccihuge(n, m):
	
	#find Pisano period length
	pisanoPeriod = []
	pisanoPeriodLength = 2
	# a = F(i+2), b = F(i), c = F(i+1)
	b = fibmodm(0,m)
	c = fibmodm(1,m)
	for i in range(2, (m**2) + 1):
		#b = fibmodm(i+1,m)
		#c = fibmodm(i+2,m)
		b = (c + b) % m
		c = (b + c) % m
		
		pisanoPeriod.append(b)
		pisanoPeriod.append(c)		

		pisanoPeriodLength += 1
				
		if [0,1] in pisanoPeriod:
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
