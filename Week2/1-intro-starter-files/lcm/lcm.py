# Uses python3
import sys

def gcdEuclid(a, b):
    if b == 0:
    	return a
    else:
    	return gcdEuclid(b, a % b)

def lcm(a, b):
    return (a*b)//gcdEuclid(a, b)


if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

