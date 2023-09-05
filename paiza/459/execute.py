"""
Title:
    A051:板たおし
URL:
    https://paiza.jp/challenges/459/show
Memo:

Run:
    >>> rye run python paiza/459/execute.py < paiza/459/input.txt
"""
H, W = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]
result = [[0 for _ in range(W)] for _ in range(H)]
result[0] = S[0]

for i in range(1, H):
    for index, it in enumerate(S[i]):
        top = max(
            result[i-1][index-1] if index-1 >= 0 else 0,
            result[i-1][index],
            result[i-1][index+1]  if index+1 <= (W-1) else 0
        )
        result[i][index] = it + top

print(max(result[-1]))
