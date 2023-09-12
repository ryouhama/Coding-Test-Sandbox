"""
Title:
    A033:読書の課題
URL:
    https://paiza.jp/challenges/315/show
Memo:
    ナップザック問題
	動的計画法
Run:
    >>> rye run python paiza/315/execute.py < paiza/315/input.txt
"""
N, M = map(int, input().split())
B_X = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (M + 1) for _ in range(N+1)]

for index, (B, X) in enumerate(B_X):
	for j in range(M+1):
		dp[index+1][j] = dp[index][j]
		if j - X >= 0:
			dp[index+1][j] = max(dp[index+1][j], dp[index][j - X] + B)

print(dp[-1][-1])
