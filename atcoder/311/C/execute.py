"""
Title:
    Find it!
URL:
    https://atcoder.jp/contests/abc311/tasks/abc311_c
Memo:
    よくわからんかった。。。
Run:
    >>> rye run python atcoder/311/C/execute.py < atcoder/311/C/input.txt
"""
N = int(input())
A = list(map(int, ("0 " + input()).split()))
now = 1
for _ in range(N): now = A[now]
B = [now]
while B[0] != A[now]:
	now = A[now]
	B.append(now)
print(len(B))
print(*B)
