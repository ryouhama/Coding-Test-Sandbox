"""
Title:
    012 - Primality Test
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_l
Memo:

Run:
    >>> rye run python atcoder/math-and-algorithm/012/execute.py < atcoder/math-and-algorithm/012/input.txt
"""
N = int(input())

def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or N % 3 == 0:
        return False

    i = 5
    while i * i < N:
        if N % i == 0 or N % (i + 2) == 0:
            return False
        i += 6
    return True

print("Yes" if is_prime(N) else "No")
