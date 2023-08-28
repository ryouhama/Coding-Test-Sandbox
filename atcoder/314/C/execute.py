"""
Title:
    Rotate Colored Subsequence
URL:
    https://atcoder.jp/contests/abc314/tasks/abc314_c
Memo:
    文字列をそのまま操作するのは難しいので、文字列と色を分けて管理する
    文字列のインデックスを操作し、最終的に文字を出力する
Run:
    >>> rye run python atcoder/314/C/execute.py < atcoder/314/C/input.txt
"""
N, M = map(int, input().split())
S = list(input())
C = list(map(int, input().split()))

# 色とその文字のインデックスを配列
color_group = [[] for _ in range(M)]
for i, c in enumerate(C):
    color_group[c - 1].append(i)
# color_group >> [[0, 3, 6], [1, 4, 5, 7], [2]]

T = S.copy()
for color in color_group:
    # 対応している色が存在しない場合、そのまま
    if len(color) <= 1:
        continue
    for i in range(len(color)):
        prev_idx = color[i]
        next = color[(i + 1) % len(color)]
        prev = S[prev_idx]
        T[next] = prev
        print(prev_idx, next, prev, T[next], T)

print(*T, sep='')
