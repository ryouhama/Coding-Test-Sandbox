"""
Title:
    009 - Brute Force 2
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_i
Memo:
    動的計画法(Dynamic Programing: DP)を用いて考える。

Run:
    >>> rye run python atcoder/math-and-algorithm/009/execute.py < atcoder/math-and-algorithm/009/input.txt
"""
N, S = map(int, input().split())
A = [int(it) for it in input().split()]

dp_table = [[0 for _ in range(S+1)] for _ in range(N)]

for i in range(S+1):
    if i >= A[0]:
        dp_table[0][i] = A[0]

for i in range(1, N):
    # 0 ~ Sまでの範囲をそれぞれ計算する
    for j in range(S+1):
        # 前回の値を取得する
        prev = dp_table[i-1][j]
        if A[i] > j:
            dp_table[i][j] = prev
        else:
            sum_num = dp_table[i-1][j - A[i]] + A[i]
            dp_table[i][j] = max(prev, sum_num)

print("Yes") if dp_table[N-1][S] == S else print("No")
