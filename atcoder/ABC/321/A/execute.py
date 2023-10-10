"""
Title:
	A - 321-like Checker
URL:
	https://atcoder.jp/contests/abc321/tasks/abc321_a
Memo:

Run:
	>>> rye run python atcoder/ABC/321/A/execute.py < atcoder/ABC/321/A/input.txt
"""
N = input()

prev = 99999
for it in N:
    if prev <= int(it):
        print("No")
        exit()
    else:
        prev = int(it)

print("Yes")
