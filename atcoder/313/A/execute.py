"""
Title:
	To Be Saikyo
URL:
	https://atcoder.jp/contests/abc313/tasks/abc313_a
Memo:

Run:
	>>> rye run python atcoder/313/A/execute.py < atcoder/313/A/input.txt
"""
N = int(input())
if N == 1:
    print(0)
    exit()
p1, *p = map(int, input().split())
ans = max(max(p) + 1 - p1, 0)
print(ans)
