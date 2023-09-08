"""
Title:
    A073:パスワード解読
URL:
    https://paiza.jp/challenges/637/show
Memo:

Run:
    >>> rye run python paiza/637/execute.py < paiza/637/input.txt
"""
D = 1000000007
N = int(input())
A = [[] for _ in range(N)]
for index, it in enumerate(input().split()):
    if int(it) != 0:
	    A[int(it)-1].append(index)

print(A)
