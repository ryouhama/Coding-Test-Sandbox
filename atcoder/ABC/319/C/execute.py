"""
Title:
    C - False Hope
URL:
    https://atcoder.jp/contests/abc319/tasks/abc319_c
Memo:
    わからんかった
Run:
    >>> rye run python atcoder/ABC/319/C/execute.py < atcoder/ABC/319/C/input.txt
"""
from itertools import permutations

C = [list(map(int, input().split())) for _ in range(3)]


def check(a, b, c):
    count = 0
    for i, j, k in permutations([a, b, c]):
        if i == j and i != k:
            count += 1
        elif i == k and i != j:
            count += 1
        elif j == k and i != j:
            count += 1
    return count


result = 0
result += check(C[0][0], C[0][1], C[0][2])
result += check(C[1][0], C[1][1], C[1][2])
result += check(C[2][0], C[2][1], C[2][2])
result += check(C[0][0], C[1][0], C[2][0])
result += check(C[0][1], C[1][1], C[2][1])
result += check(C[0][2], C[1][2], C[2][2])
result += check(C[0][0], C[1][1], C[2][2])
result += check(C[0][2], C[1][1], C[2][0])

print(result / 9)
