"""
Title:
    A052:階段登り
URL:
    https://paiza.jp/challenges/462/show
Memo:

Run:
    >>> rye run python paiza/462/execute.py < paiza/462/input.txt
"""
N = int(input())
A, B = map(int, input().split())

kaidan = ["-" for _ in range(N+1)]
kaidan[0] = "o"

for i in range(N):
	if kaidan[i] == "o":
		if i+A >= N+1:
			kaidan[-1] = "o"
		else:
			kaidan[i+A] = "o"
		if i+B >= N+1:
			kaidan[-1] = "o"
		else:
			kaidan[i+B] = "o"

print(len(list(filter(lambda it:it=="-", kaidan))))
