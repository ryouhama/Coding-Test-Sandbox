"""
Title:
    First ABC
URL:
    https://atcoder.jp/contests/abc311/tasks/abc311_a
Memo:

Run:
    >>> rye run python atcoder/311/A/execute.py < atcoder/311/A/input.txt
"""
_ = input()
S = input()

A = 0
B = 0 
C = 0
for index, i in enumerate(S, start=1):
    if i == 'A' and A == 0:
        A = 1
    elif i == "B" and B == 0:
        B =1
    elif i == "C" and C == 0:
        C = 1
    else:
        continue

    if A >= 1 and B >= 1 and C >=1:
        print(index)
