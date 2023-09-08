"""
Title:
    014 - Factorization
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_n
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/014/execute.py < atcoder/math-and-algorithm/014/input.txt
"""
N = int(input())

def prime_factors(n):
	factors = []

	for divisor in range(2, int(n ** 0.5) + 1):
		while n % divisor == 0:
			factors.append(divisor)
			n = n // divisor
	
	if n > 1:
		factors.append(n)
	return factors

print(" ".join(map(str, prime_factors(N))))
