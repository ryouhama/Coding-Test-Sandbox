"""
Title:
    S055:弱肉強食
URL:
    https://paiza.jp/challenges/619/show
Memo:

Run:
    >>> rye run python paiza/619/execute.py < paiza/619/input.txt
"""
H, W = map(int, input().split())
A = [input().split() for _ in range(H)]
N = int(input())
P = [tuple(input().split()) for _ in range(N)]

def prey(predator, x, y):
    target = A[y][x]
    if target != "-" and (predator, target) in P:
        A[y][x] = "-"

for y in range(H):
    for x in range(W):
        it = A[y][x]
        if A[y][x] == "-":
            continue

        if (x-1) >= 0 and (y-1) >= 0:
            prey(it, x-1, y-1)
        if (y-1) >= 0:
            prey(it, x, y-1)
        if (x+1) <= (W-1) and (y-1) >= 0:
            prey(it, x+1, y-1)
        if (x-1) >= 0:
            prey(it, x-1, y)
        if (x+1) <= (W-1):
            prey(it, x+1, y)
        if (x-1) >= 0 and (y+1) <= (H-1):
            prey(it, x-1, y+1)
        if (y+1) <= (H-1):
            prey(it, x, y+1)
        if (x+1) <= (W-1) and (y+1) <= (H-1):
            prey(it, x+1, y+1)

for row in A:
    print(" ".join(row))
