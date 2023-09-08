"""
Title:
    A023:週休2日制
URL:
    https://paiza.jp/challenges/202/show
Memo:

Run:
    >>> rye run python paiza/202/execute.py < paiza/202/input.txt
"""
N = int(input())
D = list(map(int, input().split()))

count = [0]
for i in range(N-6):
	if len(list(filter(lambda it:it == 0, D[i:i+7]))) >=2:
		if i == N-7:
			count[-1] += 7
		else:
			count[-1] += 1
	else:
		count.append(0)

print(max(count))
