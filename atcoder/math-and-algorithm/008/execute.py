"""
Title:
    008 - Brute Force 1
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_h
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/008/execute.py < atcoder/math-and-algorithm/008/input.txt
"""
N, S = map(int, input().split())

total = 0
for red in range(1, N+1):
    for blue in range(1, N+1):
        if red + blue <= S:
            total += 1
        else:
            break

print(total)
