"""
Title:

URL:
    https://paiza.jp/challenges/527/show
Memo:

Run:
    >>> rye run python paiza/527/execute.py < paiza/527/input.txt
"""
N, M = map(int, input().split())
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]

result = [0 for _ in range(N)]
now = 0
for it in B:
    leave = it
    while leave > 0:
        index = now % N
        if leave >= A[index]:
            leave -= A[index]
            now += 1
            result[index] += A[index]
        else:
            result[index] += leave
            now += 1
            break

for i in result:
    print(i)
