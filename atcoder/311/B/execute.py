"""
Title:
    Vacation Together
URL:
    https://atcoder.jp/contests/abc311/tasks/abc311_b
Memo:
    それぞれの人の予定から、各日付あたりの予定のデータを作成する
    その予定が全て`o`の場合は、全員が空いている状態になるため、連続している日数をカウントする
    最大値を求め、結果を出力する
    イメージ
    ```
    [[xooox], [oooxx], [oooxo]]
    -> `ooo`の箇所が全員の予定が空いていることになる
    [[xoo], [ooo], [ooo], [oxo], [xxo]]
    ```
Run:
    >>> rye run python atcoder/311/B/execute.py < atcoder/311/B/input.txt
"""
N, D = map(int, input().split())
S = [input() for _ in range(N)]
T = [[] for _ in range(D)]

for it in S:
    for index, d in enumerate(it):
        T[index].append(d)

all_ok = ["o" for _ in range(N)]

prev = False
count = []
for index, it in enumerate(T, start=1):
    if it == all_ok and not prev:
        count.append(1)
        prev = True
    elif it == all_ok and prev:
        count[len(count) - 1] += 1
    else:
        prev = False

print(max(count) if len(count) >= 1 else 0)
