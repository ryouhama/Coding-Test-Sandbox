N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    f, s = map(int, input().split())
    G[f-1].append(s)
for i in range(N):
    G[i].sort(reverse=True)

# どっちも同じ味の時
ans = 0
for i in range(N):
    if len(G[i]) >= 2:
        ans = max(ans, (G[i][0] + G[i][1] // 2))

# 異なる味の時
top = []
for i in range(N):
    if len(G[i]) >= 1:
        top.append(G[i][0])
top.sort(reverse=True)
ans = max(ans, sum(top[:2]))

print(ans)
