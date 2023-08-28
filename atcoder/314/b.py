"""
B - Roulette
https://atcoder.jp/contests/abc314/tasks/abc314_b
"""
N = int(input())
l = []
for i in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    l.append((C, A))
X = int(input())

result = []
for index, it in enumerate(l, 1):
    if X in it[1]:
        result.append((index, it[0]))
if len(result): print("0")
ans = sorted(lambda x: x[1], result)
print(" ".join(map(lambda x: x[0] , ans)))
