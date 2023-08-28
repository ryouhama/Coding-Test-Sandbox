N = int(input())
dist = {}
total = 0
for i in range(N):
    X, Y, Z = map(int, input().split())
    dist.append((X, Y, Z))
    total += Z

musut_get = Z // 2 + 1
