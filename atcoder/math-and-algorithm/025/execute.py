"""
Title:
    025 - Jiro's Vacation
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_y
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/025/execute.py < atcoder/math-and-algorithm/025/input.txt
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ev = 0

for i in range(N):
	ev += (A[i] * 1/3 + B[i] * 2/3)

print(ev)
