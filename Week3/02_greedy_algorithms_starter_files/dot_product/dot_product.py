#Uses python3

import sys

#a = [1, 3, -5]
#b = [-2, 4, 1]

def min_dot_product(a, b):
    a.sort(key = lambda x: x, reverse=True)
    b.sort(key = lambda x: x)
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
