"""
Title:
    Invisible Hand
URL:
    https://atcoder.jp/contests/abc312/tasks/abc312_c
Memo:
    よくわからんかった。。。
    
Run:
    >>> rye run python atcoder/312/C/execute.py < atcoder/312/C/input.txt
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sorted(A + list(map(lambda x: x + 1, B)))[M - 1])
