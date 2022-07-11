# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
maxIndex1 = 0

for i in range(0, n):
	if ((maxIndex1 == 0) or (a[i] > a[maxIndex1])):
		maxIndex1 = i

maxIndex2 = 0

for j in range(0, n):
	if ((j != maxIndex1) and ((maxIndex2 == 0) or (a[j] > a[maxIndex2]))):
		maxIndex2 = j


result = a[maxIndex1]*a[maxIndex2]

print(result)
