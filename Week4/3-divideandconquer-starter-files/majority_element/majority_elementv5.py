# Uses python3
import sys

a = [4, 4, 4, 2, 3, 4, 4]

n=len(a)

left = 0

right = n


def get_majority_element(a, left, right, left_maj = None, right_maj = 0):
	if left == right:
		return -1
	if left + 1 == right:
		return a[left]
		if left_maj == right_maj and a.count(left_maj) > len(a)/2:
			return left_maj
	else:
		mid = (left + right)//2
		left_maj = get_majority_element(a, left, mid - 1, left_maj, right_maj)
		right_maj = get_majority_element(a, mid + 1, right, left_maj, right_maj)
	return -1

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n, left_maj = None, right_maj = 0) != -1:
        print(1)
    else:
        print(0)
