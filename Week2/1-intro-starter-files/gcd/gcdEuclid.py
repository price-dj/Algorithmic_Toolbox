# Uses python3
import sys

def gcdEuclid(a, b):
    if b == 0:
    	return a
    else:
    	return gcdEuclid(b, a % b)


input = input()
a, b = map(int, input.split())
print(gcdEuclid(a, b))
