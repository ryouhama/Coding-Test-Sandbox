"""
B - Good Distance
https://atcoder.jp/contests/abc133/tasks/abc133_b
"""
N, D = map(int, input().split())
Z = list([list(map(int, input().split())) for _ in range(N)])
print(N, D, Z)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        length = 0
        for it in range(D):
            length += ((Z[j][it] - Z[i][it])**2)
        if (length**(1/2)) % 1 == 0:
            ans += 1
print(ans)
