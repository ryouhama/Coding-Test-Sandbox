"""
Title:

URL:

Memo:

Run:
    >>> rye run python paiza/560/execute.py < paiza/560/input.txt
"""
N, M = map(int, input().split())
A = [int(input()) for i in range(N - 1)]
A.sort()
total = 0
for i in A:
    if i <= M:
        total += i
    else:
        break

print(total)
