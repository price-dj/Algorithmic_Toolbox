# Uses python3
import sys, random

def gcdEuclid(a, b):
    if b == 0:
    	return a
    else:
    	return gcdEuclid(b, a % b)
    	
def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
    
#stress test
while(True):

	a = random.randint(0,1000000)
	b = random.randint(0,1000000)

	result1 = gcdEuclid(a, b)
	result2 = gcd(a, b)
	
	print(a, b)
	if result1 == result2:
		print("OK")
	else:
		print("Wrong answer: Result1:" + str(result1) + " Result2: " + str(result2))
		break


#input = input()
#a, b = map(int, input.split())
#print(gcdEuclid(a, b))
