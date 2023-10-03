"""
Title:
    C - Festival
URL:
    https://atcoder.jp/contests/abc322/tasks/abc322_c
Memo:

Run:
    >>> rye run python atcoder/ABC/322/C/execute.py < atcoder/ABC/322/C/input.txt
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

expired_days = 0
for day in range(N):
    next = A[expired_days]
    if day + 1 < next:
        print(next - day - 1)
    elif day + 1 == next:
        print(0)
        expired_days += 1
