"""
Title:
    A021:海岸線
URL:
    https://paiza.jp/challenges/175/show
Memo:

Run:
    >>> rye run python paiza/175/execute.py < paiza/175/input.txt
"""
H, W = map(int, input().split())
S = [[it for it in input()] for _ in range(H)]
dp = [[0 for _ in range(W)] for _ in range(H)]


def check_arround(x, y, area, coastline_len):
    if dp[y][x] == 1:
        return area, coastline_len
    area += 1
    if (y - 1) >= 0:
        if S[y - 1][x] == "#":
            dp[y - 1][x] = 1
            plus_area, plus_coastline_len = check_arround(x, y - 1, area, coastline_len)
            area += plus_area
            coastline_len += plus_coastline_len
        else:
            coastline_len += 1
    if (x - 1) >= 0:
        if S[y][x - 1] == "#":
            dp[y][x - 1] = 1
            plus_area, plus_coastline_len = check_arround(x - 1, y, area, coastline_len)
            area += plus_area
            coastline_len += plus_coastline_len
        else:
            coastline_len += 1
    if (x + 1) <= (W - 1):
        if S[y][x + 1] == "#":
            dp[y][x + 1] = 1
            plus_area, plus_coastline_len = check_arround(x + 1, y, area, coastline_len)
            area += plus_area
            coastline_len += plus_coastline_len
        else:
            coastline_len += 1
    if (y + 1) <= (H - 1):
        if S[y + 1][x] == "#":
            dp[y + 1][x] = 1
            plus_area, plus_coastline_len = check_arround(x, y + 1, area, coastline_len)
            area += plus_area
            coastline_len += plus_coastline_len
        else:
            coastline_len += 1
    return area, coastline_len


result = []
for y in range(H):
    for x in range(W):
        if dp[y][x] == 1:
            continue
        elif S[y][x] == "#":
            area, coastline_len = check_arround(x, y, 0, 0)
            result.append((area, coastline_len))

result.sort(key=lambda it: it[0], reverse=True)

for it in result:
    print(f"{it[0]} {it[1]}")
