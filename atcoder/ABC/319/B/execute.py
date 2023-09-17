"""
Title:
    B - Measure
URL:
    https://atcoder.jp/contests/abc319/tasks/abc319_b
Memo:

Run:
    >>> rye run python atcoder/ABC/319/B/execute.py < atcoder/ABC/319/B/input.txt
"""
N = int(input())


def find_divisors(N):
    divisors = []
    for i in range(1, N + 1):
        if N % i == 0:
            divisors.append(i)
    return divisors


divisors = find_divisors(N)

result = []
for i in range(N + 1):
    min_value = None
    for div in divisors:
        if div >= 10:
            continue
        if i % (N / div) == 0:
            min_value = min(min_value, int(div)) if min_value else div
            break
    if not min_value:
        result.append("-")
    else:
        result.append(min_value)

print("".join(map(str, result)))
