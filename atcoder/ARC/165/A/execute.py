"""
Title:
    A - Sum equals LCM
URL:
    https://atcoder.jp/contests/arc165/tasks/arc165_a
Memo:

Run:
    >>> rye run python atcoder/ARC/165/A/execute.py < atcoder/ARC/165/A/input.txt
"""
import math

T = int(input())
cases = [int(input()) for _ in range(T)]


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


for n in cases:
    arr = prime_factors(n)
    x = arr[0]
    for i in arr[1:]:
        x = math.gcd(x, i)

    if x == 1:
        print("Yes")
    else:
        print("No")
