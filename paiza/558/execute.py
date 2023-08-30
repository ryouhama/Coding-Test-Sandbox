"""
Title:
    A066:連勤記録
URL:
    https://paiza.jp/challenges/558/show
Memo:

Run:
    >>> rye run python paiza/558/execute.py < paiza/558/input.txt
"""
N = int(input())
T = []
for i in range(N):
    A, B = map(int, input().split())
    T.append((A, B))

c = ['o' for _ in range(max(map(lambda it:it[1], T)))]

for task in T:
    s = task[0]
    g = task[1]
    c[s - 1:g] = ['x' for _ in range(g - s + 1)]

m = 0
cc = 0
for i in c:
    if i == 'x':
        cc += 1
        m = max(m, cc)
    else:
        cc = 0

print(m)
