dict1 = {}

def f(n):
	if n == 1:
		return 1, -1
	if dict1.get(n) is not None:
		return dict1[n]
        
	ans = (f(n - 1)[0] + 1, n - 1)

	if n % 2 == 0:
		ret = f(n // 2)
		if ans[0] > ret[0]:
			ans = (ret[0] + 1, n // 2)

	if n % 3 == 0:
		ret = f(n // 3)
		if ans[0] > ret[0]:
			ans = (ret[0] + 1, n // 3)
	
	print(dict1)
	dict1[n] = ans
	print(ans)
	return ans

def print_solution(n):
    ans = []
    while f(n)[1] != -1:
        ans.append(n)
        n = f(n)[1]
    ans.append(1)
    ans.reverse()
    for x in ans:
        print(x),

def solve(n):
    
    for i in range(1, n):
        f(i)[0]
    print_solution(n)
    


solve(5)
