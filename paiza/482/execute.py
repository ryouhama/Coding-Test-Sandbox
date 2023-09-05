"""
Title:
    A055:脱出ゲーム
URL:
    https://paiza.jp/challenges/482/show
Memo:

Run:
    >>> rye run python paiza/482/execute.py < paiza/482/input.txt
"""
from collections import deque

H, W = map(int, input().split())
M = []
start = ()
for i in range(H):
    c = []
    for j, it in enumerate(input()):
        c.append(it)
        if it == "S":
            start = (j, i)
    M.append(c)

stack = deque([start])
already_explored = []

while len(stack) >= 1:
    x, y = stack.pop()
    if x == (0 or H-1) or y == (0 or W-1):
        print("YES")
        exit()

    M[y][x] = "X"

    if M[y-1][x] == ".":
        stack.append((x, y-1))
    elif M[y+1][x] == ".":
        stack.append((x, y+1))
    elif M[y][x-1] == ".":
        stack.append((x-1, y))
    elif M[y][x+1] == ".":
        stack.append((x+1, y))

print("NO")
