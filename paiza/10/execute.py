"""
Title:
    S002:最短距離を測る
URL:
    https://paiza.jp/challenges/10/show
Memo:

Run:
    >>> rye run python paiza/10/execute.py < paiza/10/input.txt
"""
from collections import deque

m, n = map(int, input().split())
s = ()
g = ()
table = []
for i in range(n):
    row = input().split()
    for j, it in enumerate(row):
        if it == 's':
            s = (j, i)
        elif it == 'g':
            g = (j, i)
    table.append(row)

def next(x, y):
    up = (x+1, y, table[y][x+1]) if 0 <= x+1 <= m-1 else (None, None, None)
    down = (x+1, y, table[y][x-1]) if 0 <= x-1 <= m-1 else (None, None, None)
    right = (x+1, y, table[y+1][x]) if 0 <= y+1 <= n-1 else (None, None, None)
    left = (x+1, y, table[y-1][x]) if 0 <= y-1 <= n-1 else (None, None, None)
    return [up, down, right, left]

d = deque([g])
depth = 0
while len(d) >= 1:
    x, y = d[-1]

    next_column = next(x, y)
    for next_x, next_y, v in next_column:
        if v == '0' and (next_x, next_y) not in d:
            d.append((next_x, next_y))
        elif v == 's':
            d.append((next_x, next_y))
            break
        else:
            
            continue

print(d)
