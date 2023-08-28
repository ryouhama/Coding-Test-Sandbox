"""
Title:
    Approximate Equalization 2
URL:
    https://atcoder.jp/contests/abc313/tasks/abc313_c
Memo:

Run:
    >>> rye run python atcoder/313/C/execute.py < atcoder/313/C/input.txt
"""
N = int(input())
A = list(map(int, input().split()))

A.sort()
sum = sum(A)
B = [sum // N for _ in range(N)]
for i in range(0, sum % N):
    B[N - 1 - i] += 1
ans = 0
for i in range(0, N):
    ans += abs(A[i] - B[i])
print(ans // 2)
