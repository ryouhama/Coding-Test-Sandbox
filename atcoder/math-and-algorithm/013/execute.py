"""
Title:
    013 - Divisor Enumeration
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_m
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/013/execute.py < atcoder/math-and-algorithm/013/input.txt
"""
import math

N = int(input())

result = []
for i in range(1, int(math.sqrt(N)) + 1):
	if N % i == 0:
		result.append(i)
		if i != N // i:
			result.append(N // i)
	
for it in result:
	print(it)
