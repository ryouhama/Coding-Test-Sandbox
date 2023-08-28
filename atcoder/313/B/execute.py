"""
Title:
	Who is Saikyo?
URL:
	https://atcoder.jp/contests/abc313/tasks/abc313_b
Memo:

Run:
	>>> rye run python atcoder/313/B/execute.py < atcoder/313/B/input.txt
"""
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(lambda x: int(x) - 1, input().split())
    G[B].append(A)

winner = []
for i in range(N):
    if len(G[i]) == 0:
        winner.append(i)

if len(winner) == 1:
    print(winner[0] + 1)
else:
    print(-1)
