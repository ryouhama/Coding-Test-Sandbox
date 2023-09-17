"""
Title:
    B - Sliding Window Sort 2
URL:
    https://atcoder.jp/contests/arc165/tasks/arc165_b
Memo:

Run:
    >>> rye run python atcoder/ARC/165/B/execute.py < atcoder/ARC/165/B/input.txt
"""
N, K = map(int, input().split())
P = [*map(int, input().split())]

result = None


for i in range(N - K + 1):
    l = P[i : i + K]
    l.sort()
    r = P[0:i] + l + P[i + K :]
    # 比較
    if not result:
        result = r
    for i in range(len(r)):
        if result[i] < r[i]:
            result = r
            break

print(" ".join(map(str, result)))
