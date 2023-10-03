"""
Title:
    D - Polyomino
URL:
    https://atcoder.jp/contests/abc322/tasks/abc322_d
Memo:
    わからん
    むずい
    回転して良いため、Polyomino(以下Pと略す)1個に対して、4通り計算し、すべての計算の総数は64(4 ** 4)通り存在する
    しかし、1個目を固定してもできるため、16通りの計算で実施できる
    この16通りを全マス当てはまる様に計算すればいける（らしい。。。） 
Run:
    >>> rye run python atcoder/ABC/322/D/execute.py < atcoder/ABC/322/D/input.txt
"""
I = [[*input()] for _ in range(12)]
P = [I[0:4], I[4:8], I[8:12]]


def routate_right(index: int):
    result = [["" for _ in range(4)] for _ in range(4)]
    for y in range(4):
        for x in range(4):
            result[x][4 - y - 1] = P[index][y][x]
    P[index] = result


# import pprint

# print("-- I")
# pprint.pprint(I)
# print("-- P[0]")
# pprint.pprint(P[0])
# print("-- P[1]")
# pprint.pprint(P[1])
# print("-- P[2]")
# pprint.pprint(P[2])

# print("-- P[0] >> 右90度回転")
# routate_right(0)
# pprint.pprint(P[0])
# routate_right(0)
# pprint.pprint(P[0])
# routate_right(0)
# pprint.pprint(P[0])
# routate_right(0)
# pprint.pprint(P[0])
