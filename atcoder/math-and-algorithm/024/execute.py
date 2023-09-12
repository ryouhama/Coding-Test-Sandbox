"""
Title:
    024 - Answer Exam Randomly
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_x
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/024/execute.py < atcoder/math-and-algorithm/024/input.txt
"""
N = int(input())
P_Q = [map(int, input().split()) for _ in range(N)]

ev = 0

for p, q in P_Q:
	ev += q / p

print(ev)