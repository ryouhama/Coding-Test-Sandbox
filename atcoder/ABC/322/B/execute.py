"""
Title:

URL:

Memo:

Run:
    >>> rye run python atcoder/ABC/322/B/execute.py < atcoder/ABC/322/B/input.txt
"""
N, M = map(int, input().split())
S = input()
T = input()

result = S == T[0:N]
result_desc = S == T[M - N :]

if result and result_desc:
    print(0)
elif result and result_desc is False:
    print(1)
elif result is False and result_desc:
    print(2)
else:
    print(3)
