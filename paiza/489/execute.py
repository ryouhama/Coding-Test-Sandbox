"""
Title:
    A057:最長スワイプ
URL:
    https://paiza.jp/challenges/489/show
Memo:

Run:
    >>> rye run python paiza/489/execute.py < paiza/489/input.txt
"""
N = int(input())
S = [list(map(int, input())) for _ in range(N)]

dp = [[1 for _ in range(N)] for _ in range(N)]

def check_arround(x, y):
	value = S[y][x]
	if (x-1) >= 0 and (y-1) >= 0 and S[y-1][x-1] - value == 1:
		dp[y-1][x-1] = dp[y][x] + 1
	if (y-1) >= 0 and S[y-1][x] - value == 1:
		dp[y-1][x] = dp[y][x] + 1
	if (x+1) <= (N-1) and (y-1) >= 0 and S[y-1][x+1] - value == 1:
		dp[y-1][x+1] = dp[y][x] + 1
	if (x-1) >= 0  and S[y][x-1] - value == 1:
		dp[y][x-1] = dp[y][x] + 1
	if (x+1) <= (N-1) and S[y][x+1] - value == 1:
		dp[y][x+1] = dp[y][x] + 1
	if (x-1) >= 0 and (y+1) <= (N-1) and S[y+1][x-1] - value == 1:
		dp[y+1][x-1] = dp[y][x] + 1
	if (y+1) <= (N-1) and S[y+1][x] - value == 1:
		dp[y+1][x] = dp[y][x] + 1
	if (x+1) <= (N-1) and (y+1) <= (N-1) and S[y+1][x+1] - value == 1:
		dp[y+1][x+1] = dp[y][x] + 1

for i in range(N):
	for j in range(N):
		check_arround(x=j, y=i)


print(max(map(max, dp)))
