"""
Title:
    023 - Dice Expectation
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_w
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/023/execute.py < atcoder/math-and-algorithm/023/input.txt
"""
N = int(input())
B = list(map(int, input().split()))
R = list(map(int, input().split()))

ev_b = sum(B) / len(B)
ev_r = sum(R) / len(R)

print(ev_b + ev_r)
