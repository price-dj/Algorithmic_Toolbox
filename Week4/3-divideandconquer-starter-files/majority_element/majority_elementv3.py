# Uses python3
import sys

a = [1, 2, 3, 4, 4, 4, 4]

n=len(a)

left = 0

right = n


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    else:
    	mid = (left + right)//2
    	get_majority_element(a, mid + 1, right) and get_majority_element(a, left, mid - 1)
    return -1

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
