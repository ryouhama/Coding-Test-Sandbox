"""
Title:
    011 - Print Prime Numbers
URL:
    https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_k
Memo:
    素数判定と計算量を工夫をどうするか問題
    素数判定:
        2 or 3の場合は素数
        ある数字Nに対して、i^2がN以下の範囲で計算する。
        例)
            N = 90
            1 ~ 10まで計算し、その中に良い(9^2 < 90 < 10^2)
    計算量:
        6k+1の間隔で計算することで、計算量を少なくする
Run:
    >>> rye run python atcoder/math-and-algorithm/011/execute.py < atcoder/math-and-algorithm/011/input.txt
"""
N = int(input())

def is_prime(n):
    if n == 2 or n ==3:
       return True
    elif n % 2 == 0 or n % 3 ==0:
       return False
    i = 5
    while i * i <= n:
       if n % i == 0 or n % (i+2) == 0:
          return False
       i += 6
    return True

prime_list = []
for i in range(2, N+1):
    if is_prime(i):
       prime_list.append(i)

print(" ".join(map(str, prime_list)))
