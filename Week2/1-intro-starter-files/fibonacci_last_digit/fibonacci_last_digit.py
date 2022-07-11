# Uses python3
import sys

def get_fibonacci_last_digit(n):
	result = []
	result.append(0 % 10)
	result.append(1 % 10)
	for i in range(2, n+1):
		result.append((result[i-1] + result[i-2]) % 10)
	
	
	return result[n]

#if __name__ == '__main__':
#input = sys.stdin.read()
n = int(input())
print(get_fibonacci_last_digit(n))
